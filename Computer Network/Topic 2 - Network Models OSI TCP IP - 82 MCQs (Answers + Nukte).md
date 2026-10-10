# Data Communication & Computer Networks (CN)
## Topic 2 of 7 : Network Models (OSI & TCP/IP) — 82 MCQs (English + Hindi)

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** RPSC Programmer • ACP • RSMSSB IA • SA • DD • BCI • SCI • REET • RAS • DSSSB • KVS • NVS • HTET • SSC CGL/CHSL • RRB • IBPS • UPSC & all Rajasthan + Central Govt. Exams (Computer Awareness)

**Total Questions:** 82 | **Type:** MCQ (4 options) | **Bilingual:** English + Hindi (technical terms in English) | Each: ✔ why the correct answer is right + ★ Nukta. Wrong options verified internally. Answers cross-verified 4×.

### Syllabus Coverage (sub-topic wise order)

| # | Sub-topic | Questions |
|---|-----------|-----------|
| 1 | Section A — OSI Model: Basics, Layer Order & Support Layers | Q1 - Q12 |
| 2 | Section B — OSI Layer Functions (Layer 1 → Layer 7) | Q13 - Q63 |
| 3 | Section C — TCP/IP Model | Q64 - Q75 |
| 4 | Section D — Comparison, Encapsulation & PDUs | Q76 - Q82 |

---

## Section A — OSI Model: Basics, Layer Order & Support Layers

*OSI = Open Systems Interconnection (ISO, 1984): 7 layers, layer order, network vs user support layers, address types.*

### Q1. OSI stands for:

<span lang='hi'>OSI का पूरा नाम (full form) क्या है?</span>

- **(A)** Open Systems Interconnection ✅ **(CORRECT)**
- **(B)** Operating System Interface
- **(C)** Optical Service Implementation
- **(D)** None of these

**✔ Correct Answer: (A) Open Systems Interconnection** — OSI = Open Systems Interconnection — the reference model published by ISO in 1984 that standardises network communication into 7 layers.

*OSI = Open Systems Interconnection — ISO द्वारा 1984 में publish किया गया reference model जो network communication को 7 layers में बाँटता है।*

**★ Nukta (Key Point):** OSI = Open Systems Interconnection (ISO, 1984, 7 layers). Ye sabse favourite one-liner hai.

*OSI = Open Systems Interconnection (ISO, 1984, 7 layers)। सबसे favourite one-liner।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q2. The OSI model was developed by:

<span lang='hi'>OSI model किसने develop किया?</span>

- **(A)** IEEE
- **(B)** ISO ✅ **(CORRECT)**
- **(C)** IETF
- **(D)** ITU

**✔ Correct Answer: (B) ISO** — ISO (International Organization for Standardization) published the OSI reference model in 1984.

*ISO (International Organization for Standardization) ने OSI reference model 1984 में publish किया।*

**★ Nukta (Key Point):** OSI = ISO ka (1984). TCP/IP = DoD/ARPA ka. IEEE = 802 LAN standards. IETF = TCP/IP standards.

*OSI = ISO का (1984)। TCP/IP = DoD/ARPA का। IEEE = 802 LAN standards। IETF = TCP/IP standards।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q3. The OSI model has how many layers?

<span lang='hi'>OSI model में कितनी layers हैं?</span>

- **(A)** 5
- **(B)** 6
- **(C)** 7 ✅ **(CORRECT)**
- **(D)** 8

**✔ Correct Answer: (C) 7** — The OSI reference model has exactly 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application.

*OSI reference model में ठीक 7 layers हैं: Physical, Data Link, Network, Transport, Session, Presentation, Application।*

**★ Nukta (Key Point):** Mnemonic: Please Do Not Throw Sausage Pizza Away (Physical, Data-link, Network, Transport, Session, Presentation, Application).

*Mnemonic: Please Do Not Throw Sausage Pizza Away (Physical, Data-link, Network, Transport, Session, Presentation, Application)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q4. Why was the OSI model developed?

<span lang='hi'>OSI model क्यों develop किया गया?</span>

- **(A)** Manufacturers disliked the TCP/IP protocol suite / Manufacturers को TCP/IP protocol suite पसंद नहीं था
- **(B)** The rate of data transfer was increasing exponentially / Data transfer की दर तेज़ी से बढ़ रही थी
- **(C)** Standards were needed to allow any two systems to communicate / किन्हीं भी दो systems के बीच communication के लिए standards चाहिए थे ✅ **(CORRECT)**
- **(D)** None of the above / इनमें से कोई नहीं

**✔ Correct Answer: (C) Standards were needed to allow any two systems to communicate** — OSI was developed to provide an international standard so that any two systems from different vendors could communicate (open systems interconnection).

*OSI एक international standard देने के लिए बना ताकि अलग vendors के कोई भी दो systems आपस में communicate कर सकें।*

**★ Nukta (Key Point):** OSI = OPEN systems — matlab koi bhi do systems jud sakein. Isliye 'standards were needed' sahi jawab hai.

*OSI = OPEN systems — कोई भी दो systems जुड़ सकें। इसलिए 'standards were needed' सही उत्तर है।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q5. In the OSI model, when data is sent from device A to device B, which is the 5th layer to receive data at B (counting from the bottom)?

<span lang='hi'>OSI model में जब data device A से device B को भेजा जाता है, तो B पर data पाने वाली 5वीं layer (नीचे से गिनती में) कौन-सी है?</span>

- **(A)** Application layer
- **(B)** Transport layer
- **(C)** Link layer
- **(D)** Session layer ✅ **(CORRECT)**

**✔ Correct Answer: (D) Session layer** — Counting up at the receiver: 1 Physical, 2 Data Link, 3 Network, 4 Transport, 5 Session. So the 5th layer to receive is the Session layer.

*Receiver पर गिनती: 1 Physical, 2 Data Link, 3 Network, 4 Transport, 5 Session। इसलिए 5वीं layer Session है।*

**★ Nukta (Key Point):** Layer order bottom-up: Physical(1), Data-link(2), Network(3), Transport(4), Session(5), Presentation(6), Application(7).

*Layer क्रम (bottom-up): Physical(1), Data-link(2), Network(3), Transport(4), Session(5), Presentation(6), Application(7)।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q6. The session, presentation, and application layers are the ______ support layers.

<span lang='hi'>Session, Presentation और Application layers ______ support layers हैं।</span>

- **(A)** user ✅ **(CORRECT)**
- **(B)** network
- **(C)** both (a) and (b)
- **(D)** neither (a) nor (b)

**✔ Correct Answer: (A) user** — Layers 5-6-7 (Session, Presentation, Application) are called USER support layers; layers 1-2-3 are NETWORK support layers; Transport (layer 4) joins both.

*Layers 5-6-7 (Session, Presentation, Application) USER support layers कहलाती हैं; layers 1-2-3 NETWORK support layers; Transport (layer 4) दोनों को जोड़ती है।*

**★ Nukta (Key Point):** User support = 5,6,7. Network support = 1,2,3. Transport(4) = dono ka bridge.

*User support = 5,6,7। Network support = 1,2,3। Transport(4) = दोनों का bridge।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q7. Which of the following is NOT a network support layer?

<span lang='hi'>निम्नलिखित में से कौन network support layer नहीं है?</span>

- **(A)** Transport Layer ✅ **(CORRECT)**
- **(B)** Network Layer
- **(C)** Data Link Layer
- **(D)** Physical Layer

**✔ Correct Answer: (A) Transport Layer** — Network support layers = Physical(1), Data Link(2), Network(3). Transport(4) is the bridge between network and user support layers, so it is not counted as a network support layer.

*Network support layers = Physical(1), Data Link(2), Network(3)। Transport(4) network और user support layers के बीच bridge है।*

**★ Nukta (Key Point):** Yaad rakho: NOT-network-support = Transport. (1,2,3 = network support; 5,6,7 = user support.)

*याद रखो: NOT-network-support = Transport। (1,2,3 = network support; 5,6,7 = user support.)*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q8. Network support layers are:

<span lang='hi'>Network support layers कौन-सी हैं?</span>

- **(A)** 1, 2, 3 ✅ **(CORRECT)**
- **(B)** 4, 5
- **(C)** 5, 6, 7
- **(D)** 4 only

**✔ Correct Answer: (A) 1, 2, 3** — Physical(1), Data Link(2) and Network(3) form the network support layers — they move data between the two end systems.

*Physical(1), Data Link(2) और Network(3) मिलकर network support layers बनाती हैं।*

**★ Nukta (Key Point):** 1,2,3 = network support; 5,6,7 = user support; 4 = bridge. Exam mein ye grouping bar-bar aata hai.

*1,2,3 = network support; 5,6,7 = user support; 4 = bridge।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q9. Which layer connects the network support layers and the user support layers?

<span lang='hi'>कौन-सी layer network support layers और user support layers को जोड़ती है?</span>

- **(A)** Transport layer ✅ **(CORRECT)**
- **(B)** Network layer
- **(C)** Data Link layer
- **(D)** Session layer

**✔ Correct Answer: (A) Transport layer** — Transport (layer 4) sits between the network support layers (1-3) and user support layers (5-7) and joins them — it is often called the bridge layer.

*Transport (layer 4) network support layers (1-3) और user support layers (5-7) के बीच बैठकर दोनों को जोड़ती है — इसे bridge layer कहते हैं।*

**★ Nukta (Key Point):** Transport = bridge layer (na upar wale, na neeche wale — dono se judta hai).

*Transport = bridge layer (ऊपर और नीचे दोनों से जुड़ती है)।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q10. In the ISO-OSI reference model, the Session layer offers dialog control, token management and ______ as services.

<span lang='hi'>ISO-OSI reference model में Session layer dialog control, token management और ______ services देती है।</span>

