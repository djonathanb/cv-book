import cv2

image = cv2.imread('../resources/images/leaf-b&w.png', 0)
white_pixels_count = 0
black_pixels_count = 0

for x in range(0, 499):
    for y in range(0, 499):
        if image[x, y] == 255:
            white_pixels_count += 1
        else:
            black_pixels_count += 1

print(white_pixels_count)
print(black_pixels_count)
