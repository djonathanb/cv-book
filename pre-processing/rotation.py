import cv2

original_image = cv2.imread('../resources/images/leaf.png', 0)
lines, columns = original_image.shape

matrix = cv2.getRotationMatrix2D((columns / 2, lines / 2), 90, 1)

rotated_image = cv2.warpAffine(original_image, matrix, (columns, lines))

cv2.imshow('Rotated', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
