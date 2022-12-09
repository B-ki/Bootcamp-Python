from collections.abc import Iterable


def ft_reduce(function_to_apply, iterable):
    assert isinstance(iterable, Iterable), "object is not iterable"
    seq = iter(iterable)
    x = next(seq)
    for i in seq:
        x = function_to_apply(x, i)
    return x


lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
j = iter(lst)
print(ft_reduce(lambda u, v: u + v, lst))
