# source:
# functional python programming L554

from typing import Iterator, Iterable, Set, FrozenSet
import itertools


def do_sum(it: Iterator[int]) -> int:
    # generator does not create a variable in the calling context
    # elem is not accessible
    o = sum(elem for elem in it if elem % 3 == 0 or elem % 5 == 0)

    # local variable 'elem' referenced before assignment
    # elem += 1
    return o


def set_comprehension() -> None:
    s = {i for i in range(10)}
    fzs = frozenset(i for i in range(10))
    assert s == fzs


def dict_comprehension() -> None:
    d = {i: i for i in range(10)}
    assert len(d) == 10
