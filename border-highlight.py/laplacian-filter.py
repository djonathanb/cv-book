import cv2

image = cv2.imread("../resources/images/parking-b&w.png")
filtered_image = cv2.Laplacian(image, cv2.CV_8U)

cv2.imshow("Original", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
