# -*- coding: utf-8 -*-
"""ORIGINAL practice questions — WAVE 3 (worldwide exam-level, harder).

Research sources (patterns studied; questions ORIGINAL — zero repeats):
  * GATE CSE Computer Networks (byjus GATE archive, CS Junction) — subnetting,
    sliding window, protocol-mapping numeric level.
  * UGC NET Computer Science (compsciedu NET paper) — firewall/IPv4/hierarchy level.
  * Cisco CCNA 200-301 practice (smenode-academy, prepforcerts, ipcisco) —
    OSPF cost/AD, IPv6 FE80::/10 link-local, trunk/access, IP protocol 89,
    BGP TCP 179, RIP UDP 520 level.
  * CompTIA Network+ N10-009 (flashgenius) — wildcard masks, inter-VLAN,
    MAC filtering, DHCP ranges level.

Rule: NO question may repeat anything in topic*_data.py or practice_new_p1..p3 —
all original, textbook-based (Forouzan/Tanenbaum + Cisco/CompTIA syllabus style).
Printed WITHOUT solutions in practice booklets; wr/nk kept for answer-key
integrity only. Source label: 'Practice — original (textbook-based)'.
"""
SRC = "Practice — original (textbook-based)"

# ------------------------------- TOPIC 1 -------------------------------
P1_A_X = [
 (SRC,
  "The three aspects of TIMING in a protocol are speed matching, sequencing, and:",
  "एक protocol में TIMING के तीन पक्ष हैं — speed matching, sequencing और:",
  [("Flow control", "Flow control"), ("Error control", "Error control"),
   ("Syntax", "Syntax"), ("Addressing", "Addressing")],
  0,
  ("Forouzan: protocol ke 3 elements — syntax (format), semantics (meaning), "
   "timing (speed matching + sequencing + flow control).",
   "protocol के 3 elements — syntax, semantics, timing (speed matching + sequencing + flow control)।"),
  ("Yaad rakho: timing = events ka order + speed + flow control; error control "
   "reliability ke liye alag concept hai.",
   "timing = क्रम + गति + flow control; error control अलग concept है।"),
  {1: ("Error control reliability ka hissa hai, timing ka nahi.",
       "Error control reliability का भाग है, timing का नहीं।")}),
]

P1_B_X = [
 (SRC,
  "Which of the following is a measure of network RELIABILITY (not performance)?",
  "निम्न में से कौन network की RELIABILITY (performance नहीं) का माप है?",
  [("Throughput", "Throughput"), ("Frequency of failure", "Failure की आवृत्ति"),
   ("Jitter", "Jitter"), ("Delay", "Delay")],
  1,
  ("Forouzan: reliability = failure ki frequency + recovery time; throughput, "
   "delay, jitter — sab performance criteria hain.",
   "reliability = failure की आवृत्ति + recovery time; throughput, delay, jitter — performance criteria हैं।"),
  ("Performance = speed/quality of delivery; Reliability = kitni baar network "
   "toota aur kitni jaldi theek hua.",
   "Performance = गति; Reliability = टूटने की आवृत्ति और recovery।"),
  {0: ("Throughput = per unit time delivered data — performance metric.",
       "Throughput = प्रति समय delivered data — performance metric।")}),
]

P1_C_X = [
 (SRC,
  "In 100BASE-TX (Fast Ethernet over UTP), full-duplex operation is possible because:",
  "100BASE-TX (UTP पर Fast Ethernet) में full-duplex संभव है क्योंकि:",
  [("UTP uses separate wire pairs for transmitting and receiving",
    "UTP में transmit और receive के लिए अलग wire pairs हैं"),
   ("UTP uses time-division multiplexing", "UTP में time-division multiplexing है"),
   ("UTP uses two different frequencies", "UTP में दो अलग frequencies हैं"),
   ("Two UTP cables are used", "दो UTP cables प्रयोग होती हैं")],
  0,
  ("100BASE-TX pairs 1-2 aur 3-6 — ek pair TX, doosra RX; isliye dono "
   "directions ek saath (full-duplex) chal sakte hain.",
   "pairs 1-2 और 3-6 — एक pair TX, दूसरा RX; दोनों दिशाएँ साथ चलती हैं।"),
  ("Half-duplex mein ek hi pair dono directions ke liye hota (collision possible); "
   "alag pairs se collision hi nahi.",
   "half-duplex में एक pair दोनों काम करता है; अलग pairs से collision नहीं।"),
  {}),
]

