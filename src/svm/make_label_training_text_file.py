
# choose a fixed number of points (say 10) from a gps track. compute angles between segments and train svm


import glob
import pylab as plt
from get_feature_vector_from_cleantext_file import get_features

list_of_label_training_files = glob.glob("/home/skhokhar/workspace/trackManipulation/rsc/text_files/training_files/*.txt")

savePath = "/home/skhokhar/workspace/trackManipulation/rsc/label_training_features.txt"

write_file = open(savePath,"w")

labels_dict = dict(left = 1, straight = 0, right = -1)
colors_dict = dict(left = 'y', straight = 'b', right = 'r' )



for file_path in list_of_label_training_files:
        
    ground_truth_label = file_path[file_path.index('[')+1:file_path.index(']')]
    line, ignore_1, ignore_2 = get_features(file_path)
    label_num = labels_dict[ground_truth_label]    
    line = '%d'%label_num + line
    write_file.write(line)
"""  
    plt.figure()
    plt.hold('on')
    features_as_vect = get_features(file_path, return_string = 0)
    color = colors_dict[ground_truth_label]    
    plt.plot(features_as_vect, color)
    plt.axis([0,20,-0.5,0.5])
    #plt.xlabel(file_path[file_path.rindex('/'):])
"""
write_file.close()



    
    


