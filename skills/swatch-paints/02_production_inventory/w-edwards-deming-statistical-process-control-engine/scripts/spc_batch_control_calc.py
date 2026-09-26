"""
W. Edwards Deming SPC Batch Quality Control Calculator
Swatch Paints Paint Viscosity & Opacity Statistical Process Control
"""
import math
from typing import List, Dict, Any

def calculate_spc_control_limits(batch_samples: List[float], spec_lsl: float, spec_usl: float) -> Dict[str, Any]:
    n = len(batch_samples)
    if n < 5:
        raise ValueError("At least 5 batch samples required for valid SPC limits")
    if spec_usl <= spec_lsl:
        raise ValueError("USL must be strictly greater than LSL")

    mean = sum(batch_samples) / n
    variance = sum((x - mean) ** 2 for x in batch_samples) / (n - 1)
    std_dev = math.sqrt(variance)

    # 3-Sigma Shewhart / Deming Control Limits
    ucl = mean + 3 * std_dev
    lcl = max(0.0, mean - 3 * std_dev)

    # Process Capability Indices (Cp & Cpk)
    cp = (spec_usl - spec_lsl) / (6 * std_dev) if std_dev > 0 else float('inf')
    cpk = min((spec_usl - mean) / (3 * std_dev), (mean - spec_lsl) / (3 * std_dev)) if std_dev > 0 else float('inf')

    out_of_control = [x for x in batch_samples if x > ucl or x < lcl]
    
    return {
        "sample_count": n,
        "mean": round(mean, 3),
        "std_dev": round(std_dev, 3),
        "ucl_upper_control_limit": round(ucl, 3),
        "lcl_lower_control_limit": round(lcl, 3),
        "cp_capability": round(cp, 3),
        "cpk_capability": round(cpk, 3),
        "process_status": "CAPABLE" if cpk >= 1.33 else ("ACCEPTABLE" if cpk >= 1.0 else "UNSTABLE_VARIATION"),
        "out_of_control_count": len(out_of_control)
    }

if __name__ == "__main__":
    viscosity_samples = [102.5, 104.0, 101.8, 103.2, 105.1, 102.9, 103.8, 104.5]
    res = calculate_spc_control_limits(viscosity_samples, spec_lsl=95.0, spec_usl=110.0)
    assert res["mean"] > 100
    assert res["cpk_capability"] > 1.0
    print("SPC Batch Control Engine: All unit tests passed.")