# -*- coding: utf-8 -*-
"""ORIGINAL practice questions — WAVE 5 (master-spec source-wave pass).

Source wave: `Computer Network/new/` repo compilations (computer-networks [set
1–20] McqMate extracts, DCN_MCQ-Ashwini bank) — extracted 1008 candidates,
deduped against the 801-record bank (24 exact + 169 near overlaps dropped,
179 internal repeats dropped). GENUINELY NEW concepts are re-authored here in
original wording (spec §7: no verbatim copying of compiled banks) with
independently verified answers (dump answer errors corrected, e.g. the pool's
RSVP item was mislabelled to DHCP).

Rule: NO question may repeat anything in topic*_data.py or practice_new_p1..p4.
Section lists use the `*_X3` suffix (auto-attached by the builders).
"""
SRC = "Practice — original (textbook-based)"

# ------------------------------- TOPIC 1 -------------------------------
P1_E_X3 = [
 (SRC,
  "In a ______ network, the communication channel is shared by all the machines on the network:",
  "______ network में communication channel network की सभी machines में साझा होता है:",
  [("Broadcast (multipoint) network", "Broadcast (multipoint) network"),
   ("Point-to-point network", "Point-to-point network"),
   ("Circuit-switched WAN", "Circuit-switched WAN"),
   ("Extranet", "Extranet")],
  0,
  ("Broadcast/multipoint network mein ek shared channel sab hosts tak pahunchta "
   "hai (jaise bus/Ethernet) — point-to-point mein sirf do ends hote hain.",
   "Broadcast/multipoint network में एक shared channel सभी hosts तक जाता है; point-to-point में सिर्फ दो ends।"),
  ("Yaad rakho: point-to-point = dedicated link; multipoint/broadcast = shared medium.",
   "point-to-point = dedicated link; multipoint/broadcast = shared medium।"),
  {}),
]

P1_G_X3 = [
 (SRC,
  "In ______ switching, the resources needed for communication are reserved for the duration of the session:",
  "______ switching में, संचार के लिए आवश्यक संसाधन पूरे session की अवधि के लिए आरक्षित रहते हैं:",
  [("Circuit", "Circuit"), ("Packet", "Packet"), ("Message", "Message"), ("Cell", "Cell")],
  0,
  ("Circuit switching: connection ke pehle path + bandwidth reserve hoti hai "
   "(telephone jaisa); packet switching mein koi reservation nahi.",
   "Circuit switching में path + bandwidth पहले से आरक्षित; packet switching में कोई reservation नहीं।"),
  ("Reservation = circuit; store-and-forward = packet/message.",
   "Reservation = circuit; store-and-forward = packet/message।"),
  {}),
]

# ------------------------------- TOPIC 2 -------------------------------
P2_D_X3 = [
 (SRC,
  "The list of protocols used by a system — one protocol per layer — is called a:",
  "किसी system द्वारा प्रयोग की जाने वाली protocols की सूची — हर layer पर एक protocol — कहलाती है:",
  [("Protocol stack (protocol suite)", "Protocol stack (protocol suite)"),
   ("Protocol syntax", "Protocol syntax"), ("Encapsulation table", "Encapsulation table"),
   ("Address map", "Address map")],
  0,
  ("Protocol stack = layered list (jaise TCP/IP stack: IP, TCP, HTTP...). "
   "Har layer apna protocol chunta hai — 'suite' bhi kehte hain.",
   "Protocol stack = layer-wise सूची (जैसे TCP/IP stack)।"),
  ("Syntax = message ka format; stack = layers ka protocol set.",
   "Syntax = format; stack = layers का protocol set।"),
  {}),
]

