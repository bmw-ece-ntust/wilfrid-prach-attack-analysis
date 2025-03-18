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
    - LTE/LTE-A networks are highly vulnerable to jamming, spoofing, and sniffing attacks
- **Importance:**
    - LTE is widely used in critical infrastructures, including emergency services, military networks, and smart grids. Attacks on LTE can lead to service failures in life-critical situations.
- **Challenge:**
    - Less available open literature related to LTE jamming attack and mitigation of those attack
    - Effective mitigation strategies must be backward-compatible, as LTE networks cannot be completely redesigned.
- **Contribution:**
    - Comprehensive Threat Assessment (LTE's PRACH, PCFICH, PUCCH, PBCH vunerabilities and jamming efficiency vs. implementation on those channels)
    - Survey of Mitigation Techniques (Scrambling PUCCH resource mapping, encrypt MIB SIB, UE based spoofing detection, etc)

## 7. Analysis and Mitigation of Interference to the LTE Physical Control Format Indicator Channel

- **Problem:**
    - PCFICH (Physical Control Format Indicator Channel) in LTE is highly vulnerable to jamming attacks, which can severely disrupt network operations by preventing UEs from decoding downlink control information.
- **Importance:**
    - LTE is used in critical applications, including public safety, military communications, and emergency response. A successful PCFICH jamming attack can completely disrupt these essential services.
- **Challenge:**
    - PCFICH is a fundamental part of the LTE design, meaning any changes to mitigate jamming must be backward-compatible.
- **Contribution:**
    - PCFICH Vulnerability Analysis (evaluate impact of PCFICH jamning in simulation)
    - Proposed Mitigation Strategies (Extra-Blind PDCCH Decoding, eliminate PCFICH by fix number of OFDM symbols)

## 8. Detection and Mitigation of Uplink Control Channel Jamming in LTE

- **Problem:**
    - PUCCH is statically allocated in the frequency spectrum, making it an easy target for protocol-aware adversaries
- **Importance:**
    - Mission-Critical Applications: LTE is increasingly being used for public safety networks (e.g., FirstNET), military communications, and emergency response systems. Ensuring high availability of LTE networks under jamming attacks is crucial for these use cases
- **Challenge:**
    - Mitigation Trade-offs, like duplicating control signals on PUSCH will consume extra bandwidth
- **Contribution:**
    - Detection Strategies (Monitoring for Excess PUCCH Energy, Tracking PUCCH Error Rates)
    - Mitigation Strategies (shifting Control Signaling to the PUSCH, robust modulation and coding scheme) and simulation of the strategy

## 9. Jamming Attacks and Anti-Jamming Strategies in Wireless Networks: A Comprehensive Survey

- **Problem:**
    - Despite advancements in wireless communication, there is still threat of jamming attacks in wireless networks and the lack of effective anti-jamming strategies
- **Importance:**
    - With the rise of IoT, smart cities, and autonomous vehicles, Jamming can lead to severe service disruptions
- **Challenge:**
    - Limited real-world deployment of anti-jamming techniques (theoritical only)
    - Trade-off between security and network efficiency
- **Contribution:**
    - Survey of Jamming Attacks (categories of attack and technologies attacked)
    - Survey of Jamming Attacks (traditional and advanced mechanisms)
    - Identifying Research Gaps and Future Directions (integration of AI to jamming detection, Deployment challenges of advanced anti-jamming techniques in real-world networks, etc)

## 10. Enhancing the security of LTE networks against jamming attacks

- **Problem:**
    - 
- **Importance:**
    - 
- **Challenge:**
    - 
- **Contribution:**
    - 
