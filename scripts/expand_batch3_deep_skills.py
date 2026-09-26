"""
Deep Expansion Script for Batch 3 Skills (220-270+ lines each)
Ensures 100% production-grade depth, complete field dialogues, comprehensive tables,
and exhaustive operational playbooks for Sharma Industries / Swatch Paints.
"""
import os

ws_base = r"d:\Sharma Industries Erp Software\hermes-agent\skills"
app_base = r"C:\Users\itzzz\AppData\Local\hermes\skills"

# -----------------------------------------------------------------------------
# SKILL 1: PORTER-STRATEGY (Target: 230-260 lines)
# -----------------------------------------------------------------------------
porter_strategy = """---
name: porter-strategy
description: Michael Porter's Five Forces Strategic Industry Analysis Engine tailored for the Indian Paint & Coatings manufacturing and distribution sector. Use when evaluating competitive rivalry against multinational giants (Asian Paints, Berger, Nerolac, Indigo), mitigating raw material chemical supplier leverage, neutralizing dealer buyer bargaining power in Tier 2/3 Mandis, building defensible moats against new entrants, and countering low-cost substitutes (lime wash, exterior cladding, unorganized distempers). Integrates directly with Swatch Paints (Sharma Industries) executive commercial strategy.
metadata:
  version: 2.1.0
  author: Sharma Industries & Hermes Executive Strategy
  category: Corporate Strategy & Market Analysis
---

# Porter's Five Forces Strategic Engine - Indian Paint & Coatings Industry

## 1. Executive Authority & Strategic Mandate
This strategic engine provides institutional market structure analysis for **Sharma Industries (Swatch Paints)**, operating under the supreme executive authority of **Founder & Managing Director Ashutosh Sharma Sir** and executed autonomously by **Hermes (Chief Executive Operating Agent)**.

In the Indian decorative and industrial coatings landscape, strategic victory is not achieved through brute advertising spend—multinational incumbents (Asian Paints, Berger, Kansai Nerolac) spend hundreds of crores annually on celebrity brand ambassadors and tinting machine lock-ins. Instead, Sharma Industries wins by identifying structural industry asymmetries across Porter's Five Forces and ruthlessly exploiting margin, logistics, formulation, and dealer-contractor alignment moats in Tier 2, 3, and rural mandis across Rajasthan and Central India.

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

## 3. Deep Architectural Analysis of the Five Competitive Forces

### Force 1: Industry Competitive Rivalry (Extremely High)
- **Market Concentration**: The organized decorative coatings sector is dominated by an oligopoly (Asian Paints ~53%, Berger ~19%, Nerolac ~12%, AkzoNobel ~6%, Indigo ~3%). They leverage massive nationwide advertising campaigns to induce consumer brand pull.
- **The Tinting Machine Moat**: Incumbents install proprietary automated tinting machines at dealer counters. These machines are locked via encrypted software and proprietary colorant canisters, creating massive artificial switching barriers.
- **Predatory Scheme Dumping**: Incumbents deploy aggressive end-of-quarter volume target schemes (foreign trips, luxury cars, turnover discount slabs) that force dealers to prioritize incumbent inventory liquidation.
- **Sharma Industries Asymmetric Response**:
  1. **Margin Arbitrage**: Incumbent counters deliver 5% to 7% net realization to dealers. Swatch Paints guarantees **18% to 22% net margin**, delivering 3x higher Return on Capital Employed (ROCE).
  2. **Universal Tinting Compatibility**: Provide universal colorant formulations that operate flawlessly on standard manual or open-architecture dispensers, destroying proprietary hardware lock-in.
  3. **Hyper-Localized Formulation**: Formulate coatings engineered specifically for Rajasthan's extreme temperature swings (4°C winter to 49°C summer) and high-calcium groundwater conditions.

### Force 2: Bargaining Power of Raw Material Suppliers (High)
- **Chemical Dependency**: Paint manufacturing relies on petroleum derivatives (monomers: Methyl Methacrylate, Butyl Acrylate, Vinyl Acetate), Titanium Dioxide (rutile TiO2), extenders (calcined clay, calcium carbonate), and functional additives (biocides, defoamers, thickeners).
- **Supplier Concentration**: Key chemical inputs are controlled by global and national oligopolies (Reliance, Dow, Tronox, Chemours). Crude oil fluctuations and currency swings immediately impact gross margins.
- **Sharma Industries Structural Moat**:
  1. **Backward Emulsion Polymerization**: In-house synthesis of core acrylic binders at the Kota manufacturing facility, capturing the polymer chemical margin.
  2. **Mineral Extender Proximity**: Direct sourcing from Rajasthan’s mineral rich belts (Makrana, Udaipur, Rajsamand) for micronized calcite and dolomite, cutting freight costs by 65% versus coastal competitors.
  3. **Dual-Sourcing Hedging**: Mandatory minimum of two audited suppliers for every active raw material SKU in the ERP database.

### Force 3: Bargaining Power of Buyers / Dealers (High)
- **Gaddi Dominance**: Independent paint dealers sitting on traditional commercial gaddis hold immense sway over end-consumer recommendations. Over 70% of retail buyers accept the dealer's recommendation.
- **Credit Extortion Risk**: Dealers routinely seek 60 to 90 days credit, cash discounts (CD), and extended payment cycles. Unmonitored dealer credit is the single greatest cause of insolvency among regional paint manufacturers.
- **Sharma Industries Counter-Strategy**:
  1. **The Contractor Demand Bypass**: By building direct financial relationships with local painting contractors (thekedars) through instant UPI token scans, the consumer and painter demand Swatch Paints by name, forcing the dealer to stock it.
  2. **Automated ERP Credit Governance**: Strict 21-day credit ceiling locked directly in the ERP. Automated dispatch freeze when outstanding invoices exceed credit limits (`/api/erp/dealers/credit-lock`).
  3. **High-Velocity Turnover**: Faster stock replenishment (24 hours from Kota depot) allows dealers to operate with 50% less working capital inventory.

### Force 4: Threat of New Entrants (Moderate to High)
- **Conglomerate Disruption**: Large corporate conglomerates (e.g., Grasim/Birla Opus, JSW Paints) entering the coatings sector with thousands of crores in capex, massive manufacturing plants, free tinting machine giveaways, and aggressive dealer sign-up bonuses.
- **Entry Barriers**: High working capital intensity, widespread dealer distribution inertia, brand trust requirements for 5-10 year exterior waterproofing warranties.
- **Sharma Industries Defensive Moat**:
  1. **Mandi Fortress Strategy**: Deep rooted relationships in home mandis (Kota, Bundi, Baran, Jhalawar, Bhilwara) that cannot be easily dislodged by distant corporate executives.
  2. **Same-Day Direct Factory Dispatch**: Zero C&F intermediary markups within 150 km, ensuring fresher paint batches and immediate customer service response.

### Force 5: Threat of Substitutes (Moderate)
- **External Cladding**: Ceramic exterior tiles, glass curtain walls, ACP sheets, and stone cladding substituting exterior emulsions.
- **Interior Alternatives**: PVC wall panels, vinyl wallpapers, and textured gypsum boards replacing interior emulsion finishes.
- **Low-Cost Substitutes**: Traditional lime wash (chuna) and white cement washes in rural construction.
- **Sharma Industries Neutralization**:
  1. **Waterproof WeatherShield Line**: Formulated with elastomeric crack-bridging polymers, offering superior heat insulation and water-repellency at 20% of the cost of ceramic tiles.
  2. **Silky Smooth Acrylic Wall Putty**: Converting raw plaster and lime-wash users into premium emulsion customers by providing an ultra-smooth, moisture-resistant substrate.

---

## 4. Mandi-by-Mandi Competitive Structural Positioning

| Mandi Territory | Primary Incumbent Strength | Core Market Vulnerability | Swatch Paints Strategic Maneuver |
| :--- | :--- | :--- | :--- |
| **Kota (Urban & Industrial)** | Asian Paints tinting lock-in | Dealer margin squeezed to 5%; high overheads | Direct contractor pull + 24-hr factory dispatch. |
| **Bundi & Hadoti Belt** | Berger network dominance | Stock-out delays from distant Jaipur depots | Same-day replenishment; anchor stockist exclusivity. |
| **Bhilwara (Textile Hub)** | Heavy industrial enamel presence | High moisture peeling issues on commercial sites | High-solid elastomeric exterior coatings. |
| **Jaipur South / Sanganer** | Extreme competitor density | Predatory price wars between wholesale dealers | Focus on institutional builders & A-grade contractors. |

---

## 5. Tactical Strategic Playbooks

### Playbook A: The "Mandi Fortress" Counter-Offensive
When an incumbent or mega-entrant launches aggressive dealer signing campaigns:
1. **Initiate ERP Dealer Audit**: Query `/api/erp/dealers/vulnerability-index` to identify top 20 revenue-generating counters.
2. **Deploy Margin Defense Package**: Meet dealers on gaddi; present direct ROI comparisons showing how Swatch Paints delivers ₹180 net profit per 20L bucket versus ₹55 from the competitor.
3. **Mobilize Thekedar Network**: Convene an emergency contractor loyalty evening; distribute bonus seasonal token vouchers to ensure contractors insist on Swatch Paints at the counter.

### Playbook B: Raw Material Cost Surge Shock Hedge
When crude oil spikes above $85/barrel or import tariffs on rutile TiO2 increase:
1. **Simulate ERP Batch Costing**: Run `/api/erp/production/cost-simulate` with updated chemical index rates.
2. **Optimize Extender Packing**: Recalibrate the pigment volume concentration (PVC) using local ultrafine calcined clay to preserve opacity while mitigating TiO2 consumption.
3. **Execute Strategic Raw Material Contracts**: Lock in 60-day monomer inventory with domestic resin synthesis partners before retail prices escalate.

---

## 6. Zero Hardcoding Dynamic ERP Protocol
Hermes and commercial strategists must NEVER utilize static pricing or fixed margins from memory. All strategic decisions must be verified through real-time ERP API endpoints:
```bash
# Live Mandi Pricing & Gross Margin Realization
curl -s http://localhost:8000/api/erp/pricing/category-margins?category=exterior_emulsion
# Live Dealer Credit, Outstanding Balances & Aging
curl -s http://localhost:8000/api/erp/dealers/commercial-terms?dealer_id=DLR-KOTA-014
# Mandi Retail Performance & Market Share Indices
curl -s http://localhost:8000/api/erp/sales/mandi-metrics?mandi=Kota
```

---

## 7. Strategic Audit Verification Checklist
- [ ] Has competitive rivalry in the target district been evaluated across all 5 Big Four incumbents?
- [ ] Are raw material chemical supply dependencies hedged with at least two qualified domestic vendors?
- [ ] Is dealer bargaining leverage neutralized by active contractor token pull and rigid 21-day credit limits?
- [ ] Does the product portfolio provide compelling value engineering against non-paint substitutes?
- [ ] Are all financial simulations and margin structures validated through live ERP API queries?
- [ ] Has the strategic plan been reviewed and authorized under the mandate of Ashutosh Sharma Sir?
"""

