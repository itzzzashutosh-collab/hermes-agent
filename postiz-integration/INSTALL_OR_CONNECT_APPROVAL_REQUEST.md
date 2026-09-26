# Postiz Integration Approval Request

**Document ID:** REQ-POSTIZ-APP-01  
**Target Authority:** Boss Ashutosh Sharma (Owner, Swatch Paints)  
**Governance Standard:** Level 5 Owner Sign-off Pre-Requisite  

---

## 1. Scope of Proposed Implementation
1. **Architecture:** Implement a **100% Native Python Postiz Connector** inside `hermes-agent` (Zero Docker requirement).
2. **Phase 1 (Immediate):** Offline Mock Sandbox (`Stage 0`) with 100% automated test coverage. Zero external network calls.
3. **Phase 2 (Subsequent):** Connect to Postiz Cloud or self-hosted API using a scoped API key stored in `.env.secret`.
4. **Publishing Mode:** **Draft and Schedule Only**. Auto-publishing (`type: "now"`) is permanently disabled.

---

## 2. Risk & Impact Assessment

| Risk Area | Risk Level | Built-in Mitigation |
| :--- | :--- | :--- |
| **Accidental Live Post** | **ZERO in Sandbox** | Stage 0 runs against offline mock server. Live API blocked until Stage 2. |
| **Wrong Account Posting** | **LOW** | Whitelist validator rejects any account ID not belonging to Swatch Paints. |
| **Misleading Product Claims** | **CONTROLLED** | Strict gate: Wing 1.5 QC / BIS evidence required before content leaves draft. |
| **Cost / Resource Overhead** | **NEGLIGIBLE** | Zero Docker containers; runs natively in existing Python virtual environment. |

---

## 3. Owner Decision Required

Please review and select the desired execution pathway:

- [ ] **OPTION A (Recommended): APPROVE STAGE 0 SANDBOX BUILD**  
  *Build the native Hermes Postiz connector, mock engine, and safety test suite completely inside Hermes without Docker and without live accounts.*
- [ ] **OPTION B: HUMAN-OPERATED PILOT ONLY**  
  *Hermes generates captions and briefs in Markdown; human marketing executive manually copies and schedules inside Postiz UI.*
- [ ] **OPTION C: DEFER SOCIAL INTEGRATION**  
  *Focus exclusively on B2B field sales and SKU costing before onboarding social scheduling.*

---
**Decision Recorded By:** _________________________  
**Date:** _________________________  
