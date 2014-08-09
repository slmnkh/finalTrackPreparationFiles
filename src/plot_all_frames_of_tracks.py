# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import glob, os
import pylab as plt
from read_track_from_text import readSingleTrackFromFile

file_type = 'png'
plt.close('all')

list_of_clean_tracks = glob.glob("/home/skhokhar/workspace/trackPreparation/rsc/text_files/clean_texts_with_labels/*.txt")
save_path = "/home/skhokhar/workspace/trackPreparation/rsc/text_files/video_plots"

for ind, file_path in enumerate(list_of_clean_tracks):
    
    #make a separate folder for each track
    new_folder_path = save_path + "/" + file_path[file_path.rindex("/")+1:file_path.index(".")]
    if os.path.isdir(new_folder_path) is False:
        os.mkdir(new_folder_path)        
      
    # get current track as a numpy matrix
    track = readSingleTrackFromFile(file_path)
    # open a blank figure and make axes dimensions to fit track    
    plt.figure();
    minlat = min(track[:,0])
    maxlat = max(track[:,0])
    minlong = min(track[:,1])
    maxlong = max(track[:,1])
    plt.hold("on")
    plt.axis([minlong,maxlong, minlat,maxlat])
    # plot every tenth gps track point    
    sample = 10
        
    for i in range(0,len(track)/sample):
        
        plt.plot(track[i*sample,1],track[i*sample,0],'r.')
        # save path for current frame        
        figure_path = new_folder_path + "/frame%.03d"%i
        plt.savefig(figure_path)
        #plt.pause(0.05)    
    
    plt.pause(0.5)
    plt.close("all")

    print "Done with folder : " + new_folder_path + " , which is Folder number : %d of %d"%(ind,len(list_of_clean_tracks))

"""
    
    for i in range(0,len(track)/sample):
        
        plt.plot(track[i*sample,1],track[i*sample,0],'r.')
#        if pause_flag == 1:
#            plt.pause(0.05)
        #print i*sample
    #plt.pause(0.05)
    for i in range(0,len(track)/(sample*2)):
    
        plt.plot(track[i*sample,1],track[i*sample,0],'b*')
    plt.plot(track[0,1],track[0,0],'b*')
    plt.plot(track[1,1],track[1,0],'b*')

"""