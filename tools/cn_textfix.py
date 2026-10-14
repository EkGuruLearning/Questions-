# -*- coding: utf-8 -*-
"""English fixes for explanations written only in Hindi (duplicated into both
language slots) — user 'fix-all explanations' pass, Oct 2026.

Rule: exp/wr/nk slot [0] = English, slot [1] = Hindi. Jo 97 texts Hindi script
mein dono slots mein the, unke liye English yahan hai; Hindi slot as-is rehta hai.
Lookup is by exact source text (map built from the data modules by location),
so the data files are NOT mutated on disk — every builder calls
`normalize_module(m)` right after loading a topic module.
"""
import importlib.util
import os

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# (topic, section_idx, question_idx, field) -> English rendering
EN_BY_LOC = {
    (1, 0, 16, "nk"): "This is the network on which TCP/IP was later installed — the grandmother of the Internet.",
    (1, 1, 15, "wr"): "A channel's capacity is measured as bandwidth — how many frequencies/bits per second are possible.",
    (1, 4, 6, "nk"): "Remember: PAN < LAN < MAN < WAN (smallest to largest).",
    (1, 4, 32, "nk"): "VoIP = the new Internet form of the old telephone voice.",
    (3, 1, 29, "wr"): "The RFC-1918 private blocks are 10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16. 11.0.0.1 falls in none of these blocks, so it is a public IP — not private.",
    (3, 3, 8, "wr"): "Unlike IPv4's 32 bits, IPv6 addresses are 128 bits long — that is why IPv6 has no address shortage.",
    (4, 0, 7, "wr"): "A repeater regenerates (amplifies and reshapes) the weakening signal — that is why it is what we install for distance problems.",
    (5, 0, 23, "nk"): "Media = the path; Hertz = the frequency/speed measure. This distinction is what is being asked.",
    (6, 0, 7, "nk"): "Error = putting right; Flow = maintaining balance. Both are separate jobs.",
    (6, 0, 8, "nk"): "Flow control = the balance between sender and receiver; this definition is asked again and again in exams.",
    (6, 0, 12, "nk"): "Because of this waiting, its name became 'Stop-and-Wait'.",
    (6, 0, 14, "wr"): "Stop-and-Wait has window size 1 — only one frame can be out without an ACK.",
    (6, 0, 15, "wr"): "Waiting after every frame leaves the line idle — efficiency drops sharply, especially on long-distance links.",
    (6, 0, 17, "wr"): "If the ACK does not arrive, the sender's timeout timer fires and it retransmits that frame.",
    (6, 0, 19, "nk"): "GBN = 'from where you slipped, start again' — in Selective Repeat only the wrong frame is resent.",
    (6, 0, 20, "nk"): "GBN = Go Back N — everything up to N is resent; SR = only the wrong one.",
    (6, 0, 21, "wr"): "A GBN receiver wants only the next in-order frame — when frame 2 is lost, 3 and 4 are out-of-order, so they are discarded.",
    (6, 0, 23, "nk"): "The reverse of the question above — memorise the formula both ways.",
    (6, 0, 26, "wr"): "Selective Repeat resends only the lost frames and also buffers out-of-order frames — bandwidth utilisation is the highest.",
    (6, 0, 28, "wr"): "Align the two codes and count differing bits: positions 2, 5, 7 and 8 differ — 4 differences in all. Hamming distance = number of differing bits = 4.",
    (6, 0, 29, "wr"): "XOR gives 1 where the bits differ — counting the 1s gives the Hamming distance.",
    (6, 0, 31, "wr"): "The extra bits are called redundancy — overhead added on top of the data that helps catch errors.",
    (6, 0, 31, "nk"): "Redundancy = 'extra bits sent on purpose' — this is what makes error control possible.",
    (6, 0, 33, "wr"): "A parity bit adds one extra bit with every byte so that the count of 1s stays even/odd.",
    (6, 0, 35, "wr"): "In simple parity, when an odd number of bits flip, the parity changes and the error is caught; an even number of errors stays hidden.",
    (6, 0, 35, "nk"): "Parity catches odd errors and misses even ones — that is its limit.",
    (6, 0, 45, "wr"): "If (1 + x), i.e. x + 1, is a factor of G(x), then every codeword has an even number of 1s — so odd errors are caught.",
    (6, 0, 49, "nk"): "GATE 2015 key (d) 20000 km/s. Getting the speed by inverting the formula — that is the trick of this question.",
    (6, 1, 0, "wr"): "The flag pattern (e.g. HDLC's 01111110) can also appear inside data — to prevent confusion, a 0 is stuffed after every five 1s in the data (bit stuffing).",
    (6, 1, 1, "wr"): "In the user (data) stream, after five consecutive 1s a 0 is inserted so that the data can be told apart from the flag.",
    (6, 1, 1, "nk"): "Stuffing is always done in DATA, never in the flag; in byte stuffing 0x7D follows 0x7E.",
    (6, 1, 2, "wr"): "As soon as a collision is detected, all stations send a Jam signal so that the others know at once and the line clears.",
    (6, 1, 2, "nk"): "Jam = the siren shouting 'a collision happened!'. Preamble = announcement that a frame is starting.",
    (6, 1, 3, "nk"): "Remember: after the Preamble come the RECEIVER's address (Destination) first, then the sender's — the rest later.",
    (6, 1, 5, "nk"): "The whole frame ranges 64–1518 bytes; the data 46–1500. This pair is asked often.",
    (6, 1, 6, "nk"): "MTU = the data limit; 1518 = the whole frame limit. Don't confuse the two.",
    (6, 1, 7, "wr"): "In CSMA/CD the sender must detect collisions while transmitting — so the frame must be long enough for the signal to complete a round trip. That is the 64-byte limit.",
    (6, 1, 9, "wr"): "The MAC sub-layer's main job is controlling access to the channel (medium) — who transmits when.",
    (6, 1, 10, "wr"): "In Slotted ALOHA, time is divided into slots and transmission starts only at a slot boundary — so all nodes must be synchronised.",
    (6, 1, 10, "nk"): "Pure ALOHA = send whenever you like; Slotted = send only when the slot clock says so.",
    (6, 1, 15, "wr"): "CSMA/CD's job is to detect collisions and handle them — so frames on a shared medium either avoid collisions or are resent after one.",
    (6, 1, 19, "wr"): "NAV — the Wi-Fi (802.11 CSMA/CA) timer that tells how long the medium will stay busy; other stations keep quiet that long.",
    (6, 1, 21, "wr"): "In reservation protocols, stations first reserve their slot, then transmit in turn without collisions.",
    (6, 1, 21, "nk"): "Reservation = book first, travel later — contention (ALOHA/CSMA) has no booking.",
    (6, 1, 22, "wr"): "In Token Ring the token circles station to station and only its holder transmits — this is a Round Robin (turn-by-turn) method.",
    (6, 1, 25, "wr"): "This statement is reversed — a Bridge uses MAC addresses and a Router uses IP addresses. So this is the 'not correct' option.",
    (6, 1, 26, "wr"): "Building the cell header is the ATM layer's job — the AAL splits/joins user data into cells and handles error/delay.",
    (6, 2, 7, "wr"): "Fragment Offset is 13 bits — it tells where the fragment sits inside the original datagram.",
    (6, 2, 8, "wr"): "The More Fragments (MF) flag says more fragments are coming, and the Fragment Offset says where to place this one — reassembly uses these two.",
    (6, 2, 9, "wr"): "Fragmentation means breaking a large packet into small pieces so they can pass over a link with a small MTU on the way.",
    (6, 2, 12, "wr"): "TTL (Time To Live) is the packet's lifetime — it drops by 1 at every hop; at 0 the packet is discarded. This is what stops routing loops.",
    (6, 2, 12, "nk"): "TTL = loop-stopper. It is also what runs traceroute (different TTLs map the path).",
    (6, 2, 16, "wr"): "OSPF (a link-state protocol) keeps a full map of every router and runs Dijkstra's algorithm for the shortest path.",
    (6, 2, 18, "wr"): "In RIP, hop count is valid up to 15 — 16 means 'unreachable'. That is why RIP does not suit large networks.",
    (6, 2, 19, "wr"): "Split horizon (don't advertise a route back where you learned it) and poison reverse (declare the route as 16 hops) — both are loop-stopping techniques.",
    (6, 2, 20, "wr"): "In distance vector protocols, bad news keeps circulating among neighbours and hop counts keep rising — this is the count-to-infinity problem.",
    (6, 2, 20, "nk"): "Count-to-infinity is the signature of DV; link-state is free of it (but uses more memory).",
    (6, 2, 23, "wr"): "Dynamic routing protocols find paths themselves, share updates and agree on the topology — all three jobs are done.",
    (6, 2, 26, "wr"): "Traceroute shows every router (hop) on the path and its delay — by sending packets with different TTLs.",
    (6, 2, 31, "wr"): "One station transmits (p) while the other n−1 stay silent (1−p)ⁿ⁻¹; there are n such ways — hence n·p·(1−p)ⁿ⁻¹.",
    (6, 2, 32, "wr"): "TTL drops by 1 at each hop; at 0 the packet is discarded — this is why packets don't circle forever in routing loops.",
    (6, 3, 1, "wr"): "Port numbers are 16 bits — that is why ports range from 0 to 65535.",
    (6, 3, 5, "nk"): "Remember the flags: SYN = start; FIN = end; RST = abort; ACK = confirmation.",
    (6, 3, 6, "wr"): "The three-way handshake sets up the connection at both ends and exchanges sequence numbers (synchronisation).",
    (6, 3, 7, "wr"): "If a firewall blocks the SYN-ACK, the handshake never completes and no connection is made.",
    (6, 3, 7, "nk"): "The immediate cause of a failed handshake: the messages are not getting through (firewall/filter).",
    (6, 3, 12, "wr"): "Every byte has a sequence number — the receiver uses them to put the bytes back in the correct order.",
    (6, 3, 12, "nk"): "UDP has no sequence numbers — that is why it gives no ordering guarantee.",
    (6, 3, 13, "wr"): "The checksum sums the whole segment to verify integrity — if anything changed on the way, the packet is dropped.",
    (6, 3, 16, "wr"): "At connection start TCP uses Slow Start — the congestion window is kept small and increased gradually.",
    (6, 3, 17, "wr"): "cwnd controls the sender's speed according to network capacity — it shrinks on loss and grows when all is well.",
    (6, 3, 18, "wr"): "The bigger the Bandwidth × Delay (BDP), the bigger the window must be — only then is the pipe full and propagation delay hidden.",
    (6, 3, 19, "wr"): "In port knocking, connection attempts hit closed ports in a fixed sequence, after which the firewall opens a service like SSH — often used with SSH servers.",
    (6, 3, 20, "wr"): "MPLS divides traffic into classes using labels and provides QoS — routers don't repeatedly inspect the full IP header.",
    (6, 3, 23, "wr"): "DNS queries usually travel on UDP (port 53), but large transfers and zone transfers use TCP — so DNS uses both.",
    (6, 3, 26, "wr"): "Packets on TCP/IP are not private by nature — they can be seen on the way; for confidentiality you must add TLS/SSH/VPN.",
    (6, 4, 1, "nk"): "Rule: Syntax = how it looks; Semantics = what it means. Both must be agreed for communication.",
    (6, 4, 3, "nk"): "OSI has exactly 7 layers — there can be no 'Layer 10'.",
    (6, 4, 7, "wr"): "Plain FTP sends data and passwords in cleartext — that is insecure. Its secure forms are SFTP/FTPS.",
    (6, 4, 9, "wr"): "Port 22 belongs to SSH — so the SSH service is the one that will be open.",
    (6, 4, 9, "nk"): "Identify the port, identify the service — that is the trick of this question.",
    (6, 4, 19, "wr"): "TFTP (Trivial FTP) runs on UDP, not TCP — this is the statement that is wrong.",
    (6, 4, 21, "wr"): "Ping checks with ICMP Echo whether the other host is reachable and how long it takes.",
    (6, 4, 22, "wr"): "HTTP 403 means the server understood the request but permission for access is denied.",
    (6, 4, 23, "nk"): "LDAP = the network's 'address book + identity-desk counter'.",
    (6, 4, 29, "nk"): "The other names are made up — the real name contains 'Control Message'.",
    (7, 0, 15, "wr"): "A worm spreads through the network making copies of itself and eats bandwidth/memory — it does not directly destroy data.",
    (7, 0, 16, "wr"): "Unwanted bulk email = Spam. It fills the inbox and is often a vehicle for fraud.",
    (7, 1, 20, "wr"): "Symmetric keys are shared in pairs — one key per pair. N people need N(N−1)/2 pairs.",
    (7, 2, 10, "wr"): "A logic bomb driven by date/time is a Time bomb (like the Friday-13 virus).",
    (7, 2, 10, "nk"): "Logic bomb = code that explodes on a condition; if the condition is time, it is a Time bomb.",
    (7, 2, 11, "wr"): "Checking identity (ID + password) = Authentication. This is the first door of security.",
    (7, 2, 12, "wr"): "Fingerprints, iris, face — these are all biometric identification.",
    (7, 2, 12, "nk"): "Physical identity (biometric) is stronger than something known (password).",
    (7, 2, 13, "nk"): "BPSC 2024 official key (a). VPN = a private limousine on the public road.",
    (7, 2, 14, "wr"): "A firewall monitors incoming and outgoing traffic and blocks unauthorised access.",
    (7, 2, 14, "nk"): "Firewall = the network's gatekeeper — it watches, checks, stops.",
}

