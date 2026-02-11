SOC Operations & Incident Response Practice Lab

This repository documents hands-on practice in Security Operations Center (SOC) workflows, alert triage, incident response, and digital evidence preservation.
The goal of this project is to simulate real-world security scenarios and build practical experience in detection, analysis, response, and reporting using industry-standard tools and frameworks.

📌 Project Overview
This lab environment was designed to simulate the full lifecycle of security operations:
  Alert prioritization and classification
  Incident triage and validation
  Threat intelligence correlation
  Evidence preservation and hashing
  Full attack-to-response simulation
All activities were performed inside a controlled virtual lab environment.

🛠 Tools & Technologies Used
  Wazuh (SIEM & alert monitoring)
  Metasploit Framework (attack simulation)
  CrowdSec (IP blocking & response)
  Velociraptor (forensic data collection)
  AlienVault OTX & VirusTotal (threat intelligence validation)
  Windows Server 2022 VM
  VMware Virtual Environment

📚 Core Concepts Practiced

1️⃣ Alert Prioritization
  Classified alerts into Critical / High / Medium / Low
  Applied risk-based thinking using CVSS-style scoring
  Mapped alerts to MITRE ATT&CK techniques

2️⃣ Incident Classification
  Categorized events (malware, brute force, phishing, etc.)
  Enriched alerts with metadata (IP, hostname, hash, timestamp)
  Applied structured incident labeling

3️⃣ Incident Response Lifecycle
  Followed a structured response model:
  Preparation
  Identification
  Containment
  Eradication
  Recovery
  Lessons Learned

🔎 Practical Implementations

Alert Management
  Built an alert classification matrix
  Prioritized mock alerts using risk scoring
  Drafted structured incident tickets
  Simulated escalation communication

Alert Triage Exercise
  Investigated a high-severity PowerShell execution alert
  Validated file hash using AlienVault OTX and VirusTotal
  Determined false positive through contextual analysis
  Documented triage reasoning and final decision

Evidence Preservation
  Collected volatile network data using Velociraptor
  Performed memory acquisition for forensic practice
  Generated SHA256 hash for integrity verification
  Maintained chain-of-custody documentation

🚨 Capstone: Full Alert-to-Response Simulation
An end-to-end attack scenario was executed:
  1. Attack Simulation
    Exploited a vulnerable service on a Metasploitable2 machine using Metasploit.
  2. Detection
    Wazuh generated security alerts related to suspicious activity.
  3. Triage & Analysis
    Alerts were analyzed and mapped to MITRE technique T1190 (Initial Access).
  4. Containment
    The affected system was isolated and attacker IP was blocked using CrowdSec.
  5. Reporting
    A structured incident report and executive summary were prepared.

🎯 Key Skills Demonstrated
  SOC workflow execution
  Alert triage & investigation
  Threat intelligence validation
  Digital evidence handling
  Incident documentation & reporting
  End-to-end attack simulation

📁 Repository Structure

This repository includes:
  Documentation (incident reports, triage notes, response templates)
  Evidence files (CSV exports, memory dump sample, hash records)
  Workflow explanations
  Screenshots and supporting artifacts

🚀 Purpose of This Repository
  This project serves as a practical security operations lab to:
  Strengthen real-world SOC skills
  Practice structured incident handling
  Improve analytical thinking in alert investigation
  Build documented proof of hands-on cybersecurity work
