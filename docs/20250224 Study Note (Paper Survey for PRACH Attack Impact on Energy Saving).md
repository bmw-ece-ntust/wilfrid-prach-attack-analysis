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
- [2025/02/24 Study Note (Paper Survey for PRACH Attack Impact on Energy Saving)](#2025-02-24-study-note--paper-survey-for-prach-attack-impact-on-energy-saving-)
          + [tags: `2025`](#tags---2025-)
  * [1. PRACH Jamming References](#1-prach-jamming-references)
    + [1.1. Smart PRACH Jamming: A Serious Threat for 5G Campus Networks](#11-smart-prach-jamming--a-serious-threat-for-5g-campus-networks)
    + [1.2. Smart Jamming Attacks in 5G New Radio: A Review](#12-smart-jamming-attacks-in-5g-new-radio--a-review)
    + [1.3. Resilience of LTE networks against smart jamming attacks](#13-resilience-of-lte-networks-against-smart-jamming-attacks)
    + [1.4. Implementation and Evaluation of a Smart Uplink Jamming Attack in a Public 5G Network](#14-implementation-and-evaluation-of-a-smart-uplink-jamming-attack-in-a-public-5g-network)
    + [1.5. Towards Resilient 5G: Lessons Learned from Experimental Evaluations of LTE Uplink Jamming](#15-towards-resilient-5g--lessons-learned-from-experimental-evaluations-of-lte-uplink-jamming)
    + [1.6. LTE/LTE-A Jamming, Spoofing, and Sniffing: Threat Assessment and Mitigation](#16-lte-lte-a-jamming--spoofing--and-sniffing--threat-assessment-and-mitigation)
    + [1.7. Analysis and Mitigation of Interference to the LTE Physical Control Format Indicator Channel](#17-analysis-and-mitigation-of-interference-to-the-lte-physical-control-format-indicator-channel)
    + [1.8. Detection and Mitigation of Uplink Control Channel Jamming in LTE](#18-detection-and-mitigation-of-uplink-control-channel-jamming-in-lte)
    + [1.9. Jamming Attacks and Anti-Jamming Strategies in Wireless Networks: A Comprehensive Survey](#19-jamming-attacks-and-anti-jamming-strategies-in-wireless-networks--a-comprehensive-survey)
    + [1.10. Enhancing the security of LTE networks against jamming attacks](#110-enhancing-the-security-of-lte-networks-against-jamming-attacks)
    + [1.11. 5G NR Jamming, Spoofing, and Sniffing: Threat Assessment and Mitigation](#111-5g-nr-jamming--spoofing--and-sniffing--threat-assessment-and-mitigation)
    + [1.12. A Novel Jamming Attacks Detection Approach Based on Machine Learning for Wireless Communication](#112-a-novel-jamming-attacks-detection-approach-based-on-machine-learning-for-wireless-communication)
    + [1.13. Modeling and Analysis of Random Access Channels With Bursty Arrivals in OFDMA Wireless Networks](#113-modeling-and-analysis-of-random-access-channels-with-bursty-arrivals-in-ofdma-wireless-networks)
    + [1.14. Analytical Modeling and Performance Evaluation of Beam-Based Random Access Protocol for 5G Beamforming Networks](#114-analytical-modeling-and-performance-evaluation-of-beam-based-random-access-protocol-for-5g-beamforming-networks)
    + [1.15. Jamming-Resistant Receivers for the Massive MIMO Uplink](#115-jamming-resistant-receivers-for-the-massive-mimo-uplink)
  * [2. Preamble Detection References](#2-preamble-detection-references)
    + [2.1. An Enhanced PRACH Preamble Detector for Cellular IoT Communications](#21-an-enhanced-prach-preamble-detector-for-cellular-iot-communications)
    + [2.2. Enhanced PRACH Detection by Wavelet De-noising](#22-enhanced-prach-detection-by-wavelet-de-noising)
    + [2.3. A proposed preamble detection algorithm for 5G-PRACH](#23-a-proposed-preamble-detection-algorithm-for-5g-prach)
  * [3. 4 step versus 2 step RACH](#3-4-step-versus-2-step-rach)
    + [3.1. On Contention-based 2-step Random Access Procedure](#31-on-contention-based-2-step-random-access-procedure)
    + [3.2. Two-Step Random Access for 5G System: Latest Trends and Challenges](#32-two-step-random-access-for-5g-system--latest-trends-and-challenges)
    + [3.3. Analyzing Novel Grant-Based and Grant-Free Access Schemes for Small Data Transmission](#33-analyzing-novel-grant-based-and-grant-free-access-schemes-for-small-data-transmission)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 1. PRACH Jamming References

### 1.1. Smart PRACH Jamming: A Serious Threat for 5G Campus Networks

- **Problem:**
    - PRACH jammer in industrial environment can cause large-scale failure, such as an Automated Guided Vehicle (AGV) failing to move between factory zones
- **Importance:**
    - Traditional broadband jamming consumes high power and affects the entire network, but smart jamming is highly targeted, energy-efficient, and harder to detect
- **Challenge:**
    - No research has practical implementation of PRACH jammer
- **Contribution:**
    - Modeling of Smart Jamming Attack (Ratio of success preamble, etc) and Implementation of a Smart PRACH Jammer in OAI

### 1.2. Smart Jamming Attacks in 5G New Radio: A Review

- **Problem:**
    - There is a lack of systematic research on how different jamming strategies impact 5G NR networks and how to develop effective countermeasures
- **Importance:**
    - 5G is critical for modern infrastructure, including emergency response, autonomous vehicles, and smart cities. Jamming threats could cause severe disruptions in these areas
- **Challenge:**
    - In-depth knowledge of 5G NR standard to determine vunerability
- **Contribution:**
    - Comprehensive Review of 5G NR Jamming Vulnerabilities (PBCH, PDCCH, PUCCH, RACH, mMIMO vunerabilities)
    - Identifies Gaps in Current Research (lack of data for ML based jam detection, complexity of high protection DSSS method, etc) and Future Directions (building dataset for DL anti-jamming, cyber-security embedded initial design of 5G NR, etc)

### 1.3. Resilience of LTE networks against smart jamming attacks

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

### 1.4. Implementation and Evaluation of a Smart Uplink Jamming Attack in a Public 5G Network

- **Problem:**
    - Smart jamming attacks can disrupt 5G uplink communications by precisely targeting specific users (UEs) instead of jamming the entire network
- **Importance:**
    - Jamming attacks can lead to complete communication failures, causing major disruptions in mission-critical operations
- **Challenge:**
    - De-anonymizing user-specific identifiers (C-RNTI) is complex, requiring deep protocol-level knowledge
- **Contribution:**
    - Developed a method for de-anonymizing user information, allowing the jammer to identify specific users by extracting the C-RNTI in PDCCH
    - Tested the attack in both wired and over-the-air (OTA) environments, demonstrating 100% effectiveness in blocking uplink communication


### 1.5. Towards Resilient 5G: Lessons Learned from Experimental Evaluations of LTE Uplink Jamming

- **Problem:**
    - Current LTE and 5G security measures are insufficient, leaving networks exposed to targeted jamming
- **Importance:**
    - LTE networks are vulnerable to smart uplink jamming attacks, which can severely disrupt communication in critical infrastructures (e.g., energy grids, healthcare, emergency services, and transportation)
- **Challenge:**
    - Smart jammers need to use minimal power (reduce visibility) and gather information of target before attack
- **Contribution:**
    - Experimental Evaluation of Smart Uplink Jamming in PUCCH and PUSCH in srsLTE UE

### 1.6. LTE/LTE-A Jamming, Spoofing, and Sniffing: Threat Assessment and Mitigation

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

### 1.7. Analysis and Mitigation of Interference to the LTE Physical Control Format Indicator Channel

- **Problem:**
    - PCFICH (Physical Control Format Indicator Channel) in LTE is highly vulnerable to jamming attacks, which can severely disrupt network operations by preventing UEs from decoding downlink control information.
- **Importance:**
    - LTE is used in critical applications, including public safety, military communications, and emergency response. A successful PCFICH jamming attack can completely disrupt these essential services.
- **Challenge:**
    - PCFICH is a fundamental part of the LTE design, meaning any changes to mitigate jamming must be backward-compatible.
- **Contribution:**
    - PCFICH Vulnerability Analysis (evaluate impact of PCFICH jamning in simulation)
    - Proposed Mitigation Strategies (Extra-Blind PDCCH Decoding, eliminate PCFICH by fix number of OFDM symbols)

### 1.8. Detection and Mitigation of Uplink Control Channel Jamming in LTE

- **Problem:**
    - PUCCH is statically allocated in the frequency spectrum, making it an easy target for protocol-aware adversaries
- **Importance:**
    - Mission-Critical Applications: LTE is increasingly being used for public safety networks (e.g., FirstNET), military communications, and emergency response systems. Ensuring high availability of LTE networks under jamming attacks is crucial for these use cases
- **Challenge:**
    - Mitigation Trade-offs, like duplicating control signals on PUSCH will consume extra bandwidth
- **Contribution:**
    - Detection Strategies (Monitoring for Excess PUCCH Energy, Tracking PUCCH Error Rates)
    - Mitigation Strategies (shifting Control Signaling to the PUSCH, robust modulation and coding scheme) and simulation of the strategy

### 1.9. Jamming Attacks and Anti-Jamming Strategies in Wireless Networks: A Comprehensive Survey

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

### 1.10. Enhancing the security of LTE networks against jamming attacks

- **Problem:**
    - LTE lacks built-in security measures to prevent targeted jamming attacks
- **Importance:**
    - LTE is being adopted for emergency response networks, such as the Nationwide Public Safety Broadband Network (NPSBN), USA. Jamming attacks could disrupt communications for first responders, law enforcement, and disaster recovery teams.
- **Challenge:**
    - Implementation Complexity and Compatibility Issue of anti jamming solutions
    - Performance Trade-offs of anti jamming solutions
- **Contribution:**
    - proposes several security enhancements to mitigate smart jamming attacks in LTE:
        - Spread-Spectrum Jamming Resiliency
        - Encryption of MIB SIB
        - Scrambling of Uplink Control Channel Assignments
        - etc

### 1.11. 5G NR Jamming, Spoofing, and Sniffing: Threat Assessment and Mitigation

- **Problem:**
    - 5G NR is vulnerable to RF interference, jamming, spoofing, and sniffing attacks
- **Importance:**
    - Society will become increasingly dependent on 5G, making its security and availability critical
- **Challenge:**
    - Different attack vectors have varying levels of complexity and efficiency, requiring prioritization of hardening efforts
- **Contribution:**
    - Comprehensive Vulnerability Analysis of each physical channel (PBCH, etc) and signal (RS, SS) in 5G NR, identifying their vulnerabilities to jamming, spoofing, and sniffing attacks.
    - proposes specific mitigation techniques that do not require changes to specifications but can be incorporated into implementations (Timer-based and blacklisting mechanisms for PSS/SSS spoofing, limit broadcast message content to essential information, etc)

### 1.12. A Novel Jamming Attacks Detection Approach Based on Machine Learning for Wireless Communication

- **Problem:**
    - Jamming detection techniques have been proposed, including fuzzy logic, game theory, channel surfing, and time series, but most of these techniques are inefficient in detecting smart jammers
- **Importance:**
    - With billions of wireless devices expected to connect to 5G networks, the security implications are significant, especially for applications like self-driving cars, IoT, e-health services, and smart cities
- **Challenge:**
    - Existing methods typically require more resources and ultimately serve only as a stopgap
    - There's a need for accurate feature selection and algorithm training/testing, which is often neglected in existing approaches
- **Contribution:**
    - A comparison of several machine learning models (random forest, support vector machine, neural network) for detecting jamming signals
    - Investigation of signal features that effectively identify jamming signals (bad packet ratio, packet delivery ratio, received signal strength, clear channel assessment)

### 1.13. Modeling and Analysis of Random Access Channels With Bursty Arrivals in OFDMA Wireless Networks

- **Problem:**
    - Current RACH (Random Access Channel) models assume Poisson-distributed arrivals with a constant rate, but in reality, bursty arrivals cause severe congestion, leading to high collision rates and network inefficiencies.
- **Importance:**
    - M2M (Machine-to-Machine) communication is expected to introduce massive device connections, creating bursty traffic patterns that current models do not handle effectively.
- **Challenge:**
    - RACH behavior involves multiple complex factors, such as periodic access characteristics, backoff policies, and power ramping effects
- **Contribution:**
    - Analytical model that captures transient RACH behavior under bursty arrivals
    - Develop a computationally efficient method to model OFDMA RACH behavior in transient conditions, improving over past iterative approaches.

### 1.14. Analytical Modeling and Performance Evaluation of Beam-Based Random Access Protocol for 5G Beamforming Networks

- **Problem:**
    - The performance of beam-based random access (RA) in 5G beamforming networks is not well understood, particularly in scenarios with bursty arrivals from massive IoT devices.
- **Importance:**
    - Beamforming is a critical feature in 5G NR and is widely used to improve spectral efficiency and network coverage.
- **Challenge:**
    - The number of possible beam mapping configurations is very large, making it difficult to analyze all possible scenarios.
- **Contribution:**
    - Developed an Analytical Model for Beam-Based Random Access
    - Identifies potential RACH load unbalance issues and proposes solutions to distribute RA requests more evenly.
    - Examines how backoff window size and maximum retransmission limits influence RA success rates and access latency.

### 1.15. Jamming-Resistant Receivers for the Massive MIMO Uplink

- **Problem:**
    - 
- **Importance:**
    - 
- **Challenge:**
    - 
- **Contribution:**
    - 

## 2. Preamble Detection References

### 2.1. An Enhanced PRACH Preamble Detector for Cellular IoT Communications

- **Problem:**
    - Noise rise causes increased false alarms in preamble detection when using multiple non-orthogonal preambles PRACH detection for cellular IoT communication
- **Importance:**
    - False alarms due to noise rise waste radio resources through unnecessary allocations
- **Challenge:**
    - Maintaining detection performance as the number of non-orthogonal preambles increases
- **Contribution:**
    - A propose two-phase preamble detection approach:
      - Preamble Reconstruction (PR) phase: reconstructs preambles from received signals
      - Final Preamble Detection (FPD) phase: detects preambles after interference cancellation

### 2.2. Enhanced PRACH Detection by Wavelet De-noising

- **Problem:**
    -  improving PRACH detection performance in noisy and interference-heavy (low SNR conditions) environments in LTE mobile systems
- **Importance:**
    - RACH detection accuracy directly impacts the efficiency of uplink synchronization in LTE systems, as an example, failed detection causes UEs to increase power (power ramping), which negatively impacts PUSCH performance
- **Challenge:**
    - Conventional matched filter approaches fail in very noisy and time dispersive channels
    - Meeting the 3GPP requirements (99% detection probability and 0.1% false detection probability) is challenging in low SNR environments
- **Contribution:**
    - Proposes an enhanced PRACH detector with a three-module approach: Forward Wavelet Transform, Denoise (threshold-based), and Inverse Wavelet Transform
    - The proposed detector meets the 3GPP requirements while maintaining relatively low computational complexity

### 2.3. A proposed preamble detection algorithm for 5G-PRACH

- **Problem:**
    -  Need for effective preamble detection in the PRACH for 5G systems
- **Importance:**
    - Preabmle detection procedure plays a critical role in 5G system because it is the first step in both contention-based and contention-free procedures in 5G
- **Challenge:**
    - False alarm peaks caused by noise, Channel conditions including multipath fading, Doppler shift effects, Frequency offset, Timing offset
    - The need to support multiple PRACH formats in 5G with different sequence lengths and subcarrier spacing
- **Contribution:**
    - proposes a comprehensive preamble detection method with two main processing stages:
      - Front-End processing: Extracts PRACH data in frequency domain from received signals
      - Behind-End (BE) processing with a multi-step detection algorithm:
        - Finding correlation peaks in search windows
        - Identifying interest peaks based on noise threshold
        - Rejecting weak peaks, false alarm peaks due to timing offset, false alarm peaks due to frequency offset, weak users due to high noise
        - Estimating true propagation delay

## 3. 4 step versus 2 step RACH

### 3.1. On Contention-based 2-step Random Access Procedure

- **Problem:**
    - inefficiency of the traditional 4-step RACH procedure in wireless communication systems which creates unnecessary overhead, power consumption, and latency issues
- **Importance:**
    - For scenarios like non-terrestrial networks (NTN) where round trip delay between UE and BS (e.g., satellite) could be extremely large, reducing the number of required interactions is crucial
    - Reducing signaling overhead, power consumption, and latency would significantly improve the efficiency of wireless communication systems, particularly for 5G NR
- **Challenge:**
    - Potential timing misalignment issues due to the lack of prior timing information in the first step of 2-step RACH
    - Managing collisions when multiple UEs select the same preambles and share the same resources
- **Contribution:**
    - simplified 2-step RACH procedure that combines Msg1 and Msg3 into a one-shot transmission (MsgA) and Msg2 and Msg4 into a single response (MsgB), reducing the interactions between UE and BS to just one.
    - Quantitative analysis demonstrating the advantages of 2-step RACH over 4-step RACH (reduction in signaling overhead, reduction in power consumption, reduction in latency)
    - Proposal of an advanced Multi-window Minimum Mean Square Error Successive Interference Cancellation (MMSE-SIC) receiver to resolve UE multiplexing and large timing offset problems

### 3.2. Two-Step Random Access for 5G System: Latest Trends and Challenges

- **Problem:**
    - enhancing and optimizing the 2-step RACH procedure in 5G systems, specifically addressing the preamble collision problem (undetected and detected)
- **Importance:**
    - it's valuable for NR Unlicensed spectrum (NR-U) where reducing connection steps helps decrease latency
    - Efficient random access mechanisms are essential for supporting the massive number of devices in 5G scenarios
- **Challenge:**
    - Finding the optimal division of preambles between 2-step and 4-step RACH procedures
    - Handling scenarios where the gNB cannot determine the Timing Advance (TA) command for each UE due to multiple identical preambles
- **Contribution:**
    - Comprehensive Overview and Challenge Analysis of 2 step contention based random access in 5g NR
    - Propose Self-Uplink Synchronization Framework that use DNNto help UE estimate Timing advance and Enables UEs to resolve preamble collisions by accurately timing their transmissions

### 3.3. Analyzing Novel Grant-Based and Grant-Free Access Schemes for Small Data Transmission

- **Problem:**
    - Optimizing random access procedures for small data transmissions in wireless networks. Traditional grant-based (4 step) access schemes suffer from high latency and signaling overhead, while grant-free (2 step) schemes face issues related to resource contention and reliability.
- **Importance:**
    - Efficient small data transmission is crucial for applications like IoT, where devices frequently send short bursts of data. Optimizing access schemes can reduce latency, enhance network efficiency, and improve reliability, especially in dense network environments
- **Challenge:**
    - Balancing the trade-off between access delay and resource utilization remains a significant challenge. Grant-based access (4 step) offers reliable transmission but introduces delay, while grant-free access (2 step) reduces delay but increases the risk of packet collisions and interference.
- **Contribution:**
    - provides a comparative analysis of grant-based and grant-free access schemes, considering factors such as access latency, success probability, and resource efficiency.
    - presents mathematical models and simulations to evaluate the performance of these access schemes under various network conditions.
    - offers insights into optimizing access mechanisms for small data transmissions in next-generation wireless networks.


