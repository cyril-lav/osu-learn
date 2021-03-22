
from tensorflow import keras
import tensorflow as tf
from keras_retinanet import models
import keras_retinanet
from keras_retinanet.preprocessing.trainClasse import OsuGenerator
import numpy as np
from PIL import Image
import  sys
import os

my_devices = tf.config.experimental.list_physical_devices(device_type='CPU')
config = tf.config.experimental.set_visible_devices(devices= my_devices, device_type='CPU')

sess = tf.compat.v1.Session(config=config)

#config = tf.compat.v1.ConfigProto(gpu_options = 
#                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
#)
#config.gpu_options.allow_growth = True
#session = tf.compat.v1.Session(config=config)

sys.path.append('..')

from utilitaire.imgAiTrainer.imgAiTrainer import Trainer
tr = Trainer()

def generateDataSet(nb,x,y) :
    lImg = []
    lLabel = []
    lBox = []
    for j in range(nb):
        cercleT = tr.createMultiCercle((x,y),3)
        img = tf.keras.preprocessing.image.load_img("../../Assets/imgAiTrainer/cercle.png",target_size=(120,160))
        img = keras.preprocessing.image.img_to_array(img)
        lImg.append(img)
        lLabelTmp = []
        lBoxTmp = []
        box2 = np.empty((len(cercleT[0]),4))
        for i in range(len(cercleT[0])):
            box = np.zeros((4,))
            box[0] = (cercleT[0][i-1]-cercleT[3][i-1])/5
            box[1] = (cercleT[1][i-1]-cercleT[3][i-1])/5
            box[2] = (cercleT[0][i-1]+cercleT[3][i-1])/5
            box[3] = (cercleT[1][i-1]+cercleT[3][i-1])/5
            box2[i, :] = box
            #lBoxTmp.append((cercleT[0][i-1]-cercleT[3][i-1],cercleT[1][i-1]-cercleT[3][i-1],cercleT[0][i-1]+cercleT[3][i-1],cercleT[1][i-1]+cercleT[3][i-1]))
            lLabelTmp.append(0)
        lLabel.append(np.array(lLabelTmp))
        lBox.append(box2)
    lImg = np.array(lImg)
    lLabel = np.array(lLabel)
    return lImg, lBox, lLabel

model = models.backbone('resnet50').retinanet(num_classes=3)

model.compile(
    loss={
        'regression'    : keras_retinanet.losses.smooth_l1(),
        'classification': keras_retinanet.losses.focal()
    },
    optimizer=keras.optimizers.Adam(lr=1e-5, clipnorm=0.001)
)

if len(os.listdir('save/poids')) != 0:
    model.load_weights('save/poids/model')

img, box, labels = generateDataSet(1000,600,800)

trainGenerator = OsuGenerator(img, box, labels, batch_size=1)
model.fit_generator(
        generator = trainGenerator,
        steps_per_epoch=50,
        epochs=20,
        verbose=1
    )

model.save_weights('save/poids/model')
