import cv2
import numpy as np

image = cv2.imread('../resources/images/rubiks.png')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Example of how to convert rgb color to hsv
# green_rgb = np.uint8([[[0, 255, 0]]])
# green_hsv = cv2.cvtColor(green_rgb, cv2.COLOR_RGB2HSV)
# print(green_hsv)

light_tone = np.array([160, 100, 100])
dark_tone = np.array([200, 255, 255])

segmented_image = cv2.inRange(image_hsv, light_tone, dark_tone)

# removing noise
structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
processed_image = cv2.morphologyEx(
    segmented_image, cv2.MORPH_CLOSE, structuring_element
)

cv2.imshow('Original', image)
cv2.imshow('Segmented', segmented_image)
cv2.imshow('Processed', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
