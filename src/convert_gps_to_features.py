
# choose a fixed number of points (say 10) from a gps track. compute angles between segments and train svm


import glob

list_of_files = glob.glob("/home/skhokhar/workspace/trackManipulation/rsc/clean_text/*.txt")
list_of_label_training_files = glob.glob("")

savePath = "/home/skhokhar/workspace/trackManipulation/rsc/label_training.txt"

write_file = open(savePath,"a")


for i in list_of_label_training_files:
    
    
    line = getFeatures(i, return_string = 1)
    write_file.write(line)
    

write_file.close()
    
    


