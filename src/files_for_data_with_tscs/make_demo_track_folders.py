# -*- coding: utf-8 -*-

# read text file names from tracks folder and make folders of the same names
import os
import glob
import shutil
list_of_files = glob.glob("/home/skhokhar/common/people/skhokhar/demo_tracks/run_169/tracks/*.txt")
for file_name in list_of_files:
    
    dir = os.path.dirname(file_name[:file_name.index(".")])
    try:
        os.stat(dir)
    except:
        os.mkdir(dir)
    save_path = file_name[:file_name.index(".")]+"/"+file_name[file_name.rindex("/")+1:]
    shutil.move(file_name, save_path)