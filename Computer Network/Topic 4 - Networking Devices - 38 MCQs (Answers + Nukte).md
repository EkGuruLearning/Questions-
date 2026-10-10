# Data Communication & Computer Networks (CN)
## Topic 4 of 7 : Networking Devices — 38 MCQs (English + Hindi)

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** RPSC Programmer • ACP • RSMSSB IA • SA • DD • BCI • SCI • REET • RAS • DSSSB • KVS • NVS • HTET • SSC CGL/CHSL • RRB • IBPS • UPSC & all Rajasthan + Central Govt. Exams (Computer Awareness)

**Total Questions:** 38 | **Type:** MCQ (4 options) | **Bilingual:** English + Hindi (technical terms in English) | Each: ✔ why the correct answer is right + ★ Nukta. Wrong options verified internally. Answers cross-verified 4×.

### Syllabus Coverage (sub-topic wise order)

| # | Sub-topic | Questions |
|---|-----------|-----------|
| 1 | Section A — Physical-Layer Devices (Hub, Repeater, Modem & Simple Devices) | Q1 - Q9 |
| 2 | Section B — Switch / NIC / Bridge | Q10 - Q19 |
| 3 | Section C — Router / Brouter | Q20 - Q27 |
| 4 | Section D — Gateway, Firewall & NAT Devices | Q28 - Q38 |

---

## Section A — Physical-Layer Devices (Hub, Repeater, Modem & Simple Devices)

*Layer-1 dumb devices — hub, repeater, modem, multiplexer, file server; collision-domain basics.*

### Q1. Which device operates only at the Physical layer (Layer 1) of the OSI model?

<span lang='hi'>OSI model की केवल Physical layer (Layer 1) पर कौन-सा device काम करता है?</span>

- **(A)** Switch
- **(B)** Hub ✅ **(CORRECT)**
- **(C)** Router
- **(D)** Bridge

**✔ Correct Answer: (B) Hub** — A hub is a dumb Layer-1 device — it regenerates and forwards bits to ALL ports without reading MAC addresses.

*Hub एक dumb Layer-1 device है — यह bits को regenerate करके सभी ports पर भेजता है, बिना MAC addresses पढ़े।*

**★ Nukta (Key Point):** Layer 1 = Hub, Repeater, Modem, cables. Layer 2 = Switch, Bridge, NIC. Layer 3 = Router. Gateway = all 7 (protocol converter).

*Layer 1 = Hub, Repeater, Modem, cables। Layer 2 = Switch, Bridge, NIC। Layer 3 = Router। Gateway = सभी 7 (protocol converter)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch) · also CN Topic Test-6] · Easy*

---
### Q2. Which of the following pairs lists the network devices used at the physical layer?

<span lang='hi'>निम्न में से कौन-सी जोड़ी physical layer पर उपयोग होने वाले network devices बताती है?</span>

- **(A)** Gateway, Bridge
- **(B)** Router, Repeater
- **(C)** Hub, Switch
- **(D)** Repeater, Hub ✅ **(CORRECT)**

**✔ Correct Answer: (D) Repeater, Hub** — Repeater and Hub both work at the physical layer — they regenerate/forward signals without frame intelligence.

*Repeater और Hub दोनों physical layer पर काम करते हैं — ये signals को regenerate/forward करते हैं, बिना frame intelligence के।*

**★ Nukta (Key Point):** Rajasthan PYQ (verified key: D). Physical-layer pair = Repeater + Hub. Switch/Bridge = L2, Gateway = L7.

*Rajasthan PYQ (verified key: D)। Physical-layer जोड़ी = Repeater + Hub। Switch/Bridge = L2, Gateway = L7।*

*[Source: Random Test- Rajasthan PYQ (OCR), p12 — Q93 (options reconstructed from screenshot)] · Medium*

---
### Q3. Which of the following are network connecting devices? 1. Repeater  2. Bridge  3. Hub  4. Bluetooth

<span lang='hi'>निम्न में से कौन network connecting devices हैं? 1. Repeater  2. Bridge  3. Hub  4. Bluetooth</span>

- **(A)** 1, 2 and 3 ✅ **(CORRECT)**
- **(B)** 1, 2 and 4
- **(C)** 2, 3 and 4
- **(D)** 1, 3 and 4

**✔ Correct Answer: (A) 1, 2 and 3** — Repeater, Bridge and Hub are all network connecting DEVICES; Bluetooth is a wireless TECHNOLOGY/standard, not a connecting device.

*Repeater, Bridge और Hub — तीनों network connecting DEVICES हैं; Bluetooth एक wireless TECHNOLOGY/standard है, connecting device नहीं।*

**★ Nukta (Key Point):** Devices vs technologies: repeater/bridge/hub/switch/router = devices. Bluetooth/Wi-Fi/Ethernet = technologies/standards.

*Devices बनाम technologies: repeater/bridge/hub/switch/router = devices। Bluetooth/Wi-Fi/Ethernet = technologies/standards।*

*[Source: Unit Test -2 Solutions (OCR), p11] · Medium*

---
### Q4. Which of the following statements are TRUE? 1. Switch reduces collision domain. 2. Hub creates a separate collision domain for each port. 3. Router separates broadcast domains.

<span lang='hi'>निम्न में से कौन-से कथन सही हैं? 1. Switch collision domain को कम करता है। 2. Hub हर port के लिए अलग collision domain बनाता है। 3. Router broadcast domains को अलग करता है।</span>

- **(A)** 1 and 2 only
- **(B)** 2 and 3 only
- **(C)** 1 and 3 only ✅ **(CORRECT)**
- **(D)** 1, 2 and 3

**✔ Correct Answer: (C) 1 and 3 only** — Statement 1 is true (each switch port = own collision domain) and 3 is true (router = broadcast-domain boundary). Statement 2 is FALSE — a hub has ONE collision domain for all its ports.

*कथन 1 सही है (हर switch port = अपना collision domain) और 3 सही है (router = broadcast-domain सीमा)। कथन 2 गलत है — hub के सभी ports के लिए एक ही collision domain होता है।*

