import numpy as np
import matplotlib.pyplot as plt

def compute_p_success(P_noise, P_attacker_TX, P_UE_TX, alpha, beta_values, j_max, G_gNB, G_UE, G_attacker, wavelength, gamma, d_UE, d_attacker):
    # Compute received power based on channel model
    P_UE = P_UE_TX * G_UE * G_gNB * (wavelength / (4 * np.pi))**2 * (1 / d_UE)**gamma
    P_attacker = P_attacker_TX * G_attacker * G_gNB * (wavelength / (4 * np.pi))**2 * (1 / d_attacker)**gamma
    
    j_range = np.arange(1, j_max + 1)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for beta in beta_values:
        P_noise_values = [P_noise]
        
        for i in range(1, j_max + 1):
            if (i - 2) % (1 / beta) == 0 and i > 1:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_attacker
            else:
                P_next = (1 - alpha) * P_noise_values[-1] + alpha * P_noise
            
            P_noise_values.append(P_next)
        
        P_S = [1 if P_UE > P_noise_values[j] else 0 for j in range(j_max)]
        results_P_S[beta] = P_S

        P_noise_j1 = [P_noise_values[j] for j in range(j_max)]
        results_P_noise_j1[beta] = P_noise_j1
    
    return j_range, results_P_S, results_P_noise_j1

# Given parameters
P_noise = 28  # dB
P_attacker_TX = 55  # dB
P_UE_TX = 54  # dB
alpha = 0.1
beta_values = [1, 0.5, 0.25, 0.125]
j_max = 110

# Channel model parameters
G_gNB = 1
G_UE = 1
G_attacker = 1
wavelength = 4 * np.pi
gamma = 1
d_UE = 1
d_attacker = 1

# Compute results
j_range, results_P_S, results_P_noise_j1 = compute_p_success(P_noise, P_attacker_TX, P_UE_TX, alpha, beta_values, j_max, G_gNB, G_UE, G_attacker, wavelength, gamma, d_UE, d_attacker)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for beta, P_S in results_P_S.items():
    plt.plot(j_range, P_S, label=f'β = {beta}')

plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different β Values")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for beta, P_noise_j1 in results_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, label=f'β = {beta}')

plt.axhline(P_UE_TX, color='red', ls='dotted')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different β Values")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
