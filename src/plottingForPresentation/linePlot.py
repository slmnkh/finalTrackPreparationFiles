
# -*- coding: utf-8 -*-

# read a text file and plot the data in one line

import numpy, seaborn, pandas
import pylab as plt
file_to_read = "/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_01/resultsOverDistance.txt"
file_handle = open(file_to_read,"r")
data = []
for ind, line in enumerate(file_handle):
    numeric_line = line.split(" ")
    data.append(numeric_line) 

data = numpy.vstack(data)
plt.figure()
plt.hold("on")
plt.plot(data[:,0], data[:,1])
plt.axis([10, -15, 0, 100])

"""

errors to fix:

axis range shows box where there should be a negative sign

"""


