from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report():

    print("\n[+] Generating PDF Report...\n")

    pdf = SimpleDocTemplate(
        "ASM_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Attack Surface Management Report",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 12))

    files = [
        "results/subdomains.txt",
        "results/live_hosts.txt",
        "results/ports.txt",
        "results/technologies.txt",
        "results/security_headers.txt",
        "results/ssl_report.txt",
        "results/risk_report.txt"
    ]

    for file_name in files:

        try:

            with open(
                file_name,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                data = file.read()

                heading = Paragraph(
                    file_name,
                    styles["Heading2"]
                )

                body = Paragraph(
                    data.replace("\n", "<br/>"),
                    styles["BodyText"]
                )

                content.append(heading)

                content.append(body)

                content.append(PageBreak())

        except:

            pass

    pdf.build(content)

    print(
        "[+] ASM_Report.pdf Generated Successfully"
    )