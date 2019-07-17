import cv2
import numpy as np

image = cv2.imread('../resources/images/sudoku.png', 0)

modified_image = image

# comparing binarizations
ret, simple_binarized_image = cv2.threshold(
    modified_image, 135, 255, cv2.THRESH_BINARY_INV
)

processed_image = cv2.medianBlur(modified_image, 7)

binarized_image = cv2.adaptiveThreshold(
    processed_image,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11,
    5
)

cv2.imshow('Original', image)
cv2.imshow('Simple Binarized', simple_binarized_image)
cv2.imshow('Adaptative Binarized', binarized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
