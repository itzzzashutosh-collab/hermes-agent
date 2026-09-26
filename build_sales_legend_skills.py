import os

WORKSPACE_DIR = r"d:\Sharma Industries Erp Software\hermes-agent"
HERMES_DIR = r"C:\Users\itzzz\AppData\Local\hermes"

SALES_SKILLS = {
    "andy-grove-execution-engine": {
        "title": "Andy Grove Sales Execution, OKRs & Capacity Planning Engine for Swatch Paints",
        "legend": "Andy Grove (Legendary Intel CEO & Author of 'High Output Management')",
        "description": "Andy Grove OKRs, Sales Capacity Planning, Output-Oriented Review, and Managerial Leverage Engine for Swatch Paints Sales Department.",
        "dept": "01_sales",
        "tag": "andy-grove",
        "purpose": """This skill equips Swatch Paints sales leadership with Andy Grove's rigorous operational engineering disciplines: Objectives & Key Results (OKRs), Sales Capacity Planning, Managerial Leverage, and Output-Oriented Performance Management.

In Indian paint distribution, sales management often suffers from vague motivational slogans, unfocused field calls, and disjointed quarterly sprints. Andy Grove’s discipline treats the sales organization like an engineered production line: inputs (dealer visits, painter demos, sample kits) are transformed through high-leverage activities into measurable enterprise outputs (secondary volume off-take, net contribution margin, active dealer retention).

The engine's purpose is to:
- Translate CEO strategic goals into quarterly, bi-weekly, and daily field sales OKRs.
- Calculate true sales capacity (hours per rep, counter bandwidth, travel limits) to prevent rep burnout and superficial coverage.
- Maximize managerial leverage by structuring high-impact 1-on-1s, operational reviews, and peer training.
- Establish leading indicators that predict quarterly sales shortfalls 45 days before month-end, enabling proactive intervention.""",
        "when_to_use": """- Structuring quarterly OKRs for Regional Sales Managers, ASMs, and TSIs across Rajasthan.
- Territory capacity planning: determining how many dealer counters an individual sales rep can effectively manage.
- Conducting bi-weekly 1-on-1 operational reviews between ASMs and field officers.
- Diagnosing a territory that appears busy but consistently misses secondary sales milestones.
- Establishing leading operational indicators (pipeline velocity, demo-to-order ratio) vs. lagging indicators (invoiced revenue).
- Eliminating low-leverage administrative tasks to liberate sales rep bandwidth for high-leverage dealer engagements.""",
        "frameworks": """### 6.1 Grove's Production Principle Applied to Sales
Grove demonstrated that all work can be modeled as a production process with three basic operations:
1. **Delivering:** Securing the finalized purchase order and dispatch from the depot.
2. **Processing:** The sales pitch, demonstration of Swatch Rustic, dealer margin breakdown, and objection resolution.
3. **Inspection:** Validating creditworthiness, verifying dealer godown stock, and confirming painter loyalty registration.

**The Limiting Step:** In paint sales, the limiting step is almost never the dealer's desire to buy; it is the dealer's working capital liquidity and available shelf space. Sales reps must schedule all activities backward from this limiting step.

### 6.2 Objectives & Key Results (OKRs)
Grove established OKRs to answer two questions:
1. *Where do I want to go?* (The Objective: ambitious, qualitative, memorable).
2. *How will I know I'm getting there?* (The Key Results: quantifiable, time-bound, verifiable).

**Rule of OKRs:**
- Maximum 3 to 5 Objectives per quarter.
- Maximum 3 Key Results per Objective.
- Every Key Result must have a verifiable number. No subjective adjectives ("improve dealer relationships").

### 6.3 Managerial Leverage
A manager's total output is:
```
Manager's Output = Output of Manager's Unit + Output of Neighboring Units Influenced
```
High-leverage sales activities include:
- Spending 4 hours co-riding with a struggling TSI to teach Swatch Rustic texture demonstrations (affects 40 dealer accounts).
- Standardizing the 15-minute dealer audit checklist across all 6 Rajasthan territories.
- Setting unambiguous credit rules that prevent 50 hours of future collection disputes.

Negative-leverage activities to eliminate:
- Meddling in routine dealer tinting color complaints that the plant lab should handle.
- Holding 2-hour unstructured evening sales calls where reps simply read out daily billing numbers.""",
        "decision_algo": """### Step 1: Territory Capacity & Limiting Step Audit
- IF a TSI is assigned >50 active dealer counters:
  - STOP. Flag as "Capacity Overload". An effective dealer relationship requires 2 visits/month of 45 minutes each + travel time. Cap territory span at 40-45 counters.
- IF travel time consumes >35% of rep working hours:
  - Cluster accounts into tight geographic zones. Enforce the "No Cross-Town Crisscrossing" rule.

### Step 2: Formulate Quarterly OKRs
- Objective must align with enterprise growth (e.g., "Establish Swatch as the dominant texture brand in Hadoti").
- Key Result 1 must be Financial (Net Contribution Margin from Live ERP).
- Key Result 2 must be Operational (Active billing counters + demo walls executed).
- Key Result 3 must be Quality/Risk (DSO held under 28 days with zero unverified returns).

### Step 3: Implement Leading vs. Lagging Indicators
- DO NOT rely on primary billing as the primary weekly metric (Lagging).
- Track Leading Indicators daily:
  - Number of painter mock-up boards completed.
  - Number of newly scanned painter loyalty tokens.
  - Number of non-billing counters re-activated.

### Step 4: High-Leverage 1-on-1 Execution
- Conduct bi-weekly 45-minute Grove 1-on-1s between ASM and TSI.
- The agenda belongs to the employee, not the manager. Focus on performance hurdles, skill gaps, and field bottlenecks.""",
        "example1": """### Example 1: Restructuring Alwar-Bharatpur Territory OKRs
**Situation:** The TSI in Alwar hit 70% of targets for two quarters. The ASM spent 30 minutes every evening shouting at him over missed billing numbers. The TSI felt overwhelmed and resigned.
**Grove Diagnostic Applied:**
1. *Capacity Audit:* The TSI had 72 dealers across 120 km. Realistically, he could only give 15 minutes per dealer, leading to superficial visits.
2. *Limiting Step:* Local dealers were afraid of stocking new Swatch exterior emulsion because rival Asian Paints distributors offered 4-hour replenishment.
3. *High-Leverage Fix:* Territory was split: 30 non-core rural counters transferred to a regional sub-dealer. TSI focused on 42 high-potential urban accounts.
4. *Grove OKR Implemented:*
   - **Objective:** Dominate the premium contractor repaint segment in Alwar city.
   - **KR 1:** Open 12 new Swatch Rustic display counters by end of Q2.
   - **KR 2:** Conduct 24 on-site contractor demonstrations with the technical applicator.
   - **KR 3:** Maintain average DSO below 25 days.
**Outcome:** Secondary sales surged by 44% in 90 days; rep retention achieved.""",
        "example2": """### Example 2: Eliminating Negative Leverage in Kota ASM Operations
**Situation:** The Kota ASM was spending 18 hours per week manually approving discount exceptions and handling transport driver delays over WhatsApp.
**Grove Diagnostic Applied:**
- This was negative leverage: a senior manager doing clerical fire-fighting while junior TSIs lacked field coaching.
**Solution:**
- Created an automated ERP rule: any order within standard trade credit is automatically approved; exceptions over 5% require CEO desk review.
- Transferred transport follow-up to the central warehouse dispatcher.
- Freed up 14 hours/week for the ASM to conduct joint contractor site visits, increasing high-margin Swatch Rustic sales by ₹18 Lakhs in that quarter.""",
        "failures": [
            ("MBO Activity Trap", "Logging 20 calls a day with zero secondary conversion.", "Shift measurement from call volume to qualified demo-to-order conversions."),
            ("Lagging Metric Obsession", "Managing purely by looking at end-of-month revenue numbers.", "Track leading indicators (painter registrations, mock-up walls) daily."),
            ("Capacity Delusion", "Assigning 80 dealers to a single sales rep on a motorbike.", "Cap rep capacity at 40-45 accounts and institute sub-distributor models for low-volume counters."),
            ("Micromanagement 1-on-1s", "Manager talks 90% of the time, barking orders.", "Grove Rule: The subordinate prepares the agenda; the manager listens and removes road-blocks.")
        ],
        "checklist": [
            "Territory capacity is capped at 40-45 active dealer counters per rep.",
            "Quarterly OKRs have exactly 1 qualitative Objective and 3 measurable Key Results.",
            "Key Results are tied to live ERP contribution margin and DSO, not unverified claims.",
            "Daily leading indicators (demos, token scans) are visible on the mobile SFA app.",
            "Bi-weekly 45-minute 1-on-1s are scheduled with subordinate-driven agendas.",
            "Administrative friction is audited and capped at <15% of rep working hours."
        ]
    },
    "chris-voss-tactical-negotiation-engine": {
        "title": "Chris Voss Tactical Empathy & Dealer Negotiation Engine for Swatch Paints",
        "legend": "Chris Voss (Former FBI Lead International Kidnapping Negotiator & Author of 'Never Split the Difference')",
        "description": "Chris Voss Tactical Empathy, Calibrated Questions, Accusation Audits, and Hard Bargaining Framework for Swatch Paints Field Sales.",
        "dept": "01_sales",
        "tag": "chris-voss",
        "purpose": """This skill equips the Swatch Paints Sales Force, Key Account Managers, and ASMs with the tactical negotiation methodologies developed by Chris Voss. It eliminates the destructive habit of "splitting the difference" on dealer margins, giving away margin-diluting cash discounts, or surrendering to high-pressure dealer tactics.

In the Indian paint distribution industry, dealers are seasoned master negotiators. They constantly use emotional pressure, threats of switching to Asian Paints or Berger, and demands for extended credit or extra cash rebates. Untrained sales officers panic and surrender hard-earned enterprise margin.

The engine's purpose is to:
- Protect product gross margins by transforming adversarial price bargaining into collaborative problem-solving using **Tactical Empathy**.
- Defuse aggressive dealer objections with **Accusation Audits** before the dealer can voice them.
- Neutralize unfair credit demands and price-slashing threats using **Calibrated Questions** ('How am I supposed to do that?').
- Uncover hidden dealer motivations and secret constraints (**Black Swans**) such as cash crunches, hidden brand incentives, or godown space constraints.""",
        "when_to_use": """- A major paint dealer threatens to delist Swatch Paints unless granted an extra 3% cash rebate.
- Negotiating annual stocking agreements, tinting machine placements, or festival stocking commitments.
- Confronting a chronic defaulting dealer who demands new stock while holding 60-day overdue payments.
- Pitching Swatch Rustic or premium emulsions to skeptical dealers who claim 'no one in our mandi buys premium paint.'
- Recovering from deadlocks without surrendering enterprise margin or damaging long-term personal relationships.
- Training field sales officers how to resist customer price ultimatums.""",
        "frameworks": """### 6.1 Tactical Empathy & The Late-Night FM DJ Voice
Tactical empathy is not agreeing with the dealer; it is demonstrating an acute awareness of their world, constraints, and fears. 
- When a dealer is agitated, lower your voice pitch, slow your delivery, and speak with calm, unhurried downward inflection (**The Late-Night FM DJ Voice**).
- This triggers neurochemical calming in the dealer's amygdala, shifting them from fight-or-flight hostility to rational dialogue.

### 6.2 Mirroring & Labeling
- **Mirroring:** Repeat the last 1 to 3 critical words the dealer said with an upward question inflection.
  - *Dealer:* "Tumhare paints me margin nahi bachta aur credit bhi kam dete ho."
  - *Sales Rep:* "Credit bhi kam dete hain?" (Silent pause for 4 seconds).
  - *Dealer:* "Haan, Asian Paints 45 din deta hai aur tum 21 din me paise maangte ho..." (Dealer reveals the real underlying comparison).
- **Labeling:** Validate emotions without accepting blame.
  - "Aisa lagta hai ki aapko lag raha hai Swatch stock karke aapka paisa block ho jayega."
  - "Lagta hai aap purane suppliers ke payment commitments se kaafi dabav me hain."

### 6.3 The Accusation Audit
Before the dealer can attack your pricing or brand age, preemptively state every negative thought they are holding:
- *"Sethji, is meeting ke pehle main aapse saaf kehna chahta hoon: aapko shayad lagega ki Swatch ek nayi company hai jo market me Asian Paints ke samne tik nahi payegi. Aapko lagega ki hum aapko fast-moving stock ke bajaye texture bechne aaye hain aur aapka godown bhar denge. Aur aapko yeh bhi lagega ki hum aapko doosre dealers se kam discount offer kar rahe hain..."*
- By airing their accusations first, you pop the emotional balloon, leaving the dealer disarmed.

### 6.4 Calibrated 'How' and 'What' Questions
Never ask "Why" (it triggers defensiveness). Use open-ended questions that force the dealer to solve your mutual problem:
- *"Sethji, agar main aapko bina payment ke 60 din ka credit de doon, toh main factory se raw material procurement kaise ensure karunga?"*
- *"Hum is deal ko aapke aur hamare dono ke liye profitable kaise bana sakte hain?"*
- *"Aapke hisaab se sabse bada risk kya hai agar hum Swatch Rustic ka 1 feature wall display lagayein?"*

### 6.5 The Power of 'No'
Voss proved that pushing for "Yes" makes people suspicious. People feel safe and in control when they say "No."
- Instead of asking: *"Kya aap Swatch ka display lagane ke liye taiyar hain?"* (High friction, triggers fear).
- Ask: *"Kya yeh bilkul galat vichar hoga agar hum Diwali tak aapki shop me ek test display lagayein?"*
- If the dealer says: *"Nahi, test karne me koi dikkat nahi hai."* You have won the agreement.""",
        "decision_algo": """### Step 1: Pre-Negotiation Accusation Audit Preparation
- List the 5 worst accusations the dealer can make about Swatch Paints (High price, unknown brand, strict credit, slow tinting delivery).
- Open the meeting by acknowledging these concerns immediately.

### Step 2: Handle Price Pressure & Margin Demands
- IF dealer demands: "Match Asian Paints' 5% cash scheme or I won't order":
  - DO NOT counter with a lower price.
  - Label: "Aisa lagta hai ki aapko lagta hai hamari product quality unke barabar nahi hai."
  - Calibrated Question: "Main aapki shop ka profit badhana chahta hoon, par main company ka loss karke pricing kaise approve karwa sakta hoon?"

### Step 3: Negotiate via Value Levers, Never Cash
- IF the dealer refuses to move:
  - Offer non-cash trade levers: Free contractor applicator training at their shop, premium demo boards, priority morning logistics, or co-branded flex banners.
  - Keep core product invoice prices untouched.

### Step 4: The 73-38-7 Rule (Body Language & Congruence)
- If the dealer says "Theek hai, karwa do" but leans back with crossed arms, they have not truly agreed (Counterfeit Yes).
- Label the disconnect: "Aapne 'theek hai' kaha, lekin aisa lagta hai ki aapke mann me abhi bhi delivery timeline ko lekar shaq hai?" Uncover the real barrier before writing the order.""",
        "example1": """### Example 1: High-Stakes Overdue Recovery in Kota Mandi
**Situation:** A dominant hardware dealer owed ₹4.8 Lakhs past 55 days (credit limit was 21 days). He threatened: *"Agar naya stock nahi bheja toh purana paisa 3 mahine tak bhool jao. Main doosri brand se utha raha hoon."*
**Voss Methodology Applied:**
- Rep did not get angry or apologize. He used the FM DJ voice.
- *Label:* "Sethji, aisa lagta hai ki aap humse bohot naraz hain aur lagta hai aapko lag raha hai hum aapke business relationship ki izzat nahi karte."
- *Dealer softened:* "Nahi narazgi ki baat nahi hai, par mera Diwali season ka maal ruk jayega agar stock nahi mila."
- *Calibrated Question:* "Sethji, main aapka Diwali season bilkul disturb nahi karna chahta. Lekin jab tak system me 55-day overdue clear nahi hota, main finance team se dispatch authorization kaise generate karwaoon?"
- *Outcome:* The dealer acknowledged the internal rule, paid ₹3.5 Lakhs by RTGS within 4 hours, and agreed to take the new stock on 10-day PDC terms.""",
        "example2": """### Example 2: Placing Swatch Rustic in a Skeptical Dealer Shop
**Situation:** A luxury paint counter in Jaipur rejected Swatch Rustic texture, claiming *"Yahan sirf imported Italian textures chalte hain."*
**Voss Methodology Applied:**
- Rep used an Accusation Audit: *"Bhaiya, aapko lagta hoga ki hum Indian manufacturers Italian luxury finish ka muqabla nahi kar sakte, aur aapki reputation premium clients ke samne kharab ho jayegi."*
- Dealer smiled: *"Sahi pakde ho, mere clients bohot choosy hain."*
- Calibrated Question using No-oriented framing: *"Kya yeh bohot bada nuksan hoga agar hum aapki workshop me ek single panel Italian brand ke bagal me lagakar blind test karein?"*
- Result: Blind test showed Swatch Rustic had superior adhesion and lower odor. Dealer agreed to stock 500 kg for an upcoming Jagatpura villa project.""",
        "failures": [
            ("Splitting the Difference", "Surrendering 2% margin just to close the deal quickly.", "Stand firm on pricing. Trade non-monetary value assets (training, display, priority logistics) instead."),
            ("Chasing 'Yes'", "Pushing the dealer until they say 'Yes' just to get you out of their shop.", "Aim for 'That's Right' or use 'No'-oriented questions that make the client feel protected."),
            ("Why-Question Trap", "Asking 'Aap hume order kyu nahi de rahe?' which provokes hostility.", "Reframe as: 'Aapke hisaab se kaun si cheez hume partnership karne se rok rahi hai?'"),
            ("Surrendering to Bluff Threats", "Panicking when a dealer says 'Main doosra brand rakh lunga.'", "Acknowledge the fear using tactical empathy, then ask: 'Aapke business ke liye wahan shift hone ka total switching cost kya hoga?'")
        ],
        "checklist": [
            "Accusation Audit prepared with the top 4 dealer objections before meeting.",
            "Late-Night FM DJ voice used during emotional or tense moments.",
            "Dealer statements mirrored (repeated last 1-3 words) to dig deeper into real constraints.",
            "Negative emotions labeled accurately ('Lagta hai aapko chinta hai ki...') without apologizing.",
            "Calibrated questions ('How am I supposed to...') used to resist margin cuts.",
            "Zero compromises made on ERP gross margin floor; all concessions are in non-price service levers."
        ]
    },
    "frederick-reichheld-retention-engine": {
        "title": "Fred Reichheld Dealer & Painter Retention & Net Promoter Engine for Swatch Paints",
        "legend": "Fred Reichheld (Bain Fellow, Creator of Net Promoter System & Author of 'The Ultimate Question')",
        "description": "Fred Reichheld Net Promoter Engine (NPS), Dealer Churn Reduction, Painter Loyalty Economics, and Earned Growth Engine for Swatch Paints Sales Department.",
        "dept": "01_sales",
        "tag": "frederick-reichheld",
        "purpose": """This skill equips Swatch Paints with Fred Reichheld's disciplines of customer loyalty economics, the Net Promoter System (NPS), and Earned Growth metrics. It ends the costly obsession with "buying" market share through expensive promotions while existing dealers silently churn out the back door.

In the Indian paint trade, acquiring a new dealer or converting a competitor's master painter costs 6 to 8 times more than retaining an existing one. Yet, companies ignore active dealers, deliver late tinting orders, generate messy billing credit notes, and wonder why dealers switch to rivals after 12 months.

The engine's purpose is to:
- Measure and maximize **Net Promoter Score (NPS)** across both key customer groups: retail paint dealers and master painting contractors.
- Calculate the true **Economics of Retention**: quantifying how a 5% increase in dealer retention boosts enterprise net profit by 35%+.
- Eliminate **Bad Profits**: profits extracted from unfair penalty interest, delayed scheme payouts, or hidden freight deductions that turn dealers into detractors.
- Drive **Earned Growth**: measuring revenue generated purely by repeat orders and genuine dealer-to-dealer word-of-mouth referrals without advertising spend.""",
        "when_to_use": """- A territory is experiencing dealer turnover (>15% of registered dealers ordering zero stock over 90 days).
- Implementing the quarterly Swatch Paints Dealer & Painter Net Promoter Score (NPS) audit.
- Diagnosing why dealers complain about scheme payouts, credit notes, or tinting machine reliability.
- Designing the Master Painter Loyalty Program (Swatch Ustaad / Swatch Bandhu).
- Calculating customer lifetime value (CLV) to justify investments in dedicated technical support or faster logistics.
- Root-cause auditing when a high-billing dealer counter defects to a competitor.""",
        "frameworks": """### 6.1 The Net Promoter Question & Classification
Ask every dealer and registered contractor quarterly:
*"On a scale of 0 to 10, how likely are you to recommend Swatch Paints to a fellow hardware dealer or master painter?"*

- **Promoters (Score 9-10):** Enthusiastic brand advocates. They stock your full line, pay on time, and recommend Swatch to other painters.
- **Passives (Score 7-8):** Satisfied but unenthusiastic. Vulnerable to competitor schemes, discount wars, and temporary credit offers.
- **Detractors (Score 0-6):** Unhappy partners trapped by outstanding dues or dead stock. They badmouth your finish and coverage to local painters.

```
NPS = % Promoters - % Detractors (Expressed as a score from -100 to +100)
```
Target for Swatch Paints: **NPS > +55 across dealers and > +70 across painters.**

### 6.2 Good Profits vs. Bad Profits
- **Good Profits:** Earned with customer cooperation. The dealer buys Swatch Rustic because painters demand it, makes a healthy margin, and pays joyfully.
- **Bad Profits:** Extracted at the customer's expense. Examples: charging the dealer for tinting canister damage that was caused by depot transit; delaying quarterly rebate credit notes by 90 days to manipulate cash float. Bad profits breed virulent detractors.

### 6.3 The Earned Growth Rate (EGR)
Reichheld's gold standard metric that replaces accounting vanity:
```
Earned Growth = (Net Revenue Retention from Existing Dealers) + (New Revenue from Word-of-Mouth Referrals)
```
If your EGR is negative, your business is shrinking regardless of how many new counters you force open with promotional cash.""",
        "decision_algo": """### Step 1: Execute Quarterly Inner & Outer Loop NPS
- Survey 100% of 'A' and 'B' tier dealers and active registered painters via automated IVR/WhatsApp.
- Follow up immediately with the **Inner Loop**: Any score <= 6 (Detractor) triggers a mandatory visit by the ASM within 48 hours.

### Step 2: Detractor Root-Cause Resolution
- IF detractor score is caused by **Delayed Scheme Credit Notes**:
  - Auto-credit the verified balance into the dealer's ERP ledger within 24 hours. The Finance Department must treat credit note velocity as a primary customer retention metric.
- IF detractor score is caused by **Batch Inconsistency / Coverage Complaints**:
  - Send the Technical Applicator to the painter's job site within 24 hours. If product fault is verified, replace material 100% at company cost.

### Step 3: Mobilize Promoters for Earned Growth
- Identify all Promoters (Score 9-10).
- Do not just say thank you; request an active referral: *"Sethji, aapke jaise 2 honest hardware dukaandar kaun hain aas-pass ki mandi me jinhe hum Swatch se connect karein?"*
- Provide exclusive early-access allocations of seasonal texture batches to Promoters.

### Step 4: De-escalate or Exit Chronic Toxic Detractors
- IF a dealer gives a 0-score due to chronic demands for unauthorized 90-day credit and refuses to pay:
  - Do not bribe them with discounts. Settle accounts cleanly, collect receivables, and exit gracefully (Systematic Abandonment).""",
        "example1": """### Example 1: Closing the Loop with a Hadoti Detractor Dealer
**Situation:** A high-volume dealer in Jhalawar scored a 3 on the quarterly NPS survey. In the previous year, he had billed ₹14 Lakhs. In the last 60 days, his orders dropped to zero.
**Inner Loop Action:**
- ASM visited the shop within 24 hours. He discovered the dealer had a pending claim of ₹24,000 for 12 dented exterior primer buckets that the central depot rejected 4 months prior.
- The dealer felt disrespected: *"Paisa chota hai, par tumhare depot manager ne mujhe chor samjha."*
- **Resolution:** ASM immediately inspected the godown, verified the transport dent damage, and had the credit note issued on the spot from the ERP mobile portal.
- **Result:** Dealer smiled, paid his pending balance of ₹1.2 Lakhs, placed a ₹3.5 Lakh pre-Diwali stocking order, and upgraded his score to a 9.""",
        "example2": """### Example 2: Turning Master Painter Net Promoter Score into Monopoly Pull
**Situation:** In Kota, 40 painters were surveyed. NPS was +12 (low). The primary complaint was that the competitor's loyalty tokens gave instant Paytm cash, whereas Swatch points had to be redeemed physically at the distributor's desk.
**Reichheld Fix:**
- Overhauled the Swatch Ustaad Painter App to enable instant UPI transfer within 60 seconds of QR token scanning on paint bucket lids.
- Added a direct WhatsApp hotline for technical coverage advice.
- Within 90 days, painter NPS jumped to +74. Over 28 painters switched from local distemper to Swatch Shine Emulsion, pulling ₹9 Lakhs in secondary billing through authorized dealers.""",
        "failures": [
            ("Score Gaming", "Sales reps pressuring dealers: 'Sir please 10 de dena nahi toh meri naukri chali jayegi.'", "Automate surveys via independent third-party WhatsApp bot; disqualify rep bonuses if survey coercion is detected."),
            ("Ignoring the Inner Loop", "Collecting NPS survey data and dumping it in an executive presentation without calling back detractors.", "Strict rule: 100% of detractors must receive a personal visit from the ASM within 48 hours."),
            ("Addiction to Bad Profits", "Generating short-term cash by deducting petty freight or penalizing dealers for minor errors.", "Abolish all hidden penalties. Transparency is the bedrock of customer retention."),
            ("Neglecting the Passives", "Ignoring scores of 7 and 8 because they aren't complaining.", "Passives are one competitor discount away from churning; engage them with product training and exclusive bundle value.")
        ],
        "checklist": [
            "Quarterly NPS survey executed across all active dealers and registered painters.",
            "NPS score calculated using verified Promoters minus Detractors formula.",
            "100% of Detractors (<6) contacted by ASM within 48 hours for root-cause resolution.",
            "Earned Growth Rate (EGR) calculated alongside accounting revenue.",
            "Zero 'Bad Profits' (hidden deductions, delayed rebates) permitted in billing operations.",
            "Painter loyalty token redemptions automated to instant settlement."
        ]
    },
    "joe-girard-relationship-engine": {
        "title": "Joe Girard Long-Term Relationship & Rule of 250 Engine for Swatch Paints",
        "legend": "Joe Girard (Guinness World Record Holder: 'World's Greatest Salesman' & Author of 'How to Sell Anything to Anybody')",
        "description": "Joe Girard Rule of 250, Relational Selling, Customer Record Systems, and Personal Loyalty Moats for Swatch Paints Sales Department.",
        "dept": "01_sales",
        "tag": "joe-girard",
        "purpose": """This skill equips the Swatch Paints Field Force with Joe Girard’s legendary discipline of relationship selling, the **Rule of 250**, systematic personal record-keeping, and continuous appreciation touches.

In the Indian hardware and paint industry, commerce is fundamentally social. Dealers and painting contractors do not make buying decisions purely on technical TDS data or 1% price variations; they buy from sales executives who respect them, remember their families, show genuine appreciation, and stand by them during crises.

The engine's purpose is to:
- Institutionalize Girard’s **Rule of 250**: recognizing that every single painter or dealer knows at least 250 people whose opinions they influence.
- Implement Girard’s **Customer Record Card System** within the Swatch SFA app: tracking personal milestones, birthdays, children's weddings, and personal preferences.
- Execute systematic, authentic **Monthly Touchpoints**: sending personalized festival greetings, appreciation notes, and milestone acknowledgments without asking for an order.
- Turn satisfied painters and dealers into a high-octane **Birddog Referral Network** that continuously funnels new accounts to Swatch Paints.""",
        "when_to_use": """- Building long-term personal moats against aggressive multi-national paint competitors who try to poach Swatch dealers with massive ad budgets.
- Onboarding new hardware dealers and building high-trust bonds within the first 90 days.
- Managing master painting contractors and applicators who control large commercial and residential painting decisions.
- Recovering a neglected dealer account that has drifted away due to cold, impersonal corporate treatment.
- Structuring the seasonal festival gifting and relationship calendar (Diwali, Holi, New Year, Eid, Raksha Bandhan).
- Training junior field officers who mistakenly believe that sales is about slick talking rather than genuine caring.""",
        "frameworks": """### 6.1 The Rule of 250
Girard discovered that on average, an individual invites 250 people to their wedding and 250 people attend their funeral. 
- In the Indian paint ecosystem: A single Master Painter (Thekedaar) has 10 to 15 junior painters in his crew, buys from 3 hardware dealers, interacts with 50 homeowners a year, and speaks to dozens of fellow contractors at tea stalls and union meets.
- If you treat one painter with disrespect or shortchange his loyalty points, you do not lose 1 customer; you poison the minds of **250 potential buyers**.
- Conversely, make one painter feel like a king, and his word-of-mouth recommendation will win you an entire neighborhood.

### 6.2 Girard's Tool: The Living Customer Record
A sales rep must never rely on memory. For every dealer and master contractor, the SFA system must record:
- Spouse and children's names, birthdays, and educational milestones.
- Personal hobbies, favorite local sweets (Mithai), tea preferences, and religious festivals observed.
- Date of first order with Swatch Paints and annual anniversary.
- Specific personal challenges (health, construction of new home, shop renovation).

### 6.3 Girard's Direct Touch System ("I Like You")
Girard famously sent a greeting card every month to every customer on his list with a simple, genuine message: *"I like you. Happy Diwali / Happy New Year / Happy Birthday."*
- Rule: 80% of relationship touches must contain **NO sales pitch, NO order request, and NO product catalog**.
- Pure, unadulterated appreciation builds a psychological obligation of loyalty that no competitor's discount scheme can shatter.

### 6.4 The Birddog Referral Engine
Turn existing customers and non-competing trade allies into paid ambassadors ("Birddogs"):
- Cement suppliers, tile dealers, local plumbers, electric hardware shops, and retired painters.
- When they alert a Swatch rep to a new construction site or school repaint job, reward them promptly with a verified finder's fee or branded gift.""",
        "decision_algo": """### Step 1: Initialize the Girard Customer Dossier
- Mandatory on first onboarding visit: Rep must capture dealer/contractor family details and milestone dates.
- Store data in the secure CRM master, not on personal scrap paper.

### Step 2: Calendarized Appreciation Cadence
- Automate milestone triggers in the mobile SFA:
  - Rep receives notification 3 days prior to dealer's birthday or shop anniversary.
  - Mandatory action: Hand-deliver a box of premium local sweets or a handwritten note from the CEO office.

### Step 3: Enforce the "No-Pitch" Touchpoint Rule
- Send at least 1 personalized appreciation message every month.
- IF a rep includes a sales pitch ("Sethji, target bacha hai maal le lo") during a birthday or festival call:
  - Flag as a Girard Principle Violation. The call must remain 100% focused on honoring the human being.

### Step 4: Birddog Activation
- Maintain an active network of at least 15 local trade allies per territory.
- Pay referral rewards within 48 hours of order delivery. Never make a Birddog chase their reward.""",
        "example1": """### Example 1: Winning Back a Defected Dealer in Bundi
**Situation:** A top dealer in Bundi stopped stocking Swatch 8 months ago after a heated argument with a former sales officer over freight charges. Competitors dominated his shelves.
**Girard Strategy Applied:**
- New TSI visited the shop not to sell paint, but to apologize for the past friction.
- Noticed a portrait of the dealer's father with a garland. Discovered the father had founded the shop 40 years ago and his death anniversary was coming up.
- On the anniversary, the TSI sent a framed calligraphic tribute honoring the founder's contribution to Bundi's merchant community, signed by Ashutosh Sharma Sir.
- The dealer was moved to tears: *"Badi-badi companiyan aayi par kisi ne mere pitaji ki izzat nahi ki."*
- **Outcome:** Dealer cleared his old shelf space and re-ordered the entire Swatch interior and exterior emulsion lineup, giving Swatch 60% counter share.""",
        "example2": """### Example 2: The Master Painter's Wedding Gift in Bhilwara
**Situation:** A dominant painting contractor in Bhilwara (controlling 25 luxury residential sites per year) was preparing for his daughter's wedding.
**Girard Strategy Applied:**
- The ASM did not send a generic bulk diary. The company sponsored the high-grade decorative lighting and paint for the contractor's ancestral home for the wedding.
- The ASM attended the ceremony in person with a traditional Rajasthani safa and felicitated the family.
- **Outcome:** The master contractor declared Swatch as his exclusive coating partner across all 25 sites, generating over ₹22 Lakhs in secondary paint sales over the following 12 months.""",
        "failures": [
            ("Transactional Myopia", "Visiting dealers only when quotas are due on the 28th of the month.", "Mandate routine relationship calls during the first 10 days of the month with zero order requests."),
            ("Failing the Rule of 250", "Rudely dismissing a small 2-room house painter because his order is only ₹3,000.", "Treat every painter with supreme dignity; his network includes hundreds of fellow applicators."),
            ("Automated Spam Impersonation", "Sending generic SMS blast messages: 'Dear Customer, Happy Diwali from Swatch.'", "Girard requires personalized, human communication: handwritten notes, physical visits, or real phone calls."),
            ("Delaying Birddog Payouts", "Making referral sources wait months for their promised commission.", "Settle referral rewards within 48 hours to maintain high motivation and trust.")
        ],
        "checklist": [
            "Every active dealer and master contractor has a complete personal profile in the CRM.",
            "Key personal dates (birthdays, anniversaries) trigger proactive automated reminders.",
            "Monthly appreciation touchpoints executed with zero sales pitch attached.",
            "Rule of 250 trained into every sales representative during onboarding.",
            "Birddog trade referral network established and rewarded promptly.",
            "Festival relationship calendar planned 30 days in advance with high-quality physical gifts."
        ]
    },
    "neil-rackham-spin-selling-engine": {
        "title": "Neil Rackham SPIN Selling & Complex B2B Project Engine for Swatch Paints",
        "legend": "Neil Rackham (Renowned Sales Researcher & Author of 'SPIN Selling')",
        "description": "Neil Rackham Situation-Problem-Implication-Need Payoff (SPIN) Questioning Framework for Swatch Paints Commercial & Project Sales.",
        "dept": "01_sales",
        "tag": "neil-rackham",
        "purpose": """This skill equips the Swatch Paints Project Sales Team, Key Account Managers, and Technical Sales Engineers with Neil Rackham’s research-backed **SPIN Selling Model**. It replaces shallow product-pitching with consultative diagnostic inquiries for high-ticket commercial painting contracts, residential townships, government tenders, and major industrial coating projects.

In large-scale commercial sales, traditional closing techniques ("hard closes", feature pitching, aggressive persuasion) backfire completely. Builders, project management consultants (PMCs), architects, and hotel developers are sophisticated buyers who resist high-pressure sales pitches.

The engine's purpose is to:
- Move sales reps away from premature product pitching to systematic problem diagnosis.
- Uncover implicit customer dissatisfaction and magnify it into **Explicit Urgency** using **Implication Questions**.
- Enable the client to articulate the value of Swatch Paints themselves through **Need-Payoff Questions**.
- Protect enterprise pricing on multi-thousand-litre project contracts by selling total lifecycle durability and maintenance reduction rather than competing on the cheapest price per litre.""",
        "when_to_use": """- Pitching Swatch Paints and Swatch Rustic to real estate builders, commercial developers, and hotel chains.
- Meeting with architects, interior designers, and project management consultants (PMCs) to get Swatch specified in project tenders.
- Bidding for institutional painting contracts (hospitals, educational institutes, industrial factories).
- A high-value project client is stalling or demanding a 15% price cut to match cheap regional brands.
- Diagnosing why a sales engineer is losing large deals despite giving dozens of product demonstrations.
- Transitioning the sales culture from transactional commodity peddling to high-value consultative solution selling.""",
        "frameworks": """### 6.1 The Four Stages of a Complex Sales Call
Rackham proved that successful high-value sales calls follow 4 sequential stages:
1. **Preliminaries:** Establishing rapport and professional credibility without lengthy casual chatter.
2. **Investigating (Most Critical):** Asking questions to uncover customer needs. Top performers ask 4x more questions than average reps.
3. **Demonstrating Capability:** Showing how your solution solves the *explicit* problems identified in Stage 2.
4. **Obtaining Commitment:** Securing an advance (e.g., test mock-up on Tower B, architect specification sign-off), not just a closed contract.

### 6.2 The SPIN Questioning Sequence
```
[SITUATION QUESTIONS] --> Establish operational context (keep minimal)
         |
[PROBLEM QUESTIONS]   --> Uncover implicit pain, dissatisfaction, defects
         |
[IMPLICATION QUESTIONS]--> Magnify consequences of inaction (financial/reputational cost)
         |
[NEED-PAYOFF QUESTIONS]--> Guide client to voice the benefits of your solution
```

#### Detailed SPIN Matrix for Indian Paint Projects:
- **Situation (S):**
  - "Sir, currently which coating system are you using on the exterior facade of Phase 1?"
  - "What is your typical repainting cycle for these commercial towers?"
  - *(Caution: Keep S-questions under 15% of the conversation to avoid boring the buyer).*
- **Problem (P):**
  - "How often do you face efflorescence (shora/namak) or peeling paint on the north-facing walls after the monsoon?"
  - "What difficulties do your painting contractors report regarding drying time and spreading rate?"
  - "Where are your current finishes falling short of the architect’s aesthetic vision?"
- **Implication (I - The Core Leverage):**
  - "When exterior paint flakes within 18 months, how does that impact the builder’s brand reputation with high-end flat buyers?"
  - "What does it cost you in scaffolding, labor, and warranty disputes when you have to repaint a 10-story tower prematurely?"
  - "If moisture seepage penetrates through hairline cracks in the substrate, could that lead to structural reinforcement corrosion and interior drywall damage?"
- **Need-Payoff (N - The Solution):**
  - "If we could provide a flexible elastomeric texture coating that bridges hairline cracks up to 2mm, how would that protect your project warranty?"
  - "How much money would you save on scaffolding and scaffolding permits if the coating life was extended from 3 years to 7 years?"
  - "Would having direct on-site technical testing from our lab help your PMC approve the finishing sign-off faster?""",
        "decision_algo": """### Step 1: Pre-Call SPIN Planning
- Before walking into the builder's or architect's office, write down at least:
  - 3 Problem Questions targeting substrate failure, moisture, or color fading.
  - 4 Implication Questions tying coating failure to severe financial and reputational losses.
  - 3 Need-Payoff Questions highlighting the economic value of durability and Swatch lab backing.

### Step 2: Diagnostic Execution
- Resist the urge to open the product catalog or show sample boxes during the first 20 minutes.
- Listen actively; take written notes when the client describes operational headaches.

### Step 3: Magnify the Pain Before Pitching
- IF the client mentions a small problem ("Kabhi-kabhi hairline cracks aate hain"):
  - DO NOT jump in with: "Humara Swatch Rustic le lo!"
  - Apply Implication Questions immediately: "Uss hairline crack se barish me plaster me seepage hoti hai? Uska interior flat handover pe kya asar padta hai?"
  - Let the client verbalize the true multi-lakh financial risk.

### Step 4: Secure an Advance, Not a Premature Close
- In complex sales, closing on call 1 is rare.
- Secure a concrete **Advance**: An agreement to coat a 500 sq ft sample wall on Tower A, followed by joint inspection with the Chief Architect on Thursday.""",
        "example1": """### Example 1: Winning a 12-Tower Township Project in Jaipur
**Situation:** A major real estate developer in Jagatpura was building 600 flats. The purchase manager demanded a price of ₹85/litre for exterior acrylic paint, pitting Swatch against cheap local manufacturers.
**SPIN Methodology Applied:**
- Rep bypassed the purchase clerk and met the Project Director & Chief Engineer.
- *Problem Question:* "Sir, Phase 1 ke exterior balconies me barish ke baad jo moisture patches dikh rahe hain, uske bare me resident association ka kya feedback hai?"
- *Implication Question:* "Agar Phase 2 ke buyers ko handover ke waqt ye dampness patches dikhte hain, toh kya possession delay hoga? Aur har flat ke possession delay pe RERA interest penalty kitni lagti hai?"
- Project Director leaned forward: *"Ek mahine ka delay matlab ₹15 Lakh ka loss aur RERA ka notice."*
- *Need-Payoff Question:* "Agar hum aapko ek breathable, silicone-enhanced water-repellent primer aur elastomeric finish provide karein jo moisture entrapment ko roke aur 5-year guarantee de, toh kya woh RERA risk aur repainting cost ko eliminate karega?"
- **Result:** The developer rejected the cheap ₹85 paint and awarded Swatch the entire 12-tower contract at standard commercial pricing with 32% gross margin.""",
        "example2": """### Example 2: Specifying Swatch Rustic with a Leading Udaipur Heritage Architect
**Situation:** A high-profile architect specializing in boutique heritage resorts refused to meet paint reps, calling them "pamphlet droppers."
**SPIN Methodology Applied:**
- Rep sent a brief note asking a diagnostic question about stone texture durability in humid lake environments.
- During the meeting, asked: *"Jab natural sandstone carving pe algae aur black fungus jamta hai, toh conservation team ko surface restore karne me kitna manual effort lagta hai?"*
- Followed with Implication: *"Agar resort facade monsoon ke turant baad dull dikhne lage, toh luxury guest reviews aur per-night room rates pe kya impact aata hai?"*
- Presented Swatch Rustic not as paint, but as an advanced breathable stone-textured barrier engineered for high humidity.
- **Result:** Architect specified Swatch Rustic as the mandatory standard for two 5-star resort projects in Kumbhalgarh and Udaipur.""",
        "failures": [
            ("Premature Pitching", "Pulling out shade cards and talking about resin quality in the first 5 minutes.", "Strict rule: No product presentations until the client has explicitly acknowledged the pain and its cost."),
            ("Situation Question Overload", "Interrogating the buyer with 20 basic factual questions they could read online.", "Research the project online beforehand; ask only high-impact Problem and Implication questions."),
            ("Handling Objections with Arguments", "Arguing when the client says 'Aapka paint mehenga hai.'", "Use Implication to demonstrate that cheap paint costs 3x more in labor, scaffolding, and frequent repainting."),
            ("Accepting Continuations as Advances", "Leaving the meeting satisfied when the client says 'Baad me dekhenge' (Continuation).", "Never leave without a firm Advance: scheduled site demo, architect review date, or sample sign-off.")
        ],
        "checklist": [
            "Pre-call plan contains at least 3 Problem, 4 Implication, and 3 Need-Payoff questions.",
            "Client spoke for at least 65% of the meeting duration.",
            "Implication questions quantified the hidden financial and reputational cost of coating failure.",
            "Product features were introduced strictly as direct answers to client-stated needs.",
            "Meeting ended with an Advance (concrete forward action with a deadline) rather than vague pleasantries.",
            "Pricing anchored on total lifecycle cost savings rather than price per litre."
        ]
    },
    "ram-charan-execution-engine": {
        "title": "Ram Charan Execution Discipline & Cash-to-Cash Engine for Swatch Paints",
        "legend": "Ram Charan (World-Renowned Business Advisor & Co-Author of 'Execution' and 'What the CEO Wants You to Know')",
        "description": "Ram Charan Execution Discipline, People-Strategy-Operations Linkage, Working Capital Velocity, and Cash-to-Cash Cycle Engine for Swatch Paints Sales Department.",
        "dept": "01_sales",
        "tag": "ram-charan",
        "purpose": """This skill equips the Swatch Paints Executive Team, Sales Leadership, and Territory Managers with Ram Charan’s practical business fundamentals: the linkage of the **Three Core Processes (People, Strategy, Operations)**, intense operational follow-through, and ruthless focus on **Cash Velocity & Working Capital Return**.

In Indian manufacturing enterprises, strategies rarely fail because of poor vision; they fail because of broken execution. Sales executives agree to lofty annual targets in boardroom conferences, but down in the field, no one follows up on weekly milestones, the wrong people occupy critical territory roles, and revenue is tied up in uncollectible dealer receivables.

The engine's purpose is to:
- Connect the Sales Strategy directly to field operational reviews and specific human capabilities.
- Master the **Cash-to-Cash Cycle**: ensuring that sales are never celebrated until cash is banked in the company treasury.
- Institute Charan's **Robust Dialogue**: replacing defensive corporate sugar-coating with candid, intellectual honesty during operational performance reviews.
- Track the fundamental business mechanics of a paint dealership (Gross Margin Return on Inventory - GMROI, inventory turnover, and velocity) so reps talk the language of real business owners.""",
        "when_to_use": """- A strategic sales plan is falling behind schedule and closing the execution gap is urgent.
- Conducting monthly or quarterly Business Review Meetings (BRMs) across sales territories.
- Aligning hiring and promotion decisions with actual execution capability rather than educational pedigree or smooth talking.
- Dealer outstandings are rising and the Cash-to-Cash conversion cycle is lengthening.
- Coaching sales reps how to have commercial business discussions with smart Marwari and Gujarati hardware merchants.
- Breaking down silos between the Sales team (pushing dispatches) and Finance/Credit control (demanding collections).""",
        "frameworks": """### 6.1 The Three Core Processes of Execution
Execution requires seamless synchronization of three distinct processes:
1. **The People Process:** Placing the right people in the right jobs based on their past execution track record, not tenure. If a territory has a tough recovery challenge, assign a decisive, gritty operational leader, not an academic strategist.
2. **The Strategy Process:** Defining "How" we will win in specific geographies. Strategy must be built by the field leaders who execute it, not external consultants.
3. **The Operations Process:** Translating strategy into 30-day operating sprints with clear trade-offs, resource allocation, and contingency plans.

### 6.2 What the CEO Wants You to Know: The Business Engine
Every paint dealership and every branch office operates on 4 universal economic principles:
```
1. Cash Generation: Is cash coming in faster than it is going out?
2. Return on Capital (ROIC): Are assets (tinting machines, godown space, delivery vans) generating adequate profit?
3. Growth: Is market share expanding with solvent, paying customers?
4. Customers: Are we retaining our most profitable dealer partners?
```
A Swatch sales rep must view a dealer not as a target customer, but as a business partner whose **Cash-to-Cash Velocity** the rep must help accelerate.

### 6.3 Robust Dialogue & Follow-Through
Charan defines the culture of execution through two non-negotiable disciplines:
- **Robust Dialogue:** Candor, informal inquiry, and psychological safety where problems are exposed immediately without fear of blame. Never accept vague excuses ("Market me mandee hai"). Ask: "Specifically which 5 dealers stopped buying and what is our 72-hour counter-measure?"
- **Relentless Follow-Through:** An agreement without a named owner, specific milestone, and 7-day review rhythm is merely a wish. Every meeting ends with an explicit Execution Contract.""",
        "decision_algo": """### Step 1: Link People to Strategic Challenges
- Audit the territory: Is the primary challenge opening new accounts (Requires a Hunter), recovering bad debt (Requires a Tough Disciplined Operator), or expanding luxury texture lines (Requires an Influencer/Consultant)?
- Assign sales personnel strictly based on matching demonstrated strengths to the specific territory challenge.

### Step 2: The Cash-to-Cash Operating Discipline
- Primary invoices must never be counted as completed sales in sales meetings.
- Score performance on **Cash Collected Net of Margin**.
- IF a dealer's Cash-to-Cash cycle exceeds 35 days:
  - Rep must conduct a Dealer Stock Audit: Is slow-moving inventory blocking the dealer's working capital?
  - Rebalance the dealer's stock mix before pushing any new orders.

### Step 3: Conduct High-Velocity Monthly Reviews
- Ban 50-slide PowerPoint presentations.
- Review must focus on 3 operational sheets:
  1. Cash collected vs. target.
  2. Inventory turnover at dealer counters.
  3. Action item follow-through status from the last 15-day sprint.

### Step 4: Follow-Through Closure
- Log every decision in the central ERP Execution Ledger with:
  - Exact Task.
  - Single Owner (No shared ownership).
  - Verifiable Target Date.
  - Automated reminder trigger 48 hours prior to deadline.""",
        "example1": """### Example 1: Rescuing the Bhilwara Territory Execution Gap
**Situation:** Bhilwara missed revenue targets for three consecutive quarters. The RSM blamed "sluggish construction demand."
**Charan Execution Audit Applied:**
- *People Process:* The territory was managed by a quiet administrative coordinator who spent 80% of his time in the branch depot processing orders rather than visiting dealers.
- *Robust Dialogue:* At the monthly review, the CEO asked: "If demand is sluggish, why did our main rival add 14 new tinting machines in Bhilwara city during the same period?" The excuse collapsed.
- *Action:* Transferred the coordinator to depot logistics. Promoted a hungry, field-tested TSI from Kota to lead Bhilwara.
- *Operating Rhythm:* Instituted weekly Tuesday morning 20-minute operating huddles focused strictly on new counter activations and overdue recovery.
- **Outcome:** Added 19 new active counters within 90 days; revenue grew by 52%.""",
        "example2": """### Example 2: Accelerating Dealer Working Capital in Bikaner
**Situation:** A high-potential dealer in Bikaner was stuck at ₹2 Lakhs monthly turnover and refused to buy more paint, citing lack of working capital.
**Charan Business Engine Applied:**
- Rep sat with the dealer and calculated his GMROI (Gross Margin Return on Inventory).
- Found that ₹6 Lakhs of the dealer's capital was trapped in slow-moving dark-shade synthetic enamel from a rival brand that had been gathering dust for 11 months.
- Helped the dealer run a clearance promotion to painters to liquidate the dead stock at cost, generating ₹4.5 Lakhs in liquid cash.
- Re-invested that cash into fast-turning Swatch Interior Emulsion and Swatch Rustic samples (turning every 18 days).
- **Outcome:** The dealer's monthly Swatch turnover tripled to ₹6.5 Lakhs with zero additional bank borrowing.""",
        "failures": [
            ("The Strategy-Execution Chasm", "Drafting grand annual business plans that nobody reads after January.", "Break strategic goals into 30-day operating sprints with weekly milestone accountability."),
            ("Mismatched People", "Keeping a non-performing relative or loyal employee in a critical commercial territory.", "Place people based on demonstrated execution competence; coach or reassign quickly if misaligned."),
            ("Celebrating Uncollected Revenue", "Giving sales bonuses on invoiced primary sales while receivables rot past 60 days.", "Tie sales recognition strictly to banked cash collections and net margin integrity."),
            ("Vague Follow-Through", "Ending meetings with 'We should improve dealer coverage' without assigning names and dates.", "Charan Rule: Every decision must have One Name, One Date, and One Measurable Milestone.")
        ],
        "checklist": [
            "Territory assignments match specific personnel competencies to territory market realities.",
            "Monthly operating reviews practice robust dialogue (intellectual honesty, zero corporate fluff).",
            "Sales performance scored on Cash Collected and Working Capital Velocity, not just billing.",
            "Dealer inventory turnover (GMROI) monitored to ensure healthy dealer balance sheets.",
            "Execution Contract logged with Single Owner and Strict Deadlines for every action item.",
            "Zero tolerance for unaddressed execution bottlenecks across all 8 territories."
        ]
    }
}