- **(A)** Synchronization ✅ **(CORRECT)**
- **(B)** Asynchronization
- **(C)** Errors
- **(D)** Flow control

**✔ Correct Answer: (A) Synchronization** — The Session layer's three classic services are dialog control, token management and synchronisation (checkpointing for recovery).

*Session layer की तीन classic services हैं: dialog control, token management और synchronization (recovery के लिए checkpointing)।*

**★ Nukta (Key Point):** Session ki 3 services: Dialog control + Token management + Synchronization (checkpoint).

*Session की 3 services: Dialog control + Token management + Synchronization (checkpoint)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)]*

---
### Q11. How many address types (identifiers) are used from sender to receiver in OSI/TCP-IP communication?

<span lang='hi'>OSI/TCP-IP communication में sender से receiver तक कितने address types (identifiers) use होते हैं?</span>

- **(A)** 2
- **(B)** 3
- **(C)** 4 ✅ **(CORRECT)**
- **(D)** 5

**✔ Correct Answer: (C) 4** — Forouzan: four levels of addresses are used — physical (link) address, logical (IP) address, port address and specific (user-friendly) address.

*Forouzan: चार levels के addresses use होते हैं — physical (link) address, logical (IP) address, port address और specific (user-friendly) address।*

**★ Nukta (Key Point):** 4 addresses: Physical(48-bit) / IP(32-bit) / Port(16-bit) / Specific (user-friendly).

*4 addresses: Physical(48-bit) / IP(32-bit) / Port(16-bit) / Specific।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q12. Who developed the standards for the OSI reference model?

<span lang='hi'>OSI reference model के standards किसने develop किए?</span>

- **(A)** ANSI - American National Standards Institute
- **(B)** ISO - International Organization for Standardization ✅ **(CORRECT)**
- **(C)** IEEE - Institute of Electrical and Electronics Engineers
- **(D)** ACM - Association for Computing Machinery

**✔ Correct Answer: (B) ISO - International Organization for Standardization** — ISO (International Organization for Standardization) developed and published the OSI reference model standards.

*ISO (International Organization for Standardization) ने OSI reference model standards develop और publish किए।*

**★ Nukta (Key Point):** OSI ke standards = ISO ke. ANSI/IEEE/ACM ke alag kaam hain (US standards / LAN / computing society).

*OSI के standards = ISO के। ANSI/IEEE/ACM के अलग काम हैं।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---

## Section B — OSI Layer Functions (Layer 1 → Layer 7)

*Which layer does what: Physical, Data Link (LLC/MAC, framing, FCS), Network (logical addressing/routing), Transport (segmentation, end-to-end, ports), Session (dialog/checkpoint), Presentation (translation/encryption/compression), Application (services & protocols).*

### Q13. Fiber optic cables and coaxial cables function at which OSI layer?

<span lang='hi'>Fiber optic cables और coaxial cables किस OSI layer पर काम करती हैं?</span>

- **(A)** Data Link Layer
- **(B)** Physical Layer ✅ **(CORRECT)**
- **(C)** Network Layer
- **(D)** Transport Layer

**✔ Correct Answer: (B) Physical Layer** — Transmission media (fiber, coaxial, twisted pair) are used at the Physical layer — it transmits raw bits over the medium.

*Transmission media (fiber, coaxial, twisted pair) Physical layer पर use होती हैं — यह medium पर raw bits भेजती है।*

**★ Nukta (Key Point):** Media (cable, fiber, radio) = Physical layer ka kaam.

*Media (cable, fiber, radio) = Physical layer का काम।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q14. The term 'Baud Rate' is associated with which layer?

<span lang='hi'>'Baud Rate' शब्द किस layer से जुड़ा है?</span>

- **(A)** Network Layer
- **(B)** Data Link Layer
- **(C)** Physical Layer ✅ **(CORRECT)**
- **(D)** Application Layer

**✔ Correct Answer: (C) Physical Layer** — Baud rate = number of signal changes per second — a Physical layer concept (signal/line encoding).

*Baud rate = प्रति सेकंड signal changes की संख्या — Physical layer की concept (signal/line encoding)।*

**★ Nukta (Key Point):** Baud rate = signalling rate = Physical layer. Bit rate ≠ baud rate (bits per symbol yaad rakho).

*Baud rate = signalling rate = Physical layer। Bit rate ≠ baud rate।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q15. The layer used to deal with mechanical and electrical specifications is:

<span lang='hi'>Mechanical और electrical specifications से निपटने वाली layer कौन-सी है?</span>

- **(A)** Physical Layer ✅ **(CORRECT)**
- **(B)** Data Link Layer
- **(C)** Network Layer
- **(D)** Transport Layer

**✔ Correct Answer: (A) Physical Layer** — The Physical layer defines mechanical, electrical, functional and procedural specifications of the physical link (connectors, voltages, pin layout, signals).

*Physical layer physical link की mechanical, electrical, functional और procedural specifications define करती है (connectors, voltages, pin layout, signals)।*

**★ Nukta (Key Point):** Mechanical + Electrical + Functional + Procedural = Physical layer ke 4 specifications.

*Mechanical + Electrical + Functional + Procedural = Physical layer की 4 specifications।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q16. The Physical layer deals with:

<span lang='hi'>Physical layer किससे निपटती है?</span>

- **(A)** Logical addressing
- **(B)** Media, signals and binary transmission / Media, signals और binary transmission ✅ **(CORRECT)**
- **(C)** Error correction
- **(D)** Segmentation

**✔ Correct Answer: (B) Media, signals and binary transmission** — Physical layer = media, signals, line coding and bit (binary) transmission. Logical addressing = Network; error correction = Data Link/Transport; segmentation = Transport.

*Physical layer = media, signals, line coding और bit transmission। Logical addressing = Network; error correction = Data Link/Transport; segmentation = Transport।*

**★ Nukta (Key Point):** Physical = bits + signals + media. Baaki sab upar ki layers ka kaam hai.

*Physical = bits + signals + media। बाकी ऊपर की layers का काम है।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q17. The Physical layer is responsible for which of the following operations?

<span lang='hi'>Physical layer निम्नलिखित में से किन operations के लिए जिम्मेदार है?</span>

- **(A)** Line coding
- **(B)** Channel coding
- **(C)** Modulation
- **(D)** All of the above ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the above** — Line coding, channel coding and modulation are all Physical layer functions — they prepare the bits for transmission over the medium.

*Line coding, channel coding और modulation — तीनों Physical layer के functions हैं।*

**★ Nukta (Key Point):** Physical layer = Line coding + Channel coding + Modulation + signals/media — 'All of the above' yaad rakho.

*Physical layer = Line coding + Channel coding + Modulation। 'All of the above' याद रखो।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q18. Transmission data rate is decided by:

<span lang='hi'>Transmission data rate कौन तय करती है?</span>

- **(A)** Network layer
- **(B)** Physical layer ✅ **(CORRECT)**
- **(C)** Data Link layer
- **(D)** Transport layer

**✔ Correct Answer: (B) Physical layer** — The data (bit) rate is a Physical layer property — it depends on the bandwidth of the medium and the encoding/modulation used.

*Data (bit) rate Physical layer की property है — यह medium की bandwidth और encoding/modulation पर निर्भर करती है।*

**★ Nukta (Key Point):** Data rate = Physical layer. (Throughput/delay performance bhi isi layer ke signals par depend karti hai.)

*Data rate = Physical layer।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)]*

---
### Q19. Repeaters function in:

<span lang='hi'>Repeaters किस layer पर काम करते हैं?</span>

- **(A)** Physical layer ✅ **(CORRECT)**
- **(B)** Data link layer
- **(C)** Network layer
- **(D)** Both (A) and (B)

**✔ Correct Answer: (A) Physical layer** — A repeater regenerates the electrical/optical signal — a Physical layer device (layer 1).

*Repeater electrical/optical signal regenerate करता है — Physical layer device (layer 1)।*

**★ Nukta (Key Point):** Repeater/Hub = Physical (L1). Bridge/Switch = Data Link (L2). Router = Network (L3).

*Repeater/Hub = Physical (L1)। Bridge/Switch = Data Link (L2)। Router = Network (L3)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)]*

---
### Q20. The physical layer is responsible for:

<span lang='hi'>Physical layer किसके लिए जिम्मेदार है?</span>

- **(A)** Bit-by-bit delivery ✅ **(CORRECT)**
- **(B)** Port to port delivery
- **(C)** Process to process delivery
- **(D)** Application to application delivery

**✔ Correct Answer: (A) Bit-by-bit delivery** — Physical layer = transmission of individual bits over the link (bit-by-bit delivery). Port-to-port = Transport; process-to-process = Transport; application-to-application = Application. (Matches the official RPSC key.)

*Physical layer = link पर bit-by-bit delivery। Port-to-port = Transport; process-to-process = Transport; application-to-application = Application। (Official RPSC key से match.)*

**★ Nukta (Key Point):** Bit-by-bit = Physical. Hop-to-hop = Data Link. Source-to-destination = Network. Process-to-process = Transport.

*Bit-by-bit = Physical। Hop-to-hop = Data Link। Source-to-destination = Network। Process-to-process = Transport।*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q21. The sub-layer of the Physical layer which directly interfaces with the MAC sub-layer is called:

<span lang='hi'>Physical layer का वह sub-layer जो सीधे MAC sub-layer से जुड़ता है, कहलाता है:</span>

- **(A)** Physical signalling sub-layer ✅ **(CORRECT)**
- **(B)** Physical data sub-layer
- **(C)** Physical address sub-layer
- **(D)** Physical transport sub-layer

**✔ Correct Answer: (A) Physical signalling sub-layer** — In the IEEE 802 architecture the Physical Layer Signalling (PLS) sub-layer sits directly under the MAC sub-layer and passes frames to/from it.

*IEEE 802 architecture में Physical Layer Signalling (PLS) sub-layer सीधे MAC sub-layer के नीचे होता है और frames आदान-प्रदान करता है।*

