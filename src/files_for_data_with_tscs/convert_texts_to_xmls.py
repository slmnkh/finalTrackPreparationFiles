# -*- coding: utf-8 -*-

from lxml import etree as ET
import glob, shutil
list_of_files = glob.glob("/home/skhokhar/common/people/skhokhar/demo_tracks/run_169/tracks/*.txt")
#path_to_save_xmls = '/home/skhokhar/software/testing_tsc_extraction/'
path_to_save_xmls = '/home/skhokhar/common/people/skhokhar/demo_tracks/run_169/tracks/'
intersection_labels_file_handle = open('/home/skhokhar/workspace/trackPreparation/rsc/intersectionCenters.txt')
intersection_dict = dict(Middlefield_Ellis = 1, Middlefield_Logue = 2, Logue_Maude = 3, Fairchild_Ellis = 4, Ellis_National = 5, National_Fairchild = 6)


for ind, name in enumerate(list_of_files):
    
    root = ET.Element('intersections')
    intersection_name = name[name.rindex('/')+1:name.index('_NCOM_')]
    intersection_numeric_id = intersection_dict[intersection_name]
#    if intersection_numeric_id == 4:
#        continue
    intersection = ET.SubElement(root, 'intersection', idx=str(intersection_numeric_id))
    #string_label = name[name.index('[')+1:name.index(']')]
    trace = ET.SubElement(intersection, 'trace', idx=name[name.rindex("/")+1:len(name)])#, label = string_label)
    # numpy.savetxt("test.txt", track1, fmt='%3.15f', delimiter=' ')
    #st = "1,2,3\n\t4,5,6\n"
    f = open(name,"r")
    trace.text = f.read()
    xml_name = path_to_save_xmls+name[name.rindex("/")+1:name.index('.')]+".xml"
    print xml_name
    #print ET.tostring(root, pretty_print=True, xml_declaration=True, encoding = 'utf-8')
    with open(xml_name, "w") as text_file:
        text_file.write(ET.tostring(root, pretty_print=True, xml_declaration=True, encoding = 'utf-8'))
        
    save_path = xml_name[:xml_name.index(".")]+"/track.xml"
    shutil.copyfile(xml_name, save_path)
        
    print "Done with file number : "+str(ind+1)