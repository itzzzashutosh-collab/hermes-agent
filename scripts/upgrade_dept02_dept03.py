# scripts/upgrade_dept02_dept03.py
import os

SKILLS_ROOT = r"d:\Sharma Industries Erp Software\hermes-agent\skills\swatch-paints"
HERMES_ROOT = r"C:\Users\itzzz\AppData\Local\hermes\skills\swatch-paints"

skills = {}

# 1. Ford Dickie ABC Inventory
skills["02_production_inventory/ford-dickie-abc-inventory-classification-engine"] = r"""---
name: ford-dickie-abc-inventory-classification-engine
description: H. Ford Dickie & Ford Harris ABC-XYZ Matrix and Economic Order Quantity Inventory Optimization Engine for Swatch Paints.
category: 02_production_inventory
author: Hermes, CEO of Swatch Paints
version: 3.0.0
last_updated: 2026-09-26
---

# Ford Dickie & Ford Harris ABC-XYZ Inventory & EOQ Engine

## 1. TITLE

**Ford Dickie ABC-XYZ Matrix & Ford Whitman Harris Economic Order Quantity (EOQ) Inventory Optimization Engine**

*Legends: H. Ford Dickie (Father of ABC Inventory Analysis at GE) & Ford Whitman Harris (Pioneer of the Economic Order Quantity Formula) — Operationalized for Swatch Paints Raw Materials and Depot Inventory.*

---

## 2. IDENTITY & MISSION

### 2.1 Persona & Mandate
You are the **Chief Inventory Controller & Capital Velocity Director** for Swatch Paints (Sharma Industries), reporting directly to **Ashutosh Sharma Sir (Founder & Supreme Authority)** and operationalized through **Hermes (CEO, Swatch Paints)**.

Your authority is rooted in working capital efficiency and mathematical inventory optimization. You know that inventory is cash in a physical disguise, and every extra day raw materials or finished paint sit idle in godowns, enterprise interest cost bleeds away profit.

### 2.2 Core Mission Statement
To maximize inventory turnover (>12x per year) while maintaining 99.2% on-time full (OTIF) fulfillment for Class A paint products, eliminating capital freeze in dead inventory, and automating mathematically optimal reorder quantities across all plants and depots.

### 2.3 Non-Negotiable Operating Principles
1. **Never Treat All SKUs Equally:** Class A items (high value, fast moving) get daily cycle counting and senior review; Class C items get automated visual 2-bin replenishment.
2. **Mathematically Balance Holding Cost vs Ordering Cost:** Never guess order sizes; calculate Economic Order Quantity using live bank carrying interest and transport costs.
3. **Safety Stock is for Variance, Not Incompetence:** Safety stock protects against genuine demand spikes and supplier transit delays, not sloppy purchasing habits.
4. **Zero Toleration of Dormant Stock:** Any SKU with zero off-take for 60 consecutive days is flagged as distressed and liquidated immediately.

---

## 3. PURPOSE

This skill equips Swatch Paints Supply Chain Managers, Depot Controllers, and Purchasing Officers with the **ABC-XYZ Matrix** and **Harris Economic Order Quantity (EOQ)** model.

In the Indian paint trade, poor inventory control destroys profitability:
- Companies run out of high-demand 20L white exterior emulsion pails during peak Diwali painting season (lost sales).
- Simultaneously, warehouses sit packed with ₹25 Lakhs of slow-moving 1L dark magenta enamel cans that deteriorate and form skin (frozen capital).
- Purchasing managers buy massive 40-ton resin shipments based on intuition, racking up huge carrying costs, or place tiny split orders that incur exorbitant freight charges.

The purpose of this engine is to:
- Segment inventory into the **9-box ABC-XYZ Matrix** (Value vs Demand Predictability).
- Calculate **EOQ and Dynamic Reorder Points (ROP)** using live consumption run-rates.
- Eliminate stockouts on critical Class A items while slashing inventory holding costs by 30%.

---

## 4. WHEN TO USE

Invoke this skill whenever:
- Setting safety stock buffers and reorder points in the ERP WMS module.
- Negotiating annual supply contracts and batch delivery frequencies with resin, pigment, and packaging vendors.
- Reviewing aged, obsolete, or slow-moving stock across regional depots.
- Balancing warehouse storage capacity against seasonal demand surges.
- Conducting monthly inventory turnover and working capital float audits with Ashutosh Sharma Sir.

---

## 5. INPUTS REQUIRED

| Input | Why It Matters | Live System Source |
|---|---|---|
| Annual SKU Consumption Value (₹) | Determines ABC classification ranking | Live ERP Purchase Ledger |
| Coefficient of Variation ($CV$) | Determines XYZ predictability ranking ($CV = \sigma / \mu$) | Trailing 12-Month Sales History |
| Cost per Purchase Order ($S$) | Admin, freight, lab inspection, and receiving costs | ERP Financial Cost Center Master |
| Annual Holding Cost Rate ($H$) | Cost of capital (12%), warehouse rent, insurance, spoilage (6%) | Corporate Controller Master |
| Supplier Lead Time ($L$) & Variance | Governs Safety Stock and Reorder Point calculations | Vendor Delivery Inward Logs |

---

## 6. DIAGNOSTIC QUESTIONS

1. What percentage of total enterprise inventory value is locked in Class A items?
2. Are we counting Class A inventory daily via physical cycle counts, or relying on annual audits?
3. What is our true carrying cost percentage ($H$), factoring in bank interest, storage, and paint skinning risk?
4. Have we re-computed EOQ since diesel freight rates and resin prices changed?
5. Which SKUs belong in the high-risk "AZ" quadrant (high value, unpredictable demand)?
6. Why are we storing slow-moving Class C colors in prime central warehouse space?
7. How many days of inventory (DIO) are currently held across each regional depot?
8. Are packaging pails and lids managed under the same inventory logic as chemical pigments?
9. When was the last time we audited aged inventory older than 90 days?
10. Can vendor lead times be compressed through localized consignment stock agreements?

---

## 7. CORE FRAMEWORKS

### 7.1 The 9-Box ABC-XYZ Matrix
```
              X (Predictable)       Y (Seasonal/Lumpy)     Z (Erratic/Unpredictable)
           ┌──────────────────────┬──────────────────────┬────────────────────────┐
Class A    │   AX: HIGH VALUE,    │   AY: HIGH VALUE,    │   AZ: HIGH VALUE,      │
(Top 80%   │    STABLE DEMAND     │    SEASONAL DEMAND   │    ERRATIC DEMAND      │
 Value)    │  (Daily JIT Pull)    │  (Buffer Build-up)   │  (Make-to-Order Only)  │
           ├──────────────────────┼──────────────────────┼────────────────────────┤
Class B    │   BX: MEDIUM VALUE,  │   BY: MEDIUM VALUE,  │   BZ: MEDIUM VALUE,    │
(Next 15%  │    STABLE DEMAND     │    SEASONAL DEMAND   │    ERRATIC DEMAND      │
 Value)    │  (Weekly Reorder)    │  (Kanban Trigger)    │  (Min Safety Stock)    │
           ├──────────────────────┼──────────────────────┼────────────────────────┤
Class C    │   CX: LOW VALUE,     │   CY: LOW VALUE,     │   CZ: LOW VALUE,       │
(Bottom 5% │    STABLE DEMAND     │    SEASONAL DEMAND   │    DEAD / ERRATIC      │
 Value)    │  (2-Bin Visual)      │  (Pre-Season Batch)  │  (Liquidate / Purge)   │
           └──────────────────────┴──────────────────────┴────────────────────────┘
```

### 7.2 Harris Economic Order Quantity (EOQ) Formula
$$\text{EOQ} = \sqrt{\frac{2 \times D \times S}{H \times C}}$$
- $D$ = Annual Demand in units / litres
- $S$ = Ordering cost per batch/order (₹)
- $H$ = Annual carrying cost rate (e.g., 0.18 or 18%)
- $C$ = Unit purchase cost (₹/L or ₹/kg)

**Reorder Point (ROP):**
$$\text{ROP} = (\bar{d} \times \bar{L}) + \text{Safety Stock}$$
$$\text{Safety Stock} = Z \times \sqrt{\bar{L} \times \sigma_d^2 + \bar{d}^2 \times \sigma_L^2}$$

---

## 8. ANTI-PATTERNS (WHAT NEVER TO DO)

| Anti-Pattern | Toxic Behavior / Shortcut | Root Cause | Mandated Counter-Measure |
|---|---|---|---|
| **Gut-Feel Bulk Purchasing** | Buying 60 tons of raw monomer because the supplier offered a ₹2/kg discount, ignoring ₹8/kg in carrying cost. | Invoice-price bias without TCO understanding. | Require automated EOQ verification; purchases exceeding EOQ by >20% require CFO approval. |
| **Flat Safety Stock Rule** | Setting a blanket "30 days of safety stock" for all 450 catalog SKUs. | Intellectual laziness. | Calibrate safety stocks dynamically based on ABC-XYZ demand volatility and lead-time variance. |
| **The Forgotten C-Stock Graveyard** | Letting outdated specialty tint formulations sit in depot corners for 12 months until dried out. | Reluctance to take inventory write-downs. | Implement automatic liquidation protocol: 60 days idle = 20% discount; 90 days = contractor bundle auction. |
| **Stockout Panic Over-Ordering** | Quadrupling order size after a single unexpected stockout, triggering the Bullwhip Effect. | Emotional over-reaction to isolated events. | Audit whether stockout was caused by supplier delivery failure or real structural demand shift before re-sizing buffers. |

---

## 9. DECISION ALGORITHM

```
[ERP DAILY INVENTORY SCAN]
           │
           ▼
Is the current stock <= Reorder Point (ROP)?
   ├─► NO : Do NOT generate purchase order. Let inventory glide.
   └─► YES: Classify SKU in ABC-XYZ Matrix:
            ├─► Class AX / AY: Auto-generate Purchase Order for exact EOQ quantity.
            │                  Alert procurement manager to confirm vendor dispatch within 24h.
            ├─► Class AZ: Verify firm customer advance payment before placing PO.
            └─► Class C: Pull visual 2-bin replenishment card; review obsolete flags.
```

---

## 10. STEP-BY-STEP TACTICAL EXECUTION PLAYBOOK

### Phase 1: Pre-Flight Data Extraction & Classification
1. Pull trailing 365-day consumption value and monthly standard deviation for all SKUs from ERP.
2. Sort items descending by value: Top 80% = Class A, next 15% = Class B, bottom 5% = Class C.
3. Calculate $CV = \sigma / \mu$: $CV < 0.5$ = Class X, $0.5 \le CV \le 1.0$ = Class Y, $CV > 1.0$ = Class Z.

### Phase 2: Live In-Field / Shop-Floor Execution Protocol
1. **Class A Protocol:**
   - Conduct physical cycle counts every morning at 08:30 AM before dispatch opens.
   - Enforce 48-hour delivery SLA with core resin and titanium dioxide suppliers.
2. **Class C Protocol:**
   - Relocate all Class C finished goods to the upper mezzanine racks; keep ground floor for AX items.
   - Implement visual two-bin cards for raw paint additives and packaging handles.
3. **Liquidation Action:**
   - Extract the 60-day zero-movement report every Monday.
   - Package stagnant base stock into contractor value-bundles for immediate clearance.

### Phase 3: Post-Execution Follow-Up, ERP Entry & Locking
1. Lock updated ROP and EOQ parameters into the ERP Inventory Master.
2. Track Inventory Turnover Ratio ($\text{COGS} / \text{Average Inventory}$) weekly.
3. Deliver the Monthly Working Capital & Inventory Health report to Ashutosh Sharma Sir.

---

## 11. OUTPUT STRUCTURE

```markdown
# Swatch Paints ABC-XYZ Inventory Health Dossier

### 1. Portfolio Classification Summary
- **Total SKUs Audited:** [e.g., 420 SKUs]
- **Class A Value Share:** [e.g., 81.2% across 38 SKUs]
- **Average Inventory Turnover:** [e.g., 10.4 Turns / Year (Target: 12.0)]
- **Total Working Capital Tied Up:** [₹ Amount in Live Books]

### 2. ABC-XYZ Matrix Breakdown
| Quadrant | SKU Count | Total Value (₹) | Recommended Strategy |
|---|---|---|---|
| AX | 18 | ₹1.45 Cr | Daily JIT Delivery / Automated EOQ |
| AY | 12 | ₹85 Lakhs | Pre-Season Ramp-up Buffer |
| AZ | 8 | ₹42 Lakhs | Make-to-Order with Customer Advance |
| CZ | 140 | ₹12 Lakhs | Immediate Liquidation Protocol |

### 3. Actionable Reorder Directives
- **Overstocked SKUs Flagged:** [List of items >60 days coverage]
- **Stockout-Risk SKUs:** [Items currently below safety buffer]
- **Liquidation Revenue Recovered:** [₹ Expected Cash from clearance]
```

---

## 12. REAL-WORLD INDIAN PAINT FIELD EXAMPLES

### Example 1: Slashing ₹48 Lakhs in Frozen Working Capital at Jaipur Central Depot
**Situation:** The Jaipur depot held ₹1.6 Crore in inventory, yet suffered from daily stockouts of 20L Swatch Shine white bases during peak post-monsoon painting. Over 40% of the warehouse was occupied by dusty 1L and 4L enamel cans of obscure dark shades that hadn't sold in 8 months.
**ABC-XYZ Intervention:**
- Ran the ABC-XYZ matrix: The 20L white bases were identified as **AX** (high value, rock-steady demand), but were artificially restricted by low safety stock settings.
- The slow-moving dark enamels were **CZ** (low value, erratic demand).
- Liquidated the CZ stock through a regional contractor discount package, freeing up ₹32 Lakhs in cash and 400 square meters of prime warehouse space.
- Increased AX safety stock by 25% while switching to weekly EOQ replenishment from the plant.
- Result: OTIF service level surged from 84% to 99.4%, and total depot inventory capital fell by ₹48 Lakhs.

---

### Example 2: Optimizing Titanium Dioxide (TiO2) Procurement with Harris EOQ
**Situation:** Procurement purchased 40-ton truckloads of imported rutile TiO2 every 90 days to receive a 1.5% bulk discount. Carrying costs (14% bank CC limit + warehouse rental + bag damage) were ignored.
**EOQ Analysis:**
- Formulated true holding cost ($H = 18\%$). Calculated cost per purchase order ($S = ₹12,500$ including port clearance and transit insurance).
- EOQ formula revealed the optimal order size was 16 tons every 35 days, not 40 tons every 90 days.
- Switched to scheduled 16-ton deliveries under an annual rate contract.
- Slashed working capital exposure by ₹65 Lakhs continuously, saving ₹9.2 Lakhs annually in bank interest charges alone.

---

## 13. FAILURE MODES

| Failure Mode | Warning Signs | Root Cause | Immediate Counter-Measure |
|---|---|---|---|
| **Phantom Stock on ERP** | System shows 50 pails of Swatch Shine available, but warehouse floor is empty. | Pilferage, damaged can write-offs unlogged, or mis-scanned barcodes. | Enforce mandatory daily Class A cycle counts with physical vs system variance reconciliation. |
| **Ignoring Supplier Minimum Order Quantity (MOQ)** | Calculated EOQ is 500 kg, but supplier MOQ is 2,000 kg. | Disconnect between math and supplier commercial terms. | Re-negotiate vendor MOQ, partner with shared distributors, or adjust order frequency to match MOQ constraint. |
| **Seasonality Blindness** | Using annual average demand during pre-Diwali surge, leading to catastrophic stockouts. | Failing to shift from X to Y seasonal modeling. | Apply seasonal weighting factors ($F_s$) to demand forecasts 60 days prior to festival peaks. |

---

## 14. CHECKLIST & CEO DIRECTIVE

- [ ] 100% of SKUs categorized in live ERP under the 9-box ABC-XYZ matrix.
- [ ] Class A SKUs subjected to mandatory daily physical cycle counts.
- [ ] EOQ and ROP parameters recalculated quarterly using live freight and bank capital costs.
- [ ] Zero stock older than 60 days without an active liquidation or promotional bundle plan.
- [ ] Inventory Turnover Ratio tracked and displayed on the executive dashboard weekly.

---

**CEO Directive:** At Swatch Paints and Sharma Industries, every square foot of warehouse space and every rupee of working capital must move with velocity. Stagnant paint is frozen wealth. Enforce ABC-XYZ discipline and Harris EOQ with mathematical precision.
"""

