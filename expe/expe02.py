import numpy as np
import matplotlib.pyplot as plt

# Define the given parameters
P_UE = 910  # UE's Msg3 dB Power (constant)
P_attacker_values = np.linspace(860, 1020, 100)  # Range of P_attacker from 860 to 1020 (100 points)

# Define the sigmoid function P_S based on the equation
def calculate_P_S(P_attacker, P_UE):
    return 1 / (1 + np.exp(P_attacker - P_UE))

# Calculate P_S for each value of P_attacker
P_S_values = calculate_P_S(P_attacker_values, P_UE)

# Data points (provided)
data_X = np.array([1016.571429, 1009.142857, 998.1428571, 987.8571429, 980.7142857, 973.5714286, 
                   965.8571429, 954.5714286, 950.8, 940.8, 938.75, 933, 923, 913.3016484, 
                   905.6109105, 897.9201727, 890.2294349, 882.538697, 874.8479592, 867.1572214])
data_Y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.285714286, 0.714285714, 
                   1, 1, 1, 1, 1])

# Display the results
print("P_attacker | P_S")
for P_attacker, P_S in zip(P_attacker_values, P_S_values):
    print(f"{P_attacker:.2f}    | {P_S:.4f}")

# Plotting the sigmoid curve and the data points
plt.plot(P_attacker_values, P_S_values, label=r"$P_S = \frac{1}{1+e^{(P_{attacker} - P_{UE})}}$", color='b')  # Sigmoid curve
plt.scatter(data_X, data_Y, color='r', label="Data Points", marker='o')  # Data points as red markers

# Labels and title
plt.xlabel(r"$P_{attacker}$ (dB)")
plt.ylabel(r"$P_S$")
plt.title("Sigmoid Output $P_S$ vs Attacker's Power $P_{attacker}$ with Data Points")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
