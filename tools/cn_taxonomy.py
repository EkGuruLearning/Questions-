# -*- coding: utf-8 -*-
"""
cn_taxonomy.py — the single source of truth for the 7-topic Computer Networks system.

Defines:
  * EXAMS        — Rajasthan Govt. exams this question bank serves.
  * TOPICS       — the 7 syllabus topics, each with sub-topics + classification keywords.
  * classify()   — content-based classifier: assigns a question to (topic, sub-topic).

Classification is done by CONTENT (keyword scoring), never by the unreliable
page headers printed inside the source PDFs.
"""

# ---------------------------------------------------------------------------
# Exams served (Computer Networks / Data Communication is a common subject)
# ---------------------------------------------------------------------------
EXAMS = [
    "RPSC Programmer",
    "RSMSSB Informatics Assistant (IA / Suchna Sahayak)",
    "RSMSSB School Administrator (SA)",
    "RSMSSB Data Entry / Computer Operator (DD)",
    "BCI — Basic Computer Instructor",
    "SCI — Senior Computer Instructor",
    "REET (Level 1 / Level 2 — Computer)",
    "RAS / Rajasthan Govt. (General) Exams",
]
EXAMS_LINE = "RPSC Programmer • RSMSSB IA • RSMSSB SA • Data Entry/DD • BCI • SCI • REET • RAS & other Rajasthan Govt. Exams"

