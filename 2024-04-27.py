# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:11:33 2024

@author: shiduyule
"""
import numpy as np

# Assuming f_data and t_data are NumPy arrays
f_data = np.array([1, 2, np.nan, 4, np.nan])
t_data = np.array([10, 20, 30, 40, 50])

# Loop to handle NaN values
for i in range(len(f_data)):
    if np.isnan(f_data[i]):
        t_data[i] = 0
        f_data[i] = f_data[0]

print("f_data after handling NaN values:", f_data)
print("t_data after handling NaN values:", t_data)
