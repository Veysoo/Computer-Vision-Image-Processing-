import cv2 
import numpy as np


# parametreler thresold , minline , canny  gibi parametlerele oynayarak daha iyi sonuçlar elde edilebilir


def region_of_interest(img,vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255

    #maskeleme
    cv2.fillPoly(mask,vertices,match_mask_color,)
    masked_img = cv2.bitwise_and(img,mask)

    return masked_img

def draw_lines (img,lines) :

    img = np.copy(img)
    blank_img = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:

            cv2.line(blank_img,(x1,y1),(x2,y2),(0,0,255),thickness=10)

    img = cv2.addWeighted(img,0.8,blank_img,1,0.0)

    return img

def process(img):
    height,width = img.shape[0],img.shape[1]
    region_of_interest_vertices = [(0,height),(width/2,height/2),(width,height)] # maskeleme işlemi için kenar noktalarını belirlemek için
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    canny_img = cv2.Canny(gray_img,250,120)
    
    cropped_img = region_of_interest(canny_img,np.array([region_of_interest_vertices],np.int32))

    lines = cv2.HoughLinesP(cropped_img,rho=2,theta=np.pi/180,threshold=220,lines=np.array([]),minLineLength=150,maxLineGap=5)
    print(lines)

    img_with_lines = draw_lines(img,lines)
    return img_with_lines


cap = cv2.VideoCapture(video path)


while True : 
    flag ,img = cap.read()


    img = process(img)

    if flag:

        cv2.imshow("img",img)
        if cv2.waitKey(10)==27:
            break
    

    else : 
        break

cap.release()
cv2.destroyAllWindows()
