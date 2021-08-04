module Basic where

import Prelude

import Data.Array (foldl)
import Data.Int (rem)
import Data.String (length)


-------------------------------------------
-- This is (in my view) the best solution given the task FizzBuzz 
-- puts before you. It’s quick to develop, easy to understand, and 
-- unlikely to have errors. 
-- 
-- If asked this question in an interview, I would do this.
-------------------------------------------

isMultipleOf :: Int -> Int -> Boolean
isMultipleOf dividend divisor = dividend `rem` divisor == 0

fizzBuzz :: Int -> String
fizzBuzz n 
    | n `isMultipleOf` (3 * 5) = "FizzBuzz"
    | n `isMultipleOf` 3 = "Fizz"
    | n `isMultipleOf` 5 = "Buzz"
    | otherwise = show n

-------------------------------------------
-- The Above approach breaks down if you need to extend FizzBuzz. Here
-- we do something with 7 and 13 as well. To make this work, we build
-- our string incrementally
-------------------------------------------

fizzBuzzExt :: Int -> String
fizzBuzzExt n = e
    where
        a = if n `isMultipleOf` 3 then "Fizz" else ""
        b = if n `isMultipleOf` 5 then a <> "Buzz" else a
        c = if n `isMultipleOf` 7 then b <> "Pazz" else b
        d = if n `isMultipleOf` 13 then c <> "Boop" else c
        e = if length d > 0 then d else show n

-------------------------------------------
-- It's pretty simple, sure, but to undertand the pattern at work above 
-- still takes a moment. We can make this easier by extracting this logic
-- into a function
-------------------------------------------

modTag :: Int -> Int -> String -> String -> String
modTag dividend divisor tag acc =
    if dividend `rem` divisor == 0 then acc <> tag else acc

fizzBuzzExt2 :: Int -> String
fizzBuzzExt2 n = if length strn > 0 then strn else show n
    where
        becomes = modTag n
        strn = "" # 
            (3 `becomes` "Fizz") >>> 
            (5 `becomes` "Buzz") >>> 
            (7 `becomes` "Pazz") >>> 
            (13 `becomes` "Boop")
