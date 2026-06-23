import ssl
import socket
from datetime import datetime

def scan_ssl():

    print("\n[+] Checking SSL Certificates...\n")

    with open("results/live_hosts.txt", "r") as file:
        hosts = file.read().splitlines()

    report = []

    for host in hosts:

        host = host.replace("https://", "")
        host = host.replace("http://", "")

        try:

            context = ssl.create_default_context()

            with socket.create_connection((host, 443), timeout=5) as sock:
                with context.wrap_socket(
                    sock,
                    server_hostname=host
                ) as ssock:

                    cert = ssock.getpeercert()

                    issuer = dict(
                        x[0] for x in cert["issuer"]
                    )

                    expiry = cert["notAfter"]

                    report.append(
                        f"\nHost: {host}\n"
                    )

                    report.append(
                        f"Issuer: {issuer.get('organizationName', 'Unknown')}\n"
                    )

                    report.append(
                        f"Expiry: {expiry}\n"
                    )

        except Exception as e:

            report.append(
                f"\nHost: {host}\nError: {e}\n"
            )

    with open(
        "results/ssl_report.txt",
        "w"
    ) as file:

        file.writelines(report)

    print(
        "[+] Results saved to results/ssl_report.txt"
    )