from typing import NamedTuple
from collections import defaultdict


class CallCount(NamedTuple):
    count: int
    cost: int

    @staticmethod
    def empty():
        return CallCount(0, 0)


def main():
    # use the second form of defaultdict ctor that takes a "default factory"
    # function; this function produces a value of type T
    rec = defaultdict(CallCount.empty)
    print(rec['asd'])
    rec['asd'] += (1, 1)


if __name__ == '__main__':
    main()
