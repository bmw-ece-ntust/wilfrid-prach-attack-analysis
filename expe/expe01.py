import matplotlib.pyplot as plt
import numpy as np

# Data from the markdown table
frames = np.arange(42)  # frame indices (0 to 41)
data = {
    1: [17.22, 17.82, 22.3, 26.2, 29.72, 32.78, 35.48, 37.86, 39.92, 41.68, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64],
    2: [17.2, 18.02, None, 21.98, None, 24.96, None, 27.34, None, 29.16, None, 30.56, None, 31.62, None, 32.46, None, 33.16, None, 33.64, None, 34.06, None, 34.36, None, 34.62, None, 34.72, None, 34.82, None, 34.88, None, 34.94, None, 34.96, None, 35, None, 35.02, None, 35.08],
    4: [17.38, 17.82, None, None, None, 20.88, None, None, None, 22.58, None, None, None, 23.72, None, None, None, 24.5, None, None, None, 24.8, None, None, None, 25, None, None, None, 25.06, None, None, None, 25.2, None, None, None, 25.18, None, None, None, 25.36],
    8: [17.38, 18.1, None, None, None, None, None, None, None, 18.54, None, None, None, None, None, None, None, 18.42, None, None, None, None, None, None, None, 18.52, None, None, None, None, None, None, None, 18.54, None, None, None, 18.52]
}

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot data for each column (1, 2, 4, 8)
for col in data:
    plt.plot(frames, data[col], label=f'Column {col}', marker='o')

# Add labels and title
plt.xlabel('Frame')
plt.ylabel('Value')
plt.title('Graph of Frame vs Values for Columns 1, 2, 4, 8')
plt.legend()

# Show grid for better readability
plt.grid(True)

# Show the plot
plt.show()
