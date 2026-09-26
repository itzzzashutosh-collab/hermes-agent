import os

WORKSPACE_DIR = r"d:\Sharma Industries Erp Software\hermes-agent"
HERMES_DIR = r"C:\Users\itzzz\AppData\Local\hermes"

FIN_SCM_SKILLS = {
    # === 03_FINANCE_GST ===
    "adam-smith-kautilya-gst-compliance-engine": {
        "title": "Adam Smith & Kautilya GST Compliance, ITC Reconciliation & Treasury Engine for Swatch Paints",
        "legend": "Adam Smith (Wealth of Nations) & Kautilya (Chanakya - Author of Arthashastra)",
        "description": "Adam Smith Canons of Taxation & Kautilya Treasury Governance Engine for GST Input Tax Credit (ITC) Reconciliation, E-Invoicing, and Tax Compliance at Swatch Paints.",
        "dept": "03_finance_gst",
        "tag": "adam-smith-kautilya",
        "purpose": """This skill equips the Swatch Paints Finance, Accounts, and Taxation departments with Adam Smith’s classical **Canons of Taxation (Certainty, Convenience, Economy, Equality)** combined with Kautilya’s statecraft on **Treasury Governance (Kosha Mulo Danda)** and anti-leakage vigilance.

In the Indian paint industry, GST is not merely an accounting ledger entry; it is a critical driver of working capital liquidity and enterprise survival. With chemical raw materials attracting 18% to 28% GST, any failure in supplier GSTR-1 filings blocks Input Tax Credit (ITC) under Section 16(2)(aa) and Rule 36(4), freezing millions of rupees in unclaimable tax credits. Furthermore, dispatching paint without synchronized e-invoices and e-way bills invites severe interception penalties, vehicle impoundment, and reputational damage.

The engine's purpose is to:
- Enforce automated **GSTR-2B vs. Purchase Register Reconciliation**, ensuring that zero ITC is claimed without matching supplier tax filings.
- Institute a **Vendor GST Compliance Rating System**, withholding payment to defaulting raw material suppliers until their tax invoices appear on the government portal.
- Eliminate transport interception risks through 100% automated **IRN Generation & E-Way Bill Synchronization** directly from the live ERP.
- Maintain an audit-ready, airtight treasury where tax obligations are planned with absolute certainty and zero penalty interest.""",
        "when_to_use": """- Monthly closing of GST returns (GSTR-1, GSTR-3B) and annual audit reconciliation (GSTR-9/9C).
- Onboarding and qualifying new chemical and packaging raw material vendors.
- A raw material supplier has failed to upload invoices to the GST portal, causing an ITC mismatch in GSTR-2B.
- Structuring interstate vs. intrastate dispatch rules from central manufacturing plants to regional depots.
- Auditing transport documentation to eliminate e-way bill expiration or description discrepancy risks.
- Managing departmental audits, GST notices, or scrutiny assessments from state or central tax authorities.""",
        "frameworks": """### 6.1 Adam Smith's Four Canons of Taxation Operationalized
1. **Certainty:** Every tax obligation, rate classification (HSN codes: 3208, 3209, 3214), and ITC eligibility rule must be documented unambiguously. No speculative tax positions.
2. **Convenience:** Tax reporting and e-way bill generation must be seamless for dispatch operators, embedded directly into ERP warehouse workflows.
3. **Economy:** Minimize the cost of compliance and eliminate all non-value-added penalties, late fees, and interest under Section 50.
4. **Equality:** Ensure that tax incidence is borne fairly, with dealer trade schemes structured so that post-sale discounts satisfy Section 15(3)(b) documentation requirements.

### 6.2 Kautilya's Treasury Rule: Kosha Mulo Danda
*"The treasury is the root of the enterprise; all governance flows from financial integrity."*
- **Strict Separation of Custody:** The officer who creates the vendor purchase order cannot approve the invoice for payment, and the officer who processes payment cannot file the GST return.
- **Vigilance on Inward Supplies:** No payment is released to a raw material supplier until three conditions match (**Kautilya's Three Locks**):
  1. Material physically received and weighed at the gate (Gate Pass).
  2. Quality testing certificate approved by QC lab.
  3. Tax invoice reflecting in GSTR-2B with matching HSN and tax amount.

### 6.3 Rule 36(4) & GSTR-2B Automated ITC Matching Logic
```
Total ITC Claimed = Matched Invoices in GSTR-2B (100% Claimable)
  - Ineligible ITC under Section 17(5) (Blocked credits)
  - Invoices appearing in GSTR-2B where vendor cancelled registration
```
Any invoice in the internal purchase register NOT appearing in GSTR-2B is automatically segregated into the "ITC Pending Vendor Action" ledger.""",
        "decision_algo": """### Step 1: Pre-Payment Vendor GST Verification
- Query vendor GSTIN status via automated API check before processing payment.
- IF vendor status is "Suspended" or "Cancelled":
  - HALT payment immediately. Alert Procurement.
- IF invoice is missing from GSTR-2B on the 14th of the subsequent month:
  - Hold the GST component (18%/28%) from the vendor's payment voucher. Release only after invoice reflects in portal.

### Step 2: Automated Dispatch E-Way Bill Validation
- Before a paint delivery truck leaves the factory gate:
  - Verify that E-Way Bill validity duration covers the total transit distance (1 day per 200 km).
  - Cross-check truck registration number with the physical vehicle.

### Step 3: Section 15(3)(b) Trade Discount Compliance
- For dealer turnover discounts and festival schemes:
  - Verify that the scheme agreement was established *prior* to the sale date.
  - Ensure credit notes explicitly reflect the original invoice numbers and reverse the proportionate ITC.""",
        "example1": """### Example 1: Recovering ₹14.5 Lakhs in Blocked ITC from a Pigment Vendor
**Situation:** During quarterly audit, Finance discovered ₹14.5 Lakhs in unclaimable ITC. A major phthalocyanine blue pigment supplier in Gujarat had filed nil returns while issuing tax invoices.
**Kautilya Treasury Protocol Applied:**
- Automatically flagged the vendor in the ERP; placed an immediate freeze on ₹22 Lakhs in pending receivables owed to the vendor for recent shipments.
- Sent formal legal notice demanding GSTR-1 revision under Section 16(2)(aa).
- Faced with payment withholding, the vendor paid their delinquent taxes and revised their return within 72 hours.
- Result: Swatch successfully claimed 100% of the ₹14.5 Lakh ITC in GSTR-3B without paying a single rupee of penalty interest.""",
        "example2": """### Example 2: Eliminating Transit Seizure Risk on Rajasthan Inter-Depot Routes
**Situation:** A consignment of 12 MT of exterior paint traveling from the factory to the Jodhpur depot was detained at a state checkpost due to an expired E-Way bill caused by a truck engine breakdown.
**Smith Convenience & Prevention Fix:**
- Built an automated GPS-tracking alert into the logistics dispatch module: if a vehicle remains stationary for >4 hours while E-Way bill validity has <12 hours remaining, the system alerts the logistics officer to file Part-B extension online.
- Result: Zero transit detentions or tax penalties across 850+ truck movements over the past 12 months.""",
        "failures": [
            ("Claiming ITC on Unfiled Invoices", "Claiming tax credit based on physical paper invoice when vendor hasn't filed GSTR-1.", "Hard system lock: ITC claim strictly restricted to GSTR-2B auto-populated records."),
            ("Missing Section 15(3)(b) Terms", "Issuing post-sale trade discounts without prior agreement, leading to tax disallowance.", "Draft and sign annual dealer scheme policy documents before the fiscal year commences."),
            ("HSN Code Mismatch", "Using wrong HSN code for texture plaster (3214) vs emulsion (3209), attracting incorrect tax rates.", "Enforce ERP SKU creation validation against official GST HSN master tables."),
            ("Delayed Reverse Charge (RCM)", "Failing to pay RCM on GTA (goods transport agency) services, incurring 18% interest.", "Automate monthly RCM liability computation and credit offsetting in the same tax cycle.")
        ],
        "checklist": [
            "100% of claimed ITC reconciled and verified against GSTR-2B monthly.",
            "Vendor GST compliance rating active; payments blocked for delinquent filers.",
            "E-Invoicing (IRN) and E-Way bills generated automatically via ERP API integration.",
            "Three-way matching (Gate Inward, Lab QA, GSTR-2B) enforced for all vendor payouts.",
            "Dealer discount credit notes compliant with Section 15(3)(b) regulations.",
            "Zero penalty interest or late fees incurred across all state and central filings."
        ]
    },
    "chris-voss-credit-collection-engine": {
        "title": "Chris Voss High-Stakes Credit Recovery & Debt Collection Engine for Swatch Paints",
        "legend": "Chris Voss (Former FBI Lead International Kidnapping Negotiator & Author of 'Never Split the Difference')",
        "description": "Chris Voss Tactical Empathy, Calibrated Questions, and Black Swan Discovery for Overdue Accounts Receivable and Debt Collection at Swatch Paints.",
        "dept": "03_finance_gst",
        "tag": "chris-voss-credit",
        "purpose": """This skill equips the Swatch Paints Credit Control, Accounts Receivable, and Field Finance teams with Chris Voss’s high-stakes negotiation methodologies to collect delinquent and overdue dealer receivables without destroying valuable commercial relationships.

In the Indian paint trade, collecting money is the most emotionally fraught operation. Dealers routinely use delaying tactics, feign anger, blame slow retail sales, or threaten to switch brands when pressed for overdue payments. Traditional collection methods (rude legal threats, aggressive shouting, or sheepish pleading) fail: aggressive threats drive dealers into defensive resistance, while passive pleading ensures Swatch gets paid last behind Asian Paints and local cement suppliers.

The engine's purpose is to:
- Recover overdue receivables (DSO > 30 days) using **Tactical Empathy** and calibrated questions that make the dealer voluntarily prioritize Swatch’s payment.
- Defuse debtor hostility and defensive aggression using **Labels** and **Mirrors**.
- Discover hidden cash flow bottlenecks (**Black Swans**) in the dealer's business (e.g., unpaid government contracts, family partition, partner disputes).
- Structure realistic, binding recovery agreements without taking haircuts on legitimate principal balances.""",
        "when_to_use": """- A dealer counter owes overdue balances past 30, 45, or 60 days and ignores standard payment reminders.
- A dealer refuses to clear old debts while demanding fresh stock for peak festival demand.
- Negotiating structured payment plans (PDCs, weekly RTGS milestones) with financially distressed dealers.
- Recovering company-owned tinting machine assets from a defaulting or non-billing counter.
- Overcoming bad check (cheque bounce) situations before initiating formal Section 138 legal proceedings.
- Training credit recovery officers to maintain unshakeable emotional control in hostile confrontations.""",
        "frameworks": """### 6.1 Tactical Empathy in Credit Collection
When a dealer owes money, they feel guilt, fear of insolvency, and defensive pride. 
- Never attack their pride. If you say: *"Aap default kar rahe hain"*, they will close their books and lock you out.
- Instead, voice their internal anxiety: *"Sethji, aisa lagta hai ki market ke payment delays ne aapko kaafi pareshan kar rakha hai, aur aapko lag raha hai hum aapke purane dukaandar hone ki izzat nahi kar rahe."*
- When the debtor feels heard, their emotional defensiveness drops, opening the door to commercial problem-solving.

### 6.2 Calibrated Questions for Collection
Calibrated questions force the debtor to confront the reality of the situation without feeling attacked:
- *"Sethji, agar main credit limit cross hone ke baad bhi factory se naya truck dispatch karwa doon, toh main management ko kya jawab dunga jab auditors account freeze karenge?"*
- *"Hum is purane ₹3.8 Lakh balance ko bina aapki daily shop cash flow disturb kiye kaise clear kar sakte hain?"*
- *"Aapke hisaab se kaun si practical timeline hai jisme aapka rotation wapas normal ho jayega?"*

### 6.3 Finding the Black Swan
A Black Swan is a piece of hidden information that changes everything. In 80% of severe dealer defaults:
- The dealer is not a fraudster; their money is trapped in a specific large project (e.g., a local builder who hasn't paid for 6 months).
- By asking: *"Is delay ke peeche aisi kaun si cheez hai jo hume nahi pata?"*, you uncover the root cause and can help them recover funds from the end-buyer directly.""",
        "decision_algo": """### Step 1: Pre-Call Emotion Audit
- Review dealer ledger: Total balance, overdue days, bounce history.
- Script an Accusation Audit: "Sethji, aap soch rahe honge ki main subah-subah aapka mood kharab karne phone kar raha hoon..."

### Step 2: Diagnostic Conversation Execution
- Use Late-Night FM DJ voice.
- Mirror their complaints: If dealer says "Market bilkul thapp hai", mirror: "Market thapp hai?"
- Uncover the Black Swan: Identify where their cash is currently locked.

### Step 3: Enforce the "No New Paint Without Liquidity" Rule
- IF dealer demands new stock while holding >45 days overdue:
  - DO NOT say "Company policy allows no stock."
  - Ask: "Main naya stock bhejna chahta hoon, lekin main pending invoices ke hote hue finance clearance kaise generate karwaoon?"
  - Structure a 2-for-1 recovery deal: For every ₹1 Lakh of new stock ordered (paid in cash), dealer must pay ₹50,000 toward the old debt.

### Step 4: Secure Firm Milestones with PDCs
- Convert vague promises ("Agley hafte dekh lenge") into explicit commitments:
  - Exact date, exact RTGS amount or signed Cheque.
  - Test commitment with: *"Kya yeh plan realistic hai ya main aapko kisi aisi cheez ke liye commit kar raha hoon jo aap deliver nahi kar payenge?"*""",
        "example1": """### Example 1: Collecting ₹6.2 Lakhs Overdue in Alwar Mandi
**Situation:** A high-volume dealer owed ₹6.2 Lakhs past 75 days. When the sales rep visited, the dealer threw a tantrum, threw a teacup, and shouted: *"Mujhe payment ki baat mat karo, nahi toh sara maal bahar phek dunga."*
**Voss Collection Strategy Applied:**
- Credit manager visited. Did not argue. Spoke in a low, gentle voice.
- *Label:* "Sethji, lagta hai aap humse bohot zyada naraz hain aur lagta hai ki company ke automated reminder messages ne aapko bohot hurt kiya hai."
- *Result:* Dealer’s anger evaporated. He confessed: *"Bhaiya, narazgi nahi hai. Mera ₹18 Lakh ek school building project me phas gaya hai. Main raat ko so nahi pa raha hoon."*
- *Resolution:* Together they drafted a joint tripartite agreement: The school contractor issued a direct payment of ₹6.2 Lakhs to Swatch Paints against their upcoming milestone release.
- Account normalized completely; zero bad debt written off.""",
        "example2": """### Example 2: Resolving a Cheque Bounce without Litigation
**Situation:** A dealer's cheque of ₹2.4 Lakhs bounced due to insufficient funds. The sales rep wanted to immediately file a police complaint and Section 138 case.
**Tactical Intervention:**
- Credit head called the dealer before filing legal papers.
- Asked a 'No'-oriented question: *"Sethji, kya aap chahte hain ki hamara 3 saal ka business relationship courts aur police notices me khatam ho jaye?"*
- Dealer answered: *"Nahi sir, bilkul nahi. Mujhe bas 10 din ka time de do."*
- Offered a face-saving exit: Dealer split the balance into two digital RTGS transfers of ₹1.2 Lakhs spaced 5 days apart. Both cleared successfully on time.""",
        "failures": [
            ("Aggressive Shouting & Insults", "Threatening dealers verbally, causing them to shut off their phones and dig in.", "Never attack personal dignity. Tactical empathy melts resistance; aggression breeds defiance."),
            ("Accepting Vague Promises", "Leaving the shop when the dealer says 'Kuch din me karwa denge.'", "Anchor down to specific dates, specific amounts, and signed PDCs or bank transfers."),
            ("Surrendering Principal", "Offering a 10% discount on overdue debt just to get quick cash.", "Protect enterprise capital. Concessions can be in extended supply terms or marketing support, never principal write-offs."),
            ("Legal Action as First Step", "Sending lawyer notices immediately, turning a solvent but slow customer into an active enemy.", "Exhaust all tactical negotiation avenues first; reserve litigation strictly for fraudulent bad actors.")
        ],
        "checklist": [
            "Dealer overdue ledger and payment history reviewed prior to collection call.",
            "Late-Night FM DJ voice maintained during tense debt discussions.",
            "Accusation audit utilized to defuse defensiveness at conversation start.",
            "Underlying cash flow constraint (Black Swan) identified before proposing solutions.",
            "Structured payment plan backed by concrete dates and negotiable instruments (PDCs/RTGS).",
            "Zero principal write-offs permitted without formal Board authorization."
        ]
    },
    "peter-drucker-financial-control-engine": {
        "title": "Peter Drucker Financial Control, Profit Centers & Working Capital Velocity Engine for Swatch Paints",
        "legend": "Peter F. Drucker (Father of Modern Management & Author of 'The Practice of Management')",
        "description": "Peter Drucker Financial Governance, Profit Centers vs Cost Centers, Contribution Margin per SKU, and Working Capital Velocity for Swatch Paints Finance.",
        "dept": "03_finance_gst",
        "tag": "peter-drucker-finance",
        "purpose": """This skill equips the Swatch Paints Chief Financial Officer, Corporate Controllers, and Commercial Finance teams with Peter Drucker’s foundational disciplines of **Financial Control**, **Contribution Margin Governance**, and **Working Capital Velocity**.

In manufacturing businesses, accounting systems frequently report "accounting net profits" that mask severe operational decay: capital is trapped in slow-turning decorative paint stocks, unprofitable product lines are subsidized by a single flagship primer, and expensive automatic tinting machines sit idle in underperforming dealer shops generating negative Return on Capital (ROIC).

The engine's purpose is to:
- Establish unambiguous **Profit Center vs. Cost Center Accountability** across plants, regional depots, and commercial sales territories.
- Enforce **Contribution Margin (CM) Discipline**: measuring the true cash contribution of every paint SKU after subtracting direct materials, packaging, freight, and variable sales commissions.
- Accelerate **Working Capital Velocity**: shrinking the Cash Conversion Cycle (CCC = DSO + DIO - DPO) to unlock self-funding growth.
- Evaluate capital expenditures (CapEx)—such as high-shear dispersers, automated filling lines, and dealer tinting machines—strictly against their real economic return.""",
        "when_to_use": """- Setting product line pricing, dealer discount schemes, and minimum gross margin thresholds.
- Evaluating whether to approve CapEx for purchasing and deploying dealer tinting machines (₹2.5 Lakhs per machine).
- Conducting monthly P&L reviews of regional depots and territory branches.
- Auditing SKU rationalization: deciding which slow-moving paint shades or container sizes to prune (Systematic Abandonment).
- Managing working capital crunches where revenues are growing but operating bank accounts are empty.
- Structuring annual departmental budgets and capital allocation frameworks.""",
        "frameworks": """### 6.1 Drucker's Principle of Contribution Margin
*"Revenues generate profit only after all direct variable costs are recovered; overhead allocation must never disguise product unprofitability."*

```
Net Contribution Margin per Litre = Net Realized Invoiced Price 
  - (Raw Material Cost + Packaging Cost + Inward Freight + Variable Rebates + Direct Shipping Freight)
```
- **Rule:** If an SKU cannot generate at least **28% Contribution Margin**, it cannot support enterprise overheads and must be reformulated, repriced, or pruned.

### 6.2 Working Capital Velocity & The Cash Conversion Cycle (CCC)
```
CCC = DSO (Days Sales Outstanding) + DIO (Days Inventory Outstanding) - DPO (Days Payable Outstanding)
```
- **DIO Target:** <30 days of finished goods and raw materials.
- **DSO Target:** <28 days across dealer receivables.
- **DPO Target:** 45-60 days on structured chemical vendor terms.
- **Goal:** Drive CCC toward **<15 days**. Every day of reduced CCC liberates ₹12 Lakhs in liquid cash flow at current production scales.

### 6.3 Economic Value Added (EVA) on Tinting Machine Assets
A computerized tinting machine placed at a dealer counter is an investment, not an expense.
```
Machine ROIC = (Annual Net Contribution from Tinted Bases - Annual Maintenance & Depreciation) / Machine Asset Cost
```
- **Standard:** If a dealer cannot generate at least **800 litres of tinted base sales per month**, the machine generates negative ROIC and must be redeployed to a higher-velocity counter.""",
        "decision_algo": """### Step 1: Contribution Margin Audit on All Active SKUs
- Extract net invoice revenue and direct variable costs from live ERP.
- Group SKUs into 4 Drucker Quadrants:
  - Stars (High Margin, High Velocity): Swatch Rustic, Premium Exterior Emulsion.
  - Workhorses (Moderate Margin, High Velocity): Interior Primer, Acrylic Distemper.
  - Dilemmas (High Margin, Low Velocity): Specialized Floor Coatings.
  - Drains (Low Margin, Low Velocity): Synthetic Enamel half-litre cans.
- Apply Systematic Abandonment to the Drains within 60 days.

### Step 2: Tinting Machine Deployment Gate
- Dealer must achieve 3 criteria to receive a subsidized tinting machine:
  1. Average monthly paint billing >₹3.5 Lakhs.
  2. Credit score verified with zero defaults in trailing 12 months.
  3. Minimum commitment of 600 litres/month of tinting bases.
- IF commitments are missed for 3 consecutive months:
  - Issue 30-day notice; retrieve machine if off-take does not recover.

### Step 3: Cash Conversion Cycle Optimization
- Enforce 21-day credit terms with 2% cash discount for payment within 7 days.
- Stretch raw material DPO through vendor financing and letters of credit, keeping CCC lean.""",
        "example1": """### Example 1: Pruning Unprofitable SKUs via Drucker Contribution Analysis
**Situation:** The factory produced 140 distinct SKU variants (different pack sizes of primers, enamels, and distempers). Finance showed overall company net profit of 6%, but cash flow was constantly choked.
**Drucker Contribution Analysis Applied:**
- Top 25 SKUs generated 91% of total contribution margin.
- 45 SKUs in 500ml and 200ml metal tins had negative contribution margins (-4% to -11%) due to excessive packaging and line changeover costs.
- **Action:** Systematically eliminated 38 negative-margin SKUs. Consolidated packaging into 1L, 4L, 10L, and 20L standards.
- **Outcome:** Production downtime dropped by 18%; overall operating profit rose from 6% to 11.4% within two quarters.""",
        "example2": """### Example 2: Redeploying 8 Idle Tinting Machines in Jaipur Zone
**Situation:** Swatch had 32 automatic tinting machines deployed in Jaipur. 8 machines at smaller sub-dealers generated less than 120 litres per month, falling far below the cost of capital.
**ROIC Recovery Action:**
- Exercised the redeployment clause: retrieved the 8 machines from the non-performing counters.
- Re-installed them at fast-growing contractor hardware counters in suburban growth corridors (Mansarovar Extension, Jagatpura).
- Tinted paint volume from those 8 machines surged from 960 litres/month to 9,400 litres/month, generating an additional ₹6.8 Lakhs in monthly gross profit.""",
        "failures": [
            ("Confusing Revenue with Profit", "Celebrating a ₹1 Crore sales month that consisted entirely of zero-margin commodity distemper.", "Track Net Contribution Margin daily in ERP; ban revenue targets detached from margin."),
            ("Treating CapEx as a Free Gift", "Handing out expensive tinting machines to dealers as personal favors.", "Enforce strict monthly minimum off-take covenants backed by legal machine retrieval contracts."),
            ("Ignoring Working Capital Creep", "Letting receivables drift to 65 days while boasting about accounting profits.", "Tie executive bonuses to Cash Conversion Cycle (CCC) and free operating cash flow."),
            ("Failing to Abandon Obsolete Products", "Keeping old formulation paint lines alive because 'one loyal customer in Kota still buys it.'", "Apply Drucker's Systematic Abandonment: prune unprofitable legacy lines ruthlessly.")
        ],
        "checklist": [
            "Contribution Margin (CM) calculated and audited for 100% of manufactured SKUs.",
            "Zero SKUs sold below the mandatory 28% contribution margin floor without CEO sign-off.",
            "Cash Conversion Cycle (CCC) monitored weekly; target maintained under 25 days.",
            "Tinting machine fleet audited monthly against 600 litre/month minimum off-take threshold.",
            "Depots and sales branches evaluated as autonomous Profit Centers with local P&Ls.",
            "Annual Systematic Abandonment review executed to eliminate non-performing product lines."
        ]
    },
    "robert-kaplan-robin-cooper-abc-costing-engine": {
        "title": "Robert Kaplan & Robin Cooper Activity-Based Costing (ABC) Engine for Swatch Paints",
        "legend": "Robert S. Kaplan & Robin Cooper (Harvard Business School, Creators of Activity-Based Costing & Balanced Scorecard)",
        "description": "Activity-Based Costing (ABC), Cost Driver Analysis, True SKU Profitability, and Customer Cost-to-Serve Engine for Swatch Paints Finance.",
        "dept": "03_finance_gst",
        "tag": "kaplan-cooper-abc",
        "purpose": """This skill equips the Swatch Paints Cost Accounting, Pricing, and Plant Finance teams with Kaplan and Cooper’s revolutionary **Activity-Based Costing (ABC)** methodology. It eradicates the dangerous distortions caused by traditional "volume-based" cost accounting.

In conventional paint manufacturing accounting, all factory and corporate overheads (grinding electricity, QC lab testing, tinting machine servicing, warehouse picking, small-order dispatch) are lumped together into a single "overhead pool" and allocated based on direct machine hours or gross litres produced. 

This creates a deadly financial illusion:
- **Mass-volume, simple products (e.g., 20L White Wall Primer)** appear artificially expensive because they absorb massive overheads they never consume.
- **Low-volume, complex specialty products (e.g., 1L specialized solvent-based tinting bases or custom texture finishes)** appear artificially cheap because they absorb tiny overhead allocations despite consuming 5x more chemist time, line cleaning, and lab testing.
- Consequently, the company underprices complex, unprofitable products and overprices its bread-and-butter products, losing market share to focused competitors.

The engine's purpose is to:
- Trace overhead costs directly to **Activities**, and then allocate them to products and customers using verified **Cost Drivers**.
- Uncover true **Customer Cost-to-Serve**: identifying dealers who appear profitable on paper but drain profit through frequent micro-orders, high return rates, and excessive technical support calls.
- Establish accurate, margin-defending price floors for standard versus customized coatings.
- Optimize operational processes by eliminating high-cost, non-value-added production activities.""",
        "when_to_use": """- Setting product price lists, dealer discount slabs, and minimum order quantities (MOQ).
- High factory overheads are rising faster than production volume, and traditional accounting cannot explain why.
- Evaluating customer profitability: determining whether a large wholesale distributor is genuinely profitable after factoring in special freight, rebates, and credit terms.
- A competitor is undercutting Swatch on standard 20L white primers while Swatch is flooded with low-volume specialty orders.
- Deciding whether to insource or outsource specialized packaging or tinting canister filling.
- Conducting annual strategic reviews of product portfolio profitability.""",
        "frameworks": """### 6.1 The Two-Stage ABC Costing Model
```
[RESOURCES (Labor, Electricity, Machines, Tech Lab, Freight)]
                     │
              (Resource Drivers)
                     ▼
           [ACTIVITIES (Kettle Cleaning, QC Testing, Order Picking, Machine Repair)]
                     │
              (Activity Drivers)
                     ▼
             [COST OBJECTS (Specific SKUs, Specific Dealers, Specific Packs)]
```

### 6.2 Key Cost Drivers in Coatings Manufacturing
| Activity | Traditional Cost Driver | Real ABC Activity Cost Driver |
|---|---|---|
| Grinding & Dispersion | Direct Labor Hours | Kilowatt-Hours consumed + Mill bead wear per viscosity grade |
| Batch Quality Testing | Fixed % of raw materials | Number of lab tests & spectrophotometer runs performed |
| Kettle Washout & Setup | Shared plant overhead | Hours spent cleaning + Litres of wash solvent/effluent consumed |
| Warehouse Order Picking | Fixed % of invoice | Number of discrete carton picks (Small orders cost 8x more per litre) |
| Dealer Technical Support | General sales overhead | On-site applicator visits logged in SFA CRM |

### 6.3 The Customer "Whale Curve" of Cumulative Profitability
Kaplan and Cooper proved that in any distributor network:
- **Top 20% of customers** generate 150% to 200% of total company profit.
- **Middle 60%** roughly break even.
- **Bottom 20%** lose 50% to 100% of profit due to extreme Cost-to-Serve (erratic ordering, high return rates, extended credit disputes).""",
        "decision_algo": """### Step 1: Resource-to-Activity Mapping
- Disaggregate indirect factory and administrative overheads into functional activity pools:
  - Activity 1: Mixing & Grinding.
  - Activity 2: Line Setup & Kettle Washout.
  - Activity 3: Finished Goods Material Handling & Order Picking.
  - Activity 4: Dealer Logistics & Field Technical Support.

### Step 2: Calculate Activity Cost Driver Rates
- Example: Total annual kettle washout cost (Labor + Solvent + Effluent) = ₹36 Lakhs across 1,200 washouts.
  - Activity Rate = ₹3,000 per kettle changeover.
- Charge this ₹3,000 directly to the low-volume batch that required the changeover, NOT to general white paint!

### Step 3: Compute True SKU ABC Margin
- True ABC Cost = Direct Raw Materials + Direct Packaging + Direct Freight + (Sum of Activity Quantities × Activity Driver Rates).
- IF an SKU's True ABC Margin < 15%:
  - Option A: Increase Minimum Batch Order Quantity (MOQ).
  - Option B: Reprice to reflect true complexity.
  - Option C: Discontinue SKU.

### Step 4: Manage the Customer Cost-to-Serve
- IF a dealer places daily orders of 2 pails instead of weekly pallet orders:
  - Institute a "Small Order Handling Surcharge" or provide an incentive for full-pallet ordering.""",
        "example1": """### Example 1: Uncovering the Hidden Loss in 1-Litre Specialty Enamels
**Situation:** Traditional cost accounting showed 1L High-Gloss Gold Enamel had a healthy 32% gross margin. The company heavily promoted it.
**Kaplan ABC Analysis Applied:**
- Found that producing 1L cans required stopping the automated canning line, manually adjusting filling nozzles, and conducting 4 separate color checks.
- When the activity costs of line setup (₹4,200 per run) and low-speed manual packaging were assigned directly to the 1L runs, the true ABC margin was revealed to be **-8.4% (A net loss on every can sold)**.
- **Counter-measure:** Swatch raised the price of the 1L specialty can by 22% and introduced a 500-litre minimum production campaign run.
- Customers gladly paid for the rare specialty finish; turned an annual hidden loss of ₹4.8 Lakhs into a clean ₹3.2 Lakh profit.""",
        "example2": """### Example 2: Re-architecting a High-Maintenance 'Whale' Dealer
**Situation:** A top dealer in Kota billed ₹40 Lakhs annually (Swatch’s 3rd largest counter). The sales team treated him like royalty, offering free express delivery and priority chemist visits.
**ABC Cost-to-Serve Audit:**
- Dealer placed 18 micro-orders per month (average order value ₹18,000).
- Demanded dedicated tempo deliveries directly to separate job sites.
- Claimed frequent small damage returns without verification.
- True ABC Cost-to-Serve was ₹5.6 Lakhs, reducing his actual net contribution to near zero!
- **Resolution:** CFO and ASM sat with the dealer with the ABC breakdown. Structured a new agreement: 2 planned weekly dispatches of full pallets; emergency express deliveries charged at ₹800/trip.
- Result: Delivery costs fell by 68%; dealer remained satisfied; Swatch retained ₹3.8 Lakhs in net margin.""",
        "failures": [
            ("Lumping Overheads into One Pool", "Spreading lab testing and machine maintenance equally across all litres produced.", "Assign overheads to specific activities and trace them via causal activity drivers."),
            ("Ignoring Customer Cost-to-Serve", "Assuming all dealers with the same discount terms are equally profitable.", "Calculate picking, delivery, and credit costs per dealer to uncover hidden profit drains."),
            ("Over-Complicating the ABC Model", "Creating 200 tiny activity pools that require full-time consultants to maintain.", "Follow Kaplan's rule: Focus on the 5 to 8 major activities that represent 85% of overhead costs."),
            ("Calculating Without Action", "Producing an ABC report that proves products are losing money but refusing to change prices.", "Use ABC findings immediately to adjust price lists, change MOQs, or re-engineer workflows.")
        ],
        "checklist": [
            "Overheads decomposed into discrete activity pools with verified cost drivers.",
            "Kettle changeover and cleaning costs charged directly to batch runs causing them.",
            "Customer Cost-to-Serve calculated for top 20 and bottom 20 dealer accounts.",
            "Minimum Order Quantities (MOQs) enforced for high-complexity, low-volume SKUs.",
            "Small-order delivery surcharges instituted to discourage profit-draining micro-shipments.",
            "True ABC margins integrated into ERP pricing and commercial quotation modules."
        ]
    },
    "warren-buffett-cash-flow-moat-engine": {
        "title": "Warren Buffett Economic Moat, Free Cash Flow & Pricing Power Engine for Swatch Paints",
        "legend": "Warren Buffett (Chairman of Berkshire Hathaway & Legendary Capital Allocator)",
        "description": "Warren Buffett Economic Moats, Owner Earnings (Free Cash Flow), Pricing Power, and Capital Allocation Engine for Swatch Paints Executive Leadership.",
        "dept": "03_finance_gst",
        "tag": "warren-buffett",
        "purpose": """This skill equips the Swatch Paints Executive Leadership, Board of Directors, and Strategy Office with Warren Buffett’s timeless disciplines of **Economic Moats**, **Pricing Power**, **Owner Earnings (True Free Cash Flow)**, and **Disciplined Capital Allocation**.

In the paint manufacturing industry, companies frequently engage in self-destructive "growth at any cost." They expand plant capacity by taking on massive bank debt, enter vicious price wars with Asian Paints and Berger, and celebrate rising top-line turnover while their actual free cash flow is negative. When crude oil prices or imported Titanium Dioxide prices spike, companies without an economic moat are crushed by rising input costs.

The engine's purpose is to:
- Identify, protect, and widen Swatch Paints' **Economic Moats**: Brand Trust, High Switching Costs for Painting Contractors, Cost Advantages in Regional Distribution, and Specialized Formulas (Swatch Rustic).
- Measure success by **Owner Earnings (Free Cash Flow)** rather than vanity EBITDA: Cash from Operations minus Maintenance Capital Expenditures.
- Test and exercise true **Pricing Power**: the ultimate test of a business’s greatness—the ability to raise prices without losing customers to rivals.
- Allocate retained earnings ruthlessly: reinvesting only in plant or marketing initiatives that generate an incremental return on capital (ROIC) greater than the cost of capital.""",
        "when_to_use": """- Formulating long-term enterprise strategy, 5-year capital allocation, and dividend policies.
- Confronting industry-wide raw material inflation (spikes in crude oil, monomers, or TiO2 pigments).
- Evaluating major CapEx investments: expanding factory floor space, acquiring land, or setting up new regional depots.
- Defending market share against aggressive, deep-pocketed competitors attempting to buy the market with discount schemes.
- Analyzing product portfolio moats: determining which product lines have pricing power and which are generic commodities.
- Guiding annual strategic budgeting under the direction of Ashutosh Sharma Sir.""",
        "frameworks": """### 6.1 Buffett's Definition of an Economic Moat
*"A truly great business must have an enduring 'moat' that protects excellent returns on invested capital."*

The Four Moats of Swatch Paints:
1. **Intangible Assets (Brand & Specialty IP):** The unique formulation, durability, and texture aesthetics of **Swatch Rustic**, creating a distinct identity that cannot be commoditized.
2. **Switching Costs:** A master painting contractor who has mastered the application of Swatch coatings and earns consistent loyalty rewards resists switching to untrusted competitor formulations.
3. **Cost Advantage:** Proximity of manufacturing plant in Rajasthan providing 24-hour replenishment to regional dealers, bypassing the high warehousing and long-haul freight costs of national giants.
4. **Network Density:** High counter share in focused geographic clusters (Kota, Bundi, Hadoti) that creates local brand ubiquity and mutual reinforcement between dealers.

### 6.2 Buffett's Single Most Important Decision Metric: Pricing Power
*"The single most important decision in evaluating a business is pricing power. If you've got the power to raise prices without losing business to a competitor, you've got a very good business."*
- If Swatch must hold a prayer meeting before raising prices by 2% following a raw material surge, it is in a commodity business.
- If customers willingly accept a price increase because of superior finish, zero sagging, and dependable support, Swatch possesses an economic moat.

### 6.3 Owner Earnings (True Free Cash Flow)
```
Owner Earnings = Net Operating Profit After Tax (NOPAT) + Depreciation & Amortization 
                 - Maintenance CapEx (capital required to maintain current competitive position) 
                 - Change in Working Capital
```
- Accounting profit that cannot be extracted as cash in the bank is an illusion.

### 6.4 The Reinvestment Hurdle Rule
Every rupee of retained earnings must create at least **one rupee of market value** and generate an incremental **ROIC >= 18%**.""",
        "decision_algo": """### Step 1: Moat Health Diagnostic
- For every product category, evaluate: Is this a Franchise or a Commodity?
  - Commodity: Undifferentiated distemper where buyers choose strictly on cheapest price.
  - Franchise: Swatch Rustic or Luxury Exterior where the master painter demands the brand by name.
- Direct 70% of R&D and promotional resources toward widening Franchise moats.

### Step 2: Test Pricing Power Dynamically
- When chemical raw materials rise by 5%:
  - Do NOT absorb the cost through margin compression.
  - Announce a calibrated price adjustment backed by transparent communication on raw material inflation.
  - Monitor dealer order volumes over the next 30 days: If volume drops by <3%, pricing power is verified.

### Step 3: Enforce the Maintenance vs. Growth CapEx Distinction
- Separate every capital expenditure proposal into:
  - Maintenance CapEx: Essential repairs to keep the plant running safely.
  - Growth CapEx: New capacity or automated machinery.
- Growth CapEx requires a formal discounted cash flow (DCF) model proving ROIC >= 18% over a 5-year horizon.

### Step 4: Fortress Balance Sheet Protection
- Maintain zero speculative short-term debt.
- Maintain an emergency liquid cash reserve to capitalize on raw material market dislocations (e.g., buying bulk TiO2 during temporary global price dips).""",
        "example1": """### Example 1: Exercising Pricing Power on Swatch Rustic During Emulsion Inflation
**Situation:** Global acrylic monomer prices surged by 28% due to crude oil supply shocks. Competitors panicked, slashing margins or secretly adulterating paint formulas with chalky extenders.
**Buffett Pricing Power Protocol Applied:**
- Swatch refused to degrade formula quality.
- Re-anchored customer perception: Released an executive letter to dealers and architects explaining that Swatch Rustic formulation integrity was inviolable, followed by a 6% price increase.
- While rivals faced applicator complaints over flaking, Swatch Rustic sales *increased* by 14% because contractors trusted the brand’s uncompromising quality.
- Gross margin was preserved completely; enterprise reputation strengthened.""",
        "example2": """### Example 2: Rejecting a Vanity Factory Expansion Project
**Situation:** An equipment vendor proposed a ₹4.5 Crore fully automated European sand-grinding mill, promising "state-of-the-art prestige."
**Buffett Capital Allocation Audit:**
- Analyzed existing plant capacity: current mills were running at only 62% capacity due to poor shift scheduling and long changeovers (Ohno Muda).
- Implementing Kaizen changeovers and Gemba scheduling would unlock 35% additional capacity for less than ₹8 Lakhs in minor modifications.
- The ₹4.5 Crore CapEx would generate a pathetic 7% ROIC while saddling the company with bank debt.
- **Decision:** Rejected the CapEx outright; invested ₹8 Lakhs in internal line optimization, preserving ₹4.4+ Crores in liquid enterprise cash.""",
        "failures": [
            ("The Growth-at-Any-Cost Trap", "Borrowing heavily to build massive factory capacity that sits idle during economic slowdowns.", "Follow Buffett's rule: Growth is only beneficial if it generates returns well above the cost of capital."),
            ("Commoditization Capitulation", "Entering price wars on low-end distempers and destroying company net worth.", "Never compete on price alone; anchor the business around differentiated texture and luxury franchises."),
            ("EBITDA Delusion", "Managing by EBITDA while ignoring that plant equipment deteriorates and requires real cash to replace.", "Manage strictly by Owner Earnings (Free Cash Flow after maintenance capital expenditure)."),
            ("Compromising Quality for Margins", "Quietly reducing resin content to save money during chemical price spikes.", "Never compromise the moat. Product trust takes 20 years to build and 5 minutes to destroy.")
        ],
        "checklist": [
            "Economic moats (Brand, Switching Costs, Local Cost Advantage) identified and defended.",
            "Pricing power tested and validated during raw material cost fluctuations.",
            "Owner Earnings (True Free Cash Flow) calculated and reviewed monthly.",
            "CapEx divided strictly into Maintenance vs. Growth categories.",
            "Growth CapEx investments evaluated against an uncompromising 18% ROIC hurdle rate.",
            "Fortress balance sheet maintained with zero unmanageable debt exposure."
        ]
    },

    # === 04_SUPPLY_CHAIN ===
    "donald-bowersox-logistics-network-engine": {
        "title": "Donald Bowersox Logistics Network & Hub-and-Spoke Freight Engine for Swatch Paints",
        "legend": "Donald J. Bowersox (Pioneer of Modern Logistics & Author of 'Supply Chain Logistics Management')",
        "description": "Donald Bowersox Hub-and-Spoke Depot Network, Total Logistics Cost Optimization, Vehicle Routing, and Freight Management for Swatch Paints.",
        "dept": "04_supply_chain",
        "tag": "donald-bowersox",
        "purpose": """This skill equips the Swatch Paints Supply Chain, Transportation, and Regional Logistics teams with Donald Bowersox’s foundational disciplines of **Integrated Logistics Management**, **Hub-and-Spoke Network Architecture**, and **Total Cost of Distribution**.

In paint distribution across large geographical territories like Rajasthan and Western India, logistics is not merely about "booking trucks"; it is a primary driver of customer satisfaction and margin preservation. Paint is heavy, bulky, and liquid, making freight cost per litre a major expense (often 5% to 8% of total revenue). Poorly designed logistics lead to disastrous outcomes: half-empty trucks crisscrossing highways, long delivery lead times (4 to 6 days) causing dealer stockouts, transit damage (burst pails, dented tins), and high logistics expenses.

The engine's purpose is to:
- Architect an optimized **Hub-and-Spoke Depot Distribution Network**: central manufacturing and primary mixing hub feeding regional satellite transit depots.
- Balance the **Total Logistics Cost Equation**: optimizing the trade-off between Transportation Costs, Inventory Holding Costs, and Order Processing Costs.
- Maximize **Vehicle Fill Rates (Cube & Weight Utilization)** using automated 3D pallet and pail packing algorithms.
- Enforce the **24-to-48 Hour Replenishment SLA** across all authorized dealer counters in the state.""",
        "when_to_use": """- Designing or modifying regional depot locations (Jaipur, Kota, Jodhpur, Udaipur, Bikaner).
- Selecting, negotiating, and auditing third-party transport logistics providers (3PL) and dedicated fleet contracts.
- High transit damage rates (leaking paint cans, damaged bucket handles, carton tears) during highway transit.
- Delivery lead times to tier-2/3 mandis exceeding the competitive 48-hour threshold.
- Freight costs per litre rising above the budgeted logistics cost ceiling in live ERP.
- Managing seasonal transport capacity pinches during Diwali pre-stocking or agricultural harvest seasons.""",
        "frameworks": """### 6.1 Bowersox's Principle of Total Logistics Cost
Minimizing freight cost alone often increases total costs. The Bowersox equation:
```
Total Logistics Cost = Transportation Cost + Warehousing Cost + Inventory Carrying Cost + Cost of Lost Sales (Stockouts)
```
- Running full truckloads (FTL) once every 15 days lowers transport cost per kg, but it explodes dealer inventory carrying costs and causes stockouts.
- The optimum network balances frequent, reliable scheduled dispatches with high vehicle cube utilization.

### 6.2 The Hub-and-Spoke Architectural Matrix
```
[CENTRAL MANUFACTURING PLANT & MOTHER HUB (Kota)]
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
[NORTH DEPOT]    [WEST DEPOT]    [SOUTH DEPOT]
  (Jaipur)         (Jodhpur)       (Udaipur)
       │               │               │
 (Milk Runs)      (Milk Runs)     (Milk Runs)
       ▼               ▼               ▼
 [Dealers A-H]   [Dealers I-P]   [Dealers Q-Z]
```
- **Mother Hub:** Holds full product line, high-inventory raw materials, and slow-moving specialty items.
- **Spoke Depots:** Hold only the top 35 fast-moving SKUs (tinting bases, primers, standard whites) with 7-day dynamic buffer replenishment.

### 6.3 Vehicle Fill Optimization (Cube vs. Weight)
Paint pails have high density (heavy weight), while empty packaging or bubble-wrap is bulky (high cube).
- Combine heavy 20L paint pails on the floor with light texture rollers, masking tapes, and marketing displays on the top deck to achieve 95%+ weight and cubic capacity utilization on every vehicle trip.""",
        "decision_algo": """### Step 1: Route & Load Optimization
- Aggregate dealer orders by geographic corridor (e.g., Jaipur-Ajmer-Bhilwara highway belt).
- IF consolidated corridor weight >= 9 MT:
  - Dispatch direct Dedicated Truck (FTL).
- IF consolidated corridor weight < 9 MT:
  - Route through regional Spoke Depot via scheduled multi-drop "Milk Run".

### Step 2: Enforce Packaging & Pallet Restraint Standards
- Mandate stretch-wrapping on all 20L pail pallets (minimum 4 layers of 23-micron film).
- Use corner edge-protectors to prevent pail rim crimping during bumpy road transits.

### Step 3: Real-Time Transit SLA Monitoring
- Track vehicle transit via GPS integration.
- Target: Primary dispatches (Plant to Depot) completed in <18 hours; Secondary dispatches (Depot to Dealer) in <24 hours.

### Step 4: Transporter Performance Audit
- Evaluate 3PL transporters on 3 metrics: On-Time Delivery Rate (>96%), Transit Damage Rate (<0.15%), and Freight Invoicing Accuracy.""",
        "example1": """### Example 1: Slashing Jodhpur Supply Lead Time from 5 Days to 24 Hours
**Situation:** Jodhpur dealers complained that orders took 5 to 7 days to arrive from the plant, causing frequent stockouts of exterior primer during peak repainting season. Sales reps lost orders to local competitors.
**Bowersox Network Fix Applied:**
- Established a lean 2,500 sq ft Spoke Transit Depot in Jodhpur Industrial Area.
- Stocked strictly the top 25 high-velocity SKUs with a 5-day dynamic buffer.
- Established a scheduled twice-weekly 16-MT replenishment shuttle from the central plant.
- Local deliveries to Jodhpur city dealers converted to same-day delivery via small electric delivery tempos.
- Result: Order lead time collapsed from 5 days to 6 hours for urban dealers; sales in Marwar region surged by 38% in 6 months.""",
        "example2": """### Example 2: Eliminating ₹3.2 Lakhs in Monthly Transit Pail Bursting
**Situation:** Dispatches to rural Shekhawati dealers suffered a 2.4% damage rate: 20L plastic buckets cracked at the base when trucks traversed broken rural roads, spilling paint and destroying invoice paperwork.
**Bowersox Packaging Intervention:**
- Replaced cheap uncertified wooden pallets with standardized injection-molded plastic pallets with non-slip surfaces.
- Implemented an interlocking honeycomb stacking pattern (brick-stacking) instead of column stacking.
- Added corrugated cardboard slip-sheets between pallet layers and enforced machine stretch-wrapping.
- Result: Transit damage rate plummeted from 2.4% to 0.08%, saving ₹3.2 Lakhs/month and ending dealer invoice disputes.""",
        "failures": [
            ("The Half-Empty Truck Trap", "Dispatching 3-tonne loads in 10-tonne trucks to satisfy a complaining rep, doubling freight cost.", "Establish minimum order consolidation thresholds; use multi-drop milk runs to fill trucks."),
            ("Neglecting Transit Packaging", "Blaming truck drivers for paint spills caused by poor pallet wrapping and weak pail lids.", "Enforce standardized palletization and stretch-wrapping SOPs before the vehicle leaves the gate."),
            ("Over-Proliferating Satellite Godowns", "Opening a rented depot in every small district, exploding fixed rent and idle inventory holding.", "Maintain lean, fast-turning spoke depots; use reliable overnight line-haul trucking to serve adjacent districts."),
            ("Tolerating Unreliable Transporters", "Using cheap, unvetted roadside transporters who vanish for 4 days without tracking.", "Partner with contracted, GPS-enabled logistics providers with strict penalty/bonus SLA clauses.")
        ],
        "checklist": [
            "Hub-and-spoke distribution topology active with defined mother hub and spoke buffers.",
            "Vehicle fill rates (weight and cube) audited and maintained at >90% before departure.",
            "Standardized palletization and 4-layer stretch-wrapping enforced on all outbound paint.",
            "Delivery SLA (24-48 hours) measured and tracked digitally via GPS milestones.",
            "Transit damage rate tracked continuously; hard ceiling maintained at <0.20%.",
            "Freight cost per litre monitored against budgeted ERP benchmarks monthly."
        ]
    },
    "eliyahu-goldratt-supply-chain-constraint-engine": {
        "title": "Eliyahu Goldratt Supply Chain Theory of Constraints & Buffer Management Engine for Swatch Paints",
        "legend": "Dr. Eliyahu M. Goldratt (Creator of Theory of Constraints & Author of 'The Goal' and 'It's Not Luck')",
        "description": "Eliyahu Goldratt Theory of Constraints (TOC), Drum-Buffer-Rope Supply Chain, Dynamic Buffer Management (DBM), and Stockout Elimination for Swatch Paints Distribution.",
        "dept": "04_supply_chain",
        "tag": "goldratt-supply-chain",
        "purpose": """This skill equips the Swatch Paints Supply Chain, Regional Depot Management, and Distribution Planning teams with Eliyahu Goldratt’s **Theory of Constraints (TOC) for Supply Chains**, **Drum-Buffer-Rope (DBR)** replenishment, and **Dynamic Buffer Management (DBM)**.

Conventional supply chains suffer from the destructive **Bullwhip Effect**: minor fluctuations in retail dealer demand cause massive, wild swings in factory production orders. When dealers order 10% more paint, regional depots panic and order 30% more, and the factory blends 80% more, leading to massive inventory bloat followed by sudden factory shutdowns. Despite huge overall inventory, dealers constantly suffer stockouts of the exact colors and bases they need today.

The engine's purpose is to:
- Overcome the Bullwhip Effect by shifting the supply chain from speculative local forecasts to **Consumption-Driven Replenishment**.
- Maintain central finished goods inventory at the plant (where aggregate demand is predictable) and pull to regional depots in small, frequent batches.
- Implement Goldratt's **Dynamic Buffer Management (DBM)** with visual 3-Color Zones (Green, Yellow, Red) to prioritize replenishment automatically.
- Maximize **Throughput (T)** while slashing Operating Expense (OE) and Inventory Investment (I).""",
        "when_to_use": """- Depots are simultaneously suffering stockouts of fast-moving bases while their warehouses are 100% full of slow-moving stock.
- The factory is whipsawed by sudden emergency rush orders from regional depots.
- Managing seasonal demand build-up before the post-monsoon and Diwali exterior painting surge.
- Setting depot safety stock levels without relying on flawed historical spreadsheet forecasts.
- Eliminating conflicts between plant production managers (who want long runs) and distribution managers (who want instant variety).
- Prioritizing daily truck dispatches when warehouse staging capacity is constrained.""",
        "frameworks": """### 6.1 The TOC Supply Chain Paradigm: Centralized Pooling
Goldratt proved that aggregate demand for an entire state is far more predictable than demand at any single dealer or district depot.
- **The Mistake:** Pushing 80% of finished goods stock into regional depots immediately after production. (If Kota over-forecasts and Jodhpur under-forecasts, paint sits frozen in Kota while Jodhpur loses sales).
- **The TOC Solution:** Hold 60% of inventory as **Central Plant Buffer** in high-velocity base formulations. Release to regional spoke depots daily based purely on actual consumption.

### 6.2 Dynamic Buffer Management (DBM)
Every SKU at every depot has a dedicated Buffer Size divided into three equal zones:
```
+-------------------------------------------------------+
| GREEN ZONE (Top 1/3): Stock is Healthy. NO ORDER.     |
+-------------------------------------------------------+
| YELLOW ZONE (Middle 1/3): Replenish standard order.   |
+-------------------------------------------------------+
| RED ZONE (Bottom 1/3): Critical Danger of Stockout!   |
| IMMEDIATE EXPEDITED DISPATCH FROM MOTHER HUB.        |
+-------------------------------------------------------+
```

### 6.3 Dynamic Buffer Adjustment Algorithm
- **Buffer Too Big:** If stock stays in the **Green Zone for 3 consecutive replenishment cycles**, the system automatically cuts the buffer by 33% (freeing trapped cash).
- **Buffer Too Small:** If stock penetrates into the **Red Zone and stays there for >24 hours**, the system automatically expands the buffer by 33% (preventing future stockouts).""",
        "decision_algo": """### Step 1: Establish Initial Buffer Levels
- For every SKU at every depot, calculate:
  `Target Buffer = Average Daily Consumption × Reliable Replenishment Time (RRT) × Safety Multiplier (1.5)`.

### Step 2: Daily Consumption Netting
- At 06:00 PM daily, query verified dealer billings from each depot.
- Generate automatic replenishment requests equal to *exactly what was consumed today*.

### Step 3: Priority Dispatch Sequencing
- Warehouse dispatch teams DO NOT pick orders on a "first-come, first-served" basis.
- Pick and load trucks strictly by **Buffer Penetration Percentage**:
  - Depot SKUs deepest in the Red Zone are loaded first.
  - Yellow Zone SKUs loaded second.
  - Green Zone SKUs are skipped.

### Step 4: DBM Buffer Sizing Recalibration
- Review DBM color logs weekly. Let the algorithm expand or contract buffer sizes automatically without bureaucratic meetings.""",
        "example1": """### Example 1: Rescuing the Jaipur Depot from Pre-Diwali Stockouts
**Situation:** During October, the Jaipur depot stocked out of 20L Exterior White Emulsion 4 times in two weeks, losing an estimated ₹12 Lakhs in sales, despite the depot holding ₹85 Lakhs of total inventory.
**Goldratt DBM Applied:**
- Found that ₹45 Lakhs of the depot's inventory was sitting in the Green Zone (dark enamels and wood stains that hadn't moved in 40 days).
- Implemented Dynamic Buffer Management: Slashed dark enamel buffers by 50% and transferred stock back to the central plant.
- Expanded the Exterior White buffer by 33% and instituted daily overnight replenishment from the Kota plant.
- Result: Exterior White stockouts dropped to zero for the entire festival season; total depot inventory footprint fell by 22%.""",
        "example2": """### Example 2: Eliminating Emergency Freight Surcharges in Udaipur
**Situation:** Udaipur depot manager panicked every Monday, booking expensive dedicated express tempos to haul missing paint from the factory, spending ₹65,000/month in emergency freight premiums.
**TOC Solution:**
- Replaced erratic manual orders with an automated TOC DBR daily replenishment link.
- Every carton sold out of Udaipur during the day triggered a picking slip at the Kota plant that evening, dispatched on the regular nightly line-haul truck.
- Emergency freight expenses dropped to zero; on-time in-full (OTIF) availability jumped from 81% to 99.2%.""",
        "failures": [
            ("Overriding the DBM Algorithm", "Depot managers manually hoarding extra stock because they 'have a hunch' a big order is coming.", "Hard ERP rule: Replenishment is dictated strictly by DBM consumption signals, not manual hunches."),
            ("Local Optimization at the Plant", "Plant manager refusing to blend small replenishment batches because 'it hurts kettle efficiency.'", "Supply chain throughput takes precedence over local kettle efficiency metrics."),
            ("First-Come, First-Served Loading", "Dispatching trucks to the nearest depot while a distant depot is starving in the Red Zone.", "Enforce load prioritization based strictly on Red Zone buffer penetration severity."),
            ("Pushing Unwanted Stock to Clear Floor", "Shipping un-demanded paint to depots just to clear factory floor space.", "Never pollute the supply chain with un-demanded inventory. Hold stock centrally until pulled.")
        ],
        "checklist": [
            "Finished goods inventory pooled centrally at the plant mother hub.",
            "Dynamic Buffer Management (Green, Yellow, Red) active for all depot SKUs.",
            "Daily replenishment orders equal strictly to verified daily consumption.",
            "Truck loading prioritized by deepest Red Zone buffer penetration percentage.",
            "Automatic buffer size adjustment (expand/contract by 33%) operational.",
            "On-Time In-Full (OTIF) dealer order fulfillment maintained at >98%."
        ]
    },
    "ford-w-harris-warehouse-flow-engine": {
        "title": "Ford W. Harris Warehouse Layout, Staging & Pallet Density Engine for Swatch Paints",
        "legend": "Ford Whitman Harris (Pioneer of Operational Engineering & Layout Optimization)",
        "description": "Ford W. Harris Warehouse Flow Architecture, High-Density Pallet Staging, ABC Velocity Slotting, and Picking Optimization for Swatch Paints Depots.",
        "dept": "04_supply_chain",
        "tag": "ford-w-harris-warehouse",
        "purpose": """This skill equips the Swatch Paints Warehouse Operations, Material Handling, and Depot Management teams with Ford Whitman Harris’s operational engineering disciplines applied to **Warehouse Flow Layout**, **ABC Velocity Slotting**, and **High-Density Pallet Storage**.

Paint warehouses face unique material handling hazards: high product weight (a single pallet of 20L buckets weighs over 1,200 kg), leak/spill risks, and massive SKU diversity across pack sizes (1L, 4L, 10L, 20L). In poorly organized warehouses, workers wander aimlessly down aisles searching for specific shades, forklifts collide in congested loading zones, high-velocity primers are tucked away in the back of the godown, and heavy buckets are stacked unsafely, causing structural collapses.

The engine's purpose is to:
- Implement **ABC Velocity Slotting**: placing high-velocity fast-moving SKUs directly adjacent to the shipping docks to minimize material handling travel distance.
- Engineer high-density, safety-certified **Heavy-Duty Pallet Racking Systems** (Selective, Drive-in, or Gravity Flow) maximizing vertical warehouse cube space.
- Eliminate picking bottlenecks through synchronized **Zone Picking & Batch Order Staging**.
- Guarantee total worker safety, zero forklift collisions, and rapid truck turn-around times (<45 minutes per truck).""",
        "when_to_use": """- Designing or renovating finished goods warehouses and regional depot spaces.
- Warehouse workers take >30 minutes to pick and stage a standard 100-pail dealer order.
- High incidence of material handling damage: fork tines puncturing paint pails, collapsed pallet stacks.
- Warehouse storage capacity is exhausted, leading to pallet staging in outdoor courtyards exposed to sun and rain.
- Congestion at loading docks causing delivery truck queues and driver frustration.
- Performing annual physical stocktaking and inventory audit reconciliations.""",
        "frameworks": """### 6.1 ABC Velocity Slotting Architecture
Warehouse space must be segregated strictly based on pick-frequency, not alphabetical order or product category:
```
+─────────────────────────────────────────────────────────────+
|                     TRUCK LOADING DOCKS                     |
+─────────────────────────────────────────────────────────────+
|  ZONE A (Top 10% Fast-Moving SKUs: 70% of picks)            |
|  - Floor level, closest to docks (20L Primer, White Base)   |
+─────────────────────────────────────────────────────────────+
|  ZONE B (Medium 30% Velocity SKUs: 20% of picks)            |
|  - Middle aisle pallet racking, easy forklift reach         |
+─────────────────────────────────────────────────────────────+
|  ZONE C (Slow 60% Velocity SKUs: 10% of picks)              |
|  - Upper racking tiers & distant rear aisles                |
+─────────────────────────────────────────────────────────────+
```
- By positioning Zone A items within 15 meters of the dock, total picking travel distance is slashed by up to **60%**.

### 6.2 Structural Pallet Stacking & Racking Physics
- **Floor Stacking Limit:** 20L plastic paint pails can be stacked a maximum of **3 tiers high** on standard pallets. Never exceed 3 tiers; compressive creep causes bottom buckets to buckle and rupture.
- **Racking Capacity:** Heavy-duty selective racking must be rated for at least 1,500 kg per pallet position with mandatory floor-anchored steel upright column protectors.

### 6.3 One-Way Traffic Flow & Staging Cells
- Separate receiving docks (inward from factory) from dispatch docks (outward to dealers).
- Enforce strict one-way aisles for forklifts and hand-pallet trucks (HPTs) to eliminate head-on traffic bottlenecks.""",
        "decision_algo": """### Step 1: Monthly Pick-Frequency Analysis
- Extract line-item pick counts from ERP Warehouse Management Module (WMS).
- Classify SKUs into Zone A, Zone B, and Zone C.
- Re-slot items whose velocity changed (e.g., promotional seasonal items moved to Zone A).

### Step 2: Inward Goods Inspection & Put-Away
- Incoming shipments from plant must be scanned and put away to designated bin locations within **120 minutes** of dock arrival.
- Prohibit leaving pallets unattended in transit aisles.

### Step 3: Batch Picking & Order Consolidation
- Pick multi-dealer shipments in consolidated batches rather than one order at a time.
- Consolidate orders in marked Staging Bays (Floor Yellow Boxes) 30 minutes prior to truck arrival.

### Step 4: Loading Dock Gate Control
- Inspect outgoing truck beds: Must be swept clean, dry, and free of protruding nails or broken floorboards before loading paint.""",
        "example1": """### Example 1: Slashing Order Picking Time by 55% at the Central Kota Godown
**Situation:** Workers at the main plant warehouse took 45 minutes to pick and assemble a 250-pail dealer order. Pickers walked an average of 420 meters per order, winding through cluttered aisles.
**Harris Velocity Slotting Applied:**
- Re-slotted the warehouse: Moved 20L White Exterior Emulsion and 20L Cement Primer (which represented 64% of all picks) from the far back wall to the front two floor-level racking bays next to Dock #1.
- Installed clear hanging aisle signage and color-coded floor striping.
- Walking distance per pick dropped from 420 meters to 110 meters.
- Order assembly time collapsed from 45 minutes to 19 minutes; truck turn-around time improved by 50%.""",
        "example2": """### Example 2: Eliminating Pallet Collapse Disasters in Summer Heat
**Situation:** In June, ambient temperatures in the warehouse reached 46°C. Workers had stacked 20L plastic buckets 5 pallets high to save space. The plastic softened under heat and compressive load, causing a 4-pallet collapse that ruptured 48 buckets of premium emulsion (₹1.8 Lakh loss).
**Harris Safety Intervention:**
- Instituted an absolute engineering rule: Floor-stacked plastic pails are capped at maximum 2 pallets (2 tiers per pallet = 4 buckets total height).
- Installed heavy-duty selective pallet racking, shifting storage from vertical dead-weight stacking to engineered steel beams.
- Zero pallet collapses recorded in over 18 months of operation.""",
        "failures": [
            ("Chaotic Random Slotting", "Stashing pallets wherever an empty spot exists, forcing pickers to search for hours.", "Mandate digital bin location tracking in ERP; every pallet must be scanned to a specific rack coordinate."),
            ("Exceeding Floor Stacking Limits", "Stacking heavy paint buckets 4-5 layers high on soft plastic pails to save floor space.", "Never exceed structural compressive limits. Invest in proper heavy-duty pallet racking."),
            ("Two-Way Aisle Gridlock", "Allowing forklifts to enter from both ends of narrow aisles, causing deadlocks and near-misses.", "Enforce strict one-way traffic signage and painted directional floor arrows."),
            ("Staging in Transit Aisle Ways", "Leaving assembled orders in front of fire exits or blocking main forklift thoroughfares.", "Designate marked staging bays with bright yellow boundary lines; enforce zero-tolerance for aisle blocking.")
        ],
        "checklist": [
            "ABC velocity slotting reviewed and updated monthly based on ERP picking frequency.",
            "Zone A fast-moving SKUs located within immediate proximity of dispatch docks.",
            "Pallet stacking height limits (maximum 3 tiers on floor) strictly audited.",
            "Heavy-duty pallet racking certified and equipped with steel column upright guards.",
            "One-way traffic flow and marked staging bays operational across all depot floors.",
            "Truck loading dock cycle time maintained under 45 minutes per vehicle."
        ]
    },
    "joseph-orlicky-dependent-demand-engine": {
        "title": "Joseph Orlicky Packaging & Auxiliary Material Dependent Demand Engine for Swatch Paints",
        "legend": "Joseph Orlicky (Pioneer of Dependent Demand & Material Requirements Planning)",
        "description": "Joseph Orlicky Dependent Demand Architecture for Paint Packaging (Pails, Tins, Lids, Handles, Labels) Synchronized with Batch Chemistry.",
        "dept": "04_supply_chain",
        "tag": "orlicky-packaging",
        "purpose": """This skill equips the Swatch Paints Supply Chain, Packaging Procurement, and Plant Materials teams with Joseph Orlicky’s rigorous **Dependent Demand Planning** principles applied specifically to **Packaging Materials & Consumables**.

In the coatings industry, packaging management is frequently treated as an afterthought compared to chemical raw materials. Yet, paint is a packaged product: you cannot ship bulk emulsion without a certified 20L HDPE pail, a secure gasketed lid, a sturdy metal handle, a regulatory barcode label, and an tamper-evident security seal. 

Traditional factories treat packaging as an "independent inventory item" ordered on rough guesses, leading to disastrous mismatches: 8,000 empty pails take up huge warehouse volume while the matching lids are missing, or 20 tonnes of ready-mixed paint sit stagnating in kettles because the screen-printed artwork for the new bucket has not been delivered by the injection-molding vendor.

The engine's purpose is to:
- Establish a mathematically synchronized **Dependent Demand Coupling** between paint batch production schedules and packaging inventory.
- Eliminate warehouse footprint bloat caused by bulky, empty plastic pails through **Just-in-Time (JIT) Supplier Delivery Agreements**.
- Synchronize multi-part packaging sets (1 Pail + 1 Lid + 1 Handle + 1 Token + 1 Carton) to eliminate fractional, orphaned components.
- Enforce strict packaging quality standards (drop-test resistance, lid sealing integrity, stress-crack resistance).""",
        "when_to_use": """- High kettle holding times caused by missing packaging containers, handles, or labels.
- Warehouse floor space is choked with bulky, empty 20L and 10L plastic pails.
- Changing packaging artwork, logos, or regulatory statutory declarations (managing obsolescence).
- Packaging components arrive out of balance (thousands of pails in stock but zero lids).
- Negotiating long-term supply and tooling contracts with plastic injection-molders and tin-can fabricators.
- Packaging defects (leaking lids, cracking handles, peeling labels) reported from transport transit.""",
        "frameworks": """### 6.1 The Packaging Dependency Equation
Packaging demand is 100% dependent on finished goods production:
```
Packaging Set Required = Planned Production Volume (Litres) / Pack Size (Litres) × (1 + Scrap Factor)
```
Where Scrap Factor is calibrated at **0.8%** for automated filling lines and **1.5%** for semi-automatic lines.

### 6.2 The Matched Set Rule
Never order or store packaging as isolated components. Every unit of paint requires a **Matched Set**:
```
[1 HDPE Pail] + [1 Hermetic Gasketed Lid] + [1 Zinc-Plated Handle with Plastic Sleeve] + [1 Barcode/Token Sticker]
```
- **Rule:** If the warehouse has 5,000 pails but only 3,200 lids, the effective available inventory is **3,200 sets**. The excess 1,800 pails are merely dead space wasting valuable warehouse volume.

### 6.3 Bulky Packaging JIT Inward Scheduling
Empty 20-litre buckets are 95% air. Storing 20,000 empty pails requires a massive 3,500 sq ft warehouse.
- Partner with local injection-molding vendors located within a 150 km radius.
- Issue rolling 14-day MPS schedules; require vendors to deliver packaging on dedicated daily or alternate-day milk runs directly to the packaging line dock, bypassing long-term godown storage.""",
        "decision_algo": """### Step 1: Explode Packaging Requirements from MPS
- When the 7-day Master Production Schedule is frozen, automatically explode exact packaging set counts.
- Cross-check current physical matched sets in stock.

### Step 2: Vendor Delivery Call-Off
- Send digital delivery call-offs to packaging vendors with exact dock delivery windows (e.g., 5,000 pails with matching lids required at Dock #2 by Tuesday 07:00 AM).
- Enforce the "No Pails Without Matching Lids" delivery acceptance gate.

### Step 3: Inward Quality Testing Gate
- QC team pulls 10 random pails per lot before unloading:
  - Drop Test: Fill pail with 20 kg water; drop from 1.5 meters onto concrete floor. (Must show zero cracking or seal leak).
  - Handle Pull Test: Apply 45 kg static tensile force to handle lugs.

### Step 4: Artwork & Regulatory Version Control
- Manage brand design revisions via ERP lot control.
- Automatically consume 100% of legacy printed pails before activating new artwork BOMs.""",
        "example1": """### Example 1: Solving the Orphaned Lid Crisis in the 10-Litre Line
**Situation:** The packaging warehouse held 6,400 empty 10L buckets of Swatch Exterior Sheen, but production was halted because there were only 220 matching blue lids in stock. The vendor stated lids were backlogged for 8 days.
**Orlicky Matched Set Principle Applied:**
- Diagnosed root cause: Procurement issued separate purchase orders for pails and lids to two different vendors to save ₹0.40 per lid.
- Restructured procurement: Consolidated both pail and lid into a single "Matched Container Set" contract with a single qualified injection molder.
- Vendor was made contractually responsible for delivering complete sets with zero component mismatch.
- Result: Line halts due to missing lids dropped to zero permanently.""",
        "example2": """### Example 2: Liberating 2,800 Sq Ft of Godown Space via JIT Packaging Delivery
**Situation:** The plant godown was stuffed with 18,000 empty 20L plastic buckets, forcing raw material chemical pallets to be staged outside under tarpaulins.
**JIT Delivery Redesign:**
- Negotiated a JIT delivery framework with a primary plastic manufacturer in Kota Industrial Area.
- The supplier agreed to hold safety stock at their own factory and deliver 2 truckloads (2,400 pails/truck) every 48 hours directly to the filling line.
- Swatch slashed internal empty pail inventory from 18,000 units to 2,400 units, liberating 2,800 sq ft of indoor godown space for valuable raw material storage.""",
        "failures": [
            ("Unbalanced Component Purchasing", "Buying pails from one vendor and lids from another, creating massive inventory mismatches.", "Procure packaging strictly as verified matched sets from unified, single-source suppliers."),
            ("Warehousing Air", "Storing 2 months of empty bulky plastic containers inside expensive factory warehouse space.", "Implement JIT delivery schedules with local packaging fabricators on rolling 48-hour call-offs."),
            ("Skipping Inward Drop Tests", "Accepting packaging lots without drop-testing, discovering brittle pails only after paint leaks on trucks.", "Enforce mandatory 1.5-meter water-filled drop tests and handle tension tests on every inward lot."),
            ("Artwork Obsolescence Write-Offs", "Printing 10,000 custom pails right before a government regulatory labeling mandate changes.", "Align packaging order quantities strictly with production batches during artwork transition periods.")
        ],
        "checklist": [
            "Packaging materials planned strictly as Dependent Demand tied to MPS paint batches.",
            "Matched Set Rule enforced: pails, lids, handles, and labels tracked in 1:1 balance.",
            "JIT delivery agreements operational with local molders to prevent godown bloat.",
            "Inward drop-testing and handle tensile strength tests executed before lot acceptance.",
            "Artwork revisions and statutory label changes managed via strict ERP phase-in / phase-out.",
            "Zero paint kettle production delays attributable to missing packaging containers."
        ]
    },
    "philip-kotler-scm-strategy-engine": {
        "title": "Philip Kotler Channel Logistics, Distributor ROI & Partner Alignment Engine for Swatch Paints",
        "legend": "Philip Kotler (World's Foremost Marketing Authority & Author of 'Marketing Management')",
        "description": "Philip Kotler Marketing Channel Logistics, Dealer GMROI, Channel Conflict Resolution, and Vendor Managed Inventory (VMI) for Swatch Paints.",
        "dept": "04_supply_chain",
        "tag": "philip-kotler-scm",
        "purpose": """This skill equips the Swatch Paints Commercial Logistics, Channel Development, and Regional Sales leadership with Philip Kotler’s world-renowned disciplines of **Marketing Channel Management**, **Distributor Return on Investment (GMROI)**, and **Multi-Channel Conflict Resolution**.

In decorative and industrial paints, the physical supply chain is not merely an engineering function of moving boxes; it is the physical delivery of the company’s brand promise to the customer. A brilliant marketing campaign or superior chemical formula is completely neutralized if the dealer's shelf is empty when the painter walks into the shop. Furthermore, channel partners (retail dealers, mega-wholesalers, direct project distributors) frequently clash over territory poaching, wholesale price undercutting, and unfair credit terms.

The engine's purpose is to:
- Align physical supply chain delivery with the strategic demands of diverse **Marketing Channels** (Retail Hardware Counters, Exclusive Swatch Color Studios, Bulk Project Contractors).
- Protect dealer profitability by optimizing their **Gross Margin Return on Inventory (GMROI)** and inventory turnover.
- Prevent and resolve destructive **Channel Conflicts** (Horizontal conflict between neighboring dealers; Vertical conflict between company depots and wholesale distributors).
- Deploy **Vendor-Managed Inventory (VMI)** for top-tier anchor dealers, automatically managing their shelf stock so they never run out of fast-selling paint.""",
        "when_to_use": """- Structuring commercial distribution agreements and trade margin tiers for new regional markets.
- Neighboring paint dealers accuse each other of price undercutting and cross-territory dumping.
- Top-billing dealers complain of sluggish inventory turnover and low return on working capital.
- Designing the logistics fulfillment model for exclusive Swatch Color Studios vs. multi-brand hardware retailers.
- Resolving conflicts between direct project sales (serving large builders) and local retail dealers who claim territory exclusivity.
- Transitioning key accounts to Vendor-Managed Inventory (VMI) agreements.""",
        "frameworks": """### 6.1 Kotler's Marketing Channel Flows
A channel is a synchronized network of 5 interrelated flows:
1. **Physical Flow:** Bulk paint moving from plant to depot to dealer shelf.
2. **Title/Ownership Flow:** Legal transfer of ownership and risk upon invoice generation.
3. **Payment Flow:** Cash, RTGS, and credit note settlement flowing back to Swatch treasury.
4. **Information Flow:** Real-time secondary sales, painter token scans, and stock levels.
5. **Promotion Flow:** Co-branded shop boards, shade cards, demo walls, and festival schemes.
- **Rule:** A breakdown in *any one* of these five flows destroys the channel partnership.

### 6.2 Dealer Gross Margin Return on Inventory (GMROI)
Smart paint merchants evaluate partnerships not by gross margin % alone, but by GMROI:
```
GMROI = (Gross Margin % / (100% - Gross Margin %)) × Inventory Turnover Ratio
```
- A competitor offering a high 18% margin that turns only 2 times a year yields a weak GMROI.
- Swatch offering a 14% margin that turns **8 times a year** due to 24-hour depot replenishment yields **more than double the cash profit** on the dealer's invested capital!
- Sales reps must use GMROI math to win shelf space from rivals.

### 6.3 Channel Conflict Resolution Matrix
- **Vertical Conflict (Depot vs. Dealer):** Solved by strict rules of engagement: Company depots are forbidden from selling direct to retail customers or small painters; all secondary leads are routed through authorized dealers.
- **Horizontal Conflict (Dealer A vs. Dealer B):** Solved by territorial geographic boundaries, minimum advertised price (MAP) policies, and exclusive product allocations (e.g., Dealer A gets exclusive territory rights for Swatch Rustic).""",
        "decision_algo": """### Step 1: Channel Segmentation & Service Level Definition
- Segment accounts into Tier 1 (Anchor Stores), Tier 2 (Standard Retailers), and Tier 3 (Rural Counters).
- Align delivery SLAs: Tier 1 gets 24-hour VMI replenishment; Tier 2 gets 48-hour scheduled beat delivery; Tier 3 gets weekly distributor milk runs.

### Step 2: Implement Vendor-Managed Inventory (VMI)
- For top 20 Anchor Dealers: Connect dealer POS/billing data to Swatch ERP.
- When dealer stock falls below reorder point, ERP automatically triggers a replenishment order without requiring the dealer to write a purchase order.

### Step 3: Enforce Anti-Dumping Rules
- Serial numbers and QR codes on paint pails track the exact authorized dealer of origin.
- IF paint assigned to Dealer X is caught being dumped at discounted rates in Dealer Y's territory:
  - Freeze quarterly scheme payouts to Dealer X; issue formal compliance warning.

### Step 4: Quarterly Channel Partner Business Review
- Conduct structured GMROI reviews with dealer leadership, demonstrating how fast inventory turns generated superior annualized cash returns.""",
        "example1": """### Example 1: Resolving a Bitter Channel Conflict in Kota Mandi
**Situation:** A dominant mega-wholesaler in Kota bought Swatch paint at bulk tier discounts and began dumping it at 2% over cost to small sub-dealers in Bundi, undercutting the local authorized Bundi dealer who threatened to rip down his Swatch signage.
**Kotler Channel Governance Applied:**
- Traced the dumped buckets via batch QR codes back to the Kota wholesaler.
- Restructured trade discount terms: Replaced upfront bulk cash discounts with **End-Use Verified Secondary Rebates** (rebate paid only when paint is sold to registered painters in Kota city limits).
- Barred the wholesaler from receiving rebates on cross-border shipments into Bundi.
- Result: Price parity was restored; the Bundi dealer’s margins were protected, and total sales across both territories grew by 24% without margin erosion.""",
        "example2": """### Example 2: Pitching GMROI to Win the Top Counter in Bhilwara
**Situation:** The largest paint retailer in Bhilwara stocked 90% Asian Paints. He told the Swatch rep: *"Asian gives me 12% margin and brand recognition. Why should I stock Swatch for 15%?"*
**Kotler GMROI Presentation:**
- The rep proved that Asian required him to keep ₹15 Lakhs of slow-moving inventory in his godown, turning only 3 times a year.
- Offered Swatch with a 24-hour replenishment commitment from the local depot: The dealer only needed to hold ₹3 Lakhs of stock, turning 10 times a year.
- Showed the math: The dealer's annual profit per rupee invested in Swatch would be **nearly 40% higher** than his current brand!
- Result: The dealer opened a dedicated 30-foot Swatch display section and committed ₹6 Lakhs in monthly turnover.""",
        "failures": [
            ("Selling Direct Around Dealers", "Company sales reps bypassing local dealers to sell direct to builders, destroying channel trust.", "Honor channel boundaries strictly; route commercial project billing through local stocking dealers."),
            ("Ignoring Dealer GMROI", "Pitching gross margin percentages while ignoring that slow-moving stock is trapping the dealer's cash.", "Train field reps to sell inventory velocity and capital turnover, not just price discounts."),
            ("Tolerating Cross-Territory Dumping", "Allowing large wholesalers to destroy retail dealer pricing in adjacent districts.", "Implement track-and-trace QR codes on buckets and penalize unauthorized dumping aggressively."),
            ("One-Size-Fits-All Logistics", "Treating a mega-wholesaler and a tiny rural hardware counter with the exact same delivery terms.", "Segment channel partners by volume and role; tailor logistics SLAs and order frequencies accordingly.")
        ],
        "checklist": [
            "Channel flows (Physical, Title, Payment, Information, Promotion) audited and aligned.",
            "Dealer GMROI calculations utilized in all commercial and shelf-space negotiations.",
            "Channel conflict resolution policies (Anti-Dumping, Territory Boundaries) enforced.",
            "Batch QR tracking operational to trace grey-market diversion and cross-border dumping.",
            "Vendor-Managed Inventory (VMI) agreements operational with qualified anchor dealers.",
            "Direct sales bypass eliminated; all local project orders routed through authorized dealers."
        ]
    }
}

