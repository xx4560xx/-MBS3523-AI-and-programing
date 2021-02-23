import cv2
print(cv2.__version__)
faceCascade = cv2.CascadeClassifier('l/haar.xml')
cap = cv2.VideoCapture('l/guitar.mp4')

while True:
        success , img = cap.read()
        ##img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(img,1.05,5)
        print(faces)


        for (x,y,w,h)in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('facecap', img)
        if cv2.waitKey(5) & 0xff == ord('q'):
                break
cap.release()
cv2.destroyAllwindows()

