import cv2

# Getting RGB pixel colors
image = cv2.imread('../resources/images/fruits.png')
pixel_value = image[150, 150]
print(pixel_value)

# Getting Gray scale image pixel value
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
pixel_value = gray_image[150, 150]
print(pixel_value)

# Getting pixel blue color (0) intensity of RGB image
pixel_intensity = image[150, 150, 0]
print(pixel_intensity)

# Changing pixel color value
image[150, 150] = [0, 0, 0]
print(image[150, 150])
