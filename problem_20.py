import unittest

class Factorial:

    def sum_digits(self):
        pass

class PorjectEulerProblem20Tests(unittest.TestCase):
    '''Find the largest palindrome made from the product of two 3-digit numbers.'''

    def setUp(self):
        self.f = Factorial()

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        self.f.sum_digits()

if __name__ == '__main__':
    unittest.main()
