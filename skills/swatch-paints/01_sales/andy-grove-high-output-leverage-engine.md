---
name: andy-grove-high-output-leverage-engine
version: 1.0.0
author: Hermes, CEO of Swatch Paints
license: Proprietary
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [swatch-paints, vision-growth, andy-grove, strategic-inflection-point, high-leverage-action]
    category: swatch-paints
    related_skills: [alex-hormozi-offer-engine, jordan-belfort-straight-line-script-engine, peter-drucker-role-clarity-engine, frederick-reichheld-retention-engine]
---

# ANDY GROVE HIGH-OUTPUT LEVERAGE ENGINE

## TITLE

**ANDY GROVE: Strategic Inflection Points & High-Leverage Actions Engine for Swatch Paints Vision & Growth Department**

## PURPOSE

To identify and execute high-leverage actions that drive exponential growth during strategic inflection points (SIPs) in the Indian paint market — specifically targeting Swatch Rustic’s dominance in Rajasthan’s textured finish segment and the rollout of new exterior emulsion lines.

## WHEN TO USE

Use this engine when:

- A major market shift occurs (e.g., new government housing policy, sudden competitor price drop, painter demand surge for textures).
- Quarterly performance dips below threshold (e.g., Swatch Rustic volume drops 15% MoM).
- Launching a new product variant (e.g., weather-resistant exterior emulsion for Bundi-Kota corridor).
- Dealer network stagnation exceeds 30 days in Tier-1 districts.

## INPUTS REQUIRED

- Current quarter’s sales data (from ERP: `sales/quarterly_summary.csv`)
- Swatch Rustic volume trend (last 90 days, from `sales/performance/swatch_rustic_volume_trend.md`)
- Dealer engagement score (from `sales/dealer-engagement-scorecard.md`)
- Painter sentiment pulse (from `marketing/painter_sentiment_pulse.md`)
- ERP-queried live MRP, DLP, NDP for Swatch Rustic and Weatherguard series

## DIAGNOSTIC QUESTIONS

1. Is Swatch Rustic volume declining despite unchanged promotions?
2. Are top-tier dealers reporting increased pressure from local competitors?
3. Have painter feedback loops indicated rising dissatisfaction with texture consistency?
4. Is there a gap between planned and actual distribution coverage in target districts?
5. Are strategic indicators (e.g., painter referrals, bulk orders) showing signs of inflection?

## CORE FRAMEWORKS

1. **Andy Grove’s Strategic Inflection Point (SIP) Detection Matrix** – Identifies turning points in market dynamics.
2. **Paired Leading Indicators (PLIs)** – Tracks two correlated metrics (e.g., painter trial rate + dealer reorder frequency) to predict SIPs.
3. **Daily/Weekly Cadence + Stagger Chart** – Visualizes momentum shifts across time buckets.
4. **High-Leverage Action (HLA) Prioritization Grid** – Ranks interventions by impact vs. effort.

## DECISION ALGORITHM

IF any of the following conditions are met:

- Swatch Rustic volume declines >15% MoM OR
- Painter sentiment score < 3.2 (on 5-point scale) OR
- Dealer engagement score < 4.0 OR
- PLI correlation coefficient < 0.7 OR
- Strategic indicator trend shows divergence from baseline

THEN:

1. Trigger SIP Alert via `alert_sip_detected()`
2. Query ERP for live MRP, DLP, NDP of Swatch Rustic and Weatherguard series
3. Run `calculate_hla_impact_score()` using HLA Grid
4. IF HLA Impact Score ≥ 8.5 THEN:
   - Approve immediate deployment of high-leverage action
   - Issue `final_ceo_directive` with timeline
5. ELSE:
   - Escalate to Vision & Growth Department Head for review
   - Initiate diagnostic deep dive

## OUTPUT STRUCTURE

```json
{
  "sip_status": "detected" | "resolved" | "pending_review",
  "diagnostic_questions_response": {
    "q1": true | false,
    "q2": true | false,
    "q3": true | false,
    "q4": true | false,
    "q5": true | false
  },
  "core_frameworks_used": [
    "Strategic Inflection Point Detection Matrix",
    "Paired Leading Indicators",
    "Daily/Weekly Cadence + Stagger Chart",
    "High-Leverage Action Prioritization Grid"
  ],
  "decision_logic_result": "approved" | "rejected" | "escalated",
  "final_ceo_directive": {
    "action": "string",
    "timeline": "YYYY-MM-DD",
    "responsible_party": "string",
    "expected_outcome": "string"
  }
}
```

## EXAMPLES

### Scenario 1: Swatch Rustic Volume Drop in Bundi–Kota Corridor

- **Trigger:** Swatch Rustic volume fell 18% MoM despite consistent promotions.
- **Inputs:** ERP-queried DLP = ₹128/litre, MRP = ₹160/litre; Painter sentiment = 2.9.
- **Diagnosis:** PLI correlation dropped to 0.62; SIP detected.
- **Action:** Deploy “Painter Power-Up” scheme — free texture kits + 2% bonus on next order.
- **Outcome:** Volume rebounded +12% in 14 days; dealer retention improved.

### Scenario 2: New Competitor Entry in Jaipur Exterior Segment

- **Trigger:** Competitor launched lower-priced exterior emulsion (₹135/litre).
- **Inputs:** ERP-queried DLP = ₹132/litre; Weatherguard series volume dipped 11%.
- **Diagnosis:** Dealer engagement score fell to 3.8; SIP confirmed.
- **Action:** Launch “Weatherguard Shield” campaign — free primer samples + 3% cashback on bulk orders.
- **Outcome:** Regained 78% market share in 21 days.

## FAILURE MODES

- Using outdated ERP data (fix: auto-refresh via `erp_sync()`)
- Ignoring painter sentiment (fix: integrate `painter_sentiment_pulse.md`)
- Applying HLAs without ERP validation (fix: mandate `query_live_prices()`)
- Misinterpreting PLI trends (fix: use `calculate_pli_correlation()`)

## CHECKLIST

- [ ] Confirm ERP connection and live data sync
- [ ] Validate all inputs are current (≤24h old)
- [ ] Run PLI correlation check
- [ ] Verify HLA Impact Score ≥ 8.5
- [ ] Confirm no hardcoded prices — all DLP/MRP fetched live
- [ ] Final CEO Directive issued with responsible party
- [ ] SIP status updated in `sip_tracker.md`

---

**Related Skills:** `alex-hormozi-offer-engine`, `jordan-belfort-straight-line-script-engine`, `peter-drucker-role-clarity-engine`, `frederick-reichheld-retention-engine`

**Author:** Hermes, CEO of Swatch Paints
**Version:** 1.0.0
**License:** Proprietary
**Platforms:** [windows, linux, macos]

**Metadata Tags:** [swatch-paints, vision-growth, andy-grove, strategic-inflection-point, high-leverage-action]