**★ Nukta (Key Point):** PLS (Physical Layer Signalling) = Physical layer ka upper sub-layer jo MAC se directly judta hai.

*PLS (Physical Layer Signalling) = Physical layer का upper sub-layer जो MAC से जुड़ता है।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q22. The physical layer translates logical communication requests from the ______ into hardware-specific operations.

<span lang='hi'>Physical layer, ______ के logical communication requests को hardware-specific operations में बदलता है।</span>

- **(A)** Network layer
- **(B)** Transport layer
- **(C)** Data link layer ✅ **(CORRECT)**
- **(D)** Application layer

**✔ Correct Answer: (C) Data link layer** — The data link layer (directly above the physical layer) sends logical requests like 'transmit this frame'; the physical layer converts them into the electrical/optical hardware operations on the medium.

*Data link layer (physical layer के ठीक ऊपर) जैसे logical requests भेजती है — 'यह frame transmit करो'; physical layer उन्हें medium पर electrical/optical hardware operations में बदलती है।*

**★ Nukta (Key Point):** Each layer serves the layer ABOVE it — physical serves data link. Exam banks sometimes mis-key this as 'network layer'; the correct neighbour is the data link layer.

*हर layer अपने ऊपर वाली layer की सेवा करती है — physical, data link की। कुछ exam banks इसे गलती से 'network layer' लिखते हैं; सही उत्तर data link layer है।*

*[Source: InstrumentationTools 150 CN MCQs (key corrected vs Forouzan)]*

---
### Q23. Which one of the following is a data link (Layer 2) protocol?

<span lang='hi'>निम्न में से कौन data link (Layer 2) protocol है?</span>

- **(A)** Point-to-Point Protocol (PPP)
- **(B)** HDLC
- **(C)** Ethernet
- **(D)** All of these ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of these** — PPP, HDLC and Ethernet are all data link layer (Layer 2) protocols — they frame packets and handle physical addressing/error detection at the link level.

*PPP, HDLC और Ethernet — तीनों data link layer (Layer 2) protocols हैं — ये packets को frame करते हैं और link level पर physical addressing/error detection करते हैं।*

**★ Nukta (Key Point):** Layer 2 protocols = PPP, HDLC, Ethernet, Frame Relay, ATM (cell-based). Network layer = IP, ICMP, ARP.

*Layer 2 protocols = PPP, HDLC, Ethernet, Frame Relay, ATM (cell-based)। Network layer = IP, ICMP, ARP।*

*[Source: InstrumentationTools 150 CN MCQs]*

---
### Q24. The Application layer is implemented in:

<span lang='hi'>Application layer कहाँ implement होती है?</span>

- **(A)** End system ✅ **(CORRECT)**
- **(B)** NIC
- **(C)** Ethernet
- **(D)** Packet transport

**✔ Correct Answer: (A) End system** — In the protocol stack, the application layer (like transport) is implemented in the end systems — the hosts (user's computer or the server) — not inside intermediate network devices.

*Protocol stack में application layer (transport की तरह) end systems में implement होती है — hosts (user का computer या server) में — बीच के network devices में नहीं।*

**★ Nukta (Key Point):** End systems (hosts) implement layers up to the application; switches implement only Layers 1-2, routers only Layers 1-3.

*End systems (hosts) application तक की layers implement करते हैं; switches सिर्फ Layers 1-2, routers सिर्फ Layers 1-3।*

*[Source: Sanfoundry CN MCQs — Reference Models]*

---
### Q25. Which layer of the OSI model is responsible for the transmission and reception of unstructured raw data between a device and a physical transmission medium?

<span lang='hi'>OSI model की कौन-सी layer device और physical transmission medium के बीच unstructured raw data के transmission और reception के लिए जिम्मेदार है?</span>

- **(A)** Transport layer
- **(B)** Data-Link layer
- **(C)** Network layer
- **(D)** Physical layer ✅ **(CORRECT)**

**✔ Correct Answer: (D) Physical layer** — Raw (unstructured) bit transmission over the medium is exactly the Physical layer's role.

*Medium पर raw (unstructured) bits भेजना Physical layer का ही काम है।*

**★ Nukta (Key Point):** 'Raw data + physical medium' = Physical layer. SSC/Railway mein ye one-liner common hai.

*'Raw data + physical medium' = Physical layer।*

*[Source: Central exams — SSC/Railway/UPSC Computer Awareness (Exampundit)]*

---
### Q26. Which layer creates the 'collision domain'?

<span lang='hi'>'Collision domain' कौन-सी layer बनाती है?</span>

- **(A)** Physical Layer (hubs) ✅ **(CORRECT)**
- **(B)** Data Link Layer (switches/bridges)
- **(C)** Network Layer
- **(D)** Transport Layer

**✔ Correct Answer: (A) Physical Layer (hubs)** — A collision domain exists on a shared medium — the shared physical connection created by hubs/repeaters (Physical layer devices). Switches/bridges (Data Link) SEPARATE collision domains; routers separate broadcast domains.

*Collision domain shared medium पर बनता है — hubs/repeaters (Physical layer devices) के shared connection से। Switches/bridges (Data Link) collision domains को अलग करते हैं; routers broadcast domains अलग करते हैं।*

**★ Nukta (Key Point):** Hub network = ONE collision domain (Physical). Switch = per-port collision domain (Data Link). Router = broadcast domain boundary (Network).

*Hub network = एक collision domain (Physical)। Switch = per-port collision domain (Data Link)। Router = broadcast domain boundary (Network)।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q27. Data Link Layer is divided into:

<span lang='hi'>Data Link Layer किनमें विभाजित है?</span>

- **(A)** LLC and MAC ✅ **(CORRECT)**
- **(B)** Physical and Network
- **(C)** Transport and Session
- **(D)** Application and Presentation

**✔ Correct Answer: (A) LLC and MAC** — The IEEE 802 Data Link layer has two sub-layers: LLC (Logical Link Control, 802.2) and MAC (Media Access Control, e.g. 802.3).

*IEEE 802 Data Link layer के दो sub-layers हैं: LLC (Logical Link Control, 802.2) और MAC (Media Access Control, जैसे 802.3)।*

**★ Nukta (Key Point):** Data Link = LLC (upper, 802.2) + MAC (lower, 802.3). Ye hamesha saath aate hain.

*Data Link = LLC (ऊपर, 802.2) + MAC (नीचे, 802.3)।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q28. Which statement best describes the difference between the LLC and MAC sub-layers?

<span lang='hi'>LLC और MAC sub-layers के बीच अंतर सबसे अच्छा कौन बताता है?</span>

- **(A)** LLC handles physical addressing, MAC handles flow control / LLC physical addressing करता है, MAC flow control करता है
- **(B)** LLC provides the service interface to the Network layer; MAC controls access to the medium / LLC, Network layer को service interface देता है; MAC medium तक access control करता है ✅ **(CORRECT)**
- **(C)** LLC works only in wireless networks, MAC only in wired networks / LLC सिर्फ wireless में, MAC सिर्फ wired में काम करता है
- **(D)** LLC performs framing, MAC performs routing / LLC framing करता है, MAC routing करता है

**✔ Correct Answer: (B) LLC provides the service interface to the Network layer; MAC controls access to the medium** — LLC (802.2) provides an interface to the Network layer (flow/error control over the link); MAC (802.3 etc.) handles physical addressing and media access (CSMA/CD etc.).

*LLC (802.2) Network layer को interface देता है; MAC (802.3 आदि) physical addressing और media access (CSMA/CD आदि) संभालता है।*

**★ Nukta (Key Point):** LLC = upar wala sub-layer (network layer se link). MAC = neeche wala (medium access + physical address).

*LLC = ऊपर का sub-layer। MAC = नीचे का (medium access + physical address)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)]*

---
### Q29. Physical (hardware) addressing is added at:

<span lang='hi'>Physical (hardware) addressing किस layer पर जोड़ी जाती है?</span>

- **(A)** Network
- **(B)** Transport
- **(C)** Data Link ✅ **(CORRECT)**
- **(D)** Session

**✔ Correct Answer: (C) Data Link** — The MAC/physical address (48-bit) is added to the frame header at the Data Link layer.

*MAC/physical address (48-bit) frame header में Data Link layer पर जोड़ी जाती है।*

**★ Nukta (Key Point):** Physical/MAC address = Data Link. IP/Logical = Network. Port = Transport.

*Physical/MAC address = Data Link। IP/Logical = Network। Port = Transport।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q30. A frame is received at the Data Link layer with an incorrect FCS. What will happen?

<span lang='hi'>Data Link layer पर frame गलत FCS के साथ प्राप्त होता है। क्या होगा?</span>

- **(A)** Frame discarded ✅ **(CORRECT)**
- **(B)** Frame corrected
- **(C)** Sent to network layer
- **(D)** Re-transmitted automatically

**✔ Correct Answer: (A) Frame discarded** — FCS (Frame Check Sequence, usually CRC) detects errors; a frame with a bad FCS is silently discarded by the receiver's Data Link layer (retransmission, if any, is a higher-level/ARQ decision).

*FCS (Frame Check Sequence, सामान्यतः CRC) errors detect करता है; गलत FCS वाला frame receiver की Data Link layer द्वारा discard कर दिया जाता है।*

**★ Nukta (Key Point):** Bad FCS = frame drop (discard). Correction/Data Link khud re-transmit nahi karti — wo ARQ/higher layer ka decision hai.

*गलत FCS = frame discard।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q31. 'Transparent transmission' is the function of which layer?

<span lang='hi'>'Transparent transmission' किस layer का काम है?</span>

- **(A)** Data link ✅ **(CORRECT)**
- **(B)** Network
- **(C)** Session
- **(D)** Transport

