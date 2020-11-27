# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:00:24 2020

@author: sebastien WAGNER
"""
#importation des librairies 
import win32gui
import time
from pynput.mouse import Controller 


#fonction qui retourne un tuple contenant les positions de la fenêtre du jeu
def position():
    #récupère "l'identifiant" de la fenêtre nommée osu!
    window_handle = win32gui.FindWindow(None, "osu!")
    #si l'indentifiant est différent de 0 (si 0 il n'existe pas) et que la classe de la fenêtre est une application (car peut être une autre fenêtre nommée osu!)
    if window_handle!=0 and win32gui.GetClassName(window_handle)[0:28] == "WindowsForms10.Window.2b.app":
        #retourne la position de la fenêtre et 0 comme code de retour
        return win32gui.GetWindowRect(window_handle),0
    #sinon retourne les coordonnée innexactes et -1 en code d'erreur
    return win32gui.GetWindowRect(window_handle),-1


#je déclare mouse comme variable d'accès de mon curseur
mouse = Controller()
#posF la position de ma fenêtre et x mon code de retoure
posF,x = position()
#je place ma souris au centre de la fenêtre
mouse.position = (((posF[2]-posF[0])/2),((posF[3]-posF[1])/2))
#j'attend 3 seconde pour éviter les erreurs
time.sleep(3)


#tant que la fenêtre est affichée
while(x != -1):
    #je récupère la position et le code de retour
    posF,x = position()
    #je récupère la postion de ma souris
    posC = mouse.position
    #si ma souris dépace du côté gauche je la déplace vers la droite
    if posC[0] < posF[0]+2:
        mouse.move(1,0)
    #si ma souris dépace du côté droit je la déplace vers la gauche
    if posC[0] > posF[2]-2:
        mouse.move(-1,0)
    #si ma souris dépace vers le haut je la déplace vers le bas
    if posC[1] > posF[1]+25:
        mouse.move(0,-1)
    #si ma souris dépace vers le bas je la déplace vers le haut
    if posC[1] < posF[3]-3:
        mouse.move(0,1)

print("fin")



