"""
Joseph Orlicky MRP BOM Explosion Engine
Swatch Paints Batch Formulation & Material Requirement Planning
"""
from typing import Dict, Any, List

def explode_paint_bom(batch_liters: float, bom_formula: Dict[str, float], 
                      current_stock: Dict[str, float] = None) -> Dict[str, Any]:
    if batch_liters <= 0:
        raise ValueError("Batch liters must be greater than 0")
    if not bom_formula:
        raise ValueError("BOM formula cannot be empty")
        
    current_stock = current_stock or {}
    total_ratio = sum(bom_formula.values())
    if abs(total_ratio - 100.0) > 0.01:
        raise ValueError(f"BOM formula percentages must sum to 100%. Got {total_ratio}%")

    requirements = {}
    shortages = {}
    
    for raw_mat, pct in bom_formula.items():
        gross_req_kg = round(batch_liters * (pct / 100.0), 3)
        available = current_stock.get(raw_mat, 0.0)
        net_req_kg = round(max(0.0, gross_req_kg - available), 3)
        
        requirements[raw_mat] = {
            "formula_pct": pct,
            "gross_req_kg": gross_req_kg,
            "current_stock_kg": available,
            "net_req_kg": net_req_kg,
            "status": "SUFFICIENT" if net_req_kg == 0.0 else "SHORTAGE"
        }
        if net_req_kg > 0:
            shortages[raw_mat] = net_req_kg

    return {
        "batch_liters": batch_liters,
        "raw_materials_count": len(bom_formula),
        "requirements": requirements,
        "shortages": shortages,
        "is_ready_for_production": len(shortages) == 0
    }

if __name__ == "__main__":
    emulsion_bom = {
        "Water": 35.0,
        "Titanium_Dioxide_TiO2": 20.0,
        "Extender_Calcite": 25.0,
        "Acrylic_Emulsion_Binder": 15.0,
        "Biocide_Additives": 5.0
    }
    stocks = {"Water": 10000, "Titanium_Dioxide_TiO2": 800, "Extender_Calcite": 2000, "Acrylic_Emulsion_Binder": 400, "Biocide_Additives": 200}
    res = explode_paint_bom(5000, emulsion_bom, stocks)
    assert "Titanium_Dioxide_TiO2" in res["requirements"]
    assert res["requirements"]["Titanium_Dioxide_TiO2"]["gross_req_kg"] == 1000.0
    assert res["shortages"]["Titanium_Dioxide_TiO2"] == 200.0
    print("MRP BOM Explosion Engine: All unit tests passed.")