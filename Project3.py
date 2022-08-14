import cv2
framewidth=640
frameheight=480
nPlatecascade = cv2.CascadeClassifier("C:/Users/PRADYOT/Desktop/ML TUTORIAL/OPENCV PROJECTS/haarcascade_russian_plate_number.xml")
minArea = 500
cap=cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10,150)
while True:
    succes, img = cap.read()
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlatecascade.detectMultiScale(imggray, 1.1, 4)

    for (x,y,w,h) in numberPlates:
        area = w*h
        if area>minArea:

            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number-Plate",(x,y-5),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(255,0,0),2)
            imgRoi = img[y:y+h,x:x+w]

            cv2.imshow("car",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break