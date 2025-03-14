# 20250307 Thesis (PRACH Attack Problem Definition)

###### tags: `2025`

**Goal:**
- [x] Map the PRACH Attack Problem
- [x] Define the PRACH Attack Problem that I want to focus on
- [ ] Define the input and output of the problem

**References:**
- [5G/NR - Initial Access/RACH](https://www.sharetechnote.com/html/5G/5G_RACH.html)
- [Techniques and Impact Evaluation of RACH Jamming in 5G network](https://etheses.lib.ntust.edu.tw/thesis/detail/64057b454c8e6e7e11cfd2812c8fecf7/)
- [20250307 Thesis (Random Access Procedure and Attack)](https://github.com/bmw-ece-ntust/wilfrid-prach-attack-analysis/blob/master/docs/20250307%20Thesis%20(Random%20Access%20Procedure%20and%20Attack).md)

**Table of Contents:**
- [20250307 Thesis (PRACH Attack Problem Definition)](#20250307-thesis--prach-attack-problem-definition-)
          + [tags: `2025`](#tags---2025-)
  * [1. Map of PRACH Attack Problem](#1-map-of-prach-attack-problem)
  * [2. PRACH Attack Problem to focus on](#2-prach-attack-problem-to-focus-on)
  * [3. Input and Output of the PRACH Attack Problem](#3-input-and-output-of-the-prach-attack-problem)
    + [3.1. Attack Msg1](#31-attack-msg1)
      - [3.1.1. Assumptions or Constant Input Parameter](#311-assumptions-or-constant-input-parameter)
      - [3.1.2. Variable Input Parameter](#312-variable-input-parameter)
      - [3.1.3. Output Parameter or Performance Metrics](#313-output-parameter-or-performance-metrics)
      - [3.1.4. Possible Extension](#314-possible-extension)
    + [3.2. Attack Msg3](#32-attack-msg3)
      - [3.2.1. Assumptions or Constant Input Parameter](#321-assumptions-or-constant-input-parameter)
      - [3.2.2. Variable Input Parameter](#322-variable-input-parameter)
      - [3.2.3. Output Parameter or Performance Metrics](#323-output-parameter-or-performance-metrics)
      - [3.2.4. Possible Extension](#324-possible-extension)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 1. Map of PRACH Attack Problem

**Legend:**
- Different Color = Available Data from ZhongXin's Thesis
- Line to Dot = Planned problem focus

```mermaid
stateDiagram-v2
    classDef zhongXinCase fill:#fdd

    s1: PRACH Attack
    s2: Attack Msg1
    s3: Attack Msg3
    s4: Attack Msg1 and Msg3 Together
    s1 --> s2
    s1 --> s3
    s1 --> s4
    s5: Attack Msg1<br>with noise threshold
    s6: Attack Msg1<br>without noise threshold
    s2 --> s5
    s2 --> s6
    s7: Attack Msg3<br>with variable UE power
    s8: Attack Msg3<br>without variable UE power
    s3 --> s7
    s3 --> s8
    s9: Attack Msg1<br>with noise threshold<br>with 1 UE
    s10: Attack Msg1<br>with noise threshold<br>with multi UE
    s11: Attack Msg1<br>without noise threshold<br>with 1 UE
    s12: Attack Msg1<br>without noise threshold<br>with multi UE
    s5 --> s9
    s5 --> s10
    s6 --> s11
    s6 --> s12
    s13: Attack Msg3<br>with variable UE power<br>with 1 UE
    s14: Attack Msg3<br>with variable UE power<br>with multi UE
    s15: Attack Msg3<br>without variable UE power<br>with 1 UE
    s16: Attack Msg3<br>without variable UE power<br>with multi UE
    s7 --> s13
    s7 --> s14
    s8 --> s15
    s8 --> s16
    s17: Attack Msg1<br>with noise threshold<br>with 1 UE<br>with attacker start early
    s18: Attack Msg1<br>with noise threshold<br>with 1 UE<br>without attacker start early
    s19: Attack Msg1<br>with noise threshold<br>with multi UE<br>with attacker start early
    s20: Attack Msg1<br>with noise threshold<br>with multi UE<br>without attacker start early
    s21: Attack Msg1<br>without noise threshold<br>with 1 UE<br>with attacker start early
    s22: Attack Msg1<br>without noise threshold<br>with 1 UE<br>without attacker start early
    s23: Attack Msg1<br>without noise threshold<br>with multi UE<br>with attacker start early
    s24: Attack Msg1<br>without noise threshold<br>with multi UE<br>without attacker start early
    s9 --> s17
    s9 --> s18
    s10 --> s19
    s10 --> s20
    s11 --> s21
    s11 --> s22
    s12 --> s23
    s12 --> s24
    s25: Attack Msg1<br>with noise threshold<br>with 1 UE<br>with attacker start early<br>with varying attack period
    s26: Attack Msg1<br>with noise threshold<br>with 1 UE<br>with attacker start early<br>without varying attack period
    s27: Attack Msg1<br>with noise threshold<br>with 1 UE<br>without attacker start early<br>with varying attack period
    s28: Attack Msg1<br>with noise threshold<br>with 1 UE<br>without attacker start early<br>without varying attack period
    s29: Attack Msg1<br>with noise threshold<br>with multi UE<br>with attacker start early<br>with varying attack period
    s30: Attack Msg1<br>with noise threshold<br>with multi UE<br>with attacker start early<br>without varying attack period
    s31: Attack Msg1<br>with noise threshold<br>with multi UE<br>without attacker start early<br>with varying attack period
    s32: Attack Msg1<br>with noise threshold<br>with multi UE<br>without attacker start early<br>without varying attack period
    s33: Attack Msg1<br>without noise threshold<br>with 1 UE<br>with attacker start early<br>with varying attack period
    s34: Attack Msg1<br>without noise threshold<br>with 1 UE<br>with attacker start early<br>without varying attack period
    s35: Attack Msg1<br>without noise threshold<br>with 1 UE<br>without attacker start early<br>with varying attack period
    s36: Attack Msg1<br>without noise threshold<br>with 1 UE<br>without attacker start early<br>without varying attack period
    s37: Attack Msg1<br>without noise threshold<br>with multi UE<br>with attacker start early<br>with varying attack period
    s38: Attack Msg1<br>without noise threshold<br>with multi UE<br>with attacker start early<br>without varying attack period
    s39: Attack Msg1<br>without noise threshold<br>with multi UE<br>without attacker start early<br>with varying attack period
    s40: Attack Msg1<br>without noise threshold<br>with multi UE<br>without attacker start early<br>without varying attack period
    s17 --> s25
    s17 --> s26
    s18 --> s27
    s18 --> s28
    s19 --> s29
    s19 --> s30
    s20 --> s31
    s20 --> s32
    s21 --> s33
    s21 --> s34
    s22 --> s35
    s22 --> s36
    s23 --> s37
    s23 --> s38
    s24 --> s39
    s24 --> s40

    s25 --> [*]
    s26 --> [*]
    s27 --> [*]
    s28 --> [*]
    s33 --> [*]
    s34 --> [*]
    s35 --> [*]
    s36 --> [*]
    s13 --> [*]
    s15 --> [*]

    class s25,s26,s13,s15 zhongXinCase
```


## 2. PRACH Attack Problem to focus on

**Available Data from ZhongXin's Thesis:**
- Attack Msg1 and Msg3 seperately:
    - Attack Msg1:
        - with noise threshold
        - with 1 UE
        - with attacker start early
            - without varying attack period (1)
            - with varying attack period (2)
    - Attack Msg3:
        - with 1 UE
            - without variable UE power (3)
            - with variable UE power (4)

**Planned problem focus:**
```mermaid
stateDiagram-v2
    classDef zhongXinCase fill:#fdd

    s1: Zhong Xin Case
    
    s13: Attack Msg3<br>with variable UE power<br>with 1 UE
    s15: Attack Msg3<br>without variable UE power<br>with 1 UE

    s25: Attack Msg1<br>with noise threshold<br>with 1 UE<br>with attacker start early<br>with varying attack period
    s26: Attack Msg1<br>with noise threshold<br>with 1 UE<br>with attacker start early<br>without varying attack period
    s27: Attack Msg1<br>with noise threshold<br>with 1 UE<br>*without attacker start early*<br>with varying attack period
    s28: Attack Msg1<br>with noise threshold<br>with 1 UE<br>*without attacker start early*<br>without varying attack period

    s33: Attack Msg1<br>*without noise threshold*<br>with 1 UE<br>with attacker start early<br>with varying attack period
    s34: Attack Msg1<br>*without noise threshold*<br>with 1 UE<br>with attacker start early<br>without varying attack period
    s35: Attack Msg1<br>*without noise threshold*<br>with 1 UE<br>*without attacker start early*<br>with varying attack period
    s36: Attack Msg1<br>*without noise threshold*<br>with 1 UE<br>*without attacker start early*<br>without varying attack period

    s1 --> s26
    s1 --> s25
    s1 --> s15
    s1 --> s13

    s25 --> s27
    s25 --> s33
    s27 --> s35

    s26 --> s28
    s26 --> s34
    s28 --> s36

    class s1,s25,s26,s13,s15 zhongXinCase
```

## 3. Input and Output of the PRACH Attack Problem

### 3.1. Attack Msg1

#### 3.1.1. Assumptions or Constant Input Parameter

| Parameter      | Description                    | Constant Value |
| -------------- | ------------------------------ | -------------- |
| $M$            | Number of UE                   | 1              |
| $N$            | Number of Preamble ID          | 64             |
| $O$            | Number of Attacked Preamble ID | 1              |
| $P_{noise}$    | Initial Noise dB Threshold     | $x$            |
| $P_{attacker}$ | Attacker's Msg1 dB Power       | $x$            |
| $P_{UE}$       | UE's Msg1 dB Power             | $x$            |

#### 3.1.2. Variable Input Parameter

| Parameter | Description                                                                                         | Value Range    |
| --------- | --------------------------------------------------------------------------------------------------- | -------------- |
| $i$       | identifier for the ith Random Access Occasion                                                       | 0..∞ (integer) |
| $\alpha$  | Noise update factor parameter                                                                       | 0..1 (real)    |
| $j$       | Number of Random Access Occasion early start for attacker relative to UE                            | 0..∞ (integer) |
| $\beta$   | Variability/Percentage of Attack Period. This parameter is directly related to ssb-perRACH-Occasion | 0..1 (real)    |

#### 3.1.3. Output Parameter or Performance Metrics

| Parameter | Description                          | Value Range |
| --------- | ------------------------------------ | ----------- |
| $P_S$     | UE's Msg1 Access Success Probability | 0 or 1      |

```mermaid
flowchart LR
    inputC["`**Constant Input:**
    M
    N
    O
    P_noise
    P_attacker
    P_UE`"]
    inputV["`**Variable Input:**
    α
    j
    β`"]
    process["`**Msg1 Model**`"]
    output["`**Output:**
    P_S vs. j
    P_S vs. α
    P_S vs. β`"]
    inputC --> process
    inputV --> process
    process --> output
```
**Notes:**
1. Noise threshold:
```math
P_{noise,i+1} = (1 - \alpha) * P_{noise,i} + \alpha * P_{attacker}
```
2. UE's Msg1 Success with Noise threshold:
```math
P_{S,i} =
\begin{cases} 
1, & \text{if } P_{UE,i} > P_{noise,i} \\ 
0, & \text{otherwise} 
\end{cases}
```

#### 3.1.4. Possible Extension

| Parameter | Description                    | Value                                          |
| --------- | ------------------------------ | ---------------------------------------------- |
| $M$       | Number of UE                   | 1 = initial model<br>$x$ = extension           |
| $O$       | Number of Attacked Preamble ID | 1 = initial model<br>$x$ = extension (upto 64) |

### 3.2. Attack Msg3

#### 3.2.1. Assumptions or Constant Input Parameter

| Parameter      | Description                | Constant Value |
| -------------- | -------------------------- | -------------- |
| $M$            | Number of UE               | 1              |
| $N$            | Number of RAPID            | 1              |
| $O$            | Number of Attacked RAPID   | 1              |
| $P_{noise}$    | Initial Noise dB Threshold | $x$            |
| $P_{attacker}$ | Attacker's Msg3 dB Power   | $x$            |


#### 3.2.2. Variable Input Parameter

| Parameter | Description        | Value |
| --------- | ------------------ | ----- |
| $P_{UE}$  | UE's Msg3 dB Power | $x$   |


#### 3.2.3. Output Parameter or Performance Metrics

| Parameter | Description                          | Value          |
| --------- | ------------------------------------ | -------------- |
| $P_S$     | UE's Msg3 Access Success Probability | This is output |


```mermaid
flowchart LR
    inputC["`**Constant Input:**
    M
    O
    P_noise
    P_attacker`"]
    inputV["`**Variable Input:**
    P_UE`"]
    process["`**Msg3 Model**`"]
    output["`**Output:**
    P_S vs. P_UE`"]
    inputC --> process
    inputV --> process
    process --> output
```

#### 3.2.4. Possible Extension

| Parameter | Description              | Value                                           |
| --------- | ------------------------ | ----------------------------------------------- |
| $M$       | Number of UE             | 1 = initial model<br>$x$ = extension            |
| $N$       | Number of RAPID          | 1 = initial model<br>$x$ = extension (upto $M$) |
| $O$       | Number of Attacked RAPID | 1 = initial model<br>$x$ = extension (upto $N$) |

**Notes:**
1. Variable $N$ as an extension to accomodate possibility of 2 or more UE choosing the same RAPID due to collision in Msg1