P1_D_X = [
 (SRC,
  "In a bus topology, both ends of the cable are terminated with a resistor to prevent:",
  "Bus topology में cable के दोनों सिरों पर resistor लगाया जाता है ताकि रोका जा सके:",
  [("Signal reflection (bounce)", "Signal reflection (bounce)"),
   ("Crosstalk", "Crosstalk"), ("Attenuation", "Attenuation"),
   ("Dispersion", "Dispersion")],
  0,
  ("Bina termination ke travelling signal end par reflect hokar wapas aata hai "
   "aur garbage create karta hai — terminator 50-ohm resistor ye bounce khatam karta hai.",
   "bina termination के signal reflect होकर garbage बनाता है — 50-ohm terminator रोकता है।"),
  ("Terminator = signal ko absorb karne wala resistor; crosstalk = adjacent wires "
   "ka interference.",
   "Terminator = signal absorb करता है; crosstalk = पास की wires का interference।"),
  {}),
]

P1_E_X = [
 (SRC,
  "A high-speed network that connects servers to storage devices (disk arrays, tape libraries) is called:",
  "Servers को storage devices (disk arrays, tape libraries) से जोड़ने वाली high-speed network कहलाती है:",
  [("SAN (Storage Area Network)", "SAN (Storage Area Network)"),
   ("CAN (Campus Area Network)", "CAN (Campus Area Network)"),
   ("PAN (Personal Area Network)", "PAN (Personal Area Network)"),
   ("MAN (Metropolitan Area Network)", "MAN (Metropolitan Area Network)")],
  0,
  ("SAN data-centre technology hai — servers aur storage ko dedicated high-speed "
   "network (Fibre Channel/iSCSI) se jodti hai.",
   "SAN servers और storage को dedicated high-speed network से जोड़ती है।"),
  ("CAN = campus buildings; PAN = personal devices; MAN = city — ye sab "
   "general-purpose networks hain.",
   "CAN = campus; PAN = personal devices; MAN = शहर।"),
  {}),
]

P1_F_X = [
 (SRC,
  "The NSF backbone network that replaced ARPANET as the Internet's main backbone in the 1980s was:",
  "1980s में ARPANET की जगह Internet का मुख्य backbone बना NSF का network था:",
  [("NSFNET", "NSFNET"), ("MILNET", "MILNET"), ("BITNET", "BITNET"),
   ("USENET", "USENET")],
  0,
  ("NSFNET (1986) ne supercomputer centres ko joda aur ARPANET ki jagah le li; "
   "ARPANET 1990 mein retire hua.",
   "NSFNET (1986) ने supercomputer centres जोड़े; ARPANET 1990 में हटा।"),
  ("MILNET = 1983 mein ARPANET se alag hua military hissa; BITNET/USENET = "
   "academic networks, backbone nahi.",
   "MILNET = 1983 में अलग हुआ; BITNET/USENET = academic networks।"),
  {}),
]

P1_G_X = [
 (SRC,
  "In ATM (Asynchronous Transfer Mode) switching, data is carried in fixed-size cells of ______ bytes:",
  "ATM (Asynchronous Transfer Mode) switching में data ______ bytes की fixed-size cells में जाता है:",
  [("53", "53"), ("64", "64"), ("128", "128"), ("1500", "1500")],
  0,
  ("ATM cell = 53 bytes = 48-byte payload + 5-byte header — fixed size se "
   "hardware switching fast hota hai.",
   "ATM cell = 53 bytes = 48 payload + 5 header।"),
  ("64 = Ethernet ka minimum frame; 1500 = Ethernet ka maximum payload — "
   "ye ATM ke cell size nahi.",
   "64 = Ethernet minimum frame; 1500 = Ethernet maximum payload।"),
  {}),
]

# ------------------------------- TOPIC 2 -------------------------------
P2_A_X = [
 (SRC,
  "In the OSI model, error control as well as flow control are performed by which TWO layers?",
  "OSI model में error control और flow control दोनों किन दो layers में होते हैं?",
  [("Physical and Network", "Physical और Network"),
   ("Data Link and Transport", "Data Link और Transport"),
   ("Transport and Session", "Transport और Session"),
   ("Network and Session", "Network और Session")],
  1,
  ("Data link = link (node-to-node) par flow+error control; transport = end-to-end "
   "par flow+error control — dono layers ye dono kaam karti hain.",
   "Data link = link पर; transport = end-to-end — दोनों layers ये काम करती हैं।"),
  ("Network layer sirf routing/forwarding; session = dialog control.",
   "Network layer सिर्फ routing; session = dialog control।"),
  {}),
]

