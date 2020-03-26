# source: functional python programming P/107
# building iterators to consume the values created by a callable
# object (for example a function), until a sentinel value is found
# this feature is sometimes used with the read() function of a file
# to consume items until some end-of-line or end-of-file sentinel
# value is found.

from typing import IO, List, Text
import functools
import itertools
import re
import random


# type hint for file-like objects
# source:
# https://stackoverflow.com/questions/38569401/type-hint-for-a-file-or-file-like-object
# I can also use TextIO
def read_all(fp: IO[Text], sentinel: Text, pattern: Text) -> List[Text]:
    it = iter(fp.readline, sentinel)
    sel = filter(functools.partial(re.search, pattern), it)
    return list(sel)


# a callable can be passed to iter() function too
# see functional python programming P/107
def random_till_lucky(lower, upper, lucky_num):
    gen = lambda: random.randint(lower, upper)
    return iter(gen, lucky_num)
