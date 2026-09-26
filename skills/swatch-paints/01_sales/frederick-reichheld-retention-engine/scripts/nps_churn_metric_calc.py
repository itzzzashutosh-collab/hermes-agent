"""
Frederick Reichheld's Dealer NPS & Churn Early Warning System
==============================================================

A robust, type-annotated Python 3 module for calculating dealer-level
Net Promoter Score (NPS), retention probability, churn risk flags, and
supporting operational metrics (EOQ, safety buffer, contribution margin,
SPC-style control limits) for a dealer network.

All prices, rates, and thresholds are supplied via parameter dictionaries;
no business constants are hardcoded.  The module is pure-Python and uses
only the standard library.

Target function
---------------
calculate_dealer_retention_and_nps(params: dict) -> dict

Author: Hermes (CEO, Swatch Paints)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Custom exceptions
# ---------------------------------------------------------------------------


class DealerMetricError(ValueError):
    """Raised when input parameters are missing, malformed, or inconsistent."""


class DealerMetricWarning(UserWarning):
    """Non-fatal warning raised for degenerate but recoverable inputs."""


# ---------------------------------------------------------------------------
# Pure helper functions (mathematical primitives)
# ---------------------------------------------------------------------------


def _require_keys(
    container: Dict[str, Any],
    keys: List[str],
    context: str = "params",
) -> None:
    """Ensure all required keys are present and not None."""
    missing = [k for k in keys if k not in container or container[k] is None]
    if missing:
        raise DealerMetricError(
            f"{context} missing required keys: {', '.join(missing)}"
        )


def _positive(value: Any, name: str) -> float:
    """Coerce a value to a positive float."""
    try:
        f = float(value)
    except (TypeError, ValueError) as exc:
        raise DealerMetricError(f"{name} must be numeric; got {value!r}") from exc
    if not math.isfinite(f) or f <= 0:
        raise DealerMetricError(f"{name} must be a positive finite number; got {f}")
    return f


def _non_negative(value: Any, name: str) -> float:
    """Coerce a value to a non-negative float."""
    try:
        f = float(value)
    except (TypeError, ValueError) as exc:
        raise DealerMetricError(f"{name} must be numeric; got {value!r}") from exc
    if not math.isfinite(f) or f < 0:
        raise DealerMetricError(f"{name} must be a non-negative finite number; got {f}")
    return f


def _probability(value: Any, name: str) -> float:
    """Coerce a value to a float in [0, 1]."""
    f = _non_negative(value, name)
    if f > 1.0:
        raise DealerMetricError(f"{name} must be between 0 and 1; got {f}")
    return f


def _integer(value: Any, name: str, min_value: Optional[int] = None) -> int:
    """Coerce a value to an integer, optionally enforcing a minimum."""
    try:
        i = int(value)
    except (TypeError, ValueError) as exc:
        raise DealerMetricError(f"{name} must be an integer; got {value!r}") from exc
    if min_value is not None and i < min_value:
        raise DealerMetricError(f"{name} must be >= {min_value}; got {i}")
    return i


def _calculate_nps(
    promoters: int,
    passives: int,
    detractors: int,
) -> Tuple[float, int, float, float]:
    """
    Compute Net Promoter Score and its component percentages.

    Returns
    -------
    nps : float
        Promoter % minus Detractor %, bounded to [-100, 100].
    total : int
        Total respondents.
    promoter_pct : float
        Percentage of promoters.
    detractor_pct : float
        Percentage of detractors.
    """
    total = promoters + passives + detractors
    if total == 0:
        return 0.0, 0, 0.0, 0.0
    promoter_pct = (promoters / total) * 100.0
    detractor_pct = (detractors / total) * 100.0
    nps = promoter_pct - detractor_pct
    # Guard against tiny floating-point overshoot
    nps = max(-100.0, min(100.0, nps))
    return nps, total, promoter_pct, detractor_pct


def _logistic_retention(
    nps: float,
    engagement_score: float,
    tenure_months: float,
    payment_delinquency_rate: float,
    weights: Dict[str, float],
    intercept: float,
) -> float:
    """
    Estimate retention probability using a weighted logistic-style score.

    The linear predictor is:
        z = intercept
            + w_nps * nps
            + w_engagement * engagement_score
            + w_tenure * log(tenure_months + 1)
            - w_delinquency * payment_delinquency_rate

    Retention probability = 1 / (1 + exp(-z)), clamped to [0, 1].
    """
    z = (
        intercept
        + weights["nps"] * nps
        + weights["engagement"] * engagement_score
        + weights["tenure"] * math.log1p(tenure_months)
        - weights["delinquency"] * payment_delinquency_rate
    )
    probability = 1.0 / (1.0 + math.exp(-z))
    return max(0.0, min(1.0, probability))


def _calculate_eoq(
    annual_demand: float,
    ordering_cost: float,
    holding_cost_per_unit_year: float,
) -> float:
    """
    Economic Order Quantity (Harris-Wilson model).

    EOQ = sqrt(2 * D * S / H)
    """
    if holding_cost_per_unit_year == 0:
        raise DealerMetricError("holding_cost_per_unit_year must be > 0 for EOQ")
    return math.sqrt((2.0 * annual_demand * ordering_cost) / holding_cost_per_unit_year)


def _calculate_safety_buffer(
    avg_period_demand: float,
    demand_std_dev: float,
    lead_time_periods: float,
    service_level_z: float,
) -> float:
    """
    Safety stock / buffer using a normal-approximation service-level model.

    Buffer = z * sigma_LT
        where sigma_LT = demand_std_dev * sqrt(lead_time_periods)

    If demand_std_dev is zero, the buffer is zero.
    """
    if lead_time_periods < 0:
        raise DealerMetricError("lead_time_periods must be non-negative")
    sigma_lt = demand_std_dev * math.sqrt(lead_time_periods)
    return service_level_z * sigma_lt


def _calculate_contribution_margin(
    unit_selling_price: float,
    unit_variable_cost: float,
) -> Tuple[float, float]:
    """
    Contribution margin per unit and as a percentage of selling price.

    Returns (contribution_margin_per_unit, contribution_margin_ratio).
    """
    cm = unit_selling_price - unit_variable_cost
    ratio = (cm / unit_selling_price) if unit_selling_price != 0 else 0.0
    return cm, ratio


def _spc_control_limits(
    values: List[float],
    sigma_multiplier: float = 3.0,
) -> Tuple[float, float, float, float]:
    """
    Compute SPC-style control limits for a time series of metric values.

    Returns (mean, std_dev, lower_control_limit, upper_control_limit).

    For fewer than 2 data points std_dev is 0 and the limits equal the mean.
    """
    n = len(values)
    if n == 0:
        return 0.0, 0.0, 0.0, 0.0
    mean = sum(values) / n
    if n < 2:
        return mean, 0.0, mean, mean
    variance = sum((x - mean) ** 2 for x in values) / n
    std_dev = math.sqrt(variance)
    lcl = mean - sigma_multiplier * std_dev
    ucl = mean + sigma_multiplier * std_dev
    return mean, std_dev, lcl, ucl


# ---------------------------------------------------------------------------
# Dataclass for structured internal state
# ---------------------------------------------------------------------------


@dataclass
class DealerInputs:
    """Validated, normalized inputs for a single dealer calculation."""

    dealer_id: str
    promoters: int
    passives: int
    detractors: int
    engagement_score: float
    tenure_months: float
    payment_delinquency_rate: float
    annual_demand: float
    ordering_cost: float
    holding_cost_per_unit_year: float
    avg_period_demand: float
    demand_std_dev: float
    lead_time_periods: float
    service_level_z: float
    unit_selling_price: float
    unit_variable_cost: float
    historical_retention_values: List[float]
    churn_risk_threshold: float
    nps_weights: Dict[str, float]
    logistic_intercept: float
    spc_sigma_multiplier: float


# ---------------------------------------------------------------------------
# Validation / normalization
# ---------------------------------------------------------------------------


def _normalize_inputs(params: Dict[str, Any]) -> DealerInputs:
    """Validate and convert the raw parameter dict into a typed DealerInputs object."""
    _require_keys(
        params,
        [
            "dealer_id",
            "promoters",
            "passives",
            "detractors",
            "engagement_score",
            "tenure_months",
            "payment_delinquency_rate",
            "annual_demand",
            "ordering_cost",
            "holding_cost_per_unit_year",
            "avg_period_demand",
            "demand_std_dev",
            "lead_time_periods",
            "service_level_z",
            "unit_selling_price",
            "unit_variable_cost",
        ],
    )

    dealer_id = str(params["dealer_id"])
    if not dealer_id.strip():
        raise DealerMetricError("dealer_id must be a non-empty string")

    promoters = _integer(params["promoters"], "promoters", min_value=0)
    passives = _integer(params["passives"], "passives", min_value=0)
    detractors = _integer(params["detractors"], "detractors", min_value=0)

    engagement_score = _probability(params["engagement_score"], "engagement_score")
    tenure_months = _non_negative(params["tenure_months"], "tenure_months")
    payment_delinquency_rate = _probability(
        params["payment_delinquency_rate"], "payment_delinquency_rate"
    )

    annual_demand = _non_negative(params["annual_demand"], "annual_demand")
    ordering_cost = _positive(params["ordering_cost"], "ordering_cost")
    holding_cost_per_unit_year = _positive(
        params["holding_cost_per_unit_year"], "holding_cost_per_unit_year"
    )

    avg_period_demand = _non_negative(
        params["avg_period_demand"], "avg_period_demand"
    )
    demand_std_dev = _non_negative(params["demand_std_dev"], "demand_std_dev")
    lead_time_periods = _non_negative(
        params["lead_time_periods"], "lead_time_periods"
    )
    service_level_z = _non_negative(params["service_level_z"], "service_level_z")

    unit_selling_price = _positive(
        params["unit_selling_price"], "unit_selling_price"
    )
    unit_variable_cost = _non_negative(
        params["unit_variable_cost"], "unit_variable_cost"
    )
    if unit_variable_cost > unit_selling_price:
        raise DealerMetricError(
            "unit_variable_cost cannot exceed unit_selling_price"
        )

    historical_retention_values = params.get("historical_retention_values", [])
    if not isinstance(historical_retention_values, (list, tuple)):
        raise DealerMetricError(
            "historical_retention_values must be a list or tuple of floats"
        )
    historical_retention_values = [
        _probability(v, f"historical_retention_values[{i}]")
        for i, v in enumerate(historical_retention_values)
    ]

    churn_risk_threshold = _probability(
        params.get("churn_risk_threshold", 0.5), "churn_risk_threshold"
    )

    default_weights = {"nps": 0.04, "engagement": 1.2, "tenure": 0.15, "delinquency": 2.5}
    nps_weights = params.get("nps_weights", default_weights)
    if not isinstance(nps_weights, dict):
        raise DealerMetricError("nps_weights must be a dictionary")
    for k in default_weights:
        if k not in nps_weights:
            nps_weights[k] = default_weights[k]
    for k, v in nps_weights.items():
        _non_negative(v, f"nps_weights[{k}]")

    logistic_intercept = float(params.get("logistic_intercept", -2.5))
    if not math.isfinite(logistic_intercept):
        raise DealerMetricError("logistic_intercept must be finite")

    spc_sigma_multiplier = _positive(
        params.get("spc_sigma_multiplier", 3.0), "spc_sigma_multiplier"
    )

    return DealerInputs(
        dealer_id=dealer_id,
        promoters=promoters,
        passives=passives,
        detractors=detractors,
        engagement_score=engagement_score,
        tenure_months=tenure_months,
        payment_delinquency_rate=payment_delinquency_rate,
        annual_demand=annual_demand,
        ordering_cost=ordering_cost,
        holding_cost_per_unit_year=holding_cost_per_unit_year,
        avg_period_demand=avg_period_demand,
        demand_std_dev=demand_std_dev,
        lead_time_periods=lead_time_periods,
        service_level_z=service_level_z,
        unit_selling_price=unit_selling_price,
        unit_variable_cost=unit_variable_cost,
        historical_retention_values=historical_retention_values,
        churn_risk_threshold=churn_risk_threshold,
        nps_weights=nps_weights,
        logistic_intercept=logistic_intercept,
        spc_sigma_multiplier=spc_sigma_multiplier,
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def calculate_dealer_retention_and_nps(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate Frederick Reichheld-style dealer NPS, churn risk, retention
    probability, and supporting operational metrics.

    Parameters
    ----------
    params : dict
        All business inputs.  Required keys:

        dealer_id : str
            Unique dealer identifier.
        promoters, passives, detractors : int
            Raw 0-10 survey bucket counts.
        engagement_score : float
            Normalised engagement score in [0, 1].
        tenure_months : float
            Dealer tenure in months (>= 0).
        payment_delinquency_rate : float
            Share of late/missed payments in [0, 1].
        annual_demand : float
            Annual unit demand (>= 0).
        ordering_cost : float
            Fixed cost per order (> 0).
        holding_cost_per_unit_year : float
            Annual holding cost per unit (> 0).
        avg_period_demand : float
            Average demand per period (>= 0).
        demand_std_dev : float
            Standard deviation of period demand (>= 0).
        lead_time_periods : float
            Replenishment lead time in periods (>= 0).
        service_level_z : float
            Z-score for safety stock (>= 0, e.g. 1.65 for 95%).
        unit_selling_price : float
            Dealer landing / selling price per unit (> 0).
        unit_variable_cost : float
            Variable cost per unit (>= 0, <= selling price).

        Optional keys:

        historical_retention_values : list[float]
            Prior retention probabilities for SPC control-limit calculation.
        churn_risk_threshold : float
            Retention probability below which a dealer is flagged as churn-risk.
        nps_weights : dict[str, float]
            Weights for the logistic retention model.
        logistic_intercept : float
            Intercept for the logistic retention model.
        spc_sigma_multiplier : float
            Sigma multiplier for control limits (default 3.0).

    Returns
    -------
    dict
        A structured result containing:

        dealer_id : str
        nps : float
        total_respondents : int
        promoter_pct : float
        detractor_pct : float
        passive_pct : float
        retention_probability : float
        churn_risk_flag : bool
        churn_risk_reason : str or None
        eoq : float
        safety_buffer : float
        reorder_point : float
        contribution_margin_per_unit : float
        contribution_margin_ratio : float
        spc_retention_mean : float
        spc_retention_std_dev : float
        spc_retention_lcl : float
        spc_retention_ucl : float
        retention_outside_control_limits : bool
        status : str
    """
    inputs = _normalize_inputs(params)

    # NPS calculation
    nps, total, promoter_pct, detractor_pct = _calculate_nps(
        inputs.promoters, inputs.passives, inputs.detractors
    )
    passive_pct = 100.0 - promoter_pct - detractor_pct

    # Retention probability via weighted logistic model
    retention_probability = _logistic_retention(
        nps=nps,
        engagement_score=inputs.engagement_score,
        tenure_months=inputs.tenure_months,
        payment_delinquency_rate=inputs.payment_delinquency_rate,
        weights=inputs.nps_weights,
        intercept=inputs.logistic_intercept,
    )

    # Churn risk flag
    churn_risk_flag = retention_probability < inputs.churn_risk_threshold
    churn_risk_reason = None
    if churn_risk_flag:
        churn_risk_reason = (
            f"Retention probability ({retention_probability:.2%}) below threshold "
            f"({inputs.churn_risk_threshold:.2%})"
        )

    # Operational metrics
    eoq = _calculate_eoq(
        inputs.annual_demand,
        inputs.ordering_cost,
        inputs.holding_cost_per_unit_year,
    )
    safety_buffer = _calculate_safety_buffer(
        inputs.avg_period_demand,
        inputs.demand_std_dev,
        inputs.lead_time_periods,
        inputs.service_level_z,
    )
    reorder_point = (inputs.avg_period_demand * inputs.lead_time_periods) + safety_buffer

    cm_per_unit, cm_ratio = _calculate_contribution_margin(
        inputs.unit_selling_price, inputs.unit_variable_cost
    )

    # SPC control limits on historical retention values (include current retention)
    spc_series = inputs.historical_retention_values + [retention_probability]
    mean, std_dev, lcl, ucl = _spc_control_limits(
        spc_series, inputs.spc_sigma_multiplier
    )
    outside_limits = retention_probability < lcl or retention_probability > ucl

    status = "healthy"
    if churn_risk_flag and outside_limits:
        status = "critical"
    elif churn_risk_flag:
        status = "at_risk"
    elif outside_limits:
        status = "anomaly"

    return {
        "dealer_id": inputs.dealer_id,
        "nps": round(nps, 4),
        "total_respondents": total,
        "promoter_pct": round(promoter_pct, 4),
        "detractor_pct": round(detractor_pct, 4),
        "passive_pct": round(passive_pct, 4),
        "retention_probability": round(retention_probability, 6),
        "churn_risk_flag": churn_risk_flag,
        "churn_risk_reason": churn_risk_reason,
        "eoq": round(eoq, 4),
        "safety_buffer": round(safety_buffer, 4),
        "reorder_point": round(reorder_point, 4),
        "contribution_margin_per_unit": round(cm_per_unit, 4),
        "contribution_margin_ratio": round(cm_ratio, 6),
        "spc_retention_mean": round(mean, 6),
        "spc_retention_std_dev": round(std_dev, 6),
        "spc_retention_lcl": round(lcl, 6),
        "spc_retention_ucl": round(ucl, 6),
        "retention_outside_control_limits": outside_limits,
        "status": status,
    }


