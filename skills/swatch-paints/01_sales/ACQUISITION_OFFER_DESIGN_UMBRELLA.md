---
name: acquisition-offer-design-umbrella
version: 1.0.0
author: Hermes, CEO of Swatch Paints
license: Proprietary
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [swatch-paints, 01_sales, acquisition, offer_engineering]
    related_skills: [alex-hormozi-offer-engine, jordan-belfort-straight-line-script-engine, andy-grove-execution-engine, frederick-reichheld-retention-engine]
---

# Acquisition Offer Design Umbrella Skill

## 1. TITLE

**Acquisition Offer Design Umbrella Skill for Swatch Paints**

*Legend: Integrates Alex Hormozi’s Value Equation, Jordan Belfort’s Straight Line Closing, and Andy Grove’s Leading Indicators for high-converting, margin-safe campaigns in Rajasthan.*

> **CEO Directive:** This is the master framework for all acquisition offers targeting dealers, painters, and contractors. Use only with live ERP pricing and Finance approval. Never bypass margin floors or use price-only discounts.

---

## 2. PURPOSE

To unify and standardize the design of high-leverage acquisition offers across Swatch Paints’ sales ecosystem. This umbrella skill ensures every offer:

- Is built on Hormozi’s value equation: maximize perceived value while minimizing sacrifice.
- Uses Belfort’s straight-line script to guide the sales conversation with precision.
- Leverages Grove’s leading indicators to track performance in real time.
- Maintains ironclad margin protection via Finance gatekeeping.
- Is executable, measurable, and repeatable across all territories.

It prevents fragmentation, ensures consistency, and embeds CEO-level discipline into every campaign.

---

## 3. WHEN TO USE

Invoke this umbrella skill whenever:

- Designing a new acquisition offer for dealers, painters, or contractors.
- Responding to a competitor’s aggressive scheme without entering a price war.
- Launching a new product (especially Swatch Rustic) and needing early adoption momentum.
- A territory is underperforming and the existing offer is not converting.
- The CEO or Sales Head needs to evaluate whether a proposed scheme is genuinely compelling or just a disguised price discount.

Do NOT use this skill for routine order-taking, credit negotiations, or operational dispatch decisions.

---

## 4. PREREQUISITES

- Access to live ERP pricing data (via `terminal` or `web_extract` to ERP API).
- Finance & Pricing Department approval for margin floors.
- At least one of the following skills must be loaded:
  - `alex-hormozi-offer-engine`
  - `jordan-belfort-straight-line-script-engine`
  - `andy-grove-execution-engine`
  - `frederick-reichheld-retention-engine`

---

## 5. PROCEDURE

Follow this strict workflow when designing an acquisition offer:

### Step 1: Define the Target Segment

- IF target is a **new dealer** → prioritize stock protection, display support, and painter pull-through.
- IF target is a **painter** → prioritize sample kits, training, and loyalty rewards.
- IF target is a **contractor / builder** → prioritize bulk terms, project support, and on-site technical assistance.
- IF target segment is unclear → STOP. Clarify before proceeding.

### Step 2: Pull Live ERP Pricing and Margin Floor

- IF ERP pricing is unavailable → STOP. Offer cannot be finalized.
- IF proposed offer breaches the minimum gross margin floor → REJECT immediately.
- IF margin is above floor but thin → require Finance sign-off and cap total exposure.

### Step 3: Apply Hormozi’s Value Equation

- **Dream Outcome:** For a dealer = higher footfall and repeat painter orders. For a painter = better finish, more referrals, higher daily earnings. For a contractor = on-time project delivery and lower material cost.
- **Perceived Likelihood:** Proof elements — demo walls, testimonials from local painters, sample boards, case studies of nearby projects.
- **Time Delay:** Reduce it with instant samples, same-day delivery, or immediate loyalty credit.
- **Effort & Sacrifice:** Remove friction with free trial stock, free training, easy returns on slow SKUs, and dedicated relationship manager support.

