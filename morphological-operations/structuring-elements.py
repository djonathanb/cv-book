import cv2
import numpy as np

# Rect
rect_element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print()
print(rect_element)

# Ellipsis
ellipsis_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print()
print(ellipsis_element)

# Cross
cross_element = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print()
print(cross_element)

# Custom
custom_element = np.matrix([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
], np.uint8)
print()
print(custom_element)
