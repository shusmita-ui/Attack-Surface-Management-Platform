import socket

from database import save_port


def scan_ports():

    print("\n[+] Running Fast Port Scan...\n")

    ports_to_scan = [
        80,
        443,
        8080,
        8443
    ]

    with open("results/live_hosts.txt", "r") as file:
        hosts = file.read().splitlines()

    output = []

    total_open_ports = 0

    for host in hosts:

        host = host.replace("https://", "")
        host = host.replace("http://", "")

        output.append(f"\n========== {host} ==========\n")

        for port in ports_to_scan:

            try:

                sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                sock.settimeout(0.3)

                result = sock.connect_ex(
                    (host, port)
                )

                if result == 0:

                    output.append(
                        f"Port {port} OPEN\n"
                    )

                    save_port(host, port)

                    total_open_ports += 1

                sock.close()

            except:
                pass

    with open("results/ports.txt", "w") as file:
        file.writelines(output)

    print(f"[+] Open Ports Found : {total_open_ports}")
    print("[+] Results saved to results/ports.txt")
    print("[+] Port Scan Completed")