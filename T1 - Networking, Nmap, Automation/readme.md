Mini Project 1
Networking Fundamentals, Nmap Scanning & Automation

OVERVIEW
This mini project demonstrates the practical application of basic networking concepts through network scanning using Nmap and simple automation using Python. The work focuses on understanding how services are exposed on a system and how scan results are interpreted from a security perspective.

All activities were performed in a controlled and authorized local environment.

OBJECTIVES
• Understand IP addressing, ports, and protocols
• Perform TCP and UDP network scans using Nmap
• Identify exposed network services
• Automate scanning tasks using Python
• Practice professional documentation

TARGET ENVIRONMENT
• Target Type: Local Machine
• IP Address: 127.0.0.1 (localhost)
• Operating System: Windows
• Scope: Authorized local testing only

TOOLS USED
• Nmap
• Python
• python-nmap
• Command Line Interface
• draw.io

SCANS PERFORMED

TCP SYN Scan
Used to quickly identify open TCP ports without completing a full handshake.

TCP Connect Scan
Used when SYN scans are restricted; completes the full TCP handshake.

UDP Scan
Used to identify UDP-based services; results may appear as open or filtered.

KEY FINDINGS

Open TCP Services
• HTTP (80)
• HTTPS (443)
• MSRPC (135)
• SMB (445)
• VMware Services (902, 912)

UDP Services (Open / Filtered)
• NetBIOS (137)
• ISAKMP (500)
• UPnP (1900)
• NAT-T (4500)
• mDNS (5353)
• LLMNR (5355)

These results show that multiple services can be exposed even on a local system by default.

AUTOMATION
A Python script was created to automate an Nmap TCP SYN scan and generate a structured scan report automatically.

PROJECT FILES
• nmap_automation.py
• scan_report.txt
• Task_01_Report.pdf
• task01_network_diagram.png

KEY LEARNINGS
• TCP and UDP behave differently during scanning
• Scan results must be interpreted in context
• Service exposure does not always mean misconfiguration
• Automation improves efficiency and consistency

ETHICAL DISCLAIMER
All scans were conducted on an authorized local system. Unauthorized scanning of networks or systems is illegal and unethical.

CONCLUSION
This mini project builds a foundational understanding of networking, network scanning, and automation, which are essential skills for cybersecurity and SOC operations.
