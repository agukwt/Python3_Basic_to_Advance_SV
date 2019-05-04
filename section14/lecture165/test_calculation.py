import unittest
import calculation

release_name = 'lesson'

class CalTest(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    @unittest.skipIf(release_name == 'lesson', 'skip!')
    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


# CMD実行の場合、以下を記載し、CMDか通常のPycharm実行
if __name__ == '__main__':
    unittest.main()