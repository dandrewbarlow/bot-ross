'''
Andrew Barlow
main.py
'''
# Libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio
import PIL.Image

IMAGE_SIZE = [450, 337]
IMAGE_SHAPE = (IMAGE_SIZE[0], IMAGE_SIZE[1], 1)
LATENT_DIM = 100

DATA_DIR = 'img/formatted/'

def normalize(img):
    normalizer = layers.experimental.preprocessing.Normalization(axis=- 1)
    return normalizer.adapt(img)

def getImages():
    fileNames = os.listdir("img")
    images = []
    for filename in fileNames:
        img = keras.preprocessing.image.load_img(DATA_DIR + filename)
        img_array = keras.preprocessing.image.img_to_array(img)
        images.append( normalize( img_array ) )
    return images

# Generator function
def makeGenerator():
    model = keras.models.Sequential()

    model.add( layers.Dense( 256, input_dim=LATENT_DIM ) )
    model.add( layers.advanced_activations.LeakyReLU( alpha=0.2 ) )
    model.add( layers.BatchNormalization( momentum=0.8 ) )

    model.add( layers.Dense( 512 ) )
    model.add( layers.advanced_activations.LeakyReLU( alpha=0.2 ) )
    model.add( layers.BatchNormalization( momentum=0.8 ) )

    model.add( layers.Dense( 1024 ) )
    model.add( layers.advanced_activations.LeakyReLU( alpha=0.2 ) )
    model.add( layers.BatchNormalization( momentum=0.8 ) )

    model.add( layers.Dense(np.prod( IMAGE_SHAPE ), activation='tanh' ) )
    model.add( layers.Reshape( IMAGE_SHAPE ) )

    model.summary()

    noise = layers.Input( shape=LATENT_DIM )
    img = model( noise )

    return keras.models.Model( noise, img )



def train():
    pass

print (getImages())