# ------------------------------- TOPIC 3 -------------------------------
P3_D_X3 = [
 (SRC,
  "In IPv6, the field that determines the lifetime of a datagram (the counterpart of IPv4's TTL) is called:",
  "IPv6 में, datagram का जीवन-काल तय करने वाला field (IPv4 के TTL के समकक्ष) कहलाता है:",
  [("Hop Limit", "Hop Limit"), ("Flow Label", "Flow Label"),
   ("Next Header", "Next Header"), ("Payload Length", "Payload Length")],
  0,
  ("IPv6 Hop Limit = har hop par 1 ghat-ta hai (TTL jaisa); Flow Label = QoS "
   "flow pehchaan; Next Header = agla extension/upper-layer header; Payload "
   "Length = data ki lambai.",
   "IPv6 Hop Limit = हर hop पर 1 घटता है (TTL जैसा)। बाकी fields अन्य कामों के लिए।"),
  ("IPv6 ke 8 base-header fields: Version, Traffic Class, Flow Label, Payload "
   "Length, Next Header, Hop Limit, Src, Dst.",
   "IPv6 के base-header fields: Version, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, Src, Dst।"),
  {}),
 (SRC,
  "In the dual-stack approach to IPv6 migration, a host or router runs:",
  "IPv6 migration के dual-stack तरीके में, host या router चलाता है:",
  [("Both IPv4 and IPv6 protocols simultaneously", "IPv4 और IPv6 दोनों protocols साथ-साथ"),
   ("Only IPv6 with IPv4 tunnels", "सिर्फ IPv6, IPv4 tunnels के साथ"),
   ("Only IPv4 with IPv6 headers", "सिर्फ IPv4, IPv6 headers के साथ"),
   ("Neither — only translation", "कोई नहीं — सिर्फ translation")],
  0,
  ("Dual stack: dono protocols ek saath — jo destination IPv4 samajhe woh IPv4 "
   "se, jo IPv6 woh IPv6 se. Tunneling/translation alag strategies hain.",
   "Dual stack: दोनों protocols साथ; tunneling/translation अलग रणनीतियाँ हैं।"),
  ("IPv6 migration ke 3 tarika: dual stack, tunneling, translation.",
   "IPv6 migration के 3 तरीके: dual stack, tunneling, translation।"),
  {}),
 (SRC,
  "Teredo is an IPv6 transition technique that provides IPv6 connectivity to hosts behind NAT by:",
  "Teredo एक IPv6 transition तकनीक है जो NAT के पीछे के hosts को IPv6 connectivity देती है:",
  [("Encapsulating IPv6 packets inside UDP datagrams over IPv4",
    "IPv6 packets को IPv4 पर UDP datagrams के अंदर encapsulate करके"),
   ("Translating every IPv6 header to IPv4", "हर IPv6 header को IPv4 में बदलकर"),
   ("Reserving public IPv6 blocks per host", "हर host के लिए सार्वजनिक IPv6 blocks आरक्षित करके"),
   ("Broadcasting IPv6 router solicitations", "IPv6 router solicitations broadcast करके")],
  0,
  ("Teredo (RFC 4380): IPv6-in-UDP-over-IPv4 tunneling — NAT traversal ke liye "
   "UDP ports use hote hain. 6to4 alag hai (IPv6-in-IPv4, proto 41).",
   "Teredo (RFC 4380): IPv6-in-UDP-over-IPv4 tunneling — NAT traversal हेतु UDP ports।"),
  ("Teredo = UDP; 6to4 = IPv4 protocol 41; dual stack = dono protocols native.",
   "Teredo = UDP; 6to4 = IPv4 protocol 41; dual stack = दोनों native।"),
  {}),
]

