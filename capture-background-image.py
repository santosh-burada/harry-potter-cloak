# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:22:00 2020

@author: santosh sampath
"""

import cv2
cap=cv2.VideoCapture(0)
 
while cap.isOpened():
    ret,back=cap.read()
    
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5)==ord("q"):
            
            cv2.imwrite("image.jpg",back)
        
            break
cap.release()
cv2.destroyAllWindows()