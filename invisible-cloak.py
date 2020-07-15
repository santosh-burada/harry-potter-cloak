# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:49:38 2020

@author: santosh sampath
"""

import cv2
import numpy as np


cap=cv2.VideoCapture(0)
back=cv2.imread("./image.jpg")

while cap.isOpened():
    
    ret,frame=cap.read()
    
    if ret:
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        
        red=np.uint8([[[255,0,0]]])
        hsv_blue=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        #print(hsv_blue)
        l_red=np.array([60
                        , 100, 50])
        u_red=np.array([120, 255,255])
        
        mask=cv2.inRange(hsv,l_red,u_red)
        
        part1=cv2.bitwise_and(back,back,mask=mask)
        mask=cv2.bitwise_not(mask)
        part2=cv2.bitwise_and(frame,frame,mask=mask)
        
        #closing = cv2.morphologyEx(part1 + part2, cv2.MORPH_CLOSE, hsv_blue)
        
        cv2.imshow("cloak", part1 + part2)
        
        if cv2.waitKey(5)==ord("q"):
            break
        
cap.release()
cv2.destroyAllWindows()