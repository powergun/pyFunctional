# source:
# functional python programming P/201


def demo():
    def f(*a):  # f is to take 3 args!
        return sum(a)

    it = map(f, range(3), range(3), range(3))
    assert list(it) == [0, 3, 6]
