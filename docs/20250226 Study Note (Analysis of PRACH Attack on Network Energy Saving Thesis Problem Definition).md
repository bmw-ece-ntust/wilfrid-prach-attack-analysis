# 20250226 Study Note (Analysis of PRACH Attack on Network Energy Saving Thesis Problem Definition)

###### tags: `2025`

**Goal:**
- [x] Write research proposal for [Analysis of PRACH Attack on Network Energy Saving](#1-analysis-of-prach-attack-on-network-energy-saving)

**References:**
- [Prof. Ray | Template for BMW Lab.](https://hackmd.io/@RayCheng/rJIuoWmB8)

**Table of Contents:**
- [20250226 Study Note (Analysis of PRACH Attack on Network Energy Saving Thesis Problem Definition)](#20250226-study-note--analysis-of-prach-attack-on-network-energy-saving-thesis-problem-definition-)
          + [tags: `2025`](#tags---2025-)
  * [1. Analysis of PRACH Attack on Network Energy Saving](#1-analysis-of-prach-attack-on-network-energy-saving)
    + [1.1. Abstract](#11-abstract)
    + [1.2. Research Objectives](#12-research-objectives)
    + [1.3. Methodology](#13-methodology)
    + [1.4. Expected Outcomes](#14-expected-outcomes)
    + [1.5. Significance of the Study](#15-significance-of-the-study)
    + [1.6. Timeline](#16-timeline)
  * [2. Mathematical Model Breakdown](#2-mathematical-model-breakdown)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 1. Analysis of PRACH Attack on Network Energy Saving

### 1.1. Abstract

Energy efficiency is a crucial factor in 5G networks, where various energy-saving mechanisms are implemented to optimize power consumption. However, PRACH (Physical Random Access Channel) attacks pose a significant threat to these mechanisms, as attackers can exploit PRACH as a wake-up signal to force the base station (gNB) to exit its low-power state, increasing energy consumption unnecessarily.

This thesis aims to develop an analytical model to investigate the impact of PRACH attacks on network energy savings (NES). The model will analyze the interaction between an attacker, legitimate User Equipment (UE), and the base station, providing insights into how energy consumption is affected under attack scenarios. The study will further explore the potential challenges of detecting and mitigating PRACH-based energy attacks.

### 1.2. Research Objectives

1. Develop a mathematical model to analyze the impact of PRACH attacks on network energy savings
2. Investigate how attack frequency and intensity influence energy consumption in 5G base stations and UE
3. Analyze the perspectives of three key entities: attacker, regular UE, and base station in an energy-aware 5G network
4. Explore potential detection and mitigation strategies to counteract PRACH-based energy attacks
5. Validate the proposed model using analytical methods and simulations


### 1.3. Methodology

- **Literature Review** – Study existing work on 5G energy-saving mechanisms, PRACH jamming attacks, and energy-efficient network security.
- **Mathematical Modeling** – Develop an analytical model capturing the relationship between PRACH attack frequency, network wake-up cycles, and energy consumption.
- **Simulation & Validation** – Implement the model in a simulation environment to evaluate its accuracy and analyze attack impact under various conditions.
- **Performance Analysis** – Compare energy consumption with and without PRACH attacks, quantifying the waste energy caused by the attacker.
- **Exploration of Detection & Mitigation Strategies** – Investigate possible countermeasures, such as adaptive wake-up mechanisms or ML-based anomaly detection.

### 1.4. Expected Outcomes

- A formal mathematical model quantifying the impact of PRACH attacks on energy savings.
- Simulation results demonstrating energy consumption changes under attack conditions.
- Comparative analysis from the perspectives of the attacker, regular UE, and base station.
- Recommendations for detection and mitigation, improving 5G network resilience against energy-based attacks.

### 1.5. Significance of the Study

- Energy efficiency is a key concern in 5G, with operators aiming to reduce power consumption.
- PRACH attacks can exploit power-saving features, increasing operational costs and carbon footprint.
- This research provides a systematic way to analyze and quantify the impact of such attacks, guiding future energy-aware security measures.

### 1.6. Timeline

| Week  | Task                                                                  |
| ----- | --------------------------------------------------------------------- | 
| 1-2   | Literature review on PRACH attacks and energy-saving techniques in 5G | 
| 3-6   | Development of [mathematical model](#2-mathematical-model-breakdown) and system assumptions              | 
| 7-10  | Implementation of model and simulations                               | 
| 11-14 | Performance evaluation and comparative analysis                       | 
| 15-16 | Documentation and thesis writing                                      | 
| 17-18 | Review, revisions, and thesis submission                              | 

## 2. Mathematical Model Breakdown

1. Basic Collision Model
	- Define UE and PRACH parameters (e.g., number of devices, available RAOs, retry limits)
	- Use a combinatorial approach (like the paper) to model collision probability in PRACH
	- Adapt the Poisson-based approximation formula to estimate PRACH success probability
2. Incorporate Attacker into Collision Model
	- Extend the one-shot random access model by introducing an adversarial factor (attacker).
	- Modify collision probability calculations to account for malicious PRACH requests.
	- Derive an equation for collision probability under PRACH attack scenarios.
3. 5G PRACH Energy Model
	- Define energy-saving mechanisms (e.g., sleep/wake-up cycles of the base station).
	- Model the energy consumed per wake-up cycle triggered by PRACH access.
	- Consider how attack-induced PRACH collisions affect power consumption.
4. Integrate Collision Model with Energy Model
	- Use collision probability results (from step 2) to estimate additional wake-up events.
	- Derive energy loss per attack cycle, factoring in legitimate UEs vs. attacker impact.
	- Express total energy waste as a function of attack intensity and network conditions.
