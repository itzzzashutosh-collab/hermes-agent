#!/usr/bin/env python3
"""
Integrate and install requested external skills for Swatch Paints and Hermes:
1. Adapts downloaded external skills for Swatch Paints (Sharma Industries), Indian paint mandis,
   Ashutosh Sharma Sir (Founder & Supreme Authority), and Hermes (CEO).
2. Sets companion playbooks inside the respective Legend folders in swatch-paints.
3. Installs standalone skills into Hermes's skill registry:
   - C:\\Users\\itzzz\\AppData\\Local\\hermes\\skills\\
   - d:\\Sharma Industries Erp Software\\hermes-agent\\skills\\
"""

import os
from pathlib import Path

WORKSPACE_ROOT = Path(r"d:\Sharma Industries Erp Software\hermes-agent")
WORKSPACE_SWATCH = WORKSPACE_ROOT / "skills" / "swatch-paints"
WORKSPACE_SKILLS = WORKSPACE_ROOT / "skills"

HERMES_ROOT = Path(r"C:\Users\itzzz\AppData\Local\hermes\skills")
HERMES_SWATCH = HERMES_ROOT / "swatch-paints"

def ensure_parent(p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)

def write_dual(skill_name: str, content: str):
    """Write standalone skill to both workspace and Hermes local AppData."""
    p1 = WORKSPACE_SKILLS / skill_name / "SKILL.md"
    p2 = HERMES_ROOT / skill_name / "SKILL.md"
    
    ensure_parent(p1)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
        
    ensure_parent(p2)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Installed standalone skill: {skill_name}")

def write_legend_companion(dept: str, legend_folder: str, filename: str, content: str):
    """Write companion playbook into legend folder in both roots."""
    p1 = WORKSPACE_SWATCH / dept / legend_folder / filename
    p2 = HERMES_SWATCH / dept / legend_folder / filename
    
    ensure_parent(p1)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
        
    ensure_parent(p2)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Placed companion in {dept}/{legend_folder}: {filename}")

# ==============================================================================
# 1. BUILDING RAPPORT (Louis Blythe Adapted) -> Joe Girard Relationship Engine
# ==============================================================================
building_rapport_content = '''---
name: building-rapport
description: Create genuine connection and trust quickly with B2B paint dealers, retail hardware store owners, and painting contractors. Adapted from Louis Blythe sales skills for Swatch Paints (Sharma Industries).
category: sales-relationships
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Building Rapport with Paint Dealers & Contractors

## 1. Identity & Mandate
You operate under the direct authority of **Ashutosh Sharma Sir (Founder & Supreme Authority)** and **Hermes (CEO, Swatch Paints)**, serving as the master relationship architect between Swatch Paints and the dealer/contractor ecosystem.

## 2. Core Philosophy (Joe Girard x Louis Blythe)
People buy from people they like and trust. In the Indian paint mandi (Kota, Jaipur, Bhilwara, Alwar), dealers are besieged by dozens of aggressive sales reps every week pushing white primer or enamel quotas. True rapport is NOT slimy small talk about the weather; it is authentic commercial respect, acknowledging the dealer's business legacy, and showing genuine interest in their profitability.

## 3. The Indian Paint Dealer Rapport Triangle
```
                   [1. COMMERCIAL RESPECT]
                   (Understanding their shop footfall,
                    margin squeeze from Asian/Berger)
                           /        \\
                          /          \\
                         /            \\
  [2. CULTURAL & PERSONAL] ──────────── [3. CRAFTSMANSHIP EMPATHY]
  (Mandi rituals: Chai,                 (Respecting the painter's wall
   family business history)              finish, drying time, brush drag)
```

## 4. Phase-by-Phase In-Shop Execution
### Phase 1: Pre-Visit Diagnostics (Before Entering the Counter)
- Check ERP Dealer Dossier: Last order date, pending credit ledger, top-selling categories.
- Observe the shop exterior: Are competitor banners faded? Which brand pails are stacked in the front row?
- Identify the decision maker: Is the owner seated at the *Gaddi* (counter), or is the son / munimji handling billing?

### Phase 2: The First 60 Seconds (Mandi Pattern Interrupt)
- Do NOT pitch paint immediately. Respect the *Gaddi* culture:
  *Verbatim:* "Namaste Sharma Ji! Ram Ram. Dukaan par bheed kaafi achhi dikh rahi hai. Main Swatch Paints factory se Hermes ka representative hoon. Aaj koi deal bechne nahi aaya hoon, bas aapki mandi ka flow dekhne aur aapse milne aaya tha."
- Accept tea/chai respectfully. Rejecting tea in an Indian mandi breaks rapport instantly.

### Phase 3: Transitioning from Rapport to Discovery
- Link their shop floor observations to business reality:
  *Verbatim:* "Sharma Ji, main dekh raha tha aapke godown me Asian ke Royale ke 20-litre pails kaafi lage hain. Aaj kal market me margin 4% se upar nikal pa raha hai ya liquidity blocked rehti hai?"

## 5. Anti-Patterns (What NEVER To Do)
- **The "Bro" Trap:** Being overly casual or disrespectful to senior mandi elders.
- **The Rushed Pitch:** Opening catalog or price sheets before sipping chai and greeting the owner.
- **Competitor Slander:** Mocking Asian Paints or Berger; instead, respect their brand while highlighting dealer margin freedom with Swatch Paints.
'''

