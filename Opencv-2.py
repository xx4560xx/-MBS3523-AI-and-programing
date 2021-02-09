
print('hello')
import cv2
print(cv2.__version__)
capture = cv2.VideoCapture('imop/dog.mp4')
import numpy as np
kernel = np.ones((5,5), np.uint8)
img = cv2.imread('imop/dog.mp4')
Gaussian = cv2.GaussianBlur(img, (7,7),0)
Canny = cv2.Canny(img,100, 100)

Dilation = cv2.dilate(Canny, kernel, iterations =1)
cv2.imshow(dog.mp4',img)
cv2.imshow('dog.mp4',Gaussian)
cv2.imshow('dog.mp4 Canny ',Canny)
cv2.imshow('dog.mp4 dilate',Dilation)
cv2.waitKey(0)

while True:
   success , img = capture.read()
   imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   cv2.imshow('Dog',img)
   cv2.imshow('Dog Gray', imgGray)
   if cv2.waitKey(20) & 0xff == ord('q'):
      break

capture.release()
cv2.destroyAllWindows()
