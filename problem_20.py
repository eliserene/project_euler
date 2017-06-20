import unittest

class Factorial:

    def __init__(self, number):
        def find_factorial(number):
            if number == 0 or number == 1:
                return 1
            else:
                return number * find_factorial(number - 1)

        self._factorial = find_factorial(number)

    def sum_digits(self):
        return sum(int(d) for d in str(self._factorial))

class PorjectEulerProblem20Tests(unittest.TestCase):
    '''Find the largest palindrome made from the product of two 3-digit numbers.'''

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        Factorial(5).sum_digits()

    def test_sum_factorial_10(self):
        self.assertEqual(Factorial(10).sum_digits(), 27)

    def test_sum_factorial_100(self):
        self.assertEqual(Factorial(100).sum_digits(), 648)

if __name__ == '__main__':
    unittest.main()
