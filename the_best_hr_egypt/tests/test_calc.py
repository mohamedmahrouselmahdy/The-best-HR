import unittest
from decimal import Decimal as D
from the_best_hr_egypt.payroll import calc


class T(unittest.TestCase):
    def test_insurance_example_from_source(self):
        r = calc.insurance(13000)
        self.assertEqual(r["employee"], D("1430.00"))
        self.assertEqual(r["employer"], D("2437.50"))

    def test_insurance_bounds(self):
        self.assertEqual(calc.insurance(100000)["employee"], D("1837.00"))
        self.assertEqual(calc.insurance(100000)["employer"], D("3131.25"))
        self.assertEqual(calc.insurance(1000)["employee"], D("297.00"))
        self.assertEqual(calc.insurance(1000)["employer"], D("506.25"))

    def test_tax_zero_when_low(self):
        # (5000-550)*12-20000 = 33,400 -> under 40,000 -> 0
        self.assertEqual(calc.monthly_income_tax(5000, 550), D("0.00"))

    def test_tax_hand_calc(self):
        # gross 13000, insurance 1430 -> 11570*12 = 138,840 - 20,000 = 118,840
        # 0-40k 0; 40-55k 15,000*10%=1500; 55-70k 15,000*15%=2250; 70k-118,840: 48,840*20%=9768 -> 13,518/12
        self.assertEqual(calc.monthly_income_tax(13000, 1430), D("1126.50"))

    def test_refuses_high_income(self):
        with self.assertRaises(NotImplementedError):
            calc.monthly_income_tax(80000, 1837)


if __name__ == "__main__":
    unittest.main()
