import cv2
import numpy as np
image = cv2.imread("sse.jpeg")
kernel = np.ones((5, 5), np.uint8)  
opt = cv2.dilate(image, kernel)  
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', opt)
cv2.waitKey(0)
cv2.destroyAllWindows()
