import numpy as np
import matplotlib.pyplot as plt

# Define the given parameters
P_UE = 900  # UE's Msg3 dB Power (constant)
P_attacker_values = np.linspace(860, 1020, 100)  # Range of P_attacker from 860 to 1020 (100 points)

# Define the sigmoid function P_S based on the equation
def calculate_P_S(P_attacker, P_UE):
    return 1 / (1 + np.exp(P_attacker - P_UE))

# Calculate P_S for each value of P_attacker
P_S_values = calculate_P_S(P_attacker_values, P_UE)

# Display the results
print("P_attacker | P_S")
for P_attacker, P_S in zip(P_attacker_values, P_S_values):
    print(f"{P_attacker:.2f}    | {P_S:.4f}")

# Plotting the results for better visualization
plt.plot(P_attacker_values, P_S_values, label=r"$P_S = \frac{1}{1+e^{(P_{attacker} - P_{UE})}}$", color='b')
plt.xlabel(r"$P_{attacker}$ (dB)")
plt.ylabel(r"$P_S$")
plt.title("Sigmoid Output $P_S$ vs Attacker's Power $P_{attacker}$")
plt.grid(True)
plt.legend()
plt.show()
