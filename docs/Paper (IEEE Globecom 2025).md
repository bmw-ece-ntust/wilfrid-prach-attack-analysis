# Paper (IEEE Globecom 2025)

###### tags: `2025`

**Goal:**
- [ ] Write paper agenda

**References:**
- [Call for Symposium Papers](https://globecom2025.ieee-globecom.org/call-symposium-papers)
- [CISS Symposium](https://globecom2025.ieee-globecom.org/sites/globecom2025.ieee-globecom.org/files/GC25-CFP-CISS.pdf)

**Table of Contents:**
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## 1. Paper Agenda
<b>I. Introduction</b>
- Context & Motivation:
  - Importance of 5G RACH access and its role in network reliability.
  - Emerging threats: RACH jamming attacks targeting Msg1 transmissions.
  - Existing solutions focus on ML-based detection, but lack analytical models quantifying the attack impact.
- Problem Statement:
  - How does a Msg1-based RACH jamming attack affect gNB noise threshold?
  - How can we mathematically model the probability of a UE successfully connecting under attack?
- Contributions (List of key contributions of this paper):
  1. Develop an OpenAirInterface-based jamming attacker that transmits Msg1 without responding to Msg2, increasing gNB noise threshold.
  2. Derive a mathematical model to predict gNB noise accumulation and UE connection probability.
  3. Validate the model through real-world experiments using a 5G testbed and compare theoretical vs. observed results.
  4. Propose countermeasures such as adaptive noise thresholding for mitigation.
- Paper Organization (Outline of remaining sections).

<b>II. Related Work</b>
- Subsection 1: RACH Jamming Attacks in 5G
  - Summarize existing RACH jamming studies (each in 2–3 sentences):
    - What attack methodology was used?
    - What were their findings?
    - What is missing in their work that motivates our study?
- Subsection 2: 4-Step vs. 2-Step RACH Process
  - Provide a brief summary of the 4-step RACH (Msg1 → Msg2 → Msg3 → Msg4) and 2-step RACH.
  - Explain how our attack specifically targets the Msg1 transmission step.
- Gap Analysis & Motivation for Our Work
  - Prior studies focus on ML-based detection but lack predictive mathematical models.
  - No prior work validates theoretical models using real-world 5G testbed experiments.
  - Our work fills this gap by providing an analytical and experimental approach.

<b>III. System Model & Problem Definition</b>
- Subsection 1: Network Model
  - Define the network setup:
    - Entities: gNB, legitimate UEs, attacker UE.
    - Describe RACH process and how a UE normally connects.
- Subsection 2: Attacker Model
  - Explain the attacker's strategy:
    - Transmits Msg1 repeatedly but never responds to Msg2.
    - Effect: Increases gNB noise floor, preventing legitimate UEs from connecting.
- Subsection 3: Key System Parameters
  - Define critical variables:
    - P noise : gNB noise threshold.
    - P attacker : Attacker's Msg1 power.
    - α: Noise update factor.
    - T a : Attacker’s Msg1 transmission period.
    - P UE : UE’s Msg1 power.
  - Problem Formulation
    - How does P noise evolve over time under attack?
    - Under what conditions can P UE > P noise​ so the UE can still connect?

<b>IV. Mathematical Analysis of Jamming Impact</b>
- Subsection 1: Noise Threshold Evolution
  - Develop an equation for P noise accumulation over multiple RACH slots.
- Subsection 2: Probability of UE Success
  - Derive the probability function for a legitimate UE to connect.
- Subsection 3: Model Predictions & Insights
  - Analyze how attacker transmission frequency T a and power P attacker affect UE connectivity.

<b>V. Experimental Setup & Validation</b>
- Subsection 1: 5G Testbed Setup
  - Describe hardware & software:
    - gNB: OpenAirInterface gNB on USRP B210.
    - UE: Commercial UE attempting RACH access.
    - Attacker: OAI-based jamming UE.
- Subsection 2: Experimental Parameters
  - Define tested attack conditions:
    - T a values: 1, 2, 4, 8 frame intervals.
    - α values: 0.18, 0.12, 0.06, 0.
    - δ: Msg1 detection margin.
- Subsection 3: Results & Model Validation
  - Compare mathematical predictions vs. experimentally observed results.
  - Show graphs of P noise increase and UE success probability trends.

<br><b>VI. Attack Strategies & Countermeasures</b>
- Subsection 1: Optimizing the Attack
  - Identify optimal attacker period and power level for maximum disruption.
- Subsection 2: Defensive Mechanisms for gNBs
  - Adaptive Noise Thresholding: Dynamically adjust P noise to ignore attack influence.
  - Machine Learning-Based Detection: Identify anomalies in Msg1 transmission patterns.
<br><b>VII. Conclusion & Future Work</b>
- Summary of Key Findings
  - RACH jamming effectively blocks UE access by increasing P noise.
  - Our mathematical model accurately predicts attack impact.
  - Experimental results validate the model.
- Future Directions
  - Implement real-time detection mechanisms.
  - Extend the model to multiple attackers.
</p>
