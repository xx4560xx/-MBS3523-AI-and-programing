
print('hello')
import cv2
print(cv2.__version__)
capture = cv2.VideoCapture('imop/dog.mp4')

while True:
   success , img = capture.read()
   imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   cv2.imshow('Dog',img)
   cv2.imshow('Dog Gray', imgGray)
   if cv2.waitKey(20) & 0xff == ord('q'):
      break

capture.release()
cv2.destroyAllWindows()
