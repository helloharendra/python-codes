import cv2

webcam = cv2.VideoCapture(0)

while True:
    State, img = webcam.read()
    print(State)
    print(img)
    if State:
        cv2.imshow("mycam",img)
        if cv2.waitKey(1) == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()