**✔ Correct Answer: (A) Data link** — The Data Link layer makes the physical link look error-free/transparent to the Network layer — it hides all bit-level details.

*Data Link layer physical link को Network layer के लिए error-free/transparent बनाती है — सारी bit-level details छिपा देती है।*

**★ Nukta (Key Point):** Data Link = 'transparent service' — Network layer ko pata hi nahi chalta ki neeche kitni mehnat hui.

*Data Link = 'transparent service' — Network layer को नीचे की मेहनत पता नहीं चलती।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q32. Which layer handles 'hop-to-hop' flow control?

<span lang='hi'>'Hop-to-hop' flow control कौन-सी layer संभालती है?</span>

- **(A)** Network
- **(B)** Data Link ✅ **(CORRECT)**
- **(C)** Transport
- **(D)** Physical

**✔ Correct Answer: (B) Data Link** — Hop-to-hop (node-to-node) flow control is done by the Data Link layer between two adjacent nodes; end-to-end flow control is Transport's job.

*Hop-to-hop (node-to-node) flow control Data Link layer करती है; end-to-end flow control Transport का काम है।*

**★ Nukta (Key Point):** Hop-to-hop = Data Link. End-to-end = Transport. Dono flow control karte hain — scope alag hai.

*Hop-to-hop = Data Link। End-to-end = Transport।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q33. The ______ layer is responsible for delivering data units from one station to the next without errors.

<span lang='hi'>______ layer data units को एक station से अगले station तक बिना errors पहुँचाने के लिए जिम्मेदार है।</span>

- **(A)** Transport
- **(B)** Network
- **(C)** Data link ✅ **(CORRECT)**
- **(D)** Physical

**✔ Correct Answer: (C) Data link** — Forouzan: the Data Link layer is responsible for delivering data units from one station to the NEXT without errors (hop-to-hop delivery).

*Forouzan: Data Link layer data units को एक station से अगले तक बिना errors पहुँचाती है (hop-to-hop delivery)।*

**★ Nukta (Key Point):** 'Station to next station' = Data Link (hop-to-hop). 'Source to destination' = Network.

*'Station to next station' = Data Link। 'Source to destination' = Network।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q34. ______ Layer is responsible for framing, error detection and physical addressing.

<span lang='hi'>______ Layer framing, error detection और physical addressing के लिए जिम्मेदार है।</span>

- **(A)** Network
- **(B)** Transport
- **(C)** Application
- **(D)** Data Link ✅ **(CORRECT)**

**✔ Correct Answer: (D) Data Link** — Framing, error detection (CRC/FCS) and physical (MAC) addressing — all three are classic Data Link layer responsibilities.

*Framing, error detection (CRC/FCS) और physical (MAC) addressing — तीनों Data Link layer की जिम्मेदारी हैं।*

**★ Nukta (Key Point):** Framing + Error detection + MAC addressing = Data Link ka 'trio'.

*Framing + Error detection + MAC addressing = Data Link का trio।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q35. Bridge works in which layer of the OSI model?

<span lang='hi'>Bridge OSI model की किस layer पर काम करता है?</span>

- **(A)** Application layer
- **(B)** Transport layer
- **(C)** Network layer
- **(D)** Data link layer ✅ **(CORRECT)**

**✔ Correct Answer: (D) Data link layer** — A bridge connects two LAN segments and filters/forwards frames using MAC addresses — a Data Link layer (layer 2) device.

*Bridge दो LAN segments को जोड़ता है और MAC addresses से frames filter/forward करता है — Data Link layer (layer 2) device।*

**★ Nukta (Key Point):** Bridge/Switch = L2. Router = L3. Hub/Repeater = L1. Gateway = L4+.

*Bridge/Switch = L2। Router = L3। Hub/Repeater = L1। Gateway = L4+।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2) · also asked in KVS PGT CS 2018 Official Paper]*

---
### Q36. From which layer does the Data Link layer collect packets and encapsulate them into frames for transmission?

<span lang='hi'>Data Link layer किस layer से packets लेकर उन्हें transmission के लिए frames में encapsulate करती है?</span>

- **(A)** Transport layer
- **(B)** Application layer
- **(C)** Network layer ✅ **(CORRECT)**
- **(D)** Physical layer

**✔ Correct Answer: (C) Network layer** — The Data Link layer receives packets (datagrams) from the Network layer above and encapsulates them into frames.

*Data Link layer ऊपर की Network layer से packets (datagrams) लेती है और उन्हें frames में encapsulate करती है।*

**★ Nukta (Key Point):** Encapsulation: Network packet -> Data Link frame -> Physical bits. Upar se neeche.

*Encapsulation: Network packet -> Data Link frame -> Physical bits।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q37. Which OSI layer is responsible for logical addressing?

<span lang='hi'>Logical addressing के लिए कौन-सी OSI layer जिम्मेदार है?</span>

- **(A)** Data Link
- **(B)** Network ✅ **(CORRECT)**
- **(C)** Transport
- **(D)** Application

**✔ Correct Answer: (B) Network** — Logical (IP) addressing and routing are Network layer functions (layer 3).

*Logical (IP) addressing और routing Network layer (layer 3) के functions हैं।*

**★ Nukta (Key Point):** Logical address = IP = Network layer (L3). Physical address = MAC = Data Link (L2).

*Logical address = IP = Network layer (L3)। Physical address = MAC = Data Link (L2)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q38. IPv4 and IPv6 work at which OSI layer?

<span lang='hi'>IPv4 और IPv6 किस OSI layer पर काम करते हैं?</span>

- **(A)** Data link layer
- **(B)** Network layer ✅ **(CORRECT)**
- **(C)** Transport layer
- **(D)** Application layer

**✔ Correct Answer: (B) Network layer** — IP (IPv4/IPv6) is the Network layer protocol of the Internet — layer 3.

*IP (IPv4/IPv6) Internet का Network layer protocol है — layer 3।*

**★ Nukta (Key Point):** IP = Internet Protocol = Network/Internet layer (L3). Hamesha!

*IP = Network/Internet layer (L3)।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)]*

---
### Q39. The ______ layer is responsible for the source-to-destination delivery of a packet across multiple network links.

<span lang='hi'>______ layer एक packet की multiple network links के बीच source-to-destination delivery के लिए जिम्मेदार है।</span>

- **(A)** Transport
- **(B)** Network ✅ **(CORRECT)**
- **(C)** Data link
- **(D)** Physical

**✔ Correct Answer: (B) Network** — Forouzan: the Network layer handles source-to-destination (host-to-host) delivery of a packet across multiple links via routing.

*Forouzan: Network layer routing के जरिए packet की multiple links के बीच source-to-destination delivery करती है।*

**★ Nukta (Key Point):** Source-to-destination = Network. Process-to-process = Transport. Station-to-station = Data Link.

*Source-to-destination = Network। Process-to-process = Transport। Station-to-station = Data Link।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q40. Which layer performs segmentation?

<span lang='hi'>Segmentation कौन-सी layer करती है?</span>

- **(A)** Data link
- **(B)** Transport ✅ **(CORRECT)**
- **(C)** Network
- **(D)** Session

**✔ Correct Answer: (B) Transport** — The Transport layer splits the message into segments and reassembles them at the destination (segmentation and reassembly).

*Transport layer message को segments में बाँटती है और destination पर जोड़ती है (segmentation and reassembly)।*

**★ Nukta (Key Point):** Segmentation + Reassembly = Transport. (Packetisation Network ki, Framing Data Link ki.)

*Segmentation + Reassembly = Transport। (Packetisation Network की, Framing Data Link की।)*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q41. Which layer provides end-to-end communication?

<span lang='hi'>End-to-end communication कौन-सी layer देती है?</span>

- **(A)** Network
- **(B)** Transport ✅ **(CORRECT)**
- **(C)** Session
- **(D)** Physical

**✔ Correct Answer: (B) Transport** — Transport provides end-to-end (process-to-process) communication between the two end hosts.

*Transport दोनों end hosts के बीच end-to-end (process-to-process) communication देती है।*

**★ Nukta (Key Point):** End-to-end = Transport. Source-to-destination = Network. Hop-to-hop = Data Link. Bit-by-bit = Physical.

*End-to-end = Transport। Source-to-destination = Network। Hop-to-hop = Data Link। Bit-by-bit = Physical।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q42. In the OSI model, which layer(s) participate in 'end-to-end' delivery? (1) Network (2) Transport (3) Session (4) Data link

<span lang='hi'>OSI model में 'end-to-end' delivery में कौन-सी layer(s) भाग लेती हैं? (1) Network (2) Transport (3) Session (4) Data link</span>

- **(A)** 1, 2 only
- **(B)** 2 only ✅ **(CORRECT)**
- **(C)** 1, 2, 3
- **(D)** 2, 3, 4

**✔ Correct Answer: (B) 2 only** — In OSI terminology 'end-to-end' means between the two end TRANSPORT entities — that is the Transport layer (2 only). Network is source-to-destination; Data Link is hop-to-hop.

*OSI terminology में 'end-to-end' का अर्थ दोनों end TRANSPORT entities के बीच है — यानी सिर्फ Transport layer (2 only)।*

**★ Nukta (Key Point):** End-to-end = Transport only. (Network = host-to-host, Data Link = hop-to-hop.)

*End-to-end = सिर्फ Transport।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q43. Which layer performs 'service point addressing'?

<span lang='hi'>'Service point addressing' कौन-सी layer करती है?</span>

- **(A)** Network
- **(B)** Data Link
- **(C)** Transport ✅ **(CORRECT)**
- **(D)** Session

**✔ Correct Answer: (C) Transport** — Service point addressing = using PORT addresses to reach the correct process on a host — a Transport layer function.

*Service point addressing = host पर सही process तक पहुँचने के लिए PORT addresses का उपयोग — Transport layer का काम।*

**★ Nukta (Key Point):** Service point = Port. Port addressing = Transport (16-bit port numbers).

