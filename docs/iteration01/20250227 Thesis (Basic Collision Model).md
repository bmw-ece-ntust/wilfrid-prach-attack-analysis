# 20250227 Thesis (Basic Collision Model)

###### tags: `2025`

**Goal:**
- [x] Write Basic Collision Model for Analysis of PRACH Attack on Network Energy Saving

**References:**
- Modeling Random Access with Capture and Power Control for IEEE 802.11be Systems
- [Modeling and Estimation of One-Shot Random Access for Finite-User Multichannel Slotted ALOHA Systems](https://ieeexplore.ieee.org/document/6211364)

**Table of Contents:**
- [20250227 Thesis (Basic Collision Model)](#20250227-thesis--basic-collision-model-)
          + [tags: `2025`](#tags---2025-)
  * [1. Define UE and PRACH parameters](#1-define-ue-and-prach-parameters)
    + [1.1. System Model](#11-system-model)
    + [1.2. 5G PRACH](#12-5g-prach)
    + [1.3. PRACH parameters](#13-prach-parameters)
  * [2. Model Collision Probability in PRACH by Approximation](#2-model-collision-probability-in-prach-by-approximation)
    + [2.1. Model Parameters](#21-model-parameters)
    + [2.2. Equation](#22-equation)
  * [3. Model Implementation in Python Code](#3-model-implementation-in-python-code)
    + [3.1. Code based on original Paper](#31-code-based-on-original-paper)
      - [3.1.1. Parameters](#311-parameters)
      - [3.1.2. Code](#312-code)
      - [3.1.3. Result](#313-result)
    + [3.2. Modify Code to Imitate ZX's Result](#32-modify-code-to-imitate-zxs-result)
      - [3.2.1. Parameters](#321-parameters)
      - [3.2.2. Code](#322-code)
      - [3.2.3. Result](#323-result)
  * [4. Add Msg1 and Channel Noise Energy](#4-add-msg1-and-channel-noise-energy)
    + [4.1. Model Parameters](#41-model-parameters)
    + [4.2. Equation](#42-equation)
    + [4.3. Modify Code to Add Msg1 and Channel Noise Energy](#43-modify-code-to-add-msg1-and-channel-noise-energy)
      - [4.3.1. Parameters](#431-parameters)
      - [4.3.2. Code](#432-code)
      - [4.3.3. Result](#433-result)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 1. Define UE and PRACH parameters

### 1.1. System Model

```mermaid
flowchart TD
    A[BaseStation with N preambles per SSB]
    B(UE 1)
    C(UE 2)
    D(...)
	E(UE M)
    B-->A
    C-->A
    D-->A
	E-->A
```

### 1.2. 5G PRACH

```mermaid
sequenceDiagram
    gNB->>UE:SSB/PBCH<br/>System Information
	UE->>gNB: PRACH<br/>Random Access Preamble (Msg1)
    gNB->>UE: PDCCH<br/>Donwlink Control Information
    gNB->>UE: PDSCH<br/>Randon Access Response (Msg2)
    UE->>gNB: PUSCH<br/>RRC Connection Setup Request (Msg3)
    gNB->>UE: PDCCH<br/>Donwlink Control Information
    gNB->>UE: PDSCH<br/>RRC Connection Setup (Msg4)
```

### 1.3. PRACH parameters

| Category | Parameter                                                                                                 | Value                            |
| -------- | --------------------------------------------------------------------------------------------------------- | -------------------------------- |
| UE RA    | ra-ResponseWindow<hr>ra-ContentionResolutionTimer                                                         | 10ms<hr>64ms                     |
| gNB RO   | ssb-PositionsInBurst<hr>prach-ConfigurationIndex<hr>msg1-FDM<hr>ssb-perRACH-OccasionAndCB-PreamblesPerSSB | 1 SSB<hr>159<hr>1 RO<hr>OneAnd60 |

## 2. Model Collision Probability in PRACH by Approximation

### 2.1. Model Parameters

| Parameter | Description                                                                                                     |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| $M$       | number of UEs sending Msg1                                                                                      |
| $N_i$     | number of Preambles per SSB for the $i^{th}$ SSB                                                                |
| $N_{C,i}$ | expected value of the preambles that have at least 2 UEs' Msg1                                                  |
| $N_{S,i}$ | expected value of the preambles that have only 1 UE's Msg1                                                      |
| $K_i$     | Average number of UEs that transmit Msg1 in the $i^{th}$ SSB. Initially, $K_1 = M$                              |
| $P_S$     | probability of successfull Msg1 complete reception by gNB within maximum number of SSB $I_{max}$                |
| $P_C$     | ratio between the number of collided preamble and the overall number of preamble in the period of $I_{max}$ SSB |

### 2.2. Equation

1. Expected value of the number of preambles that have only 1 UE's Msg1 for the first SSB
```math
N_{S,1} = M e^{-M/N_1}
```

2. Expected value of the number of preambles that have at least 2 UEs' Msg1 for the first SSB
```math
N_{C,1} = N_1 - M e^{-M/N_1} - N_1 e^{-M/N_1}
```

3. Expected value of successfull preamble per SSB
```math
N_{S,i} = K_i e^{-K_i/N_i}
```

4. Average number of UEs that transmit Msg1 in the $i^{th}$ SSB. Initially, $K_1 = M$
```math
K_{i+1} = K_i - N_{S,i} = K_i ( 1 - e^{-K_i/N_i})
```

5. Access success probability, $P_S$, = probability of successfull Msg1 complete reception by gNB within maximum number of SSB $I_{max}$
```math
P_S = \sum_{i=1}^{I_{\text{max}}} \frac{N_{S,i}}{M}
```

6. Collision probability, $P_C$ , = ratio between the number of collided preamble and the overall number of preamble in the period of $I_{max}$ SSB
```math
P_C = \frac{\sum_{i=1}^{I_{\text{max}}} N_{C,i}}{\sum_{i=1}^{I_{\text{max}}} N_i}
```

7. Mean access delay, $T_a$, = delay for each Msg1 reception process between the UE's first Msg1 attempt and the success reception of the UE's Msg1 in gNB
```math
T_a = \left( \sum_{i=1}^{I_{\text{max}}} i \times N_{S,i} \right) / \sum_{i=1}^{I_{\text{max}}} N_{S,i}
```

## 3. Model Implementation in Python Code

### 3.1. Code based on original Paper

#### 3.1.1. Parameters

| Parameter | Value |
| --------- | ----- |
| $M$       | 100   |
| $N$       | 5~45  |
| $I_{max}$ | 10    |


#### 3.1.2. Code

```python
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
```

#### 3.1.3. Result

![image](https://hackmd.io/_uploads/ryH4LyVjJl.png)

![image](https://hackmd.io/_uploads/r1GSLyNskg.png)

![image](https://hackmd.io/_uploads/ByxULkNiJl.png)


### 3.2. Modify Code to Imitate ZX's Result

#### 3.2.1. Parameters

| Parameter | Value                       | Reference                                            |
| --------- | --------------------------- | ---------------------------------------------------- |
| $M$       | 2                           | Experiment uses MTK and Samsung UE                   |
| $N$       | 60                          | ssb-perRACH-OccasionAndCB-PreamblesPerSSB = OneAnd60 |
| $I_{max}$ | 185 (MTK) and 155 (Samsung) | -                                                    |

![image](https://hackmd.io/_uploads/rk7p3kVsyg.png)


#### 3.2.2. Code

```python=
import numpy as np
import matplotlib.pyplot as plt

def compute_PC_PS_TA(M=2, I_max=155, N=60):
    P_C = 0
    P_S = 0
    T_A = 0
    N_S_i_list = []
    N_C_i_list = []
    K_i_list = []
    i_list = []
    
    K_i = M  # Initially, all UEs attempt Msg1
    N_C_total = 0
    N_S_total = 0
    N_total = 0
    weighted_sum_TA = 0
    
    for i in range(1, I_max + 1):
        i_list.append(i)
        K_i_list.append(K_i)
        N_S_i = K_i * np.exp(-K_i / N)  # Expected successful preambles
        N_C_i = N - N_S_i - (N * np.exp(-K_i / N))  # Collided preambles
        		
        N_S_i_list.append(N_S_i)
        N_C_i_list.append(N_C_i)
		
        N_S_total += N_S_i
        N_C_total += N_C_i
        N_total += N
        weighted_sum_TA += i * N_S_i  # Weighted sum for Ta calculation
        
        K_i = K_i - N_S_i  # Remaining UEs after success
    
    P_C = N_C_total / N_total  # Collision probability
    P_S = N_S_total / M  # Access success probability
    T_A = weighted_sum_TA / N_S_total if N_S_total > 0 else 0  # Average access delay
    
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
```

#### 3.2.3. Result

$P_C$ = 0

![image](https://hackmd.io/_uploads/B1AX3XEoJx.png)

![image](https://hackmd.io/_uploads/rJ1BhQVjke.png)

![image](https://hackmd.io/_uploads/HksHnXVj1g.png)

## 4. Add Msg1 and Channel Noise Energy

### 4.1. Model Parameters

| Parameter | Description                                                                                                     |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| $M$       | number of UEs sending Msg1                                                                                      |
| $N$     | total number of Preambles per SSB                                                                |
| $N_i$     | number of Preambles per SSB for the $i^{th}$ SSB                                                                |
| $N_{C,i}$ | expected value of the preambles that have at least 2 UEs' Msg1                                                  |
| $N_{S,i}$ | expected value of the preambles that have only 1 UE's Msg1                                                      |
| $K_i$     | Average number of UEs that transmit Msg1 in the $i^{th}$ SSB. Initially, $K_1 = M$                              |
| $P_S$     | probability of successfull Msg1 complete reception by gNB within maximum number of SSB $I_{max}$                |
| $P_C$     | ratio between the number of collided preamble and the overall number of preamble in the period of $I_{max}$ SSB |
| $P_{noise,i}$     | gNB noise power threshold for the $i^{th}$ SSB |
| $P_{msg1,i}$     | UEs' power received on the gNB for the $i^{th}$ SSB |

### 4.2. Equation

0. All equations from [2.2](#22-equation) are still used

1. gNB will calculate current channel noise = 0.9 x last channel noise + 0.1 msg signal power
```math
P_{noise,i+1} = 0.9 * P_{noise,i} + P_{msg1,i}
```

2. $P_{msg1,i}$ for all UEs are constant 55dB if they havent got success
```math
P_{msg1,i} =
\begin{cases} 
50, & \text{if } P_{msg1,i} > P_{noise,i} \\ 
0, & \text{otherwise} 
\end{cases}
```

3. $N_i$ depends if $P_{msg1,i}$ > P_{noise,i}
```math
N_i =
\begin{cases} 
N, & \text{if } K_i > 0 \\ 
0, & \text{otherwise} 
\end{cases}
```

### 4.3. Modify Code to Add Msg1 and Channel Noise Energy

#### 4.3.1. Parameters

| Parameter | Value                       | Reference                                            |
| --------- | --------------------------- | ---------------------------------------------------- |
| $M$       | 2                           | Experiment uses MTK and Samsung UE                   |
| $N$       | 60                          | ssb-perRACH-OccasionAndCB-PreamblesPerSSB = OneAnd60 |
| $I_{max}$ | 185 (MTK) and 155 (Samsung) | -                                                    |
| $P_{noise,1}$ | 25 | -                                                    |

![image](https://hackmd.io/_uploads/rk7p3kVsyg.png)


#### 4.3.2. Code

```python
import numpy as np
import matplotlib.pyplot as plt

def compute_PC_PS_TA(M=2, I_max=155, N=60):
    P_C = 0
    P_S = 0
    T_A = 0
    N_i = 0
    N_S_i_list = []
    N_C_i_list = []
    K_i_list = []
    i_list = []
    
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
        i_list.append(i)
        K_i_list.append(K_i)
        N_S_i = K_i * np.exp(-K_i / N_i)  # Expected successful preambles
        N_C_i = N_i - N_S_i - (N_i * np.exp(-K_i / N_i))  # Collided preambles
		
        N_S_i_list.append(N_S_i)
        N_C_i_list.append(N_C_i)
        
        N_S_total += N_S_i
        N_C_total += N_C_i
        N_total += N_i
        weighted_sum_TA += i * N_S_i  # Weighted sum for Ta calculation
        
        K_i = K_i - N_S_i  # Remaining UEs after success
        
        if (K_i <= 0):
            P_msg1_i = 0
        
        P_noise_i = 0.9 * P_noise_i + 0.1 * P_msg1_i
    
    P_C = N_C_total / N_total  # Collision probability
    P_S = N_S_total / M  # Access success probability
    T_A = weighted_sum_TA / N_S_total if N_S_total > 0 else 0  # Average access delay
    
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

```

#### 4.3.3. Result

$P_C$ = 0

![image](https://hackmd.io/_uploads/HkJ497Ejyx.png)

![image](https://hackmd.io/_uploads/Hka4qQNsyx.png)

![image](https://hackmd.io/_uploads/r1ASc7Ni1x.png)
