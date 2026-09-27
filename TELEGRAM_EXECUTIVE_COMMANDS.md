# Hermes Telegram Executive Command & Cockpit Specification

## 1. Executive Mission & Channel Separation

This specification defines the dedicated **Telegram Executive Mobile Cockpit** for **Founder & Managing Director Ashutosh Sharma Sir** to command and monitor **Hermes (CEO Agent)** and all 8 enterprise departments of **Swatch Paints (Sharma Industries)**.

```
+---------------------------------------------------------------------------------+
|                       DUAL-CHANNEL ARCHITECTURE SEPARATION                      |
+------------------------------------------------+--------------------------------+
| 1. TELEGRAM (EXECUTIVE COCKPIT)                | 2. WHATSAPP (OPERATIONAL BRIDGE)|
| - Strictly for: Ashutosh Sharma Sir <-> Hermes | - For: Dealers, Painters, Reps |
| - High-level slash commands & approvals        | - WhatsApp Baileys bridge      |
| - Private, encrypted, allowlisted by User ID   | - Bulk broadcasts, token OTPs  |
| - Instant factory, sales & financial telemetry | - Order updates & dispatch tracking|
+------------------------------------------------+--------------------------------+
```

---

## 2. Complete Catalog of Executive Slash Commands (`/`)

Ashutosh Sharma Sir can send any of the following slash commands in the Telegram chat with Hermes for instant real-time telemetry and operational execution:

### 1. `/status` — High-Level Enterprise Dashboard
- **What it does:** Fetches a comprehensive real-time summary across all departments.
- **Output Provided:**
  - Today's plant output in Liters and active reactor batch count.
  - Total primary billing and collections received today.
  - Active accounts receivable health and 21-day credit lockouts.
  - Immediate operational alerts requiring executive attention.

### 2. `/sales` — Commercial Sales & Market Telemetry
- **What it does:** Detailed commercial performance breakdown.
- **Output Provided:**
  - Primary billing vs. monthly quota attainment.
  - Secondary liquidation velocity across key markets (Kota, Bundi, Baran, Jhalawar, Bhilwara).
  - TSO beat plan compliance and counter visit rates.
  - Top 5 performing dealers and bottom 5 stagnant counters.

### 3. `/production` — Factory & Chemical Synthesis Status
- **What it does:** Real-time production report from the Kota manufacturing plant.
- **Output Provided:**
  - Active reactor cycles (Twin-shaft dissolvers, bead mills, blenders).
  - Batches completed today (Emulsion, Exterior Primer, Acrylic Putty, Enamel).
  - NABL quality control approval status (Grind gauge, viscosity, scrub resistance).
  - Plant downtime or maintenance alerts.

### 4. `/inventory` — Finished Goods & Raw Material Stock
- **What it does:** Audits warehouse stock levels against safety buffer thresholds.
- **Output Provided:**
  - Finished goods inventory by category (20L, 10L, 4L, 1L buckets in stock).
  - Critical raw material chemical reserves (Monomers: MMA, BA, VAM; Rutile TiO2).
  - Mineral extender levels (Makrana calcite, dolomite).
  - Immediate re-order triggers for chemicals below 7-day buffer.

### 5. `/finance` — Cashflow, Collections & Credit Locks
- **What it does:** Audits working capital, accounts receivable, and taxation compliance.
- **Output Provided:**
  - Cash collected today vs. outstanding overdue debt.
  - Accounts receivable aging analysis (<21 days, 22-30 days, 31-45 days, >45 days).
  - List of dealers locked out of billing due to credit limit breach (`/api/erp/dealers/credit-lock`).
  - Active GST e-Way bills in transit.

### 6. `/dealer <id_or_name>` — Instant Dealer Dossier
- **What it does:** Pulls a complete forensic dossier on any specific paint counter.
- **Example:** `/dealer DLR-KOTA-014` or `/dealer Verma Hardware`
- **Output Provided:**
  - Credit limit, current balance, and payment history over last 6 months.
  - Swatch Paints counter margin realization (18-22%) vs. competitor estimate.
  - Monthly bucket volume trend and secondary liquidation speed.
  - Top local contractors mapped to this dealer's billing desk.

