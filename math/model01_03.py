import numpy as np
import matplotlib.pyplot as plt

def compute_p_success(P_noise, P_attacker, P_UE, alpha, delta_max, Ta, j_values):
    delta_range = np.arange(0, delta_max)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for j in j_values:
        P_noise_values = [P_noise]
        
        for i in range(1, j + 1):
            if (i - 2) % (Ta) == 0 and i > 1:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_attacker
            else:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_noise
            
            P_noise_values.append(P_next)
        
        P_S = [1 if P_UE > (P_noise_values[j] + delta) else 0 for j in range(j_max)]
        results_P_S[Ta] = P_S

        P_noise_j1 = [P_noise_values[j] for j in range(j_max)]
        results_P_noise_j1[Ta] = P_noise_j1
    
    return j_range, results_P_S, results_P_noise_j1

# Given parameters
P_noise = 17.4  # dB
P_attacker = 55  # dB
P_UE = 54  # dB
alpha = 0.12
delta = 12
Ta_values = [1, 2, 4, 8]
j_max = 42

# Compute results
j_range, results_P_S, results_P_noise_j1 = compute_p_success(P_noise, P_attacker, P_UE, alpha, delta, Ta_values, j_max)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for Ta, P_S in results_P_S.items():
    plt.plot(j_range, P_S, label=f'Ta = {Ta}')

plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different Ta Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for Ta, P_noise_j1 in results_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, label=f'Ta = {Ta}')

plt.axhline(P_UE - delta, color='red', ls='dotted', label=f'P_UE - delta')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different Ta Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