**★ Nukta (Key Point):** Switch: collision ↓ (per-port). Hub: 1 collision domain. Router: broadcast domains separated. Ye teeno golden statements hain.

*Switch: collision ↓ (per-port)। Hub: 1 collision domain। Router: broadcast domains अलग। ये तीनों golden statements हैं।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q26] · Medium*

---
### Q5. Which device combines transmission from various I/O devices into one line?

<span lang='hi'>कौन-सा device विभिन्न I/O devices के transmission को एक line में मिलाता है?</span>

- **(A)** Modifier
- **(B)** Multiplexer ✅ **(CORRECT)**
- **(C)** Concentrator
- **(D)** Gateway

**✔ Correct Answer: (B) Multiplexer** — A multiplexer (MUX) combines several input signals into ONE shared line (FDM/TDM) at the sending end; a demultiplexer separates them again.

*Multiplexer (MUX) भेजने वाली ओर कई input signals को एक shared line में मिलाता है (FDM/TDM); demultiplexer उन्हें फिर अलग करता है।*

**★ Nukta (Key Point):** MUX = many→one line (FDM/TDM/WDM). Concentrator = statistical sharing of a line. Gateway = protocol converter.

*MUX = कई→एक line (FDM/TDM/WDM)। Concentrator = line का statistical sharing। Gateway = protocol converter।*

*[Source: Unit Test-4 Solution (OCR), p22] · Medium*

---
### Q6. A file server is a ______ which is used to store files received from various client machines.

<span lang='hi'>File server एक ______ है जिसका उपयोग विभिन्न client machines से प्राप्त files संग्रहित करने के लिए होता है।</span>

- **(A)** Specialized computer system ✅ **(CORRECT)**
- **(B)** Modem
- **(C)** Router
- **(D)** Transponder

**✔ Correct Answer: (A) Specialized computer system** — A file server is a specialised computer (with large storage) that stores and serves files to clients in a client-server network.

*File server एक विशेष computer (बड़े storage के साथ) है जो client-server network में clients को files संग्रहित करके देता है।*

**★ Nukta (Key Point):** Servers (file/print/mail/web) = specialised computers. Modem = signal converter, Router = packet forwarder, Transponder = satellite relay.

*Servers (file/print/mail/web) = विशेष computers। Modem = signal converter, Router = packet forwarder, Transponder = satellite relay।*

*[Source: Unit Test-4 Solution (OCR), p24] · Medium*

---
### Q7. In a data-entry office, computer centres on the 1st and 4th floors are connected by LANs, but signals take time to travel. Which hardware can improve the data transmission?

<span lang='hi'>एक data-entry office में 1वीं और 4वीं मंज़िल के computer centres LAN से जुड़े हैं, पर signals में समय लगता है. बेहतर transmission के लिए कौन-सा hardware लगाएँ?</span>

- **(A)** Repeater ✅ **(CORRECT)**
- **(B)** Router
- **(C)** Computer
- **(D)** Modem

**✔ Correct Answer: (A) Repeater** — Repeater कमज़ोर होते signal को दोबारा ताक़तवर बनाता (regenerate करता) है — इसलिए दूरी की समस्या में यही लगता है.

*Repeater कमज़ोर होते signal को दोबारा ताक़तवर बनाता (regenerate करता) है — इसलिए दूरी की समस्या में यही लगता है.*

**★ Nukta (Key Point):** संकेत कमज़ोर → Repeater; रास्ता चाहिए → Router; analog↔digital → Modem.

*संकेत कमज़ोर → Repeater; रास्ता चाहिए → Router; analog↔digital → Modem.*

*[Source: RSMSSB Informatics Assistant 2023 (via examsmantra solved paper)] · Medium*

---
### Q8. Which of the following devices operates only in the physical layer?

<span lang='hi'>निम्न में से कौन-सा device केवल physical layer पर काम करता है?</span>

- **(A)** Two-layer switch
- **(B)** Router
- **(C)** Repeater ✅ **(CORRECT)**
- **(D)** Bridge

**✔ Correct Answer: (C) Repeater** — A repeater works at Layer 1 — it only regenerates (amplifies + reshapes) the signal to extend the cable distance.

*Repeater Layer 1 पर काम करता है — यह केवल signal को regenerate (amplify + reshape) करके cable distance बढ़ाता है।*

**★ Nukta (Key Point):** Repeater = signal regenerator (L1). Hub = multi-port repeater (L1). Both are 'dumb' devices.

*Repeater = signal regenerator (L1)। Hub = multi-port repeater (L1)। दोनों 'dumb' devices हैं।*

*[Source: Kerala PSC repeated PYQs (via pscarivukal)] · Hard*

---
### Q9. A device that operates at the physical layer of the OSI model is:

<span lang='hi'>OSI model की physical layer पर काम करने वाला device है:</span>

- **(A)** Bridge
- **(B)** Router
- **(C)** Repeater ✅ **(CORRECT)**
- **(D)** All of these

**✔ Correct Answer: (C) Repeater** — Repeater physical layer (Layer 1) का device है — यह signal regenerate करता है. Bridge Layer 2, Router Layer 3 पर.

*Repeater physical layer (Layer 1) का device है — यह signal regenerate करता है. Bridge Layer 2, Router Layer 3 पर.*

**★ Nukta (Key Point):** Layer-device जोड़ी: L1 = Repeater/Hub, L2 = Bridge/Switch, L3 = Router, L4+ = Gateway.

*Layer-device जोड़ी: L1 = Repeater/Hub, L2 = Bridge/Switch, L3 = Router, L4+ = Gateway.*

*[Source: SBI/IBPS Computer Awareness Capsule 2018 (IBT India)] · Hard*

---

## Section B — Switch / NIC / Bridge

*CAM table, per-port collision domains, flooding behaviour, VLANs & broadcast domains, wireless AP as bridge.*

### Q10. Which device stores MAC addresses in a CAM table?

<span lang='hi'>कौन-सा device MAC addresses को CAM table में संग्रहित करता है?</span>

