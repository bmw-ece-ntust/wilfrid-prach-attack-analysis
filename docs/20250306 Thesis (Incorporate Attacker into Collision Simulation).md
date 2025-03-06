# 20250306 Thesis (Incorporate Attacker into Collision Simulation)

###### tags: `2025`

**Goal:**
- [x] Write Incorporate Attacker Collision Simulation for Analysis of PRACH Attack on Network Energy Saving

**References:**
- Modeling Random Access with Capture and Power Control for IEEE 802.11be Systems
- [Modeling and Estimation of One-Shot Random Access for Finite-User Multichannel Slotted ALOHA Systems](https://ieeexplore.ieee.org/document/6211364)
- [20250306 Thesis (Basic Collision Simulation)](https://github.com/bmw-ece-ntust/prach-attack-analysis/blob/master/docs/20250306%20Thesis%20(Basic%20Collision%20Simulation).md)
- [20250304 Thesis (Incorporate Attacker into Collision Model)](https://github.com/bmw-ece-ntust/prach-attack-analysis/blob/master/docs/20250304%20Thesis%20(Incorporate%20Attacker%20into%20Collision%20Model).md)

**Table of Contents:**
- [20250306 Thesis (Incorporate Attacker into Collision Simulation)](#20250306-thesis--incorporate-attacker-into-collision-simulation-)
          + [tags: `2025`](#tags---2025-)
  * [1. Add 1 Attacker for Msg1](#1-add-1-attacker-for-msg1)
    + [1.1. System Model](#11-system-model)
    + [1.2. 5G PRACH](#12-5g-prach)
    + [1.3. Notes and Assumptions](#13-notes-and-assumptions)
  * [2. Simulation Implementation in Python Code](#2-simulation-implementation-in-python-code)
    + [2.1. Parameters](#21-parameters)
    + [2.2. Code](#22-code)
    + [2.3.3. Result](#233-result)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## 1. Add 1 Attacker for Msg1

### 1.1. System Model

```mermaid
flowchart TD
    A[BaseStation]
    B[[Attacker]]
    C(UE 1)
    D(UE 2)
    E(...)
	F(UE M)
    B-->A
    C-->A
    D-->A
	E-->A
	F-->A
```

### 1.2. 5G PRACH

```mermaid
sequenceDiagram
    gNB->>UE:SSB/PBCH<br/>System Information
    gNB->>Attacker:SSB/PBCH<br/>System Information
    UE->>gNB: PRACH<br/>Random Access Preamble (Msg1)
    Attacker->>gNB: PRACH<br/>Random Access Preamble (Msg1)
```

### 1.3. Notes and Assumptions

1. Attacker send preamble to every RO
2. Fixed preamble index sent by the attacker

## 2. Simulation Implementation in Python Code

### 2.1. Parameters

| Parameter | Value                       | Reference                                            |
| --------- | --------------------------- | ---------------------------------------------------- |
| $M$       | 2                           | Experiment uses MTK and Samsung UE                   |
| $N$       | 60                          | ssb-perRACH-OccasionAndCB-PreamblesPerSSB = OneAnd60 |
| $I_{max}$ | 185 (MTK) and 155 (Samsung) | -                                                    |
| $P_{noise,1}$ | 25 | -                                                    |

### 2.2. Code

```python

```

### 2.3.3. Result

$P_C$ = 0

