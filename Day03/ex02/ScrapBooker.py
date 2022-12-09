import numpy as np


def check(tpl):
    # Check if tuple is correct
    if not isinstance(tpl, tuple):
        return False
    if not len(tpl) == 2:
        return False
    if not isinstance(tpl[0], int) or not isinstance(tpl[1], int):
        return False
    if tpl[0] < 0 or tpl[1] < 0:
        return False
    return True


class ScrapBooker:

    def crop(self, array, dim, pos=(0, 0)):
        if not isinstance(array, np.ndarray) or not check(dim) or not check(pos):
            return
        return array[pos[0]:pos[0] + dim[0], pos[1]:pos[1] + dim[1]]

    def thin(self, array, n, axis):
        if not isinstance(array, np.ndarray) or not isinstance(n, int):
            return
        if n < 0 or axis not in (0, 1):
            return
        if axis:
            axis = 0
        else:
            axis = 1
        return np.delete(array, n-1, axis)

    def juxtapose(self, array, n, axis):
        if not isinstance(array, np.ndarray) or not isinstance(n, int):
            return
        if n < 0 or axis not in (0, 1):
            return
        if axis:
            return np.column_stack([array] * n)
            return np.tile(array, (1, n))
        else:
            return np.vstack([array] * n)
            return np.tile(array, (1, n))

    def mosaic(self, array, dim):
        if not isinstance(array, np.ndarray) or not check(dim):
            return
        return self.juxtapose(self.juxtapose(array, dim[0], 0), dim[1], 1)
