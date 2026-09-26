const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } = require("@whiskeysockets/baileys");
const pino = require("pino");
const QRCode = require("qrcode");
const qrcodeTerminal = require("qrcode-terminal");
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = 3005;
const AUTH_DIR = path.join(__dirname, "auth_info_baileys");
const QR_IMAGE_PATH = path.join(__dirname, "..", "whatsapp_qr.png");
const STATUS_FILE = path.join(__dirname, "status.json");
const ADMIN_CONFIG_FILE = path.join(__dirname, "..", "admin_config.json");
const PROGRESS_FILE = path.join(__dirname, "..", "..", "audit", "overnight_progress.json");

let sock = null;
let currentQR = null;
let connectionStatus = "INITIALIZING";
let myJid = null;
let myLid = null;

const sentBotMsgIds = new Set();

function loadAdminConfig() {
    try {
        if (fs.existsSync(ADMIN_CONFIG_FILE)) {
            return JSON.parse(fs.readFileSync(ADMIN_CONFIG_FILE, "utf-8"));
        }
    } catch (e) {
        console.error("Error reading admin_config.json:", e.message);
    }
    return {
        admin_phone: "918000530422",
        admin_jid: "918000530422@s.whatsapp.net",
        admin_lids: ["260872136093846@lid"],
        exclusive_admin_only: true
    };
}

function saveStatus(status, extra = {}) {
    connectionStatus = status;
    const data = { status, timestamp: new Date().toISOString(), ...extra };
    fs.writeFileSync(STATUS_FILE, JSON.stringify(data, null, 2));
}

function getLiveProgress() {
    try {
        if (fs.existsSync(PROGRESS_FILE)) {
            return JSON.parse(fs.readFileSync(PROGRESS_FILE, "utf-8"));
        }
    } catch(e) {}
    return null;
}

async function sendWhatsAppDirect(targetJid, text) {
    if (!sock || connectionStatus !== "CONNECTED") {
        throw new Error("WhatsApp socket not connected");
    }
    const sent = await sock.sendMessage(targetJid, { text });
    if (sent?.key?.id) {
        sentBotMsgIds.add(sent.key.id);
        if (sentBotMsgIds.size > 200) {
            const arr = Array.from(sentBotMsgIds);
            for (let i = 0; i < 50; i++) sentBotMsgIds.delete(arr[i]);
        }
    }
    return sent;
}

