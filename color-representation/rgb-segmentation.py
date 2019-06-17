import cv2

image = cv2.imread('../resources/images/fruits.png')

blue, green, red = cv2.split(image)

cv2.imshow('R Channel', red)
cv2.imshow('G Channel', green)
cv2.imshow('B Channel', blue)

cv2.imwrite('../runtime/images/fruits_red_channel.jpeg', red)
cv2.imwrite('../runtime/images/fruits_green_channel.jpeg', green)
cv2.imwrite('../runtime/images/fruits_blue_channel.jpeg', blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
