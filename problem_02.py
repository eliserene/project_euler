import unittest

def fibonacci_numbers():
    previous_term = 1
    yield previous_term
    current_term = 1
    yield current_term
    while current_term < 80:
        next_term = previous_term + current_term
        yield next_term
        previous_term = current_term
        current_term = next_term

def problem_02():
    return sum(x for x in fibonacci_numbers() if x % 2 == 0)

class PorjectEulerProblem02Tests(unittest.TestCase):
    '''By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        problem_02()

    def test_the_first_ten_terms(self):
        self.assertEqual(problem_02(), 44)

if __name__ == '__main__':
    unittest.main()
