import unittest
import calculation

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 5)

    def test_add_num_and_double_raise(self):
        cal = calculation.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1', '1')


# CMD実行の場合、以下を記載し、CMDか通常のPycharm実行
if __name__ == '__main__':
    unittest.main()