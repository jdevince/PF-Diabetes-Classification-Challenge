'''
Created on Apr 27, 2015

@author: jdevince
'''

#Used to analyze features to extract most important features

import pickle

with open("feature_importances_full_test_with_age_plus_5000_trees", 'rb') as f:
    my_list = pickle.load(f)

list = []
    
for x in range(0,my_list.size):
    if my_list[x] > 0.0028:
        list.append([x, my_list[x]])
        
print list
print len(list)