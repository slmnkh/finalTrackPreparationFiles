

# read text files one by one

# plot and wait for user input

# type in numeric label (-1 = right, 0 = straight, left = 1)

# copy file to another location , add label to name

import pylab as plt
import glob
import shutil
from plot_track_from_text import plotTrack

read_path = '/home/skhokhar/workspace/trackManipulation/rsc/text_files/clean_texts/*.txt'
save_path = '/home/skhokhar/workspace/trackManipulation/rsc/text_files/clean_texts_with_labels/'
list_of_files = glob.glob(read_path)

label_dict = ['right','straight','left']
plt.close('all')

for ind, line in enumerate(list_of_files):
    
    plotTrack(path = line)
    image_name_without_path = line[line.rindex('/')+1:line.index('.')]
    plt.pause(0.05)
    numeric_label_string = raw_input('Enter track label')
    numeric_label = int(numeric_label_string) + 1
    label = label_dict[numeric_label]
    
    path_to_save = save_path + image_name_without_path + '[' + label + '].txt'
    
    shutil.copyfile(line, path_to_save)
    
    plt.close('all')
    
        
    