from typing import NamedTuple

class Item(NamedTuple):
    count: int
    cost: int


if __name__ == '__main__':
    item = Item(10, 10)

    # prefer dot accessor
    assert item.count == 10, ""
    assert item[0] == 10, ""

