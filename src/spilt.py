import cv2
import numpy as np

image = cv2.imread('hill.png')
image1 = cv2.imread('death.png')
image2 = cv2.imread('thing.png')

if image is None or image1 is None or image2 is None:
    print("Error: One or more images could not be loaded. Check the file paths.")
    exit()

original = image.copy()
original3 = image1.copy()
original2 = image2.copy()

target_size = (image.shape[1], image.shape[0])  
image1 = cv2.resize(image1, target_size)
image2 = cv2.resize(image2, target_size)

img_blur = cv2.GaussianBlur(image2, (5, 5), 10)


b, g, r = cv2.split(image)
b1, g1, r1 = cv2.split(img_blur)
b2, g2, r2 = cv2.split(image1)

rV = cv2.bitwise_xor(r, g1)
bV = cv2.bitwise_xor(b2, g1)
gV = cv2.bitwise_xor(g, b2)


result_img = cv2.merge((bV, gV, rV))

cv2.imshow('Custom Manipulation', result_img)
cv2.imwrite("thing.png", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
