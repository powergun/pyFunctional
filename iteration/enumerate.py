#!/usr/bin/env python3

import itertools

enumerate_ = lambda xs, start=0: zip(itertools.count(start), xs)
assert list(enumerate(range(10))) == list(enumerate(range(10)))
