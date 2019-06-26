"""
Blur filter calcs a new value for each pixel based on a mask that analises
the average value of pixel's neighboors
"""
import cv2

original_image = cv2.imread("../resources/images/woman-salt-and-pepper-noise.png")
blurred_image = cv2.medianBlur(original_image, 5)

cv2.imshow("Blurred", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
