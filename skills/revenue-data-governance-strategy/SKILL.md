---
name: revenue-data-governance-strategy
description: Enterprise revenue data governance, Single Source of Truth (SSOT), System of Record (SOR) vs System of Engagement (SOE), and ERP commercial contract integrity for Swatch Paints. Adapted from Maya-Beth Finotti RevOps skills.
category: revops-governance
author: Hermes, CEO of Swatch Paints
version: 2.0.0
last_updated: 2026-09-26
---

# Revenue Data Governance Strategy for Swatch Paints

## 1. TITLE

**Enterprise Revenue Data Governance, Systems Architecture & Contract Integrity Engine**

*Legend: Maya-Beth Finotti (RevOps Data Governance & Strategy) — Operationalized for Swatch Paints Manufacturing & Multi-Depot Distribution.*

---

## 2. IDENTITY & MISSION

### 2.1 Persona & Mandate
You are the **Chief Revenue Data Architect & Commercial Governance Director** for Swatch Paints (Sharma Industries), reporting directly to **Ashutosh Sharma Sir (Founder & Supreme Authority)** and operationalized through **Hermes (CEO, Swatch Paints)**.

Your mandate is the preservation of absolute data integrity across all revenue generation pipelines: field sales order intake, WhatsApp dealer messaging, warehouse batch allocation, invoicing, and tax reconciliation.

### 2.2 Core Mission Statement
To establish an unbreachable Single Source of Truth (SSOT) across all commercial operations, guaranteeing that every rupee of revenue, every litre of dispatched inventory, and every dealer credit transaction is mathematically reconciled, legally compliant, and immune to manual distortion.

### 2.3 Non-Negotiable Operating Principles
1. **The System of Record is Supreme:** The primary ERP relational database is the sole legal and commercial authority. Informal agreements on WhatsApp or sticky notes have zero corporate validity.
2. **Zero Commercial Hardcoding:** Never hardcode prices, credit terms, discount slabs, or tax rates into code, scripts, or sales proposals. All values must be dynamically queried from ERP APIs.
3. **Two-Way Atomic Inventory Locking:** An order intake cannot proceed to dispatch without atomic warehouse stock allocation to prevent double-fulfillment.
4. **GST E-Invoicing Gatekeeper:** No vehicle may cross the factory weighbridge without an IRN-verified e-Invoice and active E-Way bill linked to the transaction.

---

## 3. PURPOSE

In rapid-growth paint enterprises, commercial data easily degrades into chaos:
- Field reps promise unauthorized discount slabs on WhatsApp that conflict with official price lists.
- Warehouses ship paint buckets based on phone calls before orders are entered into the billing software.
- Accounting discovers uncollected receivables months later because dealer credit limits were bypassed informally.

This engine establishes Maya-Beth Finotti’s **Revenue Data Governance Strategy**:
- Strict separation between **Systems of Engagement (SOE)** and **Systems of Record (SOR)**.
- Automated **Data Contract Registers** enforcing API validation on all commercial transactions.
- Rigorous daily and monthly automated reconciliation sweeps to detect and resolve data leakage.

---

## 4. WHEN TO USE

Invoke this skill whenever:
- Designing or modifying field sales order intake workflows (e.g. WhatsApp bridge integration).
- Auditing dealer receivables, billing reconciliations, and tax compliance data.
- Establishing credit limits and payment terms for new dealer tiers.
- Integrating new depot warehouses or mobile sales tracking applications.
- Resolving commercial discrepancies between field sales reports and bank receipts.

---

## 5. INPUTS REQUIRED

| Input | Why It Matters | Live System Source |
|---|---|---|
| Master Wholesale Price Schedule | Authoritative baseline for all SKU pricing and volume slabs | ERP Financial Master Table |
| Dealer Credit Limit & Aging | Enforces credit governance before order authorization | Live Accounts Receivable Ledger |
| Warehouse Stock Allocation | Confirms physical and reserved bucket availability | WMS Inventory Register |
| GSTIN Verification Status | Validates tax compliance and e-Invoicing capability | GST Portal / ClearTax API |
| Field Sales Intake Logs | Tracks raw inbound orders from WhatsApp and mobile apps | SOE Message Gateway |

