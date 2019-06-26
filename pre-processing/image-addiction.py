import cv2

red_chips_image = cv2.imread("../resources/images/red-chips.png")
black_chips_image = cv2.imread("../resources/images/black-chips.png")

image = cv2.add(red_chips_image, black_chips_image)

cv2.imshow('Added', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
