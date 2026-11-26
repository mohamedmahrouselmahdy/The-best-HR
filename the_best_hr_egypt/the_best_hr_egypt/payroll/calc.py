"""Egypt monthly payroll deductions: social insurance and salary income tax."""
import json
import os
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP

_D = Decimal


def load_rates(path=None):
    path = path or os.path.join(os.path.dirname(__file__), "egypt_rates_2026.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _money(x):
    return _D(x).quantize(_D("0.01"), rounding=ROUND_HALF_UP)


def insurance(insurable_wage, rates=None):
    """Employee and employer social insurance on the insurable wage, clamped to the legal bounds."""
    r = (rates or load_rates())["insurance"]
    w = min(max(_D(str(insurable_wage)), _D(r["min_insurable_wage_monthly"])), _D(r["max_insurable_wage_monthly"]))
    return {
        "insurable_wage": _money(w),
        "employee": _money(w * _D(str(r["employee_rate"]))),
        "employer": _money(w * _D(str(r["employer_rate"]))),
    }


def monthly_income_tax(monthly_gross, employee_insurance, rates=None):
    """Salary tax for one month, assuming the same salary all 12 months.
    annual net = 12 * (gross - employee insurance) - personal exemption, rounded down to 10."""
    t = (rates or load_rates())["tax"]
    net = (_D(str(monthly_gross)) - _D(str(employee_insurance))) * 12 - _D(t["personal_exemption_annual"])
    net = max(net, _D(0))
    net = (net / 10).to_integral_value(rounding=ROUND_DOWN) * 10
    if net > _D(t["max_annual_net_supported"]):
        raise NotImplementedError("annual net above 600,000 EGP needs the Law 7/2024 slab phase-out, not implemented")
    tax, prev = _D(0), _D(0)
    for s in t["slabs_annual"]:
        top = _D(s["up_to"]) if s["up_to"] is not None else net
        if net > prev:
            tax += (min(net, top) - prev) * _D(str(s["rate"]))
        prev = top
        if net <= top:
            break
    return _money(tax / 12)
