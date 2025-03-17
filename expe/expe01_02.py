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
            if (i - 2) % (Ta) == 0 and i > 1:
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
frames = np.arange(42)  # frame indices (0 to 41)
# Manually adjusted data to ensure every column has 42 values
data = {
    0.18: [19.16, 19.16, 25.64, 31, 35.38, 39, 41.94, 44.36, 46.38, 47.98, 49.26, 50.38, 51.24, 52.02, 52.62, 53.06, 53.48, 53.84, 54.12, 54.28, 54.48, 54.66, 54.78, 54.86, 54.94, 54.98, 55.04, 55.1, 55.12, 55.16, 55.22, 55.22, 55.18, 55.24, 55.26, 55.24, 55.28, 55.28, 55.3, 55.3, 55.32, 55.36],
    0.12: [17.78, 17.78, 22.3, 26.28, 29.8, 32.86, 35.56, 37.92, 39.94, 41.74, 43.36, 44.78, 46.02, 47.34, 48.2, 48.96, 49.74, 50.38, 50.96, 51.54, 51.98, 52.38, 52.66, 52.96, 53.32, 53.54, 53.72, 53.86, 54.02, 54.16, 54.26, 54.36, 54.46, 54.52, 54.58, 54.64, 54.68, 54.7, 54.76, 54.76, 54.72, 54.72],
    0.06: [18.38, 18.38, 20.54, 22.54, 24.4, 26.18, 27.88, 29.46, 30.96, 32.36, 33.64, 34.82, 36, 37.1, 38.1, 39.1, 40, 40.9, 41.68, 42.48, 43.18, 43.86, 44.46, 45.04, 45.64, 46.14, 46.62, 47.1, 47.54, 47.9, 48.28, 48.64, 49.02, 49.3, 49.6, 49.88, 50.18, 50.42, 50.62, 50.82, 51.02, 51.22],
    0: [18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4, 18.4]
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
plt.title("UE Msg1 Success Probability vs j for Different Ta Values")
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
plt.title("gNB's Noise Threshold at j+1 vs j for Different Ta Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
