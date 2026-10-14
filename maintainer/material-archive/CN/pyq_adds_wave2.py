# -*- coding: utf-8 -*-
"""PYQ additions WAVE 2 — GATE 2011-2026 full sweep + KVS/EMRS (Oct 2026).

All items sourced + answer-verified. Zero overlap with wave 1 (pyq_adds.py)
and existing books. Kept in-repo as Material Archive for future subjects.

Verified computations:
- GATE 2022 satellite: Tt = 8000/1e8 = 0.08 ms; Tp = 2100e3/3e8 = 7 ms -> 7.08 ms
- KVS 2017: 800*600*8*40 = 153.6 Mbps; 4 bits/unit * 1000 units/s = 1000 baud / 4000 bps
- GATE 2015 S1 stop-wait: U = Tt/(Tt+2Tp) >= 0.5 -> Tt >= 40 ms -> 64000*0.04/8 = 320 B
- GATE 2015 S2 stop-wait: 0.25 = 8/(8+2Tp) -> Tp = 12 ms
- GATE 2013 fragment: offset 300*8 = 2400 first; HLEN 10 -> 40 B header; 400-40 = 360 B
  payload -> last byte 2759; M = 0 -> last fragment
- GATE 2024: 1420 (1400 data) over MTU 542 then 360 -> frags 3 (522,522,356) -> re-frag
  (340+182)+(340+182)+(340+16) = 6 delivered
- GATE 2018 seq reuse: 2^32 bytes / (1e9/8 B/s) = 34.36 s -> 34
- GATE 2022 seq bits: 1.25e8 B/s * 60 s = 7.5e9 < 2^33 -> 33 bits
"""

# ---------------- T1: signals/bandwidth & delay computation ----------------
W2_T1_SIG = [
    ("GATE CS 2022",
     "Consider a 100 Mbps link between an earth station (sender) and a satellite "
     "(receiver) at an altitude of 2100 km. The signal propagates at 3×10⁸ m/s. "
     "The time taken (in milliseconds, rounded to two decimal places) for the receiver "
     "to completely receive a 1000-byte packet transmitted by the sender is ______.",
     "100 Mbps के link पर earth station से 2100 km ऊँचे satellite को 1000-byte packet "
     "भेजा गया; signal की speed 3×10⁸ m/s है। Receiver को packet पूरा मिलने में लगा "
     "समय (ms में, दो दशमलव) कितना है?",
     [("7.08", "7.08"), ("2.10", "2.10"), ("7.00", "7.00"), ("21.08", "21.08")],
     0,
     ("Transmission time = 8000 bits ÷ 10⁸ bps = 0.08 ms; propagation time = "
      "2100×10³ m ÷ 3×10⁸ m/s = 7 ms; total = 7.08 ms — link ki poori latency "
      "transmission aur propagation dono ka yog hota hai.",
      "Transmission time = 8000 ÷ 10⁸ = 0.08 ms; propagation = 2100×10³ ÷ 3×10⁸ = 7 ms; "
      "kul = 7.08 ms — dono delay milte hain."),
     ("Round-off trap: 2.10 sirf propagation ka fraction pakadta hai; 7.00 transmission "
      "time bhool jata hai.",
      "Round-off jaal: 2.10 sirf propagation; 7.00 mein transmission time chhoot jata hai."),
     {}),
]
W2_T1_KVS = [
    ("KVS PGT Computer Science 2017",
     "What is the bit rate for transmitting an uncompressed 800×600 pixel colour frame "
     "with 8 bits/pixel at 40 frames per second?",
     "बिना compression के 800×600 pixel वाला colour frame (8 bits/pixel) 40 frames per "
     "second पर transmit हो — bit rate कितना होगा?",
     [("2.4 Mbps", "2.4 Mbps"), ("153.6 Mbps", "153.6 Mbps"),
      ("15.36 Mbps", "15.36 Mbps"), ("1536 Mbps", "1536 Mbps")],
     1,
     ("800×600×8 bits × 40 = 153,600,000 bps = 153.6 Mbps — frame ke total bits ko "
      "frame rate se guna karo.",
      "800×600×8 × 40 = 15,36,00,000 bps = 153.6 Mbps — frame ke bits × frame rate."),
     ("Decimal shift jaal: 15.36 aur 1536 bas decimal ki galti hain; 2.4 Mbps sirf "
      "pixel count se bina bits aur frames ke nikla hai.",
      "Decimal ki galtiyan: 15.36/1536; 2.4 Mbps bits aur frames bhool kar aata hai."),
     {}),
    ("KVS PGT Computer Science 2017",
     "An analog signal carries 4 bits in each signal unit. If 1000 signal units are sent "
     "per second, then the baud rate and bit rate of the signal are ______ and ______.",
     "एक analog signal हर signal unit में 4 bits रखता है। 1000 signal units per second "
     "भेजे जाएँ तो signal की baud rate और bit rate क्रमशः कितनी होगी?",
     [("4000 bauds/sec, 4000 bps", "4000 bauds/sec, 4000 bps"),
      ("1000 bauds/sec, 1000 bps", "1000 bauds/sec, 1000 bps"),
      ("4000 bauds/sec, 1000 bps", "4000 bauds/sec, 1000 bps"),
      ("1000 bauds/sec, 4000 bps", "1000 bauds/sec, 4000 bps")],
     3,
     ("Baud rate = signal units per second = 1000 bauds; bit rate = baud × bits per unit "
      "= 1000×4 = 4000 bps — baud rate signalling speed hai, bit rate data speed.",
      "Baud rate = 1000 signals/sec = 1000 bauds; bit rate = 1000×4 = 4000 bps — baud "
      "signal ki speed, bit rate data ki."),
     ("Dono ko same mat samjho: 4000 bauds/4000 bps confusion hai; 4000 bauds/1000 bps "
      "ulta ratio hai.",
      "Dono alag hain: 4000/4000 confusion; 4000/1000 ulta hai."),
     {}),
]

