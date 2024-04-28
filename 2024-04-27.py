# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:11:33 2024

@author: shiduyule
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Set font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# Define damping vibration function model
def damping_vibration(t, A, alpha, omega, phi):
    return A * np.exp(-alpha * t) * np.cos(omega * t + phi)

# Sample data
t_data = np.array([0, 1, 2, 3, 4, 5])  # Time points
f_data = np.array([5.5, np.nan, 3.2, 2.1, np.nan, 0.5])  # Corresponding function values with NaN

# Remove NaN values from the data
valid_indices = ~np.isnan(f_data)
t_data_valid = t_data[valid_indices]
f_data_valid = f_data[valid_indices]
