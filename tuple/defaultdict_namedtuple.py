from typing import NamedTuple
from collections import defaultdict


class CallCount(NamedTuple):
    count: int
    cost: int

    @staticmethod
    def empty():
        return CallCount(0, 0)
    
    def __iadd__(self, o):
        return CallCount(self.count + o[0], self.cost + o[1])

def main():
    # use the second form of defaultdict ctor that takes a "default factory"
    # function; this function produces a value of type T
    rec = defaultdict(CallCount.empty)
    print(rec['asd'])
    
    # NOTE:
    # with overloading __iadd__() method, this will produce a plain tuple
    # rec['asd'] += (1, 1)

    rec['asd'] = CallCount(rec['asd'].count + 1, rec['asd'].cost + 10)
    print(rec['asd'])
    
    rec['bsd'] += (9, 9)
    print(rec['bsd'])


if __name__ == '__main__':
    main()
