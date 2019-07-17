import cv2

image = cv2.imread('../resources/images/coffee.png', 0)
binarization_type = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
threshold, binarized_image = cv2.threshold(image, 0, 255, binarization_type)

print(threshold)

cv2.imshow('Original', image)
cv2.imshow('Binarized', binarized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