# ---------------------------------------------------------------------------
# Unit tests (self-contained, no external test runner required)
# ---------------------------------------------------------------------------


def _run_unit_tests() -> None:
    """Execute a suite of assertions covering core calculation paths."""

    # 1. Happy path
    happy_params = {
        "dealer_id": "SWATCH-BUNDI-001",
        "promoters": 45,
        "passives": 30,
        "detractors": 10,
        "engagement_score": 0.78,
        "tenure_months": 24,
        "payment_delinquency_rate": 0.05,
        "annual_demand": 1200,
        "ordering_cost": 2500,
        "holding_cost_per_unit_year": 120,
        "avg_period_demand": 100,
        "demand_std_dev": 20,
        "lead_time_periods": 1.5,
        "service_level_z": 1.65,
        "unit_selling_price": 850,
        "unit_variable_cost": 520,
        "historical_retention_values": [0.82, 0.79, 0.81, 0.80],
        "churn_risk_threshold": 0.70,
        "nps_weights": {
            "nps": 0.04,
            "engagement": 1.2,
            "tenure": 0.15,
            "delinquency": 2.5,
        },
        "logistic_intercept": -2.5,
        "spc_sigma_multiplier": 3.0,
    }
    result = calculate_dealer_retention_and_nps(happy_params)
    assert result["dealer_id"] == "SWATCH-BUNDI-001"
    assert result["total_respondents"] == 85
    expected_nps = round(((45 / 85) * 100) - ((10 / 85) * 100), 4)
    assert abs(result["nps"] - expected_nps) < 1e-9
    assert 0.0 <= result["retention_probability"] <= 1.0
    assert result["eoq"] > 0
    assert result["safety_buffer"] >= 0
    assert result["contribution_margin_per_unit"] == 850 - 520
    assert result["status"] in {"healthy", "at_risk", "anomaly", "critical"}

    # 2. Zero respondents -> NPS 0, retention from other factors
    zero_survey = dict(happy_params)
    zero_survey.update({"promoters": 0, "passives": 0, "detractors": 0})
    zr = calculate_dealer_retention_and_nps(zero_survey)
    assert zr["nps"] == 0.0
    assert zr["total_respondents"] == 0
    assert zr["promoter_pct"] == 0.0
    assert zr["detractor_pct"] == 0.0

    # 3. All detractors -> NPS -100
    all_detractors = dict(happy_params)
    all_detractors.update({"promoters": 0, "passives": 0, "detractors": 5})
    ad = calculate_dealer_retention_and_nps(all_detractors)
    assert ad["nps"] == -100.0
    assert ad["churn_risk_flag"] is True

    # 4. All promoters -> NPS 100
    all_promoters = dict(happy_params)
    all_promoters.update({"promoters": 5, "passives": 0, "detractors": 0})
    ap = calculate_dealer_retention_and_nps(all_promoters)
    assert ap["nps"] == 100.0

    # 5. EOQ edge: zero annual demand -> EOQ 0
    zero_demand = dict(happy_params)
    zero_demand["annual_demand"] = 0
    zd = calculate_dealer_retention_and_nps(zero_demand)
    assert zd["eoq"] == 0.0

    # 6. Missing required key raises DealerMetricError
    try:
        bad = dict(happy_params)
        bad.pop("dealer_id")
        calculate_dealer_retention_and_nps(bad)
        assert False, "Expected DealerMetricError for missing dealer_id"
    except DealerMetricError:
        pass

    # 7. Negative numeric input raises DealerMetricError
    try:
        bad = dict(happy_params)
        bad["promoters"] = -3
        calculate_dealer_retention_and_nps(bad)
        assert False, "Expected DealerMetricError for negative promoters"
    except DealerMetricError:
        pass

    # 8. Variable cost > selling price raises DealerMetricError
    try:
        bad = dict(happy_params)
        bad["unit_variable_cost"] = 900
        calculate_dealer_retention_and_nps(bad)
        assert False, "Expected DealerMetricError for variable cost > price"
    except DealerMetricError:
        pass

    # 9. Probability out of range raises DealerMetricError
    try:
        bad = dict(happy_params)
        bad["engagement_score"] = 1.5
        calculate_dealer_retention_and_nps(bad)
        assert False, "Expected DealerMetricError for engagement_score > 1"
    except DealerMetricError:
        pass

    # 10. SPC with no historical data uses current retention only
    no_hist = dict(happy_params)
    no_hist["historical_retention_values"] = []
    nh = calculate_dealer_retention_and_nps(no_hist)
    assert nh["spc_retention_mean"] == nh["retention_probability"]
    assert nh["spc_retention_std_dev"] == 0.0
    assert nh["spc_retention_lcl"] == nh["retention_probability"]
    assert nh["spc_retention_ucl"] == nh["retention_probability"]

    print("All unit tests passed.")


