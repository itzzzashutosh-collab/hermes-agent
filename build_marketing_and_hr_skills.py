import os

WORKSPACE_DIR = r"d:\Sharma Industries Erp Software\hermes-agent"
HERMES_DIR = r"C:\Users\itzzz\AppData\Local\hermes"

MKT_HR_SKILLS = {
    # === 05_MARKETING_BRAND ===
    "al-ries-jack-trout-positioning-engine": {
        "title": "Al Ries & Jack Trout Positioning & Brand Battleground Engine for Swatch Paints",
        "legend": "Al Ries & Jack Trout (Pioneers of Positioning & Authors of 'Positioning: The Battle for Your Mind')",
        "description": "Al Ries & Jack Trout Positioning Strategy, Mental Real Estate Domination, Counter-Positioning, and Category Creation Engine for Swatch Paints Marketing.",
        "dept": "05_marketing_brand",
        "tag": "ries-trout-positioning",
        "purpose": """This skill equips the Swatch Paints Marketing, Brand Strategy, and Commercial Leadership with Al Ries and Jack Trout’s foundational disciplines of **Positioning: The Battle for the Mind**.

In the Indian paint market, new entrants make the fatal mistake of trying to be "everything to everybody": they launch 50 generic emulsion, distemper, and primer SKUs, claiming to be "higher quality at lower prices" than Asian Paints, Berger, and Nerolac. But the consumer and painter mind cannot register a generic "me-too" brand; the top rungs of the mental ladder for generic paint are already firmly occupied. Trying to challenge market leaders head-on in their own category is commercial suicide.

The engine's purpose is to:
- Own a single, sharp, unforgettable **Word or Concept** in the mind of the Indian consumer, architect, and contractor (e.g., Swatch = "Weather-Proof Stone Texture & Thermal Resistance").
- Execute **Counter-Positioning**: redefining competitors' strengths as their weaknesses (e.g., multinational paints are mass-market synthetic plastic films; Swatch Rustic is authentic, breathable mineral stone).
- Create and dominate a **New Category** where Swatch Paints is the undisputed #1 pioneer rather than a #5 follower.
- Ruthlessly enforce the **Law of Sacrifice**: cutting line-extension bloat to keep the brand's positioning laser-focused.""",
        "when_to_use": """- Launching brand advertising, dealership signage, architectural catalogs, and digital campaigns.
- Defining the market entry strategy for a new territory dominated by multinational paint giants.
- Repositioning Swatch Rustic or flagship exterior emulsions against commoditized competition.
- Product managers propose launching dozens of low-margin generic line extensions that dilute brand clarity.
- Formulating sales pitches that contrast Swatch against competitors without entering destructive price wars.
- Aligning corporate communication from the CEO office to dealer counters under a single positioning idea.""",
        "frameworks": """### 6.1 The Law of the Mind & Mental Ladders
Positioning is not what you do to a product; it is what you do to the **mind of the prospect**.
- On any product ladder in the consumer's mind, there is room for only 2 to 3 rungs.
  - Generic Decorative Paint: Rung 1 = Asian Paints, Rung 2 = Berger.
  - Trying to squeeze onto Rung 3 with a "me-too" emulsion requires hundreds of crores in TV advertising.
- **The Ries & Trout Breakthrough:** Build a *different ladder*.
  - Category: Authentic Stone & Rustic Architectural Finishes -> **Rung 1: Swatch Paints**.

### 6.2 The Law of the Opposite (Counter-Positioning)
If you want to establish a firm foothold against the market leader, do not copy them; present the exact opposite:
- Leader's Strength: Huge multi-national industrial factories producing standard synthetic film paint.
- The Counter-Position: *"Standard plastic paints peel and trap moisture in harsh Rajasthan heat. Swatch is the specialized mineral texture engineered specifically for intense sun, efflorescence resistance, and natural stone elegance."*

### 6.3 The Law of Sacrifice
To gain mental clarity, you must give something up:
1. **Sacrifice Product Line:** Focus marketing resources on the hero franchise (Swatch Rustic & Weather-Shield).
2. **Sacrifice Target Market:** Target premium villa builders, independent homebuilders (IHBs), and discerning master painters before chasing low-end mass rentals.
3. **Sacrifice Constant Change:** Stick with the same core positioning concept for at least 5 to 10 years.""",
        "decision_algo": """### Step 1: Identify the Mental Real Estate Word
- What single word does Swatch Paints own in Rajasthan?
  - If the answer is "quality" or "cheap", REJECT immediately. Everyone claims quality.
  - Approved Positioning Word: **"Resilient Texture"** or **"Weather-Defying Coatings"**.

### Step 2: Audit Competitor Counter-Positioning
- Map competitor claims:
  - Competitor A owns "Color Variety".
  - Competitor B owns "Waterproofing Buffer".
  - Swatch owns: **"Architectural Texture & Anti-Efflorescence Stone Shield"**.

### Step 3: Enforce the Law of Sacrifice on Packaging & Signage
- Dealer flex boards and shop signage must feature the hero positioning prominently:
  - 70% visual area dedicated to Swatch Rustic finish and high-end exterior protection.
  - Zero cluttered lists of 30 obscure product variants.

### Step 4: Consistency Verification
- All marketing collateral, TV/radio scripts, painter uniforms, and digital posts must reinforce the singular positioning anchor.""",
        "example1": """### Example 1: Repositioning Against Asian Paints in Hadoti Mandis
**Situation:** Sales reps in Kota complained: *"Jab hum dealer ke paas jate hain, woh kehta hai Asian Paints ka Apex chal raha hai, tumhara paint kyu lein?"*
**Ries & Trout Positioning Applied:**
- Reps stopped saying *"Hamara paint Apex jaisa hai par 5% sasta hai"* (a losing "me-too" pitch).
- Re-anchored the conversation on a new ladder: *"Sethji, Apex smooth plastic film hai. Jab Kota stone ya cement plaster me namak (shora) aur moisture aati hai, plastic film bubble bankar phat jati hai. Swatch Rustic breathable mineral stone texture hai jo namak aur dhoop me 10 saal tak nahi phat-ta."*
- Created a separate category in the dealer's mind.
- Result: Over 40 dealers who refused to stock Swatch as a general paint brand agreed to stock Swatch Rustic as their exclusive texture specialist.""",
        "example2": """### Example 2: Sacrificing Line Extensions to Build Brand Power
**Situation:** The sales team proposed launching "Swatch Budget White Wash" at ₹18/kg to compete with local unbranded lime washes.
**Positioning Audit:**
- Launching cheap chalk-wash would destroy Swatch’s emerging reputation as a premium architectural texture house.
- Enforced the Law of Sacrifice: Rejected the budget wash. Channeled the entire marketing budget into Swatch Rustic sample kits and display stands for top 50 dealers.
- Protected brand gross margin at 34% and elevated dealer perception of Swatch as an aspirational, high-status brand.""",
        "failures": [
            ("The 'Me-Too' Trap", "Advertising 'high quality paint at affordable prices' - the most forgotten slogan in history.", "Own a specific, differentiated category or attribute; never launch a generic me-too claim."),
            ("Line Extension Disease", "Putting the Swatch name on low-grade adhesives, thinners, and cheap brushes, diluting brand prestige.", "Follow the Law of Sacrifice: protect the core brand's high-equity reputation."),
            ("Challenging the Leader Head-On", "Trying to out-advertise Asian Paints on general color variety.", "Counter-position by highlighting the leader's structural vulnerability (synthetic mass paint vs specialized texture)."),
            ("Changing Positioning Annually", "Switching marketing slogans every season based on agency fads.", "Positioning is a multi-decade mental anchor. Maintain disciplined thematic consistency.")
        ],
        "checklist": [
            "Single positioning concept / word clearly defined and verified in consumer perception.",
            "Counter-positioning strategy articulated against dominant market leaders.",
            "Law of Sacrifice enforced: marketing budget concentrated on hero franchise products.",
            "Dealer signage and shop boards reflect clean, uncluttered category leadership.",
            "Product launch proposals vetted against brand dilution and line-extension risks.",
            "Architect and contractor pitches centered on unique functional category advantages."
        ]
    },
    "andrew-chen-cold-start-growth-engine": {
        "title": "Andrew Chen Cold Start Problem & Atomic Network Growth Engine for Swatch Paints",
        "legend": "Andrew Chen (General Partner at Andreessen Horowitz & Author of 'The Cold Start Problem')",
        "description": "Andrew Chen Cold Start Framework, Atomic Networks, Tipping Points, and Localized Network Density for Swatch Paints Distribution Growth.",
        "dept": "05_marketing_brand",
        "tag": "andrew-chen",
        "purpose": """This skill equips the Swatch Paints Growth, Digital Expansion, and Territory Strategy teams with Andrew Chen’s **Cold Start Framework**, **Atomic Networks**, and **Network Density Economics**.

In multi-sided distribution systems (comprising Paint Dealers, Painting Contractors, Homebuilders, and Company Depots), new brands suffer from the classic **Cold Start Problem**: Dealers won't stock Swatch because painters aren't asking for it, and painters won't ask for Swatch because local dealers don't stock it. Companies waste millions scattering sales reps thinly across 20 districts, achieving 1% market share everywhere and zero network density anywhere.

The engine's purpose is to:
- Solve the Cold Start Problem by building hyper-focused **Atomic Networks**: the smallest standalone market that can sustain self-reinforcing network effects (e.g., a single building hardware mandi like Bundi City or Kota Gumanpura).
- Overcome the **Anti-Network Effect** (early friction, empty shelves, missing shade cards) through high-touch manual onboarding of anchor painters and dealers.
- Drive market penetration through the **Tipping Point**: achieving 35%+ contractor awareness in a concentrated zip code where word-of-mouth takes over organic growth.
- Replicate winning atomic clusters systematically across contiguous territories using the **Flintstoning & Moat-Scaling Playbook**.""",
        "when_to_use": """- Launching Swatch Paints in a brand new district or geographic territory.
- Overcoming the chicken-and-egg deadlock: dealers waiting for painters; painters waiting for dealers.
- A sales territory is spread too thin across hundreds of kilometers with zero local dominance.
- Designing the onboarding flywheel for the Swatch Ustaad Painter App.
- Allocating quarterly field expansion budgets between new market entries vs. existing cluster deepening.
- Assessing when an atomic cluster has reached self-sustaining network velocity.""",
        "frameworks": """### 6.1 The Cold Start Curve & Atomic Networks
Chen demonstrated that network effects do not happen at state or national scale first; they ignite in tiny, dense **Atomic Networks**:
```
[COLD START] ──> [TIPPING POINT] ──> [ESCAPE VELOCITY] ──> [CEILING / MOAT]
```
- **The Atomic Network for Swatch Paints:** Defined as **1 Anchor Paint Hardware Dealer + 15 Master Painting Contractors** in a 5 km radius.
- In this micro-cluster, painters buy the paint, scan loyalty tokens, recommend it at local tea stalls, and the dealer sees rapid inventory turnover.
- **Rule of Expansion:** Never launch District 2 until District 1 has at least **3 fully self-sustaining Atomic Networks**.

### 6.2 "Flintstoning" (Doing Things That Don't Scale)
To get the flywheel spinning initially, you cannot rely on digital apps or automated dispatch. You must "Flintstone" the network through manual human effort:
- The ASM personally delivers 4 buckets of Swatch Rustic in his own car to a painter's job site when an emergency arises.
- Sales reps manually mix color samples on site to demonstrate workability.
- Manual subsidies (free tool aprons, immediate cash token redemption) overcome early contractor skepticism.

### 6.3 The Hard Side of the Network
In every network, one side is much harder to acquire and retain than the other:
- In paint: Hardware dealers are relatively easy to sign up if you give credit.
- **The Hard Side is the Master Painting Contractor (Thekedaar).** The contractor risks his entire labor fee and reputation if the paint fails. Win the Hard Side (contractors), and the dealers will enthusiastically stock your paint.""",
        "decision_algo": """### Step 1: Define the Micro-Geographic Target
- Select a concentrated target mandi (e.g., Bundi Hardware Market).
- Draw a 5 km operational boundary. Prohibit field reps from pursuing leads outside this zone during the launch sprint.

### Step 2: Capture the Hard Side (Top 15 Contractors)
- Identify the 15 most influential painting contractors in the mandi.
- Deploy the Flintstoning Playbook:
  - Personal technical texture workshops.
  - Free sample pails for their active luxury home projects.
  - Direct WhatsApp hotline to the Swatch technical lab.

### Step 3: Secure the Anchor Dealer Counter
- Take the 15 contractor commitments to the leading local hardware dealer:
  - *"Sethji, ye 15 thekedaar agle 30 din me 4,000 litre Swatch uthane wale hain. Kya aap inka billing counter banna chahte hain?"*
  - Dealer stocks stock immediately without requiring credit concessions.

### Step 4: Validate Tipping Point Velocity
- Measure weekly repeat re-orders. When >70% of dealer orders are triggered by organic painter pull rather than rep pushing, declare Tipping Point reached. Expand to the adjacent mandi.""",
        "example1": """### Example 1: Igniting the Bundi City Atomic Network
**Situation:** Swatch had zero sales in Bundi. Competitors had 100% counter share. A junior sales rep drove across the entire district for 3 months, opening 2 tiny rural accounts that bought ₹10,000 of distemper.
**Cold Start Atomic Strategy Applied:**
- Rep was pulled back and ordered to focus strictly on a 3 km radius around Bundi Purana Mandi.
- *Hard Side Focus:* Identified the 12 master contractors who handled 80% of urban residential repaints.
- Conducted an intensive 1-day Swatch Rustic masterclass at a local hotel, demonstrating rapid application and thermal crack bridging. Handed each contractor a free 4 kg sample bucket.
- Within 10 days, 8 contractors demanded Swatch for upcoming Diwali jobs.
- Rep approached the top 2 Bundi hardware dealers with confirmed contractor demand in hand.
- Both dealers took full stocking orders worth ₹4.2 Lakhs on cash-down terms.
- Within 60 days, Bundi became a self-sustaining atomic network generating ₹8 Lakhs/month.""",
        "example2": """### Example 2: Overcoming the Painter App Chicken-and-Egg Problem
**Situation:** The digital loyalty app (Swatch Ustaad) had low adoption: painters downloaded it, saw zero local dealers listed for point redemption, and uninstalled it.
**Chen Flintstoning Fix:**
- Bypassed the digital friction: Sales officers personally visited painter job sites, scanned the QR tokens on their behalf using company phones, and handed them instant cash on the spot.
- Once 50 painters had experienced the tangible cash benefit, reps introduced the app directly: *"Aapko hamara wait nahi karna padega, seedha UPI se transfer ho jayega."*
- App active adoption surged to 92% in the target city within 30 days.""",
        "failures": [
            ("The Premature Spread Trap", "Opening 1 dealer in 15 different towns, creating zero brand density anywhere.", "Concentrate all field resources to win 1 atomic network before expanding geographically."),
            ("Ignoring the Hard Side", "Signing up 20 dealers who stock paint that sits on shelves because zero painters know the brand.", "Focus 80% of acquisition energy on master contractors (the hard side) to generate pull."),
            ("Premature Automation", "Expecting an app or digital portal to solve the early cold start problem without manual human effort.", "Flintstone early network loops manually; automate only after product-market fit is proven."),
            ("Abandoning the Atomic Cluster Too Early", "Declaring victory after one large stocking order, only to have the dealer churn 90 days later.", "Remain in the cluster until secondary contractor off-take is self-reinforcing.")
        ],
        "checklist": [
            "Atomic network boundaries clearly defined (single mandi / 5 km cluster).",
            "The 'Hard Side' (master painting contractors) identified and prioritized.",
            "Flintstoning tactics (manual demos, high-touch support) active during launch.",
            "Anchor dealer stocking secured using verified contractor demand pull.",
            "Secondary off-take velocity monitored weekly to detect true Tipping Point.",
            "Contiguous geographic expansion planned only after existing atomic nodes are profitable."
        ]
    },
    "eugene-schwartz-awareness-messaging-engine": {
        "title": "Eugene Schwartz Breakthrough Advertising & Market Awareness Engine for Swatch Paints",
        "legend": "Eugene Schwartz (Legendary Copywriter & Author of 'Breakthrough Advertising')",
        "description": "Eugene Schwartz Five Stages of Market Awareness, Market Sophistication, and Direct Response Copywriting for Swatch Paints Marketing Campaigns.",
        "dept": "05_marketing_brand",
        "tag": "eugene-schwartz",
        "purpose": """This skill equips the Swatch Paints Marketing, Advertising, Digital Growth, and Creative teams with Eugene Schwartz’s immortal **Breakthrough Advertising** principles: the **Five Stages of Market Awareness**, **Levels of Market Sophistication**, and customer desire channelization.

In marketing, copywriters and advertising agencies make the catastrophic error of pitching *Product Features* to customers who don't even realize they have a problem, or using generic claims ("Best Quality Paint!") in a market with high sophistication where customers have heard the same claim a thousand times and tuned it out. Advertising cannot create desire from scratch; it can only channel the existing hopes, fears, and frustrations of the homeowner and painter onto Swatch Paints.

The engine's purpose is to:
- Diagnose the exact **Stage of Awareness (Unaware, Problem Aware, Solution Aware, Product Aware, Most Aware)** for every target audience: independent homebuilders, painting contractors, and architects.
- Craft headlines, brochures, WhatsApp messaging, and video scripts matched precisely to the audience's psychological state.
- Navigate **Market Sophistication**: breaking through cynical, crowded paint advertising with fresh mechanisms, proof elements, and dramatic demonstrations.
- Channel homeowner anxieties regarding dampness, efflorescence (shora/namak), and peeling paint into instant inquiries for Swatch protective finishes.""",
        "when_to_use": """- Designing marketing collateral: dealer flex boards, consumer brochures, architect shade cards, and painter leaflets.
- Scripting hyper-local digital ads (Facebook, Instagram, YouTube Shorts, WhatsApp status campaigns).
- High customer drop-off on marketing landing pages or low response rates to dealer WhatsApp broadcasts.
- Launching an advanced technical coating (e.g., thermal reflective roof coating, silicone water-repellent primer, Swatch Rustic).
- Competitors are running heavy mass-media ads, and Swatch must outsmart them with high-converting direct-response messaging.
- Training the sales team how to open conversations with homeowners at construction sites.""",
        "frameworks": """### 6.1 Schwartz's Five Stages of Market Awareness
```
[1. UNAWARE] ──> [2. PROBLEM AWARE] ──> [3. SOLUTION AWARE] ──> [4. PRODUCT AWARE] ──> [5. MOST AWARE]
```

1. **Stage 1: Completely Unaware**
   - The prospect doesn't know they have a problem. They are just building a brick wall.
   - *Headline Approach:* Tell an arresting story or spotlight a hidden risk. *"The hidden chemical inside your groundwater that destroys new plaster within 12 months..."*
2. **Stage 2: Problem Aware**
   - Homeowner sees white salty powder (shora) emerging on their newly painted drawing room wall.
   - *Headline Approach:* Empathize with the pain immediately. *"Tired of paint flaking off your exterior walls after every single monsoon?"*
3. **Stage 3: Solution Aware**
   - Homeowner knows waterproofing primers and elastomeric textures exist, but doesn't know Swatch.
   - *Headline Approach:* Introduce the unique mechanism. *"Why standard acrylic paint traps moisture—and how breathable mineral stone texture keeps walls bone-dry."*
4. **Stage 4: Product Aware**
   - Prospect knows Swatch Paints, but isn't sure how it compares to Asian Paints Apex Ultima.
   - *Headline Approach:* Superiority, proof, and contractor endorsements. *"Tested side-by-side in 48°C Rajasthan heat: Why Swatch Rustic outlasts synthetic emulsions by 4 years."*
5. **Stage 5: Most Aware**
   - Prospect wants Swatch Rustic; they just need the final incentive or offer to pull the trigger.
   - *Headline Approach:* Direct offer, urgency, and dealer availability. *"Get a free texture applicator kit with your first 100 kg Swatch Rustic order before October 15th."*

### 6.2 The Three Levels of Market Sophistication
In Indian decorative paints, market sophistication is at **Stage 4 (Cynical & Saturated)**:
- Everyone claims "Long Lasting", "Waterproof", and "7-Year Warranty". Nobody believes empty adjectives anymore.
- **The Schwartz Solution:** Introduce a **Unique Mechanism**: Explain *mechanistically* WHY Swatch works when others fail (e.g., cross-linking siloxane polymers that create microscopic breathable pores, allowing trapped wall vapor to escape while repelling liquid rainwater).""",
        "decision_algo": """### Step 1: Identify Audience Awareness Level
- Determine who will see this message:
  - Cold Homeowner on Instagram -> Stage 2 (Problem Aware).
  - Visiting Architect -> Stage 3 (Solution Aware).
  - Painter at Dealer Counter -> Stage 4/5 (Product / Most Aware).

### Step 2: Formulate the Mechanism
- DO NOT use generic adjectives: "Best paint", "High coverage", "Premium quality".
- Articulate the scientific/operational mechanism: "Silicone-Enhanced Mineral Matrix" or "Nano-Particle Dispersion".

### Step 3: Match Headline Structure to Awareness Stage
- Stage 2 Headline: Target the symptom and emotional frustration.
- Stage 3 Headline: Spotlight the mechanism and breakthrough.
- Stage 5 Headline: State the price, discount, or bonus directly.

### Step 4: Include Irrefutable Proof Elements
- Every piece of copy must include at least 1 proof element:
  - Macro photograph of cross-cut adhesion test.
  - Video of water beading off a painted sample board.
  - Testimonial from a named local contractor in their town.""",
        "example1": """### Example 1: Crafting an Anti-Efflorescence (Shora) Campaign for Shekhawati
**Situation:** In the Shekhawati region (Churu, Sikar, Jhunjhunu), groundwater salinity causes severe efflorescence (namak/shora) on plaster within 6 months of painting. Homeowners spent thousands on repainting every year in vain.
**Schwartz Stage 2 (Problem-Aware) Copy Created:**
- *Headline:* **"Har Saal Diwali Pe Paint Karwate Hain, Fir Bhi Har Saal Plaster Se Namak Jhadta Hai?"**
- *The Mechanism Introduced:* Explained that synthetic plastic paint seals salt inside the wall, building osmotic pressure until the plaster explodes. Swatch Breathable Damp-Proof Primer uses microscopic siloxane pores that allow moisture to breathe out while blocking salt crystal migration.
- *Proof:* Video of a concrete block treated with Swatch standing in salt water for 90 days with zero white crust.
- **Result:** The campaign generated 420 direct WhatsApp leads from homeowners in 3 weeks, driving ₹18 Lakhs in primer and exterior paint sales through local dealers.""",
        "example2": """### Example 2: Retargeting Architects at Stage 3 (Solution Aware)
**Situation:** Jaipur architects wanted textured facades for boutique hotel projects but were skeptical of paint manufacturers' claims, having seen cheap distemper textures sag and crack.
**Schwartz Solution-Aware Technical Whitepaper:**
- Headline: *"The Structural Physics of Exterior Facades: Why Heavy Cement Textures Sag—and How Micro-Polymer Aggregate Matrix Solves Plaster Cracking."*
- Bypassed marketing jargon; presented laboratory rheology curves and wind-driven rain test certifications.
- Result: Secured architectural specification across 8 luxury resort and residential apartment projects in Jaipur and Udaipur.""",
        "failures": [
            ("Mismatched Awareness Copy", "Shouting product discounts (Stage 5) to cold homeowners who don't know they have a dampness problem (Stage 1).", "Match copy strictly to the recipient's psychological stage of awareness."),
            ("Vague Adjective Addiction", "Filling brochures with 'World-class quality, premium shine, superior durability.'", "Ban empty marketing fluff. Explain the unique mechanism and provide scientific proof."),
            ("Creating Desire from Scratch", "Trying to convince consumers to paint their homes in neon purple when no cultural desire exists.", "Channel existing customer desires (pride in home, protection from rain, saving money on repaints)."),
            ("Proofless Assertions", "Claiming a 5-year exterior guarantee without showing a real-world test wall or local project photo.", "Every marketing claim must be backed by tangible demonstration or third-party proof.")
        ],
        "checklist": [
            "Target audience Stage of Awareness accurately diagnosed before drafting copy.",
            "Headline structure matched to the audience's psychological state.",
            "Unique Mechanism articulated clearly to navigate market sophistication.",
            "Generic adjectives replaced with precise functional descriptions.",
            "At least one undeniable proof element (video demo, lab test, contractor testimonial) included.",
            "Call to action (CTA) clear, actionable, and routed to authorized local dealers."
        ]
    },
    "gary-vaynerchuk-content-attention-engine": {
        "title": "Gary Vaynerchuk Underpriced Attention & Painter Social Media Engine for Swatch Paints",
        "legend": "Gary Vaynerchuk (CEO of VaynerMedia & Author of 'Jab, Jab, Jab, Right Hook' and 'Crushing It')",
        "description": "Gary Vaynerchuk Underpriced Attention, Hyper-Local Social Video, Contractor Community Building, and Day Trading Attention for Swatch Paints.",
        "dept": "05_marketing_brand",
        "tag": "gary-vaynerchuk",
        "purpose": """This skill equips the Swatch Paints Digital Media, Field Brand Ambassadors, and Creative Content teams with Gary Vaynerchuk’s modern operational disciplines: **Underpriced Attention**, **Document Don't Create**, **Jab, Jab, Jab, Right Hook (Give Value Before Asking for Business)**, and hyper-local mobile video execution.

In the Indian hardware and building materials landscape, marketing departments waste massive budgets on traditional vanity media: static roadside billboards that drivers ignore, expensive print newspaper ads that end up wrapping vegetables, and glossy agency commercials featuring Bollywood actors who have never touched a paint brush. Meanwhile, where does the real attention of the painting contractor, the hardware dealer, and the homebuilder live? **In the palm of their hand: on WhatsApp Status, YouTube Shorts, and Instagram Reels.**

The engine's purpose is to:
- Day-trade **Underpriced Attention**: dominating regional mobile video platforms where organic reach is cheap and engagement is authentic.
- Execute the **"Document, Don't Create"** philosophy: filming real job sites, raw material batch dispersion, texture trowel techniques, and real painter reactions rather than scripted studio ads.
- Institutionalize the **Jab-Right Hook Ratio**: providing 3 to 5 value touches (applicator tutorials, tips on handling wall dampness, painter felicitations) before asking for an order.
- Turn field sales officers and technical applicators into **Hyper-Local Content Creators** who build authentic relationships across regional construction communities.""",
        "when_to_use": """- Building organic brand buzz and social proof in a competitive territory without a multi-crore television ad budget.
- Running recruitment and educational campaigns for the Swatch Ustaad Painter Community.
- Demonstrating the physical workability, coverage, and aesthetic finishes of Swatch Rustic to young contractors.
- Creating viral, shareable content that painters willingly forward to homeowners over WhatsApp.
- Celebrating and felicitating top-tier master painters to turn them into fiercely loyal brand champions.
- Training territory sales reps on how to use their personal smartphones to generate local dealer leads.""",
        "frameworks": """### 6.1 Day Trading Attention & Underpriced Platforms
Attention shifts rapidly. In tier-2/3 Indian markets:
- Overpriced Attention: Print newspapers, city billboards, generic radio spots.
- **Underpriced Attention:** 
  - WhatsApp Status (viewed religiously by dealers, local builders, and painter crews).
  - YouTube Shorts showing 30-second texture application techniques.
  - Instagram Reels targeted by city (Kota, Bundi, Jaipur, Udaipur) showcasing dramatic before-and-after home transformations.

### 6.2 Document, Don't Create
Stop hiring expensive ad agencies to shoot fake studio commercials. Document real factory and field reality:
- Film the plant chemist conducting the cross-cut adhesion test on a cured sample panel.
- Film a master contractor in Bhilwara applying Swatch Rustic with a notched trowel, explaining how the texture hides substrate plaster unevenness.
- Film a dealer receiving a fresh morning shipment from the local depot within 4 hours of ordering.
- Authentic, raw, high-definition smartphone video converts 5x better than polished corporate propaganda.

### 6.3 Jab, Jab, Jab, Right Hook (The Give-Give-Give-Ask Model)
- **Jab 1 (Value):** 30-second video on how to treat salty efflorescence (namak) before applying primer.
- **Jab 2 (Value):** Post congratulating Master Painter Ramesh Kumar for completing a 12-flat project with Swatch Shine.
- **Jab 3 (Value):** Free downloadable mobile shade card and coverage calculator for contractors.
- **Right Hook (The Ask):** *"Order your Diwali stocking bundle today from your nearest authorized dealer and get a free branded applicator apron."*""",
        "decision_algo": """### Step 1: Content Production at the Gemba
- Mandate field sales reps and technical demonstrators to record **2 raw video clips daily** on job sites:
  - 1 clip demonstrating product workability / finish.
  - 1 clip interviewing a painter or dealer about their experience.

### Step 2: Micro-Content Editing & Formatting
- Convert horizontal field footage into vertical 9:16 mobile format.
- Add bold, high-contrast Hindi / regional subtitles (80% of mobile users watch videos with sound off).
- Keep video pacing fast: Hook the viewer in the first 3 seconds with a visual demonstration.

### Step 3: Distribution Engine Execution
- Push content across 3 hyper-local channels:
  1. Territory Sales WhatsApp Broadcast Lists (direct to active painters & dealers).
  2. Localized YouTube Shorts & Instagram Reels tagged with city hashtags (#KotaPaints, #JaipurArchitects).
  3. Swatch Ustaad App Community Feed.

### Step 4: Engagement & Direct Response
- Community managers must reply to 100% of user comments within 15 minutes.
- If a painter asks: *"Yeh texture Bundi me kahan milega?"*, immediately connect them via WhatsApp to the nearest stocking dealer.""",
        "example1": """### Example 1: The Viral WhatsApp Texture Video in Hadoti
**Situation:** Swatch launched a new natural sandstone finish in Swatch Rustic. Traditional print flyers distributed to dealers resulted in zero inquiries.
**Vaynerchuk 'Document' Strategy Applied:**
- Technical demonstrator took his phone to an active villa site in Kota. Filmed a 45-second close-up video of a local painter using a stainless steel trowel to create a rustic stone groove pattern.
- The painter spoke in local Hadoti dialect: *"Bhaiya, iska spreading bohot smooth hai, aur ek baar set ho jaye toh pathar jaisa ho jata hai."*
- Pushed the video to a WhatsApp broadcast group of 140 local painters and dealers.
- Within 48 hours, the video was forwarded over 1,200 times across regional painter WhatsApp groups.
- Over 22 contractors walked into local hardware shops with the video on their screens asking: *"Yeh wala maal kahan hai?"*
- Result: Generated ₹6.4 Lakhs in texture orders in 10 days with zero advertising spend.""",
        "example2": """### Example 2: The 'Painter of the Month' Recognition Campaign
**Situation:** Painting contractors felt ignored by multinational paint brands, who treated them as cheap manual laborers.
**Jab-Jab-Jab Community Strategy:**
- Swatch launched a weekly social media spotlight: "Kota Ke Ustaad".
- Profiled a senior painter, his 25-year career, his family, and showed his best villa finishing work.
- Gifted him a framed certificate signed by Ashutosh Sharma Sir and posted the video on Instagram and Facebook.
- The painter shared it proudly with all his relatives and clients: *"Pehli baar kisi company ne humari mehnat ki izzat ki."*
- Result: 18 other contractor crews proactively registered with Swatch to be featured; brand loyalty in that mandi became an unbreakable moat.""",
        "failures": [
            ("Over-Produced Corporate TV Ads", "Spending ₹10 Lakhs on an ad agency to produce a glossy video that looks like an insurance commercial.", "Focus on authentic, raw, smartphone-filmed job-site realities that painters relate to."),
            ("Right Hook Without Jabs", "Blasting dealers and painters daily with aggressive sales messages: 'Buy Now! Target Pending!'", "Provide value, education, and respect first. Earn the right to ask for an order."),
            ("Ignoring Video Comments", "Posting videos online but failing to respond to questions about pricing and dealer locations.", "Speed is king: convert video interest into dealer footfall within 15 minutes of an inquiry."),
            ("Desktop-Oriented Content", "Creating horizontal widescreen PDFs and brochures that are impossible to read on a mobile phone.", "Mobile-first, vertical 9:16 format with high-contrast Hindi captions is mandatory.")
        ],
        "checklist": [
            "Content created by documenting real field, lab, and job-site activities daily.",
            "Vertical (9:16) format with bold Hindi/regional subtitles enforced for all video assets.",
            "Jab-to-Right Hook ratio maintained: at least 3 value/educational posts for every 1 commercial pitch.",
            "Field sales reps actively broadcasting authentic content via WhatsApp Status.",
            "Social media comments and inquiries responded to within 15 minutes.",
            "Painter and contractor partners celebrated publicly as respected craftspeople."
        ]
    },
    "philip-kotler-digital-marketing-engine": {
        "title": "Philip Kotler Marketing 5.0 & Omnichannel Customer Journey Engine for Swatch Paints",
        "legend": "Philip Kotler (Author of 'Marketing 5.0: Technology for Humanity' & 'Marketing Management')",
        "description": "Philip Kotler Marketing 5.0, 5A Customer Journey (Aware, Appeal, Ask, Act, Advocate), Omnichannel Retail-to-Digital Integration for Swatch Paints.",
        "dept": "05_marketing_brand",
        "tag": "philip-kotler-digital",
        "purpose": """This skill equips the Swatch Paints Marketing Strategy, Digital Systems, and Retail Channel teams with Philip Kotler’s advanced **Marketing 5.0** framework: technology for humanity, the **5A Customer Journey Model**, and **Omnichannel Phygital (Physical + Digital)** integration.

In the contemporary Indian decorative coatings market, the customer path to purchase has fractured: a homeowner does not simply walk into a hardware shop and buy what the dealer tells them. They research exterior color palettes on Pinterest, look at Instagram reels of textured walls, ask their painting contractor for brand advice, check online user reviews, visit an authorized retail dealer to see physical shade swatches, and demand instant digital color visualization on their phone before spending ₹1 Lakh on a repaint.

The engine's purpose is to:
- Map and optimize the complete **5A Customer Journey: Aware -> Appeal -> Ask -> Act -> Advocate**.
- Build an airtight **Phygital Bridge**: seamlessly connecting digital homeowner inquiries to physical authorized paint dealers and verified local master applicators.
- Deploy **Contextual & Predictive Marketing**: using weather, construction permits, and regional festival cycles to deliver targeted digital shade recommendations.
- Transform one-time paint buyers into passionate **Brand Advocates** who actively promote Swatch Paints on digital networks.""",
        "when_to_use": """- Designing the omnichannel consumer experience across website, mobile apps, social media, and physical dealer shops.
- High lead drop-off between online digital ad clicks and physical dealer visits.
- Implementing digital visualization tools (virtual wall painter app, digital shade cards, AR room preview).
- Establishing lead management protocols that route online homeowner painting inquiries to local authorized dealers.
- Auditing brand advocacy and referral loops across the retail dealer network.
- Upgrading traditional dealer counters into modern, digital-enabled "Swatch Color Studios".""",
        "frameworks": """### 6.1 The 5A Customer Journey in Decorative Paints
Kotler proved that customer journeys are no longer linear funnels; they flow through 5 dynamic touchpoints:
```
[AWARE] ──> [APPEAL] ──> [ASK] ──> [ACT] ──> [ADVOCATE]
```
1. **Aware:** Homeowner is passively exposed to Swatch through local billboard, painter recommendation, or social reel.
2. **Appeal:** Homeowner remembers Swatch because of its unique positioning (authentic stone texture / anti-efflorescence protection).
3. **Ask (The Critical Shift):** Homeowner actively investigates: asks their painting thekedaar, browses Google, or examines digital shade swatches.
4. **Act:** Homeowner visits authorized dealer, verifies physical sample board, and completes the purchase.
5. **Advocate:** Homeowner is so thrilled with the finish and durability that they proudly post photos on Instagram and recommend Swatch to neighbors.

### 6.2 The Phygital Architecture for Paint Retail
Physical retail and digital convenience must reinforce each other:
- **Digital Driver:** Homeowner visualizes their living room wall in Swatch Rustic on their phone.
- **Physical Handshake:** Digital app issues an exclusive QR voucher redeemable at the nearest authorized Swatch dealer for a free physical sample board.
- **Human Connection:** Dealer introduces the homeowner to a certified Swatch Ustaad applicator.
- **Loop Closes:** Order is billed at the dealer; painter earns digital loyalty tokens; customer receives digital warranty certificate.

### 6.3 Marketing 5.0: The Tech-Human Balance
Kotler emphasizes that technology must augment human relationships, not replace them:
- Automated AI chatbots handle routine queries (dealer location, product TDS data, basic coverage math).
- High-touch human interactions are reserved for technical problem-solving, architectural consultation, and custom shade formulation.""",
        "decision_algo": """### Step 1: 5A Journey Bottleneck Audit
- Measure conversion ratios between each 5A stage in a target city:
  - If Aware -> Appeal is low: Positioning is weak; rewrite messaging using Schwartz/Ries frameworks.
  - If Appeal -> Ask is low: Call to action is unclear; add direct WhatsApp inquiry buttons.
  - If Ask -> Act is low: Dealers are out of stock or steering clients to competitors; fix dealer alignment and margins.
  - If Act -> Advocate is low: Product quality or application support failed; trigger Deming/DMAIC root-cause review.

### Step 2: Digital-to-Dealer Lead Routing Protocol
- When a homeowner submits an inquiry via digital ad or website:
  - Automated system matches inquiry to the nearest authorized stocking dealer within 60 seconds.
  - SMS/WhatsApp alert sent simultaneously to the homeowner (with dealer contact) and the dealer (with customer contact).
  - Field sales rep receives notification to follow up within 24 hours.

### Step 3: Post-Purchase Advocacy Automation
- 30 days after project completion:
  - Automated WhatsApp message sent to homeowner: *"Aapke naye ghar ka paint kaisa lag raha hai?"*
  - Invite homeowner to upload a photo to receive a digital 5-year warranty certificate.
  - Seamlessly prompt for a Google Business review for the local dealer.""",
        "example1": """### Example 1: Fixing the 'Ask-to-Act' Drop-off in Jaipur Urban
**Situation:** Digital ads in Jaipur generated 850 monthly website clicks and shade card downloads (High 'Ask'), but authorized dealers reported only 12 walk-ins (Pathetic 'Act'). Leads were evaporating into thin air.
**Kotler Omnichannel Redesign Applied:**
- Replaced the passive PDF shade card download with an interactive "Instant Color Consultation Voucher".
- When a homeowner requested a shade consultation, the platform automatically assigned the lead to the nearest stocking dealer and sent a WhatsApp coupon for a free 1-litre trial tester.
- The dealer was alerted immediately and called the customer within 2 hours.
- Conversion from digital inquiry to physical shop billing jumped from 1.4% to 28%, generating ₹16 Lakhs in incremental retail sales in 60 days.""",
        "example2": """### Example 2: Driving Organic Advocacy via Digital Warranty Certificates
**Situation:** Competitors offered verbal 5-year exterior warranties that dealers rarely honored, leaving consumers frustrated and skeptical.
**Kotler Advocate Engine Applied:**
- Swatch introduced a digital tamper-proof **E-Warranty Certificate** generated directly from the ERP upon batch verification.
- To activate the warranty, the homeowner scanned their bucket QR code and uploaded a completed photo of their home.
- The system generated an elegant, personalized digital certificate suitable for framing or sharing on social media.
- Over 62% of homeowners shared their home photos on WhatsApp Status and Facebook with the caption: *"My home protected by Swatch Paints 5-Year Shield."*
- Created a powerful organic advocacy loop that drove new customer inquiries at zero customer acquisition cost.""",
        "failures": [
            ("Digital Silo Disconnect", "Running expensive digital ad campaigns that local paint dealers have never heard of.", "Synchronize digital campaigns with local dealer stocking and sales rep beat plans."),
            ("The 'Ask-to-Act' Black Hole", "Collecting consumer leads online and letting them sit in an Excel sheet for 2 weeks.", "Route leads automatically to local dealers and sales officers within 60 seconds."),
            ("Over-Automated Coldness", "Forcing a customer with a serious efflorescence problem to chat with a brainless automated bot.", "Kotler Tech-Human balance: Escalate complex technical questions to human chemists within 5 minutes."),
            ("Neglecting the Advocate Stage", "Ignoring the customer immediately after the invoice is paid, losing valuable word-of-mouth.", "Automate post-purchase follow-up, digital warranty issuance, and Google review requests.")
        ],
        "checklist": [
            "5A customer journey mapped, monitored, and optimized across all regional markets.",
            "Phygital integration operational: digital inquiries routed to physical authorized dealers.",
            "Lead routing automation ensures dealer and rep notifications within 60 seconds.",
            "Digital shade cards and visualization tools integrated with live dealer inventory.",
            "Automated post-purchase follow-up and digital warranty certification active.",
            "Customer advocacy loop driving verified Google reviews and organic social shares."
        ]
    },

    # === 06_HR_LEGAL ===
    "geoff-smart-who-hiring-engine": {
        "title": "Geoff Smart & Randy Street 'Who: The A Method for Hiring' Engine for Swatch Paints",
        "legend": "Geoff Smart & Randy Street (Founders of ghSMART & Authors of 'Who: The A Method for Hiring')",
        "description": "Geoff Smart 'Who' Methodology, Role Scorecards, Topgrading Sourcing, Structured Competency Interviews, and Reference Audits for Swatch Paints Talent Acquisition.",
        "dept": "06_hr_legal",
        "tag": "geoff-smart",
        "purpose": """This skill equips the Swatch Paints Human Resources, Executive Leadership, and Department Heads with Geoff Smart and Randy Street’s **'Who' A-Method for Hiring**.

In traditional Indian enterprises, hiring is plagued by the "Voodoo Hiring Trap": managers make hiring decisions based on subjective gut feelings, superficial charm during an unstructured 20-minute chat, or impressive academic resumes. This leads to a disastrous 50%+ hiring failure rate: smooth-talking sales officers who cannot sell paint, plant chemists who lack discipline and ruin batches, and depot managers who mishandle inventory and resign within 6 months.

The engine's purpose is to:
- Eliminate vague job descriptions and replace them with rigorous, quantifiable **Role Scorecards** (Mission, Outcomes, Competencies).
- Build a continuous, proactive **Talent Sourcing Pipeline** to attract "A Players" before vacancies arise.
- Conduct deep, chronological **Topgrading Interviews** that uncover the candidate’s true operational track record over their entire career.
- Execute investigative, high-rigor **Reference Threat Interviews (TORC)** to eliminate resume exaggeration and verify cultural fit.""",
        "when_to_use": """- Recruiting Territory Sales In-Charges (TSIs), Area Sales Managers (ASMs), and Regional Commercial Heads.
- Hiring technical personnel: Senior Formulation Chemists, QC Lab Managers, and Plant Maintenance Engineers.
- Selecting high-trust operational roles: Depot In-Charges, Cash Controllers, and Procurement Managers.
- High turnover or recurring performance failures in a specific department or sales territory.
- Structuring the company’s annual campus and lateral talent acquisition strategy under the direction of Ashutosh Sharma Sir.
- Upgrading existing staff through internal promotions and leadership transitions.""",
        "frameworks": """### 6.1 The Definition of an "A Player"
*"A candidate who has at least a 90% chance of achieving a set of outcomes that only the top 10% of possible candidates could achieve."*

### 6.2 The Four Pillars of the 'Who' Method
```
1. SCORECARD   ──> Blueprint of what success looks like (Outcomes, not tasks).
2. SOURCE      ──> Systematic hunting of talent through referral networks.
3. SELECT      ──> 4-Stage structured interview process (Screening, Topgrading, Focus, Reference).
4. SELL        ──> Closing the A Player on the 5 F's (Fit, Family, Freedom, Fortune, Fun).
```

### 6.3 The Role Scorecard Structure
A Job Description lists tasks; a Scorecard lists measurable outcomes:
- **Mission:** A single sentence summarizing the role's fundamental purpose.
- **Outcomes (3 to 5 Quantified Targets):** 
  - e.g., *"Open 25 active billing dealer counters in Hadoti within 180 days."*
  - e.g., *"Maintain DSO under 28 days with zero bad debts."*
- **Core Competencies:** Cultural and behavioral traits (Integrity, Persistence, Chemical Rigor, Coachability).

### 6.4 The TORC Technique (Threat of Reference Check)
Early in the interview, establish truthfulness:
- *"In our final round, we will ask you to set up interviews with your past 3 bosses. When we speak to them, what will they tell us were your biggest strengths and your biggest areas for development?"*
- This immediately shatters fake resume claims and produces raw honesty.""",
        "decision_algo": """### Step 1: Draft the Role Scorecard
- Department head and HR must agree on the Scorecard before writing any job posting.
- Prohibit generic laundry lists of duties ("Must manage sales"). Enforce quantified outcomes.

### Step 2: Sourcing via Professional Networks
- Prohibit passive newspaper ads.
- Leverage employee referrals, supplier intelligence, and executive search to find passive A-players currently succeeding at rival paint companies.

### Step 3: The 4-Stage Interview Process
1. **Screening Interview (30 mins):** Eliminate obvious mismatches. (Career goals, professional strengths, red flags).
2. **Topgrading Chronological Interview (90-120 mins):** Walk through every job held from college to present:
   - What were you hired to do?
   - What accomplishments are you most proud of?
   - What were the low points / failures?
   - What was your boss's name, and how would they rate your performance on a 1-10 scale?
   - Why did you leave?
3. **Focused Competency Interview:** Drill deep into specific functional skills (e.g., paint formulation chemistry, dealer credit recovery).
4. **Reference Audits:** Speak directly to at least 3 past supervisors.

### Step 4: The Selling Phase (5 F's)
- Identify what matters most to the candidate (Fortune, Freedom, Family, Fit, Fun) and tailor the offer package to close them decisively.""",
        "example1": """### Example 1: Hiring an A-Player Area Sales Manager for Jaipur
**Situation:** Swatch had hired two consecutive ASMs who failed: both were charming in interviews, had 15 years of experience at big brands, but did zero field work and quit when targets were missed.
**Smart 'Who' Method Applied:**
- Replaced the vague JD with a Scorecard: Mission was to open 40 profitable counters and establish a ₹25 Lakh monthly run-rate in 9 months.
- Conducted a Topgrading interview with Candidate R:
  - Discovered that at his previous company, his reported "huge sales growth" was actually driven by a corporate national marketing campaign, while his specific territory counter count was flat.
  - Candidate S: When asked for past bosses' names for reference checks, he hesitated and made excuses. (Flagged and rejected).
  - Candidate T: Confidently provided phone numbers of his last 3 regional managers. Reference checks confirmed he was a tireless field coach who personally visited 8 dealers a day and had high integrity.
- Hired Candidate T: He achieved 112% of Scorecard outcomes in his first 6 months.""",
        "example2": """### Example 2: Selecting a Senior Paint Formulation Chemist
**Situation:** The R&D lab needed a specialist chemist in water-based exterior emulsions. Previous hires had copied formulas from textbooks that cracked under Rajasthan weather testing.
**Focused Competency & Reference Protocol:**
- Evaluated candidates with a practical laboratory blind test: Given 4 raw resins and pigments, formulate a sample with specific viscosity and opacity within 3 hours.
- Top candidate formulated a stable dispersion that passed freeze-thaw and scrub resistance tests effortlessly.
- Reference check with his previous laboratory head confirmed deep hands-on chemical knowledge and meticulous record-keeping.
- Result: New chemist formulated the breakthrough Swatch Rustic anti-crack matrix within 90 days of joining.""",
        "failures": [
            ("Voodoo Gut-Feel Hiring", "Hiring a candidate because 'I liked his confidence and he spoke good English.'", "Strict rule: Hiring decisions must be backed by quantifiable Scorecard evaluations and Topgrading data."),
            ("Accepting Curated Reference Letters", "Calling the candidate's personal best friend or reading pre-written letters of recommendation.", "You must speak directly on the phone to past direct supervisors using the TORC method."),
            ("Hiring for Tasks Instead of Outcomes", "Evaluating candidates by how many hours they worked rather than verifiable business results.", "Define success strictly through 3 to 5 quantifiable 12-month outcomes on the Scorecard."),
            ("Compromising on Cultural Fit (Integrity)", "Hiring a high-billing sales rep who has a track record of lying on expense vouchers or abusing credit.", "Never compromise on integrity. A toxic high-performer will destroy organizational culture.")
        ],
        "checklist": [
            "Role Scorecard (Mission, Outcomes, Competencies) drafted and approved before recruitment starts.",
            "Proactive sourcing executed through industry referral networks.",
            "Chronological Topgrading interview (90+ minutes) conducted for all managerial hires.",
            "Threat of Reference Check (TORC) utilized to ensure absolute candidate candor.",
            "Minimum 3 direct telephone reference checks completed with past supervisors.",
            "Hiring decision aligns with an estimated >=90% probability of achieving Scorecard outcomes."
        ]
    },
    "john-maxwell-5-levels-leadership-engine": {
        "title": "John C. Maxwell 5 Levels of Leadership & Influence Engine for Swatch Paints",
        "legend": "Dr. John C. Maxwell (World's Foremost Leadership Authority & Author of 'The 21 Irrefutable Laws of Leadership')",
        "description": "John C. Maxwell 5 Levels of Leadership, Law of the Lid, Developing Leaders Around You, and Relational Influence for Swatch Paints Organizational Development.",
        "dept": "06_hr_legal",
        "tag": "john-maxwell",
        "purpose": """This skill equips the Swatch Paints Executive Leadership, Plant Managers, Sales Directors, and Territory Supervisors with John C. Maxwell’s world-renowned **5 Levels of Leadership** and the **21 Irrefutable Laws of Leadership**.

In manufacturing and sales enterprises, managers frequently rely on blunt positional authority: *"Do this because I am your boss and I said so!"* This is **Level 1 (Position) Leadership**, the lowest and most ineffective form of leadership. Workers and sales officers obey only because they have to, giving the bare minimum effort necessary to avoid getting fired. When problems arise, blame cascades downward, employee turnover spikes, and field reps abandon the company at the first rival offer.

The engine's purpose is to:
- Guide leaders to progress through Maxwell's **Five Levels: Position -> Permission -> Production -> People Development -> Pinnacle**.
- Overcome the **Law of the Lid**: recognizing that an organization's growth is strictly capped by the leadership ability of its founders and executives.
- Foster **Level 2 (Permission) Relationships**: earning the genuine trust and willing cooperation of plant workers, truck drivers, sales officers, and dealer partners.
- Build a self-replicating engine of **Level 4 (People Development) Leaders** who coach, empower, and multiply leaders throughout Sharma Industries.""",
        "when_to_use": """- Developing junior sales supervisors and plant shift in-charges into inspiring, effective leaders.
- High voluntary employee turnover in a factory department or regional sales branch.
- Resolving toxic workplace morale, passive resistance, or union/labor friction on the factory floor.
- Structuring leadership succession planning and managerial coaching programs.
- Evaluating managerial promotions: determining whether an individual has real influence or merely a fancy title.
- Inspiring cross-departmental teams to achieve extraordinary turnaround targets under pressure.""",
        "frameworks": """### 6.1 The 5 Levels of Leadership Hierarchy
```
LEVEL 5: PINNACLE           ──> Respect: People follow because of who you are and what you represent.
       ▲
LEVEL 4: PEOPLE DEVELOPMENT ──> Reproduction: People follow because of what you have done for them.
       ▲
LEVEL 3: PRODUCTION         ──> Results: People follow because of what you have done for the enterprise.
       ▲
LEVEL 2: PERMISSION         ──> Relationships: People follow because they WANT to follow you.
       ▲
LEVEL 1: POSITION           ──> Rights: People follow only because they HAVE to (Lowest level).
```

### 6.2 Key Maxwell Leadership Laws Operationalized
1. **The Law of the Lid:** Leadership ability determines a person's level of effectiveness. If a Plant Manager's leadership ability is a 5 out of 10, the plant's operational effectiveness can never rise above a 4. To lift performance, you must lift the leadership lid.
2. **The Law of the Picture:** People do what people see. If the Area Sales Manager arrives late, complains about company leadership, and makes excuses for missed targets, the field reps will mirror those exact behaviors.
3. **The Law of Buy-In:** People buy into the leader first, then the vision. You cannot sell a difficult turnaround plan until your team trusts your personal character.
4. **The Law of the Inner Circle:** A leader's potential is determined by those closest to them. Surround yourself with high-integrity operators who challenge your thinking and execute ruthlessly.""",
        "decision_algo": """### Step 1: Diagnose the Manager's Current Leadership Level
- Observe team dynamics:
  - Do subordinates work enthusiastically when the boss leaves the room? (Level 2/3).
  - Do subordinates give minimum compliant output and check their watches at 04:55 PM? (Trapped at Level 1).

### Step 2: Elevate from Level 1 (Position) to Level 2 (Permission)
- Prohibit leading by positional rank.
- Manager must listen to team members, understand their personal motivations, and show genuine human care.
- Conduct monthly personal development 1-on-1s focused on the employee's growth, not just company quotas.

### Step 3: Drive Level 3 (Production Results) by Example
- The leader must lead from the front: Co-ride with struggling sales officers on tough dealer beats; stand on the plant floor during complex batch changeovers.
- Demonstrate that the leader knows how to deliver victories.

### Step 4: Institute Level 4 (People Development) Succession
- Spend 20% of management time deliberately coaching top 2 potential successors.
- Follow Maxwell’s 5-Step Apprenticeship Model:
  1. I do it.
  2. I do it and you watch.
  3. You do it and I watch.
  4. You do it.
  5. You do it and train someone else.""",
        "example1": """### Example 1: Turning Around a Demoralized Factory Packing Shift
**Situation:** Shift B in the packaging division had high absenteeism (24%), constant can-filling spills, and bitter hostility toward the supervisor, who shouted and threatened workers with wage cuts (Level 1 Position).
**Maxwell Leadership Transformation Applied:**
- Replaced the abusive supervisor with a Level 2/3 Leader from maintenance.
- New supervisor spent his first week listening to workers, fixing broken pallet jacks, and installing ventilation fans at the hot filling station (Building Permission).
- Worked side-by-side with operators on the canning line during peak morning runs (Demonstrating Production by Example).
- Praised operators publicly for clean runs and coached them on machine adjustments.
- Result: Absenteeism dropped from 24% to 3% in 60 days; packaging line throughput rose by 32% with zero labor disputes.""",
        "example2": """### Example 2: Lifting the 'Lid' on a Stagnant Sales Territory
**Situation:** The Jodhpur sales territory was stuck at ₹15 Lakhs monthly turnover for 3 years. The RSM blamed "lazy reps" and "tough competition."
**Law of the Lid Diagnostic:**
- The ASM was a Level 1 micromanager who hoarded dealer contacts, never coached his reps, and took personal credit for all orders. His leadership lid was a 3.
- Enrolled the ASM in structured leadership coaching; shifted his primary KPI from personal sales to *Developing Two Independent Field Officers into Assistant ASMs*.
- Implemented the 5-step apprenticeship model on dealer visits.
- Within 9 months, both field officers were autonomously managing large distributor territories, and total Jodhpur revenue surged to ₹38 Lakhs/month.""",
        "failures": [
            ("Trapped in Level 1 Position", "Believing your job title gives you the right to dictate and abuse team members.", "Earn moral authority through competence, character, and relationship building; drop positional arrogance."),
            ("Violating the Law of the Picture", "Demanding punctuality and hard work while arriving late and leaving early.", "Model the exact work ethic, integrity, and discipline you expect from your team."),
            ("Failing to Develop Successors", "Hoarding knowledge and authority out of insecurity, leaving the department paralyzed if you take leave.", "True leaders build leaders, not followers. Practice the 5-step apprenticeship model daily."),
            ("Ignoring the Inner Circle", "Keeping low-performing yes-men close because they flatter your ego.", "Surround yourself with honest, capable leaders who hold you accountable to high enterprise standards.")
        ],
        "checklist": [
            "Leaders evaluated on relational influence (Level 2/3) rather than formal job titles.",
            "Managers spend deliberate coaching time developing frontline team members.",
            "Leaders demonstrate production excellence by example (Law of the Picture).",
            "5-step leadership apprenticeship model active in sales and plant operations.",
            "Internal promotion pipelines established for all mission-critical roles.",
            "Culture of mutual respect, dignity, and shared purpose operationalized enterprise-wide."
        ]
    },
    "kautilya-arthashastra-compliance-engine": {
        "title": "Kautilya Arthashastra Corporate Governance & Anti-Fraud Engine for Swatch Paints",
        "legend": "Kautilya (Chanakya - Prime Minister of Mauryan Empire & Author of 'Arthashastra')",
        "description": "Kautilya Arthashastra Statecraft, Internal Audit Vigilance, Dual-Signoff Controls, Anti-Corruption, and Legal Compliance for Swatch Paints.",
        "dept": "06_hr_legal",
        "tag": "kautilya-governance",
        "purpose": """This skill equips the Swatch Paints Legal, Corporate Vigilance, Internal Audit, and Executive Leadership teams with Kautilya’s (Chanakya’s) timeless statecraft from the **Arthashastra**: institutional governance, **Internal Vigilance (Gudhapurusha)**, the **Three-Way Separation of Powers**, and rigorous **Anti-Fraud Controls**.

In manufacturing enterprises with high cash float and distributed operations (remote warehouses, regional depots, mobile sales forces, bulk raw material purchases), financial and operational fraud is an ever-present existential risk. Left unchecked, enterprises rot from within: procurement managers take secret kickbacks from chemical suppliers, depot in-charges create ghost inventory to hide theft, sales officers fabricate travel expense vouchers, and transport brokers bill for phantom shipments.

The engine's purpose is to:
- Establish Kautilya's **Dual-Signoff & Separation of Custody**: ensuring that no single individual has the unchecked power to purchase, approve, receive, and pay.
- Institute proactive **Randomized Unannounced Audits (Surprise Gemba Audits)** across all regional depots and plant godowns.
- Deploy an airtight **Whistleblower & Vigilance Channel** that protects honest employees while rooting out corruption.
- Safeguard the enterprise’s intellectual property (formulation recipes, dealer ledgers, margin master tables) against industrial espionage.""",
        "when_to_use": """- Establishing corporate governance, authorization matrices, and spending limit policies.
- Investigating suspected inventory leakage, scrap pilferage, or stock discrepancies at plant or depots.
- Auditing raw material procurement contracts where supplier favoritism or kickbacks are suspected.
- Managing legal compliance, statutory contracts, distributor agreements, and labor laws.
- Securing formulation trade secrets, manufacturing chemical recipes, and digital database access.
- Conducting internal fraud investigations and disciplinary proceedings under the authority of Ashutosh Sharma Sir.""",
        "frameworks": """### 6.1 Kautilya's Fundamental Law of Human Governance
*"Just as it is impossible not to taste honey or poison that finds itself at the tip of the tongue, so it is impossible for an officer handling state treasury not to taste the king’s wealth, unless governed by strict structural vigilance."*

Kautilya did not rely on naive trust; he built **Airtight Structural Systems**:
1. **Separation of Custody & Accounting:** The officer who holds the physical goods must never keep the ledger; the accountant who records the ledger must never touch the physical goods.
2. **Periodic Rotation of Sensitive Posts:** Depot managers and procurement officers must be rotated every 2 to 3 years to prevent the formation of entrenched corrupt local syndicates.
3. **Surprise Unannounced Verification:** Pre-scheduled audits are useless because fraudsters hide discrepancies in advance. True audits must be surprise inspections.

### 6.2 The Three Institutional Locks of Enterprise Governance
```
[LOCK 1: PROCUREMENT INTEGRITY] ──> Sealed competitive vendor bids + Lab quality pre-clearance.
                ▲
[LOCK 2: CUSTODY & GATE PASS]   ──> Automated weighbridge + Gate-inward security barcode scan.
                ▲
[LOCK 3: PAYMENT CLEARANCE]     ──> 3-Way digital match (PO + Gate Inward + GSTR-2B) before voucher release.
```

### 6.3 Protecting Enterprise Intellectual Property
- Paint formulation recipes (Level 2 BOMs) are state secrets.
- In ERP, recipe concentrations must be encrypted; operators see only "Additive Code A-4" rather than the raw chemical molecular name, preventing trade secret theft by departing employees.""",
        "decision_algo": """### Step 1: Enforce the Financial Authority Matrix
- No employee can authorize spending beyond their digital limit:
  - TSI: ₹0.
  - ASM: Up to ₹5,000 for verified dealer marketing support.
  - Commercial Director: Up to ₹50,000.
  - Expenditures >₹50,000 require CFO / CEO direct approval.

### Step 2: Implement Mandatory 3-Way Matching
- ERP automatically locks payment vouchers unless:
  1. PO matches invoice price.
  2. Electronic Gate Pass confirms physical delivery weight.
  3. Quality Lab Certificate confirms specification pass.

### Step 3: Execute Randomized Unannounced Depot Audits
- Central Internal Audit team descends on a regional depot without advance notice.
- Perform 100% physical cycle count of top 20 high-value SKUs within 4 hours.
- Freeze system billing during the physical audit count.

### Step 4: Whistleblower Protection & Disciplinary Action
- Maintain a direct, confidential reporting channel to Ashutosh Sharma Sir's desk.
- If fraud is proven: Zero tolerance. Immediate termination, legal recovery of stolen assets, and filing of police complaint.""",
        "example1": """### Example 1: Uncovering a Raw Material Procurement Kickback Syndicate
**Situation:** Procurement was purchasing Calcium Carbonate extender at ₹8.50/kg from a specific vendor in Alwar, while market spot rates were ₹6.80/kg. Over 1,200 tonnes per year, this represented a massive ₹20+ Lakh loss.
**Kautilyan Vigilance Protocol Applied:**
- Initiated a secret market price benchmarking audit across 5 independent mining suppliers.
- Audited the procurement officer's phone logs and email correspondence.
- Found that the officer was receiving a ₹0.80/kg monthly kickback deposited into a relative's bank account.
- **Action:** Terminated the corrupt officer immediately; blacklisted the supplier; negotiated a direct contract with a certified mine operator at ₹6.60/kg, saving ₹22.8 Lakhs annually.""",
        "example2": """### Example 2: Eliminating Ghost Stock at a Regional Satellite Depot
**Situation:** A depot manager reported an inventory "shrinkage loss" of 320 buckets of exterior paint (worth ₹4.8 Lakhs), claiming they were damaged by warehouse roof water leaks during monsoons.
**Surprise Forensic Audit Applied:**
- Internal audit team arrived unannounced within 6 hours.
- Demanded to see the physical damaged buckets and spilled paint effluent. The manager could only produce 12 empty broken buckets.
- Audited local CCTV footage and gate registers: Discovered the manager had secretly loaded the paint onto an unauthorized private tempo at 11:00 PM on Sunday night and sold it for cash to an unverified contractor.
- **Outcome:** Recovered the full ₹4.8 Lakhs from the manager's security deposit; handed the case to legal authorities; installed automated biometric access and 24/7 cloud-monitored CCTV across all depot gates.""",
        "failures": [
            ("Blind Naive Trust", "Assuming an employee won't steal because 'he has been with us for 10 years.'", "Governance requires systems, dual-signoffs, and unannounced audits, not blind emotional trust."),
            ("Single-Point Authorization", "Allowing one person to order, receive, approve, and disburse company funds.", "Enforce absolute separation of duties: three independent sets of eyes on all financial transactions."),
            ("Scheduled Toothless Audits", "Informing depot managers 2 weeks in advance that auditors are visiting.", "Surprise audits are the only true test of operational and inventory reality."),
            ("Tolerating 'Minor' Compromises", "Overlooking a ₹500 fake fuel bill because the sales rep is a high performer.", "Zero tolerance for dishonesty. Small unaddressed integrity breaches inevitably grow into multi-lakh frauds.")
        ],
        "checklist": [
            "Financial delegation of authority matrix configured and locked in ERP.",
            "Mandatory 3-way matching operational for 100% of vendor payouts.",
            "Sensitive operational and procurement posts rotated periodically.",
            "Surprise unannounced inventory and cash audits conducted across all depots.",
            "Confidential whistleblower channel active with direct reporting to CEO office.",
            "Paint chemical formulation recipes encrypted and protected as proprietary trade secrets."
        ]
    },
    "peter-drucker-performance-mgmt-engine": {
        "title": "Peter Drucker Contribution & Strengths-Based Performance Engine for Swatch Paints",
        "legend": "Peter F. Drucker (Father of Modern Management & Author of 'The Effective Executive')",
        "description": "Peter Drucker Strengths-Based Staffing, Contribution Reviews, Feedback Analysis, and Managerial Development for Swatch Paints HR.",
        "dept": "06_hr_legal",
        "tag": "peter-drucker-hr",
        "purpose": """This skill equips the Swatch Paints Human Resources, Executive Coaching, and People Operations teams with Peter Drucker’s foundational disciplines of **Strengths-Based Management**, **Contribution Performance Reviews**, and **Systematic Feedback Analysis**.

Traditional corporate performance appraisals are a bureaucratic nightmare: once a year, managers fill out superficial 20-page forms scoring employees on generic personality traits ("initiative", "attitude", "punctuality") and obsessing over fixing minor personal weaknesses. This produces mediocrity: an employee who has no glaring faults, but also produces no outstanding achievements.

The engine's purpose is to:
- **Staff from Strength:** Place employees in roles where their proven strengths can produce extraordinary business results, while rendering their weaknesses irrelevant.
- Transform annual performance appraisals into quarterly **Drucker Contribution Dialogues**: focusing strictly on actual business contribution to enterprise growth and customer satisfaction.
- Institute Drucker's **Feedback Analysis**: requiring executives to write down their expected results before making major decisions and reviewing reality 9 months later to identify true competencies.
- Manage underperformance decisively: coaching or restructuring when an employee is miscast, rather than letting non-performance infect the team.""",
        "when_to_use": """- Conducting quarterly and annual performance reviews across sales, manufacturing, finance, and logistics.
- Deciding on promotions, leadership transfers, and structural organizational redesigns.
- An employee is struggling in their current role, and leadership must determine whether they are incompetent or simply miscast.
- Designing individual development plans (IDPs) for high-potential talent.
- Eliminating subjective, personality-based bias from employee evaluations.
- Coaching managers how to conduct intellectually honest performance feedback sessions.""",
        "frameworks": """### 6.1 Staffing from Strength
*"The effective executive makes strength productive. He knows that one cannot build on weakness. To achieve results, one must use all available strengths of associates, superiors, and oneself."*
- A great sales hunter might be disorganized at paperwork; do not fire him for messy paperwork—give him administrative support and let him hunt!
- A brilliant paint formulation chemist might be introverted and socially quiet; do not force him to give motivational speeches—let him invent breakthrough coatings!
- **Rule:** Never ask *"What can't this person do?"* Always ask: *"What can this person do exceptionally well, and have we provided the platform for them to do it?"*

### 6.2 The Drucker Contribution Audit
Every performance dialogue must center on 4 essential inquiries:
1. What was this person's agreed-upon contribution to the enterprise over the past 90 days?
2. What did they actually accomplish that moved the needle for our customers and balance sheet?
3. Where did their unique strengths produce outstanding performance?
4. What must they learn or change to make their strengths even more effective in the next 90 days?

### 6.3 Systematic Feedback Analysis
Drucker's personal method for career mastery:
- Whenever an executive takes an important decision (e.g., appointing a territory manager, launching a new paint line), write down the predicted outcome.
- 9 to 12 months later, compare actual results with expectations.
- This immediately reveals where your intuition is sharp and where your blind spots lie.""",
        "decision_algo": """### Step 1: Formulate the Annual Contribution Agreement
- Employee and Manager mutually agree on 3 major contribution targets aligned with corporate OKRs.
- Focus on outcomes that directly impact revenue, quality, or cost reduction.

### Step 2: Quarterly Contribution Dialogue Execution
- Ban numerical personality grading scales.
- Focus the review session on tangible achievements and strength multiplication.
- Identify and eliminate operational obstacles that prevented the employee from utilizing their strengths.

### Step 3: Managing the Underperformer
- IF an employee consistently fails to achieve agreed-upon outcomes:
  - Question 1: Is this person miscast? (Are we asking an analytical introvert to do cold retail sales?) If yes, reassign to a role matching their strengths.
  - Question 2: If the person has had two distinct role trials and lacks fundamental competence or integrity: Execute a swift, respectful, and legally compliant exit within 30 days.

### Step 4: Succession & High-Potential Development
- Identify the top 10% high-performers. Assign them high-leverage organizational challenges that stretch their strengths.""",
        "example1": """### Example 1: Rescuing a Failing Sales Rep by Realigning Strengths
**Situation:** A TSI in Kota had the lowest new dealer counter conversion rate in the company (15% of target). His ASM wanted to fire him for "poor communication and laziness."
**Drucker Strength Audit Applied:**
- HR reviewed his work: Found that while he was uncomfortable doing cold calls on skeptical new hardware dealers, his technical product knowledge and painter rapport were extraordinary. Contractors loved him because he spent hours showing them how to apply primer without brush marks.
- Transferred him from "Commercial Territory Hunter" to "Technical Application Specialist" for the Hadoti region.
- Result: Over the next 6 months, he conducted 48 on-site contractor workshops, generating massive secondary pull that helped the new commercial TSI open 28 new dealer counters. A near-firing turned into a high-impact success.""",
        "example2": """### Example 2: Implementing Executive Feedback Analysis in Production
**Situation:** The Technical Director frequently made gut-feel modifications to batch schedules, predicting they would "speed up plant throughput," but the plant frequently bottlenecked.
**Drucker Feedback Protocol Applied:**
- Mandated that every schedule change and formulation tweak be logged in an ERP decision journal with predicted outcomes (cycle time, yield, cost).
- Reviewed actual results 60 days later: Data proved that his scheduling changes were actually increasing kettle cleaning downtime by 22%.
- Humbled by objective data, the Director standardized batch sequencing around mathematical Takt time and Heijunka leveling, eliminating emotional tampering.""",
        "failures": [
            ("Obsessing Over Weaknesses", "Spending 80% of appraisal meetings lecturing an employee about their minor flaws.", "Build on strengths; manage weaknesses by pairing them with complementary teammates or tools."),
            ("Bureaucratic Tick-Box Appraisals", "Filling out HR compliance forms once a year and filing them away without real dialogue.", "Conduct quarterly, intellectually honest contribution dialogues focused on business impact."),
            ("Tolerating Chronic Incompetence", "Keeping a failing employee in a critical post for 2 years because 'he is a nice person.'", "Leaving an incompetent person in a job damages team morale and does a disservice to the employee."),
            ("Subjective Personality Bias", "Rating employees based on extroversion or flattery rather than verified results.", "Judge performance strictly on verified contribution to enterprise survival and growth.")
        ],
        "checklist": [
            "Job descriptions replaced with objective Contribution Agreements.",
            "Managers trained to identify and staff from employee strengths.",
            "Quarterly performance dialogues focused on business outcomes, not personality traits.",
            "Decisive action taken for miscast employees (reassignment or respectful exit within 30 days).",
            "Feedback Analysis implemented for executive-level strategic decisions.",
            "High-potential talent nurtured through stretch assignments and leadership coaching."
        ]
    },
    "tony-hsieh-culture-happiness-engine": {
        "title": "Tony Hsieh Delivering Happiness & Customer Delight Culture Engine for Swatch Paints",
        "legend": "Tony Hsieh (Legendary Founder & CEO of Zappos & Author of 'Delivering Happiness')",
        "description": "Tony Hsieh Culture-First Strategy, Extreme Dealer Delight, Core Values Integration, and Painter Recognition Engine for Swatch Paints HR.",
        "dept": "06_hr_legal",
        "tag": "tony-hsieh",
        "purpose": """This skill equips the Swatch Paints People Operations, Customer Experience, and Corporate Culture teams with Tony Hsieh’s legendary **Delivering Happiness** philosophy and culture-first business architecture.

In the Indian manufacturing and construction materials sector, corporate culture is almost universally regarded as a soft, trivial gimmick: companies operate on fear, treat factory workers as disposable commodities, view retail dealers with suspicion, and treat customer service as an annoying cost center to be minimized. Consequently, employees are disengaged, customer service is cold and robotic, and brand loyalty evaporates the moment a competitor offers a 1% price cut.

The engine's purpose is to:
- Institutionalize Tony Hsieh’s core revelation: **Corporate Culture and Brand are two sides of the same coin**. The brand is merely a lagging reflection of internal company culture.
- Transform Customer Service from a defensive cost center into an active **Engine of Customer Delight and Competitive Advantage**.
- Empower frontline customer service reps, sales officers, and delivery drivers with the autonomy to surprise and delight dealers and painters on the spot without bureaucratic approvals.
- Build an enterprise where employees, channel partners, and painter applicators feel genuine joy, dignity, and belonging.""",
        "when_to_use": """- Defining and embedding Swatch Paints' Ten Commanded Core Values into daily operations.
- Customer complaints, service tickets, or dealer delivery disputes are handled mechanically and coldly.
- Onboarding new employees and instilling a culture of radical customer empathy.
- Overcoming employee burnout, disengagement, and cynicism across branch depots and factory lines.
- Designing the emotional architecture of the Swatch Ustaad Painter Community and Dealer Partner Summits.
- Evaluating cultural fit during hiring and performance evaluations.""",
        "frameworks": """### 6.1 Culture Precedes Brand
Tony Hsieh proved that you cannot build a beloved customer brand with an unhappy, cynical workforce:
```
Happy, Empowered Employees ──> Extreme Customer Delight ──> Unbreakable Brand Loyalty ──> Sustainable Enterprise Profits
```
- If your customer service desk treats an upset paint dealer with bureaucratic coldness, a ₹10 Lakh advertising campaign is completely wasted.
- **The Core Rule:** Hire for cultural fit, train for culture, and fire for culture.

### 6.2 The WOW Philosophy in Indian Paint Trade
"WOW" is delivering something that is unexpectedly personal, warm, and generous:
- An authorized dealer’s child falls ill: Swatch doesn't just send paint; the ASM sends fresh fruits and a get-well note from the CEO.
- A master painter is working late at night under floodlights to finish a Diwali project: The local Swatch sales officer shows up with hot tea and samosas for the entire 8-man crew.
- These emotional touches cost almost nothing, but they build lifelong human bonds that no multi-national price cut can sever.

### 6.3 Frontline Empowerment (No Scripts, No Red Tape)
- Abolish robotic phone scripts for customer service agents.
- Empower every customer service officer and ASM with a discretionary **"Delight Budget" (up to ₹2,500 per incident)** to resolve customer issues or create a WOW moment instantly without seeking managerial permission.""",
        "decision_algo": """### Step 1: Embed Core Values in Daily Cadence
- Formulate Swatch Paints' 5 Non-Negotiable Cultural Values (e.g., Extreme Humility, Fanatical Customer Care, Radical Transparency, Joy in Work, Uncompromising Integrity).
- Begin every weekly operational review by recognizing an employee who embodied a core value.

### Step 2: The 30-Day Cultural Onboarding
- Regardless of role (Software Engineer, Finance Manager, or Sales Director), every new corporate hire must spend their first 7 days:
  - Working on the factory packing floor filling paint pails.
  - Answering incoming dealer calls at the customer care desk.
  - Accompanying a delivery driver to unload paint at retail shops.
- This grounds everyone in the real human heartbeat of the business.

### Step 3: Unleash the Delight Budget
- When a dealer receives a damaged bucket or an incorrect tinting color:
  - Customer care officer does NOT argue or demand 4 forms of proof.
  - Dispatch replacement paint immediately; authorize local refund up to the Delight Budget limit.

### Step 4: The Cultural Exit Gate
- At the end of a new hire's first 30 days, make them **The Zappos Offer**:
  - Offer them a clean bonus of ₹10,000 to quit immediately if they do not feel 100% passionate about Swatch's mission.
  - Those who stay are culturally committed for the long haul.""",
        "example1": """### Example 1: Creating a WOW Moment for a Stranded Bundi Painter
**Situation:** On the night before Diwali, a master painting contractor in Bundi ran short by 2 pails of Swatch Shine Interior White for a luxury home handover. The local hardware shop had closed for the holiday.
**Hsieh WOW Culture in Action:**
- The painter called the Swatch customer care line in desperation.
- The local TSI received the alert. Instead of saying *"Depot band ho gaya hai, Diwali ke baad aao"*, he unlocked the branch emergency sample locker, drove 18 km on his own motorcycle, and personally delivered the two pails to the job site at 10:30 PM.
- The homeowner and painter were overwhelmed with gratitude.
- The painter became a legendary advocate: over the next year, he specified Swatch exclusively across 14 large bungalow projects, generating ₹11+ Lakhs in sales.""",
        "example2": """### Example 2: Resolving a Dealer Dispute with Radical Generosity
**Situation:** A major dealer in Alwar claimed that 10 pails of exterior primer arrived with scratched labels, making them look unattractive for display. The logistics manager wanted to reject the claim because the paint inside was undamaged.
**Delivering Happiness Intervention:**
- Customer care overridden the logistics objection: Dispatched fresh, pristine pails immediately.
- Advised the dealer to keep the scratched pails at a 30% discount to sell to commercial contractors for job-site use.
- Sent the dealer a personalized gift basket acknowledging their partnership.
- Result: The dealer was astonished by the speed and grace of the resolution; doubled his monthly Swatch stocking order within 30 days.""",
        "failures": [
            ("Treating Culture as HR Fluff", "Printing core values on posters while managers mistreat workers and scream on calls.", "Culture is defined by executive behavior and operational policies, not wall posters."),
            ("Robotic Bureaucratic Service", "Customer care agents reading robotic scripts and refusing to solve problems without 3 signatures.", "Empower frontline employees with autonomy and a discretionary Delight Budget to solve issues instantly."),
            ("Tolerating Cultural Terrorists", "Keeping a high-billing sales manager who insults colleagues and treats subordinates like dirt.", "Fire cultural misfits regardless of their sales numbers; a toxic culture destroys enterprise value."),
            ("Disconnected Corporate Executives", "Head office executives who have never visited a dealer shop or spoken to a painter.", "Mandate annual frontline Gemba immersion for all white-collar corporate employees.")
        ],
        "checklist": [
            "Core values formally integrated into hiring, performance reviews, and daily meetings.",
            "30-day onboarding includes mandatory frontline factory and customer service immersion.",
            "Frontline employees empowered with discretionary Delight Budgets to resolve issues instantly.",
            "Customer service interactions evaluated on customer delight and warmth, not call duration.",
            "Dealer and painter WOW stories documented, celebrated, and shared enterprise-wide.",
            "Zero tolerance for toxic, abusive behavior regardless of commercial performance."
        ]
    }
}

