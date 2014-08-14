
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

features_00 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/Features_00/resultsOverDistance.txt')
features_01 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/Features_01/resultsOverDistance.txt')
features_02 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/Features_02/resultsOverDistance.txt')
features_00_01 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/Features_00_01/resultsOverDistance.txt')
features_00_02 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/Features_00_02/resultsOverDistance.txt')
features_01_02 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/Features_01_02/resultsOverDistance.txt')

plt.figure()
plt.hold("on")
plt.axis([0, 25, 50, 100])


#plt.plot(data_01[:,1], color = "steelblue", label = 'States: 01')
#plt.plot(data_02[:,1], color = "seagreen", label = 'States: _ 02')
cfig = plt.plot(features_00[:,1], color = "indianred", label = '01: Distance from Lane')
plt.plot(features_01[:,1], color = "yellow", label = '02: Distance to Intersection')
plt.plot(features_02[:,1], color = "seagreen", label = '03: Angle from lane')
plt.plot(features_00_01[:,1], color = "steelblue", label = '01, 02')
plt.plot(features_00_02[:,1], color = "purple", label = '01, 03')
plt.plot(features_01_02[:,1], color = "magenta", label = '02, 03')
#cfig = sns.tsplot(data_features_00[:,1], color = "yellow")

plt.legend(loc='upper left')

#cfig.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
#cfig.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())

plt.grid(b=True, which='major', color='w', linewidth=1.0)
plt.grid(b=True, which='minor', color='w', linewidth=0.5)