# ==============================================================================
# 2. B2B SALES CONSTRAINT DIAGNOSIS (LVTD LLC Adapted) -> Andy Grove / Goldratt
# ==============================================================================
b2b_constraint_content = '''---
name: b2b-sales-constraint-diagnosis
description: Diagnose the single B2B sales bottleneck currently limiting dealer expansion, painter recruitment, or depot off-take for Swatch Paints. Adapted from LVTD LLC skills.
category: sales-strategy
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# B2B Sales Constraint Diagnosis for Swatch Paints

## 1. Identity & Mandate
Operating under **Ashutosh Sharma Sir** and **Hermes (CEO)**, this engine acts as the chief diagnostic tool for identifying why sales revenue or dealer acquisition is stalled in a given district or territory.

## 2. The 4-Stage Paint Pipeline Bottleneck Framework
Every stalled B2B paint territory is blocked by exactly ONE of these four constraints:
```
[1. COUNTER REACH]       ──► Sales rep visiting <15 new paint counters per week.
[2. DEALER ENGAGEMENT]   ──► Dealers taking sample pails but never opening them.
[3. CONVERSION / TRUST]  ──► Dealers fear stocking unadvertised brands due to painter resistance.
[4. VELOCITY / RETENTION]──► Dealers stocked initial batch but repeat reorder takes >60 days.
```

## 3. Diagnostic Flowchart
1. **Is territory lead flow <10 new prospective counters/week?**
   - *YES:* **Constraint is REACH.** Fix rep routing, mandi mapping, and contractor contact lists.
   - *NO:* Proceed to Step 2.
2. **Are dealers rejecting the first pitch outright?**
   - *YES:* **Constraint is VALUE PROPOSITION.** Rep is pitching generic paint specs instead of the Hormozi Grand Slam Dealer Margin Equation.
   - *NO:* Proceed to Step 3.
3. **Are dealers asking for unreasonable credit terms (90+ days)?**
   - *YES:* **Constraint is RISK REVERSAL.** Dealer lacks proof of retail off-take. Counter-measure: Deploy the 30-Day Painter Pull-Through Campaign.
   - *NO:* Proceed to Step 4.
4. **Is repeat order cycle stagnant?**
   - *YES:* **Constraint is PAINTER CONTRACTOR DEMAND.** Painters lack token rewards or tinting support. Counter-measure: Launch WhatsApp Painter Loyalty Scheme.
'''

