# ////////////////////////////////////////////////////////////////////Display an image:
# import cv2

# img = cv2.imread('image.jpg')

# cv2.imshow('image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ////////////////////////////////////////////////////////////////////Convert an image to grayscale:
# import cv2

# img = cv2.imread('image.jpg')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('gray image', gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ////////////////////////////////////////////////////////////////////Capture video from webcam:
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# ////////////////////////////////////////////////////////////////////Detect faces in an image using Haar cascades:
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Faces.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 0), 5)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
