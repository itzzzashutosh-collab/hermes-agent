import os
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

logger = logging.getLogger("WhatsAppBridge")
logging.basicConfig(level=logging.INFO)

CONFIG_PATH = Path(__file__).parent / "config.json"
REPORTS_DIR = Path(__file__).parent / "hourly_reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

class WhatsAppBridge:
    def __init__(self, config_file: Path = CONFIG_PATH):
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self):
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading WhatsApp config: {e}")
        return {"enabled": True, "provider": "local_log"}

    def send_hourly_report(self, hour_index: int, department: str, completed_legends: list, pending_legends: list, python_scripts: list, summary_text: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Build standard executive message
        msg_lines = [
            f"🏭 *SWATCH PAINTS ERP — HOURLY PROGRESS AUDIT*",
            f"🕒 *Timestamp:* {timestamp} | *Hour:* #{hour_index}",
            f"🏢 *Active Department:* {department}",
            "",
            f"✅ *Completed Legends ({len(completed_legends)}):*",
        ]
        for c in completed_legends[-5:]:
            msg_lines.append(f"  • {c}")
        if len(completed_legends) > 5:
            msg_lines.append(f"  • ... and {len(completed_legends) - 5} earlier legends")
            
        if python_scripts:
            msg_lines.append("")
            msg_lines.append(f"⚙️ *Tested Python Scripts ({len(python_scripts)}):*")
            for ps in python_scripts[-3:]:
                msg_lines.append(f"  • `{ps}`")
                
        if pending_legends:
            msg_lines.append("")
            msg_lines.append(f"⏳ *Upcoming In Pipeline:*")
            for p in pending_legends[:3]:
                msg_lines.append(f"  • {p}")
                
        msg_lines.append("")
        msg_lines.append(f"📊 *Summary & Quality Status:*")
        msg_lines.append(f"{summary_text}")
        msg_lines.append("")
        msg_lines.append("🤖 _Sent via Antigravity-Hermes Enterprise Bridge_")

        full_message = "\n".join(msg_lines)
        
        # 1. Always record the markdown report
        report_file = REPORTS_DIR / f"hour_{hour_index:02d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(full_message)
            
        # 2. Dispatch to configured WhatsApp provider
        provider = self.config.get("provider", "baileys_local")
        logger.info(f"Dispatching Hourly Report #{hour_index} via provider: {provider}")
        
        # Always try local Baileys bridge first (QR-based, zero API keys needed)
        sent_local = self._send_baileys_local(full_message)
        if sent_local:
            logger.info("Successfully delivered to WhatsApp via Local QR Bridge!")
        elif provider == "meta_whatsapp_cloud":
            self._send_meta_cloud(full_message)
        elif provider == "twilio":
            self._send_twilio(full_message)
        elif provider == "green_api":
            self._send_green_api(full_message)
        elif provider == "ultramsg":
            self._send_ultramsg(full_message)
        else:
            logger.info("Local Baileys waiting for QR scan. Report recorded to: " + str(report_file))
            
        return report_file, full_message

    def _send_baileys_local(self, message: str):
        url = "http://localhost:3005/send"
        payload = {"message": message}
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                logger.info(f"Local Baileys WhatsApp Bridge sent: {resp.status}")
                return True
        except Exception as e:
            return False

    def _send_meta_cloud(self, message: str):
        cfg = self.config.get("providers", {}).get("meta_whatsapp_cloud", {})
        token = cfg.get("api_token")
        phone_id = cfg.get("phone_number_id")
        recipient = cfg.get("recipient_phone")
        if not (token and phone_id and recipient):
            logger.warning("Meta WhatsApp Cloud credentials incomplete. Skipped cloud dispatch.")
            return False
            
        url = f"https://graph.facebook.com/v19.0/{phone_id}/messages"
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient,
            "type": "text",
            "text": {"body": message}
        }
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req) as resp:
                logger.info(f"Meta WhatsApp Cloud sent: {resp.status}")
                return True
        except Exception as e:
            logger.error(f"Meta WhatsApp Cloud error: {e}")
            return False

    def _send_twilio(self, message: str):
        cfg = self.config.get("providers", {}).get("twilio", {})
        sid = cfg.get("account_sid")
        token = cfg.get("auth_token")
        from_no = cfg.get("from_whatsapp_number")
        to_no = cfg.get("to_whatsapp_number")
        if not (sid and token and from_no and to_no):
            logger.warning("Twilio credentials incomplete. Skipped Twilio dispatch.")
            return False
            
        import base64
        url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json"
        data = urllib.parse.urlencode({"From": from_no, "To": to_no, "Body": message}).encode("utf-8")
        auth = base64.b64encode(f"{sid}:{token}".encode("ascii")).decode("ascii")
        try:
            req = urllib.request.Request(
                url,
                data=data,
                headers={"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"},
                method="POST"
            )
            with urllib.request.urlopen(req) as resp:
                logger.info(f"Twilio WhatsApp sent: {resp.status}")
                return True
        except Exception as e:
            logger.error(f"Twilio WhatsApp error: {e}")
            return False

    def _send_green_api(self, message: str):
        cfg = self.config.get("providers", {}).get("green_api", {})
        inst = cfg.get("instance_id")
        token = cfg.get("api_token_instance")
        chat_id = cfg.get("recipient_chat_id")
        if not (inst and token and chat_id):
            logger.warning("Green API credentials incomplete. Skipped Green API dispatch.")
            return False
        url = f"https://api.green-api.com/waInstance{inst}/sendMessage/{token}"
        payload = {"chatId": chat_id, "message": message}
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req) as resp:
                logger.info(f"Green API WhatsApp sent: {resp.status}")
                return True
        except Exception as e:
            logger.error(f"Green API error: {e}")
            return False

    def _send_ultramsg(self, message: str):
        cfg = self.config.get("providers", {}).get("ultramsg", {})
        inst = cfg.get("instance_id")
        token = cfg.get("token")
        to_phone = cfg.get("recipient_phone")
        if not (inst and token and to_phone):
            logger.warning("UltraMsg credentials incomplete. Skipped UltraMsg dispatch.")
            return False
        url = f"https://api.ultramsg.com/{inst}/messages/chat"
        data = urllib.parse.urlencode({"token": token, "to": to_phone, "body": message}).encode("utf-8")
        try:
            req = urllib.request.Request(url, data=data, method="POST")
            with urllib.request.urlopen(req) as resp:
                logger.info(f"UltraMsg WhatsApp sent: {resp.status}")
                return True
        except Exception as e:
            logger.error(f"UltraMsg error: {e}")
            return False

if __name__ == "__main__":
    bridge = WhatsAppBridge()
    bridge.send_hourly_report(
        hour_index=1,
        department="Bridge Initialization",
        completed_legends=["System Bridge Active"],
        pending_legends=["Sales Department", "Production Department"],
        python_scripts=["whatsapp_bridge.py"],
        summary_text="Antigravity-Hermes bridge is initialized. Ready to begin overnight build pipeline."
    )