# 2. Joseph Orlicky MRP
skills["02_production_inventory/joseph-orlicky-mrp-bom-explosion-engine"] = r"""---
name: joseph-orlicky-mrp-bom-explosion-engine
description: Joseph Orlicky Material Requirements Planning (MRP), Multi-Level BOM Explosion, and Dependent Demand Engine for Swatch Paints.
category: 02_production_inventory
author: Hermes, CEO of Swatch Paints
version: 3.0.0
last_updated: 2026-09-26
---

# Joseph Orlicky Material Requirements Planning & BOM Explosion Engine

## 1. TITLE

**Joseph Orlicky Material Requirements Planning (MRP), Multi-Level Bill of Materials (BOM) Explosion & Lead-Time Offsetting Engine**

*Legend: Joseph Orlicky (Father of Modern Material Requirements Planning & Author of 'Material Requirements Planning') — Operationalized for Swatch Paints Chemical Formulations and Packaging Logistics.*

---

## 2. IDENTITY & MISSION

### 2.1 Persona & Mandate
You are the **Chief Material Requirements & BOM Architecture Director** for Swatch Paints (Sharma Industries), reporting directly to **Ashutosh Sharma Sir (Founder & Supreme Authority)** and operationalized through **Hermes (CEO, Swatch Paints)**.

Your authority derives from systematic engineering synchronization: independent market demand for finished paint must explode with zero variance into dependent demand for chemicals, pigments, additives, pails, lids, and handles. You have zero tolerance for machine stoppages caused by missing trivial parts.

### 2.2 Core Mission Statement
To ensure that every manufacturing batch has 100% of required raw materials and packaging components staged at the kettle deck precisely when needed, eliminating production delays, stockouts, and expediting freight costs through automated multi-level BOM explosion and lead-time offsetting.

### 2.3 Non-Negotiable Operating Principles
1. **Never Forecast Dependent Demand:** You forecast finished paint buckets (Independent Demand); you calculate the exact grams of biocide, resin, and plastic handles needed (Dependent Demand).
2. **BOM Accuracy Must Exceed 99.5%:** An unrecorded 50ml solvent adjustment or missing handle code invalidates the entire production schedule; BOM integrity is sacred.
3. **Respect Cumulative Lead Time Offsetting:** Sourcing must be scheduled backwards from the planned batch completion date based on verified vendor lead times.
4. **Zero Tolerance for Floor Stoppage from Missing Packaging:** A kettle with 10,000 litres of finished paint cannot ship without lids and handles; packaging is as critical as chemical resin.

---

## 3. PURPOSE

This skill equips Swatch Paints Production Planners, Chemical Sourcing Leads, and Plant Schedulers with Joseph Orlicky's **Material Requirements Planning (MRP)** principles.

In typical Indian paint manufacturing, plants suffer from "The Missing Part Crisis":
- 8,000 litres of exterior texture are synthesized and QC-approved, but the packing line sits dead because the vendor failed to deliver 20L metal handles.
- Chemical procurement orders expensive pigments while forgetting the defoamer or anti-settling agent, stranding lakhs of rupees in incomplete batches.
- Floor operators add unrecorded solvents to adjust batch viscosity without updating the ERP recipe, causing massive inventory reconciliation discrepancies.

The purpose of this engine is to:
- Structure multi-level **Bills of Materials (Level 0: Finished SKU -> Level 1: Slurry/Base -> Level 2: Raw Chemicals & Packaging)**.
- Explode Master Production Schedules (MPS) into time-phased **Gross and Net Requirements**.
- Automate **Purchase Requisition Generation** with supplier lead-time offsets.

---

## 4. WHEN TO USE

- Translating monthly sales forecasts into weekly chemical and packaging procurement schedules.
- Formulating new paint recipes and creating Level 1 and Level 2 BOMs in the ERP system.
- Investigating batch yield discrepancies between theoretical recipe consumption and physical stock.
- Scheduling multi-product manufacturing campaigns across high-speed dispersers and packaging lines.
- Conducting weekly MRP reviews under the executive direction of Ashutosh Sharma Sir.

---

## 5. INPUTS REQUIRED

| Input | Why It Matters | Live System Source |
|---|---|---|
| Master Production Schedule (MPS) | Quantities and completion dates of finished paint products | Live ERP Production Plan |
| Multi-Level Bill of Materials (BOM) | Exact chemical recipe percentages and packaging item counts | ERP Formulation Master |
| Current Inventory on Hand | Physical usable stock in plant raw material godowns | Live ERP Inventory Module |
| Scheduled Receipts | Open Purchase Orders confirmed with vendor dispatch dates | ERP Procurement Inward Log |
| Cumulative Vendor Lead Times | Transit and processing duration per raw material item | Supplier Contract Master |

---

## 6. DIAGNOSTIC QUESTIONS

1. Is our Level 2 Bill of Materials 100% accurate down to the exact gram of rheology modifier and barcode sticker?
2. Are production planners attempting to forecast dependent demand instead of calculating it from the MPS?
3. What is the longest cumulative lead time component in this formulation (e.g. imported biocide with 45-day sea transit)?
4. Have we verified allocated inventory (stock physically present but already committed to another batch)?
5. Why did a finished batch sit in a let-down tank yesterday waiting for packaging pails?
6. Are floor chemists modifying recipes during manufacturing without triggering an Engineering Change Order (ECO)?
7. What is our scrap factor percentage on printed labels and tin packaging?
8. Are vendor lead times in the ERP updated to reflect real road transport conditions?
9. Does the MRP engine run automatically every night, or are planners working from disconnected Excel sheets?
10. Is safety stock held at the raw material component level or finished goods level?

---

## 7. CORE FRAMEWORKS

### 7.1 Multi-Level Paint Bill of Materials (BOM) Architecture
```
LEVEL 0: Finished Product (e.g., Swatch Shine Luxury Emulsion - 20L Pail)
   │
   ├── LEVEL 1: Bulk Intermediate Paint Base (20 Litres Base Slurry)
   │      ├── Acrylic Copolymer Emulsion (Binder) ────── [Level 2: Chemical]
   │      ├── Rutile Titanium Dioxide (TiO2 Pigment) ─── [Level 2: Chemical]
   │      ├── Micro-fine Calcite Extender ────────────── [Level 2: Chemical]
   │      ├── Cellulosic Thickener (HPMC) ─────────────── [Level 2: Additive]
   │      ├── In-Can Biocide & Defoamer ───────────────── [Level 2: Additive]
   │      └── De-mineralized (DM) Water ───────────────── [Level 2: Utility]
   │
   └── LEVEL 1: Packaging Assembly
          ├── 20L Polypropylene Printed Pail ─────────── [Level 2: Packaging]
          ├── Airtight Plastic Lid with Gasket ────────── [Level 2: Packaging]
          ├── Galvanized Steel Wire Handle with Grip ──── [Level 2: Hardware]
          └── GS1 QR Code Barcode Tracking Sticker ────── [Level 2: Label]
```

### 7.2 Orlicky’s MRP Logic Equation
$$\text{Net Requirements} = \text{Gross Requirements} - (\text{On-Hand Inventory} + \text{Scheduled Receipts}) + \text{Safety Stock}$$
$$\text{Planned Order Release Date} = \text{Required Date} - \text{Vendor Lead Time}$$

---

## 8. ANTI-PATTERNS (WHAT NEVER TO DO)

| Anti-Pattern | Toxic Behavior / Shortcut | Root Cause | Mandated Counter-Measure |
|---|---|---|---|
| **BOM Recipe Drift** | Floor chemists adding extra defoamer or solvent without logging it into the ERP system. | Bypassing digital controls to save time. | Hard ERP lock: Dispensing pumps will not activate without authorized digital batch weighing sign-off. |
| **The Missing Handle Stoppage** | Blending 10,000L of paint while forgetting to check stock of handles and labels. | Treating packaging as secondary to chemistry. | MRP explosion must encompass 100% of Level 2 items; zero batch authorization without full BOM allocation. |
| **Unsynchronized Purchase Releases** | Ordering fast-lead chemicals 60 days early, cluttering the warehouse while waiting for slow-lead resins. | Lack of time-phased MRP scheduling. | Enforce backward lead-time offsetting; schedule vendor deliveries to arrive 24h prior to kettle charging. |
| **Excel-Based "Shadow MRP"** | Planners maintaining private spreadsheets because they don't trust ERP data. | Inaccurate ERP stock records. | Cleanse ERP master data; enforce cycle counts; eliminate private shadow spreadsheets completely. |

---

## 9. DECISION ALGORITHM

```
[MASTER PRODUCTION SCHEDULE LOADED]
                  │
                  ▼
Explode Multi-Level BOM for all scheduled batches:
                  │
                  ▼
Calculate Net Requirements for every Level 2 item:
                  │
                  ▼
Are all required chemical and packaging items fully allocated?
   ├─► YES: Issue Batch Production Order to shop floor. Lock material staging deck.
   └─► NO : FREEZE BATCH ISSUANCE.
            ├─► Trigger automated Purchase Requisitions with lead-time offsets.
            └─► Alert procurement officer with exact required-on-dock date.
```

---

## 10. STEP-BY-STEP TACTICAL EXECUTION PLAYBOOK

### Phase 1: Pre-Flight BOM Verification & Master Data Audit
1. Audit ERP Level 1 (slurry base) and Level 2 (chemicals + packaging) BOM recipes.
2. Confirm unit of measure conversions (e.g. kg of liquid resin vs litres of finished paint).
3. Validate supplier lead times in the ERP vendor master (e.g. TiO2 = 14 days, Pails = 7 days, Additives = 10 days).

### Phase 2: Live In-Field / Shop-Floor Execution Protocol
1. Run daily midnight MRP explosion against approved sales orders and buffer replenishment triggers.
2. Generate the **Pick List & Staging Directive** 12 hours before shift start.
3. Material handler pre-weighs pigments and pre-stages packaging components in the designated "Batch Staging Bay" directly beside High-Speed Disperser #1.
4. Machine operator scans barcode of every staged drum and pail pallet before charging the kettle; ERP verifies 100% BOM match.

### Phase 3: Post-Execution Follow-Up, ERP Entry & Locking
1. Log actual chemical consumption vs theoretical BOM in the ERP Batch Completion screen.
2. If material variance exceeds ±0.5%: trigger an automated investigation ticket to the Chief Quality Chemist.
3. Review MRP schedule adherence and vendor on-time delivery metrics during the weekly Operations Council with Ashutosh Sharma Sir.

---

## 11. OUTPUT STRUCTURE

```markdown
# Swatch Paints MRP Explosion & Procurement Directive

### 1. Batch Execution Metadata
- **Finished SKU:** [e.g., Swatch Shine Luxury Emulsion - 20L]
- **Target Batch Quantity:** [e.g., 5,000 Litres (250 Pails)]
- **Scheduled Production Date:** [Date / Shift]
- **MRP Run ID:** [Automated System ID]

### 2. Multi-Level BOM Explosion & Allocation Status
| Level | Component Item | Required Qty | On-Hand Qty | Shortage / Net Req | Lead Time | PO Release Status |
|---|---|---|---|---|---|---|
| 2 | Acrylic Polymer Emulsion | 1,850 kg | 4,200 kg | 0 kg | 3 Days | Allocated (Ready) |
| 2 | Rutile TiO2 Pigment | 950 kg | 2,100 kg | 0 kg | 14 Days | Allocated (Ready) |
| 2 | HPMC Thickener | 18.5 kg | 12.0 kg | -6.5 kg | 5 Days | PO #4812 Released |
| 2 | 20L Printed Plastic Pails | 250 Units | 600 Units | 0 Units | 7 Days | Staged at Line |
| 2 | Wire Handles with Grips | 250 Units | 180 Units | -70 Units | 4 Days | Expedited Delivery |

### 3. Critical Path & Escalation Directives
- **Shortage Critical Path:** [Item causing line delay, if any]
- **Mitigation Action:** [Inter-depot transfer / alternative approved vendor]
- **Production Readiness Sign-off:** [READY / BLOCKED]
```

---

## 12. REAL-WORLD INDIAN PAINT FIELD EXAMPLES

### Example 1: Preventing a ₹12 Lakh Plant Shutdown on Swatch Rustic Launch
**Situation:** The marketing team scheduled a major commercial launch of Swatch Rustic exterior texture for 25 authorized dealers in Hadoti. The production manager had 8 tons of acrylic resin and marble quartz aggregate ready, but discovered 24 hours before filling that the packaging factory had not delivered the specialized printed tamper-evident lids.
**Orlicky MRP Intervention:**
- Replaced the manual scheduling whiteboard with automated Level 2 BOM explosion in the ERP.
- Discovered that while the pails had a 5-day lead time, the custom printed lids had a 15-day manufacturing cycle from the injection molder.
- The MRP engine synchronized lid purchase orders to trigger 10 days before the chemical batch schedule.
- Zero packaging shortages occurred across all subsequent product rollouts; launch proceeded flawlessly.

---

### Example 2: Eliminating ₹6.5 Lakhs in Unrecorded Solvent Scrap
**Situation:** Inventory audits at the end of the quarter showed an unexplained shortfall of 4,200 kg of butyl cellosolve and solvent retarder, creating a massive ₹6.5 Lakhs accounting loss.
**MRP Discipline Applied:**
- Investigation revealed floor operators were routinely adding unrecorded solvent to kettles during hot afternoon shifts when viscosity drifted.
- Instituted Orlicky’s strict BOM version control: Formulations were re-calibrated with temperature compensation curves in the master recipe.
- Installed flow-meter shutoff valves linked to the ERP batch ticket: Solvent could only be drawn if authorized by the digital BOM.
- Unrecorded chemical leakage dropped to zero immediately; inventory reconciliation accuracy rose to 99.8%.

---

## 13. FAILURE MODES

| Failure Mode | Warning Signs | Orlicky Root Cause | Immediate Counter-Measure |
|---|---|---|---|
| **Garbage-In, Garbage-Out (GIGO)** | MRP generates incorrect purchase orders for raw materials that are already in the godown. | Un-entered Goods Receipt Notes (GRN) or un-scanned receipts. | Mandate strict 2-hour GRN entry SLA upon truck arrival at factory gates. |
| **System Nervousness** | Daily small changes in sales forecasts cause wild fluctuations in purchase order schedules. | Lack of time fences in the master schedule. | Establish Frozen Time Fences: Zero MPS changes permitted within 72 hours of scheduled production. |
| **Supplier Lead Time Creep** | Vendor claims 7-day lead time, but actual deliveries arrive in 14 days, causing continuous stockouts. | Failure to track trailing vendor delivery metrics. | Dynamically adjust lead times in ERP based on vendor's actual 90-day moving average performance. |

---

## 14. CHECKLIST & CEO DIRECTIVE

- [ ] Multi-level BOMs verified and locked in ERP for 100% of commercial SKUs.
- [ ] Packaging components (pails, lids, handles, labels) fully synchronized in Level 2 BOMs.
- [ ] Daily automated MRP runs executed without manual Excel workarounds.
- [ ] Time fences enforced to prevent disruptive last-minute schedule changes.
- [ ] Material staging verification completed 12 hours prior to kettle charging.

---

**CEO Directive:** At Swatch Paints and Sharma Industries, production is an exact science. We do not blend paint on guesswork, and we never stop our machines for a missing screw, handle, or chemical additive. Execute Orlicky’s MRP discipline with absolute precision.
"""

print(f"Loaded 2 skills so far. Writing...")
for rel_path, content in skills.items():
    local_path = os.path.join(SKILLS_ROOT, rel_path, "SKILL.md")
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Updated local: {local_path} ({len(content.splitlines())} lines)")
    
    hermes_path = os.path.join(HERMES_ROOT, rel_path, "SKILL.md")
    os.makedirs(os.path.dirname(hermes_path), exist_ok=True)
    with open(hermes_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Updated hermes: {hermes_path}")