- **(A)** Hub
- **(B)** Router
- **(C)** Switch ✅ **(CORRECT)**
- **(D)** Modem

**✔ Correct Answer: (C) Switch** — A switch learns source MAC addresses and stores them in its CAM (Content Addressable Memory) table to forward frames only to the right port.

*Switch source MAC addresses सीखकर उन्हें अपने CAM (Content Addressable Memory) table में रखता है ताकि frames सही port पर ही भेजे जाएँ।*

**★ Nukta (Key Point):** Switch = MAC table (CAM). Router = routing table (IP). Hub = no table (floods). ARP cache = IP→MAC mapping (host).

*Switch = MAC table (CAM)। Router = routing table (IP)। Hub = कोई table नहीं (floods)। ARP cache = IP→MAC mapping (host)।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q11. A router is connected between two switches. If a broadcast frame is sent on Switch-A, what will Switch-B receive?

<span lang='hi'>दो switches के बीच एक router जुड़ा है। यदि Switch-A पर broadcast frame भेजा जाए, तो Switch-B क्या प्राप्त करेगा?</span>

- **(A)** The broadcast
- **(B)** A unicast copy
- **(C)** Nothing ✅ **(CORRECT)**
- **(D)** A multicast

**✔ Correct Answer: (C) Nothing** — Routers do not forward broadcast traffic — each side of the router is a separate broadcast domain, so Switch-B receives nothing.

*Router broadcast traffic को आगे नहीं भेजते — router के दोनों ओर अलग broadcast domains होते हैं, इसलिए Switch-B कुछ भी प्राप्त नहीं करेगा।*

**★ Nukta (Key Point):** Router = broadcast firewall. This is why routers split broadcast domains and switches don't.

*Router = broadcast firewall। इसीलिए router broadcast domains तोड़ते हैं और switches नहीं।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q12. What does a MAC address represent?

<span lang='hi'>MAC address किसका प्रतिनिधित्व करता है?</span>

- **(A)** The location of the device in the network
- **(B)** The unique identity of the NIC ✅ **(CORRECT)**
- **(C)** Internet connectivity
- **(D)** The routing path

**✔ Correct Answer: (B) The unique identity of the NIC** — The MAC address is the unique hardware identity of the NIC (Network Interface Card) — burned in by the manufacturer.

*MAC address, NIC (Network Interface Card) की unique hardware पहचान है — manufacturer द्वारा burn की गई।*

**★ Nukta (Key Point):** MAC = NIC identity (who). IP = location in network (where). Routing path = router's job.

*MAC = NIC identity (कौन)। IP = network में स्थान (कहाँ)। Routing path = router का काम।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q13. Which device reduces collision domains (each port has its own collision domain) but does NOT break broadcast domains?

<span lang='hi'>कौन-सा device collision domains को कम करता है (हर port का अपना collision domain) लेकिन broadcast domains को तोड़ता नहीं?</span>

- **(A)** Switch ✅ **(CORRECT)**
- **(B)** Router
- **(C)** Hub
- **(D)** Gateway

**✔ Correct Answer: (A) Switch** — A switch gives every port a separate collision domain (full-duplex = no collisions) but ALL its ports share ONE broadcast domain (unless VLANs are used).

*Switch हर port को अलग collision domain देता है (full-duplex = कोई collision नहीं) लेकिन सभी ports एक ही broadcast domain share करते हैं (जब तक VLAN न हो)।*

**★ Nukta (Key Point):** Switch = collision domains many, broadcast 1. Router = broadcast domains many. Hub = 1 collision + 1 broadcast. VLAN = splits broadcast on a switch.

*Switch = collision domains कई, broadcast 1। Router = broadcast domains कई। Hub = 1 collision + 1 broadcast। VLAN = switch पर broadcast तोड़ता है।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) · also CN Topic Test-6] · Medium*

---
### Q14. A switch receives a frame whose destination MAC is NOT in its MAC table. What does the switch do?

<span lang='hi'>एक switch को frame मिलता है जिसका destination MAC उसके MAC table में नहीं है। Switch क्या करेगा?</span>

- **(A)** Send the frame to the router only
- **(B)** Flood the frame out of all its ports (same broadcast domain) ✅ **(CORRECT)**
- **(C)** Drop the frame
- **(D)** Broadcast it on the entire internet

**✔ Correct Answer: (B) Flood the frame out of all its ports (same broadcast domain)** — On an unknown unicast destination, the switch floods the frame out of every port (except the source port) within the broadcast domain — this is how it learns.

*अज्ञात unicast destination पर switch frame को हर port (source port को छोड़कर) से broadcast domain के भीतर flood करता है — इसी तरह वह सीखता है।*

**★ Nukta (Key Point):** Unknown unicast → flood. Known unicast → single port. Broadcast FF:FF:... → flood. Source MAC → learn/refresh in CAM.

*Unknown unicast → flood। Known unicast → एक port। Broadcast FF:FF:... → flood। Source MAC → CAM में learn/refresh।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

---
### Q15. A switch has 4 VLANs configured. How many broadcast domains exist?

<span lang='hi'>एक switch पर 4 VLANs configure हैं। कितने broadcast domains होंगे?</span>

- **(A)** 1
- **(B)** 2
- **(C)** 4 ✅ **(CORRECT)**
- **(D)** Depends on the router

**✔ Correct Answer: (C) 4** — Each VLAN is its own broadcast domain — 4 VLANs = 4 broadcast domains on that switch.

*हर VLAN अपना अलग broadcast domain है — उस switch पर 4 VLANs = 4 broadcast domains।*

**★ Nukta (Key Point):** VLAN = virtual switch = its own broadcast domain. Inter-VLAN communication needs a router (or L3 switch).

*VLAN = virtual switch = अपना broadcast domain। Inter-VLAN संचार के लिए router (या L3 switch) चाहिए।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

---
### Q16. In a router-on-a-stick setup with VLANs, which device handles VLAN tagging and which handles inter-VLAN routing?

