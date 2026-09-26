"""
Warren Buffett Cash Flow & Moat Operating Float Engine
Swatch Paints Working Capital, DSO, DPO, and Net Cash Conversion Cycle Calculator
"""
from typing import Dict, Any

def calculate_cash_conversion_cycle(dso_days: float, dio_days: float, dpo_days: float, 
                                    annual_turnover: float) -> Dict[str, Any]:
    if annual_turnover <= 0:
        raise ValueError("Annual turnover must be > 0")
    if dso_days < 0 or dio_days < 0 or dpo_days < 0:
        raise ValueError("Days cannot be negative")

    # Net Cash Conversion Cycle = Days Sales Outstanding (Receivables) + Days Inventory Outstanding - Days Payables Outstanding
    ccc_days = (dso_days + dio_days) - dpo_days
    daily_revenue = annual_turnover / 365.0
    working_capital_tied_up = ccc_days * daily_revenue
    
    # Working capital float status: negative CCC means suppliers fund the business (Buffett Float)
    has_negative_working_capital_float = ccc_days < 0

    return {
        "dso_receivables_days": dso_days,
        "dio_inventory_days": dio_days,
        "dpo_payables_days": dpo_days,
        "net_cash_conversion_cycle_days": round(ccc_days, 1),
        "working_capital_tied_up": round(working_capital_tied_up, 2),
        "buffett_float_advantage": has_negative_working_capital_float,
        "liquidity_rating": "EXCELLENT_FLOAT" if ccc_days <= 15 else ("ACCEPTABLE" if ccc_days <= 45 else "CASH_TRAPPED")
    }

if __name__ == "__main__":
    res = calculate_cash_conversion_cycle(dso_days=42, dio_days=25, dpo_days=50, annual_turnover=50000000)
    assert res["net_cash_conversion_cycle_days"] == 17.0
    print("Cash Conversion Cycle & Float Engine: All unit tests passed.")