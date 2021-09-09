# -*- coding: utf-8 -*-
"""image recognition using keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16jsCKUbGt-5_c9BnPu-tf2xSkvV4GF0l
"""

# Import Libraries
import keras
from keras import backend as K
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.preprocessing import image
from keras.applications import imagenet_utils
from keras.applications import mobilenet
import numpy as np
from IPython.display import Image

#Select the model for image recognition
mobile=keras.applications.mobilenet.MobileNet()

def prepare_image(file):
  img_path=''
  img=image.load_img(img_path+file,target_size=(224,224))
  img_array=image.img_to_array(img)
  img_array_expended_dims=np.expand_dims(img_array,axis=0)
  return keras.applications.mobilenet.preprocess_input(img_array_expended_dims)

Image(filename='german.jpg')