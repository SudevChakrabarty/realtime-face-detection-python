# PYTHON FACE RECOGNITION PROJECT USING OPENCV
# impoting opencv libraries
import cv2

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = video_capture.read()
    if not ret or frame is None:
        print("Failed to read frame from camera")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('video_Live', frame)
    key = cv2.waitKey(10) & 0xFF
    if key == ord('a') or key == 27:  # 'a' or ESC to quit
        break

video_capture.release()
cv2.destroyAllWindows()