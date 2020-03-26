# inspired by: functional python programming P/122
# the NullAware object is essentially a Maybe value in haskell
# that only performs the computation if it is Some(_)
# recall Haskell's Data.Maybe module also provides the maybe()
# function that returns a hardcoded default value if the input
# is Nothing

from typing import TypeVar, Callable, Iterable, Optional

T_ = TypeVar('T_')
R_ = TypeVar('R_')
Value = Optional[T_]


# how to define callable's type hint:
# https://stackoverflow.com/questions/37835179/how-can-i-specify-the-function-type-in-my-type-hints
def maybe(f: Callable[[Value], R_], defa: R_, x: Value) -> R_:
    return defa if x is None else f(x)
