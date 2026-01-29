
````md
# Mini Project 1: Networking Fundamentals, Nmap Scanning, and Automation

## Overview
This mini project focuses on understanding core networking fundamentals and applying them through practical network scanning using Nmap. The project also includes basic automation using Python to demonstrate how repetitive security tasks can be streamlined in real-world cybersecurity environments.

All activities were performed in a controlled and authorized local environment following ethical security practices.

---

## Objectives
- Understand fundamental networking concepts such as IP addressing, ports, and protocols
- Perform network discovery and port scanning using Nmap
- Analyze TCP and UDP scan results
- Identify exposed services and assess potential security risks
- Automate network scanning using Python
- Practice structured documentation used in cybersecurity and SOC operations

---

## Target Environment
- Target Type: Local Machine  
- Target IP Address: 127.0.0.1 (localhost)  
- Operating System: Windows  
- Scan Scope: Authorized local testing only  

Using the loopback address ensures all scans remain within a safe and ethical testing environment.

---

## Tools and Technologies Used
- Nmap – Network discovery and security auditing
- Python – Automation scripting
- python-nmap – Python wrapper for Nmap
- Command Line Interface (CLI)
- draw.io – Network diagram visualization

---

## Nmap Scans Performed

### TCP SYN Scan (Half-Open Scan)
```bash
nmap -sS 127.0.0.1
````

This scan initiates a TCP connection without completing the full handshake. It is efficient, faster, and commonly used for identifying open TCP ports.

---

### TCP Connect Scan

```bash
nmap -sT 127.0.0.1
```

This scan completes the full TCP three-way handshake. It is more detectable and is typically used when SYN scans are restricted or administrative privileges are unavailable.

---

### UDP Scan

```bash
nmap -sU 127.0.0.1
```

This scan identifies UDP-based services. Due to the connectionless nature of UDP, results may appear as open or filtered.

---

## Scan Findings

### Open TCP Services

* Port 80 – HTTP
* Port 443 – HTTPS
* Port 135 – MSRPC
* Port 445 – SMB
* Port 902 – VMware Service
* Port 912 – VMware Service

---

### UDP Services (Open or Filtered)

* Port 137 – NetBIOS
* Port 500 – ISAKMP
* Port 1900 – UPnP
* Port 4500 – NAT-T
* Port 5353 – mDNS
* Port 5355 – LLMNR

The results demonstrate how multiple services can be exposed even on a local system by default.

---

## Automation Using Python

To enhance efficiency and demonstrate automation, a Python script was developed using the python-nmap library. The script automates the execution of an Nmap TCP SYN scan and generates a structured scan report.

### Automation Features

* Accepts a target IP address as input
* Executes a TCP SYN scan
* Extracts open ports and associated services
* Generates a readable scan report automatically

---

## Files Generated

* Python Script: nmap_automation.py
* Automated Scan Report: scan_report.txt
* Detailed Report: Task_01_Report.pdf
* Network Diagram: task01_network_diagram.png

---

## Project Structure

```
Mini-Project-1/
│── nmap_automation.py
│── scan_report.txt
│── Task_01_Report.pdf
│── task01_network_diagram.png
│── README.md
```

---

## Key Learnings

* Differences between TCP and UDP scanning behavior
* Importance of contextual interpretation of scan results
* Not all exposed services indicate misconfiguration
* Value of clear and structured documentation
* Benefits of automation in cybersecurity workflows

---

## Ethical Disclaimer

All scanning activities were performed only on an authorized local machine. Unauthorized scanning of systems or networks without permission is illegal and unethical.

---

## Conclusion

This mini project demonstrates the practical application of networking fundamentals, network scanning techniques, and basic automation. It highlights the importance of combining technical tools with analytical thinking, documentation, and ethical practices in real-world cybersecurity operations.