P2_B_X = [
 (SRC,
  "Dialog control and synchronization of data exchange between two applications is the responsibility of which OSI layer?",
  "दो applications के बीच dialog control और data exchange का synchronization किस OSI layer का काम है?",
  [("Session layer", "Session layer"), ("Transport layer", "Transport layer"),
   ("Presentation layer", "Presentation layer"), ("Application layer", "Application layer")],
  0,
  ("Session layer dialogue manage karti hai — kaun kab bolega (dialog control), "
   "sync points lagakar recovery possible karti hai.",
   "Session layer dialogue manage करती है — कौन कब बोलेगा, sync points लगाती है।"),
  ("Transport = end-to-end delivery; presentation = format/encryption; "
   "application = user services.",
   "Transport = delivery; presentation = format; application = user services।"),
  {}),
]

P2_C_X = [
 (SRC,
  "In the TCP/IP model, process-to-process (program-to-program) communication is provided by the:",
  "TCP/IP model में process-to-process (program-to-program) संवाद किसके द्वारा होता है?",
  [("Internet layer", "Internet layer"), ("Transport layer", "Transport layer"),
   ("Network access layer", "Network access layer"), ("Application layer", "Application layer")],
  1,
  ("Transport (TCP/UDP) ports ke through processes ko jodta hai; Internet layer "
   "sirf host-to-host (best-effort) delivery karti hai.",
   "Transport (TCP/UDP) ports से processes जोड़ता है; Internet layer host-to-host delivery।"),
  ("Yaad rakho: Network/Internet = host-to-host; Transport = process-to-process.",
   "Network/Internet = host-to-host; Transport = process-to-process।"),
  {}),
]

P2_D_X = [
 (SRC,
  "On the sending host, encapsulation adds headers in which order as the message moves down the OSI stack?",
  "Sending host पर message नीचे OSI stack में जाते समय headers किस क्रम में जुड़ते हैं?",
  [("Application → Transport → Network → Data Link",
    "Application → Transport → Network → Data Link"),
   ("Data Link → Network → Transport → Application",
    "Data Link → Network → Transport → Application"),
   ("Network → Application → Transport → Data Link",
    "Network → Application → Transport → Data Link"),
   ("Transport → Application → Data Link → Network",
    "Transport → Application → Data Link → Network")],
  0,
  ("Data upar se neeche jaata hai: pehle application data, phir transport header "
   "(segment), network header (datagram), data-link header+trailer (frame). "
   "Receiver par ulta (bottom-up) order mein headers hatti hain.",
   "ऊपर से नीचे: application data → transport → network → data-link; receiver पर उल्टे क्रम में।"),
  ("Encapsulation = har layer apna header add karti hai; decapsulation = reverse.",
   "Encapsulation = हर layer header जोड़ती है; decapsulation = उल्टा।"),
  {}),
]

# ------------------------------- TOPIC 3 -------------------------------
P3_A_X = [
 (SRC,
  "MAC (hardware) addresses are assigned to NIC manufacturers and administered by:",
  "MAC (hardware) addresses NIC manufacturers को दी जाती हैं और इनका प्रबंधन करता है:",
  [("IEEE", "IEEE"), ("IANA", "IANA"), ("ICANN", "ICANN"), ("ITU", "ITU")],
  0,
  ("IEEE har manufacturer ko OUI (3-byte prefix) allot karta hai; baaki bytes "
   "manufacturer khud lagata hai.",
   "IEEE हर manufacturer को OUI (3 bytes) देता है; बाकी bytes वह खुद लगाता है।"),
  ("IANA = IP addresses/port numbers; ICANN = domain names; ITU = "
   "telecom standards.",
   "IANA = IP/ports; ICANN = domains; ITU = telecom।"),
  {}),
]

P3_B_X = [
 (SRC,
  "The IPv4 address block 100.64.0.0/10 is reserved by IANA for:",
  "IPv4 address block 100.64.0.0/10 IANA द्वारा किसके लिए आरक्षित है?",
  [("Carrier-grade NAT (shared address space)", "Carrier-grade NAT (shared address space)"),
   ("Loopback testing", "Loopback testing"), ("Multicasting", "Multicasting"),
   ("Experimental use", "Experimental use")],
  0,
  ("100.64.0.0/10 = CGNAT/ISP ke andar private addressing (RFC 6598) — jab "
   "ISP ke paas public IPs kam hon. 127=loopback, 224=multicast, 240/4=experimental.",
   "100.64.0.0/10 = CGNAT (RFC 6598) — ISP आंतरिक addressing; 127=loopback, 224=multicast।"),
  ("Ye IANA special-purpose registry ka block hai — worldwide exams mein "
   "pucha jaata hai.",
   "यह IANA special registry का block है।"),
  {}),
]

