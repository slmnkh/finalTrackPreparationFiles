


# 1 - detect stops, remove them

# 2 - detect add label annotation to track

# 3 - export in format needed by svm

def filterTrack(track, **kwargs):
    
    import numpy

    if kwargs.has_key('thresh') is False:
        thresh = 1
    else:
        thresh = kwargs['thresh']

    distances = computeDistances(track)
    
    ids2remove = []
    
    for i, val in enumerate(distances):
        
        if val < thresh:
            
            ids2remove.append(i)
            
    track = numpy.delete(track,ids2remove,axis = 0)
    print len(ids2remove)
    print len(track)
    return track

        
# import matplotlib.pyplot as pp
# pp.ion()
# fig = pp.figure()

def computeDistances(track, **kwargs):
    
    from gps_util_from_gpspoints import gpsDistance
    
    if kwargs.has_key('framegap') is False:
        
        framegap = 10
        
    else:
        
        framegap = kwargs['framegap']
        
    
    distances = []
    
    for i in range(0,len(track)-framegap):
        
          distances.append(gpsDistance([track[i,0],track[i,1]],[track[i+framegap,0],track[i+framegap,1]]))
          
    return distances
    
    

