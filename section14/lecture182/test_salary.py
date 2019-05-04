import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary

class TestSaraly(unittest.TestCase):
#     def test_calculation_salary(self):
#         s = salary.Salary(year=2017)
#         s.bonus_api.bonus_price = MagicMock(return_value=1)
#         self.assertEqual(s.calculation_salary(), 101)
#         s.bonus_api.bonus_price.assert_called()                 # 本当に実体が呼ばれたか
#         s.bonus_api.bonus_price.assert_called_once()            # 実体が呼ばれたのは一度か
#         s.bonus_api.bonus_price.assert_called_with(year=2017)   # 実体への引数は正しいか
#         self.assertEqual(s.bonus_api.bonus_price.call_count, 1)
#
#     def test_calculation_salary_no_salary(self):
#         s = salary.Salary(year=2050)
#         s.bonus_api.bonus_price = MagicMock(return_value=0)
#         self.assertEqual(s.calculation_salary(), 100)
#         s.bonus_api.bonus_price.assert_not_called()
#
# #   @mock.patch('salary.ThirdPartyBonusApi.bonus_price', return_value=1)
#     @mock.patch('salary.ThirdPartyBonusApi.bonus_price')
#     def test_calculation_salary_patch(self, mock_bonus):
#         mock_bonus.return_value = 1
#
#         s = salary.Salary(year=2017)
#         salary_price = s.calculation_salary()
#
#         self.assertEqual(salary_price, 101)
#         mock_bonus.assert_called()
#
#     # 特定の処理のみをmockとして、他はmockしたくない場合、withを使用
#     def test_calculation_salary_patch_with(self):
#         with mock.patch('salary.ThirdPartyBonusApi.bonus_price') as mock_bonus:
#             mock_bonus.return_value = 1
#
#             s = salary.Salary(year=2017)
#             salary_price = s.calculation_salary()
#
#             self.assertEqual(salary_price, 101)
#             mock_bonus.assert_called()
#
#     # mockの開始・終了をsetUp/tearDownを用いて行う
#     def setUp(self):
#         self.patcher = mock.patch('salary.ThirdPartyBonusApi.bonus_price')
#         self.mock_bonus = self.patcher.start()
#
#     def tearDown(self):
#         self.patcher.stop()

    # def test_calculation_salary_patcher(self):
    #     self.mock_bonus.return_value = 1
    #
    #     s = salary.Salary(year=2017)
    #     salary_price = s.calculation_salary()
    #
    #     self.assertEqual(salary_price, 101)
    #     self.mock_bonus.assert_called()
    #
    # def test_calculation_salary_patch_side_effect(self):
    #     # def f(year):
    #     #     return year*2
    #     self.mock_bonus.side_effect = lambda year: 1    # fと同義
    #
    #     s = salary.Salary(year=2017)
    #     salary_price = s.calculation_salary()
    #
    #     self.assertEqual(salary_price, 101)
    #     self.mock_bonus.assert_called()
    #
    # def test_calculation_salary_patch_side_effect_refused_error(self):
    #     self.mock_bonus.side_effect = ConnectionRefusedError
    #
    #     s = salary.Salary(year=2017)
    #     salary_price = s.calculation_salary()
    #
    #     self.assertEqual(salary_price, 100)     # ERRORがでたらbonusは0
    #     self.mock_bonus.assert_called()
    #
    # def test_calculation_salary_patch_side_effect_list(self):
    #     self.mock_bonus.side_effect = [1, 2, 3, ValueError('Bankrupt')]
    #
    #     # 1
    #     s = salary.Salary(year=2017)
    #     salary_price = s.calculation_salary()
    #     self.assertEqual(salary_price, 101)
    #
    #     # 2
    #     s = salary.Salary(year=2018)
    #     salary_price = s.calculation_salary()
    #     self.assertEqual(salary_price, 102)
    #
    #     # 3
    #     s = salary.Salary(year=2019)
    #     salary_price = s.calculation_salary()
    #     self.assertEqual(salary_price, 103)
    #
    #     # 4
    #     s = salary.Salary(year=200)
    #     with self.assertRaises(ValueError):
    #         salary_price = s.calculation_salary()

    @mock.patch('salary.ThirdPartyBonusApi', spec=True)
    def test_calculation_salary_class(self, MockRest):
        mock_rest = MockRest.return_value
        # mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1
        mock_rest.get_api_name.return_value = 'Money'

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_rest.bonus_price.assert_called()


# CMD実行の場合、以下を記載し、CMDか通常のPycharm実行
if __name__ == '__main__':
    unittest.main()