P3_C_X = [
 (SRC,
  "The usable host range of the CIDR block 172.16.45.64/26 is:",
  "CIDR block 172.16.45.64/26 की usable host range है:",
  [("172.16.45.65 – 172.16.45.126", "172.16.45.65 – 172.16.45.126"),
   ("172.16.45.65 – 172.16.45.127", "172.16.45.65 – 172.16.45.127"),
   ("172.16.45.64 – 172.16.45.127", "172.16.45.64 – 172.16.45.127"),
   ("172.16.45.1 – 172.16.45.254", "172.16.45.1 – 172.16.45.254")],
  0,
  ("/26 = 26 network bits → block size 64. 64 se 127 tak ka block: network=64, "
   "broadcast=127, beech ke 62 addresses usable (65–126).",
   "/26 → block size 64; network=64, broadcast=127; usable = 65–126 (62 addresses)।"),
  ("Broadcast address (127) aur network address (64) hosts ko nahi milte.",
   "Broadcast (127) और network (64) address host को नहीं मिलते।"),
  {}),
 (SRC,
  "For point-to-point links between routers, a /30 prefix is preferred because it provides exactly ______ usable host addresses:",
  "Routers के बीच point-to-point links के लिए /30 prefix क्यों पसंद किया जाता है? यह ठीक ______ usable addresses देता है:",
  [("2", "2"), ("4", "4"), ("6", "6"), ("14", "14")],
  0,
  ("/30 = 4 addresses: network + broadcast + 2 hosts — P2P link par sirf 2 "
   "interfaces hote hain, isliye ideal.",
   "/30 = 4 addresses: network + broadcast + 2 hosts — P2P link के लिए ideal।"),
  ("2^2=4 addresses total; 2 reserved; 2 usable.",
   "कुल 4 में से 2 reserved; 2 usable।"),
  {}),
]

P3_D_X = [
 (SRC,
  "In IPv6, a host can generate its own address automatically without any DHCP server using:",
  "IPv6 में host बिना DHCP server के अपना address स्वयं बना सकता है — किसके द्वारा?",
  [("SLAAC (Stateless Address Autoconfiguration)", "SLAAC (Stateless Address Autoconfiguration)"),
   ("ARP", "ARP"), ("BOOTP", "BOOTP"), ("NAT-PT", "NAT-PT")],
  0,
  ("SLAAC: router ke RA (Router Advertisement) se prefix milta hai aur host "
   "apna Interface ID (EUI-64/random) khud jod leta hai — stateless.",
   "SLAAC: router के RA से prefix मिलता है, host अपना Interface ID जोड़ लेता है।"),
  ("ARP = IPv4 MAC resolution; BOOTP = DHCP ka purana version; NAT-PT = "
   "IPv4-IPv6 translation.",
   "ARP = MAC resolution; BOOTP = DHCP पुराना; NAT-PT = translation।"),
  {}),
 (SRC,
  "The prefix used for IPv6 link-local addresses (usable only on the local link) is:",
  "IPv6 link-local addresses (सिर्फ उसी link पर काम करने वाले) का prefix होता है:",
  [("FE80::/10", "FE80::/10"), ("2000::/3", "2000::/3"),
   ("FF00::/8", "FF00::/8"), ("::1/128", "::1/128")],
  0,
  ("FE80::/10 = link-local (har interface par automatically); 2000::/3 = global "
   "unicast; FF00::/8 = multicast; ::1 = loopback.",
   "FE80::/10 = link-local; 2000::/3 = global unicast; FF00::/8 = multicast; ::1 = loopback।"),
  ("Link-local = bina router ke same-link communication (neighbour discovery).",
   "Link-local = बिना router के उसी link पर communication।"),
  {}),
]

P3_E_X = [
 (SRC,
  "DNS zone transfers between primary and secondary name servers use:",
  "Primary और secondary name servers के बीच DNS zone transfer प्रयोग करती है:",
  [("TCP port 53", "TCP port 53"), ("UDP port 53", "UDP port 53"),
   ("UDP port 69", "UDP port 69"), ("TCP port 25", "TCP port 25")],
  0,
  ("Normal DNS query = UDP 53 (chhota request/response); zone transfer = pura "
   "zone ka bulk data — reliable TCP 53 chahiye.",
   "सामान्य query = UDP 53; zone transfer = bulk data — इसलिए TCP 53।"),
  ("UDP 53 = queries; UDP 69 = TFTP; TCP 25 = SMTP.",
   "UDP 53 = queries; UDP 69 = TFTP; TCP 25 = SMTP।"),
  {}),
]

