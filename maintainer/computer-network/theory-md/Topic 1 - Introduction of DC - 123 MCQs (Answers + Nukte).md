# Data Communication & Computer Networks (CN)
## Topic 1 of 7 : Introduction of DC (Data Communication) — 123 MCQs (English + Hindi)

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** RPSC Programmer • ACP • RSMSSB IA • SA • DD • BCI • SCI • REET • RAS • DSSSB • KVS • NVS • HTET • SSC CGL/CHSL • RRB • IBPS • UPSC & all Rajasthan + Central Govt. Exams (Computer Awareness)

**Total Questions:** 123 | **Type:** MCQ (4 options) | **Bilingual:** English + Hindi (technical terms in English) | Each: ✔ why the correct answer is right + ★ Nukta. Wrong options verified internally. Answers cross-verified 4×.

### Syllabus Coverage (sub-topic wise order)

| # | Sub-topic | Questions |
|---|-----------|-----------|
| 1 | Section A - DC Components & Protocol Basics (Message, Sender, Receiver, Transmission Medium, Protocol) | Q1 - Q17 |
| 2 | Section B - Characteristics (Delivery, Accuracy, Timeliness, Jitter) & Criteria (Performance, Reliability, Security) | Q18 - Q36 |
| 3 | Section C - Transmission Mode (Direction of Data Flow: Simplex, Half-Duplex, Full-Duplex) | Q37 - Q45 |
| 4 | Section D - Network Structure / Topology (Physical: Mesh, Star, Bus, Ring, Others; Logical: IEEE 802) | Q46 - Q66 |
| 5 | Section E - Types of Networks (LAN, MAN, WAN, PAN, CAN, SAN; Internet, Intranet, Extranet; Point-to-Point, Multipoint; Client-Server, P2P) | Q67 - Q99 |
| 6 | Section F - Network History (ARPANET to Today's Network) | Q100 - Q106 |
| 7 | Section G - General Network Basics (WWW, E-mail, Protocols, Servers, Switching - from repo intro tests) | Q107 - Q123 |

---

## Section A - DC Components & Protocol Basics (Message, Sender, Receiver, Transmission Medium, Protocol)

*Syllabus: DC Components - Message, Sender, Receiver, Transmission Medium, Protocol*

### Q1. The physical path between the sender and receiver is called:

<span lang='hi'>Sender और receiver के बीच का physical path _______ कहलाता है:</span>

- **(A)** Link / link (link) ✅ **(CORRECT)**
- **(B)** Node / node (node)
- **(C)** Segment / सегмент (segment)
- **(D)** Socket / सॉकेट (socket)

**✔ Correct Answer: (A) Link** — In this context, the physical medium of connection between devices is known as a link (the devices connected to it are called nodes).

*Is context में, devices को जोड़ने वाला physical medium link कहलाता है (is से जुड़े devices को nodes कहते हैं).*

**★ Nukta (Key Point):** Note: In Forouzan's 5 components, this same physical path is called the transmission medium. Both terms mean the physical path.

*Note: Forouzan के 5 components में इसी physical path को transmission medium कहा गया है। दोनों का मतलब physical path ही है।*

*[Source: Repo: BCI_SCI Subject Test-7 (UNIT TEST-2 BCI/SCI), Q20] · Easy*

---
### Q2. Identify the five components of a data communication system.

<span lang='hi'>Data communication system के पाँच components की पहचान कीजिए।</span>

- **(A)** Message, Sender, Receiver, Transmission medium, Protocol / Message, Sender, Receiver, Transmission medium, Protocol ✅ **(CORRECT)**
- **(B)** Message, Router, Switch, Cable, Software / Message, Router, Switch, Cable, Software
- **(C)** Data, Sender, Receiver, Hub, TCP/IP / Data, Sender, Receiver, Hub, TCP/IP
- **(D)** Message, Sender, Receiver, Software, Hardware / Message, Sender, Receiver, Software, Hardware

**✔ Correct Answer: (A) Message, Sender, Receiver, Transmission medium, Protocol** — Forouzan lists exactly five components — Message (the information), Sender, Receiver, Transmission medium (the physical path) and Protocol (the rules).

*Forouzan में पाँच components हैं — Message, Sender, Receiver, Transmission medium और Protocol।*

**★ Nukta (Key Point):** 5 components: Message → Sender → Medium → Receiver + Protocol (rules). सबसे favourite exam question.

*5 components: Message → Sender → Medium → Receiver + Protocol (rules)। Exam का favourite question।*

*[Source: Forouzan Ch1 (Q1-1) — Practice Set] · Medium*

---
### Q3. The _______ is the physical path over which a message travels from sender to receiver.

<span lang='hi'>_______ वह physical path है जिस पर message sender से receiver तक जाता है।</span>

- **(A)** Path / पथ
- **(B)** Medium / medium ✅ **(CORRECT)**
- **(C)** Protocol / protocol
- **(D)** Route / रूट (path)

**✔ Correct Answer: (B) Medium** — In data communication, the transmission medium is the physical path (twisted-pair, coaxial, fiber or radio waves) by which the message travels from sender to receiver. (Forouzan)

*Data communication में transmission medium वह physical path है (twisted-pair, coaxial, fiber या radio waves) जिस पर message sender से receiver तक जाता है। (Forouzan)*

**★ Nukta (Key Point):** Medium = physical path between sender and receiver. Remember: Message -> Sender -> Medium -> Receiver.

*Medium = sender और receiver के बीच का physical path. याद रखें: Message -> Sender -> Medium -> Receiver.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q35] · Medium*

---
### Q4. The information to be communicated in a data communication system is called the _______.

<span lang='hi'>Data communication system में communicate की जाने वाली information _______ कहलाती है।</span>

- **(A)** Medium / medium
- **(B)** Protocol / protocol
- **(C)** Message / message (message) ✅ **(CORRECT)**
- **(D)** Transmission / संचरण (transmission)

**✔ Correct Answer: (C) Message** — Forouzan: The message is the data (information) to be communicated. It can be text, numbers, images, audio or video.

*Forouzan: Message = communicate की जाने वाली data (information). यह text, numbers, images, audio या video हो सकती है।*

**★ Nukta (Key Point):** Message = the data/information to be communicated. 5 popular forms: text, numbers, images, audio, video.

*Message = communicate की जाने वाली data. 5 popular forms: text, numbers, images, audio, video.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q38] · Medium*

---
### Q5. Which of the following shares the data of two computers?

<span lang='hi'>निम्नलिखित में से कौन दो computers का data share (साझा) करता है?</span>

- **(A)** Library / पुस्तकालय
- **(B)** Network / network ✅ **(CORRECT)**
- **(C)** Grouping / समूह (grouping)
- **(D)** Integrated system / एकीकृत प्रणाली

**✔ Correct Answer: (B) Network** — A computer network is a set of devices (nodes) connected together mainly to share data, resources and information between computers.

*Computer network = devices (nodes) का ऐसा connection जो mainly computers के बीच data, resources और information share करने के लिए होता है।*

**★ Nukta (Key Point):** Network = 2 or more devices connected to share data/resources.

*Network = 2 या ज़्यादा devices का आपस में जुड़ना, data/resources share करने के लिए।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q13] · Medium*

---
### Q6. _______ refers to two characteristics: when data should be sent and how fast it can be sent.

<span lang='hi'>_______ दो characteristics को बताता है: data कब भेजा जाए और कितनी तेज़ी से भेजा जा सकता है।</span>

- **(A)** Semantics / अर्थ (semantics)
- **(B)** Syntax / संरचना (syntax)
- **(C)** Timing / समय-निर्धारण (timing) ✅ **(CORRECT)**
- **(D)** none of the above / इनमें से कोई नहीं

**✔ Correct Answer: (C) Timing** — The three key elements of a protocol are syntax, semantics and timing. Timing refers to two characteristics: when data should be sent and how fast it can be sent. (Forouzan)

*Protocol के 3 key elements हैं: syntax, semantics और timing. Timing दो characteristics से जुड़ा है: data कब भेजा जाए और कितनी तेज़ी से भेजा जा सकता है। (Forouzan)*

**★ Nukta (Key Point):** Protocol के 3 elements = Syntax (format), Semantics (meaning), Timing (when & how fast).

*Protocol के 3 elements = Syntax (format), Semantics (अर्थ), Timing (कब और कितनी तेज़ी से).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q44] · Medium*

---
### Q7. What are the main elements of a protocol? 1. Syntax  2. Semantics  3. Timing

<span lang='hi'>किसी protocol के मुख्य तत्व (elements) क्या हैं? 1. Syntax  2. Semantics  3. Timing</span>

- **(A)** 1, 2 only / सिर्फ 1 और 2
- **(B)** 1, 3 only / सिर्फ 1 और 3
- **(C)** 2, 3 only / सिर्फ 2 और 3
- **(D)** 1, 2, 3 only / 1, 2 और 3 सभी ✅ **(CORRECT)**

**✔ Correct Answer: (D) 1, 2, 3 only** — A protocol has three key elements: syntax (data format/structure), semantics (meaning of the data) and timing (when to send and how fast).

*Protocol के 3 key elements हैं: syntax (data का format/structure), semantics (data का अर्थ) और timing (कब भेजना है और कितनी तेज़ी से).*

**★ Nukta (Key Point):** याद रखें: Protocol = Syntax + Semantics + Timing.

*याद रखें: Protocol = Syntax + Semantics + Timing.*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q3] · Medium*

---
### Q8. Why are protocols needed in data communication?

<span lang='hi'>Data communication में protocols की आवश्यकता क्यों होती है?</span>

- **(A)** To enable communication between different types of systems by providing common rules / अलग-अलग प्रकार की systems के बीच communication के लिए common rules देना ✅ **(CORRECT)**
- **(B)** To increase the processing speed of the CPU / CPU की processing speed बढ़ाने के लिए
- **(C)** To convert every message into a common language / हर message को एक common language में बदलने के लिए
- **(D)** Protocols are optional — devices can communicate without rules / Protocols optional हैं — बिना rules के भी devices communicate कर सकती हैं

**✔ Correct Answer: (A) To enable communication between different types of systems by providing common rules** — An agreement (protocol) of rules is needed before communication can begin — without common rules, unlike devices cannot understand each other.

*Communication से पहले rules का agreement (protocol) ज़रूरी है — बिना common rules के devices एक-दूसरे को समझ नहीं सकतीं।*

**★ Nukta (Key Point):** Protocol = agreement of rules (syntax + semantics + timing). Iske बिना communication impossible.

*Protocol = rules का agreement (syntax + semantics + timing)। इसके बिना communication impossible है।*

*[Source: Forouzan Ch1 (Q1-11) — Practice Set] · Medium*

---
### Q9. A set of rules that governs data communication is called a:

<span lang='hi'>Data communication को regulate (नियंत्रित) करने वाले rules का set _______ कहलाता है:</span>

- **(A)** rule / नियम (rule)
- **(B)** medium / medium (medium)
- **(C)** Link / link (link)
- **(D)** Protocol / protocol (protocol) ✅ **(CORRECT)**

**✔ Correct Answer: (D) Protocol** — A protocol is a set of rules that governs data communication. It defines what is communicated, how it is communicated and when it is communicated. (Forouzan)

*Protocol = नियमों का set जो data communication को govern करता है. यह बताता है की क्या communicate होगा, कैसे होगा और कब होगा। (Forouzan)*

**★ Nukta (Key Point):** Protocol = rules का set. याद रखें: without a protocol, two devices may be connected but cannot communicate.

*Protocol = नियमों का set. याद रखें: बिना protocol के दो devices जुड़े to हो सकते हैं लेकिन communicate नहीं कर सकते।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3), Q15] · Medium*

---
### Q10. Consider: (1) Twisted pair cables (2) Microwaves and satellite signals (3) Repeaters (4) Analog transmissions (5) Fiber optics. Which of the above is considered as signal transmission medium in data communications?

<span lang='hi'>विचार करें: (1) Twisted pair cables (2) Microwaves और satellite signals (3) Repeaters (4) Analog transmissions (5) Fiber optics। उपरोक्त में से data communications में signal transmission medium के रूप में क्या माना जाता है?</span>

- **(A)** (1) and (5) / (1) और (5)
- **(B)** (1) and (2) / (1) और (2)
- **(C)** (1), (2) and (5) / (1), (2) और (5) ✅ **(CORRECT)**
- **(D)** (1), (2), (3) and (5) / (1), (2), (3) और (5)

**✔ Correct Answer: (C) (1), (2) and (5)** — Twisted pair, microwaves/satellite and fiber optics are transmission media (guided and unguided). A repeater is a device (it regenerates the signal), and analog transmission is a form of signal, not a medium.

*Twisted pair, microwaves/satellite और fiber optics transmission media हैं (guided और unguided). Repeater एक device है (signal regenerate करता है), और analog transmission signal का एक रूप है, medium नहीं।*

**★ Nukta (Key Point):** Guided media: twisted pair, coaxial, fiber. Unguided media: radio, microwave, infrared.

*Guided media: twisted pair, coaxial, fiber. Unguided media: radio, microwave, infrared.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q10] · Medium*

---
### Q11. Data communication is the exchange of _______ between two devices via some form of transmission medium.

<span lang='hi'>Data communication = do devices के बीच _______ का exchange, किसी transmission medium के through।</span>

- **(A)** only text messages / सिर्फ text messages
- **(B)** data (the message) - text, numbers, images, audio or video / data (message) - text, numbers, images, audio या video ✅ **(CORRECT)**
- **(C)** only electrical signals / सिर्फ electrical signals
- **(D)** only hardware devices / सिर्फ hardware devices

**✔ Correct Answer: (B) data (the message) - text, numbers, images, audio or video** — Forouzan: Data communications is the exchange of data between two devices via some form of transmission medium. The data exchanged is called the message.

*Forouzan: Data communications = do devices के बीच किसी transmission medium के through data का exchange. Exchange होने वाले data को message कहते हैं।*

**★ Nukta (Key Point):** Data communication = exchange of DATA (message) between two devices over a medium.

*Data communication = do devices के बीच DATA (message) का exchange, medium के through।*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q12. The device that sends the data message in a data communication system is called the _______.

<span lang='hi'>Data communication system में जो device data message भेजता है, use _______ कहते हैं।</span>

- **(A)** Receiver / Receiver (प्राप्तकर्ता)
- **(B)** Sender / Sender (प्रेषक) ✅ **(CORRECT)**
- **(C)** Protocol / Protocol (protocol)
- **(D)** Hub / Hub (hub)

**✔ Correct Answer: (B) Sender** — The sender is the device (computer, workstation, mobile phone, camera, TV, etc.) that sends the data message.

*Sender वह device है (computer, workstation, mobile phone, camera, TV, आदि) जो data message भेजता है।*

**★ Nukta (Key Point):** Sender = source device; Receiver = destination device.

*Sender = source device; Receiver = destination device.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q13. Which of the following best lists the popular forms of information (message) in data communication?

<span lang='hi'>Data communication में information (message) के popular forms को सबसे achhe से कौन बताता है?</span>

- **(A)** Only text and numbers / सिर्फ text और numbers
- **(B)** Only audio and video / सिर्फ audio और video
- **(C)** Text, numbers, images, audio and video / text, numbers, images, audio और video ✅ **(CORRECT)**
- **(D)** Only binary digits / सिर्फ binary digits

**✔ Correct Answer: (C) Text, numbers, images, audio and video** — Forouzan: The popular forms of information are text, numbers, images, audio, and video.

*Forouzan: Information के popular forms हैं text, numbers, images, audio, और video.*

**★ Nukta (Key Point):** 5 popular forms of message: text, numbers, images, audio, video.

*Message के 5 popular forms: text, numbers, images, audio, video.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q14. ARPANET stands for:

<span lang='hi'>ARPANET का पूरा नाम है:</span>

- **(A)** Advanced Research Projects Agency Network / Advanced Research Projects Agency Network ✅ **(CORRECT)**
- **(B)** Advanced Recheck Projects Agency Internet / Advanced Recheck Projects Agency Internet
- **(C)** American Research Projects Agency Network / American Research Projects Agency Network
- **(D)** Advanced Research Protocol Agency Network / Advanced Research Protocol Agency Network

**✔ Correct Answer: (A) Advanced Research Projects Agency Network** — ARPANET = Advanced Research Projects Agency Network — अमेरिकी रक्षा विभाग की ARPA द्वारा बनाया गया विश्व का पहला packet-switching network.

*ARPANET = Advanced Research Projects Agency Network — अमेरिकी रक्षा विभाग की ARPA द्वारा बनाया गया विश्व का पहला packet-switching network.*

**★ Nukta (Key Point):** This is the network on which TCP/IP was later installed — the grandmother of the Internet.

*यही वह network है जिस पर TCP/IP बाद में लगाया गया — Internet की दादी.*

*[Source: IBPS/SBI computer-awareness banks (via tpointtech & meritnotes)] · Medium*

---
### Q15. In a computer network, nodes are:

<span lang='hi'>Computer network में nodes होते हैं:</span>

- **(A)** the computer that originates the data / जो computer data को originate (shurua) करता है
- **(B)** the computer that routes the data / जो computer data को route करता है
- **(C)** the computer that terminates the data / जो computer data को terminate (समाप्त) करता है
- **(D)** all of the mentioned / उपर्युक्त सभी (all of the above) ✅ **(CORRECT)**

**✔ Correct Answer: (D) all of the mentioned** — A node is any device connected to the network. It can originate (sender), route (router/switch) or terminate (receiver) data, so all of the mentioned is correct.

*Node = network से जुड़ा कोई भी device. यह data को originate (sender), route (router/switch) या terminate (receiver) कर सकता है, इसलिए उपर्युक्त सभी सही हैं।*

**★ Nukta (Key Point):** Node = any connected device of the network (computer, printer, router, etc.).