# ==============================================================================
# 3. SALES SCRIPT PLAYBOOK (Shawn Pang Adapted) -> Jordan Belfort Straight Line
# ==============================================================================
sales_script_content = '''---
name: sales-script
description: Battle-tested Straight Line scripts, counter pitch talk tracks, and objection handlers for Swatch Paints sales executives visiting retail paint counters. Adapted from Shawn Pang startup founder skills.
category: sales-execution
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Swatch Paints Straight Line Sales Script

## 1. Persona & Tone
You are confident, sharp as a tack, enthusiastic as hell, and an authority in industrial and decorative paint chemistry. You represent **Ashutosh Sharma Sir** and **Hermes (CEO)**.

## 2. In-Store Dealer Counter Pitch (Hindi/English Verbatim)
### Step 1: The Opener
"Namaste [Dealer Name] Ji! Mera naam [Rep Name] hai Swatch Paints factory se. Main bas 2 minute ke liye aaya hoon. Maine notice kiya aapki counter Kota mandi me exterior emulsions ke liye sabse reputed hai. Main aapse koi 10 drum lene ko nahi kahunga—sirf ek seedhi baat poochhne aaya hoon: Agar main aapko Asian Royale jaisi 100% pure acrylic opacity deliver karwaoon, par aapka margin 4% se seedha 18% ho jaye, toh kya aap hamare sample bucket ko apne master painter se test karwayenge?"

### Step 2: The Core Value Hook (The Straight Line)
"Sharma Ji, aaj ki date me 3 badi companiyan aapko apna product bechne ke liye majboor karti hain, par end me aapke haath me 4-5% se zyada margin nahi bachta, aur saara cash unke credit cycle me phas jata hai. Swatch Paints factory-direct model par kaam karta hai:
1. **Titanium Dioxide (TiO2) High Grade:** Ek coat me 100% wall coverage.
2. **Direct Dealer Margin:** 18% se 22% net profit.
3. **Painter QR Token Scheme:** Seedha painter ke bank me instant cash transfer.
4. **Unsold Stock Protection:** 45 dino me nahi bika toh 100% replacement ya buyback."

### Step 3: Overcoming the Classic Objections
- **Objection: "Customer toh sirf Asian Paints maangta hai!"**
  *Response:* "Aap bilkul sahi keh rahe hain Sharma Ji, 70% log wahi maangte hain kyunki TV ad dekhte hain. Par jab customer aapki dukan par aata hai, toh wo aapke 20 saal ke tajurbe par vishwas karta hai. Agar aap kahenge: 'Bhaiya, ye Swatch Paints ka sample dekho, coverage double hai aur 5 saal ki guarantee main khud deta hoon'—toh kya customer aapki baat nahi maanega? Aur jahan aap 100 rupaye bacha rahe the, wahan 350 rupaye banenge."

- **Objection: "Pehle credit do 60 din ka, tab maal rakhenge."**
  *Response:* "Sharma Ji, market me jo companiyan 60 din ka credit deti hain, wo wahi paisa paint ki quality kam karke aur rate bada kar aapse vasoolti hain. Swatch Paints quality par zero compromise karta hai. Main aapse bada bill nahi maang raha—sirf ek 5-drum starter pilot pack rakhiye. Painter pasand na kare toh drum wapas."
'''

# ==============================================================================
# 4. PROBING & DISCOVERY (Kimmy Work & Louis Blythe Adapted) -> Neil Rackham SPIN
# ==============================================================================
probing_content = '''---
name: probing
description: Master diagnostic probing and exploratory questioning frameworks for uncovering hidden paint dealer dissatisfaction, contractor pain points, and commercial bottlenecks. Adapted from Kimmy Work & Louis Blythe.
category: sales-discovery
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Probing & Diagnostic Discovery Engine for Paint Sales

## 1. Purpose & Reporting Hierarchy
Authorized by **Ashutosh Sharma Sir** and **Hermes (CEO)** to execute surgical discovery before any sales presentation. Telling is NOT selling; asking the right diagnostic questions creates irresistible buying urgency.

## 2. The 4-Level Probing Architecture
```
[Level 1: Surface Operational Facts]   ──► "Kitne litres mahine ka dispatch nikalta hai?"
[Level 2: Friction & Hidden Costs]     ──► "Kya kabhi customer ne peeling ya shade fading ki complaint ki?"
[Level 3: Financial & Cash Impact]     ──► "Current brand ke stock me kitna working capital fasa hua hai?"
[Level 4: Desired Transformation]      ──► "Agar margin 4% se 18% ho jaye, toh saal ka kitna extra munafa hoga?"
```

## 3. High-Impact Diagnostic Inquiries for Paint Dealers
1. **On Inventory Turnover:** "Sharma Ji, aapke godown me kitne pails aisi hain jo 60 dino se bina bike padi hain?"
2. **On Tinting Machine Lock-in:** "Badi companiyan jo machine deti hain, kya unke tinting software me aapko dusre colorants use karne dete hain ya captive lock-in hai?"
3. **On Painter Loyalty:** "Aapke top 5 thekedar painter kya doosri dukanon par shift ho rahe hain kyunki wahan unhe better reward ya direct factory connect milta hai?"
4. **On Margin Erosion:** "Jab festive season me scheme aati hai, toh kya sara profit turnover target poora karne me hi chala jata hai?"
'''

