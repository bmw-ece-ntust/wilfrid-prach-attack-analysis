# prach-attack-analysis

**References:**
- [Modeling and Estimation of One-Shot Random Access for Finite-User Multichannel Slotted ALOHA Systems](https://ieeexplore.ieee.org/document/6211364)

**System Model:**
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

**Repository Structure:**
```
prach-attack-analysis
├── docs    : Notes for the thesis development
├── math    : source code for mathemathical model
├── simu    : source code for simulation
```
