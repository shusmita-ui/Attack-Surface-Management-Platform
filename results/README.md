# Attack Surface Management Platform

## Overview

Attack Surface Management (ASM) Platform developed using Python for cybersecurity asset discovery and security assessment.

## Features

* Subdomain Discovery using Subfinder
* Live Host Detection using httpx
* Port Scanning
* Technology Detection
* Security Header Analysis
* SSL Certificate Analysis
* Risk Scoring
* PDF Report Generation
* SQLite Database Storage

## Technologies Used

* Python
* SQLite
* Subfinder
* httpx
* Requests
* ReportLab

## Project Workflow

Target Domain
→ Subdomain Discovery
→ Live Host Detection
→ Port Scanning
→ Technology Detection
→ Security Header Analysis
→ SSL Certificate Analysis
→ Risk Scoring
→ PDF Report Generation

## Installation

Install Python dependencies:

pip install -r requirements.txt

## Run

python main.py

## Output

The project generates:

* subdomains.txt
* live_hosts.txt
* ports.txt
* technologies.txt
* security_headers.txt
* ssl_report.txt
* risk_report.txt
* ASM_Report.pdf

## Author

Shusmita Pal
