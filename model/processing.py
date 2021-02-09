import numpy as np 
#import pandas as pd 
import random
import string
import copy
#import os

def augment(w_list, aug_dict, min_letter_change = 6, max_letter_change = 10, change_prob = 0.3):

        s_list = copy.copy(w_list)

        #Randomly add letters
        #<to do>
        
        #Randomly change letters
        for i, w in enumerate(s_list):
            s = w
            if np.random.uniform() < change_prob:
                for x in range(len(s)):
                    if np.random.uniform() < change_prob:
                        s = s.replace(s[x], random.choice(string.printable), 1)

            s_list[i] = s

        #Convert words to leet
        n_words = []
        
        for w in s_list:
            k = random.randint(min_letter_change, max_letter_change)
            
            l = random.sample(list(aug_dict.keys()), k = int(k))
            #print(l)
            lr = [random.choice(aug_dict[x]) for x in l]
            #print(lr)
            
            s = w
            #print(s)
            for x in zip(l, lr):
                s = s.replace(x[0].lower(), x[1])
            
            n_words.append(s)
        
        return n_words

def OneHot(w_list, main_dict):
    
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

