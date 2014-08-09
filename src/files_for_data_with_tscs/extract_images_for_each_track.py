

import glob, os, shutil, numpy
list_of_files = glob.glob("/home/skhokhar/common/people/skhokhar/demo_tracks/run_169/tracks/*.txt")
video_tsc_file_handle = open("/home/skhokhar/software/testing_tsc_extraction/test.txt","r")
video_tscs = video_tsc_file_handle.readlines()
frames_path = "/home/skhokhar/common/people/skhokhar/framesFrom[2014_7_11_forensics]/run_169/"


for file_name in list_of_files: # for all files (each containing gps and time data from one track) 

    # read file, get start and end time stamps
    curr_file_handle = open(file_name, "r")
    lines = curr_file_handle.readlines()
    line_st = lines[0].split(' ')
    line_end = lines[-1].split(' ')
    tsc_st = float(line_st[-1])
    tsc_end = float(line_end[-1])
    
    # get the frames of video that are in current track    
    video_tscs_numeric = [float(x) for x in video_tscs]
    indices_in_track = [x for x,y in enumerate(video_tscs_numeric) if y > tsc_st and y < tsc_end]
    
    curr_track_tscs = video_tscs[indices_in_track[0]:indices_in_track[-1]+1]
    # copy those frame indices into folder for track
    save_path = file_name[:file_name.index(".")]+"/images/"
        
    
    try:
        os.stat(save_path)
    except:
        os.mkdir(save_path)
    
    for ind, val in enumerate(indices_in_track):
        
#        shutil.copyfile(frames_path + "frm%.06d.png"%val,save_path + "frm%.06d.png"%ind)
        print "File %d copied"%ind
        
    
    save_path_for_tsc_text_file = file_name[:file_name.index(".")]+"/tscs.txt"
    
    tsc_file_handle = open(save_path_for_tsc_text_file,"w")
    tsc_file_handle.writelines(curr_track_tscs)    
    
      
    
    
    
       