# Postiz Sandbox (Stage 0) Offline Test Plan

**Document ID:** PLN-POSTIZ-TEST-01  
**Version:** 1.0.0  
**Testing Framework:** `pytest` in `hermes-agent\.venv` (Python 3.11)  
**Execution Mode:** 100% Offline / Zero Docker / Synthetic Fixtures  

---

## Test Scenarios & Safety Verification Suite

### Test Suite 1: Authentication & Connection
- **Test 1.1 (Valid API Key):** Mock server returns HTTP 200 with list of Swatch channels.
- **Test 1.2 (Missing / Expired Key):** Mock server returns HTTP 401 Unauthorized; Hermes raises controlled `PostizAuthError` without leaking key in stack trace.

### Test Suite 2: Post Creation & Validation
- **Test 2.1 (Valid Draft Post):** Creates post with `type: "draft"`, valid text, and channel ID. Returns HTTP 201 with `post_id`.
- **Test 2.2 (Schedule Timestamp in the Past):** Submitting a past date raises `ValueError` before making an API call.
- **Test 2.3 (Past Due Schedule):** Correctly calculates future ISO UTC timestamp for Rajasthan IST timezone (+05:30).

### Test Suite 3: Safety Guardrails & Prohibitions
- **Test 3.1 (Unapproved Technical Claim Block):** Content containing "100% waterproof" without attached BIS test certificate raises `ClaimEvidenceMissingError`.
- **Test 3.2 (Immediate Publishing Block):** Request with `type: "now"` is intercepted and rejected by Hermes safety middleware.
- **Test 3.3 (Wrong Account Block):** Request targeting an unverified personal channel ID is blocked by `AccountWhitelistValidator`.

### Test Suite 4: Rate Limiting & Resilience
- **Test 4.1 (Rate Limit Simulation):** Mock server returns HTTP 429 Too Many Requests; client implements exponential backoff and halts without crashing.
- **Test 4.2 (Network Timeout):** Simulates connection drop; client records `DRAFT_SAVED_LOCALLY` for human manual fallback.

---

## Success Criteria
- 10/10 automated tests passing in `postiz-integration/tests/`.
- Zero credentials committed or displayed.
- Complete audit trail preserved in `staged_posts.json`.
