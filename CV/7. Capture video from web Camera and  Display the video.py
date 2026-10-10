import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open the camera")
    exit()
cv2.namedWindow("Webcam Video")
speed = 1.0  
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Webcam Video", frame)
    key = cv2.waitKey(1)
    if key == ord("+"):
        speed += 5.0
    elif key == ord("-"):
        speed -= 5.0
    elif key == ord('q'):
        break
    cap.set(cv2.CAP_PROP_FPS, 30 * speed)
cap.release()
cv2.destroyAllWindows()
