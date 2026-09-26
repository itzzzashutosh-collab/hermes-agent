"""
Ford W. Harris Economic Order Quantity & Reorder Point Calculator
Swatch Paints Raw Material & Packaging Inventory Engine
"""
import math
from typing import Dict, Any

def calculate_eoq_and_rop(annual_demand: float, order_cost: float, holding_cost_pct: float, 
                          unit_cost: float, lead_time_days: float, 
                          daily_demand_std_dev: float = 0.0, service_factor: float = 1.65) -> Dict[str, Any]:
    if annual_demand <= 0 or order_cost <= 0 or holding_cost_pct <= 0 or unit_cost <= 0:
        raise ValueError("Annual demand, order cost, holding cost %, and unit cost must be > 0")
    if lead_time_days < 0:
        raise ValueError("Lead time days cannot be negative")

    holding_cost_per_unit = unit_cost * (holding_cost_pct / 100.0)
    eoq = math.sqrt((2 * annual_demand * order_cost) / holding_cost_per_unit)
    
    daily_demand = annual_demand / 365.0
    lead_time_demand = daily_demand * lead_time_days
    
    # Safety stock based on demand variability during lead time
    safety_stock = service_factor * daily_demand_std_dev * math.sqrt(lead_time_days) if lead_time_days > 0 else 0.0
    reorder_point = lead_time_demand + safety_stock
    
    orders_per_year = annual_demand / eoq
    annual_order_cost = orders_per_year * order_cost
    annual_holding_cost = (eoq / 2.0) * holding_cost_per_unit
    total_inventory_cost = annual_order_cost + annual_holding_cost

    return {
        "eoq_units": round(eoq, 2),
        "reorder_point_units": round(reorder_point, 2),
        "safety_stock_units": round(safety_stock, 2),
        "lead_time_demand_units": round(lead_time_demand, 2),
        "orders_per_year": round(orders_per_year, 2),
        "annual_order_cost": round(annual_order_cost, 2),
        "annual_holding_cost": round(annual_holding_cost, 2),
        "total_annual_inventory_cost": round(total_inventory_cost, 2)
    }

if __name__ == "__main__":
    res = calculate_eoq_and_rop(annual_demand=12000, order_cost=2500, holding_cost_pct=18, unit_cost=150, lead_time_days=7, daily_demand_std_dev=5)
    assert res["eoq_units"] > 0
    assert res["reorder_point_units"] > res["safety_stock_units"]
    print("EOQ & ROP Engine: All unit tests passed.")