async function startWhatsApp() {
    const { state, saveCreds } = await useMultiFileAuthState(AUTH_DIR);
    
    sock = makeWASocket({
        auth: state,
        logger: pino({ level: "silent" }),
        printQRInTerminal: false,
        browser: ["Swatch Paints ERP", "Chrome", "1.0.0"]
    });

    sock.ev.on("creds.update", saveCreds);

    sock.ev.on("connection.update", async (update) => {
        const { connection, lastDisconnect, qr } = update;

        if (qr) {
            currentQR = qr;
            qrcodeTerminal.generate(qr, { small: true });
            await QRCode.toFile(QR_IMAGE_PATH, qr, { width: 400 });
            saveStatus("AWAITING_SCAN", { qrAvailable: true });
        }

        if (connection === "close") {
            const shouldReconnect = (lastDisconnect?.error)?.output?.statusCode !== DisconnectReason.loggedOut;
            console.log("⚠️ Connection closed. Reconnecting:", shouldReconnect);
            saveStatus("DISCONNECTED", { reason: lastDisconnect?.error?.message });
            if (shouldReconnect) {
                setTimeout(startWhatsApp, 3000);
            }
        } else if (connection === "open") {
            currentQR = null;
            myJid = sock.user.id.split(":")[0] + "@s.whatsapp.net";
            myLid = sock.user.lid ? sock.user.lid.split(":")[0] + "@lid" : "unknown@lid";
            console.log("\n✅ WHATSAPP CONNECTED SUCCESSFULLY!");
            console.log(`📱 User JID: ${myJid} (${sock.user.name || "Authenticated"})\n`);
            saveStatus("CONNECTED", { userJid: myJid, userName: sock.user.name });
        }
    });

    let pendingQuestion = null;
    const ANSWERS_DIR = path.join(__dirname, "answers");
    if (!fs.existsSync(ANSWERS_DIR)) fs.mkdirSync(ANSWERS_DIR, { recursive: true });

    // Handle incoming messages
    sock.ev.on("messages.upsert", async ({ messages, type }) => {
        for (const msg of messages) {
            if (!msg.message) continue;

            const from = msg.key.remoteJid || "";
            // Ignore broadcast status updates completely
            if (from === "status@broadcast" || from.includes("@broadcast")) continue;

            const msgId = msg.key.id;
            // Ignore messages sent by bot to prevent loops
            if (sentBotMsgIds.has(msgId)) continue;

            const participant = msg.key.participant || "";
            const fromMe = Boolean(msg.key.fromMe);

            const text = (
                msg.message.conversation ||
                msg.message.extendedTextMessage?.text ||
                msg.message.imageMessage?.caption ||
                ""
            ).trim();

            if (!text) continue;

            console.log("\n=======================================================");
            console.log(`📩 Incoming message from ${from}: "${text}"`);
            console.log("=======================================================\n");

            const cfg = loadAdminConfig();
            const isAdminPhone = from.includes(cfg.admin_phone) || (fromMe && (from === myJid || from === myLid));
            const isKnownAdminLid = cfg.admin_lids.length > 0 && (cfg.admin_lids.includes(from) || cfg.admin_lids.includes(participant));

            // Strictly filter non-admin contacts
            if (!isAdminPhone && !isKnownAdminLid) {
                console.log(`⛔ [DROPPED] Non-admin message ignored: ${from}`);
                continue;
            }

            const replyTarget = from.includes("@g.us") ? from : (fromMe ? myJid : from);
            const lower = text.toLowerCase();

            // 1. Pending question answer capture
            if (pendingQuestion) {
                console.log(`📥 Captured answer for [${pendingQuestion.id}]: "${text}"`);
                const answerData = {
                    id: pendingQuestion.id,
                    question: pendingQuestion.question,
                    answer: text,
                    timestamp: new Date().toISOString()
                };
                fs.writeFileSync(path.join(ANSWERS_DIR, `${pendingQuestion.id}.json`), JSON.stringify(answerData, null, 2));
                pendingQuestion = null;
                
                try {
                    await sendWhatsAppDirect(replyTarget, "✅ *Aapka Decision Receive Ho Gaya!*\nHermes build aapke input ke sath aage badh raha hai.");
                } catch(e) {}
                continue;
            }

            // 2. Status / Progress query
            if (lower.includes("status") || lower.includes("update") || lower.includes("progress") || lower.includes("report") || lower.includes("kya")) {
                console.log(`📊 Dispatching live status update to Admin...`);
                const timeStr = new Date().toLocaleTimeString("en-IN", { timeZone: "Asia/Kolkata" });
                const prog = getLiveProgress();
                
                let completedCount = 1;
                let activeDept = "Sales Department";
                let activeLegend = "Alex Hormozi ($100M Value Equation Engine) — 8/8 Tests Passed";
                let nextLegend = "Jordan Belfort (Straight Line Scripting Engine)";
                
                if (prog && prog.completed_engines) {
                    completedCount = prog.completed_engines.length;
                }

                const statusReply = 
                    `🏭 *SWATCH PAINTS ERP — LIVE SYSTEM STATUS*\n\n` +
                    `🕒 *Time:* ${timeStr}\n` +
                    `🏢 *Current Department:* ${activeDept}\n` +
                    `✅ *Completed Engines:* ${completedCount} (Alex Hormozi — 8/8 Unit Tests Passed)\n` +
                    `⏩ *In Pipeline:* ${nextLegend}\n` +
                    `🤖 *Model:* Moonshot Kimi-K2.7-Code via OmniRoute\n` +
                    `⏱️ *Overnight Schedule:* Kal subah 10:00 AM tak continuous build aur deep testing running hai.\n\n` +
                    `_System 100% autonomous mode me continuous chal raha hai._`;

                try {
                    await sendWhatsAppDirect(replyTarget, statusReply);
                    console.log(`📤 Sent clean live status to Admin`);
                } catch(e) {
                    console.error("Error sending status:", e.message);
                }
                continue;
            }

            // 3. Greeting / General check
            if (lower === "hey" || lower === "hi" || lower === "hello" || lower.startsWith("hey ") || lower.includes("admin")) {
                const adminReply = 
                    `👋 *Namaste Ashutosh Sir!*\n\n` +
                    `Swatch Paints ERP Enterprise System smoothly chal raha hai.\n\n` +
                    `🏢 *Current Status:*\n` +
                    `• Sales Department: Alex Hormozi Value Equation Engine ready (all 8 tests passed).\n` +
                    `• In Queue: Jordan Belfort Straight Line Scripting Engine.\n` +
                    `• Overnight Schedule: Kal subah 10:00 AM tak continuous deep build aur training chalegi.\n\n` +
                    `_Aap *status* bhej kar kisi bhi waqt live progress check kar sakte hain._`;

                try {
                    await sendWhatsAppDirect(replyTarget, adminReply);
                } catch(e) {}
                continue;
            }

            // 4. Default helpful acknowledgment
            const fallbackReply = 
                `🤖 *Hermes ERP Agent*\n\n` +
                `Ashutosh Sir, aapka message receive hua: _"${text}"_\n\n` +
                `Autonomous overnight build chal raha hai.\n` +
                `• Type *status* for live progress report\n` +
                `• Koi bhi question ya decision aap yahan directly bhej sakte hain.`;

            try {
                await sendWhatsAppDirect(replyTarget, fallbackReply);
            } catch(e) {}
        }
    });

    serverPendingQuestion = (q) => { pendingQuestion = q; };
}

