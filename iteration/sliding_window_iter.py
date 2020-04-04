# NOTE: a real world example is `ack -A <NUM> -B <NUM>`
# the ABIter below implements this mechanism

import collections
import itertools


class WindowIter:
    # xs=range(10), n=7
    # [[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]
    def __init__(self, it, n=1):
        self.real_it = it
        self.cached = collections.deque()
        self.size = n

    def __iter__(self):
        for elem in self.real_it:
            if len(self.cached) < self.size:
                self.cached.append(elem)
                continue
            self.cached.popleft()
            self.cached.append(elem)
            yield list(self.cached)


class DefaultWindowIter(WindowIter):
    # xs=range(10), n=7
    # [[None, None, None, None, None, None, 0], [None, None, None, None, None, 0, 1],
    # [None, None, None, None, 0, 1, 2], [None, None, None, 0, 1, 2, 3],
    # [None, None, 0, 1, 2, 3, 4], [None, 0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6],
    # [1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]
    def __init__(self, it, n=1):
        super(DefaultWindowIter, self).__init__(it, n=n)
        self.cached = collections.deque([None] * n)


class CenteredIter(DefaultWindowIter):
    # xs=range(10), n=7
    # [[0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6],
    # [1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9],
    # [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9]]
    def __iter__(self):
        for elem in itertools.chain(self.real_it, [None] * self.size):
            if len(self.cached) < self.size:
                self.cached.append(elem)
                continue
            self.cached.popleft()
            self.cached.append(elem)
            c = self.cached[len(self.cached) // 2]
            if c is None:
                continue
            yield [e for e in self.cached if e is not None]


class ABIter:
    # xs=range(10), n=7
    # [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7],
    # [0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # [2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9],
    # [5, 6, 7, 8, 9], [6, 7, 8, 9]]
    def __init__(self, it, a, b):
        self.real_it = it
        self.a = a
        self.b = b
        self.size = a + b + 1
        self.cached = collections.deque([None] * self.size)

    def __iter__(self):
        for elem in itertools.chain(self.real_it, [None] * self.size):
            if len(self.cached) < self.size:
                self.cached.append(elem)
                continue
            self.cached.popleft()
            self.cached.append(elem)
            c = self.cached[self.a]
            if c is None:
                continue
            yield [e for e in self.cached if e is not None]


class ABIterV2:
    # to yield: before_context, elem, after_context
    # xs=range(10), n=7
    # [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7],
    # [0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # [2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9],
    # [5, 6, 7, 8, 9], [6, 7, 8, 9]]
    def __init__(self, it, a, b):
        self.real_it = it
        self.a = a
        self.b = b
        self.size = a + b + 1
        self.cached = collections.deque([None] * self.size)

    def __iter__(self):
        for elem in itertools.chain(self.real_it, [None] * self.size):
            if len(self.cached) < self.size:
                self.cached.append(elem)
                continue
            self.cached.popleft()
            self.cached.append(elem)
            c = self.cached[self.a]
            if c is None:
                continue
            l = list(self.cached)
            before_context = [e for e in l[:self.a] if e is not None]
            after_context = [e for e in l[self.a + 1:] if e is not None]
            yield before_context, c, after_context


if __name__ == '__main__':
    xs = range(10)
    it = ABIterV2(xs, 3, 4)
    print(list(it))
