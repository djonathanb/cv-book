import cv2

image = cv2.imread('../resources/images/fruits.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(image)
cv2.imshow('Hue Channel', hue)
cv2.imshow('Saturation Channel', saturation)
cv2.imshow('Value Channel', value)

cv2.waitKey(0)
cv2.destroyAllWindows()