*Node = network का कोई भी connected device (computer, printer, router, आदि).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q30] · Hard*

---
### Q16. Consider the statements: S1: The physical medium of connection is known as a link. S2: The computers connected to it are known as nodes.

<span lang='hi'>कथनों पर विचार करें: S1: connection का physical medium link कहलाता है। S2: इससे जुड़े computers nodes कहलाते हैं।</span>

- **(A)** Both S1 and S2 are false / दोनों S1 और S2 ग़लत हैं
- **(B)** S1 true but S2 false / S1 सही है लेकिन S2 ग़लत है
- **(C)** S1 false but S2 true / S1 ग़लत है लेकिन S2 सही है
- **(D)** Both S1 and S2 true / दोनों S1 और S2 सही हैं ✅ **(CORRECT)**

**✔ Correct Answer: (D) Both S1 and S2 true** — In networking, the physical medium connecting devices is called a link, and the connected devices (computers) are called nodes. Both statements are true.

*Networking में devices को जोड़ने वाला physical medium link कहलाता है, और जुड़े हुए devices (computers) nodes कहलाते हैं। दोनों कथन सही हैं।*

**★ Nukta (Key Point):** Link = physical medium; Node = connected device (computer).

*Link = physical medium; Node = जुड़ा हुआ device (computer).*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q2] · Hard*

---
### Q17. Which one of the following is NOT one of the five basic components of a data communication system?

<span lang='hi'>निम्नलिखित में से कौन data communication system के five basic components में से एक नहीं है?</span>

- **(A)** Message / Message (message)
- **(B)** Protocol / Protocol (protocol)
- **(C)** Router / Router (router) ✅ **(CORRECT)**
- **(D)** Transmission medium / Transmission medium (medium)

**✔ Correct Answer: (C) Router** — The five basic components are: message, sender, receiver, transmission medium and protocol. A router is a networking device (Network layer), not one of the five fundamental components.

*Five basic components हैं: message, sender, receiver, transmission medium और protocol. Router एक networking device है (Network layer), five fundamental components में से नहीं।*

**★ Nukta (Key Point):** याद रखें 5 components: Message, Sender, Receiver, Transmission Medium, Protocol. Router = device, component नहीं।

*याद रखें 5 components: Message, Sender, Receiver, Transmission Medium, Protocol. Router = device है, component नहीं।*

*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

---

## Section B - Characteristics (Delivery, Accuracy, Timeliness, Jitter) & Criteria (Performance, Reliability, Security)

*Syllabus: Characteristics - Delivery, Accuracy, Timeliness, Jitter | Properties/Criteria - Performance, Reliability, Security*

### Q18. Which physical layer impairment mainly causes jitter in VoIP traffic?

<span lang='hi'>VoIP traffic में jitter का मुख्य kaaran कौन सा physical layer impairment है?</span>

- **(A)** Attenuation / attenuation (signal की shakti कम होना)
- **(B)** Delay variation / delay का अंतर (variation) ✅ **(CORRECT)**
- **(C)** Distortion / distortion (vikriti)
- **(D)** Crosstalk / crosstalk

**✔ Correct Answer: (B) Delay variation** — Jitter is caused by delay variation: packets experience different queuing/transmission delays, so they arrive at uneven intervals, distorting real-time VoIP/video.

*Jitter delay variation से होता है: packets को अलग-अलग queuing/transmission delays milte हैं, इसलिए वह uneven intervals पर pahunchte हैं, जिससे real-time VoIP/video ख़राब होता है।*

**★ Nukta (Key Point):** Jitter = delay variation. Attenuation = signal weakening; distortion = signal shape change; crosstalk = interference from nearby cables.

*Jitter = delay variation. Attenuation = signal की shakti कम होना; distortion = signal का रूप badalna; crosstalk = पास की cables से interference.*

*[Source: Repo: BCI Subject Test-8 (UNIT TEST-3 BCI/SCI), Q36] · Easy*

---
### Q19. What does jitter refer to in data communication?

<span lang='hi'>Data communication में jitter का मतलब क्या होता है?</span>

- **(A)** Loss of data / data का loss
- **(B)** Delay variation in packets / packets में delay का अंतर (variation) ✅ **(CORRECT)**
- **(C)** Data synchronization / data का synchronization
- **(D)** Data encoding / data का encoding

**✔ Correct Answer: (B) Delay variation in packets** — Jitter is the variation in packet arrival time. It is the uneven delay in the delivery of audio or video packets (e.g., video packets sent every 30 ms but arriving with 30 ms and 40 ms delays). (Forouzan)

*Jitter = packets के पहुँचने के समय में अंतर (variation). यह audio या video packets की delivery में uneven delay है (जैसे video packets हर 30 ms पर bheje जाते हैं लेकिन 30 ms और 40 ms के delay से pahunchte हैं). (Forouzan)*

**★ Nukta (Key Point):** Jitter = uneven delay in packet arrival -> distorted audio/video playback.

*Jitter = packet पहुँचने में uneven delay -> audio/video playback ख़राब हो जाती है।*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q1] · Medium*

---
### Q20. Which of the following is a characteristic of data communication?

<span lang='hi'>निम्नलिखित में से कौन data communication की एक characteristic (विशेषता) है?</span>

- **(A)** Timeliness / समयपालन (timeliness) ✅ **(CORRECT)**
- **(B)** Delay / деری (delay)
- **(C)** Speed / गति (speed)
- **(D)** Size / आकार (size)

**✔ Correct Answer: (A) Timeliness** — The four fundamental characteristics of effective data communication are delivery, accuracy, timeliness and jitter. Timeliness means data must be delivered in a timely manner; data delivered late is useless.

*Effective data communication की 4 fundamental characteristics हैं: delivery, accuracy, timeliness और jitter. Timeliness का मतलब है data time पर pahunchna; देर से पहुँचने वाला data बेकार है।*

**★ Nukta (Key Point):** 4 characteristics याद रखो: Delivery, Accuracy, Timeliness, Jitter.

*4 characteristics याद रखो: Delivery, Accuracy, Timeliness, Jitter.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q6] · Medium*

---
### Q21. What is the maximum data rate of a transmission medium known as?

<span lang='hi'>Transmission medium की अधिकतम data rate को क्या कहा जाता है?</span>

- **(A)** Bandwidth / bandwidth ✅ **(CORRECT)**
- **(B)** Throughput / throughput
- **(C)** Latency / latency
- **(D)** Jitter / jitter

**✔ Correct Answer: (A) Bandwidth** — Bandwidth is the maximum data rate (transmission capacity) of a communication channel/medium, usually measured in bits per second (bps).

*Bandwidth = किसी communication channel/medium की अधिकतम data rate (transmission capacity) है, जिसे आम तौर पर bits per second (bps) में मापा जाता है।*

**★ Nukta (Key Point):** Bandwidth = maximum capacity of the channel (in bps). Throughput = actual rate achieved (usually less).

*Bandwidth = channel की अधिकतम capacity (bps में). Throughput = वास्तविक रूप से हासिल होने वाली rate (आम तौर पर कम).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q9] · Medium*

---
### Q22. Speed of an internet connection is measured in:

<span lang='hi'>Internet connection की speed किसमें मापी जाती है?</span>

- **(A)** Kilobits per second (kbps) / Kilobits per second (kbps) ✅ **(CORRECT)**
- **(B)** Kilobytes per second (KB/s) only / केवल Kilobytes per second (KB/s)
- **(C)** Metres per second / Metres per second
- **(D)** Hertz / Hertz

**✔ Correct Answer: (A) Kilobits per second (kbps)** — Data transmission speed (data rate / bandwidth) is measured in bits per second — kbps, Mbps or Gbps — not bytes and not metres.

*Data transmission speed (data rate / bandwidth) bits per second में मापी जाती है — kbps, Mbps या Gbps — bytes में नहीं, metres में नहीं।*

**★ Nukta (Key Point):** Speed = bits per second (bps family). KB/s (bytes) is for file-size/download display — exam answer is kbps.

*Speed = bits per second (bps family)। KB/s (bytes) file-size/download display के लिए है — exam का answer kbps है।*

*[Source: Repo: Unit Test-4 Solution (OCR), p19] · Medium*

---
### Q23. Frequency of failure and network recovery time after a failure are measures of the _______ of a network.

<span lang='hi'>Failure की आवृत्ति (frequency) और failure के बाद network recovery time किस चीज़ के measures हैं?</span>

- **(A)** Performance / performance
- **(B)** Reliability / reliability ✅ **(CORRECT)**
- **(C)** Security / security
- **(D)** Feasibility / feasibility

**✔ Correct Answer: (B) Reliability** — Reliability is measured by the frequency of failure (how often the network fails), the time it takes to recover after a failure, and robustness in a catastrophe. (Forouzan)

*Reliability को failure की frequency (network कितनी बार fail होता है), failure के बाद recover होने का time, और catastrophe में robustness से मापा जाता है। (Forouzan)*

**★ Nukta (Key Point):** Reliability = failure frequency + recovery time + robustness. Performance = transit time, response time, throughput, delay.

*Reliability = failure frequency + recovery time + robustness. Performance = transit time, response time, throughput, delay.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q39] · Medium*

---
### Q24. What is the criteria to check the reliability of a network? 1. Downtime  2. Failure Frequency  3. Fault Tolerance  4. Security

<span lang='hi'>Network की reliability check करने के criteria क्या हैं? 1. Downtime  2. Failure Frequency  3. Fault Tolerance  4. Security</span>

- **(A)** 1, 2, 3 only / सिर्फ 1, 2, 3 ✅ **(CORRECT)**
- **(B)** 2, 3, 4 only / सिर्फ 2, 3, 4
- **(C)** 1, 2, 4 only / सिर्फ 1, 2, 4
- **(D)** 1, 2, 3, 4 only / 1, 2, 3, 4 सभी

**✔ Correct Answer: (A) 1, 2, 3 only** — Reliability is measured by downtime/frequency of failure, recovery time and fault tolerance (robustness). Security is a separate criterion of a network, not a reliability measure.

*Reliability को downtime/failure frequency, recovery time और fault tolerance (robustness) से मापा जाता है। Security एक अलग criterion है, reliability measure नहीं।*

**★ Nukta (Key Point):** 3 network criteria: Performance, Reliability, Security. Reliability = failure frequency + recovery time + fault tolerance.

*3 network criteria: Performance, Reliability, Security. Reliability = failure frequency + recovery time + fault tolerance.*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q1] · Medium*

---
### Q25. What are the three criteria necessary for an effective and efficient network?

<span lang='hi'>Effective और efficient network के लिए आवश्यक तीन criteria क्या हैं?</span>

- **(A)** Performance, Reliability, Security / Performance, Reliability, Security ✅ **(CORRECT)**
- **(B)** Delivery, Accuracy, Timeliness / Delivery, Accuracy, Timeliness
- **(C)** Speed, Cost, Size / Speed, Cost, Size
- **(D)** Message, Sender, Receiver / Message, Sender, Receiver

**✔ Correct Answer: (A) Performance, Reliability, Security** — Forouzan: an effective network must satisfy three criteria — Performance (throughput/delay), Reliability (failure frequency/downtime) and Security (protection from unauthorised access).

*Forouzan: network के तीन criteria — Performance, Reliability और Security।*

**★ Nukta (Key Point):** Network के 3 CRITERIA = Performance, Reliability, Security. Data communication के 4 CHARACTERISTICS = Delivery, Accuracy, Timeliness, Jitter. दोनों को confuse मत करना!

*Network के 3 criteria = Performance, Reliability, Security। Data communication के 4 characteristics = Delivery, Accuracy, Timeliness, Jitter।*

*[Source: Forouzan Ch1 (Q1-2) — Practice Set] · Medium*

---
### Q26. What network property is achieved through the use of the Automatic Repeat reQuest (ARQ) mechanism?

<span lang='hi'>Automatic Repeat reQuest (ARQ) mechanism से network की कौन सी property हासिल होती है?</span>

- **(A)** Reliability / reliability ✅ **(CORRECT)**
- **(B)** Availability / availability
- **(C)** Confidentiality / confidentiality
- **(D)** Scalability / scalability

**✔ Correct Answer: (A) Reliability** — ARQ (Automatic Repeat reQuest) is an error-control mechanism: lost/corrupted frames are retransmitted, so reliable data transfer is achieved. Reliability is thus the property achieved.

*ARQ (Automatic Repeat reQuest) एक error-control mechanism है: khoye/corrupt frames दोबारा bheje जाते हैं, जिससे reliable data transfer होता है। इसलिए reliability property हासिल होती है।*

**★ Nukta (Key Point):** ARQ = error control -> Reliability. Flow control = efficient delivery (no overflow).

*ARQ = error control -> Reliability. Flow control = efficient delivery (receiver का buffer overflow नहीं होना).*

*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)] · Medium*

---
### Q27. For effective data communication, the system must deliver data to the correct destination. This characteristic is called _______.

<span lang='hi'>Effective data communication के लिए system को data सही destination पर पहुँचाना चाहिए। Is characteristic को _______ कहते हैं।</span>

- **(A)** Accuracy / accuracy
- **(B)** Timeliness / timeliness
- **(C)** Delivery / delivery ✅ **(CORRECT)**
- **(D)** Jitter / jitter

**✔ Correct Answer: (C) Delivery** — Delivery: the system must deliver data to the correct destination. Data must be received by the intended device or user and only by that device or user. (Forouzan)

*Delivery: system को data सही destination पर पहुँचाना चाहिए। Data सिर्फ usi intended device/user को pahunchna चाहिए जिस के लिए है। (Forouzan)*

**★ Nukta (Key Point):** 4 characteristics: Delivery (right destination), Accuracy (error-free), Timeliness (on time), Jitter (even delay).

*4 characteristics: Delivery (सही jagah), Accuracy (error-free), Timeliness (time पर), Jitter (even delay).*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q28. Data delivered late is useless (especially in real-time audio/video). Delivering data in a timely manner is called _______.

<span lang='hi'>देर से पहुँचने वाला data बेकार है (ख़ास कर real-time audio/video में)। Time पर data pahunchane को _______ कहते हैं।</span>

- **(A)** Delivery / delivery
- **(B)** Accuracy / accuracy
- **(C)** Timeliness / timeliness ✅ **(CORRECT)**
- **(D)** Jitter / jitter

**✔ Correct Answer: (C) Timeliness** — Timeliness: the system must deliver data in a timely manner. Data delivered late is useless. For video/audio, timely delivery means delivering data as they are produced, in the same order, without significant delay (real-time transmission). (Forouzan)

*Timeliness: system को data time पर पहुँचाना चाहिए। देर से पहुँचने वाला data बेकार है। Video/audio के लिए timely delivery का मतलब है data जिस तरह produce हुए हैं usi तरह, बिना किसी बड़े delay के पहुँचाना (real-time transmission). (Forouzan)*

**★ Nukta (Key Point):** Timeliness = on-time delivery; late data is useless -> real-time transmission (audio/video).

*Timeliness = time पर पहुँचाना; देर वाला data बेकार है -> real-time transmission (audio/video).*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q29. The network criterion measured by transit time, response time, throughput and delay is called _______.

<span lang='hi'>Transit time, response time, throughput और delay से maape jane वाले network criterion को _______ कहते हैं।</span>

- **(A)** Performance / performance ✅ **(CORRECT)**
- **(B)** Reliability / reliability
- **(C)** Security / security
- **(D)** Delivery / delivery

**✔ Correct Answer: (A) Performance** — Performance of a network is measured by transit time (time for a message to travel from one device to another), response time (time between request and response), throughput and delay. (Forouzan)

*Network की performance को transit time (एक device से दूसरे तक message पहुँचने का time), response time (request और response के बीच का time), throughput और delay से मापा जाता है। (Forouzan)*

**★ Nukta (Key Point):** Performance = transit time + response time (throughput & delay are related measures).

*Performance = transit time + response time (throughput और delay isse जुड़े measures हैं).*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q30. Accuracy in data communication means:

<span lang='hi'>Data communication में accuracy का अर्थ है:</span>

- **(A)** Data is sent quickly / data तेज़ी से भेजा जाता है
- **(B)** Data is not corrupted / data corrupted (खराब) नहीं होता ✅ **(CORRECT)**
- **(C)** Data is encrypted / data encrypt होता है
- **(D)** Data reaches the receiver / data receiver तक pahunchta है

**✔ Correct Answer: (B) Data is not corrupted** — Accuracy means the system must deliver the data accurately. Data that has been altered in transmission and left uncorrected is useless.

*Accuracy का मतलब है system data को accurately (सही) पहुँचाए. जो data transmission में बदल गया और सुधारा नहीं गया, बेकार है।*

**★ Nukta (Key Point):** Accuracy = error-free data; altered/corrupted data is useless.

*Accuracy = error-free data; बदल गया/corrupt data बेकार है।*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q8] · Hard*

---
### Q31. An unauthorized user is a network _______ issue.

<span lang='hi'>An unauthorized user एक network _______ issue है.</span>

- **(A)** Performance / performance
- **(B)** Reliability / reliability
- **(C)** Security / security ✅ **(CORRECT)**
- **(D)** All of the above / ऊपर दिए गए सभी

**✔ Correct Answer: (C) Security** — Security means protecting data from unauthorized access, protecting data from damage, and ensuring confidentiality and data integrity. An unauthorized user is a security issue.

*Security का मतलब है data को unauthorized access से bachana, damage से bachana, और confidentiality और data integrity sunishchit करना। Unauthorized user एक security issue है।*

**★ Nukta (Key Point):** Security = unauthorized access से बचाव + confidentiality + integrity (CIA triad).

*Security = unauthorized access से बचाव + confidentiality + integrity (CIA triad).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q40] · Hard*

