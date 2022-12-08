import numpy as np


class ColorFilter:
    def check(self, tpl):
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

    def invert(self, array):
        if not isinstance(array, np.ndarray):
            return
        colors_arr = array[:, :, :3]
        invert_color_arr = 255 - colors_arr
        is_png = array.shape[2] == 4
        if is_png:
            alpha_ch = array[:, :, 3]
            return np.dstack((invert_color_arr, alpha_ch))
        else:
            return invert_color_arr

    def to_green(self, array):
        if not isinstance(array, np.ndarray):
            return
        im = array.copy()
        im[:, :, (0, 2)] = 0
        return im

    def to_blue(self, array):
        if not isinstance(array, np.ndarray):
            return
        im = array.copy()
        im[:, :, (0, 1)] = 0
        return im

    def to_red(self, array):
        if not isinstance(array, np.ndarray):
            return
        im = array.copy()
        im[:, :, (1, 2)] = 0
        return im
