import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../resources/images/leaf-gray.png')
# ravel turns the pixels' matrix into a vector
plt.hist(image.ravel(), 256, [0, 256])
plt.show()