# ---------------------------------------------------------------------------
# Demonstration entry point
# ---------------------------------------------------------------------------


def _demo_swatch_paints() -> None:
    """Run a representative Swatch Paints dealer scenario."""
    swatch_dealer_params = {
        "dealer_id": "SWATCH-BUNDI-RUSTIC-007",
        "promoters": 62,
        "passives": 24,
        "detractors": 14,
        "engagement_score": 0.72,
        "tenure_months": 36,
        "payment_delinquency_rate": 0.08,
        "annual_demand": 2400,
        "ordering_cost": 1800,
        "holding_cost_per_unit_year": 95,
        "avg_period_demand": 200,
        "demand_std_dev": 35,
        "lead_time_periods": 2.0,
        "service_level_z": 1.65,
        "unit_selling_price": 720,
        "unit_variable_cost": 445,
        "historical_retention_values": [0.88, 0.85, 0.87, 0.84, 0.86],
        "churn_risk_threshold": 0.75,
        "nps_weights": {
            "nps": 0.035,
            "engagement": 1.1,
            "tenure": 0.12,
            "delinquency": 2.8,
        },
        "logistic_intercept": -2.4,
        "spc_sigma_multiplier": 3.0,
    }

    result = calculate_dealer_retention_and_nps(swatch_dealer_params)

    print("\n=== Swatch Paints Dealer NPS & Churn Early Warning ===\n")
    for key, value in result.items():
        print(f"{key:40s}: {value}")
    print()


if __name__ == "__main__":
    _run_unit_tests()
    _demo_swatch_paints()
