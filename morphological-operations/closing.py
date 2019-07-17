import cv2

image = cv2.imread('../resources/images/bearing-noise-inner.png')
structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
processed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, structuring_element)

cv2.imshow('Original', image)
cv2.imshow('Processed', processed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