---
### Q32. Which of the following is NOT one of the three fundamental criteria (properties) that a network must meet?

<span lang='hi'>निम्नलिखित में से कौन network के तीन fundamental criteria (properties) में से एक नहीं है?</span>

- **(A)** Performance / performance
- **(B)** Reliability / reliability
- **(C)** Security / security
- **(D)** Topology / topology ✅ **(CORRECT)**

**✔ Correct Answer: (D) Topology** — Forouzan: a network must meet certain criteria; the most important are performance, reliability, and security. Topology is a structure/arrangement, not one of the three criteria.

*Forouzan: एक network को कुछ criteria पूरे करने चाहिए; सबसे ज़रूरी हैं performance, reliability और security. Topology एक structure/arrangement है, तीन criteria में से नहीं।*

**★ Nukta (Key Point):** Network criteria = 3: Performance, Reliability, Security.

*Network criteria = 3: Performance, Reliability, Security.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

---
### Q33. The capacity of a communication channel is measured in:

<span lang='hi'>Communication channel की क्षमता मापी जाती है:</span>

- **(A)** Bandwidth / Bandwidth ✅ **(CORRECT)**
- **(B)** Bit capacity / Bit capacity
- **(C)** Volume / Volume
- **(D)** Noise / Noise

**✔ Correct Answer: (A) Bandwidth** — A channel's capacity is measured as bandwidth — how many frequencies/bits per second are possible.

*Channel की क्षमता यानी bandwidth मापी जाती है — कितनी आवृत्तियाँ/bits प्रति सेकंड संभव हैं.*

**★ Nukta (Key Point):** Channel capacity ↔ bandwidth (Hz या bps) — यही standard इकाई है.

*Channel capacity ↔ bandwidth (Hz या bps) — यही standard इकाई है.*

*[Source: KVS PGT/TGT/PRT computer banks 2018 (via jagranjosh)] · Hard*

---
### Q34. Consider a 100 Mbps link between an earth station (sender) and a satellite (receiver) at an altitude of 2100 km. The signal propagates at 3×10⁸ m/s. The time taken (in milliseconds, rounded to two decimal places) for the receiver to completely receive a 1000-byte packet transmitted by the sender is ______.

<span lang='hi'>100 Mbps के link पर earth station से 2100 km ऊँचे satellite को 1000-byte packet भेजा गया; signal की speed 3×10⁸ m/s है। Receiver को packet पूरा मिलने में लगा समय (ms में, दो दशमलव) कितना है?</span>

- **(A)** 7.08 / 7.08 ✅ **(CORRECT)**
- **(B)** 2.10 / 2.10
- **(C)** 7.00 / 7.00
- **(D)** 21.08 / 21.08

**✔ Correct Answer: (A) 7.08** — Transmission time = 8000 bits ÷ 10⁸ bps = 0.08 ms; propagation time = 2100×10³ m ÷ 3×10⁸ m/s = 7 ms; total = 7.08 ms — link ki poori latency transmission aur propagation dono ka yog hota hai.

*Transmission time = 8000 ÷ 10⁸ = 0.08 ms; propagation = 2100×10³ ÷ 3×10⁸ = 7 ms; kul = 7.08 ms — dono delay milte hain.*

**★ Nukta (Key Point):** Round-off trap: 2.10 sirf propagation ka fraction pakadta hai; 7.00 transmission time bhool jata hai.

*Round-off jaal: 2.10 sirf propagation; 7.00 mein transmission time chhoot jata hai.*

*[Source: GATE CS 2022] · Hard*

---
### Q35. What is the bit rate for transmitting an uncompressed 800×600 pixel colour frame with 8 bits/pixel at 40 frames per second?

<span lang='hi'>बिना compression के 800×600 pixel वाला colour frame (8 bits/pixel) 40 frames per second पर transmit हो — bit rate कितना होगा?</span>

- **(A)** 2.4 Mbps / 2.4 Mbps
- **(B)** 153.6 Mbps / 153.6 Mbps ✅ **(CORRECT)**
- **(C)** 15.36 Mbps / 15.36 Mbps
- **(D)** 1536 Mbps / 1536 Mbps

**✔ Correct Answer: (B) 153.6 Mbps** — 800×600×8 bits × 40 = 153,600,000 bps = 153.6 Mbps — frame ke total bits ko frame rate se guna karo.

*800×600×8 × 40 = 15,36,00,000 bps = 153.6 Mbps — frame ke bits × frame rate.*

**★ Nukta (Key Point):** Decimal shift jaal: 15.36 aur 1536 bas decimal ki galti hain; 2.4 Mbps sirf pixel count se bina bits aur frames ke nikla hai.

*Decimal ki galtiyan: 15.36/1536; 2.4 Mbps bits aur frames bhool kar aata hai.*

*[Source: KVS PGT Computer Science 2017] · Hard*

---
### Q36. An analog signal carries 4 bits in each signal unit. If 1000 signal units are sent per second, then the baud rate and bit rate of the signal are ______ and ______.

<span lang='hi'>एक analog signal हर signal unit में 4 bits रखता है। 1000 signal units per second भेजे जाएँ तो signal की baud rate और bit rate क्रमशः कितनी होगी?</span>

- **(A)** 4000 bauds/sec, 4000 bps / 4000 bauds/sec, 4000 bps
- **(B)** 1000 bauds/sec, 1000 bps / 1000 bauds/sec, 1000 bps
- **(C)** 4000 bauds/sec, 1000 bps / 4000 bauds/sec, 1000 bps
- **(D)** 1000 bauds/sec, 4000 bps / 1000 bauds/sec, 4000 bps ✅ **(CORRECT)**

**✔ Correct Answer: (D) 1000 bauds/sec, 4000 bps** — Baud rate = signal units per second = 1000 bauds; bit rate = baud × bits per unit = 1000×4 = 4000 bps — baud rate signalling speed hai, bit rate data speed.

*Baud rate = 1000 signals/sec = 1000 bauds; bit rate = 1000×4 = 4000 bps — baud signal ki speed, bit rate data ki.*

**★ Nukta (Key Point):** Dono ko same mat samjho: 4000 bauds/4000 bps confusion hai; 4000 bauds/1000 bps ulta ratio hai.

*Dono alag hain: 4000/4000 confusion; 4000/1000 ulta hai.*

*[Source: KVS PGT Computer Science 2017] · Hard*

---

## Section C - Transmission Mode (Direction of Data Flow: Simplex, Half-Duplex, Full-Duplex)

*Syllabus: Transmission Mode - Simplex, Half-Duplex, Full-Duplex*

### Q37. Communication between a computer and a keyboard involves ______________ transmission.

<span lang='hi'>Computer और keyboard के बीच communication में ______________ transmission होता है।</span>

- **(A)** Automatic / automatic
- **(B)** Half-duplex / half-duplex
- **(C)** Half-duplex (variant) / half-duplex
- **(D)** Simplex / simplex ✅ **(CORRECT)**

**✔ Correct Answer: (D) Simplex** — A keyboard only sends data to the computer; the computer does not send data back to the keyboard. So the communication is unidirectional = simplex.

*Keyboard सिर्फ computer को data भेजता है; computer keyboard को data wapas नहीं भेजता. इसलिए communication एक ही direction में है = simplex.*

**★ Nukta (Key Point):** Keyboard -> Computer = simplex (one way). Examples: keyboard-monitor, TV broadcast.

*Keyboard -> Computer = simplex (एक तरफ़). Examples: keyboard-monitor, TV broadcast.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q33] · Medium*

---
### Q38. A television broadcast is an example of _______ transmission.

<span lang='hi'>Television broadcast _______ transmission का एक example है।</span>

- **(A)** simplex / simplex ✅ **(CORRECT)**
- **(B)** half-duplex / half-duplex
- **(C)** full-duplex / full-duplex
- **(D)** automatic / automatic

**✔ Correct Answer: (A) simplex** — TV broadcast is unidirectional: the TV station only transmits and the TV set only receives. One direction only = simplex.

*TV broadcast एक direction का है: TV station सिर्फ transmit करता है और TV set सिर्फ receive करता है। Ek ही direction = simplex.*

**★ Nukta (Key Point):** TV/radio broadcast = simplex (station -> TV only, wapas नहीं).

*TV/radio broadcast = simplex (station -> TV ही, wapas नहीं).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q41] · Medium*

---
### Q39. What is the mode of transmission where data flows in only one direction?

<span lang='hi'>Wo transmission mode kaunsa है जिसमें data सिर्फ एक direction में flow करता है?</span>

- **(A)** Simplex / simplex ✅ **(CORRECT)**
- **(B)** Half-Duplex / half-duplex
- **(C)** Full-Duplex / full-duplex
- **(D)** Multiplex / multiplex

**✔ Correct Answer: (A) Simplex** — Simplex: communication is unidirectional, like a one-way street. Only one of the two devices on a link can transmit; the other can only receive. (Forouzan)

*Simplex: communication एक ही direction का होता है, जैसे one-way street. Link के दो devices में से सिर्फ एक transmit कर सकता है; दूसरा सिर्फ receive करता है। (Forouzan)*

**★ Nukta (Key Point):** Simplex = one-way only (keyboard to monitor, TV broadcast).

*Simplex = सिर्फ एक तरफ़ (keyboard to monitor, TV broadcast).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q3] · Medium*

---
### Q40. Which transmission mode is used in walkie-talkie communication?

<span lang='hi'>Walkie-talkie communication में कौन सा transmission mode use होता है?</span>

- **(A)** Simplex / simplex
- **(B)** Half-Duplex / half-duplex ✅ **(CORRECT)**
- **(C)** Full-Duplex / full-duplex
- **(D)** Multiplex / multiplex

**✔ Correct Answer: (B) Half-Duplex** — A walkie-talkie is the classic example of half-duplex: both sides can talk, but only one at a time (push-to-talk). (Forouzan)

*Walkie-talkie half-duplex का classic example है: दोनों तरफ़ baat कर सकते हैं, लेकिन एक समय में सिर्फ एक (push-to-talk). (Forouzan)*

**★ Nukta (Key Point):** Walkie-talkie = half-duplex (push-to-talk, एक समय में एक ही bolega).

*Walkie-talkie = half-duplex (push-to-talk, एक समय में एक ही bolega).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q10] · Medium*

---
### Q41. Which of the following statements are TRUE?
1. Hubs operate in Half-Duplex mode.
2. Switches operate in Full-Duplex mode.
3. Routers broadcast by default.

<span lang='hi'>निम्नलिखित में से कौन से statements TRUE हैं?
1. Hubs Half-Duplex mode में काम करते हैं।
2. Switches Full-Duplex mode में काम करते हैं।
3. Routers by default broadcast करते हैं।</span>

- **(A)** 1 and 2 / 1 और 2 ✅ **(CORRECT)**
- **(B)** 2 and 3 / 2 और 3
- **(C)** 1 and 3 / 1 और 3
- **(D)** 1, 2 and 3 / 1, 2 और 3

**✔ Correct Answer: (A) 1 and 2** — Statement 1 TRUE: a hub shares one collision domain and works in half-duplex. Statement 2 TRUE: a switch gives each port its own collision domain and supports full-duplex. Statement 3 FALSE: routers do NOT forward broadcasts by default (each router port = separate broadcast domain).

*Statement 1 TRUE: hub एक collision domain share करता है, Half-Duplex में काम करता है। Statement 2 TRUE: switch हर port को अलग collision domain देता है, Full-Duplex support करता है। Statement 3 FALSE: routers by default broadcasts forward नहीं करते।*

**★ Nukta (Key Point):** Hub = half-duplex + एक collision domain; Switch = full-duplex + per-port collision domain; Router = broadcasts rokta है.

*Hub = Half-Duplex + एक collision domain; Switch = Full-Duplex + per-port collision domain; Router = broadcasts रोकता है।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

---
### Q42. Which of the following transmission directions listed is not a legitimate channel?

<span lang='hi'>निम्नलिखित में से कौन सा transmission direction एक legitimate (vaidh) channel नहीं है?</span>

- **(A)** Simplex / simplex
- **(B)** Half Duplex / half duplex
- **(C)** Full Duplex / full duplex
- **(D)** Double Duplex / double duplex ✅ **(CORRECT)**

**✔ Correct Answer: (D) Double Duplex** — The three legitimate directions of data flow are simplex (one way only), half-duplex (both ways, one at a time) and full-duplex (both ways simultaneously). Double duplex is not a stअंदरd term.

*Data flow के तीन legitimate directions हैं: simplex (एक ही तरफ़), half-duplex (दोनों तरफ़, एक समय में एक), full-duplex (दोनों तरफ़, एक साथ). Double duplex कोई stअंदरd term नहीं है।*

**★ Nukta (Key Point):** 3 transmission modes: Simplex, Half-Duplex, Full-Duplex. Double duplex = गलत.

*3 transmission modes: Simplex, Half-Duplex, Full-Duplex. Double duplex = गलत है।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q3] · Hard*

---
### Q43. What is the difference between half-duplex and full-duplex transmission modes?

<span lang='hi'>Half-Duplex और Full-Duplex transmission modes में अंतर क्या है?</span>

- **(A)** Half-duplex allows only one-way flow; full-duplex also allows only one-way flow / Half-Duplex में सिर्फ one-way flow; Full-Duplex में भी सिर्फ one-way flow
- **(B)** Half-duplex flows both ways one direction at a time; full-duplex flows both ways at the same time / Half-Duplex में data दोनों तरफ़ पर एक समय में एक direction; Full-Duplex में एक साथ दोनों तरफ़ ✅ **(CORRECT)**
- **(C)** Half-duplex is only for wireless; full-duplex only for wired networks / Half-Duplex सिर्फ wireless के लिए; Full-Duplex सिर्फ wired के लिए
- **(D)** There is no difference between the two / दोनों में कोई अंतर नहीं है

**✔ Correct Answer: (B) Half-duplex flows both ways one direction at a time; full-duplex flows both ways at the same time** — Half-duplex = both directions, one at a time (walkie-talkie). Full-duplex = both directions simultaneously (telephone).

*Half-Duplex = दोनों direction, पर एक समय में एक (walkie-talkie)। Full-Duplex = एक साथ दोनों direction (telephone)।*

**★ Nukta (Key Point):** Half = एक time पर एक ही side (walkie-talkie). Full = दोनों side एक साथ (telephone).

*Half = एक समय में एक side (walkie-talkie)। Full = दोनों side एक साथ (telephone)।*

*[Source: Forouzan Ch1 (Q1-6) — Practice Set] · Hard*

---
### Q44. Data flow between two devices can occur in a _______ way.

<span lang='hi'>Do devices के बीच data flow _______ tareeke से हो सकता है।</span>

- **(A)** simplex / simplex
- **(B)** half-duplex / half-duplex
- **(C)** full-duplex / full-duplex
- **(D)** all of the above / ऊपर दिए गए सभी ✅ **(CORRECT)**

**✔ Correct Answer: (D) all of the above** — Data flow between two devices can be simplex (one way), half-duplex (both ways, one at a time) or full-duplex (both ways at the same time). Hence all of the above.

*Do devices के बीच data flow simplex (एक तरफ़), half-duplex (दोनों तरफ़, एक समय में एक) या full-duplex (दोनों तरफ़, एक साथ) हो सकता है। इसलिए ऊपर सभी सही हैं।*

**★ Nukta (Key Point):** 3 ways of data flow: simplex, half-duplex, full-duplex.

*Data flow के 3 tareeke: simplex, half-duplex, full-duplex.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q45] · Hard*

---
### Q45. In a telephone conversation, both persons can speak and hear each other at the same time. This is an example of _______.

<span lang='hi'>Telephone conversation में दोनों persons एक साथ bol और sun सकते हैं। यह _______ का example है।</span>

- **(A)** Simplex / simplex
- **(B)** Half-duplex / half-duplex
- **(C)** Full-duplex / full-duplex ✅ **(CORRECT)**
- **(D)** Unicast / unicast

**✔ Correct Answer: (C) Full-duplex** — Full-duplex: both stations can transmit and receive simultaneously. The telephone network is Forouzan's example of full-duplex.

*Full-duplex: दोनों stations एक साथ transmit और receive कर सकते हैं। Telephone network full-duplex का Forouzan का example है।*

**★ Nukta (Key Point):** Telephone = full-duplex (दोनों एक साथ bol और sun सकते हैं).

*Telephone = full-duplex (दोनों एक साथ bol और sun सकते हैं).*

*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

---

## Section D - Network Structure / Topology (Physical: Mesh, Star, Bus, Ring, Others; Logical: IEEE 802)

*Syllabus: Physical Topology - Mesh, Star, Bus, Ring, Others (Hybrid, Tree) | Logical Topology - IEEE 802*

### Q46. IEEE 802.2 stअंदरd is related to which sub-layer?

<span lang='hi'>IEEE 802.2 stअंदरd किस sub-layer से संबंधित है?</span>

- **(A)** MAC Sublayer / MAC Sublayer
- **(B)** LLC Sublayer / LLC Sublayer ✅ **(CORRECT)**
- **(C)** Physical Layer / Physical Layer
- **(D)** Network Layer / Network Layer

**✔ Correct Answer: (B) LLC Sublayer** — IEEE 802.2 defines the Logical Link Control (LLC) sub-layer of the Data Link layer; the MAC sub-layer is defined by IEEE 802.3 (Ethernet).

*IEEE 802.2 Data Link layer का LLC (Logical Link Control) sub-layer define करता है; MAC sub-layer IEEE 802.3 (Ethernet) से जुड़ा है।*

**★ Nukta (Key Point):** 802.2 = LLC (upper sub-layer of Data Link). 802.3 = Ethernet/MAC, 802.5 = Token Ring, 802.11 = Wi-Fi.