# ---------------- T3: IPv4 addressing computations + ARP ----------------
W2_T3_CLASSC = [
    ("GATE CS 2012",
     "In the IPv4 addressing format, the number of networks allowed under Class C "
     "addresses is:",
     "IPv4 addressing में Class C addresses के अंतर्गत कुल कितने networks allowed हैं?",
     [("2¹⁴", "2¹⁴"), ("2⁷", "2⁷"), ("2²¹", "2²¹"), ("2²⁴", "2²⁴")],
     2,
     ("Class C mein network ID ke liye 24 bits hote hain, par pehle 3 bits fixed (110) "
      "hain — isliye 2⁴⁻³ = 2²¹ networks bante hain (GATE 2012 official key).",
      "Class C में network ID 24 bits की, पर पहले 3 bits fix (110) — इसलिए 2⁴⁻³ = 2²¹ "
      "networks (GATE 2012 official key)."),
     ("2²⁴ poore network field ka size hai (fixed 3 bits bhool kar); 2⁷ aur 2¹⁴ host/other "
      "class ke figures hain.",
      "2²⁴ poora field (3 fixed bits bhool kar); 2⁷/2¹⁴ doosre figures hain."),
     {}),
]
W2_T3_CIDR = [
    ("GATE CS 2024 Set-2",
     "Which one of the following CIDR prefixes exactly represents the range of IP "
     "addresses 10.12.2.0 to 10.12.3.255?",
     "CIDR prefix में से कौन-सा 10.12.2.0 से 10.12.3.255 तक की IP range को ठीक-ठीक "
     "दर्शाता है?",
     [("10.12.2.0/24", "10.12.2.0/24"), ("10.12.2.0/23", "10.12.2.0/23"),
      ("10.12.0.0/22", "10.12.0.0/22"), ("10.12.3.0/25", "10.12.3.0/25")],
     1,
     ("Range mein 512 addresses hain (2⁹) aur 10.12.2.0 9 host-bits ke liye properly "
      "aligned hai — /32−9 = /23, yaani 10.12.2.0/23.",
      "Range में 512 addresses (2⁹) और 10.12.2.0 alignment सही — /32−9 = /23, यानी "
      "10.12.2.0/23."),
     ("/24 sirf 2.0–2.255 cover karta hai; /22 bahut bada (4 blocks); /25 aadha block.",
      "/24 sirf 2.x; /22 bahut bada; /25 aadha block."),
     {}),
]
W2_T3_SLASH30 = [
    ("GATE CS 2019",
     "Three machines M, N and P have IP addresses 100.10.5.2, 100.10.5.5 and 100.10.5.6 "
     "respectively. The subnet mask is set to 255.255.255.252 for all three machines. "
     "Which one of the following is true?",
     "तीन machines M, N, P के IP addresses क्रमशः 100.10.5.2, 100.10.5.5 और 100.10.5.6 "
     "हैं। तीनों का subnet mask 255.255.255.252 है। निम्न में से कौन-सा कथन सही है?",
     [("All three belong to the same subnet", "तीनों एक ही subnet में हैं"),
      ("M and N belong to the same subnet", "M और N एक ही subnet में हैं"),
      ("N and P belong to the same subnet", "N और P एक ही subnet में हैं"),
      ("M and P belong to the same subnet", "M और P एक ही subnet में हैं")],
     2,
     ("Mask /30 ke 4-address blocks banata hai: 100.10.5.0–.3, .4–.7; M (.2) pehle block "
      "mein, N (.5) aur P (.6) doosre block mein — N aur P ek hi subnet ke hain.",
      "Mask /30 se 4-address blocks: .0–.3, .4–.7; M (.2) पहले में, N (.5), P (.6) दूसरे "
      "में — N और P एक ही subnet के।"),
     ("Adjacent numbers ka matlab same subnet nahi — /30 par block boundary .3/.4 par "
      "hoti hai.",
      "पास के numbers = एक subnet नहीं; /30 में boundary .3/.4 पर है।"),
     {}),
]
W2_T3_ARP = [
    ("GATE CS 2019",
     "Suppose that in an IP-over-Ethernet network, a machine X wishes to find the MAC "
     "address of another machine Y in its subnet. Which one of the following techniques "
     "can be used for this?",
     "IP-over-Ethernet network में machine X को अपने ही subnet की machine Y का MAC "
     "address जानना है। इसके लिए निम्न में से कौन-सी technique प्रयोग होगी?",
     [("ARP request broadcast", "ARP request broadcast"),
      ("RARP request broadcast", "RARP request broadcast"),
      ("DNS query", "DNS query"), ("ICMP query", "ICMP query")],
     0,
     ("X ARP request ko broadcast karta hai (Y ki IP puch kar); Y unicast ARP reply mein "
      "apna MAC deta hai — ARP hi IP→MAC resolution ka tarika hai.",
      "X ARP request broadcast karta hai (Y ki IP); Y unicast reply mein MAC deta hai — "
      "ARP = IP→MAC resolution."),
     ("RARP ulta (MAC→IP) hai; DNS naam→IP; ICMP error/control — koi bhi MAC nahi deta.",
      "RARP उल्टा (MAC→IP); DNS नाम→IP; ICMP error — MAC कोई नहीं देता।"),
     {}),
]
W2_T3_NEXTHOP = [
    ("GATE CS 2025 Set-2",
     "Node X has a TCP connection open to node Y. Packets from X to Y go through an "
     "intermediate IP router R; Ethernet switch S is the first switch on the path. For a "
     "packet sent from X, which of the following is TRUE about its destination IP and MAC "
     "addresses at the time it leaves X?",
     "Node X की node Y से TCP connection है; packets router R से होकर जाते हैं और पहला "
     "Ethernet switch S है। X से निकलते packet के destination IP और MAC addresses के "
     "बारे में क्या सही है?",
     [("Destination IP = Y's IP; destination MAC = R's MAC",
       "Destination IP = Y का IP; destination MAC = R का MAC"),
      ("Destination IP = R's IP; destination MAC = R's MAC",
       "Destination IP = R का IP; destination MAC = R का MAC"),
      ("Destination IP = Y's IP; destination MAC = Y's MAC",
       "Destination IP = Y का IP; destination MAC = Y का MAC"),
      ("Destination IP = R's IP; destination MAC = S's MAC",
       "Destination IP = R का IP; destination MAC = S का MAC")],
     0,
     ("IP address end-to-end hota hai — destination IP hamesha Y ka; MAC har hop par "
      "badalta hai, isliye pehle hop (router R) ka MAC lagta hai — ARP se gateway ka MAC "
      "mila hota hai.",
      "IP end-to-end होता है — destination IP सदा Y का; MAC हर hop पर बदलता है, पहले hop "
      "(router R) का MAC लगता है।"),
     ("IP ko hop-by-hop badalna common galti hai; switch MAC forwarding karta hai par "
      "packet ka destination MAC router ka hi rehta hai.",
      "IP को hop-by-hop बदलना आम गलती; packet का destination MAC router का ही रहता है।"),
     {}),
]

