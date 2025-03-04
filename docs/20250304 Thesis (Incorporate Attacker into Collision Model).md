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
