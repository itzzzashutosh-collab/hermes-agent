import os

WORKSPACE_DIR = r"d:\Sharma Industries Erp Software\hermes-agent"
HERMES_DIR = r"C:\Users\itzzz\AppData\Local\hermes"

VIS_SYS_SKILLS = {
    # === 07_VISION_GROWTH ===
    "andy-grove-high-output-leverage-engine": {
        "title": "Andy Grove 10x Managerial Leverage & Scale Operations Engine for Swatch Paints",
        "legend": "Andy Grove (Iconic CEO of Intel & Author of 'High Output Management')",
        "description": "Andy Grove Managerial Leverage, High-Output Activities, Time Allocation, and 10x Scale Engine for Swatch Paints Executive Leadership.",
        "dept": "07_vision_growth",
        "tag": "andy-grove-scale",
        "purpose": """This skill equips the Swatch Paints Executive Leadership, Founder's Office, and Strategy Directors with Andy Grove’s legendary framework of **Managerial Leverage** and **High-Output Scaling**.

As an enterprise grows from a regional paint manufacturer into a multi-territory powerhouse, the primary constraint to scaling is never capital or machinery; it is **Executive Managerial Leverage**. Executives get sucked into low-leverage, reactive firefighting: negotiating petty ₹500 freight disputes, arbitrating trivial employee arguments, and attending endless low-output meetings. Consequently, senior leadership has zero time for high-leverage strategic initiatives—such as automated ERP formulation locking, strategic raw material partnerships, or territory leadership coaching.

The engine's purpose is to:
- Maximize **Managerial Leverage (L)**: prioritizing activities where an executive’s 1 hour of input produces 100 hours of positive operational output across the enterprise.
- Eliminate **Negative Leverage**: removing micromanagement, ambiguous directives, and meddling that demoralize teams and stall decisions.
- Engineer **High-Output Meetings**: structured 1-on-1s, operational reviews, and mission-driven crisis taskforces.
- Maintain **Strategic Clarity**: ensuring that every managerial action accelerates Swatch Paints' journey toward market dominance in Western India.""",
        "when_to_use": """- Designing organizational structures and delegation frameworks for rapid multi-state expansion.
- Executive leadership feels overwhelmed by daily firefighting and lacks time for long-term strategy.
- Structuring the agenda and governance rhythm for Executive Board Reviews under Ashutosh Sharma Sir.
- Deciding whether a senior executive should intervene personally in an operational crisis or delegate it.
- Eliminating low-value corporate meetings and time-wasting administrative rituals.
- Evaluating managerial productivity and organizational leverage ratios.""",
        "frameworks": """### 6.1 The Managerial Output Equation
```
Manager's Total Output = (Output of Manager's Direct Unit) + (Output of Neighboring Units Influenced)
```
- A manager does not produce paint or write invoices directly; their output is measured strictly by the output of the organization they lead and influence.

### 6.2 The Three Types of High-Leverage Activities
1. **High Leverage via Many People:** An action that impacts the behavior of dozens of employees simultaneously.
   - Example: Designing the standardized 10-point Dealer Audit Checklist used by all 35 sales reps daily.
2. **High Leverage via Enduring Time:** An action that shapes organizational behavior over a long horizon.
   - Example: Negotiating a 12-month indexed supply contract for pure acrylic emulsion with BASF.
3. **High Leverage via Critical Knowledge:** A brief intervention based on specialized insight that prevents a catastrophic failure.
   - Example: The Technical Director spotting an improper thickener sequence on a 10,000-litre kettle run before batch dispersion begins.

### 6.3 Grove's Meeting Taxonomy
Grove proved that meetings are not an interruption of work; they are the medium through which managerial work occurs. However, they must be classified:
- **Process-Oriented Meetings:** Regular operational cadences (1-on-1s, Staff Meetings, Operational Reviews). Standardized, predictable agendas.
- **Mission-Oriented Meetings:** Ad-hoc emergency meetings called strictly to produce a specific decision (e.g., responding to a competitor's sudden price war). Must never exceed 45 minutes and must end with an actionable decision.""",
        "decision_algo": """### Step 1: Weekly Executive Time-Audit
- Dissect the executive's weekly calendar into:
  - Low-Leverage (<2x multiplier): Answering routine emails, sitting in passive briefings. (Target: Eliminate or delegate).
  - Medium-Leverage (5x multiplier): Standard operational reviews, customer visits.
  - High-Leverage (>10x multiplier): Training subordinates, strategic pricing, institutionalizing SOPs. (Target: >50% of time).

### Step 2: High-Leverage Training Mandate
- Grove’s Rule: **Training is the boss’s job, not HR’s job.**
- Every senior executive must personally conduct at least 2 hours of direct operational training per month for their frontline team. (12 hours of preparation improves the work of 20 people for an entire year = Massive Leverage).

### Step 3: Eliminating Negative Leverage
- Ban "meddling": If an executive delegates a task to an ASM, they must not secretly overturn the ASM's decision on the side, which destroys the subordinate's confidence and authority.

### Step 4: Mission-Oriented Meeting Discipline
- Any meeting with >6 attendees must have a written 1-page pre-read distributed 24 hours in advance. No slide-reading allowed.""",
        "example1": """### Example 1: Multiplying Sales Capacity via Grove Subordinate Training
**Situation:** The Commercial Sales Director spent 25 hours per week traveling across Rajasthan personally negotiating individual dealer stocking deals, leaving him exhausted with zero time for strategic distributor network expansion.
**High-Leverage Intervention Applied:**
- Pulled the Director out of individual deal-making.
- Dedicated those 25 hours over 2 weeks to codifying his personal deal-making scripts into a master 4-hour training module for all 18 ASMs and TSIs.
- Personally conducted 3 intensive simulation workshops coaching reps on dealer margin defense.
- **Outcome:** The 18 newly empowered reps closed 42 new dealer accounts in 30 days without requiring the Director’s presence. The Director’s 25 hours of training produced over 3,000 hours of competent field execution (120x Leverage).""",
        "example2": """### Example 2: Slashing 14 Hours of Negative-Leverage Executive Meetings
**Situation:** The weekly Monday executive review meeting lasted 4.5 hours with 12 managers present, devolving into shouting matches over weekly truck dispatches and missing paperwork.
**Grove Meeting Discipline Applied:**
- Cancelled the 4.5-hour verbal review.
- Replaced with a standardized digital dashboard: automated ERP summary distributed Monday at 07:30 AM.
- Re-architected into a 45-minute strict "Exception Review": Attendees discussed only red-flag deviations where cross-functional decisions were required.
- Liberated 48 management hours per week enterprise-wide, re-channeling senior bandwidth into factory productivity and customer acquisition.""",
        "failures": [
            ("The Doer-to-Manager Trap", "A promoted manager continuing to do the operational work themselves because 'it's faster than teaching someone else.'", "Your job is to multiply output through others; spend time teaching subordinates standard work."),
            ("Negative Leverage Micromanagement", "Overturning a subordinate's decisions in front of their team, destroying their authority.", "Delegate cleanly. Provide guidelines and let subordinates own the outcome."),
            ("Meeting Bloat", "Calling 10-person meetings without an agenda just to 'share updates.'", "Updates belong in automated dashboards. Meetings are strictly for decisions and alignment."),
            ("Abdication Instead of Delegation", "Dumping a critical task on an untrained employee and ignoring them until disaster strikes.", "Grove Rule: Delegation without monitoring is abdication. Establish structured review milestones.")
        ],
        "checklist": [
            "Executive time allocated primarily to high-leverage activities (>10x output multiplier).",
            "Senior leaders personally conduct frontline training programs monthly.",
            "Meetings categorized strictly into Process-Oriented vs. Mission-Oriented.",
            "Mission-oriented meetings capped at 45 minutes with clear pre-reads and actionable decisions.",
            "Negative managerial leverage (meddling, public reprimands) strictly prohibited.",
            "Delegation supported by structured monitoring milestones, not blind abdication."
        ]
    },
    "clayton-christensen-disruption-engine": {
        "title": "Clayton Christensen Disruptive Innovation & Jobs-to-be-Done Engine for Swatch Paints",
        "legend": "Clayton M. Christensen (Harvard Business School Professor & Author of 'The Innovator's Dilemma')",
        "description": "Clayton Christensen Low-End Disruption, New-Market Footholds, and Jobs-to-be-Done (JTBD) Theory for Swatch Paints Market Expansion.",
        "dept": "07_vision_growth",
        "tag": "clayton-christensen",
        "purpose": """This skill equips the Swatch Paints Strategy Office, R&D Lab, and Product Innovation teams with Clayton Christensen’s groundbreaking theories of **Disruptive Innovation** and **Jobs-to-be-Done (JTBD)**.

In the Indian coatings industry, incumbent multinational giants suffer from the classic **Innovator's Dilemma**: they are prisoner to their highest-margin, tier-1 urban luxury customers. They continually over-engineer their premium emulsions with complex, expensive features (e.g., Teflon coatings, Italian metallic sheen) that ordinary homeowners neither understand nor need, creating a massive vacuum at the bottom and middle of the market. Furthermore, they dismiss small regional players as "insignificant low-end pests."

The engine's purpose is to:
- Execute **Low-End Disruption**: capturing neglected tier-2/3/4 semi-urban and rural housing markets with simpler, reliable, high-coverage coatings that incumbent titans cannot profitably serve.
- Master the **Jobs-to-be-Done (JTBD)** of the painter and independent homebuilder (IHB): uncovering why they "hire" a paint (e.g., *"I don't hire paint for chemical gloss; I hire paint to hide uneven cement plaster in a single coat so I can finish the job in 1 day and get paid"*).
- Identify **Non-Consumption Footholds**: bringing professional decorative texture aesthetics (Swatch Rustic) to small-town homeowners who previously could only afford basic lime whitewash.
- Build an asymmetric business model where incumbents have zero financial incentive to fight back until it is too late.""",
        "when_to_use": """- Formulating long-term product roadmap and R&D formulation priorities.
- Entering rural, semi-urban, or tier-3 markets neglected by multinational paint corporations.
- High-end competitors launch aggressive loyalty schemes in tier-1 luxury segments.
- Conducting customer research to uncover the true underlying Job-to-be-Done of applicators and homeowners.
- Evaluating whether to launch a new product line or prune an existing over-engineered formulation.
- Defending Swatch against lower-tier unorganized commodity paint manufacturers.""",
        "frameworks": """### 6.1 The Mechanics of Low-End Disruption
```
PERFORMANCE
     ▲
     │                                     / Incumbent Trajectory (Overshooting Market)
     │                                    /
     │                 ┌─────────────────/────── High-End Customer Needs
     │                /                 /
     │               /                 /
     │              /  ┌──────────────/───────── Mainstream Customer Needs
     │             /  /              /
     │            /  /  ┌───────────/─────────── Low-End Customer Needs
     │           /  /  /           /
     │          /  /  /  ┌────────/───────────── Swatch Disruptive Foothold
     │         /  /  /  /
     └────────┴──┴──┴──┴─────────────────────────► TIME
```
- Incumbents continually overshoot customer needs, making products too complex and expensive.
- Disruptor enters at the bottom with a product that is "good enough", simpler, and more convenient.
- Disruptor marches upward as manufacturing quality improves, eventually displacing the incumbent.

### 6.2 The Jobs-to-be-Done (JTBD) Framework
Customers do not buy products; they "hire" them to make progress in specific circumstances:
- **Circumstance:** A master painter in Bundi painting a 2-room brick house on rough local plaster.
- **The Core Job:** Hide substrate roughness, dry quickly in extreme heat, and provide zero customer callbacks for efflorescence.
- If a ₹350/litre luxury paint requires 3 coats and complex wall putty preparation, it fails the job! A ₹160/litre high-build, high-opacity Swatch primer-emulsion hybrid that does the job in 1 coat is the disruptive winner.

### 6.3 Asymmetric Motivation
Choose battles where the competitor's rational response is to **flee upward rather than fight**:
- When Swatch dominates tier-3 exterior textures, Asian Paints' corporate management views the segment as "low-margin, messy, labor-intensive" and retreats to urban luxury interiors, ceding the territory to Swatch.""",
        "decision_algo": """### Step 1: Identify Overshot Customers
- Interview local hardware dealers: Which products do customers complain are "too complicated" or "too expensive for what they actually do"?
- Target the gap with a high-durability, simplified formulation.

### Step 2: Uncover the Non-Consumption Opportunity
- Look for people who are currently using non-paint alternatives (e.g., unbranded white cement, chuna, distemper).
- Formulate an entry-level texture/emulsion that converts them into branded coating consumers.

### Step 3: Architect the Asymmetric Business Model
- Build low-overhead regional manufacturing and lean direct-to-dealer logistics.
- Ensure Swatch can earn healthy 30%+ gross margins at price points where multinational giants would lose money.

### Step 4: Upward March Strategy
- Once the low-end foothold is secured, systematically improve formula aesthetics (e.g., adding luxury mineral metallics to Swatch Rustic) to capture mainstream customers.""",
        "example1": """### Example 1: Capturing the Tier-3 Plaster-Hiding Job in Hadoti
**Situation:** Multinational paint brands pushed super-smooth, thin-film luxury emulsions in rural Hadoti. Local painters hated them because rural brickwork plaster was uneven; thin paint highlighted every wall wave, leading to homeowner complaints.
**Christensen JTBD Solution:**
- Swatch R&D engineered a high-build, flexible textured exterior coating with micro-silica aggregates.
- It did the exact Job-to-be-Done: filled and hid plaster imperfections up to 3mm in a single trowel-and-roller pass, saving painters 40% in labor time.
- Painters enthusiastically adopted Swatch, rejecting the expensive multinational thin-film paints.
- Swatch captured 65% market share in the rural contractor segment in 12 months.""",
        "example2": """### Example 2: Converting Non-Consumers of Architectural Textures
**Situation:** Luxury Italian texture finishes cost ₹120 to ₹250 per square foot, making them accessible only to the ultra-wealthy in metro cities. Small-town villa builders in Bundi and Alwar used plain cement wash because textures were unaffordable.
**Disruptive Innovation Applied:**
- Swatch engineered **Swatch Rustic** using local mineral stone aggregates and high-durability acrylic binders, reducing application cost to under ₹35 per square foot.
- Brought architectural luxury texture to hundreds of middle-class homebuilders who were previously non-consumers.
- Multinational competitors ignored it as "niche rural texture"; Swatch turned it into a ₹multi-crore regional monopoly.""",
        "failures": [
            ("Head-On Incumbent Attack", "Launching an identical copy of Asian Paints Royale at the same price in urban luxury malls.", "Disruption requires an asymmetric entry point: target overshot customers or non-consumers first."),
            ("Feature Bloat Creep", "Adding 20 unnecessary chemical additives that inflate costs without solving the customer's core Job.", "Formulate strictly for the core Job-to-be-Done; keep formulations lean, robust, and cost-effective."),
            ("Ignoring the Upward March", "Staying trapped forever in low-margin commodity products without improving quality.", "Once the low-end beachhead is secured, use process improvements to march upward into higher-margin tiers."),
            ("Focusing on Demographics Instead of Jobs", "Segmenting customers by age/income rather than the job they are trying to get done.", "Cluster products around functional customer circumstances and jobs, not abstract demographic buckets.")
        ],
        "checklist": [
            "Customer Job-to-be-Done clearly identified through real-world contractor interviews.",
            "Overshot customer segments or non-consumption opportunities targeted.",
            "Asymmetric motivation verified: incumbents have no financial incentive to defend the entry niche.",
            "Formulation engineered for simplicity, workability, and cost advantage.",
            "Direct-to-dealer lean distribution enables profitability at disruptive price points.",
            "Strategic roadmap planned for the eventual upward march into mainstream segments."
        ]
    },
    "geoffrey-moore-chasm-scaling-engine": {
        "title": "Geoffrey Moore Crossing the Chasm & Beachhead Scaling Engine for Swatch Paints",
        "legend": "Geoffrey A. Moore (Silicon Valley Strategist & Author of 'Crossing the Chasm')",
        "description": "Geoffrey Moore Technology Adoption Life Cycle, Crossing the Chasm, Beachhead Strategy, and Whole Product Solution for Swatch Paints Innovation.",
        "dept": "07_vision_growth",
        "tag": "geoffrey-moore",
        "purpose": """This skill equips the Swatch Paints Strategy Office, Product Management, and Commercial Expansion teams with Geoffrey Moore’s iconic **Crossing the Chasm** methodology and **Beachhead Strategy**.

When launching innovative, differentiated coatings (such as **Swatch Rustic** architectural textures or thermal-reflective elastomeric roof shields), companies easily win over a few enthusiastic **Innovators & Early Adopters** (visionary architects and adventurous contractors). But then, sales suddenly stall, revenues plateau, and the product falls into the deadly **Chasm**. The conservative, pragmatic **Early Majority** (mainstream hardware dealers and cautious painters) refuses to buy because they demand proven track records, instant local tinting, standard application tools, and peer references.

The engine's purpose is to:
- Identify and navigate the **Chasm** between early visionary enthusiasts and the pragmatic mainstream paint trade.
- Execute the **Beachhead Strategy (D-Day Invasion Model)**: focusing 100% of enterprise resources to conquer one narrow, highly specific market niche before expanding.
- Build the **Whole Product Solution**: surrounding the core paint can with everything the pragmatic buyer needs (specialized application trowels, video training, certified applicator network, guaranteed tinting delivery).
- Position Swatch as the pragmatic, safe choice for conservative commercial contractors and dealers.""",
        "when_to_use": """- A newly launched innovative product line (e.g., Swatch Rustic) experiences early buzz followed by stagnant mainstream sales.
- Expanding into a competitive new geographic market dominated by entrenched traditional brands.
- Pragmatic hardware dealers resist stocking new formulations, saying: *"Pehle doosre dukaandaro ko bechne do, fir dekhenge."*
- Deciding how to allocate commercial marketing budgets between broad horizontal campaigns vs. narrow vertical beachheads.
- Transitioning product positioning from "visionary, artistic innovation" to "dependable, standard industry practice."
- Engineering the complete ecosystem of tools, training, and warranties around core paint products.""",
        "frameworks": """### 6.1 The Technology Adoption Life Cycle & The Chasm
```
[INNOVATORS] ──> [EARLY ADOPTERS] ──|| THE CHASM ||──> [EARLY MAJORITY] ──> [LATE MAJORITY] ──> [LAGGARDS]
```
- **Early Adopters:** Visionaries who want a revolutionary finish to stand out. They tolerate bugs, missing tools, and delivery delays.
- **The Chasm:** The vast difference in buying psychology between Visionaries and Pragmatists.
- **Early Majority (Pragmatists):** Conservative merchants and contractors. They want evolutionary improvements, low risk, and peer references. If Asian Paints doesn't make it, they are suspicious.
- **The Chasm Crossing Rule:** You cannot cross the chasm with a broad, scattered attack; you must spearhead a concentrated **Beachhead Attack**.

### 6.2 The D-Day Beachhead Strategy
Just as the Allied invasion of Europe focused all force on Normandy rather than attacking the entire coastline of France:
- Pick **ONE specific segment** in **ONE specific territory** with a compelling reason to buy (e.g., Heritage Boutique Resorts in Udaipur & Kumbhalgarh needing breathable stone texture).
- Dominate 80% of that beachhead completely.
- Use that beachhead as the secure launching pad to invade adjacent mainstream segments.

### 6.3 The Whole Product Model
Pragmatic buyers will not buy an incomplete product:
```
+-----------------------------------------------------------------+
|                    THE WHOLE PRODUCT MODEL                      |
|                                                                 |
|   [POTENTIAL PRODUCT]: Digital Warranty + Architect Referral    |
|   [AUGMENTED PRODUCT]: On-site Applicator Training + Mixer Tool |
|   [EXPECTED PRODUCT] : Consistent Tinting + Primers + Trowel    |
|   [CORE PRODUCT]     : 20L Bucket of Swatch Rustic Paint        |
+-----------------------------------------------------------------+
```
If any layer of the Whole Product is missing, the pragmatic buyer walks away.""",
        "decision_algo": """### Step 1: Target Market Segment Selection
- Score candidate beachhead segments against 4 criteria:
  1. Target customer has a compelling reason to buy (high pain).
  2. Whole product can be delivered within 90 days.
  3. No entrenched competitor dominates this exact niche.
  4. Winning this niche provides immediate word-of-mouth leverage into adjacent markets.

### Step 2: Assemble the Whole Product Solution
- Before pitching to mainstream dealers, ensure the Whole Product is complete:
  - Core: Swatch Rustic paint bucket.
  - Expected: Matched base primer + standardized stainless application trowels.
  - Augmented: Free 2-hour job-site training for painter crews.
  - Potential: Direct lead forwarding from the Swatch digital platform.

### Step 3: Crush the Beachhead
- Focus 100% of regional sales, marketing, and technical demonstrators on the chosen beachhead until 60%+ market share is achieved.
- Prohibit field reps from pursuing opportunistic, distracting side-deals in other non-core segments.

### Step 4: Invade the Mainstream Bowling Alley
- Use references from the conquered beachhead to roll into adjacent mainstream dealer counters.""",
        "example1": """### Example 1: Crossing the Chasm with Swatch Rustic in Udaipur
**Situation:** Swatch Rustic won early praise from 3 artistic interior designers in Jaipur, but mainstream paint hardware dealers across Rajasthan refused to stock it, calling it "a high-risk, slow-moving art product."
**Beachhead Strategy Applied:**
- Selected a razor-sharp Beachhead: **Luxury Boutique Heritage Resorts & Havelis in Udaipur**.
- Reason to buy: Moisture from lakes caused standard paints to peel within 12 months, ruining luxury room revenues.
- Built the Whole Product: Swatch provided the breathable texture, supplied specialized imported finishing trowels, and trained 3 dedicated local applicator crews.
- Conquered the niche: Swatch Rustic was used on 14 prominent lakeside properties.
- Converted Pragmatic Dealers: Swatch reps walked into top Udaipur hardware dealers with photographs and endorsements from Udaipur's most famous hoteliers: *"Pura resort Swatch se bana hai."*
- Dealers immediately agreed to stock Swatch Rustic as standard inventory; successfully crossed the chasm into mainstream retail.""",
        "example2": """### Example 2: Eliminating the Missing Tool Chasm Barrier
**Situation:** Sales of Swatch Exterior Texture stalled in Kota because painters complained: *"Texture toh badhiya hai, par local hardware shops pe textured design banane wala roller nahi milta."*
**Whole Product Intervention:**
- Recognized that the missing ₹350 pattern roller was preventing the sale of ₹20,000 paint orders.
- Sourced high-grade silicone pattern rollers directly from manufacturers.
- Packed 1 free roller inside every 4-bucket combo pack of Swatch Rustic.
- Friction disappeared instantly; contractor adoption surged by 180% within 45 days.""",
        "failures": [
            ("The Broad Scattered Launch", "Attempting to cross the chasm by advertising to everyone in Rajasthan simultaneously.", "Concentrate all force on a single, defensible beachhead niche until it is 100% conquered."),
            ("Selling an Incomplete Product", "Shipping paint buckets without the primers, tools, and training necessary to apply it successfully.", "Pragmatic buyers demand the Whole Product; assemble all complementary assets before launching."),
            ("Listening to Visionaries Instead of Pragmatists", "Adding complex artistic custom features requested by 1 visionary designer that mainstream dealers hate.", "Pragmatic buyers want standardization, reliability, and ease of use; standardize the product."),
            ("Abandoning the Beachhead Prematurely", "Winning 2 accounts in the beachhead and immediately jumping to a new market before securing dominance.", "Hold the beachhead until you achieve dominant word-of-mouth referencability.")
        ],
        "checklist": [
            "Pragmatic mainstream buyers differentiated from early visionary adopters.",
            "Single target Beachhead niche selected with a compelling reason to buy.",
            "Whole Product Solution (primers, trowels, training, warranty) fully assembled.",
            "Field sales resources concentrated 100% on beachhead conquest.",
            "Dominant market share (>50%) achieved in beachhead before geographic expansion.",
            "Verified peer case studies and contractor references leveraged to cross into mainstream dealers."
        ]
    },
    "jeff-bezos-day1-long-term-engine": {
        "title": "Jeff Bezos Day 1 Vitality & Customer Obsession Engine for Swatch Paints",
        "legend": "Jeff Bezos (Founder of Amazon & Author of 'Invent & Wander')",
        "description": "Jeff Bezos Day 1 Culture, Fanatical Customer Obsession, High-Velocity Decision Making (Type 1 vs Type 2), and Working Backwards for Swatch Paints.",
        "dept": "07_vision_growth",
        "tag": "jeff-bezos",
        "purpose": """This skill equips the Swatch Paints Executive Leadership, Product Development, and Operational Strategy teams with Jeff Bezos’s foundational **Day 1 Philosophy**, **Customer Obsession**, and **High-Velocity Decision Making**.

As manufacturing enterprises scale, they inevitably slide into **Day 2 Stasis**: bureaucracy thickens, decision-making slows to a crawl, internal processes replace real customer outcomes, and the company becomes internally focused and complacent. In Day 2 companies, meetings are held to schedule other meetings, customer complaints are treated as annoying paperwork, and bold initiatives are smothered by risk-averse committees. Day 2 is stasis, followed by irrelevance, followed by agonizing decline and death.

The engine's purpose is to:
- Preserve **Day 1 Vitality**: maintaining the hunger, nimbleness, customer obsession, and speed of a startup regardless of how large Swatch Paints grows.
- Enforce **Customer Obsession over Competitor Obsession**: starting every new product, service, or policy by **Working Backwards** from the real pain of the painter and dealer, rather than copying rival paint companies.
- Drive **High-Velocity Decision Making**: categorizing decisions into **Type 1 (Irreversible Doors)** vs. **Type 2 (Two-Way Reversible Doors)**, making Type 2 decisions with 70% information at lightning speed.
- Resist **Proxies**: refusing to let process, survey scores, or administrative metrics substitute for true customer reality.""",
        "when_to_use": """- Long-term strategic planning, annual shareholder vision memos, and organizational redesign.
- Executive decision-making is slowing down due to excessive analysis paralysis or committee reviews.
- Designing new customer-facing products or services: applying the "Working Backwards (PR/FAQ)" methodology.
- Customer complaints or negative dealer feedback are being dismissed by internal departments as "isolated exceptions."
- Battling complacency, bureaucratic arrogance, or internal empire-building as company headcount scales.
- Evaluating whether to approve bold, experimental business initiatives under Ashutosh Sharma Sir’s directive.""",
        "frameworks": """### 6.1 The Day 1 vs. Day 2 Doctrine
- **Day 1:** Customer obsession, eagerness to experiment, rapid decision-making, direct engagement with reality, and relentless innovation.
- **Day 2:** Process-obsession, risk aversion, slow decision-making, relying on proxies, and resting on past laurels.
- **CEO Mandate:** Swatch Paints must *always* remain a Day 1 company.

### 6.2 Customer Obsession vs. Competitor Obsession
Many paint companies are competitor-obsessed: they wait to see what Asian Paints or Berger launches, and then copy it with a 5% discount.
- **Customer Obsession:** Listen deeply to what the master painter and retail dealer struggle with daily, and invent solutions on their behalf before they even know how to ask.
- Competitors will copy what you did yesterday; customer obsession ensures you are inventing what they will need tomorrow.

### 6.3 Type 1 vs. Type 2 Decisions
Bezos demonstrated that decision slowness occurs when companies treat all decisions as irreversible:
- **Type 1 Decisions (One-Way Doors):** Irreversible, high-stakes decisions with massive enterprise consequences (e.g., buying a ₹15 Crore industrial manufacturing plot, fundamentally altering corporate legal structure).
  - *Process:* Deliberate slowly, consult experts, analyze exhaustively.
- **Type 2 Decisions (Two-Way Doors):** Reversible decisions that can be undone if proven wrong (e.g., testing a new dealer display stand, trialing a 10% painter referral bonus in Bundi, changing packing carton design).
  - *Process:* Make them rapidly with small teams with ~70% of desired information. If wrong, walk back through the door!
- **Pathology to Eliminate:** Treating Type 2 decisions like Type 1 decisions, subjecting minor initiatives to 4 layers of managerial sign-offs.

### 6.4 The Working Backwards PR/FAQ
Before writing a single line of chemical formulation or building a single display unit:
- The project lead must draft a 1-page **Internal Press Release (PR)** announcing the finished product from the customer's perspective.
- Accompanied by a **Frequently Asked Questions (FAQ)** document detailing exact costs, trade margins, and technical parameters.
- If the PR is not stunningly compelling to the customer, the project is abandoned immediately.""",
        "decision_algo": """### Step 1: Decision Classification Gate
- Whenever an operational proposal is presented to leadership:
  - Ask: Is this a Type 1 or Type 2 decision?
  - IF Type 2: Delegate immediately to the frontline owner. Empower them to execute within 48 hours without executive committee approval.

### Step 2: Working Backwards Audit
- Reject PowerPoint presentations for new product concepts.
- Mandate a 2-page written PR/FAQ:
  - What is the customer's problem?
  - How does this product solve it simply and brilliantly?
  - What will the painter or dealer say on launch day?

### Step 3: Resist Proxies (Direct Gemba Reality)
- If an internal report says: "Depot order fulfillment is 98%", but a dealer calls Ashutosh Sir saying his tinting order was 3 days late:
  - Trust the customer, investigate the proxy! Averages hide operational reality.

### Step 4: Disagree and Commit
- Leaders must vigorously debate with intellectual honesty during decision formulation.
- Once a decision is finalized, everyone must 100% **Disagree and Commit**—backing execution with complete energy and zero sabotage.""",
        "example1": """### Example 1: Slashing Decision Latency on Dealer Display Stands
**Situation:** The marketing team wanted to pilot a new rotating wire display stand for 1-litre Swatch Shine cans in 20 Kota shops. The proposal was stuck for 7 weeks waiting for approvals from Sales, Finance, Legal, and Depot Logistics.
**Type 2 Decision Protocol Applied:**
- The CEO identified this as a classic **Type 2 Reversible Decision**: Total risk was ₹35,000; if it failed, the stands could be repurposed or scrapped.
- Dissolved the approval committee. Empowered the junior marketing associate to order the 20 stands immediately on his own authority.
- Stands were deployed in 5 days; generated a 42% lift in retail walk-in sales; rolled out across all 150 authorized dealers in 30 days.""",
        "example2": """### Example 2: Working Backwards to Create the 24-Hour Tinting Delivery Guarantee
**Situation:** Management wanted to increase market share in Jaipur. Traditional executives proposed a ₹5 Lakh billboard campaign.
**Customer-Obsessed Working Backwards PR/FAQ Applied:**
- Team wrote a mock Press Release from the perspective of an independent Jaipur painting contractor: *"Never lose a job-site day again: Swatch Paints guarantees custom-tinted architectural paint delivered to your dealer within 24 hours, or the freight is free."*
- Working backwards from this customer promise, the supply chain was re-engineered: installed high-speed automated tinting dispensers at the Jaipur depot and partnered with local two-wheeler express couriers for micro-deliveries.
- The service became a massive competitive differentiator, winning over 60 premier contractors without spending a rupee on billboards.""",
        "failures": [
            ("Sliding into Day 2 Complacency", "Resting on past successes and allowing bureaucracy to choke speed and innovation.", "Fight Day 2 relentlessly: maintain customer obsession, lean operational structures, and startup agility."),
            ("Treating Type 2 Decisions as Type 1", "Requiring 4 executive signatures to approve a ₹5,000 dealer marketing banner.", "Push decision-making authority down to frontline operators; encourage fast, reversible experiments."),
            ("Competitor Obsession Paranoia", "Spending all day analyzing Asian Paints' moves instead of inventing for your customers.", "Focus 90% of strategic energy on customer needs, painter friction, and dealer profitability."),
            ("Process as a Proxy for Truth", "Believing an Excel spreadsheet metric while real dealers are unhappy.", "Stay connected to the ground truth: visit shops, talk to painters, and inspect customer complaints personally.")
        ],
        "checklist": [
            "Day 1 culture of hunger, speed, and continuous experimentation active enterprise-wide.",
            "Decisions categorized into Type 1 (Irreversible) vs Type 2 (Reversible) at meeting start.",
            "Type 2 decisions executed with ~70% information within 48 hours.",
            "New product and service initiatives planned using the Working Backwards PR/FAQ method.",
            "Customer obsession prioritized over competitor obsession in all strategic allocations.",
            "Disagree and Commit principle practiced: full cross-functional alignment once decisions are made."
        ]
    },
    "michael-porter-competitive-strategy-engine": {
        "title": "Michael Porter Five Forces, Cost Leadership & Differentiation Engine for Swatch Paints",
        "legend": "Michael E. Porter (Harvard Business School Professor & Father of Modern Strategic Management)",
        "description": "Michael Porter Five Forces Industry Analysis, Generic Competitive Strategies, Value Chain Optimization, and Strategic Positioning for Swatch Paints.",
        "dept": "07_vision_growth",
        "tag": "michael-porter",
        "purpose": """This skill equips the Swatch Paints Board of Directors, Executive Leadership, and Strategy Office with Michael Porter’s timeless **Five Competitive Forces**, **Generic Competitive Strategies**, and **Value Chain Architecture**.

In business, companies frequently confuse "operational effectiveness" (doing the same things slightly better than rivals) with **Strategy** (doing things *differently* to deliver a unique mix of value). In the Indian paint sector, regional manufacturers fall into the fatal **"Stuck-in-the-Middle" Trap**: they have neither the scale to beat Asian Paints on low-cost mass commodity distribution, nor the clear differentiation to command luxury price premiums. They compete in a destructive operational race to the bottom, bleeding margins and ending in bankruptcy.

The engine's purpose is to:
- Conduct rigorous **Five Forces Industry Structure Audits**: analyzing Supplier Power (chemical cartels), Buyer Power (consolidated dealer associations), Threat of New Entrants, Threat of Substitutes, and Competitive Rivalry.
- Enforce strict adherence to a **Generic Strategy**: Pursuing **Focused Differentiation** (owning premium weather-proof architectural textures and high-coverage emulsions in targeted tier-2/3 growth corridors) rather than getting stuck in the middle.
- Deconstruct and optimize the **Value Chain**: aligning Inbound Logistics, Operations, Outbound Logistics, Marketing, and Service into an interdependent system of reinforcing activities that rivals cannot copy.
- Build a sustainable, defensible competitive advantage that preserves above-average Returns on Invested Capital (ROIC).""",
        "when_to_use": """- Formulating the 3-to-5 year strategic master plan for Swatch Paints and Sharma Industries.
- Industry-wide structural shocks occur: raw material price spikes, new multi-billion dollar conglomerate entrants (e.g., Grasim/Birla Opus), or dealer margin disputes.
- A product category is suffering from margin erosion due to intense competitive rivalry.
- Evaluating vertical integration: deciding whether to manufacture internal resin binders or continue third-party procurement.
- Analyzing territory expansion: determining whether to enter a new state or deepen existing competitive positions.
- Auditing the company's Value Chain to uncover sources of sustainable cost advantage or premium differentiation.""",
        "frameworks": """### 6.1 The Five Competitive Forces of the Indian Paint Industry
```
                      [THREAT OF NEW ENTRANTS]
                      (High: Conglomerates entering)
                                │
                                ▼
[SUPPLIER POWER]     ──► [COMPETITIVE RIVALRY] ◄── [BUYER POWER]
(High: Crude oil, TiO2)  (Intense: Ad wars, rebates) (High: Powerful dealers)
                                ▲
                                │
                      [THREAT OF SUBSTITUTES]
                      (Moderate: Wallpaper, tiles, bare concrete)
```
- Sustainable profitability is determined by industry structure, not whether the product is high-tech or low-tech.

### 6.2 Porter's Generic Strategies & The "Stuck in the Middle" Trap
```
                     STRATEGIC ADVANTAGE
               Low Cost Position      Uniqueness Perceived
             +----------------------+----------------------+
Broad Target | 1. COST LEADERSHIP   | 2. DIFFERENTIATION   |
             +----------------------+----------------------+
Narrow Focus | 3A. COST FOCUS       | 3B. DIFFERENTIATION  |
             |                      |     FOCUS (SWATCH)   |
             +----------------------+----------------------+
```
- **The Stuck-in-the-Middle Trap:** Trying to be all things to all people. You are too small to be the low-cost producer, and too generic to charge a premium.
- **Swatch Paints' Winning Position: 3B. Differentiation Focus.** Focused on high-durability architectural mineral textures (Swatch Rustic) and high-coverage weather-proof emulsions for regional homeowners and contractors in harsh climate zones.

### 6.3 Strategic Fit & Activity Systems
Competitive advantage is not based on a single magic formula; it stems from a **System of Interlocking Activities** that fit together:
- Proximity of Rajasthan manufacturing plant + Formulations engineered specifically for high-calcium, salty plaster + Dedicated master painter application training + Fast 24-hour depot replenishment.
- A competitor can easily copy one element (e.g., lower price), but they cannot copy the entire interdependent activity system without disrupting their own business model.""",
        "decision_algo": """### Step 1: Industry Structure Analysis
- Continuously monitor shifts in the Five Forces:
  - Is supplier power rising due to global TiO2 shortages? (Action: Qualify alternate extender chemistries).
  - Is buyer power rising due to dealer consolidation? (Action: Strengthen direct painter loyalty pull).

### Step 2: Test Against the "Stuck-in-the-Middle" Filter
- Whenever a new product or marketing scheme is proposed, ask:
  - Does this reinforce our Focused Differentiation, or does it drag us into a generic commodity war?
  - IF it is a generic me-too product with no clear differentiation: REJECT immediately.

### Step 3: Value Chain Strategic Fit Audit
- Map all 9 value chain activities (Inbound, Operations, Outbound, Marketing, Service, Infrastructure, HR, Technology, Procurement).
- Ensure that every activity reinforces the brand's core differentiation (Reliability, Climate Durability, Painter Empowerment).

### Step 4: Competitor Response Modeling
- Predict rival counter-moves before launching major initiatives.
- Structure moves where rivals' corporate overheads prevent them from matching you profitably.""",
        "example1": """### Example 1: Escaping the 'Stuck in the Middle' Trap in Exterior Paints
**Situation:** Swatch was producing a generic exterior acrylic emulsion that competed head-to-head with Asian Paints Apex and Berger WeatherCoat. Swatch’s gross margin was compressed to 14% as sales reps offered discount after discount to win dealer orders.
**Porter Strategic Repositioning Applied:**
- Recognized that Swatch was dangerously "stuck in the middle."
- Shifted strategy to **Differentiation Focus**: Discontinued the generic me-too acrylic; reformulated the product into an advanced **Silicone-Enhanced Mineral Elastomeric Shield** specifically engineered for Rajasthan’s extreme 48°C heat and plaster efflorescence.
- Repositioned from commodity paint to specialized climate shield; raised price by 12%.
- Sales volume grew by 34% while gross margin surged from 14% to 32% because the product delivered unique, unmatched value for regional conditions.""",
        "example2": """### Example 2: Outmaneuvering a Multi-Billion Dollar Conglomerate Entrant
**Situation:** A massive national industrial conglomerate entered the paint market, spending ₹500 Crores on television advertising and offering dealers 120-day credit terms to buy shelf space.
**Porter Five Forces Defense Applied:**
- Swatch did not attempt to match the conglomerate's unsustainable credit terms or ad spend (which would have bankrupted the company).
- *Value Chain Moat Defense:* Swatch leveraged its intimate regional proximity.
  - Held painter meets at dealer shops every Thursday.
  - Provided direct factory chemist visits to resolve job-site technical questions within 4 hours.
  - Kept dealer working capital turning fast (8 turns/year) with same-day depot dispatches.
- When the conglomerate’s paint suffered application blistering due to lack of local technical support, dealers returned the conglomerate's stock and recommitted to Swatch as their trusted local partner.""",
        "failures": [
            ("The Stuck-in-the-Middle Suicide", "Attempting to compete with multinational giants on broad advertising and scale without differentiation.", "Choose and maintain a focused generic strategy: deliver distinct, specialized value to targeted customer segments."),
            ("Confusing Operational Effectiveness with Strategy", "Believing that installing a faster packaging line constitutes a competitive strategy.", "Operational effectiveness is necessary but insufficient; strategy requires doing different things or doing things differently."),
            ("Copying Competitor Moves Blindly", "Launching a loyalty scheme simply because a competitor launched one, eroding industry profitability.", "Compete to be unique, not to be the same. Design moves that reinforce your own activity system."),
            ("Ignoring Buyer and Supplier Power", "Allowing a few giant dealers to dictate commercial terms while relying on a single chemical supplier.", "Diversify supplier networks and build direct pull with master painters to balance channel power.")
        ],
        "checklist": [
            "Five Competitive Forces analyzed quarterly for structural threats and opportunities.",
            "Generic strategy maintained strictly as Focused Differentiation; zero stuck-in-the-middle drift.",
            "Value chain activities aligned into an interdependent, self-reinforcing operational system.",
            "Formulations and services tailored specifically to unique regional market requirements.",
            "Pricing reflects premium differentiated customer value rather than cost-plus discounting.",
            "Long-term Return on Invested Capital (ROIC) defended against competitive rivalry."
        ]
    },

    # === 08_SYSTEMS_SOPS ===
    "andy-grove-execution-discipline-engine": {
        "title": "Andy Grove Breakfast Factory & Operational Discipline Engine for Swatch Paints",
        "legend": "Andy Grove (Master Operational Engineer & Author of 'High Output Management')",
        "description": "Andy Grove Operational Indicators, Breakfast Factory Production Model, Limiting Steps, and Execution Discipline for Swatch Paints Systems.",
        "dept": "08_systems_sops",
        "tag": "andy-grove-systems",
        "purpose": """This skill equips the Swatch Paints Systems, Process Engineering, Operational Control, and Administrative teams with Andy Grove’s legendary **Breakfast Factory Model**, **Operational Indicators**, and **Execution Discipline**.

In growing enterprises, management systems frequently degrade into chaotic, subjective verbal debates: when a shipment is delayed or a batch fails, departments blame each other, meetings are held to argue about opinions, and executives lack objective, leading indicators to steer operations. Managers behave like amateur cooks trying to serve toast, coffee, and eggs simultaneously—serving cold toast and burnt eggs because they don't understand the **Limiting Step** of the process.

The engine's purpose is to:
- Model every departmental workflow (manufacturing, order-to-cash, tinting dispatch, customer complaint resolution) as an engineered **Production Line**.
- Identify and manage the **Limiting Step**: scheduling all dependent operational activities backward from the most time-consuming or rigid operational constraint.
- Build a cockpit of **Operational Leading Indicators** that detect system drift and bottlenecks before they impact the dealer or painter.
- Enforce uncompromising **Execution Discipline**: transforming standard operating procedures (SOPs) from dusty binder decorations into living, non-negotiable operational habits.""",
        "when_to_use": """- Designing or redesigning Standard Operating Procedures (SOPs) for plant operations, depots, and administrative offices.
- A critical business process (e.g., Dealer Onboarding, Batch Quality Release, Order Dispatch) suffers from unpredictable lead times.
- Establishing executive dashboards and real-time operational indicators in the ERP.
- Eliminating cross-departmental friction between Sales, Dispatch, and Finance.
- Diagnosing why customer service tickets or product complaint resolutions take days instead of hours.
- Auditing operational compliance and process discipline across branch locations.""",
        "frameworks": """### 6.1 Grove's Breakfast Factory Operational Model
Grove famously modeled all business operations on the challenge of serving a 3-minute soft-boiled egg, buttered toast, and hot coffee simultaneously:
```
TIME REQUIRED:
Coffee: 15 seconds to pour
Toast : 2 minutes in toaster
Egg   : 3 minutes boiling in water
```
- **The Limiting Step:** Boiling the egg (3 minutes). 
- If you start pouring coffee or toasting bread first, the breakfast fails. **Everything must be scheduled backward from the limiting step.**
- In paint dispatch: The limiting step is the spectrophotometer color match and lab viscosity release (takes 45 minutes). The packaging, invoice printing, and truck docking must be synchronized backward from the lab test!

### 6.2 The Five Essential Operational Indicators
Grove proved that every operation requires 5 distinct leading indicators to maintain control:
1. **Sales / Intake Forecast:** What customer demand is coming tomorrow?
2. **Raw Material / WIP Inventory:** Are buffers sufficient to sustain production without stockouts?
3. **Equipment / Process Condition:** Are dispersers, sand mills, and filling nozzles calibrated and running?
4. **Labor & Manpower Availability:** Are operators and chemists present on shift?
5. **Quality Metric (The Paired Indicator):** Measuring speed *paired* with defect rates to prevent reckless corner-cutting.

### 6.3 The Paired Indicator Rule
Never measure a process with a single metric. Always pair it with an opposing quality check:
- *Single Metric:* "Pack 1,000 buckets per shift." (Result: Operators rush, spill paint, and seal lids improperly).
- *Paired Metric:* "Pack 1,000 buckets per shift **WITH <0.1% fill weight variance and zero leaking lids**."
- Speed paired with Quality creates sustainable execution discipline.""",
        "decision_algo": """### Step 1: Process Mapping & Limiting Step Identification
- Break the workflow into discrete physical and administrative operations.
- Identify the Limiting Step (the longest, most rigid operation).
- Schedule all upstream and downstream tasks backward from this milestone.

### Step 2: Establish the Daily 5-Indicator Cockpit
- Build a 1-page visual dashboard for each department head:
  - Demand intake, WIP level, equipment uptime, shift attendance, and paired quality metric.
- Review at the 08:30 AM daily operational huddle.

### Step 3: Implement Automated Quality Windows (Inspection Gates)
- Establish gate checks at the lowest-value stage of production:
  - Test pigment dispersion fineness in the slurry *before* adding expensive acrylic resins.
  - Catching an error in the grind phase costs ₹200; catching it in the finished pail costs ₹15,000!

### Step 4: SOP Standardization & Audit Discipline
- Display photo-based SOPs directly at the workstation.
- Conduct weekly random audits: An SOP that is not audited daily is merely a recommendation.""",
        "example1": """### Example 1: Streamlining the Depot Order-to-Dispatch Process
**Situation:** Retail paint orders at the Jaipur depot took an unpredictable 6 to 28 hours to dispatch. Dealers constantly called screaming that painters were waiting at their shops.
**Grove Breakfast Factory Model Applied:**
- Mapped the process: Order Entry (15 mins), Credit Approval (takes 4 hours due to waiting for finance manager), Picking (30 mins), Invoicing (15 mins), Truck Loading (30 mins).
- The Limiting Step was **Credit Approval**.
- *Systemic Fix:* Re-engineered credit approval: ERP auto-approves orders within dealer credit limit instantly (10 seconds); only credit exceptions require manual review.
- Synchronized warehouse picking so that picking slips print at the loading dock the moment the truck arrives.
- Order-to-dispatch time collapsed from an average of 14 hours to a predictable 90 minutes; on-time dispatch rate reached 99.4%.""",
        "example2": """### Example 2: Paired Indicators End Yield Fraud in Canning Line
**Situation:** The packaging line supervisor was rewarded purely on "Buckets Packed per Shift." To hit his volume quota, he bypassed weight checks, allowing the automated line to overfill pails by 400g to prevent line stops.
**Grove Paired Indicator Implemented:**
- Paired the volume metric with a material yield variance metric: *Target is 1,200 pails per shift WITH gross weight variance within ±50 grams.*
- If weight variance exceeded tolerance, the volume bonus was nullified.
- Result: Shift volume remained high, while raw material giveaway was eliminated, saving ₹5.8 Lakhs in monthly yield loss.""",
        "failures": [
            ("Managing Without Leading Indicators", "Looking only at end-of-month financial reports when it's too late to fix operational failures.", "Establish daily operational indicators that detect process drift in real time."),
            ("Single Metric Gaming", "Measuring reps purely on volume, leading them to dump inventory and create bad debt.", "Always pair volume metrics with quality and financial health checks (Paired Indicators)."),
            ("Ignoring the Limiting Step", "Speeding up fast operations while the bottleneck operation remains choked, increasing WIP.", "Identify the limiting step; focus all engineering and scheduling resources on optimizing it."),
            ("Inspect at the End Mentality", "Inspecting paint only after it has been canned, labeled, and palletized.", "Inspect raw materials and intermediate slurries at the lowest-value stage to minimize rework costs.")
        ],
        "checklist": [
            "Every departmental workflow modeled as an engineered production line.",
            "The Limiting Step identified and used to schedule all dependent operations backward.",
            "Daily operational dashboard displays all 5 essential indicators.",
            "All speed/volume metrics paired with an opposing quality/variance metric.",
            "In-process inspection gates established at the lowest-value stage of manufacturing.",
            "Standard Operating Procedures (SOPs) audited weekly for strict operational compliance."
        ]
    },
    "masaaki-imai-gemba-sop-engine": {
        "title": "Masaaki Imai Gemba SOP Architecture & Visual Management Engine for Swatch Paints",
        "legend": "Masaaki Imai (Father of Continuous Improvement & Author of 'Gemba Kaizen')",
        "description": "Masaaki Imai Gemba-Built Standard Operating Procedures (SOPs), Visual Workplace Standards, Poka-Yoke, and Continuous Standardization for Swatch Paints.",
        "dept": "08_systems_sops",
        "tag": "masaaki-imai-sop",
        "purpose": """This skill equips the Swatch Paints Systems, Quality Assurance, and Operations teams with Masaaki Imai’s **Gemba SOP Architecture**, **Visual Management**, and **Continuous Standardization**.

In traditional corporate environments, Standard Operating Procedures (SOPs) are written by theoretical desk-bound engineers or external consultants who have never run a sand mill or loaded a paint delivery truck. These SOPs end up as 50-page text-heavy binders locked in administrative cupboards. On the actual factory floor (the Gemba), operators ignore the binders and work according to their own personal habits, leading to wild quality variations between shift changes, frequent safety accidents, and zero repeatability.

The engine's purpose is to:
- Build **Gemba-Born SOPs**: written, tested, and illustrated directly at the machine face with the full participation of frontline operators.
- Implement **Visual Management & 5S Standardization**: ensuring that anyone—even a temporary worker or visitor—can spot an operational abnormality within 5 seconds.
- Institute **Visual Mistake-Proofing (Poka-Yoke)** across formulation dispensing, tinting machine calibration, and packaging lines.
- Transform standards into **Living Foundations for Kaizen**: recognizing that without a standardized baseline, continuous improvement is impossible.""",
        "when_to_use": """- High variance in product quality or cycle times between Day Shift and Night Shift.
- Recurring workplace safety hazards, chemical spills, or operator handling injuries.
- Onboarding new operators, chemists, or depot workers; needing rapid, error-free training.
- Documenting critical technical processes (e.g., dispersion grind testing, tinting machine calibration, biocide addition).
- Implementing visual management across factory decks, raw material godowns, and finished goods docks.
- Preparing the enterprise for ISO 9001 / 14001 / 45001 international quality and safety certifications.""",
        "frameworks": """### 6.1 The Gemba Law of Standardization
*"There can be no improvement where there is no standard. If you have no standard, how do you know if you are improving or deteriorating?"*
- A standard is not a rigid ceiling; it is the **current best known way to do a job**.
- The moment an operator finds a safer, faster, higher-quality method through Kaizen, the standard is updated!

### 6.2 The Three Criteria of a World-Class Gemba SOP
1. **Visual over Text:** 80% photos, schematics, and color codes; 20% concise text. (Readable in 30 seconds at eye level).
2. **Frontline Ownership:** Drafted by the operator who actually performs the work, validated by the engineer.
3. **Direct Abnormality Detection:** The SOP must explicitly show: *"What does GOOD look like? What does BAD look like?"* with side-by-side color photographs.

### 6.3 Visual Workplace (Visual Management)
A visual workplace is self-ordering, self-explaining, self-regulating, and self-improving:
- **Shadow Boards:** Outlines of tools painted on walls; if an adjustable wrench is missing, the empty red silhouette alerts the supervisor instantly.
- **Pipeline Color Codes:** Water (Blue), Solvent (Red), Emulsion (Yellow), Compressed Air (Green) with directional flow arrows.
- **Min/Max Sight Gauges:** Visual red/green level stickers on tank level indicators; zero need to read complex manuals.""",
        "decision_algo": """### Step 1: Go to the Gemba to Draft the SOP
- Engineer and Operator stand together at the machine face.
- Document the exact step-by-step physical actions required to complete the task safely and flawlessly.

### Step 2: Photography & Abnormality Definition
- Capture high-resolution photos of every critical step.
- Include explicit "Correct vs. Incorrect" visual comparisons:
  - Example: Photo of smooth, lump-free slurry vs. Photo of aerated, agglomerated slurry.

### Step 3: Deployment at Eye Level
- Laminate the 1-page visual SOP.
- Mount directly on the machine control panel or workstation at eye level.
- Prohibit filing SOPs in closed administrative binders.

### Step 4: The 5-Minute Daily SOP Audit
- Shift supervisor randomly selects 1 operator daily and observes them performing the SOP.
- Coach immediately if deviations are observed; update the SOP if the operator has discovered a superior method.""",
        "example1": """### Example 1: Eliminating Raw Material Dispensing Errors on Kettle #3
**Situation:** Once a month, an operator accidentally dumped 50 kg of Calcined Kaolin clay instead of Titanium Dioxide into the disperser kettle because both raw materials came in similar 25 kg brown paper bags, ruining ₹1.2 Lakhs of paint.
**Gemba Visual SOP & Poka-Yoke Applied:**
- Took high-visibility color photographs of the exact bag labeling and texture difference.
- Created color-coded pallet staging bays on the floor: Green Zone for TiO2; Orange Zone for Extender Clay.
- Created a 1-page visual SOP mounted directly above the bag-dump hopper showing the bag markings.
- Installed a simple barcode scanner interlock: Operator must scan the raw material bag barcode before the hopper dust lid unlocks.
- Result: Raw material dispensing errors dropped to absolute zero for 14 consecutive months.""",
        "example2": """### Example 2: Standardizing the 15-Minute Tinting Dispenser Calibration
**Situation:** Automated tinting machines at dealer counters frequently dispensed off-shade colorant because dealer operators cleaned tinting nozzles irregularly, using metal needles that scratched the nozzle orifice.
**Visual Gemba SOP Developed:**
- Replaced the 12-page technical manual with a single laminated plastic card attached to the machine by a chain.
- Contained 4 visual steps with photos:
  1. Moisten the felt sponge with distilled water.
  2. Gently wipe nozzle tips using a circular motion (Photo: No metal tools!).
  3. Purge 0.5 ml of colorant.
  4. Visual check: Clean jet stream (Photo Good) vs Deflected spray (Photo Bad).
- Off-shade dealer tinting complaints dropped by 74% across all 45 installed machines.""",
        "failures": [
            ("Desk-Bound SOP Writing", "Engineers writing procedures in an office without observing the real shop floor reality.", "SOPs must be created and tested at the Gemba with frontline operator participation."),
            ("Text-Heavy Binder Graveyards", "Writing 30-page text manuals that operators never read.", "Enforce 1-page visual SOPs with high-contrast photos displayed directly at the workstation."),
            ("Static Frozen Standards", "Treating an SOP as an unchangeable legal contract rather than a living baseline for improvement.", "Revise SOPs whenever Kaizen improvements yield a superior operational method."),
            ("Zero Audit Follow-Through", "Posting SOPs on the wall and never verifying whether operators follow them.", "Institute daily 5-minute supervisory SOP observation audits.")
        ],
        "checklist": [
            "SOPs developed and validated at the Gemba with frontline operator input.",
            "Visual format enforced: minimum 70% photos/diagrams showing Good vs. Bad states.",
            "SOPs laminated and mounted at eye level directly at the workstation.",
            "Visual management standards (shadow boards, color-coded pipes, sight gauges) operational.",
            "Poka-Yoke mistake-proofing mechanisms integrated into high-risk process steps.",
            "Daily supervisory observational audits verify 100% standard work compliance."
        ]
    },
    "peter-senge-fifth-discipline-engine": {
        "title": "Peter Senge Systems Thinking & Learning Organization Engine for Swatch Paints",
        "legend": "Peter M. Senge (MIT Professor & Author of 'The Fifth Discipline')",
        "description": "Peter Senge Systems Thinking, Causal Loop Diagrams, Shared Vision, Mental Models, and Team Learning for Swatch Paints Enterprise Architecture.",
        "dept": "08_systems_sops",
        "tag": "peter-senge",
        "purpose": """This skill equips the Swatch Paints Executive Leadership, Cross-Functional Committees, and Systems Architects with Peter Senge’s revolutionary disciplines of **Systems Thinking (The Fifth Discipline)** and the **Learning Organization**.

In traditional corporate silos, departments behave like blind men touching an elephant: Sales blames Production for stockouts, Production blames Procurement for missing raw materials, Procurement blames Finance for delayed supplier payments, and Finance blames Sales for uncollected receivables. Everyone optimizes their own local silo, yet the enterprise as a whole bleeds cash, suffers inventory whiplash, and fails customers. Managers treat surface symptoms with quick-fix band-aids that cause even worse long-term side effects.

The engine's purpose is to:
- Institutionalize **Systems Thinking**: seeing the whole forest rather than isolated trees, mapping complex causal feedback loops and time delays across the enterprise.
- Surface and test **Mental Models**: challenging deeply ingrained assumptions and dogmas that blind leadership to new market realities.
- Unify all 8 departments under a genuine **Shared Vision** inspired by Ashutosh Sharma Sir’s founding purpose.
- Foster **Team Learning & Dialogue**: replacing defensive departmental blame with collaborative, deep problem-solving.""",
        "when_to_use": """- Chronic, recurring cross-departmental conflicts (e.g., Sales vs. Finance vs. Manufacturing).
- Implementing enterprise-wide digital transformation or major ERP architectural redesign.
- Experiencing systemic boom-and-bust cycles in inventory, cash flow, or dealer credit.
- Formulating annual strategic visions and multi-year organizational development plans.
- Root-cause auditing of complex, multi-departmental failures that defy simple mechanical explanations.
- Cultivating an enduring learning culture where mistakes are treated as systemic feedback rather than personal sins.""",
        "frameworks": """### 6.1 The Five Disciplines of the Learning Organization
1. **Personal Mastery:** Continuous personal growth and commitment to excellence by every individual.
2. **Mental Models:** Surfacing, testing, and improving our internal pictures of how the world works.
3. **Shared Vision:** Building a genuine sense of shared commitment to enterprise purpose, not passive compliance.
4. **Team Learning:** Transforming conversational habits from debate (trying to win) to dialogue (seeking deep collective understanding).
5. **Systems Thinking (The Fifth Discipline):** The conceptual cornerstone that integrates the other four disciplines into a coherent whole.

### 6.2 Key Systems Archetypes in Paint Manufacturing
- **1. Fixes that Fail:** 
  - *Symptom:* Month-end sales target is missed. 
  - *Quick Fix:* Offer a 4% unauthorized cash scheme to dealers to dump stock on the 31st.
  - *Unintended Consequence:* Next month's sales crater because dealers are overstocked; DSO explodes; future baseline targets are even harder to hit!
- **2. Shifting the Burden:**
  - Relying on external transport contractors to fix chronic depot delivery delays instead of fixing internal warehouse slotting and picking workflows.
- **3. Causal Loop Diagrams (Reinforcing & Balancing Loops):**
  - Mapping how an increase in painter training workshops creates a reinforcing loop: More trained painters -> Higher Swatch Rustic demand -> Faster dealer inventory turns -> Greater dealer shelf space -> Higher company profits -> More investment in painter training!""",
        "decision_algo": """### Step 1: Map the Causal Feedback Loop
- When a chronic operational problem arises, gather representatives from all affected departments.
- Draw a Causal Loop Diagram on a whiteboard:
  - Identify Reinforcing (R) loops, Balancing (B) loops, and Time Delays (||).
  - Locate the systemic root cause, not the immediate surface symptom.

### Step 2: Surface Unexamined Mental Models
- Ask: What assumptions are we holding that might no longer be true?
  - Example Mental Model: *"Dealers will only buy paint if we give 45 days of credit."*
  - Test with data: Show dealers who buy on 7-day cash terms because of high inventory velocity.

### Step 3: Find the Point of Highest Leverage
- Systems Thinking Principle: **Small, well-focused actions can produce significant, enduring improvements if applied at the right place (High Leverage).**
- Banning month-end billing dumping is a high-leverage intervention that stabilizes the entire factory, warehouse, and cash flow.

### Step 4: Conduct Cross-Departmental Dialogue Circles
- Hold monthly "Dialogue Councils" where Sales, Plant, and Finance discuss systemic bottlenecks without finger-pointing.""",
        "example1": """### Example 1: Breaking the 'Fixes that Fail' Month-End Primary Dumping Loop
**Situation:** For 3 years, Swatch suffered from the "Hockey Stick" sales curve: 60% of monthly sales were billed in the last 4 days of the month through massive dealer discounts. The first 15 days of every new month, the factory ran at 20% capacity with workers idle, followed by panic 14-hour overtime shifts at month-end.
**Senge Systems Archetype Applied:**
- Mapped the Causal Loop: Proved that month-end discounting was a classic "Fix that Fails"—each round of discounting made the subsequent month's hangover worse, creating extreme inventory volatility and factory overtime expense.
- *High-Leverage Systemic Fix:* Abolished the single-day month-end volume bonus. Split sales quotas into three 10-day sprints.
- Result: Orders smoothed out evenly across the month; factory capacity utilization stabilized at 84%; overtime costs dropped by 70%, and working capital velocity accelerated.""",
        "example2": """### Example 2: Aligning Factory and Field Around a Shared Vision
**Situation:** Plant chemists viewed sales reps as "irresponsible cowboys who promise impossible custom colors," while sales reps viewed chemists as "arrogant nerds who sit in air-conditioned labs and destroy deals."
**Team Learning & Shared Vision Intervention:**
- Swapped roles for 2 days: Sales reps worked in the lab measuring viscosity and experiencing the chemistry constraints; plant chemists spent 2 days co-riding on dusty dealer beats listening to painter complaints.
- Mutual respect replaced hostility.
- Formed joint "Speed-to-Market" squads that reduced custom color turnaround from 7 days to 24 hours.""",
        "failures": [
            ("Local Silo Optimization", "Production celebrating high kettle efficiency while warehouses are full of unsold paint.", "Systems Thinking rule: Optimizing a subsystem almost always sub-optimizes the total system."),
            ("Linear Blame Game", "Blaming individuals for failures that are structural properties of the system architecture.", "Look at the causal loops, incentives, and delays; fix the system structure rather than blaming people."),
            ("Addiction to Band-Aid Quick Fixes", "Using discounts, emergency freight, or overtime to treat symptoms while ignoring root causes.", "Map the 'Fixes that Fail' archetype; find the point of high structural leverage."),
            ("Fragmented Silo Meetings", "Holding meetings within sales, within plant, and within finance, but never together.", "Mandate cross-functional dialogue councils to align the whole enterprise.")
        ],
        "checklist": [
            "Chronic problems analyzed using Causal Loop Diagrams and Systems Archetypes.",
            "Root causes identified through structural system analysis rather than personal blame.",
            "Implicit mental models and company dogmas surfaced, tested, and updated.",
            "High-leverage intervention points prioritized over superficial quick-fix band-aids.",
            "Cross-functional dialogue councils operational between Sales, Manufacturing, and Finance.",
            "Shared enterprise vision actively communicated and reinforced across all operational tiers."
        ]
    },
    "taiichi-ohno-standardization-engine": {
        "title": "Taiichi Ohno Standardized Work & Poka-Yoke Systems Engine for Swatch Paints",
        "legend": "Taiichi Ohno (Architect of the Toyota Production System & Standardized Work)",
        "description": "Taiichi Ohno Standard Work Combinations, Takt Time Synchronization, Standard WIP (SWIP), and Poka-Yoke for Swatch Paints Manufacturing.",
        "dept": "08_systems_sops",
        "tag": "taiichi-ohno-standards",
        "purpose": """This skill equips the Swatch Paints Industrial Engineering, Factory Automation, and Operations Systems teams with Taiichi Ohno’s rigorous principles of **Standardized Work (Hyojun Sagyo)**, **Standard Work-in-Progress (SWIP)**, and **Mistake-Proofing (Poka-Yoke)**.

In many Indian manufacturing plants, work is executed through chaotic individual improvisation: Worker A loads pigment into the disperser in 10 minutes, while Worker B takes 35 minutes and dumps the bags in reverse order; Chemist X checks grind fineness after 20 minutes, while Chemist Y forgets and checks after an hour. Without precise standardized work, quality is unpredictable, cycle times swing wildly, and safety hazards abound.

The engine's purpose is to:
- Establish the three non-negotiable elements of Ohno's **Standardized Work: Takt Time, Work Sequence, and Standard Work-in-Progress (SWIP)**.
- Engineer visual **Standard Work Combination Sheets (SWCS)** detailing human manual time, machine automatic time, and walking time down to exact seconds.
- Deploy mechanical and digital **Poka-Yoke (Mistake-Proofing)** devices that make human error physically impossible.
- Maintain absolute process repeatability so that every batch of Swatch Paints is chemically and physically identical regardless of who is on shift.""",
        "when_to_use": """- Designing new production lines, automated packaging conveyors, or tinting dispensing stations.
- High variance in cycle time or yield across different operators on the same machine.
- Packaging lines suffer from frequent human errors (missing lids, incorrect batch barcode stickers, misaligned labels).
- Work-in-Progress (WIP) paint accumulates between grinding mills and packaging tanks, creating floor congestion.
- Training new machine operators and technical line workers to full productivity within 48 hours.
- Conducting line balancing and ergonomic workstation optimization.""",
        "frameworks": """### 6.1 The Three Elements of Standardized Work
Ohno defined Standardized Work as the optimal combination of people and machines using minimum resources:
1. **Takt Time:** The pace of production synchronized with customer demand:
   ```
   Takt Time = Available Daily Operating Time / Daily Customer Demand
   ```
2. **Work Sequence:** The exact, sequential order in which an operator performs physical tasks (e.g., Step 1: Open hopper -> Step 2: Scan bag -> Step 3: Dump pigment -> Step 4: Engage disperser).
3. **Standard Work-in-Progress (SWIP):** The minimum number of unfinished pieces or slurry litres required to keep the process running smoothly without idle waiting.

### 6.2 Standard Work Combination Sheet (SWCS)
A visual chart displaying:
- **Manual Time (Solid Line):** Physical human action.
- **Machine Time (Dotted Line):** Automated machine processing.
- **Walking Time (Wavy Line):** Operator movement between stations.
- The total cycle time must equal or be slightly less than Takt Time.

### 6.3 Poka-Yoke (Mistake-Proofing) Principles
Human beings are fallible; the system must make mistakes impossible:
- **Contact Method:** Physical pins or sensors that detect whether a pail is properly positioned under the filling nozzle before paint can flow.
- **Fixed-Value Method:** Automated batch scales that prevent the mixer from starting unless exactly the prescribed kilograms of raw material have been dispensed.
- **Motion-Step Method:** Sequence-locking software that requires scanning the barcode on the resin barrel before the solvent valve will open.""",
        "decision_algo": """### Step 1: Time Study & Baseline Measurement
- Video record 10 consecutive cycles of the target operation.
- Break down elements into Manual Time, Machine Time, and Walking Time.
- Eliminate all unnecessary motion (Muda).

### Step 2: Establish Standard Work Sequence & SWIP
- Define the optimal sequence that minimizes worker fatigue and ergonomic strain.
- Calculate exact SWIP (e.g., exactly 1 buffer tank of 2,000 litres between sand mill and canning line).

### Step 3: Implement Poka-Yoke Controls
- Identify high-risk failure points (e.g., missing lid gasket, wrong can label).
- Install fail-safe mechanisms:
  - Photo-eye sensors that stop the line if a pail passes without a lid.
  - Barcode interlocks on chemical ingredient dosing.

### Step 4: Standardized Work Auditing
- Post the Standard Work Sheet at the workstation.
- Line supervisor verifies operator compliance daily; deviations trigger retraining.""",
        "example1": """### Example 1: Balancing the 20-Litre Distemper Canning Line
**Situation:** The automated 20L canning line had a theoretical capacity of 300 pails/hour, but achieved only 165 pails/hour. Operators were bumping into each other, and the lid-pressing machine frequently jammed.
**Standardized Work Applied:**
- Mapped the Standard Work Combination Sheet:
  - Takt Time required: 15 seconds per pail.
  - Found that Operator 1 was spending 8 seconds walking across the conveyor to fetch lids.
  - Re-positioned lid storage directly adjacent to the conveyor (Walking time slashed to 0).
  - Standardized the work sequence: Operator 1 feeds pails and lids; Operator 2 verifies seal and attaches barcode; Operator 3 palletizes.
- Line output increased from 165 to 285 pails/hour with zero overtime; operator physical fatigue dropped noticeably.""",
        "example2": """### Example 2: Poka-Yoke Prevents Multi-Lakh Color Contamination
**Situation:** Operators occasionally loaded red solvent-based tinting colorant into the white water-based dispenser tank, ruining 3,000 litres of premium base paint (loss of ₹3.6 Lakhs).
**Poka-Yoke Fix Installed:**
- Changed the mechanical inlet coupling geometry: Water-based tanks were fitted with square female quick-connect couplers; solvent tanks were fitted with round threaded couplers.
- A solvent hose physically cannot connect to a water-based tank!
- Zero chemical cross-contamination incidents recorded since installation.""",
        "failures": [
            ("Standardization Without Operator Involvement", "Engineers imposing paper standards that ignore physical line realities.", "Operators must participate in designing and validating standard work sequences."),
            ("Allowing 'Secret' Individual Workarounds", "Tolerating operators using unapproved private tools or bypassing steps.", "Enforce absolute standard work adherence; improve the standard formally if a better method is found."),
            ("Poka-Yoke Bypassing", "Operators using tape or wire to bypass safety interlocks and sensors.", "Zero tolerance for bypassing safety or quality Poka-Yoke controls; automated line stops if bypassed."),
            ("Ignoring SWIP Limits", "Accumulating 20 unsealed pails in front of the lid-presser, cluttering the floor.", "Enforce strict Standard Work-in-Progress limits; halt upstream work when SWIP is full.")
        ],
        "checklist": [
            "Takt Time calculated and visible on the factory floor.",
            "Standard Work Combination Sheets (SWCS) documented for all production stations.",
            "Standard Work-in-Progress (SWIP) defined and controlled visually.",
            "Poka-Yoke mistake-proofing devices active on all critical packaging and dosing steps.",
            "Ergonomic line balancing executed to eliminate unnecessary walking and lifting motion.",
            "Daily supervisory standard work adherence audits active across all operating shifts."
        ]
    },
    "w-edwards-deming-process-systems-engine": {
        "title": "W. Edwards Deming Enterprise Systems Architecture & Red Bead Engine for Swatch Paints",
        "legend": "W. Edwards Deming (Pioneer of Total Quality Management & System of Profound Knowledge)",
        "description": "Deming Red Bead Experiment, Eliminating Departmental Barriers, Abolishing Numerical Quotas, and Process Systems Architecture for Swatch Paints.",
        "dept": "08_systems_sops",
        "tag": "w-edwards-deming-systems",
        "purpose": """This skill equips the Swatch Paints Executive Leadership, Systems Architects, and Cross-Functional Process Design teams with W. Edwards Deming’s revolutionary **Enterprise Systems Architecture**, the famous **Red Bead Experiment**, and the abolition of destructive managerial quotas.

Most corporate management systems operate on a deeply flawed psychological premise: they believe that workers and managers can produce higher quality simply by "trying harder", offering merit bonuses, threatening punishments, and posting motivational slogans on walls ("Zero Defects!", "Strive for Excellence!"). Deming’s Red Bead Experiment proved that **performance is 94% determined by the design of the system, and only 6% by the individual worker**. Blaming individuals for system failures breeds fear, cynicism, data falsification, and cross-departmental warfare.

The engine's purpose is to:
- Redesign company workflows as an integrated **Deming Process System**: where suppliers, manufacturing, distribution, and customers form a cooperative cooperative network.
- **Abolish Numerical Quotas & Slogans**: replacing arbitrary targets with capable, stable processes and managerial coaching.
- **Drive Out Fear**: creating an environment where frontline workers and sales reps report operational bottlenecks and defects immediately without fear of punishment.
- **Break Down Barriers Between Departments**: aligning Purchasing, R&D, Manufacturing, and Sales under a single shared purpose of long-term enterprise survival and customer delight.""",
        "when_to_use": """- Redesigning enterprise-wide Standard Operating Procedures and cross-departmental handoffs.
- Departments are engaged in bitter political blame wars (e.g., Sales blaming Plant; Plant blaming Procurement).
- Frontline employees are hiding quality defects, transport damages, or inventory errors out of fear.
- Evaluating the impact of numerical sales quotas and incentive schemes on product quality and customer trust.
- Structuring long-term supplier partnerships based on single-sourcing and statistical quality.
- Conducting enterprise-wide systems transformation under the authority of Ashutosh Sharma Sir.""",
        "frameworks": """### 6.1 Deming's Flow Diagram: Production as a System
Deming’s revolutionary 1950 diagram that transformed post-war Japanese industry:
```
[SUPPLIERS OF MATERIALS] ──► [RECEIPT & TEST] ──► [PRODUCTION PROCESSES] ──► [DISTRIBUTION] ──► [CONSUMERS]
            ▲                                                                                 │
            │                                                                                 ▼
            └─────────────────────── [RESEARCH & CUSTOMER FEEDBACK] ◄─────────────────────────┘
```
- A paint plant is not an isolated castle; it is an interdependent system. If procurement buys low-grade extender to save money, the factory suffers grind blockages, the depot receives off-spec paint, the dealer loses face, and the customer churns.

### 6.2 The Red Bead Experiment Operationalized
Deming proved that when workers are given a paddle and told to draw beads from a box containing 80% white beads and 20% red beads (defects):
- No amount of motivation, bonuses, shouting, or performance improvement plans (PIPs) can reduce the number of red beads drawn!
- **The moral:** The defects are in the system (the box). Only management has the power to redesign the system (filter out the red beads from raw materials and processes).

### 6.3 Deming's Anti-Quota Principle
*"Numerical quotas and work standards for the workforce establish a ceiling on quality and output. Eliminate management by numbers and arbitrary numerical goals; substitute leadership."*
- When a sales rep has a hard quota of ₹10 Lakhs, they dump unwanted paint at 30% discount on the 31st. The quota was met, but the enterprise was damaged.""",
        "decision_algo": """### Step 1: Cross-Functional Process Mapping
- Convene the cross-departmental team.
- Map the end-to-end customer journey from raw chemical procurement to painter wall application.
- Identify every handoff point where friction, finger-pointing, or data loss occurs.

### Step 2: Systemic Root-Cause Attribution
- When a major operational failure occurs:
  - Strictly enforce Deming’s 94/6 Rule: Assume 94% of the problem is systemic architecture, not individual malice.
  - Redesign the process, training, or tooling rather than issuing reprimands.

### Step 3: Replace Slogans with Capability
- Remove empty motivational posters ("Do It Right First Time!").
- Provide the tools, calibrated instruments, and standard work instructions that make doing it right unavoidable.

### Step 4: Eliminate Departmental Turf Wars
- Establish shared cross-functional KPIs (e.g., Plant and Sales share a single joint metric: On-Time In-Full Dealer Delivery Net of Customer Satisfaction).""",
        "example1": """### Example 1: Ending the War Between Procurement and Production
**Situation:** The plant suffered 12 kettle batch blockages in 2 months. The Production Manager accused the Purchasing Manager of "buying garbage pigments from cheap traders." The Purchasing Manager responded that he was hit his KPI of "cutting raw material procurement costs by 4%."
**Deming Systems Thinking Intervention Applied:**
- Replaced the conflicting individual KPIs with a single **Joint System KPI: Total Finished Cost per Delivered Litre**.
- Proved that the ₹1.2 Lakh savings in cheap pigment resulted in ₹4.8 Lakhs in kettle downtime, solvent wash, and overtime labor.
- Procurement and Production chemists jointly qualified single-source pigment manufacturers with certified statistical process capability.
- Batch blockages fell to zero; total system manufacturing costs fell by 6.2%.""",
        "example2": """### Example 2: Driving Out Fear to Prevent Catastrophic Product Recalls
**Situation:** An operator on Kettle #2 noticed that a batch of exterior emulsion had a strange sour smell (bacterial biocide failure), but said nothing because the plant had a policy of deducting pay for scrapped batches. The 4,000 litres were canned, dispatched, and subsequently spoiled on dealer shelves, costing ₹6.8 Lakhs in returns and customer anger.
**Deming 'Drive Out Fear' Culture Overhaul:**
- CEO Ashutosh Sharma Sir publicly abolished financial penalties for reporting batch abnormalities.
- Instituted a policy: Any operator who halts a potentially defective batch receives an immediate ₹1,000 "Vigilance Award" at the morning huddle.
- Frontline transparency flourished; minor abnormalities were caught in the kettle before canning, preventing any further contaminated product from reaching the market.""",
        "failures": [
            ("Blaming Workers for System Defects", "Punishing machine operators for batch defects caused by uncalibrated scales or poor raw materials.", "Deming 94/6 Rule: Fix the system design, raw material inputs, and tooling first."),
            ("Managing by Arbitrary Quotas", "Setting a numerical sales quota of ₹1 Crore without providing the marketing, supply chain, or credit systems to achieve it.", "Focus on improving the capability of the underlying processes; output will follow naturally."),
            ("Departmental Silo Warfare", "Allowing departments to optimize their own local metrics at the expense of enterprise solvency.", "Break down barriers; align departments under shared customer-focused metrics."),
            ("Managing by Fear", "Threatening employees with termination for making honest mistakes, driving bad news underground.", "Drive out fear. A healthy enterprise welcomes bad news early so problems can be solved before they become disasters.")
        ],
        "checklist": [
            "Enterprise workflows mapped and governed as integrated Deming Process Systems.",
            "Deming 94/6 Rule practiced: systems architecture prioritized over individual blame.",
            "Empty motivational slogans and arbitrary numerical quotas eliminated.",
            "Fear driven out of the workplace; early defect reporting rewarded.",
            "Suppliers integrated into long-term quality partnerships based on total cost.",
            "Cross-functional metrics align Procurement, Manufacturing, Finance, and Sales."
        ]
    }
}

