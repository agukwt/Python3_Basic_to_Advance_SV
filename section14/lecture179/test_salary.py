import unittest
from unittest.mock import MagicMock
import salary

class TestSaraly(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        s.bonus_api.bonus_price.assert_called()                 # 本当に実体が呼ばれたか
        s.bonus_api.bonus_price.assert_called_once()            # 実体が呼ばれたのは一度か
        s.bonus_api.bonus_price.assert_called_with(year=2017)   # 実体への引数は正しいか
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()


    # CMD実行の場合、以下を記載し、CMDか通常のPycharm実行
if __name__ == '__main__':
    unittest.main()
