import unittest
from functools import reduce

def problem_01():
    numbers = [x for x in range(10) if x % 3 == 0 or x % 5 == 0]
    return reduce((lambda x, y: x + y), numbers, 0)

class PorjectEulerProblem01Tests(unittest.TestCase):
    '''test for the tenpin bowling score kata'''

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        problem_01()

    def test_multiples_below_10(self):
        self.assertEqual(problem_01(), 23)

if __name__ == '__main__':
    unittest.main()
