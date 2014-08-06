# -*- coding: utf-8 -*-
from random import shuffle

def get_list_of_feature_vectors(path_to_text_file):
    file_handle = open(path_to_text_file, "r")
    file_text = file_handle.read()
    file_list = file_text.split('\n')
    return file_list

left_features_list = get_list_of_feature_vectors("/home/skhokhar/workspace/finalHMM/finalHMM/rsc/featuresForSVM/straight.txt")
right_features_list = get_list_of_feature_vectors("/home/skhokhar/workspace/finalHMM/finalHMM/rsc/featuresForSVM/right.txt")
straight_feature_file_handle = open("/home/skhokhar/workspace/finalHMM/finalHMM/rsc/featuresForSVM/straight.txt","r")



left_feature_file_handle = open("/home/skhokhar/workspace/finalHMM/finalHMM/rsc/featuresForSVM/left.txt","r")
right_feature_file_handle = open("/home/skhokhar/workspace/finalHMM/finalHMM/rsc/featuresForSVM/right.txt","r")
straight_feature_file_handle = open("/home/skhokhar/workspace/finalHMM/finalHMM/rsc/featuresForSVM/straight.txt","r")

left_features_text = left_feature_file_handle.read()
right_features_text = right_feature_file_handle.read()
straight_features_text = straight_feature_file_handle.read()

left_features_list = left_features_text.split('\n')
right_features_list = right_features_text.split('\n')
straight_features_list = straight_features_text.split('\n')

percent_for_training = 0.8
training_list = []
testing_list = []

left_features_list = shuffle(left_features_list)
right_features_list = shuffle(right_features_list)
straight_features_list = shuffle(straight_features_list)

