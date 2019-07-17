import cv2

image = cv2.imread('../resources/images/rice.png', 0)
structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
processed_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, structuring_element)

treated_image = cv2.add(processed_image, processed_image)

cv2.imshow('Original', image)
cv2.imshow('Result', processed_image)
cv2.imshow('Final', treated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()