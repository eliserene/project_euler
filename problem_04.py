import unittest

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def problem_04():
    pass

class PorjectEulerProblem04Tests(unittest.TestCase):
    '''Find the largest palindrome made from the product of two 3-digit numbers.'''

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        problem_04()

    def test_is_pelindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(123))

if __name__ == '__main__':
    unittest.main()