# ==============================================================================
# 5. GRAND SLAM OFFERS (Corey Haines & Wondelai Adapted) -> Alex Hormozi
# ==============================================================================
offers_content = '''---
name: offers
description: Design, construct, and optimize irresistible B2B Grand Slam offers for paint dealers, retail hardware stores, and construction contractors. Adapted from Corey Haines & Wondelai 100M Offers.
category: commercial-strategy
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Grand Slam Offer Design for Swatch Paints

## 1. Identity & Mandate
Under **Ashutosh Sharma Sir** and **Hermes (CEO)**, this engine builds commercial propositions so compelling that paint dealers and contractors feel foolish saying no.

## 2. The Hormozi Value Equation for Paint Dealers
```
                   Dream Outcome (High Profit + Zero Peeling Complaints)
VALUE = ─────────────────────────────────────────────────────────────────────────────
        Perceived Likelihood of Success x Time Delay (Immediate) x Effort & Sacrifice (Zero)
```

## 3. Swatch Paints Dealer Launch Stack: The "Risk-Reversed Mandi Dominator"
Instead of selling "paint pails at Rs. X/Litre", package the complete ecosystem:
1. **Core Asset:** 500 Litres of Premium Exterior Emulsion & Acrylic Primer at Tier-1 Wholesale Price.
2. **Bonus 1 (Dealer Margin Expansion):** 18% Gross Margin vs 4.5% Market Standard.
3. **Bonus 2 (Painter Contractor Engine):** 50 Painter QR Loyalty Cards loaded with Rs. 100 instant cash payout on bucket scan.
4. **Bonus 3 (Local Counter Marketing):** Premium 8x3 ft Weatherproof Dealer Glow-Sign Board & Counter Display Rack installed free.
5. **Bonus 4 (Tinting Machine Co-Op):** Factory-calibrated computerized tinting dispenser installed on a 90-day volume rebate agreement.
6. **The Ultimate Risk Reversal (Guarantee):** "45-Day 100% Unsold Stock Buyback Guarantee." If the paint doesn't move off your shelves, Swatch Paints picks up the drums and refunds 100% of your invoice amount.

## 4. Anti-Patterns in Offer Construction
- **Price Slicing:** Lowering base price rather than adding high-perceived-value bonuses.
- **Vague Promises:** Saying "high quality paint" instead of "100% pure rutile TiO2 with 7-year anti-fungal warranty".
- **Uncapped Credit:** Giving loose 90-day credit which attracts deadbeat accounts instead of offering structured cash discounts.
'''

# ==============================================================================
# 6. SALES MARKET SIZING (Maya-Beth Finotti Adapted) -> Michael Porter / Drucker
# ==============================================================================
market_sizing_content = '''---
name: sales-market-sizing
description: TAM, SAM, and SOM calculation engine for paint depot territories, mandi penetration, dealer quota setting, and district expansion. Adapted from Maya-Beth Finotti sales skills.
category: market-analysis
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Paint Sales Market Sizing (TAM, SAM, SOM) for Swatch Paints

## 1. Mandate & Reporting
Reporting to **Ashutosh Sharma Sir** and **Hermes (CEO)** to ground all territory sales quotas, depot expansions, and manufacturing capacity in empirical market reality.

## 2. Mathematical Market Sizing Models
### Model A: Bottom-Up Paint Dealer Population Method
```
TAM (District) = Active Paint Counters x Average Monthly Paint Sales (L) x 12
SAM (Serviceable) = Independent Retail Counters within 150 km Depot Radius
SOM (Target Share) = SAM x Achievable Counter Share % (e.g. 8% to 15%)
```

### Model B: Per-Capita Construction Sizing Method
```
Paint Demand (L/year) = District Urban Population x Per Capita Consumption (approx 4.8 kg/year)
```

## 3. Sample Case: Kota District Expansion
- **Active Retail Paint Counters:** ~320 dealers.
- **Average Monthly Emulsion Off-Take per Dealer:** 2,200 Litres.
- **District Annual Volume (TAM):** 320 x 2,200 x 12 = **8,448,000 Litres/Year**.
- **Serviceable Addressable Market (SAM):** 180 Grade-B & Grade-C dealers open to alternative brands = **4,752,000 Litres/Year**.
- **Swatch Paints 18-Month SOM (Target 10% Counter Share):** **475,200 Litres/Year** (~39,600 Litres/Month).
- **Rep Quota Distribution:** 4 territory sales officers, each carrying ~10,000 Litres/month target across 12-15 active accounts.
'''

