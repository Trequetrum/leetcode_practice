module Readermonad where

import Prelude

import Control.Monad.Reader (Reader, ask, runReader)
import Data.Array (foldl)
import Data.Array.NonEmpty (fromArray, head, tail)
import Data.Int (rem)
import Data.Maybe (Maybe(..))
import Data.String (length)

modTag :: Int -> String -> String -> Reader Int String
modTag divisor tag acc = do
    dividend <- ask
    pure $ if dividend `rem` divisor == 0 then acc <> tag else acc

defaultNum :: String -> Reader Int String
defaultNum acc = do
    n <- ask
    pure $ if length acc > 0 then acc else show n

composeAndRun :: Array (String -> Reader Int String) -> Int -> String
composeAndRun fns = case fromArray fns of
    Nothing -> \n -> show n
    Just (someFns) -> runReader $ "" # foldl (>=>) (head someFns) (tail someFns)

fizzBuzz :: Int -> String
fizzBuzz = composeAndRun 
    [   modTag 3 "Fizz"
    ,   modTag 5 "Buzz"
    ,   defaultNum
    ]