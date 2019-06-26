import cv2

original_image = cv2.imread("../resources/images/parking-b&w.png")
new_image = cv2.Canny(original_image, 100, 200)

cv2.imshow("Borders", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