def generate_vis_sys_skill(name, data):
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
        f"*{data['legend']} — Operationalized for Swatch Paints Enterprise Architecture.*",
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
        "Before invoking this engine, collect the following real-time inputs from live enterprise systems, ERP ledgers, and operational logs. Zero static assumptions or hardcoded parameters are permitted.",
        "",
        "### 4.1 Enterprise & Strategic Inputs",
        "",
        "| Input | Why It Matters | Live System Source |",
        "|---|---|---|",
        "| Process Cycle Time & Lead Time Logs | Identifies limiting steps, bottlenecks, and process delays | SCADA / ERP Workflow Engine |",
        "| Cross-Departmental Performance Data | Maps interdependent flows between Sales, Plant, and Finance | Central Executive MIS |",
        "| Quality Variance & Scrap Records | Quantifies common cause vs special cause system noise | LIMS / Quality Ledger |",
        "| Competitor & Market Structural Data | Evaluates Five Forces, price elasticity, and industry shifts | Field Intelligence Master |",
        "",
        "### 4.2 Financial & Strategic Guardrails",
        "",
        "| Guardrail | Enforcement Rule | Authority |",
        "|---|---|---|",
        "| Generic Strategy Sanctity | Never compromise Focused Differentiation for commodity volume | CEO Office / Board |",
        "| 94/6 Systems Rule | Systemic architecture investigated before individual reprimands | Executive Leadership |",
        "| Type 1 vs Type 2 Gate | Reversible Type 2 decisions executed within 48 hours | Operational Directors |",
        "",
        "---",
        "",
        "## 5. DIAGNOSTIC QUESTIONS",
        "",
        f"Apply these 10 diagnostic inquiries before taking strategic, structural, or systems action under the {name} framework:",
        "",
        "1. What is the fundamental systemic bottleneck or limiting step in this operational chain?",
        "2. Are we confusing superficial operational effectiveness with deep, defensible strategic differentiation?",
        "3. Is this a Type 1 irreversible door or a Type 2 reversible door decision?",
        "4. Have we mapped the complete causal feedback loop, including delayed unintended consequences?",
        "5. Are we blaming frontline workers for a failure that is mathematically built into the system architecture?",
        "6. Does our Standard Operating Procedure (SOP) communicate visually and unmistakably at the Gemba?",
        "7. Are we practicing high-leverage managerial training or micromanaging low-impact tasks?",
        "8. Are our departments cooperating as an interdependent system or fighting destructive silo turf wars?",
        "9. What is the worst-case systemic failure mode, and what fail-safe Poka-Yoke controls prevent it?",
        "10. Who has single-point accountability for governance, and how is the learning documented?",
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
        "Every strategic vision memo, SOP architecture document, or systems design blueprint must follow this standardized schema:",
        "",
        "```markdown",
        f"# Swatch Paints Enterprise Architecture Directive: {data['title']}",
        "",
        "### 1. Strategic Scope & Objective",
        "- **Target Domain / Division:** [Corporate / Manufacturing / Supply Chain / Systems]",
        "- **Lead Executive:** [Designation & Name]",
        "- **Time Horizon:** [Effective Date – Strategic Review Date]",
        "- **Core Quantified Objective:** [Single measurable statement of target system outcome]",
        "",
        "### 2. Methodological & Systems Intervention",
        "- **Systemic Diagnostic Findings:** [Root cause causal loops / limiting step analysis]",
        "- **Actionable Standard / Protocol:** [Specific process or architectural change]",
        "- **Mistake-Proofing & Visual Controls:** [Poka-Yoke / Gemba SOP / Paired Indicators]",
        "",
        "### 3. Enterprise & Quality Guardrails",
        "- **Strategic Alignment Floor:** [Focused Differentiation / Core Values adherence]",
        "- **Process Capability Target:** [Minimum acceptable statistical quality threshold]",
        "- **Emergency Rollback Trigger:** [Specific event requiring immediate project halt]",
        "",
        "### 4. Governance & Cadence",
        "- **Audit / Review Cadence:** [Weekly / Monthly operational review]",
        "- **Process System Owner:** [Named Systems Architect / Operations Director]",
        "- **Final Executive Approval:** [CEO Office / Ashutosh Sharma Sir]",
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
        "Watch for these recurring strategic, structural, and systems failure modes:",
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
        "Before finalizing or launching any systems protocol under this skill, verify:",
        ""
    ])
    for item in data['checklist']:
        sections.append(f"- [ ] {item}")
        
    sections.extend([
        "",
        "---",
        "",
        f"**CEO Directive:** At Swatch Paints, operational mastery and strategic vision are the ultimate engines of enterprise greatness. We reject bureaucratic stasis, departmental silos, and superficial band-aids. Every executive, plant engineer, and systems architect must embody the principles of {data['legend']} daily, building an enduring, world-class enterprise that sets the standard for the Indian coatings industry."
    ])
    return "\n".join(sections)

def main():
    for name, data in VIS_SYS_SKILLS.items():
        content = generate_vis_sys_skill(name, data)
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
