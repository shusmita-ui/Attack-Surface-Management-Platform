import subprocess
import os

from database import save_subdomains
from database import save_live_hosts


def run_recon(domain):

    os.makedirs("results", exist_ok=True)

    print("\n[+] Running Subfinder...")

    subfinder_result = subprocess.run(
        ["subfinder.exe", "-d", domain],
        capture_output=True,
        text=True
    )

    with open("results/subdomains.txt", "w") as file:
        file.write(subfinder_result.stdout)

    subdomains = subfinder_result.stdout.strip().splitlines()

    save_subdomains(subdomains)

    print(f"[+] Found {len(subdomains)} subdomains")

    print("\n[+] Running httpx...")

    httpx_result = subprocess.run(
        [
            "httpx.exe",
            "-l",
            "results/subdomains.txt"
        ],
        capture_output=True,
        text=True
    )

    with open("results/live_hosts.txt", "w") as file:
        file.write(httpx_result.stdout)

    live_hosts = httpx_result.stdout.strip().splitlines()

    save_live_hosts(live_hosts)

    print("\n===== LIVE HOSTS =====\n")

    for host in live_hosts:
        print(host)

    print("\n" + "=" * 50)
    print(f"Total Subdomains : {len(subdomains)}")
    print(f"Total Live Hosts : {len(live_hosts)}")
    print("=" * 50)