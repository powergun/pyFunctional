# source:
# functional python programming: P/201
# itertools.starmap() is *a version of map()

import itertools


def demo():
    def f(a, b):
        return a + b

    xs = [(1, 2), (3, 4)]
    it = itertools.starmap(f, xs)
    assert list(it) == [3, 7]