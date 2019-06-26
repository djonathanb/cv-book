import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../resources/images/leaf.png')
blue, green, red = cv2.split(image)

plt.subplot(1, 3, 1)
plt.hist(blue.ravel(), 256, [0, 256])
plt.title('Blue')

plt.subplot(1, 3, 2)
plt.hist(green.ravel(), 256, [0, 256])
plt.title('Green')

plt.subplot(1, 3, 3)
plt.hist(red.ravel(), 256, [0, 256])
plt.title('Red')

plt.show()
