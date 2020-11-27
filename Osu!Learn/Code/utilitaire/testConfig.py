# -*- coding: utf-8 -*-
from configOsu import Config
import win32gui
import time


cf = Config()

cf.config()
results = []

while(1):
        if win32gui.FindWindow("WindowsForms10.Window.2b.app.0.358a177_r10_ad1", "osu!"):
            print("jeu Osu! lancé")
            break
        
while win32gui.FindWindow("WindowsForms10.Window.2b.app.0.358a177_r10_ad1", "osu!"):
    1
    
time.sleep(1)

print("jeu Osu! fermé")
cf.reload()