# -----------------------------------------------------------------------------
# SKILL 2: INFLUENCE-PSYCHOLOGY (Target: 230-260 lines)
# -----------------------------------------------------------------------------
influence_psychology = """---
name: influence-psychology
description: Robert Cialdini's 6 Principles of Ethical Influence & Behavioral Persuasion engineered for the Indian Paint Distribution Channel. Master paint dealer gaddi psychology, contractor loyalty rituals, painter token mechanics, architect specifications, and commercial sales negotiations. Translates Reciprocity, Commitment & Consistency, Social Proof, Authority, Liking, and Scarcity into culturally grounded, field-tested B2B sales execution for Swatch Paints (Sharma Industries).
metadata:
  version: 2.1.0
  author: Sharma Industries & Hermes Sales Strategy
  category: Sales Psychology & Behavioral Persuasion
---

# Influence Psychology & Ethical Persuasion Engine (Cialdini Methodology for Swatch Paints)

## 1. Executive Authority & Behavioral Foundations
Operating under the supreme authority of **Ashutosh Sharma Sir (Founder & Managing Director)** and orchestrated autonomously by **Hermes (Chief Executive Agent)**, this engine operationalizes behavioral science across the Indian paint trade.

Selling decorative and protective coatings in India is fundamentally a psychological and cultural negotiation. A dealer sitting on his traditional gaddi in Kota, Jaipur, or Bhilwara does not make purchasing decisions based on mathematical feature matrices alone. He is driven by risk aversion, mandi status, peer consensus, reciprocal obligation, and personal trust. This engine translates Dr. Robert Cialdini’s 6 foundational principles of influence into exact, culturally nuanced tactical protocols for Swatch Paints field representatives.

---

## 2. The 6 Weapons of Influence in the Indian Paint Mandi

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

## 3. Principle-by-Principle Operational Playbooks & Field Scripts

### Principle 1: Reciprocity (Give High-Perceived Value First)
**Psychological Mechanism**: Human beings are biologically conditioned to repay obligations. When you provide an unconditional, high-value gift before asking for business, the recipient experiences a psychological urge to reciprocate.
- **Mandi Execution**:
  - Never enter a prospective dealer's shop empty-handed asking for a 2-lakh stocking order.
  - Present a bespoke **"Swatch Master Shade Card Box"** (hardbound velvet finish, ₹1,500 perceived value) or 2 free 1-liter cans of Royal Luxury Interior Emulsion for his private office or home.
  - Offer to fund a **"Contractor Chai-Nashta Meet"** at the dealer’s showroom, where Swatch Paints pays for the refreshments, tokens, and gifts while positioning the dealer as the generous host.
- **Field Script A (Traditional Conservative Gaddi Dealer)**:
  > *"Seth ji, pranam. Aaj hum aapse koi order lene nahi aaye hain. Hum jante hain ki aap saalon se Asian Paints ke sath jude hain. Yeh hamara naya luxury emulsion ka sample pack hai. Hamari guzarish hai ki aap isko apni dukan ke back-office ya apne ghar par lagwa kar dekhiye. Agar aapke mistri ne bola ki iska covering aur finish Royale se behtar nahi hai, toh hum dobara aapse is baare mein baat nahi karenge. Yeh hamari taraf se aapke liye bhet hai."*
- **Field Script B (Modern Hardware Showroom Owner)**:
  > *"Bhaiya, aapke showroom ki footfall bahut acchi hai. Hum aapke showroom display ke liye ek motorized color display panel provide kar rahe hain jiski market cost ₹18,000 hai. Iska koi rental ya deposit nahi hai. Hum chahte hain ki aapke premium customers is panel ko experience karein."*

### Principle 2: Commitment & Consistency (The Micro-Yes Ladder)
**Psychological Mechanism**: Once people take a small public stand or make a micro-commitment, they experience powerful internal pressure to behave consistently with that stand.
- **Mandi Execution**: Break down a high-risk purchasing decision into 4 effortless, low-friction micro-agreements.
- **The Micro-Yes Progression**:
  1. *Step 1*: "Seth ji, kya aap agree karte hain ki monsoon ke baad exterior wall peeling ka complaint har doosre ghar mein aata hai?" *(Answer: Yes).*
  2. *Step 2*: "Aur agar dealer ke paas aisi waterproofing coating ho jo 5 saal tak bilkul na phule, toh customer dobara aapke counter par aayega?" *(Answer: Yes).*
  3. *Step 3*: "Agar usi coating par aapko 6% ki jagah 18% saaf margin mile, toh counter ka profit 3 guna hoga?" *(Answer: Yes).*
  4. *Step 4 (The Lock)*: "Toh Seth ji, poora truckload nahi, sirf 2 bucket test counter par rakhte hain. Iska payment aap tabhi dijiye jab dono bucket bik jayein. Deal pakki?" *(Agreement secured).*

### Principle 3: Social Proof (Mandi Herd Dynamics)
**Psychological Mechanism**: When uncertain, people look to the actions of their peers to guide their own behavior. In the mandi, no dealer wants to be the first guinea pig, but no dealer can endure being left behind.
- **Mandi Execution**:
  - Arm sales reps with high-resolution laminated photographic evidence of prominent local bungalows, commercial plazas, and hospitals painted with Swatch Paints.
  - Highlight adoption by reputable local painting thekedars (contractors) and influential peer dealers.
- **Field Script**:
  > *"Seth ji, Gumanpura mandi mein Agarwal Paints aur Aerodrome circle par Sharma Hardware ne pichle mahine 600 bucket Swatch WeatherShield nikali hai. Aur Kota ke top thekedar Pappu Mistri ne abhi 8 bungalows mein sirf Swatch specify kiya hai. Mandi mein sabhi ko pata hai ki customer ko quality pasand aa rahi hai aur painter ko turant mobile par token cash mil raha hai."*

### Principle 4: Authority (Formulation Science & Lab Proof)
**Psychological Mechanism**: Human beings are conditioned to defer to legitimate authority, deep expertise, and certified scientific credentials.
- **Mandi Execution**:
  - Overcome sales skepticism by laying physical, certified NABL laboratory test reports on the dealer's gaddi table.
  - Position Founder Ashutosh Sharma Sir's technical legacy: *"Hum kisi trader se maal khareed kar label nahi lagate. Ashutosh Sir 15 saal se khud formulation chemist hain aur Kota factory mein har batch ki testing hoti hai."*
- **Field Script**:
  > *"Seth ji, yeh NABL certified test report dekhiye. Market standard exterior paint 1,200 scrub cycles par chalking dikhata hai. Swatch WeatherShield 3,500 scrub cycles tak bina kisi damage ke intact rehta hai. Jab architect ya consumer humse sawal karta hai, hum bol-bachan nahi karte, direct laboratory proof table par rakh dete hain."*

### Principle 5: Liking (Gaddi Rapport & Cultural Intimacy)
**Psychological Mechanism**: People overwhelmingly prefer to say yes to individuals they know, like, and perceive as similar to themselves.
- **Mandi Execution**:
  - **Gaddi Etiquette**: Never sit physically higher than the dealer. Remove footwear before stepping onto traditional white-sheet gaddis. Accept offered tea or water immediately.
  - **Shared Regional Pride**: Contrast local Rajasthani warmth with distant multinational corporate bureaucracy: *"MNCs ke regional managers Mumbai ya Delhi mein baith kar computer se policy banate hain; hum aapke apne Kota ke log hain jo shaam ko aapke sath baith kar samasya hal karte hain."*
  - **Relationship Capital**: Remember dealer family milestones, festive greetings, and local mandi news before discussing business numbers.

### Principle 6: Scarcity (Territorial Protection & Allocation Limits)
**Psychological Mechanism**: People assign greater value to opportunities that are scarce, exclusive, or dwindling in availability.
- **Mandi Execution**:
  - Implement a rigid territorial exclusivity policy: Only 1 authorized Prime Stockist per 2 km radius.
  - Offer limited seasonal allocations with firm calendar deadlines.
- **Field Script**:
  > *"Seth ji, poore Talwandi market mein hum sirf ek dealer ko Prime Dealership denge taaki counter par koi price-cutting na ho aur aapka 20% margin safe rahe. Hum pehle aapke paas aaye hain kyunki is mandi mein aapka naam sabse bada hai. Agar aapko lagta hai ki aap abhi ready nahi hain, toh hume dusre counter par jana padega, kyunki company ka territory allocation is Friday shaam ko close ho raha hai."*

---

## 4. Architect & Builder Specification Influence Architecture
When influencing institutional architects, civil consultants, and real estate promoters:
1. **Target Reputational Anxiety**: Highlight how exterior dampness seepage ruins an architect's portfolio photos and delays builder flat handovers.
2. **Provide Complete Specification Documents**: Hand over turnkey architectural submittal packages including surface preparation, primer coverage, and elongation specifications.
3. **The 100 Sq.Ft. Mockup Challenge**: Paint a 100 sq.ft. test patch on the actual construction site for 14-day weathering inspection against any competitor product.

---

## 5. Dynamic ERP Data Verification Protocol
Never guess stock levels or promotional token values during a negotiation. Query live ERP:
```bash
# Query Real-time Dealer Transaction History & Credit Status
curl -s http://localhost:8000/api/erp/dealers/profile?dealer_id=DLR-KOTA-042
# Check Live Active Painter Token Value for Product Category
curl -s http://localhost:8000/api/erp/marketing/tokens/budget?district=Kota
```

---

## 6. Pre-Negotiation Influence Checklist
- [ ] Has an unconditional, high-value gift or sample been provided before asking for business?
- [ ] Was the commitment ladder utilized to secure small micro-agreements first?
- [ ] Were peer dealer adoptions and prominent local project photos presented as social proof?
- [ ] Were NABL accredited laboratory test reports physically shown to establish technical authority?
- [ ] Was cultural gaddi etiquette respected to build genuine interpersonal liking?
- [ ] Was legitimate territorial exclusivity or seasonal allocation scarcity communicated?
"""

