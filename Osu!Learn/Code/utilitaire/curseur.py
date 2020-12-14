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

#fonction de vérification de position de la souris x,y -> Position du curseur / xF_g,yF_g -> position en haut à gauche de la fenêtre / xF_d,yF_d -> position en bas à droite de la fenêtre
def isSortie(x,y):
    #Si le curseur est sorti de la fenêtre je return False sinon je return True
    return x < 0 or x > 800 or y < 0 or y > 600

#fonction qui traduit les coordonnée relative à la fenêtre en coordonnée relative à l'écran
def viser(xF_g,yF_d,xV,yV):
        return xV+xF_g+2,yV+yF_d

#fonction de clique
def cliquer():
    if isClic:
        souris.release(Button.left)
        isClic = False
    else :
        souris.press(Button.left)
        isClic = True

"""
#tant que la fenêtre est affichée
while(x != -1):
    #je récupère la position et le code de retour
    posF,x = position()
    #je récupère la postion de ma souris
    posC = mouse.position
    #si ma souris dépace du côté gauche je la déplace vers la droite
    if posC[0] < posF[0]+2:
        mouse.position = (posF[0]+2,posC[1])
    #si ma souris dépace du côté droit je la déplace vers la gauche
    if posC[0] > posF[2]-5:
         mouse.position = (posF[2]-5,posC[1])
    #si ma souris dépace vers le haut je la déplace vers le bas
    if posC[1 ] < posF[1]+26:
         mouse.position = (posC[0],posF[1]+26)
    #si ma souris dépace vers le bas je la déplace vers le haut
    if posC[1] > posF[3]-4:
        mouse.position = (posC[0],posF[3]-4)
"""
print("fin")