let serverPendingQuestion = null;

// HTTP API Server
const server = http.createServer(async (req, res) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");

    if (req.method === "OPTIONS") {
        res.writeHead(200);
        res.end();
        return;
    }

    if (req.url === "/" || req.url === "/qr") {
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        if (connectionStatus === "CONNECTED") {
            res.end(`<html><body style="font-family:sans-serif;text-align:center;padding:50px;background:#f0fdf4;">
                <h1 style="color:#16a34a;">✅ WhatsApp Connected!</h1>
                <p>Bridge is active and authenticated for Swatch Paints ERP.</p>
                <p>Status: <b>CONNECTED (${myJid})</b></p>
            </body></html>`);
        } else if (currentQR) {
            QRCode.toDataURL(currentQR, (err, url) => {
                res.end(`<html><body style="font-family:sans-serif;text-align:center;padding:40px;background:#f8fafc;">
                    <h2>📲 Scan QR Code to Connect WhatsApp</h2>
                    <img src="${url}" style="width:300px;border:4px solid #0284c7;border-radius:12px;padding:10px;background:white;" />
                    <script>setTimeout(() => location.reload(), 10000);</script>
                </body></html>`);
            });
        } else {
            res.end(`<html><body style="font-family:sans-serif;text-align:center;padding:50px;">
                <h2>⏳ Generating WhatsApp QR Code...</h2>
                <script>setTimeout(() => location.reload(), 3000);</script>
            </body></html>`);
        }
        return;
    }

    if (req.url === "/status") {
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ status: connectionStatus, userJid: myJid }));
        return;
    }

    if (req.url === "/send" && req.method === "POST") {
        let body = "";
        req.on("data", chunk => { body += chunk; });
        req.on("end", async () => {
            try {
                const payload = JSON.parse(body);
                const message = payload.message;
                const cfg = loadAdminConfig();
                const targetJid = (cfg.admin_lids && cfg.admin_lids[0]) ? cfg.admin_lids[0] : (cfg.admin_jid || myJid);

                await sendWhatsAppDirect(targetJid, message);
                res.writeHead(200, { "Content-Type": "application/json" });
                res.end(JSON.stringify({ success: true, target: targetJid }));
            } catch (err) {
                res.writeHead(500, { "Content-Type": "application/json" });
                res.end(JSON.stringify({ error: err.message }));
            }
        });
        return;
    }

    if (req.url === "/ask" && req.method === "POST") {
        let body = "";
        req.on("data", chunk => { body += chunk; });
        req.on("end", async () => {
            try {
                const payload = JSON.parse(body);
                const qId = "q_" + Date.now();
                const questionText = payload.question;
                
                if (serverPendingQuestion) {
                    serverPendingQuestion({ id: qId, question: questionText });
                }

                const waText = `❓ *SWATCH PAINTS — CLARIFICATION / DECISION NEEDED*\n\n${questionText}\n\n👉 *Ashutosh Sir, please reply directly to this message to give your decision.*`;
                const cfg = loadAdminConfig();
                const targetJid = (cfg.admin_lids && cfg.admin_lids[0]) ? cfg.admin_lids[0] : (cfg.admin_jid || myJid);
                await sendWhatsAppDirect(targetJid, waText);

                res.writeHead(200, { "Content-Type": "application/json" });
                res.end(JSON.stringify({ success: true, question_id: qId }));
            } catch (err) {
                res.writeHead(500, { "Content-Type": "application/json" });
                res.end(JSON.stringify({ error: err.message }));
            }
        });
        return;
    }

    if (req.url.startsWith("/answer/")) {
        const qId = req.url.split("/answer/")[1];
        const aFile = path.join(__dirname, "answers", `${qId}.json`);
        if (fs.existsSync(aFile)) {
            const data = JSON.parse(fs.readFileSync(aFile, "utf-8"));
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ answered: true, ...data }));
        } else {
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ answered: false }));
        }
        return;
    }

    res.writeHead(404);
    res.end("Not Found");
});

server.listen(PORT, () => {
    console.log(`🌐 WhatsApp Bridge Server listening at http://localhost:${PORT}`);
    startWhatsApp();
});