def generate_mkt_hr_skill(name, data):
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
        f"*{data['legend']} — Operationalized for Swatch Paints Enterprise Culture & Market Architecture.*",
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
        "Before invoking this engine, collect the following real-time inputs from live human resources, marketing, and CRM systems. Zero static assumptions or hardcoded parameters are permitted.",
        "",
        "### 4.1 Talent, Brand & Customer Inputs",
        "",
        "| Input | Why It Matters | Live System Source |",
        "|---|---|---|",
        "| Candidate / Employee Profile | Evaluates demonstrated outcomes, competencies, and cultural fit | HRMS / Topgrading Dossier |",
        "| Audience Segment & Awareness Level | Identifies customer psychological state and messaging requirements | Marketing CRM / Ad Manager |",
        "| Partner / Contractor Satisfaction Data | Tracks Net Promoter Score, service complaints, and churn risk | SFA App / Customer Support Portal |",
        "| Marketing Campaign Performance Logs | Measures engagement velocity, lead quality, and customer acquisition cost | Live Digital Analytics Dashboard |",
        "",
        "### 4.2 Financial & Strategic Guardrails",
        "",
        "| Guardrail | Enforcement Rule | Authority |",
        "|---|---|---|",
        "| Zero Tolerance on Integrity Violations | Dishonesty, corruption, or kickbacks trigger immediate exit | Executive Board / Legal Dept |",
        "| Customer Delight Discretionary Limit | Frontline agents empowered up to pre-approved Delight Budget | People Operations Policy |",
        "| Brand Identity & Positioning Sanctity | No marketing collateral may deviate from approved category anchor | CEO Office / Marketing Director |",
        "",
        "---",
        "",
        "## 5. DIAGNOSTIC QUESTIONS",
        "",
        f"Apply these 10 diagnostic inquiries before taking marketing, talent, or cultural action under the {name} framework:",
        "",
        "1. What is the fundamental human, psychological, or brand bottleneck we are addressing?",
        "2. Does this action build long-term trust, dignity, and cultural strength for Swatch Paints?",
        "3. Are we communicating at the exact psychological Stage of Awareness of our target audience?",
        "4. Have we staffed from demonstrated strengths rather than attempting to fix minor human weaknesses?",
        "5. Are we measuring verifiable business outcomes and real human engagement rather than vanity metrics?",
        "6. Does our message or culture stand out with sharp, unmistakable distinctiveness against generic competitors?",
        "7. Have we verified all background facts, candidate track records, and operational realities at the Gemba?",
        "8. Are our leaders modeling the exact behaviors, work ethic, and values they expect from their teams?",
        "9. What is the worst-case cultural or brand failure mode, and what guardrails prevent it?",
        "10. Who has single-point accountability for execution, and how will success be measured?",
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
        "Every strategic brand blueprint, talent acquisition scorecard, or cultural directive must follow this standardized schema:",
        "",
        "```markdown",
        f"# Swatch Paints Executive Strategy Directive: {data['title']}",
        "",
        "### 1. Operational Scope & Objective",
        "- **Target Domain / Cohort:** [Territory / Department / Candidate / Customer Segment]",
        "- **Lead Executive:** [Designation & Name]",
        "- **Time Horizon:** [Launch Date – Target Milestone Date]",
        "- **Primary Quantified Objective:** [Single measurable statement of target outcome]",
        "",
        "### 2. Methodological & Strategic Intervention",
        "- **Core Diagnostic Findings:** [Psychological, cultural, or brand root causes]",
        "- **Actionable Protocol:** [Specific campaign, interview, or cultural initiative]",
        "- **Proof & Verification Mechanism:** [Tangible demonstrations / reference checks / metrics]",
        "",
        "### 3. Cultural, Legal & Brand Guardrails",
        "- **Brand Positioning / Cultural Alignment:** [Verification against enterprise standards]",
        "- **Budget & Discretionary Parameters:** [Approved expenditure ceiling from live ERP]",
        "- **Rollback / Disqualification Trigger:** [Specific event requiring immediate project halt]",
        "",
        "### 4. Governance & Cadence",
        "- **Review Cadence:** [Weekly sprint review / Monthly cultural council]",
        "- **Lead Metric Owner:** [Named HR Lead / Marketing Director]",
        "- **Final Sign-off:** [CEO Office / Ashutosh Sharma Sir]",
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
        "Watch for these recurring marketing, organizational, and cultural failure modes:",
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
        "Before finalizing or launching any initiative under this skill, verify:",
        ""
    ])
    for item in data['checklist']:
        sections.append(f"- [ ] {item}")
        
    sections.extend([
        "",
        "---",
        "",
        f"**CEO Directive:** At Swatch Paints, our brand reputation and organizational culture are our most valuable enterprise assets. We reject hollow corporate slogans, arrogant managerial titles, and impersonal customer service. Every leader, marketing executive, and human resources officer must live the disciplines of {data['legend']} daily, building an organization that commands the deep respect of our employees, our channel partners, and the communities we serve."
    ])
    return "\n".join(sections)

def main():
    for name, data in MKT_HR_SKILLS.items():
        content = generate_mkt_hr_skill(name, data)
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
        print(f"Generated {name:48s} | {lines:3d} lines | {size:5d} bytes")

if __name__ == "__main__":
    main()
