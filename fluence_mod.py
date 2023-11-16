import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

density = 1.00  # g/cm^3
cutoff = 62
exclude_initial_points = 0  # Adjust this value based on the number of initial points to exclude

df = pd.read_csv('output.csv', header=0)

energy_list = df['Energy'].tolist()
distance_arr = []

data = {'Energy': [], 'Mass_Stopping_Power': [], 'Stopping_Power': [], 'Distance_Travelled': [], 'Cumulative_Distance': [], 'Filtered_Stopping_Power': []}

# Function to calculate fluence with a 25% decrease from 0 to 15 cm
def calculate_fluence(distance):
    # Implement your fluence calculation logic here
    # For example, you can use a linear decrease from 0 to 15 cm
    if distance <= 15:
        return 0.75 * (15 - distance) / 15
    else:
        return 0.75

for i, mass_stopping_power in enumerate(df['Stopping_power']):
    current_energy = energy_list[i]

    # Check if current energy is 5 MeV or lower
    if current_energy <= cutoff:
        if i == len(df['Stopping_power']) - 1:
            break

        next_energy = energy_list[i + 1]
        diffenergy = next_energy - current_energy
        stopping_power = mass_stopping_power * density
        distance_travelled = diffenergy / stopping_power
        distance_arr.append(distance_travelled)

        # Append values to the data dictionary
        data['Energy'].append(current_energy)
        data['Mass_Stopping_Power'].append(mass_stopping_power)
        data['Stopping_Power'].append(stopping_power)
        data['Distance_Travelled'].append(distance_travelled)
        data['Filtered_Stopping_Power'].append(df['Stopping_power'].tolist()[i])

# Exclude initial points from the plot
total_distance_travelled = np.flip(np.cumsum(np.flip(distance_arr)))
data['Cumulative_Distance'] = total_distance_travelled
filtered_stopping_power = np.flip(np.cumsum(np.flip(data['Filtered_Stopping_Power'])))

# Calculate fluence values for both non-modified and modified cases
fluence_values_original = np.ones_like(total_distance_travelled)
fluence_values_modified = np.array([calculate_fluence(d) for d in total_distance_travelled])

# Plot the graph with both non-modified and modified fluence
plt.plot(total_distance_travelled[exclude_initial_points:], filtered_stopping_power[exclude_initial_points:] * fluence_values_original[exclude_initial_points:], 'b', label='Non-Modified Fluence')
plt.plot(total_distance_travelled[exclude_initial_points:], filtered_stopping_power[exclude_initial_points:] * fluence_values_modified[exclude_initial_points:], 'r', label='Modified Fluence')
plt.xlabel('Distance Travelled (cm)')
plt.ylabel('Stopping Power (MeV/cm)')
plt.title('Stopping Power vs Distance Travelled with Non-Modified and Modified Fluence')
plt.legend()
plt.show()