*802.2 = LLC। 802.3 = Ethernet/MAC, 802.5 = Token Ring, 802.11 = Wi-Fi।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q47. What are the advantages of star topology?

<span lang='hi'>Star topology के क्या advantages (लाभ) हैं?</span>

- **(A)** Less number of cables are required / कम number में cables चाहिए ✅ **(CORRECT)**
- **(B)** More number of cables are required / ज़्यादा number में cables चाहिए
- **(C)** It is a distributed topology / यह एक distributed topology है
- **(D)** Security is high / security ज़्यादा है

**✔ Correct Answer: (A) Less number of cables are required** — In a star topology, each device has a dedicated point-to-point link only to a central hub, so far fewer cables are required than in a mesh. It is also easy to install and reconfigure.

*Star topology में हर device का सिर्फ central hub से dedicated point-to-point link होता है, इसलिए mesh की tulna में kaafi कम cables चाहिए. इसे install और reconfigure करना भी आसान है।*

**★ Nukta (Key Point):** Star = hub at centre, dedicated links, fewer cables (vs mesh), easy to install. But if hub fails, whole network goes down.

*Star = centre में hub, dedicated links, कम cables (mesh के muqable), install करना आसान. लेकिन hub fail हो गया toh पूरा network band हो जाता है।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q1] · Medium*

---
### Q48. Which type of topology is best suited for large businesses which must carefully control and coordinate the operation of distributed branch outlets?

<span lang='hi'>Large businesses के लिए कौन सी topology सबसे उपयुक्त है, jahan distributed branch outlets के operation को carefully control और coordinate करना हो?</span>

- **(A)** Ring / ring
- **(B)** Local area / local area
- **(C)** Hierarchical / hierarchical (tree) ✅ **(CORRECT)**
- **(D)** Star / star

**✔ Correct Answer: (C) Hierarchical** — A hierarchical (tree) topology is best for large organisations with distributed branch outlets because it is a hierarchy of stars and allows central control and coordination at each level.

*Hierarchical (tree) topology large organisations के लिए सबसे उपयुक्त है jahan distributed branch outlets hon, क्योंकि यह stars की hierarchy है और हर level पर central control/coordination की अनुमति देती है।*

**★ Nukta (Key Point):** Tree = hierarchical star. Large orgs with branches -> hierarchical/tree topology.

*Tree = hierarchical star. Badi sansthaon में branches के लिए -> hierarchical/tree topology.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q2] · Medium*

---
### Q49. In a traditional ring network, repeaters are particularly associated with which topology because each station can regenerate and forward the signal?

<span lang='hi'>पारंपरिक ring network में repeaters किस topology से विशेष रूप से जुड़े हैं, क्योंकि हर station signal को regenerate और आगे भेज सकता है?</span>

- **(A)** Ring topology / Ring topology ✅ **(CORRECT)**
- **(B)** Mesh topology / Mesh topology
- **(C)** Bus topology / Bus topology
- **(D)** Star topology / Star topology

**✔ Correct Answer: (A) Ring topology** — In a classic/traditional ring, each station commonly regenerates (repeats) the incoming signal before passing it to the next station — repeaters are thus built into the ring model.

*पारंपरिक ring में हर station आने वाले signal को अगले station को देने से पहले regenerate (repeat) करता है — इसलिए ring model में repeaters अंतर्निहित हैं।*

**★ Nukta (Key Point):** Concept-check correction of the old "repeater is used in ___ topology" stem (that wording wrongly implied repeaters are exclusive to one topology). Repeaters are Physical-layer devices usable on many links; the "traditional ring network" qualifier keeps the intended textbook answer (Ring) without the false universal claim. Not a verified PYQ.

*पुराने "repeater किस topology में" वाले प्रश्न का सुधार — repeater Physical-layer device है, हर link पर चलता है; "पारंपरिक ring" जोड़ने से अभीष्ट उत्तर (Ring) बना रहता है। यह सत्यापित PYQ नहीं है।*

*[Source: Practice — original (concept-check correction — not a verified PYQ)] · Medium*

---
### Q50. What type of topology connects each node in a closed loop?

<span lang='hi'>कौन सी topology हर node को एक closed loop में जोड़ती है?</span>

- **(A)** Star / star
- **(B)** Mesh / mesh
- **(C)** Ring / ring ✅ **(CORRECT)**
- **(D)** Bus / bus

**✔ Correct Answer: (C) Ring** — In a ring topology, each device is connected to its two neighbours (one on each side), forming a closed loop. Data travels in one direction and each device regenerates the signal (token passing).

*Ring topology में हर device अपने दोनों neighbours से जुड़ा होता है (एक दोनों तरफ़), जिससे एक closed loop बनता है। Data एक ही direction में जाता है और हर device signal को regenerate करता है (token passing).*

**★ Nukta (Key Point):** Ring = closed loop, one direction, token passing, each device = repeater.

*Ring = closed loop, एक direction, token passing, हर device = repeater.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q4] · Medium*

---
### Q51. In a _______ topology, every device has a dedicated point-to-point link to every other device. For n devices, the number of links is n(n-1)/2 and each device needs n-1 I/O ports.

<span lang='hi'>_______ topology में हर device का हर दूसरे device से dedicated point-to-point link होता है। n devices के लिए links की संख्या n(n-1)/2 होती है और हर device को n-1 I/O ports चाहिए।</span>

- **(A)** Bus / bus
- **(B)** Star / star
- **(C)** Ring / ring
- **(D)** Mesh / mesh ✅ **(CORRECT)**

**✔ Correct Answer: (D) Mesh** — Mesh: every device has a dedicated point-to-point link to every other device. Number of links = n(n-1)/2; each device needs n-1 I/O ports. (Forouzan)

*Mesh: हर device का हर दूसरे device से dedicated point-to-point link होता है। Links की संख्या = n(n-1)/2; हर device को n-1 I/O ports चाहिए। (Forouzan)*

**★ Nukta (Key Point):** Mesh formula (EXAM favourite): links = n(n-1)/2, ports per device = n-1. E.g., 5 devices -> 10 links.

*Mesh formula (EXAM favourite): links = n(n-1)/2, हर device के ports = n-1. Jaise 5 devices -> 10 links.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q52. In a _______ topology, each device has a dedicated point-to-point link only to a central controller, usually called a hub (or switch).

<span lang='hi'>_______ topology में हर device का सिर्फ एक central controller (hub/switch) से dedicated point-to-point link होता है।</span>

- **(A)** Mesh / mesh
- **(B)** Ring / ring
- **(C)** Star / star ✅ **(CORRECT)**
- **(D)** Bus / bus

**✔ Correct Answer: (C) Star** — Star: each device has a dedicated point-to-point link only to a central controller, usually called a hub. The hub relays frames to the destination. (Forouzan)

*Star: हर device का सिर्फ एक central controller (usually hub) से dedicated point-to-point link होता है। Hub frames को destination तक relay करता है। (Forouzan)*

**★ Nukta (Key Point):** Star = hub/switch at centre; easy to install & reconfigure; but if hub fails, the WHOLE network goes down.

*Star = centre में hub/switch; install और reconfigure करना आसान; लेकिन hub fail हो गया तो पूरा network बंद हो जाता है।*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q53. Which network topology requires a multipoint connection?

<span lang='hi'>किस network topology में multipoint connection की आवश्यकता होती है?</span>

- **(A)** Ring / Ring
- **(B)** Bus / Bus ✅ **(CORRECT)**
- **(C)** Star / Star
- **(D)** Mesh / Mesh

**✔ Correct Answer: (B) Bus** — In a bus topology one long cable acts as a backbone and three or more devices share it — a multipoint connection. Mesh, star and ring use point-to-point links.

*Bus topology में एक long cable backbone बनती है और तीन+ devices उसे share करती हैं — यही multipoint connection है। Mesh, star, ring point-to-point links use करते हैं।*

**★ Nukta (Key Point):** Bus = multipoint (shared backbone). Mesh/Star/Ring = point-to-point links. Yahi difference exam में poochha जाता है.

*Bus = multipoint (shared backbone)। Mesh/Star/Ring = point-to-point links।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

---
### Q54. In a _______ topology, each device is connected to its two neighbours, data travels in one direction around the loop, and each device regenerates (repeats) the signal - this is called token passing.

<span lang='hi'>_______ topology में हर device अपने दो neighbours से जुड़ा होता है, data loop में एक ही direction में जाता है, और हर device signal को regenerate (repeat) करता है - इसे token passing कहते हैं।</span>

- **(A)** Bus / bus
- **(B)** Ring / ring ✅ **(CORRECT)**
- **(C)** Star / star
- **(D)** Mesh / mesh

**✔ Correct Answer: (B) Ring** — Ring: each device is connected to its two neighbours. Data travels in one direction. Each device in the ring incorporates a repeater; it regenerates the bits and passes them along. Access is typically by token passing. (Forouzan)

*Ring: हर device अपने दो neighbours से जुड़ा होता है। Data एक ही direction में जाता है। Ring का हर device एक repeater की तरह काम करता है; यह bits को regenerate करके आगे pass करता है। Access आम तौर पर token passing से होता है। (Forouzan)*

**★ Nukta (Key Point):** Ring = loop, one direction, token passing, each device = repeater.

*Ring = loop, एक direction, token passing, हर device = repeater.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q55. A network in which two or more different topologies are combined (e.g., a star connected to another star) is called a _______ topology, while a _______ topology is a hierarchy of stars (a variation of the star topology).

<span lang='hi'>जिसमें do या ज़्यादा अलग topologies combine हो (जैसे एक star दूसरे star से जुड़ा हो), use _______ topology कहते हैं, और _______ topology stars की hierarchy है (star topology का variation).</span>

- **(A)** Hybrid ; Tree / hybrid ; tree ✅ **(CORRECT)**
- **(B)** Tree ; Hybrid / tree ; hybrid
- **(C)** Mesh ; Ring / mesh ; ring
- **(D)** Bus ; Star / bus ; star

**✔ Correct Answer: (A) Hybrid ; Tree** — Hybrid = a combination of two or more different topologies (e.g., a star of stars). Tree = a hierarchical arrangement of stars, a variation of the star topology.

*Hybrid = do या ज़्यादा अलग topologies का combination है (जैसे star of stars). Tree = stars की hierarchical arrangement है, star topology का एक variation.*

**★ Nukta (Key Point):** Hybrid = mix of topologies; Tree = star of stars (hierarchical star).

*Hybrid = topologies का mix; Tree = star of stars (hierarchical star).*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q56. Hierarchical topology, used to establish a network, is also known as a:

<span lang='hi'>Hierarchical topology, जिससे network स्थापित किया जाता है, किस नाम से भी जानी जाती है?</span>

- **(A)** Bus network / Bus network
- **(B)** Star network / Star network
- **(C)** Tree network / Tree network ✅ **(CORRECT)**
- **(D)** Mesh network / Mesh network

**✔ Correct Answer: (C) Tree network** — A hierarchical (tree) topology connects groups of computers to a central computer (root/hub) and then links those groups in a tree-like structure — a star of stars.

*Hierarchical (tree) topology computers के groups को एक central computer (root/hub) से जोड़ती है, और फिर उन groups को tree जैसी structure में जोड़ती है — star of stars।*

**★ Nukta (Key Point):** Hierarchical = Tree = star-of-stars (root + branches). Used in big office/campus LANs.

*Hierarchical = Tree = star-of-stars (root + branches)। बड़े office/campus LANs में use होती है।*

*[Source: Repo: Unit Test-4 Solution (OCR), p17] · Medium*

---
### Q57. The ______ topology of a network defines how the devices are physically laid out/connected, whereas the ______ topology defines how the data actually flow / how the devices access the network to transmit.

<span lang='hi'>Network की _______ topology बताती है की devices physically कैसे जुड़े हैं, jabki _______ topology बताती है की data asal में कैसे flow करता है / devices transmit करने के लिए network को कैसे access करते हैं।</span>

- **(A)** Logical ; Physical / logical ; physical
- **(B)** Physical ; Logical / physical ; logical ✅ **(CORRECT)**
- **(C)** Star ; Bus / star ; bus
- **(D)** Mesh ; Ring / mesh ; ring

**✔ Correct Answer: (B) Physical ; Logical** — Physical topology = the actual layout of devices and cables. Logical topology = the way data flows / how devices access the medium. Two networks can have the same logical topology but different physical topologies.

*Physical topology = devices और cables का वास्तविक layout. Logical topology = data कैसे flow करता है / devices medium को कैसे access करते हैं। दो networks की logical topology same हो सकती है लेकिन physical अलग हो सकती है।*

**★ Nukta (Key Point):** Physical = कैसे जुड़े (cables); Logical = data कैसे flow करता है (access). Same logical, different physical possible.

*Physical = कैसे जुड़े (cables); Logical = data कैसे flow करता है (access). Same logical, different physical हो सकता है।*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q58. Which physical topology offers the highest robustness (fault tolerance) because of multiple redundant paths, but is also the most expensive and hardest to install because of the huge amount of cabling?

<span lang='hi'>कौन सी physical topology सबसे ज़्यादा robust (fault tolerant) है क्योंकि ismein कई redundant paths होते हैं, लेकिन सबसे महंगी और install करने में सबसे मुश्किल भी है क्योंकि बहुत ज़्यादा cabling चाहिए?</span>

- **(A)** Bus / bus
- **(B)** Ring / ring
- **(C)** Star / star
- **(D)** Mesh / mesh ✅ **(CORRECT)**

**✔ Correct Answer: (D) Mesh** — Mesh has a dedicated link between every pair of devices, so the failure of one link does not affect the others - it is the most robust. But n(n-1)/2 links make it the most expensive and hardest to install/wire.

*Mesh में हर pair of devices के बीच dedicated link होता है, इसलिए एक link fail होने से दूसरे affected नहीं होते - यह सबसे robust है। लेकिन n(n-1)/2 links की वजह से यह सबसे महंगी और install करने में सबसे मुश्किल है।*

**★ Nukta (Key Point):** Mesh = most robust + most costly (n(n-1)/2 cables). Star = cheap & easy but hub is a single point of failure. Bus = cheapest, hardest fault isolation.

*Mesh = सबसे robust + सबसे महंगी (n(n-1)/2 cables). Star = sasti और आसान लेकिन hub single point of failure है. Bus = सबसे sasti, fault isolation सबसे मुश्किल.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q59. Which one of the following is not a network topology?

<span lang='hi'>निम्नलिखित में से कौन एक network topology नहीं है?</span>

- **(A)** Star / star
- **(B)** Ring / ring
- **(C)** Bus / bus
- **(D)** Peer to Peer / peer to peer ✅ **(CORRECT)**

**✔ Correct Answer: (D) Peer to Peer** — Star, ring and bus are physical topologies. Peer-to-peer is a network architecture (how devices share resources), not a topology.

*Star, ring और bus physical topologies हैं। Peer-to-peer एक network architecture है (devices कैसे resources share karenge), topology नहीं।*

**★ Nukta (Key Point):** Topologies = mesh, star, bus, ring, hybrid, tree. P2P = architecture (not topology).

*Topologies = mesh, star, bus, ring, hybrid, tree. P2P = architecture है (topology नहीं).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q9] · Hard*

---
### Q60. For n devices in a network, how many cable links are required in a mesh topology?

<span lang='hi'>Network में n devices के लिए mesh topology में कितने cable links चाहिए?</span>

- **(A)** n / n
- **(B)** n - 1 / n - 1
- **(C)** n(n - 1)/2 / n(n - 1)/2 ✅ **(CORRECT)**
- **(D)** n(n - 1) / n(n - 1)

**✔ Correct Answer: (C) n(n - 1)/2** — In a mesh every device has a dedicated point-to-point link to every other device, so links = n(n-1)/2 (each link is shared by two devices).

*Mesh में हर device का हर दूसरे device तक dedicated point-to-point link होता है, इसलिए links = n(n-1)/2।*

**★ Nukta (Key Point):** Mesh cables = n(n-1)/2, ports/device = n-1. Star = n cables. Ring = n. Bus = 1 backbone.

*Mesh cables = n(n-1)/2, ports/device = n-1। Star = n। Ring = n। Bus = 1।*

*[Source: Forouzan Ch1 (Q1-8) — Practice Set] · Hard*

---
### Q61. Six devices are arranged in a mesh topology. How many cables are needed, and how many ports does each device need?

<span lang='hi'>छह devices को mesh topology में जोड़ा गया है। कितनी cables चाहिए और हर device को कितने ports चाहिए?</span>

- **(A)** 15 cables, 5 ports each / 15 cables, हर device पर 5 ports ✅ **(CORRECT)**
- **(B)** 30 cables, 6 ports each / 30 cables, हर device पर 6 ports
- **(C)** 15 cables, 6 ports each / 15 cables, हर device पर 6 ports
- **(D)** 6 cables, 5 ports each / 6 cables, हर device पर 5 ports

**✔ Correct Answer: (A) 15 cables, 5 ports each** — Links = n(n-1)/2 = 6×5/2 = 15 cables. Each device connects to the other 5 devices, so each needs n-1 = 5 ports.

*Links = n(n-1)/2 = 6×5/2 = 15 cables। हर device बाकी 5 devices से जुड़ता है, इसलिए ports = 5।*

**★ Nukta (Key Point):** Mesh formula: cables = n(n-1)/2, ports/device = n-1. Numerical में हमेशा yahi do numbers maange जाते हैं.

*Mesh: cables = n(n-1)/2, ports/device = n-1। Numerical में यही दो numbers पूछे जाते हैं।*

*[Source: Forouzan Ch1 (P1-3) — Practice Set (Problem)] · Hard*

---
### Q62. If a computer network cable breaks, the whole network goes down in which topology?

<span lang='hi'>यदि computer network cable टूट जाए, तो किस topology में पूरा network बंद हो जाता है?</span>

