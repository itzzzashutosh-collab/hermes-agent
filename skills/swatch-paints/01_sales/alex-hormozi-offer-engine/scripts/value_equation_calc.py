import math
import unittest
from typing import Dict, Any


def calculate_dealer_value_equation(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Alex Hormozi's Acquisition & Value Equation for a Swatch Paints dealer.

    Calculates:
      - Customer Acquisition Cost (CAC)
      - Economic Order Quantity (EOQ)
      - Safety stock / reorder point
      - SPC control limits on monthly demand
      - Contribution margin, annual net contribution, LTV
      - Value Equation Score: (LTV - CAC) / CAC

    Required keys in inputs:
      annual_demand_units: int/float
      unit_cost: float
      selling_price: float
      order_cost: float
      holding_cost_rate: float (e.g. 0.25 for 25% annually)
      lead_time_days: int/float
      demand_stddev: float
      service_level_z: float (e.g. 1.65 for 95%)
      acquisition_spend: float
      new_dealers_acquired: int/float
      churn_rate: float (annual, e.g. 0.10)
      gross_margin_rate: float (optional; if omitted, derived from price/cost)
    """
    required = [
        "annual_demand_units",
        "unit_cost",
        "selling_price",
        "order_cost",
        "holding_cost_rate",
        "lead_time_days",
        "demand_stddev",
        "service_level_z",
        "acquisition_spend",
        "new_dealers_acquired",
        "churn_rate",
    ]
    missing = [k for k in required if k not in inputs]
    if missing:
        raise ValueError(f"Missing required inputs: {missing}")

    D = float(inputs["annual_demand_units"])
    c = float(inputs["unit_cost"])
    p = float(inputs["selling_price"])
    S = float(inputs["order_cost"])
    h_rate = float(inputs["holding_cost_rate"])
    L = float(inputs["lead_time_days"])
    sigma_d = float(inputs["demand_stddev"])
    z = float(inputs["service_level_z"])
    spend = float(inputs["acquisition_spend"])
    dealers = float(inputs["new_dealers_acquired"])
    churn = float(inputs["churn_rate"])

    if D < 0:
        raise ValueError("annual_demand_units must be non-negative")
    if c < 0 or p < 0:
        raise ValueError("unit_cost and selling_price must be non-negative")
    if S < 0:
        raise ValueError("order_cost must be non-negative")
    if not (0 <= h_rate <= 1):
        raise ValueError("holding_cost_rate must be between 0 and 1")
    if L < 0:
        raise ValueError("lead_time_days must be non-negative")
    if sigma_d < 0:
        raise ValueError("demand_stddev must be non-negative")
    if dealers <= 0:
        raise ValueError("new_dealers_acquired must be positive")
    if not (0 <= churn < 1):
        raise ValueError("churn_rate must be in [0, 1)")

    gross_margin_rate = float(
        inputs.get("gross_margin_rate", (p - c) / p if p else 0.0)
    )
    if not (0 <= gross_margin_rate <= 1):
        raise ValueError("gross_margin_rate must be between 0 and 1")

    contribution_margin_per_unit = p - c
    if contribution_margin_per_unit < 0:
        raise ValueError("selling_price must be >= unit_cost for positive contribution")

    H = h_rate * c
    eoq = math.sqrt((2 * D * S) / H) if H > 0 else 0.0

    daily_demand = D / 365.0
    sigma_lt = sigma_d * math.sqrt(L / 365.0) if L > 0 else 0.0
    safety_stock = z * sigma_lt
    reorder_point = daily_demand * L + safety_stock

    monthly_demand = D / 12.0
    monthly_std = sigma_d / math.sqrt(12.0)
    spc_ucl = monthly_demand + 3 * monthly_std
    spc_lcl = max(monthly_demand - 3 * monthly_std, 0.0)

    cac = spend / dealers
    avg_customer_lifespan_years = 1.0 / churn if churn > 0 else float("inf")
    annual_gross_profit = D * contribution_margin_per_unit
    annual_holding_cost = (eoq / 2.0 + safety_stock) * H
    annual_net_contribution = annual_gross_profit - annual_holding_cost
    ltv = annual_net_contribution * avg_customer_lifespan_years
    value_equation_score = (ltv - cac) / cac if cac > 0 else float("inf")
    payback_years = cac / annual_net_contribution if annual_net_contribution > 0 else float("inf")

    return {
        "status": "success",
        "inputs": inputs,
        "gross_margin_rate": round(gross_margin_rate, 4),
        "contribution_margin_per_unit": round(contribution_margin_per_unit, 2),
        "eoq": round(eoq, 2),
        "holding_cost_per_unit_per_year": round(H, 2),
        "safety_stock": round(safety_stock, 2),
        "reorder_point": round(reorder_point, 2),
        "spc_monthly_ucl": round(spc_ucl, 2),
        "spc_monthly_lcl": round(spc_lcl, 2),
        "customer_acquisition_cost": round(cac, 2),
        "avg_dealer_lifespan_years": round(avg_customer_lifespan_years, 2) if churn > 0 else float("inf"),
        "annual_gross_profit": round(annual_gross_profit, 2),
        "annual_holding_cost": round(annual_holding_cost, 2),
        "annual_net_contribution": round(annual_net_contribution, 2),
        "lifetime_value": round(ltv, 2),
        "value_equation_score": round(value_equation_score, 4),
        "payback_period_years": round(payback_years, 2),
    }


class TestDealerValueEquation(unittest.TestCase):
    def _base_inputs(self) -> Dict[str, Any]:
        return {
            "annual_demand_units": 2400,
            "unit_cost": 120.0,
            "selling_price": 180.0,
            "order_cost": 250.0,
            "holding_cost_rate": 0.22,
            "lead_time_days": 14.0,
            "demand_stddev": 50.0,
            "service_level_z": 1.65,
            "acquisition_spend": 120000.0,
            "new_dealers_acquired": 30.0,
            "churn_rate": 0.10,
        }

    def test_success_path(self):
        result = calculate_dealer_value_equation(self._base_inputs())
        self.assertEqual(result["status"], "success")
        self.assertAlmostEqual(result["contribution_margin_per_unit"], 60.0)
        self.assertAlmostEqual(result["customer_acquisition_cost"], 4000.0)
        self.assertAlmostEqual(result["lifetime_value"], 1407591.95, places=0)
        self.assertGreater(result["value_equation_score"], 0)

    def test_missing_input_raises(self):
        inputs = self._base_inputs()
        del inputs["churn_rate"]
        with self.assertRaises(ValueError) as ctx:
            calculate_dealer_value_equation(inputs)
        self.assertIn("churn_rate", str(ctx.exception))

    def test_negative_demand_raises(self):
        inputs = self._base_inputs()
        inputs["annual_demand_units"] = -100
        with self.assertRaises(ValueError):
            calculate_dealer_value_equation(inputs)

    def test_zero_dealers_raises(self):
        inputs = self._base_inputs()
        inputs["new_dealers_acquired"] = 0
        with self.assertRaises(ValueError):
            calculate_dealer_value_equation(inputs)

    def test_negative_contribution_raises(self):
        inputs = self._base_inputs()
        inputs["selling_price"] = 100.0
        inputs["unit_cost"] = 120.0
        with self.assertRaises(ValueError):
            calculate_dealer_value_equation(inputs)

    def test_zero_churn_infinite_lifespan(self):
        inputs = self._base_inputs()
        inputs["churn_rate"] = 0.0
        result = calculate_dealer_value_equation(inputs)
        self.assertEqual(result["avg_dealer_lifespan_years"], float("inf"))
        self.assertEqual(result["lifetime_value"], float("inf"))

    def test_eoq_formula(self):
        inputs = self._base_inputs()
        result = calculate_dealer_value_equation(inputs)
        expected_eoq = math.sqrt(
            (2 * inputs["annual_demand_units"] * inputs["order_cost"])
            / (inputs["holding_cost_rate"] * inputs["unit_cost"])
        )
        self.assertAlmostEqual(result["eoq"], expected_eoq, places=1)

    def test_spc_limits_non_negative(self):
        inputs = self._base_inputs()
        inputs["annual_demand_units"] = 120
        inputs["demand_stddev"] = 500
        result = calculate_dealer_value_equation(inputs)
        self.assertGreaterEqual(result["spc_monthly_lcl"], 0.0)
        self.assertGreater(result["spc_monthly_ucl"], result["spc_monthly_lcl"])


if __name__ == "__main__":
    swatch_dealer_inputs = {
        "annual_demand_units": 2400,
        "unit_cost": 120.0,
        "selling_price": 180.0,
        "order_cost": 250.0,
        "holding_cost_rate": 0.22,
        "lead_time_days": 14.0,
        "demand_stddev": 50.0,
        "service_level_z": 1.65,
        "acquisition_spend": 120000.0,
        "new_dealers_acquired": 30.0,
        "churn_rate": 0.10,
    }

    print("=== Swatch Paints Dealer Value Equation ===")
    result = calculate_dealer_value_equation(swatch_dealer_inputs)
    for key, value in result.items():
        if key == "inputs":
            continue
        print(f"{key}: {value}")

    print("\n=== Running Unit Tests ===")
    unittest.main(verbosity=2, exit=False)