import cv2

image = cv2.imread('../resources/images/fruits.png')

blue, green, red = cv2.split(image)

new_image = cv2.merge((blue, green, red))
cv2.imshow('Merging Fruits', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