- **(A)** Star / Star
- **(B)** Ring / Ring ✅ **(CORRECT)**
- **(C)** Mesh / Mesh
- **(D)** All of these / ये सभी

**✔ Correct Answer: (B) Ring** — In a Ring topology every device is connected to its two neighbours in a closed loop — one cable break opens the ring, so the whole network goes down.

*Ring topology में हर device अपने दो neighbours से बंद loop में जुड़ा होता है — एक cable टूटने से ring खुल जाती है, इसलिए पूरा network बंद हो जाता है।*

**★ Nukta (Key Point):** Ring = one break downs ALL. Star = only that device drops. Mesh = network survives (many paths).

*Ring = एक break से सब down। Star = सिर्फ वह device गिरता है। Mesh = network बच जाता है (कई paths)।*

*[Source: Repo: Unit Test-4 Solution (OCR), p16] · Hard*

---
### Q63. In which topology does the failure of a single cable or device NOT affect the rest of the network?

<span lang='hi'>किस topology में एक cable या device के fail होने पर बाकी network प्रभावित नहीं होता?</span>

- **(A)** Bus / Bus
- **(B)** Ring / Ring
- **(C)** Star / Star
- **(D)** Mesh / Mesh ✅ **(CORRECT)**

**✔ Correct Answer: (D) Mesh** — In a mesh, redundant links exist — if one link/device fails, traffic takes another path, so the rest of the network keeps working. In bus/ring a cable failure breaks the whole network; in star the hub is a single point of failure.

*Mesh में redundant links होती हैं — एक link/device fail होने पर traffic दूसरे रास्ते से चलता है। Bus/ring में cable failure पूरा network तोड़ देता है; star में hub single point of failure है।*

**★ Nukta (Key Point):** Mesh = most fault-tolerant (redundant paths) — इसलिए 'highest robustness' mesh में होती है.

*Mesh = सबसे ज़्यादा fault-tolerant (redundant paths) — इसीलिए mesh most robust है।*

*[Source: Forouzan Ch1 (P1-4) — Practice Set (Problem)] · Hard*

---
### Q64. In a _______ topology, one long cable acts as a backbone to link all the devices; devices connect via drop lines and taps, and terminators are needed at both ends of the backbone.

<span lang='hi'>_______ topology में एक लंबा cable backbone की तरह सभी devices को जोड़ता है; devices drop lines और taps से connect होते हैं, और backbone के दोनों ends पर terminators चाहिए।</span>

- **(A)** Bus / bus ✅ **(CORRECT)**
- **(B)** Star / star
- **(C)** Ring / ring
- **(D)** Mesh / mesh

**✔ Correct Answer: (A) Bus** — Bus: one long cable acts as a backbone to link all the devices. Nodes are connected to the bus cable by drop lines and taps. Terminators at both ends absorb the signal to prevent reflection. (Forouzan)

*Bus: एक लंबा cable backbone की तरह सभी devices को जोड़ता है। Nodes को bus cable से drop lines और taps के through जोड़ा जाता है। दोनों ends पर terminators signal को absorb करते हैं ताकि reflection na हो। (Forouzan)*

**★ Nukta (Key Point):** Bus = one backbone + drop lines + taps + terminators at both ends. Fault isolation is difficult; a backbone break stops everything.

*Bus = एक backbone + drop lines + taps + दोनों ends पर terminators. Fault isolation मुश्किल है; backbone tootne से सब कुछ band हो जाता है।*

*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

---
### Q65. The IEEE 802 stअंदरds (such as 802.3 for Ethernet, 802.5 for Token Ring, 802.11 for Wi-Fi) primarily define the ______ of LANs/MANs.

<span lang='hi'>IEEE 802 stअंदरds (जैसे 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi) primarily LANs/MANs की _______ define करते हैं।</span>

- **(A)** Physical and Data Link layers (including the logical topology / MAC) / Physical और Data Link layers (logical topology / MAC sahit) ✅ **(CORRECT)**
- **(B)** Only the Application layer / सिर्फ Application layer
- **(C)** Only IP addressing / सिर्फ IP addressing
- **(D)** Only WAN routing / सिर्फ WAN routing

**✔ Correct Answer: (A) Physical and Data Link layers (including the logical topology / MAC)** — IEEE 802 is the family of stअंदरds for LANs and MANs; it covers the Physical layer and the Data Link layer (split into LLC - 802.2 - and MAC sublayers). 802.3 = Ethernet, 802.5 = Token Ring, 802.11 = Wireless LAN. The logical topology (bus/ring) is a Data-Link/MAC concern.

*IEEE 802 LANs और MANs के लिए stअंदरds का family है; यह Physical layer और Data Link layer को cover करता है (LLC - 802.2 - और MAC sublayers में बनता है). 802.3 = Ethernet, 802.5 = Token Ring, 802.11 = Wireless LAN. Logical topology (bus/ring) एक Data-Link/MAC concern है।*

**★ Nukta (Key Point):** IEEE 802 = LAN/MAN stअंदरds (Physical + Data Link). 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi.

*IEEE 802 = LAN/MAN stअंदरds (Physical + Data Link). 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

---
### Q66. Four network segments in Bus topology are: A1–A2, B1–B2–B3, C1–C2 and D1–D2–D3. If A1, B1, C1 and D1 are interconnected in a mesh, how many mesh connections are required?

<span lang='hi'>Bus topology में चार network segments हैं: A1–A2, B1–B2–B3, C1–C2 और D1–D2–D3। यदि A1, B1, C1 और D1 को mesh में जोड़ा जाए, तो कितने mesh connections चाहिए?</span>

- **(A)** 12 / 12
- **(B)** 10 / 10
- **(C)** 6 / 6 ✅ **(CORRECT)**
- **(D)** 45 / 45

**✔ Correct Answer: (C) 6** — Only the four interconnecting nodes (A1, B1, C1, D1) are meshed: links = n(n-1)/2 = 4×3/2 = 6. (Matches the official RPSC key.)

*सिर्फ चार interconnecting nodes (A1, B1, C1, D1) mesh हो रहे हैं: links = n(n-1)/2 = 4×3/2 = 6। (Official RPSC key से match.)*

**★ Nukta (Key Point):** Mesh formula n(n-1)/2 — लेकिन n सिर्फ meshed nodes है (4), पूरे network के hosts (10) नहीं!

*Mesh formula n(n-1)/2 — पर n सिर्फ meshed nodes है (4), पूरे network के hosts (10) नहीं!*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

---

## Section E - Types of Networks (LAN, MAN, WAN, PAN, CAN, SAN; Internet, Intranet, Extranet; Point-to-Point, Multipoint; Client-Server, P2P)

*Syllabus: Types of Networks - Geographical (LAN, MAN, WAN, PAN, CAN, SAN) | Accessibility (Internet, Intranet, Extranet) | Architecture (Point-to-Point, Multipoint)*

### Q67. The term WAN stands for?

<span lang='hi'>WAN का पूरा नाम (full form) क्या है?</span>

- **(A)** Wide Area Net / Wide Area Net
- **(B)** Wide Access Network / Wide Access Network
- **(C)** Wide Area Network / Wide Area Network ✅ **(CORRECT)**
- **(D)** Wide Access Net / Wide Access Net

**✔ Correct Answer: (C) Wide Area Network** — WAN = Wide Area Network. It spans a large geographical area - a country, continent or the whole world. The Internet is the largest WAN.

*WAN = Wide Area Network. यह एक बड़े geographical area को span करता है - एक देश, continent या पूरी दुनिया। Internet सबसे बड़ा WAN है।*

**★ Nukta (Key Point):** WAN = Wide Area Network. Internet सबसे बड़ा WAN है.

*WAN = Wide Area Network. Internet सबसे बड़ा WAN है।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q11 / BCI_SCI Subject Test-01, Q11] · Medium*

---
### Q68. Which network is suitable for a building?

<span lang='hi'>किसी एक building के लिए कौन सा network उपयुक्त (suitable) है?</span>

- **(A)** WAN / WAN
- **(B)** LAN / LAN ✅ **(CORRECT)**
- **(C)** MAN / MAN
- **(D)** PAN / PAN

**✔ Correct Answer: (B) LAN** — A LAN (Local Area Network) is usually privately owned and covers a small geographical area - a single office, building, or campus. So a building -> LAN.

*LAN (Local Area Network) आम तौर पर privately owned होता है और एक chhote geographical area - एक office, building, या campus - को cover करता है। इसलिए building के लिए LAN उपयुक्त है।*

**★ Nukta (Key Point):** LAN = Local Area Network - छोटा area (office/building/campus), private, high speed.

*LAN = Local Area Network - छोटा area (office/building/campus), private, high speed.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q27] · Medium*

---
### Q69. Bluetooth is an example of:

<span lang='hi'>Bluetooth इसका example है:</span>

- **(A)** personal area network / personal area network (PAN) ✅ **(CORRECT)**
- **(B)** local area network / local area network (LAN)
- **(C)** virtual private network / virtual private network (VPN)
- **(D)** none of the mentioned / इनमें से कोई नहीं

**✔ Correct Answer: (A) personal area network** — Bluetooth connects devices around one person (mobile phone with earphones/headset). A network organized around an individual person is a PAN (Personal Area Network).

*Bluetooth एक व्यक्ति के aas-पास के devices को जोड़ता है (mobile phone को earphones/headset से). Ek व्यक्ति के around organized network को PAN (Personal Area Network) कहते हैं।*

**★ Nukta (Key Point):** PAN = Personal Area Network - एक person के around (Bluetooth: phone <-> earphones).

*PAN = Personal Area Network - एक person के around (Bluetooth: phone <-> earphones).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q31] · Medium*

---
### Q70. Which one of the following extends a private network across public networks?

<span lang='hi'>निम्नलिखित में से कौन एक private network को public networks के paar (across) extend करता है?</span>

- **(A)** local area network / local area network (LAN)
- **(B)** virtual private network / virtual private network (VPN) ✅ **(CORRECT)**
- **(C)** enterprise private network / enterprise private network
- **(D)** storage area network / storage area network (SAN)

**✔ Correct Answer: (B) virtual private network** — A Virtual Private Network (VPN) extends a private network across a public network (e.g., the Internet) using tunneling and encryption, so data travels securely as if on a private network.

*Virtual Private Network (VPN) एक private network को एक public network (जैसे Internet) के paar extend करता है, tunneling और encryption के through, ताकि data private network की तरह securely travel करे।*

**★ Nukta (Key Point):** VPN = Virtual Private Network - private network को public (Internet) पर extend करता है, securely.

*VPN = Virtual Private Network - private network को public (Internet) पर extend करता है, securely.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q32] · Medium*

---
### Q71. ______ is a network that covers geographic areas that are larger, such as districts or cities.

<span lang='hi'>______ एक ऐसा network है जो बड़े geographical areas, जैसे districts या cities, को cover करता है।</span>

- **(A)** LAN / LAN
- **(B)** MAN / MAN ✅ **(CORRECT)**
- **(C)** WAN / WAN
- **(D)** None of these / इनमें से कोई नहीं

**✔ Correct Answer: (B) MAN** — MAN (Metropolitan Area Network) covers a metropolitan area, usually a city - larger than a LAN but smaller than a WAN. Example: cable TV network of a city.

*MAN (Metropolitan Area Network) एक metropolitan area, आम तौर पर एक city, को cover करता है - LAN से बड़ा लेकिन WAN से छोटा। Example: एक city का cable TV network.*

**★ Nukta (Key Point):** MAN = Metropolitan Area Network - city level (cable TV network).

*MAN = Metropolitan Area Network - city level (cable TV network).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q49] · Medium*

---
### Q72. Which factor primarily decides whether a communication system is a LAN or a WAN?

<span lang='hi'>कौन-सा factor मुख्य रूप से तय करता है कि communication system LAN है या WAN?</span>

- **(A)** The geographical area it spans / वह कितने geographical area में फैला है ✅ **(CORRECT)**
- **(B)** The number of protocols it uses / वह कितने protocols use करता है
- **(C)** The colour of the cables / Cables का रंग
- **(D)** The type of keyboard attached / जुड़े keyboard का प्रकार

**✔ Correct Answer: (A) The geographical area it spans** — Forouzan: a LAN covers a building/plant/campus (small area); a WAN spans states, countries or the whole world — geographical span is the primary factor.

*Forouzan: LAN building/campus जैसे छोटे area को cover करता है; WAN states/countries/दुनिया तक फैला होता है — geographical span ही मुख्य factor है।*

**★ Nukta (Key Point):** Chhoti area = LAN, city = MAN, state/country/world = WAN. Faisla सिर्फ area का.

*छोटा area = LAN, city = MAN, state/country/world = WAN। फैसला सिर्फ area का।*

*[Source: Forouzan Ch1 (Q1-9) — Practice Set] · Medium*

---
### Q73. In terms of the size of the network, the correct order (ascending) is:

<span lang='hi'>Network के size के hisaab से सही kram (badhta हुआ/ascending order) क्या है?</span>

- **(A)** PAN, MAN, LAN, WAN / PAN, MAN, LAN, WAN
- **(B)** LAN, MAN, WAN, PAN / LAN, MAN, WAN, PAN
- **(C)** PAN, LAN, MAN, WAN / PAN, LAN, MAN, WAN ✅ **(CORRECT)**
- **(D)** LAN, PAN, MAN, WAN / LAN, PAN, MAN, WAN

**✔ Correct Answer: (C) PAN, LAN, MAN, WAN** — Ascending order of size: PAN (around a person, smallest) < LAN (building/campus) < MAN (city) < WAN (country/world, largest).

*Size के hisaab से badhta kram: PAN (एक person के around, सबसे छोटा) < LAN (building/campus) < MAN (city) < WAN (देश/दुनिया, सबसे बड़ा).*

**★ Nukta (Key Point):** Remember: PAN < LAN < MAN < WAN (smallest to largest).

*याद रखें: PAN < LAN < MAN < WAN (छोटा से बड़ा).*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q42] · Medium*

---
### Q74. Which type of network covers an entire city or campus?

<span lang='hi'>कौन सा network पूरे एक city या campus को cover करता है?</span>

- **(A)** LAN / LAN
- **(B)** MAN / MAN ✅ **(CORRECT)**
- **(C)** WAN / WAN
- **(D)** PAN / PAN

**✔ Correct Answer: (B) MAN** — MAN (Metropolitan Area Network) covers an entire city; a large campus can also be of MAN scale. (Official answer key: MAN)

*MAN (Metropolitan Area Network) एक पूरे city को cover करता है; एक बड़ा campus भी MAN scale का हो सकता है। (Official answer key: MAN)*

**★ Nukta (Key Point):** MAN = city level. Note: a single building/campus LAN is usually LAN/CAN; an entire city = MAN.

*MAN = city level. Note: एक building/campus का LAN आम तौर पर LAN/CAN होता है; पूरी city = MAN.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q2] · Medium*

---
### Q75. The Internet is an example of:

<span lang='hi'>Internet इसका example है:</span>

- **(A)** LAN / LAN
- **(B)** MAN / MAN
- **(C)** WAN / WAN ✅ **(CORRECT)**
- **(D)** PAN / PAN

**✔ Correct Answer: (C) WAN** — The Internet is a global system of interconnected networks - it is the largest WAN (Wide Area Network).

*Internet interconnected networks का एक global system है - यह सबसे बड़ा WAN (Wide Area Network) है।*

**★ Nukta (Key Point):** Internet = सबसे बड़ा WAN (network of networks).

*Internet = सबसे बड़ा WAN (network of networks).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q12] · Medium*

---
### Q76. SAN is mainly used for:

<span lang='hi'>SAN का मुख्य उपयोग किसके लिए होता है?</span>

- **(A)** File Sharing / file sharing
- **(B)** Storage Management / storage management ✅ **(CORRECT)**
- **(C)** Internet Access / internet access
- **(D)** Printing Documents / documents print करना

**✔ Correct Answer: (B) Storage Management** — SAN (Storage Area Network) is a dedicated high-speed private network used for storage management - connecting servers to storage devices in data centres.

*SAN (Storage Area Network) एक dedicated high-speed private network है जो storage management के लिए use होता है - servers को storage devices से जोड़ने के लिए (data centres में).*

**★ Nukta (Key Point):** SAN = Storage Area Network - servers <-> storage devices, data centre.

*SAN = Storage Area Network - servers <-> storage devices, data centre.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q13] · Medium*

---
### Q77. PAN is used for connecting:

<span lang='hi'>PAN किसके connect करने के लिए use होता है?</span>

- **(A)** Personal devices like mobile, laptop, Bluetooth headset / personal devices जैसे mobile, laptop, Bluetooth headset ✅ **(CORRECT)**
- **(B)** Computers in a company / एक company के computers
- **(C)** Computers in a city / एक city के computers
- **(D)** Global offices / global offices

**✔ Correct Answer: (A) Personal devices like mobile, laptop, Bluetooth headset** — PAN (Personal Area Network) is a network organized around an individual person - connecting personal devices like mobile, laptop, Bluetooth headset.

*PAN (Personal Area Network) एक व्यक्ति के around organized एक network है - personal devices जैसे mobile, laptop, Bluetooth headset को जोड़ने के लिए।*

**★ Nukta (Key Point):** PAN = Personal Area Network - एक person के devices (mobile, laptop, headset).

*PAN = Personal Area Network - एक person के devices (mobile, laptop, headset).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q14] · Medium*

---
### Q78. A school has four computer labs in the same building. Each lab has 20 computers connected to a central server. Students can share files and print from any lab. Which type of network is implemented in this school?

<span lang='hi'>Ek school में एक ही building में चार computer labs हैं. हर lab में 20 computers एक central server से जुड़े हैं। Students किसी भी lab से files share और print कर सकते हैं। School में कौन सा network implemented है?</span>

