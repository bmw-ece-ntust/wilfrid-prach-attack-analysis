##
## Institution : National Taiwan Univeristy of Science and Technology
## Name : Wilfrid Azariah
## File Name : expe01_02.py
## Dependency : numpy, matplotlib
##
## Description:
## Basic attacker model that will calculate UE's msg1 received
## probability by gNB when attacker has j early start
## This code change the gnb noise updater (alpha) while keeping
## T_a = 1 and delta = 12
##
## This program also contain the data from real OAI gNB setup
## and plot it on the same figure as the math model
###############################################################

import matplotlib.pyplot as plt
import numpy as np

##### Mathematical #####
def compute_p_success(P_noise, P_attacker, P_UE, alpha_values, delta, Ta, j_max):
    j_range = np.arange(0, j_max + 1)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for alpha in alpha_values:
        P_noise_values = [P_noise]
        
        for i in range(1, j_max + 1):
            if (i - 1) % (Ta) == 0 and i > 0:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_attacker
            else:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_noise
            
            P_noise_values.append(P_next)
        
        P_S = [1 if P_UE > (P_noise_values[j] + delta) else 0 for j in range(j_max + 1)]
        results_P_S[alpha] = P_S

        P_noise_j1 = [P_noise_values[j] for j in range(j_max + 1)]
        results_P_noise_j1[alpha] = P_noise_j1
    
    return j_range, results_P_S, results_P_noise_j1

##### Experiment #####
# Data from the markdown table (with None values replaced by np.nan for missing data)
frames = np.arange(16)  # frame indices (0 to 15)
# Manually adjusted data to ensure every column has 16 values
data_P_Noise = {
    0.24: [16.7, 25.4, 31.2, 36.1, 39.9, 42.2, 44.4, 45.8, 48, 48.8, 49.7, 49.9, 50.2, 50.5, 51.4, 51.7],
    0.12: [17.1, 21.26666667, 24.8, 27.76666667, 30.46666667, 32.73333333, 34.7, 36.23333333, 37.7, 39.83333333, 40.93333333, 42, 42.96666667, 43.6, 44.5, 45.66666667],
    0.06: [16.5, 18.5, 20.2, 21.9, 23.6, 25.1, 26.5, 27.6, 29.1, 30.3, 31.4, 32.4, 33.4, 34.3, 35.2, 36],
    0: [16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8, 16.8]
}
data_P_S = {
    0.24: [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    0.12: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    0.06: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    0: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

##### Main Program #####
# Given parameters
P_noise = 16.88 # dB
P_attacker = 51  # dB
P_UE = 56.4  # dB
alpha_values = [0.24,0.12,0.06,0]
delta = 12
Ta = 1
j_max = 15

# Compute results
j_range, math_P_S, math_P_noise_j1 = compute_p_success(P_noise, P_attacker, P_UE, alpha_values, delta, Ta, j_max)


# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for alpha, P_S in math_P_S.items():
    plt.plot(j_range, P_S, label=f'$\\alpha$ = {alpha}')
for col in data_P_S:
    if (col == 0.24):
        plt.plot(frames, data_P_S[col], linestyle='none', color='blue', label=f'$\\alpha$ = {alpha} (Expe)', marker='o')
    if (col == 0.12):
        plt.plot(frames, data_P_S[col], linestyle='none', color='orange', label=f'$\\alpha$ = {alpha} (Expe)', marker='o')
    if (col == 0.06):
        plt.plot(frames, data_P_S[col], linestyle='none', color='green', label=f'$\\alpha$ = {alpha} (Expe)', marker='o')
    if (col == 0):
        plt.plot(frames, data_P_S[col], linestyle='none', color='red', label=f'$\\alpha$ = {alpha} (Expe)', marker='o')

plt.xlabel("$j$ (Attacker No. of RAO Early Start)")
plt.xticks(np.arange(0, 16, 2))
plt.ylabel("$P_{S,j}$ (UE Msg1 Success Probability at j)")
plt.title("$P_{S,j}$ vs $j$ for Different $\\alpha$ Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for alpha, P_noise_j1 in math_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, label=f'$\\alpha$ = {alpha}')
for col in data_P_Noise:
    if (col == 0.24):
        plt.plot(frames, data_P_Noise[col], linestyle='none', color='blue', label=f'$\\alpha$ = {col} (Expe)', marker='o')
    if (col == 0.12):
        plt.plot(frames, data_P_Noise[col], linestyle='none', color='orange', label=f'$\\alpha$ = {col} (Expe)', marker='o')
    if (col == 0.06):
        plt.plot(frames, data_P_Noise[col], linestyle='none', color='green', label=f'$\\alpha$ = {col} (Expe)', marker='o')
    if (col == 0):
        plt.plot(frames, data_P_Noise[col], linestyle='none', color='red', label=f'$\\alpha$ = {col} (Expe)', marker='o')

plt.axhline((P_UE - delta), color='purple', ls='dotted', label="$P_{UE} - \delta$")
plt.xlabel("$j$ (Attacker No. of RAO Early Start)")
plt.xticks(np.arange(0, 16, 2))
plt.ylabel("$P_{th,j}$ (gNB's Noise Threshold at j)")
plt.title("$P_{th,j}$ vs $j$ for Different $\\alpha$ Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
