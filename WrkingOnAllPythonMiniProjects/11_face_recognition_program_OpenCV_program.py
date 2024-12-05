import cv2
import os

# Path to face cascade and face recognizer models
face_cascade_path = 'd'
face_recognizer_path = 'face_recognizer.yml'

# Create face cascade and face recognizer objects
face_cascade = cv2.CascadeClassifier(face_cascade_path)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load face recognizer model
face_recognizer.read(face_recognizer_path)

# Create labels for recognized faces
labels = ['Person 1', 'Person 2', 'Person 3']

# Initialize video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read frame from video capture object
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # For each detected face, predict the label and draw a rectangle around it
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(roi_gray)
        if confidence < 50:
            text = labels[label]
        else:
            text = 'Unknown'
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Exit loop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture object and destroy windows
cap.release()
cv2.destroyAllWindows()
