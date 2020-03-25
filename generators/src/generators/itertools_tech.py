import itertools
from typing import Iterable, Any, List, Tuple, TypeVar


# source: FP Python P/48
# itertools.tee()
def limits(it: Iterable[Any]) -> Any:
    # tee returns a tuple of N independent iterators
    # this leaves the original iterator untouched;
    # we can consume these two clones to get maximum and min val

    max_tee, min_tee = itertools.tee(it, 2)
    return max(max_tee), min(min_tee)


# composing iterators
def take(it: Iterable[Any], n: int) -> List[Any]:
    return [x for x, _ in zip(it, range(n))]


# inspired by: Functional Python Programming P/69
# given s = {1, 2, 3, 4, 5..}
# want  {(1, 2), (2, 3), (3, 4)...}
T_ = TypeVar('T_')
TT = Tuple[T_, T_]
IterTT = Iterable[TT]
IterT = Iterable[T_]


def iter_pairs(it: IterT) -> IterTT:
    # the original iterator, it, must be preserved
    first, second = itertools.tee(it, 2)
    try:
        next(second)
    except StopIteration:
        return iter(tuple())
    return zip(first, second)