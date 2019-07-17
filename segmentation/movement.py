import cv2
import numpy as np

first_capture = cv2.imread('../resources/images/poker_cap1.png')
second_capture = cv2.imread('../resources/images/poker_cap2.png')

rgb_img = cv2.subtract(first_capture, second_capture)
hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)

light_tone = np.array([0, 120, 120])
dark_tone = np.array([180, 255, 255])

segmented_image = cv2.inRange(hsv_img, light_tone, dark_tone)

cv2.imshow('Segmented', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
