# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 08:56:42 2020

@author: sebas
"""

import numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1920, 1080))

while True:
    img = ImageGrab.grab(bbox=(0,0,800,600))
    img_np = np.array(img)
    
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    
    cv2.imshow("Screen", frame)
    
    #f9 
    if cv2.waitKey(1) == 120:
        break

out.release()
cv2.destroyAllWindows