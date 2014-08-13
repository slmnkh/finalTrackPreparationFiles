

# -*- coding: utf-8 -*-
import numpy as np
def get_data_from_text_file(path):
    file_to_read = path
    file_handle = open(file_to_read,"r")
    data = []
    for ind, line in enumerate(file_handle):
        string_line = (line.split(" "))
        numeric_line = map(float,string_line) 
        data.append(numeric_line) 
    
    data = np.vstack(data)
    return data