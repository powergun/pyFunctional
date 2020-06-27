# source:
# https://towardsdatascience.com/8-advanced-python-tricks-used-by-seasoned-programmers-757804975802
# a data class requires a minimal amount of code
# you can compare data classes because __eq__ is implemented for you
# you can easily print a data class for debugging because __repr__ is implemented as well
# data classes require type hints, reduced the chances of bugs

import dataclasses
import unittest


@dataclasses.dataclass
class Card:
    rank: str
    suit: str


class TestDataClass(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(Card('1', '2'), Card('1', '2'))


if __name__ == '__main__':
    unittest.main()