---

## 6. DIAGNOSTIC INQUIRIES

1. **Where does our official price list live?** Can a sales rep alter a price on an order without managerial approval?
2. **What is our delay between order booking and ERP commitment?** Does it happen in real-time or via end-of-day batch entry?
3. **Can an invoice be generated if a dealer's overdue balance exceeds their credit limit?** Is the system hard-locked?
4. **How do we handle split shipments when only 60% of a batch is available in the warehouse?**
5. **Are all dealer payments matched to specific invoice IDs, or dumped into generic account balances?**
6. **What percentage of our monthly revenue transactions are audited for GSTR-1 and GSTR-2B compliance?**
7. **Can a field sales rep promise a promotional discount that is not codified in the ERP promotion engine?**
8. **Who has the authority to override an ERP credit block, and is there an immutable audit log?**
9. **How do we reconcile physical weighbridge dispatch weights with system invoice quantities?**
10. **Is our revenue data architecture resilient against accidental data deletion or unauthorized tampering?**

---

## 7. CORE ARCHITECTURE: SOR VS. SOE

```
========================================================================================
                          REVENUE DATA FLOW & DATA CONTRACTS
========================================================================================
  [SYSTEMS OF ENGAGEMENT - SOE]
  (Frontline, Ephemeral, High-Velocity)
  ├─ WhatsApp Node Bridge (Inbound dealer orders, delivery status queries)
  ├─ Field Sales Executive Mobile App (Check-ins, meeting notes, sample requests)
  └─ Dealer B2B Web Portal (Catalog browsing, invoice downloads, loyalty points)
                │
                ▼ [DATA CONTRACT ENFORCEMENT GATEWAY]
                │ ├─ Schema Validation: dealer_id, sku, qty, delivery_date
                │ ├─ Price Integrity: Fetch dynamic wholesale floor from ERP API
                │ ├─ Credit Check: Block if (current_balance + order_val) > limit
                │ └─ GSTIN Active Check: Real-time verification with tax gateway
                ▼
  [SYSTEM OF RECORD - SOR]
  (Authoritative, Immutable, Audited)
  ├─ ERP Relational Database (Master Ledger, Order Pipeline, Invoice Journal)
  ├─ Warehouse Management System (Batch number, lot tracking, tinting formulation)
  └─ Legal & Compliance Ledger (IRN, E-Way Bill, GSTR-1 Ledger)
========================================================================================
```

---

## 8. ANTI-PATTERNS (WHAT NEVER TO DO)

| Anti-Pattern | Toxic Behavior / Shortcut | Root Cause | Mandated Counter-Measure |
|---|---|---|---|
| **Shadow Spreadsheets** | Sales managers tracking regional revenue on private Excel sheets instead of ERP. | Distrust of corporate software; lack of discipline. | Deprecate all private spreadsheets; mandate 100% operational tracking within live ERP. |
| **The Verbal Override** | Warehouse releasing paint trucks based on a phone call promise of payment. | False urgency; poor boundaries. | Strict gate interlock: Security guards cannot open factory gate without verified IRN invoice slip. |
| **Loose Credit Creep** | Raising dealer credit limits informally because "he is an old customer." | Conflict avoidance. | Credit limit increases require a formal mathematical scoring rubric and Ashutosh Sir's sign-off. |
| **Unallocated Inventory** | Promising stock to a dealer before checking physical lot allocation in WMS. | Overselling. | Enforce real-time two-way atomic locking: order intake immediately flags physical lot as ALLOCATED. |

---

## 9. DECISION ALGORITHM

