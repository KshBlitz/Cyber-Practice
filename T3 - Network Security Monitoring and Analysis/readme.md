# Task 03: Network Security Monitoring and Analysis

## Project Overview
This project focuses on real-world network security monitoring workflows used in Security Operations Centers (SOC).
The objective is to understand how malicious or suspicious network activity appears at the packet level and how it can be observed, detected, and validated using multiple defensive security tools.

The task combines:
- Passive traffic analysis
- Active intrusion detection
- Controlled attack simulation

This layered approach reflects how SOC analysts correlate data from different tools to accurately detect reconnaissance and early-stage attack behavior.

---

## Tools & Environment
- Host OS: Windows
- Analysis VM: Kali Linux
- Packet Analysis: Wireshark
- Intrusion Detection System: Snort (IDS mode)
- Packet Crafting & Simulation: Scapy
- Network Mode: Bridged Adapter

---

## Phase 1: Passive Network Traffic Analysis (Wireshark)

### Objective
- Observe live network traffic without interacting with it
- Identify protocol usage and baseline behavior
- Detect early indicators of suspicious activity

### What Was Done
- Captured live traffic on the active interface
- Applied protocol-based filters (TCP, UDP, ICMP)
- Analyzed packet behavior and communication patterns
- Isolated TCP SYN-only packets to identify reconnaissance-style activity

### Key Observations
- TCP dominated normal traffic (HTTP, HTTPS, SSH)
- UDP traffic observed mainly for DNS
- ICMP appeared only during diagnostic activity
- Repeated TCP SYN packets indicated potential scanning behavior

---

## Phase 2: Intrusion Detection (Snort IDS)

### Objective
- Actively monitor traffic in real time
- Detect suspicious patterns using IDS rules
- Generate alerts for reconnaissance behavior

### Configuration
- Snort configured in IDS (detection-only) mode
- Custom local rules added for:
  - TCP SYN packet detection
  - Port scan detection

### Detection Results
- Snort generated alerts for repeated SYN packets
- Port scanning behavior detected across multiple destination ports
- Alerts included source IP, destination IP, ports, protocol, and rule IDs

---

## Phase 3: Attack Simulation & Validation (Scapy)

### Objective
- Generate controlled malicious-like traffic
- Validate IDS rule effectiveness
- Simulate real reconnaissance behavior safely

### What Was Done
- Created a Python script using Scapy
- Generated TCP SYN packets targeting common ports
- Introduced delays to avoid packet flooding
- Executed script with elevated privileges

### Validation
- Scapy-generated SYN packets immediately triggered Snort alerts
- Alerts matched both SYN detection and port scan rules
- Confirmed end-to-end detection workflow

---

## Correlation & Analysis
- Wireshark provided visibility into packet-level behavior
- Snort provided real-time alerting
- Scapy provided controlled testing and validation

Correlation across all three tools confirmed that detected alerts were directly linked to observable packet behavior and were not false positives.

---

## Files Included
```
├── capture.pcapng
├── test_packets.py
├── snort.conf / local.rules
├── screenshots/
└── README.md
```

---

## Key Learnings
- Passive monitoring establishes baselines and reveals anomalies
- IDS detection depends on repeated patterns, not single packets
- TCP SYN scans are common early-stage attack techniques
- Correlating multiple tools improves detection accuracy
- Packet-level visibility is critical for SOC analysts
- Detection validation is essential in security operations

---

## Conclusion
This project demonstrates a complete SOC-style network monitoring workflow by combining packet analysis, intrusion detection, and controlled attack simulation.
It highlights how layered defensive tools work together to provide accurate and reliable threat detection.

---

## Disclaimer
All activities were performed in an authorized, isolated lab environment strictly for educational purposes.
