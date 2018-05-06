--Problem 001
--Name: Multiples of 3 and 5
--URL: https://projecteuler.net/problem=1
--Text: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
--Find the sum of all the multiples of 3 or 5 below 1000.
module Problem001 where

import Test.Tasty.HUnit

problem001 n = sum [x | x <- [1..(n - 1)], x `mod` 3 == 0 || x `mod` 5 == 0]

main = putStrLn $ show (problem001 1000)

unit_test1 = assertEqual "less than 10" 23 (problem001 10)
unit_test2 = assertEqual "less than 100" 2318 (problem001 100)

--tests = TestList [TestLabel "test1: less than 10" test1, TestLabel "test 2: less than 100" test2]