import os

WORKSPACE_DIR = r"d:\Sharma Industries Erp Software\hermes-agent"
HERMES_DIR = r"C:\Users\itzzz\AppData\Local\hermes"

PROD_SKILLS = {
    "bill-smith-six-sigma-engine": {
        "title": "Bill Smith & Mikel Harry Six Sigma Batch Variation & Defect Reduction Engine for Swatch Paints",
        "legend": "Bill Smith & Dr. Mikel Harry (Fathers of Six Sigma at Motorola)",
        "description": "Six Sigma DMAIC Methodology, Cpk Process Capability, Defect Reduction, and Variance Control Engine for Swatch Paints Production Department.",
        "dept": "02_production_inventory",
        "tag": "bill-smith",
        "purpose": """This skill equips the Swatch Paints Production Engineering, Quality Assurance, and Plant Operations teams with Bill Smith and Mikel Harry's Six Sigma disciplines: the **DMAIC (Define, Measure, Analyze, Improve, Control)** roadmap, **Process Capability (Cp and Cpk)** analysis, and systematic reduction of batch-to-batch variation.

In Indian paint manufacturing, plant managers frequently accept high batch variation as an unavoidable fact of life. They tolerate color shade drift (Delta E > 1.2), viscosity fluctuations due to seasonal ambient temperature shifts, and varying settling rates between summer and monsoon batches. This leads to costly batch rework, shade adjustments in blending kettles, tinting machine nozzle clogging at dealer counters, and painter rejection.

The engine's purpose is to:
- Institutionalize the **DMAIC Roadmap** for all manufacturing lines: Interior Emulsions, Exterior Weather-proof Coatings, Primers, and Swatch Rustic.
- Shift quality governance from reactive post-batch quality checks to proactive **Process Capability (Cpk >= 1.33)** control of critical-to-quality (CTQ) parameters.
- Measure and eliminate Defect-Per-Million-Opportunities (DPMO) in pigment dispersion, binder polymerization, and automated can-filling lines.
- Eliminate costly kettle rework time, slashing cycle times and cutting raw material scrap to near zero.""",
        "when_to_use": """- A specific paint formulation experiences recurring batch failures or requires repeated tinting adjustments in the kettle.
- Process Capability (Cpk) for batch viscosity, pH, specific gravity, or fineness of grind drops below 1.33.
- Dealers report shade variation or tinting mismatch across different batch lots of the same base white.
- Packaging lines suffer from weight variance (over-filling causing profit leakage or under-filling violating Weights & Measures regulations).
- Initiating a plant-wide root-cause analysis (RCA) on pigment agglomeration or emulsion separation.
- Training plant chemists and line supervisors in statistical process control.""",
        "frameworks": """### 6.1 The DMAIC Roadmap for Paint Manufacturing
1. **Define:** Identify the Critical-to-Quality (CTQ) metric impacting customer satisfaction (e.g., Viscosity in Krebs Units for Exterior Emulsion: Spec 102 ± 4 KU).
2. **Measure:** Collect baseline data across 30 consecutive batches using calibrated viscometers at a standardized 25°C water bath. Calculate baseline DPMO and short-term Z-score.
3. **Analyze:** Construct an Ishikawa (Fishbone) Diagram and 5-Why Tree analyzing the 6M categories (Machine, Method, Material, Measurement, Mother Nature/Environment, Manpower). Conduct ANOVA or regression to isolate primary root causes (e.g., shear rate variation in high-speed dispersers).
4. **Improve:** Design of Experiments (DOE) to optimize mixing parameters: disperser blade RPM, slurry temperature rise, and order of addition of cellulosic thickeners (HEC/ASE).
5. **Control:** Implement Statistical Process Control (SPC) X-bar and R charts. Establish automated kettle shut-off interlocks and standard operating procedures (SOPs).

### 6.2 Process Capability Indices (Cp & Cpk)
```
Cp  = (Upper Specification Limit - Lower Specification Limit) / (6 × σ)
Cpk = Min [ (USL - Mean) / (3 × σ) , (Mean - LSL) / (3 × σ) ]
```
- **Cpk < 1.0:** Incapable process. Batches will produce defects, requiring constant kettle adjustments.
- **1.0 <= Cpk < 1.33:** Barely capable; high risk of drift when ambient temperatures exceed 40°C in Rajasthan summers.
- **Cpk >= 1.33 (Swatch Target):** Statistically capable; virtually defect-free production (<64 ppm).

### 6.3 Gage R&R (Measurement System Analysis)
Before blaming raw materials or operators, measure the measurement system:
- Repeatability (equipment variation) and Reproducibility (chemist-to-chemist variation) must account for <10% of total process tolerance.
- Ban subjective visual shade matching; mandate spectrophotometer readings (Delta E < 0.5 under D65 daylight).""",
        "decision_algo": """### Step 1: CTQ Specification & Baseline Audit
- Identify CTQ: Viscosity (KU), Grind Fineness (Hegman Gauge), Gloss (60°), or Delta E.
- IF Cpk < 1.33:
  - Place formulation on "Quality Watch". Mandatory dual-chemist verification before discharge.

### Step 2: Fishbone & 5-Why Root Cause Isolation
- Form a cross-functional squad: 1 Plant Chemist, 1 Production Supervisor, 1 Maintenance Tech.
- Drill down to the root cause:
  - Why was batch viscosity low? Insufficient thickener activation.
  - Why? Dispersion slurry temperature did not reach 35°C before HEC addition.
  - Why? High-speed disperser blade was worn down by 15%, reducing friction shear.

### Step 3: DOE & Process Improvement
- Run a 2^k factorial experiment testing blade geometry, mixing duration, and wetting agent concentration.
- Lock the optimized formula recipe in the ERP Production Master; lock PLC recipe controllers.

### Step 4: Institute Mistake-Proofing (Poka-Yoke) Control
- Install automatic temperature interlocks: thickener dispenser valve cannot open until slurry temperature reaches 36°C-40°C.
- Log daily X-bar and R control charts on the production display board.""",
        "example1": """### Example 1: Solving Viscosity Instability in Swatch Exterior Emulsion
**Situation:** During May-June (ambient temperature 44°C in Kota), 38% of Swatch Exterior White batches failed the 100-105 KU specification, coming out between 88 and 94 KU. Plant chemists had to add post-thickener, wasting 3 hours per batch.
**DMAIC Applied:**
- *Measure:* Cpk was 0.62 (severely incapable). Viscometer Gage R&R passed (4.2%).
- *Analyze:* 5-Why revealed that in extreme heat, operators reduced high-speed dispersion time from 35 mins to 20 mins to prevent kettle overheating, resulting in poor polymer wetting.
- *Improve:* Installed a chilled water jacket circulation line on Kettles #2 and #4. Set standardized dispersion time to 32 minutes at controlled 32°C.
- *Control:* Cpk rose to 1.48. Batch rework time dropped from 3 hours to zero; zero off-spec batches in 90 days.""",
        "example2": """### Example 2: Eliminating Weight Variation on 20-Litre Automated Can Lines
**Situation:** Automated filling line for 20L distemper buckets had a standard deviation of 280 grams. To prevent underweight penalties, the line was calibrated to overfill by 350 grams per pail.
**Six Sigma Applied:**
- This was massive profit leakage: 350g × 1,200 pails/day = 420 kg of paint given away free daily (worth >₹25,000/day).
- Replaced mechanical pneumatic cutoff valves with high-precision load-cell digital feedback valves.
- Retrained operators on tare-weight recalibration every morning.
- Reduced standard deviation to 35 grams. Reset average fill target to exactly 20.04 kg.
- **Outcome:** Saved over ₹7.5 Lakhs per month in raw material yield with zero underweight infractions.""",
        "failures": [
            ("Measuring Without Controlling", "Collecting Cpk data in a spreadsheet and filing it away without line actions.", "Enforce out-of-control action plans (OCAP): line automatically pauses if 3 consecutive points fall outside 2 sigma."),
            ("Chemist-to-Chemist Variation", "Chemist A tests viscosity at 22°C; Chemist B tests at 34°C without water bath correction.", "Mandate constant-temperature water bath immersion for all QC viscosity samples."),
            ("Post-Batch Firefighting", "Relying on adding water or thickener at the end of the batch instead of fixing the grinding process.", "Ban unauthorized post-batch additions. Fix the core dispersion and letdown phases."),
            ("Blaming Operators Instead of Systems", "Reprimanding line workers for batch errors caused by uncalibrated weighing scales.", "Institute daily digital scale calibration with certified brass weights before shift start.")
        ],
        "checklist": [
            "Critical-to-Quality (CTQ) specifications clearly documented for every SKU.",
            "Process capability (Cpk) calculated across minimum 30 batches; target Cpk >= 1.33.",
            "Measurement System Analysis (Gage R&R) verified under 10% tolerance.",
            "DMAIC root-cause analysis conducted using Fishbone and 5-Why tools.",
            "Automatic process interlocks (Poka-Yoke) installed on critical mixing and dispensing steps.",
            "Automated filling line weight variance verified within ±0.2% tolerance."
        ]
    },
    "ford-w-harris-eoq-engine": {
        "title": "Ford W. Harris Economic Order Quantity (EOQ) & Chemical Inventory Engine for Swatch Paints",
        "legend": "Ford Whitman Harris (Pioneer of Operations Research & Creator of the EOQ Formula, 1913)",
        "description": "Ford W. Harris Economic Order Quantity (EOQ), Raw Material Carrying Cost vs. Ordering Cost Optimization, and Safety Stock Engine for Swatch Paints Production.",
        "dept": "02_production_inventory",
        "tag": "ford-w-harris",
        "purpose": """This skill equips the Swatch Paints Procurement, Plant Inventory, and Finance teams with Ford Whitman Harris’s foundational **Economic Order Quantity (EOQ)** model and mathematical inventory optimization disciplines.

In paint manufacturing, raw materials represent 65% to 72% of total production cost. Plant managers often vacillate between two dangerous extremes:
1. **Over-ordering bulk materials** (e.g., ordering 40 tonnes of Titanium Dioxide or Acrylic Emulsion) to obtain bulk supplier rebates, thereby locking up millions in working capital, risking drum leakage, polymer skinning/degradation, and incurring warehouse holding costs.
2. **Under-ordering** in tiny piecemeal lots, which triggers chronic stockouts, high freight per kilogram, kettle shutdowns, and emergency freight charges.

The engine's purpose is to:
- Mathematically calculate the exact **Economic Order Quantity (EOQ)** for all raw material classes: Pigments (TiO2, Phthalocyanine Blue), Binders (Pure Acrylic, Styrene Acrylic), Solvents, and Additives.
- Quantify true **Carrying Costs (H)**: including warehouse space, cost of tied-up capital (WACC), evaporation/settling risk, and insurance.
- Establish robust **Reorder Points (ROP)** and dynamic **Safety Stocks** calibrated to supplier lead-time variability.
- Maximize inventory turns while guaranteeing 99.5% raw material availability for scheduled production runs.""",
        "when_to_use": """- Determining order batch sizes and delivery schedules for imported and domestic raw material contracts.
- Evaluating supplier volume discount offers: determining whether a 2% price cut justifies ordering 3 months of inventory.
- Rising bank interest rates or tight working capital requiring a reduction in inventory holding costs.
- Managing packaging inventory (empty tin cans, plastic pails, lids, handles) to prevent storage bloat.
- Formulating annual raw material procurement contracts with chemical suppliers (Dow, BASF, Arkema, Reliance).
- Resolving disputes between Procurement (who want bulk discounts) and Finance (who want lean cash).""",
        "frameworks": """### 6.1 The Classical EOQ Formula
Harris's balance between Ordering/Setup Costs (S) and Inventory Carrying Costs (H):
```
EOQ = SQRT( (2 × D × S) / H )
```
Where:
- **D = Annual Demand (Units or kg):** Total projected consumption from ERP Master Production Schedule.
- **S = Ordering Cost per Order (₹):** Purchase order generation, inspection, laboratory testing, and transport freight fixed charge.
- **H = Annual Holding/Carrying Cost per Unit (₹/kg/year):**
  ```
  H = Unit Cost (P) × Carrying Cost Percentage (i)
  ```
  Where `i` at Swatch Paints typically includes: Cost of Capital (11%) + Godown Footprint/Storage (4%) + Spoilage/Skinning/Leakage Risk (3%) + Handling/Insurance (2%) = **20% per year**.

### 6.2 Total Cost of Inventory Curve
```
Total Annual Cost (TC) = (D / Q) × S + (Q / 2) × H + (D × P)
```
- At EOQ, Annual Ordering Cost equals Annual Carrying Cost.
- Any deviation from EOQ increases total operational costs.

### 6.3 Reorder Point (ROP) & Safety Stock (SS)
Never reorder when the godown is empty. Reorder when stock touches the ROP:
```
ROP = (Daily Demand Rate × Lead Time in Days) + Safety Stock
Safety Stock (SS) = Z × SQRT( (Lead Time × σ_d²) + (Demand² × σ_lt²) )
```
Where:
- `Z` = Service Level factor (Z = 2.33 for 99% availability).
- `σ_d` = Standard deviation of daily paint production consumption.
- `σ_lt` = Standard deviation of supplier delivery lead time (e.g., transit delays from Gujarat or Maharashtra ports).""",
        "decision_algo": """### Step 1: Parameter Extraction from Live ERP
- Query annual consumption `D` from ERP production module.
- Query current unit purchase price `P` from active purchase contracts.
- Calculate ordering cost `S` and annual holding cost rate `H`.

### Step 2: Compute Base EOQ
- Run calculation: `EOQ = SQRT((2 × D × S) / H)`.
- Convert EOQ into standard commercial packaging units (e.g., 200 kg drums, 1,000 kg IBC totes, or 25 MT road tankers).

### Step 3: Evaluate Supplier Quantity Discounts
- IF supplier offers a price discount for ordering `Q_discount > EOQ`:
  - Calculate `TC(EOQ)` vs. `TC(Q_discount)` using the Total Cost equation.
  - IF Net Savings > Carrying Cost Increase: Accept discount order.
  - IF Net Savings < Carrying Cost Increase: Reject discount; maintain EOQ.

### Step 4: Calculate ROP and Set ERP Alerts
- Set automated ERP Purchase Requisition triggers when physically available inventory + in-transit stock <= ROP.
- Lock safety stock buffers against accidental manual overriding.""",
        "example1": """### Example 1: Titanium Dioxide (TiO2) Rutile Procurement Optimization
**Situation:** Swatch consumes 120,000 kg of TiO2 annually. Price is ₹280/kg. The procurement manager placed bi-weekly orders of 5,000 kg, incurring ₹4,500 in PO processing, sampling, and lab testing costs per order.
**Harris EOQ Applied:**
- D = 120,000 kg/year.
- S = ₹4,500 per order.
- H = 20% of ₹280 = ₹56/kg/year.
- `EOQ = SQRT((2 × 120,000 × 4,500) / 56) = SQRT(1,080,000,000 / 56) = 13,887 kg`.
- Adjusted to standard 1-pallet container size (approx 14 MT or 560 bags of 25 kg).
- Orders per year dropped from 24 orders to 8.6 orders.
- **Outcome:** Saved ₹62,000 in administrative ordering costs while keeping holding costs fully balanced.""",
        "example2": """### Example 2: Evaluating a Bulk Emulsion Supplier Discount
**Situation:** An emulsion supplier offered a 2.5% discount on Pure Acrylic Emulsion (₹140/kg base price) if Swatch ordered 40 MT (tanker load) instead of their standard 15 MT batch.
**Total Cost Analysis:**
- Annual demand: 90 MT (90,000 kg).
- Holding cost rate: 22% (emulsion has finite shelf-life and risks bacterial spoiling/skinning).
- Annual purchase savings from discount: 90,000 kg × ₹3.50 = ₹315,000.
- Extra holding cost of holding 40 MT vs. 15 MT: Average inventory increases by 12,500 kg × (₹136.50 × 0.22) = ₹375,375.
- Net Effect: The "attractive" discount would cause a **net loss of ₹60,375 per year** + elevated risk of polymer skinning in summer heat.
- **Decision:** Rejected the 40 MT bulk deal; maintained 15 MT orders.""",
        "failures": [
            ("The Discount Illusion", "Buying 6 months of raw materials to get a 2% rebate, tying up millions in cash.", "Always run Total Cost of Inventory (TCO) analysis including holding and capital costs."),
            ("Static Lead Time Fallacy", "Assuming supplier lead time is always 5 days when monsoon flooding delays trucks by 12 days.", "Incorporate lead-time variance (sigma_lt) into the Safety Stock equation."),
            ("Ignoring Shelf-Life Risk", "Applying standard EOQ to biocides or tinting colorants that expire in 180 days.", "Cap maximum order size at shelf-life expiration limit regardless of mathematical EOQ."),
            ("Separating Packaging from Chemicals", "Having 20 tonnes of paint ready in the kettle with zero empty 20L plastic buckets in stock.", "Synchronize packaging EOQ with paint batch scheduling.")
        ],
        "checklist": [
            "Annual holding cost rate (H%) accurately calibrated with Finance (Capital + Storage + Risk).",
            "EOQ calculated for all top 20 Class-A raw materials in ERP.",
            "Reorder Points (ROP) calibrated with supplier lead-time standard deviation.",
            "Supplier volume discount offers evaluated using full TCO equation before approval.",
            "Chemical shelf-life and storage temperature limits respected in batch sizing.",
            "Zero kettle production halts attributable to stockouts of active SKUs."
        ]
    },
    "joseph-orlicky-mrp-engine": {
        "title": "Joseph Orlicky Material Requirements Planning (MRP) & BOM Explosion Engine for Swatch Paints",
        "legend": "Joseph Orlicky (Pioneer of Computerized Material Requirements Planning & Author of 'Material Requirements Planning', 1975)",
        "description": "Joseph Orlicky Material Requirements Planning (MRP), Bill of Materials (BOM) Explosion, Time-Phased Component Netting, and Production Scheduling Engine for Swatch Paints.",
        "dept": "02_production_inventory",
        "tag": "joseph-orlicky",
        "purpose": """This skill equips the Swatch Paints Production Planning, Materials Management, and ERP Systems teams with Joseph Orlicky’s revolutionary disciplines of **Material Requirements Planning (MRP)**, **Bill of Materials (BOM) Explosion**, and **Time-Phased Component Netting**.

In a coatings manufacturing facility, finished products (e.g., 20L Swatch Rustic White or 4L Exterior Weather-Shield Gold) have *independent demand* driven by the market. However, raw materials (TiO2, Calcined Clay, Monomers, Thickeners, Preservatives) and packaging components (Tins, Pails, Handles, Labels, Corrugated Cartons) have **dependent demand** derived strictly from the production schedule. 

Treating dependent components as independent items leads to classic manufacturing chaos: a ₹5 Lakh batch of premium emulsion sits stranded in a blending kettle because a ₹4 plastic handle or 500 grams of biocide is missing from the godown.

The engine's purpose is to:
- Structure multi-level, precise **Bills of Materials (BOM)** for every paint SKU down to exact grams and milliliters.
- Explode the Master Production Schedule (MPS) into time-phased gross requirements and net component requirements.
- Calculate exact purchase order release dates by netting on-hand stock and work-in-progress (WIP) against supplier procurement lead times.
- Synchronize raw chemical dispensing with packaging line availability, guaranteeing zero line stoppages.""",
        "when_to_use": """- Translating monthly sales forecasts into weekly factory batch blending and packaging schedules.
- Exploding seasonal production requirements for festival pre-stocking (Diwali exterior painting rush).
- Introducing a new paint formulation or packaging redesign (managing BOM phase-in / phase-out to avoid obsolete packaging).
- A production line is frequently halted due to missing auxiliary components (lids, colorants, driers).
- Auditing inventory discrepancy between physical godown stock and ERP ledger records.
- Calculating capacity requirements planning (CRP) across sand mills, dispersers, and filling lines.""",
        "frameworks": """### 6.1 Orlicky's Fundamental Law of Dependent Demand
*"Demand for manufacturing components is calculated from the parent production schedule, never forecasted independently."*

In paint production, you forecast the market demand for 20L pails of Swatch Shine Emulsion. You NEVER forecast the demand for bucket handles or anti-settling agents; you *calculate* them by exploding the BOM.

### 6.2 The Multi-Level Coatings BOM Architecture
```
Level 0: Finished Goods SKU (e.g., 20L Swatch Rustic Texture White Pail)
  ├── Level 1: Bulk Paint Base Slurry (24.2 kg)
  │     ├── Level 2: Liquid Phase (Water, Glycol, Defoamer, Biocide)
  │     ├── Level 2: Pigment & Extender Grind (TiO2 Rutile, Dolomite, Silica 300 Mesh)
  │     └── Level 2: Let-Down Phase (Pure Acrylic Emulsion, Coalescing Solvent, HEC)
  └── Level 1: Packaging Assembly
        ├── Level 2: 20L HDPE Injection Molded Pail (Screen-Printed)
        ├── Level 2: Tamper-Proof Snap-Fit Lid with Gasket
        ├── Level 2: Galvanized Steel Handle with Plastic Grip
        └── Level 2: Barcode & Batch QR Loyalty Token Sticker
```

### 6.3 Time-Phased Component Netting Logic
For every component across discrete time buckets (Day / Week):
```
Net Requirements = Gross Requirements - (On-Hand Inventory + Scheduled Receipts) + Safety Stock
Planned Order Release = Net Requirements backward-scheduled by Component Lead Time
```
- If a solvent takes 7 days to arrive from Gujarat, and Kettle #3 requires it on Day 12, the MRP engine must generate the Purchase Order release precisely on **Day 5**.""",
        "decision_algo": """### Step 1: Master Production Schedule (MPS) Input
- Import finalized 14-day production plan from Sales & Operations Planning (S&OP).
- Verify formulation batch ticket sizes (e.g., 2,500 kg standard kettle batch).

### Step 2: BOM Explosion & Gross Requirements Calculation
- Explode parent SKUs into component level requirements down to Level 2.
- Multiply batch quantity by exact BOM recipe ratios (accounting for 1.2% normal process shrinkage/volatilization).

### Step 3: Component Netting
- Query real-time physical inventory from ERP Godown Ledger.
- Subtract allocated reservations for batches currently running in WIP.
- Determine Net Requirement:
  - IF Net Requirement > 0: Trigger Planned Order.
  - IF Net Requirement <= 0: No action needed.

### Step 4: Backward Scheduling & PO Release
- Subtract supplier lead time + inward QA testing time (e.g., 48 hours for raw material quarantine testing).
- Generate automated Purchase Requisitions with exact required dock arrival dates.""",
        "example1": """### Example 1: Preventing a Batch Stranding Crisis in Exterior Primer
**Situation:** A 10,000-litre run of Exterior Wall Primer was scheduled for Monday morning. The plant had 8 tonnes of polymer and 12 tonnes of extenders. However, when the kettle was charged, the supervisor found only 4 kg of in-can biocide (isothiazolinone) in stock; the formulation required 25 kg. The entire 10,000-litre batch was stranded, risking microbial contamination.
**Orlicky MRP Fix Applied:**
- Diagnosed root cause: Biocide was being ordered manually by the godown in-charge based on visual checks.
- Formally integrated Biocide into the Level-2 Master BOM.
- Automated MRP netting: ERP now schedules biocide orders 10 days before production based on MPS explosion.
- Zero stranded batches in 12 months; biocide inventory holding reduced by 30%.""",
        "example2": """### Example 2: Managing Packaging Phase-In for Swatch Rustic Rebranding
**Situation:** Marketing launched a newly designed 20L Swatch Rustic pail. The plant had 1,400 old pails in stock. If the new schedule ran blindly, the old pails would become scrap (loss of ₹2.8 Lakhs).
**MRP Phase-In Logic Applied:**
- Implemented an MRP "Effective Date / Lot Expiry" transition rule.
- Directed the MPS to consume exactly 1,400 units of the old packaging BOM on specific non-flagship runs before switching the active BOM to the new artwork code.
- Result: 100% of legacy packaging consumed with zero write-offs, achieving a seamless brand transition.""",
        "failures": [
            ("Unaccounted Evaporation / Shrinkage", "BOM assumes 100% yield, but solvent volatile losses cause material deficits.", "Include calibrated shrinkage factors (1-2%) in the chemical BOM explosion."),
            ("Phantom Inventory in ERP", "ERP says 500 kg of pigment is in godown, but physical stock is torn/ruined.", "Institute daily cycle counting to maintain 98%+ inventory record accuracy."),
            ("Lead-Time Complacency", "Assuming supplier lead time is fixed; ignoring port customs delays on imported rutile.", "Maintain dynamic lead-time tables updated with trailing 90-day vendor delivery realities."),
            ("BOM Recipe Drift", "Chemist changes formula on a paper ticket without updating the central ERP BOM.", "Hard system lock: Production cannot issue materials without an approved digital BOM revision.")
        ],
        "checklist": [
            "100% of manufactured paint SKUs have certified, multi-level digital BOMs in ERP.",
            "Raw materials and packaging components categorized strictly under Dependent Demand.",
            "Time-phased component netting executed daily across rolling 14-day MPS horizon.",
            "Lead times include supplier transit and mandatory inward laboratory QA testing.",
            "Cycle counting program enforces >98% physical-to-digital inventory accuracy.",
            "Zero batch delays caused by missing auxiliary raw materials or packaging components."
        ]
    },
    "masaaki-imai-kaizen-engine": {
        "title": "Masaaki Imai Kaizen & Gemba Continuous Improvement Engine for Swatch Paints",
        "legend": "Masaaki Imai (Father of Continuous Improvement, Founder of Kaizen Institute & Author of 'Gemba Kaizen')",
        "description": "Masaaki Imai Gemba Kaizen, 5S Workplace Organization, Muda (Waste) Elimination, and Daily Continuous Improvement Engine for Swatch Paints Factory Floor.",
        "dept": "02_production_inventory",
        "tag": "masaaki-imai",
        "purpose": """This skill equips the Swatch Paints Plant Management, Floor Supervisors, Maintenance Crews, and Operators with Masaaki Imai’s disciplines of **Gemba Kaizen**, **5S Visual Management**, and relentless daily elimination of operational waste (**Muda**).

In traditional Indian paint manufacturing plants, leadership manages from air-conditioned offices looking at delayed reports, while the factory floor (Gemba) suffers from chronic disorder: spilt dry pigment powders, misplaced wrenches causing 45-minute sand-mill setup delays, leaking solvent transfer hoses, and cluttered walkways. Managers believe that improvement requires massive capital expenditure on new automated European machinery, ignoring the thousands of low-cost, common-sense improvements available immediately.

The engine's purpose is to:
- Instill the **Gemba Philosophy**: Go to the real place, see the real product, talk to the real operators, and find the real facts.
- Enforce strict **5S Standards (Seiri, Seiton, Seiso, Seiketsu, Shitsuke)** across raw material godowns, grinding decks, mixing kettles, tinting labs, and packing docks.
- Systematically eliminate the **3 Ms: Muda (Waste), Muri (Overburden), and Mura (Unevenness)**.
- Empower front-line operators to submit and implement **Daily Kaizen Suggestions**, creating an unstoppable culture of micro-innovations.""",
        "when_to_use": """- High kettle changeover and cleaning downtime when switching from dark color batches to white base batches.
- High accident risk or safety violations: wet slippery floors, ungrounded solvent transfer barrels creating static fire hazards.
- Cluttered raw material godowns where workers waste 20+ minutes searching for specific pigment bags or additive tins.
- High equipment breakdown rate caused by poor daily cleaning and operator maintenance (TPM).
- Cultivating worker ownership and continuous improvement among plant operators and contract laborers.
- Preparing the factory for ISO 9001 / ISO 14001 certification or customer visual audits.""",
        "frameworks": """### 6.1 The Golden Rules of Gemba Management
1. When an abnormality occurs, **go to the Gemba first**. Do not debate theories in a conference room.
2. Check the **Gembutsu** (the physical equipment, paint slurry, batch ticket, spilled material).
3. Take **temporary countermeasures** on the spot to contain the issue.
4. Find the **root cause** by asking "Why?" five times at the machine face.
5. **Standardize** the solution to prevent recurrence.

### 6.2 The 5S Pillars for Coatings Plants
- **1. Seiri (Sort):** Separate necessary items from unnecessary items. Red-tag broken pallets, hardened pigment residues, obsolete colorant canisters, and scrap hoses. Remove them immediately.
- **2. Seiton (Set in Order):** A place for everything and everything in its place. Tool shadow boards for kettle maintenance wrenches; color-coded floor markings for raw material staging, WIP tanks, and finished pallets.
- **3. Seiso (Shine / Clean-as-Inspection):** Cleaning is not janitorial work; it is an act of inspection. While wiping down a high-speed disperser shaft, an operator detects a vibrating bearing or oil seal leak before it causes a catastrophic shutdown.
- **4. Seiketsu (Standardize):** Visual workplace rules. Standard fill level markings, photo-based SOPs displayed at eye level, and color-coded pipelines (Water = Blue, Solvent = Red, Resin = Yellow).
- **5. Shitsuke (Sustain / Discipline):** Daily 5-minute 5S routines at shift start and shift end. Weekly management Gemba walks with published scoring audits.

### 6.3 Eliminating the 3 Ms (Muda, Muri, Mura)
- **Muda (Waste):** Reworking off-spec batches, searching for tools, excess movement.
- **Muri (Overburden):** Forcing workers to manually lift 50 kg extender bags to kettle hoppers without mechanical hoists (causes physical fatigue and spilling).
- **Mura (Unevenness):** Running 3 kettles on Monday and 14 kettles on Friday; level the schedule.""",
        "decision_algo": """### Step 1: Daily 15-Minute Gemba Walk
- Plant Head and Production Supervisor walk the shop floor at 08:30 AM every day.
- Observe: Are raw material bags neatly stacked on pallets? Are disperser operators wearing PPE? Is there any powder dust leakage?

### Step 2: Red Tag Campaign Execution
- Conduct monthly Red Tag events:
  - Any item not used in the past 30 days receives a Red Tag.
  - If unclaimed within 7 days, scrap or relocate to central salvage.

### Step 3: Fast Changeover (SMED - Single Minute Exchange of Die)
- IF changeover from colored paint to white emulsion takes >60 minutes:
  - Video record the changeover.
  - Separate internal work (can only be done while kettle is stopped) from external work (can be done while previous batch is running, e.g., staging next batch raw materials).
  - Pre-wash rinsing lines using automated spray heads. Target changeover time: <25 minutes.

### Step 4: The Kaizen Teian (Suggestion) Board
- Install a simple visual Kaizen Board on the factory floor.
- Every operator who submits a implemented idea that saves 5 minutes or reduces waste receives public recognition and a monthly cash prize.""",
        "example1": """### Example 1: Slashing Kettle Washout Downtime by 65%
**Situation:** Switching Kettle #1 from dark brick-red exterior emulsion to white primer took 110 minutes of manual scrubbing with water hoses, producing 400 litres of contaminated effluent wash-water.
**Kaizen Team Action:**
- The Gemba team watched the cleaning process. Workers were using low-pressure domestic water hoses and handheld scrubbers.
- *Kaizen Improvements:*
  1. Installed a high-pressure 360-degree rotating spray nozzle inside the kettle lid (cost: ₹14,000).
  2. Scheduled batches by shade progression (White -> Off-White -> Pastel -> Medium -> Dark) to eliminate dark-to-white washouts whenever possible.
  3. Reused the final light rinse water as the base water for the next batch of the same dark shade.
- **Outcome:** Cleaning downtime slashed from 110 minutes to 28 minutes. Effluent waste reduced by 60%; plant output increased by 2 full batches per shift.""",
        "example2": """### Example 2: Eliminating Spilled Raw Material in Pigment Godown
**Situation:** In the pigment godown, workers manually slit open 25 kg bags of calcium carbonate and silica. Powder dust filled the air, and 2% to 3% of material was tracked across the floor as chalky dust, creating a slipping hazard and breathing irritation.
**Gemba Kaizen Applied:**
- Operator suggested building an enclosed bag-dump station with a localized dust extraction bag filter and integrated bag-slitting blade.
- Plant maintenance built the unit in-house using scrap sheet metal for under ₹35,000.
- Floor cleanliness improved 100%; dust-related operator coughing complaints dropped to zero; recovered 180 kg of clean raw powder every week that was previously swept into drains.""",
        "failures": [
            ("Office-Bound Leadership", "Plant managers reviewing operations via Excel dashboards while the floor is in chaos.", "Enforce the Gemba rule: spend at least 60 minutes daily physically on the shop floor."),
            ("5S as Spring Cleaning", "Cleaning up the plant once a year for an auditor's visit, then allowing filth to return.", "5S must be integrated into daily shift handovers as a permanent operating condition."),
            ("Ignoring Frontline Operator Ideas", "Engineers imposing complex top-down changes without asking the machine operators.", "Operators know the machine best; front-line Kaizen ideas have 90%+ success rates."),
            ("Accepting 'That's How We Do It Here'", "Tolerating leaking pipes and makeshift wire repairs as normal operations.", "Challenge the status quo relentlessly; every leak and loose bolt is a failure of standard work.")
        ],
        "checklist": [
            "Daily 15-minute Gemba walk conducted by plant leadership at shift start.",
            "5S visual organization standards audited weekly with published scores.",
            "Color-coded floor zoning strictly enforced for raw materials, WIP, and finished stock.",
            "Kettle changeover procedures optimized via SMED methodology.",
            "Visual Kaizen Suggestion Board active with operator submissions recognized monthly.",
            "Personal Protective Equipment (PPE) compliance at 100% across all hazardous zones."
        ]
    },
    "taiichi-ohno-production-planning-engine": {
        "title": "Taiichi Ohno Toyota Production System & Pull Scheduling Engine for Swatch Paints",
        "legend": "Taiichi Ohno (Father of Toyota Production System, Just-in-Time & Seven Wastes)",
        "description": "Taiichi Ohno Pull Production (Kanban), Eliminating the 7 Wastes (Muda), Takt Time, and Level Scheduling (Heijunka) Engine for Swatch Paints Manufacturing.",
        "dept": "02_production_inventory",
        "tag": "taiichi-ohno",
        "purpose": """This skill equips the Swatch Paints Production Operations, Factory Scheduling, and Supply Chain teams with Taiichi Ohno’s world-renowned **Toyota Production System (TPS)**: **Just-in-Time (JIT)**, **Pull Production (Kanban)**, and the systematic elimination of the **Seven Wastes (Muda)**.

Traditional paint factories operate on a destructive **Push System**: the factory produces massive, uncoordinated batches of whatever raw materials are easiest to grind, filling godowns with thousands of unsold pails of low-demand shades while fast-moving white base and primer stock out. This overproduction locks up working capital, clutters warehouse space, causes pail damage, and forces costly month-end discounting.

The engine's purpose is to:
- Convert the factory from a blind "Push" model to a market-synchronized **Pull System** triggered by dealer orders and depot replenishment signals.
- Institutionalize **Kanban Cards / Digital Signals** between depot staging, finished goods packaging, and bulk kettle blending.
- Eliminate the **Seven Classic Wastes**: Overproduction (the worst waste), Waiting, Transport, Inappropriate Processing, Excess Inventory, Unnecessary Motion, and Defects.
- Implement **Heijunka (Production Leveling)**: smoothing out seasonal and weekly batch schedules to avoid factory panic spikes and idle downtime.""",
        "when_to_use": """- Finished goods godowns are overflowing with slow-moving SKUs while top-selling SKUs face chronic stockouts.
- Transitioning the factory from large, speculative batch runs to flexible, responsive customer-demand batches.
- Slashing lead time from dealer order placement to dispatch from 5 days down to 24 hours.
- Resolving bottlenecks between bulk mixing kettles and automated packing/canning lines.
- Implementing Visual Kanban inventory control for fast-moving tinting bases (Base White 1, Base 2, Base 3).
- Leveling production runs across high-viscosity texture products (Swatch Rustic) and high-fluidity interior primers.""",
        "frameworks": """### 6.1 The Seven Wastes (Muda) in Coatings Manufacturing
Ohno identified Seven Deadly Wastes, with Overproduction as the mother of all wastes:
1. **Overproduction:** Making 5,000 litres of dark brown enamel before orders arrive, tying up resin and kettles.
2. **Inventory:** Godowns stacked 4 pallets high with finished paint buckets gathering dust.
3. **Waiting:** Packaging line operators standing idle while waiting for the QC lab to release the viscosity test.
4. **Transportation:** Moving paint drums three times between godown A, godown B, and the tinting shed.
5. **Over-Processing:** Grinding pigment slurry for 60 minutes when 35 minutes achieves the required Hegman 6 fineness.
6. **Motion:** Operators walking 40 meters across the plant floor to fetch a water hose or batch additive.
7. **Defects:** Off-shade or aerated paint batches that require rework, filtering, or disposal.

### 6.2 The Pull Production & Kanban Mechanism
In a Pull System, nothing is produced downstream until upstream signals consumption.
```
Dealer Buys 40 Pails from Depot --> Triggers Depot Kanban Signal 
  --> Finished Goods Warehouse releases 40 Pails 
  --> Packaging Line fills 40 Pails 
  --> Bulk Mixing Kettle blends 800 Litres of Base 
  --> Raw Material Godown dispenses raw ingredients.
```
- **Rule of Kanban:** No production order can be initiated without a physical or digital Kanban token authorizing it.

### 6.3 Takt Time & Heijunka (Leveling)
```
Takt Time = Available Operating Time per Shift / Customer Demand per Shift
```
If daily dealer demand across Rajasthan is 12,000 litres, and the plant runs two 8-hour shifts (960 gross minutes - 60 mins break = 900 operating minutes):
```
Takt Time = 54,000 seconds / 12,000 litres = 4.5 seconds per litre
```
The canning and blending lines must pace their cycle times to match this exact rhythm, neither faster (causes overproduction) nor slower (causes stockouts).""",
        "decision_algo": """### Step 1: Implement Finished Goods Kanban Bins
- Establish minimum/maximum buffer levels for the top 15 high-velocity SKUs:
  - Red Zone (Critical: Expedite immediate batch run).
  - Yellow Zone (Reorder Kanban Trigger: Schedule standard batch).
  - Green Zone (Adequate Stock: Zero production permitted).

### Step 2: Strict Ban on Overproduction
- IF a kettle finishes early:
  - The supervisor is FORBIDDEN from starting an unauthorized batch just to "keep workers busy."
  - Redeploy operators to 5S cleaning, autonomous maintenance, or operator training.

### Step 3: Implement Visual Management (Andon)
- Install Andon signal lights on packaging and disperser lines:
  - Green: Running normally at Takt pace.
  - Yellow: Minor material delay / approaching tolerance limit.
  - Red: Process defect or safety hazard; line stops immediately for root-cause resolution.

### Step 4: Level the Mix (Heijunka)
- Do NOT produce all monthly exterior emulsion in Week 1 and all primer in Week 2.
- Produce a mixed daily sequence: Run 4 batches of Primer, 2 batches of Emulsion, and 1 batch of Swatch Rustic every day to match continuous market pull.""",
        "example1": """### Example 1: Eliminating the Overproduction Trap in Enamel Paint
**Situation:** The production manager loved running 10,000-litre batches of synthetic enamel because "it maximizes machine efficiency." As a result, the plant accumulated ₹34 Lakhs of unsold gloss enamel that sat in the warehouse for 7 months, while dealers screamed for Swatch Shine Interior White.
**Ohno Pull System Applied:**
- Capped maximum batch size for slow-moving enamel at 2,000 litres, running strictly against confirmed distributor orders.
- Converted the main 10,000-litre kettle to fast-moving interior emulsion white base.
- Released ₹26 Lakhs in trapped working capital within 60 days.
- Warehouse floor space was liberated, eliminating the need to rent an external overflow godown.""",
        "example2": """### Example 2: Implementing Pail-Filling Kanban Line
**Situation:** The 20-litre packaging line frequently ran out of buckets midway through canning, leaving 4,000 litres of paint exposed to air in holding tanks, causing skin formation on the paint surface.
**TPS Kanban Solution:**
- Created a 2-bin physical Kanban square on the packaging floor holding exactly 2 pallets (96 pails) of labeled buckets.
- When the first pallet is emptied, the empty pallet flag triggers the warehouse forklift to immediately bring the replenishment pallet.
- Paint skinning losses dropped to zero; packaging line uptime increased by 22%.""",
        "failures": [
            ("The Machine Efficiency Fallacy", "Running large batches of unwanted product just to show 95% machine utilization.", "Ohno Rule: Producing something that does not sell is 100% waste. Efficiency without market pull is an illusion."),
            ("Breaking the Kanban Discipline", "Authorizing production batches without a customer or Kanban trigger because 'workers have nothing to do.'", "Enforce strict discipline: if there is no Kanban, stop the line and conduct maintenance or training."),
            ("Chaotic Batch Sequencing", "Running highly pigmented red paint followed immediately by white base, causing extreme cleaning delays.", "Establish standard Heijunka scheduling sequences from light to dark."),
            ("Ignoring Line Stoppages (Andon)", "Bypassing warning alarms on filling lines to hit end-of-shift volume counts.", "When the Andon lights red, stop and fix the problem immediately to prevent mass defects.")
        ],
        "checklist": [
            "Factory operated strictly on Pull signals (Kanban) from depot off-take.",
            "Overproduction eliminated; zero unscheduled batches authorized.",
            "Visual min/max Kanban zones established for all fast-moving tinting bases.",
            "Takt Time calculated and displayed on the factory floor.",
            "Heijunka mixed-model scheduling implemented to level daily production runs.",
            "Andon visual stop-the-line system active on all packaging and mixing lines."
        ]
    },
    "w-edwards-deming-quality-engine": {
        "title": "W. Edwards Deming Statistical Quality & System of Profound Knowledge Engine for Swatch Paints",
        "legend": "W. Edwards Deming (Father of Quality Revolution, 14 Points for Management & PDCA Cycle)",
        "description": "W. Edwards Deming Statistical Process Control (SPC), System of Profound Knowledge, Ceasing Reliance on Mass Inspection, and 14 Points Engine for Swatch Paints Operations.",
        "dept": "02_production_inventory",
        "tag": "w-edwards-deming",
        "purpose": """This skill equips the Swatch Paints Executive Leadership, Quality Assurance, and Plant Engineering teams with W. Edwards Deming’s revolutionary **System of Profound Knowledge**, the **14 Points for Management**, and rigorous **Statistical Process Control (SPC)**.

In conventional Indian manufacturing enterprises, quality is treated as a policing function: finished paint cans are inspected at the end of the line, and defective batches are blamed on "careless workers." Managers oscillate between blaming suppliers for raw material defects and firing workers for off-spec batches, completely failing to understand that **94% of quality problems belong to the system, not the individual worker**.

The engine's purpose is to:
- **Cease reliance on mass inspection** to achieve quality: build quality into the formulation, raw material control, and dispersion process from the very start.
- Differentiate between **Common Cause Variation** (inherent in the production system) and **Special Cause Variation** (external shocks), ending managerial tampering that actually increases batch variance.
- Drive the **PDCA (Plan-Do-Check-Act)** cycle across every department: formulation design, vendor qualification, depot dispatch, and dealer service.
- Break down departmental barriers between Production, Sales, and Procurement, uniting the enterprise under a single shared purpose of customer delight.""",
        "when_to_use": """- High variance in paint physical properties (viscosity, specific gravity, hiding power/opacity, scrub resistance).
- Formulating quality control policies that move away from end-of-line rejection toward in-process statistical capability.
- Management is reacting emotionally to daily metric fluctuations, tampering with machine settings and making batch variance worse.
- Resolving chronic blame wars between the Sales team (complaining about quality) and Plant Chemists (blaming application errors).
- Evaluating raw material vendor contracts based on total cost and relationship rather than lowest price tag.
- Instituting an enterprise culture of psychological safety, continuous training, and joy in work.""",
        "frameworks": """### 6.1 The System of Profound Knowledge (SoPK)
Deming stated that effective management requires four interconnected lenses:
1. **Appreciation for a System:** A paint plant is not a collection of independent silos; it is an interdependent network where purchasing affects dispersion, dispersion affects canning, and canning affects dealer trust.
2. **Knowledge about Variation:** Everything varies. Using SPC control charts (Upper and Lower Control Limits: UCL/LCL set at ±3 sigma) to know when to act and when to leave the system alone.
3. **Theory of Knowledge:** Rational prediction based on theory. Experience alone teaches nothing without a grounded theory of chemistry and rheology.
4. **Psychology:** People want to do good work. Fear-based management, ranking systems, and numerical quotas destroy pride in workmanship.

### 6.2 Common Causes vs. Special Causes of Variation
- **Common Cause Variation:** Inherent noise in the stable system (e.g., standard ±2 KU viscosity drift due to raw material lot tolerances). 
  - *Deming Warning:* If you adjust kettle settings in response to common cause noise, you are **Tampering**, which mathematically *doubles* the variance!
- **Special Cause Variation:** An external shock (e.g., cooling water pump failure, uncalibrated pH meter, adulterated solvent lot). 
  - *Action:* Identify and remove the special cause immediately.

### 6.3 The PDCA Cycle (Shewhart/Deming Cycle)
```
[PLAN]  --> Formulate hypothesis, define test parameters, predict outcome.
   |
[DO]    --> Execute the trial on a small scale (pilot kettle).
   |
[CHECK] --> Compare statistical results with prediction; identify deviations.
   |
[ACT]   --> Standardize the successful change or revise theory and repeat.
```

### 6.4 Selected Deming 14 Points for Swatch Paints
- **Point 3:** Cease reliance on inspection to achieve quality.
- **Point 4:** End the practice of awarding business on the basis of price tag alone. Move toward single suppliers for key materials (e.g., emulsions) to reduce incoming variation.
- **Point 8:** Drive out fear so that everyone may work effectively for the company.
- **Point 9:** Break down barriers between departments.""",
        "decision_algo": """### Step 1: Establish In-Process SPC Control Charts
- Deploy X-bar and R charts on core manufacturing metrics: Viscosity, Hegman Grind, and Delta E Color Deviation.
- Calculate statistical control limits (UCL / LCL) based on 25 baseline stable batches.

### Step 2: Separate Common Cause from Special Cause
- IF a batch metric falls within the UCL and LCL limits:
  - DO NOT tamper with kettle parameters. Accept as system common cause.
- IF a data point breaches the UCL/LCL boundary or exhibits a 7-point run in one direction:
  - STOP. This is a Special Cause. Halt production, identify the root cause, and resolve before continuing.

### Step 3: Shift from Lowest-Price Bidding to Total Cost
- Procurement is STRICTLY FORBIDDEN from switching chemical suppliers to save 1% on price tag without full PDCA laboratory and plant qualification.
- Incoming variation from cheap raw materials destroys multiples of savings on the factory floor.

### Step 4: Break Down Sales vs. Production Silos
- Hold joint weekly Quality Councils where Sales and Plant Chemists review customer feedback without blaming individuals.""",
        "example1": """### Example 1: Stopping Managerial Tampering on Paint Tinting Bases
**Situation:** In the tinting base line, the specification for Specific Gravity was 1.35 ± 0.03. Every time a batch tested at 1.37, the plant manager panicked and added water. The next batch tested at 1.32, so he added calcium carbonate. Batch variation exploded, and dealers complained of watery paint.
**Deming SPC Applied:**
- Plotted 30 historical batches on an X-bar control chart. The system was in statistical control between 1.33 and 1.37.
- Proved that the manager’s adjustments were textbook **Tampering** (The Funnel Experiment), artificially causing instability.
- Manager was instructed: *Keep your hands off the formula as long as points stay within control limits.*
- Result: Standard deviation dropped by 45%; batch consistency normalized instantly.""",
        "example2": """### Example 2: Ending Single-Bid Vendor Purchasing for Emulsion Resins
**Situation:** Procurement constantly switched acrylic emulsion vendors between 4 regional suppliers based on who offered the cheapest price per kg that week. The plant suffered constant foaming issues, settling, and unpredictable drying times.
**Deming Point 4 Applied:**
- Quantified total cost: The ₹2/kg price saving from cheap vendors was wiped out by ₹7/kg in antifoam additives, customer rework, and painter complaints.
- Selected one primary high-quality emulsion manufacturer. Negotiated a 12-month partnership contract based on mutual statistical quality and prompt delivery.
- Result: Raw material incoming variance dropped to near-zero; foaming defects disappeared from production.""",
        "failures": [
            ("Tampering with a Stable System", "Adjusting machine settings every time a batch deviates slightly from the exact target mean.", "Deming Rule: Never adjust a process that is in statistical control; address the fundamental system design instead."),
            ("Fear-Driven Quality Concealment", "Workers hiding off-spec batches or diluting them secretly because management punishes mistakes.", "Drive out fear. Quality defects are opportunities to improve system architecture."),
            ("Penny-Wise Vendor Churn", "Buying off-brand biocides or cheap pigments to save pennies, causing multi-lakh batch failures.", "Partner with verified, long-term suppliers committed to statistical process control."),
            ("End-of-Line Inspection Mentality", "Hiring 10 inspectors to catch bad paint at the loading dock instead of fixing grinding.", "Build quality into the dispersion and let-down processes; make inspection redundant.")
        ],
        "checklist": [
            "Statistical Process Control (SPC) charts deployed on all active kettle lines.",
            "Common cause vs. Special cause variation understood and distinguished by QC staff.",
            "Managerial tampering eliminated; process adjustments guided strictly by statistical rules.",
            "Raw material purchasing decisions based on Total Cost and quality consistency, not just price tag.",
            "PDCA cycles formally documented for all formulation and process revisions.",
            "Fear driven out of the workplace; front-line defect reporting welcomed without punishment."
        ]
    }
}