**CEO Directive:** Never increase value only by lowering price. Increase the numerator (outcome and proof) and decrease the denominator (speed and friction).

### Step 4: Build the Offer Stack Using Belfort’s Framework

- **Lead Magnet:** Low-risk entry point that gets the target to raise their hand. (Free Swatch Rustic sample kit for painters; free shade card + small tester stock for dealers.)
- **Tripwire:** Small first commitment that converts a lead into a customer. (Introductory 10-litre bundle at standard trade terms with a bonus tool/apron.)
- **Core Offer:** The main profitable transaction. (Regular dealer stocking order or contractor bulk purchase at approved ERP pricing.)
- **Profit Maximizer:** Upsell that increases average order value. (Premium texture finish add-on, primer-sealer combo, extended support package.)
- **Return Path / Retention:** Mechanism to bring the customer back. (Loyalty points, festival pre-booking credit, exclusive preview of new shades.)

### Step 5: Implement Grove’s Leading Indicators

Track these metrics in real time:
- New accounts opened per day
- Litres sold per territory
- Repeat purchase rate
- Painter satisfaction score (via post-sale survey)
- Display placements secured

Set alerts for drops below threshold.

### Step 6: Stress-Test for Abuse

- IF the offer can be gamed by hoarding → cap quantity per account and require verified end-use.
- IF the offer invites return fraud → define condition of returned goods and require manager approval.
- IF the offer can be passed through to end-users without dealer margin → structure bonuses as account credits, not cash discounts.

### Step 7: Approve and Assign Ownership

- IF margin, abuse risk, and value stack all pass → draft the offer memo.
- IF any gate fails → revise or reject.
- Assign named owner, start/end date, territory, and success metric before launch.

---

## 6. PITFALLS

| Pitfall | Why It Happens | Fix |
|--------|----------------|-----|
| **Price-only offer** | Designer defaults to discounting | Add at least two non-price value layers |
| **Margin breach** | ERP data not pulled or Finance not consulted | Require live ERP query and Finance sign-off |
| **No urgency** | Offer lacks scarcity or time limit | Add Diwali deadline, first-15-dealers cap |
| **No proof** | Claims lack validation | Add demo wall, testimonial, case study |
| **Abuse risk** | Hoarding or fraud possible | Cap quantities, require verification |
| **No owner** | Offer is discussed but not executed | Assign named sales executive and follow-up date |
| **No metric** | Success is vague | Define accounts, litres, repeat rate, or display count |
| **Competitor mirroring** | Offer is copycat | Build around Swatch-specific assets (local factory, Rustic range, service speed) |
| **Complexity overload** | Too many conditions confuse | Simplify to 3-5 clear value layers |
| **Finance not consulted** | Margin or budget not verified | Hard stop until ERP pricing and Finance approval are obtained |

---

## 7. VERIFICATION

After completing the offer, verify:

- [ ] Live ERP pricing has been pulled.
- [ ] Minimum gross margin floor has been respected.
- [ ] At least two non-price value layers are included.
- [ ] Risk reversal is included and budgeted.
- [ ] Urgency or scarcity mechanism is included.
- [ ] Proof element (demo / testimonial / case study) is included.
- [ ] Abuse safeguards are defined.
- [ ] Success metric and follow-up date are set.
- [ ] Named sales executive owns execution.
- [ ] Finance & Pricing Department has approved the offer.
- [ ] Offer memo is saved in the sales / strategy repository.

---

## 8. OUTPUT STRUCTURE

Every offer produced by this skill must be documented in the following structure:

