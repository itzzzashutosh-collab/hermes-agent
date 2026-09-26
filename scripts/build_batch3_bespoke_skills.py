"""
Bespoke Skill Generator for Batch 3 (Curated, Deep & Production-Grade)
Transforms selected high-value external skills into Swatch Paints (Sharma Industries)
operational playbooks for Hermes Agent.
"""
import os
import sys

def build_batch3_skills():
    ws_base = r"d:\Sharma Industries Erp Software\hermes-agent\skills"
    app_base = r"C:\Users\itzzz\AppData\Local\hermes\skills"
    
    skills = {}
    
    # =========================================================================
    # SKILL 1: PORTER-STRATEGY
    # =========================================================================
    skills["porter-strategy"] = """---
name: porter-strategy
description: Michael Porter's Five Forces Strategic Industry Analysis Engine tailored for the Indian Paint & Coatings manufacturing and distribution sector. Use when evaluating competitive rivalry against multinational giants (Asian Paints, Berger, Nerolac, Indigo), mitigating raw material chemical supplier leverage, neutralizing dealer buyer bargaining power in Tier 2/3 Mandis, building defensible moats against new entrants, and countering low-cost substitutes (lime wash, exterior cladding, unorganized distempers). Integrates directly with Swatch Paints (Sharma Industries) executive commercial strategy.
metadata:
  version: 2.0.0
  author: Sharma Industries & Hermes Executive Strategy
  category: Corporate Strategy & Market Analysis
---

# Porter's Five Forces Strategic Engine - Indian Paint & Coatings Industry

## 1. Executive Authority & Strategic Mandate
This strategic engine provides institutional market structure analysis for **Sharma Industries (Swatch Paints)**, operating under the supreme executive authority of **Founder & Managing Director Ashutosh Sharma Sir** and executed autonomously by **Hermes (Chief Executive Operating Agent)**.

In the Indian decorative and industrial coatings landscape, strategic victory is not achieved through brute advertising spend—multinational incumbents (Asian Paints, Berger, Kansai Nerolac) spend hundreds of crores on celebrity endorsements and tinting machine lock-ins. Instead, Sharma Industries wins by identifying structural industry asymmetries across Porter's Five Forces and ruthlessly exploiting margin, logistics, and dealer-contractor alignment moats in Tier 2, 3, and rural mandis.

---

## 2. Porter's Five Forces: Indian Coatings Landscape

```
                        +------------------------------------+
                        |       Threat of New Entrants       |
                        | (High Capex, Tinting Machine Moat, |
                        |      Distribution Network Inertia)  |
                        +-----------------+------------------+
                                          |
                                          v
+-----------------------+       +-------------------+       +-----------------------+
|  Supplier Bargaining  |       | Industry Rivalry  |       |   Buyer Bargaining    |
|         Power         | ----> |  (Asian Paints,   | <---- |         Power         |
| (Crude Derivatives,   |       | Berger, Nerolac,  |       |  (Dealer Cartels,     |
| Monomers, TiO2)       |       |  Swatch Paints)   |       |  Credit Terms 60-90d) |
+-----------------------+       +-------------------+       +-----------------------+
                                          ^
                                          |
                        +-----------------+------------------+
                        |       Threat of Substitutes        |
                        | (Lime Wash, Wall Putty Topcoats,   |
                        |  Ceramic Cladding, PVC Wallpapers) |
                        +------------------------------------+
```

---

## 3. Deep Analysis of the Five Competitive Forces

### Force 1: Industry Rivalry (Very High)
- **Incumbent Dominance**: The "Big Four" control over 65% of the organized decorative paint market through aggressive tinting machine deployment, heavy TV advertising, and bundled dealer schemes.
- **Switching Costs**: Dealers face high cognitive switching costs due to existing automated tinting machines tied to incumbent proprietary colorants and software.
- **Price Competition**: Incumbents frequently initiate tactical price cuts on base whites and distempers while extracting super-profits on high-end luxury emulsions and specialty primers.
- **Sharma Industries Defense**: 
  - Compete on **Dealer Return on Capital Employed (ROCE)** rather than TV ad spend. Offer 18-22% gross counter margin vs. MNCs' 6-8%.
  - Universal colorant compatibility eliminating proprietary tinting lock-in.

### Force 2: Bargaining Power of Suppliers (Moderate to High)
- **Key Raw Materials**: Titanium Dioxide (TiO2), Pure Acrylic Emulsions, VAM (Vinyl Acetate Monomer), Extenders (Calcium Carbonate, Talc), Biocides, and Packaging Tins.
- **Market Structure**: Crude-oil linked monomers and imported TiO2 are controlled by global and national chemical conglomerates (e.g., Reliance, Chemours, Tronox).
- **Supply Shocks**: Sudden crude price spikes or rupee depreciation directly inflate raw material costs.
- **Sharma Industries Defense**:
  - In-house resin formulation capabilities and local supplier hedging.
  - Backward integration into high-grade water-based binder manufacturing at the Kota facility.
  - Multi-sourcing agreements for extenders across Rajasthan's mineral belts (Makrana, Udaipur).

### Force 3: Bargaining Power of Buyers / Dealers (High)
- **Mandi Dynamics**: Paint dealers operate from traditional "gaddis" in key trade hubs (Kota, Bhilwara, Jaipur, Indore). They hold immense power over brand recommendations to walk-in consumers.
- **Credit Exposure**: Dealers routinely demand 60 to 90 days credit, cash discounts (CD), and turnover discounts (TOD). Unchecked dealer credit is the #1 killer of emerging paint manufacturers.
- **Sharma Industries Defense**:
  - Strict 21-day credit window backed by automated ERP ledger locks (`/api/erp/dealers/credit-check`).
  - Bypass dealer gatekeeping by cultivating direct contractor and painter demand (Painter Token Loyalty Program). When the painter demands Swatch Paints, the dealer must stock it.

### Force 4: Threat of New Entrants (Moderate)
- **Barriers to Entry**:
  - High working capital requirements to finance channel inventory and dealer credit.
  - Extensive distribution footprint required to achieve supply chain economies of scale.
  - Tinting machine capital investment per retail counter.
  - Rising environmental compliance (Pollution Control Board clearances for chemical synthesis).
- **Emerging Threat**: Large conglomerate entrants (e.g., Grasim/Birla Opus) flooding the market with massive capex, free tinting machines, and aggressive dealer sign-up bonuses.
- **Sharma Industries Defense**:
  - Regional focus: Defend the home turf of Hadoti, Mewar, and Dhundhar before over-extending.
  - Direct factory-to-dealer logistics with same-day dispatch within a 150 km radius from Kota.

### Force 5: Threat of Substitutes (Low to Moderate)
- **Exterior Substitutes**: Ceramic tiles, stone cladding, glass facades, and textured cement boards.
- **Interior Substitutes**: PVC wall panels, designer wallpapers, and untreated gypsum finish.
- **Economical Substitutes**: Traditional lime wash (chuna) and white cement washes in rural construction.
- **Sharma Industries Defense**:
  - Value-engineered exterior emulsions (WeatherShield series) offering better thermal reflection and waterproofing than expensive ceramic cladding.
  - Premium acrylic water-based wall putty providing silky smooth substrate holdout, converting lime-wash users into premium emulsion customers.

---

## 4. Tactical Strategic Playbooks

### Playbook A: The "Mandi Fortress" Territory Defense
When an incumbent or new mega-entrant attempts to squeeze Swatch Paints out of a regional mandi:
1. **Audit Counter Share**: Query `/api/erp/sales/mandi-metrics?mandi=Kota` to identify vulnerable A-category dealers.
2. **Execute Margin Arbitrage**: Offer the dealer a guaranteed 18% net realization on 20L emulsion buckets against competitor's 7% net realization.
3. **Deploy Painter Squads**: Assign 5 Dedicated Contractor Relationship Executives to route all local bungalow painting contracts directly through that dealer's billing desk.

### Playbook B: Supplier Raw Material Shock Hedge
When crude oil spikes >$90/barrel or TiO2 prices surge >15%:
1. **Run ERP Batch Formulation Costing**: Execute `/api/erp/production/cost-simulate` with updated raw material indices.
2. **Value-Engineer Extender Ratio**: Utilize Rajasthan's local micronized calcium carbonate and calcined clay reserves to optimize hiding power without compromising scrub resistance.
3. **Pre-Purchase Bulk Polymers**: Lock in 60-day binder inventory through verified regional suppliers before price hikes reach retail dealers.

---

## 5. Zero-Price Dynamic ERP Query Protocol
Hermes and sales strategists must NEVER quote static prices or fixed rupee margins from memory. All strategic calculations must query the live ERP system:
```bash
# Live Mandi Pricing & Margin Calculation
curl -s http://localhost:8000/api/erp/pricing/category-margins?category=exterior_emulsion
# Live Dealer Credit & Turnover Discount Tiers
curl -s http://localhost:8000/api/erp/dealers/commercial-terms?dealer_id=DLR-KOTA-014
```

---

## 6. Execution Checklist for Strategic Audits
- [ ] Has competitive rivalry in the target mandi been evaluated (Incumbent share vs Challenger share)?
- [ ] Are dealer credit limits strictly enforced via ERP to prevent working capital traps?
- [ ] Has painter pull-demand been activated to neutralize dealer bargaining power?
- [ ] Are raw material supply risks hedged with local alternative suppliers?
- [ ] Has the strategic plan received executive sign-off under Ashutosh Sharma Sir's directives?
"""

    # =========================================================================
    # SKILL 2: INFLUENCE-PSYCHOLOGY
    # =========================================================================
    skills["influence-psychology"] = """---
name: influence-psychology
description: Robert Cialdini's 6 Principles of Ethical Influence & Behavioral Persuasion engineered for the Indian Paint Distribution Channel. Master paint dealer gaddi psychology, contractor loyalty rituals, painter token mechanics, architect specifications, and commercial sales negotiations. Translates Reciprocity, Commitment & Consistency, Social Proof, Authority, Liking, and Scarcity into culturally grounded, field-tested B2B sales execution for Swatch Paints (Sharma Industries).
metadata:
  version: 2.0.0
  author: Sharma Industries & Hermes Sales Strategy
  category: Sales Psychology & Behavioral Persuasion
---

# Influence Psychology & Ethical Persuasion Engine (Cialdini Methodology for Swatch Paints)

## 1. Executive Authority & Behavioral Foundations
Operating under the authority of **Ashutosh Sharma Sir (Founder & Managing Director)** and orchestrated by **Hermes (CEO Agent)**, this engine operationalizes behavioral science across the Indian paint mandi ecosystem.

Selling paint in India is not a rational spreadsheet transaction. A dealer sitting on his traditional gaddi in Kota, Jaipur, or Bhilwara makes purchasing decisions influenced by trust, social standing, perceived risk, peer validation, and reciprocal loyalty. This skill decodes Dr. Robert Cialdini’s 6 foundational principles of influence and provides exact tactical scripts, psychological triggers, and operational rituals for Swatch Paints field representatives.

---

## 2. The 6 Principles Applied to the Indian Paint Mandi

```
+-------------------------------------------------------------------------------+
|                       CIALDINI'S 6 WEAPONS OF INFLUENCE                       |
+-------------------+--------------------+-------------------+------------------+
| 1. RECIPROCITY    | 2. COMMITMENT      | 3. SOCIAL PROOF   | 4. AUTHORITY     |
| Give value first; | Micro-agreements   | Mandi herd        | Technical mastery|
| dealer feels      | build irreversible | validation & peer | & lab certs      |
| moral debt        | momentum           | adoption          | neutralize doubt |
+-------------------+--------------------+-------------------+------------------+
|                   | 5. LIKING          | 6. SCARCITY       |                  |
|                   | Gaddi rapport,     | Exclusive radius  |                  |
|                   | shared regional    | & seasonal batch  |                  |
|                   | pride & intimacy   | allocations       |                  |
+-------------------+--------------------+-------------------+------------------+
```

---

## 3. Principle-by-Principle Operational Playbooks

### Principle 1: Reciprocity (Give High-Perceived Value First)
**The Mandi Rule**: If you ask a dealer for a 2-lakh opening stock order before offering value, his defense mechanisms activate. Give first to create an unspoken obligation.
- **The Tactic**:
  - Never walk into a new counter empty-handed.
  - Present a bespoke **"Swatch Master Painter Swatch Deck"** ($1,500 INR retail value) or 2 free 1-liter sample cans of Royal Luxury Interior Emulsion for the dealer's personal home or shop touch-up.
  - Offer to conduct a free **"Contractor High-Tea Meet"** at the dealer's shop, where Swatch Paints pays for the samosas, tea, and painter gifts while branding the dealer as the host.
- **Field Script**:
  > *"Seth ji, aapse business shuru karne se pehle hum chahte hain ki aap hamari quality khud parkhein. Yeh hamara luxury emulsion ka sample pack hai, aap apne showroom ke display panel ya ghar par lagwaiye. Agar aapko lagta hai ki iski finishing aur covering Asian Paints Royale se kam hai, toh hum aapse dobara baat nahi karenge. Yeh hamari taraf se aapke liye bhet hai."*

### Principle 2: Commitment & Consistency (The Micro-Yes Ladder)
**The Mandi Rule**: Large commitments terrify dealers who have been burned by dead inventory. Guide them through small, effortless agreements that make the final stocking decision a natural progression.
- **The Step-by-Step Micro-Ladder**:
  1. *Agreement 1*: "Seth ji, kya aap maante hain ki aaj kal exterior paint mein waterproof primer ka demand badh gaya hai?" (Yes)
  2. *Agreement 2*: "Aur agar dealer ko 6% ki jagah 18% saaf margin mile, toh counter par fayda zyada hoga?" (Yes)
  3. *Agreement 3*: "Toh kya hum sirf 2 bucket fast-moving primer counter display par rakh sakte hain, jiska payment aap tabhi dijiye jab dono bucket bik jayein?" (Yes - Micro commitment secured).
  4. *The Consistency Lock*: Once the 2 buckets sell in 48 hours, the dealer's self-image as a "smart businessman making higher margin" demands re-ordering a full carton.

### Principle 3: Social Proof (Mandi Herd Dynamics)
**The Mandi Rule**: Paint dealers are hyper-aware of their competitors in the same market. They fear missing out on what the leading contractors and prominent shops are already profiting from.
- **The Tactic**:
  - Document every major bungalow, temple, hospital, or commercial complex in the district painted with Swatch Paints.
  - Carry a laminated tablet or physical photo portfolio of local landmark sites with nameplates of reputed painting thekedars (contractors).
- **Field Script**:
  > *"Seth ji, Vigyan Nagar mein Verma Paint Store aur Aerodrome circle par Gupta Hardware ne pichle mahine 450 bucket Swatch WeatherShield nikali hai. Kota ke top contractor Pappu Mistri ne abhi 14 bungalows mein sirf Swatch specify kiya hai. Mandi mein sabko pata hai ki customer ko quality pasand aa rahi hai aur painter ko double token reward mil raha hai."*

### Principle 4: Authority (Formulation Science & Institutional Rigor)
**The Mandi Rule**: Dealers and architects encounter dozens of smooth-talking sales reps every month. Authority cuts through sales puffery by citing verifiable chemical parameters.
- **The Tactic**:
  - Arm sales officers with certified NABL test reports: Scrub resistance (>3,000 cycles), Titanium Dioxide content (verified percentage), VOC compliance, and UV-radiation exposure test certificates.
  - Position Founder Ashutosh Sharma Sir’s technical manufacturing legacy in Kota: *"Hum trader nahi hain, hum direct chemical manufacturer hain jo 15 saal se khud formulation design karte hain."*
- **Field Script**:
  > *"Seth ji, yeh NABL accredited lab report dekhiye. Market ka standard exterior paint 1,200 scrub cycles par chalking dikhata hai. Swatch WeatherShield 3,500 cycles tak intact rehta hai. Jab architect ya consumer humse sawal karta hai, hum lab proof counter par table par rakh dete hain."*

### Principle 5: Liking (Gaddi Rituals & Cultural Rapport)
**The Mandi Rule**: In Rajasthan and North-Central India, transactions follow relationships. If the dealer does not like you as a person, he will find a dozen excuses about "no demand" or "credit cycle issues".
- **The Rituals**:
  - **The Gaddi Demeanor**: Never sit above the dealer. Remove footwear if entering a traditional gaddi. Accept tea or water without hesitation.
  - **Active Listening**: Inquire about family, festive trade expectations, and mandi gossip for the first 5 minutes before mentioning product catalogs.
  - **Local Identity**: Emphasize regional pride: *"Hum Rajasthan ki apni industry hain, local dealer ka dard MNCs ke sales managers kabhi nahi samajhte."*

### Principle 6: Scarcity (Protecting Territorial Exclusivity)
**The Mandi Rule**: A product available in every corner grocery store holds zero prestige. Paint dealers want exclusivity so their neighbor cannot undercut them on price.
- **The Tactic**:
  - Strict dealer density policy: Only 1 authorized Swatch Paints Prime Distributor per 2 km commercial radius.
  - Limited seasonal pre-booking allocations: Offer exclusive pre-monsoon waterproofing discount slots capped at the first 5 dealers per tehsil.
- **Field Script**:
  > *"Seth ji, hum poore Gumanpura mandi mein sirf 2 dealers ko Prime Stockist banayenge taaki counter par price cutting na ho aur aapka 20% margin safe rahe. Pehla counter humne aapke samne offer kiya hai. Agar aapko lagta hai ki aap abhi nahi shuru karna chahte, toh hume Bajrang Nagar wale store ko call karna padega, kyunki hamara territory allocation is hafte band ho raha hai."*

---

## 4. Architect & Builder Specification Influence Architecture
When influencing institutional specifiers (Architects, Civil Engineers, PMC Consultants):
1. **Target the Fear of Reputational Damage**: Architects care about dampness seepage and exterior color fading destroying their portfolio aesthetics.
2. **Provide Detailed Architectural Specification Sheets**: Submit comprehensive MasterFormat CSI-style specifications with exact surface prep guidelines.
3. **Offer Sample Mockup Walls**: Paint a 100 sq.ft. test patch on the actual construction site for 14-day curing inspection.

---

## 5. Dynamic ERP Data Verification
Never guess inventory levels or promotional budgets during a negotiation. Query live ERP:
```bash
# Verify Dealer Past Order Frequency & Credit Rating
curl -s http://localhost:8000/api/erp/dealers/profile?dealer_id=DLR-KOTA-042
# Check Live Promotional Token Budget for Mandi
curl -s http://localhost:8000/api/erp/marketing/tokens/budget?district=Kota
```

---

## 6. Execution Protocol for Field Representatives
- [ ] Has a high-perceived-value gift or sample been provided before asking for stock commitment?
- [ ] Has the micro-yes agreement ladder been utilized rather than pushing full truckloads?
- [ ] Has local social proof (nearby contractors, landmark sites) been demonstrated?
- [ ] Were certified NABL lab reports presented to establish formulation authority?
- [ ] Was territorial exclusivity and seasonal batch scarcity clearly communicated?
"""

    # =========================================================================
    # SKILL 3: GTM-STRATEGY
    # =========================================================================
    skills["gtm-strategy"] = """---
name: gtm-strategy
description: Go-To-Market (GTM) Regional Mandi Expansion and Territory Launch Engine for Swatch Paints (Sharma Industries). Master the sequential conquest of new geographic territories across Rajasthan and Madhya Pradesh (Bundi, Baran, Jhalawar, Bhilwara, Chittorgarh, Jaipur, Indore). Covers depot logistics, anchor dealer recruitment, painter contractor melas, trade credit governance, secondary demand pull, and rapid territory breakeven economics.
metadata:
  version: 2.0.0
  author: Sharma Industries & Hermes Commercial Operations
  category: Territory Expansion & Go-To-Market
---

# GTM Territory Launch & Mandi Expansion Engine (Swatch Paints Regional Conquest)

## 1. Executive Authority & Strategic Mission
Orchestrated under the supreme command of **Founder & Managing Director Ashutosh Sharma Sir** and executed by **Hermes (CEO Agent)**, this engine governs the step-by-step geographic expansion of Swatch Paints.

Launching a new paint territory without a structured GTM framework leads to trapped capital, uncollected dealer debt, and dead stock on dusty shelves. The Swatch Paints GTM methodology follows a **"Hub-and-Spoke Blitzkrieg"**: establishing unshakeable operational dominance in Kota, then methodically expanding into concentric regional trade rings through a synchronized 5-phase territory launch blueprint.

---

## 2. The 5-Phase Mandi Launch Blueprint

```
+---------------------------------------------------------------------------------+
|                         5-PHASE TERRITORY LAUNCH ENGINE                         |
+-------------------+--------------------+-------------------+--------------------+
| PHASE 1: RECON    | PHASE 2: LOGISTICS | PHASE 3: ANCHOR   | PHASE 4: PAINTER   |
| Mandi mapping,    | Regional depot,    | Sign 2-3 prominent| Contractor meets,  |
| dealer profiling, | 24-hr dispatch     | Prime Stockists   | live demo, instant |
| contractor census | SLA established    | with margin moat  | mobile token scans |
+-------------------+--------------------+-------------------+--------------------+
                    | PHASE 5: SECONDARY PULL & LOCAL BRANDING|
                    | Mandi transit branding, sample flat flats,  |
                    | institutional builder specification locks   |
+-------------------+-------------------------------------------------------------+
```

---

## 3. Deep Phase-by-Phase Execution Protocols

### Phase 1: Mandi Intelligence & Reconnaissance (Days 1 to 14)
- **Objective**: Complete a forensic audit of the target district before deploying sales capital.
- **Field Deliverables**:
  1. **Retail Census**: Map every paint shop, hardware store, and building material counter in the target mandi. Categorize them into Tier A (>15L monthly paint billing), Tier B (5-15L), and Tier C (<5L).
  2. **Competitor Friction Audit**: Identify which incumbents are abusing dealers with delayed turnover discounts, high minimum order quantities (MOQs), or forced slow-moving stock dumping.
  3. **Contractor Top-50 Roster**: Collect names, mobile numbers, and active site locations of the 50 most influential painting thekedars (contractors) in the district.
- **ERP Integration**:
  ```bash
  curl -X POST http://localhost:8000/api/erp/territory/census \\
    -H "Content-Type: application/json" \\
    -d '{"mandi": "Bhilwara", "total_counters": 68, "tier_a_targets": 12}'
  ```

### Phase 2: Depot & Logistics Activation (Days 15 to 21)
- **The Core Rule**: Never recruit a dealer until delivery within 24 hours is physically guaranteed.
- **Distribution Setup**:
  - Establish a regional mother depot or dedicated C&F (Carrying & Forwarding) tie-up with local warehousing.
  - Buffer stock formulation: 60% fast-moving white bases & exterior primers, 25% interior/exterior emulsions, 15% water-based wall putty.
  - Same-day dispatch SLA for all orders received by 11:00 AM within municipal limits.

### Phase 3: Anchor Stockist Recruitment (Days 22 to 35)
- **Target Profile**: Do not target the #1 entrenched Asian Paints dealer who is hopelessly indebted or tied to incumbent loyalty trips. Target the ambitious #2 or #3 dealer who wants to grow fast and is starved for higher margins.
- **The Anchor Pitch Package**:
  - **Margin Arbitrage**: Guaranteed 18-22% gross counter margin on core emulsion lines.
  - **Counter Branding**: High-visibility showroom cladding, illuminated 3D acrylic Swatch Paints board, and motorized display panels.
  - **Strict Territorial Exclusivity**: Signed legal memorandum ensuring no competing distributor within his assigned retail zone.
  - **Credit Protection**: Initial billing on 50% advance / 50% on 14 days, supported by PDC (Post-Dated Cheque) or bank mandate.

### Phase 4: Contractor Melas & Painter Token Activation (Days 36 to 45)
- **The Secret Weapon**: Secondary pull created by the local painter workforce completely neutralizes dealer resistance.
- **The "Swatch Karigar Mela" Protocol**:
  1. Convene 40-80 local painters and contractors at a reputed local hotel or banquet hall.
  2. Live Demonstration: Place Swatch Royal Luxury Emulsion side-by-side with incumbent market leader on freshly prepared cement boards. Demonstrate superior opacity, single-coat hiding, and high water-repellency.
  3. Digital Token Onboarding: Register every attendee on the Swatch Painter Mobile Portal. Demonstrate instant UPI cash back upon scanning barcode tokens inside every 20L bucket.
  4. Hand out official Swatch Paints painter kit bags (overalls, high-grade putty blades, masking tape, branded caps).

### Phase 5: Secondary Demand Generation & Expansion (Days 46 to 90)
- **Mandi Branding**: Paint 25 high-traffic railway crossing walls, mandi entrance banners, and dealer delivery auto-rickshaws.
- **Sample Flat Program**: Offer local prominent real estate builders free paint material for their 1 sample flat in exchange for bulk project quotation rights.
- **Route Beat Plan (PJP)**: Institute a rigid Permanent Journey Plan for the local Territory Sales Officer: 8 counters visited daily, audited in real-time via ERP GPS check-in.

---

## 4. Territory Unit Economics & Breakeven Modeling
A new territory must achieve positive contribution margin within **90 days** of launch:
- **Monthly Fixed Operating Cost (Per District)**:
  - 1 Territory Sales Officer (TSO) + 1 Contractor Relationship Exec (CRE): Base + TA/DA.
  - Depot logistics allocation / freight freight per ton.
  - Local marketing / contractor mela amortization.
- **Target Volume Threshold**:
  - Minimum monthly liquidation: 12 metric tons of emulsion/primer/putty.
  - Average gross margin realization: Calculated dynamically via `/api/erp/finance/target-contribution`.

---

## 5. Zero Hardcoding Dynamic ERP Bindings
Field teams must pull real-time inventory availability and logistics lead times directly from the ERP:
```bash
# Query Target Mandi Readiness & Depot Inventory
curl -s http://localhost:8000/api/erp/logistics/depot-status?mandi=Jaipur_South
# Check New Territory Dealer Onboarding Pipeline
curl -s http://localhost:8000/api/erp/territory/pipeline?region=Hadoti
```

---

## 6. GTM Launch Gate Checklist
- [ ] Phase 1 Mandi census completed with minimum 50 painter contacts verified?
- [ ] Regional depot stocked with minimum 10-day safety inventory?
- [ ] 24-hour delivery SLA tested and verified with local transport carriers?
- [ ] First 2 Anchor Stockists signed with verified credit terms and PDC mandates?
- [ ] First Swatch Karigar Mela executed with minimum 40 painters registered?
- [ ] TSO beat plan mapped and activated in ERP with geo-fencing?
"""

    # =========================================================================
    # SKILL 4: SALES-STRATEGIST
    # =========================================================================
    skills["sales-strategist"] = """---
name: sales-strategist
description: Strategic Commercial Sales Operations, Territory Quota Engineering, Field Rep Incentive Design, and B2B Pipeline Governance for Swatch Paints (Sharma Industries). Use when structuring sales organizational roles (TSO, CRE, IPM), building collection-linked compensation structures, designing Permanent Journey Plans (PJP beat plans), accelerating dealer conversion velocity, and governing institutional builder/project sales pipelines.
metadata:
  version: 2.0.0
  author: Sharma Industries & Hermes Commercial Operations
  category: Sales Strategy & Commercial Operations
---

# Commercial Sales Strategy & Revenue Operations Engine

## 1. Executive Mandate & Strategic Philosophy
Operating under the supreme authority of **Founder & Managing Director Ashutosh Sharma Sir** and executed autonomously by **Hermes (CEO Agent)**, this engine establishes commercial discipline across all sales operations.

**The Golden Rule**: *"A-players trapped in a broken sales system will fail; disciplined B-players backed by an airtight, incentive-aligned system will conquer mandis."*
Sales heroics do not scale. Predictable revenue in paint manufacturing is built on rigid journey planning, non-negotiable credit governance, collection-linked commissions, and relentless secondary pull.

---

## 2. Sales Organizational Architecture

```
                    +------------------------------------+
                    |   Ashutosh Sharma Sir (Founder)    |
                    |   & Hermes (Chief Executive Agent) |
                    +-----------------+------------------+
                                      |
                                      v
                    +------------------------------------+
                    |    Head of Commercial Operations   |
                    +-----------------+------------------+
                                      |
         +----------------------------+----------------------------+
         |                                                         |
         v                                                         v
+-------------------------------+                         +-------------------------------+
|  Territory Sales Officers     |                         | Institutional Project         |
|  (TSOs - Retail Network)      |                         | Managers (IPMs - Builders)    |
|  - Dealer Counter Acquisition |                         | - Real Estate Developers      |
|  - Beat Plan Compliance       |                         | - Government & Hospital Tenders|
|  - Primary & Secondary Billing|                         | - Architect Specifications    |
+---------------+---------------+                         +-------------------------------+
                |
                v
+-------------------------------+
| Contractor Relationship Execs |
| (CREs - Field Activation)     |
| - Painter Token Adoption      |
| - Site Mockups & Demos        |
| - Karigar Melas & Loyalty     |
+-------------------------------+
```

---

## 3. Compensation & Incentive Engineering

### The Fatal Flaw of Traditional Sales Incentives
Most paint companies pay sales reps bonuses on **Primary Billing** (the invoice value sent to the dealer). This incentivizes reps to dump unwanted stock on dealers at the end of the month, resulting in massive unpaid debt, high market returns, and sour dealer relationships.

### The Swatch Paints Collection-Linked Incentive Formula
Sales commissions at Sharma Industries are strictly tied to **Realized Cash Collections** and **Secondary Sell-Through**:
1. **Zero Commission on Uncollected Debt**: No incentive is disbursed until the dealer invoice is paid in full within the authorized credit window (maximum 21 days).
2. **Margin-Weighted Volume Multiplier**:
   - High-Margin Specialty Emulsions (Royal Luxury, WeatherShield PU): 1.5x incentive weight.
   - Standard Interior Acrylics & Primers: 1.0x incentive weight.
   - Low-Margin Putty & Distemper: 0.5x incentive weight.
3. **The Active Counter Retention Bonus**: TSOs receive a recurring monthly stipend for every active dealer counter that places at least 2 repeat orders every 30 days.

---

## 4. Territory Quota & Beat Plan Design (PJP)

### Permanent Journey Plan (PJP) Standards
- Every TSO must follow a pre-scheduled, cyclical route beat plan locked in the ERP:
  - **Monday**: Central Mandi & Hardware Belt (Counters 1-10).
  - **Tuesday**: Industrial Area & Sub-Dealers (Counters 11-20).
  - **Wednesday**: Outstation Tehsil Hub A (Counters 21-30).
  - **Thursday**: Institutional Builder Sites with IPM (Active Construction).
  - **Friday**: Outstation Tehsil Hub B (Counters 31-40).
  - **Saturday**: Dealer Collections, Account Reconciliation, Painter Token Audits.
- **Daily Performance Metrics**:
  - Minimum 8 productive dealer visits per day.
  - GPS check-in via mobile app at the dealer's geo-coordinates.
  - Daily Primary Billing vs Secondary Liquidation ratio.

---

## 5. B2B Institutional Project Pipeline Governance

When selling directly to Real Estate Builders, Commercial Contractors, and Infrastructure Projects:

### The MEDDIC-Paint Qualification Matrix
Every project opportunity above 5,000 liters must be qualified against the 6 pillars:
1. **Metrics**: Total carpet/built-up area, liters required per coat, total project cost savings target.
2. **Economic Buyer**: Is the Managing Director or Chief Purchase Officer approving the purchase order, or just a site supervisor with zero signing authority?
3. **Decision Criteria**: Whiteness index, scrub resistance, VOC limits, RERA compliance certification, payment credit schedule.
4. **Decision Process**: Technical submittal -> Site sample patch inspection -> Purchase Committee commercial negotiation -> PO issuance.
5. **Identify Pain**: What went wrong with their previous paint supplier? (e.g., Peeling exterior after monsoon, delayed delivery stalling handover, color batch variation).
6. **Champion**: Have we secured the Project Architect or Head Civil Engineer as our internal advocate?

---

## 6. Pipeline Velocity & Bottleneck Diagnostic Formula
```
Pipeline Velocity = (Active Deals × Win Rate % × Average Deal Size INR) / Sales Cycle Days
```
- **If Win Rate < 25%**: Sales rep is pitching features instead of diagnosing dealer/builder pain (Trigger `pain-is-the-pitch`).
- **If Sales Cycle > 45 Days**: Deal is stuck at the sample approval stage; deploy CRE to paint on-site mockups within 24 hours.
- **If Deal Size is Small**: Sales rep is timidly selling putty instead of bundling the full 4-layer system (Putty + Primer + 2 Coats Luxury Emulsion).

---

## 7. Dynamic ERP Sales Operations Commands
Sales strategists must pull real-time quota attainment and beat tracking via live ERP APIs:
```bash
# Audit Rep Quota Attainment & Cash Collection Compliance
curl -s http://localhost:8000/api/erp/sales/rep-performance?rep_id=TSO-KOTA-07
# Check Outstanding Dealer Receivables & Overdue Debt
curl -s http://localhost:8000/api/erp/finance/aging-report?territory=Hadoti
```

---

## 8. Operational Discipline Checklist
- [ ] Is sales commission strictly tied to collected cash rather than uncollected billing?
- [ ] Are TSOs adhering to their 6-day PJP beat plan with verified geo-location check-ins?
- [ ] Are high-margin luxury coatings prioritized over low-margin distemper dumping?
- [ ] Have all institutional builder accounts above 5,000L been qualified through MEDDIC?
- [ ] Is secondary liquidation tracked weekly to prevent channel stuffing?
"""

    # =========================================================================
    # SKILL 5: MARKETING-COUNCIL
    # =========================================================================
    skills["marketing-council"] = """---
name: marketing-council
description: Simulated Board of Legendary Marketing Advisors for Swatch Paints (Sharma Industries). Convene David Ogilvy, Eugene Schwartz, Alex Hormozi, Byron Sharp, April Dunford, Claude Hopkins, and Gary Halbert to rigorously debate, stress-test, and refine brand campaigns, packaging, trade promotions, contractor loyalty mechanics, and product positioning. Discovers blind spots and synthesizes consensus across contrasting marketing philosophies.
metadata:
  version: 2.0.0
  author: Sharma Industries & Hermes Brand Strategy
  category: Strategic Marketing & Advisory Simulation
---

# Marketing Council - Legendary Advisory Board for Swatch Paints

## 1. Executive Mandate & Advisory Mechanism
Operating under the supreme executive direction of **Founder & Managing Director Ashutosh Sharma Sir** and moderated by **Hermes (CEO Agent)**, this engine convenes a simulated council of history's greatest marketing minds.

Before Sharma Industries commits capital to a new advertising campaign, dealer trade scheme, exterior emulsion packaging design, or painter loyalty program, the proposal is presented before the **Marketing Council**. The value of this council is not unanimous agreement—it is the **sharp, intellectual friction between opposing marketing philosophies**. By exposing every marketing initiative to rigorous cross-examination, Swatch Paints eliminates expensive mistakes before market launch.

---

## 2. The 7 Council Advisors & Their Strategic Lenses

```
+-----------------------------------------------------------------------------------+
|                        THE SWATCH PAINTS MARKETING COUNCIL                        |
+---------------------+-----------------------+---------------------+---------------+
| 1. DAVID OGILVY     | 2. EUGENE SCHWARTZ    | 3. ALEX HORMOZI     | 4. BYRON SHARP|
| "The Consumer isn't | "Channel existing     | "Grand Slam Offers, | "Mental &     |
| a moron; she's your | desire; don't try to  | risk reversal, 3x   | physical      |
| wife. Give facts."  | create new desire."   | dealer ROI."        | availability."|
+---------------------+-----------------------+---------------------+---------------+
| 5. APRIL DUNFORD    | 6. CLAUDE HOPKINS     | 7. GARY HALBERT                     |
| "Position against   | "Scientific testing,  | "Raw emotional grabbers, bold       |
| the real market     | sample trial coupons, | dealer letters, urgent stakes."     |
| alternatives."      | measurable proof."    |                                     |
+---------------------+-----------------------+-------------------------------------+
```

---

## 3. Detailed Profiles & Diagnostic Lenses of the Advisors

### Advisor 1: David Ogilvy (Craftsmanship, Long-term Equity & Reason-Why)
- **Core Philosophy**: Advertising must sell. It must be dignified, factual, and anchored in rigorous product craftsmanship. Avoid clever gimmicks, cheap puns, and empty slogans.
- **The Ogilvy Lens on Swatch Paints**:
  - *"Tell the consumer exactly what is inside the tin. How many grams of pure acrylic binder? How many scrub cycles in the NABL laboratory? Show the craftsman painting a heritage wall in Kota. Treat the homeowner and contractor with utmost respect. Build an enduring brand image that commands a premium price for the next 50 years."*
- **Key Test**: Does this advertisement provide verifiable facts, or is it merely corporate fluff?

### Advisor 2: Eugene Schwartz (Stages of Awareness & Market Sophistication)
- **Core Philosophy**: Copy cannot create desire for a product. It can only take the hopes, dreams, fears, and desires that already exist in millions of people and focus them onto a specific product.
- **The Schwartz Lens on Swatch Paints**:
  - *"In Tier 2/3 Indian cities, homeowners are not in the 'Unaware' stage about paint—they are in the 'Solution-Aware' or 'Product-Aware' stage. They know Asian Paints and Berger exist, but they are terrified of moisture seepage (seelan) ruining their new walls. Speak directly to their existing fear of peeling paint during the monsoon. Match the headline to their exact stage of sophistication."*
- **Key Test**: What stage of awareness is the target prospect, and does our message meet them there?

### Advisor 3: Alex Hormozi (Grand Slam Offers & Frictionless Unit Economics)
- **Core Philosophy**: If your offer needs explaining, it is too weak. Make offers so good that people feel stupid saying no. Maximize perceived value, eliminate risk, and optimize dealer margin velocity.
- **The Hormozi Lens on Swatch Paints**:
  - *"Why should a dealer switch from Asian Paints to Swatch? Because we give him 3x the net profit with zero inventory risk. Bundle 10 buckets of WeatherShield with a free contractor spray machine, double painter token payouts, and a 100% buyback guarantee on unsold stock after 60 days. Make it an absolute mathematical no-brainer for the dealer."*
- **Key Test**: Is the offer so compelling and risk-reversed that rejecting it feels financially irrational?

### Advisor 4: Byron Sharp (Distinctive Brand Assets & Physical Availability)
- **Core Philosophy**: Loyalty is largely a myth; brands grow through mental availability (being remembered at the moment of purchase) and physical availability (being easily found on the shelf).
- **The Sharp Lens on Swatch Paints**:
  - *"Forget brand loyalty. Homeowners repaint every 5 years and buy whatever the painter or dealer has in stock. You need two things: Distinctive Brand Assets (a distinct color bucket, a bold, unforgettable logo, a consistent mascot) and Physical Availability (you must be present in every single hardware shop on the Kota-Bundi highway). Reach all category buyers, not just loyalists."*
- **Key Test**: Are our brand assets instantly recognizable from 10 meters away, and is the product physically in stock?

### Advisor 5: April Dunford (Differentiated Context & Positioning)
- **Core Philosophy**: Positioning is not clever messaging; it is defining the context where your unique strengths are obvious to your best-fit customers.
- **The Dunford Lens on Swatch Paints**:
  - *"What are you positioned against? If you position as 'another paint brand like Asian Paints', you will lose. But if you position Swatch as 'The High-Solid Waterproof Coating Engineered Specifically for Rajasthan's Harsh 48°C Heat & Extreme Monsoon Seepage', your formulation strengths become uniquely indispensable."*
- **Key Test**: What is the immediate competitive alternative, and why are we the obvious choice for our target segment?

### Advisor 6: Claude Hopkins (Scientific Advertising & Sampling Trials)
- **Core Philosophy**: Advertising is salesmanship in print. Almost any product can be sold through direct sampling and trackable response mechanisms.
- **The Hopkins Lens on Swatch Paints**:
  - *"Never ask a painter to buy on trust. Put a free 1-liter sample can in his hands. Give him a coupon redeemable at the local dealer. Track how many coupons come back. If 100 sample cans produce 35 bulk orders, scale the sampling program to 5,000 cans. Measure every rupee spent."*
- **Key Test**: Is there an immediate, low-friction trial mechanism that can be scientifically measured?

### Advisor 7: Gary Halbert (Direct Response Grabbers & Urgent Stakes)
- **Core Philosophy**: A bland message dies in the trash bin. Grab the prospect by the throat with an irresistible hook, tell a gripping emotional story, and give an urgent, deadline-driven reason to act today.
- **The Halbert Lens on Swatch Paints**:
  - *"Send a direct physical letter to the top 200 contractors in the district. Start with: 'Dear Contractor, if you are sick and tired of angry homeowners calling you back because their exterior paint flaked off after 6 months, read this letter right now.' Give them a deadline to claim their festive loyalty bonus before midnight on Diwali."*
- **Key Test**: Does the communication grab immediate attention and compel rapid physical action?

---

## 4. Council Deliberation & Synthesis Protocol
When invoking the Marketing Council:
1. **Present the Strategic Initiative**: Detail the proposed product, campaign, or trade scheme.
2. **Convene the Advisors**: Have each relevant advisor evaluate the proposal through their documented lens, highlighting strengths, fatal flaws, and blind spots.
3. **Stage the Debate**: Pit conflicting perspectives against each other (e.g., Ogilvy’s long-term brand equity vs. Hormozi’s aggressive promotional stacking; Sharp’s broad reach vs. Dunford’s narrow niche).
4. **Hermes Executive Synthesis**: Deliver an authoritative final recommendation incorporating the best insights into an actionable Swatch Paints execution plan.

---

## 5. Dynamic ERP Data Verification
Advisory evaluations must never rely on assumed margins. Check live ERP data:
```bash
# Verify Current Marketing ROI & Campaign Spend
curl -s http://localhost:8000/api/erp/marketing/campaigns/active
# Pull Real-time Category Profitability & Contribution
curl -s http://localhost:8000/api/erp/finance/category-profitability?category=luxury_emulsions
```
"""

    # =========================================================================
    # SKILL 6: PAIN-IS-THE-PITCH
    # =========================================================================
    skills["pain-is-the-pitch"] = """---
name: pain-is-the-pitch
description: Hyper-Specific Pain-Driven Sales Pitch & Messaging Engine for Swatch Paints (Sharma Industries). Transforms generic, feature-heavy sales copy and rep pitches into emotionally vivid, commercially acute diagnostic messaging using the Daniel Bustamante / Alex Hormozi "Pain is the Pitch" framework. Identifies acute paint dealer financial bleeding, contractor call-back humiliation, and builder handover bottlenecks to construct irresistible sales conversations.
metadata:
  version: 2.0.0
  author: Sharma Industries & Hermes Sales Strategy
  category: Sales Communication & Direct Response Copywriting
---

# Pain Is The Pitch - High-Conversion Sales Messaging Engine

## 1. Executive Mandate & Psychological Principle
Operating under the authority of **Founder & Managing Director Ashutosh Sharma Sir** and executed by **Hermes (CEO Agent)**, this engine eliminates weak, ineffective sales pitches across all commercial touchpoints.

**The Foundational Law**: *"Prospects do not buy features, chemical formulations, or product specs. They buy immediate relief from chronic, agonizing financial and emotional pain."*
When a sales rep talks about "superior scrub resistance" or "100% pure acrylic polymers," the dealer’s eyes glaze over. But when the rep exposes the **exact rupee hemorrhage** of dead inventory, delayed MNC turnover discounts, and angry painting thekedars demanding compensation, the dealer leans forward. Pain creates urgency; features create price negotiations.

---

## 2. The Mandi Pain Matrix: Real-World Industry Agonies

```
+-----------------------------------------------------------------------------------+
|                           THE PAINT MANDI PAIN MATRIX                             |
+---------------------+-------------------------------+-----------------------------+
| 1. THE PAINT DEALER | 2. THE PAINTING THEKEDAR      | 3. THE BUILDER / DEVELOPER  |
| - Capital locked in | - Peeling call-backs after    | - Dampness & seepage on new |
|   slow-moving stock |   monsoon ruin reputation     |   walls delay flat handover |
| - Razor-thin 5-7%   | - Clients withholding final   | - RERA penalty risks from   |
|   margins from MNCs |   25% payment due to patches  |   construction delays       |
| - Forced end-of-    | - Fake/unscannable tokens     | - Cost overruns from 3-coat |
|   month target dumps|   robbing them of rewards     |   paints with poor hiding   |
+---------------------+-------------------------------+-----------------------------+
```

---

## 3. The 4-Step "Pain-to-Pitch" Transformation Framework

```
[ Step 1: Unmask the Hemorrhage ] -> [ Step 2: Amplify Cost of Inaction ]
                |
                v
[ Step 3: Neutralize Perceived Risk ] -> [ Step 4: The Prescription Offer ]
```

### Step 1: Unmask the Invisible Hemorrhage
Name the precise operational frustration the prospect suffers in vivid, unmistakable detail. Use their exact vocabulary (gaddi, theka, seelan, udhedna, fasa hua paisa).
- *Weak Pitch*: "Hamara paint bahut accha hai aur iska coverage 140 sq.ft. hai."
- *Pain Pitch*: "Seth ji, pichle 3 mahine se counter ke peeche jo 15 bucket slow-moving primer padi hai, usme aapka 45,000 rupaye bina kisi byaj ke fasa hua hai. MNC company ka sales officer targeted dumping karke chala gaya, par gaddi par nuksan sirf aapka ho raha hai."

### Step 2: Amplify the Cost of Inaction
Show them what happens in 90 days if they tolerate the status quo. Financial bleeding does not stop on its own; it compounds.
- *Pain Amplification*: "Agar agle monsoon tak yeh stock nahi nikla, toh pigment settle ho jayega aur material kharab ho jayega. Upar se jab aap unke turnover discount ka claim bhejenge, toh unka portal 'target not met' bolkar aapka 8% discount cancel kar dega. Kab tak doosron ke target ke liye apna counter jalayenge?"

### Step 3: Neutralize the Perceived Risk
Every prospect fears that changing suppliers will create a brand new catastrophe. You must dismantle this fear with concrete guarantees.
- *Risk Neutralization*: "Hum aapse 1 lakh ka order maang hi nahi rahe hain. Aap sirf 2 bucket test kijiye. Aur agar aapke thekedar ne bola ki iska covering Asian Paints se kam hai, toh dono bucket ka paisa hum wapas karenge aur khali tin bhi nahi maangenge."

### Step 4: The Targeted Prescription Offer
Position Swatch Paints not as a generic paint alternative, but as the exact, tailored surgical medicine for their specific diagnosed pain.
- *The Prescription*: "Swatch Paints aapko 18% saaf counter margin deta hai, har 20L bucket par painter ko turant 150 rupaye ka UPI cash token milta hai, aur hum 24 ghante ke andar direct Kota factory se fresh stock deliver karte hain. Aapka paisa safe, margin 3 guna, aur thekedar khush."

---

## 4. Hyper-Specific Pitch Rewriter Scenarios

### Scenario A: Cold Dealer Acquisition Pitch
- **Before (Bland Feature Pitch)**:
  *"Namaste Seth ji. Hum Swatch Paints se hain. Hum Rajasthan ke leading manufacturer hain. Hamare paas interior, exterior, primer aur wall putty sabhi products hain. Quality international standard ki hai aur rate bahut competitive hai."*
- **After (Pain-Is-The-Pitch Transformation)**:
  *"Seth ji, namaste. Ek seedha sawal: Pichle saal aapne 40 lakh ka paint becha, par saal ke aakhir mein aapki jeb mein kya bacha? 5 ya 6 percent? Baki sara munafa company ke target schemes aur unke luxury tours mein chala gaya jahan aapko 2 bucket short hone par disqualify kar diya gaya.*
  *Mandi mein sabhi dealers pareshan hain ki gaddi unki hai, dukan unki hai, grahak unka hai, par kamai MNC le ja rahi hai. Hum Kota mein Sharma Industries hain. Hum aapko seedha 18% saaf margin dete hain—bina kisi hidden target ke aur har hafte cash collection par instant cash discount. Kya hum 5 minute baithkar aapke counter ka real margin calculate kar sakte hain?"*

### Scenario B: Painting Contractor (Thekedar) Pitch
- **Before (Bland Feature Pitch)**:
  *"Bhaiya, yeh Swatch ka exterior paint hai. Isme UV resistance hai aur fungus nahi lagti. Ek baar try karke dekho."*
- **After (Pain-Is-The-Pitch Transformation)**:
  *"Ustad ji, sabse bada dard tab hota hai jab aap 3 mahine dhoop mein mehnat karke 4-manzil ka bangla paint karte hain, aur barish ke baad deewar par chitey aur peeling aane lagti hai. Homeowner aapka 50,000 rupaye rok leta hai aur bolta hai pehle theek karo. Dosh paint ka hota hai, par badnami mistri ki hoti hai.*
  *Swatch WeatherShield mein pure acrylic binder hai jo 48 degree garmi mein bhi crack nahi hota. Aur sabse badi baat: bucket kholte hi dhakkan ke andar 200 rupaye ka direct scanner code hai jo seedha aapke bank account mein credit hota hai—koi dukandar ke chakkaron mein padne ki zaroorat nahi."*

---

## 5. Dynamic ERP Commercial Verification
Never fabricate margin claims during a pitch. Pull real financial parameters from ERP:
```bash
# Pull Verified Dealer Margin Comparisons by Category
curl -s http://localhost:8000/api/erp/pricing/margin-analysis?category=exterior
# Check Active Instant Token Value for Products
curl -s http://localhost:8000/api/erp/marketing/tokens/active-slabs
```

---

## 6. Pitch Quality Audit Checklist
- [ ] Does the pitch open with an acute operational pain rather than company introduction?
- [ ] Is the pain quantified in terms of lost rupees, wasted hours, or damaged reputation?
- [ ] Has the cost of staying with the status quo been vividly amplified?
- [ ] Is the perceived risk completely reversed with a zero-risk trial guarantee?
- [ ] Is the prescription simple, direct, and mathematically superior?
"""

    # =========================================================================
    # SKILL 7: HORMOZI-EVALUATOR
    # =========================================================================
    skills["hormozi-evaluator"] = """---
name: hormozi-evaluator
description: Alex Hormozi Ruthless Offer, Pricing, and Unit Economics Audit Engine for Swatch Paints (Sharma Industries). Evaluates sales proposals, dealer onboarding packages, contractor loyalty schemes, and retail promotions against $100M Offers, $100M Leads, and $100M Money Models. Demands mathematical precision, extreme perceived value, risk reversal guarantees, and bulletproof unit margins. Triggers on "hormozi check", "audit offer", "stress test deal", "grand slam check".
metadata:
  version: 2.0.0
  author: Sharma Industries & Hermes Commercial Strategy
  category: Commercial Evaluation & Offer Architecture
---

# Hormozi Evaluator - Ruthless Offer & Unit Economics Audit Engine

## 1. Executive Activation & Persona Mindset
Operating under the authority of **Ashutosh Sharma Sir (Founder & Managing Director)** and moderated by **Hermes (CEO Agent)**, this engine acts as an uncompromising, mathematically relentless commercial evaluator channeling the thinking of Alex Hormozi.

**The Operating Mindset**:
- *"If your offer requires 10 minutes of verbal explanation, your offer is trash."*
- *"Most businesses fail at the offer level, not the execution level. You don't have a lead problem or a sales rep problem; you have a mediocre offer that forces people to negotiate on price."*
- *"Volume covers all operational sins—but only AFTER your unit economics are bulletproof."*
- *"Accurate > Polite. Every single time."*

---

## 2. The Hormozi Value Equation for Paint Manufacturing

```
                         Dream Outcome (0-10) × Perceived Likelihood of Achievement (0-10)
Value Score (0-100) = ------------------------------------------------------------------------
                             Time Delay (Minimize) × Effort & Sacrifice (Minimize)
```

### The 4 Variables Deconstructed for Swatch Paints:

#### 1. Dream Outcome (Scale 0-10)
- **What the Dealer Actually Dreams Of**: Doubling net counter profit without borrowing more bank debt, gaining prestige in the mandi, and having contractors queue up outside his shop.
- **What the Homeowner Dreams Of**: A magnificent, mirror-smooth luxury home finish that makes neighbors jealous and stays spotless for 7+ years with zero maintenance.

#### 2. Perceived Likelihood of Achievement (Scale 0-10)
- **The Problem**: Talk is cheap. Every paint salesman promises "high quality."
- **The Hormozi Solution**: Overwhelm with proof. NABL lab scrub test certificates, video demonstrations of scrub resistance, 50 local landmark bungalows already painted, written manufacturer warranties signed by Ashutosh Sharma Sir.

#### 3. Time Delay (Scale 0-10, Goal: Near Zero)
- **The Problem**: A contractor or dealer hates waiting 4 days for outstation depot dispatches.
- **The Hormozi Solution**: Immediate same-day dispatch from the Kota facility. Instant mobile UPI token scan rewards for painters credited in <10 seconds.

#### 4. Effort & Sacrifice (Scale 0-10, Goal: Near Zero)
- **The Problem**: Switching paint brands requires clearing shelf space, retraining painters, changing tinting habits, and risking customer complaints.
- **The Hormozi Solution**: Provide free high-visibility display racks, pre-tinted fast-moving bases, free painter application toolkits, and on-site technical support for first 3 jobs.

---

## 3. The 5-Point Ruthless Offer Audit Matrix

When evaluating any Swatch Paints commercial proposal, score each element from 0 to 20 (Total Score / 100):

| Audit Category | Evaluation Standard | Failure Indicator |
| :--- | :--- | :--- |
| **1. Margin Arbitrage (0-20)** | Does the dealer make at least **2.5x to 3x** the net rupee profit compared to Asian Paints or Berger? | Dealer margin is <12% or tied up in year-end target hoops. |
| **2. Risk Reversal (0-20)** | Is there an unconditional, asymmetric guarantee that removes 100% of the buyer's risk? | "Product once sold will not be taken back" (Instant Fail). |
| **3. Value Stacking (0-20)** | Are high-perceived-value bonuses included that cost little to manufacture but feel massive to the buyer? | Just discounting the list price by 5% (Lazy marketing). |
| **4. Scarcity & Urgency (0-20)** | Is there a real, legitimate commercial reason to act today rather than next month? | Artificial fake countdown timers with zero consequence. |
| **5. Naming & Clarity (0-20)** | Does the offer name clearly communicate the avatar, the outcome, and the mechanism? | Generic internal SKU codes (e.g., "Scheme Q3-2026"). |

---

## 4. Real-World Offer Transformation Case Study

### Proposal Under Audit: "New Dealer Introductory Scheme"
- **The Original Rep Proposal**:
  *"Dealers who buy 50 buckets of Swatch Paints will get 5% extra cash discount and a free wall clock."*
- **Hormozi Evaluation**:
  - *Score*: 18/100 (Unacceptable).
  - *Critique*: "This is pathetic. A 5% discount on an unknown challenger brand is an insult. A wall clock? Is this 1985? The dealer has to risk 1.5 lakhs of working capital for a 7,500 rupee discount and a piece of plastic. He will say 'No thanks, I'll stick with Asian Paints'."

### The Hormozi "Grand Slam" Re-Architecture:
- **Offer Title**: **The "Zero-Risk Mandi Monopoly" Starter Package**
- **The Stack**:
  1. **Core Product**: 25 fast-moving buckets of Swatch WeatherShield & Royal Luxury Emulsion.
  2. **Margin Arbitrage**: Immediate 18% gross counter margin (vs. 6% industry standard) = Dealer clears 3x net cash.
  3. **Bonus 1 (Value ₹15,000)**: Complete High-Visibility Showroom Branding Kit (3D Acrylic Glow-sign board + motorized color sample stand) provided 100% free.
  4. **Bonus 2 (Value ₹8,000)**: Exclusive Contractor High-Tea Sponsorship for 25 local thekedars hosted at the dealer's shop.
  5. **Bonus 3 (Value ₹5,000)**: 5 Contractor Welcome Kits (Premium Putty Blades, Painter Overalls, Measuring Tapes) for his top 5 painters.
  6. **The Unconditional Guarantee**: **100% Sell-Through or Full Buyback Guarantee**. *"If any bucket remains unsold after 45 days, our truck picks it up and returns your money in full. Zero questions asked."*
  7. **Scarcity Constraint**: Limited strictly to **1 Prime Stockist per 2-kilometer trade zone** to prevent local counter price-cutting.
- *Hormozi Verdict*: "Now you have an offer. A dealer who says no to this is actively choosing to make less money while taking more risk."

---

## 5. Dynamic ERP Unit Economics Query Protocol
Never evaluate a Grand Slam offer without verifying contribution margins in the live ERP:
```bash
# Verify Raw Material Cost of Production vs Selling Price
curl -s http://localhost:8000/api/erp/production/unit-economics?sku=ROYAL-EMULSION-20L
# Check Promotional Bonus Reserve Budget for Region
curl -s http://localhost:8000/api/erp/marketing/trade-budget?region=Hadoti
```

---

## 6. Pre-Execution Audit Checklist
- [ ] Is the offer headline clear, avatar-specific, and benefit-driven?
- [ ] Does the dealer or customer achieve at least 3x perceived value relative to price?
- [ ] Is there an ironclad, unconditional risk reversal (buyback or trial guarantee)?
- [ ] Are bonuses high-perceived-value and low-marginal-cost?
- [ ] Is the unit margin verified through ERP to ensure positive net profit contribution?
"""

    # Write each skill to both destinations
    created_count = 0
    for name, content in skills.items():
        ws_dir = os.path.join(ws_base, name)
        app_dir = os.path.join(app_base, name)
        
        os.makedirs(ws_dir, exist_ok=True)
        os.makedirs(app_dir, exist_ok=True)
        
        ws_file = os.path.join(ws_dir, "SKILL.md")
        app_file = os.path.join(app_dir, "SKILL.md")
        
        with open(ws_file, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
            
        with open(app_file, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
            
        lines = len(content.strip().splitlines())
        print(f"Created: {name} ({lines} lines) -> dual-installed.")
        created_count += 1
        
    print(f"\nAll {created_count} Batch 3 bespoke skills successfully created and installed!")

if __name__ == "__main__":
    build_batch3_skills()
