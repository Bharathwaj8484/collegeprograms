import cv2
import numpy as np
img = cv2.imread("sse.jpeg")
img = cv2.resize(img,(255, 255))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
opt = cv2.filter2D(gray_img, -1, laplacian_kernel)
opt = cv2.cvtColor(opt, cv2.COLOR_GRAY2BGR)
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', opt)
cv2.waitKey(0)
cv2.destroyAllWindows()