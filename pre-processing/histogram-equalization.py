import cv2
import numpy as np
from matplotlib import pyplot as plt

original_image = cv2.imread('../resources/images/pointers.png', 0)
equalized_image = cv2.equalizeHist(original_image)

cv2.imshow('Original', original_image)
cv2.imshow('Equalized', equalized_image)

plt.subplot(1, 2, 1)
plt.hist(original_image.ravel(), 256, [0, 256])
plt.title('Original')

plt.subplot(1, 2, 2)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Equalized')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
