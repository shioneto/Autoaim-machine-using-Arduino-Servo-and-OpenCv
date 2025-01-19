import numpy as np
import cv2
import cv2.data
import serial

center_x = 0
arduino = serial.Serial('COM5',9600) #port and baudrate

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5,minSize=(30,30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        #drawing the rectangle of the face that is detected
        center_x= x+w//2
        #setting center x axis
        center_y = y+h//2
        # setting center y axis
        center_coords = f"{center_x},{center_y}"
        # setting center coordinates of the rectangle/box
        coordinates = f"{x},{y}\n"
        arduino.write(coordinates.encode())
        # sending the data to arduino

        print(coordinates)

        cv2.putText(frame,center_coords, (center_x,center_y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()