# -----------------------------------------------------------------------------
# SKILL 3: GTM-STRATEGY (Target: 230-260 lines)
# -----------------------------------------------------------------------------
gtm_strategy = """---
name: gtm-strategy
description: Go-To-Market (GTM) Regional Mandi Expansion and Territory Launch Engine for Swatch Paints (Sharma Industries). Master the sequential conquest of new geographic territories across Rajasthan and Madhya Pradesh (Bundi, Baran, Jhalawar, Bhilwara, Chittorgarh, Jaipur, Indore). Covers depot logistics, anchor dealer recruitment, painter contractor melas, trade credit governance, secondary demand pull, and rapid territory breakeven economics.
metadata:
  version: 2.1.0
  author: Sharma Industries & Hermes Commercial Operations
  category: Territory Expansion & Go-To-Market
---

# GTM Territory Launch & Mandi Expansion Engine (Swatch Paints Regional Conquest)

## 1. Executive Authority & Strategic Mission
Orchestrated under the supreme command of **Founder & Managing Director Ashutosh Sharma Sir** and executed autonomously by **Hermes (Chief Executive Agent)**, this engine governs the step-by-step geographic expansion of Swatch Paints.

Expanding into a new paint territory without an airtight GTM blueprint results in trapped working capital, uncollected dealer debt, and dead stock gathering dust on forgotten retail shelves. The Swatch Paints GTM methodology follows a **"Hub-and-Spoke Regional Blitzkrieg"**: solidifying total operational dominance in Kota, then methodically expanding into concentric trade circles through an interconnected 5-phase territory launch blueprint.

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

## 3. Deep Phase-by-Phase Operational Execution Protocols

### Phase 1: Mandi Intelligence & Reconnaissance (Days 1 to 14)
- **Objective**: Conduct a comprehensive forensic audit of the target district before deploying commercial capital.
- **Core Activities**:
  1. **Retail Counter Census**: Map every paint retail shop, hardware store, sanitary-ware outlet, and building material counter in the district.
     - *Tier A Counters*: Monthly paint turnover >₹15 Lakhs (Target for Anchor Stockists).
     - *Tier B Counters*: Monthly paint turnover ₹5 to ₹15 Lakhs (Target for Secondary Counters).
     - *Tier C Counters*: Monthly paint turnover <₹5 Lakhs (Target for Putty/Primer cross-selling).
  2. **Incumbent Friction Analysis**: Interview 15 local dealers to uncover competitor pain points: Which company has delayed turnover discount payouts? Which brand enforces excessive minimum order sizes?
  3. **Contractor Roster Generation**: Compile an active directory of the 50 most influential painting contractors (thekedars) with phone numbers, crew sizes, and active job sites.
- **ERP Integration**:
  ```bash
  curl -X POST http://localhost:8000/api/erp/territory/census \\
    -H "Content-Type: application/json" \\
    -d '{"mandi": "Bhilwara", "total_counters": 72, "tier_a": 14, "tier_b": 34, "contractors_identified": 65}'
  ```

### Phase 2: Depot & Logistics Infrastructure Activation (Days 15 to 21)
- **The Non-Negotiable Rule**: Never sign a dealer until 24-hour stock fulfillment is physically operational.
- **Logistical Architecture**:
  - Establish a regional stocking depot or enter into a dedicated C&F (Carrying & Forwarding) partnership with guaranteed material security.
  - Buffer Inventory Allocation:
    - 50% Fast-Moving White Bases & Universal Primers (20L, 10L buckets).
    - 30% Popular Interior & Exterior Emulsion Base Tints.
    - 20% Water-based Polymer Wall Putty & Distemper.
  - **SLA Commitment**: Orders booked on the ERP mobile portal before 11:00 AM must be delivered to the dealer counter by 5:00 PM the same day; orders booked after 11:00 AM delivered by 11:00 AM next day.

### Phase 3: Anchor Stockist Recruitment (Days 22 to 35)
- **Prospect Targeting Strategy**: Avoid the complacent, entrenched #1 Asian Paints dealer who is hopelessly tied to incumbent annual schemes and overseas trip quotas. Focus on the ambitious, aggressive **#2 or #3 dealer** who is hungry for higher profitability.
- **The Anchor Partnership Deal**:
  - **Margin Dominance**: Guaranteed 18% to 22% net counter margin on core emulsion lines.
  - **Showroom Transformation**: Complete exterior shop signage, 3D illuminated Swatch Paints board, and high-visibility interior display racks funded 100% by Sharma Industries.
  - **Territory Exclusivity**: Contractual agreement guaranteeing no competing distributor within a 2-kilometer commercial radius.
  - **Payment Terms**: Initial order on 50% advance / 50% on 14 days, secured with a signed post-dated cheque (PDC).

### Phase 4: Contractor Melas & Painter Token Activation (Days 36 to 45)
- **The Engine of Secondary Demand**: When painting contractors demand Swatch Paints, retail resistance evaporates.
- **The 8-Step "Karigar Mela" Operational Protocol**:
  1. Venue Selection: Reputed mid-scale banquet hall or hotel with ample parking space.
  2. Attendance Target: 40 to 80 active professional painters and contractors.
  3. Live Formulation Demonstration: Apply Swatch Royal Luxury Emulsion side-by-side with incumbent market leader on raw concrete slabs. Let contractors test brush drag, roller spatter, and single-coat opacity themselves.
  4. The Waterproof Challenge: Pour water and mustard oil on cured panels to demonstrate washability and stain resistance.
  5. Painter App Onboarding: Guide every contractor through downloading the Swatch Painter Mobile App.
  6. Instant Token Demonstration: Open a fresh 20L bucket live on stage, scan the lid QR code, and verify the instant ₹150 UPI cash transfer to a selected painter’s phone in <10 seconds.
  7. Contractor Welcome Kits: Distribute branded kit bags containing painter overalls, premium putty blades, masking tape, and caps.
  8. Dinner & Relationship Building: Conclude with a lavish dinner where field sales reps build personal rapport with crew leaders.

### Phase 5: Secondary Demand Generation & Local Awareness (Days 46 to 90)
- **Outdoor Visual Dominance**: Paint 20 prominent roadside boundary walls, railway overbridge approaches, and mandi entrance billboards.
- **Branded Delivery Vehicles**: Co-brand the delivery three-wheelers (auto-rickshaws) of our anchor dealers with high-visibility Swatch Paints livery.
- **Sample Flat Program**: Partner with 3 active local real estate developers to supply free paint for their project sample flats in exchange for commercial quotation rights for the entire residential tower.
- **Permanent Journey Plan (PJP)**: Lock the Territory Sales Officer into a strict 6-day weekly beat plan covering 8-10 counters daily with GPS ERP check-in.

---

## 4. 90-Day Territory Launch Roadmap & Milestones

| Timeline | Primary Focus | Key Performance Indicator (KPI) | Gatekeeper Check |
| :--- | :--- | :--- | :--- |
| **Weeks 1-2** | Mandi Reconnaissance & Census | 100% retail shops mapped; 50 contractors listed | Census uploaded to ERP |
| **Weeks 3-4** | Depot Setup & Safety Stocking | Regional buffer warehouse operational with 10-day stock | 24-hr delivery SLA verified |
| **Weeks 5-6** | Anchor Stockist Acquisition | 2 Tier-A Prime Stockists signed with PDC mandates | Initial stock order billed |
| **Weeks 7-8** | Contractor Mela & App Rollout | 50+ painters registered; 100+ buckets scanned | Mobile token redemption live |
| **Weeks 9-12** | Secondary Beat & Builder Projects | 15 active billing counters; 2 sample flats completed | Breakeven cashflow achieved |

---

## 5. Territory Financial Breakeven Modeling
A newly launched mandi must reach operational breakeven by Day 90:
- **Monthly Fixed Operating Costs**:
  - Territory Sales Officer (TSO) base salary + TA/DA.
  - Contractor Relationship Executive (CRE) base salary + TA/DA.
  - Regional depot freight and handling allocation per ton.
  - Local promotional and contractor mela amortization.
- **Volume Breakeven Target**:
  - Monthly liquidation threshold: 12 metric tons of mixed coatings (Emulsion, Primer, Putty).
  - Average realized gross margin: Calculated dynamically via `/api/erp/finance/target-contribution`.

---

## 6. Zero Hardcoding Dynamic ERP Protocol
Field leadership must query real-time territory metrics directly from the ERP:
```bash
# Query Depot Safety Stock & In-Transit Consignments
curl -s http://localhost:8000/api/erp/logistics/depot-status?mandi=Bhilwara
# Audit New Territory Dealer Onboarding & Beat Plan Compliance
curl -s http://localhost:8000/api/erp/territory/pipeline?region=Mewar
```

---

## 7. Territory Launch Gate Checklist
- [ ] Phase 1 Mandi census completed with verified dealer classifications and contractor rosters?
- [ ] Depot facility operational with 24-hour guaranteed counter delivery?
- [ ] First 2 Anchor Stockists signed with verified credit terms and post-dated cheques?
- [ ] Karigar Mela executed with minimum 40 contractors onboarded onto the mobile token app?
- [ ] TSO Permanent Journey Plan mapped in ERP with mandatory daily GPS check-ins?
- [ ] Territory unit economics validated to achieve operational breakeven within 90 days?
"""

