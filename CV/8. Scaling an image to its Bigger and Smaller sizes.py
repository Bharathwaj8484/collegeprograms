import cv2
img= cv2.imread("sse.jpeg") 
cv2.imshow("original image",img)
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
