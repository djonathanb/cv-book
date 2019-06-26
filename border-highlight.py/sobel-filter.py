import cv2

image = cv2.imread("../resources/images/parking-b&w.png")

sobelx = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_8U, 0, 1, ksize=3)

cv2.imshow("Original", image)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
