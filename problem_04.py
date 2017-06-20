import unittest

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def products(numbers):
    return (x * y for x in numbers for y in numbers)

def palindromes(numbers):
    return (n for n in products(numbers) if is_palindrome(n))

def numbersWithDigits(n):
    return range(pow(10, n-1), pow(10, n))

def problem_04():
    return max(palindromes(numbersWithDigits(3)))

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
