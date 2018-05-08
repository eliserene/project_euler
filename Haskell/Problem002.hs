--Problem 002
--Name: Even Fibonacci Numbers
--URL: https://projecteuler.net/problem=2
--Text: Each new term in the Fibonacci sequence is generated by adding the 
--previous two terms. By starting with 1 and 2, the first 10 terms will be:

--1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

--By considering the terms in the Fibonacci sequence whose values do not 
--exceed four million, find the sum of the even-valued terms.
module Problem002 where

import Test.Tasty.HUnit

--sumEven :: Num(a) => [a] -> a
sumEven xs = sum [x | x <- xs, even x]

--findFibTerm :: Num(a) => a -> a
findFibTerm 0 = 1
findFibTerm 1 = 1
findFibTerm n = findFibTerm (n - 1) + findFibTerm (n - 2)

fibTerms n = take n (map findFibTerm [0..])

problem002 n = sumEven (takeWhile n (map findFibTerm [0..]))

main = putStr $ show (problem002 (< 4000000))

unit_addEvenTerms = assertEqual "add even numbers less than ten" 20 (sumEven [1..9])
unit_findFirstFibTerm = assertEqual "the zeroth fibonacci number" 1 (findFibTerm 0)
unit_findSecondFibTerm = assertEqual "the first fibonacci number" 1 (findFibTerm 1)
unit_findFifthFibTerm = assertEqual "the fifth fibonacci number" 8 (findFibTerm 5)

unit_first10Terms = assertEqual "the first ten fibonacci terms" [1,1,2,3,5,8,13,21,34,55] (fibTerms 10)
unit_fullSolution55 = assertEqual "sum even terms less than fifty five" 44 (problem002 (< 55))