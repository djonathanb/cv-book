import cv2

image = cv2.imread('../resources/images/fruits.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(image)

new_image = cv2.merge((hue, saturation, value))
new_image = cv2.cvtColor(new_image, cv2.COLOR_HSV2BGR)

cv2.imshow('HSV Merged', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
