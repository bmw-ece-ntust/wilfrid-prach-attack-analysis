##
## Institution : National Taiwan Univeristy of Science and Technology
## Name : Wilfrid Azariah
## File Name : expe01_03.py
## Dependency : numpy, matplotlib
##
## Description:
## Basic attacker model that will calculate UE's msg1 received
## probability by gNB when attacker has j early start
## This code change the gnb noise to msg1 threshold while keeping
## alpha = 0.12 and T_a = 1
##
## This program also contain the data from real OAI gNB setup
## and plot it on the same figure as the math model
###############################################################

import matplotlib.pyplot as plt
import numpy as np

##### Mathematical #####
def compute_p_success(P_noise, P_attacker, P_UE, alpha, delta_values, Ta, j_max):
    j_range = np.arange(0, j_max + 1)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for delta in delta_values:
        P_noise_values = [P_noise]
        
        for i in range(1, j_max + 1):
            if (i - 1) % (Ta) == 0 and i > 0:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_attacker
            else:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_noise
            
            P_noise_values.append(P_next)
        
        P_S = [1 if P_UE > (P_noise_values[j] + delta) else 0 for j in range(j_max + 1)]
        results_P_S[delta] = P_S

        P_noise_j1 = [P_noise_values[j] for j in range(j_max + 1)]
        results_P_noise_j1[delta] = P_noise_j1
    
    return j_range, results_P_S, results_P_noise_j1

##### Experiment #####
# Data from the markdown table (with None values replaced by np.nan for missing data)
frames = np.arange(16)  # frame indices (0 to 15)
# Manually adjusted data to ensure every column has 16 values
data_P_Noise = {
    24: [19.24, 19.24, 23.6, 27.4, 30.72, 33.66, 36.28, 38.46, 40.5, 42.3, 43.8, 45.16, 46.4, 47.42, 48.34, 49.14, 49.98, 50.6, 51.14, 51.6, 52.04, 52.42, 52.72, 53.04, 53.26, 53.46, 53.72, 53.86, 53.98, 54.12, 54.2, 54.26, 54.4, 54.5, 54.58, 54.62, 54.68, 54.74, 54.76, 54.82, 54.86, 54.9],
    12: [17.78, 17.78, 22.3, 26.28, 29.8, 32.86, 35.56, 37.92, 39.94, 41.74, 43.36, 44.78, 46.02, 47.34, 48.2, 48.96, 49.74, 50.38, 50.96, 51.54, 51.98, 52.38, 52.66, 52.96, 53.32, 53.54, 53.72, 53.86, 54.02, 54.16, 54.26, 54.36, 54.46, 54.52, 54.58, 54.64, 54.68, 54.7, 54.76, 54.76, 54.72, 54.72],
    6: [19.34, 19.34, 23.64, 26.52, 30, 33, 35.68, 38.04, 40.12, 41.88, 43.44, 44.8, 46.04, 47.14, 48.1, 48.94, 49.64, 50.28, 50.8, 51.32, 51.76, 52.16, 52.5, 52.84, 53.12, 53.34, 53.58, 53.74, 53.88, 54, 54.12, 54.22, 54.36, 54.46, 54.56, 54.62, 54.64, 54.66, 54.64, 54.68, 54.68, 54.62],
    0: [19.3, 19.3, 23.6, 27.36, 30.7, 33.64, 36.22, 38.48, 40.48, 42.22, 43.8, 45.14, 46.36, 47.36, 48.22, 49.02, 49.72, 50.34, 50.92, 51.44, 51.84, 52.28, 52.6, 52.9, 53.14, 53.34, 53.52, 53.7, 53.78, 53.86, 53.96, 54.08, 54.2, 54.3, 54.4, 54.5, 54.58, 54.64, 54.6, 54.66, 54.7, 54.72]
}
data_P_S = {
    24: [19.24, 19.24, 23.6, 27.4, 30.72, 33.66, 36.28, 38.46, 40.5, 42.3, 43.8, 45.16, 46.4, 47.42, 48.34, 49.14, 49.98, 50.6, 51.14, 51.6, 52.04, 52.42, 52.72, 53.04, 53.26, 53.46, 53.72, 53.86, 53.98, 54.12, 54.2, 54.26, 54.4, 54.5, 54.58, 54.62, 54.68, 54.74, 54.76, 54.82, 54.86, 54.9],
    12: [17.78, 17.78, 22.3, 26.28, 29.8, 32.86, 35.56, 37.92, 39.94, 41.74, 43.36, 44.78, 46.02, 47.34, 48.2, 48.96, 49.74, 50.38, 50.96, 51.54, 51.98, 52.38, 52.66, 52.96, 53.32, 53.54, 53.72, 53.86, 54.02, 54.16, 54.26, 54.36, 54.46, 54.52, 54.58, 54.64, 54.68, 54.7, 54.76, 54.76, 54.72, 54.72],
    6: [19.34, 19.34, 23.64, 26.52, 30, 33, 35.68, 38.04, 40.12, 41.88, 43.44, 44.8, 46.04, 47.14, 48.1, 48.94, 49.64, 50.28, 50.8, 51.32, 51.76, 52.16, 52.5, 52.84, 53.12, 53.34, 53.58, 53.74, 53.88, 54, 54.12, 54.22, 54.36, 54.46, 54.56, 54.62, 54.64, 54.66, 54.64, 54.68, 54.68, 54.62],
    0: [19.3, 19.3, 23.6, 27.36, 30.7, 33.64, 36.22, 38.48, 40.48, 42.22, 43.8, 45.14, 46.36, 47.36, 48.22, 49.02, 49.72, 50.34, 50.92, 51.44, 51.84, 52.28, 52.6, 52.9, 53.14, 53.34, 53.52, 53.7, 53.78, 53.86, 53.96, 54.08, 54.2, 54.3, 54.4, 54.5, 54.58, 54.64, 54.6, 54.66, 54.7, 54.72]
}


