import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot


cap = cv2.VideoCapture(0)

detector = FaceMeshDetector()

plotY = LivePlot(540,360,[10,60])

idList = [22,23,24,26,110,157,158,159,160,161,130,243]# gözdeki noktaların id leri
color = (0,255,255)


counter = 0 
blinkcounter =0
while True: 

    ratioList = []

    flag ,img = cap.read()

    img , faces = detector.findFaceMesh(img,draw=False)

    if faces :

        face = faces[0]

        for id in idList:
            cv2.circle(img,face[id],5,color,cv2.FILLED)

        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRigth = face[243] 

        lenght_ver ,_= detector.findDistance(leftUp,leftDown)
        lenght_hor ,_= detector.findDistance(leftLeft,leftRigth)

        cv2.line(img,leftUp,leftDown,(0,0,255),3)
        cv2.line(img,leftRigth,leftLeft,(0,0,255),3)

        ratio = int((lenght_ver/lenght_hor)*100)
        ratioList.append(ratio)

        if len(ratioList) >3 :
            ratioList.pop(0)

        ratio_avg = sum(ratioList)/len(ratioList)

        print(ratio_avg) # eişk değeri belirlemek için

        if ratio_avg < 35 and counter == 0:
            blinkcounter  += 1
            color = (0,255,0)
            counter = 1
        if counter != 0 :
            counter+=1
            if counter > 10 :
                counter = 0
                color = (255,0,0)

        cvzone.putTextRect(img,f'Blink Count :{blinkcounter} ' , (50,100),colorR=color)

        imgPlot = plotY.update(ratio_avg,color)
        img = cv2.resize(img,(640,360))
        img_stack = cvzone.stackImages([img,imgPlot],2,1)
    if flag : 

        cv2.imshow("img",img_stack)

        if cv2.waitKey(1) == 27:
            break
    else:
        break