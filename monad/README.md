# Monad in Python

## PyMonad and Thoughts

inspired by the PyMonad chapter in Functional Python Programming
book; I briefly tried this library, `pymonad` but was not impressed.

Python does not need monad as it is imperative by nature.

If I need to separate the effect from the pure computation I can
use class and function. I can use generator and some meld if-
statements

Recall that local, encapsulated mutable state is not harmful.

Another fact the Haskell-like monad won't play well in Python is
that Python does not allow custom operators, therefore these Haskell
idioms do not have their counterpart in Python - not without
extensive hacking. I feel the `>>` bind operator brought by
pymonad is one of these hacks.
