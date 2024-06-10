import numpy as np
import imageio 
import scipy.ndimage
import cv2

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.1989,0.5878,0.1140])

def dodge(front, back):
    final_sketch = front * 255 / (255 - back )
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch

img = "cicek.jpg"

# Resmi yükle
ss = cv2.imread(img)
# Resmi gri tonlamalı hale dönüştür
gray = rgb2gray(ss)
# Ters gri tonlamalı resim elde et
i = 255 - gray 
# Gaussian blur uygula
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=25)
# Dodge efekti uygula
r = dodge(blur, gray)
# Sonucu PNG olarak kaydet
cv2.imwrite("rob4.png", r)