# ---------------- T6 SEC_C: error/flow numerics ----------------
W2_T6C_SW1 = [
    ("GATE CS 2015 Set-1",
     "Suppose the stop-and-wait protocol is used on a link with a bit rate of 64 kilobits "
     "per second and 20 milliseconds propagation delay. Acknowledgement transmission time "
     "and processing times are negligible. The minimum frame size in bytes to achieve a "
     "link utilisation of at least 50% is ______.",
     "64 kbps की link पर stop-and-wait protocol है, propagation delay 20 ms है (ACK "
     "transmission व processing नगण्य)। कम से कम 50% link utilisation के लिए न्यूनतम "
     "frame size (bytes में) कितनी हो?",
     [("160", "160"), ("320", "320"), ("640", "640"), ("1280", "1280")],
     1,
     ("U = Tt/(Tt+2Tp) ≥ 0.5 → Tt ≥ 2Tp = 40 ms; frame ≥ 64000 bps × 0.04 s ÷ 8 = "
      "320 bytes.",
      "U = Tt/(Tt+2Tp) ≥ 0.5 → Tt ≥ 2Tp = 40 ms; frame ≥ 64000 × 0.04 ÷ 8 = 320 bytes."),
     ("160 bas ek Tp ka hissa hai; 640/1280 utilisation formula ke ratio bhool jane se "
      "aate hain.",
      "160 एक Tp; 640/1280 ratio भूलने से आते हैं।"),
     {}),
]
W2_T6C_SW2 = [
    ("GATE CS 2015 Set-2",
     "A link has a transmission speed of 10⁶ bits/sec. It uses data packets of size 1000 "
     "bytes each. Acknowledgements have negligible transmission delay and the same "
     "propagation delay as data; processing delays are negligible. The efficiency of the "
     "stop-and-wait protocol is exactly 25%. The one-way propagation delay (in "
     "milliseconds) is ______.",
     "एक link की speed 10⁶ bits/sec है और packets 1000 bytes के हैं। ACK का transmission "
     "delay नगण्य, propagation delay data के बराबर है। Stop-and-wait की efficiency ठीक "
     "25% है। एक-तरफ़ा propagation delay (ms में) कितना है?",
     [("8", "8"), ("10", "10"), ("12", "12"), ("20", "20")],
     2,
     ("Tt = 8000 bits ÷ 10⁶ = 8 ms; η = Tt/(Tt+2Tp) = 0.25 → 8+2Tp = 32 → Tp = 12 ms.",
      "Tt = 8000 ÷ 10⁶ = 8 ms; η = Tt/(Tt+2Tp) = 0.25 → 8+2Tp = 32 → Tp = 12 ms."),
     ("8 ms Tt hai Tp nahi; 10/20 round numbers ke jaal hain.",
      "8 ms Tt है; 10/20 गोल आँकड़ों के जाल।"),
     {}),
]
W2_T6C_SS = [
    ("GATE CS 2018",
     "Consider the following statements regarding the slow start phase of TCP congestion "
     "control (cwnd = congestion window, MSS = maximum segment size):\n"
     "(i) cwnd increases by 2 MSS on every successful acknowledgement.\n"
     "(ii) cwnd approximately doubles on every successful acknowledgement.\n"
     "(iii) cwnd increases by 1 MSS every round trip time.\n"
     "(iv) cwnd approximately doubles every round trip time.\n"
     "Which one of the following is correct?",
     "TCP congestion control के slow start चरण (cwnd = congestion window, MSS = maximum "
     "segment size) के बारे में विचार कीजिए:\n"
     "(i) हर successful acknowledgement पर cwnd 2 MSS बढ़ता है।\n"
     "(ii) हर successful acknowledgement पर cwnd लगभग दोगुना होता है।\n"
     "(iii) हर round trip time में cwnd 1 MSS बढ़ता है।\n"
     "(iv) हर round trip time में cwnd लगभग दोगुना होता है।\n"
     "क्या सही है?",
     [("(i) and (iii) only", "केवल (i) और (iii)"),
      ("(ii) and (iv) only", "केवल (ii) और (iv)"),
      ("(iv) only", "केवल (iv)"), ("(ii) only", "केवल (ii)")],
     2,
     ("Slow start mein har ACK par cwnd 1 MSS badhta hai; RTT mein cwnd/MSS ACKs aate "
      "hain — isliye per RTT cwnd double hota hai: sirf (iv) sahi hai.",
      "Slow start में हर ACK पर cwnd +1 MSS; एक RTT में cwnd/MSS ACKs — इसलिए per RTT "
      "double: केवल (iv) सही।"),
     ("Per-ACK doubling (ii) bahut tez hota; (iii) per-RTT sirf 1 MSS congestion "
      "avoidance jaisa hai.",
      "Per-ACK doubling (ii) असंभव-सा; (iii) तो congestion avoidance जैसा।"),
     {}),
]

