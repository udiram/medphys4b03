import pandas as pd

# Read data from the CSV file
df = pd.read_csv('output.csv', header=0)

# Extract energy and stopping power columns
energy = df['Energy'].tolist()
stopping_power = df['Stopping_power'].tolist()

# Calculate distance for each energy level
distances = [energy[i] / stopping_power[i] for i in range(len(energy))]

# Calculate cumulative distance
cumulative_distance = 0
cumulative_distances = []

# Print the results
for i in range(len(energy)):
    cumulative_distance += distances[i]
    cumulative_distances.append(cumulative_distance)
    print(f"Energy: {energy[i]}, Stopping Power: {stopping_power[i]}, Distance: {distances[i]}, Cumulative Distance: {cumulative_distance}")

# Print cumulative distances separately
print("\nCumulative Distances:")
for i in range(len(energy)):
    print(f"Energy: {energy[i]}, Cumulative Distance: {cumulative_distances[i]}")
