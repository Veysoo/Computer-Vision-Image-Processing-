import cv2
import numpy as np 
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 1)

mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)

pTime = 0
cTime = 0
while True : 

    flag , img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = faceMesh.process(imgRGB)

    landmarks = results.multi_face_landmarks


    if landmarks:
        for faceLms in landmarks:
            mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACEMESH_TESSELATION , drawSpec) #FACEMESH_TESSELATION yerine FACE_CONTOURS de kullanılabilir nokta oluşturur
        
            for id , lm in enumerate(faceLms.landmark):
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                

    cTime = time.time()
    fps = int(1/(cTime-pTime))
    pTime = cTime

    cv2.putText(img,"FPS : "+ str(fps),(10,65),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)

    cv2.imshow("img",img)

    if cv2.waitKey(1)==27:
        break

