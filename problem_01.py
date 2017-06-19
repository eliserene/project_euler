import unittest
from functools import reduce

def problem_01(r):
    return sum(x for x in range(r) if x % 3 == 0 or x % 5 == 0)

class PorjectEulerProblem01Tests(unittest.TestCase):
    '''test for the tenpin bowling score kata'''

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        problem_01(10)

    def test_multiples_below_10(self):
        self.assertEqual(problem_01(10), 23)

    def test_multiples_below_1000(self):
        self.assertEqual(problem_01(1000), 233168)

if __name__ == '__main__':
    unittest.main()
