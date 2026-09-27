- **Andon Cord Principle**: Immediate stoppage

## DECISION ALGORITHM
IF (Observation made at Gemba AND problem is visible AND process deviation exists) THEN
  IF (Issue is resolvable by floor team) THEN
    Issue a STOP WORK ORDER (via ERP mobile app)
    Assign corrective action to responsible operator
    Set 1-hour resolution deadline
    Log in Gemba Tracker (ERP)
  ELSE IF (Issue requires engineering/procurement) THEN
    Escalate via Andon Signal (red light + SMS to supervisor)
    Create high-priority ticket in ERP with severity tag: CRITICAL
    Notify Head of Operations & Quality Assurance
    Set 4-hour SLA for response
ELSE
  Log observation as "Observation Only" in Gemba Tracker
  Tag with "No Immediate Action Required"

## OUTPUT STRUCTURE
- **Gemba Observation Report** (ERP-formatted JSON payload):
  - timestamp: ISO8601
  - location: Workshop/Area/Station
  - observer: Full Name, Role, Employee ID
  - issue_category: Process, Tool, Material, Safety, Waste
  - severity: LOW/MEDIUM/HIGH/CRITICAL
  - resolution_status: RESOLVED/ESCALATED/PENDING
  - resolution_time: HH:MM (if resolved)
  - corrective_action: Free-text description
  - ERP_ticket_ref: Unique ID (auto-generated)
  - attachments: [image_urls, video_links] (if any)

## EXAMPLES

### Scenario 1: Batch Rejection Due to Incorrect Additive Ratio
- **Context**: During a Wednesday shift, a batch of Swatch Rustic exterior emulsion failed viscosity test.
- **Gemba Observation**: Operator noticed inconsistent mixing speed on Mixer #3.
- **Diagnostic Check**: Issue visible at Gemba → Yes. Caused by misaligned timer on control panel → Yes. Resolvable by floor team → Yes.
- **Action Taken**: STOP WORK ORDER issued. Timer recalibrated. Batch restarted after validation.
- **Outcome**: 12% yield loss avoided. Resolution time: 47 minutes. ERP ticket closed.

### Scenario 2: Conveyor Belt Jam in Packaging Line
- **Context**: Friday morning, packaging line halted due to plastic wrap jam.
- **Gemba Observation**: Supervisor saw tangled film near roller.
- **Diagnostic Check**: Issue visible at Gemba → Yes. Caused by worn roller bearing → Yes. Requires procurement → Yes.
- **Action Taken**: Andon Signal triggered (red light + SMS to maintenance). Ticket raised: CRITICAL. Procurement notified.
- **Outcome**: Line resumed in 3 hours. Spare part ordered. Prevented 2-day shutdown.

## FAILURE MODES
- **Failure to Document**: Observations not logged → Risk: Recurring issues, audit failure.
- **Delayed Escalation**: Critical issues not escalated within SLA → Risk: Production halt, quality breach.
- **Incorrect Severity Tagging**: Low-severity issues tagged HIGH → Risk: Resource misallocation.
- **No Follow-Up**: Resolution not verified → Risk: False closure, recurrence.

## CHECKLIST
- [ ] Confirm shift schedule is current
- [ ] Pull latest ERP batch log
- [ ] Verify inventory reconciliation report is ≤24h old
- [ ] Review maintenance ticket log for unresolved items
- [ ] Collect operator feedback from last 7 days
- [ ] Conduct walk-through with team leads
- [ ] Log all observations in ERP Gemba Tracker
- [ ] Escalate CRITICAL issues within 15 mins
- [ ] Close all resolved tickets within 1 hour
- [ ] Archive report to D:\Sharma Industries Erp Software\audit\gemba\YYYY-MM-DD\