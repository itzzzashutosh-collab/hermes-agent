---
name: geoffrey-moore-chasm-scaling-engine
version: 1.0
author: Hermes, CEO of Swatch Paints
license: MIT
platforms: [windows]
category: Vision & Growth Department
metadata:
  hermes:
    tags: [scaling, chasm, bowling-pin, territory-expansion]
    description: Enables Swatch Paints to cross the Chasm in Rajasthan markets using Geoffrey Moore’s framework.
    related_skills: [alex-hormozi-offer-engine, jordan-belfort-straight-line-script-engine]
    config:
      department: Vision & Growth Department
---

# Geoffrey Moore Chasm Scaling Engine

## 1. TITLE

**GEOFFREY MOORE CHASM SCALING ENGINE**

## 2. PURPOSE

To enable Swatch Paints to systematically cross the Chasm between early adopters and mainstream market adoption in Tier-2 and Tier-3 Rajasthan towns by deploying targeted, high-leverage Bowling Pin Territory expansion tactics rooted in Moore’s Technology Adoption Life Cycle. This engine ensures scalable, margin-protected growth without diluting brand equity or overextending distribution capacity.

## 3. WHEN TO USE

Use this skill when:

- Entering a new district or city in Rajasthan where Swatch Paints has less than 15% market penetration
- Launching Swatch Rustic in a new painter cluster with no prior brand presence
- Observing stagnant sales velocity despite strong initial trial rates in a territory
- Planning expansion beyond existing dealer clusters into adjacent rural-urban zones
- Executing post-launch scaling campaigns after successful pilot launches (≤3 months)

## 4. INPUTS REQUIRED

- Current market penetration % in target territory (from ERP sales dashboard)
- Number of active painters using Swatch Rustic (from painter loyalty program logs)
- Dealer performance tier (A/B/C) in the zone (from ERP dealer classification matrix)
- Swatch Rustic trial conversion rate (last 30 days) from ERP campaign analytics
- Local competitor activity heatmap (from competitor-research/00_EXECUTIVE_SUMMARY_AND_COMPETITIVE_MATRIX.md)
- Live ERP database connection (for dynamic price lookup: MRP, DLP, NDP)

## 5. DIAGNOSTIC QUESTIONS

Answer each to determine stage of adoption lifecycle:

1. Are early adopter painters actively recommending Swatch Rustic to peers (>3 referrals/month)?
2. Is >60% of dealer inventory being sold within 45 days of delivery?
3. Are contractors placing bulk orders (>50 L) for Swatch Rustic?
4. Have we observed ≥3 consecutive months of declining trial-to-sale conversion?
5. Are local competitors offering volume discounts below Swatch’s DLP floor?

## 6. CORE FRAMEWORKS

- **Geoffrey Moore’s Chasm Framework** – Identifies the gap between innovators/early adopters and the early majority.
- **Bowling Pin Strategy** – Focuses resources on 3–5 high-potential painter clusters per district to dominate first, then expand outward.
- **Diffusion of Innovations Curve (Rogers)** – Used to classify painter personas and tailor messaging.

## 7. DECISION ALGORITHM

IF:
- Market penetration < 15%
- Trial conversion rate < 40%
- AND at least 3 diagnostic questions answered YES

THEN:
- Activate **Chasm Bridging Mode**:
  - Assign one dedicated Painter Champion per Bowling Pin cluster
  - Deploy Hormozi-style offer: “Buy 5 L, Get 1 L Free + ₹500 Painter Token”
  - Lock in exclusive territory rights for top 3 dealers (A-tier only)
  - Freeze credit terms for 90 days

ELSE IF:
- Market penetration ≥ 15%
- Dealer inventory turnover > 45 days
- AND 2 or fewer diagnostic questions YES

THEN:
- Activate **Mainstream Expansion Mode**:
  - Expand to adjacent districts using existing dealer network
  - Launch contractor incentive: “Order 200 L, Get 10 L Free + Free Roller Kit”
  - Introduce regional painter ambassador program (5 per district)
  - Allow limited credit (max 30 days) only for A-tier dealers

ELSE:
- Maintain **Status Quo Mode**:
  - Monitor ERP KPIs monthly
  - No new offers or territory expansions
  - Review diagnostics quarterly

## 8. OUTPUT STRUCTURE

Return a structured JSON payload with:

```json
{
  "recommendation": "Chasm Bridging Mode | Mainstream Expansion Mode | Status Quo Mode",
  "action_plan": [
    {
      "step": 1,
      "task": "Assign Painter Champion",
      "owner": "Marketing Dept Head",
      "deadline": "24 hours"
    },
    {
      "step": 2,
      "task": "Deploy Hormozi Offer",
      "owner": "Finance & Pricing Dept",
      "deadline": "48 hours"
    }
  ],
  "expected_impact": {
    "sales_growth": "15-25% in 60 days",
    "margin_preservation": "Maintained above 28%",
    "dealer_retention": "≥90% retention in Bowling Pin zones"
  },
  "erp_verification_required": [
    "MRP_DLP_NDP_lookup",
    "dealer_classification_status"
  ]
}
```

## 9. EXAMPLES

### Scenario 1: Churu District, Rajasthan

- **Context**: Swatch Rustic launched 2 months ago. Penetration: 8%. Trial conversion: 32%. 4 painters refer others monthly.
- **Diagnosis**: 4 YES answers → Chasm Bridging Mode triggered.
- **Action**: Assigned Painter Champion to Churu City Center cluster. Deployed “Buy 5 L, Get 1 L Free + ₹500 Token” offer. Locked A-tier dealer exclusivity.
- **Outcome**: Sales rose 22% in 58 days. Margin held at 29.1%. Painter referral rate increased to 6/month.

### Scenario 2: Udaipur Rural Zone

- **Context**: Swatch Rustic has 22% penetration. Inventory turnover: 60 days. No bulk contractor orders. 1 referral/month.
- **Diagnosis**: 2 YES answers → Mainstream Expansion Mode triggered.
- **Action**: Launched contractor incentive: “Order 200 L, Get 10 L Free + Free Roller Kit”. Activated regional ambassador program.
- **Outcome**: Contractor orders grew by 38% in 45 days. Dealer retention improved to 92%.

## 10. FAILURE MODES

- **Premature Scaling**: Expanding before crossing the Chasm → inventory pile-up, margin erosion.
- **Overpromising Offers**: Discounting below DLP floor → violates CEO Rule #1.
- **Ignoring Painter Champions**: No local advocates → weak demand pull.
- **Credit Risk Exposure**: Allowing credit to B/C-tier dealers → violates cash flow mandate.
- **Static Monitoring**: Not re-running diagnostics quarterly → missed inflection points.

## 11. CHECKLIST

✅ Confirm market penetration <15% OR ≥15% with lagging turnover
✅ Validate trial conversion rate and referral trends
✅ Query ERP for live MRP/DLP/NDP values
✅ Classify dealer tier (A/B/C)
✅ Run diagnostic questions (all 5)
✅ Trigger correct mode via decision algorithm
✅ Assign Painter Champion and lock territory
✅ Deploy offer via alex-hormozi-offer-engine
✅ Freeze credit terms (if applicable)
✅ Schedule next diagnostic review in 60 days

> **Note**: All prices and margins are dynamically pulled from the live ERP database. Hardcoded values are prohibited.
