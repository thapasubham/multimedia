import cv2
import numpy as np

# replace the image name 

image = cv2.imread('image.png')
original = image.copy()
image = cv2.resize(image, (1280,720))


# 5. Histogram Equalization (Contrast Enhancement)
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
enhanced = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
cv2.imshow('Enhanced Contrast', enhanced)


# 2. Edge Detection (Canny)
edges = cv2.Canny(enhanced, 100, 200)
cv2.imshow('edge',edges)

# 9. Blurring
blurred = cv2.GaussianBlur(edges, (5, 5), 0)
cv2.imshow('Blurred', blurred)


cv2.waitKey(0)
cv2.destroyAllWindows()