*Service point = Port। Port addressing = Transport (16-bit port numbers)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q44. Which OSI layer handles message boundaries (knowing where one message ends and the next begins)?

<span lang='hi'>कौन-सी OSI layer message boundaries संभालती है (एक message कहाँ समाप्त होता है और अगला कहाँ शुरू)?</span>

- **(A)** Presentation
- **(B)** Session
- **(C)** Transport ✅ **(CORRECT)**
- **(D)** Network

**✔ Correct Answer: (C) Transport** — Message boundaries are a Transport concern: message-oriented delivery (e.g. UDP/user datagrams) preserves each message as a separate unit at the destination.

*Message boundaries Transport की चिंता है: message-oriented delivery (जैसे UDP/user datagrams) हर message को अलग unit रूप में रखती है।*

**★ Nukta (Key Point):** Message boundary = transport-level concept (UDP message = poora message).

*Message boundary = transport-level concept।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q45. The reliable data transfer is implemented by:

<span lang='hi'>Reliable data transfer कौन-सी layer implement करती है?</span>

- **(A)** Network layer
- **(B)** Physical layer
- **(C)** Presentation layer
- **(D)** Transport layer ✅ **(CORRECT)**

**✔ Correct Answer: (D) Transport layer** — Reliability (acknowledgements, retransmission, in-order delivery) is implemented by the Transport layer (e.g. TCP). (Matches the official RPSC key.)

*Reliability (acknowledgements, retransmission, in-order delivery) Transport layer implement करती है (जैसे TCP)। (Official RPSC key से match.)*

**★ Nukta (Key Point):** Reliable delivery = Transport (TCP). IP (Network) unreliable hai — best-effort only.

*Reliable delivery = Transport (TCP)। IP (Network) unreliable है।*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q46. Which layer is responsible for reliable delivery in the OSI model?

<span lang='hi'>OSI model में reliable delivery के लिए कौन-सी layer जिम्मेदार है?</span>

- **(A)** Session
- **(B)** Transport ✅ **(CORRECT)**
- **(C)** Network
- **(D)** Application

**✔ Correct Answer: (B) Transport** — The Transport layer ensures reliable (error-free, in-order) message delivery between processes.

*Transport layer processes के बीच reliable (error-free, in-order) message delivery सुनिश्चित करती है।*

**★ Nukta (Key Point):** Reliable = Transport. (OSI Transport class 4 = error recovery wali service.)

*Reliable = Transport।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)]*

---
### Q47. Which layer is responsible for process-to-process delivery?

<span lang='hi'>Process-to-process delivery के लिए कौन-सी layer जिम्मेदार है?</span>

- **(A)** Network layer
- **(B)** Transport layer ✅ **(CORRECT)**
- **(C)** Session layer
- **(D)** Data link layer

**✔ Correct Answer: (B) Transport layer** — Process-to-process (end-to-end) delivery of the entire message is the Transport layer's responsibility, using port addresses.

*पूरे message की process-to-process (end-to-end) delivery Transport layer की जिम्मेदारी है, port addresses के साथ।*

**★ Nukta (Key Point):** Process-to-process = Transport (ports ke saath). Host-to-host = Network (IP ke saath).

*Process-to-process = Transport। Host-to-host = Network।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q48. If a port number is 16 bits (2 bytes), what is the MINIMUM size of the transport-layer header needed to carry the port addresses?

<span lang='hi'>यदि port number 16 bits (2 bytes) का है, तो port addresses ले जाने के लिए transport-layer header की MINIMUM size कितनी होगी?</span>

- **(A)** 2 bytes
- **(B)** 4 bytes ✅ **(CORRECT)**
- **(C)** 8 bytes
- **(D)** 20 bytes

**✔ Correct Answer: (B) 4 bytes** — A transport header must carry at least two port numbers (source + destination) = 2 × 2 bytes = 4 bytes. (Real protocols add more: UDP header = 8 bytes, TCP header = 20 bytes.)

*Transport header में कम से कम दो port numbers (source + destination) होते हैं = 2 × 2 bytes = 4 bytes। (असली protocols में और fields होते हैं: UDP = 8 bytes, TCP = 20 bytes।)*

**★ Nukta (Key Point):** Min transport header (ports only) = 4 bytes. UDP = 8, TCP = 20 — teeno numbers exam mein aate hain.

*Min transport header (ports only) = 4 bytes। UDP = 8, TCP = 20।*

*[Source: Forouzan Ch1 (Q1-23) — Practice Set]*

---
### Q49. Determine the OSI layer responsible for dialogue control (half-duplex or full-duplex communication).

<span lang='hi'>Dialogue control (half-duplex या full-duplex communication) के लिए कौन-सी OSI layer जिम्मेदार है?</span>

- **(A)** Session Layer ✅ **(CORRECT)**
- **(B)** Transport Layer
- **(C)** Network Layer
- **(D)** Data Link Layer

**✔ Correct Answer: (A) Session Layer** — Dialog control — deciding whose turn it is to speak (half/full-duplex dialog) — is a Session layer service.

*Dialog control — किसकी बारी है (half/full-duplex dialog) — Session layer की service है।*

**★ Nukta (Key Point):** Dialog control + Token management + Synchronization = Session layer ka kaam.

*Dialog control + Token management + Synchronization = Session layer का काम।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q50. Which layer supports 'checkpointing' (synchronisation for recovery)?

<span lang='hi'>कौन-सी layer 'checkpointing' (recovery के लिए synchronization) support करती है?</span>

- **(A)** Transport
- **(B)** Application
- **(C)** Session ✅ **(CORRECT)**
- **(D)** Data link

**✔ Correct Answer: (C) Session** — The Session layer inserts checkpoints/synchronisation points in the data stream so a dialog can resume after a failure.

*Session layer data stream में checkpoints/synchronisation points लगाती है ताकि failure के बाद dialog जारी रह सके।*

**★ Nukta (Key Point):** Checkpointing = Session (synchronization). Ye exam ka classic sawaal hai.

*Checkpointing = Session।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q51. Which layer translates data from a format used by the application into a common format (e.g., ASCII to EBCDIC)?

<span lang='hi'>कौन-सी layer data को application के format से common format में बदलती है (जैसे ASCII से EBCDIC)?</span>

- **(A)** Application Layer
- **(B)** Presentation Layer ✅ **(CORRECT)**
- **(C)** Session Layer
- **(D)** Transport Layer

**✔ Correct Answer: (B) Presentation Layer** — Translation between data formats (ASCII/EBCDIC), encryption and compression are Presentation layer jobs.

*Data formats के बीच translation (ASCII/EBCDIC), encryption और compression Presentation layer का काम है।*

**★ Nukta (Key Point):** Presentation = Translation + Encryption + Compression (TEC). ASCII<->EBCDIC isi layer ka classic example hai.

*Presentation = Translation + Encryption + Compression।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q52. Which layer is responsible for encryption?

<span lang='hi'>Encryption के लिए कौन-सी layer जिम्मेदार है?</span>

- **(A)** Session
- **(B)** Presentation ✅ **(CORRECT)**
- **(C)** Application
- **(D)** Transport

**✔ Correct Answer: (B) Presentation** — Encryption/decryption of data for presentation is a Presentation layer responsibility (layer 6).

*Presentation के लिए data की encryption/decryption Presentation layer (layer 6) की जिम्मेदारी है।*

**★ Nukta (Key Point):** Encryption + Compression + Translation = Presentation (L6).

*Encryption + Compression + Translation = Presentation (L6)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q53. Which OSI layer ensures interoperability between different data formats?

<span lang='hi'>कौन-सी OSI layer अलग-अलग data formats के बीच interoperability सुनिश्चित करती है?</span>

- **(A)** Presentation ✅ **(CORRECT)**
- **(B)** Application
- **(C)** Session
- **(D)** Network

**✔ Correct Answer: (A) Presentation** — The Presentation layer provides a common data representation/translation so different systems understand each other's formats.

*Presentation layer एक common data representation/translation देती है ताकि अलग systems एक-दूसरे के formats समझ सकें।*

**★ Nukta (Key Point):** Common format = Presentation. Isi liye ise 'syntax layer' bhi kehte hain.

*Common format = Presentation। इसे 'syntax layer' भी कहते हैं।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q54. Which OSI layer decides the type of compression?

<span lang='hi'>कौन-सी OSI layer compression का प्रकार तय करती है?</span>

- **(A)** Application
- **(B)** Presentation ✅ **(CORRECT)**
- **(C)** Transport
- **(D)** Data link

**✔ Correct Answer: (B) Presentation** — Data compression (and its type) is a Presentation layer function.

*Data compression (और उसका प्रकार) Presentation layer का काम है।*

**★ Nukta (Key Point):** Compression = Presentation. (Encryption aur translation bhi isi ke saath.)

*Compression = Presentation।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q55. Which OSI layer is responsible for encryption and compression?

<span lang='hi'>Encryption और compression के लिए कौन-सी OSI layer जिम्मेदार है?</span>

- **(A)** Presentation Layer ✅ **(CORRECT)**
- **(B)** Session Layer
- **(C)** Transport Layer
- **(D)** Network Layer

**✔ Correct Answer: (A) Presentation Layer** — Both encryption and compression are Presentation layer functions (layer 6).

*Encryption और compression दोनों Presentation layer (layer 6) के functions हैं।*

**★ Nukta (Key Point):** Trio yaad rakho: Translation, Encryption, Compression = Presentation.

*Trio: Translation, Encryption, Compression = Presentation।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)]*

---
### Q56. Which layer helps to present data in one form on a host to another host in its native representation?

<span lang='hi'>कौन-सी layer एक host पर किसी form में data को दूसरे host पर उसकी native representation में प्रस्तुत करने में मदद करती है?</span>

