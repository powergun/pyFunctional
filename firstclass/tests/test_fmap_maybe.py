import unittest
import functools
import itertools

from firstclass import fmap_maybe


class TestFmapMaybe(unittest.TestCase):
    def test_fmap_all(self):
        xs = itertools.chain(range(4), (None, ), range(8))
        ys = map(functools.partial(fmap_maybe.maybe, lambda x: x + 10, 0), xs)
        self.assertEqual(len(list(ys)), 13)
