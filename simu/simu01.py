import numpy as np
import matplotlib.pyplot as plt

##### Mathematical #####
def compute_p_success(P_noise, P_attacker, P_UE, alpha, beta_values, j_max):
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

##### Simulation #####
class UE:
    def __init__(self, power):
        self.power = power  # UE Msg1 power

    def check_success(self, noise_threshold):
        return 1 if self.power > noise_threshold else 0

class Attacker:
    def __init__(self, power, beta):
        self.power = power  # Attacker Msg1-like power
        self.beta = beta  # Attack periodicity
    
    def is_active(self, rao):
        return (rao - 2) % (1 / self.beta) == 0 and rao > 1

class gNB:
    def __init__(self, initial_noise, alpha):
        self.noise = initial_noise  # Initial noise threshold
        self.alpha = alpha  # Noise update factor
    
    def update_noise(self, attacker_active, attacker_power, base_noise):
        if attacker_active:
            self.noise = (1 - self.alpha) * self.noise + self.alpha * attacker_power
        else:
            self.noise = (1 - self.alpha) * self.noise + self.alpha * base_noise
        return self.noise

def simulate(j_max, P_noise, P_attacker, P_UE, alpha, beta_values):
    j_range = np.arange(1, j_max + 1)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for beta in beta_values:
        ue = UE(P_UE)
        attacker = Attacker(P_attacker, beta)
        gnb = gNB(P_noise, alpha)
        
        P_noise_values = [P_noise]
        P_S_values = []
        
        for j in range(j_max):
            attacker_active = attacker.is_active(j+1)
            noise_level = gnb.update_noise(attacker_active, P_attacker, P_noise)
            P_noise_values.append(noise_level)
            P_S_values.append(ue.check_success(noise_level))
        
        results_P_S[beta] = P_S_values
        results_P_noise_j1[beta] = P_noise_values[:j_max]
    
    return j_range, results_P_S, results_P_noise_j1

##### Main Program #####
# Given parameters
P_noise = 28  # dB
P_attacker = 55  # dB
P_UE = 54  # dB
alpha = 0.1
beta_values = [1, 0.5, 0.25, 0.125]
j_max = 110

# Compute results
j_range, math_P_S, math_P_noise_j1 = compute_p_success(P_noise, P_attacker, P_UE, alpha, beta_values, j_max)

# Run simulation
j_range, simu_P_S, simu_P_noise_j1 = simulate(j_max, P_noise, P_attacker, P_UE, alpha, beta_values)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for beta, P_S in math_P_S.items():
    plt.plot(j_range, P_S, linestyle='-', label=f'β = {beta}')
for beta, P_S in simu_P_S.items():
    plt.plot(j_range, P_S, linestyle='none', marker='.', label=f'β = {beta} sim')

plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different β Values (Simulation)")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for beta, P_noise_j1 in math_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, linestyle='-', label=f'β = {beta}')
for beta, P_noise_j1 in simu_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, linestyle='none', marker='.', label=f'β = {beta} sim')

plt.axhline(P_UE, color='red', ls='dotted')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different β Values (Simulation)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
