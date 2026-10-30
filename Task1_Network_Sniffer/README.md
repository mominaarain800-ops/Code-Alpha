# Task 1: Basic Network Sniffer

## Objective
Use Python and Scapy to inspect network packet metadata and learn how protocols move across a network.

## Features
- Captures a finite number of packets.
- Displays timestamp, protocol, source/destination IP, ports, TCP flags, and DNS query names when available.
- Supports an optional BPF capture filter.
- Payload preview is opt-in and limited to 32 bytes in hex.
- Does not save traffic to a file.

## Ethical use
Only capture traffic on your own device or a network where you have explicit permission. Payload previews can reveal private data, so leave them disabled unless required in a controlled lab.

## Run
```bash
python -m pip install -r requirements.txt
python network_sniffer.py --count 20
python network_sniffer.py --list-interfaces
python network_sniffer.py --interface "Wi-Fi" --count 10 --filter "tcp"
```
Interface names vary by operating system. On Windows, install Npcap if required. Packet capture may require elevated privileges.

## Sample output (illustrative)
```text
[14:20:03] TCP   192.168.1.10 -> 142.250.72.14 | ports=53122->443 | flags=S
[14:20:04] UDP   192.168.1.10 -> 192.168.1.1 | ports=53000->53 | dns_query=example.com
```
The sample IPs and domains are examples, not real capture results.