<span lang='hi'>VLANs वाले router-on-a-stick setup में VLAN tagging कौन करता है और inter-VLAN routing कौन?</span>

- **(A)** Switch – VLAN tags, Router – routing ✅ **(CORRECT)**
- **(B)** Router – VLAN tags, Switch – routing
- **(C)** Both switch and router do VLAN tagging
- **(D)** Neither does VLAN tagging

**✔ Correct Answer: (A) Switch – VLAN tags, Router – routing** — The switch carries VLAN-tagged (802.1Q) frames on the trunk, and the router (sub-interfaces) routes between the VLANs.

*Switch trunk पर VLAN-tagged (802.1Q) frames ले जाता है, और router (sub-interfaces) VLANs के बीच routing करता है।*

**★ Nukta (Key Point):** 802.1Q tagging = switch trunk job. Inter-VLAN routing = router (router-on-a-stick) or L3 switch.

*802.1Q tagging = switch trunk का काम। Inter-VLAN routing = router (router-on-a-stick) या L3 switch।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

---
### Q17. A packet travels: wired PC → Switch → Access Point → Wireless laptop. Which devices operate at Layer 2 only?

<span lang='hi'>एक packet यात्रा करता है: wired PC → Switch → Access Point → Wireless laptop। कौन-से devices केवल Layer 2 पर काम करते हैं?</span>

- **(A)** Switch only
- **(B)** Access Point only
- **(C)** Both switch and access point ✅ **(CORRECT)**
- **(D)** Neither

**✔ Correct Answer: (C) Both switch and access point** — A switch is a Layer-2 device and an access point acts as a wireless bridge — also Layer-2 (it bridges 802.3 frames to 802.11 frames).

*Switch एक Layer-2 device है और access point एक wireless bridge की तरह काम करता है — वह भी Layer-2 (यह 802.3 frames को 802.11 frames में बदलता है)।*

**★ Nukta (Key Point):** AP = wireless bridge (L2). Switch = L2. Router = L3. WAPs don't route unless configured as routers.

*AP = wireless bridge (L2)। Switch = L2। Router = L3। WAPs routing नहीं करते (जब तक router mode में न हों)।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

---
### Q18. Which of the following component is responsible for network communication in a computer system?

<span lang='hi'>कंप्यूटर सिस्टम में network communication के लिए कौन-सा component ज़िम्मेदार होता है?</span>

- **(A)** UPS
- **(B)** Ethernet card (NIC) ✅ **(CORRECT)**
- **(C)** SVGA card
- **(D)** SMPS

**✔ Correct Answer: (B) Ethernet card (NIC)** — Ethernet card यानी NIC (Network Interface Card) ही computer को network से जोड़ता है और frames भेजने-पाने का काम करता है.

*Ethernet card यानी NIC (Network Interface Card) ही computer को network से जोड़ता है और frames भेजने-पाने का काम करता है.*

**★ Nukta (Key Point):** NIC = computer का network वाला हाथ — इसी पर MAC address बसा होता है.

*NIC = computer का network वाला हाथ — इसी पर MAC address बसा होता है.*

*[Source: Unit Test-4 Solution.pdf (OCR), p18] · Medium*

---
### Q19. LANs can be connected by which of the following devices that operate on the data link layer?

<span lang='hi'>LANs को data link layer पर काम करने वाले निम्न में से किस device से जोड़ा जा सकता है?</span>

- **(A)** Hub
- **(B)** Bridges ✅ **(CORRECT)**
- **(C)** HDLC
- **(D)** Tunnel

**✔ Correct Answer: (B) Bridges** — Bridges LANs को data link layer (Layer 2) पर जोड़ते हैं और MAC addresses देखकर frames आगे भेजते हैं.

*Bridges LANs को data link layer (Layer 2) पर जोड़ते हैं और MAC addresses देखकर frames आगे भेजते हैं.*

**★ Nukta (Key Point):** Hub = L1, Bridge/Switch = L2, Router = L3, Gateway = L4+.

*Hub = L1, Bridge/Switch = L2, Router = L3, Gateway = L4+.*

*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Medium*

---

## Section C — Router / Brouter

*Router functions & layers, per-hop packet changes, broadcast-domain boundaries, congestion (RED), routing basics.*

### Q20. A router performs which of the following? (1) Packet forwarding  (2) Logical addressing  (3) Collision detection  (4) Routing decision

<span lang='hi'>Router निम्न में से कौन-सा कार्य करता है? (1) Packet forwarding  (2) Logical addressing  (3) Collision detection  (4) Routing decision</span>

- **(A)** 1, 2 and 4 ✅ **(CORRECT)**
- **(B)** 2, 3 and 4
- **(C)** 1 and 3 only
- **(D)** 1, 2, 3 and 4

**✔ Correct Answer: (A) 1, 2 and 4** — A router forwards packets, uses logical (IP) addressing and makes routing decisions — but collision detection is a Layer-2 (CSMA/CD) function, not a router's.

*Router packets भेजता है, logical (IP) addressing उपयोग करता है और routing decisions लेता है — लेकिन collision detection Layer-2 (CSMA/CD) का काम है, router का नहीं।*

**★ Nukta (Key Point):** Router = forward + route + logical addressing. NOT collision detection (that's Ethernet L2 on switches/NICs).

*Router = forward + route + logical addressing। Collision detection नहीं (वह switches/NICs पर Ethernet L2 का काम है)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch) — Q28] · Easy*

---
### Q21. A router drops some packets deliberately due to congestion. What is this technique called?

<span lang='hi'>Router congestion के कारण कुछ packets जानबूझकर छोड़ देता है। इस तकनीक को क्या कहते हैं?</span>

- **(A)** Delay policing
- **(B)** Redundancy
- **(C)** Random Early Detection (RED) ✅ **(CORRECT)**
- **(D)** Reverse flooding

**✔ Correct Answer: (C) Random Early Detection (RED)** — Random Early Detection (RED) proactively drops (or marks) packets before the queue is full, signalling senders to slow down — a congestion-avoidance technique.

