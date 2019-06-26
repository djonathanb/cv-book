import cv2

image = cv2.imread("../resources/images/radiography.png")
softed_image = cv2.GaussianBlur(image, (13, 13), 3)
image_details = 3 * cv2.subtract(image, softed_image)
highlighted_image = cv2.add(image, image_details)

cv2.imshow("Original", image)
cv2.imshow("Softed", softed_image)
cv2.imshow("Details", image_details)
cv2.imshow("Highlighted", highlighted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
