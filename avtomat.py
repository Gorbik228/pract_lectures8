import unittest
from math import sqrt

def funck(a, b):
    try:
        result = round(sqrt(((a+b)**3)/((a-b)**2)), 4)
    except ZeroDivisionError:
        result = 'there is zero divizion'
    except ValueError:
        result = 'complex'
    except TypeError:
        result = 'this is not a number'
    return result

class TestEqualize(unittest.TestCase):
    def test_integer_positive_numbers(self):
        self.assertEqual(funck(2, 1), 5.1962)

    def test_integer_negative_numbers(self):
        self.assertEqual(funck(2, -1), 0.3333)

    def test_zero_divizion(self):
        self.assertEqual(funck(2, 2), 'there is zero divizion')

    def test_float_positive_numbers(self):
        self.assertEqual(funck(0.2, 0.1), 1.6432)

    def test_negative_root(self):
        self.assertEqual(funck(1, -2), 'complex')

    def test_error_input(self):
        self.assertEqual(funck('asdff', 0), 'this is not a number')
        self.assertEqual(funck('', 0), 'this is not a number')
        self.assertEqual(funck('10**-9', 0), 'this is not a number')

if __name__ == '__main__':
    unittest.main()