##### Main Program #####
# Given parameters
P_noise = 16.88  # dB
P_attacker = 51  # dB
P_UE = 54  # dB
alpha = 0.12
delta_values = [18, 12, 6, 0]
Ta = 1
j_max = 15

# Compute results
j_range, math_P_S, math_P_noise_j1 = compute_p_success(P_noise, P_attacker, P_UE, alpha, delta_values, Ta, j_max)


# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for delta, P_S in math_P_S.items():
    plt.plot(j_range, P_S, label=f'delta = {delta}')
for col in data_P_S:
    if (col == 18):
        plt.plot(frames, data_P_S[col], linestyle='none', color='blue', label=f'delta = {delta} (Expe)', marker='o')
    if (col == 12):
        plt.plot(frames, data_P_S[col], linestyle='none', color='orange', label=f'delta = {delta} (Expe)', marker='o')
    if (col == 6):
        plt.plot(frames, data_P_S[col], linestyle='none', color='green', label=f'delta = {delta} (Expe)', marker='o')
    #if (col == 0):
        #plt.plot(frames, data_P_S[col], linestyle='none', color='red', label=f'delta = {delta} (Expe)', marker='o')
        
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.xticks(np.arange(0, 16, 2))
plt.title("UE Msg1 Success Probability vs j for Different delta Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for delta, P_noise_j1 in math_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, label=f'delta = {delta}')
for col in data_P_Noise:
    if (col == 18):
        plt.plot(frames, data_P_Noise[col], linestyle='none', color='blue', label=f'delta = {col} (Expe)', marker='o')
    if (col == 12):
        plt.plot(frames, data_P_Noise[col], linestyle='none', color='orange', label=f'delta = {col} (Expe)', marker='o')
    if (col == 6):
        plt.plot(frames, data_P_Noise[col], linestyle='none', color='green', label=f'delta = {col} (Expe)', marker='o')
    #if (col == 0):
        #plt.plot(frames, data_P_Noise[col], linestyle='none', color='red', label=f'delta = {col} (Expe)', marker='o')

plt.axhline(P_UE - delta_values[0], color='blue', ls='dotted', label=f'P_UE - {delta_values[0]}')
plt.axhline(P_UE - delta_values[1], color='orange', ls='dotted', label=f'P_UE - {delta_values[1]}')
plt.axhline(P_UE - delta_values[2], color='green', ls='dotted', label=f'P_UE - {delta_values[2]}')
plt.axhline(P_UE - delta_values[3], color='red', ls='dotted', label=f'P_UE - {delta_values[3]}')
plt.xlabel("j (RAO Early Start)")
plt.xticks(np.arange(0, 16, 2))
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different delta Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