### 7. `/contractor <id_or_name>` — Painter Thekedar Profile
- **What it does:** Audits a painting contractor's loyalty and token scan activity.
- **Example:** `/contractor Pappu Mistri`
- **Output Provided:**
  - Total 20L bucket tokens scanned this season and UPI cashback disbursed.
  - Active job sites and crew size.
  - Preferred product lines (WeatherShield vs. Royal Luxury vs. Putty).
  - Loyalty tier status and VIP event eligibility.

### 8. `/market <city>` — Territorial Market Share & Reconnaissance
- **What it does:** Summarizes competitive dynamics in a specific district or city.
- **Example:** `/market Bhilwara` or `/market Kota`
- **Output Provided:**
  - Total retail counters mapped vs. active Swatch billing stockists.
  - Incumbent competitive moves (Asian Paints/Berger schemes, Birla Opus sign-ups).
  - Regional depot inventory buffer and 24-hr dispatch SLA status.
  - Contractor mela schedule and upcoming dealer high-tea meets.

### 9. `/dispatch` — Logistics & Fleet Milk-Run Status
- **What it does:** Tracks vehicle delivery routes and customer fulfillment.
- **Output Provided:**
  - Dispatches completed today from Kota mother factory.
  - Vehicles currently en route to regional markets with GPS ETA.
  - Delivery SLA compliance percentage (<24 hours).
  - Reported transit damage or leakage claims.

### 10. `/scrapling <url_or_query>` — On-Demand Competitor & Market Scraping
- **What it does:** Executes Scrapling stealth scraper to pull live market intelligence.
- **Example:** `/scrapling https://competitor-distributor.com/rates`
- **Output Provided:**
  - Current competitor retail MRP and trade discount rates.
  - Chemical spot price index on domestic trade bulletins.
  - Public tender announcements from Rajasthan eProcurement / CPWD portals.

### 11. `/evolve <skill_name>` — Trigger Autonomous Skill Optimization
- **What it does:** Runs DSPy + GEPA self-evolution on a target operational skill.
- **Example:** `/evolve influence-psychology` or `/evolve 01_sales`
- **Output Provided:**
  - Analyzes recent execution traces and field objection failures.
  - Mutates prompt strategies and evaluates against fitness benchmarks.
  - Reports Pareto improvement score and automatically commits the optimized version.

### 12. `/memory <query>` — Query Supermemory Knowledge Vault
- **What it does:** Searches semantic long-term memory for past decisions and context.
- **Example:** `/memory What margin did we promise to Gumanpura dealers for Diwali?`
- **Output Provided:**
  - Direct citations from previous session turns and executive directives.
  - Historical context without needing to search raw chat logs.

### 13. `/sop [department]` — Daily SOP Provisioning & Execution Telemetry
- **What it does:** Displays today's active SOP checklists and execution progress provisioned by Department 08.
- **Example:** `/sop` or `/sop sales` or `/sop production`
- **Output Provided:**
  - Mandatory daily checklists assigned to target department.
  - Live completion percentages and pending items.
  - Verification telemetry (GPS check-ins, batch log sheets, bank reconciliations).

### 14. `/compliance` — Enterprise SOP Scorecard & Exception Dashboard
- **What it does:** Generates the real-time Enterprise SOP Compliance Index (ESCI) across all 7 operational departments.
- **Output Provided:**
  - Departmental compliance breakdown: Green (≥90%), Yellow (75-89%), Red (<75%).
  - Active operational exceptions and root cause flags.
  - Escalated critical deviations requiring Founder review.

### 15. `/alert` — Emergency Operational Alerts
- **What it does:** Filters and displays all high-severity exceptions across the enterprise.
- **Output Provided:**
  - Overdue dealer receivables >30 days without payment promise.
  - Reactor batch quality test failures requiring chemist re-dosing.
  - Raw material chemical stockouts threatening production schedules.

