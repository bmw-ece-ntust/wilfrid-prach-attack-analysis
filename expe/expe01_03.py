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
            if (i - 2) % (Ta) == 0 and i > 1:
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
frames = np.arange(42)  # frame indices (0 to 41)
# Manually adjusted data to ensure every column has 42 values
data = {
    18: [],
    12: [],
    6: [],
    0: []
}

##### Main Program #####
# Given parameters
P_noise = 18.4  # dB
P_attacker = 55  # dB
P_UE = 54  # dB
alpha_values = [0.18,0.12,0.06,0]
delta = 12
Ta = 1
j_max = 41

# Compute results
j_range, math_P_S, math_P_noise_j1 = compute_p_success(P_noise, P_attacker, P_UE, alpha_values, delta, Ta, j_max)


# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for alpha, P_S in math_P_S.items():
    plt.plot(j_range, P_S, label=f'alpha = {alpha}')

plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different alpha Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for alpha, P_noise_j1 in math_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, label=f'alpha = {alpha}')
for col in data:
    plt.plot(frames, data[col], linestyle='none', label=f'alpha = {col} (Expe)', marker='o')

plt.axhline((P_UE - delta), color='red', ls='dotted', label=f'P_UE - delta')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different alpha Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
