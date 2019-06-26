import cv2

red_chips_image = cv2.imread("../resources/images/red-chips.png")
black_chips_image = cv2.imread("../resources/images/black-chips.png")

image = cv2.addWeighted(black_chips_image, 0.2, red_chips_image, 1.0, 0)

cv2.imshow('Mixed', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
