import requests

def check_headers():

    print("\n[+] Checking Security Headers...\n")

    with open("results/live_hosts.txt", "r") as file:
        hosts = file.read().splitlines()

    report = []

    security_headers = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    for host in hosts:

        try:

            response = requests.get(
                host,
                timeout=5
            )

            headers = response.headers

            report.append(f"\nHost: {host}\n")

            missing = []

            for header in security_headers:

                if header not in headers:
                    missing.append(header)

            if missing:

                report.append("Missing Headers:\n")

                for item in missing:
                    report.append(f"- {item}\n")

            else:

                report.append(
                    "All Security Headers Present\n"
                )

        except Exception as e:

            report.append(
                f"\nHost: {host}\nError: {e}\n"
            )

    with open(
        "results/security_headers.txt",
        "w"
    ) as file:

        file.writelines(report)

    print(
        "[+] Results saved to results/security_headers.txt"
    )