### 16. `/help` — Executive Command Directory
- **What it does:** Displays the quick-reference guide of all slash commands directly inside Telegram.

---

## 3. BotFather Command Configuration Block

When configuring the bot in Telegram via **[@BotFather](https://t.me/BotFather)**, use the `/setcommands` command and paste the exact block below:

```text
status - Real-time enterprise health & plant dashboard
sales - Daily sales, primary billing & market metrics
production - Kota plant reactor batch status & QA reports
inventory - Finished goods stock & raw chemical reserves
finance - Cash collections, AR aging & 21-day credit locks
sop - Daily SOP checklists & execution telemetry by department
compliance - Enterprise SOP scorecard & operational exceptions
dealer - Search dealer dossier, credit terms & order history
contractor - Painter thekedar token scans & loyalty profile
market - District market share, depot SLA & competitor intel
dispatch - Outbound logistics & fleet delivery status
scrapling - Scrape competitor paint prices or chemical rates
evolve - Trigger self-evolution skill optimization cycle
memory - Search Supermemory for past decisions & promises
alert - View high-priority operational & financial alerts
help - Show executive command directory
```

---

## 4. Step-by-Step Telegram Setup & Security Instructions

### Step 1: Create the Bot via @BotFather
1. Open Telegram on your phone or desktop.
2. Search for **@BotFather** (verified account with blue checkmark) and send `/start`.
3. Send `/newbot`.
4. Choose a display name: `Swatch Paints Executive Cockpit` (or `Hermes CEO`).
5. Choose a bot username ending in `bot`: e.g. `swatch_hermes_ceo_bot`.
6. BotFather will issue your secret **API Token**:
   ```
   1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ_example
   ```
7. Send `/setcommands` to BotFather, select your new bot, and paste the command block from Section 3 above.

---

### Step 2: Get Ashutosh Sharma Sir's Telegram User ID
For strict security, Hermes must ONLY respond to Ashutosh Sharma Sir and reject any unauthorized messages.
1. In Telegram, search for **@userinfobot** or **@RawDataBot**.
2. Send `/start`. The bot will immediately reply with your numeric User ID:
   ```
   Id: 987654321
   First: Ashutosh
   Last: Sharma
   ```
3. Copy this numeric User ID (e.g. `987654321`).

---

### Step 3: Configure `.env` in `hermes-agent`
Create or update the `.env` file in `d:\Sharma Industries Erp Software\hermes-agent\.env`:

```env
# =============================================================================
# TELEGRAM EXECUTIVE COCKPIT (HERMES <-> ASHUTOSH SHARMA SIR)
# =============================================================================
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ_example
TELEGRAM_ALLOWED_USERS=987654321
GATEWAY_ALLOW_ALL_USERS=false

# =============================================================================
# WHATSAPP OPERATIONAL BRIDGE (DEALERS, PAINTERS, REPS)
# =============================================================================
WHATSAPP_ENABLED=true
```

> **Security Guarantee:** With `GATEWAY_ALLOW_ALL_USERS=false` and `TELEGRAM_ALLOWED_USERS=987654321`, any stranger who attempts to message your Telegram bot will be silently dropped with zero response. Only Ashutosh Sharma Sir's account has executive access.

---

### Step 4: Launching Hermes with Telegram Gateway Active
Start Hermes with the gateway enabled using PowerShell or batch:

```powershell
# From hermes-agent directory:
cd "d:\Sharma Industries Erp Software\hermes-agent"
python -m hermes_cli.main gateway
```
Or launch using `run_hermes.bat`.

Hermes will log:
```
[INFO] Telegram gateway initialized for bot @swatch_hermes_ceo_bot
[INFO] Polling started. Allowed users: [987654321]
```

Open Telegram, send `/start` or `/status` to your bot, and Hermes will greet you with live executive telemetry!
