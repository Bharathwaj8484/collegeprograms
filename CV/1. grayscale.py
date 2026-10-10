import cv2 
i1 = cv2.imread("sse.jpeg") 
cv2.imshow('Original', i1) 
sse= cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Grayscale', sse) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