# ---------------- T6 SEC_D: network layer ----------------
W2_T6D_ROUTER1 = [
    ("GATE CS 2015 Set-1",
     "Which one of the following fields of an IP header is NOT modified by a typical IP "
     "router?",
     "IP header का कौन-सा field एक सामान्य IP router द्वारा संशोधित नहीं किया जाता?",
     [("Checksum", "Checksum"), ("Source address", "Source address"),
      ("Time to Live (TTL)", "Time to Live (TTL)"), ("Length", "Length")],
     1,
     ("Router TTL ko ghatata hai, checksum phir se calculate karta hai, fragmentation par "
      "length badal sakti hai — par source address hamesha wahi rehta hai (GATE 2015 key).",
      "Router TTL घटाता है, checksum नया, fragmentation पर length बदल सकती है — source "
      "address वही रहता है (GATE 2015 key)."),
     ("Checksum aur TTL router ke haath badalte hain; length fragmentation se badal sakti "
      "hai.",
      "Checksum/TTL बदलते हैं; length fragmentation से बदल सकती है।"),
     {}),
]
W2_T6D_ROUTER2 = [
    ("GATE CS 2024 Set-2",
     "Which of the following fields of an IP header is/are ALWAYS modified by any router "
     "before it forwards the IP packet?",
     "IP packet forward करने से पहले हर router IP header के कौन-से fields हमेशा बदलता है?",
     [("TTL only", "केवल TTL"), ("Checksum only", "केवल Checksum"),
      ("TTL and header checksum", "TTL और header checksum"),
      ("Source address and TTL", "Source address और TTL")],
     2,
     ("Har hop par TTL ghat-ta hai (1 kam) aur uske kaaran header checksum bhi har router "
      "ko phir se lagana hi padta hai — dono always modified hote hain.",
      "हर hop पर TTL घटता है और उससे header checksum भी हर router को नया करना पड़ता है — "
      "दोनों हमेशा बदलते हैं।"),
     ("Checksum ko optional samajhna galti hai — TTL badalne par checksum invalid ho jata "
      "hai.",
      "Checksum optional नहीं — TTL बदलते ही checksum अमान्य हो जाता है।"),
     {}),
]
W2_T6D_NAT = [
    ("GATE CS 2024 Set-1",
     "Which of the following fields is/are modified in the IP header of a packet going "
     "out of a Network Address Translation (NAT) device from an internal network to an "
     "external network?",
     "NAT device से internal network से external network की तरफ़ जाते packet के IP "
     "header में कौन-से fields बदले जाते हैं?",
     [("Source IP address only", "केवल Source IP address"),
      ("Destination IP address only", "केवल Destination IP address"),
      ("Source IP address and header checksum", "Source IP address और header checksum"),
      ("TTL and destination address", "TTL और destination address")],
     2,
     ("NAT bahar jaate packet ka private source IP apne public IP se badalta hai (aur "
      "mapping banaata hai); us badalav se header checksum bhi recompute hota hai.",
      "NAT बाहर जाते packet का private source IP अपने public IP से बदलता है; उससे "
      "header checksum भी नया होता है।"),
     ("Destination address wahi rehta hai (jana to server ko hi hai); TTL alag cheez hai.",
      "Destination वही रहता है; TTL अलग चीज़ है।"),
     {}),
]
W2_T6D_FRAG = [
    ("GATE CS 2024 Set-1",
     "Consider sending an IP datagram of size 1420 bytes (including a 20-byte IP header) "
     "over a path of two links with a router between them. The first link has MTU 542 "
     "bytes and the second link has MTU 360 bytes. The number of fragments delivered at "
     "the receiver is ______.",
     "1420 bytes का IP datagram (20-byte header सहित) दो links के रास्ते भेजा जा रहा है, "
     "बीच में एक router है। पहले link का MTU 542 bytes और दूसरे का 360 bytes है। Receiver "
     "पर कुल कितने fragments पहुँचेंगे?",
     [("4", "4"), ("5", "5"), ("6", "6"), ("8", "8")],
     2,
     ("1400 bytes data पहले link पर 3 fragments (522, 522, 356); दूसरे link (340 bytes "
      "data per fragment) पर हर बड़ा fragment 2 में टूटता है — कुल 2+2+2 = 6 fragments.",
      "1400 bytes data पहले link पर 3 (522, 522, 356); दूसरे link पर (340 data) हर बड़ा "
      "2 में — कुल 6."),
     ("5/8 fragmentation ko sirf ek baar maante hain; 4 total data ko 360 se seedha "
      "bhaag dete hain.",
      "5/8 fragmentation एक ही बार मानते हैं; 4 सीधे 360 से भाग देते हैं।"),
     {}),
]
W2_T6D_LASTFRAG = [
    ("GATE CS 2013",
     "In an IPv4 datagram, the M bit is 0, the value of HLEN is 10, the value of total "
     "length is 400 and the fragment offset value is 300. The position of the datagram, "
     "and the sequence numbers of the first and the last bytes of the payload, "
     "respectively, are:",
     "एक IPv4 datagram में M bit = 0, HLEN = 10, total length = 400 और fragment offset "
     "= 300 है। इस datagram की स्थिति तथा payload के पहले और आख़िरी bytes के sequence "
     "numbers क्रमशः हैं:",
     [("Last fragment, 2400 and 2759", "Last fragment, 2400 और 2759"),
      ("First fragment, 2400 and 2759", "First fragment, 2400 और 2759"),
      ("Last fragment, 300 and 659", "Last fragment, 300 और 659"),
      ("Last fragment, 2400 and 2779", "Last fragment, 2400 और 2779")],
     0,
     ("HLEN 10 → header 40 bytes; offset 300 × 8 = 2400 se payload shuru; payload 400−40 "
      "= 360 bytes → aakhri byte 2400+359 = 2759; M = 0 matlab yeh aakhri fragment hai.",
      "HLEN 10 → header 40 bytes; offset 300×8 = 2400 से payload; 400−40 = 360 bytes → "
      "आख़िरी byte 2759; M = 0 = यही अंतिम fragment है।"),
     ("Offset ko byte nahi 8-byte units mein count karna zaroori hai; 2779 header ko do "
      "baar jod deta hai.",
      "Offset 8-byte units में होता है; 2779 header दो बार जोड़ता है।"),
     {}),
]
W2_T6D_LSDV = [
    ("GATE CS 2014 Set-1",
     "Consider the following three statements about link state and distance vector "
     "routing protocols for a large network with 500 nodes and 4000 links:\n"
     "S1: The computational overhead in link state protocols is higher than in distance "
     "vector protocols.\n"
     "S2: A distance vector protocol (with split horizon) avoids persistent routing loops, "
     "but a link state protocol does not.\n"
     "S3: After a topology change, a link state protocol converges faster than a distance "
     "vector protocol.\n"
     "Which one is correct?",
     "500 nodes और 4000 links वाले बड़े network के लिए link state व distance vector routing "
     "protocols के बारे में तीन कथन:\n"
     "S1: Link state में computational overhead distance vector से अधिक है।\n"
     "S2: Distance vector (split horizon सहित) persistent loops से बचता है, पर link state "
     "नहीं।\n"
     "S3: Topology बदलने पर link state, distance vector से तेज़ converge करता है।\n"
     "कौन-सा सही है?",
     [("S1, S2 and S3 are all true", "S1, S2, S3 तीनों सही"),
      ("S1, S2 and S3 are all false", "S1, S2, S3 तीनों गलत"),
      ("S1 and S2 are true, S3 is false", "S1 और S2 सही, S3 गलत"),
      ("S1 and S3 are true, S2 is false", "S1 और S3 सही, S2 गलत")],
     3,
     ("S1 sahi: har node poora SPF/Dijkstra chalata hai. S3 sahi: flooding se LS topology "
      "turant jaanti hai. S2 galat: link state shortest-path tree loop-free hota hai — "
      "loops ki samasya distance vector ki hai.",
      "S1 सही: हर node पूरा SPF चलाता है। S3 सही: flooding से तेज़ converge। S2 गलत: "
      "link state tree loop-free होता है।"),
     ("S2 ulta hai — split horizon count-to-infinity se poora bachata bhi nahi.",
      "S2 उल्टा — split horizon count-to-infinity से पूरा बचाता भी नहीं।"),
     {}),
]
W2_T6D_RIPOSPF = [
    ("GATE CS 2014 Set-2",
     "Which one of the following is TRUE about the interior gateway routing protocols "
     "RIP (Routing Information Protocol) and OSPF (Open Shortest Path First)?",
     "Interior gateway routing protocols RIP (Routing Information Protocol) और OSPF "
     "(Open Shortest Path First) के बारे में कौन-सा कथन सही है?",
     [("RIP uses distance vector routing and OSPF uses link state routing",
       "RIP distance vector और OSPF link state routing प्रयोग करता है"),
      ("OSPF uses distance vector routing and RIP uses link state routing",
       "OSPF distance vector और RIP link state routing प्रयोग करता है"),
      ("Both RIP and OSPF use link state routing", "दोनों link state routing प्रयोग करते हैं"),
      ("Both RIP and OSPF use distance vector routing", "दोनों distance vector routing प्रयोग करते हैं")],
     0,
     ("RIP neighbours ko apni distance vector bhejta hai (distance vector family); OSPF "
      "poora topology map flood kar Dijkstra chalata hai (link state) — yeh standard "
      "classification hai.",
      "RIP अपनी distance vector भेजता है; OSPF topology flood कर Dijkstra चलाता है "
      "(link state) — यही मानक भेद है।"),
     ("Dono ko ek hi category mein daalna common galti hai.",
      "दोनों को एक श्रेणी में डालना आम गलती।"),
     {}),
]
W2_T6D_STMTS = [
    ("GATE CS 2020",
     "Consider the following statements about the functionality of an IP based router:\n"
     "I. A router does not modify the IP packets during forwarding.\n"
     "II. It is not necessary for a router to implement any routing protocol.\n"
     "III. A router should reassemble IP fragments if the MTU of the outgoing link is "
     "larger than the size of the incoming IP packet.\n"
     "Which of the above statement(s) is/are TRUE?",
     "IP आधारित router की कार्यप्रणाली के बारे में विचार:\n"
     "I. Router forwarding के दौरान IP packets को संशोधित नहीं करता।\n"
     "II. Router के लिए कोई routing protocol लागू करना आवश्यक नहीं है।\n"
     "III. यदि outgoing link का MTU आने वाले packet से बड़ा हो तो router को fragments "
     "जोड़ने चाहिए।\n"
     "इनमें कौन-सा कथन सही है?",
     [("I only", "केवल I"), ("II only", "केवल II"),
      ("I and III only", "केवल I और III"), ("None of the above", "कोई नहीं")],
     1,
     ("I galat: router TTL ghatata hai aur checksum badalta hai. II sahi: static routes "
      "se bhi router chal sakta hai. III galat: reassembly sirf destination host karta "
      "hai, router kabhi nahi.",
      "I गलत: router TTL/checksum बदलता है। II सही: static routes से भी चलेगा। III गलत: "
      "reassembly सिर्फ़ destination करता है।"),
     ("Fragmentation ke baad re-fragmentation ka kaam router ka hai, jodna nahi.",
      "Router re-fragment कर सकता है, जोड़ता नहीं।"),
     {}),
]
W2_T6D_FIELDS = [
    ("GATE CS 2014 Set-3",
     "Host A (on TCP/IPv4 network A) sends an IP datagram D to host B (on TCP/IPv4 "
     "network B) with no transmission error. When D reaches B, which of the following IP "
     "header field(s) may be different from that of the original datagram D?\n"
     "I. TTL    II. Checksum    III. Fragment Offset",
     "Host A ने (TCP/IPv4 network A से) बिना किसी त्रुटि के IP datagram D, host B को "
     "भेजा। D के B पर पहुँचने पर निम्न में से कौन-से IP header fields मूल datagram से "
     "भिन्न हो सकते हैं?\n"
     "I. TTL    II. Checksum    III. Fragment Offset",
     [("I only", "केवल I"), ("II and III only", "केवल II और III"),
      ("I and II only", "केवल I और II"), ("I, II and III", "I, II और III तीनों")],
     3,
     ("Har router par TTL ghat-ta hai aur checksum naya hota hai; raaste mein fragmentation "
      "hui to fragment offset bhi lag sakta hai — teeno badal sakte hain (GATE 2014 key).",
      "हर router पर TTL घटता है, checksum नया; रास्ते में fragmentation हुई तो offset भी — "
      "तीनों बदल सकते हैं।"),
     ("Offset ko 'sirf fragmentation ke time' samajh kar chhod dena galti hai — puchha "
      "hai 'ho sakta hai'.",
      "Offset को छोड़ देना गलती — पूछा है 'हो सकता है'।"),
     {}),
]

