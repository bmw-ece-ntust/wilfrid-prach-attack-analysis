##
## Institution : National Taiwan Univeristy of Science and Technology
## Name : Wilfrid Azariah
## File Name : expe01_04.py
## Dependency : numpy, matplotlib
##
## Description:
## Basic attacker model that will calculate UE's msg1 received
## probability by gNB when attacker has j early start
## 
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
            if (i - 2) % (Ta) == 0 and i > 1:
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
frames = np.arange(42)  # frame indices (0 to 41)
# Manually adjusted data to ensure every column has 42 values
data_1 = {
    1: [17.78,17.78, 22.3, 26.28, 29.8, 32.86, 35.56, 37.92, 39.94, 41.74, 43.36, 44.78, 46.02, 47.34, 48.2, 48.96, 49.74, 50.38, 50.96, 51.54, 51.98, 52.38, 52.66, 52.96, 53.32, 53.54, 53.72, 53.86, 54.02, 54.16, 54.26, 54.36, 54.46, 54.52, 54.58, 54.64, 54.68, 54.7, 54.76, 54.76, 54.72, 54.72],
    2: [17.2, 18.02, np.nan, 21.98, np.nan, 24.96, np.nan, 27.34, np.nan, 29.16, np.nan, 30.56, np.nan, 31.62, np.nan, 32.46, np.nan, 33.16, np.nan, 33.64, np.nan, 34.06, np.nan, 34.36, np.nan, 34.62, np.nan, 34.72, np.nan, 34.82, np.nan, 34.88, np.nan, 34.94, np.nan, 34.96, np.nan, 35, np.nan, 35.02, np.nan, 35.08],
    4: [17.38, 17.82, np.nan, np.nan, np.nan, 20.88, np.nan, np.nan, np.nan, 22.58, np.nan, np.nan, np.nan, 23.72, np.nan, np.nan, np.nan, 24.5, np.nan, np.nan, np.nan, 24.8, np.nan, np.nan, np.nan, 25, np.nan, np.nan, np.nan, 25.06, np.nan, np.nan, np.nan, 25.2, np.nan, np.nan, np.nan, 25.18, np.nan, np.nan, np.nan, 25.36],
    8: [17.38, 18.1, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.54, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.42, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.52, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.54, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 18.52]
}
# Manually adjusted data to ensure every column has 42 values
data_2 = {
    1: [18.46, 18.46, 20.06, 21.52, 22.82, 23.92, 24.9, 25.68, 26.42, 27.06, 27.62, 28.1, 28.5, 28.9, 29.26, 29.58, 29.84, 30.04, 30.24, 30.44, 30.56, 30.7, 30.84, 30.92, 31.02, 31.08, 31.18, 31.24, 31.28, 31.3, 31.36, 31.4, 31.38, 31.46, 31.46, 31.46, 31.44, 31.44, 31.42, 31.4, 31.44, 31.4]
}


##### Main Program #####
# Given parameters
P_noise = 17.8  # dB
P_attacker = 55  # dB
P_UE = 45  # dB
alpha = 0.12
delta = 12
Ta_values = [1, 2, 4, 8]
j_max = 41

# Compute results 1
j_range, math_P_S_1, math_P_noise_j1_1 = compute_p_success(P_noise, P_attacker, P_UE, alpha, delta, Ta_values, j_max)

# Slightly Change parameters
P_attacker = 31.4  # dB

# Compute results 2
j_range, math_P_S_2, math_P_noise_j1_2 = compute_p_success(P_noise, P_attacker, P_UE, alpha, delta, Ta_values, j_max)


# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for Ta, P_S in math_P_S_1.items():
    if (Ta == 2):
        plt.plot(j_range, P_S, label=f'Ta = {Ta}, Pattacker = 55')
for Ta, P_S in math_P_S_2.items():
    if (Ta == 1):
        plt.plot(j_range, P_S, label=f'Ta = {Ta}, Pattacker = 31.4')


plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different Ta,Pattacker Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for Ta, P_noise_j1 in math_P_noise_j1_1.items():
    if (Ta == 2):
        plt.plot(j_range, P_noise_j1, label=f'Ta = {Ta}, Pattacker = 55')
for Ta, P_noise_j1 in math_P_noise_j1_2.items():
    if (Ta == 1):
        plt.plot(j_range, P_noise_j1, label=f'Ta = {Ta}, Pattacker = 31.4')
for col in data_1:
    if (col == 2):
        plt.plot(frames, data_1[col], linestyle='none', color='blue', label=f'Ta = {col}, Pattacker = 55 (Expe)', marker='o')
for col in data_2:
    if (col == 1):
        plt.plot(frames, data_2[col], linestyle='none', color='orange', label=f'Ta = {col}, Pattacker = 31.4 (Expe)', marker='o')

plt.axhline((P_UE - delta), color='purple', ls='dotted', label=f'P_UE - delta')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different Ta,Pattacker Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
