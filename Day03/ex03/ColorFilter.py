import numpy as np


class ColorFilter:
    def __check_ndarray(*args, **kwarg):
        def inner(*args, **kwarg):
            # Check if tuple is correct
            array = args[0]
            if not (isinstance(array, np.ndarray) and
                    ('float' in str(array.dtype) or 'int' in str(array.dtype))):
                return None
            try:
                return_value = funct(*args, **kwarg)
            except:
                return None
            return return_value
        return inner

    def invert(self, array: np.ndarray) -> np.ndarray:
        return 255 - array[:, :, :3]

    def invert2(self, array: np.ndarray) -> np.ndarray:
        '''This one keeps the alpha parameter'''
        colors_arr = array[:, :, :3]
        invert_color_arr = 255 - colors_arr
        is_png = array.shape[2] == 4
        if is_png:
            alpha_ch = array[:, :, 3]
            return np.dstack((invert_color_arr, alpha_ch))
        else:
            return invert_color_arr

    def to_green(self, array: np.ndarray) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            return
        im = array.copy()
        im[:, :, (0, 2)] = 0
        return im

    def to_blue(self, array: np.ndarray) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            return
        im = array.copy()
        im[:, :, (0, 1)] = 0
        return im

    def to_red(self, array: np.ndarray) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            return
        im = array.copy()
        im[:, :, (1, 2)] = 0
        return im

    def to_celluloid(self, array: np.ndarray) -> np.ndarray:
        ret = array[:, :, :3]
        threshold = np.arange(0, 256, 255//4)
        for i in range(len(threshold) - 1):
            ret[(ret > threshold[i]) & (ret < threshold[i+1])] = threshold[i]
        return ret

    def to_grayscale(self, array: np.ndarray, filter: str, **kwargs):
        if filter not in ('m', 'mean', 'w', 'weight'):
            return None
        if kwargs and (sum(kwargs.values()) != 1 or len(kwargs) != 3):
            return None
        new_arr = array[:, :, :3]
        if filter in ('m', 'mean'):
            for row in new_arr:
                for pixel in row:
                    gray = pixel.sum() / 3
                    for i in range(0, 3):
                        pixel[i] = gray
        else:
            weight = np.array(kwargs.values())
            w_arr = np.array([kwargs['r'], kwargs['b'], kwargs['g']])
            for row in new_arr:
                for pixel in row:
                    gray = np.sum([pixel * w_arr])
                    for i in range(0, 3):
                        pixel[i] = gray
        return new_arr
