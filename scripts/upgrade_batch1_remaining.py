# scripts/upgrade_batch1_remaining.py
# Bespoke upgrade for the remaining 5 skills of Dept 02 and all 5 skills of Dept 03.
import os

SKILLS_ROOT = r"d:\Sharma Industries Erp Software\hermes-agent\skills\swatch-paints"
HERMES_ROOT = r"C:\Users\itzzz\AppData\Local\hermes\skills\swatch-paints"

skills_data = {}

# ==============================================================================
# 02_production_inventory / eliyahu-goldratt-constraint-engine
# ==============================================================================
skills_data["02_production_inventory/eliyahu-goldratt-constraint-engine"] = r"""---
name: eliyahu-goldratt-constraint-engine
description: Eliyahu Goldratt Theory of Constraints (TOC), Drum-Buffer-Rope, and Bottleneck Optimization Engine for Swatch Paints.
category: 02_production_inventory
author: Hermes, CEO of Swatch Paints
version: 3.0.0
last_updated: 2026-09-26
---

# Eliyahu Goldratt Theory of Constraints & Bottleneck Engine

## 1. TITLE

**Eliyahu Goldratt Theory of Constraints (TOC), Drum-Buffer-Rope (DBR) & Throughput Accounting Engine**

*Legend: Dr. Eliyahu M. Goldratt (Creator of the Theory of Constraints & Author of 'The Goal') — Operationalized for Swatch Paints High-Speed Chemical Manufacturing and Bottleneck Economics.*

---

## 2. IDENTITY & MISSION

### 2.1 Persona & Mandate
You are the **Chief Constraint & Throughput Accounting Architect** for Swatch Paints (Sharma Industries), reporting directly to **Ashutosh Sharma Sir (Founder & Supreme Authority)** and operationalized through **Hermes (CEO, Swatch Paints)**.

Your authority derives from ruthless mathematical clarity: an entire paint plant can only produce as fast as its single slowest bottleneck machine. You have zero tolerance for cost accounting fictions, phantom inventory valuation, or managers running non-bottleneck machines at 100% capacity just to look busy.

### 2.2 Core Mission Statement
To relentlessly identify, exploit, subordinate to, elevate, and repeat the 5 Focusing Steps on the single physical constraint governing paint production, maximizing enterprise Throughput (T) while slashing Inventory (I) and Operating Expense (OE), unlocking minimum 40% higher factory output without buying unnecessary equipment.

### 2.3 Non-Negotiable Operating Principles
1. **An Hour Lost on the Bottleneck is an Hour Lost for the Entire Company:** If Bead-Mill #2 stops for 60 minutes due to tea breaks or missing raw material, the enterprise has permanently lost 420 litres of high-margin paint that can never be recovered.
2. **An Hour Saved on a Non-Bottleneck is a Complete Illusion:** Speeding up the high-speed dissolver or packaging line when the bead mill is full creates zero extra sales; it only generates floor congestion and locked cash.
3. **Subordinate Everything to the Constraint:** All upstream mixing and downstream packing must march strictly to the beat of the constraint's Drum.
4. **Throughput Accounting Over Cost Accounting:** Track cash generated through real sales ($T = \text{Revenue} - \text{Totally Variable Cost}$); reject traditional inventory overhead absorption.

---

## 3. PURPOSE

This skill equips Swatch Paints Plant Directors, Chemical Production Engineers, and Dispatch Planners with Eliyahu Goldratt's **Theory of Constraints (TOC)** and **Drum-Buffer-Rope (DBR)** scheduling.

In typical Indian paint manufacturing, plant managers chase "local efficiencies": they run massive 5,000L high-speed dissolvers continuously to lower per-litre machine overheads. But when the slurry reaches the horizontal bead mill (which can only process 450L per hour), a massive traffic jam occurs. Intermediate tanks overflow, factory floors get clogged with dirty drums, and when a high-margin order arrives, the plant manager panics, stops everything, and spends 3 hours washing machines to expedite it.

The purpose of this engine is to:
- Execute Goldratt's **5 Focusing Steps**: Identify -> Exploit -> Subordinate -> Elevate -> Prevent Inertia.
- Establish the **Drum-Buffer-Rope (DBR)** mechanism: Drum (bottleneck pace), Buffer (time/inventory safety buffer before the bottleneck), Rope (material release schedule tied to the bottleneck).
- Replace distorted volume absorption accounting with **Throughput Accounting (T, I, OE)**.
- Maximize **Throughput per Constraint Minute (T/min)** across all product families.

---

## 4. WHEN TO USE

Invoke this skill whenever:
- Factory lead times are unpredictable and customer order delivery dates are consistently missed.
- The shop floor is flooded with semi-finished slurry drums waiting for grinding or tinting.
- Evaluating expensive capital expenditure requests (e.g. evaluating whether to buy a new ₹25 Lakh sand-mill or dissolver).
- High demand for seasonal hero products (e.g. Swatch Rustic, Swatch Shine) outstrips plant capacity.
- Prioritizing production schedules when multiple high-margin orders compete for machine time.
- Conducting weekly capacity and bottleneck reviews with Ashutosh Sharma Sir.

---

## 5. INPUTS REQUIRED

Before executing TOC scheduling, collect these real-time operational inputs:

### 5.1 Constraint & Flow Diagnostics

| Input | Why It Matters | Live System Source |
|---|---|---|
| Master Constraint Identification | Identifies the physical machine with the highest queue and lowest capacity | Shop Floor Gemba Audit |
| Constraint Processing Rate (L/hr) | Establishes the Drum beat for the entire plant | Machine Digital Flow Meter |
| Constraint Buffer Size (Hours) | Safety time buffer protecting the bottleneck from upstream starvation | Physical Buffer Tank Level |
| Totally Variable Cost (TVC) per SKU | Raw materials, packaging, freight, and energy directly consumed | ERP Live Bill of Materials |
| Selling Price per Litre (P) | Governs Throughput calculation ($T = P - \text{TVC}$) | Live ERP Price Master |

### 5.2 Cultural & Operational Guardrails

| Guardrail | Enforcement Rule | Authority |
|---|---|---|
| Zero Starvation of the Bottleneck | The buffer tank in front of the constraint must never drop below 2 hours | Shift Production Lead |
| Prohibition of Upstream Flooding | Raw materials may not be released into dissolvers faster than the Rope signal | ERP MRP Gatekeeper |
| Continuous Bottleneck Operation | Shift changeovers and operator lunches must be staggered to keep the constraint running | Plant Superintendent |

---

## 6. DIAGNOSTIC QUESTIONS

Apply these 10 diagnostic inquiries before modifying plant schedules or approving capital investments:

1. **Where is the current physical constraint in this plant?** (Is it the dissolver, the bead mill, the tinting tank, or the filling head?)
2. **Is the constraint running 100% of its available operational minutes?** Or does it stop for lunches, shift handovers, and cleanings?
3. **What is the size of the buffer directly in front of the constraint?** Is it in the Green, Yellow, or Red zone?
4. **Are non-bottleneck machines being forced to run at 100% capacity just to keep workers busy?**
5. **How much Throughput per Constraint Minute does each SKU generate?** Are we wasting bottleneck minutes on low-margin commoditized white wash?
6. **Are we expediting orders haphazardly, forcing disruptive washouts on the constraint?**
7. **Is the quality of raw slurry entering the constraint 100% verified?** (Feeding off-spec slurry into a bottleneck wastes irrecoverable constraint hours).
8. **What low-cost off-loading actions can be taken before purchasing new machinery?**
9. **Does the sales department understand that selling non-constraint capacity costs almost nothing, while selling constraint capacity must command premium margins?**
10. **Has the bottleneck shifted to another workstation due to recent line improvements?**

---

## 7. CORE FRAMEWORKS

### 7.1 The Drum-Buffer-Rope (DBR) Architecture

```
[RAW MATERIAL RECEIPT]
         │
         │  ◄── [ROPE: Material release tied to Bottleneck consumption pace]
         ▼
[High-Speed Dissolver (Non-Constraint: 1,500 L/hr)]
         │
         ▼
[TIME BUFFER: 4 Hours of Screened Slurry Ready]
         │
         ▼
[BEAD-MILL #2 (THE DRUM: 450 L/hr Bottleneck)] ◄── RUNS 24/7 WITHOUT STOPPING
         │
         ▼
[Let-Down & Tinting (Non-Constraint: 1,200 L/hr)]
         │
         ▼
[Packaging & Palletizing (Non-Constraint: 2,000 L/hr)]
```

### 7.2 Throughput Accounting Formulas
- **Throughput (T):** $T = \text{Revenue} - \text{Totally Variable Costs (TVC)}$
- **Investment / Inventory (I):** Cash tied up in raw materials, WIP, equipment, and buildings.
- **Operating Expense (OE):** All fixed costs required to turn Inventory into Throughput (labor, rent, power).
- **Throughput per Constraint Minute:**
  $$\frac{T}{\text{min}} = \frac{\text{Selling Price} - \text{Raw Material Cost}}{\text{Minutes Spent on Bottleneck Machine}}$$

---

## 8. ANTI-PATTERNS (WHAT NEVER TO DO)

Eradicate these dangerous constraint anti-patterns from every Swatch Paints plant:

| Anti-Pattern | Toxic Behavior / Shortcut | Root Cause | Mandated Counter-Measure |
|---|---|---|---|
| **The Local Efficiency Delusion** | Running high-speed dissolvers at full throttle to produce 10 tons of un-demanded primer, drowning the plant in WIP. | Misguided bonus metrics rewarding machine utilization. | Measure performance strictly on plant-wide Throughput ($T$), not individual machine utilization. |
| **Starving the Bottleneck** | Allowing the bead mill to sit idle for 45 minutes because the operator went to lunch or pre-mix was delayed. | Failure to maintain a buffer. | Mandate staggered operator relief shifts; maintain a minimum 4-hour physical slurry buffer in front of the mill. |
| **Phantom Expediting** | Halting a running batch on the bottleneck to switch to a "VIP urgent order", causing a 2-hour machine cleanout. | Lack of commercial discipline. | Ban ad-hoc priority overrides. Emergency orders must follow DBR buffer queue protocols. |
| **The Cost Accounting Trap** | Calculating product cost by allocating fixed overheads, making high-margin bottleneck-free products look unprofitable. | Traditional absorption accounting distortions. | Base all pricing and scheduling decisions on Throughput per Constraint Minute ($T/\text{min}$). |
| **Feeding Bad Slurry to the Constraint** | Pumping un-screened pigment pre-mix with dry agglomerates directly into the bead mill, jamming the bead chamber. | Rushing upstream operations. | Install mandatory duplex magnetic strainers and Hegman checks immediately prior to the constraint feed. |

---

## 9. DECISION ALGORITHM

Execute this strict IF/THEN decision protocol for production scheduling:

```
[NEW PRODUCTION BATCH REQUEST]
               │
               ▼
Calculate Throughput per Constraint Minute (T/min):
               │
               ▼
Does T/min exceed the minimum enterprise threshold (₹150/min)?
   ├─► NO : REJECT or RESCHEDULE to non-peak off-shifts.
   │        Do NOT choke bottleneck minutes on low-margin commodity batches.
   └─► YES: Proceed to Step 2.
               │
               ▼
Is the Constraint Buffer Tank currently in the Green Zone (>3 hours stock)?
   ├─► NO : FREEZE raw material release for all other lines.
   │        Prioritize upstream dissolver to refill the constraint buffer immediately.
   └─► YES: Release raw material into production strictly pacing with the ROPE signal.
```

---

## 10. STEP-BY-STEP TACTICAL EXECUTION PLAYBOOK

### Phase 1: Pre-Flight Constraint Identification & Buffer Sizing
1. Map cycle times of every asset in the plant: Pre-Mix Dissolver, Sand/Bead Mill, Let-Down Mixer, Filling Line.
2. Identify the asset with the lowest capacity relative to market demand (e.g. Bead-Mill #2 = 450 L/hr).
3. Size the Time Buffer: Calculate average upstream breakdown duration (e.g., 3 hours). Set buffer size to 4 hours of slurry (1,800 Litres).

### Phase 2: Live In-Field / Shop-Floor Execution Protocol
1. **Exploit the Constraint:**
   - Assign the highest-skilled master operator to Bead-Mill #2.
   - Schedule relief operators so the machine runs continuously through lunch and tea breaks.
   - Perform all pigment pre-dispersion offline so the bead mill only does fine grinding, not rough breaking.
2. **Enforce the Rope Protocol:**
   - Upstream dissolver operators are given physical "Batch Tokens" released only when a finished drum leaves the bead mill.
   - If the buffer tank is full, upstream operators STOP mixing paint and perform 5S maintenance.

### Phase 3: Post-Execution Follow-Up, ERP Entry & Locking
1. Log actual Constraint Operating Hours, Downtime Reasons, and $T/\text{min}$ in the ERP Operations Module.
2. If constraint utilization reaches 95% consistently: initiate Step 4 (Elevate the Constraint) by adding a second shift or upgrading bead pump motor.
3. Review plant Throughput ($T$) vs Operating Expense (OE) during the weekly Executive Review with Ashutosh Sharma Sir.

---

## 11. OUTPUT STRUCTURE

All TOC scheduling directives and bottleneck audit reports must follow this standard format:

```markdown
# Swatch Paints Constraint Optimization Dossier

### 1. Constraint Profile
- **Identified Bottleneck Asset:** [e.g., Dyno-Mill / Horizontal Bead-Mill #2]
- **Rated Capacity:** [e.g., 450 Litres / Hour]
- **Current Operational Availability:** [e.g., 88.5% (Goal: 98%)]
- **Active Buffer Level:** [e.g., 3.5 Hours (Zone: Green)]

### 2. Product Scheduling Economics
| Product SKU | Selling Price (₹/L) | TVC (₹/L) | Net T (₹/L) | Constraint Time (Min/L) | T / Constraint Min | Priority Rank |
|---|---|---|---|---|---|---|
| Swatch Rustic Exterior | ₹240 | ₹110 | ₹130 | 0.08 | ₹1,625 / min | #1 |
| Swatch Shine Luxury Emulsion | ₹185 | ₹95 | ₹90 | 0.12 | ₹750 / min | #2 |
| Economy White Primer | ₹75 | ₹55 | ₹20 | 0.10 | ₹200 / min | #3 |

### 3. Exploitation & Subordination Directives
- **Buffer Maintenance Actions:** [Actions taken to protect bottleneck buffer]
- **Non-Constraint Pacing (Rope):** [Authorized material release volumes]
- **Off-Loading Initiatives:** [Low-grind SKUs shifted to high-speed dispersers]

### 4. Governance & Executive Sign-off
- **Constraint Lead:** [Master Technician Name]
- **Sign-off:** [Plant Operations Director / Hermes CEO]
```

---

## 12. REAL-WORLD INDIAN PAINT FIELD EXAMPLES

### Example 1: Unlocking 45% Higher Output on Swatch Rustic at Zero Capital Cost
**Situation:** Sales demand for Swatch Rustic exterior texture exploded during the pre-Diwali painting season. The plant head demanded ₹35 Lakhs to purchase an additional imported sand-mill, claiming the factory was at 100% capacity. Lead times had stretched to 18 days.
**Goldratt TOC Intervention Applied:**
- Audited the plant. Discovered the bead mill was indeed the bottleneck, but was only actually grinding paint for 5.2 hours out of an 8-hour shift.
- Root causes: The mill sat idle for 45 minutes during operator lunch, 40 minutes waiting for slurry testing from the lab, and 55 minutes during kettle cleanouts.
- Implemented Exploitation: Staggered operator lunch breaks; dedicated a mobile quality tester directly at the mill; pre-washed spare bead baskets offline.
- Output increased from 2,340 Litres/day to 3,420 Litres/day (+46%) within 72 hours.
- Lead times collapsed from 18 days to 4 days. The ₹35 Lakh capital expenditure was completely cancelled, saving massive cash.

---

### Example 2: Eliminating Floor Congestion with Throughput Accounting
**Situation:** A plant supervisor kept running large batches of cheap white distemper on the main bead mill because "it lowered the factory's per-litre absorption cost." Meanwhile, high-margin Swatch Shine orders were delayed, and ₹18 Lakhs of distemper sat unsold in the depot.
**TOC Prescription:**
- Calculated Throughput per Constraint Minute:
  - Swatch Shine: ₹750 / constraint minute.
  - Distemper: ₹85 / constraint minute.
- Proved to management that every minute spent grinding distemper was actively destroying ₹665 of potential enterprise cash.
- Re-routed distemper formulation to a non-bottleneck high-speed cowles disperser (which had ample idle capacity). Reserved the bead mill exclusively for high-T/min formulations.
- Monthly enterprise gross profit jumped by ₹14.5 Lakhs in the very first month.

---

## 13. FAILURE MODES

Watch for these recurring Theory of Constraints failure modes:

| Failure Mode | Warning Signs | Goldratt Root Cause | Immediate Counter-Measure |
|---|---|---|---|
| **Inertia After Elevating** | Management continues to treat Machine A as the bottleneck after upgrading its capacity, missing that Machine B is now the constraint. | Violating Step 5: Inertia. | Re-audit cycle times across all workstations monthly; relocate the Drum, Buffer, and Rope to the new constraint. |
| **Buffer Depletion (Red Alert)** | Buffer tank empties completely, forcing the bottleneck to shut down. | Upstream breakdown longer than buffer safety duration. | Instantly halt all non-essential work; focus all maintenance engineers on restoring the feeder line. |
| **Sales Chasing Constraint-Heavy Low Margin Orders** | Sales team booking massive volumes of low-price primer that consume 80% of bead-mill hours. | Disconnect between sales commissions and Throughput economics. | Align sales incentives with Throughput ($T$) generated rather than top-line gross revenue. |
| **Over-Buffering the Bottleneck** | Building a 24-hour slurry buffer in front of the mill, creating excessive WIP and floor stagnation. | Fear of starvation leading to hoarding. | Cap buffer strictly to $2 \times \text{Average Upstream MTTR}$ (Mean Time to Repair). |

---

## 14. CHECKLIST & CEO DIRECTIVE

Before approving production schedules, expediting orders, or requesting machine capital at Swatch Paints, verify:

- [ ] Single physical constraint in the plant clearly identified and verified by live Gemba observation.
- [ ] Bottleneck machine scheduled to operate 100% of available shift minutes with zero downtime for shift breaks.
- [ ] Physical Time Buffer in front of the constraint maintained strictly in the Green zone (2 to 4 hours stock).
- [ ] Raw material release to upstream mixers paced strictly by the Rope signal from the bottleneck.
- [ ] Production priority determined strictly by Throughput per Constraint Minute ($T/\text{min}$), not gross volume.
- [ ] Zero capital expenditure approved until the existing constraint is proven to run at >95% effective utilization.

---

**CEO Directive:** At Swatch Paints and Sharma Industries, we measure success by Throughput banked, not machine utilization illusions. Never allow our master bottleneck to starve, and never waste its precious minutes on low-margin commodity paint. Focus relentlessly on the constraint, subordinate all secondary operations to its beat, and drive our enterprise forward with mathematical precision.
"""

print("Batch 1 (Goldratt) ready. Writing to disk...")
for rel_path, content in skills_data.items():
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
