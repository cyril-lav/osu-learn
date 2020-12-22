import sys, os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from PIL import ImageDraw
sys.path.append('..')
from utilitaire.imgAiTrainer.imgAiTrainer import Trainer
import time
import timeit
from datetime import timedelta
import statistics 

tr = Trainer()

model = keras.models.load_model('save/model/model')
model.load_weights('save/poids/model')

cercleT = tr.createCercle((800,600),True)
img = tf.keras.preprocessing.image.load_img("../../Assets/imgAiTrainer/cercle.png",target_size=(120,160))
img = keras.preprocessing.image.img_to_array(img)
imgIa = np.expand_dims(img, axis=0)
test1 = timeit.Timer("y_pred = model.predict(imgIa)", "from __main__ import model;from __main__ import imgIa")
#print(test1.timeit(1)*1000," ms")
a = test1.timeit(1)*1000

l = []
for i in range(50):
    cercleT = tr.createCercle((800,600),True)
    img = tf.keras.preprocessing.image.load_img("../../Assets/imgAiTrainer/cercle.png",target_size=(120,160))
    img = keras.preprocessing.image.img_to_array(img)
    imgIa = np.expand_dims(img, axis=0)
    test1 = timeit.Timer("y_pred = model.predict(imgIa)", "from __main__ import model;from __main__ import imgIa")
    #print(test1.timeit(1)*1000," ms")
    a = test1.timeit(1)*1000
    print(a)
    l.append(a)
    #time.sleep(1)

print(statistics.mean(l)," ms")




