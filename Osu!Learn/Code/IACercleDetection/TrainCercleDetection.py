import sys, os
import numpy as np
import tensorflow as tf
from tensorflow import keras
import PIL
from PIL import Image
from PIL import ImageDraw
import gc
config = tf.compat.v1.ConfigProto(gpu_options = 
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
sys.path.append('..')
from utilitaire.imgAiTrainer.imgAiTrainer import Trainer

#entrainement de l'ia supervisée
class TrainCercleDetection:
    __tr = Trainer()
    __img_shape = (120,160,3)

    #génère la liste de donnée pour l'entrainement de l'IA
    def __listImg(self,nb,x,y):
        lImg = []
        lLabel = []
        for i in range(nb):
            cercleT = self.__tr.createCercle((x,y),True)
            img = Image.open("../../Assets/imgAiTrainer/cercle.png")
            img = img.resize((160, 120))
            #img = tf.keras.preprocessing.image.load_img("../../Assets/imgAiTrainer/cercle.png",target_size=(120,160))
            img = keras.preprocessing.image.img_to_array(img)
            lImg.append(img)
            lLabel.append((cercleT[0][0],cercleT[0][1],cercleT[1],cercleT[2]))
        lImg = np.array(lImg)
        lLabel = np.array(lLabel)
        return lImg, lLabel

    # modele de l'IA
    def __modele(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Convolution2D(32, 5, 5, padding='same',  activation='relu', input_shape=self.__img_shape))
        model.add(keras.layers.Convolution2D(64, 5, 5, padding='same',  activation='relu'))
        model.add(keras.layers.Convolution2D(128, 5, 5, padding='same',  activation='relu'))
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(100, activation='relu'))
        model.add(keras.layers.Dense(4, activation='linear'))

        opt = keras.optimizers.Adam(learning_rate=1e-4)
        model.compile(optimizer=opt,loss='mean_squared_error',metrics=[keras.metrics.mean_absolute_percentage_error])
        print("---------------------\nmodel générée")
        return model

    #entrainement de l'IA
    def __entrainement(self,model,nbImages,batch_size,epochs):
        if len(os.listdir('save/poids')) != 0:
            model.load_weights('save/poids/model')
        print("---------------------\npoids chargée\n---------------------")
        limg , lLabel = self.__listImg(nbImages,800,600)
        print("Images train générée\n---------------------")
        model.fit(limg, lLabel,batch_size=batch_size, epochs=epochs, verbose=1)
        model.save_weights('save/poids/model')
        del limg
        del lLabel

    # mise en place de l'entrainement de l'IA
    def train(self,nbImages,batch_size,epochs):
        model = self.__modele()
        i = 0
        while 1:
            i=i+1
            gc.collect()
            self.__entrainement(model,nbImages,batch_size,epochs)
            model.save("save/model/model")
            print("---------------------\nTrain ",i," fini\n---------------------")

    def evaluate(self,nbImages):
        model = keras.models.load_model('save/model/model')
        print("---------------------\nmodel chargé\n---------------------")
        limg , lLabel = self.__listImg(nbImages,800,600)
        print("Images train générée\n---------------------")
        scores = model.evaluate(limg, lLabel)
        print("Précision : %.5f %%" % (100-scores[1]))
