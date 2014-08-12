# -*- coding: utf-8 -*-

# read text file names from tracks folder and make folders of the same names
import os
import glob
import shutil
list_of_files = glob.glob("/home/skhokhar/common/people/skhokhar/demo_tracks/run_169/tracks/*.txt")
for file_name in list_of_files:
    
    dir = file_name[:file_name.index(".")]
    if os.path.isdir(dir) is False:
        os.mkdir(dir)
    save_path = file_name[:file_name.index(".")]+"/track.txt"
    shutil.copyfile(file_name, save_path)