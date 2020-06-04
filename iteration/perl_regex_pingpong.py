# perl has a powerful iteration idiom called pingpong:

# /pattern/../pattern/ and do ...
# 
# this selects all the lines starting from pattern to pattern, inclusive

# in python, I implemented this idiom like so:
import re

def pingpong(iterator, pattern_start, pattern_stop):
    def _ignore_unless(in_it, f):
        for l in in_it:
            if f(l):
                break
        return in_it

    def _unless(in_it, f):
        for l in in_it:
            if f(l):
                break
            else:
                yield l

    it_ = _ignore_unless(iterator,
                         lambda l: re.search(pattern_start, l) is not None)
    return _unless(it_, lambda l: re.search(pattern_stop, l) is not None)

# example:
text = '''


  Background:
    Given this calendar exists:
      | date       | isBusinessDate |
      | 2020-01-01 | Y              |
      | 2020-01-02 | Y              |
      | 2020-01-03 | Y              |
      | 2020-01-04 | N              |
      | 2020-01-05 | N              |
      | 2020-01-06 | Y              |
      | 2020-01-07 | Y              |
      | 2020-01-08 | Y              |
      | 2020-01-09 | Y              |
      | 2020-01-10 | Y              |
      | 2020-01-11 | N              |
      | 2020-01-12 | N              |
      | 2020-01-13 | Y              |
      | 2020-01-14 | Y              |
      | 2020-01-15 | Y              |
      | 2020-01-16 | Y              |
      | 2020-01-17 | Y              |
      | 2020-01-18 | N              |
      | 2020-01-19 | N              |
      | 2020-01-20 | Y              |
      | 2020-01-21 | Y              |
      | 2020-01-22 | Y              |
      | 2020-01-23 | Y              |
      | 2020-01-24 | Y              |
      | 2020-01-25 | N              |
      | 2020-01-26 | N              |
      | 2020-01-27 | Y              |
      | 2020-01-28 | Y              |
      | 2020-01-29 | Y              |
      | 2020-01-30 | Y              |
      | 2020-01-31 | Y              |
      | 2020-02-01 | N              |
      | 2020-02-02 | N              |
      | 2020-02-03 | Y              |
      | 2020-02-04 | Y              |
      | 2020-02-05 | Y              |
      | 2020-02-06 | Y              |
      | 2020-02-07 | Y              |
      | 2020-02-08 | N              |
      | 2020-02-09 | N              |
      | 2020-02-10 | Y              |
      | 2020-02-11 | Y              |
      | 2020-02-12 | Y              |
      | 2020-02-13 | Y              |
      | 2020-02-14 | Y              |
      | 2020-02-15 | N              |
      | 2020-02-16 | N              |
      | 2020-02-17 | Y              |
      | 2020-02-18 | Y              |
      | 2020-02-19 | Y              |
      | 2020-02-20 | Y              |
      | 2020-02-21 | Y              |
      | 2020-02-22 | N              |
      | 2020-02-23 | N              |
      | 2020-02-24 | Y              |
      | 2020-02-25 | Y              |
      | 2020-02-26 | Y              |
      | 2020-02-27 | Y              |
      | 2020-02-28 | Y              |
      | 2020-02-29 | N              |
      | 2020-03-01 | N              |
      | 2020-03-02 | Y              |
      | 2020-03-03 | Y              |
      | 2020-03-04 | Y              |
      | 2020-03-05 | Y              |
      | 2020-03-06 | Y              |
      | 2020-03-07 | N              |
      | 2020-03-08 | N              |
      | 2020-03-09 | Y              |
      | 2020-03-10 | Y              |
      | 2020-03-11 | Y              |
      | 2020-03-12 | Y              |
      | 2020-03-13 | Y              |
      | 2020-03-14 | N              |
      | 2020-03-15 | N              |

    And today is 2020-01-15
'''
lines = text.split('\n')
for l in pingpong(iter(lines), r'Given', r'^\s*$'):
    print(l)

