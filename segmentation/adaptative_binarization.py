import cv2

image = cv2.imread('../resources/images/pills.png', 0)
processed_image = cv2.medianBlur(image, 7)

binarized_image = cv2.adaptiveThreshold(
    processed_image,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11,
    5
)

cv2.imshow('Original', image)
cv2.imshow('Binarized', binarized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
