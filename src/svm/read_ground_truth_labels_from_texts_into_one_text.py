# -*- coding: utf-8 -*-

import glob

path_for_ground_truthed_files = '/home/skhokhar/workspace/trackManipulation/rsc/text_files/clean_texts_with_labels/*.txt'

list_of_files = glob.glob(path_for_ground_truthed_files)
ground_truth_file_handle = open("/home/skhokhar/workspace/trackManipulation/rsc/text_files/ground_truth_file.txt","w")
label_dict = dict(left = 1, straight = 0, right = -1)

for line in list_of_files:
    
    string_label = line[line.index('[')+1:line.index(']')]
    numeric_label = label_dict[string_label]
    line_to_write = string_label + ' ' + str(numeric_label) + ' ' + line
    ground_truth_file_handle.writelines(line_to_write + '\n')
    
ground_truth_file_handle.close()
    
    