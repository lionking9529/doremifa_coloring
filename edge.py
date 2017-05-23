import cv2
import numpy as np
from matplotlib import pyplot as plt
from glob import glob
from random import randint


cimg = cv2.imread("index.jpeg" ,0)

img_edge = cv2.adaptiveThreshold(cimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=15)

plt.subplot(131),plt.imshow(cimg)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(img_edge,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
