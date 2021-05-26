import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread('Resources\iron-man-wallpaper-13.jpg')
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting into grayscale
imgb=cv2.GaussianBlur(imgg,(7,7),0)   #Adding slight blur to decrease level of noise in the image
imgedge=cv2.Canny(img,100,100)        #Edge detection
cv2.imshow('op4',imgedge)
cv2.waitKey(0)

