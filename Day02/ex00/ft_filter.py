from collections.abc import Iterable


def ft_filter(function_to_apply, iterable):
    assert isinstance(iterable, Iterable), "object is not iterable"
    for i in iterable:
        if function_to_apply(i):
            yield i


if isinstance(4, Iterable):
    print("Iterable")
else:
    print("not Iterable")
# Example 1:
x = [1, 2, 3, 4, 5]
'''for i in ft_map(lambda dum: dum + 1, 4):
    print(i)'''
print(ft_filter(lambda dum: not (dum % 2), x))
print()
print(list(ft_filter(lambda dum: not (dum % 2), x)))
