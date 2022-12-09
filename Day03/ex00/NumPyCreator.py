import numpy as np
from collections.abc import Iterable


class NumPyCreator:
    def from_list(self, lst):
        if not isinstance(lst, list):
            return
        it = iter(lst)
        the_len = len(next(it))
        if not all(len(x) == the_len for x in it):
            return
        return np.array(lst, dtype=object)

    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple):
            return
        return np.asarray(tpl)

    def from_iterable(self, itr):
        if not isinstance(itr, Iterable):
            return
        return np.fromiter(itr, type(itr[0]))

    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple):
            return
        return np.full(shape, value)

    def random(self, shape):
        if not isinstance(shape, tuple):
            return
        return np.random.random_sample(shape)

    def identity(self, n):
        if not isinstance(n, int) or not n > 0:
            return
        return np.identity(n)
