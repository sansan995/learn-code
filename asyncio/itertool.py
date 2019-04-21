
def accumulate(iterable, func = operator.add):
    'Return runging totals'
    # accumulate([1,2,3,4,5]) ---> 1 3 4 10 15
    it = iter(iterable)
    try:
        total = next(it)
    except(StopIteration):
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


def chain(*iterables):
    # chain('ABC','DEF') ---> A B C D E F
    for it in iterable:
        for element in it:
            yield element

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n -r:
                break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j - 1] + 1
            yield tuple(pool[i] for i in indices)