*Random Early Detection (RED) queue भरने से पहले ही packets छोड़ (या mark) देता है, जिससे senders धीमे हो जाएँ — यह एक congestion-avoidance तकनीक है।*

**★ Nukta (Key Point):** Congestion tools: RED (early random drops), Queuing (FIFO/PQ), Traffic shaping. Dropping ALL at overflow = tail drop.

*Congestion tools: RED (early random drops), Queuing (FIFO/PQ), Traffic shaping। Overflow पर सब छोड़ना = tail drop।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q22. Which device creates a separate broadcast domain?

<span lang='hi'>कौन-सा device अलग broadcast domain बनाता है?</span>

- **(A)** Switch
- **(B)** Bridge
- **(C)** Router ✅ **(CORRECT)**
- **(D)** Repeater

**✔ Correct Answer: (C) Router** — Each router interface belongs to a different broadcast domain — the router is the boundary between them.

*हर router interface अलग broadcast domain से संबंधित होता है — router उनके बीच की सीमा है।*

**★ Nukta (Key Point):** Broadcast domain boundary = router (or VLAN). Collision domain boundary = switch port/bridge.

*Broadcast domain सीमा = router (या VLAN)। Collision domain सीमा = switch port/bridge।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q23. Which device operates at Layer 3 of the OSI model?

<span lang='hi'>OSI model की Layer 3 पर कौन-सा device काम करता है?</span>

- **(A)** Hub
- **(B)** Switch
- **(C)** Router ✅ **(CORRECT)**
- **(D)** Repeater

**✔ Correct Answer: (C) Router** — The router works at the Network layer (Layer 3) — it forwards packets using logical IP addresses and routing tables.

*Router Network layer (Layer 3) पर काम करता है — यह logical IP addresses और routing tables का उपयोग करके packets भेजता है।*

**★ Nukta (Key Point):** Device-layer ladder: Repeater/Hub 1, Switch/Bridge/NIC 2, Router 3, Gateway 7.

*Device-layer ladder: Repeater/Hub 1, Switch/Bridge/NIC 2, Router 3, Gateway 7।*

*[Source: SSC CGL Tier-2 repeated Qs (via Oliveboard)] · Medium*

---
### Q24. Consider: S1: The TTL field decreases at each router. S2: The MAC address changes at each hop. Which is correct?

<span lang='hi'>देखिए: S1: TTL field हर router पर घटती है। S2: MAC address हर hop पर बदलता है। कौन-सा सही है?</span>

- **(A)** Only S1
- **(B)** Only S2
- **(C)** Both S1 and S2 ✅ **(CORRECT)**
- **(D)** Neither S1 nor S2

**✔ Correct Answer: (C) Both S1 and S2** — At every router hop the TTL is decremented (and header checksum recomputed) AND a new frame with new source/destination MAC addresses is built. Both statements are true.

*हर router hop पर TTL घटती है (और header checksum फिर से बनता है) और नए source/destination MAC addresses वाला नया frame बनता है। दोनों कथन सही हैं।*

**★ Nukta (Key Point):** Per-hop changes: TTL↓ + MAC rewritten. End-to-end: IP addresses unchanged (except NAT).

*Per-hop बदलाव: TTL↓ + MAC फिर से लिखा जाता है। End-to-end: IP addresses अपरिवर्तित (NAP को छोड़कर)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

---
### Q25. Which hardware forwards data packets between computer networks?

<span lang='hi'>कौन-सा hardware computer networks के बीच data packets को आगे भेजता है?</span>

- **(A)** Switch
- **(B)** Router ✅ **(CORRECT)**
- **(C)** Cable
- **(D)** Nibble

**✔ Correct Answer: (B) Router** — A router forwards packets between DIFFERENT networks using the routing information (IP addresses) in the packet.

*Router packet के भीतर routing information (IP addresses) का उपयोग करके विभिन्न networks के बीच packets को आगे भेजता है।*

**★ Nukta (Key Point):** Official KVS key. Router = between networks (L3). Switch = within a network (L2). Cable = medium. Nibble = 4 bits!

*Official KVS key। Router = networks के बीच (L3)। Switch = network के भीतर (L2)। Cable = medium। Nibble = 4 bits!*

*[Source: KVS Librarian 2023 Official Paper (via Testbook) · also CN Topic Test-03] · Hard*

---
### Q26. Among these network devices — i. Repeater  ii. Hub  iii. Switch  iv. Router — which are considered intelligent devices?

<span lang='hi'>इन network devices में — i. Repeater  ii. Hub  iii. Switch  iv. Router — कौन-से intelligent devices माने जाते हैं?</span>

- **(A)** i and iv only
- **(B)** i and ii only
- **(C)** iii and iv only ✅ **(CORRECT)**
- **(D)** ii and iii only

**✔ Correct Answer: (C) iii and iv only** — Switch and router are intelligent — they read addresses (MAC/IP) and make forwarding decisions; repeater and hub blindly repeat/forward signals.

*Switch और router intelligent हैं — ये addresses (MAC/IP) पढ़कर forwarding decisions लेते हैं; repeater और hub अंधों की तरह signals दोहराते/भेजते हैं।*

**★ Nukta (Key Point):** Intelligent = reads addresses + filters/forwards selectively (switch, router, bridge, gateway). Dumb = hub, repeater.

*Intelligent = addresses पढ़ता है + selectively filter/forward करता है (switch, router, bridge, gateway)। Dumb = hub, repeater।*

*[Source: Kerala PSC repeated PYQs (via pscarivukal)] · Hard*

---
### Q27. Consider the statements about an IP router: I. A router does not modify the IP packets during forwarding. II. It is not necessary for a router to implement any routing protocol. III. A router should reassemble IP fragments if the MTU of the outgoing link is larger than the incoming fragment. Which is correct?

<span lang='hi'>IP router के बारे में कथन देखिए: I. Forwarding के दौरान router IP packets को नहीं बदलता। II. Router के लिए कोई routing protocol लागू करना आवश्यक नहीं है। III. यदि outgoing link का MTU आने वाले fragment से बड़ा हो तो router को IP fragments फिर से जोड़ने चाहिए। कौन-सा सही है?</span>