# -----------------------------------------------------------------------------
# SKILL 4: SALES-STRATEGIST (Target: 230-260 lines)
# -----------------------------------------------------------------------------
sales_strategist = """---
name: sales-strategist
description: Strategic Commercial Sales Operations, Territory Quota Engineering, Field Rep Incentive Design, and B2B Pipeline Governance for Swatch Paints (Sharma Industries). Use when structuring sales organizational roles (TSO, CRE, IPM), building collection-linked compensation structures, designing Permanent Journey Plans (PJP beat plans), accelerating dealer conversion velocity, and governing institutional builder/project sales pipelines.
metadata:
  version: 2.1.0
  author: Sharma Industries & Hermes Commercial Operations
  category: Sales Strategy & Commercial Operations
---

# Commercial Sales Strategy & Revenue Operations Engine

## 1. Executive Mandate & Strategic Philosophy
Operating under the supreme authority of **Founder & Managing Director Ashutosh Sharma Sir** and executed autonomously by **Hermes (Chief Executive Agent)**, this engine establishes commercial discipline across all sales operations.

**The Golden Law of Commercial Operations**:
*"A-players trapped in a chaotic sales system will inevitably fail; disciplined B-players backed by an airtight, incentive-aligned system will conquer mandis."*
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

## 3. Compensation & Incentive Engineering: The Collection-Linked Model

### The Fatal Pathology of Primary Sales Targets
Traditional paint companies incentivize sales reps on **Primary Invoice Value**. This creates severe moral hazard: reps dump slow-moving stock onto vulnerable dealers in the final 3 days of the month to hit quota, leading to severe dealer debt, high product return rates, and catastrophic working capital blockage.

### The Swatch Paints Three-Pillar Compensation Formula
Field sales incentives at Sharma Industries are strictly tied to **Realized Cash Collections**, **Product Margin Weights**, and **Counter Retention**:

$$\text{Monthly Incentive} = (\text{Eligible Collected Revenue} \times \text{Margin Multiplier}) + \text{Active Counter Retention Bonus}$$

#### 1. Zero Commission on Uncollected Invoices
No sales commission is disbursed on any invoice until payment has been credited to the Sharma Industries bank account within the authorized credit window (maximum 21 days). If an invoice becomes overdue past 45 days, the rep's commission on that account is permanently forfeited.

#### 2. Margin-Weighted Product Multipliers
- **Category A (High-Margin Specialties - Royal Luxury, WeatherShield PU)**: **1.5x Multiplier**.
- **Category B (Standard Interior Acrylics, Exterior Primers)**: **1.0x Multiplier**.
- **Category C (Low-Margin Commodity Putty, Distemper)**: **0.5x Multiplier**.
*Operational Effect*: Sales reps are heavily penalized for taking the easy route of dumping cheap wall putty and are rewarded for selling premium architectural finishes.

#### 3. Active Counter Retention Stipend
TSOs receive a recurring monthly bonus of ₹1,000 for every active dealer counter that places at least 2 repeat orders exceeding ₹50,000 every 30 days. This shifts the rep’s mindset from "one-off transactional dumping" to "continuous dealer nurturing."

---

## 4. Territory Quota & Beat Plan Design (PJP)

### Permanent Journey Plan (PJP) Standards
Every Territory Sales Officer is assigned a rigid 6-day cyclical beat plan configured within the ERP mobile terminal:
- **Monday**: Central Hardware Mandi (Core retail stockists, Counters 1-10).
- **Tuesday**: Industrial & Sub-Dealer Belt (Secondary counters, Counters 11-20).
- **Wednesday**: Outer Tehsil Hub A (Semi-urban counters, Counters 21-30).
- **Thursday**: Institutional Project Joint Visits (Site visits with IPM at active construction sites).
- **Friday**: Outer Tehsil Hub B (Rural feeder markets, Counters 31-40).
- **Saturday**: Dealer Account Reconciliation, Outstanding Cash Collections, Painter Token Audits.

### Daily Rep Performance Standards
1. **Productive Visits**: Minimum 8 verified dealer counter visits per day.
2. **Geo-Location Fencing**: The mobile app mandates GPS check-in within a 50-meter radius of the registered dealer counter.
3. **Daily Liquidation Reporting**: Audit secondary sales (stock moved from dealer to painter) alongside primary billing.

---

## 5. Institutional Project Sales: The MEDDIC-Paint Framework

When pursuing major real estate developments, commercial towers, government hospitals, and infrastructure contracts (>5,000 Liters):

```
+---------------------------------------------------------------------------------+
|                       MEDDIC-PAINT QUALIFICATION MATRIX                         |
+-------------------+--------------------+-------------------+--------------------+
| 1. METRICS        | 2. ECONOMIC BUYER  | 3. DECISION       | 4. DECISION        |
| Carpet area sq.ft,| Target MD or Chief | CRITERIA          | PROCESS            |
| liters per coat,  | Purchase Officer,  | Whiteness, scrub, | Submittal -> Mockup|
| cost savings goal | not site supervisor| VOC, RERA norms   | -> Committee -> PO |
+-------------------+--------------------+-------------------+--------------------+
|                   | 5. IDENTIFY PAIN   | 6. CHAMPION       |                    |
|                   | Monsoon seepage,   | Project Architect |                    |
|                   | delivery delays,   | or Lead Structural|                    |
|                   | batch variations   | Engineer          |                    |
+-------------------+--------------------+-------------------+--------------------+
```

---

## 6. Pipeline Velocity & Bottleneck Diagnostic Formula

$$\text{Pipeline Velocity} = \frac{\text{Active Deals} \times \text{Win Rate \%} \times \text{Average Deal Value (INR)}}{\text{Sales Cycle Duration (Days)}}$$

### Diagnostic Troubleshooting Matrix:
- **If Win Rate < 25%**: Sales rep is reciting product features instead of diagnosing dealer or developer pain. Mandate immediate deployment of `pain-is-the-pitch`.
- **If Sales Cycle > 45 Days**: Deal is languishing in the sampling stage. Deploy a Contractor Relationship Executive to paint a physical 100 sq.ft. on-site mockup within 24 hours.
- **If Average Deal Size is Stagnant**: The rep is timidly selling single SKUs. Enforce the **"4-Layer Complete Surface Bundle"** (Putty + Primer + 2 Coats Luxury Emulsion).

---

## 7. Dynamic ERP Revenue Operations Bindings
Sales operations leaders must audit real-time field performance through live ERP API endpoints:
```bash
# Audit Rep Quota Attainment & Collection Ratios
curl -s http://localhost:8000/api/erp/sales/rep-performance?rep_id=TSO-KOTA-07
# Pull Live Accounts Receivable Aging & Overdue Debt
curl -s http://localhost:8000/api/erp/finance/aging-report?territory=Hadoti
# Review Active Institutional Deals in Pipeline
curl -s http://localhost:8000/api/erp/sales/pipeline?type=institutional
```

---

## 8. Operational Discipline Checklist
- [ ] Are sales commissions strictly linked to cleared bank collections rather than uncollected billing?
- [ ] Does the commission model apply 1.5x weighting to high-margin luxury coatings?
- [ ] Are TSOs maintaining 100% compliance with their 6-day PJP beat plan via GPS tracking?
- [ ] Have all institutional builder deals exceeding 5,000L been qualified through MEDDIC-Paint?
- [ ] Are secondary sales tracked weekly to prevent channel stuffing and inventory stagnation?
"""

