import numpy as np
import cv2


def view_cam(cam_pos=0):
    cap = cv2.VideoCapture(cam_pos)
    font = cv2.FONT_HERSHEY_SIMPLEX

    while(True):
        ret, frame = cap.read()
        if ret:
            cv2.putText(frame,'press q to quit',(10,10), font, .5 ,(255,255,255),2,cv2.LINE_AA)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('gray',gray)
            cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def record(path):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    out = cv2.VideoWriter(path,fourcc, 20.0, (640,480))
    font = cv2.FONT_HERSHEY_SIMPLEX 
    while cap.isOpened():
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
            cv2.putText(frame,'press q to quit',(10,10), font, .5 ,(255,255,255),2,cv2.LINE_AA)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()