#!/usr/bin/env python3
"""Beginner-friendly packet metadata sniffer for authorized lab use.

Captures packet headers/metadata. Payload preview is disabled by default.
Use only on networks and devices you own or have explicit permission to monitor.
"""
import argparse
import sys
from datetime import datetime

try:
    from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, DNS, DNSQR, get_if_list
except ImportError:
    print("Scapy is not installed. Run: python -m pip install scapy", file=sys.stderr)
    raise SystemExit(1)


def describe_packet(packet, show_payload=False):
    timestamp = datetime.now().strftime("%H:%M:%S")
    src = dst = "N/A"
    protocol = "OTHER"
    details = []

    if IP in packet:
        src, dst = packet[IP].src, packet[IP].dst
    elif IPv6 in packet:
        src, dst = packet[IPv6].src, packet[IPv6].dst

    if TCP in packet:
        protocol = "TCP"
        details.append(f"ports={packet[TCP].sport}->{packet[TCP].dport}")
        details.append(f"flags={packet[TCP].flags}")
    elif UDP in packet:
        protocol = "UDP"
        details.append(f"ports={packet[UDP].sport}->{packet[UDP].dport}")
    elif ICMP in packet:
        protocol = "ICMP"

    if DNS in packet and packet[DNS].qd and DNSQR in packet:
        try:
            query = packet[DNSQR].qname.decode("utf-8", errors="replace").rstrip(".")
            details.append(f"dns_query={query}")
        except Exception:
            details.append("dns_query=<unavailable>")

    line = f"[{timestamp}] {protocol:5} {src} -> {dst}"
    if details:
        line += " | " + " | ".join(details)

    if show_payload:
        # Limited preview for authorized lab troubleshooting; may expose sensitive data.
        try:
            raw = bytes(packet.payload)
            preview = raw[:32].hex(" ")
            if preview:
                line += f" | payload_preview_hex(first 32 bytes)={preview}"
        except Exception:
            line += " | payload_preview=<unavailable>"

    print(line)


def main():
    parser = argparse.ArgumentParser(description="Capture packet metadata in an authorized lab.")
    parser.add_argument("--interface", help="Capture interface name (default: Scapy chooses one)")
    parser.add_argument("--count", type=int, default=20, help="Number of packets to capture (default: 20)")
    parser.add_argument("--filter", dest="bpf_filter", default="", help="Optional BPF filter, e.g. 'tcp or udp'")
    parser.add_argument("--show-payload", action="store_true",
                        help="Show a short hex preview; use only in an authorized lab")
    parser.add_argument("--list-interfaces", action="store_true", help="List available interfaces and exit")
    args = parser.parse_args()

    if args.list_interfaces:
        print("\n".join(get_if_list()))
        return
    if args.count < 1:
        parser.error("--count must be at least 1")

    print("CodeAlpha Basic Network Sniffer")
    print("Safety: capture only traffic you are authorized to inspect.")
    print(f"Starting capture: count={args.count}, interface={args.interface or 'default'}")
    try:
        sniff(
            iface=args.interface,
            count=args.count,
            filter=args.bpf_filter or None,
            prn=lambda pkt: describe_packet(pkt, args.show_payload),
            store=False,
        )
    except PermissionError:
        print("Permission denied. Try an authorized elevated terminal and verify capture-driver setup.", file=sys.stderr)
        raise SystemExit(2)
    except OSError as exc:
        print(f"Capture failed: {exc}", file=sys.stderr)
        print("Check interface name, capture permissions, and platform driver (e.g. Npcap on Windows).", file=sys.stderr)
        raise SystemExit(3)
    print("Capture complete.")


if __name__ == "__main__":
    main()
