import sys, os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
config = tf.compat.v1.ConfigProto(gpu_options = 
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
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
            cercleT = self.__tr.createMultiCercle((x,y),2)
            img = tf.keras.preprocessing.image.load_img("../../Assets/imgAiTrainer/multiCercle.png",target_size=(120,160))
            img = keras.preprocessing.image.img_to_array(img)
            lImg.append(img)
            lLabel.append((cercleT[0],cercleT[1],cercleT[2],cercleT[3]))
        lImg = np.array(lImg)
        lLabel = np.array(lLabel)
        return lImg, lLabel

    def __modele(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Convolution2D(32, 5, 5, padding='same',  activation='relu', input_shape=self.__img_shape))
        model.add(keras.layers.Convolution2D(64, 5, 5, padding='same',  activation='relu'))
        model.add(keras.layers.Convolution2D(128, 5, 5, padding='same',  activation='relu'))
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(256, activation='relu'))
        model.add(keras.layers.Dense(128, activation='relu'))
        model.add(keras.layers.Dense(4, activation='linear'))

        opt = keras.optimizers.Adam(learning_rate=1e-4)
        model.compile(optimizer=opt,loss='mean_squared_error')
        print("---------------------\nmodel générée")
        return model

    def __entrainement(self,model,nbImages,batch_size,epochs,nbTours):
        if len(os.listdir('save/poids')) != 0:
            model.load_weights('save/poids/model')
        print("---------------------\npoids chargée\n---------------------")
        limg , lLabel = self.__listImg(nbImages,800,600)
        print("Images train générée\n---------------------")
        history = model.fit(limg, lLabel,batch_size=batch_size, epochs=epochs, verbose=1)
        model.save_weights('save/poids/model')
        self.__graph(history,nbTours)
        del limg
        del lLabel

    def __graph(self,history,nbTours):
        plt.plot(history.history['loss'],label='loss')
        plt.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0.)
        plt.savefig("../../Assets/Train/loss"+str(nbTours)+".png")
        plt.clf()
        """ plt.plot(history.history['mean_absolute_percentage_error'],label='mean_absolute_percentage_error')
        plt.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0.)
        plt.savefig("../../Assets/Train/meanPercentage"+str(nbTours)+".png")
        plt.clf() """
        
    def train(self,nbImages,batch_size,epochs):
        model = self.__modele()
        i = 0
        while 1:
            i=i+1
            gc.collect()
            self.__entrainement(model,nbImages,batch_size,epochs,i)
            model.save("save/model/model")
            print("---------------------\nTrain ",i," fini\n---------------------")

    def evaluate(self,nbImages):
        model = keras.models.load_model('save/model/model')
        print("---------------------\nmodel chargé\n---------------------")
        limg , lLabel = self.__listImg(nbImages,800,600)
        print("Images train générée\n---------------------")
        scores = model.evaluate(limg, lLabel)
        print("Précision : %.5f %%" % (100-scores[1]))