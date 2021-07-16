import cv2
import face_recognition as fr
import os
import numpy as np
Images=[]
names=[]
path='C:/Users/OPTIMUS/PycharmProjects/OpencvPython/Face Recognition/Images'
dest=os.listdir(path)
for cl in dest:
    curImg=cv2.imread(f'{path}/{cl}')
    Images.append(curImg)
    names.append(os.path.splitext(cl)[0])
def encoding(images):
    encodlis=[]
    for i in images:
        fp=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
        en=fr.face_encodings(fp)[0]
        encodlis.append(en)
    return encodlis
trueList=encoding(Images)
cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    #resize curr image
    imgR=cv2.resize(img,(0,0),None,0.25,0.25)
    imgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2RGB)
    imgLoc=fr.face_locations(imgR)
    imgEnc=fr.face_encodings(imgR,imgLoc)
    for iL,iE in zip(imgLoc,imgEnc):
        result=fr.compare_faces(trueList,iE)
        loc=fr.face_distance(trueList,iE)
        index=np.argmin(loc)
        if(result[index]):
            name=names[index].upper()
            y1,x2,y2,x1=iL
            x1,y1,x2,y2=x1*4,y1*4,x2*4,y2*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(255,0,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
    cv2.imshow('Show',img)
    cv2.waitKey(1)


