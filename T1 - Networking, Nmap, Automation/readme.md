# Task 01: Networking Fundamentals, Nmap Scanning, and Automation

## Scans Performed

### 1. TCP SYN Scan (Half-Open Scan)
```bash
nmap -sS 127.0.0.1 -oN syn_scan.txt
```
- Efficient and less intrusive  
- Does not complete TCP handshake  
- Used to identify open TCP services  

---

### 2. TCP Connect Scan
```bash
nmap -sT 127.0.0.1 -oN tcp_scan.txt
```
- Completes full TCP three-way handshake  
- More detectable than SYN scan  
- Useful when SYN scans are restricted  

---

### 3. UDP Scan
```bash
nmap -sU 127.0.0.1 -oN udp_scan.txt
```
- Identifies UDP-based services  
- Slower and less deterministic  
- Results may appear as `open|filtered`  

---

## Scan Findings

### Open TCP Ports
| Port | Protocol | Service |
|------|----------|---------|
| 80   | TCP | HTTP |
| 443  | TCP | HTTPS |
| 135  | TCP | MSRPC |
| 445  | TCP | SMB |
| 902  | TCP | VMware Service |
| 912  | TCP | VMware Service |

---

### UDP Ports (Open / Filtered)
| Port | Protocol | Service |
|------|----------|---------|
| 137  | UDP | NetBIOS |
| 500  | UDP | ISAKMP |
| 1900 | UDP | UPnP |
| 4500 | UDP | NAT-T |
| 5353 | UDP | mDNS |
| 5355 | UDP | LLMNR |

---

## Service & Security Analysis
- HTTP (80): Unencrypted traffic; vulnerable if misconfigured  
- HTTPS (443): Secure but application-risk dependent  
- SMB (445): High-risk if exposed; common lateral movement vector  
- MSRPC (135): Core Windows service; frequently abused internally  
- UDP Services: Discovery and VPN-related protocols; harder to assess  

---

## Network Diagram
- Created using draw.io  
- Shows Nmap scanner, target host (127.0.0.1), scan types, and identified services  

File: task01_network_diagram.png  

---

## Python Automation

### Script: nmap_automation.py
- Accepts target input  
- Executes TCP SYN scan  
- Extracts open ports and services  
- Generates structured scan report  

### Generated Report
File: scan_report.txt  

Includes timestamp, host state, open ports, and services  

---

## Files Included
```
├── nmap_automation.py
├── scan_report.txt
├── syn_scan.txt
├── tcp_scan.txt
├── udp_scan.txt
├── task01_network_diagram.png
└── README.md
```

---

## Key Learnings
- TCP scans give deterministic results  
- UDP scans require interpretation  
- Context matters more than raw ports  
- Documentation is critical  
- Automation enables scalability  

---

## Conclusion
This task demonstrates real-world SOC-style network scanning, analysis, visualization, and automation using Nmap and Python.

---

## Disclaimer
All scanning activities were performed on an authorized local system for educational purposes only.
