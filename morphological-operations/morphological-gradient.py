import cv2

image = cv2.imread('../resources/images/bearing.png')
structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
processed_image = cv2.morphologyEx(
    image, cv2.MORPH_GRADIENT, structuring_element
)

cv2.imshow('Original', image)
cv2.imshow('Result', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
