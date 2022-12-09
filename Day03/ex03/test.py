from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker
from ColorFilter import ColorFilter
import numpy as np


np_img = ImageProcessor.load("LesAmoureux.png")
# ImageProcessor.display(new_arr)
# print(np_img)
SB = ScrapBooker()
CF = ColorFilter()
print(np_img.shape)
mosaic = SB.mosaic(SB.crop(np_img, (300, 300), (70, 180)), (6, 4))
new_arr = CF.to_blue(mosaic)
new_arr2 = CF.invert2(mosaic)
new_arr4 = CF.invert2(mosaic)
new_arr3 = CF.to_red(mosaic)
new_arr5 = CF.to_celluloid(mosaic)
# new_arr6 = CF.to_grayscale(mosaic, 'w', r=0, b=0.5, g=0.5)
# ImageProcessor.display(new_arr6)
ImageProcessor.display(new_arr5)
ImageProcessor.display(np.column_stack([new_arr, new_arr2, new_arr3]))
