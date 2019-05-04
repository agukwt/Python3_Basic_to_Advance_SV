import pytest
from lecture167 import calculation


class TestCal(object):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = calculation.Cal()
            cal.add_num_and_double('1', '1')
