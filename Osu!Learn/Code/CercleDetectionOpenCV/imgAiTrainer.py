# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import random

class Trainer:
    
    # fonction qui génère une image pour entréner l'IA de reconnaissance de cercles en prenant la taille de l'image et si on génére 1 deuxième cercle autour
    def createImg(self,size,circle, nb):
        
        # Définit la fonction d'écart entre les deux cercles à None
        rayon2 = None
        # créer une image noir de la taille pasé en paramêtre
        img = Image.new('RGB', size)
        # permet de dessiner sur l'image
        draw = ImageDraw.Draw(img)
        # genère un diamêtre aléatoire
        d = random.randint(70, 150)
        for i in range(nb):
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
        
        # sauvegarde l'image dans les Assets
        img.save("img.png", "PNG")
        # retournr la position x,y du centre des cercles , le rayon du cercle 1 et 2 =
        return posx+d/2,posy+d/2,d/2,rayon2