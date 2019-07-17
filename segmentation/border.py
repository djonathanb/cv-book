import cv2
import numpy as np

image = cv2.imread('../resources/images/coffee.png', 0)

ret, binarized_image = cv2.threshold(image, 135, 255, cv2.THRESH_BINARY_INV)

e = np.ones((3, 3), np.uint8)
processed_image = cv2.morphologyEx(binarized_image, cv2.MORPH_CLOSE, e)
processed_image = cv2.erode(processed_image, e, iterations=2)

segmented_image = cv2.Canny(processed_image, 100, 200)

cv2.imshow('Binarized', binarized_image)
cv2.imshow('Processed', processed_image)
cv2.imshow('Segmented', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
