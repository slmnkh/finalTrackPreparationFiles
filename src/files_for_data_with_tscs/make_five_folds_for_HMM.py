# -*- coding: utf-8 -*-

# read in xml files. 

# shuffle to avoid segregating intersections into folds.
# divide each of the three lists (right, straight and left) into 5 parts each
# put four parts into training folders for fold "i" (/Fold'i'/left etc) and the fifth part of all three into /Fold'i'/testing/
# also keep a copy in this project for svm results


import glob

def get_list_of_files_from_path(path):
    list_of_files = glob.glob(path)
    list_of_files.sort()
    return list_of_files

def get_list_of_folds(list_in, folds):
    num_entries = len(list_in)
    length_of_fold = num_entries/folds
    list_of_folds = []    
    for i in range(folds-1):
        list_of_folds.append(list_in[i*length_of_fold:(i+1)*length_of_fold])
    list_of_folds.append(list_in[(i+1)*length_of_fold:])
    return list_of_folds
    
required_folds = 5    
    
sorted_list_of_left = get_list_of_files_from_path("/home/skhokhar/workspace/trackPreparation/rsc/ml_file_exports/xml_files/left/*.xml")
sorted_list_of_right = get_list_of_files_from_path("/home/skhokhar/workspace/trackPreparation/rsc/ml_file_exports/xml_files/right/*.xml")
sorted_list_of_straight = get_list_of_files_from_path("/home/skhokhar/workspace/trackPreparation/rsc/ml_file_exports/xml_files/straight/*.xml")

left_folds = get_list_of_folds(sorted_list_of_left, required_folds)
right_folds = get_list_of_folds(sorted_list_of_right, required_folds)
straight_folds = get_list_of_folds(sorted_list_of_straight, required_folds)