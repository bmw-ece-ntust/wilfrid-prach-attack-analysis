import matplotlib.pyplot as plt
import numpy as np

# Data from the markdown table (with None values replaced by np.nan for missing data)
frames = np.arange(42)  # frame indices (0 to 41)
data = {
    1: [17.22, 17.82, 22.3, 26.2, 29.72, 32.78, 35.48, 37.86, 39.92, 41.68, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64, 42.64],
    2: [17.2, 18.02, np.nan, 21.98, np.nan, 24.96, np.nan, 27.34, np.nan, 29.16, np.nan, 30.56, np.nan, 31.62, np.nan, 32.46, np.nan, 33.16, np.nan, 33.64, np.nan, 34.06, np.nan, 34.36, np.nan, 34.62, np.nan, 34.72, np.nan, 34.82, np.nan, 34.88, np.nan, 34.94, np.nan, 34.96, np.nan, 35, np.nan, 35.02, np.nan, 35.08],
    4: [17.38, 17.82, np.nan, np.nan, np.nan, 20.88, np.nan, np.nan, np.nan, 22.58, np.nan, np.nan, np.nan, 23.72, np.nan, np.nan, np.nan, 24.5, np.nan, np.nan, np.nan, 24.8, np.nan, np.nan, np.nan, 25, np.nan, np.nan, np.nan, 25.06, np.nan, np.nan, np.nan, 25.2, np.nan, np.nan, np.nan, 25.18, np.nan, np.nan, np.nan, 25.36],
    8: [17.38, 18.1, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.54, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.42, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.52, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.54, np.nan, np.nan, np.nan, 18.52]
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
