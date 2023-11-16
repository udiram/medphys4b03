import numpy as np

# Given data points
energies = np.array([27.5, 30.0, 35.0])
displacements = np.array([20.13, 18.76, 16.56])

# Point to interpolate
point = 32.5

# Perform linear interpolation
interpolated_energy = np.interp(point, energies, displacements)

print(f"Interpolated energy at {point}: {interpolated_energy}")