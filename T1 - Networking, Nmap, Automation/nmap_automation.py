import nmap
from datetime import datetime

# Initialize Nmap PortScanner object
scanner = nmap.PortScanner()

# Take target input from user
target = input("Enter target IP or hostname: ")

print(f"\n[+] Starting SYN scan on target: {target}\n")

# Perform SYN scan
scanner.scan(hosts=target, arguments="-sS")

# Prepare report file
report_file = "scan_report.txt"

with open(report_file, "w") as report:
    report.write("Nmap Automation Scan Report\n")
    report.write("=" * 30 + "\n")
    report.write(f"Scan Time: {datetime.now()}\n")
    report.write(f"Target: {target}\n\n")

    # Iterate through scanned hosts
    for host in scanner.all_hosts():
        report.write(f"Host: {host}\n")
        report.write(f"State: {scanner[host].state()}\n\n")

        # Check TCP ports
        if 'tcp' in scanner[host]:
            report.write("Open TCP Ports:\n")
            report.write("-" * 20 + "\n")

            for port in scanner[host]['tcp']:
                port_state = scanner[host]['tcp'][port]['state']
                service = scanner[host]['tcp'][port]['name']
                version = scanner[host]['tcp'][port]['version']

                if port_state == "open":
                    report.write(
                        f"Port: {port} | Service: {service} | Version: {version}\n"
                    )

        report.write("\n")

    report.write("Scan completed successfully.\n")

print(f"[+] Scan complete. Report saved as {report_file}")
