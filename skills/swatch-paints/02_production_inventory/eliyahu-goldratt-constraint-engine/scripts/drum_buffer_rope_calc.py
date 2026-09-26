"""
Eliyahu Goldratt Drum-Buffer-Rope Bottleneck Scheduler
Swatch Paints Theory of Constraints Paint Manufacturing Throughput Engine
"""
from typing import Dict, Any, List

def calculate_dbr_schedule(bottleneck_capacity_liters_per_hr: float, 
                           work_orders: List[Dict[str, Any]], 
                           buffer_time_hours: float = 4.0) -> Dict[str, Any]:
    if bottleneck_capacity_liters_per_hr <= 0:
        raise ValueError("Bottleneck capacity must be > 0")
    if not work_orders:
        raise ValueError("Work orders list cannot be empty")

    schedule = []
    current_drum_time = 0.0
    total_throughput_liters = 0.0

    for wo in work_orders:
        wo_id = wo.get("id", "WO_UNKNOWN")
        liters = wo.get("liters", 0.0)
        drum_duration_hrs = liters / bottleneck_capacity_liters_per_hr
        
        # Rope release time = Drum start time minus buffer
        drum_start = current_drum_time
        drum_finish = drum_start + drum_duration_hrs
        rope_release_time = max(0.0, drum_start - buffer_time_hours)
        
        schedule.append({
            "order_id": wo_id,
            "liters": liters,
            "drum_duration_hrs": round(drum_duration_hrs, 2),
            "rope_material_release_hr": round(rope_release_time, 2),
            "drum_mill_start_hr": round(drum_start, 2),
            "drum_mill_finish_hr": round(drum_finish, 2)
        })
        
        current_drum_time = drum_finish
        total_throughput_liters += liters

    return {
        "bottleneck_resource": "High-Speed Bead Mill / Sand Mill",
        "total_throughput_liters": total_throughput_liters,
        "total_drum_time_hours": round(current_drum_time, 2),
        "buffer_size_hours": buffer_time_hours,
        "scheduled_orders_count": len(schedule),
        "schedule": schedule
    }

if __name__ == "__main__":
    orders = [{"id": "EMULSION_WHITE_1", "liters": 2500}, {"id": "PRIMER_RED_OXIDE", "liters": 1500}, {"id": "ENAMEL_GLOSS", "liters": 1000}]
    res = calculate_dbr_schedule(bottleneck_capacity_liters_per_hr=500, work_orders=orders, buffer_time_hours=3)
    assert res["total_throughput_liters"] == 5000.0
    assert res["total_drum_time_hours"] == 10.0
    print("Drum-Buffer-Rope Engine: All unit tests passed.")