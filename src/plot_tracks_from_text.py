# -*- coding: utf-8 -*-

import glob
import pylab as plt

from plot_track_from_text import plotTrack

file_type = 'png'
plt.close('all')

list_of_clean_tracks = glob.glob("/home/skhokhar/workspace/trackPreparation/rsc/text_files/clean_texts_with_labels/*.txt")
save_path = "/home/skhokhar/workspace/trackPreparation/rsc/text_files/plots_of_cleaned_texts_with_labels"

for file_path in list_of_clean_tracks:
    
    plotTrack(path = file_path, pause_flag = 0)
    figure_path = save_path + file_path[file_path.rindex('/'):file_path.index('.')+1] + file_type
    print figure_path    
    plt.savefig(figure_path)
    plt.pause(0.05)
    plt.close('all')
