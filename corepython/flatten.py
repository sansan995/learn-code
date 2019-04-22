def list_or_tuple(x):
    return isinstance(x, (list, tuple))
def flatten(sequence, to_expand=list_or_tuple):
    for item in sequence:
        if to_expand(item):
            for subitem in flatten(item, to_expand):
                yield subitem
        else:
            yield item

for x in flatten([1, 2, [3, [ 4 ], 4, [ 4, 5, 6 ], [ 8,], 9], 43]):
    print(x)

def flattendigui(sequence, to_expand = list_or_tuple):
    iterators = [ iter(sequence) ]
    while iterators:
        for item in iterators[-1]:
            if to_expand(item):
                iteraors.append(iter(item))
                break
            else:
               yield item
        else:
            iterators.pop()


    
