import sys, os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from PIL import ImageDraw
import gc
sys.path.append('..')
from utilitaire.imgAiTrainer.imgAiTrainer import Trainer

class TrainCercleDetection:
    __tr = Trainer()
    __img_shape = (120,160,3)

    def __listImg(self,nb,x,y):
        lImg = []
        lLabel = []
        for i in range(nb):
            cercleT = self.__tr.createCercle((x,y),True)
            img = tf.keras.preprocessing.image.load_img("../../Assets/imgAiTrainer/cercle.png",target_size=(120,160))
            img = keras.preprocessing.image.img_to_array(img)
            lImg.append(img)
            lLabel.append((cercleT[0][0],cercleT[0][1],cercleT[1],cercleT[2]))
        lImg = np.array(lImg)
        lLabel = np.array(lLabel)
        return lImg, lLabel

    def __modele(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Convolution2D(32, 5, 5, padding='same',  activation='relu', input_shape=self.__img_shape))
        model.add(keras.layers.Convolution2D(64, 5, 5, padding='same',  activation='relu'))
        model.add(keras.layers.Convolution2D(128, 5, 5, padding='same',  activation='relu'))
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(100, activation='relu'))
        model.add(keras.layers.Dense(4, activation='linear'))

        opt = keras.optimizers.Adam(learning_rate=1e-4)
        model.compile(optimizer=opt,loss='mean_squared_error')
        print("---------------------\nmodel générée")
        return model

    def __entrainement(self,model,nbImages,batch_size,epochs):
        #model.load_weights('save/poids/model')
        print("---------------------\npoids chargée\n---------------------")
        limg , lLabel = self.__listImg(nbImages,800,600)
        print("Images train générée\n---------------------")
        model.fit(limg, lLabel,batch_size=batch_size, epochs=epochs, verbose=1)
        model.save_weights('save/poids/model')
        del limg
        del lLabel

    def train(self,nbImages,batch_size,epochs):
        model = self.__modele()
        i = 0
        while 1:
            i=i+1
            gc.collect()
            self.__entrainement(model,nbImages,batch_size,epochs)
            model.save("save/model/model")
            print("---------------------\nTrain ",i," fini\n---------------------")
