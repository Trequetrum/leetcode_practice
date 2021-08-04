-- From @rhendric/discourse
module Rwmonad where

import Prelude

import Control.Monad.Reader.Class (class MonadReader, asks)
import Control.Monad.RWS (execRWS)
import Control.Monad.Writer.Class (class MonadWriter, listen, tell)
import Data.Int (rem)
import Data.String (null)
import Data.Tuple (snd)

-- Pretend we aren't on try.purescript.org
--log :: String -> Effect Unit
--log = render <<< p <<< text

execRW :: forall r w a. Monoid w => (forall m. MonadReader r m => MonadWriter w m => m a) -> r -> w
execRW rws r = snd $ execRWS rws r unit

fizzBuzzExt :: Int -> String
fizzBuzzExt = execRW ( showIfSilent do
  whenValue (<) 5 "Itty"
  whenValue isMultipleOf 3 "Fizz"
  whenValue isMultipleOf 5 "Buzz"
  whenValue isMultipleOf 7 "Pazz"
  whenValue isMultipleOf 13 "Boop" )

isMultipleOf :: Int -> Int -> Boolean
isMultipleOf n m = n `rem` m == 0

whenValue :: forall m r w r'. MonadReader r m => MonadWriter w m => (r -> r' -> Boolean) -> r' -> w -> m Unit
whenValue relatesTo r = whenM (asks (_ `relatesTo` r)) <<< tell

showIfSilent :: forall m r a. Show r => MonadReader r m => MonadWriter String m => m a -> m Unit
showIfSilent = listen >=> snd >>> \str ->
  when (null str) $ asks show >>= tell