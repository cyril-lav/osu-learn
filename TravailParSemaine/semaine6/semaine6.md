### IA supervisé de reconnaissance de cercles (MITERAN Justin) :  
#### Créer une IA capable de détécter un cercle et de donner son centre et ses deux rayons.
<p align="center"><img src="imagegénéré par l'IA" width="200px"></p>

  -[script](../../Osu!Learn/Code/IACercleDetection/TrainCercledetection.py) contenant la classe TrainCercleDetection  
  -[script](../../Osu!Learn/Code/IACercleDetection/testTrainCercledetection.py) contenant l'entrainement de l'IA  
  -[script](../../Osu!Learn/Code/IACercleDetection/testCercledetection.py) test de la détection de cercle sur l'IA entrainée 

#### Classes TrainCercleDetection :  
Constructeur :  
      &nbsp;&nbsp;&nbsp;- TrainCercleDetection()  
Fonctions :  
      &nbsp;&nbsp;&nbsp;.train(nbImages,batch_size,epochs) *# entaine l'IA avec une boucle infini tant que le programme n'est pas tué*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nbImages : int *# nombres d'image a générer pour le dataset*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- batch_size: int *# taille des paquets pour chaque itérations de l'IA*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- epochs: int *# nombre d'itération de l'IA par dataset*
      &nbsp;&nbsp;&nbsp;.evaluate(nbImages) *# donne une évaluation de l'IA sur sa précision*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nbImages : int *# nombres d'image a générer pour le test de précision*  
