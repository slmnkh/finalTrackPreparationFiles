# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""

- script reads gps files from sensor. separates a complete drives track into 
parts (this is done for each intersection whose centers are provided below)
saves a separate text file for each track with the format

[intersection_name]_[intersection_name]_[original_sensor_output_filename]_[track_number].txt

...in the location "save_path" given below

"""
# import readTracks
from read_track_from_text import return_full_drive_track
from mark_proximity import prox
from mark_proximity import readCenterLocation

import numpy
from itertools import groupby
from operator import itemgetter

# Intersection information:
# 
# Middlefield_Ellis 01 37.395867 -122.053874
# Middlefield_Logue 02 37.394303 -122.051627
# Logue_Maude 03 37.397342 -122.050207
# Fairchild_Ellis 04 37.402978 -122.051131
# Ellis_National 05 37.400990 -122.051895
# National_Fairchild 06 37.404168 -122.053366
##############################################

list_of_intersections = ["Middlefield_Ellis","Middlefield_Logue","Logue_Maude","Fairchild_Ellis","Ellis_National","National_Fairchild"]
path_to_gps_file = "/home/skhokhar/common/Project/VSLAM-2k/2014_7_11_forensic/NCOM_169.txt"
save_path = "/home/skhokhar/common/people/skhokhar/demo_tracks/run_169/tracks/"

for interName in list_of_intersections:
    
    center = readCenterLocation("/home/skhokhar/workspace/trackPreparation/rsc/intersectionCenters.txt", interName)
    track = return_full_drive_track(path_to_gps_file)
    proximity = prox(track, center)
    name = path_to_gps_file[path_to_gps_file.rindex("/")+1:path_to_gps_file.index(".")]
    data = proximity
    blocks = [map(itemgetter(0), itemgetter(0, -1)(list(g))) + [k] for k, g in groupby(enumerate(data), itemgetter(1))]
    trackblocks = [x for x in blocks if x[2]==1]
    
    for i,oneblock in enumerate(trackblocks):
        
        temp = track[oneblock[0]:oneblock[1],:] # 
        numpy.savetxt(save_path+interName+"_"+name+"_%.03d.txt" %i, temp, fmt='%.15f', delimiter=' ') 
        print "\nDone with track : "+str(i+1)+ " of "+str(len(trackblocks))
    
    print "\n\n ---- Done with intersection : "+interName     