module Readerhidden where

import Prelude

import Data.Array (foldl)
import Data.Int (rem)
import Data.String (length)

smallTag :: String -> String -> Int -> String
smallTag tag acc n =
    if n < 5 then acc <> tag else acc

modTag :: Int -> String -> String -> Int -> String
modTag divisor tag acc dividend =
    if dividend `rem` divisor == 0 then acc <> tag else acc

defaultNum :: String -> Int -> String
defaultNum acc n = if length acc > 0 then acc else show n

composeAndRun :: Array (String -> Int -> String) -> Int -> String
composeAndRun fns n = foldl (\acc fn -> fn acc n) "" fns

fizzBuzzExt :: Int -> String
fizzBuzzExt = composeAndRun 
    [   smallTag "Itty"
    ,   modTag 3 "Fizz"
    ,   modTag 5 "Buzz"
    ,   modTag 7 "Pazz"
    ,   modTag 13 "Poob"
    ,   defaultNum
    ]