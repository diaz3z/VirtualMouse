import cv2

import numpy as np
import HandTrackingModule as htm
import time
import autopy

wCam , hCam = 640, 480
smoothening = 7
plocX,plocY = 0, 0
clocX,clocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
frameR = 100

cap.set(4,hCam)
pTime = 0

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
#print(wScr,hScr)


while (True):

    # Capture the video frame
    # by frame
    success, img = cap.read()

    img = detector.findHands(img)
    lmlist,bbox = detector.findPosition(img)


    if len(lmlist)!= 0:
        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[12][1:]


        fingers = detector.fingersUp()

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),(255, 0, 255), 2)

        if fingers[1] == 1 and fingers[2] == 0:

            x3 = np.interp(x1, (frameR,wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0,hScr))

            clocX = plocX + (x3 - plocX)/smoothening
            clocY = plocY + (y3 - plocY)/smoothening

            autopy.mouse.move(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),15, (255,0,255),cv2.FILLED)
            plocX,plocY = clocX,clocY
        if fingers[1] == 1 and fingers[2] == 1:
            lenght, img, lineInfo = detector.findDistance(8,12,img)
            #print(lenght)
            if lenght < 40:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                autopy.mouse.click()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    # Display the resulting frame
    cv2.imshow('Image', img)
    cv2.waitKey(1)

