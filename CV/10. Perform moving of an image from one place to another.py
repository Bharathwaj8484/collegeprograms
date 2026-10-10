import cv2
src = cv2.imread("sse.jpeg")
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("og", src)
cv2.imshow("new", image)
cv2.waitKey(0)
