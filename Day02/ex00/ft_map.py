from collections.abc import Iterable


def ft_map(function_to_apply, iterable):
    assert isinstance(iterable, Iterable), "object is not iterable"
    for i in iterable:
        yield function_to_apply(i)


if isinstance(4, Iterable):
    print("Iterable")
else:
    print("not Iterable")
# Example 1:
x = [1, 2, 3, 4, 5]
'''for i in ft_map(lambda dum: dum + 1, 4):
    print(i)'''
print(ft_map(lambda dum: dum + 1, x))
print()
print(list(ft_map(lambda t: t + 1, x)))
x = ft_map(lambda t: t + 1, x)
print(x)
print(list(x))
print(list(x))