# ---------------- T6 SEC_E: transport/application ----------------
W2_T6E_STATEFUL = [
    ("GATE CS 2016 Set-1",
     "Which of the following is/are example(s) of stateful application layer protocols?\n"
     "I. HTTP    II. FTP    III. TCP    IV. POP3",
     "निम्न में से कौन-सा stateful application layer protocol का उदाहरण है?\n"
     "I. HTTP    II. FTP    III. TCP    IV. POP3",
     [("I and II only", "केवल I और II"), ("II only", "केवल II"),
      ("I only", "केवल I"), ("II and III only", "केवल II और III")],
     1,
     ("FTP control connection par session state rakhta hai (stateful); HTTP 1.0 request "
      "ke baad bhool jata hai (stateless); TCP application layer ka protocol hi nahi; "
      "POP3 independent commands — sirf II (GATE 2016 key).",
      "FTP control connection पर state रखता है (stateful); HTTP 1.0 भूल जाता है; TCP "
      "application का protocol नहीं; POP3 स्वतंत्र — केवल II।"),
     ("TCP ko application protocol samajhna option jaal hai; HTTP stateful sirf modern "
      "keep-alive mein lagta hai.",
      "TCP application protocol नहीं; HTTP सिर्फ़ आधुनिक keep-alive में stateful लगता है।"),
     {}),
]
W2_T6E_SEQ = [
    ("GATE CS 2016 Set-2",
     "Identify the correct sequence in which the following packets are transmitted by a "
     "host when a browser requests a web page from a remote server, assuming that the host "
     "has just been restarted:",
     "मान लीजिए host अभी-अभी restart हुआ है और browser एक remote server से web page "
     "माँगता है। निम्न packets सही क्रम में transmit होंगे:",
     [("HTTP GET request, DNS query, TCP SYN",
       "HTTP GET request, DNS query, TCP SYN"),
      ("DNS query, HTTP GET request, TCP SYN",
       "DNS query, HTTP GET request, TCP SYN"),
      ("DNS query, TCP SYN, HTTP GET request",
       "DNS query, TCP SYN, HTTP GET request"),
      ("TCP SYN, DNS query, HTTP GET request",
       "TCP SYN, DNS query, HTTP GET request")],
     2,
     ("Restart ke baad cache khaali: pehle DNS query se server ka IP milta hai, phir TCP "
      "three-way handshake (SYN...), tabhi HTTP GET ja sakta hai (GATE 2016 key).",
      "Restart पर cache ख़ाली: पहले DNS से IP, फिर TCP handshake (SYN...), तब HTTP GET "
      "(GATE 2016 key)."),
     ("GET pehle ja hi nahi sakta — connection bina handshake ke nahi banti; restart yaani "
      "DNS cache bhi khaali.",
      "GET पहले नहीं जा सकता; restart में DNS cache भी ख़ाली।"),
     {}),
]
W2_T6E_MAIL = [
    ("GATE CS 2019",
     "Which of the following protocol pairs can be used to send and retrieve e-mails "
     "(in that order)?",
     "ई-मेल भेजने और प्राप्त करने (इसी क्रम में) के लिए निम्न में से किस protocol जोड़ी "
     "का प्रयोग हो सकता है?",
     [("SMTP and POP3", "SMTP और POP3"), ("POP3 and SMTP", "POP3 और SMTP"),
      ("IMAP and SMTP", "IMAP और SMTP"), ("SMTP and IMAP only", "केवल SMTP और IMAP")],
     0,
     ("SMTP mail bhejne (push) ke liye; POP3 mail lane (retrieve) ke liye — yeh classic "
      "jodi GATE 2019 ka answer hai.",
      "SMTP भेजने (push) के लिए; POP3 लाने (retrieve) के लिए — यही जोड़ी (GATE 2019)।"),
     ("Ulti jodi (POP3 and SMTP) order ke against hai; IMAP bhi retrieve karta hai par "
      "sabse common jodi SMTP+POP3 hai.",
      "उल्टी जोड़ी गलत; IMAP भी retrieve करता है पर सबसे सामान्य जोड़ी SMTP+POP3।"),
     {}),
]
W2_T6E_SEQREUSE = [
    ("GATE CS 2018",
     "Consider a long-lived TCP session with an end-to-end bandwidth of 1 Gbps (= 10⁹ "
     "bits/second). The session starts with a sequence number of 1234. The minimum time "
     "(in seconds, rounded to the closest integer) before this sequence number can be "
     "used again is ______.",
     "एक लंबी TCP session की bandwidth 1 Gbps (= 10⁹ bits/second) है और वह sequence "
     "number 1234 से शुरू होती है। इस sequence number के पुनः प्रयोग से पहले न्यूनतम "
     "समय (seconds में, निकटतम पूर्णांक) कितना है?",
     [("34", "34"), ("35", "35"), ("43", "43"), ("32", "32")],
     0,
     ("TCP sequence numbers bytes count karte hain: 2³² bytes ka space; 1 Gbps = 1.25×10⁸ "
      "bytes/sec → 2³² ÷ 1.25×10⁸ = 34.36 s → 34 second.",
      "TCP sequence numbers bytes गिनते हैं: 2³² bytes; 1 Gbps = 1.25×10⁸ B/s → 34.36 s "
      "→ 34 second."),
     ("Bits mein hisaab karke 4 s; ya 2³² bits samajh kar galat number — bytes ka chakkar "
      "hai.",
      "Bits में हिसाब लगाना (4 s) या 2³² bits मानना गलत।"),
     {}),
]
W2_T6E_HANDSHAKE = [
    ("GATE CS 2021 Set-2",
     "In the TCP three-way handshake, host P sends a connection request to Q with SYN = 1, "
     "SEQ = X, ACK = 0. Q accepts the connection. Which of the following represents the "
     "information in the TCP segment header sent by Q to P?",
     "TCP three-way handshake में host P, Q को connection request भेजता है: SYN = 1, "
     "SEQ = X, ACK = 0। Q connection स्वीकार करता है। Q द्वारा P को भेजे segment header "
     "में क्या होगा?",
     [("SYN = 1, SEQ = Y, ACK = X", "SYN = 1, SEQ = Y, ACK = X"),
      ("SYN = 1, SEQ = X, ACK = Y", "SYN = 1, SEQ = X, ACK = Y"),
      ("SYN = 1, SEQ = Y, ACK = X+1", "SYN = 1, SEQ = Y, ACK = X+1"),
      ("SYN = 0, SEQ = Y, ACK = X+1", "SYN = 0, SEQ = Y, ACK = X+1")],
     2,
     ("Q apna random sequence number Y bhejta hai, SYN=1 rakhta hai (apna SYN), aur "
      "acknowledge karta hai X ka — agla byte X+1 (GATE 2021 key: III).",
      "Q अपना sequence number Y भेजता है, SYN=1, और X का ack = X+1 (GATE 2021 key: III)।"),
     ("ACK = X galat (yeh khud ko X+1 expect karna hua); SYN=0 second segment jaisa hota.",
      "ACK = X गलत (X+1 अपेक्षित); SYN=0 दूसरे जैसा।"),
     {}),
]
W2_T6E_SEQBITS = [
    ("GATE CS 2022",
     "Consider data transfer using TCP over a 1 Gbps link. Assuming that the maximum "
     "segment lifetime (MSL) is set to 60 seconds, the minimum number of bits required "
     "for the sequence number field of the TCP header, to prevent the sequence number "
     "space from wrapping around during the MSL, is ______.",
     "1 Gbps link पर TCP से data transfer हो रहा है। Maximum segment lifetime (MSL) 60 "
     "seconds है। MSL के दौरान sequence number space के wrap होने से बचने के लिए TCP "
     "header के sequence number field में न्यूनतम कितने bits चाहिए?",
     [("32", "32"), ("33", "33"), ("34", "34"), ("36", "36")],
     1,
     ("1 Gbps = 1.25×10⁸ bytes/sec; 60 s में 7.5×10⁹ bytes; 2³² = 4.29×10⁹ < 7.5×10⁹ < "
      "2³³ = 8.59×10⁹ — इसलिए कम से कम 33 bits (GATE 2022 key).",
      "1.25×10⁸ B/s × 60 = 7.5×10⁹ bytes; 2³² < 7.5×10⁹ < 2³³ — इसलिए 33 bits।"),
     ("32 bits mein space 60 s के लिए kam padta hai; 34/36 zyada hain (minimum pucha hai).",
      "32 कम पड़ता; 34/36 ज़्यादा (न्यूनतम पूछा है)।"),
     {}),
]
W2_T6E_FINWAIT = [
    ("GATE CS 2017 Set-1",
     "A TCP client and server complete data transfer. The client calls close; a FIN segment "
     "is sent to the server, which responds with an ACK received by the client. As per the "
     "TCP connection state diagram (RFC 793), in which state does the client-side TCP "
     "connection wait for the FIN from the server?",
     "TCP client-server का data transfer पूरा हुआ। Client close करता है; server को FIN "
     "जाता है; server का ACK client को मिलता है। RFC 793 की state diagram के अनुसार "
     "client-side connection server के FIN की प्रतीक्षा किस state में करती है?",
     [("TIME_WAIT", "TIME_WAIT"), ("FIN_WAIT_2", "FIN_WAIT_2"),
      ("CLOSE_WAIT", "CLOSE_WAIT"), ("LAST_ACK", "LAST_ACK")],
     1,
     ("Client: FIN_WAIT_1 (FIN bheja) → ACK mila → FIN_WAIT_2 (server ke FIN ka intezar) "
      "→ phir TIME_WAIT. CLOSE_WAIT server-side hoti hai.",
      "Client: FIN_WAIT_1 (FIN भेजा) → ACK मिला → FIN_WAIT_2 (server के FIN का इंतज़ार) "
      "→ फिर TIME_WAIT. CLOSE_WAIT server-side।"),
     ("TIME_WAIT aakhri state hai (dono FIN ke baad); CLOSE_WAIT server ki hoti hai.",
      "TIME_WAIT अंत में; CLOSE_WAIT server की।"),
     {}),
]
W2_T6E_FLAGS = [
    ("GATE CS 2025 Set-1",
     "In the TCP three-way handshake, let the three packets exchanged during connection "
     "establishment be P1, P2 and P3 in order. Which of the following is TRUE about the "
     "TCP header flags set in these packets?",
     "TCP three-way handshake में connection establishment के दौरान तीन packets P1, P2 "
     "और P3 (इसी क्रम में) बदले जाते हैं। इनमें सेट TCP header flags के बारे में क्या "
     "सही है?",
     [("P1: SYN; P2: SYN, ACK; P3: ACK", "P1: SYN; P2: SYN, ACK; P3: ACK"),
      ("P1: SYN, ACK; P2: ACK; P3: FIN", "P1: SYN, ACK; P2: ACK; P3: FIN"),
      ("P1: SYN; P2: ACK; P3: FIN", "P1: SYN; P2: ACK; P3: FIN"),
      ("P1: ACK; P2: SYN; P3: ACK", "P1: ACK; P2: SYN; P3: ACK")],
     0,
     ("Classic handshake: P1 SYN (request), P2 SYN+ACK (server ka SYN + acknowledgement), "
      "P3 ACK (final) — flags ka yehi standard pattern hai (GATE 2025).",
      "क्लासिक handshake: P1 SYN, P2 SYN+ACK, P3 ACK — यही मानक पैटर्न (GATE 2025)।"),
     ("FIN connection release ka flag hai; pehle packet par ACK kabhi nahi hota.",
      "FIN release का flag है; पहले packet पर ACK नहीं होता।"),
     {}),
]
W2_T6E_WWW = [
    ("EMRS PGT Computer Science",
     "The World Wide Web (WWW) is:",
     "World Wide Web (WWW) क्या है?",
     [("another name for the Internet", "Internet का दूसरा नाम"),
      ("a worldwide connection of computers", "कंप्यूटरों का विश्वव्यापी जुड़ाव"),
      ("a worldwide collection of information", "सूचना का विश्वव्यापी संग्रह"),
      ("a collection of linked information residing on computers connected by the Internet",
       "Internet से जुड़े कंप्यूटरों पर रखी link की गई सूचनाओं का संग्रह")],
     3,
     ("WWW Internet par hosted linked documents (web pages) ka sangrah hai — Internet "
      "khud network infrastructure hai, WWW uspar chalne wali information service.",
      "WWW, Internet पर hosted linked documents का संग्रह है — Internet खुद network "
      "है, WWW उसकी information service।"),
     ("Internet aur WWW ko same bolna sabse common galti hai; 'connection of computers' "
      "to network ki paribhasha hai.",
      "Internet और WWW को एक मानना सबसे आम गलती; 'connection' तो network है।"),
     {}),
]
