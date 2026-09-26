"""
Robert Kaplan & Robin Cooper Activity-Based Costing SKU Margin Engine
Swatch Paints SKU Contribution & Overhead Allocation Calculator
"""
from typing import Dict, Any

def calculate_sku_abc_margin(selling_price_per_ltr: float, direct_raw_material_cost: float, 
                             direct_packaging_cost: float, machine_grinding_hours: float, 
                             grinding_rate_per_hr: float, warehouse_storage_days: float, 
                             storage_rate_per_ltr_day: float, tinting_batches: int = 1, 
                             tinting_overhead_per_batch: float = 0.0) -> Dict[str, Any]:
    if selling_price_per_ltr <= 0:
        raise ValueError("Selling price must be > 0")

    prime_cost = direct_raw_material_cost + direct_packaging_cost
    activity_grinding_cost = machine_grinding_hours * grinding_rate_per_hr
    activity_storage_cost = warehouse_storage_days * storage_rate_per_ltr_day
    activity_tinting_cost = tinting_batches * tinting_overhead_per_batch
    
    total_activity_cost = activity_grinding_cost + activity_storage_cost + activity_tinting_cost
    fully_absorbed_cost = prime_cost + total_activity_cost
    
    gross_margin = selling_price_per_ltr - prime_cost
    gross_margin_pct = (gross_margin / selling_price_per_ltr) * 100.0
    
    net_abc_margin = selling_price_per_ltr - fully_absorbed_cost
    net_abc_margin_pct = (net_abc_margin / selling_price_per_ltr) * 100.0

    return {
        "selling_price_per_ltr": selling_price_per_ltr,
        "prime_direct_cost": round(prime_cost, 2),
        "activity_overheads_cost": round(total_activity_cost, 2),
        "fully_absorbed_unit_cost": round(fully_absorbed_cost, 2),
        "gross_margin": round(gross_margin, 2),
        "gross_margin_pct": round(gross_margin_pct, 2),
        "net_abc_margin": round(net_abc_margin, 2),
        "net_abc_margin_pct": round(net_abc_margin_pct, 2),
        "profitability_tier": "HIGH_PROFIT" if net_abc_margin_pct >= 25 else ("STANDARD" if net_abc_margin_pct >= 12 else "MARGIN_DANGER")
    }

if __name__ == "__main__":
    res = calculate_sku_abc_margin(selling_price_per_ltr=320, direct_raw_material_cost=180, direct_packaging_cost=25, machine_grinding_hours=0.05, grinding_rate_per_hr=200, warehouse_storage_days=15, storage_rate_per_ltr_day=0.5)
    assert res["gross_margin"] > 0
    assert res["net_abc_margin"] > 0
    print("ABC SKU Margin Engine: All unit tests passed.")