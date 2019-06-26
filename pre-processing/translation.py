import cv2
import numpy as np

original_image = cv2.imread('../resources/images/leaf.png', 0)
lines, columns = original_image.shape[:2]

matrix = np.float32([[1, 0, 100], [0, 1, 100]])

translated_image = cv2.warpAffine(original_image, matrix, (columns, lines))

cv2.imshow('Translated', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
