#!/usr/bin/env python3

import itertools

xs = itertools.groupby(range(30), key=lambda x: x * x / 3 < 5)
for v, it in xs:
    print(v, list(it))

xs = itertools.groupby('{:b}'.format(0xbeef), key=lambda ch: ch == '0')
for v, it in xs:
    print(v, sum((ord(n) for n in it)))
