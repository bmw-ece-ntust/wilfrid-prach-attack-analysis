# 20250313 Thesis (Test of PRACH Attacker for Basic Msg1 Model)

###### tags: `2025`


**Goal:**
- [x] [Test PRACH Attacker for Basic Msg1 Model]()

**References:**
- [OAI 5G NR SA tutorial with OAI nrUE](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/NR_SA_Tutorial_OAI_nrUE.md?ref_type=heads)
- [OAI UE + USRP B210 Installation Guide](https://hackmd.io/@zhongxin/BJSPWUy90)
- [Attacker guide for Wilfrid paper](https://ntust-bmwlab.notion.site/Attacker-guide-for-Wilfrid-paper-12d1009831438064b6afcf322b4fa252)

**Table of Contents:**
- [20250313 Thesis (Test of PRACH Attacker for Basic Msg1 Model)](#20250313-thesis--test-of-prach-attacker-for-basic-msg1-model-)
          + [tags: `2025`](#tags---2025-)
  * [0. Summary](#0-summary)
  * [1. PRACH Attacker for Basic Msg1 Model](#1-prach-attacker-for-basic-msg1-model)
    + [1.0. Minimum Requirement](#10-minimum-requirement)
      - [1.0.1. OAI gNB with USRP](#101-oai-gnb-with-usrp)
      - [1.0.2. OAI UE with USRP for attacker](#102-oai-ue-with-usrp-for-attacker)
    + [1.1. Topology](#11-topology)
    + [1.2. Environment](#12-environment)
      - [1.2.1. OAI gNB](#121-oai-gnb)
      - [1.2.2. OAI UE for attacker](#122-oai-ue-for-attacker)
    + [1.3. Compile](#13-compile)
      - [1.3.1. Compile gNB](#131-compile-gnb)
      - [1.3.2. Compile Attacker](#132-compile-attacker)
    + [1.4. Run](#14-run)
      - [1.4.1. Configuration](#141-configuration)
        * [1.4.1.1. gNB Configuration](#1411-gnb-configuration)
        * [1.4.1.2. Attacker Configuration](#1412-attacker-configuration)
      - [1.4.2. Result](#142-result)
        * [1.4.2.1. Initial Run](#1421-initial-run)
        * [1.4.2.2. Modify Attacker Period to every 2 frames](#1422-modify-attacker-period-to-every-2-frames)
        * [1.4.2.3. Modify Attacker Period to every 4 frames](#1423-modify-attacker-period-to-every-4-frames)
        * [1.4.2.4. Modify Attacker Period to every 8 frames](#1424-modify-attacker-period-to-every-8-frames)
    + [1.5. Results Compilation and Visualization](#15-results-compilation-and-visualization)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 0. Summary

1. More early attacker’s Msg1 start relative to UE = Higher gNB noise threshold
2. Attacker period decrease (more frequent attacker Msg1 transmissions) = Higher gNB noise threshold
3. Attacker with higher power but less frequent interval (e.g., 55 dB with $T_a = 2$) = Higher gNB noise threshold > attacker with lower power but more frequent interval (e.g., 31.4 dB with $T_a = 1$)
4. Low $\alpha$ in gNB = noise threshold at the gNB updates more slowly = increase UE access success
5. Low $\delta$ in gNB = required UE power for Msg1 detection is reduced = increase UE access success 

## 1. PRACH Attacker for Basic Msg1 Model

| Step                        | Status             |
| --------------------------- | ------------------ |
| gNB Run                     | :heavy_check_mark: |
| Attacker Run                | :heavy_check_mark: |
| Attacker Sync to gNB        | :heavy_check_mark: |
| [Attacker Send Msg1 to gNB](#1421-initial-run)   | :heavy_check_mark: |
| UE Run and Send Msg1 to gNB | :x: |
| [Data Compiled](#15-results-compilation-and-visualization)               | :heavy_check_mark: |

### 1.0. Minimum Requirement

- [Source](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/system_requirements.md)

#### 1.0.1. OAI gNB with USRP

<b>Hardware:</b>

| Item   | Info       |
| ------ | ---------- |
| CPU    |  |
| Memory |         |

<b>Software:</b>

| Item | Info            |
| ---- | --------------- |
| OS   |  |

#### 1.0.2. OAI UE with USRP for attacker

<b>Hardware:</b>

| Item   | Info       |
| ------ | ---------- |
| CPU    |  |
| Memory |         |

<b>Software:</b>

| Item | Info            |
| ---- | --------------- |
| OS   |  |

### 1.1. Topology

```mermaid
flowchart TD
    A("`**Basestation:**
    -----------
    OAI gNB
    (Intel NUC Kit NUC7i7BNH)`")
    B["`**UE:**
    -------
    MTK UE`"]
    C[["`**Attacker:**
    ---------
    OAI gNB
    (Intel NUC Kit NUC7i7BNH)`"]]
    u1(["`USRP B210`"])
    u2(["`USRP B210`"])
    B-- OTA -->u1
    subgraph Attacker
    C-->u2
    end
    u2-- OTA -->u1
    subgraph Basestation
    u1-->A
    end
```

### 1.2. Environment

#### 1.2.1. OAI gNB

<b>Hardware:</b>

| Item         | Info                                     |
| ------------ | ---------------------------------------- |
| CPU          | Intel(R) Core(TM) i7-7567U CPU @ 3.50GHz |
| Memory       | 8GB                                      |
| Disk         | 922GB                                    |
| Server Model | Intel Corporation NUC7i7BNH J31153-310   |

Command Line Codes
```shell=
# Check CPU Type, freq, cores, numbers
lscpu

# Check total memory
sudo lshw -C memory

# Check total disk
df -h
df --total -h | grep 'total' | awk '{print $2}'

# Check server model
sudo dmidecode -t system
```

<b>Software:</b>

| Item       | Info                       |
| ---------- | -------------------------- |
| OS         | Ubuntu 22.04.4 LTS (jammy) |
| Kernel     | 6.8.0-52-generic           |
| OAI Commit | 60b0c1827dbda37e1b2d0dfc91227d6ce9826827 (HEAD -> develop, origin/develop, origin/HEAD)                           |

Command Line Codes
```shell=
# Check OS
lsb_release -a

# Check kernel
uname -a
uname -r

# Check OAI commit
git log -1
```

#### 1.2.2. OAI UE for attacker

<b>Hardware:</b>

| Item         | Info                                     |
| ------------ | ---------------------------------------- |
| CPU          | Intel(R) Core(TM) i7-7567U CPU @ 3.50GHz |
| Memory       | 8GB                                      |
| Disk         | 922GB                                    |
| Server Model |                                          |

Command Line Codes
```shell=
# Check CPU Type, freq, cores, numbers
lscpu

# Check total memory
sudo lshw -C memory

# Check total disk
df -h
df --total -h | grep 'total' | awk '{print $2}'

# Check server model
sudo dmidecode -t system
```


<b>Software:</b>

| Item       | Info                       |
| ---------- | -------------------------- |
| OS         | Ubuntu 22.04.4 LTS (jammy) |
| Kernel     | 6.8.0-52-generic           |
| OAI Commit | 59b419d31c0ed8d6bea975c087b06d77f7ce25d7 (HEAD, origin/develop, origin/HEAD, develop)                           |

Command Line Codes
```shell=
# Check OS
lsb_release -a

# Check kernel
uname -a
uname -r

# Check OAI commit
git log -1
```


### 1.3. Compile


#### 1.3.1. Compile gNB

<b>1. Install USRP B210 dependency</b>

```shell=
sudo apt install -y autoconf automake build-essential ccache cmake cpufrequtils doxygen ethtool g++ git inetutils-tools libboost-all-dev libncurses5 libncurses5-dev libusb-1.0-0 libusb-1.0-0-dev libusb-dev python3-dev python3-mako python3-numpy python3-requests python3-scipy python3-setuptools python3-ruamel.yaml
```

<b>2. Build UHD from source</b>

```shell=
git clone https://github.com/EttusResearch/uhd.git
cd uhd
git checkout v4.6.0.0
cd host
mkdir build
cd build
cmake ../
make -j $(nproc)
make test # This step is optional
sudo make install
sudo ldconfig
```

<b>3. Download FPGA Image</b>

```shell=
sudo uhd_images_downloader
```

<b>4. Install Gnuradio</b>

```shell=
sudo apt install gnuradio
```

<b>5. Check if the system can recognise B210 through USB</b>

```shell=
lsusb
```
![image](https://github.com/user-attachments/assets/62f7b806-ded9-47db-a60b-be403876438d)

<b>6. Test the device with uhd to see if it works</b>

```shell=
sudo uhd_find_devices
```
![image](https://github.com/user-attachments/assets/a7924ed6-28cf-4a0c-993a-6d680106dbc4)

<b>7. Download OAI gNB from gitlab</b>

```shell=
git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git
cd openairinterface5g
git checkout develop
```
![image](https://github.com/user-attachments/assets/81627044-e22e-4b86-88bb-f946c2caa73e)

<b>8. Dependency</b>

```shell=
cd cmake_targets
./build_oai -I
```
![image](https://github.com/user-attachments/assets/8f365538-230e-4a47-a42b-9d4e2930d6f9)

<b>9. Install nrscope</b>

```shell=
sudo apt install -y libforms-dev libforms-bin
```
![image](https://github.com/user-attachments/assets/ea4316bb-e8e9-4aa3-a274-238768dfef43)

<b>10. Optional Reinstall yaml-cpp</b>

```shell=
# this is optional
# sometimes, the yaml-cpp library is broken, so will result in error of step 11
sudo apt update
sudo apt install --reinstall libyaml-cpp-dev
```
![image](https://github.com/user-attachments/assets/221673fa-ad55-4d89-9802-d0c45e66c127)

<b>11. Build oai gNB with USRP mode</b>

```shell=
./build_oai -w USRP --ninja --nrUE --gNB --build-lib "nrscope" -C
```
![image](https://github.com/user-attachments/assets/f5a08d78-d968-4c93-b1cc-72d2d69c3c21)

#### 1.3.2. Compile Attacker

<b>1. Install USRP B210 dependency</b>

```shell=
sudo apt install -y autoconf automake build-essential ccache cmake cpufrequtils doxygen ethtool g++ git inetutils-tools libboost-all-dev libncurses5 libncurses5-dev libusb-1.0-0 libusb-1.0-0-dev libusb-dev python3-dev python3-mako python3-numpy python3-requests python3-scipy python3-setuptools python3-ruamel.yaml
```

<b>2. Build UHD from source</b>

```shell=
git clone https://github.com/EttusResearch/uhd.git
cd uhd
git checkout v4.6.0.0
cd host
mkdir build
cd build
cmake ../
make -j $(nproc)
make test # This step is optional
sudo make install
sudo ldconfig
```

<b>3. Download FPGA Image</b>

```shell=
sudo uhd_images_downloader
```

<b>4. Install Gnuradio</b>

```shell=
sudo apt install gnuradio
```

<b>5. Check if the system can recognise B210 through USB</b>

```shell=
lsusb
```
![image](https://github.com/user-attachments/assets/74b16423-e985-4729-9eaf-494168a294a4)

<b>6. Test the device with uhd to see if it works</b>

```shell=
sudo uhd_find_devices
```
![image](https://github.com/user-attachments/assets/70109067-5a38-4971-92e8-0e58a5b2324b)

<b>7. Clone MSG1 Attacker and checkout to rework_UE branch</b>

```shell=
git clone https://github.com/Richard-yq/OAI-UE-MSG1-attacker.git
cd  OAI-UE-MSG1-attacker
git checkout develop
```

<b>8. Install ASN.1</b>

```shell=
cd cmake_targets
sudo ./build_oai -I
```

<b>9. Install nrscope</b>

```shell=
sudo apt install -y libforms-dev libforms-bin
```

<b>10. Build the attacker as OAI UE</b>

```shell=
./build_oai -w USRP --ninja --nrUE --gNB --build-lib "nrscope" -C
```
![image](https://github.com/user-attachments/assets/c8f094ed-7492-47c5-b204-e02d2bfa7b16)


### 1.4. Run

#### 1.4.1. Configuration

##### 1.4.1.1. gNB Configuration

<b>1. We use example configuration from `/targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf`</b>

<b>2. Be aware that you might need to change 4 things in the configuration file:</b>
- AMF and Network Interface Parameters (modify as your AMF and gNB ip address. Values that I use is below)
```shell=
////////// AMF parameters:
amf_ip_address = ({ ipv4 = "127.0.0.5"; }); 


NETWORK_INTERFACES :
{
    GNB_IPV4_ADDRESS_FOR_NG_AMF              = "127.0.0.17"; 
    GNB_IPV4_ADDRESS_FOR_NGU                 = "127.0.0.18"; 
    GNB_PORT_FOR_S1U                         = 2152; # Spec 2152
};
```
- PLMN List (modify as your desired Slice Configuration. Values that I use is below)
```shell=
plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; snssaiList = ({ sst = 1}) });
```
- min_rxtxtime (modify as your desired min_rxtxtime. Values that I use is below)
```shell=
# i use this because i cannot pass --gNBs.[0].min_rxtxtime 6 when running OAI gNB
gNBs =
(
 {
    ...
    min_rxtxtime = 6; # value 6 is because default USRP value
    ...
```
- prach_ConfigurationIndex (modify as your desired prach_ConfigurationIndex. Values that I use is below)
```shell=
prach_ConfigurationIndex = 159;
```

##### 1.4.1.2. Attacker Configuration

<b>We directly pass attacker's simulated UE configuration through command line</b>

#### 1.4.2. Result

##### 1.4.2.1. Initial Run

<b>1. Run OAI gNB</b>

```shell=
cd openairinterface5g/cmake_target/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 -E --continuous-tx --log_config.PRACH_debug
```
![image](https://github.com/user-attachments/assets/6650b2f5-90a0-4db5-a9bd-91a7ba9d81a4)

<b>2. Run Attacker</b>

```shell=
cd OAI-UE-MSG1-attacker/cmake_target/ran_build/build
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --ssb 516 -E --ue-fo-compensation --sa
```
![image](https://github.com/user-attachments/assets/ec91cf07-b6c8-4070-927d-c75f945939fe)

<b>3. Result explanation</b>
- We can see from Attacker's Log, it is placing Msg1 in every frame slot 19 symbol 0
![image](https://github.com/user-attachments/assets/765ccb52-4cd4-4cc5-98f2-875f249625a8)
- And from gNB, it receive the attacker's Msg1 and start RA procedure
![image](https://github.com/user-attachments/assets/8f06dd75-6f21-4c3c-9130-1ac692f8c7e3)
- gNB use TC-RNTI 5ea7 for attacker and generate Msg2
![image](https://github.com/user-attachments/assets/ab6cf0c2-8be3-4f94-ba7c-352b34a091b5)
- But gNB never receive attacker's Msg3, so gNB schedules retransmission of Msg3
![image](https://github.com/user-attachments/assets/aa6783a0-f454-4046-a0ed-13090adb31f6)
- Be aware that we hardcode the prach_ConfigurationIndex to 159 in `openair2/LAYER2/NR_MAC_UE/config_ue.c` in 2 functions
![image](https://github.com/user-attachments/assets/dd5fa1bb-08d9-4ba6-a1b9-ea768d5cb62d)
![image](https://github.com/user-attachments/assets/e3635ed4-2f41-45dd-94d1-5ec2dc8f15d3)


##### 1.4.2.2. Modify Attacker Period to every 2 frames

<b>0.1. Hardcode prach_ConfigurationIndex to 149 in `openair2/LAYER2/NR_MAC_UE/config_ue.c` in 2 functions</b>
![image](https://github.com/user-attachments/assets/f71f5932-7f0b-4eb1-888a-db40d401650e)
![image](https://github.com/user-attachments/assets/75fe00c5-8745-4d38-8a25-b1ba4134aca8)

<b>0.2. Recompile Attacker following [1.3.2.](#132-compile-attacker)</b>
![image](https://github.com/user-attachments/assets/c8f094ed-7492-47c5-b204-e02d2bfa7b16)

<b>1. Run OAI gNB</b>

```shell=
cd openairinterface5g/cmake_target/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 --sa -E --continuous-tx --log_config.PRACH_debug
```
![image](https://github.com/user-attachments/assets/6650b2f5-90a0-4db5-a9bd-91a7ba9d81a4)

<b>2. Run Attacker</b>

```shell=
cd OAI-UE-MSG1-attacker/cmake_target/ran_build/build
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --ssb 516 -E --ue-fo-compensation --sa
```
![image](https://github.com/user-attachments/assets/eca5e60e-c4ac-4ebf-855f-9990a8dbe392)

<b>3. Result explanation</b>
- We can see from Attacker's Log, it is placing Msg1 in every odd frame slot 19 symbol 0
![image](https://github.com/user-attachments/assets/d79e9838-5c30-4351-afa4-2d769545044c)
- And from gNB, it receive the attacker's Msg1 and start RA procedure but never receive Msg3
![image](https://github.com/user-attachments/assets/7ddc0a5b-047b-464a-b8c4-43aeb8ecc520)

##### 1.4.2.3. Modify Attacker Period to every 4 frames

<b>0.1. Hardcode prach_ConfigurationIndex to 147 in `openair2/LAYER2/NR_MAC_UE/config_ue.c` in 2 functions</b>
![image](https://github.com/user-attachments/assets/0753b6d6-3b23-4202-ac9d-4c1d622c9ef7)
![image](https://github.com/user-attachments/assets/8f3857fc-a35b-4b5a-af61-bd04ccaaba23)


<b>0.2. Recompile Attacker following [1.3.2.](#132-compile-attacker)</b>
![image](https://github.com/user-attachments/assets/c8f094ed-7492-47c5-b204-e02d2bfa7b16)

<b>1. Run OAI gNB</b>

```shell=
cd openairinterface5g/cmake_target/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 --sa -E --continuous-tx --log_config.PRACH_debug
```
![image](https://github.com/user-attachments/assets/6650b2f5-90a0-4db5-a9bd-91a7ba9d81a4)

<b>2. Run Attacker</b>

```shell=
cd OAI-UE-MSG1-attacker/cmake_target/ran_build/build
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --ssb 516 -E --ue-fo-compensation --sa
```
![image](https://github.com/user-attachments/assets/4d5c449d-24d9-4861-97da-d8847f6815cf)

<b>3. Result explanation</b>
- We can see from Attacker's Log, it is placing Msg1 in every odd frame slot 19 symbol 0
![image](https://github.com/user-attachments/assets/0da49fa8-eb6e-4bf0-8f41-fe7fa75adbec)
- And from gNB, it receive the attacker's Msg1 and start RA procedure but never receive Msg3
![image](https://github.com/user-attachments/assets/8e22f2e5-b161-4e4c-90da-294288a9c87f)

##### 1.4.2.4. Modify Attacker Period to every 8 frames

<b>0.1. Hardcode prach_ConfigurationIndex to 146 in `openair2/LAYER2/NR_MAC_UE/config_ue.c` in 2 functions</b>
![image](https://github.com/user-attachments/assets/4567ac15-c874-44ce-90de-887cafc71325)
![image](https://github.com/user-attachments/assets/acd899e1-7acf-462e-9dbd-aa7af4e54e3d)

<b>0.2. Recompile Attacker following [1.3.2.](#132-compile-attacker)</b>
![image](https://github.com/user-attachments/assets/c8f094ed-7492-47c5-b204-e02d2bfa7b16)

<b>0.3. Configure gNB's prach_ConfigurationIndex to 161 in `targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf`</b>
![image](https://github.com/user-attachments/assets/283e228a-1153-4860-b8a6-ccf6675e3bb7)

<b>1. Run OAI gNB</b>

```shell=
cd openairinterface5g/cmake_target/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 --sa -E --continuous-tx --log_config.PRACH_debug
```
![image](https://github.com/user-attachments/assets/6650b2f5-90a0-4db5-a9bd-91a7ba9d81a4)

<b>2. Run Attacker</b>

```shell=
cd OAI-UE-MSG1-attacker/cmake_target/ran_build/build
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --ssb 516 -E --ue-fo-compensation --sa
```
![image](https://github.com/user-attachments/assets/d6bf5841-5bbf-4b8c-9173-8c346e91ea51)

<b>3. Result explanation</b>
- We can see from Attacker's Log, it is placing Msg1 in every odd frame slot 19 symbol 0
![image](https://github.com/user-attachments/assets/eefb3b1a-56ca-432c-926b-8ebebe4548f8)
- And from gNB, it receive the attacker's Msg1 and start RA procedure but never receive Msg3
![image](https://github.com/user-attachments/assets/15a71bd7-6097-4f27-bfbe-3e4b75ce23fe)

##### 1.4.2.5. Modify gNB Alpha Value

<b>0.1. Change alpha value updater in `openair1/SCHED_NR/nr_prach_procedures.c`</b>
![image](https://github.com/user-attachments/assets/9f988cb8-42b2-4c5d-9d48-59cb3c9e87c7)

<b>0.2. Recompile gNB following [1.3.1.](#131-compile-gnb)</b>

##### 1.4.2.6. Modify gNB Delta Value

<b>0.1. Change delta value in `openair1/SCHED_NR/nr_prach_procedures.c`</b>
![image](https://github.com/user-attachments/assets/ee9f04b5-af40-4734-9aaa-b3ff0546e9eb)

##### 1.4.2.7. Modify Attacker Msg1 Energy

<b>0.1. add `--ue-txgain 60` parameter when running attacker (adjust value to adjust power)</b>

### 1.5. Results Compilation and Visualization

#### 1.5.1. Parameters Description

| Parameter | Description                                                                                         | (actor) Parameter in OAI    |
| --------- | --------------------------------------------------------------------------------------------------- | -------------- |
| $\alpha$  | Noise update factor parameter                                                                       | (gNB) Hardcoded, need to recompile after change    |
| $\delta$  | Msg1 to Noise dB Threshold                                                                       | (gNB) prach_dtx_threshold    |
| $j$       | Number of Random Access Occasion early start for attacker relative to UE                            | (attacker) No parameter, this is time of how long attacker start early |
| $T_a$     | Variability of Attack Period                                                                        | (gNB) prach_ConfigurationIndex<br>(attacker) prach_ConfigurationIndex, but need to hardcode so that attacker does not follow gNB's PBCH  |
| $P_{attacker}$     | Attacker's Msg1 dB Power                                                                        | (attacker) ue-txgain, should also be affected by distance of attacker to gNB  |

#### 1.5.2. Results

1. More early attacker’s Msg1 start relative to UE (bigger j) = Higher gNB noise threshold<br>
(all figures)
2. Attacker period decrease (more frequent attacker Msg1 transmissions) = Higher gNB noise threshold<br>
$\alpha = 0.12$,
$\delta = 12$
![image](https://github.com/user-attachments/assets/ca947927-df72-4891-ad96-ec4af4d1b499)
3. Attacker with higher power but less frequent interval (e.g., 55 dB with $T_a = 2$) = Higher gNB noise threshold > attacker with lower power but more frequent interval (e.g., 31.4 dB with $T_a = 1$)<br>
$\alpha = 0.12$,
$\delta = 12$
![image](https://github.com/user-attachments/assets/c7bf8154-9eb6-44c8-801a-d6bbf4854e53)
4. Low $\alpha$ in gNB = noise threshold at the gNB updates more slowly = increase UE access success<br>
$T_a = 1$,
$\delta = 12$
![image](https://github.com/user-attachments/assets/0e19a389-e3cb-4b82-919e-21fac7c6ad43)
5. Low $\delta$ in gNB = required UE power for Msg1 detection is reduced = increase UE access success<br>
$\alpha = 0.12$,
$T_a = 1$
![image](https://github.com/user-attachments/assets/d2b831c0-bbcc-4d43-b0c1-68e6129951a9)