- **(A)** WAN / WAN
- **(B)** MAN / MAN
- **(C)** LAN / LAN ✅ **(CORRECT)**
- **(D)** CAN / CAN

**✔ Correct Answer: (C) LAN** — All four labs are in the same building and share a central server - this is a small, privately-owned, single-site network = LAN (Local Area Network).

*Chaaron labs एक ही building में हैं और एक central server share करते हैं - यह एक छोटा, privately-owned, single-site network है = LAN (Local Area Network).*

**★ Nukta (Key Point):** LAN = single building/campus, private, high speed. Example: school lab, office.

*LAN = एक building/campus, private, high speed. Example: school lab, office.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q15] · Medium*

---
### Q79. A university has different departments in separate buildings like Engineering, Arts, and Commerce. Each department has its own LAN. All these LANs are connected together for communication. Which type of network connects all these LANs?

<span lang='hi'>Ek university में अलग-अलग departments अलग buildings में हैं जैसे Engineering, Arts, Commerce। हर department का apna LAN है। यह सब LANs communication के लिए आपस में जुड़े हैं। कौन सा network in सब LANs को जोड़ता है?</span>

- **(A)** LAN / LAN
- **(B)** CAN / CAN ✅ **(CORRECT)**
- **(C)** MAN / MAN
- **(D)** WAN / WAN

**✔ Correct Answer: (B) CAN** — A CAN (Campus Area Network) interconnects the LANs of different buildings across a campus (university/corporate). Here, multiple departmental LANs are joined = CAN.

*CAN (Campus Area Network) एक campus (university/corporate) की अलग buildings में maujood LANs को interconnect करता है। यहाँ कई departmental LANs जुड़े हैं = CAN.*

**★ Nukta (Key Point):** CAN = Campus Area Network - एक campus की multiple buildings के LANs को जोड़ता है.

*CAN = Campus Area Network - एक campus की कई buildings के LANs को जोड़ता है।*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q16] · Medium*

---
### Q80. An international bank connects its main office in New York with branches in Delhi, London, and Tokyo. Which network type is used here?

<span lang='hi'>Ek international bank अपने main office (New York) को Delhi, London, और Tokyo की branches से जोड़ता है। यहाँ कौन सा network type use होता है?</span>

- **(A)** MAN / MAN
- **(B)** WAN / WAN ✅ **(CORRECT)**
- **(C)** CAN / CAN
- **(D)** LAN / LAN

**✔ Correct Answer: (B) WAN** — Branches in different cities and countries (New York, Delhi, London, Tokyo) are connected over long distances - this is a WAN (Wide Area Network).

*Alag-अलग cities और deshon में branches (New York, Delhi, London, Tokyo) लंबी दूरी पर जुड़े हैं - यह WAN (Wide Area Network) है।*

**★ Nukta (Key Point):** WAN = long distance (city/country/continent). Bank branches worldwide = WAN.

*WAN = लंबी दूरी (city/देश/continent). Worldwide bank branches = WAN.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q17] · Medium*

---
### Q81. A company has several servers that store and manage large volumes of data. All storage devices are interconnected for high-speed data access. Which type of network is this?

<span lang='hi'>Ek company के पास कई servers हैं जो बड़ी matra में data store और manage करते हैं। सब storage devices high-speed data access के लिए interconnected हैं। यह कौन सा network है?</span>

- **(A)** LAN / LAN
- **(B)** SAN / SAN ✅ **(CORRECT)**
- **(C)** CAN / CAN
- **(D)** WAN / WAN

**✔ Correct Answer: (B) SAN** — Servers plus storage devices, all interconnected for high-speed data access = SAN (Storage Area Network), a dedicated network for storage.

*Servers + storage devices, सब high-speed data access के लिए interconnected = SAN (Storage Area Network), storage के लिए एक dedicated network.*

**★ Nukta (Key Point):** SAN = Storage Area Network - storage devices को high-speed access dene के लिए.

*SAN = Storage Area Network - storage devices को high-speed access dene के लिए।*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q18] · Medium*

---
### Q82. A supplier accessing a company's order tracking system uses:

<span lang='hi'>Ek supplier जो company के order tracking system को access करता है, कौन सा network use करता है?</span>

- **(A)** Internet / Internet
- **(B)** Intranet / Intranet
- **(C)** Extranet / Extranet ✅ **(CORRECT)**
- **(D)** VPN / VPN

**✔ Correct Answer: (C) Extranet** — An Extranet is an intranet extended to authorized outsiders (suppliers, partners, customers). A supplier accessing the company's order tracking system = Extranet.

*Extranet एक ऐसा intranet है जो authorized outsiders (suppliers, partners, customers) के लिए extend किया गया हो। Company के order tracking system को access करने वाला supplier = Extranet.*

**★ Nukta (Key Point):** Extranet = intranet + authorized outsiders (suppliers/partners/customers).

*Extranet = intranet + authorized outsiders (suppliers/partners/customers).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q19] · Medium*

---
### Q83. Which network type provides maximum security and privacy?

<span lang='hi'>कौन सा network type अधिकतम (maximum) security और privacy provide करता है?</span>

- **(A)** Internet / Internet
- **(B)** Intranet / Intranet ✅ **(CORRECT)**
- **(C)** Extranet / Extranet
- **(D)** None / None

**✔ Correct Answer: (B) Intranet** — An Intranet is a private network inside an organization, accessible only to its members - so it provides maximum security and privacy. Internet is public; extranet is shared with outsiders.

*Intranet एक organization के अंदर का private network है, सिर्फ uske members के लिए accessible - इसलिए यह maximum security और privacy provide करता है। Internet public है; extranet outsiders के साथ share होता है।*

**★ Nukta (Key Point):** Security order: Intranet (सबसे secure/private) > Extranet > Internet (public).

*Security order: Intranet (सबसे secure/private) > Extranet > Internet (public).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q20] · Medium*

---
### Q84. A software company shares project reports and progress updates with its clients through a secure online portal that requires login credentials. Which network type is this?

<span lang='hi'>Ek software company अपने clients के साथ project reports और progress updates एक secure online portal के through share करती है जिसमें login credentials चाहिए। यह कौन सा network type है?</span>

- **(A)** Internet / Internet
- **(B)** Intranet / Intranet
- **(C)** Extranet / Extranet ✅ **(CORRECT)**
- **(D)** MAN / MAN

**✔ Correct Answer: (C) Extranet** — Sharing internal project information with clients (outsiders) through a secure login portal = Extranet (the company's intranet extended to authorized clients).

*Clients (outsiders) के साथ internal project information share करना, एक secure login portal के through = Extranet (company का intranet authorized clients के लिए extend किया गया).*

**★ Nukta (Key Point):** Clients को secure portal से share करना = Extranet.

*Clients को secure portal से share करना = Extranet.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q21] · Medium*

---
### Q85. Three or more devices share a link in ________ connection.

<span lang='hi'>Teen या अधिक devices एक link ________ connection में share करते हैं।</span>

- **(A)** Unipoint / unipoint
- **(B)** Multipoint / multipoint ✅ **(CORRECT)**
- **(C)** Point to point / point to point
- **(D)** None of the mentioned / इनमें से कोई नहीं

**✔ Correct Answer: (B) Multipoint** — A multipoint (multidrop) connection is one in which more than two devices share a single link; the capacity of the channel is shared spatially or temporally. (Forouzan)

*Multipoint (multidrop) connection में do से ज़्यादा devices एक single link share करते हैं; channel की capacity spatially या temporally share होती है। (Forouzan)*

**★ Nukta (Key Point):** Multipoint = एक link, कई devices; capacity shared. Point-to-point = dedicated link, सिर्फ 2 devices.

*Multipoint = एक link, कई devices; capacity shared. Point-to-point = dedicated link, सिर्फ 2 devices.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q36] · Medium*

---
### Q86. What are the two types of line configuration?

<span lang='hi'>Line configuration के दो प्रकार क्या हैं?</span>

- **(A)** Simplex and Half-Duplex / Simplex और Half-Duplex
- **(B)** Serial and Parallel / Serial और Parallel
- **(C)** Point-to-Point and Multipoint / Point-to-Point और Multipoint ✅ **(CORRECT)**
- **(D)** Analog and Digital / Analog और Digital

**✔ Correct Answer: (C) Point-to-Point and Multipoint** — Forouzan: line configuration describes how devices are connected — a dedicated link between two devices (point-to-point) or a link shared by three or more devices (multipoint).

*Forouzan: line configuration बताती है कि devices कैसे जुड़ी हैं — दो devices के बीच dedicated link (point-to-point) या तीन+ devices का shared link (multipoint)।*

**★ Nukta (Key Point):** Line configuration के सिर्फ 2 type: Point-to-Point & Multipoint. Simplex/Half/Full-Duplex TRANSMISSION MODES हैं.

*Line configuration के 2 type: Point-to-Point और Multipoint। Simplex/Half/Full-Duplex transmission modes हैं।*

*[Source: Forouzan Ch1 (Q1-4) — Practice Set] · Medium*

---
### Q87. What is the advantage of a multipoint connection over a point-to-point connection?

<span lang='hi'>Point-to-point connection की तुलना में multipoint connection का क्या लाभ है?</span>

- **(A)** Fewer cables are needed, so the cost is lower / कम cables लगती हैं, इसलिए cost कम होती है ✅ **(CORRECT)**
- **(B)** It provides a dedicated link for every pair of devices / हर device-युग्म को dedicated link मिलता है
- **(C)** It is more secure than point-to-point / यह point-to-point से ज़्यादा secure है
- **(D)** It needs more cables and ports / इसमें ज़्यादा cables और ports लगते हैं

**✔ Correct Answer: (A) Fewer cables are needed, so the cost is lower** — In a multipoint connection three or more devices SHARE one link, so fewer cables are required and the cost is shared — its main advantage over dedicated point-to-point links.

*Multipoint connection में तीन+ devices एक link share करती हैं, इसलिए cables कम लगती हैं और cost कम आती है — यही इसका मुख्य लाभ है।*

**★ Nukta (Key Point):** Multipoint = कम cable = कम kharch. Point-to-point = dedicated link (ज़्यादा cable, ज़्यादा privacy).

*Multipoint = कम cable = कम खर्च। Point-to-point = dedicated link (ज़्यादा cable, ज़्यादा privacy)।*

*[Source: Forouzan Ch1 (Q1-3) — Practice Set] · Medium*

---
### Q88. A _______ connection provides a dedicated link between two devices.

<span lang='hi'>Ek _______ connection do devices के बीच एक dedicated link provide करता है।</span>

- **(A)** point-to-point / point-to-point ✅ **(CORRECT)**
- **(B)** multipoint / multipoint
- **(C)** primary / primary
- **(D)** secondary / secondary

**✔ Correct Answer: (A) point-to-point** — A point-to-point connection provides a dedicated link between two devices; the entire capacity of the link is reserved for transmission between those two devices. (Forouzan)

*Point-to-point connection do devices के बीच एक dedicated link provide करता है; link की पूरी capacity सिर्फ unhi do devices के लिए reserved होती है। (Forouzan)*

**★ Nukta (Key Point):** Point-to-point = dedicated link, पूरी capacity सिर्फ 2 devices के लिए. Example: TV remote (IR), leased line.

*Point-to-point = dedicated link, पूरी capacity सिर्फ 2 devices के लिए. Example: TV remote (IR), leased line.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q42] · Medium*

---
### Q89. When a person makes a local telephone call to another person, what type of connection is it?

<span lang='hi'>जब कोई व्यक्ति दूसरे व्यक्ति को local telephone call करता है, तो यह किस प्रकार का connection है?</span>

- **(A)** Multipoint connection / Multipoint connection
- **(B)** Point-to-point connection / Point-to-point connection ✅ **(CORRECT)**
- **(C)** Broadcast connection / Broadcast connection
- **(D)** Multicast connection / Multicast connection

**✔ Correct Answer: (B) Point-to-point connection** — A local telephone call creates a dedicated circuit between exactly two parties through the exchange — a point-to-point connection.

*Local telephone call में exchange के medium से ठीक दो parties के बीच dedicated circuit बनता है — यह point-to-point connection है।*

**★ Nukta (Key Point):** Telephone call = 2 parties, dedicated link = point-to-point. Bus/Ethernet = multipoint.

*Telephone call = 2 parties, dedicated link = point-to-point। Bus/Ethernet = multipoint।*

*[Source: Forouzan Ch1 (P1-7) — Practice Set (Problem)] · Medium*

---
### Q90. Which of the following is an example of Client-Server architecture?

<span lang='hi'>निम्नलिखित में से कौन Client-Server architecture का example है?</span>

- **(A)** Chat between two Bluetooth devices / do Bluetooth devices के बीच chat
- **(B)** Web browser accessing a website / web browser जो एक website access कर रहा है ✅ **(CORRECT)**
- **(C)** File transfer via USB cable / USB cable से file transfer
- **(D)** Two laptops connected directly / do laptops directly connected

**✔ Correct Answer: (B) Web browser accessing a website** — A web browser (client) requesting and receiving a web page from a web server is the classic client-server architecture: the client requests a service and the server provides it.

*Web browser (client) जो एक web server से web page request करता है और receive करता है - यह classic client-server architecture है: client service request करता है और server use provide करता है।*

**★ Nukta (Key Point):** Client-Server = client request करता है, server service provide करता है. Example: web browser - website.

*Client-Server = client request करता है, server service provide करता है। Example: web browser - website.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q23] · Medium*

---
### Q91. In a bank, customers use ATMs to check balance or withdraw cash. ATM machines send the request to a central computer for verification and processing. Which type of architecture is used here?

<span lang='hi'>Ek bank में customers ATMs से balance check या cash withdraw करते हैं। ATM machines request एक central computer को verification और processing के लिए bhejte हैं। यहाँ कौन सी architecture use होती है?</span>

- **(A)** Peer-to-Peer / peer-to-peer
- **(B)** Client-Server / client-server ✅ **(CORRECT)**
- **(C)** Multipoint / multipoint
- **(D)** Point-to-Point / point-to-point

**✔ Correct Answer: (B) Client-Server** — The ATM (client) sends a request to a central computer (server) for verification and processing - the client requests a service and the server provides it = client-server architecture.

*ATM (client) request एक central computer (server) को verification और processing के लिए भेजता है - client service request करता है और server use provide करता है = client-server architecture.*

**★ Nukta (Key Point):** ATM -> central server = client-server (client request, server verify/process).

*ATM -> central server = client-server (client request, server verify/process).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q25] · Medium*

---
### Q92. In a LAN, connectivity can be created using Wi-Fi or _______.

<span lang='hi'>Ek LAN में connectivity Wi-Fi या _______ से बनाई जा सकती है।</span>

- **(A)** TV / TV
- **(B)** Radio / radio
- **(C)** Mobile / mobile
- **(D)** Ethernet / Ethernet ✅ **(CORRECT)**

**✔ Correct Answer: (D) Ethernet** — LAN connectivity is created using Wi-Fi (wireless) or Ethernet cables (wired). TV, radio and mobile are not LAN connectivity media.

*LAN connectivity Wi-Fi (wireless) या Ethernet cables (wired) से बनाई जाती है। TV, radio और mobile LAN connectivity media नहीं हैं।*

**★ Nukta (Key Point):** LAN connectivity = Wi-Fi (wireless) + Ethernet (wired cable).

*LAN connectivity = Wi-Fi (wireless) + Ethernet (wired cable).*

*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)] · Medium*

---
### Q93. Which network type is built on top of another existing network?

<span lang='hi'>कौन-सा network type किसी मौजूदा network के ऊपर बनाया जाता है?</span>

- **(A)** Overlay network / Overlay network ✅ **(CORRECT)**
- **(B)** Prime network / Prime network
- **(C)** Prior network / Prior network
- **(D)** Chief network / Chief network

**✔ Correct Answer: (A) Overlay network** — An overlay network is a virtual network built on top of another (host) network — e.g. VPN tunnels over the Internet or P2P networks over the Internet.

*Overlay network एक virtual network है जो किसी दूसरे (host) network के ऊपर बनता है — जैसे Internet पर VPN tunnels या P2P networks।*

**★ Nukta (Key Point):** Overlay = network के ऊपर बना network (VPN classic example है). Baaki 3 asli network types नहीं हैं.

*Overlay = network के ऊपर बना network (VPN इसका classic example है)। बाकी 3 real network types नहीं हैं।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

---
### Q94. ______ converts analog voice signals into digital and then transmits them over the broadband line.

<span lang='hi'>______ analog voice signals को digital में बदलकर broadband line पर भेजता है.</span>

- **(A)** VoIP (Voice over Internet Protocol) / VoIP (Voice over Internet Protocol) ✅ **(CORRECT)**
- **(B)** Chatting / Chatting
- **(C)** Website / Website
- **(D)** Video conferencing / Video conferencing

**✔ Correct Answer: (A) VoIP (Voice over Internet Protocol)** — VoIP आवाज़ को digital packets में बदलकर Internet जैसी lines पर भेजता है — Skype/WhatsApp call इसी के उदाहरण हैं.

*VoIP आवाज़ को digital packets में बदलकर Internet जैसी lines पर भेजता है — Skype/WhatsApp call इसी के उदाहरण हैं.*

**★ Nukta (Key Point):** VoIP = the new Internet form of the old telephone voice.

*VoIP = पुरानी फ़ोन-आवाज़ का नया internet-रूप.*

*[Source: RSMSSB Informatics Assistant 2023 (via examsmantra solved paper)] · Medium*

---
### Q95. Which of these is NOT a type of network?

<span lang='hi'>इनमें से कौन network का एक prakar (type) नहीं है?</span>

- **(A)** LAN / LAN
- **(B)** MAN / MAN
- **(C)** WAN / WAN
- **(D)** TAN / TAN ✅ **(CORRECT)**

