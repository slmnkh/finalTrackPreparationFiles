
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

data_01 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_01/resultsOverDistance.txt')
data_02 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/HMMstates_02/resultsOverDistance.txt')
data_03 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/HMMstates_03/resultsOverDistance.txt')
data_04 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_03/resultsOverDistance.txt')
data_05 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/5Fold/HMMtest/resultsOverDistance.txt')
plt.figure()
plt.hold("on")
plt.axis([0, 25, 50, 100])


#plt.plot(data_01[:,1], color = "steelblue", label = 'States: 01')
#plt.plot(data_02[:,1], color = "seagreen", label = 'States: _ 02')
plt.plot(data_03[:,1], color = "indianred", label = 'States: _ 03')
cfig = plt.plot(data_04[:,1], color = "yellow", label = 'States: 03')
plt.plot(data_05[:,1], color = "purple", label = 'States: v2_ 03')
#cfig = sns.tsplot(data_features_00[:,1], color = "yellow")

plt.legend(loc='upper left')

#cfig.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
#cfig.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())

plt.grid(b=True, which='major', color='w', linewidth=1.0)
plt.grid(b=True, which='minor', color='w', linewidth=0.5)



