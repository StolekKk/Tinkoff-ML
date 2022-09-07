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


def make_text(filepath):
        row = ""

        with open(filepath, "r", encoding='utf-8') as f:
            for line in f.readlines():
                if line != '\n':
                    row += line
        return row

def token(row):
    row = row.lower()
    row = re.sub(r'[^a-z0-9а-яё\s]', '', row)
    row = re.sub(r'\n', ' ', row)
    row = row.split()
    return row

def fit(dictionary, row, order):
    for i in range(0, len(row) - order):
        if order == 1: 
            if row[i] in dictionary:
                dictionary[row[i]].append(row[i+1])
            else:
                dictionary[row[i]] = [row[i+1]]
        else:
            window = tuple(row[i: i+order])
            if window in dictionary:
                dictionary[window].append(row[i+order])
            else:
                dictionary[window] = [row[i+order]]


# In[ ]:


length = input()
data = {}
model_path = str(Path.home() / 'Documents/bot/model.pkl')
data_path = str(Path.home() / 'Documents/bot/lev.txt')
#data = open(data_path, r)
i = 1
while i <= int(length):
    fit(data, token(make_text(data_path)),i)
    i+=1
with open(model_path, "w+b") as f:
    pickle.dump(data, f)
# По сути тут заканчится train.py


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




