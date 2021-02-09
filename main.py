import cv2
print(cv2.__version__)
import numpy as np
kernel = np.ones((5,5), np.uint8)
img = cv2.imread('imop/lena.png')
Gaussian = cv2.GaussianBlur(img, (7,7),0)
Canny = cv2.Canny(img,100, 100)

Dilation = cv2.dilate(Canny, kernel, iterations =1)
cv2.rectangle(img,(50,100),(350,450),(55,0,0),5)
cv2.putText(img,'Lena is pretty!',(10,80),2,cv2.FONT_HERSHEY_PLAIN,(255,255,255))
cv2.imshow('Lena Blur',img)
cv2.imshow('Lena',Gaussian)
cv2.imshow('Lena Canny ',Canny)
cv2.imshow('Lena dilate',Dilation)
cv2.waitKey(0)
