import numpy as np
import matplotlib.pyplot as plt

def compute_p_success(P_noise, P_attacker, P_UE, alpha, delta_values, Ta, j_max):
    j_range = np.arange(0, j_max)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for delta in delta_values:
        P_noise_values = [P_noise]
        
        for i in range(1, j_max + 1):
            if (i - 2) % (Ta) == 0 and i > 1:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_attacker
            else:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_noise
            
            P_noise_values.append(P_next)
        
        P_S = [1 if P_UE > (P_noise_values[j] + delta) else 0 for j in range(j_max)]
        results_P_S[delta] = P_S

        P_noise_j1 = [P_noise_values[j] for j in range(j_max)]
        results_P_noise_j1[delta] = P_noise_j1
    
    return j_range, results_P_S, results_P_noise_j1

# Given parameters
P_noise = 17.4  # dB
P_attacker = 55  # dB
P_UE = 54  # dB
alpha = 0.12
delta_values = [18,12,6,0]
Ta = 1
j_max = 42

# Compute results
j_range, results_P_S, results_P_noise_j1 = compute_p_success(P_noise, P_attacker, P_UE, alpha, delta_values, Ta, j_max)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for delta, P_S in results_P_S.items():
    plt.plot(j_range, P_S, label=f'delta = {delta}')

plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different delta Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for delta, P_noise_j1 in results_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, label=f'delta = {delta}')
plt.axhline(P_UE - delta_values[0], color='blue', ls='dotted', label=f'P_UE - {delta_values[0]}')
plt.axhline(P_UE - delta_values[1], color='orange', ls='dotted', label=f'P_UE - {delta_values[1]}')
plt.axhline(P_UE - delta_values[2], color='green', ls='dotted', label=f'P_UE - {delta_values[2]}')
plt.axhline(P_UE - delta_values[3], color='red', ls='dotted', label=f'P_UE - {delta_values[3]}')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different delta Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
