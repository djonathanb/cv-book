import cv2
import numpy as np

original_image = cv2.imread('../resources/images/sudoku.png')

initial_points = np.float32([[189, 87], [459, 84], [192, 373], [484, 372]])
final_points = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])

matrix = cv2.getPerspectiveTransform(initial_points, final_points)
modified_image = cv2.warpPerspective(original_image, matrix, (500, 500))

cv2.imshow('Modified Sudoku - Perspective', modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
