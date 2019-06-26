import cv2

original_image = cv2.imread('../resources/images/leaf.png')

resized_image = cv2.resize(original_image, None, fx=0.5, fy=0.5,
                           interpolation=cv2.INTER_CUBIC)

cv2.imshow('Resized', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
