class Cal(object):
    def add_num_and_double(self, x, y):
        if type(x) is not int or type(x) is not int:
            raise ValueError

        result = x + y
        result *= 2
        return result
