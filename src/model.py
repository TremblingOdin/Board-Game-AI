import config
import numpy as np

import matplotlib.pyplot as plt

from keras.models import Sequential, load_model, Model
from keras.layers import Input, Dense, Conv2D, Flatten, BatchNormalization, Activation, LeakyReLU, add
from keras.optimizers import SGD
from keras import regularizers

import keras.backend as K

from loss import softmax_cross_entropy_with_logits

class General_Model():
    def __init__(self, reg_const, learning_rate, input_dim, output_dim):
        self.reg_const = reg_const
        self.learning_rate = learning_rate
        self.input_dim = input_dim
        self.output_dim = output_dim

    def predict(self, x):
        return self.model.predict(x)


