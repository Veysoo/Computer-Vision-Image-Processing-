import cv2
import numpy as np
import math
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection(0.2)#0-100 arası hassasiyet var 

mpDraw = mp.solutions.drawing_utils


while True:
    flag , img = cap.read()


    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = faceDetection.process(imgRGB)

    #print(results.detections)

    if results.detections:
        for id , detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box # x_min,y_min,w ,h gibi değişkenler var içerisinde
            h,w, _ = img.shape

            bbox = int(bboxC.xmin*w) ,int(bboxC.ymin*h),int(bboxC.width*w),int(bboxC.height*h)

            #print(bbox)
            cv2.rectangle(img,bbox,(0,255,255),2)

    cv2.imshow("img",img)

    if cv2.waitKey(1) == 27 :
        break