import unittest

def fibonacci_numbers(limit):
    last_n, n = 1, 1
    yield last_n
    while n < limit:
        yield n
        last_n, n = n, (last_n + n)


def problem_02(limit):
    return sum(x for x in fibonacci_numbers(limit) if x % 2 == 0)

class PorjectEulerProblem02Tests(unittest.TestCase):
    '''By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        problem_02(5)

    def test_the_first_ten_terms(self):
        self.assertEqual(problem_02(80), 44)

    def test_less_than_four_million(self):
        self.assertEqual(problem_02(4000000), 4613732)

if __name__ == '__main__':
    unittest.main()
