decision_algorithm: |
  IF conflict type = Vertical (dealer vs. direct sales)
  THEN enforce ERP DLP floor + activate exclusive territory lock
  ELSE IF conflict type = Horizontal (dealer vs. dealer)
  THEN apply Tier-Based Escalation Protocol:
     IF A-tier dealer involved → immediate margin top-up + bonus incentive
     IF B-tier or C-tier → freeze credit line + initiate performance audit
  ELSE IF conflict type = Multi-Channel (online vs. offline)
  THEN deploy Dynamic Channel Pricing Engine:
     IF online channel exceeds 15% of total sales → cap volume at 30%
     IF offline dealer sales drop >20% YoY → trigger territory realignment

## Output Structure
```json
{
  "conflict_type": "vertical|horizontal|multi-channel",
  "resolution_strategy": "territory_lock|margin_top_up|channel_capping|realignment",
  "executive_action": [
    "freeze_credit_line_dealer_X",
    "adjust_DLP_for_SKU_Y",
    "assign_exclusive_zone_Z"
  ],
  "risk_score": 0-10,
  "expected_margin_impact": "+/- X%",
  "implementation_deadline": "YYYY-MM-DD"
}
```

## Examples

### Scenario 1: Contractor Direct Sales Bypass
- **Context**: A contractor in Udaipur orders 500 liters of Swatch Rustic directly from HQ, undercutting local dealer rates.
- **Diagnosis**: Vertical conflict – direct channel bypassing dealer.
- **Action**: Activate ERP territory lock for Udaipur zone. Freeze contractor’s direct access. Assign exclusive dealer (A-tier) with 5% margin top-up.
- **Outcome**: Dealer retention secured. Contractor redirected to official channel.

### Scenario 2: Dealer Price War in Jaipur
- **Context**: Two B-tier dealers in Jaipur’s industrial area undercut each other by 8%, triggering margin collapse.
- **Diagnosis**: Horizontal conflict – intra-channel price competition.
- **Action**: Freeze credit lines of both dealers. Initiate performance audit. Assign new exclusive zones with buffer zones.
- **Outcome**: Price stability restored. Margin recovery within 4 weeks.

## Failure Modes
- Ignoring ERP DLP floor → margin erosion
- Delayed territory realignment → prolonged conflict
- Overuse of margin top-ups → unsustainable cost center
- Misclassification of conflict type → wrong resolution path

## Checklist
- [ ] Confirm ERP DLP floor is enforced
- [ ] Validate dealer tier classification
- [ ] Audit channel access logs
- [ ] Apply buffer zones in overlapping territories
- [ ] Monitor post-resolution margin trends
- [ ] Update ERP conflict matrix weekly
- [ ] Escalate unresolved cases to Ashutosh Sharma Sir

---

> **Legend**: Philip Kotler
> **Department**: Distribution & Supply Chain Department
> **Focus**: Multichannel Logistics & Channel Conflicts
> **Status**: Active — validated by Ashutosh Sharma Sir
> **Last Updated**: 2026-09-26
> **Version**: 1.0
> **Author**: Hermes, CEO of Swatch Paints
> **Source**: Internal ERP data + Philip Kotler’s *Marketing Management*, Indian paint industry case studies
> **Validation Acknowledged By**: Ashutosh Sharma Sir (+919079609627)