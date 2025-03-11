import numpy as np
import matplotlib.pyplot as plt

class UE:
    def __init__(self, power_tx, distance, gain):
        self.power_tx = power_tx  # UE Msg1 power transmitted
        self.distance = distance  # Distance from gNB
        self.gain = gain  # Antenna gain

    def received_power(self, gNB_gain, wavelength, path_loss_exp):
        return self.power_tx * self.gain * gNB_gain * (wavelength / (4 * np.pi))**2 * (1 / self.distance)**path_loss_exp

    def check_success(self, noise_threshold):
        return 1 if self.received_power(1, 1, 4 * np.pi) > noise_threshold else 0

class Attacker:
    def __init__(self, power_tx, distance, gain, beta):
        self.power_tx = power_tx  # Attacker Msg1-like power transmitted
        self.distance = distance  # Distance from gNB
        self.gain = gain  # Antenna gain
        self.beta = beta  # Attack periodicity

    def received_power(self, gNB_gain, wavelength, path_loss_exp):
        return self.power_tx * self.gain * gNB_gain * (wavelength / (4 * np.pi))**2 * (1 / self.distance)**path_loss_exp
    
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

def simulate(j_max, P_noise, P_UE_TX, P_attacker_TX, alpha, beta_values, d_UE, d_attacker, G_UE, G_attacker, G_gNB, wavelength, path_loss_exp):
    j_range = np.arange(1, j_max + 1)
    results_P_S = {}
    results_P_noise_j1 = {}
    
    for beta in beta_values:
        ue = UE(P_UE_TX, d_UE, G_UE)
        attacker = Attacker(P_attacker_TX, d_attacker, G_attacker, beta)
        gnb = gNB(P_noise, alpha)
        
        P_noise_values = [P_noise]
        P_S_values = []
        
        P_UE = ue.received_power(G_gNB, wavelength, path_loss_exp)
        P_attacker = attacker.received_power(G_gNB, wavelength, path_loss_exp)
        
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
P_UE_TX = 54  # dB
P_attacker_TX = 55  # dB
alpha = 0.1
beta_values = [1, 0.5, 0.25, 0.125]
j_max = 110
d_UE = 1
d_attacker = 1
G_UE = 1
G_attacker = 1
G_gNB = 1
wavelength = 1
path_loss_exp = 4 * np.pi

# Run simulation
j_range, results_P_S, results_P_noise_j1 = simulate(j_max, P_noise, P_UE_TX, P_attacker_TX, alpha, beta_values, d_UE, d_attacker, G_UE, G_attacker, G_gNB, wavelength, path_loss_exp)

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

plt.axhline(P_UE_TX, color='red', ls='dotted')
plt.xlabel("j (RAO Early Start)")
plt.ylabel("P_noise_j1 (gNB's Noise Threshold at j+1)")
plt.title("gNB's Noise Threshold at j+1 vs j for Different β Values (Simulation)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
