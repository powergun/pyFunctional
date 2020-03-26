import unittest
import io

from generators import iter_sentinel


class TestIterSentinel(unittest.TestCase):
    def test_read_from_file(self):
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

    def test_random_till_lucky(self):
        it = iter_sentinel.random_till_lucky(1, 30, 15)
        print(list(it))
