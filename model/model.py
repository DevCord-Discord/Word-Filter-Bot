import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, LSTM 

class SiamLSTM(Model):

    def __init__(self):
        super(SiamLSTM, self).__init__()
        self.d1 = Dense(64)
        self.l1 = LSTM(128, dropout = 0.1, recurrent_dropout = 0.1)
        self.o  = Dense(12)

    def call(inputs, training):
        x = self.d1(inputs)
        x = self.l1(x)
        x = self.o(x)

        return x 

def loss(f_a, f_b):
    m_dist = tf.reduce_sum(tf.math.abs(f_a - f_b), axis = -1)
    
    #return loss
    return tf.reduce_mean(tf.exp(m_dist))