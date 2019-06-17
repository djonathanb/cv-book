import cv2

image = cv2.imread('../resources/images/fruits.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

cv2.imshow('RGB', image)
cv2.imshow('RGB to Gray Scale', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
