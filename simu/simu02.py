import numpy as np
import matplotlib.pyplot as plt

def compute_PC_PS_TA(M=2, I_max=155, N=60, num_simulations=int(1e4)):
    P_C = 0
    P_S = 0
    T_A = 0
    N_i = 0
    N_S_i_list = []
    N_C_i_list = []
    K_i_list = []
    i_list = []
    
    total_collisions = 0
    total_successes = 0
    total_attempts = 0
    total_T_A = 0
    
    for i in range(1, I_max + 1):
        i_list.append(i)
        K_i_list.append(0)
        N_S_i_list.append(0)
        N_C_i_list.append(0)
    
    for i_simulations in range(num_simulations):
        print("i_simulations = " + str(i_simulations) + "\n") 
        K_i = M  # Initially, all UEs attempt Msg1
        P_msg1_i = 50
        P_noise_i = 25
        N_C_total = 0
        N_S_total = 0
        N_total = 0
        weighted_sum_TA = 0
        
        for i in range(1, I_max + 1):
            if (P_msg1_i > P_noise_i):
                N_i = N
            else:
                N_i = 0.000000001
            K_i_list[i-1] = K_i_list[i-1] + K_i
            preamble_choices = np.random.randint(0, N, K_i)  # Each UE picks a preamble randomly
            unique, counts = np.unique(preamble_choices, return_counts=True)
            successful_preambles = (counts == 1).sum()
            collided_preambles = (counts > 1).sum()
            
            N_S_i = successful_preambles
            N_C_i = collided_preambles
            
            N_S_i_list[i-1] = N_S_i_list[i-1] + N_S_i
            N_C_i_list[i-1] = N_C_i_list[i-1] + N_C_i
            
            N_S_total += N_S_i
            N_C_total += N_C_i
            N_total += N
            weighted_sum_TA += i * N_S_i  # Weighted sum for Ta calculation
            
            K_i -= N_S_i  # Remaining UEs after success
            
            if (K_i <= 0):
                P_msg1_i = 0
        
            P_noise_i = 0.9 * P_noise_i + 0.1 * P_msg1_i
            
            if K_i <= 0:
                break  # All UEs successfully sent Msg1
        
        total_collisions += N_C_total
        total_successes += N_S_total
        total_attempts += N_total
        if N_S_total > 0:
            total_T_A += weighted_sum_TA / N_S_total
    
    P_C = total_collisions / total_attempts  # Collision probability
    P_S = total_successes / (M * num_simulations)  # Access success probability
    T_A = total_T_A / num_simulations if total_successes > 0 else 0  # Average access delay
    
    K_i_list[:] = [x / num_simulations for x in K_i_list]
    N_S_i_list[:] = [x / num_simulations for x in N_S_i_list]
    N_C_i_list[:] = [x / num_simulations for x in N_C_i_list]
    
    return N, P_C, P_S, T_A, K_i_list, i_list, N_S_i_list, N_C_i_list

# Compute values
N, P_C, P_S, T_A, K_i_list, i_list, N_S_i_list, N_C_i_list = compute_PC_PS_TA()

print("P_C = " + str(P_C) + "\n")

# Plot Ki graph
plt.figure(figsize=(18, 5))
plt.subplot(1, 3, 1)
plt.plot(i_list, K_i_list, marker='o', linestyle='-', color='r', label='K_i')
plt.xlabel('Number of Slots (i)')
plt.ylabel('Remaining UEs (K_i)')
plt.title('Remaining UEs vs Number of Slots')
plt.ylim(0, 5)
plt.grid(True)
plt.legend()

# Plot NSi graph
plt.subplot(1, 3, 2)
plt.plot(i_list, N_S_i_list, marker='o', linestyle='-', color='b', label='N_S_i')
plt.xlabel('Number of Slots (i)')
plt.ylabel('Expected successful preambles (N_S_i)')
plt.title('Expected successful preambles vs Number of Slots')
plt.ylim(0, 5)
plt.grid(True)
plt.legend()

# Plot NCi graph
plt.subplot(1, 3, 3)
plt.plot(i_list, N_C_i_list, marker='o', linestyle='-', color='g', label='N_C_i')
plt.xlabel('Number of Slots (i)')
plt.ylabel('Collided preambles (N_C_i)')
plt.title('Collided preambles vs Number of Slots')
plt.ylim(0, 5)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
