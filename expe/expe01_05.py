##
## Institution : National Taiwan Univeristy of Science and Technology
## Name : Wilfrid Azariah
## File Name : expe01.py
## Dependency : numpy, matplotlib
##
## Description:
## Basic attacker model that will calculate UE's msg1 received
## probability by gNB when attacker has j early start
## This code change the attacker periode while keeping
## alpha = 0.12 and delta = 12
##
## This program also contain the data from real OAI gNB setup
## and plot it on the same figure as the math model
###############################################################

import matplotlib.pyplot as plt
import numpy as np

##### Mathematical #####
def compute_p_success(P_noise, P_attacker, P_UE, alpha, delta, Ta_values, j_max):
    j_range = np.arange(0, j_max + 1)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for Ta in Ta_values:
        P_noise_values = [P_noise]
        
        for i in range(1, j_max + 1):
            if (i - 2) % (Ta) == 0 and i > 0:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_attacker
            else:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_noise
            
            P_noise_values.append(P_next)
        
        P_S = [1 if P_UE > (P_noise_values[j] + delta) else 0 for j in range(j_max + 1)]
        results_P_S[Ta] = P_S

        P_noise_j1 = [P_noise_values[j] for j in range(j_max + 1)]
        results_P_noise_j1[Ta] = P_noise_j1
    
    return j_range, results_P_S, results_P_noise_j1

##### Experiment #####
# Data from the markdown table (with None values replaced by np.nan for missing data)
frames = np.arange(20)  # frame indices (0 to 19)
# Manually adjusted data to ensure every column has 20 values
data_P_noise = {
    1: [17.1, 21.26666667, 24.8, 27.76666667, 30.46666667, 32.73333333, 34.7, 36.23333333, 37.7, 39.83333333, 40.93333333, 42, 42.96666667, 43.6, 44.5, 45.66666667, 46.56666667, 46.93333333, 47.3, 47.6],
    2: [17.2, 18.02, np.nan, 21.98, np.nan, 24.96, np.nan, 27.34, np.nan, 29.16, np.nan, 30.56, np.nan, 31.62, np.nan, 32.46, np.nan, 33.16, np.nan, 33.64, np.nan, 34.06, np.nan, 34.36, np.nan, 34.62, np.nan, 34.72, np.nan, 34.82, np.nan, 34.88, np.nan, 34.94, np.nan, 34.96, np.nan, 35, np.nan, 35.02, np.nan, 35.08],
    4: [17.38, 17.82, np.nan, np.nan, np.nan, 20.88, np.nan, np.nan, np.nan, 22.58, np.nan, np.nan, np.nan, 23.72, np.nan, np.nan, np.nan, 24.5, np.nan, np.nan, np.nan, 24.8, np.nan, np.nan, np.nan, 25, np.nan, np.nan, np.nan, 25.06, np.nan, np.nan, np.nan, 25.2, np.nan, np.nan, np.nan, 25.18, np.nan, np.nan, np.nan, 25.36],
    8: [17.38, 18.1, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.54, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.42, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.52, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.54, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.52]
}
data_P_S = {
    1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    2: [17.2, 18.02, np.nan, 21.98, np.nan, 24.96, np.nan, 27.34, np.nan, 29.16, np.nan, 30.56, np.nan, 31.62, np.nan, 32.46, np.nan, 33.16, np.nan, 33.64, np.nan, 34.06, np.nan, 34.36, np.nan, 34.62, np.nan, 34.72, np.nan, 34.82, np.nan, 34.88, np.nan, 34.94, np.nan, 34.96, np.nan, 35, np.nan, 35.02, np.nan, 35.08],
    4: [17.38, 17.82, np.nan, np.nan, np.nan, 20.88, np.nan, np.nan, np.nan, 22.58, np.nan, np.nan, np.nan, 23.72, np.nan, np.nan, np.nan, 24.5, np.nan, np.nan, np.nan, 24.8, np.nan, np.nan, np.nan, 25, np.nan, np.nan, np.nan, 25.06, np.nan, np.nan, np.nan, 25.2, np.nan, np.nan, np.nan, 25.18, np.nan, np.nan, np.nan, 25.36],
    8: [17.38, 18.1, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.54, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.42, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.52, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.54, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.52]
}


##### Main Program #####
# Given parameters
P_noise = 17.1  # dB
P_attacker = 51  # dB
P_UE = 56.4  # dB
alpha = 0.12
delta = 12
Ta_values = [1, 2, 4, 8]
j_max = 19

# Compute results
j_range, math_P_S, math_P_noise_j1 = compute_p_success(P_noise, P_attacker, P_UE, alpha, delta, Ta_values, j_max)


# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for Ta, P_S in math_P_S.items():
    if (Ta == 1):
        plt.plot(j_range, P_S, label=f'Ta = {Ta}')

plt.xlabel("j (RAO Early Start)")
plt.xticks(np.arange(0, 19, 2))
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different Ta Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for Ta, P_noise_j1 in math_P_noise_j1.items():
    if (Ta == 1):
        plt.plot(j_range, P_noise_j1, label=f'Ta = {Ta}')
for col in data:
    if (col == 1):
        plt.plot(frames, data[col], linestyle='none', color='blue', label=f'Ta = {col} (Expe)', marker='o')
    #if (col == 2):
        #plt.plot(frames, data[col], linestyle='none', color='orange', label=f'Ta = {col} (Expe)', marker='o')
    #if (col == 4):
        #plt.plot(frames, data[col], linestyle='none', color='green', label=f'Ta = {col} (Expe)', marker='o')
    #if (col == 8):
        #plt.plot(frames, data[col], linestyle='none', color='red', label=f'Ta = {col} (Expe)', marker='o')

plt.axhline((P_UE - delta), color='purple', ls='dotted', label=f'P_UE - delta')
plt.xlabel("j (RAO Early Start)")
plt.xticks(np.arange(0, 19, 2))
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different Ta Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