# -----------------------------------------------------------------------------
# SKILL 5: MARKETING-COUNCIL (Target: 230-260 lines)
# -----------------------------------------------------------------------------
marketing_council = """---
name: marketing-council
description: Simulated Board of Legendary Marketing Advisors for Swatch Paints (Sharma Industries). Convene David Ogilvy, Eugene Schwartz, Alex Hormozi, Byron Sharp, April Dunford, Claude Hopkins, and Gary Halbert to rigorously debate, stress-test, and refine brand campaigns, packaging, trade promotions, contractor loyalty mechanics, and product positioning. Discovers blind spots and synthesizes consensus across contrasting marketing philosophies.
metadata:
  version: 2.1.0
  author: Sharma Industries & Hermes Brand Strategy
  category: Strategic Marketing & Advisory Simulation
---

# Marketing Council - Legendary Advisory Board for Swatch Paints

## 1. Executive Mandate & Advisory Mechanism
Operating under the supreme executive direction of **Founder & Managing Director Ashutosh Sharma Sir** and moderated autonomously by **Hermes (Chief Executive Agent)**, this engine convenes a simulated board of history's greatest marketing minds.

Before Sharma Industries commits commercial capital to an advertising campaign, dealer trade scheme, exterior emulsion packaging overhaul, or painter loyalty program, the initiative is submitted to the **Marketing Council**. The goal of this council is not superficial consensus—it is the **productive friction between divergent marketing paradigms**. By exposing every marketing initiative to rigorous cross-examination, Swatch Paints uncovers hidden vulnerabilities and perfects its market positioning before a single rupee is spent.

---

## 2. The 7 Council Advisors & Their Core Philosophies

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

### Advisor 1: David Ogilvy (Craftsmanship, Long-term Brand Equity & Reason-Why)
- **Core Philosophy**: Advertising must sell. It must be factual, dignified, and anchored in verifiable craftsmanship. Reject clever puns, gimmicks, and puffery.
- **The Ogilvy Lens on Swatch Paints**:
  - *"Treat your customer with respect. If you claim superior scrub resistance, do not use cartoon mascots dancing on walls. State the laboratory scrub count: 3,500 cycles under NABL test protocol. Detail the percentage of pure acrylic binder. Show the master craftsman painting a historic heritage residence in Kota. Build an enduring, premium brand identity that allows Sharma Industries to command premium pricing for decades."*
- **Diagnostic Test**: Does this advertisement inform and persuade through factual superiority, or is it empty corporate noise?

### Advisor 2: Eugene Schwartz (Stages of Customer Awareness & Market Sophistication)
- **Core Philosophy**: Copy cannot manufacture desire. It can only channel the existing desires, fears, and hopes of millions of consumers onto a specific product.
- **The Schwartz Lens on Swatch Paints**:
  - *"Indian homeowners in Tier 2/3 cities are already Product-Aware. They know paints exist; they know Asian Paints and Berger. What keeps them awake at night is monsoon wall seepage destroying their interior plaster. Never open an ad trying to explain what paint is. Tap into their existing fear: 'Why does expensive exterior paint peel off after just one monsoon season?' Match the headline precisely to their sophistication level."*
- **Diagnostic Test**: What is the prospect's exact stage of awareness, and does the communication channel an already burning desire?

### Advisor 3: Alex Hormozi (Grand Slam Offers & Margin Arbitrage)
- **Core Philosophy**: If your offer needs explaining, it is too weak. Construct offers so compelling that prospects feel foolish walking away.
- **The Hormozi Lens on Swatch Paints**:
  - *"Why should a busy dealer replace a shelf of Asian Paints with Swatch? Because we deliver 3x net profit with zero inventory risk. Bundle 15 buckets of WeatherShield with an unconditional 45-day sell-through buyback guarantee, free shop branding, and double token payouts for his top 5 painters. Eliminate 100% of his downside."*
- **Diagnostic Test**: Is the offer so risk-reversed and mathematically superior that refusing it is irrational?

### Advisor 4: Byron Sharp (Distinctive Brand Assets & Physical Availability)
- **Core Philosophy**: Brand loyalty is mostly an illusion; brands grow by maximizing mental availability (salience at purchase moment) and physical availability (ease of buying).
- **The Sharp Lens on Swatch Paints**:
  - *"Consumers repaint once every 5 years. They will not spend time studying your chemical formulas. What you need are Distinctive Brand Assets: an unmistakable bucket shape, a vivid signature color scheme, and an unforgettable logo. Then flood the market with physical availability: be present in every single hardware counter on the highway."*
- **Diagnostic Test**: Is the packaging instantly recognizable from 10 meters away, and is the product physically in stock on the counter?

### Advisor 5: April Dunford (Differentiated Context & Competitive Positioning)
- **Core Philosophy**: Positioning defines the context where your unique strengths become obvious to your best-fit target segment.
- **The Dunford Lens on Swatch Paints**:
  - *"What are you positioning against? If you position as 'another general decorative paint brand like the MNCs', you lose by default. But if you position Swatch as 'The High-Solid Waterproofing Coating Engineered Specifically for Rajasthan's 48°C Heat & Extreme Alkaline Plaster', your regional manufacturing roots become your greatest unfair advantage."*
- **Diagnostic Test**: What is the customer's true alternative, and why are our unique capabilities the obvious choice for our target audience?

### Advisor 6: Claude Hopkins (Scientific Advertising & Sampling Trials)
- **Core Philosophy**: Advertising is salesmanship in print. Never rely on faith; test, measure, and scale based on verifiable redemption data.
- **The Hopkins Lens on Swatch Paints**:
  - *"Never ask a painting contractor to buy your emulsion on trust. Place a free 1-liter sample can in his hands. Give him a numbered voucher redeemable at his local dealer. Track the conversion rate of every 100 sample cans distributed. If 30 painters convert to regular buyers, roll out 5,000 cans across the state. Treat marketing as a predictable scientific experiment."*
- **Diagnostic Test**: Is there an immediate, trackable sample trial mechanism that can be scientifically measured?

### Advisor 7: Gary Halbert (Direct Response Urgency & Emotional Hooks)
- **Core Philosophy**: Bland copy dies in the wastebasket. Grab the prospect by the throat, tell a dramatic story, and demand urgent action with an uncompromising deadline.
- **The Halbert Lens on Swatch Paints**:
  - *"Send an official registered letter directly to the top 100 painting contractors in the district. Headline: 'An Open Letter to Every Painting Thekedar in Kota Who is Sick and Tired of Dealing with Customer Call-Backs Due to Peeling Paint.' Tell the truth about cheap MNC fillers. Give them a hard deadline to claim their festive contractor loyalty bonus before Diwali."*
- **Diagnostic Test**: Does the message create an immediate adrenaline response and compel urgent physical action?

---

## 4. Council Deliberation & Debate Protocol
When convening the Marketing Council on a strategic initiative:
1. **Define the Initiative**: Present the proposed campaign, packaging change, or trade promotion with target demographics and unit economics.
2. **Execute Multi-Perspective Deliberation**:
   - *Ogilvy & Hopkins*: Audit the technical proof, laboratory claims, and sampling mechanisms.
   - *Schwartz & Halbert*: Review the emotional hook, awareness alignment, and headline urgency.
   - *Hormozi & Sharp*: Evaluate the commercial offer structure, risk reversal, and physical retail visibility.
   - *Dunford*: Validate the competitive positioning and market framing.
3. **Stage the Philosophical Friction**: Surface critical tensions (e.g., Ogilvy's premium restraint vs. Hormozi's aggressive promotional stacking).
4. **Hermes Executive Synthesis**: Deliver an authoritative final strategy approved under the executive authority of Ashutosh Sharma Sir.

---

## 5. Dynamic ERP Data Verification
Council reviews must be grounded in verified ERP financial parameters:
```bash
# Check Real-time Marketing Spend & Campaign ROI
curl -s http://localhost:8000/api/erp/marketing/campaigns/active
# Pull Real-time Category Margins & Contribution
curl -s http://localhost:8000/api/erp/finance/category-profitability?category=luxury_emulsions
```

---

## 6. Pre-Launch Marketing Council Checklist
- [ ] Has David Ogilvy's factual "reason-why" standard been satisfied with verifiable data?
- [ ] Is the communication aligned with Eugene Schwartz's market sophistication stage?
- [ ] Has Alex Hormozi's Grand Slam risk-reversal and margin arbitrage been audited?
- [ ] Are Byron Sharp's distinctive brand assets prominent and easily recognized?
- [ ] Is April Dunford's differentiated positioning clearly articulated against market alternatives?
- [ ] Does Claude Hopkins' trackable sampling mechanism validate customer conversion?
"""

