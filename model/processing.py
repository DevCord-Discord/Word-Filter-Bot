import numpy as np 
import tensorflow as tf
import random
import string
import copy

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
            lr = [random.choice(aug_dict[x]) for x in l]
            
            s = w
            for x in zip(l, lr):
                s = s.replace(x[0].lower(), x[1])
            
            n_words.append(s)
        
        return n_words

def sample(w_list, aug_dict, sample_size, change_prob = 0.3):
    sp = random.sample(w_list, k = sample_size)
    sp_a = augment(sp,  aug_dict = aug_dict, min_letter_change = 3, change_prob = change_prob)

    sp = ['<start> ' + ' '.join(w) + ' <end>' for w in sp]
    sp_a = ['<start> ' + ' '.join(w) + ' <end>' for w in sp_a]

    return sp, sp_a

def build_tokenizer(langs):

    lang_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
    for lang in langs:
        lang_tokenizer.fit_on_texts(lang)

    return lang_tokenizer

def tokenize(tokenizer, word_list):

    tensor = lang_tokenizer.texts_to_sequences(lang)
    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding='post')

    return tensor
