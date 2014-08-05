# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 17:00:22 2014

@author: skhokhar
"""

# ellis intersection lat = 37.3959, long = -122.0539 (from google maps 37.395867, -122.053874)
# formula taken from here: http://www.movable-type.co.uk/scripts/latlong.html
# legend from weblink to my code: phi = lat, lambda = long
# google maps location, manually clicked some distance away: 37.395524, -122.053282

#def gpsDistance(lat1, long1, lat2, long2):
def gpsDistance(P1, P2):
        
    import math
    lat1 = P1[0]
    long1 = P1[1]
    lat2 = P2[0]
    long2 = P2[1]
    
    R = 6371000 # earths radius in meters    
    lat1 = lat1/180*math.pi
    lat2 = lat2/180*math.pi
    long1 = long1/180*math.pi
    long2 = long2/180*math.pi    
    dlat = abs(lat1-lat2)
    dlong = abs(long1-long2)
    
    a = math.pow((math.sin(dlat/2)),2) + math.cos(lat1)*math.cos(lat2)*math.pow(math.sin(dlong/2),2)
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    x = R*c
    
    return x
    
    
def gpsBearing(P1,P2):
    
# formula: θ = atan2( sin Δλ ⋅ cos φ2 , cos φ1 ⋅ sin φ2 − sin φ1 ⋅ cos φ2 ⋅ cos Δλ )
    
    import math
    lat1 = P1[0]
    long1 = P1[1]
    lat2 = P2[0]
    long2 = P2[1]
    
    #R = 6371000 # earths radius in meters    
    lat1 = lat1/180*math.pi
    lat2 = lat2/180*math.pi
    long1 = long1/180*math.pi
    long2 = long2/180*math.pi
    #dlat = abs(lat1-lat2)
    dlong = abs(long1-long2)
    
    bearing = math.atan2(math.sin(dlong)*math.cos(lat2), math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(dlong))
    return bearing