- **(A)** I and II only
- **(B)** I only
- **(C)** II and III only
- **(D)** II only ✅ **(CORRECT)**

**✔ Correct Answer: (D) II only** — Only II is true: a router can use static routes (no routing protocol). I is false — the router decrements TTL and updates the checksum. III is false — reassembly is done only by the destination, not routers.

*केवल II सही है: router static routes उपयोग कर सकता है (कोई routing protocol नहीं)। I गलत है — router TTL घटाता है और checksum अपडेट करता है। III गलत है — reassembly केवल destination करता है, routers नहीं।*

**★ Nukta (Key Point):** Advanced but classic: routers modify IP header (TTL/checksum), may run static-only, never reassemble fragments (destination does).

*उन्नत लेकिन classic: router IP header बदलता है (TTL/checksum), केवल static चला सकता है, fragments कभी नहीं जोड़ता (destination जोड़ता है)।*

*[Source: Unit Test-4 Solution (OCR), p15] · Hard*

---

## Section D — Gateway, Firewall & NAT Devices

*Gateway as protocol converter, firewall types (packet/stateful/proxy), NAT types, device-vs-software identification.*

### Q28. Which type of firewall inspects packets at the network layer and decides based on IP addresses?

<span lang='hi'>कौन-सी firewall network layer पर packets की जाँच करके IP addresses के आधार पर निर्णय लेती है?</span>

- **(A)** Packet Filtering Firewall ✅ **(CORRECT)**
- **(B)** Stateful Firewall
- **(C)** Proxy Firewall
- **(D)** Application Firewall

**✔ Correct Answer: (A) Packet Filtering Firewall** — A packet-filtering firewall works at the network layer — it allows/denies packets by source/destination IP (and ports) using ACL rules.

*Packet-filtering firewall network layer पर काम करती है — यह ACL rules से source/destination IP (और ports) के आधार पर packets को allow/deny करती है।*

**★ Nukta (Key Point):** Firewall types: Packet filtering (L3/L4, stateless) → Stateful (tracks sessions) → Proxy/Application gateway (L7) → Circuit-level gateway (L5).

*Firewall types: Packet filtering (L3/L4, stateless) → Stateful (sessions याद रखती है) → Proxy/Application gateway (L7) → Circuit-level gateway (L5)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q29. Which firewall acts as an intermediary between the client and server at the application layer?

<span lang='hi'>कौन-सी firewall application layer पर client और server के बीच मध्यस्थ (intermediary) के रूप में काम करती है?</span>

- **(A)** Packet Filtering Firewall
- **(B)** Stateful Firewall
- **(C)** Proxy Firewall ✅ **(CORRECT)**
- **(D)** Circuit-level Gateway

**✔ Correct Answer: (C) Proxy Firewall** — A proxy (application) firewall terminates the client connection and opens a separate connection to the server — hiding the internal client completely.

*Proxy (application) firewall client connection समाप्त करके server के लिए अलग connection खोलती है — internal client को पूरी तरह छिपाती है।*

**★ Nukta (Key Point):** Proxy = L7 intermediary (deep inspection, hides internals). Circuit gateway = L5 (session/relay).

*Proxy = L7 intermediary (गहरी जाँच, internals छिपाती है)। Circuit gateway = L5 (session/relay)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q30. If two systems use DIFFERENT protocols, which device is used to link them?

<span lang='hi'>यदि दो systems भिन्न protocols उपयोग करते हैं, तो उन्हें जोड़ने के लिए कौन-सा device उपयोग होता है?</span>

- **(A)** Repeater
- **(B)** Gateway ✅ **(CORRECT)**
- **(C)** Bridge
- **(D)** Hub

**✔ Correct Answer: (B) Gateway** — A gateway is a protocol converter — it translates between different protocols/architectures so dissimilar systems can communicate.

*Gateway एक protocol converter है — यह विभिन्न protocols/architectures के बीच अनुवाद करता है ताकि भिन्न systems संवाद कर सकें।*

**★ Nukta (Key Point):** Gateway = protocol converter (L7). Bridge = similar LANs, same protocols (L2). Repeater/Hub = signal level (L1).

*Gateway = protocol converter (L7)। Bridge = समान LANs, समान protocols (L2)। Repeater/Hub = signal level (L1)।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Medium*

---
### Q31. Which device can operate across all 7 layers of the OSI model?

<span lang='hi'>कौन-सा device OSI model की सभी 7 layers पर काम कर सकता है?</span>

- **(A)** Router
- **(B)** Hub
- **(C)** Gateway ✅ **(CORRECT)**
- **(D)** Switch

**✔ Correct Answer: (C) Gateway** — A gateway (protocol converter) works at the application layer and may involve all layers to translate between different protocol stacks.

*Gateway (protocol converter) application layer पर काम करता है और भिन्न protocol stacks के बीच अनुवाद के लिए सभी layers को शामिल कर सकता है।*

**★ Nukta (Key Point):** Gateway = 'all 7 layers' device. Hub 1, switch/bridge 2, router 3 — exam one-liner.

*Gateway = 'सभी 7 layers' वाला device। Hub 1, switch/bridge 2, router 3 — exam one-liner।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

---
### Q32. Devices on one network can communicate with devices on another network via:

<span lang='hi'>एक network के devices दूसरे network के devices से किसके माध्यम से संवाद कर सकते हैं?</span>

- **(A)** File server
- **(B)** Utility server
- **(C)** Printer server
- **(D)** Gateway ✅ **(CORRECT)**

**✔ Correct Answer: (D) Gateway** — A gateway connects different networks (often with different protocols) and lets their devices communicate — the entry/exit point between networks.

*Gateway विभिन्न networks (अक्सर भिन्न protocols वाले) को जोड़ता है और उनके devices को संवाद करने देता है — networks के बीच प्रवेश/निकास बिंदु।*

