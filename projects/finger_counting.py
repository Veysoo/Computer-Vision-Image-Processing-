import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

mpHand = mp.solutions.hands
hands = mpHand.Hands()

mpDraw = mp.solutions.drawing_utils

tipIds = [4,8,12,16,20] # parmakların tepe noktaları

while 1:
    flag , img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    lms = results.multi_hand_landmarks
    lmList = []

    if lms:
        for handLms in lms:
            mpDraw.draw_landmarks(img,handLms,mpHand.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)

                # if id == 6:
                #    cv2.circle(img,(cx,cy),9,(255,0,0),cv2.FILLED)
                # if id == 8:
                #    cv2.circle(img,(cx,cy),9,(0,0,255),cv2.FILLED)



                lmList.append([id,cx,cy])

    if len(lmList)!=0:
        fingers=[]

        #bas parmak 

        if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        #diger parmaklar

        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2] :
                fingers.append(1)
            else:
                fingers.append(0)

        totalF = fingers.count(1)
        print(totalF)
        cv2.putText(img,"sayac = "+str(totalF),(15,75),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)        

    cv2.imshow("img",img)
    if cv2.waitKey(1) == 27:
        break