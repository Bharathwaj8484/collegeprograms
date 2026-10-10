import cv2
image_path = "i2.jpeg"
x,y,width,height = 100,50,200, 150
image = cv2.imread(image_path)
cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
roi = image[y:y + height, x:x + width]
cv2.imshow("Image with Rectangle", image)
cv2.imshow("Extracted Region", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()