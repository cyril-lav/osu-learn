# Semaine 2  


### OUTPUT DU RESEAU DE NEURONES (WAGNER Sébastien) :  
##### Gérer la position de la souris via le code : Grâce à la librairie pynput.mouse (à installer) on peut modifier la position de la souris (en instantané).  
  -mouse = controller() -> La variable mouse devient la variable d’accès  à la souris  
  -print(mouse.position) -> rend la position de la souris (x , y)  
  -mouse.position =  (x, y) -> Déplace la souris à la position x, y (x=0, y=0) en haut à gauche de l’écran  
  -mouse.move(x, y) -> Déplace la souris par rapport à sa position x et y en nombre de pixels  

##### Gérer les clicks de la souris :  
  -mouse.click(Button.right, nb) -> click droit / nb = nombre de click(s)  
  -mouse.click(Button.left, 1) -> click gauche  
  -mouse.press(Button.right) -> click droit enfoncé  
  -mouse.press(Button.left) -> click gauche enfoncé  
  -mouse.release(Button.right) -> relache click droit  
  -mouse.release(Button.left) -> relache click gauche  
  -mouse.scroll(0, x) -> scroll si x > 0 vers le haut si x < 0 vers le bas  


### Partie Tensorflow et autres outils (Cyril Laveyssiere)  

Le réseau de neuronnes :  
Utilisation d’un réseau de neurones convolutif. Outil : Tensorflow -> keras  
Initialisation :  Pas l’initialisation de Xavier (sert à la classification)  
Lien utile :  
Initialisation de Glorot & Bengio :
https://www.racinely.com/post/l-initialisation-de-glorot-bengio  
Fonction d’activation :
https://www.tensorflow.org/api_docs/python/tf/keras/layers/Activation   
Les couches de neurones :  
Input layer : https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer  
Couche : https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer  
Couche de convolution : https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D  
	Installer Tensorflow : 
	https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/  

### Partie détection des cercles (Cyril Laveyssiere)  
  
#####Comment détecter les cercles ?  
Deux outils :  
	le filtre de Sobel : 
Utilisé pour la detection de bords sur des images complexes en calculant le gradient de l’intensité de chaque pixel. Outils : openCV, tensorflow, scipy.  
Lien utile : 
https://www.codingame.com/playgrounds/38470/how-to-detect-circles-in-images  
	la transformée de Hough :
Utilisé pour détecter des lignes et de formes (donc de cercles et sliders) même s’il manque des points sur les formes ou l’image est dégradée. Outils : openCV, numpy, scipy.  
Liens utiles :
https://github.com/PavanGJ/Circle-Hough-Transformé  
https://subscription.packtpub.com/book/application_development/9781788474443/4/ch04lvl1sec58/detecting-lines-and-circles-using-the-hough-transform  
  
### Persistence du modele (Justin Miteran)  

requière numpy, tensorflow, keras  

##### Enregistrement de model Keras (API KERAS) :  
	- Format TensorFlow SavedModel  
	  model.save('path/to/location')  
	  model = keras.models.load_model('path/to/location')  
	- L'ancien format Keras H5  
	  save_format='h5'  

##### Enregistrement seulement des poids :  
	- get_weights() et set_weights()  
	- model.save_weights  
Lien utile :  
https://www.tensorflow.org/guide/keras/save_and_serialize  

###Visualisation du modele (Justin Miteran)  

Possiblité avec Graphviz (librairie de création de graphes code pour la récuperation du model a faire nous même)  
	-génére des images sous forme de graphes  
https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/ 
  
###récuperation des infos sur la fenetre d'OSU! (Justin Miteran & Wagner Sébastien)  
  
Possibilité avec win32gui  
	- FindWindow(None, "osu!")  
	- GetWindowRect()  
[voir](test/testFenetreOsu.py) code de test testFenetreOsu.py  