# ---------------------------------------------------------------------------
# The 7 topics. Each sub-topic carries keywords used for content classification.
# ---------------------------------------------------------------------------
TOPICS = [
    {
        "num": 1, "key": "intro",
        "short": "Introduction of DC",
        "title": "Introduction of DC (Data Communication)",
        "note": "Data communication basics: components, characteristics, transmission modes, topology, network types, history.",
        "subtopics": [
            {"name": "DC Components & Protocol Basics",
             "note": "Message, Sender, Receiver, Transmission Medium, Protocol",
             "keywords": ["transmission medium", "sender", "receiver", "protocol", "message is", "data to be communicated", "set of rules", "physical path", "five components", "5 components"]},
            {"name": "Characteristics & Criteria",
             "note": "Delivery, Accuracy, Timeliness, Jitter; Performance, Reliability, Security",
             "keywords": ["delivery", "accuracy", "timeliness", "jitter", "reliability", "downtime", "failure frequency", "fault tolerance", "performance", "security", "criteria", "characteristic"]},
            {"name": "Transmission Mode",
             "note": "Simplex, Half-Duplex, Full-Duplex",
             "keywords": ["simplex", "half-duplex", "half duplex", "full-duplex", "full duplex", "double duplex", "direction of data", "transmission mode", "one way", "both ways", "keyboard", "monitor", "walkie", "telephone", "television broadcast"]},
            {"name": "Network Structure / Topology",
             "note": "Physical: Mesh, Star, Bus, Ring, Hybrid, Tree; Logical: IEEE 802",
             "keywords": ["topology", "mesh", "star topology", "bus topology", "ring topology", "hybrid", "tree topology", "physical topology", "logical topology", "ieee 802", "802.3", "802.5", "802.11", "collision domain", "backbone", "n(n-1)", "number of cables", "cables required"]},
            {"name": "Types of Networks",
             "note": "LAN, MAN, WAN, PAN, CAN, SAN; Internet, Intranet, Extranet; Point-to-Point, Multipoint; Client-Server, P2P",
             "keywords": ["lan", "man", "wan", "pan", "can", "san", "local area", "metropolitan", "wide area", "personal area", "campus area", "storage area", "internet", "intranet", "extranet", "point-to-point", "point to point", "multipoint", "client-server", "peer-to-peer", "peer to peer", "p2p", "bittorrent", "geographical", "covers a", "spans a", "network type", "types of network", "category of network"]},
            {"name": "Network History",
             "note": "ARPANET to today's network",
             "keywords": ["arpanet", "history", "first network", "1969", "1972", "1983", "tcp/ip adopted", "nsfnet", "world wide web", "www invented", "tim berners", "internet began", "evolution"]},
            {"name": "General Network Basics",
             "note": "WWW, E-mail, Protocols, Servers, Switching",
             "keywords": ["world wide web", "www", "e-mail", "email", "web server", "mail server", "file server", "print server", "packet switching", "circuit switching", "message switching", "web browser", "hypertext", "url", "http"]},
        ],
    },
    {
        "num": 2, "key": "models",
        "short": "Network Models (OSI & TCP-IP)",
        "title": "Network Models (OSI & TCP/IP)",
        "note": "OSI reference model (1984, 7 layers) and TCP/IP model (1972); layers, functions, comparison.",
        "subtopics": [
            {"name": "OSI Model Basics",
             "note": "7 layers, 1984, ISO, layer names & order",
             "keywords": ["osi", "iso", "1984", "seven layer", "7 layer", "7-layer", "reference model", "layers are", "order of layers", "physical layer", "data link layer", "network layer", "transport layer", "session layer", "presentation layer", "application layer", "which layer", "layer is responsible", "layer provides", "layer handles", "layer performs", "layer deals"]},
            {"name": "TCP/IP Model",
             "note": "TCP/IP (1972), 4/5 layers, ARPANET, protocols",
             "keywords": ["tcp/ip", "tcp ip", "1972", "four layer", "4 layer", "5 layer", "five layer", "link layer", "internet layer", "host-to-network", "network access layer", "doD model", "department of defense", "protocol stack", "protocol suite"]},
            {"name": "OSI vs TCP/IP & Layer Functions",
             "note": "Comparison, encapsulation, PDU, interfaces, services, protocols per layer",
             "keywords": ["comparison", "difference between", "encapsulation", "decapsulation", "pdu", "protocol data unit", "sdu", "interface between", "service provided", "segment", "packet", "frame", "header", "trailer", "which protocol works", "protocol at", "logical addressing", "physical addressing", "which layer does", "which layer is responsible", "layer provides", "layer offers"]},
        ],
    },
    {
        "num": 3, "key": "addressing",
        "short": "Addressing (MAC, IPv4, IPv6, Port, DNS)",
        "title": "Addressing (MAC, IPv4, IPv6, Port, DNS)",
        "note": "MAC (48-bit), IPv4 (32-bit), IPv6 (128-bit), classful/classless, CIDR, subnetting, port (16-bit), DNS/URL.",
        "subtopics": [
            {"name": "MAC Address",
             "note": "48-bit physical/hardware address, OUI, unicast/multicast/broadcast",
             "keywords": ["mac address", "physical address", "hardware address", "48 bit", "48-bit", "6 bytes", "oui", "organizationally unique", "unicast", "multicast", "broadcast address", "ff-ff-ff", "0a-01", "ethernet address", "burned-in", "bia"]},
            {"name": "IPv4 Addressing",
             "note": "32-bit, dotted decimal, classes A-E, network/host, private IP, special IPs",
             "keywords": ["ipv4", "ip address", "32 bit", "32-bit", "dotted decimal", "class a", "class b", "class c", "class d", "class e", "network address", "host address", "host id", "network id", "private ip", "public ip", "loopback", "127.0.0.1", "0.0.0.0", "255.255.255.255", "first byte", "first octet", "classful", "classless", "default mask", "default subnet"]},
            {"name": "Subnetting & CIDR",
             "note": "Subnet mask, CIDR notation, subnets, supernetting, hosts per subnet",
             "keywords": ["subnet", "subnetting", "cidr", "classless inter", "slash", "/24", "/26", "/27", "/28", "/29", "/30", "supernet", " supernetting", "number of subnets", "hosts per subnet", "number of hosts", "block size", "borrowed bits", "subnet mask", "wildcard", "prefix"]},
            {"name": "IPv6 Addressing",
             "note": "128-bit, hexadecimal, ::/0, link-local, unicast/anycast/multicast",
             "keywords": ["ipv6", "128 bit", "128-bit", "hexadecimal", "16 bytes", "colon", "fe80", "link-local", "link local", "unicast", "anycast", "global unicast", "::/", "ipv6 address", "next generation ip"]},
            {"name": "Port Numbers & DNS/URL",
             "note": "16-bit port, well-known ports, DNS, URL structure",
             "keywords": ["port number", "port address", "16 bit", "16-bit", "well-known", "well known", "ephemeral", "socket", "dns", "domain name", "domain name system", "url", "uniform resource locator", "top level domain", "tld", "maps domain", "host name", "ip address of"]},
        ],
    },
    {
        "num": 4, "key": "devices",
        "short": "Networking Devices",
        "title": "Networking Devices",
        "note": "Hub, Repeater, Modem, Switch, NIC, Bridge, Router, Brouter, Gateway, Firewall; layer & domains.",
        "subtopics": [
            {"name": "Hub / Repeater / Modem",
             "note": "Physical layer devices; amplify/regenerate; collision domain",
             "keywords": ["hub", "repeater", "modem", "amplifier", "regenerat", "physical layer device", "collision domain", "broadcast domain", "multiport repeater", "active hub", "passive hub", "modulator", "demodulator", "dumb device"]},
            {"name": "Switch / NIC / Bridge",
             "note": "Data link layer; MAC table; segments collision domains; NIC",
             "keywords": ["switch", "nic", "network interface card", "bridge", "layer 2", "layer two", "data link layer device", "mac table", "filtering", "forwarding", "mac address table", "separates collision", "collision domain", "full duplex", "cut-through", "store and forward", "network card", "adapter"]},
            {"name": "Router / Brouter",
             "note": "Network layer; routing table; path determination; brouter = bridge+router",
             "keywords": ["router", "brouter", "layer 3", "layer three", "network layer device", "routing table", "path determination", "routing", "default gateway", "hop", "hop count", "broadcast domain", "separates broadcast", "bridge router", "gateway of last resort"]},
            {"name": "Gateway / Firewall",
             "note": "Gateway = protocol converter; Firewall = security filter (packet/ACL)",
             "keywords": ["gateway", "firewall", "protocol converter", "default gateway", "packet filter", "access control list", "acl", "stateful", "stateless", "proxy", "nat", "network address translation", "security device", "block traffic", "allow traffic", "intrusion"]},
        ],
    },
    {
        "num": 5, "key": "medium",
        "short": "Transmission Medium",
        "title": "Transmission Medium",
        "note": "Guided (twisted pair, coaxial, fiber) & Unguided (radio, microwave, infrared); signals & performance.",
        "subtopics": [
            {"name": "Guided Media",
             "note": "Twisted pair (UTP/STP), coaxial, fiber optic; categories, connectors",
             "keywords": ["twisted pair", "twisted-pair", "utp", "stp", "coaxial", "coax", "fiber optic", "optical fiber", "fibre", "cat 5", "cat 5e", "cat 6", "cat 7", "rj-45", "rj45", "bnc", "st connector", "sc connector", "core", "cladding", "single mode", "single-mode", "multi mode", "multimode", "guided media", "guided medium"]},
            {"name": "Unguided Media",
             "note": "Radio, microwave, infrared; wireless propagation",
             "keywords": ["unguided", "unguided media", "wireless", "radio wave", "radio wave", "microwave", "infrared", "infrared", "line of sight", "propagation", "omnidirectional", "unidirectional", "electromagnetic spectrum", "frequency", "wavelength", "bandwidth of"]},
            {"name": "Signals & Performance",
             "note": "Analog/digital, attenuation, distortion, noise, bandwidth, throughput, Shannon",
             "keywords": ["attenuation", "distortion", "noise", "bandwidth", "throughput", "shannon", "channel capacity", "signal to noise", "snr", "decibel", "db", "analog signal", "digital signal", "data rate", "bit rate", "baud rate", "encoding", "manchester", "nrz", "ami", "modulation", "pcm", "quantiz", "sampling", "nyquist"]},
        ],
    },
    {
        "num": 6, "key": "osi",
        "short": "OSI Layers in Detail",
        "title": "OSI Layers in Detail",
        "note": "Physical; Data Link (flow/error control, framing, MAC); Network; Transport; Session; Presentation; Application.",
        "subtopics": [
            {"name": "Data Link: Flow & Error Control",
             "note": "Stop-and-Wait, Go-Back-N, Selective Repeat; Parity, Checksum, CRC, Hamming",
             "keywords": ["stop-and-wait", "stop and wait", "go-back-n", "go back n", "selective repeat", "sliding window", "flow control", "error control", "parity", "checksum", "crc", "cyclic redundancy", "hamming", "hamming code", "acknowledgement", "ack", "nak", "retransmit", "retransmission", "error detection", "error correction", "redundant", "polynomial", "generator polynomial"]},
            {"name": "Data Link: Framing & MAC",
             "note": "Framing, ALOHA, CSMA/CD, CSMA/CA, Ethernet",
             "keywords": ["framing", "frame", "character stuffing", "bit stuffing", "aloha", "pure aloha", "slotted aloha", "csma", "csma/cd", "csma cd", "csma/ca", "csma ca", "carrier sense", "collision", "jam signal", "backoff", "ethernet", "ieee 802.3", "token ring", "token bus", "token passing", "mac sublayer", "multiple access", "nav", "network allocation vector"]},
            {"name": "Network Layer",
             "note": "IPv4/IPv6 headers, routing: RIP, OSPF, BGP; ICMP, ARP, RARP, DHCP",
             "keywords": ["ipv4 header", "ipv6 header", "header field", "ttl", "time to live", "fragmentation", "fragment offset", "total length", "identification", "rip", "routing information protocol", "ospf", "open shortest path", "bgp", "border gateway", "icmp", "internet control message", "arp", "address resolution protocol", "rarp", "reverse arp", "dhcp", "dynamic host", "ping", "traceroute", "routing algorithm", "distance vector", "link state", "unicast routing", "multicast routing"]},
            {"name": "Transport Layer",
             "note": "TCP, UDP, SCTP; segment, ports, connection, 3-way handshake",
             "keywords": ["tcp", "udp", "sctp", "transmission control protocol", "user datagram", "segment", "connection-oriented", "connection oriented", "connectionless", "connection less", "three-way handshake", "3-way handshake", "three way handshake", "syn", "ack", "fin", "sequence number", "acknowledgement number", "window size", "flow control", "congestion", "port", "socket", "multiplexing", "demultiplexing", "well-known port"]},
            {"name": "Session, Presentation & Application",
             "note": "Session/Presentation functions; HTTP/HTTPS, SMTP/POP/IMAP/MIME, FTP/TELNET, DNS",
             "keywords": ["session layer", "presentation layer", "application layer", "http", "https", "smtp", "pop", "pop3", "imap", "mime", "ftp", "telnet", "dns", "ssh", "web browser", "web page", "email", "mail", "file transfer", "remote login", "encryption", "compression", "translation", "dialogue control", "synchronization", "checkpoint", "domain name", "url", "web", "hypertext"]},
        ],
    },
    {
        "num": 7, "key": "security",
        "short": "Network Security",
        "title": "Network Security",
        "note": "IDS/IPS, Cryptography, IPSec (transport/tunnel mode), VPN, Firewall, authentication.",
        "subtopics": [
            {"name": "Cryptography",
             "note": "Symmetric/asymmetric, cipher, keys, digital signature",
             "keywords": ["cryptography", "encryption", "decryption", "cipher", "plaintext", "ciphertext", "symmetric", "asymmetric", "public key", "private key", "secret key", "shared key", "rsa", "des", "aes", "digital signature", "hash", "md5", "sha", "key exchange", "diffie", "confidentiality", "integrity", "non-repudiation", "nonrepudiation", "substitution", "transposition", "steganography", "cryptanalysis"]},
            {"name": "IDS / IPS / Firewall",
             "note": "Intrusion detection/prevention, firewall types, VPN",
             "keywords": ["ids", "intrusion detection", "ips", "intrusion prevention", "firewall", "vpn", "virtual private network", "packet filter", "proxy", "stateful", "stateless", "nat", "network address translation", "access control", "honeypot", "malware", "virus", "worm", "trojan", "ransomware", "phishing", "spoofing", "dos", "ddos", "denial of service", "antivirus", "security threat", "attack", "intrusion", "audit", "log"]},
            {"name": "IPSec & Security Protocols",
             "note": "IPSec transport/tunnel mode, AH, ESP, SSL/TLS, PGP, WPA2",
             "keywords": ["ipsec", "ip sec", "transport mode", "tunnel mode", "ah protocol", "authentication header", "esp", "encapsulating security", "ssl", "tls", "ssl/tls", "https", "pgp", "pretty good privacy", "wpa", "wpa2", "wep", "wifi security", "security protocol", "secure socket", "handshake", "certificate", "ca ", "certificate authority", "digital certificate"]},
        ],
    },
]

