#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import pickle
import os
import re
import sys
from pathlib import Path
import random


# In[ ]:


#А тут начентся generate.py
model_path = str(Path.home() / 'Documents/bot/model.pkl')
data_path = str(Path.home() / 'Documents/bot/lev.txt')
length = input()
with open(model_path, "rb") as f:
    data = pickle.load(f)
def gen_rand_word():
    word = [random.choice(list(filter(lambda x: isinstance(x, str), list(data.keys()))))]
    return word
def gen_first_word():
    if 'я' in data:
        seed_word = 'я'
        while seed_word == 'я':
            seed_word =  gen_rand_word()
        return seed_word
    return random.choice(data.keys())
def gen_sentence(length):
    windowl =tuple(('я'))
    word = gen_first_word()
    sentence = word
    i = 0
    while i < int(length)-1:
        if i <=1:
            if sentence[i] in data:
                sentence.append(random.choice(data[sentence[i]]))
        else:    
            if len(windowl) == 2:
                print(i)
                window = windowl
                windowl =tuple(('я'))
            else:
                window = tuple(word[0: i])
            if window in data:
                
                sentence.append(random.choice(data[window]))
            else:
                windowl = tuple((word[i-1],word[i]))
                sentence.append(random.choice(data[word[i]]))
        i += 1
    return ' '.join(sentence) + '.'
gen_sentence(length)

