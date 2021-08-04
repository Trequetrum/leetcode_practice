module Main where

import Prelude

import Data.Array (range)
import Data.Traversable (for_)
import Effect (Effect)
import Effect.Console (log)
import Basic as Basic
import Readerhidden as Readerhidden
import Readermonad as Readermonad
import Rwmonad as Rwmonad

main :: Effect Unit
main = for_ (range 1 100) \n ->
    log (Readerhidden.fizzBuzz n)