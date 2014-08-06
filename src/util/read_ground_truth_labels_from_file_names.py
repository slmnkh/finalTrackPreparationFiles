# -*- coding: utf-8 -*-

import glob
path_to_files_with_labels = "/home/skhokhar/workspace/trackPreparation/rsc/plots_of_cleaned_texts_with_labels"
list_of_files =glob.glob(path_to_files_with_labels + "/*.png")
file_to_write_handle = open("/home/skhokhar/workspace/trackPreparation/rsc/ground_truth_labels.txt","w")
labels_dict = dict(right = -1, straight = 0, left = 1)
ind = 0
for file_name in list_of_files:
    ind = ind + 1    
    name = file_name[:file_name.index('.')]
    string_label = name[name.index('[')+1: name.index(']')]
    numeric_label = labels_dict[string_label]
    file_to_write_handle.write(str(numeric_label)+" "+string_label+" "+name+"\n")
    
print ind