def generate_fin_scm_skill(name, data):
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
        f"*{data['legend']} — Operationalized for Swatch Paints Enterprise Governance Architecture.*",
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
        "Before invoking this engine, collect the following real-time inputs from live commercial, tax, and ERP systems. Zero static assumptions or hardcoded parameters are permitted.",
        "",
        "### 4.1 Enterprise & Transactional Inputs",
        "",
        "| Input | Why It Matters | Live System Source |",
        "|---|---|---|",
        "| Partner / Depot Ledger Account | Tracks verified billing, payments, credit limits, and outstandings | Live ERP General Ledger |",
        "| Statutory Tax & GSTIN Records | Validates tax compliance, e-way bills, and GSTR-2B ITC eligibility | Government GST Portal / API |",
        "| Route & Freight Rate Master | Governs logistics contracts, vehicle weight limits, and transit times | Live Transport ERP Master |",
        "| Inventory Buffer & Velocity Data | Establishes daily consumption run-rates and storage constraints | Live Warehouse / WMS Module |",
        "",
        "### 4.2 Financial & Operational Guardrails",
        "",
        "| Guardrail | Enforcement Rule | Authority |",
        "|---|---|---|",
        "| Absolute ITC Verification | Zero ITC claimed without matching GSTR-2B reflection | Statutory Tax Policy |",
        "| Credit Period Ceiling | Hard ceiling on credit days; automatic order block upon breach | Credit Committee / CFO |",
        "| Transit Damage Threshold | Damage rate must remain strictly below 0.20% of freight value | Supply Chain Director |",
        "",
        "---",
        "",
        "## 5. DIAGNOSTIC QUESTIONS",
        "",
        f"Apply these 10 diagnostic inquiries before taking strategic, financial, or logistics action under the {name} framework:",
        "",
        "1. What is the fundamental commercial bottleneck or liquidity constraint we are addressing?",
        "2. Does this action protect enterprise net contribution margin and working capital velocity?",
        "3. Have we verified all underlying data against live ERP and statutory systems rather than manual spreadsheets?",
        "4. How does this decision impact customer and partner trust over a 12-month horizon?",
        "5. Are we confusing top-line revenue volume with real, cash-in-bank free cash flow?",
        "6. What is the true Cost-to-Serve or Total Logistics Cost of this transaction?",
        "7. Are we suffering from the Bullwhip Effect or speculative forecasting instead of real consumption pull?",
        "8. Have we uncovered all hidden constraints, tax liabilities, or unrecorded freight costs?",
        "9. What is the worst-case regulatory or financial failure mode, and what guardrails prevent it?",
        "10. Who has single-point accountability for governance, and what is the weekly audit cadence?",
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
        "Every strategic financial directive, tax audit memo, or logistics routing blueprint must follow this standardized schema:",
        "",
        "```markdown",
        f"# Swatch Paints Executive Governance Directive: {data['title']}",
        "",
        "### 1. Operational Scope & Objective",
        "- **Target Entity / Geography:** [Depot / Dealer / Vendor / Tax Authority]",
        "- **Responsible Officer:** [Designation & Name]",
        "- **Time Horizon:** [Effective Date – Audit Review Date]",
        "- **Primary Metric Target:** [Quantified financial or operational outcome]",
        "",
        "### 2. Methodological & Strategic Intervention",
        "- **Diagnostic Findings:** [Root cause analysis from live data]",
        "- **Actionable Protocol:** [Specific operational / commercial change]",
        "- **Execution Safeguards:** [Anti-leakage controls / automated system locks]",
        "",
        "### 3. Financial & Risk Guardrails",
        "- **Margin / Working Capital Impact:** [Quantified cash impact from live ERP]",
        "- **Statutory & Legal Compliance:** [Tax / credit / transit regulation adherence]",
        "- **Rollback Trigger:** [Specific event requiring immediate escalation to CEO]",
        "",
        "### 4. Governance & Cadence",
        "- **Review Cadence:** [Weekly / Monthly review meeting]",
        "- **Primary Metric Owner:** [Named Finance Manager / Logistics Lead]",
        "- **Sign-off Authority:** [CFO / Commercial Director / CEO Office]",
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
        "Watch for these recurring administrative, financial, and supply chain failure modes:",
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
        "Before finalizing or launching any operational protocol under this skill, verify:",
        ""
    ])
    for item in data['checklist']:
        sections.append(f"- [ ] {item}")
        
    sections.extend([
        "",
        "---",
        "",
        f"**CEO Directive:** At Swatch Paints, financial rigor and supply chain precision are non-negotiable pillars of enterprise resilience. We reject sloppy tax compliance, uncontrolled credit leakage, and chaotic warehouse logistics. Every commercial officer, accountant, and logistics manager must execute the principles of {data['legend']} with uncompromising discipline, protecting the company's capital and customer reputation at all times."
    ])
    return "\n".join(sections)

def main():
    for name, data in FIN_SCM_SKILLS.items():
        content = generate_fin_scm_skill(name, data)
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
