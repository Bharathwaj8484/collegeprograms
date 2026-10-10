import cv2
image = cv2.imread("sse.jpeg")
r = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2),45,1.0)
output = cv2.warpAffine(image, r, (image.shape[1], image.shape[0]))
cv2.imshow('Original', image)
cv2.imshow('Transformed', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
