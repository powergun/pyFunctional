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