# ==============================================================================
# 7. STORYBRAND MESSAGING (Wondelai Adapted) -> Al Ries & Jack Trout
# ==============================================================================
storybrand_content = '''---
name: storybrand-messaging
description: Clarify brand positioning and customer messaging using Donald Miller StoryBrand 7-part framework adapted for paints. Position the dealer, painter, and homeowner as the hero, and Swatch Paints as the trusted technical guide.
category: brand-messaging
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# StoryBrand Brand Messaging Framework for Swatch Paints

## 1. The Core Philosophy
The customer is the HERO, not your paint can. Swatch Paints is the trusted GUIDE (Sherpa) who gives the hero the plan and calls them to action.

## 2. The 7-Part StoryBrand Structure for Swatch Paints
```
1. A CHARACTER       ──► The Independent Paint Dealer / The Family Homeowner.
2. HAS A PROBLEM     ──► Margin squeeze & dead stock / Damp, peeling walls after monsoon.
3. MEETS A GUIDE     ──► Swatch Paints (Sharma Industries: 30+ yrs manufacturing mastery).
4. WHO GIVES A PLAN  ──► 3-Step: Sample Test ──► Painter Demo ──► High-Margin Stocking.
5. CALLS TO ACTION   ──► Direct Order / WhatsApp Booking.
6. AVOIDS FAILURE    ──► Zero margin erosion, zero peeling customer complaints.
7. ENDS IN SUCCESS   ──► Thriving profitable shop / Beautiful waterproof home that lasts a decade.
```

## 3. The One-Liner Elevator Pitch
"Most paint dealers are trapped making razor-thin 4% margins while big brands demand cash upfront. At Swatch Paints, we provide factory-direct, craftsman-grade architectural paints with 18% dealer margins and instant painter loyalty rewards, so you can build a highly profitable, independent business."
'''

# ==============================================================================
# 8. MARKETING MINDSET (Axel Freeman Adapted) -> Gary Vee / Kotler
# ==============================================================================
marketing_mindset_content = '''---
name: marketing-mindset
description: Strategic operating mindset for paint brand building, customer acquisition, direct-response advertising, and contractor community engagement. Adapted from Axel Freeman marketing mindset.
category: marketing-strategy
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Marketing Mindset for Swatch Paints

## 1. Core Operating Mental Models
Authorized by **Ashutosh Sharma Sir** and **Hermes (CEO)**.

### Model 1: The Eye & The Wall (Visual Dominance)
In paint marketing, words never beat eyes. A single 10-second video of water beading off a Swatch Waterproofing Emulsion wall beats 10 pages of technical data sheets.
- **The Visual Hook:** High contrast water spray, scratch test, wet scrub resistance.

### Model 2: Dealer Counter as the Supreme Media Channel
Before spending rupees on billboards, win the 3 feet of counter space in front of the dealer's gaddi. The dealer's word at the point of sale is worth 100 TV commercials.

### Model 3: Painter Community as the Word-of-Mouth Flywheel
Painters do not read brochures; they care about:
- Does it drag on the roller?
- Does it cover in one coat?
- Does the QR token give real money instantly?
'''

