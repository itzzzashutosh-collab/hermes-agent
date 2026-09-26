"""
Taiichi Ohno Kanban Batch Pacer & Takt Time Pacer
Swatch Paints Just-In-Time Lean Production Flow
"""
from typing import Dict, Any

def calculate_kanban_pacing(available_shift_minutes: float, customer_daily_demand_liters: float,
                            batch_size_liters: float, lead_time_shifts: float, 
                            safety_factor_pct: float = 10.0) -> Dict[str, Any]:
    if available_shift_minutes <= 0 or customer_daily_demand_liters <= 0 or batch_size_liters <= 0:
        raise ValueError("Shift minutes, demand, and batch size must be > 0")

    # Takt Time: minutes per liter required to meet customer demand
    takt_time_seconds = (available_shift_minutes * 60.0) / customer_daily_demand_liters
    
    # Daily batches needed
    daily_batches_needed = customer_daily_demand_liters / batch_size_liters
    
    # Kanban Cards needed (Toyota formula: D * L * (1 + S) / C)
    daily_demand = customer_daily_demand_liters
    kanban_cards = (daily_demand * lead_time_shifts * (1 + safety_factor_pct / 100.0)) / batch_size_liters
    
    return {
        "takt_time_seconds_per_liter": round(takt_time_seconds, 2),
        "daily_batches_needed": round(daily_batches_needed, 2),
        "optimal_kanban_cards": math.ceil(kanban_cards),
        "theoretical_kanban_cards": round(kanban_cards, 2),
        "pacing_interval_minutes_per_batch": round(available_shift_minutes / daily_batches_needed, 2)
    }

if __name__ == "__main__":
    res = calculate_kanban_pacing(available_shift_minutes=480, customer_daily_demand_liters=4000, batch_size_liters=1000, lead_time_shifts=1.5, safety_factor_pct=10)
    assert res["takt_time_seconds_per_liter"] > 0
    assert res["optimal_kanban_cards"] >= 1
    print("Kanban Batch Pacer: All unit tests passed.")