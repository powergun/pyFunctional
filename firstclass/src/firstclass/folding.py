#!/usr/bin/env python3

import functools
from typing import TypeVar, Iterable, Callable, List

A = TypeVar('A')
B = TypeVar('B')


# inspired by:
# https://www.burgaud.com/foldl-foldr-python
# which mentions the best way to reverse a python list: [::-1]
# https://stackoverflow.com/questions/3705670/best-way-to-create-a-reversed-list-in-python/3705676#3705676
def fold(func: Callable[[B, A], B], acc: B, xs: Iterable[A]) -> B:
    return functools.reduce(func, xs, acc)