# ==============================================================================
# 9. WHATSAPP MARKETING (Arnab Bag Adapted) -> Philip Kotler / Sales Ops
# ==============================================================================
whatsapp_marketing_content = '''---
name: whatsapp-marketing
description: High-converting WhatsApp Business marketing, broadcast campaigns, automated order notices, and painter contractor loyalty flows for Swatch Paints India. Adapted from Arnab Bag brand building skills.
category: digital-marketing
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# WhatsApp Marketing & Loyalty Automation for Swatch Paints

## 1. Identity & Mandate
Reporting to **Ashutosh Sharma Sir** and **Hermes (CEO)**, this engine manages all WhatsApp conversational marketing, dealer notifications, and contractor reward communications.

## 2. Broadcast Campaign Blueprints
### Campaign A: Festive Pre-Diwali Stocking Blast (Dealers)
- **Target:** Verified Dealers in Rajasthan & MP.
- **Message Hook:** "Diwali Stocking Alert 🎨: 18% Guaranteed Margin + Free Computerized Color Card Kit on all orders placed before Oct 10th. Reply 'STOCK' to view ERP catalog."

### Campaign B: Painter Loyalty Token Double Points (Thekedars)
- **Target:** Registered Painter Contractors.
- **Message:** "Ram Ram Ustaad Ji! Swatch Paints Double Dhamaka: Is hafte har 20L Weather-Shield pail par token payout Rs. 100 ke bajaye Rs. 200 seedha aapke UPI me! Aaj hi apne nazdeeki dealer se sample lein."

## 3. Automated Transactional Flows (ERP Bridge)
- **Order Confirmation:** "Shri [Dealer Name], aapka order #SW-8942 verify ho chuka hai. 240L Emulsion dispatch ke liye tayyar hai. Live tracking link: [ERP Link]."
- **Dispatch Alert:** "Aapka truck vehicle #RJ-20-GA-1234 plant se nikal chuka hai. Expected delivery: Tomorrow 11:00 AM."
'''

# ==============================================================================
# 10. BRAND STRATEGY & POSITIONING (Arnab Bag Adapted) -> Al Ries & Jack Trout
# ==============================================================================
brand_strategy_content = '''---
name: brand-strategy
description: Brand strategy, positioning against legacy paint monopolies, brand voice, and long-term brand equity development for Swatch Paints. Adapted from Arnab Bag brand building skills.
category: brand-strategy
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Brand Strategy & Competitive Positioning for Swatch Paints

## 1. Identity & Mandate
Directed by **Ashutosh Sharma Sir** and **Hermes (CEO)**.

## 2. Positioning Against Legacy Giants
```
LEGACY PAINT MONOPOLIES                SWATCH PAINTS POSITIONING
(Asian Paints, Berger, Nerolac)        (Craftsman-Grade Factory-Direct)
───────────────────────────────        ─────────────────────────────────
Mass TV advertising, heavy corporate   Engineered chemical purity, high TiO2
Dealer margin squeezed to 4-5%         Dealer margin empowered at 18-22%
Captive tinting machine lock-in        Open tinting flexibility
Slow complaint resolution              24-hour factory lab technical support
```

## 3. Brand Voice Guidelines
- **Grounded & Industrial:** We talk like master chemical formulators, not airy advertising agencies.
- **Respectful & Mandi-Fluent:** Hindi and English technical vocabulary aligned with Indian shop-floor reality.
- **Uncompromising Quality:** Zero chalking, zero solvent diluting, maximum solids content.
'''

# ==============================================================================
# 11. SALES AUTOMATOR (Sickn33 Adapted) -> Andy Grove Execution / Systems
# ==============================================================================
sales_automator_content = '''---
name: sales-automator
description: Automated sales cadence generator, proposal drafting, ERP lead routing, and follow-up sequence automation for Swatch Paints field executives. Adapted from Sickn33 agentic skills.
category: sales-automation
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Paint Sales Automator Engine

## 1. Purpose & Reporting Hierarchy
Authorized by **Ashutosh Sharma Sir** and **Hermes (CEO)** to automate mundane sales administration, freeing territory officers to spend 80% of their day in front of dealers and painters.

## 2. Automated Follow-Up Sequences
- **Day 1 Post-Visit:** Automated WhatsApp thank you note + PDF product comparison sheet.
- **Day 3 Follow-Up:** Check if painter tested the sample drum.
- **Day 7 Decision Prompt:** Present pilot stocking offer with 45-day buyback guarantee.
- **Day 14 Re-engagement:** Share case study of a neighboring dealer in Kota who increased monthly profits by Rs. 85,000.
'''

