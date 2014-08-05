# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-


def return_full_drive_track(*args): # args[0] should be path to file, args[1] should be a flag indicating whether time stamps should be retained (1 = yes, default)
    
    # note the path to the input file points to a file that is saved directly by the car sensors 
    
    import numpy
    
    print len(args)
    if len(args) == 0:
        filePath = "/home/skhokhar/common/Project/VSLAM-2k/2014_6_18_Rakesh/GPS_061814_134428.txt"
    else:
        filePath = args[0]

    if len(args) < 2:
#         print len(args)
        add_tsc = 1
    else:
#         print len(args)
        add_tsc = args[1]
        
    my_file = open(filePath,"r")
    
    def findall(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]
        
    track = []
    badIds = []
    for a, b in enumerate(my_file):
        
        #print a
           
        commas = findall(b,',')
        if len(commas) < 3:
            break
        if add_tsc == 0:
            b = b[commas[2]+1:len(b)]
        else:
            b = b[commas[2]+1:len(b)]+","+b[0:commas[0]]
        c = [float(x) for x in b.split(',')]
                
        if len(c) != 7:
            badIds.append(a)
        
        track.append(c)
    
    if len(badIds) > 1:
        return badIds
    else:
        track = numpy.vstack(track)
        return track
    

# track = returnTrack("/home/skhokhar/common/Project/VSLAM-2k/2014_6_18_Rakesh/GPS_061814_125558.txt")

# track = returnTrack()

             
def readSingleTrackFromFile(*args):
    
        
    import numpy
    if len(args) == 0:
        filePath = "/home/skhokhar/workspace/trackManipulation/rsc/text_files/Ellis_National_GPS_061714_152841_000.txt"
    else:
        filePath = args[0]

    my_file = open(filePath,"r")
    
    def findall(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]
        
    track = []
    badIds = []
    
    for a, b in enumerate(my_file):

        c = [float(x) for x in b.split(' ')]
        track.append(c)
    
    if len(badIds) > 1:
        return badIds
    else:
        track = numpy.vstack(track)
        return track
    

