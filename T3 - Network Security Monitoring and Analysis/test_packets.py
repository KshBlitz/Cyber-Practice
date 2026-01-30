"""
test_packets.py

This script uses Scapy to generate TCP SYN packets in order to
simulate basic network attacks such as SYN scanning / port scanning.

The generated traffic is intended to trigger Snort IDS rules
configured to detect:
1. SYN packets
2. Potential port scan activity
"""

from scapy.all import IP, TCP, send
from typing import List
import time


def generate_syn_packets(target_ip: str, ports: List[int]) -> None:
    """
    Sends TCP SYN packets to multiple destination ports.

    Args:
        target_ip (str): Target IP address.
        ports (List[int]): List of destination ports to scan.
    """
    print("[*] Starting SYN packet generation...")

    for port in ports:
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        send(packet, verbose=False)
        print(f"[+] Sent SYN packet to port {port}")
        time.sleep(1)

    print("[*] SYN packet generation completed.")


if __name__ == "__main__":
    # Target is localhost for safe testing
    TARGET_IP = "127.0.0.1"

    # Common ports used to simulate a port scan
    TARGET_PORTS = [21, 22, 25, 80, 443]

    generate_syn_packets(TARGET_IP, TARGET_PORTS)
