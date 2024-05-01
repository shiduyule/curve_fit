import numpy as np
import matplotlib.pyplot as plt

# Set font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# Define damping vibration function model
def damping_vibration(t, A, alpha, omega, phi):
    return A * np.exp(-alpha * t) * np.cos(omega * t + phi)

# Given parameters
A_fit = 1.0  # Amplitude
alpha_fit = 0.05  # Damping coefficient
omega_fit = 0.1  # Natural frequency
phi_fit = 0  # Initial phase

# Calculate damping ratio
zeta = alpha_fit / omega_fit

# Generate time data
t_plot = np.linspace(0, 100, 1000)

# Calculate damping vibration function values
f_fit = damping_vibration(t_plot, A_fit, alpha_fit, omega_fit, phi_fit)

# Plot damping vibration
# plt.plot(t_plot, f_fit, label='Damped Vibration')
plt.plot(t_plot, f_fit, label=f'A={A_fit}, alpha={alpha_fit}, omega={omega_fit}, phi={phi_fit}, zeta={zeta:.2f}')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Damped Vibration')
plt.legend()

# Annotate the plot with equations and damping ratio
equation_text = r'$x(t) = Ae^{-\alpha t} \cos(\omega t + \phi)$'
zeta_text = rf'Damping Ratio ($\zeta$) = $\frac{{\alpha}}{{\omega}}$'
plt.annotate(equation_text, xy=(0.5, 0.5), xycoords='axes fraction', fontsize=14, ha='center')
plt.annotate(zeta_text, xy=(0.5, 0.4), xycoords='axes fraction', fontsize=14, ha='center')

plt.grid(True)
plt.show()
