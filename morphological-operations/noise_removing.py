import cv2

image = cv2.imread('../resources/images/bearing-noise.png')
structuring_element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
processed_image = cv2.erode(image, structuring_element, iterations=1)

cv2.imshow('Original', image)
cv2.imshow('Result', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
