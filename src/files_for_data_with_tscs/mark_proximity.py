# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 18:16:05 2014

@author: skhokhar
"""

def prox(track, centre):
    
#     from readTracks import returnTrack
#     import gpsDistance

    from gps_util_from_gpspoints import gpsDistance
    
#     centre = [37.395867, -122.053874]
    threshold = 30
    proximity = []
    
    for iRow in range(0,track.shape[0]):
        
        temp = list(track[iRow,0:2])
        distance = gpsDistance(temp, centre)
        proximity.append(int(distance < threshold))
    
    return proximity    

def findall(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
    
def readCenterLocation(filePath, interName):
    
    my_file = open(filePath)
    
    for line in my_file:
        spaces = findall(line," ")
        if line[0:spaces[0]]==interName:
            center = [float(line[spaces[1]+1:spaces[2]]),float(line[spaces[2]+1:len(line)-1])]
            return center
    
    return [-1,-1]

    
    