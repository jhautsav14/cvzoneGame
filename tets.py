
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np
import pyautogui
import time


width, height = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
detector = HandDetector(detectionCon=0.8, maxHands=1)

pTime = 0

gestureThreshold = 300

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img, flipType=False)
    detector.
    cv2.line(img,(0,gestureThreshold), (width,gestureThreshold),(0,255,0),10)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx,cy = hand['center']
        # print(fingers)
        if fingers[1]==1 and fingers[2]==0:

        if cy <=gestureThreshold: # if hand is hieght of face

            # gesture 1 - left
            if fingers == [1,0,0,0,0]:
                print("left")

            if fingers == [0,0,0,0,1]:
                print("Right")





    # Fram Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    # Display
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break