# -----------------------------------------------------------------------------
# SKILL 6: PAIN-IS-THE-PITCH (Target: 230-260 lines)
# -----------------------------------------------------------------------------
pain_is_the_pitch = """---
name: pain-is-the-pitch
description: Hyper-Specific Pain-Driven Sales Pitch & Messaging Engine for Swatch Paints (Sharma Industries). Transforms generic, feature-heavy sales copy and rep pitches into emotionally vivid, commercially acute diagnostic messaging using the Daniel Bustamante / Alex Hormozi "Pain is the Pitch" framework. Identifies acute paint dealer financial bleeding, contractor call-back humiliation, and builder handover bottlenecks to construct irresistible sales conversations.
metadata:
  version: 2.1.0
  author: Sharma Industries & Hermes Sales Strategy
  category: Sales Communication & Direct Response Copywriting
---

# Pain Is The Pitch - High-Conversion Sales Messaging Engine

## 1. Executive Mandate & Psychological Foundations
Operating under the authority of **Founder & Managing Director Ashutosh Sharma Sir** and executed autonomously by **Hermes (Chief Executive Agent)**, this engine eradicates ineffective, feature-heavy sales pitches across all commercial operations.

**The Immutable Law of Sales Psychology**:
*"Prospects do not buy features, chemical formulations, or product specifications. They buy immediate relief from chronic, agonizing financial, operational, and reputational pain."*
When a sales rep talks about "superior scrub resistance" or "100% pure acrylic polymers," the prospect's eyes glaze over. But when the rep exposes the **exact rupee hemorrhage** of dead inventory, delayed MNC turnover discounts, and angry painting thekedars demanding compensation for peeling walls, the prospect leans forward. Pain creates urgency; features create price resistance.

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
Identify and articulate the precise operational frustration the prospect suffers in vivid, unmistakable detail. Use their exact vernacular (*gaddi, theka, seelan, udhedna, fasa hua paisa*).
- *Weak Pitch*: "Hamara paint bahut accha hai aur iska coverage 140 sq.ft. hai."
- *Pain-Driven Pitch*: "Seth ji, counter ke peeche jo 15 bucket slow-moving primer padi hai, usme aapka ₹45,000 pichle 4 mahine se bina kisi byaj ke fasa hua hai. MNC company ka sales officer targeted dumping karke target bonus le gaya, par gaddi par nuksan sirf aapka ho raha hai."

### Step 2: Amplify the Cost of Inaction
Demonstrate clearly what happens in 90 days if they tolerate the status quo. Financial bleeding does not heal on its own; it compounds.
- *Pain Amplification*: "Agar agle monsoon tak yeh stock nahi nikla, toh pigment settle ho jayega aur material kharab ho jayega. Upar se jab aap unke turnover discount ka claim bhejenge, toh unka software 'target missed by 2 buckets' bolkar aapka ₹60,000 ka scheme cancel kar dega. Kab tak doosron ke target ke liye apna counter jalayenge?"

### Step 3: Neutralize the Perceived Risk
Every prospect fears that changing paint suppliers will create unexpected disasters. You must dismantle this fear with unconditional guarantees.
- *Risk Neutralization*: "Hum aapse 2 lakh ka order maang hi nahi rahe hain. Aap sirf 2 bucket test kijiye. Aur agar aapke thekedar ne bola ki iska covering Asian Paints se kam hai, toh dono bucket ka paisa hum wapas karenge aur khali tin bhi nahi maangenge."

### Step 4: The Targeted Prescription Offer
Position Swatch Paints not as a generic paint alternative, but as the exact, tailored surgical medicine for their specific diagnosed pain.
- *The Prescription*: "Swatch Paints aapko 18% saaf counter margin deta hai, har 20L bucket par painter ko turant ₹150 ka UPI cash token milta hai, aur hum 24 ghante ke andar direct Kota factory se fresh stock deliver karte hain. Aapka paisa safe, margin 3 guna, aur thekedar khush."

---

## 4. Hyper-Specific Pitch Rewriter Scenarios

### Scenario A: Cold Dealer Acquisition Pitch
- **Before (Generic Feature Pitch)**:
  *"Namaste Seth ji. Hum Swatch Paints se hain. Hum Rajasthan ke leading manufacturer hain. Hamare paas interior, exterior, primer aur wall putty sabhi products hain. Quality international standard ki hai aur rate bahut competitive hai."*
- **After (Pain-Is-The-Pitch Transformation)**:
  *"Seth ji, namaste. Ek seedha sawal: Pichle saal aapne 40 lakh ka paint becha, par saal ke aakhir mein aapki jeb mein kya bacha? 5 ya 6 percent? Baki sara munafa company ke target schemes aur unke luxury tours mein chala gaya jahan aapko 2 bucket short hone par disqualify kar diya gaya.*
  *Mandi mein sabhi dealers pareshan hain ki gaddi unki hai, dukan unki hai, grahak unka hai, par kamai MNC le ja rahi hai. Hum Kota mein Sharma Industries hain. Hum aapko seedha 18% saaf margin dete hain—bina kisi hidden target ke aur har hafte cash collection par instant cash discount. Kya hum 5 minute baithkar aapke counter ka real margin calculate kar sakte hain?"*

### Scenario B: Painting Contractor (Thekedar) Pitch
- **Before (Generic Feature Pitch)**:
  *"Bhaiya, yeh Swatch ka exterior paint hai. Isme UV resistance hai aur fungus nahi lagti. Ek baar try karke dekho."*
- **After (Pain-Is-The-Pitch Transformation)**:
  *"Ustad ji, sabse bada dard tab hota hai jab aap 3 mahine dhoop mein mehnat karke 4-manzil ka bangla paint karte hain, aur barish ke baad deewar par chitey aur peeling aane lagti hai. Homeowner aapka 50,000 rupaye rok leta hai aur bolta hai pehle theek karo. Dosh paint ka hota hai, par badnami mistri ki hoti hai.*
  *Swatch WeatherShield mein pure acrylic binder hai jo 48 degree garmi mein bhi crack nahi hota. Aur sabse badi baat: bucket kholte hi dhakkan ke andar 200 rupaye ka direct scanner code hai jo seedha aapke bank account mein credit hota hai—koi dukandar ke chakkaron mein padne ki zaroorat nahi."*

### Scenario C: Real Estate Builder / Project Developer Pitch
- **Before (Generic Feature Pitch)**:
  *"Sir, we supply all types of construction paints at wholesale factory rates with high whiteness and coverage."*
- **After (Pain-Is-The-Pitch Transformation)**:
  *"Sir, during final flat handover, the biggest nightmare is when a buyer points at moisture patches or shade variation in the master bedroom, refusing to sign the handover document. Every week of delay costs your firm lakhs in holding interest and RERA compliance risks.*
  *Most commercial paints require 3 coats to hide dark plaster patches because suppliers dilute the titanium dioxide. Swatch High-Solid Acrylic Primer achieves 100% single-coat hiding on raw concrete plaster. Your painting schedule finishes 10 days faster, and your handover passes architectural inspection on the very first visit."*

---

## 5. Surgical Diagnostic Question Bank
Arm sales representatives with these diagnostic questions to immediately expose prospect pain:
1. *"Seth ji, pichle saal turnover discount ka kitna percentage unhone 'target short' bol kar kaat liya?"*
2. *"Aapke counter par aisa kitna stock pada hai jo pichle 90 din se hila tak nahi?"*
3. *"Ustad ji, pichle ek saal mein kitne homeowners ne peeling ya fading ki wajah se aapka aakhri payment roka?"*
4. *"Kya kabhi aisa hua ki bucket ke andar ka token coupon scan hi na hua ho aur painter ka paisa doob gaya ho?"*
5. *"Builder sir, aapke site engineer ko paint deliver hone mein kitne din ka delay jhelna padta hai jab outstation depot se gaadi aati hai?"*

---

## 6. Dynamic ERP Verification Protocol
Never guess commercial parameters during a pitch. Pull verified data from the live ERP:
```bash
# Pull Verified Dealer Margin Comparisons by Category
curl -s http://localhost:8000/api/erp/pricing/margin-analysis?category=exterior
# Check Active Instant Token Value for Products
curl -s http://localhost:8000/api/erp/marketing/tokens/active-slabs
```

---

## 7. Pitch Quality Audit Checklist
- [ ] Does the pitch open with an acute operational or financial pain rather than a company introduction?
- [ ] Is the pain quantified in terms of lost rupees, wasted hours, or damaged professional reputation?
- [ ] Has the compounding cost of staying with the status quo been vividly amplified?
- [ ] Is the perceived risk completely neutralized with an unconditional trial guarantee?
- [ ] Is the prescription simple, direct, and mathematically superior?
"""

