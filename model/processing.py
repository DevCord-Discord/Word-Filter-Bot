import numpy as np 
#import pandas as pd 
import random
import string
#import os

def augment(w_list, aug_dict, min_letter_change = 6, max_letter_change = 10):

        #Randomly add letters
        #<to do>
        
        #Randomly change letters
        #<to do>

        #Convert words to leet
        n_words = []
        
        for w in w_list:
            k = random.randint(min_letter_change, max_letter_change)
            
            l = random.sample(list(leet_dict.keys()), k = int(k))
            #print(l)
            lr = [random.choice(aug_dict[x]) for x in l]
            #print(lr)
            
            s = w
            for x in zip(l, lr):
                s = s.replace(x[0].lower(), x[1])
            
            n_words.append(s)
        
        return n_words

def wordsToLists(w_list, main_dict):
    
    I_n = np.identity(len(main_dict))
    
    word_o_h_l = []
    
    for w in w_list:
        
        word_l = list(w)
        word_o_h = []
        
        for letter in word_l:
            letter_o_h = I_n[main_dict.index(letter)]
            word_o_h.append(letter_o_h )
        
        word_o_h_l.append(word_o_h)
        
    return word_o_h_l