- **(A)** Application Layer
- **(B)** Presentation Layer ✅ **(CORRECT)**
- **(C)** Session Layer
- **(D)** Transport Layer

**✔ Correct Answer: (B) Presentation Layer** — Converting between a host's internal representation and a common format is the Presentation layer's translation job.

*Host की internal representation और common format के बीच बदलना Presentation layer का translation काम है।*

**★ Nukta (Key Point):** Native format <-> common format = Presentation (translation).

*Native format <-> common format = Presentation।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q57. ______ layer defines how data is formatted, presented, encoded, and converted for use on the network.

<span lang='hi'>______ layer तय करती है कि data network में उपयोग के लिए कैसे format, present, encode और convert होता है।</span>

- **(A)** Transport
- **(B)** Presentation ✅ **(CORRECT)**
- **(C)** Application
- **(D)** Physical

**✔ Correct Answer: (B) Presentation** — This is the textbook definition of the Presentation layer — formatting, encoding and conversion of data.

*यह Presentation layer की textbook definition है — data का formatting, encoding और conversion।*

**★ Nukta (Key Point):** 'Formatted, presented, encoded, converted' = Presentation ke liye mnemonic-type line.

*'Formatted, presented, encoded, converted' = Presentation।*

*[Source: Central exams — SSC/Bank/Insurance Computer Awareness (BYJU'S)]*

---
### Q58. Which layer provides services to the user?

<span lang='hi'>कौन-सी layer user को services देती है?</span>

- **(A)** Application layer ✅ **(CORRECT)**
- **(B)** Session layer
- **(C)** Presentation layer
- **(D)** Physical layer

**✔ Correct Answer: (A) Application layer** — The Application layer (layer 7) provides network services directly to user applications (HTTP, FTP, SMTP, DNS...).

*Application layer (layer 7) user applications को सीधे network services देती है (HTTP, FTP, SMTP, DNS...)।*

**★ Nukta (Key Point):** User ke sabse kareeb = Application layer (L7).

*User के सबसे करीब = Application layer (L7)।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q59. A server at a company is using TCP/IP to connect to the network and is running multiple applications. At which OSI layer is this server operating?

<span lang='hi'>एक company का server network से जुड़ने के लिए TCP/IP use कर रहा है और अनेक applications चला रहा है। यह server किस OSI layer पर काम कर रहा है?</span>

- **(A)** Application Layer ✅ **(CORRECT)**
- **(B)** Physical Layer
- **(C)** Network Layer
- **(D)** Transport Layer

**✔ Correct Answer: (A) Application Layer** — Running multiple applications that serve users = Application layer work (the applications use the lower layers for delivery).

*users के लिए अनेक applications चलाना = Application layer का काम (applications नीचे की layers use करती हैं)।*

**★ Nukta (Key Point):** Server + running applications = Application layer.

*Server + applications = Application layer।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q60. Simple Network Management Protocol (SNMP) runs on:

<span lang='hi'>Simple Network Management Protocol (SNMP) किस layer पर चलता है?</span>

- **(A)** Application layer ✅ **(CORRECT)**
- **(B)** Transport layer
- **(C)** Network layer
- **(D)** Data link layer

**✔ Correct Answer: (A) Application layer** — SNMP is an Application layer protocol (it uses UDP at the transport layer to manage network devices).

*SNMP एक Application layer protocol है (network devices manage करने के लिए यह UDP use करता है)।*

**★ Nukta (Key Point):** SNMP/DNS/HTTP/FTP/SMTP = Application layer protocols. UDP/TCP = Transport. IP = Network.

*SNMP/DNS/HTTP/FTP/SMTP = Application layer protocols।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)]*

---
### Q61. Application layer protocol defines:

<span lang='hi'>Application layer protocol क्या define करता है?</span>

- **(A)** Types of messages exchanged / कौन-से messages आदान-प्रदान होते हैं
- **(B)** Rules for when and how processes send and respond to messages / processes messages कब और कैसे भेजें/जवाब दें — इसके rules
- **(C)** Message format, syntax and semantics / Message format, syntax और semantics
- **(D)** All of the above / उपरोक्त सभी ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the above** — An application-layer protocol defines the message types, the rules for when/how processes send and respond, and the message format (syntax + semantics) — all of the above.

*Application-layer protocol message types, भेजने/जवाब के rules, और message format (syntax + semantics) — सब define करता है।*

**★ Nukta (Key Point):** Application protocol = Message types + Rules + Format. 'All of the above' hi jawab hai.

*Application protocol = Message types + Rules + Format।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q62. SMTP, FTP and DNS are the protocols of which layer of the OSI model?

<span lang='hi'>SMTP, FTP और DNS OSI model की किस layer के protocols हैं?</span>

- **(A)** Network layer
- **(B)** Transport layer
- **(C)** Application layer ✅ **(CORRECT)**
- **(D)** Data Link layer

**✔ Correct Answer: (C) Application layer** — SMTP (e-mail), FTP (file transfer) and DNS (name resolution) are all Application layer protocols (layer 7).

*SMTP (e-mail), FTP (file transfer) और DNS (name resolution) — तीनों Application layer protocols (layer 7) हैं।*

**★ Nukta (Key Point):** User-facing protocols (HTTP, FTP, SMTP, DNS, POP3, IMAP) = Application layer.

*User-facing protocols = Application layer।*

*[Source: Central exams — SSC/Railway/UPSC Computer Awareness (Exampundit)]*

---
### Q63. Consider the statements:
S1: Network layer handles both logical addressing and routing.
S2: Transport layer handles segmentation and reassembly.
Which is correct?

<span lang='hi'>Statements देखिए:
S1: Network layer logical addressing और routing दोनों संभालती है।
S2: Transport layer segmentation और reassembly संभालती है।
कौन सा सही है?</span>

- **(A)** Only S1
- **(B)** Only S2
- **(C)** Both S1 and S2 ✅ **(CORRECT)**
- **(D)** Neither S1 nor S2

**✔ Correct Answer: (C) Both S1 and S2** — Both statements are textbook-correct: Network = logical addressing + routing; Transport = segmentation + reassembly.

*दोनों statements textbook-correct हैं: Network = logical addressing + routing; Transport = segmentation + reassembly।*

**★ Nukta (Key Point):** Network = IP addressing + Routing. Transport = Segmentation + Reassembly. Dono sahi.

*Network = IP addressing + Routing। Transport = Segmentation + Reassembly।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---

## Section C — TCP/IP Model

*TCP/IP (DoD, 1970s): 4/5 layers, layer mapping to OSI, Internet layer protocols, address levels.*

### Q64. TCP/IP model does not have ______ layer but the OSI model has it.

<span lang='hi'>TCP/IP model में ______ layer नहीं है पर OSI model में है।</span>

- **(A)** Session layer
- **(B)** Presentation layer
- **(C)** Application layer
- **(D)** Both (a) and (b) ✅ **(CORRECT)**

**✔ Correct Answer: (D) Both (a) and (b)** — TCP/IP has no separate Session or Presentation layers — their functions are absorbed by the TCP/IP Application layer. (OSI = 7 layers; TCP/IP = 4 layers.)

*TCP/IP में Session या Presentation की अलग layer नहीं है — उनके काम TCP/IP की Application layer में आ जाते हैं।*

**★ Nukta (Key Point):** TCP/IP mein Session + Presentation nahi hoti — dono Application mein merge ho jaati hain.

*TCP/IP में Session + Presentation नहीं होती — दोनों Application में merge होती हैं।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q65. The TCP/IP model was developed ______ the OSI model.

<span lang='hi'>TCP/IP model, OSI model के ______ develop हुआ।</span>

- **(A)** prior to ✅ **(CORRECT)**
- **(B)** after
- **(C)** simultaneous to
- **(D)** none of these

**✔ Correct Answer: (A) prior to** — TCP/IP was developed in the 1970s (by Cerf & Kahn for ARPANET/DoD) — BEFORE the OSI model (published by ISO in 1984).

*TCP/IP 1970s में develop हुआ (Cerf & Kahn ने ARPANET/DoD के लिए) — OSI model (1984) से पहले।*

**★ Nukta (Key Point):** TCP/IP (1970s, adopted 1983) PEHLE; OSI (1984) BAAD mein. 'Prior to' yaad rakho.

*TCP/IP (1970s) पहले; OSI (1984) बाद में।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q66. The TCP/IP ______ layer is equivalent to the combined Session, Presentation and Application layers of the OSI model.

<span lang='hi'>TCP/IP की ______ layer, OSI model की Session, Presentation और Application layers के समकक्ष है।</span>

- **(A)** application ✅ **(CORRECT)**
- **(B)** network
- **(C)** data link
- **(D)** physical

**✔ Correct Answer: (A) application** — The TCP/IP Application layer covers what OSI layers 5 + 6 + 7 do (application + presentation + session).

*TCP/IP Application layer वही करती है जो OSI की layers 5 + 6 + 7 करती हैं।*

**★ Nukta (Key Point):** Mapping: TCP/IP Application = OSI Session+Presentation+Application; TCP/IP Internet = OSI Network; TCP/IP Network Access = OSI Data Link+Physical.

*Mapping: TCP/IP Application = OSI 5+6+7; Internet = Network; Network Access = Data Link+Physical।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q67. Which of the following is NOT a part of the TCP/IP model?

<span lang='hi'>निम्नलिखित में से कौन TCP/IP model का हिस्सा नहीं है?</span>

- **(A)** Application
- **(B)** Transport
- **(C)** Data link
- **(D)** Session ✅ **(CORRECT)**

**✔ Correct Answer: (D) Session** — TCP/IP (4-layer) = Application, Transport, Internet, Network Access. Session is an OSI layer with no separate TCP/IP layer.

*TCP/IP (4-layer) = Application, Transport, Internet, Network Access। Session OSI की layer है, TCP/IP में अलग नहीं।*

