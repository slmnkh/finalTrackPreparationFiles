


from lxml import etree as ET
import glob
list_of_files = glob.glob("/home/skhokhar/workspace/trackManipulation/rsc/text_files/clean_texts_with_labels/*.txt")

for ind, filename in enumerate(list_of_files):
    
    root = ET.Element('Placemark')
    name = ET.SubElement(root, 'name')
    name.text = "Simple placemark"
    point = ET.SubElement(root, 'Point')
    coordinates = ET.SubElement(point, 'coordinates')
    # numpy.savetxt("test.txt", track1, fmt='%3.15f', delimiter=' ')
    #st = "1,2,3\n\t4,5,6\n"
    f = open(filename,"r")
    coordinates.text = f.read()
    filename = filename[0:filename.index("text")]+"kml_files/"+filename[filename.rindex("/")+1:len(filename)-4]+".kml"
    #print ET.tostring(root, pretty_print=True, xml_declaration=True, encoding = 'utf-8')
    text_file = open(filename, "w")
    text_file.write(ET.tostring(root, pretty_print=True, xml_declaration=True, encoding = 'utf-8'))
        
        
    print "Done with file number : "+str(ind+1)