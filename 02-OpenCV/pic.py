import cv2

img = cv2.imread('555.png')
print(img.shape)
img = cv2.resize(img, (300, 300))
print(img.shape)
cv2.imshow('result', img)
cv2.waitKey(0)
