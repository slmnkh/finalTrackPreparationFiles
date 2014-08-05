# -*- coding: utf-8 -*-

import shutil

prediction_file_path = "/home/skhokhar/workspace/trackManipulation/rsc/prediction.output"
prediction_file_handle = open(prediction_file_path,"r")
prediction_text = prediction_file_handle.read()
prediction_lines = prediction_text.split('\n')
# remove first line. prediction data starts from second line
prediction_lines.pop(0)

file_names_path = "/home/skhokhar/workspace/trackManipulation/rsc/label_prediction_file_names.txt"
file_names_file_handle = open(file_names_path,"r")
file_names_text = file_names_file_handle.read()
file_names_list = file_names_text.split('\n')

# path to save the renamed text files
saving_path = "/home/skhokhar/workspace/trackManipulation/rsc/text_files/clean_texts_with_labels/"

# possible labels for data (-1 = right, 0 = straight, 1 = left)
labels = ['right', 'straight', 'left']

# read the file names in order. read the same index for label assigned. get label string. 
# change the name of the file to include label and change the folder in the name string. save. 

for ind, line in enumerate(file_names_list):

    if len(line) is 0:
        continue
    # get the string for label
    prediction_at_ind = prediction_lines[ind]
    numeric_label = int(prediction_at_ind[0:prediction_at_ind.index(' ')])
    label = labels[numeric_label+1]
    # sanity check: label should be between -2 and 2 (excluding limits)
    assert (numeric_label < 2 and numeric_label > -2)
    
    file_name_to_save = line[line.rindex('/')+1:line.index('.')] + '[' + label + '].txt'
    path_to_file_to_save = saving_path + file_name_to_save
        
    
    shutil.copyfile(line,path_to_file_to_save)
    
    
    
    
    
    
    

    