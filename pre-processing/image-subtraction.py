import cv2

red_chips_position_1 = cv2.imread("../resources/images/red-chip-position-1.png")
red_chips_position_2 = cv2.imread("../resources/images/red-chip-position-2.png")

image = cv2.subtract(red_chips_position_1, red_chips_position_2)

cv2.imshow('Subtracted', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
