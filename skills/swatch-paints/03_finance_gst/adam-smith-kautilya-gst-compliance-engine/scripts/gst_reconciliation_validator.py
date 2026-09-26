"""
Adam Smith & Kautilya GST Reconciliation Validator
Swatch Paints GSTR-2B ITC Matching & Tax Compliance Calculator
"""
from typing import Dict, Any, List

def reconcile_gstr2b_with_purchase_register(gstr2b_invoices: List[Dict[str, Any]], 
                                            purchase_register: List[Dict[str, Any]]) -> Dict[str, Any]:
    matched = []
    missing_in_2b = []
    value_mismatch = []
    
    pr_dict = {inv["invoice_number"].strip().upper(): inv for inv in purchase_register}
    gstr2b_dict = {inv["invoice_number"].strip().upper(): inv for inv in gstr2b_invoices}

    total_pr_itc = sum(inv.get("itc_amount", 0.0) for inv in purchase_register)
    eligible_2b_itc = 0.0

    for inv_no, pr_inv in pr_dict.items():
        if inv_no in gstr2b_dict:
            b2_inv = gstr2b_dict[inv_no]
            pr_tax = pr_inv.get("itc_amount", 0.0)
            b2_tax = b2_inv.get("itc_amount", 0.0)
            
            if abs(pr_tax - b2_tax) <= 1.0: # Tolerance of Rs. 1 for round-off
                matched.append(inv_no)
                eligible_2b_itc += b2_tax
            else:
                value_mismatch.append({
                    "invoice_number": inv_no,
                    "pr_tax": pr_tax,
                    "gstr2b_tax": b2_tax,
                    "difference": round(pr_tax - b2_tax, 2)
                })
        else:
            missing_in_2b.append({
                "invoice_number": inv_no,
                "vendor_gstin": pr_inv.get("vendor_gstin", "UNKNOWN"),
                "itc_blocked_amount": pr_inv.get("itc_amount", 0.0)
            })

    ineligible_itc = sum(x["itc_blocked_amount"] for x in missing_in_2b)

    return {
        "total_pr_invoices": len(purchase_register),
        "total_pr_itc_claimed": round(total_pr_itc, 2),
        "eligible_itc_in_2b": round(eligible_2b_itc, 2),
        "blocked_itc_missing_in_2b": round(ineligible_itc, 2),
        "matched_count": len(matched),
        "missing_in_2b_count": len(missing_in_2b),
        "value_mismatch_count": len(value_mismatch),
        "compliance_ratio_pct": round((eligible_2b_itc / total_pr_itc * 100.0) if total_pr_itc > 0 else 0.0, 2)
    }

if __name__ == "__main__":
    pr = [{"invoice_number": "INV-001", "vendor_gstin": "08AAACG1234F1Z1", "itc_amount": 18000.0},
          {"invoice_number": "INV-002", "vendor_gstin": "08AAACG9999F1Z9", "itc_amount": 9000.0}]
    b2 = [{"invoice_number": "INV-001", "vendor_gstin": "08AAACG1234F1Z1", "itc_amount": 18000.0}]
    res = reconcile_gstr2b_with_purchase_register(b2, pr)
    assert res["matched_count"] == 1
    assert res["missing_in_2b_count"] == 1
    print("GST Reconciliation Engine: All unit tests passed.")