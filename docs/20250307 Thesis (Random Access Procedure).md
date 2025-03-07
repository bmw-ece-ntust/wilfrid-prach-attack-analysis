# 20250307 Thesis (Random Access Procedure)

###### tags: `2025`

**Goal:**
- [x] Understand 5G Random Access Procedure

**References:**
- 

**Table of Contents:**
- 

## 1. Step by step

1.  gNB transmits the synchronization signal and PBCH (SSB), enabling the UE to acquire the cell’s system information and synchronize with the downlink
transmission

2. UE determines the allocation of PRACH resources and transmits a preamble (Msg1) to the gNB

3. UE starts calculating the random access response (RAR, also called Msg2) window, which is defined by the ra-ResponseWindow parameter determined by the gNB

4. gNB indicates the downlink control information (DCI) on the PDCCH, specifying the location of the PDSCH where Msg2 will be transmitted

5. Msg2 will be transmitted by gNB

6. UE uses the information in Msg2, to transmit the RRC setup request (Msg3) on PUSCH

7. UE starts the contention resolution (CR) timer, defined by the ra-ContentionResolutionTimer parameter

8. When the gNB receives Msg3, it responds with DCI on PDCCH

9. gNB send RRC connection setup (Msg4) on the PDSCH

10.  If the UE receives Msg4 within the CR timer, it transitions to the RRC connected state and sends the RRC connection complete (Msg4 Ack), completing the RA process
