# -*- coding: utf-8 -*-
from configOsu import Config
import win32gui
import time


cf = Config()

cf.config()
results = []

while(1):
        window_handle = win32gui.FindWindow(None, "osu!")
		if window_handle!=0 and win32gui.GetClassName(window_handle)[0:28] == "WindowsForms10.Window.2b.app":
            print("jeu Osu! lancé")
            break
        
	window_handle = win32gui.FindWindow(None, "osu!")
	if window_handle!=0 and win32gui.GetClassName(window_handle)[0:28] == "WindowsForms10.Window.2b.app":
    1
    
time.sleep(1)

print("jeu Osu! fermé")
cf.reload()