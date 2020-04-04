import unittest

import operator
from reduce import folding


class TestFoldl(unittest.TestCase):
    def test_small_stream(self):
        r = range(30)
        o = folding.fold(operator.add, 0, r)
        self.assertEqual(o, sum(r))

    def test_large_stream(self):
        # does not blow up stack
        r = range(100000000)
        o = folding.fold(operator.add, 0, r)
        self.assertTrue(o)

    def test_order(self):
        r = range(4)
        o = folding.fold(lambda x, y: print(x, y) or x + y, 0, r)
        # pytest -s
        # see: https://docs.pytest.org/en/latest/capture.html
        # the order is 0 1, 1 2, 3 3
        # therefore it is NOT a foldr!
        self.assertEqual(o, 6)
