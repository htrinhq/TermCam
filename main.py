#!/usr/bin/env python3
##
## Hugo TRINH QUY, 2018
## main.py
## File description:
## TermCam
##

import cv2 as cv
import curses

if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        if cap.isOpened() == False:
            cap.open()
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display
        cv.imshow('frame', gray)
        # Quit command
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    # Release video capture
    cap.release()
    cv.destroyAllWindows()