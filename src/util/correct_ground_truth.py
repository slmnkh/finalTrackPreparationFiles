# -*- coding: utf-8 -*-
import glob
import os
input_folder = '/home/skhokhar/workspace/trackManipulation/rsc/text_files/clean_texts_with_labels'

list_of_files = glob.glob(input_folder + '/*.txt')

labels_dict = dict(right = -1, straight = 0, left = 1)
labels_list = ['right', 'straight', 'left']

for name in list_of_files:
    
    label = name[name.index('[')+1:name.index(']')]
    
    if labels_dict[label] == -1:
        
        new_name = name[:name.index('[')]+'[left].txt'
        os.rename(name, new_name)
        
    elif labels_dict[label] == 1:
        
        new_name = name[:name.index('[')]+'[right].txt'
        os.rename(name, new_name)
        