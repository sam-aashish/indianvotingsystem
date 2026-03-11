# Enhancing Voter Confidence in EVMs through Streamlit-Powered Interfaces

## Overview

This research project proposes a system to enhance voter confidence in Electronic Voting Machines (EVMs) by introducing a verification mechanism using Aadhaar authentication and SMS confirmation.

The system aims to reduce voter impersonation and increase transparency in the Indian electoral process through real-time verification and voter engagement.

This work was presented at the **2024 International Conference on Advancement in Electronics & Communication Engineering (AECE)**.

---
## Published Research

This research paper was presented at the **4th International Conference on Advancement in Electronics & Communication Engineering (AECE 2024).**

Title:
**Bridging the Gap: Enhancing Voter Confidence in EVMs through Streamlit-Powered Interfaces**

You can view the publication and details here:

Publication:
https://ieeexplore.ieee.org/document/10911058
## Research Problem

Although EVMs improved election efficiency, concerns remain about:

- voter impersonation
- lack of transparency
- voter verification after voting

Many voters cannot confirm whether their vote was actually recorded.

This project introduces a verification system that allows voters to validate their participation after voting.

---

## Proposed Solution

The system integrates:

- **Streamlit-based interfaces**
- **Aadhaar-linked voter verification**
- **SQLite voter database**
- **SMS confirmation using Twilio API**

After voting is recorded by the polling officer, the voter receives an SMS confirmation asking them to verify their vote.

If a voter replies indicating they did not vote, the system flags the case for investigation.

---

## System Architecture

The system consists of three major modules:

### Voter Registration Portal
Registers voters using:

- Voter ID
- Aadhaar Number
- Mobile Number
- Name

### Polling Officer Portal
Allows election officers to log votes and update voter status in the database.

### Election Commission Dashboard
Displays vote statistics and sends verification SMS to voters.

---

## Technologies Used

- Python
- Streamlit
- SQLite
- Twilio SMS API
- Data Visualization (Matplotlib)

---

## Repository Structure
source-code/ Python implementation
database/ SQLite voter database
screenshots/ UI and system screenshots
documentation/ Research paper and diagrams
---

## Security Features

The system includes several security measures:

- Encryption of voter data
- Aadhaar identity verification
- Secure communication using HTTPS
- Restricted access for election officers

These mechanisms help protect voter information and maintain election integrity.

---

## Results

Testing showed that the system can:

- detect potential voter impersonation
- improve voter trust in EVM systems
- provide transparency in the voting process

SMS-based verification allows voters to confirm whether their vote was legitimately cast.

---

## Research Paper

The complete research paper is available in the repository.

Title:

**Bridging the Gap: Enhancing Voter Confidence in EVMs through Streamlit-Powered Interfaces**

Presented at:

**AECE 2024 Conference**

---

## Author

Aashish Vishwakarma  
MCA Graduate  
AI Research | Data Analytics | GovTech Projects