```markdown
### Offer Name
- **Target:** [Dealer / Painter / Contractor]
- **Territory:** [District / Town]
- **Duration:** [Start – End]
- **Objective:** [Accounts / Litres / Repeat rate / Display placements]

### Value Stack
1. Core product / bundle: [SKU from ERP]
2. Lead magnet / trial: [Free sample / demo / training]
3. Risk reversal: [Guarantee / exchange / service promise]
4. Urgency / scarcity: [Time or quantity limit]
5. Retention hook: [Loyalty credit / next-order bonus / exclusivity]

### Financial Gate
- Minimum gross margin: [X% from Finance]
- Projected acquisition cost per customer: ₹[X]
- Projected CLV: ₹[X]
- Approved budget holder: [Name]

### Execution
- Owner: [Sales executive name]
- Follow-up date: [DD-MM-YYYY]
- Success metric: [Measurable KPI]
- Abuse safeguards: [Quantity caps / verification / return rules]
```

---

## 9. EXAMPLES

### Example 1: Dealer Acquisition in Bundi — Swatch Rustic Launch

**Situation:** A mid-size paint dealer in Bundi currently stocks Asian Paints and Berger. He is unwilling to commit shelf space to a new brand unless he sees painter demand.

**Diagnostic Answers:**
- Target: Dealer
- Current brand: Asian Paints / Berger
- Pain point: Fear of dead stock and no painter pull
- Margin floor: Pulled from ERP
- Non-price assets: Swatch Rustic demo wall, local painter testimonials, nearby project photos

**Offer Built:**

- **Core Offer:** Dealer stocks Swatch Rustic 4 kg and 20 kg packs at standard ERP trade terms.
- **Lead Magnet:** Free Swatch Rustic shade card standee + 2 sample boards for the shop front.
- **Risk Reversal:** Any slow-moving Swatch Rustic SKU exchanged within 90 days, capped at 10% of first order value.
- **Urgency:** Valid only for dealers who confirm stock before Diwali ordering deadline.
- **Painter Pull-Through:** Swatch sales team conducts a free painter meet at the dealer's shop within 15 days of stocking, with free sample pouches for attending painters.
- **Retention Hook:** Dealer earns loyalty credit on every Swatch Rustic litre sold, redeemable as free marketing material or co-branded shop signage.

**Why It Works:** The dealer does not take price risk. He gets footfall (painter meet), display support, and stock protection. Swatch does not cut MRP or DLP.

---

### Example 2: Painter Switching in Kota — From Local Distemper to Swatch Shine Interior Emulsion

**Situation:** A 5-member painter team in Kota uses a cheap local distemper brand for budget interior jobs. They believe emulsion is "too costly" and "not worth it for rental flats."

**Diagnostic Answers:**
- Target: Painter crew
- Current brand: Local distemper
- Pain point: Perceived high cost and fear of client pushback on price
- Margin floor: Pulled from ERP
- Non-price assets: Swatch Shine coverage demo, cost-per-square-foot comparison, free toolkit

**Offer Built:**

- **Lead Magnet:** Free 1-litre Swatch Shine trial bucket + free brush set for the crew head.
- **Tripwire:** First 20-litre job pack at standard painter price, with a free mixing paddle and masking tape bundle.
- **Core Offer:** Ongoing Swatch Shine supply with painter loyalty points per litre.
- **Risk Reversal:** If the client complains about finish in the first 30 days, Swatch provides free touch-up material.
- **Proof:** Side-by-side demo wall showing one-coat coverage vs. local distemper; testimonial from a Kota contractor who reduced repaint callbacks.
- **Urgency:** First 30 painters in Kota zone get a free branded T-shirt and entry into a quarterly tool raffle.

**Why It Works:** The painter's real fear is client rejection and extra effort. The offer removes both with proof, a trial, and a low-risk first job. No product price is cut.

---

## 10. REFERENCES

- `references/value_equation_diagram.png`: Visual of Hormozi’s value equation.
- `references/belfort_script_flowchart.pdf`: Step-by-step flow of the straight-line script.
- `references/grove_leading_indicators_table.csv`: Template for tracking daily sales KPIs.

---

**CEO Note:** This skill exists to win customers, not to win price wars. Every offer must increase perceived value, protect gross margin, and deepen the Swatch Paints distribution network. If an offer cannot pass the checklist, it does not launch.