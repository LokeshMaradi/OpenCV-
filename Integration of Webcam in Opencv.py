import cv2
cap=cv2.VideoCapture(0) #id for default webcam
cap.set(3,640) #Width of window
cap.set(4,480) #Height of window
cap.set(10,500) #Brightness level
while True:
    success,img=cap.read()
    cv2.imshow('op',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
