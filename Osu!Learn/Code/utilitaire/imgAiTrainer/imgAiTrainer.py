# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import random
from math import sqrt,acos,pi
import os

class Trainer:
    
    # fonction qui génère une image pour entréner l'IA de reconnaissance de cercles en prenant la taille de l'image et si on génére 1 deuxième cercle autour
    def createCercle(self,size,circle):
        # appel de la création de l'image
        x,y,r1,r2,img = self.__circle(size, circle)
        # sauvegarde l'image dans les Assets
        img.save("../../../Assets/imgAiTrainer/cercle.png", "PNG")
        # retour des informations sur l'image
        return (x,y),r1,r2
    
    # fonction qui crée le cercle
    def __circle(self,size,circle) :
        # Définit la fonction d'écart entre les deux cercles à None
        rayon2 = None
        # créer une image noir de la taille pasé en paramêtre
        img = Image.new('RGB', size)
        # permet de dessiner sur l'image
        draw = ImageDraw.Draw(img)
        # genère un diamêtre aléatoire
        d = random.randint(70, 150)
        # genère une position X aléatoire dans l'écran
        posx = random.randint(0, size[0]-d)
        # genère une position Y aléatoire dans l'écran
        posy = random.randint(0, size[1]-d)
        # dessine un cercle blanc dans l'écran
        draw.ellipse([posx,posy,posx+d,posy+d], fill = 'white', outline ='black', width=5)
        
        # si on veut générer un deuxième cercle autour
        if(circle):
            # ecart entre les deux cercles généré aléatoirement
            ecartD = random.randint(0, 75)
            # ecart entre les deux cercles dessine le cercle
            draw.ellipse([posx-ecartD,posy-ecartD,posx+d+ecartD,posy+d+ecartD], fill = None, outline ='White', width=5)
            # calcule le rayon du deuxième cercle
            rayon2 = d/2+ecartD
        
        # retournr la position x,y du centre des cercles , le rayon du cercle 1 et 2 =
        return posx+d/2,posy+d/2,d/2,rayon2,img

    # fonction qui génère une image pour entréner l'IA de reconnaissance de slider en prenant la taille de l'image
    def createSlider(self,size,droit,start):
        # appel de la création de l'image
        if droit == True :
            debut,fin,cercle,r1,r2,img = self.__slider(size,start)
            # sauvegarde l'image dans les Assets
        else :
            debut,fin,cercle,r1,r2,img = self.__sliderArr(size,start)
        img.save("../../../Assets/imgAiTrainer/slider.png", "PNG")
        # retour des informations sur l'image
        return debut,fin,cercle,r1,r2
    
    # fonction qui crée un slider
    def __slider(self,size,start) :
        # créer une image noir de la taille pasé en paramêtre
        img = Image.new('RGB', size)
        # genère un diamêtre aléatoire
        d = random.randint(70, 150)
        # permet de dessiner sur l'image
        draw = ImageDraw.Draw(img)
        # génère un draw de cercle
        c1 = self.__randomCircle(size, d, draw)
        # redéfinition du draw
        draw = c1[2]
        # génère un draw de cercle
        c2 = self.__randomCircle(size, d, draw)
        # redéfinition du draw
        draw = c2[2]
        
        # vecteurs
        # création du vecteur entre les deux cercles
        v1 = [0,0,c1[0]-c2[0],c1[1]-c2[1]]
        # création du vecteur perpendiculaire au précedent
        v2 = [0,0,(-(v1[3]*1))/v1[2],1]
        # récupération de la taille du vécteur 2
        t2 = self.__norme(v2)
        # définition de la taille du vecteur 2 a la taille du rayon des cercles
        v2[2]=v2[2]/t2*(d/2-5)
        v2[3]=v2[3]/t2*(d/2-5)
        # déplacement du vecteur avec les coordonée du cercle
        v3=self.__v(v2, c1[0], c1[1],1)
        # dessiner une ligne entre le bord des deux cercles a l'ai du déplacement du vecteur
        draw.line(self.__v(v1, v3[2], v3[3],-1),fill='white', width=10)
        # déplacement du vecteur avec les coordonée du cercle
        v3=self.__v(v2, c1[0], c1[1],-1)
        # dessiner une ligne entre l'autre bord des deux cercles a l'ai du déplacement du vecteur
        draw.line(self.__v(v1, v3[2], v3[3],-1),fill='white', width=10)
        
        # calculs arcs
        # calcul de l'angle du slider
        a = self.__angle(v2,[0,0,1,0])*180/pi
        # condition pour desiner le demis cercle
        if (c1[0]<c2[0] and c1[1]<c2[1]) or (c1[0]<c2[0] and c1[1]>c2[1]) :
            #dessiner les deux demis cercles pour fermer le slider
            draw.arc([c1[0]-d/2,c1[1]-d/2,c1[0]+d/2,c1[1]+d/2],a,a+180,fill='white', width=10)
            draw.arc([c2[0]-d/2,c2[1]-d/2,c2[0]+d/2,c2[1]+d/2],a+180,a,fill='white', width=10)
        else :
            #dessiner les deux demis cercles pour fermer le slider
            draw.arc([c1[0]-d/2,c1[1]-d/2,c1[0]+d/2,c1[1]+d/2],a+180,a,fill='white', width=10)
            draw.arc([c2[0]-d/2,c2[1]-d/2,c2[0]+d/2,c2[1]+d/2],a,a+180,fill='white', width=10)
        
        if(start == True):
            #cercle clic
            draw.ellipse([c1[0]-d/2,c1[1]-d/2,c1[0]+d/2,c1[1]+d/2], fill = 'white', outline ='black', width=5) 
            # si on veut générer un deuxième cercle autour
            # ecart entre les deux cercles généré aléatoirement
            ecartD = random.randint(0, 75)
            # ecart entre les deux cercles dessine le cercle
            draw.ellipse([c1[0]-d/2-ecartD,c1[1]-d/2-ecartD,c1[0]+d/2+ecartD,c1[1]+d/2+ecartD], fill = None, outline ='White', width=5)
            # retour des information sur les cercles
            return (c1[0],c1[1]),(c2[0],c2[1]),(c1[0],c1[1]),d/2,d/2+ecartD,img
        else:
            #génére un vecteur d'une tailler aléatoire entre les deux cercles
            vC = self.__v(v1,c1[0],c1[1],random.random()*-1)
            #cercle clic aléatoire sur le slider
            draw.ellipse([vC[2]-d/2,vC[3]-d/2,vC[2]+d/2,vC[3]+d/2], fill = 'white', outline ='black', width=5) 
            # retour des information sur les cercles
            return (c1[0],c1[1]),(c2[0],c2[1]),(vC[2],vC[3]),d/2,None,img
    
    #slider arrondie
    def __sliderArr(self,size,start):
        img = Image.new('RGB', size)
        nb = len(os.listdir("../../../Assets/imgAiTrainer/sliderArr"))
        num = random.randint(1, nb)
        slider = Image.open("../../../Assets/imgAiTrainer/sliderArr/"+str(num)+'.png')
        slider = slider.rotate(random.randint(0, 359),expand = 1)
        
        img.paste(slider,(random.randint(0, size[0]-slider.size[0]),random.randint(0, size[1]-slider.size[1])))
        return None,None,None,None,None,img


    
    # fonction pour changer les coordonées et la taille d'un vecteur
    def __v(self,v,x,y,n) :
        return [v[0]+x,v[1]+y,(v[2]*n)+x,(v[3]*n)+y]
    
    # fonction qui génère un cercle a un endroit aléatoire
    def __randomCircle(self,size,d,draw) :
        # genère une position X aléatoire dans l'écran
        posx = random.randint(0, size[0]-d)
        # genère une position Y aléatoire dans l'écran
        posy = random.randint(0, size[1]-d)
        # retourne les informations du cercle
        return posx+d/2,posy+d/2,draw

    # fonction qui calcule la norme d'un vecteur
    def __norme(self,v):
        return sqrt(v[2]*v[2]+v[3]*v[3])
    
    # fonction qui calcule l'angle en radian entre 2 vecteurs
    def __angle(self,v1,v2):
        cos = (v1[2]*v2[2]+v1[3]*v2[3])/(self.__norme(v1)*self.__norme(v2))
        return acos(cos)