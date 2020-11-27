# -*- coding: utf-8 -*-
from pynput.mouse import Button, Controller 
import random
import time
"""
Created on Fri Nov 20 13:09:30 2020

@author: sebas
"""
mouse = Controller()
pos = mouse.position
print(pos[0])
print(pos[1])
"""
x = random.randint(0,1500)
y = random.randint(0,1500)
mouse.position = (x, y)
"""