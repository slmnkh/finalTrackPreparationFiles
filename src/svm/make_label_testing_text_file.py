# -*- coding: utf-8 -*-


# choose a fixed number of points (say 10) from a gps track. compute angles between segments and train svm


import glob

from get_feature_vector_from_cleantext_file import get_features

list_of_label_testing_files = glob.glob("/home/skhokhar/workspace/trackManipulation/rsc/text_files/clean_texts/*.txt")

savePath = "/home/skhokhar/workspace/trackManipulation/rsc/label_prediction_features.txt"
save_order_path = "/home/skhokhar/workspace/trackManipulation/rsc/label_prediction_file_names.txt"

write_file = open(savePath,"w")
write_file_names = open(save_order_path,"w")
# labels_dict = dict(left = 1, straight = 0, right = -1)

for file_path in list_of_label_testing_files:
        
    #ground_truth_label = file_path[file_path.index('[')+1:file_path.index(']')]
    line, ignore_1, ignore_2 = get_features(file_path)
    label_num = -99#labels_dict[ground_truth_label]    
    line = '%d'%label_num + line
    write_file.write(line)
    write_file_names.write(file_path + '\n')
    
write_file.close()
write_file_names.close()
    
    


