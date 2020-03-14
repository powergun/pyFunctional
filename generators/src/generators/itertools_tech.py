import itertools
from typing import Iterable, Any, List


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
