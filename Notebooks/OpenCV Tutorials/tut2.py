import cv2
import random

img = cv2.imread('assets/logo.jpg',-1)


copy = img[500:700, 600:900]
img[100:300,200:500] = copy

"""
for i in range(100):
    for j in range(img.shape[1]):
        img[i,j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
"""
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()