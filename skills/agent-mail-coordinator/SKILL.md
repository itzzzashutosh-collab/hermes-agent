---
name: agent-mail-coordinator
description: "Asynchronous multi-agent coordination, advisory file reservations, and inter-department messaging engine for the 8 Swatch Paints departments. Prevents concurrent write collisions on ERP ledgers, batch tickets, and dispatch manifests using FastMCP + SQLite + Git audit ledger."
metadata:
  department: "All 8 Departments, 08_systems_sops"
  role: "Cross-Department Concurrency & Mailbox Orchestrator"
  version: "1.1.0"
  architecture: "14-Section Production Grade"
---

# Section 01: Metadata & Operational Identity
- **Specialization**: Inter-Agent Asynchronous Messaging, Concurrency Control, Advisory File Leases, Threaded Task Handoffs.
- **Scope**: Governing communications and state mutations across all 8 Swatch Paints enterprise departments.
- **Reporting Line**: Master coordination protocol administered by Department 08 (`08_systems_sops`).
- **Core Technology Stack**: FastMCP protocol, SQLite WAL with Full-Text Search (FTS5), Git audit ledger, advisory reservation leases.

# Section 02: The Multi-Department Concurrency Problem
In a live paint manufacturing business, autonomous sub-agents can create catastrophic race conditions if uncoordinated:
1. **Sales vs Finance**: `01_sales` attempts to approve a ₹3,00,000 dispatch invoice while `04_finance` is in the middle of recalculating the dealer's 45-day overdue balance.
2. **Production vs Inventory**: `02_production` commits a 2,000L batch ticket deducting 400 kg of Titanium Dioxide, while `03_inventory` is simultaneously allocating that same stock to another line.
3. **Dispatch vs Sales**: `07_vision_dispatch` updates vehicle loading manifests while `01_sales` is modifying delivery destinations.
4. **Resolution**: `agent-mail-coordinator` provides an asynchronous mailbox, structured threads, and advisory file reservations to prevent collisions and maintain complete auditability.

# Section 03: The Mailbox Architecture: Inboxes, Outboxes & Threads
1. Every department agent has a verified system identity:
   - `agent:sales` (`01_sales_legend`)
   - `agent:production` (`02_production_legend`)
   - `agent:inventory` (`03_inventory_legend`)
   - `agent:finance` (`04_finance_legend`)
   - `agent:marketing` (`05_marketing_council`)
   - `agent:hr` (`06_hr_admin`)
   - `agent:dispatch` (`07_vision_dispatch`)
   - `agent:systems` (`08_systems_sops` - Master Auditor)
   - `agent:overseer` (Ashutosh Sharma Sir - Human Executive)
2. Every inter-department communication is a structured message in an asynchronous SQLite inbox with a unique `thread_id`.
3. Messages retain full lineage: originating trigger, parent message ID, action state (`PENDING`, `ACKNOWLEDGED`, `RESOLVED`, `ESCALATED`).

# Section 04: Advisory File Reservations (Leases)
1. Before any agent modifies an ERP record, ledger file, batch ticket, or manifest, it must request an **advisory lease**:
   - Target resource (e.g., `erp/dealers/jaipur_modern_paints.json`).
   - Lease duration (default: 5 minutes / 300 seconds).
   - Intent note (e.g., "Updating outstanding ledger with ₹50,000 NEFT receipt").
2. If another agent holds an active lease, the requesting agent receives a `LEASE_BUSY` notification with the holder's ID and expiry timestamp.
3. The requesting agent enters a wait-state or re-queues the task, preventing dirty writes and conflicting state changes.
4. Auto-release mechanism: Once the writing operation succeeds, the lease is explicitly released via `release_lease()`.

# Section 05: Inter-Department Routing & Contact Policies
1. **Allowed Direct Routes**:
   - `agent:sales` <--> `agent:finance` (Credit checks, payment confirmation, invoice release).
   - `agent:production` <--> `agent:inventory` (RM requisition, shortage alerts, batch yields).
   - `agent:sales` <--> `agent:dispatch` (Delivery address, transporter assignment, urgent orders).
   - `agent:systems` <--> ALL AGENTS (SOP provisioning, compliance audits, performance tracking).
