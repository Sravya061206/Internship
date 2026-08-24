# Vulnerability Scanner (CLI Script)

A simple Python script to detect common vulnerabilities in a web application or network.  
It scans for open ports, extracts service banners, identifies weak configurations or outdated versions, and queries the NVD CVE API for known vulnerabilities.

---

## Features
- **Port scanning**: Choose between common ports, a custom range, or a custom list.
- **Banner grabbing**: Dynamically extracts service and version information from open ports.
- **Weak configuration checks**: Flags insecure defaults (e.g., Telnet, anonymous FTP).
- **CVE lookup**: Queries NVD API for vulnerabilities against detected service/version.
- **Severity classification**: Uses CVSS scores to categorize vulnerabilities (High/Medium/Low).
- **Report generation**: Prints results to console and saves them to a `.txt` file.

---


---

## ⚙️ Installation

1. Clone or download the project.
2. Ensure Python 3.8+ is installed.
3. Install required dependency:
   ```bash
   pip install requests
   python port_scanner.py
