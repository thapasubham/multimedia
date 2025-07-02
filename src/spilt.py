import cv2
import numpy as np

# Read image
#replace the images name or it wont work
image = cv2.imread('the.png')
original = image.copy()
image1 = cv2.imread('food.png')
original3= image1.copy()
image2= cv2.imread("Death.png")
original2 = image2.copy()
img = cv2.GaussianBlur(original2, (5, 5), 5)


# Split channels (BGR order)
b, g, r = cv2.split(image)
b1,g1,r1=cv2.split(img)
b2,g2,r2=cv2.split(original3)

# Boost red channel
r = np.clip((r1|r2)-(2|g1) + 40, 0, 255).astype(np.uint8)

# Bitwise OR between red and blue
b = np.clip(r1| b2, 0, 255).astype(np.uint8)

# Avoid division by zero
b_safe = b.copy().astype(np.float32)
b_safe[b_safe == 0] = 1.0

# Compute new green channel
g_zero = np.clip((r1.astype(np.float32) + g1.astype(np.float32)) / b_safe, 0, 255).astype(np.uint8)

# merge the split BGR channel
img = cv2.merge((b2, g, r1))

cv2.imshow('Custom Manipulation', img)
cv2.imwrite("thing.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
