"""
Blur filter calcs a new value for each pixel based on a mask that analises
the average value of pixel's neighboors
"""
import cv2

original_image = cv2.imread("../resources/images/parking-gaussian-noise.png")
blurred_image = cv2.bilateralFilter(original_image, 9, 75, 75)

cv2.imshow("Filtered", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
