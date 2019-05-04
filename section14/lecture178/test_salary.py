import unittest
from unittest.mock import MagicMock
import salary

class TestSaraly(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)

# CMD実行の場合、以下を記載し、CMDか通常のPycharm実行
if __name__ == '__main__':
    unittest.main()