def generate_prod_skill(name, data):
    sections = [
        "---",
        f"name: {name}",
        f"description: {data['description']}",
        f"category: {data['dept']}",
        "author: Hermes, CEO of Swatch Paints",
        "version: 2.0.0",
        "last_updated: 2026-09-26",
        "---",
        "",
        f"# {data['title']}",
        "",
        "## 1. TITLE",
        "",
        f"**{data['title']}**",
        "",
        f"*{data['legend']} — Operationalized for Swatch Paints Enterprise Manufacturing Architecture.*",
        "",
        "---",
        "",
        "## 2. PURPOSE",
        "",
        data['purpose'],
        "",
        "---",
        "",
        "## 3. WHEN TO USE",
        "",
        data['when_to_use'],
        "",
        "---",
        "",
        "## 4. INPUTS REQUIRED",
        "",
        "Before invoking this engine, collect the following real-time inputs from live factory and ERP systems. Zero static assumptions or hardcoded parameters are permitted.",
        "",
        "### 4.1 Production & Quality Data Inputs",
        "",
        "| Input | Why It Matters | Live System Source |",
        "|---|---|---|",
        "| SKU Recipe & Formulation Master | Defines the baseline chemistry and raw material ratios | ERP Formulation Master |",
        "| Machine & Batch Logs | Records real-time cycle times, temperatures, and shear RPM | SCADA / Line Operator Logs |",
        "| Laboratory QC Test Records | Viscosity, fineness of grind, gloss, opacity, Delta E | LIMS / Quality Module |",
        "| Inventory Ledger (Raw & WIP) | Exact on-hand chemical kilograms and work-in-progress | Live ERP Inventory Module |",
        "",
        "### 4.2 Financial & Operational Guardrails",
        "",
        "| Guardrail | Enforcement Rule | Authority |",
        "|---|---|---|",
        "| Process Capability Floor (Cpk) | Cpk must be maintained at >= 1.33 on critical parameters | QA Director / CEO Office |",
        "| Zero Uncertified Formula Edits | No chemist may alter batch recipes on the floor | Technical Director Sign-off |",
        "| Dynamic Cost Accounting | Raw material costs pulled dynamically from live ledger | Finance & Costing Dept |",
        "",
        "---",
        "",
        "## 5. DIAGNOSTIC QUESTIONS",
        "",
        f"Apply these 10 diagnostic inquiries before taking manufacturing or inventory action under the {name} framework:",
        "",
        "1. What is the fundamental operational constraint or source of variation in this process?",
        "2. Are we addressing a common cause inherent to the system, or a special cause external event?",
        "3. Is this action driven by real customer demand (Pull), or are we pushing unneeded inventory into the warehouse?",
        "4. Have we checked the physical Gemba and verified the facts with the frontline operators?",
        "5. What is the process capability (Cpk) or statistical control limit of the parameters involved?",
        "6. Are we tampering with a stable process and inadvertently increasing batch variance?",
        "7. Does our Bill of Materials (BOM) accurately reflect reality, including normal shrinkage and volatile losses?",
        "8. Are raw material procurement decisions optimizing Total Cost of Ownership rather than naive unit price tags?",
        "9. What are the leading indicators that will alert us to process drift before an off-spec batch is produced?",
        "10. Have we mistake-proofed (Poka-Yoke) the workflow to prevent recurrence of this defect?",
        "",
        "---",
        "",
        "## 6. CORE FRAMEWORKS",
        "",
        data['frameworks'],
        "",
        "---",
        "",
        "## 7. DECISION ALGORITHM",
        "",
        data['decision_algo'],
        "",
        "---",
        "",
        "## 8. OUTPUT STRUCTURE",
        "",
        "Every standard operating procedure, batch improvement directive, or inventory protocol must follow this standardized schema:",
        "",
        "```markdown",
        f"# Swatch Paints Technical Operations Directive: {data['title']}",
        "",
        "### 1. Operational Scope & Objective",
        "- **Target Line / Unit:** [Plant / Kettle / Packaging Line / Godown]",
        "- **Lead Engineer:** [Designation & Name]",
        "- **Target Parameter:** [CTQ Metric / Inventory Horizon / Waste Category]",
        "- **Standard Operating Baseline:** [Quantified metric before intervention]",
        "",
        "### 2. Methodological Intervention",
        "- **Root Cause Analysis (Gemba / 5-Why / SPC):** [Diagnostic evidence]",
        "- **Actionable Protocol:** [Specific process or scheduling change]",
        "- **Visual & Mistake-Proofing Control:** [Poka-Yoke / Kanban / 5S standard]",
        "",
        "### 3. Risk & Quality Guardrails",
        "- **Process Capability Target (Cpk):** [Minimum acceptable statistical floor]",
        "- **Safety & Environmental Compliance:** [Solvent handling / effluent standard]",
        "- **Rollback Trigger:** [Condition requiring immediate process halt]",
        "",
        "### 4. Governance & Cadence",
        "- **Shift Audit Cadence:** [Daily / Weekly inspection frequency]",
        "- **Owner of Control Chart:** [Named QC Chemist / Line Supervisor]",
        "- **Monthly Review:** [Review with Technical Director & CEO Office]",
        "```",
        "",
        "---",
        "",
        "## 9. REAL-WORLD INDIAN PAINT FIELD EXAMPLES",
        "",
        data['example1'],
        "",
        "---",
        "",
        data['example2'],
        "",
        "---",
        "",
        "## 10. FAILURE MODES",
        "",
        "Watch for these recurring manufacturing and inventory failure modes:",
        "",
        "| Failure Mode | Warning Signs | Prescribed Counter-Measure |",
        "|---|---|---|",
    ]
    for fm, symp, fix in data['failures']:
        sections.append(f"| **{fm}** | {symp} | {fix} |")
    
    sections.extend([
        "",
        "---",
        "",
        "## 11. CHECKLIST",
        "",
        "Before finalizing or launching any manufacturing protocol under this skill, verify:",
        ""
    ])
    for item in data['checklist']:
        sections.append(f"- [ ] {item}")
        
    sections.extend([
        "",
        "---",
        "",
        f"**CEO Directive:** At Swatch Paints, manufacturing excellence is the bedrock of our commercial reputation. We do not tolerate careless batch variation, uncalibrated instruments, or messy plant floors. Every chemist, supervisor, and line operator must execute the disciplines of {data['legend']} to the letter, building world-class quality and lean precision into every single litre of paint we produce."
    ])
    return "\n".join(sections)

def main():
    for name, data in PROD_SKILLS.items():
        content = generate_prod_skill(name, data)
        target_ws = os.path.join(WORKSPACE_DIR, "skills", "swatch-paints", data["dept"], name, "SKILL.md")
        target_hm = os.path.join(HERMES_DIR, "skills", "swatch-paints", data["dept"], name, "SKILL.md")
        
        os.makedirs(os.path.dirname(target_ws), exist_ok=True)
        os.makedirs(os.path.dirname(target_hm), exist_ok=True)
        
        with open(target_ws, "w", encoding="utf-8") as f:
            f.write(content)
        with open(target_hm, "w", encoding="utf-8") as f:
            f.write(content)
            
        lines = len(content.splitlines())
        size = len(content.encode("utf-8"))
        print(f"Generated {name:40s} | {lines:3d} lines | {size:5d} bytes")

if __name__ == "__main__":
    main()
