# -*- coding: utf-8 -*-

import os
import shutil as sh
import filecmp as fc


class Config:
    
    __osuDir = ""
    __fullFile = ""

    #fonction de configuration du jeu osu!
    def config(self):
        # variable correspondant au dossier appdata/local de windows
        localDir = os.getenv('LOCALAPPDATA')
        
        # test si le dossier appdata/local existe
        if(localDir != None):
            # test si le dossier Osu! n'existe pasfsf
            if not (os.path.exists(localDir+"/osu!")):
                # demander la saisie du chemin
               localDir = self.__saisirDir()
        else :
            # demander la saisie du chemin
           localDir = self.__saisirDir()
            
        # variable correspondant dossier Osu!
        self.__osuDir =localDir+"/osu!"
        
        # configurer le skin
        self.__configSkin(self.__osuDir)
        # configurer le parametres du jeu
        self.__configOption(self.__osuDir)
        print("configuration initialized")
    
    def reload(self):
        if os.path.isfile(self.__fullFile+".old"):
            # supprime le fichier .old
            if os.path.isfile(self.__fullFile):
                os.remove(self.__fullFile)
            os.rename(self.__fullFile+".old",self.__fullFile)
            print("configuration reloaded")
        
    # fonction qui configure le skin 
    def __configSkin(self,osuDir):
        # nom du skin
        skinName="OsuLearn_v1"
        
        # si le dossier du skin n'existe pas
        if not(os.path.exists(osuDir+"/Skins/"+skinName)):
            # copier le skin dans le fichier
            self.__copySkin("../../Assets/config/"+skinName,osuDir+"/Skins/"+skinName)
        else :
            # si le skin est le meme est different de celui a copier
            cmpDir = fc.dircmp("../../Assets/config/"+skinName,osuDir+"/Skins/"+skinName, ignore=None, hide=None)
            if(cmpDir.same_files != cmpDir.left_list or cmpDir.same_files != cmpDir.right_list):
                # supprime dossier du skin
                sh.rmtree(osuDir+"/Skins/"+skinName)
                # copier le skin dans le fichier
                self.__copySkin("../../Assets/config/"+skinName,osuDir+"/Skins/"+skinName)
      
    # fonction qui configure les options du jeu
    def __configOption(self,osuDir):
        
        # nom du fichier de config
        configName="config.cfg"
    
        # chaque fichier dans le répertoire osu!
        for file in os.listdir(osuDir):
            # si le fichier a le format <string>.<string>.cfg
            splitFile = file.split('.')
            if splitFile[len(splitFile)-1] == "cfg" and len(splitFile)==3:
                # creation du chemin du fichier
                fullFile = os.path.join(osuDir,file)
                # si il existe déja une version de ce fichier avec l'extention .old
                if os.path.isfile(fullFile+".old"):
                    # supprime le fichier .old
                    os.remove(fullFile+".old")
                # on renomme le fichier .cfg en <nom du fichier>.old
                os.rename(fullFile, fullFile+".old")
                # on copie dans le dossier osu le fichier de configuration a charger
                sh.copy("../../Assets/config/"+configName, osuDir)
                # on le renomme avec le nom du fichier à remplacer
                os.rename(os.path.join(osuDir,configName), fullFile)
                self.__fullFile = fullFile
    
        
    #fonction de saisie du chemin du dossier osu!
    def __saisirDir(self):
        # saisir le chemin du dosier osu!
        localDir = input("Saisir le chemin du dossier dans lequel se trouve le jeu OSU! : ")
        # tant que le chemin n'est pas valide
        while not(os.path.exists(localDir+"/osu!")):
            print("\nErreur chemins invalide")
            # saisir le chemin du dossier osu!
            localDir = input("Saisir le chemin du dossier dans lequel se trouve le jeu OSU! : ")
        # retourne le chemin
        return localDir
    
    #fonction de copie de dossier vers une destination
    def __copySkin(self,dirA,dirB):
        # création du dossier destination
        os.mkdir(dirB)
        # pour chaque fichier du dossier
        for file in os.listdir(dirA):
            # creation du chemin du fichier a copier
            fullFile = os.path.join(dirA, file)
            # si le fichier existe
            if (os.path.isfile(fullFile)):
                # le copier dans la destination
                sh.copy(fullFile, dirB)