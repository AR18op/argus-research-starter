"""Standalone paper-research sizing example; no broker connections."""

from decimal import Decimal


def position_size(entry, stop, notional_cap, planned_risk_budget):
    values = [Decimal(str(x)) for x in (entry, stop, notional_cap, planned_risk_budget)]
    if any(not x.is_finite() for x in values):
        raise ValueError("Inputs must be finite")
    entry, stop, notional_cap, planned_risk_budget = values
    if not (entry > stop > 0 and notional_cap >= 0 and planned_risk_budget >= 0):
        raise ValueError("Use positive long-entry prices and nonnegative budgets")
    return min(int(notional_cap / entry), int(planned_risk_budget / (entry - stop)))


if __name__ == "__main__":
    print("Hypothetical shares:", position_size(100, 95, 10000, 250))
    print("Planned stop risk is not a guaranteed maximum loss.")
