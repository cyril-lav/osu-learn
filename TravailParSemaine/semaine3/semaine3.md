# Semaine 3  


### SCRIPT CONFIGURATION OSU! (MITERAN Justin) :  
#### Créer un script capable de configurer automatiquement le jeu osu avec le [SKIN et le fichier de configuration](../../Osu!Learn/Assets/config).  
  -[script](../../Osu!Learn/Code/utilitaire/config/configOsu.py) contenant la classe Config  
  -[script](../../Osu!Learn/Code/utilitaire/config/testConfig.py) de test de configuration du jeu Osu!  

#### Classes Config :  
Constructeur :  
      &nbsp;&nbsp;&nbsp;- Config()  
Fonctions :  
      &nbsp;&nbsp;&nbsp;.config() *# permet de configurer le jeu*  
      &nbsp;&nbsp;&nbsp;.reload() *# permet de reinitialiser les parametres du jeu de l'utilisateur*  
      
### SCRIPT ENTRAINEMENT AI RECONNAISSANCE IMAGES (MITERAN Justin) :  
#### Créer un script capable de générer une image contenant un cercle pour entrainer l'IA de reconnaissance de cercle.
<p align="center"><img src="../../Osu!Learn/Assets/imgAiTrainer/img.png" width="200px"></p>

  -[script](../../Osu!Learn/Code/utilitaire/imgAiTrainer/imgAiTrainer.py) contenant la classe Trainer  
  -[script](../../Osu!Learn/Code/utilitaire/imgAiTrainer/testImgAiTrainer.py) de test la génération d'image dans Assets  

#### Classes Trainer :  
Constructeur :  
      &nbsp;&nbsp;&nbsp;- Trainer()  
Fonctions :  
      &nbsp;&nbsp;&nbsp;.createImg(taille,cercle) *# génère une image noir avec un cercle blanc pour entrainer l'IA*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- taille : tuple *# (x,y) taille x et y de l'image en pixels*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- cercle : boolean *# False pour générer un cercle et True pour générer un deuxième cercle autour*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return x,y,rayon1,rayon2  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- x : int *# Coordonée x du centre du cercle*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- y : int *# Coordonée y du centre du cercle*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rayon1 : rayon1 *# Rayon du cercle*  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rayon2 : rayon2 *# None si ```cercle=False``` ou le rayon du cercle généré autour du premier*  
      
### MAP TEST ET SCRIPT DU CURSEUR (WAGNER Sébastien) :  
#### Créer des maps tests pour l'IA :  
  -Silent pather - Osu!Learn--circle.osz) -> map avec un seul cercle  
  -Silent Panther - Osu!learn--spinner.osz -> map avec un seul spinner  
  -Silent Panther - Osu!learn--slider.osz -> map avec un seul slider  
  -Silent Panther - Osu!Learn--Full_cercles.osz -> map avec plusieurs cercles  
  ---- - Osu!Learn.osz -> map test avec de tout  

#### Créer un script pour que le curseur reste dans la fenêtre du jeu :  
  -[curseur.py](../../Osu!Learn/Code/utilitaire/curseur.py) qui permet que le curseur reste dans la fenêtre du jeu
  
