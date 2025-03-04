
```

2. Expected value of the number of preambles that have at least 2 UEs and/or attacker's Msg1 for the $i^{th}$ SSB
```math
N_{C,i} = N_i - (K_i + 1) e^{-(K_i + 1)/N_1} - N_i e^{-(K_i + 1)/N_i}
```

3. $N_{S,i}$ should be transformed to $\hat{N}_{S,i}$ according to whether attacker's Msg1 is inside $N_{S,i}$ or $N_{C,i}$
```math
\hat{N}_{S,i} =
\begin{cases} 
N, & \text{if } K_i > 0 \\ 
0, & \text{otherwise} 
\end{cases}
```
