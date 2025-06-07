import mediapipe as mp
import cv2 as cv
import time
import pose_detection as pd

cap=cv.VideoCapture(0)
detector=pd.PoseDetectori()
count=0
count_half=0
l=10

while(True):
    success, img = cap.read()
    img = detector.findPose(img, draw=True)
    lmlist = detector.findPosition(img, draw=True)

    if(len(lmlist)!=0 and lmlist[0][1]>220 and l<220):
        print(lmlist[0])
        l=lmlist[0][1]

    elif(len(lmlist)!=0 and lmlist[0][1]<220 and l>220):
        count+=1
        print(lmlist[0])
        l=lmlist[0][1]
    
    cv.putText(img,f"count :{count}",(10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0,0), 2)
    cv.imshow("pose_partne",img)

    if cv.waitKey(20) & 0XFF==ord("q"):
        cv.destroyAllWindows
        cap.release()
        break
    