**★ Nukta (Key Point):** Gateway = network-to-network doorway (also default gateway = router IP used to exit the LAN).

*Gateway = network-to-network दरवाज़ा (default gateway भी = LAN से बाहर निकलने के लिए router IP)।*

*[Source: SSC CGL Internet & Networking (via EduRev bank)] · Medium*

---
### Q33. What is the role of a firewall in computer networks?

<span lang='hi'>Computer networks में firewall की भूमिका क्या है?</span>

- **(A)** Managing IP addresses
- **(B)** Filtering and controlling network traffic ✅ **(CORRECT)**
- **(C)** Resolving domain names
- **(D)** Assigning MAC addresses dynamically

**✔ Correct Answer: (B) Filtering and controlling network traffic** — A firewall monitors and filters incoming/outgoing traffic according to security rules — protecting the trusted network from unauthorised access.

*Firewall security rules के अनुसार आने-जाने वाले traffic की निगरानी और छँटनी करता है — trusted network को unauthorised access से बचाता है।*

**★ Nukta (Key Point):** Firewall = traffic filter between trusted & untrusted networks (screening router, DMZ...). DHCP = IP management; DNS = names.

*Firewall = trusted और untrusted networks के बीच traffic filter (screening router, DMZ...)। DHCP = IP management; DNS = names।*

*[Source: 30 important CN MCQs (Medium blog bank)] · Medium*

---
### Q34. What is the purpose of a proxy server in networking?

<span lang='hi'>Networking में proxy server का उद्देश्य क्या है?</span>

- **(A)** Managing IP addresses
- **(B)** Filtering and forwarding network traffic ✅ **(CORRECT)**
- **(C)** Assigning MAC addresses dynamically
- **(D)** Encrypting network communication

**✔ Correct Answer: (B) Filtering and forwarding network traffic** — A proxy server sits between clients and the internet — it filters requests (policy, caching) and forwards them, hiding the client's identity.

*Proxy server clients और internet के बीच बैठता है — यह requests को filter (policy, caching) करके आगे भेजता है, client की पहचान छिपाता है।*

**★ Nukta (Key Point):** Proxy = filter + forward + cache + hide client. Firewall = block/allow by rules. Both are security/traffic devices.

*Proxy = filter + forward + cache + client छिपाना। Firewall = rules से block/allow। दोनों security/traffic devices हैं।*

*[Source: 30 important CN MCQs (Medium blog bank)] · Medium*

---
### Q35. Which is a network security system designed to protect a trusted private network from an untrusted outside network to which it is connected?

<span lang='hi'>कौन-सी network security system trusted private network को उस जुड़े हुए untrusted outside network से बचाने के लिए बनी है?</span>

- **(A)** Bridge
- **(B)** Cookies
- **(C)** Firewall ✅ **(CORRECT)**
- **(D)** SSL

**✔ Correct Answer: (C) Firewall** — A firewall is the security system placed between a trusted internal network and an untrusted external network (like the Internet).

*Firewall एक security system है जो trusted internal network और untrusted external network (जैसे Internet) के बीच लगाया जाता है।*

**★ Nukta (Key Point):** Rajasthan PYQ (verified key: C) — the classic firewall definition. Compare: bridge = L2 link, cookie = web state, SSL = encryption.

*Rajasthan PYQ (verified key: C) — firewall की classic परिभाषा। तुलना: bridge = L2 link, cookie = web state, SSL = encryption।*

*[Source: Random Test- Rajasthan PYQ (OCR), p6 — Q110 (options reconstructed from screenshot)] · Medium*

---
### Q36. What kind of NAT maps one private IP to exactly one public IP?

<span lang='hi'>किस प्रकार का NAT एक private IP को ठीक एक public IP से जोड़ता है?</span>

- **(A)** Dynamic NAT
- **(B)** Static NAT ✅ **(CORRECT)**
- **(C)** PAT (Port Address Translation)
- **(D)** Port Forwarding

**✔ Correct Answer: (B) Static NAT** — Static NAT creates a permanent one-to-one mapping between a private and a public IP address (used for servers).

*Static NAT एक private और एक public IP address के बीच स्थायी one-to-one mapping बनाता है (servers के लिए उपयोग)।*

**★ Nukta (Key Point):** NAT types: Static = 1↔1 permanent. Dynamic = pool mapping. PAT/NAT-overload = many↔1 using ports.

*NAT types: Static = 1↔1 स्थायी। Dynamic = pool mapping। PAT/NAT-overload = ports से many↔1।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

---
### Q37. Which of the following is NOT a networking device?

<span lang='hi'>निम्न में से कौन-सा networking device नहीं है?</span>

- **(A)** Gateway
- **(B)** Linux ✅ **(CORRECT)**
- **(C)** Router
- **(D)** Firewall

**✔ Correct Answer: (B) Linux** — Linux is an operating system, not a networking device — gateway, router and firewall are all network devices/functions.

*Linux एक operating system है, networking device नहीं — gateway, router और firewall सब network devices/functions हैं।*

**★ Nukta (Key Point):** Device vs OS: hardware devices (hub/switch/router) vs software (OS, antivirus) vs firmware-based security devices (firewall).

*Device बनाम OS: hardware devices (hub/switch/router) बनाम software (OS, antivirus) बनाम firmware-based security devices (firewall)।*

*[Source: InstrumentationTools 150 CN MCQs] · Hard*

---
### Q38. Which of the following is NOT a networking device? (Hub / Switch / Bridge / None of these)

<span lang='hi'>निम्न में से कौन-सा networking device नहीं है? (Hub / Switch / Bridge / इनमें से कोई नहीं)</span>

- **(A)** Hub
- **(B)** Switch
- **(C)** Bridge
- **(D)** None of these ✅ **(CORRECT)**

**✔ Correct Answer: (D) None of these** — Hub, switch and bridge are ALL networking devices — so the answer is 'None of these'.

*Hub, switch और bridge — तीनों networking devices हैं — इसलिए उत्तर 'इनमें से कोई नहीं' है।*