2. **Restricted Routes (Require `agent:systems` or `agent:overseer` clearance)**:
   - Changing raw material standard BOM formulas (`agent:production` cannot unilaterally alter recipe without QA & Overseer approval).
   - Writing off bad debts (`agent:sales` cannot cancel unpaid balances without `agent:finance` and `agent:overseer`).
   - Overriding minimum price floors (`agent:sales` cannot quote below contribution margin floor without `agent:finance` approval).

# Section 06: Department 08 Master Coordination Protocol
1. Department 08 (`systems_and_sops`) monitors the central mailbox continuously.
2. Tracks:
   - Open unacknowledged messages (>30 minutes triggers warning).
   - Unreleased file leases (>10 minutes triggers automated lease revocation).
   - Blocked inter-department handoffs (e.g. Sales waiting for Finance credit clearance).
3. Compiles inter-department telemetry into the 18:30 PM daily executive telegram scorecard:
   - Average inter-department response time.
   - Number of contentious lease requests successfully arbitrated.
   - Open pending approvals awaiting Ashutosh Sharma Sir's intervention.

# Section 07: Message Schemas & Payload Formatting
All agent messages follow strict JSON envelope standards:
```json
{
  "message_id": "msg_20260926_00142",
  "thread_id": "thread_dealer_modern_paints_4402",
  "from_agent": "agent:sales",
  "to_agent": "agent:finance",
  "priority": "HIGH",
  "subject": "Credit Override Request: Modern Paints Jaipur",
  "timestamp": "2026-09-26T12:45:00Z",
  "lease_held": "erp/dealers/modern_paints.json",
  "payload": {
    "dealer_id": "D-104",
    "current_outstanding": 240000,
    "current_credit_limit": 250000,
    "requested_order_value": 75000,
    "exposure_with_order": 315000,
    "reason": "Monsoon exterior stock requirement; ₹50,000 cheque clearing Monday"
  },
  "required_action": "APPROVE_OR_REJECT",
  "timeout_seconds": 1800
}
```

# Section 08: Human Overseer Interrupt & Telegram Escalations
1. When an inter-department task requires executive intervention (e.g., credit override > ₹1,00,000 or raw material substitute approval):
   - Message is copied to `agent:overseer`.
   - Dispatched immediately to Ashutosh Sharma Sir's Telegram with inline action buttons (`/approve` or `/reject`).
   - All sub-agents pause execution on that specific thread until Overseer responds.
2. If Overseer responds via Telegram:
   - Message is parsed by Hermes gateway.
   - Status updated in SQLite mailbox as `OVERSEER_APPROVED` or `OVERSEER_REJECTED`.
   - Dependent sub-agents are signaled to resume immediately.

# Section 09: Conflict Resolution & Pre-Commit Guards
1. If two agents attempt to claim a resource simultaneously:
   - Priority hierarchy resolves the conflict:
     `agent:overseer` > `agent:systems` > `agent:finance` > `agent:production` > `agent:sales` > `agent:inventory` > `agent:dispatch` > `agent:marketing`.
2. Git-backed pre-commit hooks ensure no file can be committed to the master branch without a valid registered reservation token.
3. Every commit must reference the originating `thread_id` and `message_id`.

# Section 10: Persistence Layer: SQLite FTS5 + Git Audit Ledger
1. The message database runs on SQLite with Full-Text Search (FTS5) enabled:
   - Instant search across all historical agent discussions, approvals, and decisions.
   - Search queries: `find_thread("Modern Paints")`, `list_overdue_approvals()`.
2. Every significant state change (BOM change, dealer credit limit modification, finished batch release) generates a signed Git commit log for permanent audit trails.
3. Nightly SQLite database backups synced to `C:/Users/itzzz/AppData/Local/hermes/backups`.

# Section 11: Disaster Recovery & Dead-Letter Handling
1. If an agent crashes or loses connectivity while holding an active file lease:
   - Heartbeat watchdog detects inactivity after 300 seconds.
   - Stale lease is quarantined into the dead-letter table.
   - Department 08 initiates automated state rollback to the last clean Git checkpoint.
   - Notification sent to Overseer: `⚠️ Dead-letter recovery executed for agent:sales on invoice #4402`.
2. Manual unlock tool: `python -m tools.agent_mail unlock --all` for emergency administrator overrides.

