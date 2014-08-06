# -*- coding: utf-8 -*-
import os
import os.path
import shutil
path_to_list_of_files_to_copy = "/home/skhokhar/workspace/trackPreparation/rsc/ground_truth_labels.txt"
file_for_list_to_copy_handle = open(path_to_list_of_files_to_copy)
path_to_copy_files_from = "/home/skhokhar/workspace/trackPreparation/rsc/text_files/clean_texts_with_labels"
path_to_copy_files_to = "/home/skhokhar/workspace/trackPreparation/rsc/text_files/clean_texts_with_labels_temp"

def findall(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
    
for line in file_for_list_to_copy_handle:
    
    spaces = findall(line, ' ')    
    file_path_only = line[spaces[1]:-1]
    file_name_only = file_path_only[file_path_only.rindex('/'):]
    file_path_to_check = path_to_copy_files_from + "/" + file_name_only + ".txt" 
        
    if os.path.isfile(file_path_to_check):
        
        file_path_to_save = path_to_copy_files_to + "/" + file_name_only + ".txt"
        shutil.copyfile(file_path_to_check, file_path_to_save)      

