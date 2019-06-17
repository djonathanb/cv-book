import cv2

image = cv2.imread('../resources/images/cat.jpg')
cv2.imshow('Cat', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