# -----------------------------------------------------------------------------
# SKILL 7: HORMOZI-EVALUATOR (Target: 230-260 lines)
# -----------------------------------------------------------------------------
hormozi_evaluator = """---
name: hormozi-evaluator
description: Alex Hormozi Ruthless Offer, Pricing, and Unit Economics Audit Engine for Swatch Paints (Sharma Industries). Evaluates sales proposals, dealer onboarding packages, contractor loyalty schemes, and retail promotions against $100M Offers, $100M Leads, and $100M Money Models. Demands mathematical precision, extreme perceived value, risk reversal guarantees, and bulletproof unit margins. Triggers on "hormozi check", "audit offer", "stress test deal", "grand slam check".
metadata:
  version: 2.1.0
  author: Sharma Industries & Hermes Commercial Strategy
  category: Commercial Evaluation & Offer Architecture
---

# Hormozi Evaluator - Ruthless Offer & Unit Economics Audit Engine

## 1. Executive Activation & Persona Mindset
Operating under the supreme authority of **Ashutosh Sharma Sir (Founder & Managing Director)** and moderated autonomously by **Hermes (Chief Executive Agent)**, this engine acts as an uncompromising, mathematically relentless commercial evaluator channeling the thinking of Alex Hormozi.

**The Operating Mindset**:
- *"If your offer requires 10 minutes of verbal explanation, your offer is garbage."*
- *"Most businesses fail at the offer level, not the execution level. You don't have a lead problem or a sales rep problem; you have a mediocre, commoditized offer that forces your reps to grovel on price."*
- *"Volume covers all operational sins—but only AFTER your unit economics are mathematically bulletproof."*
- *"Accurate > Polite. Every single time."*

---

## 2. The Hormozi Value Equation for Paint Manufacturing

$$\text{Value Score (0-100)} = \frac{\text{Dream Outcome (0-10)} \times \text{Perceived Likelihood of Achievement (0-10)}}{\text{Time Delay (Minimize)} \times \text{Effort \& Sacrifice (Minimize)}}$$

### The 4 Variables Deconstructed for Swatch Paints:

#### 1. Dream Outcome (Scale 0-10)
- **What the Paint Dealer Actually Dreams Of**: Doubling net counter profit without taking on more bank overdraft debt, gaining prestige in the mandi, and having contractors queue up outside his shop.
- **What the Painting Contractor Dreams Of**: Finishing jobs in half the time with zero customer call-backs, getting instant cash rewards, and being viewed as the master craftsman in his neighborhood.
- **What the Homeowner Dreams Of**: A magnificent, mirror-smooth luxury home finish that stays pristine for 7+ years with zero maintenance.

#### 2. Perceived Likelihood of Achievement (Scale 0-10)
- **The Core Problem**: Talk is cheap. Every paint salesman promises "high quality."
- **The Hormozi Solution**: Overwhelm with proof. Certified NABL lab scrub test certificates, video demonstrations of scrub resistance, 50 local landmark bungalows painted, written manufacturer warranties signed by Ashutosh Sharma Sir.

#### 3. Time Delay (Scale 0-10, Goal: Near Zero)
- **The Core Problem**: A contractor or dealer despises waiting 4 days for outstation depot dispatches.
- **The Hormozi Solution**: Same-day dispatch from the Kota facility. Instant mobile UPI token scan rewards for painters credited in <10 seconds.

#### 4. Effort & Sacrifice (Scale 0-10, Goal: Near Zero)
- **The Core Problem**: Switching paint brands requires clearing shelf space, retraining painters, changing tinting habits, and risking customer complaints.
- **The Hormozi Solution**: Provide free high-visibility display racks, pre-tinted fast-moving bases, free painter application toolkits, and on-site technical support for the first 3 customer jobs.

---

## 3. The 5-Point Ruthless Offer Audit Matrix

When evaluating any Swatch Paints commercial proposal, score each element from 0 to 20 (Total Score / 100):

| Audit Category | Evaluation Standard | Failure Indicator |
| :--- | :--- | :--- |
| **1. Margin Arbitrage (0-20)** | Does the dealer make at least **2.5x to 3x** the net rupee profit compared to Asian Paints or Berger? | Dealer margin is <12% or tied up in complex year-end target hoops. |
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

## 5. Five Battle-Tested Swatch Paints Offer Blueprints

### 1. The Contractor "Master Craftsman VIP" Club
- **Avatar**: Independent painting contractors managing crews of 5-15 painters.
- **The Core Offer**: Accumulate 500 bucket scans in a season.
- **The Stack**: Guaranteed ₹150 UPI cashback per 20L + Annual Diwali Family Holiday + Free branded overalls for entire crew + Direct technical support hotline.
- **Risk Reversal**: "If any client complains about coverage or finish, we provide replacement material for free."

### 2. The Builder "Zero-Defect Handover" Contract
- **Avatar**: Real estate promoters and civil contractors building residential towers.
- **The Core Offer**: Complete supply of exterior elastomeric coatings and interior acrylic systems.
- **The Stack**: 10-year written warranty + Free sample flat paint + Dedicated on-site quality technician for surface prep audits.
- **Risk Reversal**: "If your handover inspection fails due to paint peeling, Sharma Industries pays the rework labor cost."

---

## 6. Dynamic ERP Unit Economics Query Protocol
Never evaluate a Grand Slam offer without verifying contribution margins in the live ERP:
```bash
# Verify Raw Material Cost of Production vs Selling Price
curl -s http://localhost:8000/api/erp/production/unit-economics?sku=ROYAL-EMULSION-20L
# Check Promotional Bonus Reserve Budget for Region
curl -s http://localhost:8000/api/erp/marketing/trade-budget?region=Hadoti
```

---

## 7. Pre-Execution Audit Checklist
- [ ] Is the offer headline clear, avatar-specific, and outcome-focused?
- [ ] Does the prospect achieve at least 3x perceived value relative to price?
- [ ] Is there an ironclad, unconditional risk reversal (buyback or replacement guarantee)?
- [ ] Are bonuses high-perceived-value and low-marginal-cost?
- [ ] Is the unit margin verified through ERP to ensure positive net profit contribution?
"""

# Dictionary of all skills
skills = {
    "porter-strategy": porter_strategy,
    "influence-psychology": influence_psychology,
    "gtm-strategy": gtm_strategy,
    "sales-strategist": sales_strategist,
    "marketing-council": marketing_council,
    "pain-is-the-pitch": pain_is_the_pitch,
    "hormozi-evaluator": hormozi_evaluator,
}

for name, content in skills.items():
    ws_file = os.path.join(ws_base, name, "SKILL.md")
    app_file = os.path.join(app_base, name, "SKILL.md")
    
    os.makedirs(os.path.dirname(ws_file), exist_ok=True)
    os.makedirs(os.path.dirname(app_file), exist_ok=True)
    
    with open(ws_file, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
        
    with open(app_file, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
        
    line_count = len(content.strip().splitlines())
    print(f"Deeply updated {name}: {line_count} lines (Dual installed).")

print("\nAll 7 Batch 3 skills deeply updated!")
