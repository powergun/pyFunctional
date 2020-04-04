# Iteration

## Sliding Window

Note, [more-itertools](https://github.com/more-itertools/more-itertools)
has an implementation called `windowed` which uses deque's FILO mechanism
to create the sliding window

```text
  [ x x x ] <- x ....
x [ x x x ] x ....
```

see `ABIter` in sliding_window_iter.py for an implementation that
simulates `ack` and `grep`'s before, after context

## define enumerate in terms of zip\*() and count()

source: functional python programming P/183

## cycle and repeat

cycle(it)

repeat(value)
