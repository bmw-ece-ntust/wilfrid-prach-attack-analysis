# 2025/02/24 Study Note (Paper Survey for PRACH Attack Impact on Energy Saving)

###### tags: `2025`

**Goal:**
- [ ] Read ZX’s work reference and Paper sent by Andreas

**References:**
- [Prof. Ray | Template for BMW Lab.](https://hackmd.io/@RayCheng/rJIuoWmB8)
- [Smart PRACH Jamming: A Serious Threat for 5G Campus Networks](https://arxiv.org/abs/2410.08729)
- [Smart Jamming Attacks in 5G New Radio: A Review](https://ieeexplore.ieee.org/document/9031175)
- [Resilience of LTE networks against smart jamming attacks](https://ieeexplore.ieee.org/document/7036895)
- [Implementation and Evaluation of a Smart Uplink Jamming Attack in a Public 5G Network](https://ieeexplore.ieee.org/document/10186886)
- [Towards Resilient 5G: Lessons Learned from Experimental Evaluations of LTE Uplink Jamming](https://ieeexplore.ieee.org/document/8756977)

**Table of Contents:**
- [1. Smart PRACH Jamming: A Serious Threat for 5G Campus Networks](#1-smart-prach-jamming--a-serious-threat-for-5g-campus-networks)
- [2. Smart Jamming Attacks in 5G New Radio: A Review](#2-smart-jamming-attacks-in-5g-new-radio-a-review)
- [3. Resilience of LTE networks against smart jamming attacks](#3-resilience-of-lte-networks-against-smart-jamming-attacks)
- [4. Implementation and Evaluation of a Smart Uplink Jamming Attack in a Public 5G Network](#4-implementation-and-evaluation-of-a-smart-uplink-jamming-attack-in-a-public-5g-network)
- [5. Towards Resilient 5G: Lessons Learned from Experimental Evaluations of LTE Uplink Jamming](#5-towards-resilient-5g-lessons-learned-from-experimental-evaluations-of-lte-uplink-jamming)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## 1. Smart PRACH Jamming: A Serious Threat for 5G Campus Networks

- **Problem:**
    - PRACH jammer in industrial environment can cause large-scale failure, such as an Automated Guided Vehicle (AGV) failing to move between factory zones
- **Importance:**
    - Traditional broadband jamming consumes high power and affects the entire network, but smart jamming is highly targeted, energy-efficient, and harder to detect
- **Challenge:**
    - No research has practical implementation of PRACH jammer
- **Contribution:**
    - Modeling of Smart Jamming Attack (Ratio of success preamble, etc) and Implementation of a Smart PRACH Jammer in OAI

## 2. Smart Jamming Attacks in 5G New Radio: A Review

- **Problem:**
    - There is a lack of systematic research on how different jamming strategies impact 5G NR networks and how to develop effective countermeasures
- **Importance:**
    - 5G is critical for modern infrastructure, including emergency response, autonomous vehicles, and smart cities. Jamming threats could cause severe disruptions in these areas
- **Challenge:**
    - In-depth knowledge of 5G NR standard to determine vunerability
- **Contribution:**
    - Comprehensive Review of 5G NR Jamming Vulnerabilities (PBCH, PDCCH, PUCCH, RACH, mMIMO vunerabilities)
    - Identifies Gaps in Current Research (lack of data for ML based jam detection, complexity of high protection DSSS method, etc) and Future Directions (building dataset for DL anti-jamming, cyber-security embedded initial design of 5G NR, etc)

## 3. Resilience of LTE networks against smart jamming attacks

- **Problem:**
    - Current LTE networks lack built-in resilience against targeted jamming attacks, making them susceptible to low-cost adversaries using software-defined radios (SDRs)
- **Importance:**
    - Smart jammers use narrowband attacks to target specific LTE control channels (e.g., PRACH, PBCH, PCFICH, PUCCH), causing denial-of-service (DoS) attacks without needing to hack the network
- **Challenge:**
    - Existing anti-jamming techniques (e.g., frequency hopping, pilot boosting) may degrade network performance rather than effectively counteract attacks
    - Game-theoretic approaches must balance network resilience with practical implementation constraints, ensuring countermeasures do not disrupt legitimate network operations
- **Contribution:**
    - Game-Theoretic Modeling of Smart Jamming Attacks (Cheater and Saboteur vs. eNB, single shot and repeated bayesian game)
    - Proposed Adaptive Anti-Jamming Countermeasures (Increase CS-RS Tx Power, change eNB frequency, etc)

## 4. Implementation and Evaluation of a Smart Uplink Jamming Attack in a Public 5G Network

- **Problem:**
    - Smart jamming attacks can disrupt 5G uplink communications by precisely targeting specific users (UEs) instead of jamming the entire network
- **Importance:**
    - Jamming attacks can lead to complete communication failures, causing major disruptions in mission-critical operations
- **Challenge:**
    - De-anonymizing user-specific identifiers (C-RNTI) is complex, requiring deep protocol-level knowledge
- **Contribution:**
    - Developed a method for de-anonymizing user information, allowing the jammer to identify specific users by extracting the C-RNTI in PDCCH
    - Tested the attack in both wired and over-the-air (OTA) environments, demonstrating 100% effectiveness in blocking uplink communication


## 5. Towards Resilient 5G: Lessons Learned from Experimental Evaluations of LTE Uplink Jamming

- **Problem:**
    - Current LTE and 5G security measures are insufficient, leaving networks exposed to targeted jamming
- **Importance:**
    - LTE networks are vulnerable to smart uplink jamming attacks, which can severely disrupt communication in critical infrastructures (e.g., energy grids, healthcare, emergency services, and transportation)
- **Challenge:**
    - Smart jammers need to use minimal power (reduce visibility) and gather information of target before attack
- **Contribution:**
    - Experimental Evaluation of Smart Uplink Jamming in PUCCH and PUSCH in srsLTE UE

## 6. LTE/LTE-A Jamming, Spoofing, and Sniffing: Threat Assessment and Mitigation

- **Problem:**
    - abc
- **Importance:**
    - abc
- **Challenge:**
    - abc
- **Contribution:**
    - abc



