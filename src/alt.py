import cv2
import numpy as np

#replace the image name
image = cv2.imread('death.png')
image1 = cv2.imread('the.png')
image2 = cv2.imread("hill.png")

# Resize all images to the first image size
image1 = cv2.resize(image1, (image.shape[1], image.shape[0]))
image2 = cv2.resize(image2, (image.shape[1], image.shape[0]))

# Split channels (BGR order)
b, g, r = cv2.split(image)
b1, g1, r1 = cv2.split(image2)
b2, g2, r2 = cv2.split(image1)

# Bitwise and arithmetic fusion the bgr channels
r_mix = np.clip((r | 2) - (g | g1) + 40, 0, 255).astype(np.uint8)

b_mix = cv2.bitwise_or(r1, b2)

# Avoid zero division
b_safe = b_mix.astype(np.float32)
b_safe[b_safe == 0] = 1.0

g_mix = np.clip((r.astype(np.float32) + g.astype(np.float32)) / b_safe, 0, 255).astype(np.uint8)

r_avg = np.clip((r_mix.astype(np.float32) + r1 + r) / 3, 0, 255).astype(np.uint8)

# Merge all fused channels in BGR order
output = cv2.merge(( b1, g2,r))

cv2.imshow('epic fusion', output)
cv2.imwrite("epic122.png", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
