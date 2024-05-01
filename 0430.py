# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:44:53 2024

@author: shiduyule
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Set font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'



data = np.load('data6.npy')
f_data = data[:,1]
t_data = data[:,0]

# Loop to handle NaN values
for i in range(len(f_data)):
    if np.isnan(f_data[i]):
        t_data[i] = 0
        f_data[i] = f_data[0]



# Define damping vibration function model
def damping_vibration(t, A, alpha, omega):
    return A * np.exp(-alpha * t) * np.cos(omega * t)

# Load data
# data = np.load('data1.npy')
# data = data.astype(float)   


# Fit the data using curve_fit
initial_guess = (1 , 0.05, 0.02)  # Initial guess for parameters (A, alpha, omega)
lower_bounds = (0, 0, 0)  # Lower bounds for parameters (A, alpha, omega)
upper_bounds = (np.inf, np.inf, np.inf)  # Upper bounds for parameters (A, alpha, omega)
params, covariance = curve_fit(damping_vibration, t_data, f_data, p0=initial_guess, maxfev=5000)


# Fitted parameter values
A_fit, alpha_fit, omega_fit,  = params

omega_fit = np.abs(omega_fit) 

print(f"Fitted parameters: A={A_fit}, alpha={alpha_fit}, omega={omega_fit}")

# Calculate damping ratio

omega_n = omega_fit  # Natural frequency from the fit
zeta = alpha_fit / omega_n

# Plot the fitted curve
t_plot = np.linspace(0, 400, 100)  # Time points for plotting the fitted curve
f_fit = damping_vibration(t_plot, *params)  # Calculate function values on the fitted curve

# Plot original data and fitted curve
plt.plot(t_data, f_data, 'bo', label='Original Data', alpha=0.7)  # Blue circles with transparency
plt.plot(t_plot, f_fit, 'maroon', label=f'Fitted Curve\nDamping Ratio: {zeta:.3f}')  # Maroon solid line for the fitted curve

plt.xlabel('Time (s)')
plt.ylabel('Function Value')
plt.legend()
plt.title('Damped Vibration with Fitted Curve')
plt.grid(True)
plt.show()
