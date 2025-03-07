# 20250307 Thesis (PRACH Attack Problem Definition)

###### tags: `2025`

**Goal:**
- [x] Map the PRACH Attack Problem
- [x] Define the PRACH Attack Problem that I want to focus on

**References:**
- [5G/NR - Initial Access/RACH](https://www.sharetechnote.com/html/5G/5G_RACH.html)
- [Techniques and Impact Evaluation of RACH Jamming in 5G network](https://etheses.lib.ntust.edu.tw/thesis/detail/64057b454c8e6e7e11cfd2812c8fecf7/)
- [20250307 Thesis (Random Access Procedure and Attack)](https://github.com/bmw-ece-ntust/wilfrid-prach-attack-analysis/blob/master/docs/20250307%20Thesis%20(Random%20Access%20Procedure%20and%20Attack).md)

**Table of Contents:**

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## 1. Map of PRACH Attack Problem

```mermaid
stateDiagram-v2
    s1: PRACH Attack
    s2: Attack Msg1
    s3: Attack Msg3
    s4: Attack Msg1 and Msg3 Together
    s1 --> s2
    s1 --> s3
    s1 --> s4
    s5: Attack Msg1<br>with noise threshold
    s6: Attack Msg1<br>without noise threshold
    s2 --> s5
    s2 --> s6
    s7: Attack Msg3<br>with noise threshold
    s8: Attack Msg3<br>without noise threshold
    s3 --> s7
    s3 --> s8
    s9: Attack Msg1<br>with noise threshold<br>1 UE
    s10: Attack Msg1<br>with noise threshold<br>multi UE
    s11: Attack Msg1<br>without noise threshold<br>1 UE
    s12: Attack Msg1<br>without noise threshold<br>multi UE
    s5 --> s9
    s5 --> s10
    s6 --> s11
    s6 --> s12
    s13: Attack Msg3<br>with noise threshold<br>1 UE
    s14: Attack Msg3<br>with noise threshold<br>multi UE
    s15: Attack Msg3<br>without noise threshold<br>1 UE
    s16: Attack Msg3<br>without noise threshold<br>multi UE
    s7 --> s13
    s7 --> s14
    s8 --> s15
    s8 --> s16
```


## 2. PRACH Attack Problem to focus on

