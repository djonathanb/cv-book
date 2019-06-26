import cv2

image = cv2.imread('../resources/images/fruits.png')

# print lines, columns and colors channels count
print(image.shape)
# print pixels count (multiplied by colors channels counts)
print(image.size)
# print pixels count for RGB image
print(image.size / 3)
