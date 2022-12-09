from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker
import numpy as np


np_img = ImageProcessor.load("LesAmoureux.png")
# ImageProcessor.display(new_arr)
# print(np_img)
SB = ScrapBooker()
new_arr = SB.mosaic(SB.crop(np_img, (300, 300), (70, 180)), (6, 4))
ImageProcessor.display(new_arr)
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print(arr2)
print(SB.thin(arr2, 3, 0))
arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(SB.juxtapose(arr3, 3, 1))
print(arr3)
print(SB.mosaic(arr3, (2,3)))