# ------------------------------- TOPIC 4 -------------------------------
P4_A_X = [
 (SRC,
  "A 24-port hub creates how many collision domains?",
  "24-port hub कितने collision domains बनाता है?",
  [("1", "1"), ("12", "12"), ("24", "24"), ("48", "48")],
  0,
  ("Hub ek shared segment hai — saare ports ek hi collision domain mein hain "
   "(switch hota to har port apna collision domain).",
   "Hub एक shared segment है — सारे ports एक ही collision domain में (switch में हर port अलग)।"),
  ("Hub = layer-1 dumb device, signal ko sab ports par repeat karta hai.",
   "Hub = layer-1 device, signal सब ports पर repeat करता है।"),
  {}),
]

P4_B_X = [
 (SRC,
  "Connecting each switch port to a single host so that every port becomes its own collision domain is called:",
  "Switch के हर port पर एक host लगाकर उसे अलग collision domain बनाना कहलाता है:",
  [("Microsegmentation", "Microsegmentation"), ("Trunking", "Trunking"),
   ("VLAN hopping", "VLAN hopping"), ("Bridging loop", "Bridging loop")],
  0,
  ("Microsegmentation se collisions khatam — full-duplex possible; trunking = "
   "multiple VLANs ka traffic ek link par.",
   "Microsegmentation से collisions खत्म; trunking = कई VLANs का traffic एक link पर।"),
  ("Collision domain ka size chhota karna hi microsegmentation hai.",
   "Collision domain छोटा करना = microsegmentation।"),
  {}),
]