# ------------------------------- TOPIC 5 -------------------------------
P5_B_X3 = [
 (SRC,
  "A coaxial cable consists of ______ concentric copper conductors:",
  "Coaxial cable में ______ संकेंद्रित (concentric) copper conductors होते हैं:",
  [("Two (inner wire + outer shield)", "दो (भीतरी तार + बाहरी shield)"),
   ("Four", "चार"), ("Eight", "आठ"), ("One", "एक")],
  0,
  ("Coax: beech mein inner copper conductor, uske chaaron taraf outer copper "
   "shield — dono ke beech insulator. Isi se EMI resistance aati hai.",
   "Coax: भीतरी copper conductor और बाहरी copper shield — बीच में insulator।"),
  ("UTP = 4 pairs (8 wires); coax = 2 concentric conductors.",
   "UTP = 4 pairs; coax = 2 संकेंद्रित conductors।"),
  {}),
 (SRC,
  "10Base5, 10Base2 and 10BaseT are different types of:",
  "10Base5, 10Base2 और 10BaseT हैं किसके अलग-अलग प्रकार:",
  [("Ethernet", "Ethernet"), ("Token Ring", "Token Ring"), ("FDDI", "FDDI"), ("ATM", "ATM")],
  0,
  ("Ye sab Ethernet cable standards hain: 10 Mbps; Base = baseband. "
   "10Base5 = thick coax (Thicknet), 10Base2 = thin coax (Thinnet), 10BaseT = UTP.",
   "ये सब Ethernet cable standards हैं (10 Mbps, baseband): 10Base5 thick coax, 10Base2 thin coax, 10BaseT UTP।"),
  ("Suffix: 5/2 = segment length (sau metre mein); T = twisted pair.",
   "Suffix: 5/2 = segment length (सौ मीटर में); T = twisted pair।"),
  {}),
 (SRC,
  "In the Ethernet names 10Base2 and 10Base5, the digits '2' and '5' indicate:",
  "Ethernet नामों 10Base2 और 10Base5 में अंक '2' और '5' बताते हैं:",
  [("Maximum segment length in hundreds of metres (~200 m and ~500 m)",
    "अधिकतम segment लंबाई, सौ मीटर में (~200 m और ~500 m)"),
   ("Number of hosts per segment", "प्रति segment hosts की संख्या"),
   ("Cable thickness in mm", "Cable की मोटाई mm में"),
   ("Transmission speed in Mbps", "Transmission गति Mbps में")],
  0,
  ("10Base2 = ~185-200 m (thin coax), 10Base5 = 500 m (thick coax) — '10' = "
   "10 Mbps, 'Base' = baseband.",
   "10Base2 = ~185-200 m; 10Base5 = 500 m; '10' = 10 Mbps; 'Base' = baseband।"),
  ("Speed '10' mein hai; digits 2/5 distance mein (sau metre).",
   "Speed '10' में; अंक 2/5 दूरी में (सौ मीटर)।"),
  {}),
 (SRC,
  "The function of a DSLAM (DSL Access Multiplexer) located at the telephone exchange is to:",
  "Telephone exchange पर स्थित DSLAM (DSL Access Multiplexer) का काम है:",
  [("Aggregate many DSL subscriber lines onto a high-speed backbone link",
    "कई DSL subscriber lines को high-speed backbone link पर इकट्ठा करना"),
   ("Convert digital voice to analog", "Digital voice को analog में बदलना"),
   ("Assign IP addresses to DSL modems", "DSL modems को IP addresses देना"),
   ("Encrypt DSL traffic", "DSL traffic encrypt करना")],
  0,
  ("DSLAM: exchange par sab DSL lines multiplex karke backbone par daalta hai "
   "(aur aksar ISP routing tak). Ghar par DSL modem hota hai.",
   "DSLAM: exchange पर सभी DSL lines को backbone पर multiplex करता है; घर पर DSL modem होता है।"),
  ("DHCP = IP dena; modem = signal convert; DSLAM = aggregation.",
   "DHCP = IP; modem = signal convert; DSLAM = aggregation।"),
  {}),
 (SRC,
  "Cable Internet access (HFC) differs from DSL in that:",
  "Cable Internet access (HFC), DSL से भिन्न है क्योंकि:",
  [("The HFC bandwidth is shared among all subscribers on the neighbourhood segment",
    "HFC bandwidth पड़ोस के segment के सभी subscribers में साझा होती है"),
   ("It uses the telephone line's DSLAM", "यह telephone line का DSLAM प्रयोग करता है"),
   ("It cannot carry television signals simultaneously", "यह television signals साथ नहीं चला सकता"),
   ("Each subscriber gets a dedicated fibre pair", "हर subscriber को dedicated fibre जोड़ी मिलती है")],
  0,
  ("HFC (Hybrid Fibre-Coax): fibre tak, phir coax — segment ka bandwidth shared "
   "(peak hours par slow). DSL mein har line exchange tak dedicated hoti hai.",
   "HFC: bandwidth साझा (peak hours पर धीमा); DSL में हर line exchange तक dedicated।"),
  ("DSL = dedicated last-mile; Cable = shared coax segment.",
   "DSL = dedicated last-mile; Cable = shared coax segment।"),
  {}),
 (SRC,
  "In SONET (Synchronous Optical Networking), the base electrical signal level STS-1 has a data rate of approximately:",
  "SONET में, आधार electrical signal level STS-1 की data rate लगभग होती है:",
  [("51.84 Mbps", "51.84 Mbps"), ("155.52 Mbps", "155.52 Mbps"),
   ("622.08 Mbps", "622.08 Mbps"), ("43.2 Mbps", "43.2 Mbps")],
  0,
  ("STS-1 = 51.84 Mbps; STS-3 = 155.52 (OC-3); STS-12 = 622.08 (OC-12) — "
   "har level n × STS-1.",
   "STS-1 = 51.84 Mbps; STS-3 = 155.52; STS-12 = 622.08 — हर level n × STS-1।"),
  ("Yaad karo: STS-1 = 51.84 Mbps, aur OC-n/STS-n = n × 51.84.",
   "STS-1 = 51.84 Mbps; OC-n/STS-n = n × 51.84।"),
  {}),
 (SRC,
  "In the SONET protocol stack, the photonic layer corresponds to which layer of the OSI model?",
  "SONET protocol stack में, photonic layer OSI model की किस layer के बराबर है?",
  [("Physical layer", "Physical layer"), ("Data link layer", "Data link layer"),
   ("Network layer", "Network layer"), ("Session layer", "Session layer")],
  0,
  ("SONET ke 4 layers: Photonic (physical/electrical-optical), Section, Line, "
   "Path — Photonic layer light signals/green-red lasers ka kaam sambhalti hai.",
   "SONET की 4 layers: Photonic, Section, Line, Path — Photonic = physical।"),
  ("Section/Line/Path = overhead management levels; Photonic = actual light.",
   "Section/Line/Path = overhead; Photonic = प्रकाश संकेत।"),
  {}),
]

