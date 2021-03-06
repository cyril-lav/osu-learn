import sys, os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from PIL import ImageDraw
import gc
sys.path.append('..')
from utilitaire.imgAiTrainer.imgAiTrainer import Trainer

tr = Trainer()
img_shape = (600,800,3)

def listImg(nb,x,y):
    lImg = []
    lLabel = []
    for i in range(nb):
        cercleT = tr.createCercle((x,y),True)
        img = Image.open("../../Assets/imgAiTrainer/cercle.png")
        imgGray = tf.keras.preprocessing.image.img_to_array(img, data_format=None, dtype=None)
        lImg.append(imgGray)
        lLabel.append((cercleT[0][0],cercleT[0][1],cercleT[1],cercleT[2]))
    lImg = np.array(lImg)
    lLabel = np.array(lLabel)
    return lImg, lLabel

def modele():
    model = keras.models.Sequential()
    model.add(keras.layers.Convolution2D(32, 5, 5, padding='same',  activation='relu', input_shape=img_shape))
    model.add(keras.layers.Convolution2D(64, 5, 5, padding='same',  activation='relu'))
    model.add(keras.layers.Convolution2D(128, 5, 5, padding='same',  activation='relu'))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(4, activation='linear'))

    opt = keras.optimizers.Adam(learning_rate=1e-4)
    model.compile(optimizer=opt,loss='mean_squared_error')
    print("---------------------\nmodel générée")
    return model

def entrainement(model,batch_size,epochs):
    model.load_weights('save/model')
    print("---------------------\npoids chargée\n---------------------")
    limg , lLabel = listImg(1000,800,600)
    print("Images train générée\n---------------------")
    model.fit(limg, lLabel,batch_size=batch_size, epochs=epochs, verbose=1)
    model.save_weights('save/model')
    del limg
    del lLabel

model = modele()
i = 0
while 1:
    i=i+1
    gc.collect()
    entrainement(model,100,100)
    print("---------------------\nTrain ",i," fini\n---------------------")
