import cv2
image = cv2.imread("sse.jpeg")  
cv2.imshow('Original Image', image)
clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Clockwise', clockwise)
counter= cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Rotated Counterclockwise', counter)
cv2.waitKey(0)
cv2.destroyAllWindows()