P5_C_X3 = [
 (SRC,
  "Terrestrial radio channels are broadly classified into ______ groups:",
  "Terrestrial radio channels मोटे तौर पर ______ समूहों में विभाजित हैं:",
  [("Three", "तीन"), ("Two", "दो"), ("Five", "पाँच"), ("Seven", "सात")],
  0,
  ("Forouzan: terrestrial radio = 3 groups — (1) VLF/LF/MF (ground waves), "
   "(2) HF (sky waves/ionosphere reflection), (3) VHF/UHF/SHF/EHF (line-of-sight).",
   "Forouzan: terrestrial radio = 3 समूह — ground wave, sky wave, line-of-sight।"),
  ("Satellite/microwave alag category hain; terrestrial = teen.",
   "Satellite/microwave अलग; terrestrial = तीन।"),
  {}),
]

# ------------------------------- TOPIC 6 -------------------------------
P6_A_X3 = [
 (SRC,
  "Network congestion occurs when:",
  "Network congestion तब होता है जब:",
  [("The offered traffic exceeds the network's capacity", "Offered traffic network की क्षमता से अधिक हो"),
   ("Two hosts use the same port", "दो hosts एक ही port प्रयोग करें"),
   ("A frame is corrupted by noise", "Noise से frame खराब हो"),
   ("The DNS server is down", "DNS server बंद हो")],
  0,
  ("Congestion = queues bhar jaate hain kyunki demand capacity se zyada hai — "
   "delay/loss badhte hain. Isi ko sambhalne ke liye congestion control hota hai.",
   "Congestion = demand क्षमता से अधिक; queues भरती हैं, delay/loss बढ़ता है।"),
  ("Flow control = receiver ki speed; congestion = network ki capacity.",
   "Flow control = receiver; congestion = network की क्षमता।"),
  {}),
]

