#-*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import pickle
import time

from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.callbacks import ReduceLROnPlateau
from keras.layers import Conv1D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import GlobalAveragePooling1D
from keras.layers import LSTM
from keras.layers import Masking
from keras.layers import MaxPooling1D
from keras.models import Sequential


class SentimentAnalysis:
    def __init__(self):






