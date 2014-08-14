
# -*- coding: utf-8 -*-

# read a text file and plot the data in one line

from get_data_from_text_file import get_data_from_text_file
import numpy, seaborn, pandas
import pylab as plt
import matplotlib as mpl

file_to_read = "/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_01/resultsOverDistance.txt"
file_handle = open(file_to_read,"r")
data = []
for ind, line in enumerate(file_handle):
    numeric_line = line.split(" ")
    data.append(numeric_line) 

states_01 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_01/resultsOverDistance.txt')
#states_02 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_02/resultsOverDistance.txt')
states_03 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_03/resultsOverDistance.txt')
#states_04 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_04/resultsOverDistance.txt')
states_05 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_05/resultsOverDistance.txt')

plt.figure()
plt.hold("on")
plt.axis([0, 25, 50, 100])


cfig = plt.plot(states_01[:,1], color = "yellow", label = '02: Distance to Intersection')
#plt.plot(states_02[:,1], color = "seagreen", label = '03: Angle from lane')
plt.plot(states_03[:,1], color = "steelblue", label = '01, 02')
#plt.plot(states_04[:,1], color = "purple", label = '01, 03')
plt.plot(states_05[:,1], color = "magenta", label = '02, 03')


plt.legend(loc='upper left')

#cfig.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
#cfig.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())

plt.grid(b=True, which='major', color='w', linewidth=1.0)
plt.grid(b=True, which='minor', color='w', linewidth=0.5)



# -*- coding: utf-8 -*-

