import cv2
image = cv2.imread("sse.jpeg") 
opt = cv2.GaussianBlur(image, (5, 5), 10)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', opt)
cv2.waitKey(0)
cv2.destroyAllWindows()