**✔ Correct Answer: (D) TAN** — LAN, MAN and WAN are stअंदरd network types (by geographical area). TAN is not a stअंदरd type of network.

*LAN, MAN और WAN stअंदरd network types हैं (geographical area के aadhar पर). TAN कोई stअंदरd network type नहीं है।*

**★ Nukta (Key Point):** Network types: PAN, LAN, MAN, WAN (+ CAN, SAN). TAN = नहीं है.

*Network types: PAN, LAN, MAN, WAN (+ CAN, SAN). TAN = नहीं है।*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q7] · Hard*

---
### Q96. What is the difference between an 'internet' and the 'Internet'?

<span lang='hi'>'internet' और 'Internet' में अंतर क्या है?</span>

- **(A)** There is no difference; both mean the World Wide Web / कोई अंतर नहीं; दोनों का अर्थ World Wide Web है
- **(B)** An internet is any network of networks; the Internet is the specific global one we use today / internet कोई भी network of networks है; Internet आज की वह विशिष्ट विश्वव्यापी network of networks है ✅ **(CORRECT)**
- **(C)** An internet is smaller than a LAN; the Internet is larger than a WAN / internet LAN से छोटा है; Internet WAN से बड़ा है
- **(D)** An internet uses cables; the Internet uses only wireless / internet cables use करता है; Internet सिर्फ wireless use करता है

**✔ Correct Answer: (B) An internet is any network of networks; the Internet is the specific global one we use today** — An 'internet' (lower-case) is any generic network of networks. The 'Internet' (capital I) is THE specific worldwide internet that grew from ARPANET.

*'internet' (छोटा i) कोई भी generic network of networks है। 'Internet' (बड़ा I) वह विशिष्ट विश्वव्यापी internet है जो ARPANET से विकसित हुआ।*

**★ Nukta (Key Point):** internet = generic network of networks. Internet = THE global network (capital I).

*internet = generic network of networks। Internet = वह global network (बड़ा I)।*

*[Source: Forouzan Ch1 (Q1-10) — Practice Set] · Hard*

---
### Q97. Bank employees access internal financial databases, while customers access their accounts through online banking websites. Which networks are being used by employees and customers respectively?

<span lang='hi'>Bank employees internal financial databases access करते हैं, jabki customers online banking websites के through अपने accounts access करते हैं। Employees और customers kramashah कौन से networks use कर रहे हैं?</span>

- **(A)** Employees - Intranet; Customers - Extranet / employees - Intranet; customers - Extranet ✅ **(CORRECT)**
- **(B)** Employees - Internet; Customers - Intranet / employees - Internet; customers - Intranet
- **(C)** Employees - Extranet; Customers - Internet / employees - Extranet; customers - Internet
- **(D)** Both - Internet / दोनों - Internet

**✔ Correct Answer: (A) Employees - Intranet; Customers - Extranet** — Employees use the bank's internal private network = Intranet. Customers access the bank's system from outside = Extranet (per the official key: the bank's online banking is its intranet extended to customers).

*Employees bank के internal private network = Intranet use करते हैं। Customers बाहर से bank के system को access करते हैं = Extranet (official key के anusaar: bank का online banking uske intranet का customers के लिए extension है).*

**★ Nukta (Key Point):** Employees -> Intranet (internal). Outsiders (customers/suppliers) -> Extranet. Public -> Internet.

*Employees -> Intranet (internal). Outsiders (customers/suppliers) -> Extranet. Public -> Internet.*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q22] · Hard*

---
### Q98. How many point-to-point WANs are needed to connect n LANs so that every LAN can directly communicate with every other LAN?

<span lang='hi'>n LANs को इस तरह जोड़ने के लिए कितने point-to-point WANs चाहिए कि हर LAN हर दूसरी LAN से सीधे communicate कर सके?</span>

- **(A)** n / n
- **(B)** n - 1 / n - 1
- **(C)** n(n - 1)/2 / n(n - 1)/2 ✅ **(CORRECT)**
- **(D)** n² / n²

**✔ Correct Answer: (C) n(n - 1)/2** — Direct communication between every pair of LANs needs one WAN link per pair — n(n-1)/2 links (the same mesh formula).

*हर LAN-युग्म के बीच सीधे communication के लिए हर युग्म को एक WAN link चाहिए — n(n-1)/2 links (mesh जैसा ही formula)।*

**★ Nukta (Key Point):** Full mesh of LANs = n(n-1)/2 WAN links. Formula mesh वाला ही है.

*LANs का full mesh = n(n-1)/2 WAN links। Formula mesh जैसा ही है।*

*[Source: Forouzan Ch1 (Q1-13) — Practice Set] · Hard*

---
### Q99. Which of the following uses Peer-to-Peer (P2P) architecture, not Client-Server?

<span lang='hi'>निम्नलिखित में से कौन Peer-to-Peer (P2P) architecture use करता है, Client-Server नहीं?</span>

- **(A)** BitTorrent file sharing / BitTorrent file sharing ✅ **(CORRECT)**
- **(B)** Google search / Google search
- **(C)** Gmail / Gmail
- **(D)** YouTube / YouTube

**✔ Correct Answer: (A) BitTorrent file sharing** — BitTorrent is peer-to-peer: users (peers) share file pieces directly with each other without a central server. Google search, Gmail and YouTube are client-server services.

*BitTorrent peer-to-peer है: users (peers) file के tukde directly आपस में share करते हैं बिना किसी central server के। Google search, Gmail और YouTube client-server services हैं।*

**★ Nukta (Key Point):** P2P = peers आपस में directly share करते हैं (BitTorrent). Client-Server = server service देता है (Google, Gmail, YouTube).

*P2P = peers आपस में directly share करते हैं (BitTorrent). Client-Server = server service देता है (Google, Gmail, YouTube).*

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q24] · Hard*

---

## Section F - Network History (ARPANET to Today's Network)

*Syllabus: Network History - ARPANET to today's network*

### Q100. The first network was:

<span lang='hi'>सबसे पहला network था:</span>

- **(A)** CNNET / CNNET
- **(B)** NSFNET / NSFNET
- **(C)** ASAPNET / ASAPNET
- **(D)** ARPANET / ARPANET ✅ **(CORRECT)**

**✔ Correct Answer: (D) ARPANET** — The first network was ARPANET (1969), created by ARPA of the U.S. Department of Defense. NSFNET (1986) came later as a backbone.

*सबसे पहला network ARPANET (1969) था, जिसे ARPA of U.S. Department of Defense ने बनाया था। NSFNET (1986) बाद में एक backbone के रूप में aaya था।*

**★ Nukta (Key Point):** First network = ARPANET (1969). NSFNET = 1986 (backbone).

*First network = ARPANET (1969). NSFNET = 1986 (backbone).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q34] · Medium*

---
### Q101. In the original ARPANET, _______ were directly connected together.

<span lang='hi'>Original ARPANET में, _______ आपस में directly connected the।</span>

- **(A)** IMPs / IMPs (Interface Message Processors) ✅ **(CORRECT)**
- **(B)** host computers / host computers
- **(C)** networks / networks
- **(D)** routers / routers

**✔ Correct Answer: (A) IMPs** — In the original ARPANET, the IMPs (Interface Message Processors - the packet switches) were directly connected together; the host computers connected to the IMPs.

*Original ARPANET में, IMPs (Interface Message Processors - packet switches) आपस में directly connected the; host computers IMPs से connect होते the।*

**★ Nukta (Key Point):** Original ARPANET: IMPs (packet switches) directly connected; hosts attached to IMPs.

*Original ARPANET: IMPs (packet switches) directly connected the; hosts IMPs से attach होते the।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q43] · Medium*

---
### Q102. The first operational computer network in the world was the _________ for the United States Department of Defense.

<span lang='hi'>दुनिया का पहला operational computer network, United States Department of Defense के लिए _________ था।</span>

- **(A)** ARPANET / ARPANET ✅ **(CORRECT)**
- **(B)** ERNET / ERNET
- **(C)** SKYNET / SKYNET
- **(D)** DARPANET / DARPANET

**✔ Correct Answer: (A) ARPANET** — ARPANET was the first operational computer network in the world, created for the U.S. Department of Defense (1969).

*ARPANET दुनिया का पहला operational computer network था, जो U.S. Department of Defense के लिए बनाया गया था (1969).*

**★ Nukta (Key Point):** First operational network = ARPANET (1969, U.S. DoD).

*First operational network = ARPANET (1969, U.S. DoD).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q48] · Medium*

---
### Q103. ARPANET - the precursor of today's Internet - was created in ______ by ARPA (Advanced Research Projects Agency) of the U.S. Department of Defense, starting with four nodes (UCLA, SRI, UC Santa Barbara, University of Utah).

<span lang='hi'>ARPANET - aaj के Internet का purvaj - ______ में ARPA (Advanced Research Projects Agency), U.S. Department of Defense द्वारा बनाया गया था, चार nodes से shuruaat हुई (UCLA, SRI, UC Santa Barbara, University of Utah).</span>

- **(A)** 1957 / 1957
- **(B)** 1969 / 1969 ✅ **(CORRECT)**
- **(C)** 1983 / 1983
- **(D)** 1991 / 1991

**✔ Correct Answer: (B) 1969** — ARPANET was born in 1969 with four nodes: UCLA, Stanford Research Institute (SRI), UC Santa Barbara and the University of Utah. The first message was sent on 29 October 1969 (the LO of LOGIN).

*ARPANET 1969 में चार nodes के साथ बना था: UCLA, Stanford Research Institute (SRI), UC Santa Barbara और University of Utah. पहला message 29 October 1969 को भेजा गया था (LOGIN का LO).*

**★ Nukta (Key Point):** ARPANET = 1969, 4 nodes (UCLA, SRI, UCSB, Utah); first message 29 Oct 1969 (LO of LOGIN).

*ARPANET = 1969, 4 nodes (UCLA, SRI, UCSB, Utah); पहला message 29 Oct 1969 (LOGIN का LO).*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q104. TCP/IP (developed by Vint Cerf and Bob Kahn) was adopted by ARPANET as its official protocol suite on 1 January ______ - an event known as the fflag day.

<span lang='hi'>TCP/IP (Vint Cerf और Bob Kahn द्वारा develop किया गया) को ARPANET ने apna official protocol suite बनाया था 1 January ______ को - is event को fflag day कहा जाता है।</span>

- **(A)** 1969 / 1969
- **(B)** 1972 / 1972
- **(C)** 1983 / 1983 ✅ **(CORRECT)**
- **(D)** 1995 / 1995

**✔ Correct Answer: (C) 1983** — On 1 January 1983, ARPANET officially switched to TCP/IP - the fflag day - making TCP/IP the common language of the network. Cerf and Kahn developed TCP/IP in the 1970s (publicly demonstrated in 1972).

*1 January 1983 को ARPANET officially TCP/IP पर switch हो गया - fflag day - जिससे TCP/IP network की common language बन गया। Cerf और Kahn ने TCP/IP 1970s में develop किया था (1972 में publicly demonstrate हुआ).*

**★ Nukta (Key Point):** Fflag day = 1 Jan 1983 (ARPANET -> TCP/IP). TCP/IP developed by Cerf & Kahn in 1970s (demo 1972). Syllabus का TCP/IP model 1972 = development era.

*Fflag day = 1 Jan 1983 (ARPANET -> TCP/IP). TCP/IP Cerf & Kahn ने 1970s में develop किया (demo 1972). Syllabus का TCP/IP model 1972 = development era.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q105. NSFNET, created by the U.S. National Science Foundation in ______, became a major backbone of the Internet, connecting universities and research centres.

<span lang='hi'>NSFNET, U.S. National Science Foundation द्वारा ______ में बनाया गया, Internet का एक major backbone बन गया, universities और research centres को जोड़ता था।</span>

- **(A)** 1969 / 1969
- **(B)** 1983 / 1983
- **(C)** 1986 / 1986 ✅ **(CORRECT)**
- **(D)** 1991 / 1991

**✔ Correct Answer: (C) 1986** — NSFNET was created in 1986 by the National Science Foundation; it connected universities and research centres with T1 lines (1.544 Mbps) and became a major Internet backbone.

*NSFNET 1986 में National Science Foundation द्वारा बनाया गया था; isne universities और research centres को T1 lines (1.544 Mbps) से जोड़ा और एक major Internet backbone बन गया।*

**★ Nukta (Key Point):** NSFNET = 1986 (National Science Foundation), T1 backbone -> Internet backbone.

*NSFNET = 1986 (National Science Foundation), T1 backbone -> Internet backbone.*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---
### Q106. The World Wide Web (WWW) was invented in 1991 at CERN by ______, and it made the Internet popular among the general public.

<span lang='hi'>World Wide Web (WWW) का invention 1991 में CERN में ______ ने किया था, और isne Internet को आम public के बीच popular बनाया।</span>

- **(A)** Vint Cerf / Vint Cerf
- **(B)** Tim Berners-Lee / Tim Berners-Lee ✅ **(CORRECT)**
- **(C)** Bob Kahn / Bob Kahn
- **(D)** Marc Andreessen / Marc Andreessen

**✔ Correct Answer: (B) Tim Berners-Lee** — Tim Berners-Lee invented the WWW at CERN in 1991 (using HTML, HTTP and URLs). The Mosaic browser (1993) later made the web popular; the Internet opened to commercial use in the 1990s.

*Tim Berners-Lee ने 1991 में CERN में WWW का invention किया था (HTML, HTTP और URLs का use करके). Mosaic browser (1993) ने बाद में web को popular बनाया; Internet 1990s में commercial use के लिए खुला।*

**★ Nukta (Key Point):** WWW = 1991, Tim Berners-Lee @ CERN. Mosaic browser 1993. Vint Cerf & Bob Kahn = fathers of the Internet (TCP/IP).

*WWW = 1991, Tim Berners-Lee @ CERN. Mosaic browser 1993. Vint Cerf & Bob Kahn = Internet के fathers (TCP/IP).*

*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

---

## Section G - General Network Basics (WWW, E-mail, Protocols, Servers, Switching - from repo intro tests)

*Syllabus: Introduction of DC - general basics asked in BCI/RPSC exams (Specific Address/URL, Application services, Switching)*

### Q107. A collection of hyperlinked documents on the internet forms the?

<span lang='hi'>Internet पर hyperlinked documents का sangrah (collection) क्या banata है?</span>

- **(A)** World Wide Web (WWW) / World Wide Web (WWW) ✅ **(CORRECT)**
- **(B)** E-mail system / e-mail system
- **(C)** Mailing list / mailing list
- **(D)** Hypertext markup language / hypertext markup language (HTML)

**✔ Correct Answer: (A) World Wide Web (WWW)** — A collection of hyperlinked documents on the Internet forms the World Wide Web (WWW). HTML is the markup language used to create those documents.

*Internet पर hyperlinked documents का sangrah World Wide Web (WWW) banata है। HTML वह markup language है जिस से यह documents bante हैं।*

**★ Nukta (Key Point):** WWW = hyperlinked documents का collection. HTML = un documents की language (WWW नहीं).

*WWW = hyperlinked documents का collection. HTML = un documents की language है (WWW नहीं).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q5] · Medium*

---
### Q108. Which one of the following is a valid email address?

<span lang='hi'>निम्नलिखित में से कौन सा एक valid email address है?</span>

- **(A)** computech@academy.com / computech@academy.com ✅ **(CORRECT)**
- **(B)** gmail.com / gmail.com
- **(C)** compu@.com / compu@.com
- **(D)** computech@books / computech@books

**✔ Correct Answer: (A) computech@academy.com** — A valid email address has a local part, the @ symbol, and a domain with a top-level domain (TLD). computech@academy.com follows this format.

*Ek valid email address में local part, @ symbol, और एक domain with top-level domain (TLD) होता है। computech@academy.com यह format follow करता है।*

**★ Nukta (Key Point):** Valid email = local@domain.TLD (e.g., name@site.com).

*Valid email = local@domain.TLD (जैसे name@site.com).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q6] · Medium*

---
### Q109. Which of the following best describes uploading information?

<span lang='hi'>निम्नलिखित में से कौन uploading information को सबसे achhe से describe करता है?</span>

- **(A)** Sorting data on a disk drive / disk drive पर data को sort करना
- **(B)** Sending information to a host computer / information को एक host computer को भेजना ✅ **(CORRECT)**
- **(C)** Receiving information from a host computer / एक host computer से information receive करना
- **(D)** Sorting data on a hard drive / hard drive पर data को sort करना

**✔ Correct Answer: (B) Sending information to a host computer** — Uploading means sending/transferring information from a local device to a host/remote computer over a network.

*Uploading का मतलब है information को एक local device से एक host/remote computer को network के through भेजना।*

**★ Nukta (Key Point):** Uploading = local से remote/host को भेजना. Downloading = remote से local को लेना.

*Uploading = local से remote/host को भेजना. Downloading = remote से local को लेना.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q7] · Medium*

---
### Q110. Which one of the following is the most common internet protocol?

<span lang='hi'>Nimnlikhis में से कौन सा सबसे common internet protocol है?</span>

- **(A)** HTML / HTML
- **(B)** NetBEUI / NetBEUI
- **(C)** TCP/IP / TCP/IP ✅ **(CORRECT)**
- **(D)** IPX/SPX / IPX/SPX

**✔ Correct Answer: (C) TCP/IP** — TCP/IP is the core protocol suite of the Internet - it is the most common protocol used on the Internet. HTML is a markup language, not a protocol.

*TCP/IP Internet का core protocol suite है - यह Internet पर सबसे common protocol है। HTML एक markup language है, protocol नहीं।*

**★ Nukta (Key Point):** Internet का core protocol = TCP/IP. HTML = language, protocol नहीं.