P4_C_X = [
 (SRC,
  "A brouter forwards non-routable protocols (e.g., NetBEUI) at OSI layer ______ and routable protocols (e.g., IP) at layer 3:",
  "Brouter non-routable protocols (जैसे NetBEUI) को OSI layer ______ पर और routable protocols (IP) को layer 3 पर भेजता है:",
  [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
  1,
  ("Brouter = bridge + router: jin protocols par routing possible nahi unke liye "
   "bridge (layer 2) ki tarah; routable ke liye router (layer 3) ki tarah.",
   "Brouter = bridge + router: गैर-routable के लिए bridge (layer 2), routable के लिए router (layer 3)।"),
  ("Bridge ka kaam = MAC addresses se frame forward karna.",
   "Bridge = MAC addresses से frame forward करता है।"),
  {}),
]

P4_D_X = [
 (SRC,
  "Port Address Translation (PAT), which maps many private IP addresses to one public IP using port numbers, is also called:",
  "Port Address Translation (PAT) — जो port numbers से कई private IPs को एक public IP पर map करती है — कहलाती है भी:",
  [("NAT overload", "NAT overload"), ("Static NAT", "Static NAT"),
   ("Dynamic NAT", "Dynamic NAT"), ("Proxy NAT", "Proxy NAT")],
  0,
  ("Cisco terminology: 'ip nat inside source list … overload' = PAT = NAT "
   "overload — ek public IP se 65536 tak connections.",
   "Cisco में '… overload' = PAT = NAT overload — एक public IP से हजारों connections।"),
  ("Static NAT = 1:1 fixed mapping; dynamic NAT = pool se temporary 1:1.",
   "Static NAT = 1:1 fixed; dynamic NAT = pool से temporary 1:1।"),
  {}),
]

# ------------------------------- TOPIC 5 -------------------------------
P5_A_X = [
 (SRC,
  "According to Shannon's capacity theorem, a 1 MHz channel with SNR = 30 dB has a capacity of approximately:",
  "Shannon के सूत्र से 1 MHz channel जिसका SNR = 30 dB हो, की capacity लगभग होगी:",
  [("10 Mbps", "10 Mbps"), ("20 Mbps", "20 Mbps"),
   ("30 Mbps", "30 Mbps"), ("1 Mbps", "1 Mbps")],
  0,
  ("SNR(dB) = 30 → SNR = 1000. C = B × log2(1+SNR) = 10^6 × log2(1001) ≈ 10^6 × "
   "9.97 ≈ 10 Mbps.",
   "SNR(dB)=30 → SNR=1000; C = 10^6 × log2(1001) ≈ 10 Mbps।"),
  ("Shannon mein SNR linear value lagti hai, dB nahi — pehle convert karo.",
   "Shannon में SNR linear value लगती है, dB नहीं।"),
  {}),
 (SRC,
  "In NRZ-I encoding, a binary 1 is represented by:",
  "NRZ-I encoding में binary 1 को दर्शाया जाता है:",
  [("A transition at the beginning of the bit interval",
    "Bit interval की शुरुआत में transition"),
   ("No transition at all", "कोई transition नहीं"),
   ("A transition in the middle of the bit", "Bit के बीच में transition"),
   ("A positive voltage", "धनात्मक voltage")],
  0,
  ("NRZ-I (Invert): 1 = signal invert (transition) at start of bit; 0 = "
   "no transition. Consecutive 1s ke liye clock sync rehti hai.",
   "NRZ-I: 1 = bit की शुरुआत में invert/transition; 0 = बिना transition।"),
  ("Middle transition = Manchester (har bit mein); NRZ-I mein middle nahi.",
   "बीच का transition = Manchester; NRZ-I में नहीं।"),
  {}),
]

P5_B_X = [
 (SRC,
  "Which twisted-pair cable standard supports 10 Gbps Ethernet over the full 100 m channel?",
  "कौन-सी twisted-pair cable standard पूरे 100 m channel पर 10 Gbps Ethernet चलाती है?",
  [("Cat5e", "Cat5e"), ("Cat6", "Cat6"), ("Cat6a", "Cat6a"), ("Cat3", "Cat3")],
  2,
  ("Cat6a = 10 Gbps @ 100 m (augmented, alien-crosstalk controlled); Cat6 = "
   "10 Gbps sirf ~55 m tak.",
   "Cat6a = 10 Gbps @ 100 m; Cat6 = 10 Gbps सिर्फ ~55 m तक।"),
  ("Cat5e = 1 Gbps; Cat3 = 10 Mbps (purani voice-grade).",
   "Cat5e = 1 Gbps; Cat3 = 10 Mbps।"),
  {}),
]

P5_C_X = [
 (SRC,
  "The IEEE 802.11n (Wi-Fi 4) standard greatly increased wireless throughput by using multiple antennas for parallel data streams, a technology called:",
  "IEEE 802.11n (Wi-Fi 4) ने throughput बढ़ाने के लिए कई antennas से समांतर data streams भेजीं — यह तकनीक है:",
  [("MIMO", "MIMO"), ("OFDM", "OFDM"), ("DSSS", "DSSS"), ("FHSS", "FHSS")],
  0,
  ("MIMO (Multiple-Input Multiple-Output) = multiple spatial streams; 802.11n "
   "se 600 Mbps tak theoretical rate; OFDM pehle 802.11a/g mein tha.",
   "MIMO = कई spatial streams; 802.11n से सैद्धांतिक 600 Mbps; OFDM 802.11a/g में था।"),
  ("OFDM = subcarriers par modulation (802.11a/g); DSSS/FHSS = purani spread "
   "spectrum techniques (802.11b).",
   "OFDM = subcarriers (802.11a/g); DSSS/FHSS = पुरानी techniques (802.11b)।"),
  {}),
]

# ------------------------------- TOPIC 6 -------------------------------
P6_A_X = [
 (SRC,
  "In Go-Back-N ARQ, the receiver's window size is:",
  "Go-Back-N ARQ में receiver की window size होती है:",
  [("1", "1"), ("Same as the sender's window", "Sender की window के बराबर"),
   ("2^(n−1)", "2^(n−1)"), ("Unbounded", "असीमित")],
  0,
  ("GBN receiver sirf agla expected frame accept karta hai (window=1); isliye "
   "out-of-order frame aaye to use phenk kar pura Go-Back-N retransmission hota hai.",
   "GBN में receiver सिर्फ अगला expected frame लेता है (window=1); out-of-order आने पर पूरा Go-Back-N।"),
  ("Selective Repeat mein receiver ki window badi hoti hai — wahi out-of-order "
   "frames buffer karta hai.",
   "Selective Repeat में receiver window बड़ी — out-of-order buffer होते हैं।"),
  {}),
 (SRC,
  "Delaying an acknowledgement so that it can be attached to the next outgoing data frame in the reverse direction is called:",
  "Acknowledgement को रोककर विपरीत दिशा में जाने वाले अगले data frame के साथ जोड़ना कहलाता है:",
  [("Piggybacking", "Piggybacking"), ("Broadcasting", "Broadcasting"),
   ("Framing", "Framing"), ("Stuffing", "Stuffing")],
  0,
  ("Piggybacking: bidirectional link par ack ko data frame ke saath chipka do — "
   "alag ack frame bachta hai, bandwidth bachti hai.",
   "Piggybacking: bidirectional link पर ack को data frame के साथ जोड़ना — bandwidth बचती है।"),
  ("Piggybacking mein ack ke liye timer hota hai, taaki der zyada na ho.",
   "Piggybacking में ack timer होता है, ताकि देर न हो।"),
  {}),
]

P6_B_X = [
 (SRC,
  "Gigabit Ethernet over optical fiber is defined by which IEEE standard?",
  "Optical fiber पर Gigabit Ethernet किस IEEE standard में परिभाषित है?",
  [("802.3z", "802.3z"), ("802.3ab", "802.3ab"), ("802.3u", "802.3u"),
   ("802.3ae", "802.3ae")],
  0,
  ("802.3z = 1000BASE-X (fiber/STP); 802.3ab = 1000BASE-T (UTP); 802.3u = "
   "Fast Ethernet (100 Mbps); 802.3ae = 10 Gbps Ethernet.",
   "802.3z = 1000BASE-X (fiber); 802.3ab = 1000BASE-T (UTP); 802.3u = Fast Ethernet; 802.3ae = 10 GbE।"),
  ("Suffix -T = twisted pair, -X = fiber — standard numbers yaad rakho.",
   "-T = twisted pair, -X = fiber।"),
  {}),
]

P6_C_X = [
 (SRC,
  "OSPF exchanges routing information directly over IP using IP protocol number:",
  "OSPF routing information IP पर सीधे भेजता है — IP protocol number होता है:",
  [("89", "89"), ("179", "179"), ("520", "520"), ("6", "6")],
  0,
  ("OSPF = IP protocol 89 (na TCP na UDP); BGP = TCP 179; RIP = UDP 520; "
   "protocol 6 = TCP.",
   "OSPF = IP protocol 89 (न TCP न UDP); BGP = TCP 179; RIP = UDP 520।"),
  ("Ye teen (89/179/520) worldwide exams ke favourite hain.",
   "ये तीनों (89/179/520) exams के प्रिय प्रश्न हैं।"),
  {}),
 (SRC,
  "BGP, the protocol that routes between autonomous systems on the Internet, uses:",
  "BGP — जो Internet पर autonomous systems के बीच routing करता है — प्रयोग करता है:",
  [("TCP port 179", "TCP port 179"), ("IP protocol 89", "IP protocol 89"),
   ("UDP port 520", "UDP port 520"), ("TCP port 23", "TCP port 23")],
  0,
  ("BGP = TCP port 179 — reliable transport chahiye Internet-scale routing ke liye.",
   "BGP = TCP port 179 — Internet-scale routing के लिए reliable transport।"),
  ("89 = OSPF; 520 = RIP; 23 = Telnet.",
   "89 = OSPF; 520 = RIP; 23 = Telnet।"),
  {}),
 (SRC,
  "The RIP routing protocol uses which transport protocol and port number?",
  "RIP routing protocol कौन-सा transport protocol और port number प्रयोग करता है?",
  [("UDP port 520", "UDP port 520"), ("TCP port 520", "TCP port 520"),
   ("UDP port 161", "UDP port 161"), ("TCP port 89", "TCP port 89")],
  0,
  ("RIP = UDP 520 (chhote periodic updates, reliable transport ki zaroorat nahi).",
   "RIP = UDP 520 (छोटे periodic updates)।"),
  ("161 = SNMP; TCP 89 kuch nahi (OSPF TCP par nahi chalta).",
   "161 = SNMP; TCP 89 — कुछ नहीं (OSPF TCP पर नहीं चलता)।"),
  {}),
]

P6_D_X = [
 (SRC,
  "After a TCP connection is closed, the side performing the active close waits in the TIME-WAIT state for:",
  "TCP connection बंद होने के बाद active close करने वाला पक्ष TIME-WAIT state में रहता है:",
  [("2 × MSL (Maximum Segment Lifetime)", "2 × MSL (Maximum Segment Lifetime)"),
   ("1 × RTT", "1 × RTT"), ("3 × RTT", "3 × RTT"),
   ("One congestion timeout", "एक congestion timeout")],
  0,
  ("2×MSL wait se purane connection ke delayed duplicate segments khatam ho "
   "jaate hain, naya connection safe rehta hai (RFC 793).",
   "2×MSL के इंतज़ार से पुराने duplicates खत्म होते हैं (RFC 793)।"),
  ("MSL = maximum time ek segment Internet mein reh sakta hai.",
   "MSL = segment का अधिकतम जीवनकाल।"),
  {}),
 (SRC,
  "The 8-byte UDP header consists of which fields?",
  "8-byte UDP header में कौन-से fields होते हैं?",
  [("Source port, destination port, length, checksum",
    "Source port, destination port, length, checksum"),
   ("Source port, destination port, sequence number, ack number",
    "Source port, destination port, sequence number, ack number"),
   ("Source port, destination port, window, checksum",
    "Source port, destination port, window, checksum"),
   ("Ports, length, checksum, urgent pointer",
    "Ports, length, checksum, urgent pointer")],
  0,
  ("UDP header = 4 fields × 2 bytes = 8 bytes; sequence/ack/window — sab TCP "
   "ke fields hain.",
   "UDP header = 4 fields × 2 bytes = 8; sequence/ack/window — TCP के fields।"),
  ("UDP ka mantra: 'chhota header, koi guarantee nahi'.",
   "UDP: 'छोटा header, कोई guarantee नहीं'।"),
  {}),
]

P6_E_X = [
 (SRC,
  "DHCP uses which pair of UDP ports (server port, client port)?",
  "DHCP कौन-सी UDP ports की जोड़ी प्रयोग करता है (server port, client port)?",
  [("67 and 68", "67 और 68"), ("69 and 70", "69 और 70"),
   ("53 and 54", "53 और 54"), ("20 and 21", "20 और 21")],
  0,
  ("DHCP server = UDP 67, DHCP client = UDP 68 (DORA process in dono ports par).",
   "DHCP server = UDP 67, client = UDP 68 (DORA इन्हीं पर)।"),
  ("69 = TFTP; 53 = DNS; 20/21 = FTP data/control.",
   "69 = TFTP; 53 = DNS; 20/21 = FTP।"),
  {}),
]

# ------------------------------- TOPIC 7 -------------------------------
P7_A_X = [
 (SRC,
  "A SYN flood (denial-of-service) attack exploits which part of network communication?",
  "SYN flood (denial-of-service) attack संचार के किस भाग का दुरुपयोग करता है?",
  [("The TCP three-way handshake", "TCP three-way handshake"),
   ("The DNS resolution process", "DNS resolution process"),
   ("The ARP cache", "ARP cache"),
   ("The ICMP echo request", "ICMP echo request")],
  0,
  ("Attacker dheron SYN bhejta hai — server har ek ke liye half-open connection "
   "banata hai (SYN-RECV) aur resources khatam ho jaate hain.",
   "Attacker ढेरों SYN भेजता है — server की half-open connections से resources खत्म होती हैं।"),
  ("ARP spoofing = cache poisoning; ICMP flood = echo requests — alag attacks.",
   "ARP spoofing = cache poisoning; ICMP flood = echo — अलग attacks।"),
  {}),
]

P7_B_X = [
 (SRC,
  "The AES symmetric encryption standard supports key sizes of:",
  "AES symmetric encryption standard की key sizes होती हैं:",
  [("128, 192 and 256 bits", "128, 192 और 256 bits"),
   ("56, 128 and 256 bits", "56, 128 और 256 bits"),
   ("1024, 2048 and 4096 bits", "1024, 2048 और 4096 bits"),
   ("64, 128 and 192 bits", "64, 128 और 192 bits")],
  0,
  ("AES (Rijndael): 128/192/256-bit keys, 128-bit blocks; DES = 56-bit key "
   "(purana); RSA 1024+ = asymmetric.",
   "AES: 128/192/256-bit keys, 128-bit blocks; DES = 56-bit; RSA 1024+ = asymmetric।"),
  ("Symmetric = chhoti keys (128-256); asymmetric = badi keys (1024+).",
   "Symmetric = छोटी keys; asymmetric = बड़ी keys।"),
  {}),
]

P7_C_X = [
 (SRC,
  "Which IPSec protocol provides encryption (confidentiality) of the packet data?",
  "IPSec का कौन-सा protocol packet data की encryption (confidentiality) देता है?",
  [("ESP", "ESP"), ("AH", "AH"), ("IKE", "IKE"), ("HMAC", "HMAC")],
  0,
  ("ESP (Encapsulating Security Payload) = encryption + integrity + optional "
   "authentication; AH = authentication + integrity, encryption nahi.",
   "ESP = encryption + integrity; AH = authentication + integrity, encryption नहीं।"),
  ("IKE = key exchange ka protocol; HMAC = message authentication code.",
   "IKE = key exchange; HMAC = authentication code।"),
  {}),
 (SRC,
  "In which IPSec mode is the original IP header encrypted together with the payload (as used in VPNs)?",
  "IPSec की किस mode में मूल IP header भी payload के साथ encrypt होता है (जैसे VPN में)?",
  [("Tunnel mode", "Tunnel mode"), ("Transport mode", "Transport mode"),
   ("Transparent mode", "Transparent mode"), ("Stealth mode", "Stealth mode")],
  0,
  ("Tunnel mode = pura original packet encapsulate + encrypt, naya outer header "
   "lagta hai — site-to-site VPNs isi par chalti hain. Transport mode mein sirf "
   "payload encrypt hota hai, original header khula.",
   "Tunnel mode = पूरा packet encapsulate + encrypt, नया outer header; VPN इसी में। Transport mode में सिर्फ payload encrypt।"),
  ("Transport mode = host-to-host security (jaise IPsec ke andar TLS jaisa use).",
   "Transport mode = host-to-host security।"),
  {}),
]
