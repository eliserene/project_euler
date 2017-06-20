import unittest

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def problem_04():
  xs, ys = range(999, 100, -1), range(999, 100, -1)
  return max([x * y for x in xs for y in ys if is_palindrome(x * y)])

class PorjectEulerProblem04Tests(unittest.TestCase):
    '''Find the largest palindrome made from the product of two 3-digit numbers.'''

    def test_function_runs(self):
        ''''Basic smole test: does the function run?'''
        problem_04()

    def test_is_pelindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(123))

    def test_largest_palindrome(self):
        self.assertEqual(problem_04(), 906609)

if __name__ == '__main__':
    unittest.main()
