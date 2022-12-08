import matplotlib
import filetype
from PIL import Image
import numpy as np


class ImageProcessor:
    def load(path):
        if not isinstance(path, str):
            print(path, "is not correct")
            return
        if not filetype.is_image(path):
            print(path, "is not correct")
            return
        img = Image.open(path)
        print(img.size)
        return np.asarray(img)

    def display(array):
        pilImage = Image.fromarray(array)
        pilImage.show()
