# prach-attack-analysis

**References:**
- [Modeling and Estimation of One-Shot Random Access for Finite-User Multichannel Slotted ALOHA Systems](https://ieeexplore.ieee.org/document/6211364)

**System Model:**
```mermaid
flowchart TD
    A("`**Basestation:**
    -----------
    *N* - preamble ID
    *P_noise* - threshold
    *α* - noise threshold update factor
    *delta* - Msg1 threshold`")
    B["`**UE (M=1):**
    -------
    *P_UE* - msg1 power`"]
    C[["`**Attacker:**
    ---------
    *O* - number of msg1 attacked
    *P_attacker* - msg1 power
    *j* - time early start
    *T_a* - attack period`"]]
    B-->A
    C-->A
```
**Repository Structure:**
```
prach-attack-analysis
├── docs    : Notes for the thesis development
├── expe    : source code for experiment results
├── math    : source code for mathemathical model
├── simu    : source code for simulation
```
