import cv2

image = cv2.imread('../resources/images/coffee.png', 0)
ret, binarized_image = cv2.threshold(image, 135, 255, cv2.THRESH_BINARY_INV)

# morphological operations to noise removing
structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
processed_image = cv2.morphologyEx(
    binarized_image, cv2.MORPH_CLOSE, structuring_element
)
processed_image = cv2.erode(
    processed_image, structuring_element, iterations=2
)

cv2.imshow('Original', image)
cv2.imshow('Binarized', binarized_image)
cv2.imshow('Whithout noise', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
