# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:11:33 2024

@author: shiduyule
"""
import numpy as np

# Assuming f_data and t_data are NumPy arrays


data = np.load('data1.npy')
f_data = data[:,1]
t_data = data[:,0]

# Loop to handle NaN values
for i in range(len(f_data)):
    if np.isnan(f_data[i]):
        t_data[i] = 0
        f_data[i] = f_data[0]

# print("f_data after handling NaN values:", f_data)
# print("t_data after handling NaN values:", t_data)