**★ Nukta (Key Point):** Mirror question of the 'Linux' variant — read the option SET carefully: here everything listed IS a device.

*'Linux' वाले प्रश्न का दर्पण — option SET ध्यान से पढ़ें: यहाँ सूचीबद्ध सब devices हैं।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Hard*

---

## ★ Nukte Rapid-Fire — Exam Pointers

- **Device-layer ladder (1/2/3/7)?** *(Device-layer ladder (1/2/3/7)?)* → **Hub/Repeater/Modem = 1; Switch/Bridge/NIC = 2; Router = 3; Gateway = 7.** *(Hub/Repeater/Modem = 1; Switch/Bridge/NIC = 2; Router = 3; Gateway = 7।)*
- **Dumb devices?** *(Dumb devices?)* → **Hub and Repeater (no address reading). Bridge/switch/router = intelligent.** *(Hub और Repeater (address नहीं पढ़ते)। Bridge/switch/router = intelligent।)*
- **Hub vs switch — collision domain?** *(Hub vs switch — collision domain?)* → **Hub = 1 collision domain for all ports. Switch = per-port collision domain.** *(Hub = सभी ports के लिए 1 collision domain। Switch = per-port collision domain।)*
- **Who separates broadcast domains?** *(Broadcast domains कौन अलग करता है?)* → **Router (and VLANs on a switch). Switch alone does NOT.** *(Router (और switch पर VLANs)। अकेला switch नहीं।)*
- **Switch CAM table stores?** *(Switch CAM table में क्या होता है?)* → **MAC addresses (learned from source MACs) — for fast frame forwarding.** *(MAC addresses (source MACs से सीखे) — तेज़ frame forwarding के लिए।)*
- **Unknown unicast at a switch?** *(Switch पर unknown unicast?)* → **Flood out all ports (except source). Known = single port. Broadcast = flood.** *(सभी ports से flood (source को छोड़कर)। Known = एक port। Broadcast = flood।)*
- **Router between two switches + broadcast?** *(दो switches के बीच router + broadcast?)* → **Broadcast does NOT cross the router — the other side receives nothing.** *(Broadcast router पार नहीं करता — दूसरी ओर कुछ नहीं मिलता।)*
- **4 VLANs = ? broadcast domains** *(4 VLANs = ? broadcast domains)* → **4 (each VLAN is its own broadcast domain).** *(4 (हर VLAN अपना broadcast domain है)।)*
- **Access point operates at?** *(Access point किस layer पर?)* → **Layer 2 — it is a wireless bridge (802.3 ↔ 802.11 frames).** *(Layer 2 — यह wireless bridge है (802.3 ↔ 802.11 frames)।)*
- **What does a router do per hop?** *(हर hop पर router क्या करता है?)* → **Decrements TTL, updates checksum, rewrites BOTH MAC addresses. IP addresses stay same.** *(TTL घटाता है, checksum अपडेट करता है, दोनों MAC addresses बदलता है। IP addresses same रहते हैं।)*
- **Router functions NOT included?** *(Router के काम में क्या शामिल नहीं?)* → **Collision detection (that's Layer-2 CSMA/CD on switches/NICs).** *(Collision detection (वह Layer-2 CSMA/CD है — switches/NICs पर)।)*
- **Routers reassemble fragments?** *(Routers fragments जोड़ते हैं?)* → **NO — only the destination reassembles. Routers may fragment but never reassemble.** *(नहीं — केवल destination जोड़ता है। Routers fragment कर सकते हैं पर कभी नहीं जोड़ते।)*
- **RED technique?** *(RED technique?)* → **Random Early Detection — drops packets early (randomly) to avoid congestion collapse.** *(Random Early Detection — congestion से बचने के लिए जल्दी (randomly) packets छोड़ता है।)*
- **Gateway = ?** *(Gateway = ?)* → **Protocol converter — links systems with DIFFERENT protocols (works at all 7 layers).** *(Protocol converter — भिन्न protocols वाले systems जोड़ता है (सभी 7 layers पर)।)*
- **Default gateway means?** *(Default gateway का अर्थ?)* → **The router IP used to leave the local network (gateway of last resort).** *(Local network छोड़ने के लिए उपयोग होने वाला router IP (gateway of last resort)।)*
- **Firewall = ?** *(Firewall = ?)* → **Security system between trusted private & untrusted outside networks — filters traffic.** *(Trusted private और untrusted outside networks के बीच security system — traffic filter करता है।)*
- **Packet-filtering vs stateful vs proxy firewall?** *(Packet-filtering vs stateful vs proxy firewall?)* → **L3/L4 IP rules (stateless) → tracks sessions → L7 intermediary (hides clients).** *(L3/L4 IP rules (stateless) → sessions याद → L7 intermediary (clients छिपाती है)।)*
- **Static NAT vs PAT?** *(Static NAT vs PAT?)* → **Static = 1 private ↔ 1 public (permanent). PAT = many private ↔ 1 public (ports).** *(Static = 1 private ↔ 1 public (स्थायी)। PAT = many private ↔ 1 public (ports)।)*
- **MUX = ?** *(MUX = ?)* → **Multiplexer — combines many I/O signals into ONE line (FDM/TDM/WDM); demux splits again.** *(Multiplexer — कई I/O signals को एक line में मिलाता है (FDM/TDM/WDM); demux फिर अलग करता है।)*
- **Intelligent devices?** *(Intelligent devices?)* → **Switch + router (they read addresses & decide). Repeater + hub = dumb.** *(Switch + router (address पढ़कर निर्णय लेते हैं)। Repeater + hub = dumb।)*
- **File server = ?** *(File server = ?)* → **A specialised computer that stores & serves files to clients.** *(एक विशेष computer जो clients को files संग्रहित करके देता है।)*
- **Repeaters extend network how?** *(Repeaters network कैसे बढ़ाते हैं?)* → **Regenerate (amplify + reshape) signals — so data can travel farther without degradation.** *(Signals regenerate (amplify + reshape) करके — data बिना कमज़ोरी के दूर तक जा सकता है।)*