*Internet का core protocol = TCP/IP. HTML = language है, protocol नहीं.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q8] · Medium*

---
### Q111. The dial-up connections to access the internet use ___ protocol.

<span lang='hi'>Internet access के लिए dial-up connections ___ protocol use करते हैं।</span>

- **(A)** PPP (Point to Point protocol) / PPP (Point to Point protocol) ✅ **(CORRECT)**
- **(B)** X.25 protocol / X.25 protocol
- **(C)** PLIP protocol / PLIP protocol
- **(D)** None of the above / इनमें से कोई नहीं

**✔ Correct Answer: (A) PPP (Point to Point protocol)** — Dial-up connections to access the Internet use PPP (Point-to-Point Protocol), which carries IP traffic over the telephone line.

*Internet access के लिए dial-up connections PPP (Point-to-Point Protocol) use करते हैं, जो telephone line पर IP traffic carry करता है।*

**★ Nukta (Key Point):** Dial-up Internet = PPP (Point-to-Point Protocol).

*Dial-up Internet = PPP (Point-to-Point Protocol).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q18] · Medium*

---
### Q112. When a resident uses a dial-up or DSL service to connect to the Internet, what is the role of the telephone company?

<span lang='hi'>जब कोई व्यक्ति Internet से जुड़ने के लिए dial-up या DSL service use करता है, तो telephone company की भूमिका क्या होती है?</span>

- **(A)** It provides the switching/connection path from the user to the ISP / वह user से ISP तक switching/connection path देती है ✅ **(CORRECT)**
- **(B)** It hosts every website the user visits / वह user की हर website host करती है
- **(C)** It assigns IP addresses to every website / वह हर website को IP address देती है
- **(D)** It encrypts all the user's data / वह user का सारा data encrypt करती है

**✔ Correct Answer: (A) It provides the switching/connection path from the user to the ISP** — Forouzan: with dial-up/DSL the telephone company is a switching service provider — it provides the local loop and connection path (circuit) from the customer to the ISP; the ISP connects to the Internet.

*Forouzan: dial-up/DSL में telephone company switching service provider है — वह customer से ISP तक local loop/connection path देती है; ISP Internet से जोड़ता है।*

**★ Nukta (Key Point):** Telephone company सिर्फ 'road' देती है (local loop + switching). Website hosting/IP assignment ISP/DNS का काम है.

*Telephone company सिर्फ रास्ता देती है (local loop + switching)। Website hosting/IP assignment ISP/DNS का काम है।*

*[Source: Forouzan Ch1 (Q1-14) — Practice Set] · Medium*

---
### Q113. Which of the following servers allows LAN users to share data?

<span lang='hi'>निम्नलिखित में से कौन सा server LAN users को data share करने की अनुमति देता है?</span>

- **(A)** Data server / data server
- **(B)** Point server / point server
- **(C)** File server / file server ✅ **(CORRECT)**
- **(D)** Communication server / communication server

**✔ Correct Answer: (C) File server** — A file server stores files and allows LAN users to share/access data (files) over the network.

*Ek file server files store करता है और LAN users को network पर data (files) share/access करने की अनुमति देता है।*

**★ Nukta (Key Point):** File server = files store + LAN users को share करने देता है.

*File server = files store करता है + LAN users को share करने देता है।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q22] · Medium*

---
### Q114. EDI stands for ____.

<span lang='hi'>EDI का पूरा नाम है ____.</span>

- **(A)** Electronic Data Interchange / Electronic Data Interchange ✅ **(CORRECT)**
- **(B)** Electronic Digital Internet / Electronic Digital Internet
- **(C)** Electronic Digital Interchange / Electronic Digital Interchange
- **(D)** Electronic Data Internet / Electronic Data Internet

**✔ Correct Answer: (A) Electronic Data Interchange** — EDI = Electronic Data Interchange - the computer-to-computer exchange of business documents (orders, invoices) in a stअंदरd electronic format.

*EDI = Electronic Data Interchange - business documents (orders, invoices) का computer-to-computer exchange, एक stअंदरd electronic format में.*

**★ Nukta (Key Point):** EDI = Electronic Data Interchange (business documents का e-exchange).

*EDI = Electronic Data Interchange (business documents का e-exchange).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q25] · Medium*

---
### Q115. The term UPnP is a short form of:

<span lang='hi'>UPnP term का पूरा नाम (full form) क्या है?</span>

- **(A)** Uniform Plug and Play / Uniform Plug and Play
- **(B)** Unit Plug and Play / Unit Plug and Play
- **(C)** Useful Plug and Play / Useful Plug and Play
- **(D)** Universal Plug and Play / Universal Plug and Play ✅ **(CORRECT)**

**✔ Correct Answer: (D) Universal Plug and Play** — UPnP = Universal Plug and Play — a set of networking protocols that lets devices discover each other and connect automatically (zero-configuration).

*UPnP = Universal Plug and Play — networking protocols का एक set जो devices को एक-दूसरे को automatically discover और connect (zero-configuration) करने देता है।*

**★ Nukta (Key Point):** UPnP = Universal Plug and Play (device auto-discovery). Compare: DHCP = auto IP configuration.

*UPnP = Universal Plug and Play (device auto-discovery)। तुलना: DHCP = auto IP configuration।*

*[Source: Repo: Unit Test-4 Solution (OCR), p11] · Medium*

---
### Q116. Consider the switching statements:
1. Circuit Switching establishes a dedicated path.
2. Packet Switching routes data in packets on different paths.
3. Message Switching uses store-and-forward.
Which statements are correct?

<span lang='hi'>Switching statements देखिए:
1. Circuit Switching dedicated path बनाता है।
2. Packet Switching data को packets में अलग paths पर भेजता है।
3. Message Switching store-and-forward use करता है।
कौन से statements सही हैं?</span>

- **(A)** 1 and 2 only / सिर्फ 1 और 2
- **(B)** 2 and 3 only / सिर्फ 2 और 3
- **(C)** 1 and 3 only / सिर्फ 1 और 3
- **(D)** 1, 2 and 3 / 1, 2 और 3 ✅ **(CORRECT)**

**✔ Correct Answer: (D) 1, 2 and 3** — All three correct: circuit switching sets up a dedicated end-to-end path; packet switching splits data into packets that may take different paths; message switching stores the whole message at each node and forwards it (store-and-forward).

*तीनों सही: circuit switching dedicated end-to-end path बनाता है; packet switching data को packets में बाँटकर अलग paths से भेजता है; message switching हर node पर पूरा message store करके आगे भेजता है।*

**★ Nukta (Key Point):** 3 switching types: Circuit (dedicated path), Packet (packets, अलग paths), Message (store-and-forward) — teeno statements correct.

*3 switching types: Circuit (dedicated path), Packet (packets, अलग paths), Message (store-and-forward) — तीनों सही।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

---
### Q117. All the information on the internet is passed using _______ switching method.

<span lang='hi'>Internet पर saari information _______ switching method से pass होती है।</span>

- **(A)** Portable / portable
- **(B)** Packets / packets ✅ **(CORRECT)**
- **(C)** Pouch / pouch
- **(D)** Primary / primary

**✔ Correct Answer: (B) Packets** — The Internet uses packet switching: data is broken into small packets that travel independently over the network and are reassembled at the destination.

*Internet packet switching use करता है: data को chhote packets में tod कर भेजा जाता है जो network पर independently travel करते हैं और destination पर reassemble होते हैं।*

**★ Nukta (Key Point):** Internet = packet switching. Circuit switching = dedicated path (old telephone).

*Internet = packet switching. Circuit switching = dedicated path (पुराना telephone).*

*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)] · Medium*

---
### Q118. Which technique breaks data into packets for transmission?

<span lang='hi'>Transmission के लिए data को packets में तोड़ने की technique कौन-सी है?</span>

- **(A)** Circuit switching / Circuit switching
- **(B)** Packet switching / Packet switching ✅ **(CORRECT)**
- **(C)** Frequency division multiplexing / Frequency division multiplexing
- **(D)** Time division multiplexing / Time division multiplexing

**✔ Correct Answer: (B) Packet switching** — Packet switching breaks the message into packets, sends each (possibly over different paths) and reassembles them at the destination. Circuit switching sends a continuous stream over a dedicated path; FDM/TDM are multiplexing techniques.

*Packet switching message को packets में तोड़ता है, हर packet भेजता है और destination पर जोड़ता है। Circuit switching dedicated path पर continuous stream भेजता है; FDM/TDM multiplexing techniques हैं।*

**★ Nukta (Key Point):** Internet packet switching पर चलता है — data packets में tootta है.

*Internet packet switching पर चलता है — data packets में टूटता है।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

---
### Q119. Home broadband connections that work on DSL (Digital Subscriber Line) use ___ protocol.

<span lang='hi'>DSL (Digital Subscriber Line) पर काम करने वाले home broadband connections ___ protocol use करते हैं।</span>

- **(A)** PPPoE (PPP over Ethernet) / PPPoE (PPP over Ethernet) ✅ **(CORRECT)**
- **(B)** PPPoA (PPP over ATM) / PPPoA (PPP over ATM)
- **(C)** Bridge protocol / bridge protocol
- **(D)** All of the above / ऊपर दिए गए सभी

**✔ Correct Answer: (A) PPPoE (PPP over Ethernet)** — Home DSL broadband connections typically use PPPoE (PPP over Ethernet) to carry PPP traffic over the DSL/Ethernet connection.

*Home DSL broadband connections आम तौर पर PPPoE (PPP over Ethernet) use करते हैं ताकि PPP traffic DSL/Ethernet connection पर carry हो sake।*

**★ Nukta (Key Point):** Home DSL broadband = PPPoE (PPP over Ethernet).

*Home DSL broadband = PPPoE (PPP over Ethernet).*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q19] · Hard*

---
### Q120. A computer network permits sharing of:

<span lang='hi'>एक computer network किस चीज़ की sharing की अनुमति देता है?</span>

- **(A)** Resources / resources (printer, disk, etc.)
- **(B)** Information / information (data)
- **(C)** Both a & b / दोनों a और b ✅ **(CORRECT)**
- **(D)** None of these / इनमें से कोई नहीं

**✔ Correct Answer: (C) Both a & b** — A computer network permits sharing of both resources (printers, storage, devices) and information (data/messages) among connected users.

*Ek computer network दोनों cheezon की sharing की अनुमति देता है: resources (printers, storage, devices) और information (data/messages), connected users के बीच।*

**★ Nukta (Key Point):** Network = resources + information sharing.

*Network = resources + information sharing.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q47 / CN Topic Test-02 (UNIT TEST-2), Q47] · Hard*

---
### Q121. Which of the following is a benefit of networking?

<span lang='hi'>Networking का कौन-सा लाभ (benefit) है?</span>

- **(A)** File sharing / File sharing
- **(B)** Easier access to resources / resources तक आसान पहुँच
- **(C)** Easier backups / आसान backups
- **(D)** All of the above / ऊपर दिए गए सभी ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the above** — Computer networks allow file sharing, easy access to shared resources (printers, servers, internet) and easier centralised backups — so all of these are benefits.

*Computer networks file sharing, shared resources (printers, server, internet) तक आसान पहुँच, और आसान centralised backups की अनुमति देते हैं — इसलिए ये सभी लाभ हैं।*

**★ Nukta (Key Point):** Networking benefits: sharing (files/resources/peripherals) + communication + backup + cost saving. Exam favourite: "All of the above".

*Networking के लाभ: sharing (files/resources/peripherals) + communication + backup + cost saving। Exam favourite: "All of the above"।*

*[Source: InstrumentationTools 150 CN MCQs] · Hard*

---
### Q122. How many digits of the Data Network Identification Code (DNIC) identify the country?

<span lang='hi'>Data Network Identification Code (DNIC) के kitne digits देश (country) की पहचान करते हैं?</span>

- **(A)** first three / पहले तीन ✅ **(CORRECT)**
- **(B)** first four / पहले चार
- **(C)** first five / पहले पाँच
- **(D)** first six / पहले छह

**✔ Correct Answer: (A) first three** — In the DNIC (used in X.121 addressing), the first three digits are the country code and the fourth digit identifies the network within that country. So the first three digits identify the country.

*DNIC (X.121 addressing में use होता है) में पहले तीन digits country code होते हैं और चौथा digit उस देश के अंदर के network की पहचान करता है। इसलिए पहले तीन digits देश की पहचान करते हैं।*

**★ Nukta (Key Point):** DNIC: first 3 digits = country code, 4th digit = network code.

*DNIC: पहले 3 digits = country code, चौथा digit = network code.*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q15] · Hard*

---
### Q123. Which of the following is true for Circuit Switching handling multiple simultaneous connections?

<span lang='hi'>एक साथ अनेक connections संभालते समय Circuit Switching के बारे में क्या सही है?</span>

- **(A)** A single path is used and shared for all data / एक ही path सभी data के लिए share होता है
- **(B)** All connections are multiplexed into a single channel / सभी connections एक channel में multiplex होते हैं
- **(C)** It encodes all data into a single channel / यह सारे data को एक channel में encode करता है
- **(D)** Separate physical paths are allocated for each channel / हर channel के लिए अलग physical paths दिए जाते हैं ✅ **(CORRECT)**

**✔ Correct Answer: (D) Separate physical paths are allocated for each channel** — In circuit switching each connection gets its own dedicated physical path for the whole duration — multiple simultaneous connections mean multiple separate paths (as in the traditional telephone network). (Matches the official RPSC key.)

*Circuit switching में हर connection को पूरे समय के लिए अपना dedicated physical path मिलता है — एक साथ अनेक connections = अलग-अलग paths (पारंपरिक telephone network जैसा)। (Official RPSC key से match.)*

**★ Nukta (Key Point):** Circuit switching = हर connection का apna अलग path. Packet switching = shared medium, packets अलग paths से.

*Circuit switching = हर connection का अपना अलग path। Packet switching = shared medium, packets अलग paths से।*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

---

## ★ Nukte Rapid-Fire — Exam Pointers

- **5 components of data communication?** *(Data communication के 5 components?)* → **Message, Sender, Receiver, Medium, Protocol** *(Message, Sender, Receiver, Medium, Protocol)*
- **3 criteria of a good network?** *(अच्छे network के 3 criteria?)* → **Performance, Reliability, Security** *(Performance, Reliability, Security)*
- **4 characteristics of data communication?** *(Data communication के 4 characteristics?)* → **Delivery, Accuracy, Timeliness, Jitter** *(Delivery, Accuracy, Timeliness, Jitter)*
- **Jitter means?** *(Jitter का अर्थ?)* → **Delay variation between packets** *(Packets के बीच delay का बदलाव)*
- **Protocol elements?** *(Protocol के elements?)* → **Syntax, Semantics, Timing** *(Syntax, Semantics, Timing)*
- **Simplex example?** *(Simplex का उदाहरण?)* → **TV broadcast / keyboard→monitor (one-way)** *(TV broadcast / keyboard→monitor (one-way))*
- **Half-Duplex example?** *(Half-Duplex का उदाहरण?)* → **Walkie-talkie (both ways, one at a time)** *(Walkie-talkie (दोनों तरफ़, पर एक समय में एक))*
- **Full-Duplex example?** *(Full-Duplex का उदाहरण?)* → **Telephone (both ways, same time)** *(Telephone (दोनों तरफ़, एक साथ))*
- **Mesh cables formula?** *(Mesh cables का formula?)* → **n(n-1)/2 cables, n-1 ports per device** *(n(n-1)/2 cables, n-1 ports per device)*
- **Star / Ring / Bus cables?** *(Star / Ring / Bus cables?)* → **Star = n, Ring = n, Bus = 1** *(Star = n, Ring = n, Bus = 1)*
- **Most fault-tolerant topology?** *(सबसे ज़्यादा fault-tolerant topology?)* → **Mesh (redundant paths)** *(Mesh (redundant paths))*
- **Easy to install & reconfigure?** *(Install/reconfigure में आसान?)* → **Star topology** *(Star topology)*
- **Multipoint topology?** *(Multipoint topology?)* → **Bus (shared backbone)** *(Bus (shared backbone))*
- **IEEE 802.2 / 802.3 / 802.5 / 802.11?** *(IEEE 802.2 / 802.3 / 802.5 / 802.11?)* → **LLC / Ethernet(MAC) / Token Ring / Wi-Fi** *(LLC / Ethernet(MAC) / Token Ring / Wi-Fi)*
- **Network size order?** *(Network size का क्रम?)* → **PAN < LAN < MAN < WAN** *(PAN < LAN < MAN < WAN)*
- **internet vs Internet?** *(internet बनाम Internet?)* → **Any network of networks vs THE global one** *(कोई भी network of networks बनाम वह विश्वव्यापी)*
- **Intranet vs Extranet?** *(Intranet बनाम Extranet?)* → **Intranet = inside the organisation; Extranet = trusted outsiders (supplier)** *(Intranet = संस्था के अंदर; Extranet = भरोसेमंद बाहरी (supplier))*
- **Client-Server vs P2P examples?** *(Client-Server बनाम P2P उदाहरण?)* → **ATM = Client-Server; BitTorrent = P2P** *(ATM = Client-Server; BitTorrent = P2P)*
- **ARPANET facts?** *(ARPANET तथ्य?)* → **1969 (ARPA); TCP/IP adopted 1983; WWW 1991 (CERN, Tim Berners-Lee)** *(1969 (ARPA); TCP/IP adopted 1983; WWW 1991 (CERN, Tim Berners-Lee))*
- **Internet switching?** *(Internet कौन-सी switching use करता है?)* → **Packet switching (data travels in packets)** *(Packet switching (data packets में चलता है))*
- **Circuit switching key?** *(Circuit switching की कुंजी?)* → **Dedicated separate physical path per connection** *(हर connection का dedicated अलग physical path)*

