import unittest

class Factorial:

    def __init__(self, number):
        self._number = number
        self._factorial = self.find_factorial(number)

    def find_factorial(self, number):
        if number == 0 or number == 1:
            return 1
        else:
            return number * self.find_factorial(number - 1)

    def sum_digits(self):
        return sum([int(d) for d in str(self._factorial)])

class PorjectEulerProblem20Tests(unittest.TestCase):
    '''Find the largest palindrome made from the product of two 3-digit numbers.'''

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        f = Factorial(5)
        f.sum_digits()

    def test_sum_factorial_10(self):
        f = Factorial(10)
        self.assertEqual(f.sum_digits(), 27)

    def test_sum_factorial_100(self):
        f = Factorial(100)
        self.assertEqual(f.sum_digits(), 648)

if __name__ == '__main__':
    unittest.main()
