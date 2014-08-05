# -*- coding: utf-8 -*-
def plotTrack(**args):
    
    import pylab as plt
    from read_track_from_text import readSingleTrackFromFile
    if args.has_key('in_track') is True:
        track = args['in_track']
    elif args.has_key('path') is True:
        track = readSingleTrackFromFile(args['path'])
    if args.has_key('sample') is True:
        sample = args['sample']
    else:
        sample = 10
    if args.has_key('pause_flag') is True:
        pause_flag = args['pause_flag']


    print track.shape    
    plt.figure()
    minlat = min(track[:,0])
    maxlat = max(track[:,0])
    minlong = min(track[:,1])
    maxlong = max(track[:,1])
    plt.hold(1)
    plt.axis([minlong,maxlong, minlat,maxlat])    
    #sample = 1
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



