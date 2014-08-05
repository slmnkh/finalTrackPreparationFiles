# -*- coding: utf-8 -*-


def getFeatures(filePath, **args):
        
    if args.has_key('return_string'):
        return_string_flag = args['return_string']
    else:
        return_string_flag = 1
    
    if args.has_key('num_points'):
        num_points = args['num_points']
    else:
        num_points = 20
        
    

    # read a text file, choose ten points, compute angle differences, return features in one line


    read_gps_file = open(filePath,"r")
    track = []
    for line in read_gps_file:
        
        line = line.split(' ')
        track.append([float(line[0]), float(line[1])])
        
    track_len = len(track)
    jump = round(track_len/num_points)
    reduced_track = []
    #print "value of jump : %f" %jump    
    
    for i in range(0,num_points):
        
        reduced_track.append(track[int(i*jump)])
    
    headings, features = compute_angle_diff(reduced_track)
    
    if return_string_flag is 0:
        
        return headings, features
        
    else:
        
        return headings, convert_to_svm_input(features), reduced_track
        
def compute_angle_diff(track):
    
    from gps_util_from_gpspoints import gpsBearing
    headings = []
    
    for i in range(0,len(track)-1):
        
        headings.append(gpsBearing([track[i][0],track[i][1]],[track[i+1][0],track[i+1][1]]))
        
    angle_diffs = []
    
    for i in range(0,len(headings)-1):
        
        angle_diffs.append(smallest_angle(headings[i], headings[i+1]))
    
    return headings, angle_diffs
                
    
def convert_to_svm_input(features):
    
    feature_string = '' # the string that will hold the values in the feature vector input in svm input form

    for ind, value in enumerate(features): # for all features in vector
        
            feature_string = feature_string + ' %d:'%(ind+1) + '%0.15f'%value # add to string, with index of feature 
    
    feature_string = feature_string + '\n'
    
    return feature_string
            
        
def smallest_angle(first_point_heading, second_point_heading):
    
    # note that the returned angle has an associated sign. A positive value implies turning left (counter-clockwise)    
    import math
    difference_in_orientation = second_point_heading-first_point_heading
    return (difference_in_orientation+math.pi)%(2*math.pi) - math.pi
    
    
    