# Section 12: Anti-Patterns & Concurrency Traps
1. *The Infinite Wait Trap*: An agent blocked forever waiting for another agent's reply without a defined timeout. Every request must have a hard `timeout_seconds`.
2. *The Ghost Lease Trap*: Reserving a file and forgetting to release it after work completes. Always use `try...finally` lease release blocks.
3. *The Circular Deadlock*: Agent A holds Resource 1 and waits for Resource 2; Agent B holds Resource 2 and waits for Resource 1. Enforced by global lock ordering.
4. *The Silent Drop*: Discarding an unhandled message without marking it failed or returning an error acknowledgment.

# Section 13: Operational Telemetry & Daily Health Metrics
Department 08 publishes daily coordination metrics at 18:30 PM:
- Total cross-department messages exchanged.
- Average response latency per department (e.g., Finance average credit review: 4.2 minutes).
- Number of file lease contentions detected and avoided.
- Zero data corruption or dirty-write events recorded.
- Percentage of automated inter-department handoffs completed without human intervention.

# Section 14: Verification Checklist & Handshake Guarantees
Before any multi-agent transaction is considered complete:
1. Originating agent verifies lease acquisition.
2. Recipient agent sends explicit acknowledgment receipt.
3. Transaction payload passes schema validation.
4. Advisory lease is released and logged in the SQLite audit ledger.
5. System state is clean and consistent across all departmental records.
6. Audit trail is permanent and searchable via SQLite FTS5.
# Section 15: FastMCP Server DDL & SQLite Table Definitions
```sql
-- Central multi-agent mailbox schema
CREATE TABLE IF NOT EXISTS agent_inbox (
    message_id TEXT PRIMARY KEY,
    thread_id TEXT NOT NULL,
    from_agent TEXT NOT NULL,
    to_agent TEXT NOT NULL,
    priority TEXT NOT NULL DEFAULT 'NORMAL',
    subject TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    acknowledged_at TIMESTAMP
);

-- Advisory file reservation leases
CREATE TABLE IF NOT EXISTS file_reservations (
    resource_path TEXT PRIMARY KEY,
    held_by_agent TEXT NOT NULL,
    lease_expires_at TIMESTAMP NOT NULL,
    reason TEXT NOT NULL
);

-- Full text search index
CREATE VIRTUAL TABLE IF NOT EXISTS agent_inbox_fts USING fts5(
    message_id, thread_id, subject, payload_json
);
```

# Section 16: Multi-Department Race Condition Scenarios
## Scenario A: Simultaneous Order Booking & Credit Limit Breach
1. `agent:sales` attempts to reserve `erp/orders/ORD-9912.json`.
2. Simultaneously, `agent:finance` holds lease on `erp/dealers/modern_paints.json` recalculating unpaid ₹1.8L balance.
3. `agent:sales` receives `LEASE_BUSY` from `agent:finance`.
4. Order booking halts in `PENDING_CREDIT_REVIEW` state.
5. `agent:finance` completes ledger run, logs remaining credit limit (₹60,000).
6. Order value is ₹75,000 -> Auto-escalates to `agent:overseer` (Ashutosh Sharma Sir) on Telegram for ₹15k credit override.
7. Result: Zero bad debt slip, zero dirty write, complete audit trail.

# Section 17: Multi-Agent Handshake & Verification Guarantee
- [ ] Every agent has a verified identifier (`agent:<dept>`).
- [ ] Advisory leases mandatory before touching any ERP JSON/DB record.
- [ ] Dead-letter watchdog purges expired locks after 300 seconds.
- [ ] Ashutosh Sharma Sir maintains unilateral Telegram override authority.
# Section 18: Troubleshooting & Operational Diagnostics
## 18.1 Deadlock Resolution Algorithm
- If circular wait is detected by Department 08 watchdog:
  - Step 1: Force-release lowest priority agent's file lease.
  - Step 2: Roll back uncommitted transaction in SQLite journal.
  - Step 3: Queue retry after exponential backoff jitter (random 1-5 seconds).
  - Step 4: Log collision in system telemetry ledger.

## 18.2 Master Reset Command
- In catastrophic runtime stalls, administrator triggers:
  `python -m tools.agent_mail --reset-all-leases --notify-overseer`

# Section 19: Departmental Signoff & Governance History
- **Initial Author**: Swatch Paints Systems & Enterprise Architecture Team
- **Certified By**: Department 08 (Systems & SOPs Master Controller)
- **Executive Sponsor**: Ashutosh Sharma Sir (Managing Director)
- **Audit Schedule**: Monthly automated conformance checks via Hermes runtime
- **Deployment Status**: Production Active across Workspace & AppData runtimes
