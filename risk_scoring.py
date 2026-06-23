def calculate_risk():

    print("\n[+] Calculating Risk Score...\n")

    score = 0

    report = []

    # Security Headers Analysis
    try:

        with open(
            "results/security_headers.txt",
            "r"
        ) as file:

            data = file.read()

            if "Content-Security-Policy" in data:
                score += 10

            if "Strict-Transport-Security" in data:
                score += 15

            if "X-Frame-Options" in data:
                score += 10

            if "X-Content-Type-Options" in data:
                score += 10

    except:
        pass

    # Port Analysis
    try:

        with open(
            "results/ports.txt",
            "r"
        ) as file:

            data = file.read()

            if "8080" in data:
                score += 20

            if "21" in data:
                score += 25

            if "22" in data:
                score += 10

    except:
        pass

    # SSL Analysis
    try:

        with open(
            "results/ssl_report.txt",
            "r"
        ) as file:

            data = file.read()

            if "Error" in data:
                score += 25

    except:
        pass

    if score <= 20:
        severity = "LOW"

    elif score <= 50:
        severity = "MEDIUM"

    else:
        severity = "HIGH"

    report.append(
        f"Risk Score : {score}\n"
    )

    report.append(
        f"Severity : {severity}\n"
    )

    with open(
        "results/risk_report.txt",
        "w"
    ) as file:

        file.writelines(report)

    print(f"Risk Score : {score}")
    print(f"Severity : {severity}")

    print(
        "[+] Results saved to results/risk_report.txt"
    )