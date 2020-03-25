import unittest
from generators import itertools_tech


class TestItertoolsTechniques(unittest.TestCase):
    def test_limits(self):
        it = range(1, 30)
        ma, mi = itertools_tech.limits(it)
        self.assertEqual(1, mi)
        self.assertEqual(29, ma)

    def test_take(self):
        self.assertEqual(['i', 'd', 'd', 'q'],
                         itertools_tech.take("iddqd_e1m1_idkfa", 4))
        self.assertEqual(['i', 'd'], itertools_tech.take("id", 100))

    def test_iter_pairs(self):
        i = list(itertools_tech.iter_pairs(iter(tuple())))
        self.assertEqual(i, [])
        i = list(itertools_tech.iter_pairs(range(1)))
        self.assertEqual(i, [])
        i = list(itertools_tech.iter_pairs(range(5)))
        self.assertEqual(i, [(0, 1), (1, 2), (2, 3), (3, 4)])

        # this does not work!!
        # iter wraps a mutable container
        # i = list(itertools_tech.iter_pairs(iter([0, 1, 2, 3, 4])))
        # self.assertEqual(i, [(0, 1), (1, 2), (2, 3), (3, 4)])