**★ Nukta (Key Point):** TCP/IP ke 4 layers: Application, Transport, Internet, Network Access. Session sirf OSI mein.

*TCP/IP की 4 layers: Application, Transport, Internet, Network Access। Session सिर्फ OSI में।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)]*

---
### Q68. The number of layers in the Internet protocol stack (reference model) is:

<span lang='hi'>Internet protocol stack (reference model) में layers की संख्या कितनी है?</span>

- **(A)** 5 ✅ **(CORRECT)**
- **(B)** 7
- **(C)** 6
- **(D)** 3

**✔ Correct Answer: (A) 5** — The TCP/IP Internet reference (protocol) stack has 5 layers: Physical, Data Link, Network, Transport, Application. (The original TCP/IP suite has 4 — Network Access merges Physical+Data Link.)

*TCP/IP Internet reference stack में 5 layers हैं: Physical, Data Link, Network, Transport, Application। (मूल TCP/IP suite में 4 — Network Access में Physical+Data Link मिले हुए।)*

**★ Nukta (Key Point):** 5-layer Internet stack vs 4-layer TCP/IP suite vs 7-layer OSI — teeno numbers exam mein aate hain!

*5-layer Internet stack, 4-layer TCP/IP suite, 7-layer OSI — तीनों numbers याद रखो!*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q69. How many layers are there in the TCP/IP model (original 4-layer suite)?

<span lang='hi'>TCP/IP model (मूल 4-layer suite) में कितनी layers हैं?</span>

- **(A)** Seven
- **(B)** Five
- **(C)** Four ✅ **(CORRECT)**
- **(D)** Nine

**✔ Correct Answer: (C) Four** — The original TCP/IP model has 4 layers: Network Access, Internet, Host-to-Host (Transport), Application.

*मूल TCP/IP model में 4 layers हैं: Network Access, Internet, Host-to-Host (Transport), Application।*

**★ Nukta (Key Point):** 4-layer TCP/IP: Network Access + Internet + Transport (Host-to-Host) + Application.

*4-layer TCP/IP: Network Access + Internet + Transport + Application।*

*[Source: Central exams — SSC/Bank Computer Awareness (BYJU'S)]*

---
### Q70. Which of the following is NOT a layer of the TCP/IP model? (Host-to-Host / Internet / Network Access / Physical)

<span lang='hi'>निम्नलिखित में से कौन TCP/IP model की layer नहीं है? (Host-to-Host / Internet / Network Access / Physical)</span>

- **(A)** Host to Host
- **(B)** Internet
- **(C)** Network Access
- **(D)** Physical ✅ **(CORRECT)**

**✔ Correct Answer: (D) Physical** — The 4-layer TCP/IP suite has no separate Physical layer — physical functions are part of Network Access.

*4-layer TCP/IP suite में अलग Physical layer नहीं है — physical functions Network Access का हिस्सा हैं।*

**★ Nukta (Key Point):** TCP/IP ki 4 layers: Network Access, Internet, Host-to-Host, Application. 'Physical' alag layer nahi hai.

*TCP/IP की 4 layers: Network Access, Internet, Host-to-Host, Application।*

*[Source: Central exams — SSC/Bank Computer Awareness (BYJU'S)]*

---
### Q71. The Data Link layer and Physical layer of the OSI model combine to form the ______ layer of the TCP/IP model.

<span lang='hi'>OSI model की Data Link और Physical layers मिलकर TCP/IP model की ______ layer बनाती हैं।</span>

- **(A)** Network Access ✅ **(CORRECT)**
- **(B)** Internet
- **(C)** Host to Host
- **(D)** Application

**✔ Correct Answer: (A) Network Access** — OSI layers 1 + 2 (Physical + Data Link) map to the single TCP/IP Network Access layer.

*OSI की layers 1 + 2 (Physical + Data Link) मिलकर TCP/IP की Network Access layer बनाती हैं।*

**★ Nukta (Key Point):** OSI 1+2 = TCP/IP Network Access. OSI 5+6+7 = TCP/IP Application. Bas ye 2 mappings yaad rakho.

*OSI 1+2 = Network Access। OSI 5+6+7 = Application।*

*[Source: Central exams — SSC/Bank Computer Awareness (BYJU'S)]*

---
### Q72. IP (Internet Protocol) is a protocol of the ______ layer of the TCP/IP model.

<span lang='hi'>IP (Internet Protocol) TCP/IP model की ______ layer का protocol है.</span>

- **(A)** Network Access
- **(B)** Internet ✅ **(CORRECT)**
- **(C)** Transport
- **(D)** Application

**✔ Correct Answer: (B) Internet** — IP, ICMP, ARP work at the Internet layer of TCP/IP (equivalent to the OSI Network layer).

*IP, ICMP, ARP TCP/IP की Internet layer पर काम करते हैं (OSI Network layer के समकक्ष)।*

**★ Nukta (Key Point):** IP = Internet layer. TCP/UDP = Transport. Ethernet = Network Access.

*IP = Internet layer। TCP/UDP = Transport। Ethernet = Network Access।*

*[Source: Central exams — SSC/Bank Computer Awareness (BYJU'S)]*

---
### Q73. In TCP/IP, which layer uses specific (user-friendly) addresses — e.g. a URL like example.com?

<span lang='hi'>TCP/IP में कौन-सी layer specific (user-friendly) addresses use करती है — जैसे example.com जैसी URL?</span>

- **(A)** Application layer ✅ **(CORRECT)**
- **(B)** Network layer
- **(C)** Data link layer
- **(D)** Physical layer

**✔ Correct Answer: (A) Application layer** — Forouzan's four address levels: specific/user-friendly addresses (URLs, domain names) are used at the Application layer; port addresses at Transport; IP at Network; physical (MAC) at Data Link.

*Forouzan के चार address levels: specific/user-friendly addresses (URL, domain name) Application layer पर; port addresses Transport पर; IP Network पर; MAC Data Link पर।*

**★ Nukta (Key Point):** Address levels: Application = specific (URL), Transport = port (16-bit), Network = IP (32/128-bit), Data Link = MAC (48-bit).

*Address levels: Application = specific, Transport = port, Network = IP, Data Link = MAC।*

*[Source: Forouzan Ch1 (Q1-24) — Practice Set]*

---
### Q74. In the TCP/IP model, a link-layer switch operates at which layers?

<span lang='hi'>TCP/IP model में link-layer switch किन layers पर काम करता है?</span>

- **(A)** Network and Transport layers
- **(B)** Physical and Data Link layers ✅ **(CORRECT)**
- **(C)** Application layer only
- **(D)** All five layers

**✔ Correct Answer: (B) Physical and Data Link layers** — A link-layer switch reads MAC addresses and regenerates signals — it works at the Physical and Data Link layers (the TCP/IP Network Access layer).

*link-layer switch MAC addresses पढ़ता है और signals regenerate करता है — यह Physical और Data Link layers (Network Access) पर काम करता है।*

**★ Nukta (Key Point):** Switch = L1+L2 (Network Access). Router = L3 tak. Gateway = L4+.

*Switch = L1+L2। Router = L3 तक। Gateway = L4+।*

*[Source: Forouzan Ch1 (Q1-16) — Practice Set]*

---
### Q75. Which is the standard protocol suite of the Internet?

<span lang='hi'>Internet की मानक protocol suite कौन-सी है?</span>

- **(A)** TCP/IP ✅ **(CORRECT)**
- **(B)** UDP
- **(C)** FTP
- **(D)** WWW

**✔ Correct Answer: (A) TCP/IP** — TCP/IP ही Internet की standard protocol suite है — इसी पर पूरा Internet चलता है.

*TCP/IP ही Internet की standard protocol suite है — इसी पर पूरा Internet चलता है.*

**★ Nukta (Key Point):** UDP/FTP इसी suite के अंदर के protocols हैं; WWW तो सेवा है, protocol नहीं.

*UDP/FTP इसी suite के अंदर के protocols हैं; WWW तो सेवा है, protocol नहीं.*

*[Source: IBPS RRB PO Computer Awareness PYQ (via meritnotes) + SSC MTS computer PYQ (via Testbook)]*

---

## Section D — Comparison, Encapsulation & PDUs

*OSI vs TCP/IP, encapsulation order & direction, PDUs per layer, numericals.*

### Q76. Identify the correct order of data encapsulation from Layer 7 to Layer 1:

<span lang='hi'>Layer 7 से Layer 1 तक data encapsulation का सही क्रम पहचानिए:</span>

- **(A)** Data → Segment → Packet → Frame → Bits ✅ **(CORRECT)**
- **(B)** Data → Packet → Segment → Frame → Bits
- **(C)** Bits → Frame → Packet → Segment → Data
- **(D)** Data → Frame → Packet → Segment → Bits

**✔ Correct Answer: (A) Data → Segment → Packet → Frame → Bits** — Going down the OSI stack: Application data → Transport segment → Network packet → Data Link frame → Physical bits.

*OSI stack में नीचे जाते हुए: Application data → Transport segment → Network packet → Data Link frame → Physical bits।*

**★ Nukta (Key Point):** Encapsulation order: Data -> Segment -> Packet -> Frame -> Bits. Mnemonic: 'Do Some People Fear Barking?'

*Encapsulation: Data -> Segment -> Packet -> Frame -> Bits।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)]*

---
### Q77. Encapsulation happens from:

<span lang='hi'>Encapsulation किस दिशा में होती है?</span>

- **(A)** Top to bottom ✅ **(CORRECT)**
- **(B)** Bottom to top
- **(C)** Random
- **(D)** Parallel

**✔ Correct Answer: (A) Top to bottom** — At the sender, each layer adds its header going DOWN the stack (top to bottom); the receiver removes headers going UP (bottom to top).

*Sender पर हर layer नीचे जाते हुए अपना header जोड़ती है (top to bottom); receiver पर ऊपर जाते हुए headers हटते हैं (bottom to top)।*

**★ Nukta (Key Point):** Sender = encapsulation (top->bottom, headers add). Receiver = de-encapsulation (bottom->top, headers remove).

*Sender = encapsulation (top->bottom)। Receiver = de-encapsulation (bottom->top)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)]*

---
### Q78. In the layer hierarchy, as the data packet moves from the upper to the lower layers, headers are:

<span lang='hi'>Layer hierarchy में, जब data packet ऊपर से नीचे की layers की ओर जाता है, तो headers:</span>

- **(A)** Added ✅ **(CORRECT)**
- **(B)** Removed
- **(C)** Rearranged
- **(D)** Modified

**✔ Correct Answer: (A) Added** — Each lower layer ADDS its own header (and sometimes a trailer) to the data unit received from above — that is encapsulation.

*हर नीचे की layer ऊपर से आए data unit में अपना header (कभी-कभी trailer) जोड़ती है — यही encapsulation है।*

**★ Nukta (Key Point):** Down the stack = headers ADD. Up the stack = headers REMOVE.

*नीचे की ओर = headers ADD। ऊपर की ओर = headers REMOVE।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)]*

---
### Q79. A source S and destination D are connected through ONE intermediate router R. How many times does a packet visit the Network layer and the Data Link layer during the journey?

<span lang='hi'>Source S और destination D के बीच एक intermediate router R है। यात्रा के दौरान packet Network layer और Data Link layer को कितनी बार visit करता है?</span>

- **(A)** Network layer - 4 times, Data link layer - 4 times
- **(B)** Network layer - 4 times, Data link layer - 6 times
- **(C)** Network layer - 2 times, Data link layer - 4 times
- **(D)** Network layer - 3 times, Data link layer - 4 times ✅ **(CORRECT)**

**✔ Correct Answer: (D) Network layer - 3 times, Data link layer - 4 times** — Network layer: once at S (send), once at R (forward), once at D (receive) = 3. Data Link: 2 links (S→R, R→D), each visited twice (send + receive) = 4.

*Network layer: S पर 1, R पर 1, D पर 1 = 3 बार। Data Link: 2 links (S→R, R→D), हर link 2 बार (send + receive) = 4 बार।*

**★ Nukta (Key Point):** Formula: n routers -> Network layer visits = n+2, Data Link visits = 2(n+1). Yahan n=1 -> NL=3, DL=4.

*Formula: n routers -> Network layer = n+2, Data Link = 2(n+1)। यहाँ n=1 -> NL=3, DL=4।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)]*