P6_C_X3 = [
 (SRC,
  "If the Protocol field of an IPv4 header is 17, the transport-layer protocol carried in the datagram is:",
  "यदि IPv4 header का Protocol field 17 हो, तो datagram में लिया गया transport-layer protocol है:",
  [("UDP", "UDP"), ("TCP", "TCP"), ("ICMP", "ICMP"), ("IGMP", "IGMP")],
  0,
  ("Protocol numbers: 1 = ICMP, 2 = IGMP, 6 = TCP, 17 = UDP, 89 = OSPF. "
   "Ye field fragmentation ke saath-saath next-header ki pehchaan deta hai.",
   "Protocol numbers: 1=ICMP, 2=IGMP, 6=TCP, 17=UDP, 89=OSPF।"),
  ("6 TCP, 17 UDP — dono sabse zyada puche jaate hain.",
   "6 TCP, 17 UDP — सबसे अधिक पूछे जाते हैं।"),
  {}),
 (SRC,
  "In IPv4 fragmentation, the LAST fragment has the More Fragments (MF) flag set to:",
  "IPv4 fragmentation में, अंतिम fragment का More Fragments (MF) flag होता है:",
  [("0", "0"), ("1", "1"), ("Its fragment offset value", "उसका fragment offset मान"),
   ("The same as the first fragment", "पहले fragment के बराबर")],
  0,
  ("MF = 1 matlab 'aur fragments aane hain'; aakhri fragment par MF = 0. "
   "Har fragment ka offset alag hota hai.",
   "MF=1 = 'और fragments आने हैं'; अंतिम पर MF=0।"),
  ("Dono fields (MF flag + offset) milkar reassembly karte hain.",
   "MF flag + offset मिलकर reassembly करते हैं।"),
  {}),
 (SRC,
  "The Fragment Offset field in the IPv4 header is used to:",
  "IPv4 header का Fragment Offset field प्रयोग होता है:",
  [("Place the fragment at its correct position in the original datagram during reassembly",
    "Reassembly के दौरान fragment को मूल datagram में सही स्थान पर रखने के लिए"),
   ("Count the total number of fragments", "कुल fragments गिनने के लिए"),
   ("Encrypt fragment payloads", "Fragment payloads encrypt करने के लिए"),
   ("Set the fragment's lifetime", "Fragment का जीवन-काल तय करने के लिए")],
  0,
  ("Offset (8-byte units mein) batata hai fragment original datagram mein kahan "
   "baitha hai — destination sirf offset se hi sahi order bana sakta hai.",
   "Offset (8-byte units में) बताता है fragment का स्थान — इसी से सही क्रम बनता है।"),
  ("Offset = position; MF = aur aane hain ya nahi.",
   "Offset = स्थान; MF = और आने हैं या नहीं।"),
  {}),
 (SRC,
  "The data field of an IPv4 datagram can carry:",
  "IPv4 datagram का data field ले जा सकता है:",
  [("TCP segment, UDP datagram, or ICMP message — all of these",
    "TCP segment, UDP datagram, या ICMP message — ये सब"),
   ("Only TCP segments", "सिर्फ TCP segments"),
   ("Only UDP datagrams", "सिर्फ UDP datagrams"),
   ("Only application data", "सिर्फ application data")],
  0,
  ("IP ka payload kuch bhi ho sakta hai jo Protocol field bataye — TCP/UDP "
   "segments, ICMP/IGMP messages, tunnels mein doosra IP packet bhi.",
   "IP का payload कुछ भी हो सकता है — TCP/UDP, ICMP/IGMP, या tunnel में दूसरा IP packet।"),
  ("Protocol field = 6/17/1/2/41... isi se pata chalta hai kya andar hai.",
   "Protocol field से पता चलता है क्या अंदर है।"),
  {}),
 (SRC,
  "RSVP (Resource ReSerVation Protocol) is used by hosts to:",
  "RSVP (Resource ReSerVation Protocol) का उपयोग hosts करते हैं:",
  [("Request reservation of network resources (bandwidth) along a path for QoS flows",
    "QoS flows के लिए रास्ते में network संसाधन (bandwidth) आरक्षित करने के अनुरोध हेतु"),
   ("Assign IP addresses automatically", "स्वतः IP addresses देने के लिए"),
   ("Resolve domain names", "Domain names हल करने के लिए"),
   ("Exchange routing tables between routers", "Routers के बीच routing tables बाँटने के लिए")],
  0,
  ("RSVP = signalling protocol jo routers se kehta hai ki flow ke liye "
   "resources reserve karo (IntServ/QoS). IP assignment = DHCP; routing = OSPF/BGP; "
   "names = DNS.",
   "RSVP = routers से संसाधन आरक्षित करने का संकेत (QoS)। IP=DHCP; routing=OSPF/BGP; names=DNS।"),
  ("RSVP 'reservation' ka protocol hai — circuit-switching jaisi guarantee nahi, "
   "bas soft-state reservations.",
   "RSVP = soft-state reservations; पूरी guarantee नहीं।"),
  {}),
]

