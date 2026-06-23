import requests


def detect_technologies():

    print("\n[+] Detecting Technologies...\n")

    with open("results/live_hosts.txt", "r") as file:
        hosts = file.read().splitlines()

    report = []

    for host in hosts:

        try:

            response = requests.get(
                host,
                timeout=5
            )

            headers = response.headers

            report.append(
                f"\nHost: {host}\n"
            )

            if "Server" in headers:
                report.append(
                    f"Server: {headers['Server']}\n"
                )

            if "X-Powered-By" in headers:
                report.append(
                    f"Technology: {headers['X-Powered-By']}\n"
                )

        except Exception as e:

            report.append(
                f"\nHost: {host}\nError: {e}\n"
            )

    with open(
        "results/technologies.txt",
        "w"
    ) as file:

        file.writelines(report)

    print(
        "[+] Results saved to results/technologies.txt"
    )