---
### Q80. In TCP/IP, which data unit is encapsulated INSIDE a frame?

<span lang='hi'>TCP/IP में कौन-सा data unit frame के अंदर encapsulate होता है?</span>

- **(A)** A segment
- **(B)** A datagram ✅ **(CORRECT)**
- **(C)** A bit
- **(D)** A message

**✔ Correct Answer: (B) A datagram** — The Data Link layer encapsulates the Network layer's packet (datagram) inside a frame (frame = header + datagram + trailer).

*Data Link layer Network layer के packet (datagram) को frame के अंदर encapsulate करती है (frame = header + datagram + trailer)।*

**★ Nukta (Key Point):** Frame ke andar DATAGRAM hota hai. Segment -> Datagram -> Frame -> Bits.

*Frame के अंदर DATAGRAM होता है।*

*[Source: Forouzan Ch1 (Q1-20) — Practice Set]*

---
### Q81. In the TCP/IP model, the unit of data at the transport layer is called a:

<span lang='hi'>TCP/IP model में transport layer पर data की unit कहलाती है:</span>

- **(A)** Packet
- **(B)** Segment ✅ **(CORRECT)**
- **(C)** Frame
- **(D)** Stream

**✔ Correct Answer: (B) Segment** — Transport layer data unit = segment (TCP) or user datagram (UDP); Network = datagram/packet; Data Link = frame; Physical = bits.

*Transport layer की data unit = segment (TCP) या user datagram (UDP); Network = datagram/packet; Data Link = frame; Physical = bits।*

**★ Nukta (Key Point):** PDU pairs: Transport = Segment, Network = Datagram/Packet, Data Link = Frame, Physical = Bits.

*PDU: Transport = Segment, Network = Datagram, Data Link = Frame, Physical = Bits।*

*[Source: Forouzan Ch1 (Q1-20/21) — Practice Set]*

---
### Q82. A system uses five protocol layers. The application creates a 100-byte message and EVERY layer (including the 5th and the 1st) adds a 10-byte header. What is the efficiency (application bytes / total transmitted bytes)?

<span lang='hi'>एक system में पाँच protocol layers हैं। Application 100-byte message बनाती है और हर layer (5वीं और 1वीं सहित) 10-byte header जोड़ती है। Efficiency कितनी होगी (application bytes / कुल transmitted bytes)?</span>

- **(A)** 50%
- **(B)** 66.7% ✅ **(CORRECT)**
- **(C)** 75%
- **(D)** 80%

**✔ Correct Answer: (B) 66.7%** — Total bytes = 100 (message) + 5 × 10 (headers) = 150. Efficiency = 100/150 = 2/3 ≈ 66.7%.

*कुल bytes = 100 (message) + 5 × 10 (headers) = 150। Efficiency = 100/150 = 2/3 ≈ 66.7%।*

**★ Nukta (Key Point):** Encapsulation overhead numerical: efficiency = data / (data + headers). 100/(100+50) = 66.7%.

*Efficiency = data / (data + headers) = 100/150 = 66.7%।*

*[Source: Forouzan Ch1 (P1-11) — Practice Set (Problem)]*

---

## ★ Nukte Rapid-Fire — Exam Pointers

- **OSI layers mnemonic?** *(OSI layers की mnemonic?)* → **Please Do Not Throw Sausage Pizza Away (L1→L7)** *(Please Do Not Throw Sausage Pizza Away (L1→L7))*
- **OSI kisne banaya, kab?** *(OSI किसने बनाया, कब?)* → **ISO, in 1984 — 7 layers** *(ISO, 1984 में — 7 layers)*
- **TCP/IP kisne banaya?** *(TCP/IP किसने बनाया?)* → **Cerf & Kahn (DoD/ARPA), 1970s — adopted 1983** *(Cerf & Kahn (DoD/ARPA), 1970s — adopted 1983)*
- **Layer counts?** *(Layer counts?)* → **OSI = 7, Internet stack = 5, TCP/IP suite = 4** *(OSI = 7, Internet stack = 5, TCP/IP suite = 4)*
- **TCP/IP mein kya missing?** *(TCP/IP में क्या missing?)* → **No separate Session & Presentation layers** *(Session और Presentation की अलग layers नहीं)*
- **OSI→TCP/IP mapping?** *(OSI→TCP/IP mapping?)* → **OSI 1+2 = Network Access; OSI 5+6+7 = Application** *(OSI 1+2 = Network Access; OSI 5+6+7 = Application)*
- **PDU per layer?** *(हर layer की PDU?)* → **Data / Segment / Packet-Datagram / Frame / Bits** *(Data / Segment / Packet-Datagram / Frame / Bits)*
- **Encapsulation direction?** *(Encapsulation की दिशा?)* → **Sender: top→bottom (headers add); Receiver: bottom→top (remove)** *(Sender: top→bottom; Receiver: bottom→top)*
- **4 levels of addresses?** *(4 levels के addresses?)* → **Physical(48-bit), IP(32/128-bit), Port(16-bit), Specific(URL)** *(Physical(48-bit), IP(32/128-bit), Port(16-bit), Specific(URL))*
- **Delivery scopes?** *(Delivery के scopes?)* → **Bit-by-bit=Physical; Hop-to-hop=Data Link; Source-destination=Network; End-to-end/Process-process=Transport** *(Bit-by-bit=Physical; Hop-to-hop=Data Link; Source-destination=Network; End-to-end=Transport)*
- **Presentation layer kaam?** *(Presentation layer के काम?)* → **Translation + Encryption + Compression** *(Translation + Encryption + Compression)*
- **Session layer ke 3 kaam?** *(Session layer के 3 काम?)* → **Dialog control + Token management + Synchronization (checkpoint)** *(Dialog control + Token management + Synchronization)*
- **Data Link ka trio?** *(Data Link का trio?)* → **Framing + Error detection + Physical(MAC) addressing** *(Framing + Error detection + MAC addressing)*
- **LLC vs MAC?** *(LLC बनाम MAC?)* → **LLC (802.2) = Network layer interface; MAC (802.3) = medium access + MAC address** *(LLC = interface; MAC = medium access + address)*
- **Support layers grouping?** *(Support layers grouping?)* → **Network support = 1,2,3; User support = 5,6,7; Transport(4) = bridge** *(Network support = 1,2,3; User support = 5,6,7; Transport = bridge)*
- **Device layers?** *(Devices की layers?)* → **Repeater/Hub=L1; Bridge/Switch=L2; Router=L3; Gateway=L4+** *(Repeater/Hub=L1; Bridge/Switch=L2; Router=L3; Gateway=L4+)*
- **Reliable delivery?** *(Reliable delivery?)* → **Transport layer (TCP) — IP is best-effort only** *(Transport layer (TCP) — IP सिर्फ best-effort)*
- **Router visits formula?** *(Router visits का formula?)* → **n routers: Network layer = n+2, Data Link = 2(n+1)** *(n routers: Network layer = n+2, Data Link = 2(n+1))*
- **Physical layer ka kaam?** *(Physical layer का काम?)* → **Signals, media, line/channel coding, modulation, baud rate, bit-by-bit** *(Signals, media, coding, modulation, baud rate, bit-by-bit)*
- **IP/ICMP/ARP kis layer ke?** *(IP/ICMP/ARP किस layer के?)* → **Network / Internet layer (L3)** *(Network / Internet layer (L3))*