_FIX_BY_TEXT = {}


def _build():
    if _FIX_BY_TEXT:
        return
    for n in range(1, 8):
        spec = importlib.util.spec_from_file_location(
            f"_tfix_t{n}", os.path.join(DATA, f"topic{n}_data.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        for si, s in enumerate(m.SECTIONS):
            for qi, q in enumerate(s["questions"]):
                for key in ("wr", "nk"):
                    v = q.get(key) if isinstance(q, dict) else None
                    if isinstance(v, (list, tuple)) and len(v) >= 2:
                        loc = (n, si, qi, key)
                        if loc in EN_BY_LOC:
                            _FIX_BY_TEXT[str(v[0])] = EN_BY_LOC[loc]


def fix_pair(en, hi):
    """Return (english, hindi) with English supplied where the source had
    Hindi script in the English slot."""
    en = "" if en is None else str(en)
    hi = "" if hi is None else str(hi)
    _build()
    if en in _FIX_BY_TEXT:
        return _FIX_BY_TEXT[en], hi
    return en, hi


def normalize_module(m):
    """In-memory fix of a loaded topic data module's question explanations."""
    for s in getattr(m, "SECTIONS", []) or []:
        for q in s.get("questions", []):
            if not isinstance(q, dict):
                continue
            for key in ("wr", "nk"):
                v = q.get(key)
                if isinstance(v, (list, tuple)) and len(v) >= 2:
                    en, hi = fix_pair(v[0], v[1])
                    q[key] = [en, hi]
