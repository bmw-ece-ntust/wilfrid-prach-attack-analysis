import numpy as np
import matplotlib.pyplot as plt

def compute_PC_PS_TA(M=100, I_max=10, N_values=range(5, 46)):
    P_C_list = []
    P_S_list = []
    T_A_list = []
    
    for N in N_values:
        K_i = M  # Initially, all UEs attempt Msg1
        N_C_total = 0
        N_S_total = 0
        N_total = 0
        weighted_sum_TA = 0
        
        for i in range(1, I_max + 1):
            N_S_i = K_i * np.exp(-K_i / N)  # Expected successful preambles
            N_C_i = N - N_S_i - (N * np.exp(-K_i / N))  # Collided preambles
            
            N_S_total += N_S_i
            N_C_total += N_C_i
            N_total += N
            weighted_sum_TA += i * N_S_i  # Weighted sum for Ta calculation
            
            K_i = K_i - N_S_i  # Remaining UEs after success
        
        P_C = N_C_total / N_total  # Collision probability
        P_S = N_S_total / M  # Access success probability
        T_A = weighted_sum_TA / N_S_total if N_S_total > 0 else 0  # Average access delay
        
        P_C_list.append(P_C)
        P_S_list.append(P_S)
        T_A_list.append(T_A)
    
    return N_values, P_C_list, P_S_list, T_A_list

# Compute values
N_values, P_C_list, P_S_list, T_A_list = compute_PC_PS_TA()

# Plot PC graph
plt.figure(figsize=(18, 5))
plt.subplot(1, 3, 1)
plt.plot(N_values, P_C_list, marker='o', linestyle='-', color='r', label='P_C')
plt.xlabel('Number of Preambles (N)')
plt.ylabel('Collision Probability (P_C)')
plt.title('Collision Probability vs Number of Preambles')
plt.ylim(0, 1)
plt.grid(True)
plt.legend()

# Plot PS graph
plt.subplot(1, 3, 2)
plt.plot(N_values, P_S_list, marker='s', linestyle='-', color='b', label='P_S')
plt.xlabel('Number of Preambles (N)')
plt.ylabel('Access Success Probability (P_S)')
plt.title('Access Success Probability vs Number of Preambles')
plt.ylim(0, 1)
plt.grid(True)
plt.legend()

# Plot TA graph
plt.subplot(1, 3, 3)
plt.plot(N_values, T_A_list, marker='^', linestyle='-', color='g', label='T_A')
plt.xlabel('Number of Preambles (N)')
plt.ylabel('Average Access Delay (T_A)')
plt.title('Average Access Delay vs Number of Preambles')
plt.ylim(0, 10)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