P6_E_X3 = [
 (SRC,
  "The first line of an HTTP request message is called the:",
  "HTTP request message की पहली पंक्ति कहलाती है:",
  [("Request line", "Request line"), ("Header line", "Header line"),
   ("Status line", "Status line"), ("Body line", "Body line")],
  0,
  ("Request line = METHOD URI HTTP/VERSION (jaise 'GET /index.html HTTP/1.1'). "
   "Response message ki pehli line STATUS line hoti hai.",
   "Request line = METHOD URI HTTP/VERSION। Response की पहली line = status line।"),
  ("Status line sirf RESPONSE mein hoti hai.",
   "Status line सिर्फ RESPONSE में होती है।"),
  {}),
 (SRC,
  "By default, HTTP/1.1 connections are:",
  "डिफ़ॉल्ट रूप से, HTTP/1.1 connections होते हैं:",
  [("Persistent (keep-alive)", "Persistent (keep-alive)"), ("Non-persistent", "Non-persistent"),
   ("Simplex", "Simplex"), ("Datagram-based", "Datagram-based")],
  0,
  ("HTTP/1.1 default persistent connection: ek TCP connection par kai "
   "request/response (Connection: close se band hota hai). HTTP/1.0 default "
   "non-persistent tha.",
   "HTTP/1.1 default persistent: एक connection पर कई request/response; HTTP/1.0 non-persistent था।"),
  ("Persistent = connection reuse; non-persistent = har object par nayi connection.",
   "Persistent = connection reuse; non-persistent = हर object पर नई connection।"),
  {}),
 (SRC,
  "In HTTP, a conditional GET (using If-Modified-Since) allows:",
  "HTTP में conditional GET (If-Modified-Since के साथ) संभव बनाता है:",
  [("Cache validation — the server sends a 304 Not Modified instead of the object if unchanged",
    "Cache validation — अपरिवर्तित होने पर server वस्तु के बजाय 304 Not Modified भेजे"),
   ("Automatic language translation", "स्वतः भाषा अनुवाद"),
   ("Password-free login", "बिना password login"),
   ("Parallel downloads", "समांतर downloads")],
  0,
  ("Conditional GET: browser poochta hai 'kitne din se badla?'; agar object "
   "same hai to sirf 304 header — bandwidth bachti hai.",
   "Conditional GET: object अपरिवर्तित हो तो सिर्फ 304 Not Modified — bandwidth बचती है।"),
  ("304 = Not Modified; 200 = OK (poora content).",
   "304 = Not Modified; 200 = OK।"),
  {}),
 (SRC,
  "Which of the following is NOT a valid HTTP status code?",
  "निम्न में से कौन-सा वैध HTTP status code नहीं है?",
  [("250", "250"), ("200", "200"), ("404", "404"), ("503", "503")],
  0,
  ("200 = OK, 3xx redirection (301/302/304), 4xx client errors (400/403/404), "
   "5xx server errors (500/503). '250' SMTP ka 'mail action ok' code hai, HTTP ka nahi.",
   "200=OK; 3xx=redirection; 4xx=client error; 5xx=server error। 250 SMTP का code है।"),
  ("HTTP 2xx family: 200, 201, 204... 250 nahi.",
   "HTTP 2xx: 200, 201, 204... 250 नहीं।"),
  {}),
]

# ------------------------------- TOPIC 7 -------------------------------
P7_A_X3 = [
 (SRC,
  "A honeypot in network security is:",
  "Network security में honeypot होता है:",
  [("A decoy system set up to attract attackers and study their activity",
    "एक प्रलोभन (decoy) system जो attackers को आकर्षित कर उनकी गतिविधि अध्ययन करता है"),
   ("A firewall rule that blocks all traffic", "सभी traffic रोकने वाला firewall rule"),
   ("A backup server", "एक backup server"),
   ("An antivirus quarantine folder", "Antivirus quarantine folder")],
  0,
  ("Honeypot = jaal jaisa fake system/data — attackers usme fass kar apne "
   "tools/tarike dikha dete hain; defenders ko intelligence milti hai.",
   "Honeypot = जाल जैसा decoy system — attackers अपने तरीके दिखा देते हैं।"),
  ("Firewall rokta hai; honeypot fasata hai aur seekhata hai.",
   "Firewall रोकता है; honeypot फँसाता और सिखाता है।"),
  {}),
 (SRC,
  "A shadow honeypot combines a honeypot with:",
  "Shadow honeypot जोड़ता है honeypot के साथ:",
  [("An anomaly detection system (suspect traffic is run inside the honeypot)",
    "Anomaly detection system (संदिग्ध traffic को honeypot के अंदर चलाया जाता है)"),
   ("A physical lock", "एक भौतिक lock"),
   ("A DNS sinkhole only", "सिर्फ DNS sinkhole"),
   ("A load balancer", "एक load balancer")],
  0,
  ("Shadow honeypot: IDS/IPS ka anomaly detector jo kuch block kare, uske "
   "shadow copy ko honeypot par chala kar dekhte hain ki attack tha ya false "
   "positive — learning + safety dono.",
   "Shadow honeypot: anomaly detector की shadow copy को honeypot पर चलाकर जाँच — attack या false positive।"),
  ("Simple honeypot = decoy; shadow = decoy + anomaly detector ka validation.",
   "Simple honeypot = decoy; shadow = decoy + anomaly detector।"),
  {}),
]