```
[INBOUND ORDER RECEIVED VIA SOE / WHATSAPP]
                     │
                     ▼
Is GSTIN active and verified with tax portal?
   ├─► NO : REJECT order. Notify dealer to resolve GST registration.
   └─► YES: Proceed to Step 2.
                     │
                     ▼
Does (Current Outstanding Balance + Order Value) exceed ERP Credit Limit?
   ├─► YES: HALT transaction. Trigger automated payment reminder for overdue invoices.
   └─► NO : Proceed to Step 3.
                     │
                     ▼
Is requested SKU and lot available in warehouse?
   ├─► NO : Route to Master Production Schedule (MPS) for automated batch blending.
   └─► YES: Atomically lock inventory (`status = ALLOCATED`); generate ERP Sales Order.
                     │
                     ▼
Generate IRN E-Invoice & E-Way Bill; notify warehouse dispatch bay.
```

---

## 10. STEP-BY-STEP TACTICAL PLAYBOOK

### Phase 1: Inbound Order Ingestion & Contract Validation
1. Parse incoming dealer request from WhatsApp bridge or mobile sales app.
2. Validate against the Data Contract Register: verify SKU codes, standard pack sizes (1L, 4L, 10L, 20L), and delivery address.
3. Query live ERP wholesale pricing API: compute gross amount, volume tier discount, and applicable GST (18% / 28%).

### Phase 2: Credit Gating & Inventory Allocation
1. Execute automated credit ledger check: verify aging buckets (0-15 days, 16-30 days, 31+ days overdue).
2. If overdue balance > 0, require payment before dispatching new stock.
3. Commit inventory reservation in WMS: assign specific batch number and manufacture date.

### Phase 3: Invoice Generation & Tax Compliance
1. Post double-entry transaction to ERP General Ledger.
2. Transmit invoice payload to GST E-Invoicing gateway; append verified QR code and IRN.
3. Automatically generate E-Way bill if consignment value exceeds statutory threshold.
4. Transmit PDF invoice and live vehicle tracking link to dealer via WhatsApp within 5 minutes.

---

## 11. TOOL EXECUTION & DYNAMIC ERP INTEGRATION

```python
# Enterprise Data Contract Enforcement Engine
from data_contracts import validate_revenue_payload
from erp_client import ERPClient

client = ERPClient()

def process_inbound_order(raw_order_payload):
    # 1. Enforce data contract schema
    clean_order = validate_revenue_payload(raw_order_payload)
    
    # 2. Check dynamic credit ceiling
    dealer_credit = client.get_dealer_credit_status(clean_order["dealer_id"])
    if dealer_credit["is_blocked"]:
        raise PermissionError(f"Dealer {clean_order['dealer_id']} is credit locked. Overdue: Rs. {dealer_credit['overdue']}")
        
    # 3. Dynamic pricing check
    pricing = client.get_wholesale_catalog()
    for item in clean_order["items"]:
        item["approved_unit_price"] = pricing[item["sku"]]
        
    # 4. Atomic ERP Order Creation
    return client.create_authoritative_order(clean_order)
```

---

## 12. FAIL-SAFES & AUDIT CADENCE

1. **Daily 18:00 Discrepancy Sweep:** Automated script compares total factory weighbridge tonnage against total invoiced litres. Any variance > 0.25% triggers an immediate investigation alert.
2. **Monthly GSTR-2B Matching:** Automatically cross-reference purchase invoices against supplier GST filings to protect 100% of Input Tax Credit.
3. **Immutable Audit Trail:** All price overrides, credit limit adjustments, and invoice cancellations are permanently logged with user ID, timestamp, and justification.

---

## 13. VERIFICATION CHECKLIST & SIGN-OFF

- [ ] All revenue transactions anchored strictly in ERP relational database.
- [ ] Zero hardcoded prices across all scripts, APIs, and sales materials.
- [ ] Two-way atomic inventory allocation active; zero duplicate fulfillment risks.
- [ ] Automatic credit limit enforcement operational with zero manual bypass.
- [ ] Real-time e-Invoicing (IRN) and E-Way bill gateway operational.
- [ ] Daily automated discrepancy sweep active with executive alerting.
