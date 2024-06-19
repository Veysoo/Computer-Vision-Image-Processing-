import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

while 1: 
    flag ,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = pose.process(imgRGB)
    #print(results.pose_landmarks)

    lms = results.pose_landmarks

    if lms :
        mpDraw.draw_landmarks(img,lms,mpPose.POSE_CONNECTIONS)

        for id , lm in enumerate(lms.landmark):
            h,w,c = img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)

            if id == 4:
                cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
    
    cTime = time.time()
    fps = int(1/(cTime-pTime))
    pTime = cTime

    cv2.putText(img,"fps:"+str(fps),(10,65),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
    cv2.imshow("img",img)
    if cv2.waitKey(1)==27:
        break