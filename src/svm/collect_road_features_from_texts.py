# -*- coding: utf-8 -*-
from random import shuffle
import math
#import os
def get_list_of_feature_vectors(path_to_text_file):
    file_handle = open(path_to_text_file, "r")
    file_text = file_handle.read()
    file_list = file_text.split('\n')
    return file_list

def get_training_and_testing_lists(list_in, training_percentage):
    
    num_training = int(math.floor(len(list_in)*training_percentage))
    shuffle(list_in)
    training_list = list_in[0:num_training]
    testing_list = list_in[num_training:len(list_in)]    
    
    return training_list, testing_list

def print_list_to_file(path_to_file_to_write, list_to_write):
    
    file_handle = open(path_to_file_to_write,"w")
    for item in list_to_write:
        file_handle.write("%s\n" %item)
        
distance_string = "distance[-15]"
left_features_list = get_list_of_feature_vectors("/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/featuresForSVM/"+distance_string+"left.txt")
right_features_list = get_list_of_feature_vectors("/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/featuresForSVM/"+distance_string+"right.txt")
straight_features_list = get_list_of_feature_vectors("/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/featuresForSVM/"+distance_string+"straight.txt")

training_percentage = 0.9

left_training_list, left_testing_list = get_training_and_testing_lists(left_features_list,training_percentage)
right_training_list, right_testing_list = get_training_and_testing_lists(right_features_list,training_percentage)
straight_training_list, straight_testing_list = get_training_and_testing_lists(straight_features_list,training_percentage)
training_lists = left_training_list + right_training_list + straight_training_list
testing_lists = left_testing_list + right_testing_list + straight_testing_list

# error checking (removing empty list elements)

training_lists = [x for x in training_lists if x]
testing_lists = [x for x in testing_lists if x]

training_filepath = "/home/skhokhar/workspace/trackPreparation/src/svm/training_svm.txt"
testing_filepath = "/home/skhokhar/workspace/trackPreparation/src/svm/testing_svm.txt"
print_list_to_file(training_filepath, training_lists)
print_list_to_file(testing_filepath, testing_lists)


""" 

to run this code and svm binaries run the bash file at ~/software/libsvm-3.18/salman.sh (another copy in this project src/sv/salman.sh, need to change addresses for svm binaries if using this file)

"""