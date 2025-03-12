import numpy as np
import matplotlib.pyplot as plt

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

# Given parameters
P_noise = 28  # dB
P_attacker = 55  # dB
P_UE = 54  # dB
alpha = 0.1
beta_values = [1, 0.5, 0.25, 0.125]
j_max = 1000

# Run simulation
j_range, results_P_S, results_P_noise_j1 = simulate(j_max, P_noise, P_attacker, P_UE, alpha, beta_values)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
for beta, P_S in results_P_S.items():
    plt.plot(j_range, P_S, label=f'β = {beta}')

plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_S (Msg1 Success Probability)")
plt.title("UE Msg1 Success Probability vs j for Different β Values (Simulation)")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for beta, P_noise_j1 in results_P_noise_j1.items():
    plt.plot(j_range, P_noise_j1, label=f'β = {beta}')

plt.axhline(P_UE, color='red', ls='dotted')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different β Values (Simulation)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
