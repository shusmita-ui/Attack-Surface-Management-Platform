from database import create_database
from recon import run_recon
from scanner import scan_ports
from technology_detector import detect_technologies
from security_headers import check_headers
from ssl_scanner import scan_ssl
from risk_scoring import calculate_risk
from report_generator import generate_report

create_database()

print("=" * 50)
print("ATTACK SURFACE MANAGEMENT PLATFORM")
print("=" * 50)

domain = input("\nEnter Domain: ")

run_recon(domain)

scan_ports()

detect_technologies()

check_headers()

scan_ssl()

calculate_risk()

generate_report()

print("\n[+] ASM Scan Completed Successfully")
print("[+] PDF Report Generated")