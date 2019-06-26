import cv2
from matplotlib import pyplot as plt

original_image = cv2.imread("../resources/images/red-chips.png")
light_image = cv2.add(original_image, 40)
dark_image = cv2.add(original_image, -40)

plt.subplot(2, 3, 1)
plt.imshow(original_image)
plt.subplot(2, 3, 4)
plt.hist(original_image.ravel(), 256, [0, 256])
plt.title("Original")

plt.subplot(2, 3, 2)
plt.imshow(light_image)
plt.subplot(2, 3, 5)
plt.hist(light_image.ravel(), 256, [0, 256])
plt.title("Light")

plt.subplot(2, 3, 3)
plt.imshow(dark_image)
plt.subplot(2, 3, 6)
plt.hist(dark_image.ravel(), 256, [0, 256])
plt.title("Dark")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
