# CodeAlpha Cyber Security Internship Projects

This package contains three beginner-friendly projects:
1. Basic Network Sniffer (Python)
2. Phishing Awareness Training (interactive HTML module)
3. Secure Coding Review (Python example, review report, and remediation)

## Safety and authorization
- Run packet capture only on a device/network you own or have explicit permission to monitor.
- The sniffer displays packet metadata and a short payload preview only. Payloads may contain private information; use the preview option only in an approved lab.
- Do not use these projects to intercept other people's communications, collect credentials, or access systems without permission.
- The phishing module is awareness-only. It does not send emails or collect passwords.

## Requirements
- Python 3.10+
- Task 1: `scapy` (`python -m pip install scapy`)
- Task 2: Any modern web browser
- Task 3: Python 3.10+ (standard library only)

## Project 1 — Basic Network Sniffer
### Run
Open a terminal in `Task1_Network_Sniffer`:
```bash
python -m pip install scapy
python network_sniffer.py --count 20
```
On some systems, packet capture requires administrator/root privileges and a supported capture driver (such as Npcap on Windows). Start with a short capture on your own test network.
Optional interface:
```bash
python network_sniffer.py --interface "Wi-Fi" --count 20
```
List interfaces:
```bash
python network_sniffer.py --list-interfaces
```
Optional payload preview (only in an authorized lab):
```bash
python network_sniffer.py --count 10 --show-payload
```

## Project 2 — Phishing Awareness Training
Open `Task2_Phishing_Awareness/index.html` in a browser. Read the examples and complete the quiz. The page is self-contained and works offline.

## Project 3 — Secure Coding Review
Run:
```bash
python Task3_Secure_Coding_Review/secure_example.py
python Task3_Secure_Coding_Review/test_secure_example.py
```
Read `review_report.md` for findings and recommendations.

## Suggested GitHub repository
Repository name: `CodeAlpha_CyberSecurity_Projects`
Suggested structure: upload this folder's contents to the repository root. Do not upload real packet captures, passwords, API keys, or private information.

## LinkedIn project post (edit before publishing)
I completed three hands-on cybersecurity learning projects as part of my CodeAlpha internship tasks:

- **Basic Network Sniffer:** used Python and Scapy to inspect packet metadata in an authorized lab.
- **Phishing Awareness Training:** created an interactive learning module covering common warning signs and safe reporting practices.
- **Secure Coding Review:** documented common input-validation and error-handling risks and demonstrated safer Python patterns.

These projects helped me strengthen my understanding of network protocols, security awareness, and secure coding practices. I focused on responsible testing and ethical use.

#CodeAlpha #CyberSecurity #Python #NetworkSecurity #PhishingAwareness #SecureCoding
