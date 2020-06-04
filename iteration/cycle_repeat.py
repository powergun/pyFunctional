import itertools

# take() implemented in terms of islice()
# https://docs.python.org/2/library/itertools.html


nums = [1, 2, 3]
for i in itertools.islice(itertools.cycle(iter(nums)), 10):
    print(i)