# ==============================================================================
# 12. RELATIONSHIP-LED LINK BUILDING & PR (LVTD Adapted) -> Philip Kotler
# ==============================================================================
relationship_linking_content = '''---
name: relationship-led-link-building
description: Build authority relationships with Rajasthan architectural firms, builder associations (CREDAI), interior design portals, and contractor forums. Adapted from LVTD LLC skills.
category: pr-authority
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Relationship-Led Authority & Specifier Building for Swatch Paints

## 1. Purpose & Reporting
Directed by **Ashutosh Sharma Sir** and **Hermes (CEO)** to get Swatch Paints specified in architectural BOQs (Bills of Quantities) across major real estate and government infrastructure projects.

## 2. Strategic Specifier Outreach
- **Architectural Specifier Kit:** Deliver physical shade fans, wet scrub test slabs, and VOC lab certificates to top 50 architectural firms in Jaipur, Udaipur, and Kota.
- **Builder Association Partnerships:** Host technical seminars on "Preventing Monsoon Efflorescence in High-Rise Plaster" for CREDAI regional chapters.
- **Digital Authority:** Secure features in Indian architectural journals and building material forums.
'''

# ==============================================================================
# EXECUTE INSTALLATIONS & COMPANION PLACEMENT
# ==============================================================================

# A. Install Standalone Skills in Hermes Registry (Both AppData and Workspace)
standalone_skills = [
    ("building-rapport", building_rapport_content),
    ("b2b-sales-constraint-diagnosis", b2b_constraint_content),
    ("sales-script", sales_script_content),
    ("probing", probing_content),
    ("offers", offers_content),
    ("sales-market-sizing", market_sizing_content),
    ("storybrand-messaging", storybrand_content),
    ("marketing-mindset", marketing_mindset_content),
    ("whatsapp-marketing", whatsapp_marketing_content),
    ("brand-strategy", brand_strategy_content),
    ("sales-automator", sales_automator_content),
    ("relationship-led-link-building", relationship_linking_content),
]

print("\n--- [Step 1] Installing Standalone Skills into Hermes Registry ---")
for name, content in standalone_skills:
    write_dual(name, content)

# B. Place Specialized Companion Playbooks inside Swatch Paints Legend Folders
companion_mappings = [
    ("01_sales", "joe-girard-relationship-engine", "BUILDING_RAPPORT_PLAYBOOK.md", building_rapport_content),
    ("01_sales", "andy-grove-execution-engine", "B2B_SALES_CONSTRAINTS.md", b2b_constraint_content),
    ("01_sales", "jordan-belfort-straight-line-script-engine", "SALES_SCRIPTS_PLAYBOOK.md", sales_script_content),
    ("01_sales", "neil-rackham-spin-selling-engine", "PROBING_DISCOVERY_PLAYBOOK.md", probing_content),
    ("01_sales", "alex-hormozi-offer-engine", "OFFER_CONSTRUCTION_PLAYBOOK.md", offers_content),
    ("01_sales", "peter-drucker-role-clarity-engine", "MARKET_SIZING_TAM_SAM_SOM.md", market_sizing_content),
    ("07_vision_growth", "michael-porter-competitive-advantage-engine", "MARKET_SIZING_TAM_SAM_SOM.md", market_sizing_content),
    ("05_marketing_brand", "al-ries-jack-trout-positioning-engine", "STORYBRAND_MESSAGING_FRAMEWORK.md", storybrand_content),
    ("05_marketing_brand", "al-ries-jack-trout-positioning-engine", "BRAND_STRATEGY_PLAYBOOK.md", brand_strategy_content),
    ("05_marketing_brand", "gary-vaynerchuk-attention-content-engine", "MARKETING_MINDSET_PLAYBOOK.md", marketing_mindset_content),
    ("05_marketing_brand", "philip-kotler-digital-marketing-engine", "WHATSAPP_MARKETING_PLAYBOOK.md", whatsapp_marketing_content),
    ("05_marketing_brand", "philip-kotler-digital-marketing-engine", "RELATIONSHIP_LINKING_PLAYBOOK.md", relationship_linking_content),
    ("08_systems_sops", "andy-grove-execution-discipline-engine", "SALES_AUTOMATION_PLAYBOOK.md", sales_automator_content),
]

print("\n--- [Step 2] Placing Companion Playbooks into Legend Folders ---")
for dept, legend, fname, content in companion_mappings:
    write_legend_companion(dept, legend, fname, content)

print("\n--- [SUCCESS] All 12 external skills successfully integrated and installed for Hermes and Swatch Paints! ---")
