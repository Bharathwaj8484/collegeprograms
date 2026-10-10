import cv2
import numpy as np
cap = cv2.VideoCapture('vid.mp4')
src_points = np.float32([[100, 100], [300, 100], [100, 300], [300, 300]])
dst_points = np.float32([[50, 50], [250, 50], [50, 250], [250, 250]])
perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    transformed_frame = cv2.warpPerspective(frame, perspective_matrix, (frame.shape[1], frame.shape[0]))
    cv2.imshow('Original Video', frame)
    cv2.imshow('Transformed Video', transformed_frame)
    if cv2.waitKey(30) & 0xFF == 27: 
        break
cap.release()
cv2.destroyAllWindows()
