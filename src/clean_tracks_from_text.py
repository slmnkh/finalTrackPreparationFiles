# -*- coding: utf-8 -*-

from read_tracks_from_text import readSingleTrackFromFile
from filter_track_from_nparray import filterTracks
from plot_track_from_text import plotTrack
import glob, numpy
list_of_files = glob.glob("/home/skhokhar/workspace/trackManipulation/rsc/text_files/*.txt")

for ind, filename in enumerate(list_of_files):

    track = readSingleTrackFromFile(filename)
  #  print "Length of track : %d" %len(track)
    track = filterTracks(track, thresh = 0.1)
#    print "After filtering : %d" %len(track)
#    plotTrack(in_track=track)
    
    filename = filename[0:filename.index("text")]+"clean_text/"+filename[filename.rindex("/")+1:len(filename)-4]+".txt"
    #print ET.tostring(root, pretty_print=True, xml_declaration=True, encoding = 'utf-8')
    text_file = open(filename, "w")
    numpy.savetxt(filename, track, fmt='%3.15f', delimiter=' ')
    print "\n Done with file %d"%ind
    
    