'''
Created on Apr 27, 2015

@author: jdevince
'''

#Used to analyze features to extract most important features
#Run this after running ENSEMBLE - RF, SVM, NB (or file won't exist)

import pickle

with open("feature_importances", 'rb') as f:
    my_list = pickle.load(f)

list = []
    
for x in range(0,my_list.size):
    if my_list[x] > 0.0028:
        list.append([x, my_list[x]])
        
print list
print len(list)