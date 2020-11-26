# -*- coding: utf-8 -*-

import os
import shutil as sh
import filecmp as fc

#fonction de configuration du jeu osu!
def config():
    
    # variable correspondant au dossier appdata/local de windows
    localDir = os.getenv('LOCALAPPDATA')
    
    # test si le dossier appdata/local existe
    if(localDir != None):
        # test si le dossier Osu! n'existe pasfsf
        if not (os.path.exists(localDir+"/osu!")):
            # demander la saisie du chemin
            localDir = __saisirDir()
    else :
        # demander la saisie du chemin
        localDir = __saisirDir()
        
    # variable correspondant dossier Osu!
    osuDir = localDir+"/osu!"
    
    # configurer le skin
    __configSkin(osuDir)
    # configurer le parametres du jeu
    __configOption(osuDir)
    
# fonction qui configure le skin 
def __configSkin(osuDir):
    # nom du skin
    skinName="OsuLearn_v1"
    
    # si le dossier du skin n'existe pas
    if not(os.path.exists(osuDir+"/Skins/"+skinName)):
        # copier le skin dans le fichier
        __copySkin("../../Assets/config/"+skinName,osuDir+"/Skins/"+skinName)
    else :
        # si le skin est le meme est different de celui a copier
        cmpDir = fc.dircmp("../../Assets/config/"+skinName,osuDir+"/Skins/"+skinName, ignore=None, hide=None)
        if(cmpDir.same_files != cmpDir.left_list or cmpDir.same_files != cmpDir.right_list):
            # supprime dossier du skin
            sh.rmtree(osuDir+"/Skins/"+skinName)
            # copier le skin dans le fichier
            __copySkin("../../Assets/config/"+skinName,osuDir+"/Skins/"+skinName)
    
def __configOption(osuDir):
    
    configName="config.cfg"

    for file in os.listdir(osuDir):
        splitFile = file.split('.')
        if splitFile[len(splitFile)-1] == "cfg" and len(splitFile)==3:
            fullFile = os.path.join(osuDir,file)
            if os.path.isfile(fullFile+".old"):
                os.remove(fullFile+".old")
            os.rename(fullFile, fullFile+".old")
            sh.copy("../../Assets/config/"+configName, osuDir)
            os.rename(os.path.join(osuDir,configName), fullFile)

    
#fonction de saisie du chemin du dossier osu!
def __saisirDir():
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
def __copySkin(dirA,dirB):
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
            
config()
