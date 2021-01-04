# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 08:56:42 2020

@author: sebastien
"""

from tensorflow import keras
from PIL import ImageGrab
import matplotlib.image as mpimg
import numpy as np
import win32gui


def position():
    window_handle = win32gui.FindWindow(None, "osu!")
    if window_handle!=0 and win32gui.GetClassName(window_handle)[0:28] == "WindowsForms10.Window.2b.app":
        return win32gui.GetWindowRect(window_handle),0
    return win32gui.GetWindowRect(window_handle),-1

def Foncimg(x,y,x1,y1):
    img = ImageGrab.grab(bbox=(x,y,x1,y1))
    img = img.resize((160, 120))
    img = keras.preprocessing.image.img_to_array(img)
    imgIa = np.expand_dims(img, axis=0)
    return imgIa

pos,i = position()
img1 = Foncimg(pos[0],pos[1],pos[2],pos[3])
