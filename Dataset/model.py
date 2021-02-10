import tensorflow as tf 
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, LSTM

class SiamRNN(Model):

    def __init__(self):
        
        super (SiamRNN, self).__init__()
        
        self.d1 = Dense(64) 
        self.l1 = LSTM(128, dropout = 0.1, recurrent_dropout = 0.1)
        self.o1 = Dense(10)

    def call(self, inputs, training = False):

        x = self.d1(inputs)
        x = self.l1(x, training = training)
        x = self.o1(x)

        return x