def generate_skill_content(name, data):
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
        f"*{data['legend']} — Operationalized for Swatch Paints Enterprise Architecture in the Indian Paint Industry.*",
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
        "Before invoking this engine, collect the following real-time inputs. Zero static assumptions or hardcoded pricing lists are permitted.",
        "",
        "### 4.1 Field & Operational Data Inputs",
        "",
        "| Input | Why It Matters | Live System Source |",
        "|---|---|---|",
        "| Target Account / Territory | Identifies the geographic and commercial context | Sales Territory Master |",
        "| Historical Off-Take & Velocity | Establishes baseline run-rate and seasonal cycles | Live ERP Sales Ledger |",
        "| Outstanding Ledger Balance | Prevents bad debt exposure and margin leakage | Live ERP Accounts Receivable |",
        "| Competitor Channel Schemes | Understands rival switching incentives | Field Intelligence Network |",
        "",
        "### 4.2 Financial & Commercial Guardrails",
        "",
        "| Guardrail | Enforcement Rule | Authority |",
        "|---|---|---|",
        "| Gross Margin Floor | Never breach the minimum product margin floor | Finance & Costing Dept |",
        "| Credit Period Limit | Hard ceiling on open credit days (strictly enforced) | Credit Control Policy |",
        "| Live ERP Dynamic Pricing | All baseline prices pulled dynamically via live query | Live ERP Database |",
        "",
        "---",
        "",
        "## 5. DIAGNOSTIC QUESTIONS",
        "",
        f"Apply these 10 diagnostic inquiries before taking operational action under the {name} framework:",
        "",
        "1. What is the fundamental business bottleneck we are solving for right now?",
        "2. Does the proposed action create real, lasting economic value for both Swatch Paints and our channel partner?",
        "3. What are the leading operational indicators that will prove whether this initiative is succeeding?",
        "4. How does this decision impact our working capital velocity and cash-to-cash cycle?",
        "5. Are the right people with the right capabilities assigned to own execution?",
        "6. What non-monetary value assets (training, speed, quality, brand trust) can we leverage instead of cutting price?",
        "7. What is the worst-case failure mode, and what guardrails prevent catastrophic downside?",
        "8. Are we confusing busy activity with high-leverage business achievement?",
        "9. What specific operational friction or waste can we eliminate from this workflow immediately?",
        "10. Who has single-point accountability for the outcome, and what is the exact review cadence?",
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
        "Every strategic plan, operating memo, or territory directive produced under this skill must follow this standardized schema:",
        "",
        "```markdown",
        f"# Swatch Paints Executive Operating Directive: {data['title']}",
        "",
        "### 1. Executive Summary & Objective",
        "- **Target Territory / Entity:** [Territory / Counter / Project]",
        "- **Lead Executive:** [Designation & Name]",
        "- **Timeline:** [Start Date – Milestone Date]",
        "- **Primary Objective:** [Single quantified statement of target outcome]",
        "",
        "### 2. Operational Action Plan",
        "- **Core Diagnostic Findings:** [Summary of root causes uncovered]",
        "- **High-Leverage Interventions:** [Specific actions ordered by impact]",
        "- **Resource Allocation:** [Budget / Materials / Personnel required]",
        "",
        "### 3. Financial & Risk Guardrails",
        "- **Minimum Contribution Margin:** [Verified via live ERP query]",
        "- **Working Capital / Credit Exposure:** [Maximum allowable risk floor]",
        "- **Fallback Contingency:** [Pre-agreed rollback trigger]",
        "",
        "### 4. Governance & Cadence",
        "- **Weekly Review Cadence:** [Day, Time, Attendees]",
        "- **Leading Operational Metric:** [Daily / Weekly milestone]",
        "- **Lagging Financial Metric:** [Monthly cash / margin milestone]",
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
        "Watch for these recurring administrative and operational failure modes:",
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
        f"**CEO Directive:** At Swatch Paints, management science is not an academic theory; it is our operational weapon. Every executive and field sales officer is expected to embody the core principles of {data['legend']}, driving uncompromising execution, protecting cash flow, and building unbreakable bonds of trust with our dealers and painters."
    ])
    return "\n".join(sections)

def main():
    for name, data in SALES_SKILLS.items():
        content = generate_skill_content(name, data)
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
