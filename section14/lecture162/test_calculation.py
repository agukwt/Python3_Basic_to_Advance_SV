import unittest

import lecture162.calculation


class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = lecture162.calculation.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 5)



# # CMD実行の場合、以下を記載し、CMDか通常のPycharm実行
# if __name__ == '__main__':
#     unittest.main()