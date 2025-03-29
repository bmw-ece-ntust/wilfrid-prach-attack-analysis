##
## Institution : National Taiwan Univeristy of Science and Technology
## Name : Wilfrid Azariah
## File Name : model01_02.py
## Dependency : numpy, matplotlib
##
## Description:
## Basic attacker model that will calculate UE's msg1 received
## probability by gNB when attacker has j early start
## This code change the gnb noise updater (alpha) while keeping
## T_a = 1 and delta = 12
###############################################################

import numpy as np
import matplotlib.pyplot as plt

def compute_p_success(P_noise, P_attacker, P_UE, alpha_values, delta, Ta, j_max):
    j_range = np.arange(0, j_max+1)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for alpha in alpha_values:
        P_noise_values = [P_noise]
        
        for i in range(1, j_max + 1):
            if (i - 1) % (Ta) == 0 and i > 1:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_attacker
            else:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_noise
            
            P_noise_values.append(P_next)
        
        P_S = [1 if P_UE > (P_noise_values[j] + delta) else 0 for j in range(j_max+1)]
        results_P_S[alpha] = P_S

        P_noise_j1 = [P_noise_values[j] for j in range(j_max+1)]
        results_P_noise_j1[alpha] = P_noise_j1
    
    return j_range, results_P_S, results_P_noise_j1

# Given parameters
P_noise = 17.1  # dB
P_attacker = 51  # dB
P_UE = 56.4  # dB
alpha_values = [0.24,0.12,0.06,0]
delta = 12
Ta = 1
j_max = 15

# Compute results
j_range, results_P_S, results_P_noise_j1 = compute_p_success(P_noise, P_attacker, P_UE, alpha_values, delta, Ta, j_max)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for alpha, P_S in results_P_S.items():
    plt.plot(j_range, P_S, label=f'alpha = {alpha}')

plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different alpha Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for alpha, P_noise_j1 in results_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, label=f'alpha = {alpha}')

plt.axhline(P_UE - delta, color='red', ls='dotted', label=f'P_UE - delta')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different alpha Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
