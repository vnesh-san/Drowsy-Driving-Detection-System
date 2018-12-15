# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 18:57:11 2017

@author: subha
"""

import mne
import pyeeg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

from sklearn.decomposition import FastICA, PCA

data=mne.io.read_raw_edf('C:\\Users\\User\\Desktop\\ctdt\\datasets\\vigneshf.edf');

text_file = np.loadtxt("C:\\Users\\User\\Desktop\\ctdt\\datasets\\vigneshf.txt","string");
file2=text_file[:,1]
file3=[];
for line in file2:
    file3.append(float(line))

arr=np.asarray(file3);
ica = mne.preprocessing.ICA()
ica.fit(data);  # Get the estimated sources
C=ica.get_components();
S=ica.get_sources(data);
#ica.plot_sources(data);

arr1=[0.5,4,7,12,30] 
S1,S2=pyeeg.bin_power(file3,arr1,500);
print S1


