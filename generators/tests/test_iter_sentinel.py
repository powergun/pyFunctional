import unittest
import io

from generators import iter_sentinel


class TestIterSentinel(unittest.TestCase):
    def test_(self):
        sut = '''
there is a cow
is
there 
is 
a cow
'''
        fp = io.StringIO(sut)
        self.assertEqual(iter_sentinel.read_all(fp, 'is\n', r'^there'),
                         ['there is a cow\n'])
