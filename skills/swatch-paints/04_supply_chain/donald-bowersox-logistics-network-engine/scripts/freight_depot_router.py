"""
Donald Bowersox Logistics & Depot Optimization Calculator
Swatch Paints Freight Cost, Depot Replenishment & Truckload Router
"""
from typing import Dict, Any, List

def calculate_depot_freight_optimization(depots: List[Dict[str, Any]], 
                                         diesel_rate_per_km: float, 
                                         full_truckload_capacity_liters: float) -> Dict[str, Any]:
    if diesel_rate_per_km <= 0 or full_truckload_capacity_liters <= 0:
        raise ValueError("Diesel rate and truckload capacity must be > 0")

    depot_results = []
    total_freight_cost = 0.0
    total_liters_dispatched = 0.0

    for d in depots:
        name = d.get("depot_name", "UNKNOWN")
        distance_km = d.get("distance_km", 0.0)
        demand_liters = d.get("demand_liters", 0.0)
        
        trucks_needed = math.ceil(demand_liters / full_truckload_capacity_liters) if demand_liters > 0 else 0
        trip_cost = trucks_needed * distance_km * 2 * diesel_rate_per_km # Round-trip
        freight_per_liter = (trip_cost / demand_liters) if demand_liters > 0 else 0.0
        
        depot_results.append({
            "depot_name": name,
            "distance_km": distance_km,
            "demand_liters": demand_liters,
            "truckloads_needed": trucks_needed,
            "total_trip_cost": round(trip_cost, 2),
            "freight_cost_per_liter": round(freight_per_liter, 2)
        })
        
        total_freight_cost += trip_cost
        total_liters_dispatched += demand_liters

    avg_freight_per_liter = (total_freight_cost / total_liters_dispatched) if total_liters_dispatched > 0 else 0.0

    return {
        "full_truckload_capacity_liters": full_truckload_capacity_liters,
        "total_liters_dispatched": total_liters_dispatched,
        "total_freight_cost": round(total_freight_cost, 2),
        "average_freight_cost_per_liter": round(avg_freight_per_liter, 2),
        "depot_breakdown": depot_results
    }

if __name__ == "__main__":
    depot_list = [
        {"depot_name": "Bundi Depot", "distance_km": 40, "demand_liters": 4500},
        {"depot_name": "Jaipur Depot", "distance_km": 240, "demand_liters": 9500}
    ]
    res = calculate_depot_freight_optimization(depot_list, diesel_rate_per_km=35.0, full_truckload_capacity_liters=5000)
    assert res["total_freight_cost"] > 0
    assert res["average_freight_cost_per_liter"] > 0
    print("Freight Depot Router: All unit tests passed.")