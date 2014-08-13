# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-

# read a text file and plot the data in one line
from get_data_from_text_file import get_data_from_text_file
import numpy as np 
import seaborn as sns 
import pandas as pd
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(style="darkgrid", palette = "dark")
sns.set_style("darkgrid", {"grid.linewidth":.5, "axes.facecolor":"0.9"})

data_01 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_01/resultsOverDistance.txt')
data_02 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_02/resultsOverDistance.txt')
data_03 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_03/resultsOverDistance.txt')
data_04 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/HMMstates_04/resultsOverDistance.txt')
#data_features_00 = get_data_from_text_file('/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/supplementaryResults_[withroad]/Features_00/resultsOverDistance.txt')
data_all = np.dstack(data_01[:,1],data_02[:,1],data_03[:,1],data_04[:,1])

cfig = plt.subplots(1,1)
plt.hold(True)

# define location of intersection
vertline = np.array([[0,10],[100,10]])
plt.plot(vertline[:,1], vertline[:,0])

sns.tsplot(data_all)
"""
sns.tsplot(data_01[:,1], color = "steelblue")
sns.tsplot(data_02[:,1], color = "seagreen")
sns.tsplot(data_03[:,1], color = "indianred")
sns.tsplot(data_04[:,1], color = "yellow")
"""
# set plot window properties

cfig.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
cfig.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
cfig.grid(b=True, which='major', color='w', linewidth=1.0)
cfig.grid(b=True, which='minor', color='w', linewidth=0.5)
cfig.axis([0, 25, 50, 100])

"""

errors to fix:

axis range shows box where there should be a negative sign

"""


