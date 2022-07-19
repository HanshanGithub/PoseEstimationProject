import cv2
import time

import PoseMoudule as pm

# cap = cv2.VdieoCapture(0)
cap = cv2.VideoCapture("video/1.mp4")
pTime = 0
detecor = pm.PostDetector()

while True:
    _, img = cap.read()
    img = detecor.findPose(img) # ,False
    lmList = detecor.findPosition(img)
    if len(lmList) != 0:
        print(lmList[0])
        cv2.circle(img, (lmList[0][1], lmList[0][2]), 5, (0, 255, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("video", img)
    cv2.waitKey(10)