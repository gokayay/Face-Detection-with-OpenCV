import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
from regionofinterest import regionOfInterest
from tkinter import *
import tkinter.messagebox



def capturef():
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    log.basicConfig(filename='webcam.log', level=log.INFO)

    video_capture = cv2.VideoCapture(0)
    anterior = 0

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if cv2.waitKey(1) & 0xFF == ord('s'):
           cv2.imwrite("image.jpg",frame)
           #root=Tk()
           tkinter.messagebox.showinfo('Photo Capturation','Photo has been captured!')

           #root.mainloop()
           break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )


        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Display the resulting frame
        cv2.imshow('Video', frame)

    # When everything is done, release the capture
    cv2.waitKey(0)
    video_capture.release()
    cv2.destroyAllWindows()