def _norm(text):
    return " " + " ".join(str(text).lower().split()) + " "

import re
def _kw_count(text, kw):
    """Count keyword matches NOT inside a larger alphanumeric word (word-boundary)."""
    kw = kw.strip()
    if not kw:
        return 0
    pat = r"(?<![a-z0-9])" + re.escape(kw) + r"(?![a-z0-9])"
    return len(re.findall(pat, text))

def classify(text):
    """Content-based classification. Returns (topic_num, subtopic_name).
    text = question + options (English). Scoring by keyword hits.
    Score is computed at TOPIC level (sum across the topic's sub-topics) so that
    several related keywords in one topic beat a single stray hit in another."""
    t = _norm(text)
    best_topic = (None, -1, None, -1)   # (num, topic_total, best_sub_name, best_sub_score)
    for topic in TOPICS:
        topic_total = 0
        best_sub = (None, -1)
        for sub in topic["subtopics"]:
            s = 0
            for kw in sub["keywords"]:
                s += _kw_count(t, kw)
            topic_total += s
            if s > best_sub[1]:
                best_sub = (sub["name"], s)
        if topic_total > best_topic[1]:
            best_topic = (topic["num"], topic_total, best_sub[0], best_sub[1])
    if best_topic[1] <= 0:
        return (None, "General")
    return (best_topic[0], best_topic[2])

def topic_by_num(n):
    for t in TOPICS:
        if t["num"] == n:
            return t
    return None

def all_subtopic_names(n):
    t = topic_by_num(n)
    return [s["name"] for s in t["subtopics"]] if t else []

if __name__ == "__main__":
    # quick self-test
    tests = [
        ("Which OSI layer is responsible for logical addressing? Data Link Network Transport Application", (2, None)),
        ("A MAC address is of how many bits? 16 32 48 64", (3, None)),
        ("Which device operates at the network layer? Hub Switch Router Repeater", (4, None)),
        ("Stop-and-Wait is a ___ control technique. flow error framing routing", (6, None)),
        ("IPSec works in transport mode and ___ mode. tunnel session application", (7, None)),
        ("The physical path over which a message travels is called? Path Medium Protocol Route", (1, None)),
        ("Optical fiber cable works on the principle of? total internal reflection refraction diffraction dispersion", (5, None)),
    ]
    for q, exp in tests:
        tn, sn = classify(q)
        print(f"topic={tn} sub={sn!r:45s} expected_topic={exp[0]}  {'OK' if tn==exp[0] else 'CHECK'}  | {q[:50]}")
