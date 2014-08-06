# -*- coding: utf-8 -*-
import os
import os.path
import glob
path_to_delete_files_from = "/home/skhokhar/workspace/trackPreparation/rsc/text_files/clean_texts_with_labels"
path_to_read_error_list_from = "/home/skhokhar/workspace/trackPreparation/rsc/tracksWithErrors.txt" 
error_list_file_handle = open(path_to_read_error_list_from)
list_of_files_in_target_folder = glob.glob(path_to_delete_files_from + "/*.txt")

for line in error_list_file_handle:
    
    
   
    for file_name in list_of_files_in_target_folder:
        
        #print line+ " : "+file_name
        if file_name.find(line[:-1]) > -1:
            
            print "\nFound!\n"
            os.remove(file_name)
            break



        
        