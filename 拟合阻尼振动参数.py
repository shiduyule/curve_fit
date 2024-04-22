import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Set font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# Define damping vibration function model
def damping_vibration(t, A, alpha, omega, phi):
    return A * np.exp(-alpha * t) * np.cos(omega * t + phi)

# Sample data

# t_data = np.array([0, 1, 2, 3, 4, 5])  # Time points
    
# f_data = np.array([5.5, 4.3, 3.2, 2.1, 1.0, 0.5])  # Corresponding function values

#t_data = np.transpose(data)
data = np.load('data1.npy')
data = data.astype(float)   

t_data = data[:,0] # Time points
    
f_data = data[:,1]  # Corresponding function values

# Fit the data using curve_fit
initial_guess = (1.0, 0.1, 1.0, 0)  # Initial guess for parameters (A, alpha, omega, phi)
params, covariance = curve_fit(damping_vibration, t_data, f_data, p0=initial_guess)

# Fitted parameter values
A_fit, alpha_fit, omega_fit, phi_fit = params
print(f"Fitted parameters: A={A_fit}, alpha={alpha_fit}, omega={omega_fit}, phi={phi_fit}")

# Plot the fitted curve
t_plot = np.linspace(0, 160, 100)  # Time points for plotting the fitted curve
f_fit = damping_vibration(t_plot, *params)  # Calculate function values on the fitted curve

plt.plot(t_data, f_data, 'bo', label='Original Data')  # Plot original data
plt.plot(t_plot, f_fit, 'r-', label='Fitted Curve')  # Plot fitted curve
plt.xlabel('Time')
plt.ylabel('Function Value')
plt.legend()

# Save the image with tight bounding box
plt.savefig('damping_vibration_fit.png', dpi=300, bbox_inches='tight')
plt.show()
