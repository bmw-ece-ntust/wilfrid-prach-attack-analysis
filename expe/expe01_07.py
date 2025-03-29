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
    24: [16.7, 20.8, 24.2, 27.5, 30, 32.4, 35.5, 37.3, 39.5, 40.9, 42, 43.1, 45.1, 46.7, 46.9, 47.9],
    12: [17.1, 21.26666667, 24.8, 27.76666667, 30.46666667, 32.73333333, 34.7, 36.23333333, 37.7, 39.83333333, 40.93333333, 42, 42.96666667, 43.6, 44.5, 45.66666667],
    6: [17, 21.3, 24.3, 27.6, 30.5, 32.4, 34.6, 36.6, 38, 39.7, 40.7, 41.8, 42.8, 43.8, 44.6, 45.2],
    0: [19.3, 19.3, 23.6, 27.36, 30.7, 33.64, 36.22, 38.48, 40.48, 42.22, 43.8, 45.14, 46.36, 47.36, 48.22, 49.02, 49.72, 50.34, 50.92, 51.44, 51.84, 52.28, 52.6, 52.9, 53.14, 53.34, 53.52, 53.7, 53.78, 53.86, 53.96, 54.08, 54.2, 54.3, 54.4, 54.5, 54.58, 54.64, 54.6, 54.66, 54.7, 54.72]
}
data_P_S = {
    24: [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    12: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    6: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
    if (delta != 0):
        plt.plot(j_range, P_S, label=f'delta = {delta}')
for col in data_P_S:
    if (col == 24):
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
    if (delta != 0):
        plt.plot(j_range, P_noise_j1, label=f'delta = {delta}')
for col in data_P_Noise:
    if (col == 24):
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
#plt.axhline(P_UE - delta_values[3], color='red', ls='dotted', label=f'P_UE - {delta_values[3]}')
plt.xlabel("j (RAO Early Start)")
plt.xticks(np.arange(0, 16, 2))
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different delta Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
