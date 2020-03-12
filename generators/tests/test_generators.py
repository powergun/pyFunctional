import unittest

from generators import list_comprehension


class TestListComprehension(unittest.TestCase):
    def test_sum(self):
        list_comprehension.do_sum(range(1, 10))
