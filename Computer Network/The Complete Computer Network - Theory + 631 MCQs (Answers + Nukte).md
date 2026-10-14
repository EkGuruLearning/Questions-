# Data Communication & Computer Networks (CN) — The Complete Book

## Theory + 627 MCQs (English + Hindi) — Topic 1 to 7

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** RPSC Programmer • ACP • RSMSSB IA • SA • DD • BCI • SCI • REET • RAS • DSSSB • KVS • NVS • HTET • SSC CGL/CHSL • RRB • IBPS • UPSC & all Rajasthan + Central Govt. Exams (Computer Awareness)

Format: har section mein pehle **समझ (Theory)**, phir questions **Easy → Medium → Hard**.
Question row: left = question + options | right = **✔ answer + ★ Nukte**.

# TOPIC 1 — Introduction of Data Communication

## Section A - DC Components & Protocol Basics (Message, Sender, Receiver, Transmission Medium, Protocol)

*Syllabus: DC Components - Message, Sender, Receiver, Transmission Medium, Protocol*

**Data Communication = do devices ke beech message ka exchange. Iske 5 components hote hain aur communication rules ko protocol kehte hain.**

*Data Communication का अर्थ है दो उपकरणों के बीच message का आदान-प्रदान। इसके 5 components होते हैं और संचार के नियमों को protocol कहते हैं।*

- Message — information (data) jo bheji jaati hai: text, number, picture, audio, video.
  - *Message — वह सूचना (data) जो भेजी जाती है: text, number, picture, audio, video.*
- Sender (source) — device jo message bhejta hai; Receiver (destination) — jise message milta hai.
  - *Sender (source) — message भेजने वाला उपकरण; Receiver (destination) — जिसे message मिलता है।*
- Transmission medium — rasta jisse message jaata hai (guided: wire/cable; unguided: wireless).
  - *Transmission medium — वह माध्यम जिससे message जाता है (guided: तार/cable; unguided: wireless)।*
- Protocol = communication ke rules (agreed set of rules). Har protocol mein 3 cheezein: Syntax (format/order), Semantics (har section ka meaning), Timing (speed + order).
  - *Protocol = संचार के नियमों का समुच्चय। हर protocol में 3 चीज़ें: Syntax (format/order), Semantics (भागों का अर्थ), Timing (गति + क्रम)।*
- Network = devices (nodes) + connecting links; data ko share karne ke liye banaya jata hai.
  - *Network = उपकरण (nodes) + जोड़ने वाली links; data साझा करने के लिए बनाया जाता है।*
- Data flow direction ko transmission mode kehte hain (Simplex / Half-Duplex / Full-Duplex) — yeh Section C mein hai.
  - *Data की दिशा को transmission mode कहते हैं (Simplex / Half-Duplex / Full-Duplex) — यह Section C में है।*

| Component | Kaam (work) |
|---|---|
| Message | data jo jaana hai — the information |
| Sender | message ko bhejta hai — source device |
| Receiver | message ko paata hai — destination device |
| Transmission medium | message ka rasta — guided / unguided |
| Protocol | communication ke rules — syntax, semantics, timing |

### Questions (Easy → Medium → Hard)

**Q1.** The physical path between the sender and receiver is called:
*Sender और receiver के बीच का physical path _______ कहलाता है:*
- **(A)** Link / link (link)
- **(B)** Node / node (node)
- **(C)** Segment / सегмент (segment)
- **(D)** Socket / सॉकेट (socket)
✔ **(A) Link**
★ **Nukta:** Note: In Forouzan's 5 components, this same physical path is called the transmission medium. Both terms mean the physical path.
*Note: Forouzan के 5 components में इसी physical path को transmission medium कहा गया है। दोनों का मतलब physical path ही है।*
*[Source: Repo: BCI_SCI Subject Test-7 (UNIT TEST-2 BCI/SCI), Q20] · Easy*

**Q2.** Identify the five components of a data communication system.
*Data communication system के पाँच components की पहचान कीजिए।*
- **(A)** Message, Sender, Receiver, Transmission medium, Protocol
- **(B)** Message, Router, Switch, Cable, Software
- **(C)** Data, Sender, Receiver, Hub, TCP/IP
- **(D)** Message, Sender, Receiver, Software, Hardware
✔ **(A) Message, Sender, Receiver, Transmission medium, Protocol**
★ **Nukta:** 5 components: Message → Sender → Medium → Receiver + Protocol (rules). सबसे favourite exam question.
*5 components: Message → Sender → Medium → Receiver + Protocol (rules)। Exam का favourite question।*
*[Source: Forouzan Ch1 (Q1-1) — Practice Set] · Medium*

**Q3.** The _______ is the physical path over which a message travels from sender to receiver.
*_______ वह physical path है जिस पर message sender से receiver तक जाता है।*
- **(A)** Path / पथ
- **(B)** Medium
- **(C)** Protocol
- **(D)** Route / रूट (path)
✔ **(B) Medium**
★ **Nukta:** Medium = physical path between sender and receiver. Remember: Message -> Sender -> Medium -> Receiver.
*Medium = sender और receiver के बीच का physical path. याद रखें: Message -> Sender -> Medium -> Receiver.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q35] · Medium*

**Q4.** The information to be communicated in a data communication system is called the _______.
*Data communication system में communicate की जाने वाली information _______ कहलाती है।*
- **(A)** Medium
- **(B)** Protocol
- **(C)** Message / message (message)
- **(D)** Transmission / संचरण (transmission)
✔ **(C) Message**
★ **Nukta:** Message = the data/information to be communicated. 5 popular forms: text, numbers, images, audio, video.
*Message = communicate की जाने वाली data. 5 popular forms: text, numbers, images, audio, video.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q38] · Medium*

**Q5.** Which of the following shares the data of two computers?
*निम्नलिखित में से कौन दो computers का data share (साझा) करता है?*
- **(A)** Library / पुस्तकालय
- **(B)** Network
- **(C)** Grouping / समूह (grouping)
- **(D)** Integrated system / एकीकृत प्रणाली
✔ **(B) Network**
★ **Nukta:** Network = 2 or more devices connected to share data/resources.
*Network = 2 या ज़्यादा devices का आपस में जुड़ना, data/resources share करने के लिए।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q13] · Medium*

**Q6.** _______ refers to two characteristics: when data should be sent and how fast it can be sent.
*_______ दो characteristics को बताता है: data कब भेजा जाए और कितनी तेज़ी से भेजा जा सकता है।*
- **(A)** Semantics / अर्थ (semantics)
- **(B)** Syntax / संरचना (syntax)
- **(C)** Timing / समय-निर्धारण (timing)
- **(D)** none of the above / इनमें से कोई नहीं
✔ **(C) Timing**
★ **Nukta:** Protocol के 3 elements = Syntax (format), Semantics (meaning), Timing (when & how fast).
*Protocol के 3 elements = Syntax (format), Semantics (अर्थ), Timing (कब और कितनी तेज़ी से).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q44] · Medium*

**Q7.** What are the main elements of a protocol? 1. Syntax  2. Semantics  3. Timing
*किसी protocol के मुख्य तत्व (elements) क्या हैं? 1. Syntax  2. Semantics  3. Timing*
- **(A)** 1, 2 only / सिर्फ 1 और 2
- **(B)** 1, 3 only / सिर्फ 1 और 3
- **(C)** 2, 3 only / सिर्फ 2 और 3
- **(D)** 1, 2, 3 only / 1, 2 और 3 सभी
✔ **(D) 1, 2, 3 only**
★ **Nukta:** याद रखें: Protocol = Syntax + Semantics + Timing.
*याद रखें: Protocol = Syntax + Semantics + Timing.*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q3] · Medium*

**Q8.** Why are protocols needed in data communication?
*Data communication में protocols की आवश्यकता क्यों होती है?*
- **(A)** To enable communication between different types of systems by providing common rules / अलग-अलग प्रकार की systems के बीच communication के लिए common rules देना
- **(B)** To increase the processing speed of the CPU / CPU की processing speed बढ़ाने के लिए
- **(C)** To convert every message into a common language / हर message को एक common language में बदलने के लिए
- **(D)** Protocols are optional — devices can communicate without rules / Protocols optional हैं — बिना rules के भी devices communicate कर सकती हैं
✔ **(A) To enable communication between different types of systems by providing common rules**
★ **Nukta:** Protocol = agreement of rules (syntax + semantics + timing). Iske बिना communication impossible.
*Protocol = rules का agreement (syntax + semantics + timing)। इसके बिना communication impossible है।*
*[Source: Forouzan Ch1 (Q1-11) — Practice Set] · Medium*

**Q9.** A set of rules that governs data communication is called a:
*Data communication को regulate (नियंत्रित) करने वाले rules का set _______ कहलाता है:*
- **(A)** rule / नियम (rule)
- **(B)** medium / medium (medium)
- **(C)** Link / link (link)
- **(D)** Protocol / protocol (protocol)
✔ **(D) Protocol**
★ **Nukta:** Protocol = rules का set. याद रखें: without a protocol, two devices may be connected but cannot communicate.
*Protocol = नियमों का set. याद रखें: बिना protocol के दो devices जुड़े to हो सकते हैं लेकिन communicate नहीं कर सकते।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3), Q15] · Medium*

**Q10.** Consider: (1) Twisted pair cables (2) Microwaves and satellite signals (3) Repeaters (4) Analog transmissions (5) Fiber optics. Which of the above is considered as signal transmission medium in data communications?
*विचार करें: (1) Twisted pair cables (2) Microwaves और satellite signals (3) Repeaters (4) Analog transmissions (5) Fiber optics। उपरोक्त में से data communications में signal transmission medium के रूप में क्या माना जाता है?*
- **(A)** (1) and (5) / (1) और (5)
- **(B)** (1) and (2) / (1) और (2)
- **(C)** (1), (2) and (5) / (1), (2) और (5)
- **(D)** (1), (2), (3) and (5) / (1), (2), (3) और (5)
✔ **(C) (1), (2) and (5)**
★ **Nukta:** Guided media: twisted pair, coaxial, fiber. Unguided media: radio, microwave, infrared.
*Guided media: twisted pair, coaxial, fiber. Unguided media: radio, microwave, infrared.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q10] · Medium*

**Q11.** Data communication is the exchange of _______ between two devices via some form of transmission medium.
*Data communication = do devices के बीच _______ का exchange, किसी transmission medium के through।*
- **(A)** only text messages / सिर्फ text messages
- **(B)** data (the message) - text, numbers, images, audio or video / data (message) - text, numbers, images, audio या video
- **(C)** only electrical signals / सिर्फ electrical signals
- **(D)** only hardware devices / सिर्फ hardware devices
✔ **(B) data (the message) - text, numbers, images, audio or video**
★ **Nukta:** Data communication = exchange of DATA (message) between two devices over a medium.
*Data communication = do devices के बीच DATA (message) का exchange, medium के through।*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q12.** The device that sends the data message in a data communication system is called the _______.
*Data communication system में जो device data message भेजता है, use _______ कहते हैं।*
- **(A)** Receiver / Receiver (प्राप्तकर्ता)
- **(B)** Sender / Sender (प्रेषक)
- **(C)** Protocol / Protocol (protocol)
- **(D)** Hub / Hub (hub)
✔ **(B) Sender**
★ **Nukta:** Sender = source device; Receiver = destination device.
*Sender = source device; Receiver = destination device.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q13.** Which of the following best lists the popular forms of information (message) in data communication?
*Data communication में information (message) के popular forms को सबसे achhe से कौन बताता है?*
- **(A)** Only text and numbers / सिर्फ text और numbers
- **(B)** Only audio and video / सिर्फ audio और video
- **(C)** Text, numbers, images, audio and video / text, numbers, images, audio और video
- **(D)** Only binary digits / सिर्फ binary digits
✔ **(C) Text, numbers, images, audio and video**
★ **Nukta:** 5 popular forms of message: text, numbers, images, audio, video.
*Message के 5 popular forms: text, numbers, images, audio, video.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q14.** ARPANET stands for:
*ARPANET का पूरा नाम है:*
- **(A)** Advanced Research Projects Agency Network
- **(B)** Advanced Recheck Projects Agency Internet
- **(C)** American Research Projects Agency Network
- **(D)** Advanced Research Protocol Agency Network
✔ **(A) Advanced Research Projects Agency Network**
★ **Nukta:** This is the network on which TCP/IP was later installed — the grandmother of the Internet.
*यही वह network है जिस पर TCP/IP बाद में लगाया गया — Internet की दादी.*
*[Source: IBPS/SBI computer-awareness banks (via tpointtech & meritnotes)] · Medium*

**Q15.** In a computer network, nodes are:
*Computer network में nodes होते हैं:*
- **(A)** the computer that originates the data / जो computer data को originate (shurua) करता है
- **(B)** the computer that routes the data / जो computer data को route करता है
- **(C)** the computer that terminates the data / जो computer data को terminate (समाप्त) करता है
- **(D)** all of the mentioned / उपर्युक्त सभी (all of the above)
✔ **(D) all of the mentioned**
★ **Nukta:** Node = any connected device of the network (computer, printer, router, etc.).
*Node = network का कोई भी connected device (computer, printer, router, आदि).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q30] · Hard*

**Q16.** Consider the statements: S1: The physical medium of connection is known as a link. S2: The computers connected to it are known as nodes.
*कथनों पर विचार करें: S1: connection का physical medium link कहलाता है। S2: इससे जुड़े computers nodes कहलाते हैं।*
- **(A)** Both S1 and S2 are false / दोनों S1 और S2 ग़लत हैं
- **(B)** S1 true but S2 false / S1 सही है लेकिन S2 ग़लत है
- **(C)** S1 false but S2 true / S1 ग़लत है लेकिन S2 सही है
- **(D)** Both S1 and S2 true / दोनों S1 और S2 सही हैं
✔ **(D) Both S1 and S2 true**
★ **Nukta:** Link = physical medium; Node = connected device (computer).
*Link = physical medium; Node = जुड़ा हुआ device (computer).*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q2] · Hard*

**Q17.** Which one of the following is NOT one of the five basic components of a data communication system?
*निम्नलिखित में से कौन data communication system के five basic components में से एक नहीं है?*
- **(A)** Message / Message (message)
- **(B)** Protocol / Protocol (protocol)
- **(C)** Router / Router (router)
- **(D)** Transmission medium / Transmission medium (medium)
✔ **(C) Router**
★ **Nukta:** याद रखें 5 components: Message, Sender, Receiver, Transmission Medium, Protocol. Router = device, component नहीं।
*याद रखें 5 components: Message, Sender, Receiver, Transmission Medium, Protocol. Router = device है, component नहीं।*
*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

## Section B - Characteristics (Delivery, Accuracy, Timeliness, Jitter) & Criteria (Performance, Reliability, Security)

*Syllabus: Characteristics - Delivery, Accuracy, Timeliness, Jitter | Properties/Criteria - Performance, Reliability, Security*

**Ek achhi communication service ki 4 characteristics hoti hain — Delivery, Accuracy, Timeliness, Jitter — aur service ko 3 criteria par taula jata hai: Performance, Reliability, Security.**

*अच्छी communication service की 4 characteristics होती हैं — Delivery, Accuracy, Timeliness, Jitter — और service को 3 criteria पर तौला जाता है: Performance, Reliability, Security।*

- Delivery — message sahi destination par pahunche (galat jagah nahi).
  - *Delivery — message सही destination पर पहुँचे (गलत जगह नहीं)।*
- Accuracy — data bina errors ke pahunche; corrupted data deliver nahi hona chahiye.
  - *Accuracy — data बिना त्रुटियों के पहुँचे; ख़राब data deliver नहीं होना चाहिए।*
- Timeliness — message time par pahunche, late nahi (real-time: audio/video).
  - *Timeliness — message समय पर पहुँचे (real-time: audio/video के लिए ज़रूरी)।*
- Jitter — packets ke beech delay ka variation; audio/video mein uneven playback ki wajah.
  - *Jitter — packets के बीच delay में उतार-चढ़ाव; audio/video में असमान playback का कारण।*
- Performance ko measure karte hain Throughput (asli data rate) aur Delay/Latency se; dono opposite hain — jyada load matlab kam throughput, jyada delay.
  - *Performance को Throughput (वास्तविक data rate) और Delay/Latency से नापते हैं; दोनों विपरीत चलते हैं।*
- Reliability = failure frequency + recovery speed (MTBF — mean time between failures).
  - *Reliability = विफलता की दर + ठीक होने की गति (MTBF)।*
- Security = data ko unauthorized access/modification/destruction se bachana (encryption, password, firewall).
  - *Security = data को unauthorized access/modification/destruction से बचाना (encryption, password, firewall)।*

| Characteristic | Matlab (meaning) |
|---|---|
| Delivery | sahi jagah pahunchna |
| Accuracy | bina error ke |
| Timeliness | time par |
| Jitter | delay ka variation (uneven delay) |

### Questions (Easy → Medium → Hard)

**Q18.** Which physical layer impairment mainly causes jitter in VoIP traffic?
*VoIP traffic में jitter का मुख्य kaaran कौन सा physical layer impairment है?*
- **(A)** Attenuation / attenuation (signal की shakti कम होना)
- **(B)** Delay variation / delay का अंतर (variation)
- **(C)** Distortion / distortion (vikriti)
- **(D)** Crosstalk
✔ **(B) Delay variation**
★ **Nukta:** Jitter = delay variation. Attenuation = signal weakening; distortion = signal shape change; crosstalk = interference from nearby cables.
*Jitter = delay variation. Attenuation = signal की shakti कम होना; distortion = signal का रूप badalna; crosstalk = पास की cables से interference.*
*[Source: Repo: BCI Subject Test-8 (UNIT TEST-3 BCI/SCI), Q36] · Easy*

**Q19.** What does jitter refer to in data communication?
*Data communication में jitter का मतलब क्या होता है?*
- **(A)** Loss of data / data का loss
- **(B)** Delay variation in packets / packets में delay का अंतर (variation)
- **(C)** Data synchronization / data का synchronization
- **(D)** Data encoding / data का encoding
✔ **(B) Delay variation in packets**
★ **Nukta:** Jitter = uneven delay in packet arrival -> distorted audio/video playback.
*Jitter = packet पहुँचने में uneven delay -> audio/video playback ख़राब हो जाती है।*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q1] · Medium*

**Q20.** Which of the following is a characteristic of data communication?
*निम्नलिखित में से कौन data communication की एक characteristic (विशेषता) है?*
- **(A)** Timeliness / समयपालन (timeliness)
- **(B)** Delay / деری (delay)
- **(C)** Speed / गति (speed)
- **(D)** Size / आकार (size)
✔ **(A) Timeliness**
★ **Nukta:** 4 characteristics याद रखो: Delivery, Accuracy, Timeliness, Jitter.
*4 characteristics याद रखो: Delivery, Accuracy, Timeliness, Jitter.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q6] · Medium*

**Q21.** What is the maximum data rate of a transmission medium known as?
*Transmission medium की अधिकतम data rate को क्या कहा जाता है?*
- **(A)** Bandwidth
- **(B)** Throughput
- **(C)** Latency
- **(D)** Jitter
✔ **(A) Bandwidth**
★ **Nukta:** Bandwidth = maximum capacity of the channel (in bps). Throughput = actual rate achieved (usually less).
*Bandwidth = channel की अधिकतम capacity (bps में). Throughput = वास्तविक रूप से हासिल होने वाली rate (आम तौर पर कम).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q9] · Medium*

**Q22.** Speed of an internet connection is measured in:
*Internet connection की speed किसमें मापी जाती है?*
- **(A)** Kilobits per second (kbps)
- **(B)** Kilobytes per second (KB/s) only / केवल Kilobytes per second (KB/s)
- **(C)** Metres per second
- **(D)** Hertz
✔ **(A) Kilobits per second (kbps)**
★ **Nukta:** Speed = bits per second (bps family). KB/s (bytes) is for file-size/download display — exam answer is kbps.
*Speed = bits per second (bps family)। KB/s (bytes) file-size/download display के लिए है — exam का answer kbps है।*
*[Source: Repo: Unit Test-4 Solution (OCR), p19] · Medium*

**Q23.** Frequency of failure and network recovery time after a failure are measures of the _______ of a network.
*Failure की आवृत्ति (frequency) और failure के बाद network recovery time किस चीज़ के measures हैं?*
- **(A)** Performance
- **(B)** Reliability
- **(C)** Security
- **(D)** Feasibility
✔ **(B) Reliability**
★ **Nukta:** Reliability = failure frequency + recovery time + robustness. Performance = transit time, response time, throughput, delay.
*Reliability = failure frequency + recovery time + robustness. Performance = transit time, response time, throughput, delay.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q39] · Medium*

**Q24.** What is the criteria to check the reliability of a network? 1. Downtime  2. Failure Frequency  3. Fault Tolerance  4. Security
*Network की reliability check करने के criteria क्या हैं? 1. Downtime  2. Failure Frequency  3. Fault Tolerance  4. Security*
- **(A)** 1, 2, 3 only / सिर्फ 1, 2, 3
- **(B)** 2, 3, 4 only / सिर्फ 2, 3, 4
- **(C)** 1, 2, 4 only / सिर्फ 1, 2, 4
- **(D)** 1, 2, 3, 4 only / 1, 2, 3, 4 सभी
✔ **(A) 1, 2, 3 only**
★ **Nukta:** 3 network criteria: Performance, Reliability, Security. Reliability = failure frequency + recovery time + fault tolerance.
*3 network criteria: Performance, Reliability, Security. Reliability = failure frequency + recovery time + fault tolerance.*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q1] · Medium*

**Q25.** What are the three criteria necessary for an effective and efficient network?
*Effective और efficient network के लिए आवश्यक तीन criteria क्या हैं?*
- **(A)** Performance, Reliability, Security
- **(B)** Delivery, Accuracy, Timeliness
- **(C)** Speed, Cost, Size
- **(D)** Message, Sender, Receiver
✔ **(A) Performance, Reliability, Security**
★ **Nukta:** Network के 3 CRITERIA = Performance, Reliability, Security. Data communication के 4 CHARACTERISTICS = Delivery, Accuracy, Timeliness, Jitter. दोनों को confuse मत करना!
*Network के 3 criteria = Performance, Reliability, Security। Data communication के 4 characteristics = Delivery, Accuracy, Timeliness, Jitter।*
*[Source: Forouzan Ch1 (Q1-2) — Practice Set] · Medium*

**Q26.** What network property is achieved through the use of the Automatic Repeat reQuest (ARQ) mechanism?
*Automatic Repeat reQuest (ARQ) mechanism से network की कौन सी property हासिल होती है?*
- **(A)** Reliability
- **(B)** Availability
- **(C)** Confidentiality
- **(D)** Scalability
✔ **(A) Reliability**
★ **Nukta:** ARQ = error control -> Reliability. Flow control = efficient delivery (no overflow).
*ARQ = error control -> Reliability. Flow control = efficient delivery (receiver का buffer overflow नहीं होना).*
*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)] · Medium*

**Q27.** For effective data communication, the system must deliver data to the correct destination. This characteristic is called _______.
*Effective data communication के लिए system को data सही destination पर पहुँचाना चाहिए। Is characteristic को _______ कहते हैं।*
- **(A)** Accuracy
- **(B)** Timeliness
- **(C)** Delivery
- **(D)** Jitter
✔ **(C) Delivery**
★ **Nukta:** 4 characteristics: Delivery (right destination), Accuracy (error-free), Timeliness (on time), Jitter (even delay).
*4 characteristics: Delivery (सही jagah), Accuracy (error-free), Timeliness (time पर), Jitter (even delay).*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q28.** Data delivered late is useless (especially in real-time audio/video). Delivering data in a timely manner is called _______.
*देर से पहुँचने वाला data बेकार है (ख़ास कर real-time audio/video में)। Time पर data pahunchane को _______ कहते हैं।*
- **(A)** Delivery
- **(B)** Accuracy
- **(C)** Timeliness
- **(D)** Jitter
✔ **(C) Timeliness**
★ **Nukta:** Timeliness = on-time delivery; late data is useless -> real-time transmission (audio/video).
*Timeliness = time पर पहुँचाना; देर वाला data बेकार है -> real-time transmission (audio/video).*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q29.** The network criterion measured by transit time, response time, throughput and delay is called _______.
*Transit time, response time, throughput और delay से maape jane वाले network criterion को _______ कहते हैं।*
- **(A)** Performance
- **(B)** Reliability
- **(C)** Security
- **(D)** Delivery
✔ **(A) Performance**
★ **Nukta:** Performance = transit time + response time (throughput & delay are related measures).
*Performance = transit time + response time (throughput और delay isse जुड़े measures हैं).*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q30.** Accuracy in data communication means:
*Data communication में accuracy का अर्थ है:*
- **(A)** Data is sent quickly / data तेज़ी से भेजा जाता है
- **(B)** Data is not corrupted / data corrupted (खराब) नहीं होता
- **(C)** Data is encrypted / data encrypt होता है
- **(D)** Data reaches the receiver / data receiver तक pahunchta है
✔ **(B) Data is not corrupted**
★ **Nukta:** Accuracy = error-free data; altered/corrupted data is useless.
*Accuracy = error-free data; बदल गया/corrupt data बेकार है।*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q8] · Hard*

**Q31.** An unauthorized user is a network _______ issue.
*An unauthorized user एक network _______ issue है.*
- **(A)** Performance
- **(B)** Reliability
- **(C)** Security
- **(D)** All of the above / ऊपर दिए गए सभी
✔ **(C) Security**
★ **Nukta:** Security = unauthorized access से बचाव + confidentiality + integrity (CIA triad).
*Security = unauthorized access से बचाव + confidentiality + integrity (CIA triad).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q40] · Hard*

**Q32.** Which of the following is NOT one of the three fundamental criteria (properties) that a network must meet?
*निम्नलिखित में से कौन network के तीन fundamental criteria (properties) में से एक नहीं है?*
- **(A)** Performance
- **(B)** Reliability
- **(C)** Security
- **(D)** Topology
✔ **(D) Topology**
★ **Nukta:** Network criteria = 3: Performance, Reliability, Security.
*Network criteria = 3: Performance, Reliability, Security.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

**Q33.** The capacity of a communication channel is measured in:
*Communication channel की क्षमता मापी जाती है:*
- **(A)** Bandwidth
- **(B)** Bit capacity
- **(C)** Volume
- **(D)** Noise
✔ **(A) Bandwidth**
★ **Nukta:** Channel capacity ↔ bandwidth (Hz या bps) — यही standard इकाई है.
*Channel capacity ↔ bandwidth (Hz या bps) — यही standard इकाई है.*
*[Source: KVS PGT/TGT/PRT computer banks 2018 (via jagranjosh)] · Hard*

**Q34.** Consider a 100 Mbps link between an earth station (sender) and a satellite (receiver) at an altitude of 2100 km. The signal propagates at 3×10⁸ m/s. The time taken (in milliseconds, rounded to two decimal places) for the receiver to completely receive a 1000-byte packet transmitted by the sender is ______.
*100 Mbps के link पर earth station से 2100 km ऊँचे satellite को 1000-byte packet भेजा गया; signal की speed 3×10⁸ m/s है। Receiver को packet पूरा मिलने में लगा समय (ms में, दो दशमलव) कितना है?*
- **(A)** 7.08
- **(B)** 2.10
- **(C)** 7.00
- **(D)** 21.08
✔ **(A) 7.08**
★ **Nukta:** Round-off trap: 2.10 sirf propagation ka fraction pakadta hai; 7.00 transmission time bhool jata hai.
*Round-off jaal: 2.10 sirf propagation; 7.00 mein transmission time chhoot jata hai.*
*[Source: GATE CS 2022] · Hard*

**Q35.** What is the bit rate for transmitting an uncompressed 800×600 pixel colour frame with 8 bits/pixel at 40 frames per second?
*बिना compression के 800×600 pixel वाला colour frame (8 bits/pixel) 40 frames per second पर transmit हो — bit rate कितना होगा?*
- **(A)** 2.4 Mbps
- **(B)** 153.6 Mbps
- **(C)** 15.36 Mbps
- **(D)** 1536 Mbps
✔ **(B) 153.6 Mbps**
★ **Nukta:** Decimal shift jaal: 15.36 aur 1536 bas decimal ki galti hain; 2.4 Mbps sirf pixel count se bina bits aur frames ke nikla hai.
*Decimal ki galtiyan: 15.36/1536; 2.4 Mbps bits aur frames bhool kar aata hai.*
*[Source: KVS PGT Computer Science 2017] · Hard*

**Q36.** An analog signal carries 4 bits in each signal unit. If 1000 signal units are sent per second, then the baud rate and bit rate of the signal are ______ and ______.
*एक analog signal हर signal unit में 4 bits रखता है। 1000 signal units per second भेजे जाएँ तो signal की baud rate और bit rate क्रमशः कितनी होगी?*
- **(A)** 4000 bauds/sec, 4000 bps
- **(B)** 1000 bauds/sec, 1000 bps
- **(C)** 4000 bauds/sec, 1000 bps
- **(D)** 1000 bauds/sec, 4000 bps
✔ **(D) 1000 bauds/sec, 4000 bps**
★ **Nukta:** Dono ko same mat samjho: 4000 bauds/4000 bps confusion hai; 4000 bauds/1000 bps ulta ratio hai.
*Dono alag hain: 4000/4000 confusion; 4000/1000 ulta hai.*
*[Source: KVS PGT Computer Science 2017] · Hard*

## Section C - Transmission Mode (Direction of Data Flow: Simplex, Half-Duplex, Full-Duplex)

*Syllabus: Transmission Mode - Simplex, Half-Duplex, Full-Duplex*

**Transmission mode batata hai ki data kis direction mein flow karta hai — simplex, half-duplex ya full-duplex.**

*Transmission mode बताता है कि data किस दिशा में बहता है — simplex, half-duplex या full-duplex।*

- Simplex — sirf ek direction; ek device sirf bhejta hai, doosra sirf paata hai (keyboard → monitor; TV/Radio broadcast).
  - *Simplex — केवल एक दिशा; एक उपकरण सिर्फ़ भेजता है, दूसरा सिर्फ़ पाता है (keyboard → monitor; TV/Radio)।*
- Half-Duplex — dono direction, par ek time par sirf ek taraf (walkie-talkie; one LAN, shared medium).
  - *Half-Duplex — दोनों दिशाएँ, पर एक समय में केवल एक तरफ़ (walkie-talkie)।*
- Full-Duplex — dono taraf ek saath; do do channels chahiye (telephone; modern LAN switches ke ports).
  - *Full-Duplex — दोनों तरफ़ एक साथ; दो channels चाहिए (telephone; switch ports)।*
- Half-duplex mein capacity waste hoti hai (ek taraf wait karna padta hai); full-duplex mein nahi.
  - *Half-duplex में capacity बेकार जाती है (प्रतीक्षा करनी पड़ती है); full-duplex में नहीं।*
- Yaad rakho: Simplex = one way; Half = both ways, one at a time; Full = both ways, together.
  - *याद रखो: Simplex = एक तरफ़; Half = दोनों, बारी-बारी; Full = दोनों, एक साथ।*

| Mode | Direction | Example |
|---|---|---|
| Simplex | एक तरफ़ ही (unidirectional) | Keyboard, monitor, radio |
| Half-Duplex | दोनों पर बारी-बारी | Walkie-talkie |
| Full-Duplex | दोनों एक साथ | Telephone, switch port |

### Questions (Easy → Medium → Hard)

**Q37.** Communication between a computer and a keyboard involves ______________ transmission.
*Computer और keyboard के बीच communication में ______________ transmission होता है।*
- **(A)** Automatic
- **(B)** Half-duplex
- **(C)** Half-duplex (variant) / half-duplex
- **(D)** Simplex
✔ **(D) Simplex**
★ **Nukta:** Keyboard -> Computer = simplex (one way). Examples: keyboard-monitor, TV broadcast.
*Keyboard -> Computer = simplex (एक तरफ़). Examples: keyboard-monitor, TV broadcast.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q33] · Medium*

**Q38.** A television broadcast is an example of _______ transmission.
*Television broadcast _______ transmission का एक example है।*
- **(A)** simplex
- **(B)** half-duplex
- **(C)** full-duplex
- **(D)** automatic
✔ **(A) simplex**
★ **Nukta:** TV/radio broadcast = simplex (station -> TV only, wapas नहीं).
*TV/radio broadcast = simplex (station -> TV ही, wapas नहीं).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q41] · Medium*

**Q39.** What is the mode of transmission where data flows in only one direction?
*Wo transmission mode kaunsa है जिसमें data सिर्फ एक direction में flow करता है?*
- **(A)** Simplex
- **(B)** Half-Duplex
- **(C)** Full-Duplex
- **(D)** Multiplex
✔ **(A) Simplex**
★ **Nukta:** Simplex = one-way only (keyboard to monitor, TV broadcast).
*Simplex = सिर्फ एक तरफ़ (keyboard to monitor, TV broadcast).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q3] · Medium*

**Q40.** Which transmission mode is used in walkie-talkie communication?
*Walkie-talkie communication में कौन सा transmission mode use होता है?*
- **(A)** Simplex
- **(B)** Half-Duplex
- **(C)** Full-Duplex
- **(D)** Multiplex
✔ **(B) Half-Duplex**
★ **Nukta:** Walkie-talkie = half-duplex (push-to-talk, एक समय में एक ही bolega).
*Walkie-talkie = half-duplex (push-to-talk, एक समय में एक ही bolega).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q10] · Medium*

**Q41.** Which of the following statements are TRUE?
1. Hubs operate in Half-Duplex mode.
2. Switches operate in Full-Duplex mode.
3. Routers broadcast by default.
*निम्नलिखित में से कौन से statements TRUE हैं?
1. Hubs Half-Duplex mode में काम करते हैं।
2. Switches Full-Duplex mode में काम करते हैं।
3. Routers by default broadcast करते हैं।*
- **(A)** 1 and 2 / 1 और 2
- **(B)** 2 and 3 / 2 और 3
- **(C)** 1 and 3 / 1 और 3
- **(D)** 1, 2 and 3 / 1, 2 और 3
✔ **(A) 1 and 2**
★ **Nukta:** Hub = half-duplex + एक collision domain; Switch = full-duplex + per-port collision domain; Router = broadcasts rokta है.
*Hub = Half-Duplex + एक collision domain; Switch = Full-Duplex + per-port collision domain; Router = broadcasts रोकता है।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

**Q42.** Which of the following transmission directions listed is not a legitimate channel?
*निम्नलिखित में से कौन सा transmission direction एक legitimate (vaidh) channel नहीं है?*
- **(A)** Simplex
- **(B)** Half Duplex
- **(C)** Full Duplex
- **(D)** Double Duplex
✔ **(D) Double Duplex**
★ **Nukta:** 3 transmission modes: Simplex, Half-Duplex, Full-Duplex. Double duplex = गलत.
*3 transmission modes: Simplex, Half-Duplex, Full-Duplex. Double duplex = गलत है।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q3] · Hard*

**Q43.** What is the difference between half-duplex and full-duplex transmission modes?
*Half-Duplex और Full-Duplex transmission modes में अंतर क्या है?*
- **(A)** Half-duplex allows only one-way flow; full-duplex also allows only one-way flow / Half-Duplex में सिर्फ one-way flow; Full-Duplex में भी सिर्फ one-way flow
- **(B)** Half-duplex flows both ways one direction at a time; full-duplex flows both ways at the same time / Half-Duplex में data दोनों तरफ़ पर एक समय में एक direction; Full-Duplex में एक साथ दोनों तरफ़
- **(C)** Half-duplex is only for wireless; full-duplex only for wired networks / Half-Duplex सिर्फ wireless के लिए; Full-Duplex सिर्फ wired के लिए
- **(D)** There is no difference between the two / दोनों में कोई अंतर नहीं है
✔ **(B) Half-duplex flows both ways one direction at a time; full-duplex flows both ways at the same time**
★ **Nukta:** Half = एक time पर एक ही side (walkie-talkie). Full = दोनों side एक साथ (telephone).
*Half = एक समय में एक side (walkie-talkie)। Full = दोनों side एक साथ (telephone)।*
*[Source: Forouzan Ch1 (Q1-6) — Practice Set] · Hard*

**Q44.** Data flow between two devices can occur in a _______ way.
*Do devices के बीच data flow _______ tareeke से हो सकता है।*
- **(A)** simplex
- **(B)** half-duplex
- **(C)** full-duplex
- **(D)** all of the above / ऊपर दिए गए सभी
✔ **(D) all of the above**
★ **Nukta:** 3 ways of data flow: simplex, half-duplex, full-duplex.
*Data flow के 3 tareeke: simplex, half-duplex, full-duplex.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q45] · Hard*

**Q45.** In a telephone conversation, both persons can speak and hear each other at the same time. This is an example of _______.
*Telephone conversation में दोनों persons एक साथ bol और sun सकते हैं। यह _______ का example है।*
- **(A)** Simplex
- **(B)** Half-duplex
- **(C)** Full-duplex
- **(D)** Unicast
✔ **(C) Full-duplex**
★ **Nukta:** Telephone = full-duplex (दोनों एक साथ bol और sun सकते हैं).
*Telephone = full-duplex (दोनों एक साथ bol और sun सकते हैं).*
*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

## Section D - Network Structure / Topology (Physical: Mesh, Star, Bus, Ring, Others; Logical: IEEE 802)

*Syllabus: Physical Topology - Mesh, Star, Bus, Ring, Others (Hybrid, Tree) | Logical Topology - IEEE 802*

**Network topology batata hai ki devices kis shape mein judi hain. Physical topology = asli wiring; Logical topology = data ka path/frame ka flow (IEEE 802 standards).**

*Network topology बताता है कि उपकरण किस आकार में जुड़े हैं। Physical topology = वास्तविक wiring; Logical topology = data का मार्ग (IEEE 802 standards)।*

- Mesh topology — har device ka har doosre device se dedicated link: n(n−1)/2 links, n(n−1)/2 ports per device. Robust + private, par costly aur wiring jyada.
  - *Mesh topology — हर उपकरण का हर दूसरे से dedicated link: n(n−1)/2 links। मज़बूत + निजी, पर महँगा और wiring अधिक।*
- Star topology — sab devices central hub/switch se jude: easy add/remove, ek link fail hone par sirf woh device; par central device fail = poora network down.
  - *Star topology — सब central hub/switch से जुड़े: जोड़ना-हटाना आसान; central device ख़राब = पूरा network बंद।*
- Bus topology — ek hi backbone cable; saste aur aasan; par backbone fail = poora network down, aur traffic jyada hone par performance girti hai.
  - *Bus topology — एक ही backbone cable; सस्ता; पर backbone टूटा = पूरा network बंद, भीड़ में performance कम।*
- Ring topology — devices ek circle mein; data ek direction mein token ke saath chalta hai; equal access milta hai.
  - *Ring topology — उपकरण वृत्त में; data एक दिशा में token के साथ चलता है; सबको बराबर मौक़ा।*
- Hybrid/Tree — in sab ka combination (star ka star).
  - *Hybrid/Tree — इन सब का मिश्रण (star का star)।*
- Logical topology standards: IEEE 802 (Ethernet = bus/logical bus; Token Ring = logical ring) — data ka flow logical topology se tay hota hai.
  - *Logical topology: IEEE 802 (Ethernet = logical bus; Token Ring = logical ring) — data का प्रवाह इसी से तय होता है।*

| Topology | Links / Feature | Kamzori (weakness) |
|---|---|---|
| Mesh | n(n−1)/2 dedicated links — robust | महँगा, ज़्यादा wiring |
| Star | central hub/switch — easy expand | central device = single point of failure |
| Bus | single backbone — sasta | backbone fail = all down |
| Ring | token, equal access | ek node fail = ring toot sakti hai |

### Questions (Easy → Medium → Hard)

**Q46.** IEEE 802.2 stअंदरd is related to which sub-layer?
*IEEE 802.2 stअंदरd किस sub-layer से संबंधित है?*
- **(A)** MAC Sublayer
- **(B)** LLC Sublayer
- **(C)** Physical Layer
- **(D)** Network Layer
✔ **(B) LLC Sublayer**
★ **Nukta:** 802.2 = LLC (upper sub-layer of Data Link). 802.3 = Ethernet/MAC, 802.5 = Token Ring, 802.11 = Wi-Fi.
*802.2 = LLC। 802.3 = Ethernet/MAC, 802.5 = Token Ring, 802.11 = Wi-Fi।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q47.** What are the advantages of star topology?
*Star topology के क्या advantages (लाभ) हैं?*
- **(A)** Less number of cables are required / कम number में cables चाहिए
- **(B)** More number of cables are required / ज़्यादा number में cables चाहिए
- **(C)** It is a distributed topology / यह एक distributed topology है
- **(D)** Security is high / security ज़्यादा है
✔ **(A) Less number of cables are required**
★ **Nukta:** Star = hub at centre, dedicated links, fewer cables (vs mesh), easy to install. But if hub fails, whole network goes down.
*Star = centre में hub, dedicated links, कम cables (mesh के muqable), install करना आसान. लेकिन hub fail हो गया toh पूरा network band हो जाता है।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q1] · Medium*

**Q48.** Which type of topology is best suited for large businesses which must carefully control and coordinate the operation of distributed branch outlets?
*Large businesses के लिए कौन सी topology सबसे उपयुक्त है, jahan distributed branch outlets के operation को carefully control और coordinate करना हो?*
- **(A)** Ring
- **(B)** Local area
- **(C)** Hierarchical / hierarchical (tree)
- **(D)** Star
✔ **(C) Hierarchical**
★ **Nukta:** Tree = hierarchical star. Large orgs with branches -> hierarchical/tree topology.
*Tree = hierarchical star. Badi sansthaon में branches के लिए -> hierarchical/tree topology.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q2] · Medium*

**Q49.** In a traditional ring network, repeaters are particularly associated with which topology because each station can regenerate and forward the signal?
*पारंपरिक ring network में repeaters किस topology से विशेष रूप से जुड़े हैं, क्योंकि हर station signal को regenerate और आगे भेज सकता है?*
- **(A)** Ring topology
- **(B)** Mesh topology
- **(C)** Bus topology
- **(D)** Star topology
✔ **(A) Ring topology**
★ **Nukta:** Concept-check correction of the old "repeater is used in ___ topology" stem (that wording wrongly implied repeaters are exclusive to one topology). Repeaters are Physical-layer devices usable on many links; the "traditional ring network" qualifier keeps the intended textbook answer (Ring) without the false universal claim. Not a verified PYQ.
*पुराने "repeater किस topology में" वाले प्रश्न का सुधार — repeater Physical-layer device है, हर link पर चलता है; "पारंपरिक ring" जोड़ने से अभीष्ट उत्तर (Ring) बना रहता है। यह सत्यापित PYQ नहीं है।*
*[Source: Practice — original (concept-check correction — not a verified PYQ)] · Medium*

**Q50.** What type of topology connects each node in a closed loop?
*कौन सी topology हर node को एक closed loop में जोड़ती है?*
- **(A)** Star
- **(B)** Mesh
- **(C)** Ring
- **(D)** Bus
✔ **(C) Ring**
★ **Nukta:** Ring = closed loop, one direction, token passing, each device = repeater.
*Ring = closed loop, एक direction, token passing, हर device = repeater.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q4] · Medium*

**Q51.** In a _______ topology, every device has a dedicated point-to-point link to every other device. For n devices, the number of links is n(n-1)/2 and each device needs n-1 I/O ports.
*_______ topology में हर device का हर दूसरे device से dedicated point-to-point link होता है। n devices के लिए links की संख्या n(n-1)/2 होती है और हर device को n-1 I/O ports चाहिए।*
- **(A)** Bus
- **(B)** Star
- **(C)** Ring
- **(D)** Mesh
✔ **(D) Mesh**
★ **Nukta:** Mesh formula (EXAM favourite): links = n(n-1)/2, ports per device = n-1. E.g., 5 devices -> 10 links.
*Mesh formula (EXAM favourite): links = n(n-1)/2, हर device के ports = n-1. Jaise 5 devices -> 10 links.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q52.** In a _______ topology, each device has a dedicated point-to-point link only to a central controller, usually called a hub (or switch).
*_______ topology में हर device का सिर्फ एक central controller (hub/switch) से dedicated point-to-point link होता है।*
- **(A)** Mesh
- **(B)** Ring
- **(C)** Star
- **(D)** Bus
✔ **(C) Star**
★ **Nukta:** Star = hub/switch at centre; easy to install & reconfigure; but if hub fails, the WHOLE network goes down.
*Star = centre में hub/switch; install और reconfigure करना आसान; लेकिन hub fail हो गया तो पूरा network बंद हो जाता है।*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q53.** Which network topology requires a multipoint connection?
*किस network topology में multipoint connection की आवश्यकता होती है?*
- **(A)** Ring
- **(B)** Bus
- **(C)** Star
- **(D)** Mesh
✔ **(B) Bus**
★ **Nukta:** Bus = multipoint (shared backbone). Mesh/Star/Ring = point-to-point links. Yahi difference exam में poochha जाता है.
*Bus = multipoint (shared backbone)। Mesh/Star/Ring = point-to-point links।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q54.** In a _______ topology, each device is connected to its two neighbours, data travels in one direction around the loop, and each device regenerates (repeats) the signal - this is called token passing.
*_______ topology में हर device अपने दो neighbours से जुड़ा होता है, data loop में एक ही direction में जाता है, और हर device signal को regenerate (repeat) करता है - इसे token passing कहते हैं।*
- **(A)** Bus
- **(B)** Ring
- **(C)** Star
- **(D)** Mesh
✔ **(B) Ring**
★ **Nukta:** Ring = loop, one direction, token passing, each device = repeater.
*Ring = loop, एक direction, token passing, हर device = repeater.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q55.** A network in which two or more different topologies are combined (e.g., a star connected to another star) is called a _______ topology, while a _______ topology is a hierarchy of stars (a variation of the star topology).
*जिसमें do या ज़्यादा अलग topologies combine हो (जैसे एक star दूसरे star से जुड़ा हो), use _______ topology कहते हैं, और _______ topology stars की hierarchy है (star topology का variation).*
- **(A)** Hybrid ; Tree
- **(B)** Tree ; Hybrid
- **(C)** Mesh ; Ring
- **(D)** Bus ; Star
✔ **(A) Hybrid ; Tree**
★ **Nukta:** Hybrid = mix of topologies; Tree = star of stars (hierarchical star).
*Hybrid = topologies का mix; Tree = star of stars (hierarchical star).*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q56.** Hierarchical topology, used to establish a network, is also known as a:
*Hierarchical topology, जिससे network स्थापित किया जाता है, किस नाम से भी जानी जाती है?*
- **(A)** Bus network
- **(B)** Star network
- **(C)** Tree network
- **(D)** Mesh network
✔ **(C) Tree network**
★ **Nukta:** Hierarchical = Tree = star-of-stars (root + branches). Used in big office/campus LANs.
*Hierarchical = Tree = star-of-stars (root + branches)। बड़े office/campus LANs में use होती है।*
*[Source: Repo: Unit Test-4 Solution (OCR), p17] · Medium*

**Q57.** The ______ topology of a network defines how the devices are physically laid out/connected, whereas the ______ topology defines how the data actually flow / how the devices access the network to transmit.
*Network की _______ topology बताती है की devices physically कैसे जुड़े हैं, jabki _______ topology बताती है की data asal में कैसे flow करता है / devices transmit करने के लिए network को कैसे access करते हैं।*
- **(A)** Logical ; Physical
- **(B)** Physical ; Logical
- **(C)** Star ; Bus
- **(D)** Mesh ; Ring
✔ **(B) Physical ; Logical**
★ **Nukta:** Physical = कैसे जुड़े (cables); Logical = data कैसे flow करता है (access). Same logical, different physical possible.
*Physical = कैसे जुड़े (cables); Logical = data कैसे flow करता है (access). Same logical, different physical हो सकता है।*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q58.** Which physical topology offers the highest robustness (fault tolerance) because of multiple redundant paths, but is also the most expensive and hardest to install because of the huge amount of cabling?
*कौन सी physical topology सबसे ज़्यादा robust (fault tolerant) है क्योंकि ismein कई redundant paths होते हैं, लेकिन सबसे महंगी और install करने में सबसे मुश्किल भी है क्योंकि बहुत ज़्यादा cabling चाहिए?*
- **(A)** Bus
- **(B)** Ring
- **(C)** Star
- **(D)** Mesh
✔ **(D) Mesh**
★ **Nukta:** Mesh = most robust + most costly (n(n-1)/2 cables). Star = cheap & easy but hub is a single point of failure. Bus = cheapest, hardest fault isolation.
*Mesh = सबसे robust + सबसे महंगी (n(n-1)/2 cables). Star = sasti और आसान लेकिन hub single point of failure है. Bus = सबसे sasti, fault isolation सबसे मुश्किल.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q59.** Which one of the following is not a network topology?
*निम्नलिखित में से कौन एक network topology नहीं है?*
- **(A)** Star
- **(B)** Ring
- **(C)** Bus
- **(D)** Peer to Peer
✔ **(D) Peer to Peer**
★ **Nukta:** Topologies = mesh, star, bus, ring, hybrid, tree. P2P = architecture (not topology).
*Topologies = mesh, star, bus, ring, hybrid, tree. P2P = architecture है (topology नहीं).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q9] · Hard*

**Q60.** For n devices in a network, how many cable links are required in a mesh topology?
*Network में n devices के लिए mesh topology में कितने cable links चाहिए?*
- **(A)** n
- **(B)** n - 1
- **(C)** n(n - 1)/2
- **(D)** n(n - 1)
✔ **(C) n(n - 1)/2**
★ **Nukta:** Mesh cables = n(n-1)/2, ports/device = n-1. Star = n cables. Ring = n. Bus = 1 backbone.
*Mesh cables = n(n-1)/2, ports/device = n-1। Star = n। Ring = n। Bus = 1।*
*[Source: Forouzan Ch1 (Q1-8) — Practice Set] · Hard*

**Q61.** Six devices are arranged in a mesh topology. How many cables are needed, and how many ports does each device need?
*छह devices को mesh topology में जोड़ा गया है। कितनी cables चाहिए और हर device को कितने ports चाहिए?*
- **(A)** 15 cables, 5 ports each / 15 cables, हर device पर 5 ports
- **(B)** 30 cables, 6 ports each / 30 cables, हर device पर 6 ports
- **(C)** 15 cables, 6 ports each / 15 cables, हर device पर 6 ports
- **(D)** 6 cables, 5 ports each / 6 cables, हर device पर 5 ports
✔ **(A) 15 cables, 5 ports each**
★ **Nukta:** Mesh formula: cables = n(n-1)/2, ports/device = n-1. Numerical में हमेशा yahi do numbers maange जाते हैं.
*Mesh: cables = n(n-1)/2, ports/device = n-1। Numerical में यही दो numbers पूछे जाते हैं।*
*[Source: Forouzan Ch1 (P1-3) — Practice Set (Problem)] · Hard*

**Q62.** If a computer network cable breaks, the whole network goes down in which topology?
*यदि computer network cable टूट जाए, तो किस topology में पूरा network बंद हो जाता है?*
- **(A)** Star
- **(B)** Ring
- **(C)** Mesh
- **(D)** All of these / ये सभी
✔ **(B) Ring**
★ **Nukta:** Ring = one break downs ALL. Star = only that device drops. Mesh = network survives (many paths).
*Ring = एक break से सब down। Star = सिर्फ वह device गिरता है। Mesh = network बच जाता है (कई paths)।*
*[Source: Repo: Unit Test-4 Solution (OCR), p16] · Hard*

**Q63.** In which topology does the failure of a single cable or device NOT affect the rest of the network?
*किस topology में एक cable या device के fail होने पर बाकी network प्रभावित नहीं होता?*
- **(A)** Bus
- **(B)** Ring
- **(C)** Star
- **(D)** Mesh
✔ **(D) Mesh**
★ **Nukta:** Mesh = most fault-tolerant (redundant paths) — इसलिए 'highest robustness' mesh में होती है.
*Mesh = सबसे ज़्यादा fault-tolerant (redundant paths) — इसीलिए mesh most robust है।*
*[Source: Forouzan Ch1 (P1-4) — Practice Set (Problem)] · Hard*

**Q64.** In a _______ topology, one long cable acts as a backbone to link all the devices; devices connect via drop lines and taps, and terminators are needed at both ends of the backbone.
*_______ topology में एक लंबा cable backbone की तरह सभी devices को जोड़ता है; devices drop lines और taps से connect होते हैं, और backbone के दोनों ends पर terminators चाहिए।*
- **(A)** Bus
- **(B)** Star
- **(C)** Ring
- **(D)** Mesh
✔ **(A) Bus**
★ **Nukta:** Bus = one backbone + drop lines + taps + terminators at both ends. Fault isolation is difficult; a backbone break stops everything.
*Bus = एक backbone + drop lines + taps + दोनों ends पर terminators. Fault isolation मुश्किल है; backbone tootne से सब कुछ band हो जाता है।*
*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

**Q65.** The IEEE 802 stअंदरds (such as 802.3 for Ethernet, 802.5 for Token Ring, 802.11 for Wi-Fi) primarily define the ______ of LANs/MANs.
*IEEE 802 stअंदरds (जैसे 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi) primarily LANs/MANs की _______ define करते हैं।*
- **(A)** Physical and Data Link layers (including the logical topology / MAC) / Physical और Data Link layers (logical topology / MAC sahit)
- **(B)** Only the Application layer / सिर्फ Application layer
- **(C)** Only IP addressing / सिर्फ IP addressing
- **(D)** Only WAN routing / सिर्फ WAN routing
✔ **(A) Physical and Data Link layers (including the logical topology / MAC)**
★ **Nukta:** IEEE 802 = LAN/MAN stअंदरds (Physical + Data Link). 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi.
*IEEE 802 = LAN/MAN stअंदरds (Physical + Data Link). 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Hard*

**Q66.** Four network segments in Bus topology are: A1–A2, B1–B2–B3, C1–C2 and D1–D2–D3. If A1, B1, C1 and D1 are interconnected in a mesh, how many mesh connections are required?
*Bus topology में चार network segments हैं: A1–A2, B1–B2–B3, C1–C2 और D1–D2–D3। यदि A1, B1, C1 और D1 को mesh में जोड़ा जाए, तो कितने mesh connections चाहिए?*
- **(A)** 12
- **(B)** 10
- **(C)** 6
- **(D)** 45
✔ **(C) 6**
★ **Nukta:** Mesh formula n(n-1)/2 — लेकिन n सिर्फ meshed nodes है (4), पूरे network के hosts (10) नहीं!
*Mesh formula n(n-1)/2 — पर n सिर्फ meshed nodes है (4), पूरे network के hosts (10) नहीं!*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

## Section E - Types of Networks (LAN, MAN, WAN, PAN, CAN, SAN; Internet, Intranet, Extranet; Point-to-Point, Multipoint; Client-Server, P2P)

*Syllabus: Types of Networks - Geographical (LAN, MAN, WAN, PAN, CAN, SAN) | Accessibility (Internet, Intranet, Extranet) | Architecture (Point-to-Point, Multipoint)*

**Networks geographical span ke hisaab se LAN, MAN, WAN, PAN, CAN, SAN hote hain; access method se point-to-point ya multipoint; architecture se client-server ya peer-to-peer.**

*Networks भौगोलिक विस्तार के अनुसार LAN, MAN, WAN, PAN, CAN, SAN होते हैं; पहुँच के तरीक़े से point-to-point या multipoint; ढाँचे से client-server या peer-to-peer।*

- LAN — building/campus tak, high speed, private (Ethernet, Wi-Fi).
  - *LAN — building/campus तक, तेज़, निजी (Ethernet, Wi-Fi)।*
- MAN — city tak (cable TV network, DQDB); LANs ko connect karta hai.
  - *MAN — शहर तक (cable TV, DQDB); LANs को जोड़ता है।*
- WAN — country/continent; public carriers (PSTN, satellite, leased lines); Internet sabse bada WAN.
  - *WAN — देश/महाद्वीप; public carriers (PSTN, satellite); Internet सबसे बड़ा WAN।*
- PAN — body ke paas (Bluetooth, Zigbee); CAN — campus area; SAN — storage area network (servers/disks).
  - *PAN — शरीर के पास (Bluetooth); CAN — campus; SAN — storage area network।*
- Point-to-point = dedicated link do nodes ke beech; Multipoint = ek link par multiple nodes (shared).
  - *Point-to-point = दो nodes के बीच dedicated link; Multipoint = एक link पर कई nodes (shared)।*
- Client-Server — server resources deta hai, clients maangte hain (centralized control). P2P — har computer barabar, koi dedicated server nahi.
  - *Client-Server — server resources देता है, clients माँगते हैं। P2P — हर computer बराबर, कोई dedicated server नहीं।*
- Internet = networks ka network; Intranet = organization ka private internet; Extranet = authorized bahari users ke liye intranet ka extended hissa.
  - *Internet = networks का network; Intranet = संस्था का private internet; Extranet = अधिकृत बाहरी users के लिए विस्तार।*

| Type | Span | Example |
|---|---|---|
| PAN | एक व्यक्ति के आसपास | Bluetooth headset |
| LAN | building/campus | office Ethernet |
| MAN | city | cable TV network |
| WAN | country/continent | Internet |
| SAN | storage devices | data centre storage |

### Questions (Easy → Medium → Hard)

**Q67.** The term WAN stands for?
*WAN का पूरा नाम (full form) क्या है?*
- **(A)** Wide Area Net
- **(B)** Wide Access Network
- **(C)** Wide Area Network
- **(D)** Wide Access Net
✔ **(C) Wide Area Network**
★ **Nukta:** WAN = Wide Area Network. Internet सबसे बड़ा WAN है.
*WAN = Wide Area Network. Internet सबसे बड़ा WAN है।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q11 / BCI_SCI Subject Test-01, Q11] · Medium*

**Q68.** Which network is suitable for a building?
*किसी एक building के लिए कौन सा network उपयुक्त (suitable) है?*
- **(A)** WAN
- **(B)** LAN
- **(C)** MAN
- **(D)** PAN
✔ **(B) LAN**
★ **Nukta:** LAN = Local Area Network - छोटा area (office/building/campus), private, high speed.
*LAN = Local Area Network - छोटा area (office/building/campus), private, high speed.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q27] · Medium*

**Q69.** Bluetooth is an example of:
*Bluetooth इसका example है:*
- **(A)** personal area network / personal area network (PAN)
- **(B)** local area network / local area network (LAN)
- **(C)** virtual private network / virtual private network (VPN)
- **(D)** none of the mentioned / इनमें से कोई नहीं
✔ **(A) personal area network**
★ **Nukta:** PAN = Personal Area Network - एक person के around (Bluetooth: phone <-> earphones).
*PAN = Personal Area Network - एक person के around (Bluetooth: phone <-> earphones).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q31] · Medium*

**Q70.** Which one of the following extends a private network across public networks?
*निम्नलिखित में से कौन एक private network को public networks के paar (across) extend करता है?*
- **(A)** local area network / local area network (LAN)
- **(B)** virtual private network / virtual private network (VPN)
- **(C)** enterprise private network
- **(D)** storage area network / storage area network (SAN)
✔ **(B) virtual private network**
★ **Nukta:** VPN = Virtual Private Network - private network को public (Internet) पर extend करता है, securely.
*VPN = Virtual Private Network - private network को public (Internet) पर extend करता है, securely.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q32] · Medium*

**Q71.** ______ is a network that covers geographic areas that are larger, such as districts or cities.
*______ एक ऐसा network है जो बड़े geographical areas, जैसे districts या cities, को cover करता है।*
- **(A)** LAN
- **(B)** MAN
- **(C)** WAN
- **(D)** None of these / इनमें से कोई नहीं
✔ **(B) MAN**
★ **Nukta:** MAN = Metropolitan Area Network - city level (cable TV network).
*MAN = Metropolitan Area Network - city level (cable TV network).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q49] · Medium*

**Q72.** Which factor primarily decides whether a communication system is a LAN or a WAN?
*कौन-सा factor मुख्य रूप से तय करता है कि communication system LAN है या WAN?*
- **(A)** The geographical area it spans / वह कितने geographical area में फैला है
- **(B)** The number of protocols it uses / वह कितने protocols use करता है
- **(C)** The colour of the cables / Cables का रंग
- **(D)** The type of keyboard attached / जुड़े keyboard का प्रकार
✔ **(A) The geographical area it spans**
★ **Nukta:** Chhoti area = LAN, city = MAN, state/country/world = WAN. Faisla सिर्फ area का.
*छोटा area = LAN, city = MAN, state/country/world = WAN। फैसला सिर्फ area का।*
*[Source: Forouzan Ch1 (Q1-9) — Practice Set] · Medium*

**Q73.** In terms of the size of the network, the correct order (ascending) is:
*Network के size के hisaab से सही kram (badhta हुआ/ascending order) क्या है?*
- **(A)** PAN, MAN, LAN, WAN
- **(B)** LAN, MAN, WAN, PAN
- **(C)** PAN, LAN, MAN, WAN
- **(D)** LAN, PAN, MAN, WAN
✔ **(C) PAN, LAN, MAN, WAN**
★ **Nukta:** Remember: PAN < LAN < MAN < WAN (smallest to largest).
*याद रखें: PAN < LAN < MAN < WAN (छोटा से बड़ा).*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q42] · Medium*

**Q74.** Which type of network covers an entire city or campus?
*कौन सा network पूरे एक city या campus को cover करता है?*
- **(A)** LAN
- **(B)** MAN
- **(C)** WAN
- **(D)** PAN
✔ **(B) MAN**
★ **Nukta:** MAN = city level. Note: a single building/campus LAN is usually LAN/CAN; an entire city = MAN.
*MAN = city level. Note: एक building/campus का LAN आम तौर पर LAN/CAN होता है; पूरी city = MAN.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q2] · Medium*

**Q75.** The Internet is an example of:
*Internet इसका example है:*
- **(A)** LAN
- **(B)** MAN
- **(C)** WAN
- **(D)** PAN
✔ **(C) WAN**
★ **Nukta:** Internet = सबसे बड़ा WAN (network of networks).
*Internet = सबसे बड़ा WAN (network of networks).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q12] · Medium*

**Q76.** SAN is mainly used for:
*SAN का मुख्य उपयोग किसके लिए होता है?*
- **(A)** File Sharing
- **(B)** Storage Management
- **(C)** Internet Access
- **(D)** Printing Documents / documents print करना
✔ **(B) Storage Management**
★ **Nukta:** SAN = Storage Area Network - servers <-> storage devices, data centre.
*SAN = Storage Area Network - servers <-> storage devices, data centre.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q13] · Medium*

**Q77.** PAN is used for connecting:
*PAN किसके connect करने के लिए use होता है?*
- **(A)** Personal devices like mobile, laptop, Bluetooth headset / personal devices जैसे mobile, laptop, Bluetooth headset
- **(B)** Computers in a company / एक company के computers
- **(C)** Computers in a city / एक city के computers
- **(D)** Global offices
✔ **(A) Personal devices like mobile, laptop, Bluetooth headset**
★ **Nukta:** PAN = Personal Area Network - एक person के devices (mobile, laptop, headset).
*PAN = Personal Area Network - एक person के devices (mobile, laptop, headset).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q14] · Medium*

**Q78.** A school has four computer labs in the same building. Each lab has 20 computers connected to a central server. Students can share files and print from any lab. Which type of network is implemented in this school?
*Ek school में एक ही building में चार computer labs हैं. हर lab में 20 computers एक central server से जुड़े हैं। Students किसी भी lab से files share और print कर सकते हैं। School में कौन सा network implemented है?*
- **(A)** WAN
- **(B)** MAN
- **(C)** LAN
- **(D)** CAN
✔ **(C) LAN**
★ **Nukta:** LAN = single building/campus, private, high speed. Example: school lab, office.
*LAN = एक building/campus, private, high speed. Example: school lab, office.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q15] · Medium*

**Q79.** A university has different departments in separate buildings like Engineering, Arts, and Commerce. Each department has its own LAN. All these LANs are connected together for communication. Which type of network connects all these LANs?
*Ek university में अलग-अलग departments अलग buildings में हैं जैसे Engineering, Arts, Commerce। हर department का apna LAN है। यह सब LANs communication के लिए आपस में जुड़े हैं। कौन सा network in सब LANs को जोड़ता है?*
- **(A)** LAN
- **(B)** CAN
- **(C)** MAN
- **(D)** WAN
✔ **(B) CAN**
★ **Nukta:** CAN = Campus Area Network - एक campus की multiple buildings के LANs को जोड़ता है.
*CAN = Campus Area Network - एक campus की कई buildings के LANs को जोड़ता है।*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q16] · Medium*

**Q80.** An international bank connects its main office in New York with branches in Delhi, London, and Tokyo. Which network type is used here?
*Ek international bank अपने main office (New York) को Delhi, London, और Tokyo की branches से जोड़ता है। यहाँ कौन सा network type use होता है?*
- **(A)** MAN
- **(B)** WAN
- **(C)** CAN
- **(D)** LAN
✔ **(B) WAN**
★ **Nukta:** WAN = long distance (city/country/continent). Bank branches worldwide = WAN.
*WAN = लंबी दूरी (city/देश/continent). Worldwide bank branches = WAN.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q17] · Medium*

**Q81.** A company has several servers that store and manage large volumes of data. All storage devices are interconnected for high-speed data access. Which type of network is this?
*Ek company के पास कई servers हैं जो बड़ी matra में data store और manage करते हैं। सब storage devices high-speed data access के लिए interconnected हैं। यह कौन सा network है?*
- **(A)** LAN
- **(B)** SAN
- **(C)** CAN
- **(D)** WAN
✔ **(B) SAN**
★ **Nukta:** SAN = Storage Area Network - storage devices को high-speed access dene के लिए.
*SAN = Storage Area Network - storage devices को high-speed access dene के लिए।*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q18] · Medium*

**Q82.** A supplier accessing a company's order tracking system uses:
*Ek supplier जो company के order tracking system को access करता है, कौन सा network use करता है?*
- **(A)** Internet
- **(B)** Intranet
- **(C)** Extranet
- **(D)** VPN
✔ **(C) Extranet**
★ **Nukta:** Extranet = intranet + authorized outsiders (suppliers/partners/customers).
*Extranet = intranet + authorized outsiders (suppliers/partners/customers).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q19] · Medium*

**Q83.** Which network type provides maximum security and privacy?
*कौन सा network type अधिकतम (maximum) security और privacy provide करता है?*
- **(A)** Internet
- **(B)** Intranet
- **(C)** Extranet
- **(D)** None
✔ **(B) Intranet**
★ **Nukta:** Security order: Intranet (सबसे secure/private) > Extranet > Internet (public).
*Security order: Intranet (सबसे secure/private) > Extranet > Internet (public).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q20] · Medium*

**Q84.** A software company shares project reports and progress updates with its clients through a secure online portal that requires login credentials. Which network type is this?
*Ek software company अपने clients के साथ project reports और progress updates एक secure online portal के through share करती है जिसमें login credentials चाहिए। यह कौन सा network type है?*
- **(A)** Internet
- **(B)** Intranet
- **(C)** Extranet
- **(D)** MAN
✔ **(C) Extranet**
★ **Nukta:** Clients को secure portal से share करना = Extranet.
*Clients को secure portal से share करना = Extranet.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q21] · Medium*

**Q85.** Three or more devices share a link in ________ connection.
*Teen या अधिक devices एक link ________ connection में share करते हैं।*
- **(A)** Unipoint
- **(B)** Multipoint
- **(C)** Point to point
- **(D)** None of the mentioned / इनमें से कोई नहीं
✔ **(B) Multipoint**
★ **Nukta:** Multipoint = एक link, कई devices; capacity shared. Point-to-point = dedicated link, सिर्फ 2 devices.
*Multipoint = एक link, कई devices; capacity shared. Point-to-point = dedicated link, सिर्फ 2 devices.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q36] · Medium*

**Q86.** What are the two types of line configuration?
*Line configuration के दो प्रकार क्या हैं?*
- **(A)** Simplex and Half-Duplex / Simplex और Half-Duplex
- **(B)** Serial and Parallel / Serial और Parallel
- **(C)** Point-to-Point and Multipoint / Point-to-Point और Multipoint
- **(D)** Analog and Digital / Analog और Digital
✔ **(C) Point-to-Point and Multipoint**
★ **Nukta:** Line configuration के सिर्फ 2 type: Point-to-Point & Multipoint. Simplex/Half/Full-Duplex TRANSMISSION MODES हैं.
*Line configuration के 2 type: Point-to-Point और Multipoint। Simplex/Half/Full-Duplex transmission modes हैं।*
*[Source: Forouzan Ch1 (Q1-4) — Practice Set] · Medium*

**Q87.** What is the advantage of a multipoint connection over a point-to-point connection?
*Point-to-point connection की तुलना में multipoint connection का क्या लाभ है?*
- **(A)** Fewer cables are needed, so the cost is lower / कम cables लगती हैं, इसलिए cost कम होती है
- **(B)** It provides a dedicated link for every pair of devices / हर device-युग्म को dedicated link मिलता है
- **(C)** It is more secure than point-to-point / यह point-to-point से ज़्यादा secure है
- **(D)** It needs more cables and ports / इसमें ज़्यादा cables और ports लगते हैं
✔ **(A) Fewer cables are needed, so the cost is lower**
★ **Nukta:** Multipoint = कम cable = कम kharch. Point-to-point = dedicated link (ज़्यादा cable, ज़्यादा privacy).
*Multipoint = कम cable = कम खर्च। Point-to-point = dedicated link (ज़्यादा cable, ज़्यादा privacy)।*
*[Source: Forouzan Ch1 (Q1-3) — Practice Set] · Medium*

**Q88.** A _______ connection provides a dedicated link between two devices.
*Ek _______ connection do devices के बीच एक dedicated link provide करता है।*
- **(A)** point-to-point
- **(B)** multipoint
- **(C)** primary
- **(D)** secondary
✔ **(A) point-to-point**
★ **Nukta:** Point-to-point = dedicated link, पूरी capacity सिर्फ 2 devices के लिए. Example: TV remote (IR), leased line.
*Point-to-point = dedicated link, पूरी capacity सिर्फ 2 devices के लिए. Example: TV remote (IR), leased line.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q42] · Medium*

**Q89.** When a person makes a local telephone call to another person, what type of connection is it?
*जब कोई व्यक्ति दूसरे व्यक्ति को local telephone call करता है, तो यह किस प्रकार का connection है?*
- **(A)** Multipoint connection
- **(B)** Point-to-point connection
- **(C)** Broadcast connection
- **(D)** Multicast connection
✔ **(B) Point-to-point connection**
★ **Nukta:** Telephone call = 2 parties, dedicated link = point-to-point. Bus/Ethernet = multipoint.
*Telephone call = 2 parties, dedicated link = point-to-point। Bus/Ethernet = multipoint।*
*[Source: Forouzan Ch1 (P1-7) — Practice Set (Problem)] · Medium*

**Q90.** Which of the following is an example of Client-Server architecture?
*निम्नलिखित में से कौन Client-Server architecture का example है?*
- **(A)** Chat between two Bluetooth devices / do Bluetooth devices के बीच chat
- **(B)** Web browser accessing a website / web browser जो एक website access कर रहा है
- **(C)** File transfer via USB cable / USB cable से file transfer
- **(D)** Two laptops connected directly / do laptops directly connected
✔ **(B) Web browser accessing a website**
★ **Nukta:** Client-Server = client request करता है, server service provide करता है. Example: web browser - website.
*Client-Server = client request करता है, server service provide करता है। Example: web browser - website.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q23] · Medium*

**Q91.** In a bank, customers use ATMs to check balance or withdraw cash. ATM machines send the request to a central computer for verification and processing. Which type of architecture is used here?
*Ek bank में customers ATMs से balance check या cash withdraw करते हैं। ATM machines request एक central computer को verification और processing के लिए bhejte हैं। यहाँ कौन सी architecture use होती है?*
- **(A)** Peer-to-Peer
- **(B)** Client-Server
- **(C)** Multipoint
- **(D)** Point-to-Point
✔ **(B) Client-Server**
★ **Nukta:** ATM -> central server = client-server (client request, server verify/process).
*ATM -> central server = client-server (client request, server verify/process).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q25] · Medium*

**Q92.** In a LAN, connectivity can be created using Wi-Fi or _______.
*Ek LAN में connectivity Wi-Fi या _______ से बनाई जा सकती है।*
- **(A)** TV
- **(B)** Radio
- **(C)** Mobile
- **(D)** Ethernet
✔ **(D) Ethernet**
★ **Nukta:** LAN connectivity = Wi-Fi (wireless) + Ethernet (wired cable).
*LAN connectivity = Wi-Fi (wireless) + Ethernet (wired cable).*
*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)] · Medium*

**Q93.** Which network type is built on top of another existing network?
*कौन-सा network type किसी मौजूदा network के ऊपर बनाया जाता है?*
- **(A)** Overlay network
- **(B)** Prime network
- **(C)** Prior network
- **(D)** Chief network
✔ **(A) Overlay network**
★ **Nukta:** Overlay = network के ऊपर बना network (VPN classic example है). Baaki 3 asli network types नहीं हैं.
*Overlay = network के ऊपर बना network (VPN इसका classic example है)। बाकी 3 real network types नहीं हैं।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q94.** ______ converts analog voice signals into digital and then transmits them over the broadband line.
*______ analog voice signals को digital में बदलकर broadband line पर भेजता है.*
- **(A)** VoIP (Voice over Internet Protocol)
- **(B)** Chatting
- **(C)** Website
- **(D)** Video conferencing
✔ **(A) VoIP (Voice over Internet Protocol)**
★ **Nukta:** VoIP = the new Internet form of the old telephone voice.
*VoIP = पुरानी फ़ोन-आवाज़ का नया internet-रूप.*
*[Source: RSMSSB Informatics Assistant 2023 (via examsmantra solved paper)] · Medium*

**Q95.** Which of these is NOT a type of network?
*इनमें से कौन network का एक prakar (type) नहीं है?*
- **(A)** LAN
- **(B)** MAN
- **(C)** WAN
- **(D)** TAN
✔ **(D) TAN**
★ **Nukta:** Network types: PAN, LAN, MAN, WAN (+ CAN, SAN). TAN = नहीं है.
*Network types: PAN, LAN, MAN, WAN (+ CAN, SAN). TAN = नहीं है।*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q7] · Hard*

**Q96.** What is the difference between an 'internet' and the 'Internet'?
*'internet' और 'Internet' में अंतर क्या है?*
- **(A)** There is no difference; both mean the World Wide Web / कोई अंतर नहीं; दोनों का अर्थ World Wide Web है
- **(B)** An internet is any network of networks; the Internet is the specific global one we use today / internet कोई भी network of networks है; Internet आज की वह विशिष्ट विश्वव्यापी network of networks है
- **(C)** An internet is smaller than a LAN; the Internet is larger than a WAN / internet LAN से छोटा है; Internet WAN से बड़ा है
- **(D)** An internet uses cables; the Internet uses only wireless / internet cables use करता है; Internet सिर्फ wireless use करता है
✔ **(B) An internet is any network of networks; the Internet is the specific global one we use today**
★ **Nukta:** internet = generic network of networks. Internet = THE global network (capital I).
*internet = generic network of networks। Internet = वह global network (बड़ा I)।*
*[Source: Forouzan Ch1 (Q1-10) — Practice Set] · Hard*

**Q97.** Bank employees access internal financial databases, while customers access their accounts through online banking websites. Which networks are being used by employees and customers respectively?
*Bank employees internal financial databases access करते हैं, jabki customers online banking websites के through अपने accounts access करते हैं। Employees और customers kramashah कौन से networks use कर रहे हैं?*
- **(A)** Employees - Intranet; Customers - Extranet
- **(B)** Employees - Internet; Customers - Intranet
- **(C)** Employees - Extranet; Customers - Internet
- **(D)** Both - Internet / दोनों - Internet
✔ **(A) Employees - Intranet; Customers - Extranet**
★ **Nukta:** Employees -> Intranet (internal). Outsiders (customers/suppliers) -> Extranet. Public -> Internet.
*Employees -> Intranet (internal). Outsiders (customers/suppliers) -> Extranet. Public -> Internet.*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q22] · Hard*

**Q98.** How many point-to-point WANs are needed to connect n LANs so that every LAN can directly communicate with every other LAN?
*n LANs को इस तरह जोड़ने के लिए कितने point-to-point WANs चाहिए कि हर LAN हर दूसरी LAN से सीधे communicate कर सके?*
- **(A)** n
- **(B)** n - 1
- **(C)** n(n - 1)/2
- **(D)** n²
✔ **(C) n(n - 1)/2**
★ **Nukta:** Full mesh of LANs = n(n-1)/2 WAN links. Formula mesh वाला ही है.
*LANs का full mesh = n(n-1)/2 WAN links। Formula mesh जैसा ही है।*
*[Source: Forouzan Ch1 (Q1-13) — Practice Set] · Hard*

**Q99.** Which of the following uses Peer-to-Peer (P2P) architecture, not Client-Server?
*निम्नलिखित में से कौन Peer-to-Peer (P2P) architecture use करता है, Client-Server नहीं?*
- **(A)** BitTorrent file sharing
- **(B)** Google search
- **(C)** Gmail
- **(D)** YouTube
✔ **(A) BitTorrent file sharing**
★ **Nukta:** P2P = peers आपस में directly share करते हैं (BitTorrent). Client-Server = server service देता है (Google, Gmail, YouTube).
*P2P = peers आपस में directly share करते हैं (BitTorrent). Client-Server = server service देता है (Google, Gmail, YouTube).*
*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q24] · Hard*

## Section F - Network History (ARPANET to Today's Network)

*Syllabus: Network History - ARPANET to today's network*

**Aaj ka Internet ARPANET se nikla hai — packet switching ka pehla bada network, jo research se hokar aam internet bana.**

*आज का Internet ARPANET से निकला है — packet switching का पहला बड़ा network, जो research से होकर सामान्य internet बना।*

- ARPANET (1969, DARPA/US Defense) — packet switching ka pehla operational network; 4 nodes se shuruaat.
  - *ARPANET (1969, DARPA) — packet switching का पहला चालू network; 4 nodes से शुरू।*
- Pehle NCP (Network Control Protocol) chala, phir 1983 mein TCP/IP adopt hua — is tarikh ko Internet ka janm manate hain.
  - *पहले NCP चला, फिर 1983 में TCP/IP अपनाया — इसे Internet का जन्म मानते हैं।*
- NSFNET (1986) — universities ko joda; phir 1990s mein commercial use shuru hua.
  - *NSFNET (1986) — universities जुड़ीं; फिर 1990s में व्यावसायिक उपयोग शुरू।*
- World Wide Web (1991) — Tim Berners-Lee ne CERN mein banaya (HTML, URL, HTTP); Internet par information rakhne ka aasan tareeka.
  - *World Wide Web (1991) — Tim Berners-Lee ने CERN में बनाया (HTML, URL, HTTP)।*
- Evolution: ARPANET → NSFNET → Internet → WWW → broadband/Wi-Fi/mobile Internet.
  - *विकास: ARPANET → NSFNET → Internet → WWW → broadband/Wi-Fi/mobile Internet।*

| Saal (Year) | Ghatna (Event) |
|---|---|
| 1969 | ARPANET — packet switching network (4 nodes) |
| 1983 | TCP/IP adopt — Internet ka janm |
| 1986 | NSFNET — university backbone |
| 1991 | WWW (Tim Berners-Lee, CERN) |
| 1990s+ | commercial Internet, broadband, Wi-Fi |

### Questions (Easy → Medium → Hard)

**Q100.** The first network was:
*सबसे पहला network था:*
- **(A)** CNNET
- **(B)** NSFNET
- **(C)** ASAPNET
- **(D)** ARPANET
✔ **(D) ARPANET**
★ **Nukta:** First network = ARPANET (1969). NSFNET = 1986 (backbone).
*First network = ARPANET (1969). NSFNET = 1986 (backbone).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q34] · Medium*

**Q101.** In the original ARPANET, _______ were directly connected together.
*Original ARPANET में, _______ आपस में directly connected the।*
- **(A)** IMPs / IMPs (Interface Message Processors)
- **(B)** host computers
- **(C)** networks
- **(D)** routers
✔ **(A) IMPs**
★ **Nukta:** Original ARPANET: IMPs (packet switches) directly connected; hosts attached to IMPs.
*Original ARPANET: IMPs (packet switches) directly connected the; hosts IMPs से attach होते the।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q43] · Medium*

**Q102.** The first operational computer network in the world was the _________ for the United States Department of Defense.
*दुनिया का पहला operational computer network, United States Department of Defense के लिए _________ था।*
- **(A)** ARPANET
- **(B)** ERNET
- **(C)** SKYNET
- **(D)** DARPANET
✔ **(A) ARPANET**
★ **Nukta:** First operational network = ARPANET (1969, U.S. DoD).
*First operational network = ARPANET (1969, U.S. DoD).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q48] · Medium*

**Q103.** ARPANET - the precursor of today's Internet - was created in ______ by ARPA (Advanced Research Projects Agency) of the U.S. Department of Defense, starting with four nodes (UCLA, SRI, UC Santa Barbara, University of Utah).
*ARPANET - aaj के Internet का purvaj - ______ में ARPA (Advanced Research Projects Agency), U.S. Department of Defense द्वारा बनाया गया था, चार nodes से shuruaat हुई (UCLA, SRI, UC Santa Barbara, University of Utah).*
- **(A)** 1957
- **(B)** 1969
- **(C)** 1983
- **(D)** 1991
✔ **(B) 1969**
★ **Nukta:** ARPANET = 1969, 4 nodes (UCLA, SRI, UCSB, Utah); first message 29 Oct 1969 (LO of LOGIN).
*ARPANET = 1969, 4 nodes (UCLA, SRI, UCSB, Utah); पहला message 29 Oct 1969 (LOGIN का LO).*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q104.** TCP/IP (developed by Vint Cerf and Bob Kahn) was adopted by ARPANET as its official protocol suite on 1 January ______ - an event known as the fflag day.
*TCP/IP (Vint Cerf और Bob Kahn द्वारा develop किया गया) को ARPANET ने apna official protocol suite बनाया था 1 January ______ को - is event को fflag day कहा जाता है।*
- **(A)** 1969
- **(B)** 1972
- **(C)** 1983
- **(D)** 1995
✔ **(C) 1983**
★ **Nukta:** Fflag day = 1 Jan 1983 (ARPANET -> TCP/IP). TCP/IP developed by Cerf & Kahn in 1970s (demo 1972). Syllabus का TCP/IP model 1972 = development era.
*Fflag day = 1 Jan 1983 (ARPANET -> TCP/IP). TCP/IP Cerf & Kahn ने 1970s में develop किया (demo 1972). Syllabus का TCP/IP model 1972 = development era.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q105.** NSFNET, created by the U.S. National Science Foundation in ______, became a major backbone of the Internet, connecting universities and research centres.
*NSFNET, U.S. National Science Foundation द्वारा ______ में बनाया गया, Internet का एक major backbone बन गया, universities और research centres को जोड़ता था।*
- **(A)** 1969
- **(B)** 1983
- **(C)** 1986
- **(D)** 1991
✔ **(C) 1986**
★ **Nukta:** NSFNET = 1986 (National Science Foundation), T1 backbone -> Internet backbone.
*NSFNET = 1986 (National Science Foundation), T1 backbone -> Internet backbone.*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

**Q106.** The World Wide Web (WWW) was invented in 1991 at CERN by ______, and it made the Internet popular among the general public.
*World Wide Web (WWW) का invention 1991 में CERN में ______ ने किया था, और isne Internet को आम public के बीच popular बनाया।*
- **(A)** Vint Cerf
- **(B)** Tim Berners-Lee
- **(C)** Bob Kahn
- **(D)** Marc Andreessen
✔ **(B) Tim Berners-Lee**
★ **Nukta:** WWW = 1991, Tim Berners-Lee @ CERN. Mosaic browser 1993. Vint Cerf & Bob Kahn = fathers of the Internet (TCP/IP).
*WWW = 1991, Tim Berners-Lee @ CERN. Mosaic browser 1993. Vint Cerf & Bob Kahn = Internet के fathers (TCP/IP).*
*[Source: Extra (Forouzan) - fills syllabus gap] · Medium*

## Section G - General Network Basics (WWW, E-mail, Protocols, Servers, Switching - from repo intro tests)

*Syllabus: Introduction of DC - general basics asked in BCI/RPSC exams (Specific Address/URL, Application services, Switching)*

**General basics: WWW aur Internet alag cheezein hain; e-mail protocols, servers, aur switching ke tareeke — yeh sab chhote exams mein bahut puche jaate hain.**

*General basics: WWW और Internet अलग चीज़ें हैं; e-mail protocols, servers, और switching के तरीक़े — छोटी परीक्षाओं में बहुत पूछे जाते हैं।*

- WWW = Internet par rakhi linked information ka sangrah (web pages + hyperlinks); Internet khud network infrastructure hai.
  - *WWW = Internet पर रखी linked information का संग्रह; Internet खुद network infrastructure है।*
- E-mail: SMTP se bhejte hain, POP3/IMAP se lete hain; mail user agent + mail transfer agent kaam karte hain.
  - *E-mail: SMTP से भेजते हैं, POP3/IMAP से लेते हैं।*
- Server = resources/services dene wala computer; Client = service maangne wala.
  - *Server = resources/services देने वाला; Client = माँगने वाला।*
- Switching ke 3 tareeke: Circuit switching (dedicated path — telephone), Packet switching (packets alag-alag routes se — Internet), Message switching (store-and-forward).
  - *Switching के 3 तरीक़े: Circuit switching (dedicated path), Packet switching (packets अलग-अलग मार्गों से), Message switching (store-and-forward)।*
- URL = address of web page: scheme://host/path (jaise https://example.com/page).
  - *URL = web page का पता: scheme://host/path।*

| Switching | Path | Example |
|---|---|---|
| Circuit | dedicated, reserved | telephone call |
| Packet | har packet alag route | Internet |
| Message | store-and-forward messages | telegraph/early networks |

### Questions (Easy → Medium → Hard)

**Q107.** A collection of hyperlinked documents on the internet forms the?
*Internet पर hyperlinked documents का sangrah (collection) क्या banata है?*
- **(A)** World Wide Web (WWW)
- **(B)** E-mail system
- **(C)** Mailing list
- **(D)** Hypertext markup language / hypertext markup language (HTML)
✔ **(A) World Wide Web (WWW)**
★ **Nukta:** WWW = hyperlinked documents का collection. HTML = un documents की language (WWW नहीं).
*WWW = hyperlinked documents का collection. HTML = un documents की language है (WWW नहीं).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q5] · Medium*

**Q108.** Which one of the following is a valid email address?
*निम्नलिखित में से कौन सा एक valid email address है?*
- **(A)** computech@academy.com
- **(B)** gmail.com
- **(C)** compu@.com
- **(D)** computech@books
✔ **(A) computech@academy.com**
★ **Nukta:** Valid email = local@domain.TLD (e.g., name@site.com).
*Valid email = local@domain.TLD (जैसे name@site.com).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q6] · Medium*

**Q109.** Which of the following best describes uploading information?
*निम्नलिखित में से कौन uploading information को सबसे achhe से describe करता है?*
- **(A)** Sorting data on a disk drive / disk drive पर data को sort करना
- **(B)** Sending information to a host computer / information को एक host computer को भेजना
- **(C)** Receiving information from a host computer / एक host computer से information receive करना
- **(D)** Sorting data on a hard drive / hard drive पर data को sort करना
✔ **(B) Sending information to a host computer**
★ **Nukta:** Uploading = local से remote/host को भेजना. Downloading = remote से local को लेना.
*Uploading = local से remote/host को भेजना. Downloading = remote से local को लेना.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q7] · Medium*

**Q110.** Which one of the following is the most common internet protocol?
*Nimnlikhis में से कौन सा सबसे common internet protocol है?*
- **(A)** HTML
- **(B)** NetBEUI
- **(C)** TCP/IP
- **(D)** IPX/SPX
✔ **(C) TCP/IP**
★ **Nukta:** Internet का core protocol = TCP/IP. HTML = language, protocol नहीं.
*Internet का core protocol = TCP/IP. HTML = language है, protocol नहीं.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q8] · Medium*

**Q111.** The dial-up connections to access the internet use ___ protocol.
*Internet access के लिए dial-up connections ___ protocol use करते हैं।*
- **(A)** PPP (Point to Point protocol)
- **(B)** X.25 protocol
- **(C)** PLIP protocol
- **(D)** None of the above / इनमें से कोई नहीं
✔ **(A) PPP (Point to Point protocol)**
★ **Nukta:** Dial-up Internet = PPP (Point-to-Point Protocol).
*Dial-up Internet = PPP (Point-to-Point Protocol).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q18] · Medium*

**Q112.** When a resident uses a dial-up or DSL service to connect to the Internet, what is the role of the telephone company?
*जब कोई व्यक्ति Internet से जुड़ने के लिए dial-up या DSL service use करता है, तो telephone company की भूमिका क्या होती है?*
- **(A)** It provides the switching/connection path from the user to the ISP / वह user से ISP तक switching/connection path देती है
- **(B)** It hosts every website the user visits / वह user की हर website host करती है
- **(C)** It assigns IP addresses to every website / वह हर website को IP address देती है
- **(D)** It encrypts all the user's data / वह user का सारा data encrypt करती है
✔ **(A) It provides the switching/connection path from the user to the ISP**
★ **Nukta:** Telephone company सिर्फ 'road' देती है (local loop + switching). Website hosting/IP assignment ISP/DNS का काम है.
*Telephone company सिर्फ रास्ता देती है (local loop + switching)। Website hosting/IP assignment ISP/DNS का काम है।*
*[Source: Forouzan Ch1 (Q1-14) — Practice Set] · Medium*

**Q113.** Which of the following servers allows LAN users to share data?
*निम्नलिखित में से कौन सा server LAN users को data share करने की अनुमति देता है?*
- **(A)** Data server
- **(B)** Point server
- **(C)** File server
- **(D)** Communication server
✔ **(C) File server**
★ **Nukta:** File server = files store + LAN users को share करने देता है.
*File server = files store करता है + LAN users को share करने देता है।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q22] · Medium*

**Q114.** EDI stands for ____.
*EDI का पूरा नाम है ____.*
- **(A)** Electronic Data Interchange
- **(B)** Electronic Digital Internet
- **(C)** Electronic Digital Interchange
- **(D)** Electronic Data Internet
✔ **(A) Electronic Data Interchange**
★ **Nukta:** EDI = Electronic Data Interchange (business documents का e-exchange).
*EDI = Electronic Data Interchange (business documents का e-exchange).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q25] · Medium*

**Q115.** The term UPnP is a short form of:
*UPnP term का पूरा नाम (full form) क्या है?*
- **(A)** Uniform Plug and Play
- **(B)** Unit Plug and Play
- **(C)** Useful Plug and Play
- **(D)** Universal Plug and Play
✔ **(D) Universal Plug and Play**
★ **Nukta:** UPnP = Universal Plug and Play (device auto-discovery). Compare: DHCP = auto IP configuration.
*UPnP = Universal Plug and Play (device auto-discovery)। तुलना: DHCP = auto IP configuration।*
*[Source: Repo: Unit Test-4 Solution (OCR), p11] · Medium*

**Q116.** Consider the switching statements:
1. Circuit Switching establishes a dedicated path.
2. Packet Switching routes data in packets on different paths.
3. Message Switching uses store-and-forward.
Which statements are correct?
*Switching statements देखिए:
1. Circuit Switching dedicated path बनाता है।
2. Packet Switching data को packets में अलग paths पर भेजता है।
3. Message Switching store-and-forward use करता है।
कौन से statements सही हैं?*
- **(A)** 1 and 2 only / सिर्फ 1 और 2
- **(B)** 2 and 3 only / सिर्फ 2 और 3
- **(C)** 1 and 3 only / सिर्फ 1 और 3
- **(D)** 1, 2 and 3 / 1, 2 और 3
✔ **(D) 1, 2 and 3**
★ **Nukta:** 3 switching types: Circuit (dedicated path), Packet (packets, अलग paths), Message (store-and-forward) — teeno statements correct.
*3 switching types: Circuit (dedicated path), Packet (packets, अलग paths), Message (store-and-forward) — तीनों सही।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

**Q117.** All the information on the internet is passed using _______ switching method.
*Internet पर saari information _______ switching method से pass होती है।*
- **(A)** Portable
- **(B)** Packets
- **(C)** Pouch
- **(D)** Primary
✔ **(B) Packets**
★ **Nukta:** Internet = packet switching. Circuit switching = dedicated path (old telephone).
*Internet = packet switching. Circuit switching = dedicated path (पुराना telephone).*
*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)] · Medium*

**Q118.** Which technique breaks data into packets for transmission?
*Transmission के लिए data को packets में तोड़ने की technique कौन-सी है?*
- **(A)** Circuit switching
- **(B)** Packet switching
- **(C)** Frequency division multiplexing
- **(D)** Time division multiplexing
✔ **(B) Packet switching**
★ **Nukta:** Internet packet switching पर चलता है — data packets में tootta है.
*Internet packet switching पर चलता है — data packets में टूटता है।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

**Q119.** Home broadband connections that work on DSL (Digital Subscriber Line) use ___ protocol.
*DSL (Digital Subscriber Line) पर काम करने वाले home broadband connections ___ protocol use करते हैं।*
- **(A)** PPPoE (PPP over Ethernet)
- **(B)** PPPoA (PPP over ATM)
- **(C)** Bridge protocol
- **(D)** All of the above / ऊपर दिए गए सभी
✔ **(A) PPPoE (PPP over Ethernet)**
★ **Nukta:** Home DSL broadband = PPPoE (PPP over Ethernet).
*Home DSL broadband = PPPoE (PPP over Ethernet).*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q19] · Hard*

**Q120.** A computer network permits sharing of:
*एक computer network किस चीज़ की sharing की अनुमति देता है?*
- **(A)** Resources / resources (printer, disk, etc.)
- **(B)** Information / information (data)
- **(C)** Both a & b / दोनों a और b
- **(D)** None of these / इनमें से कोई नहीं
✔ **(C) Both a & b**
★ **Nukta:** Network = resources + information sharing.
*Network = resources + information sharing.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q47 / CN Topic Test-02 (UNIT TEST-2), Q47] · Hard*

**Q121.** Which of the following is a benefit of networking?
*Networking का कौन-सा लाभ (benefit) है?*
- **(A)** File sharing
- **(B)** Easier access to resources / resources तक आसान पहुँच
- **(C)** Easier backups / आसान backups
- **(D)** All of the above / ऊपर दिए गए सभी
✔ **(D) All of the above**
★ **Nukta:** Networking benefits: sharing (files/resources/peripherals) + communication + backup + cost saving. Exam favourite: "All of the above".
*Networking के लाभ: sharing (files/resources/peripherals) + communication + backup + cost saving। Exam favourite: "All of the above"।*
*[Source: InstrumentationTools 150 CN MCQs] · Hard*

**Q122.** How many digits of the Data Network Identification Code (DNIC) identify the country?
*Data Network Identification Code (DNIC) के kitne digits देश (country) की पहचान करते हैं?*
- **(A)** first three / पहले तीन
- **(B)** first four / पहले चार
- **(C)** first five / पहले पाँच
- **(D)** first six / पहले छह
✔ **(A) first three**
★ **Nukta:** DNIC: first 3 digits = country code, 4th digit = network code.
*DNIC: पहले 3 digits = country code, चौथा digit = network code.*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q15] · Hard*

**Q123.** Which of the following is true for Circuit Switching handling multiple simultaneous connections?
*एक साथ अनेक connections संभालते समय Circuit Switching के बारे में क्या सही है?*
- **(A)** A single path is used and shared for all data / एक ही path सभी data के लिए share होता है
- **(B)** All connections are multiplexed into a single channel / सभी connections एक channel में multiplex होते हैं
- **(C)** It encodes all data into a single channel / यह सारे data को एक channel में encode करता है
- **(D)** Separate physical paths are allocated for each channel / हर channel के लिए अलग physical paths दिए जाते हैं
✔ **(D) Separate physical paths are allocated for each channel**
★ **Nukta:** Circuit switching = हर connection का apna अलग path. Packet switching = shared medium, packets अलग paths से.
*Circuit switching = हर connection का अपना अलग path। Packet switching = shared medium, packets अलग paths से।*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

# TOPIC 2 — Network Models (OSI & TCP/IP)

## Section A — OSI Model: Basics, Layer Order & Support Layers

*OSI = Open Systems Interconnection (ISO, 1984): 7 layers, layer order, network vs user support layers, address types.*

**OSI (Open Systems Interconnection) model ISO ne 1984 mein banaya — communication ko 7 layers mein baanta taaki har layer ka kaam alag ho sake.**

*OSI (Open Systems Interconnection) model ISO ने 1984 में बनाया — संचार को 7 layers में बाँटा ताकि हर layer का काम अलग हो सके।*

- 7 layers ka kram upar se neeche: Application, Presentation, Session, Transport, Network, Data Link, Physical.
  - *7 layers का क्रम ऊपर से नीचे: Application, Presentation, Session, Transport, Network, Data Link, Physical।*
- Yad rakhne ka mantra: 'Please Do Not Throw Sausage Pizza Away' (Physical, Data Link, Network, Transport, Session, Presentation, Application).
  - *याद रखने का मंत्र: 'Please Do Not Throw Sausage Pizza Away'।*
- Har layer sirf apne upar-wali aur neeche-wali layer se baat karti hai (interfaces); do systems ki SAME layer peer-to-peer protocol se baat karti hai.
  - *हर layer सिर्फ़ ऊपर/नीचे वाली layer से बात करती है; दो systems की SAME layer peer protocol से बात करती है।*
- Layers 1–4 = support layers (data transport ke liye); Layers 5–7 = user support layers (user ke kaam ke liye).
  - *Layers 1–4 = support layers; Layers 5–7 = user support layers।*
- Model ek reference framework hai — khud koi data carry nahi karta; real implementations isse map hote hain.
  - *Model एक reference framework है — खुद data carry नहीं करता।*
- Har layer apni header (data link trailer bhi) add karti jaati hai — isse kehte hain encapsulation.
  - *हर layer अपनी header जोड़ती जाती है — इसे encapsulation कहते हैं।*

| Layer # | Naam | PDU |
|---|---|---|
| 7 | Application | Data/Message |
| 6 | Presentation | Data/Message |
| 5 | Session | Data/Message |
| 4 | Transport | Segment (TCP) / Datagram (UDP) |
| 3 | Network | Packet / Datagram |
| 2 | Data Link | Frame |
| 1 | Physical | Bits |

### Questions (Easy → Medium → Hard)

**Q124.** The OSI model was developed by:
*OSI model किसने develop किया?*
- **(A)** IEEE
- **(B)** ISO
- **(C)** IETF
- **(D)** ITU
✔ **(B) ISO**
★ **Nukta:** OSI = ISO ka (1984). TCP/IP = DoD/ARPA ka. IEEE = 802 LAN standards. IETF = TCP/IP standards.
*OSI = ISO का (1984)। TCP/IP = DoD/ARPA का। IEEE = 802 LAN standards। IETF = TCP/IP standards।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q125.** OSI stands for:
*OSI का पूरा नाम (full form) क्या है?*
- **(A)** Open Systems Interconnection
- **(B)** Operating System Interface
- **(C)** Optical Service Implementation
- **(D)** None of these
✔ **(A) Open Systems Interconnection**
★ **Nukta:** OSI = Open Systems Interconnection (ISO, 1984, 7 layers). Ye sabse favourite one-liner hai.
*OSI = Open Systems Interconnection (ISO, 1984, 7 layers)। सबसे favourite one-liner।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q126.** The OSI model has how many layers?
*OSI model में कितनी layers हैं?*
- **(A)** 5
- **(B)** 6
- **(C)** 7
- **(D)** 8
✔ **(C) 7**
★ **Nukta:** Mnemonic: Please Do Not Throw Sausage Pizza Away (Physical, Data-link, Network, Transport, Session, Presentation, Application).
*Mnemonic: Please Do Not Throw Sausage Pizza Away (Physical, Data-link, Network, Transport, Session, Presentation, Application)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

**Q127.** Why was the OSI model developed?
*OSI model क्यों develop किया गया?*
- **(A)** Manufacturers disliked the TCP/IP protocol suite / Manufacturers को TCP/IP protocol suite पसंद नहीं था
- **(B)** The rate of data transfer was increasing exponentially / Data transfer की दर तेज़ी से बढ़ रही थी
- **(C)** Standards were needed to allow any two systems to communicate / किन्हीं भी दो systems के बीच communication के लिए standards चाहिए थे
- **(D)** None of the above / इनमें से कोई नहीं
✔ **(C) Standards were needed to allow any two systems to communicate**
★ **Nukta:** OSI = OPEN systems — matlab koi bhi do systems jud sakein. Isliye 'standards were needed' sahi jawab hai.
*OSI = OPEN systems — कोई भी दो systems जुड़ सकें। इसलिए 'standards were needed' सही उत्तर है।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q128.** In the OSI model, when data is sent from device A to device B, which is the 5th layer to receive data at B (counting from the bottom)?
*OSI model में जब data device A से device B को भेजा जाता है, तो B पर data पाने वाली 5वीं layer (नीचे से गिनती में) कौन-सी है?*
- **(A)** Application layer
- **(B)** Transport layer
- **(C)** Link layer
- **(D)** Session layer
✔ **(D) Session layer**
★ **Nukta:** Layer order bottom-up: Physical(1), Data-link(2), Network(3), Transport(4), Session(5), Presentation(6), Application(7).
*Layer क्रम (bottom-up): Physical(1), Data-link(2), Network(3), Transport(4), Session(5), Presentation(6), Application(7)।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q129.** Network support layers are:
*Network support layers कौन-सी हैं?*
- **(A)** 1, 2, 3
- **(B)** 4, 5
- **(C)** 5, 6, 7
- **(D)** 4 only
✔ **(A) 1, 2, 3**
★ **Nukta:** 1,2,3 = network support; 5,6,7 = user support; 4 = bridge. Exam mein ye grouping bar-bar aata hai.
*1,2,3 = network support; 5,6,7 = user support; 4 = bridge।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q130.** Which layer connects the network support layers and the user support layers?
*कौन-सी layer network support layers और user support layers को जोड़ती है?*
- **(A)** Transport layer
- **(B)** Network layer
- **(C)** Data Link layer
- **(D)** Session layer
✔ **(A) Transport layer**
★ **Nukta:** Transport = bridge layer (na upar wale, na neeche wale — dono se judta hai).
*Transport = bridge layer (ऊपर और नीचे दोनों से जुड़ती है)।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q131.** In the ISO-OSI reference model, the Session layer offers dialog control, token management and ______ as services.
*ISO-OSI reference model में Session layer dialog control, token management और ______ services देती है।*
- **(A)** Synchronization
- **(B)** Asynchronization
- **(C)** Errors
- **(D)** Flow control
✔ **(A) Synchronization**
★ **Nukta:** Session ki 3 services: Dialog control + Token management + Synchronization (checkpoint).
*Session की 3 services: Dialog control + Token management + Synchronization (checkpoint)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q132.** How many address types (identifiers) are used from sender to receiver in OSI/TCP-IP communication?
*OSI/TCP-IP communication में sender से receiver तक कितने address types (identifiers) use होते हैं?*
- **(A)** 2
- **(B)** 3
- **(C)** 4
- **(D)** 5
✔ **(C) 4**
★ **Nukta:** 4 addresses: Physical(48-bit) / IP(32-bit) / Port(16-bit) / Specific (user-friendly).
*4 addresses: Physical(48-bit) / IP(32-bit) / Port(16-bit) / Specific।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

**Q133.** Who developed the standards for the OSI reference model?
*OSI reference model के standards किसने develop किए?*
- **(A)** ANSI - American National Standards Institute
- **(B)** ISO - International Organization for Standardization
- **(C)** IEEE - Institute of Electrical and Electronics Engineers
- **(D)** ACM - Association for Computing Machinery
✔ **(B) ISO - International Organization for Standardization**
★ **Nukta:** OSI ke standards = ISO ke. ANSI/IEEE/ACM ke alag kaam hain (US standards / LAN / computing society).
*OSI के standards = ISO के। ANSI/IEEE/ACM के अलग काम हैं।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q134.** The session, presentation, and application layers are the ______ support layers.
*Session, Presentation और Application layers ______ support layers हैं।*
- **(A)** user
- **(B)** network
- **(C)** both (a) and (b)
- **(D)** neither (a) nor (b)
✔ **(A) user**
★ **Nukta:** User support = 5,6,7. Network support = 1,2,3. Transport(4) = dono ka bridge.
*User support = 5,6,7। Network support = 1,2,3। Transport(4) = दोनों का bridge।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Hard*

**Q135.** Which of the following is NOT a network support layer?
*निम्नलिखित में से कौन network support layer नहीं है?*
- **(A)** Transport Layer
- **(B)** Network Layer
- **(C)** Data Link Layer
- **(D)** Physical Layer
✔ **(A) Transport Layer**
★ **Nukta:** Yaad rakho: NOT-network-support = Transport. (1,2,3 = network support; 5,6,7 = user support.)
*याद रखो: NOT-network-support = Transport। (1,2,3 = network support; 5,6,7 = user support.)*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Hard*

## Section B — OSI Layer Functions (Layer 1 → Layer 7)

*Which layer does what: Physical, Data Link (LLC/MAC, framing, FCS), Network (logical addressing/routing), Transport (segmentation, end-to-end, ports), Session (dialog/checkpoint), Presentation (translation/encryption/compression), Application (services & protocols).*

**Har layer ka apna kaam hai — yeh exam ka sabse favourite hissa hai: kaun si layer kya karti hai.**

*हर layer का अपना काम है — यह exam का सबसे प्रिय भाग है: कौन-सी layer क्या करती है।*

- Physical (L1) — bits ko signals mein badal kar medium par bhejna; voltage, cables, connectors, topology, data rate.
  - *Physical (L1) — bits को signals में बदलकर medium पर भेजना; voltage, cables, topology, data rate।*
- Data Link (L2) — framing, physical (MAC) addressing, error control, flow control; FCS (error check) trailer; LLC + MAC sub-layers.
  - *Data Link (L2) — framing, MAC addressing, error/flow control; FCS; LLC + MAC sub-layers।*
- Network (L3) — logical (IP) addressing, routing (best path), fragmentation; protocols: IPv4/IPv6, ARP, ICMP, IGMP.
  - *Network (L3) — logical addressing, routing, fragmentation; IPv4/IPv6, ARP, ICMP, IGMP।*
- Transport (L4) — end-to-end delivery, port addressing, segmentation, reliability, flow/congestion control; TCP (reliable) vs UDP (fast).
  - *Transport (L4) — end-to-end delivery, ports, segmentation, flow/congestion control; TCP vs UDP।*
- Session (L5) — sessions/dialog control, synchronization (checkpoints), simplex/half/full dialogs.
  - *Session (L5) — sessions/dialog control, synchronization (checkpoints)।*
- Presentation (L6) — translation (ASCII/EBCDIC), encryption/decryption, compression — 'data ka format'.
  - *Presentation (L6) — translation, encryption/decryption, compression।*
- Application (L7) — user ko services: HTTP, FTP, SMTP, DNS, SNMP — user applications yahin se service lete hain.
  - *Application (L7) — उपयोगकर्ता को सेवाएँ: HTTP, FTP, SMTP, DNS।*
- Yaad karo: 'Some People Fear To Buy Stupid Appliances' ulte kram mein (7→1) bhi poochha jaata hai!
  - *याद रखो: 7→1 क्रम भी पूछा जाता है।*

| Layer | Kaam (key work) | Address / PDU |
|---|---|---|
| Physical | bits → signals | no address / bits |
| Data Link | framing, MAC, FCS | MAC (48-bit) / frame |
| Network | routing, logical address | IP (32/128-bit) / packet |
| Transport | end-to-end, ports | port (16-bit) / segment |
| Session | dialog + checkpoints | — |
| Presentation | translate, encrypt, compress | — |
| Application | user services | — |

### Questions (Easy → Medium → Hard)

**Q136.** Fiber optic cables and coaxial cables function at which OSI layer?
*Fiber optic cables और coaxial cables किस OSI layer पर काम करती हैं?*
- **(A)** Data Link Layer
- **(B)** Physical Layer
- **(C)** Network Layer
- **(D)** Transport Layer
✔ **(B) Physical Layer**
★ **Nukta:** Media (cable, fiber, radio) = Physical layer ka kaam.
*Media (cable, fiber, radio) = Physical layer का काम।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q137.** The Physical layer deals with:
*Physical layer किससे निपटती है?*
- **(A)** Logical addressing
- **(B)** Media, signals and binary transmission / Media, signals और binary transmission
- **(C)** Error correction
- **(D)** Segmentation
✔ **(B) Media, signals and binary transmission**
★ **Nukta:** Physical = bits + signals + media. Baaki sab upar ki layers ka kaam hai.
*Physical = bits + signals + media। बाकी ऊपर की layers का काम है।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q138.** The sub-layer of the Physical layer which directly interfaces with the MAC sub-layer is called:
*Physical layer का वह sub-layer जो सीधे MAC sub-layer से जुड़ता है, कहलाता है:*
- **(A)** Physical signalling sub-layer
- **(B)** Physical data sub-layer
- **(C)** Physical address sub-layer
- **(D)** Physical transport sub-layer
✔ **(A) Physical signalling sub-layer**
★ **Nukta:** PLS (Physical Layer Signalling) = Physical layer ka upper sub-layer jo MAC se directly judta hai.
*PLS (Physical Layer Signalling) = Physical layer का upper sub-layer जो MAC से जुड़ता है।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q139.** Which layer creates the 'collision domain'?
*'Collision domain' कौन-सी layer बनाती है?*
- **(A)** Physical Layer (hubs)
- **(B)** Data Link Layer (switches/bridges)
- **(C)** Network Layer
- **(D)** Transport Layer
✔ **(A) Physical Layer (hubs)**
★ **Nukta:** Hub network = ONE collision domain (Physical). Switch = per-port collision domain (Data Link). Router = broadcast domain boundary (Network).
*Hub network = एक collision domain (Physical)। Switch = per-port collision domain (Data Link)। Router = broadcast domain boundary (Network)।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q140.** Data Link Layer is divided into:
*Data Link Layer किनमें विभाजित है?*
- **(A)** LLC and MAC
- **(B)** Physical and Network
- **(C)** Transport and Session
- **(D)** Application and Presentation
✔ **(A) LLC and MAC**
★ **Nukta:** Data Link = LLC (upper, 802.2) + MAC (lower, 802.3). Ye hamesha saath aate hain.
*Data Link = LLC (ऊपर, 802.2) + MAC (नीचे, 802.3)।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q141.** Physical (hardware) addressing is added at:
*Physical (hardware) addressing किस layer पर जोड़ी जाती है?*
- **(A)** Network
- **(B)** Transport
- **(C)** Data Link
- **(D)** Session
✔ **(C) Data Link**
★ **Nukta:** Physical/MAC address = Data Link. IP/Logical = Network. Port = Transport.
*Physical/MAC address = Data Link। IP/Logical = Network। Port = Transport।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q142.** 'Transparent transmission' is the function of which layer?
*'Transparent transmission' किस layer का काम है?*
- **(A)** Data link
- **(B)** Network
- **(C)** Session
- **(D)** Transport
✔ **(A) Data link**
★ **Nukta:** Data Link = 'transparent service' — Network layer ko pata hi nahi chalta ki neeche kitni mehnat hui.
*Data Link = 'transparent service' — Network layer को नीचे की मेहनत पता नहीं चलती।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q143.** Which layer handles 'hop-to-hop' flow control?
*'Hop-to-hop' flow control कौन-सी layer संभालती है?*
- **(A)** Network
- **(B)** Data Link
- **(C)** Transport
- **(D)** Physical
✔ **(B) Data Link**
★ **Nukta:** Hop-to-hop = Data Link. End-to-end = Transport. Dono flow control karte hain — scope alag hai.
*Hop-to-hop = Data Link। End-to-end = Transport।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q144.** Which OSI layer is responsible for logical addressing?
*Logical addressing के लिए कौन-सी OSI layer जिम्मेदार है?*
- **(A)** Data Link
- **(B)** Network
- **(C)** Transport
- **(D)** Application
✔ **(B) Network**
★ **Nukta:** Logical address = IP = Network layer (L3). Physical address = MAC = Data Link (L2).
*Logical address = IP = Network layer (L3)। Physical address = MAC = Data Link (L2)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q145.** Which layer performs segmentation?
*Segmentation कौन-सी layer करती है?*
- **(A)** Data link
- **(B)** Transport
- **(C)** Network
- **(D)** Session
✔ **(B) Transport**
★ **Nukta:** Segmentation + Reassembly = Transport. (Packetisation Network ki, Framing Data Link ki.)
*Segmentation + Reassembly = Transport। (Packetisation Network की, Framing Data Link की।)*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q146.** Which layer provides end-to-end communication?
*End-to-end communication कौन-सी layer देती है?*
- **(A)** Network
- **(B)** Transport
- **(C)** Session
- **(D)** Physical
✔ **(B) Transport**
★ **Nukta:** End-to-end = Transport. Source-to-destination = Network. Hop-to-hop = Data Link. Bit-by-bit = Physical.
*End-to-end = Transport। Source-to-destination = Network। Hop-to-hop = Data Link। Bit-by-bit = Physical।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q147.** In the OSI model, which layer(s) participate in 'end-to-end' delivery? (1) Network (2) Transport (3) Session (4) Data link
*OSI model में 'end-to-end' delivery में कौन-सी layer(s) भाग लेती हैं? (1) Network (2) Transport (3) Session (4) Data link*
- **(A)** 1, 2 only
- **(B)** 2 only
- **(C)** 1, 2, 3
- **(D)** 2, 3, 4
✔ **(B) 2 only**
★ **Nukta:** End-to-end = Transport only. (Network = host-to-host, Data Link = hop-to-hop.)
*End-to-end = सिर्फ Transport।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q148.** Which layer performs 'service point addressing'?
*'Service point addressing' कौन-सी layer करती है?*
- **(A)** Network
- **(B)** Data Link
- **(C)** Transport
- **(D)** Session
✔ **(C) Transport**
★ **Nukta:** Service point = Port. Port addressing = Transport (16-bit port numbers).
*Service point = Port। Port addressing = Transport (16-bit port numbers)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q149.** Which OSI layer handles message boundaries (knowing where one message ends and the next begins)?
*कौन-सी OSI layer message boundaries संभालती है (एक message कहाँ समाप्त होता है और अगला कहाँ शुरू)?*
- **(A)** Presentation
- **(B)** Session
- **(C)** Transport
- **(D)** Network
✔ **(C) Transport**
★ **Nukta:** Message boundary = transport-level concept (UDP message = poora message).
*Message boundary = transport-level concept।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q150.** Determine the OSI layer responsible for dialogue control (half-duplex or full-duplex communication).
*Dialogue control (half-duplex या full-duplex communication) के लिए कौन-सी OSI layer जिम्मेदार है?*
- **(A)** Session Layer
- **(B)** Transport Layer
- **(C)** Network Layer
- **(D)** Data Link Layer
✔ **(A) Session Layer**
★ **Nukta:** Dialog control + Token management + Synchronization = Session layer ka kaam.
*Dialog control + Token management + Synchronization = Session layer का काम।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q151.** Which layer supports 'checkpointing' (synchronisation for recovery)?
*कौन-सी layer 'checkpointing' (recovery के लिए synchronization) support करती है?*
- **(A)** Transport
- **(B)** Application
- **(C)** Session
- **(D)** Data link
✔ **(C) Session**
★ **Nukta:** Checkpointing = Session (synchronization). Ye exam ka classic sawaal hai.
*Checkpointing = Session।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q152.** Which layer translates data from a format used by the application into a common format (e.g., ASCII to EBCDIC)?
*कौन-सी layer data को application के format से common format में बदलती है (जैसे ASCII से EBCDIC)?*
- **(A)** Application Layer
- **(B)** Presentation Layer
- **(C)** Session Layer
- **(D)** Transport Layer
✔ **(B) Presentation Layer**
★ **Nukta:** Presentation = Translation + Encryption + Compression (TEC). ASCII<->EBCDIC isi layer ka classic example hai.
*Presentation = Translation + Encryption + Compression।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q153.** Which layer is responsible for encryption?
*Encryption के लिए कौन-सी layer जिम्मेदार है?*
- **(A)** Session
- **(B)** Presentation
- **(C)** Application
- **(D)** Transport
✔ **(B) Presentation**
★ **Nukta:** Encryption + Compression + Translation = Presentation (L6).
*Encryption + Compression + Translation = Presentation (L6)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q154.** Which OSI layer ensures interoperability between different data formats?
*कौन-सी OSI layer अलग-अलग data formats के बीच interoperability सुनिश्चित करती है?*
- **(A)** Presentation
- **(B)** Application
- **(C)** Session
- **(D)** Network
✔ **(A) Presentation**
★ **Nukta:** Common format = Presentation. Isi liye ise 'syntax layer' bhi kehte hain.
*Common format = Presentation। इसे 'syntax layer' भी कहते हैं।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q155.** Which OSI layer decides the type of compression?
*कौन-सी OSI layer compression का प्रकार तय करती है?*
- **(A)** Application
- **(B)** Presentation
- **(C)** Transport
- **(D)** Data link
✔ **(B) Presentation**
★ **Nukta:** Compression = Presentation. (Encryption aur translation bhi isi ke saath.)
*Compression = Presentation।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q156.** The term 'Baud Rate' is associated with which layer?
*'Baud Rate' शब्द किस layer से जुड़ा है?*
- **(A)** Network Layer
- **(B)** Data Link Layer
- **(C)** Physical Layer
- **(D)** Application Layer
✔ **(C) Physical Layer**
★ **Nukta:** Baud rate = signalling rate = Physical layer. Bit rate ≠ baud rate (bits per symbol yaad rakho).
*Baud rate = signalling rate = Physical layer। Bit rate ≠ baud rate।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q157.** The layer used to deal with mechanical and electrical specifications is:
*Mechanical और electrical specifications से निपटने वाली layer कौन-सी है?*
- **(A)** Physical Layer
- **(B)** Data Link Layer
- **(C)** Network Layer
- **(D)** Transport Layer
✔ **(A) Physical Layer**
★ **Nukta:** Mechanical + Electrical + Functional + Procedural = Physical layer ke 4 specifications.
*Mechanical + Electrical + Functional + Procedural = Physical layer की 4 specifications।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q158.** The Physical layer is responsible for which of the following operations?
*Physical layer निम्नलिखित में से किन operations के लिए जिम्मेदार है?*
- **(A)** Line coding
- **(B)** Channel coding
- **(C)** Modulation
- **(D)** All of the above
✔ **(D) All of the above**
★ **Nukta:** Physical layer = Line coding + Channel coding + Modulation + signals/media — 'All of the above' yaad rakho.
*Physical layer = Line coding + Channel coding + Modulation। 'All of the above' याद रखो।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q159.** Transmission data rate is decided by:
*Transmission data rate कौन तय करती है?*
- **(A)** Network layer
- **(B)** Physical layer
- **(C)** Data Link layer
- **(D)** Transport layer
✔ **(B) Physical layer**
★ **Nukta:** Data rate = Physical layer. (Throughput/delay performance bhi isi layer ke signals par depend karti hai.)
*Data rate = Physical layer।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Medium*

**Q160.** The physical layer translates logical communication requests from the ______ into hardware-specific operations.
*Physical layer, ______ के logical communication requests को hardware-specific operations में बदलता है।*
- **(A)** Network layer
- **(B)** Transport layer
- **(C)** Data link layer
- **(D)** Application layer
✔ **(C) Data link layer**
★ **Nukta:** Each layer serves the layer ABOVE it — physical serves data link. Exam banks sometimes mis-key this as 'network layer'; the correct neighbour is the data link layer.
*हर layer अपने ऊपर वाली layer की सेवा करती है — physical, data link की। कुछ exam banks इसे गलती से 'network layer' लिखते हैं; सही उत्तर data link layer है।*
*[Source: InstrumentationTools 150 CN MCQs (key corrected vs Forouzan)] · Medium*

**Q161.** The Application layer is implemented in:
*Application layer कहाँ implement होती है?*
- **(A)** End system
- **(B)** NIC
- **(C)** Ethernet
- **(D)** Packet transport
✔ **(A) End system**
★ **Nukta:** End systems (hosts) implement layers up to the application; switches implement only Layers 1-2, routers only Layers 1-3.
*End systems (hosts) application तक की layers implement करते हैं; switches सिर्फ Layers 1-2, routers सिर्फ Layers 1-3।*
*[Source: Sanfoundry CN MCQs — Reference Models] · Medium*

**Q162.** Which statement best describes the difference between the LLC and MAC sub-layers?
*LLC और MAC sub-layers के बीच अंतर सबसे अच्छा कौन बताता है?*
- **(A)** LLC handles physical addressing, MAC handles flow control / LLC physical addressing करता है, MAC flow control करता है
- **(B)** LLC provides the service interface to the Network layer; MAC controls access to the medium / LLC, Network layer को service interface देता है; MAC medium तक access control करता है
- **(C)** LLC works only in wireless networks, MAC only in wired networks / LLC सिर्फ wireless में, MAC सिर्फ wired में काम करता है
- **(D)** LLC performs framing, MAC performs routing / LLC framing करता है, MAC routing करता है
✔ **(B) LLC provides the service interface to the Network layer; MAC controls access to the medium**
★ **Nukta:** LLC = upar wala sub-layer (network layer se link). MAC = neeche wala (medium access + physical address).
*LLC = ऊपर का sub-layer। MAC = नीचे का (medium access + physical address)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

**Q163.** A frame is received at the Data Link layer with an incorrect FCS. What will happen?
*Data Link layer पर frame गलत FCS के साथ प्राप्त होता है। क्या होगा?*
- **(A)** Frame discarded
- **(B)** Frame corrected
- **(C)** Sent to network layer
- **(D)** Re-transmitted automatically
✔ **(A) Frame discarded**
★ **Nukta:** Bad FCS = frame drop (discard). Correction/Data Link khud re-transmit nahi karti — wo ARQ/higher layer ka decision hai.
*गलत FCS = frame discard।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

**Q164.** The ______ layer is responsible for delivering data units from one station to the next without errors.
*______ layer data units को एक station से अगले station तक बिना errors पहुँचाने के लिए जिम्मेदार है।*
- **(A)** Transport
- **(B)** Network
- **(C)** Data link
- **(D)** Physical
✔ **(C) Data link**
★ **Nukta:** 'Station to next station' = Data Link (hop-to-hop). 'Source to destination' = Network.
*'Station to next station' = Data Link। 'Source to destination' = Network।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q165.** ______ Layer is responsible for framing, error detection and physical addressing.
*______ Layer framing, error detection और physical addressing के लिए जिम्मेदार है।*
- **(A)** Network
- **(B)** Transport
- **(C)** Application
- **(D)** Data Link
✔ **(D) Data Link**
★ **Nukta:** Framing + Error detection + MAC addressing = Data Link ka 'trio'.
*Framing + Error detection + MAC addressing = Data Link का trio।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q166.** From which layer does the Data Link layer collect packets and encapsulate them into frames for transmission?
*Data Link layer किस layer से packets लेकर उन्हें transmission के लिए frames में encapsulate करती है?*
- **(A)** Transport layer
- **(B)** Application layer
- **(C)** Network layer
- **(D)** Physical layer
✔ **(C) Network layer**
★ **Nukta:** Encapsulation: Network packet -> Data Link frame -> Physical bits. Upar se neeche.
*Encapsulation: Network packet -> Data Link frame -> Physical bits।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q167.** IPv4 and IPv6 work at which OSI layer?
*IPv4 और IPv6 किस OSI layer पर काम करते हैं?*
- **(A)** Data link layer
- **(B)** Network layer
- **(C)** Transport layer
- **(D)** Application layer
✔ **(B) Network layer**
★ **Nukta:** IP = Internet Protocol = Network/Internet layer (L3). Hamesha!
*IP = Network/Internet layer (L3)।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

**Q168.** The ______ layer is responsible for the source-to-destination delivery of a packet across multiple network links.
*______ layer एक packet की multiple network links के बीच source-to-destination delivery के लिए जिम्मेदार है।*
- **(A)** Transport
- **(B)** Network
- **(C)** Data link
- **(D)** Physical
✔ **(B) Network**
★ **Nukta:** Source-to-destination = Network. Process-to-process = Transport. Station-to-station = Data Link.
*Source-to-destination = Network। Process-to-process = Transport। Station-to-station = Data Link।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q169.** Which layer is responsible for reliable delivery in the OSI model?
*OSI model में reliable delivery के लिए कौन-सी layer जिम्मेदार है?*
- **(A)** Session
- **(B)** Transport
- **(C)** Network
- **(D)** Application
✔ **(B) Transport**
★ **Nukta:** Reliable = Transport. (OSI Transport class 4 = error recovery wali service.)
*Reliable = Transport।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

**Q170.** Which layer is responsible for process-to-process delivery?
*Process-to-process delivery के लिए कौन-सी layer जिम्मेदार है?*
- **(A)** Network layer
- **(B)** Transport layer
- **(C)** Session layer
- **(D)** Data link layer
✔ **(B) Transport layer**
★ **Nukta:** Process-to-process = Transport (ports ke saath). Host-to-host = Network (IP ke saath).
*Process-to-process = Transport। Host-to-host = Network।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q171.** Which OSI layer is responsible for encryption and compression?
*Encryption और compression के लिए कौन-सी OSI layer जिम्मेदार है?*
- **(A)** Presentation Layer
- **(B)** Session Layer
- **(C)** Transport Layer
- **(D)** Network Layer
✔ **(A) Presentation Layer**
★ **Nukta:** Trio yaad rakho: Translation, Encryption, Compression = Presentation.
*Trio: Translation, Encryption, Compression = Presentation।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

**Q172.** Which layer helps to present data in one form on a host to another host in its native representation?
*कौन-सी layer एक host पर किसी form में data को दूसरे host पर उसकी native representation में प्रस्तुत करने में मदद करती है?*
- **(A)** Application Layer
- **(B)** Presentation Layer
- **(C)** Session Layer
- **(D)** Transport Layer
✔ **(B) Presentation Layer**
★ **Nukta:** Native format <-> common format = Presentation (translation).
*Native format <-> common format = Presentation।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q173.** ______ layer defines how data is formatted, presented, encoded, and converted for use on the network.
*______ layer तय करती है कि data network में उपयोग के लिए कैसे format, present, encode और convert होता है।*
- **(A)** Transport
- **(B)** Presentation
- **(C)** Application
- **(D)** Physical
✔ **(B) Presentation**
★ **Nukta:** 'Formatted, presented, encoded, converted' = Presentation ke liye mnemonic-type line.
*'Formatted, presented, encoded, converted' = Presentation।*
*[Source: Central exams — SSC/Bank/Insurance Computer Awareness (BYJU'S)] · Medium*

**Q174.** Which layer provides services to the user?
*कौन-सी layer user को services देती है?*
- **(A)** Application layer
- **(B)** Session layer
- **(C)** Presentation layer
- **(D)** Physical layer
✔ **(A) Application layer**
★ **Nukta:** User ke sabse kareeb = Application layer (L7).
*User के सबसे करीब = Application layer (L7)।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q175.** A server at a company is using TCP/IP to connect to the network and is running multiple applications. At which OSI layer is this server operating?
*एक company का server network से जुड़ने के लिए TCP/IP use कर रहा है और अनेक applications चला रहा है। यह server किस OSI layer पर काम कर रहा है?*
- **(A)** Application Layer
- **(B)** Physical Layer
- **(C)** Network Layer
- **(D)** Transport Layer
✔ **(A) Application Layer**
★ **Nukta:** Server + running applications = Application layer.
*Server + applications = Application layer।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q176.** Simple Network Management Protocol (SNMP) runs on:
*Simple Network Management Protocol (SNMP) किस layer पर चलता है?*
- **(A)** Application layer
- **(B)** Transport layer
- **(C)** Network layer
- **(D)** Data link layer
✔ **(A) Application layer**
★ **Nukta:** SNMP/DNS/HTTP/FTP/SMTP = Application layer protocols. UDP/TCP = Transport. IP = Network.
*SNMP/DNS/HTTP/FTP/SMTP = Application layer protocols।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q177.** Consider the statements:
S1: Network layer handles both logical addressing and routing.
S2: Transport layer handles segmentation and reassembly.
Which is correct?
*Statements देखिए:
S1: Network layer logical addressing और routing दोनों संभालती है।
S2: Transport layer segmentation और reassembly संभालती है।
कौन सा सही है?*
- **(A)** Only S1
- **(B)** Only S2
- **(C)** Both S1 and S2
- **(D)** Neither S1 nor S2
✔ **(C) Both S1 and S2**
★ **Nukta:** Network = IP addressing + Routing. Transport = Segmentation + Reassembly. Dono sahi.
*Network = IP addressing + Routing। Transport = Segmentation + Reassembly।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

**Q178.** Repeaters function in:
*Repeaters किस layer पर काम करते हैं?*
- **(A)** Physical layer
- **(B)** Data link layer
- **(C)** Network layer
- **(D)** Both (A) and (B)
✔ **(A) Physical layer**
★ **Nukta:** Repeater/Hub = Physical (L1). Bridge/Switch = Data Link (L2). Router = Network (L3).
*Repeater/Hub = Physical (L1)। Bridge/Switch = Data Link (L2)। Router = Network (L3)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q179.** The physical layer is responsible for:
*Physical layer किसके लिए जिम्मेदार है?*
- **(A)** Bit-by-bit delivery
- **(B)** Port to port delivery
- **(C)** Process to process delivery
- **(D)** Application to application delivery
✔ **(A) Bit-by-bit delivery**
★ **Nukta:** Bit-by-bit = Physical. Hop-to-hop = Data Link. Source-to-destination = Network. Process-to-process = Transport.
*Bit-by-bit = Physical। Hop-to-hop = Data Link। Source-to-destination = Network। Process-to-process = Transport।*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q180.** Which one of the following is a data link (Layer 2) protocol?
*निम्न में से कौन data link (Layer 2) protocol है?*
- **(A)** Point-to-Point Protocol (PPP)
- **(B)** HDLC
- **(C)** Ethernet
- **(D)** All of these
✔ **(D) All of these**
★ **Nukta:** Layer 2 protocols = PPP, HDLC, Ethernet, Frame Relay, ATM (cell-based). Network layer = IP, ICMP, ARP.
*Layer 2 protocols = PPP, HDLC, Ethernet, Frame Relay, ATM (cell-based)। Network layer = IP, ICMP, ARP।*
*[Source: InstrumentationTools 150 CN MCQs] · Hard*

**Q181.** Which layer of the OSI model is responsible for the transmission and reception of unstructured raw data between a device and a physical transmission medium?
*OSI model की कौन-सी layer device और physical transmission medium के बीच unstructured raw data के transmission और reception के लिए जिम्मेदार है?*
- **(A)** Transport layer
- **(B)** Data-Link layer
- **(C)** Network layer
- **(D)** Physical layer
✔ **(D) Physical layer**
★ **Nukta:** 'Raw data + physical medium' = Physical layer. SSC/Railway mein ye one-liner common hai.
*'Raw data + physical medium' = Physical layer।*
*[Source: Central exams — SSC/Railway/UPSC Computer Awareness (Exampundit)] · Hard*

**Q182.** Bridge works in which layer of the OSI model?
*Bridge OSI model की किस layer पर काम करता है?*
- **(A)** Application layer
- **(B)** Transport layer
- **(C)** Network layer
- **(D)** Data link layer
✔ **(D) Data link layer**
★ **Nukta:** Bridge/Switch = L2. Router = L3. Hub/Repeater = L1. Gateway = L4+.
*Bridge/Switch = L2। Router = L3। Hub/Repeater = L1। Gateway = L4+।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2) · also asked in KVS PGT CS 2018 Official Paper] · Hard*

**Q183.** The reliable data transfer is implemented by:
*Reliable data transfer कौन-सी layer implement करती है?*
- **(A)** Network layer
- **(B)** Physical layer
- **(C)** Presentation layer
- **(D)** Transport layer
✔ **(D) Transport layer**
★ **Nukta:** Reliable delivery = Transport (TCP). IP (Network) unreliable hai — best-effort only.
*Reliable delivery = Transport (TCP)। IP (Network) unreliable है।*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q184.** If a port number is 16 bits (2 bytes), what is the MINIMUM size of the transport-layer header needed to carry the port addresses?
*यदि port number 16 bits (2 bytes) का है, तो port addresses ले जाने के लिए transport-layer header की MINIMUM size कितनी होगी?*
- **(A)** 2 bytes
- **(B)** 4 bytes
- **(C)** 8 bytes
- **(D)** 20 bytes
✔ **(B) 4 bytes**
★ **Nukta:** Min transport header (ports only) = 4 bytes. UDP = 8, TCP = 20 — teeno numbers exam mein aate hain.
*Min transport header (ports only) = 4 bytes। UDP = 8, TCP = 20।*
*[Source: Forouzan Ch1 (Q1-23) — Practice Set] · Hard*

**Q185.** Application layer protocol defines:
*Application layer protocol क्या define करता है?*
- **(A)** Types of messages exchanged / कौन-से messages आदान-प्रदान होते हैं
- **(B)** Rules for when and how processes send and respond to messages / processes messages कब और कैसे भेजें/जवाब दें — इसके rules
- **(C)** Message format, syntax and semantics / Message format, syntax और semantics
- **(D)** All of the above / उपरोक्त सभी
✔ **(D) All of the above**
★ **Nukta:** Application protocol = Message types + Rules + Format. 'All of the above' hi jawab hai.
*Application protocol = Message types + Rules + Format।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Hard*

**Q186.** SMTP, FTP and DNS are the protocols of which layer of the OSI model?
*SMTP, FTP और DNS OSI model की किस layer के protocols हैं?*
- **(A)** Network layer
- **(B)** Transport layer
- **(C)** Application layer
- **(D)** Data Link layer
✔ **(C) Application layer**
★ **Nukta:** User-facing protocols (HTTP, FTP, SMTP, DNS, POP3, IMAP) = Application layer.
*User-facing protocols = Application layer।*
*[Source: Central exams — SSC/Railway/UPSC Computer Awareness (Exampundit)] · Hard*

## Section C — TCP/IP Model

*TCP/IP (DoD, 1970s): 4/5 layers, layer mapping to OSI, Internet layer protocols, address levels.*

**TCP/IP model (DoD model) practical model hai jo aaj Internet par chalta hai — 4 layers (kuch jagah 5) aur OSI ka simplified version.**

*TCP/IP model (DoD model) व्यावहारिक model है जो आज Internet पर चलता है — 4 layers (कहीं 5) और OSI का सरल रूप।*

- TCP/IP ke 4 layers: Network Access (Physical + Data Link), Internet, Transport, Application (Session+Presentation+Application mil kar).
  - *TCP/IP की 4 layers: Network Access, Internet, Transport, Application।*
- 5-layer version: Physical, Data Link, Network, Transport, Application — books mein yeh zyada padhaya jata hai.
  - *5-layer version: Physical, Data Link, Network, Transport, Application।*
- Internet layer: IP, ARP, ICMP, IGMP — packet delivery ke liye.
  - *Internet layer: IP, ARP, ICMP, IGMP।*
- Transport layer: TCP (connection-oriented, reliable) aur UDP (connectionless, fast).
  - *Transport layer: TCP (connection-oriented) और UDP (connectionless)।*
- Application layer: HTTP, FTP, SMTP, DNS, DHCP, SNMP — OSI ke top 3 layers ka kaam.
  - *Application layer: HTTP, FTP, SMTP, DNS — OSI की top 3 layers का काम।*
- Network Access layer: Ethernet, Wi-Fi, PPP — framing + physical transmission.
  - *Network Access layer: Ethernet, Wi-Fi, PPP।*

| TCP/IP Layer | OSI Layers | Protocols |
|---|---|---|
| Application | Application + Presentation + Session | HTTP, FTP, SMTP, DNS |
| Transport | Transport | TCP, UDP |
| Internet | Network | IP, ARP, ICMP, IGMP |
| Network Access | Data Link + Physical | Ethernet, Wi-Fi, PPP |

### Questions (Easy → Medium → Hard)

**Q187.** Which is the standard protocol suite of the Internet?
*Internet की मानक protocol suite कौन-सी है?*
- **(A)** TCP/IP
- **(B)** UDP
- **(C)** FTP
- **(D)** WWW
✔ **(A) TCP/IP**
★ **Nukta:** UDP/FTP इसी suite के अंदर के protocols हैं; WWW तो सेवा है, protocol नहीं.
*UDP/FTP इसी suite के अंदर के protocols हैं; WWW तो सेवा है, protocol नहीं.*
*[Source: IBPS RRB PO Computer Awareness PYQ (via meritnotes) + SSC MTS computer PYQ (via Testbook)] · Easy*

**Q188.** The TCP/IP model was developed ______ the OSI model.
*TCP/IP model, OSI model के ______ develop हुआ।*
- **(A)** prior to
- **(B)** after
- **(C)** simultaneous to
- **(D)** none of these
✔ **(A) prior to**
★ **Nukta:** TCP/IP (1970s, adopted 1983) PEHLE; OSI (1984) BAAD mein. 'Prior to' yaad rakho.
*TCP/IP (1970s) पहले; OSI (1984) बाद में।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q189.** The TCP/IP ______ layer is equivalent to the combined Session, Presentation and Application layers of the OSI model.
*TCP/IP की ______ layer, OSI model की Session, Presentation और Application layers के समकक्ष है।*
- **(A)** application
- **(B)** network
- **(C)** data link
- **(D)** physical
✔ **(A) application**
★ **Nukta:** Mapping: TCP/IP Application = OSI Session+Presentation+Application; TCP/IP Internet = OSI Network; TCP/IP Network Access = OSI Data Link+Physical.
*Mapping: TCP/IP Application = OSI 5+6+7; Internet = Network; Network Access = Data Link+Physical।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q190.** The number of layers in the Internet protocol stack (reference model) is:
*Internet protocol stack (reference model) में layers की संख्या कितनी है?*
- **(A)** 5
- **(B)** 7
- **(C)** 6
- **(D)** 3
✔ **(A) 5**
★ **Nukta:** 5-layer Internet stack vs 4-layer TCP/IP suite vs 7-layer OSI — teeno numbers exam mein aate hain!
*5-layer Internet stack, 4-layer TCP/IP suite, 7-layer OSI — तीनों numbers याद रखो!*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q191.** The Data Link layer and Physical layer of the OSI model combine to form the ______ layer of the TCP/IP model.
*OSI model की Data Link और Physical layers मिलकर TCP/IP model की ______ layer बनाती हैं।*
- **(A)** Network Access
- **(B)** Internet
- **(C)** Host to Host
- **(D)** Application
✔ **(A) Network Access**
★ **Nukta:** OSI 1+2 = TCP/IP Network Access. OSI 5+6+7 = TCP/IP Application. Bas ye 2 mappings yaad rakho.
*OSI 1+2 = Network Access। OSI 5+6+7 = Application।*
*[Source: Central exams — SSC/Bank Computer Awareness (BYJU'S)] · Medium*

**Q192.** IP (Internet Protocol) is a protocol of the ______ layer of the TCP/IP model.
*IP (Internet Protocol) TCP/IP model की ______ layer का protocol है.*
- **(A)** Network Access
- **(B)** Internet
- **(C)** Transport
- **(D)** Application
✔ **(B) Internet**
★ **Nukta:** IP = Internet layer. TCP/UDP = Transport. Ethernet = Network Access.
*IP = Internet layer। TCP/UDP = Transport। Ethernet = Network Access।*
*[Source: Central exams — SSC/Bank Computer Awareness (BYJU'S)] · Medium*

**Q193.** In TCP/IP, which layer uses specific (user-friendly) addresses — e.g. a URL like example.com?
*TCP/IP में कौन-सी layer specific (user-friendly) addresses use करती है — जैसे example.com जैसी URL?*
- **(A)** Application layer
- **(B)** Network layer
- **(C)** Data link layer
- **(D)** Physical layer
✔ **(A) Application layer**
★ **Nukta:** Address levels: Application = specific (URL), Transport = port (16-bit), Network = IP (32/128-bit), Data Link = MAC (48-bit).
*Address levels: Application = specific, Transport = port, Network = IP, Data Link = MAC।*
*[Source: Forouzan Ch1 (Q1-24) — Practice Set] · Medium*

**Q194.** In the TCP/IP model, a link-layer switch operates at which layers?
*TCP/IP model में link-layer switch किन layers पर काम करता है?*
- **(A)** Network and Transport layers
- **(B)** Physical and Data Link layers
- **(C)** Application layer only
- **(D)** All five layers
✔ **(B) Physical and Data Link layers**
★ **Nukta:** Switch = L1+L2 (Network Access). Router = L3 tak. Gateway = L4+.
*Switch = L1+L2। Router = L3 तक। Gateway = L4+।*
*[Source: Forouzan Ch1 (Q1-16) — Practice Set] · Medium*

**Q195.** TCP/IP model does not have ______ layer but the OSI model has it.
*TCP/IP model में ______ layer नहीं है पर OSI model में है।*
- **(A)** Session layer
- **(B)** Presentation layer
- **(C)** Application layer
- **(D)** Both (a) and (b)
✔ **(D) Both (a) and (b)**
★ **Nukta:** TCP/IP mein Session + Presentation nahi hoti — dono Application mein merge ho jaati hain.
*TCP/IP में Session + Presentation नहीं होती — दोनों Application में merge होती हैं।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Hard*

**Q196.** Which of the following is NOT a part of the TCP/IP model?
*निम्नलिखित में से कौन TCP/IP model का हिस्सा नहीं है?*
- **(A)** Application
- **(B)** Transport
- **(C)** Data link
- **(D)** Session
✔ **(D) Session**
★ **Nukta:** TCP/IP ke 4 layers: Application, Transport, Internet, Network Access. Session sirf OSI mein.
*TCP/IP की 4 layers: Application, Transport, Internet, Network Access। Session सिर्फ OSI में।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Hard*

**Q197.** How many layers are there in the TCP/IP model (original 4-layer suite)?
*TCP/IP model (मूल 4-layer suite) में कितनी layers हैं?*
- **(A)** Seven
- **(B)** Five
- **(C)** Four
- **(D)** Nine
✔ **(C) Four**
★ **Nukta:** 4-layer TCP/IP: Network Access + Internet + Transport (Host-to-Host) + Application.
*4-layer TCP/IP: Network Access + Internet + Transport + Application।*
*[Source: Central exams — SSC/Bank Computer Awareness (BYJU'S)] · Hard*

**Q198.** Which of the following is NOT a layer of the TCP/IP model? (Host-to-Host / Internet / Network Access / Physical)
*निम्नलिखित में से कौन TCP/IP model की layer नहीं है? (Host-to-Host / Internet / Network Access / Physical)*
- **(A)** Host to Host
- **(B)** Internet
- **(C)** Network Access
- **(D)** Physical
✔ **(D) Physical**
★ **Nukta:** TCP/IP ki 4 layers: Network Access, Internet, Host-to-Host, Application. 'Physical' alag layer nahi hai.
*TCP/IP की 4 layers: Network Access, Internet, Host-to-Host, Application।*
*[Source: Central exams — SSC/Bank Computer Awareness (BYJU'S)] · Hard*

## Section D — Comparison, Encapsulation & PDUs

*OSI vs TCP/IP, encapsulation order & direction, PDUs per layer, numericals.*

**OSI aur TCP/IP mein kya fark hai, aur data kaise packets/frames mein badal kar chalta hai (encapsulation) — yeh concepts numericals ke liye zaroori hain.**

*OSI और TCP/IP में क्या फ़र्क़ है, और data कैसे packets/frames में बदलकर चलता है (encapsulation)।*

- OSI = reference model (7 layers, theory); TCP/IP = practical model (4 layers, Internet par chalta hai).
  - *OSI = reference model (7 layers); TCP/IP = practical model (4 layers)।*
- Encapsulation: sender par har layer header add karti hai — data → segment → packet → frame → bits.
  - *Encapsulation: sender पर हर layer header जोड़ती है — data → segment → packet → frame → bits।*
- De-encapsulation: receiver par ulta — bits → frame → packet → segment → data; har layer apni header utarti hai.
  - *De-encapsulation: receiver पर उल्टा; हर layer अपनी header उतारती है।*
- PDU: Physical = bits; Data Link = frame; Network = packet/datagram; Transport = segment; upper layers = message.
  - *PDU: Physical = bits; Data Link = frame; Network = packet; Transport = segment; ऊपर की layers = message।*
- Address bhi har level par milte hain: MAC (hop-to-hop), IP (source-to-destination), port (process-to-process).
  - *Address हर level पर: MAC (hop-to-hop), IP (source-to-destination), port (process-to-process)।*
- Data link header + trailer add karti hai (FCS), baaki layers sirf header.
  - *Data link header + trailer जोड़ती है (FCS), बाक़ी सिर्फ़ header।*

| Stage | Kya banta hai | Header kaun lagata hai |
|---|---|---|
| Data | message | Application/Presentation/Session |
| Segment | data + port info | Transport |
| Packet | segment + IP addresses | Network |
| Frame | packet + MAC + FCS | Data Link |
| Bits | signals | Physical |

### Questions (Easy → Medium → Hard)

**Q199.** Identify the correct order of data encapsulation from Layer 7 to Layer 1:
*Layer 7 से Layer 1 तक data encapsulation का सही क्रम पहचानिए:*
- **(A)** Data → Segment → Packet → Frame → Bits
- **(B)** Data → Packet → Segment → Frame → Bits
- **(C)** Bits → Frame → Packet → Segment → Data
- **(D)** Data → Frame → Packet → Segment → Bits
✔ **(A) Data → Segment → Packet → Frame → Bits**
★ **Nukta:** Encapsulation order: Data -> Segment -> Packet -> Frame -> Bits. Mnemonic: 'Do Some People Fear Barking?'
*Encapsulation: Data -> Segment -> Packet -> Frame -> Bits।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q200.** Encapsulation happens from:
*Encapsulation किस दिशा में होती है?*
- **(A)** Top to bottom
- **(B)** Bottom to top
- **(C)** Random
- **(D)** Parallel
✔ **(A) Top to bottom**
★ **Nukta:** Sender = encapsulation (top->bottom, headers add). Receiver = de-encapsulation (bottom->top, headers remove).
*Sender = encapsulation (top->bottom)। Receiver = de-encapsulation (bottom->top)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q201.** In the layer hierarchy, as the data packet moves from the upper to the lower layers, headers are:
*Layer hierarchy में, जब data packet ऊपर से नीचे की layers की ओर जाता है, तो headers:*
- **(A)** Added
- **(B)** Removed
- **(C)** Rearranged
- **(D)** Modified
✔ **(A) Added**
★ **Nukta:** Down the stack = headers ADD. Up the stack = headers REMOVE.
*नीचे की ओर = headers ADD। ऊपर की ओर = headers REMOVE।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q202.** In TCP/IP, which data unit is encapsulated INSIDE a frame?
*TCP/IP में कौन-सा data unit frame के अंदर encapsulate होता है?*
- **(A)** A segment
- **(B)** A datagram
- **(C)** A bit
- **(D)** A message
✔ **(B) A datagram**
★ **Nukta:** Frame ke andar DATAGRAM hota hai. Segment -> Datagram -> Frame -> Bits.
*Frame के अंदर DATAGRAM होता है।*
*[Source: Forouzan Ch1 (Q1-20) — Practice Set] · Medium*

**Q203.** In the TCP/IP model, the unit of data at the transport layer is called a:
*TCP/IP model में transport layer पर data की unit कहलाती है:*
- **(A)** Packet
- **(B)** Segment
- **(C)** Frame
- **(D)** Stream
✔ **(B) Segment**
★ **Nukta:** PDU pairs: Transport = Segment, Network = Datagram/Packet, Data Link = Frame, Physical = Bits.
*PDU: Transport = Segment, Network = Datagram, Data Link = Frame, Physical = Bits।*
*[Source: Forouzan Ch1 (Q1-20/21) — Practice Set] · Medium*

**Q204.** A system uses five protocol layers. The application creates a 100-byte message and EVERY layer (including the 5th and the 1st) adds a 10-byte header. What is the efficiency (application bytes / total transmitted bytes)?
*एक system में पाँच protocol layers हैं। Application 100-byte message बनाती है और हर layer (5वीं और 1वीं सहित) 10-byte header जोड़ती है। Efficiency कितनी होगी (application bytes / कुल transmitted bytes)?*
- **(A)** 50%
- **(B)** 66.7%
- **(C)** 75%
- **(D)** 80%
✔ **(B) 66.7%**
★ **Nukta:** Encapsulation overhead numerical: efficiency = data / (data + headers). 100/(100+50) = 66.7%.
*Efficiency = data / (data + headers) = 100/150 = 66.7%।*
*[Source: Forouzan Ch1 (P1-11) — Practice Set (Problem)] · Medium*

**Q205.** A source S and destination D are connected through ONE intermediate router R. How many times does a packet visit the Network layer and the Data Link layer during the journey?
*Source S और destination D के बीच एक intermediate router R है। यात्रा के दौरान packet Network layer और Data Link layer को कितनी बार visit करता है?*
- **(A)** Network layer - 4 times, Data link layer - 4 times
- **(B)** Network layer - 4 times, Data link layer - 6 times
- **(C)** Network layer - 2 times, Data link layer - 4 times
- **(D)** Network layer - 3 times, Data link layer - 4 times
✔ **(D) Network layer - 3 times, Data link layer - 4 times**
★ **Nukta:** Formula: n routers -> Network layer visits = n+2, Data Link visits = 2(n+1). Yahan n=1 -> NL=3, DL=4.
*Formula: n routers -> Network layer = n+2, Data Link = 2(n+1)। यहाँ n=1 -> NL=3, DL=4।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

# TOPIC 3 — Addressing (MAC, IPv4, IPv6, Port, DNS)

## Section A — Address Levels & MAC Address (Physical Address)

*Forouzan's four address levels; the 48-bit burned-in MAC address, unicast/multicast/broadcast MAC.*

**Forouzan ke hisaab se communication mein 4 levels ke addresses lagte hain — physical (MAC), logical (IP), port, aur application. MAC address data link layer ka physical address hai.**

*Forouzan के अनुसार communication में 4 स्तर के addresses लगते हैं — physical (MAC), logical (IP), port, और application।*

- Physical address (MAC) — node ka data link address; NIC par burned-in hota hai isliye 'burned-in address' bhi; 48 bits (6 bytes) ka.
  - *Physical address (MAC) — node का data link address; NIC पर burned-in; 48 bits (6 bytes) का।*
- MAC flat address hota hai (hierarchy nahi) — har hop par badalta hai: frame ka source/dest MAC har link ke hisaab se.
  - *MAC flat address होता है — हर hop पर बदलता है (frame का source/dest MAC)।*
- Unicast (ek node), Multicast (group), Broadcast (sab) — MAC ke 3 types; broadcast MAC = FF-FF-FF-FF-FF-FF.
  - *Unicast (एक), Multicast (समूह), Broadcast (सब); broadcast MAC = FF-FF-FF-FF-FF-FF।*
- Logical address (IP) — network layer ka address, poore network mein unique, routing ke liye; har hop par nahi, end-to-end same rehta hai.
  - *Logical address (IP) — network layer का address, end-to-end same रहता है।*
- Port address — transport layer, process ko identify karti hai; socket = IP + port.
  - *Port address — transport layer; socket = IP + port।*
- Application address (jaise e-mail address) — user ki pehchaan, sabse upar ki layer.
  - *Application address (जैसे e-mail address) — उपयोगकर्ता की पहचान।*

| Address Level | Layer | Size / Example |
|---|---|---|
| Physical (MAC) | Data Link | 48-bit, FF-FF-FF-FF-FF-FF broadcast |
| Logical (IP) | Network | 32-bit IPv4 / 128-bit IPv6 |
| Port | Transport | 16-bit (0–65535) |
| Application | Application | e-mail address, URL |

### Questions (Easy → Medium → Hard)

**Q206.** Which of the following is a static hardware address?
*निम्न में से कौन-सा static hardware address है?*
- **(A)** IP address
- **(B)** MAC address
- **(C)** Port number
- **(D)** Domain name
✔ **(B) MAC address**
★ **Nukta:** Static = burned into hardware (MAC). Dynamic/logical = configured (IP via DHCP, port per connection, name via DNS).
*Static = hardware में burned (MAC)। Dynamic/logical = configure होते हैं (IP via DHCP, port per connection, name via DNS)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q207.** A MAC address is also called a ______ address.
*MAC address को ______ address भी कहा जाता है।*
- **(A)** Physical address
- **(B)** Logical address
- **(C)** Source address
- **(D)** Destination address
✔ **(A) Physical address**
★ **Nukta:** MAC = physical/hardware address (burned-in, 48-bit). IP = logical address (configured). Both change hands at different layers.
*MAC = physical/hardware address (burned-in, 48-bit)। IP = logical address (configured)।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1) · also BCI_SCI ST-7] · Medium*

**Q208.** The address used in the Data Link Layer is called:
*Data Link Layer में उपयोग होने वाले address को क्या कहते हैं?*
- **(A)** Logical address
- **(B)** Port address
- **(C)** MAC address
- **(D)** IP address
✔ **(C) MAC address**
★ **Nukta:** Layer-address map again: Data link→MAC, Network→IP, Transport→Port, Application→socket.
*Layer-address map: Data link→MAC, Network→IP, Transport→Port, Application→socket।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q209.** Which address identifies a unique device on a local network segment?
*Local network segment पर कौन-सा address एक unique device की पहचान करता है?*
- **(A)** IP address
- **(B)** MAC address
- **(C)** Gateway
- **(D)** Subnet mask
✔ **(B) MAC address**
★ **Nukta:** L2 delivery (same network) = MAC. L3 delivery (across networks) = IP. Exam loves this pair.
*L2 delivery (same network) = MAC। L3 delivery (across networks) = IP। Exam इस जोड़ी को बहुत पूछता है।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

**Q210.** What type of MAC address is FF:FF:FF:FF:FF:FF?
*FF:FF:FF:FF:FF:FF किस प्रकार का MAC address है?*
- **(A)** Unicast
- **(B)** Multicast
- **(C)** Broadcast
- **(D)** Loopback
✔ **(C) Broadcast**
★ **Nukta:** MAC broadcast = FF:FF:FF:FF:FF:FF (all 48 bits 1). Unicast = first byte's last bit 0; multicast = first byte's last bit 1.
*MAC broadcast = FF:FF:FF:FF:FF:FF (सभी 48 bits 1)। Unicast = first byte का अंतिम bit 0; multicast = first byte का अंतिम bit 1।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

**Q211.** Which addresses are used in an internet employing the TCP/IP protocols?
*TCP/IP protocols वाले internet में कौन-से addresses उपयोग होते हैं?*
- **(A)** Physical address and logical address
- **(B)** Port address
- **(C)** Specific address
- **(D)** All of these
✔ **(D) All of these**
★ **Nukta:** Forouzan's 4 address levels: Physical(48-bit MAC) at data link, IP(32-bit) at network, Port(16-bit) at transport, Specific (socket) at application.
*Forouzan की 4 address levels: Physical(48-bit MAC) data link पर, IP(32-bit) network पर, Port(16-bit) transport पर, Specific (socket) application पर।*
*[Source: LMT MCQ bank (Computer Communication Networks)] · Hard*

**Q212.** What is the size (length) of a MAC address?
*MAC address का size (लंबाई) कितना होता है?*
- **(A)** 42 bits
- **(B)** 48 bits
- **(C)** 24 bits
- **(D)** 36 bits
✔ **(B) 48 bits**
★ **Nukta:** MAC = 48 bits (6 bytes / 12 hex digits). IPv4 = 32 bits, IPv6 = 128 bits, Port = 16 bits. Ye char sizes exam में बार-बार आते हैं।
*MAC = 48 bits (6 bytes / 12 hex digits)। IPv4 = 32 bits, IPv6 = 128 bits, Port = 16 bits। ये चार sizes exam में बार-बार आते हैं।*
*[Source: RPSC Programmer 2024 Paper-1 (official key) · also BCI_SCI ST-7 / Sanfoundry / InstrumentationTools] · Hard*

**Q213.** An Ethernet destination address 0A-01-12-03-04-05 is a:
*Ethernet destination address 0A-01-12-03-04-05 कौन-सा address है?*
- **(A)** Unicast address
- **(B)** Multicast address
- **(C)** Broadcast address
- **(D)** All of these
✔ **(A) Unicast address**
★ **Nukta:** I/G bit (last bit of first octet): 0 = unicast, 1 = multicast. All-ones (FF:FF...) = broadcast.
*I/G bit (पहले octet का अंतिम bit): 0 = unicast, 1 = multicast। All-ones (FF:FF...) = broadcast।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

**Q214.** Consider the statements: S1: Every computer or Internet device has a unique MAC address. S2: Every computer or Internet device has a unique IP address. Which is correct?
*कथन देखिए: S1: हर computer या Internet device का unique MAC address होता है। S2: हर computer या Internet device का unique IP address होता है। कौन-सा सही है?*
- **(A)** S1 is true and S2 is false
- **(B)** Both S1 and S2 are false
- **(C)** S1 is false and S2 is true
- **(D)** Both S1 and S2 are true
✔ **(A) S1 is true and S2 is false**
★ **Nukta:** MAC = permanent + globally unique. IP = logical + can repeat across private networks (NAT handles the overlap).
*MAC = स्थायी + globally unique। IP = logical + private networks में दोहराया जा सकता है (NAT overlap संभालता है)।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Hard*

**Q215.** Which header field is rewritten (not removed) when an IP packet passes through a router?
*जब एक IP packet router से गुजरता है तो कौन-सा header field बदला (rewrite) जाता है?*
- **(A)** Source IP address
- **(B)** Destination IP address
- **(C)** MAC (Media Access Control) address
- **(D)** Subnet mask
✔ **(C) MAC (Media Access Control) address**
★ **Nukta:** Per hop: MAC header changes. End-to-end: IP addresses stay the same. TTL also decrements (a router function).
*Per hop: MAC header बदलता है। End-to-end: IP addresses same रहते हैं। TTL भी घटता है (router का काम)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

## Section B — IPv4 Addressing (Format, Classes & Special Addresses)

*32-bit dotted-decimal, octets, classes A-E, default masks, loopback/APIPA/private/special addresses, NAT.*

**IPv4 address 32 bits ka hota hai jo dotted-decimal mein 4 numbers (octets) ke roop mein likha jaata hai — classes A se E tak, aur kuch special addresses har exam mein poochhe jaate hain.**

*IPv4 address 32 bits का होता है जो dotted-decimal में 4 numbers (octets) में लिखा जाता है — classes A से E तक, और कुछ special addresses।*

- 32 bits = 4 octets (har octet 8 bits, 0–255); dotted-decimal: jaise 192.168.1.1.
  - *32 bits = 4 octets (हर octet 8 bits, 0–255); dotted-decimal: जैसे 192.168.1.1।*
- Class A: first bit 0 (0–127), mask /8 — bahut bade networks; Class B: 10 (128–191), mask /16; Class C: 110 (192–223), mask /24.
  - *Class A: पहला bit 0 (0–127), mask /8; Class B: (128–191), /16; Class C: (192–223), /24।*
- Class D = multicast (224–239); Class E = reserved/research (240–255).
  - *Class D = multicast (224–239); Class E = reserved (240–255)।*
- Loopback = 127.x.x.x (127.0.0.1 = localhost); APIPA = 169.254.x.x (jab DHCP fail ho).
  - *Loopback = 127.x.x.x (127.0.0.1); APIPA = 169.254.x.x (DHCP fail hone पर)।*
- Private addresses (Internet par nahi chalte): 10.x.x.x, 172.16–31.x.x, 192.168.x.x — NAT se bahar jaate hain.
  - *Private addresses: 10.x, 172.16–31.x, 192.168.x — NAT से बाहर जाते हैं।*
- Special: 0.0.0.0 = default/unknown; 255.255.255.255 = limited broadcast; network ID aur host ID bits class se tay hote hain.
  - *Special: 0.0.0.0 = default; 255.255.255.255 = broadcast; network/host bits class से तय।*
- Classful addressing ka rule: network ID bits fixed (class se), host ID bits network ke andar hosts ko dete hain.
  - *Classful addressing: network ID bits class से fix, host ID bits hosts को।*

| Class | First bits | Range (1st octet) | Default mask | Networks |
|---|---|---|---|---|
| A | 0 | 0–127 | 255.0.0.0 (/8) | 2⁷ (0–127) |
| B | 10 | 128–191 | 255.255.0.0 (/16) | 2¹⁴ |
| C | 110 | 192–223 | 255.255.255.0 (/24) | 2²¹ |
| D | 1110 | 224–239 | — | multicast |
| E | 1111 | 240–255 | — | reserved |

### Questions (Easy → Medium → Hard)

**Q216.** The first octet of a Class A IP address ranges from:
*Class A IP address का पहला octet किस range में होता है?*
- **(A)** 0-127
- **(B)** 128-191
- **(C)** 192-223
- **(D)** 224-239
✔ **(A) 0-127**
★ **Nukta:** Class ranges by first octet: A 0-127, B 128-191, C 192-223, D 224-239 (multicast), E 240-255 (experimental).
*पहले octet से Class ranges: A 0-127, B 128-191, C 192-223, D 224-239 (multicast), E 240-255 (experimental)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q217.** Which class of IP address is used for multicasting?
*Multicasting के लिए किस class का IP address उपयोग होता है?*
- **(A)** Class A
- **(B)** Class B
- **(C)** Class C
- **(D)** Class D
✔ **(D) Class D**
★ **Nukta:** D = Multicast (one-to-group). E = Experimental (240-255). Broadcast (255.255.255.255) is separate.
*D = Multicast (one-to-group)। E = Experimental (240-255)। Broadcast (255.255.255.255) अलग है।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch) · also CN Topic Test-6] · Easy*

**Q218.** Which class of address is reserved for experimental purposes?
*प्रायोगिक (experimental) उद्देश्यों के लिए किस class का address reserved है?*
- **(A)** Class C
- **(B)** Class B
- **(C)** Class D
- **(D)** Class E
✔ **(D) Class E**
★ **Nukta:** Class E = Experimental (240-255). Remember: A-ny (0), B-128, C-192, D-224 (multicast), E-240 (experiment).
*Class E = Experimental (240-255)। याद रखें: A-ny (0), B-128, C-192, D-224 (multicast), E-240 (experiment)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q219.** The IP address 127.0.0.1 is used for:
*IP address 127.0.0.1 किस काम में आती है?*
- **(A)** Broadcast
- **(B)** Class D network
- **(C)** Loopback testing
- **(D)** APIPA
✔ **(C) Loopback testing**
★ **Nukta:** Whole 127.0.0.0/8 block = loopback. `ping 127.0.0.1` tests the local IP stack.
*पूरा 127.0.0.0/8 block = loopback। `ping 127.0.0.1` से local IP stack जाँचते हैं।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) · also CN Topic Test-03 / CN Topic Test-04] · Easy*

**Q220.** What is the maximum number of unique IPv4 addresses?
*Unique IPv4 addresses की अधिकतम संख्या कितनी है?*
- **(A)** 2^16
- **(B)** 2^24
- **(C)** 2^32
- **(D)** 2^64
✔ **(C) 2^32**
★ **Nukta:** 2^32 ≈ 4.29 billion IPv4 addresses. IPv6 = 2^128 ≈ 3.4 × 10^38.
*2^32 ≈ 4.29 billion IPv4 addresses। IPv6 = 2^128 ≈ 3.4 × 10^38।*
*[Source: IP Addressing quiz (Studocu bank, with keys)] · Medium*

**Q221.** An IPv4 address is divided into how many parts?
*IPv4 address कितने भागों में बाँटा जाता है?*
- **(A)** 2
- **(B)** 3
- **(C)** 4
- **(D)** 5
✔ **(A) 2**
★ **Nukta:** 2 parts = network + host. IPv4 CLASSIC division; subnetting borrows bits from host to make sub-networks.
*2 parts = network + host। Subnetting में host bits से bits उधार लेकर sub-networks बनते हैं।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

**Q222.** The first octet of a Class B IP address falls between:
*Class B IP address का पहला octet किस range में आता है?*
- **(A)** 0-127
- **(B)** 128-191
- **(C)** 192-223
- **(D)** 224-239
✔ **(B) 128-191**
★ **Nukta:** B = 128-191 (default /16). Trick: A starts 0, B starts 128, C starts 192, D starts 224, E starts 240.
*B = 128-191 (default /16)। Trick: A 0 से, B 128 से, C 192 से, D 224 से, E 240 से।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q223.** How many bits are used for the network portion in a Class C IP address?
*Class C IP address में network भाग के लिए कितने bits उपयोग होते हैं?*
- **(A)** 8
- **(B)** 16
- **(C)** 24
- **(D)** 32
✔ **(C) 24**
★ **Nukta:** Class C = /24 network (24 bits) + 8 host bits. Class B = /16, Class A = /8.
*Class C = /24 network (24 bits) + 8 host bits। Class B = /16, Class A = /8।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

**Q224.** Which IP address class provides the largest number of hosts per network?
*कौन-सी IP address class प्रति network सबसे अधिक hosts देती है?*
- **(A)** Class A
- **(B)** Class B
- **(C)** Class C
- **(D)** Class D
✔ **(A) Class A**
★ **Nukta:** Hosts per class: A = 2^24−2, B = 2^16−2 (65,534), C = 2^8−2 (254). D/E have no hosts (multicast/experimental).
*प्रति class hosts: A = 2^24−2, B = 2^16−2 (65,534), C = 2^8−2 (254)। D/E में hosts नहीं (multicast/experimental)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q225.** Which class of IP addresses supports 65,534 hosts per network?
*कौन-सी IP address class प्रति network 65,534 hosts support करती है?*
- **(A)** Class A
- **(B)** Class B
- **(C)** Class C
- **(D)** Class D
✔ **(B) Class B**
★ **Nukta:** 65,534 = 2^16−2 = Class B hosts. 254 = 2^8−2 = Class C. 16,777,214 = 2^24−2 = Class A.
*65,534 = 2^16−2 = Class B hosts। 254 = 2^8−2 = Class C। 16,777,214 = 2^24−2 = Class A।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q226.** What is the maximum number of IP addresses in a Class C network?
*Class C network में IP addresses की अधिकतम संख्या कितनी होती है?*
- **(A)** 254
- **(B)** 256
- **(C)** 1024
- **(D)** 65536
✔ **(B) 256**
★ **Nukta:** Total addresses = 2^host-bits. Usable hosts = total − 2. Exam asks BOTH — read 'addresses' vs 'hosts' carefully!
*कुल addresses = 2^host-bits। उपयोगी hosts = कुल − 2। Exam दोनों पूछता है — 'addresses' और 'hosts' में ध्यान से फर्क पढ़ें!*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

**Q227.** Which of the following is a Class D address?
*निम्न में से कौन-सा Class D address है?*
- **(A)** 224.1.1.1
- **(B)** 233.0.0.10
- **(C)** 239.5.5.5
- **(D)** All of the above
✔ **(D) All of the above**
★ **Nukta:** Class D = 224-239 (multicast). Any address in this range is Class D — exam often gives mixed octets like these.
*Class D = 224-239 (multicast)। इस range का कोई भी address Class D है — exam में अक्सर ऐसे मिश्रित octets दिए जाते हैं।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q228.** Which IP address is reserved for future use and experimental purposes?
*कौन-सा IP address भविष्य के उपयोग और प्रायोगिक उद्देश्यों के लिए reserved है?*
- **(A)** 127.0.0.1
- **(B)** 224.0.0.1
- **(C)** 240.0.0.0
- **(D)** 192.168.0.1
✔ **(C) 240.0.0.0**
★ **Nukta:** 240.0.0.0/4 = Class E = future use. 127.x = loopback, 224.x = multicast, 192.168.x = private.
*240.0.0.0/4 = Class E = future use। 127.x = loopback, 224.x = multicast, 192.168.x = private।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q229.** Which of the following is a Class B host address?
*निम्न में से कौन-सा Class B host address है?*
- **(A)** 230.0.0.0
- **(B)** 130.4.5.6
- **(C)** 230.7.6.5
- **(D)** 30.4.5.6
✔ **(B) 130.4.5.6**
★ **Nukta:** 230.x = Class D (multicast). 30.x = Class A. 130.x = Class B — look at the FIRST octet.
*230.x = Class D (multicast)। 30.x = Class A। 130.x = Class B — पहले octet को देखें।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q230.** Which of the following is a valid IPv4 address?
*निम्न में से कौन-सा वैध IPv4 address है?*
- **(A)** 192.256.1.1
- **(B)** 172.31.0.1
- **(C)** 300.100.50.25
- **(D)** 500.10.5.2
✔ **(B) 172.31.0.1**
★ **Nukta:** Octet range check: 0-255 only. 172.16-172.31.x is also the private Class B range (bonus!).
*Octet range check: केवल 0-255। 172.16-172.31.x private Class B range भी है (bonus!)।*
*[Source: 30 important CN MCQs (Medium blog bank)] · Medium*

**Q231.** The address 255.255.255.255 is used for:
*Address 255.255.255.255 किसके लिए उपयोग होती है?*
- **(A)** A public IP
- **(B)** A default gateway
- **(C)** A network ID
- **(D)** Broadcast to all nodes
✔ **(D) Broadcast to all nodes**
★ **Nukta:** Limited broadcast = 255.255.255.255 (this network only). Directed broadcast = last address of a subnet (e.g., 192.168.1.255).
*Limited broadcast = 255.255.255.255 (केवल यह network)। Directed broadcast = subnet का अंतिम address (जैसे 192.168.1.255)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q232.** What is the purpose of the reserved IP address 0.0.0.0?
*Reserved IP address 0.0.0.0 का उद्देश्य क्या है?*
- **(A)** Default gateway
- **(B)** Used for DHCP servers
- **(C)** Default route or 'any network'
- **(D)** Multicast address
✔ **(C) Default route or 'any network'**
★ **Nukta:** 0.0.0.0/0 = default route (gateway of last resort). As source = 'not yet assigned an IP'.
*0.0.0.0/0 = default route (gateway of last resort)। Source के रूप में = 'अभी IP नहीं मिला'।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q233.** The IP address used by a host's packets as the source while the host is being booted (before it gets an IP) is:
*जब host boot हो रहा होता है (IP मिलने से पहले) तो उसके packets का source IP address कौन-सा होता है?*
- **(A)** 0.0.0.0
- **(B)** 1.0.0.0
- **(C)** 1.1.1.1
- **(D)** 255.255.255.255
✔ **(A) 0.0.0.0**
★ **Nukta:** Boot/DHCP phase: source 0.0.0.0, destination 255.255.255.255 (broadcast). Ye DHCP handshake ka classic pattern hai.
*Boot/DHCP चरण: source 0.0.0.0, destination 255.255.255.255 (broadcast)। यह DHCP handshake का classic pattern है।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q234.** What is the range of addresses for APIPA (Automatic Private IP Addressing)?
*APIPA (Automatic Private IP Addressing) की address range क्या है?*
- **(A)** 169.254.0.1 to 169.254.255.254
- **(B)** 10.0.0.0 to 10.255.255.255
- **(C)** 192.168.0.0 to 192.168.255.255
- **(D)** 172.16.0.0 to 172.31.255.255
✔ **(A) 169.254.0.1 to 169.254.255.254**
★ **Nukta:** APIPA = 169.254.x.x (link-local, auto). Private blocks: 10.x / 172.16-31.x / 192.168.x (RFC 1918).
*APIPA = 169.254.x.x (link-local, auto)। Private blocks: 10.x / 172.16-31.x / 192.168.x (RFC 1918)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q235.** Which IP address can be used in a WAN (public network)?
*कौन-सा IP address WAN (public network) में उपयोग हो सकता है?*
- **(A)** 256.0.0.1
- **(B)** 172.16.0.10
- **(C)** 15.1.5.6
- **(D)** 127.256.0.118
✔ **(C) 15.1.5.6**
★ **Nukta:** WAN needs public IPs. Private ranges (10.x, 172.16-31.x, 192.168.x) + loopback + invalid octets — sab hatana seekho.
*WAN के लिए public IPs चाहिए। Private ranges (10.x, 172.16-31.x, 192.168.x) + loopback + invalid octets — सब हटाना सीखें।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q236.** Each computer connected to the internet must:
*Internet से जुड़े प्रत्येक computer को क्या होना चाहिए?*
- **(A)** Be an IBM PC
- **(B)** Have a unique IP address
- **(C)** Be internet compatible
- **(D)** Have a modem connection
✔ **(B) Have a unique IP address**
★ **Nukta:** Unique IP = the fundamental Internet requirement (IPv4 32-bit or IPv6 128-bit).
*Unique IP = Internet की मूल आवश्यकता (IPv4 32-bit या IPv6 128-bit)।*
*[Source: SSC CGL Internet & Networking (via EduRev bank)] · Medium*

**Q237.** Which organization is responsible for managing IP address allocation globally?
*वैश्विक स्तर पर IP address allocation का प्रबंधन कौन-सा संगठन करता है?*
- **(A)** IEEE
- **(B)** ICANN
- **(C)** IETF
- **(D)** ISO
✔ **(B) ICANN**
★ **Nukta:** ICANN/IANA = addresses + names. IETF = protocols (RFCs). IEEE = LAN standards (802.x). ISO = OSI model.
*ICANN/IANA = addresses + names। IETF = protocols (RFCs)। IEEE = LAN standards (802.x)। ISO = OSI model।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q238.** What is the size of each octet in an IPv4 address?
*IPv4 address के प्रत्येक octet का size कितना होता है?*
- **(A)** 4 bits
- **(B)** 8 bits
- **(C)** 16 bits
- **(D)** 32 bits
✔ **(B) 8 bits**
★ **Nukta:** Octet = 8 bits (0-255 in decimal). 4 octets = 32 bits = dotted-decimal notation.
*Octet = 8 bits (decimal में 0-255)। 4 octets = 32 bits = dotted-decimal notation।*
*[Source: IP Addressing quiz (Studocu bank, with keys)] · Hard*

**Q239.** An IPv4 address is of size:
*IPv4 address कितने bits का होता है?*
- **(A)** 8 bit
- **(B)** 16 bit
- **(C)** 32 bit
- **(D)** 64 bit
✔ **(C) 32 bit**
★ **Nukta:** Size shortcut: MAC 48, IPv4 32, IPv6 128, Port 16 (bits).
*Size shortcut: MAC 48, IPv4 32, IPv6 128, Port 16 (bits)।*
*[Source: Networking MCQ bank (MQuestions blog)] · Hard*

**Q240.** If the number of networks and number of hosts in Class B are 2^m and (2^n − 2) respectively, then the relation between m and n is:
*यदि Class B में networks और hosts की संख्या क्रमशः 2^m और (2^n − 2) है, तो m और n के बीच क्या संबंध है?*
- **(A)** 3m = 2n
- **(B)** 7m = 8n
- **(C)** 8m = 7n
- **(D)** 2m = 3n
✔ **(C) 8m = 7n**
★ **Nukta:** Class B classful counts: networks 2^14, hosts 2^16−2. So m=14, n=16 → 8m=7n. (Class A: 2^7 nets, 2^24−2 hosts; Class C: 2^21 nets, 2^8−2 hosts.)
*Class B classful counts: networks 2^14, hosts 2^16−2। अतः m=14, n=16 → 8m=7n। (Class A: 2^7 nets, 2^24−2 hosts; Class C: 2^21 nets, 2^8−2 hosts।)*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q241.** Which subnet mask is the default for the Class B IP address range?
*Class B IP address range के लिए default subnet mask कौन-सा है?*
- **(A)** 255.255.255.0
- **(B)** 255.0.0.0
- **(C)** 255.255.0.0
- **(D)** 255.255.255.255
✔ **(C) 255.255.0.0**
★ **Nukta:** Default masks: A 255.0.0.0 (/8), B 255.255.0.0 (/16), C 255.255.255.0 (/24).
*Default masks: A 255.0.0.0 (/8), B 255.255.0.0 (/16), C 255.255.255.0 (/24)।*
*[Source: 30 important CN MCQs (Medium blog bank) · also CN Topic Test-6] · Hard*

**Q242.** What is the primary purpose of NAT (Network Address Translation) in IPv4?
*IPv4 में NAT (Network Address Translation) का मुख्य उद्देश्य क्या है?*
- **(A)** To map private IP addresses to a public IP address
- **(B)** To increase the security of IP addresses
- **(C)** To facilitate communication between different subnets
- **(D)** All of the above
✔ **(A) To map private IP addresses to a public IP address**
★ **Nukta:** NAT core = private→public mapping. Bonus effects: hides internal IPs (security), helps address exhaustion. Some banks key 'All of these' — the PRIMARY purpose is the mapping.
*NAT का core = private→public mapping। अतिरिक्त प्रभाव: internal IPs छिपती हैं (security), address exhaustion कम होती है। कुछ banks 'All of these' key करते हैं — मुख्य उद्देश्य mapping ही है।*
*[Source: IP Addressing quiz (Studocu bank, with keys)] · Hard*

**Q243.** A host is connected to a department network which is part of a university network; the university network in turn is part of the Internet. Which is the LARGEST network among these?
*एक host department network से जुड़ा है जो university network का हिस्सा है; university network बदले में Internet का हिस्सा है। इनमें सबसे बड़ा network कौन-सा है?*
- **(A)** The subnet to which the host belongs
- **(B)** The department network
- **(C)** The university network
- **(D)** The Internet
✔ **(D) The Internet**
★ **Nukta:** Hierarchy: subnet ⊂ department LAN ⊂ university CAN ⊂ Internet. Addressing mirrors this (network prefix lengths).
*पदानुक्रम: subnet ⊂ department LAN ⊂ university CAN ⊂ Internet। Addressing भी इसी तरह (network prefix lengths)।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Hard*

**Q244.** Which IP address type is used to communicate with all devices on a subnet?
*Subnet के सभी devices से संवाद करने के लिए किस type का IP address उपयोग होता है?*
- **(A)** Unicast
- **(B)** Broadcast
- **(C)** Multicast
- **(D)** Anycast
✔ **(B) Broadcast**
★ **Nukta:** IP communication types: Unicast (one-to-one), Broadcast (one-to-all-on-subnet), Multicast (one-to-group), Anycast (one-to-nearest).
*IP communication types: Unicast (one-to-one), Broadcast (one-to-all-on-subnet), Multicast (one-to-group), Anycast (one-to-nearest)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q245.** Which of the following is NOT a valid private (RFC-1918) IP address?
*निम्न में से कौन-सा वैध private (RFC-1918) IP पता नहीं है?*
- **(A)** 10.0.0.1
- **(B)** 172.16.5.4
- **(C)** 192.168.1.10
- **(D)** 11.0.0.1
✔ **(D) 11.0.0.1**
★ **Nukta:** Private ranges याद रखो: 10.x (Class A), 172.16–172.31.x (Class B), 192.168.x (Class C) — बाकी सब public.
*Private ranges याद रखो: 10.x (Class A), 172.16–172.31.x (Class B), 192.168.x (Class C) — बाकी सब public.*
*[Source: CN Topic Test 5.pdf] · Hard*

**Q246.** In the IPv4 addressing format, the number of networks allowed under Class C addresses is:
*IPv4 addressing में Class C addresses के अंतर्गत कुल कितने networks allowed हैं?*
- **(A)** 2¹⁴
- **(B)** 2⁷
- **(C)** 2²¹
- **(D)** 2²⁴
✔ **(C) 2²¹**
★ **Nukta:** 2²⁴ poore network field ka size hai (fixed 3 bits bhool kar); 2⁷ aur 2¹⁴ host/other class ke figures hain.
*2²⁴ poora field (3 fixed bits bhool kar); 2⁷/2¹⁴ doosre figures hain.*
*[Source: GATE CS 2012] · Hard*

**Q247.** Which one of the following CIDR prefixes exactly represents the range of IP addresses 10.12.2.0 to 10.12.3.255?
*CIDR prefix में से कौन-सा 10.12.2.0 से 10.12.3.255 तक की IP range को ठीक-ठीक दर्शाता है?*
- **(A)** 10.12.2.0/24
- **(B)** 10.12.2.0/23
- **(C)** 10.12.0.0/22
- **(D)** 10.12.3.0/25
✔ **(B) 10.12.2.0/23**
★ **Nukta:** /24 sirf 2.0–2.255 cover karta hai; /22 bahut bada (4 blocks); /25 aadha block.
*/24 sirf 2.x; /22 bahut bada; /25 aadha block.*
*[Source: GATE CS 2024 Set-2] · Hard*

**Q248.** Three machines M, N and P have IP addresses 100.10.5.2, 100.10.5.5 and 100.10.5.6 respectively. The subnet mask is set to 255.255.255.252 for all three machines. Which one of the following is true?
*तीन machines M, N, P के IP addresses क्रमशः 100.10.5.2, 100.10.5.5 और 100.10.5.6 हैं। तीनों का subnet mask 255.255.255.252 है। निम्न में से कौन-सा कथन सही है?*
- **(A)** All three belong to the same subnet / तीनों एक ही subnet में हैं
- **(B)** M and N belong to the same subnet / M और N एक ही subnet में हैं
- **(C)** N and P belong to the same subnet / N और P एक ही subnet में हैं
- **(D)** M and P belong to the same subnet / M और P एक ही subnet में हैं
✔ **(C) N and P belong to the same subnet**
★ **Nukta:** Adjacent numbers ka matlab same subnet nahi — /30 par block boundary .3/.4 par hoti hai.
*पास के numbers = एक subnet नहीं; /30 में boundary .3/.4 पर है।*
*[Source: GATE CS 2019] · Hard*

## Section C — Subnetting & CIDR

*Subnet masks, /n notation, usable hosts & subnet counts, block arithmetic — basic to advanced calculations.*

**Subnetting se ek network ko chhote hisson mein baante hain; CIDR se addresses ko class se azaad kar aggregate karte hain. Yeh numericals ka favourite area hai.**

*Subnetting से एक network को छोटे हिस्सों में बाँटते हैं; CIDR से addresses class से मुक्त कर aggregate करते हैं।*

- Subnet mask batata hai ki address mein kitne bits network (aur subnet) ke hain aur kitne host ke — 1 = network, 0 = host.
  - *Subnet mask बताता है कि कितने bits network के हैं और कितने host के — 1 = network, 0 = host।*
- /n notation: mask ke pehle n bits 1 hote hain (jaise /24 = 255.255.255.0).
  - */n notation: mask के पहले n bits 1 होते हैं (जैसे /24)।*
- Subnetting: host bits mein se borrow kar subnet banate hain; usable hosts = 2ʰ − 2 (network aur broadcast chhod kar).
  - *Subnetting: host bits में से borrow कर subnet बनाते हैं; usable hosts = 2ʰ − 2।*
- Subnets ki sankhya = 2ˢ (s = borrowed bits); CIDR mein 'subnet zero' allowed hone par 2ˢ hi rehta hai.
  - *Subnets की संख्या = 2ˢ; CIDR में 'subnet zero' allowed होने पर 2ˢ।*
- CIDR (Classless Inter-Domain Routing) — /n prefix se address blocks; route aggregation (summarization) se routing table chhoti hoti hai.
  - *CIDR — /n prefix से address blocks; route aggregation से routing table छोटी।*
- VLSM (Variable Length Subnet Mask) — alag-alag subnets ko alag size dene ke liye mask badalna.
  - *VLSM — अलग-अलग subnets को अलग size के लिए mask बदलना।*
- NAT — private IPs ko public IP mein badalna (static, dynamic, overload/PAT); ek public IP se bahut sare hosts chalte hain.
  - *NAT — private IPs को public IP में बदलना (static, dynamic, overload)।*
- Numerical tip: network address = IP AND mask; broadcast = network + sab host bits 1; first host = network+1, last host = broadcast−1.
  - *Numerical tip: network = IP AND mask; broadcast = network + सब host bits 1; first host = network+1।*

| Mask | /n | Host bits (h) | Usable hosts (2ʰ−2) |
|---|---|---|---|
| 255.255.255.0 | /24 | 8 | 254 |
| 255.255.255.128 | /25 | 7 | 126 |
| 255.255.255.192 | /26 | 6 | 62 |
| 255.255.255.224 | /27 | 5 | 30 |
| 255.255.255.252 | /30 | 2 | 2 |

### Questions (Easy → Medium → Hard)

**Q249.** A subnet /30 is MOST commonly used for:
*Subnet /30 सबसे अधिक किसके लिए उपयोग होती है?*
- **(A)** Two-host networks
- **(B)** Four-host networks
- **(C)** Loopback only
- **(D)** VPN networks
✔ **(A) Two-host networks**
★ **Nukta:** Link between 2 routers = /30. WAN links ya tunnel endpoints ke liye standard.
*2 routers के बीच link = /30। WAN links या tunnel endpoints के लिए standard।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q250.** Which part of the IP address 172.16.5.4/24 identifies the network?
*IP address 172.16.5.4/24 का कौन-सा भाग network पहचानता है?*
- **(A)** 172
- **(B)** 172.16
- **(C)** 172.16.5
- **(D)** 172.16.5.4
✔ **(C) 172.16.5**
★ **Nukta:** Visual trick: /8 → 1 octet, /16 → 2 octets, /24 → 3 octets network.
*Visual trick: /8 → 1 octet, /16 → 2 octets, /24 → 3 octets network।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q251.** A network ID (address with all host bits = 0) cannot be assigned to:
*Network ID (सभी host bits = 0 वाला address) किसे assign नहीं किया जा सकता?*
- **(A)** A router
- **(B)** A switch
- **(C)** A host device
- **(D)** The entire network
✔ **(C) A host device**
★ **Nukta:** Network ID = first address of the block (host bits 0). Broadcast = last (host bits 1). Both reserved; usable hosts = middle addresses only.
*Network ID = block का पहला address (host bits 0)। Broadcast = अंतिम (host bits 1)। दोनों reserved; उपयोगी hosts = बीच के addresses ही।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q252.** A host has IP 192.168.10.45/27. Which statement is TRUE?
*एक host का IP 192.168.10.45/27 है। कौन-सा कथन सही है?*
- **(A)** Broadcast address = 192.168.10.63
- **(B)** Network ID = 192.168.10.32
- **(C)** First usable host = 192.168.10.33
- **(D)** All of the above
✔ **(D) All of the above**
★ **Nukta:** Block arithmetic: 45 ÷ 32 → block 32. Network = block start; broadcast = next block − 1.
*Block arithmetic: 45 ÷ 32 → block 32। Network = block की शुरुआत; broadcast = अगला block − 1।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) · also CN Topic Test-03] · Medium*

**Q253.** What does the term 'subnetting' refer to in networking?
*Networking में 'subnetting' शब्द का क्या अर्थ है?*
- **(A)** Dividing a large network into smaller logical networks
- **(B)** Allocating IP addresses to devices
- **(C)** Filtering network traffic
- **(D)** Assigning MAC addresses
✔ **(A) Dividing a large network into smaller logical networks**
★ **Nukta:** Subnetting = big network → smaller networks (better performance, security, less broadcast).
*Subnetting = बड़ा network → छोटे networks (बेहतर performance, security, कम broadcast)।*
*[Source: 30 important CN MCQs (Medium blog bank) · also CN Topic Test-03] · Hard*

**Q254.** When IPv4 addressing is manually configured, which property identifies the network and host portions of the address?
*जब IPv4 addressing manually configure होती है, तो कौन-सा property address के network और host भाग पहचानती है?*
- **(A)** DNS server address
- **(B)** Subnet mask
- **(C)** Default gateway
- **(D)** DHCP server address
✔ **(B) Subnet mask**
★ **Nukta:** Mask = boundary between network and host. /24 = 255.255.255.0 = 24 network bits + 8 host bits.
*Mask = network और host के बीच सीमा। /24 = 255.255.255.0 = 24 network bits + 8 host bits।*
*[Source: IP Addressing quiz (Studocu bank, with keys)] · Hard*

**Q255.** In a subnet mask, the number of 1's represents:
*Subnet mask में 1's की संख्या किसका प्रतिनिधित्व करती है?*
- **(A)** Host bits
- **(B)** Network bits
- **(C)** Broadcast bits
- **(D)** Subnet bits
✔ **(B) Network bits**
★ **Nukta:** Count of 1s = prefix length (/n). Example: 255.255.255.0 has 24 ones = /24.
*1s की गिनती = prefix length (/n)। उदाहरण: 255.255.255.0 में 24 ones = /24।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q256.** In CIDR notation, what does /16 represent?
*CIDR notation में /16 का क्या अर्थ है?*
- **(A)** 16 host bits
- **(B)** 16 network bits
- **(C)** 16 bytes
- **(D)** 16 subnets
✔ **(B) 16 network bits**
★ **Nukta:** CIDR /n = n network bits. Host bits = 32 − n. /16 → 2^16 − 2 hosts.
*CIDR /n = n network bits। Host bits = 32 − n। /16 → 2^16 − 2 hosts।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q257.** What does /24 denote in CIDR?
*CIDR में /24 किसे दर्शाता है?*
- **(A)** 24 bits are used for the host portion
- **(B)** 24 bits are used for the network portion
- **(C)** 24 subnets are created
- **(D)** 24 addresses are available in the subnet
✔ **(B) 24 bits are used for the network portion**
★ **Nukta:** Official RPSC 2024 key: /24 = 24 network bits. Same idea: /27 = 27 network bits, /30 = 30.
*Official RPSC 2024 key: /24 = 24 network bits। वैसे ही: /27 = 27 network bits, /30 = 30।*
*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

**Q258.** How many USABLE hosts are there in a /24 subnet?
*/24 subnet में कितने उपयोगी (usable) hosts होते हैं?*
- **(A)** 128
- **(B)** 256
- **(C)** 254
- **(D)** 512
✔ **(C) 254**
★ **Nukta:** Formula: usable hosts = 2^host_bits − 2. /24 → 254, /25 → 126, /26 → 62, /27 → 30, /28 → 14, /29 → 6, /30 → 2.
*सूत्र: उपयोगी hosts = 2^host_bits − 2। /24 → 254, /25 → 126, /26 → 62, /27 → 30, /28 → 14, /29 → 6, /30 → 2।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5) · also CN Topic Test-03] · Hard*

**Q259.** How many usable hosts are there in a /30 subnet?
*/30 subnet में कितने उपयोगी hosts होते हैं?*
- **(A)** 2
- **(B)** 4
- **(C)** 6
- **(D)** 14
✔ **(A) 2**
★ **Nukta:** /30 = 2 hosts (router-to-router links). /29 = 6 hosts (small office).
*/30 = 2 hosts (router-to-router links)। /29 = 6 hosts (छोटा office)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q260.** A subnet mask of 255.255.255.248 allows how many usable hosts?
*Subnet mask 255.255.255.248 कितने उपयोगी hosts की अनुमति देता है?*
- **(A)** 2
- **(B)** 6
- **(C)** 14
- **(D)** 30
✔ **(B) 6**
★ **Nukta:** .248 = /29 = 6 hosts. Remember the /30-/29-/28 ladder: 2, 6, 14.
*.248 = /29 = 6 hosts। /30-/29-/28 ladder याद रखें: 2, 6, 14।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Hard*

**Q261.** The subnet mask 255.255.255.128 provides how many subnets for a Class C network?
*Subnet mask 255.255.255.128, Class C network के लिए कितने subnets देता है?*
- **(A)** 1
- **(B)** 2
- **(C)** 4
- **(D)** 8
✔ **(B) 2**
★ **Nukta:** Borrowed bits n → 2^n subnets. .128 = 1 bit borrowed → 2 subnets.
*उधार bits n → 2^n subnets। .128 = 1 bit उधार → 2 subnets।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q262.** A network needs 5 subnets, each with at least 16 hosts. Which subnet mask (Class C) should be used?
*एक network को 5 subnets चाहिए, हर एक में कम से कम 16 hosts। कौन-सा subnet mask (Class C) उपयोग करें?*
- **(A)** 255.255.255.192
- **(B)** 255.255.255.248
- **(C)** 255.255.255.240
- **(D)** 255.255.255.224
✔ **(D) 255.255.255.224**
★ **Nukta:** Subnetting trade-off: more subnets → fewer hosts each. Borrow just enough bits (3 here).
*Subnetting trade-off: ज़्यादा subnets → हर एक में कम hosts। बस पर्याप्त bits उधार लें (यहाँ 3)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q263.** A subnet mask for Class C can have how many 1's by default (remaining bits 0)?
*Class C के लिए subnet mask में डिफ़ॉल्ट रूप से कितने 1's हो सकते हैं (बाकी bits 0)?*
- **(A)** 10
- **(B)** 24
- **(C)** 12
- **(D)** 7
✔ **(B) 24**
★ **Nukta:** Class C default = /24 = 24 ones. (With subnetting it can go up to /30 practically.)
*Class C default = /24 = 24 ones। (Subnetting के साथ यह व्यावहारिक रूप से /30 तक जा सकता है।)*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q264.** What is the valid host range for the subnet 192.168.1.0/25?
*Subnet 192.168.1.0/25 के लिए वैध host range क्या है?*
- **(A)** 192.168.1.0 - 192.168.1.255
- **(B)** 192.168.1.1 - 192.168.1.126
- **(C)** 192.168.1.1 - 192.168.1.254
- **(D)** 192.168.1.0 - 192.168.1.127
✔ **(B) 192.168.1.1 - 192.168.1.126**
★ **Nukta:** Host range = network+1 to broadcast−1. For /25: .1-.126 (first subnet) and .129-.254 (second).
*Host range = network+1 से broadcast−1। /25 के लिए: .1-.126 (पहला subnet) और .129-.254 (दूसरा)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q265.** In subnetting, reducing the number of host bits does what?
*Subnetting में host bits की संख्या घटाने से क्या होता है?*
- **(A)** Increases the broadcast domain
- **(B)** Decreases the number of subnets
- **(C)** Increases the number of subnets
- **(D)** Increases the number of hosts
✔ **(C) Increases the number of subnets**
★ **Nukta:** More subnet bits ⇔ more subnets ⇔ fewer hosts each. Ye subnetting ka basic trade-off hai.
*ज़्यादा subnet bits ⇔ ज़्यादा subnets ⇔ हर एक में कम hosts। यह subnetting का मूल trade-off है।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Hard*

**Q266.** In a class B subnet: IP address 125.134.112.66, mask 255.255.224.0. What is the first address (network address)?
*Class B subnet में: IP address 125.134.112.66, mask 255.255.224.0। पहला address (network address) क्या होगा?*
- **(A)** 125.134.96.0
- **(B)** 125.134.112.0
- **(C)** 125.134.112.66
- **(D)** 125.134.0.0
✔ **(A) 125.134.96.0**
★ **Nukta:** Block size = 256 − last non-255 octet (256−224 = 32). Floor(112/32)×32 = 96.
*Block size = 256 − अंतिम गैर-255 octet (256−224 = 32)। Floor(112/32)×32 = 96।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q267.** A Class B network is to be split into subnets with a 3-bit subnet number. What is the maximum number of subnets and hosts in each subnet?
*एक Class B network को 3-bit subnet number में बाँटना है। प्रत्येक subnet में subnets और hosts की अधिकतम संख्या कितनी होगी?*
- **(A)** 8 subnets and 262141 hosts
- **(B)** 6 subnets and 262141 hosts
- **(C)** 6 subnets and 1022 hosts
- **(D)** None of the above
✔ **(D) None of the above**
★ **Nukta:** Class B /16 + 3 subnet bits = /19: 8 subnets × 8190 hosts each. Since options are unusual, the correct choice is 'None of the above'.
*Class B /16 + 3 subnet bits = /19: 8 subnets × 8190 hosts। विकल्प असामान्य हैं इसलिए सही विकल्प 'None of the above' है।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q268.** IP address 172.16.123.213 has subnet mask 255.255.255.240. What is its network (first) address?
*IP address 172.16.123.213 का subnet mask 255.255.255.240 है। इसका network (पहला) address क्या है?*
- **(A)** 172.16.123.240
- **(B)** 172.16.123.208
- **(C)** 172.16.123.213
- **(D)** 172.16.123.245
✔ **(B) 172.16.123.208**
★ **Nukta:** /28 = 16-address blocks: .208-.223 here. Network = .208, broadcast = .223, hosts = .209-.222 (14 hosts).
*/28 = 16-address blocks: यहाँ .208-.223। Network = .208, broadcast = .223, hosts = .209-.222 (14 hosts)।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

**Q269.** An organization has a Class B network and wishes to form subnets for 64 departments. The subnet mask would be:
*एक संगठन के पास Class B network है और वह 64 departments के लिए subnets बनाना चाहता है। Subnet mask क्या होगा?*
- **(A)** 255.255.128.0
- **(B)** 255.255.0.0
- **(C)** 255.255.64.0
- **(D)** 255.255.252.0
✔ **(D) 255.255.252.0**
★ **Nukta:** Borrow 6 bits: 16+6 = 22 network bits = 255.255.252.0. RPSC 2024 official key.
*6 bits उधार: 16+6 = 22 network bits = 255.255.252.0। RPSC 2024 official key।*
*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

**Q270.** A Class B network has a subnet mask of 255.255.248.0. What is the maximum number of hosts per subnet?
*एक Class B network का subnet mask 255.255.248.0 है। प्रति subnet hosts की अधिकतम संख्या कितनी है?*
- **(A)** 2046
- **(B)** 1022
- **(C)** 1023
- **(D)** 1024
✔ **(A) 2046**
★ **Nukta:** Official key (RPSC 2024 + Rajasthan PYQ): 2046 hosts. /21 → 2^11−2 = 2046.
*Official key (RPSC 2024 + Rajasthan PYQ): 2046 hosts। /21 → 2^11−2 = 2046।*
*[Source: RPSC Programmer 2024 Paper-1 (official key) · Rajasthan PYQ Q56] · Hard*

**Q271.** An IP address 156.233.42.56 is configured with a 7-bit subnet mask (7 bits borrowed from the host part of the classful network). How many hosts and subnets are possible?
*IP address 156.233.42.56 को 7-bit subnet mask (classful network के host भाग से 7 bits उधार) के साथ configure किया गया है। कितने hosts और subnets संभव हैं?*
- **(A)** 126 hosts, 510 subnets
- **(B)** 128 hosts, 512 subnets
- **(C)** 510 hosts, 126 subnets
- **(D)** 512 hosts, 128 subnets
✔ **(A) 126 hosts, 510 subnets**
★ **Nukta:** Bank key pattern: 7 host bits → 126 hosts; 9 subnet bits → 510 usable subnets (both −2).
*Bank key pattern: 7 host bits → 126 hosts; 9 subnet bits → 510 उपयोगी subnets (दोनों −2)।*
*[Source: Unit Test -2 Solutions (OCR), p5] · Hard*

**Q272.** If a Class B network on the internet has a subnet mask of 255.255.248.0, what is the maximum number of hosts per subnet?
*यदि internet पर किसी Class B network की subnet mask 255.255.248.0 हो, तो हर subnet में अधिकतम hosts कितने होंगे?*
- **(A)** 1023
- **(B)** 1022
- **(C)** 1024
- **(D)** 2046
✔ **(D) 2046**
★ **Nukta:** 248 = 11111000 → तीसरे octet में 5 subnet bits. हमेशा 2^hostbits − 2 (network और broadcast हटाकर).
*248 = 11111000 → तीसरे octet में 5 subnet bits. हमेशा 2^hostbits − 2 (network और broadcast हटाकर).*
*[Source: RPSC Programmer 2024 Paper-1 (via Suraku Academy official-key solutions)] · Hard*

**Q273.** The address of a Class B host is to be split into subnets with a 6-bit subnet number. What is the maximum number of subnets and the maximum number of hosts in each subnet?
*Class B host के पते को 6-bit subnet number से subnets में बाँटना है. अधिकतम subnets और हर subnet में अधिकतम hosts कितने होंगे?*
- **(A)** 62 subnets and 262142 hosts
- **(B)** 64 subnets and 262142 hosts
- **(C)** 62 subnets and 1022 hosts
- **(D)** 64 subnets and 1024 hosts
✔ **(C) 62 subnets and 1022 hosts**
★ **Nukta:** RPSC 2011 और GATE 2005 दोनों में यही प्रश्न — official key (C) 62 subnets, 1022 hosts.
*RPSC 2011 और GATE 2005 दोनों में यही प्रश्न — official key (C) 62 subnets, 1022 hosts.*
*[Source: RPSC Programmer 2011 Paper-1 (via pyqp.in) + GATE CS 2005] · Hard*

**Q274.** Suppose that in an IP-over-Ethernet network, a machine X wishes to find the MAC address of another machine Y in its subnet. Which one of the following techniques can be used for this?
*IP-over-Ethernet network में machine X को अपने ही subnet की machine Y का MAC address जानना है। इसके लिए निम्न में से कौन-सी technique प्रयोग होगी?*
- **(A)** ARP request broadcast
- **(B)** RARP request broadcast
- **(C)** DNS query
- **(D)** ICMP query
✔ **(A) ARP request broadcast**
★ **Nukta:** RARP ulta (MAC→IP) hai; DNS naam→IP; ICMP error/control — koi bhi MAC nahi deta.
*RARP उल्टा (MAC→IP); DNS नाम→IP; ICMP error — MAC कोई नहीं देता।*
*[Source: GATE CS 2019] · Hard*

**Q275.** Node X has a TCP connection open to node Y. Packets from X to Y go through an intermediate IP router R; Ethernet switch S is the first switch on the path. For a packet sent from X, which of the following is TRUE about its destination IP and MAC addresses at the time it leaves X?
*Node X की node Y से TCP connection है; packets router R से होकर जाते हैं और पहला Ethernet switch S है। X से निकलते packet के destination IP और MAC addresses के बारे में क्या सही है?*
- **(A)** Destination IP = Y's IP; destination MAC = R's MAC / Destination IP = Y का IP; destination MAC = R का MAC
- **(B)** Destination IP = R's IP; destination MAC = R's MAC / Destination IP = R का IP; destination MAC = R का MAC
- **(C)** Destination IP = Y's IP; destination MAC = Y's MAC / Destination IP = Y का IP; destination MAC = Y का MAC
- **(D)** Destination IP = R's IP; destination MAC = S's MAC / Destination IP = R का IP; destination MAC = S का MAC
✔ **(A) Destination IP = Y's IP; destination MAC = R's MAC**
★ **Nukta:** IP ko hop-by-hop badalna common galti hai; switch MAC forwarding karta hai par packet ka destination MAC router ka hi rehta hai.
*IP को hop-by-hop बदलना आम गलती; packet का destination MAC router का ही रहता है।*
*[Source: GATE CS 2025 Set-2] · Hard*

## Section D — IPv6 Addressing

*128-bit addresses, address types (no broadcast), IPv6-only header changes, transition (tunneling), AAAA records.*

**IPv6 addresses IPv4 ki khatam hote addresses ka solution hai — 128 bits, hexadecimal colon notation, aur kuch naye rules.**

*IPv6, IPv4 के समाप्त होते addresses का समाधान है — 128 bits, hexadecimal colon notation, और कुछ नए नियम।*

- IPv6 = 128 bits = 16 bytes; hexadecimal ke 8 groups (har group 4 hex digits), colon se alag: 2001:0db8::1.
  - *IPv6 = 128 bits = 16 bytes; 8 hex groups, colon से अलग: 2001:0db8::1।*
- Broadcast NAHI hota IPv6 mein — multicast, unicast aur anycast use hote hain.
  - *IPv6 में Broadcast नहीं होता — multicast, unicast, anycast।*
- IPv6 header fixed 40 bytes ka, simplified — checksum header nahi (error handling neeche/upper layers karte hain).
  - *IPv6 header 40 bytes, सरल — checksum नहीं।*
- Address types: global unicast, link-local (fe80::), loopback (::1), unspecified (::), multicast.
  - *Address types: global unicast, link-local (fe80::), loopback (::1), multicast।*
- Transition techniques: Dual stack (dono IP), Tunneling (IPv6 ko IPv4 mein), Translation (NAT-PT).
  - *Transition: Dual stack, Tunneling, Translation।*
- SLAAC (Stateless Address Autoconfiguration) — host khud address bana sakta hai (router advertisement se).
  - *SLAAC — host खुद address बना सकता है।*
- IPv4 = 32-bit dotted-decimal; IPv6 = 128-bit hex — yehi fark exam ka classic sawaal hai.
  - *IPv4 = 32-bit dotted-decimal; IPv6 = 128-bit hex।*

| Fakt (Feature) | IPv4 | IPv6 |
|---|---|---|
| Size | 32 bits | 128 bits |
| Notation | dotted-decimal | hex colon |
| Broadcast | haan | nahi (multicast/anycast) |
| Header | variable (20–60 B) | fixed 40 B |
| Checksum | header mein | nahi |

### Questions (Easy → Medium → Hard)

**Q276.** Which IPv6 address type is globally unique and globally routable?
*कौन-सा IPv6 address type globally unique और globally routable होता है?*
- **(A)** Link-Local
- **(B)** Multicast
- **(C)** Unique Local
- **(D)** Global Unicast
✔ **(D) Global Unicast**
★ **Nukta:** IPv6 unicast scopes: Link-Local (fe80::/10) = this link only; Unique-Local (fc00::/7) = like private; Global (2000::/3) = Internet.
*IPv6 unicast scopes: Link-Local (fe80::/10) = केवल यह link; Unique-Local (fc00::/7) = private जैसा; Global (2000::/3) = Internet।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

**Q277.** IPv6 was developed by:
*IPv6 किसने develop किया?*
- **(A)** IETF
- **(B)** ANSI
- **(C)** ISO
- **(D)** IEEE
✔ **(A) IETF**
★ **Nukta:** IPv4/IPv6 = IETF (RFCs). OSI = ISO. LAN standards = IEEE (802). ANSI = US standards body.
*IPv4/IPv6 = IETF (RFCs)। OSI = ISO। LAN standards = IEEE (802)। ANSI = US standards body।*
*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

**Q278.** Two IPv6 nodes must interoperate but are connected through intervening IPv4 routers. The best solution is:
*दो IPv6 nodes को interoperable होना है लेकिन वे बीच में आने वाले IPv4 routers से जुड़े हैं। सबसे अच्छा समाधान क्या है?*
- **(A)** Use the dual-stack approach
- **(B)** Tunneling
- **(C)** No solution
- **(D)** Replace the system
✔ **(B) Tunneling**
★ **Nukta:** Transition mechanisms: Tunneling (IPv6 over IPv4), Dual-stack (both), Translation (NAT64).
*Transition mechanisms: Tunneling (IPv6 over IPv4), Dual-stack (दोनों), Translation (NAT64)।*
*[Source: Sanfoundry CN MCQs — IPv6] · Medium*

**Q279.** Which DNS resource record should be queried to retrieve the IPv6 address associated with a name?
*किसी name से जुड़ा IPv6 address पाने के लिए कौन-सी DNS resource record query करनी चाहिए?*
- **(A)** The AAAA record
- **(B)** The A record
- **(C)** The NS record
- **(D)** The MX record
✔ **(A) The AAAA record**
★ **Nukta:** DNS records: A = name→IPv4, AAAA = name→IPv6, PTR = IP→name, MX = mail, NS = name server.
*DNS records: A = name→IPv4, AAAA = name→IPv6, PTR = IP→name, MX = mail, NS = name server।*
*[Source: cnp3 MCQ (Bonaventure CN textbook), DNS1] · Medium*

**Q280.** IPv6 addresses are ______ bit addresses.
*IPv6 addresses ______ bit के पते होते हैं.*
- **(A)** 32
- **(B)** 64
- **(C)** 16
- **(D)** 128
✔ **(D) 128**
★ **Nukta:** IPv4 = 32-bit (4 numbers); IPv6 = 128-bit (8 groups).
*IPv4 = 32-bit (4 numbers); IPv6 = 128-bit (8 groups).*
*[Source: SBI/IBPS Computer Awareness Capsule 2018 (IBT India)] · Medium*

**Q281.** In IPv6, how many bits are in the address?
*IPv6 में address कितने bits का होता है?*
- **(A)** 32
- **(B)** 64
- **(C)** 128
- **(D)** 256
✔ **(C) 128**
★ **Nukta:** Size line: IPv4 32, IPv6 128, MAC 48, Port 16. 128 bits = 2^128 ≈ 3.4 × 10^38 addresses.
*Size line: IPv4 32, IPv6 128, MAC 48, Port 16। 128 bits = 2^128 ≈ 3.4 × 10^38 addresses।*
*[Source: Repo: CN Topic Test-6 (UNIT TEST-6) · Sanfoundry / Medium / MQuestions banks] · Hard*

**Q282.** IPv6 does NOT use which type of address?
*IPv6 किस type का address उपयोग नहीं करता?*
- **(A)** Broadcast
- **(B)** Multicast
- **(C)** Anycast
- **(D)** None of the mentioned
✔ **(A) Broadcast**
★ **Nukta:** IPv4: unicast + broadcast + multicast. IPv6: unicast + multicast + anycast (NO broadcast).
*IPv4: unicast + broadcast + multicast। IPv6: unicast + multicast + anycast (broadcast नहीं)।*
*[Source: Sanfoundry CN MCQs — IPv6] · Hard*

**Q283.** Which features are present in IPv4 but NOT in IPv6?
*कौन-सी features IPv4 में हैं लेकिन IPv6 में नहीं?*
- **(A)** Fragmentation by routers
- **(B)** Header checksum
- **(C)** Options
- **(D)** All of the mentioned
✔ **(D) All of the mentioned**
★ **Nukta:** IPv6 header = fixed 40 bytes, 8 fields, NO checksum / NO router fragmentation / NO options field.
*IPv6 header = fixed 40 bytes, 8 fields, कोई checksum नहीं / कोई router fragmentation नहीं / कोई options field नहीं।*
*[Source: Sanfoundry CN MCQs — IPv6] · Hard*

**Q284.** Which of the following is TRUE for IPv6?
*IPv6 के लिए निम्न में से क्या सही है?*
- **(A)** Uses 32-bit addresses
- **(B)** Includes a header checksum
- **(C)** Supports anycast addressing
- **(D)** Does not support multicast
✔ **(C) Supports anycast addressing**
★ **Nukta:** IPv6 address types: Unicast, Multicast, Anycast. No broadcast, no header checksum.
*IPv6 address types: Unicast, Multicast, Anycast। Broadcast नहीं, header checksum नहीं।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Hard*

## Section E — Port Numbers, DNS/URL & Address Resolution (ARP)

*16-bit ports & ranges, socket addressing, DNS records & lookups, ARP/RARP, URL layer.*

**Process-to-process delivery ke liye ports, web ka address URL, naam se IP nikalne ka DNS, aur IP se MAC nikalne ka ARP — yeh teeno addressing ki finishing touch hain.**

*Process-to-process delivery के लिए ports, web का पता URL, नाम से IP का DNS, और IP से MAC का ARP।*

- Port = 16-bit number (0–65535): Well-known 0–1023 (HTTP 80, FTP 21, DNS 53), Registered 1024–49151, Ephemeral 49152–65535.
  - *Port = 16-bit (0–65535): Well-known 0–1023 (HTTP 80, DNS 53), Registered, Ephemeral।*
- Socket address = IP address + port number — yeh process ko uniquely identify karta hai.
  - *Socket address = IP + port — process की unique पहचान।*
- DNS — hierarchical naam→IP system: Root servers → TLD (.com, .in) → Authoritative; records: A (IPv4), AAAA (IPv6), MX (mail), CNAME (alias), PTR (IP→naam).
  - *DNS — नाम→IP प्रणाली: Root → TLD → Authoritative; records: A, AAAA, MX, CNAME, PTR।*
- Reverse lookup = IP se naam = PTR record; forward lookup = naam se IP = A/AAAA.
  - *Reverse lookup = IP से नाम (PTR); forward = नाम से IP (A/AAAA)।*
- URL parts: scheme (protocol)://host[:port]/path — jaise https://www.example.com/index.html.
  - *URL भाग: scheme://host/path।*
- ARP (Address Resolution Protocol) — IP se MAC nikalna: ARP request broadcast, ARP reply unicast.
  - *ARP — IP से MAC: request broadcast, reply unicast।*
- RARP (Reverse ARP) — MAC se IP (boot time); DHCP ne ise zyada tar replace kar diya.
  - *RARP — MAC से IP; DHCP ने अधिकतर replace किया।*

| Port | Service | Port | Service |
|---|---|---|---|
| 20/21 | FTP data/control | 110 | POP3 |
| 22 | SSH | 143 | IMAP |
| 23 | Telnet | 161/162 | SNMP |
| 25 | SMTP | 443 | HTTPS |
| 53 | DNS | 67/68 | DHCP |
| 80 | HTTP | 123 | NTP |

### Questions (Easy → Medium → Hard)

**Q285.** Which of the following sets of port numbers belongs to the 'well-known' ports category?
*निम्न में से कौन-से port numbers 'well-known' ports category में आते हैं?*
- **(A)** 80, 443, 8080
- **(B)** 49152, 110, 53
- **(C)** 22, 25, 80
- **(D)** 1024, 3306, 8080
✔ **(C) 22, 25, 80**
★ **Nukta:** Port ranges: Well-known 0-1023, Registered 1024-49151, Ephemeral (dynamic) 49152-65535.
*Port ranges: Well-known 0-1023, Registered 1024-49151, Ephemeral (dynamic) 49152-65535।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q286.** What is the typical range of ephemeral (dynamic) ports?
*Ephemeral (dynamic) ports की सामान्य range क्या है?*
- **(A)** 0-1023
- **(B)** 1024-49151
- **(C)** 49152-65535
- **(D)** 100-200
✔ **(C) 49152-65535**
★ **Nukta:** Well-known 0-1023 (services), Registered 1024-49151 (apps), Ephemeral 49152-65535 (clients).
*Well-known 0-1023 (services), Registered 1024-49151 (apps), Ephemeral 49152-65535 (clients)।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) · also CN Topic Test 5] · Easy*

**Q287.** The transport layer uses which type of addressing?
*Transport layer किस प्रकार की addressing उपयोग करता है?*
- **(A)** IP address
- **(B)** MAC address
- **(C)** Port number
- **(D)** Domain name
✔ **(C) Port number**
★ **Nukta:** Layer addressing: Data link = MAC (48), Network = IP (32), Transport = Port (16), Application = specific/socket.
*Layer addressing: Data link = MAC (48), Network = IP (32), Transport = Port (16), Application = specific/socket।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q288.** A URL (like www.example.com) belongs to which layer?
*URL (जैसे www.example.com) किस layer से संबंधित है?*
- **(A)** Presentation
- **(B)** Application
- **(C)** Transport
- **(D)** Network
✔ **(B) Application**
★ **Nukta:** Address levels at layers: specific (app) → port (transport) → IP (network) → MAC (data link).
*Layers पर address levels: specific (app) → port (transport) → IP (network) → MAC (data link)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q289.** DNS works at which layer of the OSI model?
*DNS, OSI model की किस layer पर काम करता है?*
- **(A)** Transport
- **(B)** Application
- **(C)** Network
- **(D)** Data link
✔ **(B) Application**
★ **Nukta:** Application layer examples: DNS, HTTP, FTP, SMTP, SNMP, DHCP. Transport carries them (UDP 53 for DNS).
*Application layer के उदाहरण: DNS, HTTP, FTP, SMTP, SNMP, DHCP। Transport उन्हें ले जाता है (DNS के लिए UDP 53)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q290.** Which of the following uniquely identifies a process on a host?
*Host पर किसी process की unique पहचान कौन करता है?*
- **(A)** IP address only
- **(B)** Port number only
- **(C)** IP address + Port number
- **(D)** MAC address
✔ **(C) IP address + Port number**
★ **Nukta:** IP = the host (machine). IP + Port = the specific process (socket/specific address).
*IP = host (machine)। IP + Port = विशिष्ट process (socket/specific address)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

**Q291.** What is the default port number for DNS?
*DNS का default port number क्या है?*
- **(A)** 80
- **(B)** 21
- **(C)** 53
- **(D)** 110
✔ **(C) 53**
★ **Nukta:** Port one-liners: DNS 53, HTTP 80, HTTPS 443, FTP 21/20, SMTP 25, POP3 110, Telnet 23, SSH 22, DHCP 67/68.
*Port one-liners: DNS 53, HTTP 80, HTTPS 443, FTP 21/20, SMTP 25, POP3 110, Telnet 23, SSH 22, DHCP 67/68।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

**Q292.** DNS is the abbreviation of:
*DNS का पूरा नाम (full form) क्या है?*
- **(A)** Dynamic Name System
- **(B)** Dynamic Network System
- **(C)** Domain Name System
- **(D)** Domain Network Service
✔ **(C) Domain Name System**
★ **Nukta:** DNS = Domain Name System (port 53). Hierarchical: root → TLD → authoritative servers.
*DNS = Domain Name System (port 53)। पदानुक्रम: root → TLD → authoritative servers।*
*[Source: Networking MCQ bank (MQuestions blog)] · Medium*

**Q293.** Which DNS record type maps a domain name to an IPv4 address?
*कौन-सी DNS record type domain name को IPv4 address से जोड़ती है?*
- **(A)** CNAME
- **(B)** A
- **(C)** MX
- **(D)** PTR
✔ **(B) A**
★ **Nukta:** Records quick map: A = name→IPv4, AAAA = name→IPv6, PTR = IP→name, CNAME = alias, MX = mail.
*Records quick map: A = name→IPv4, AAAA = name→IPv6, PTR = IP→name, CNAME = alias, MX = mail।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6) · also cnp3 DNS2] · Medium*

**Q294.** What is the role of DNS? It is best described as:
*DNS की भूमिका क्या है? सबसे सही विवरण है:*
- **(A)** Maps a domain name to an IP address
- **(B)** Translates a host's private IP to a public IP
- **(C)** Translates a host's IPv6 address to an IPv4 address
- **(D)** Maps a MAC address to an IP address
✔ **(A) Maps a domain name to an IP address**
★ **Nukta:** Official RPSC 2024 key. Reverse: PTR records map IP→name. DHCP = auto IP config; NAT = private→public.
*Official RPSC 2024 key। Reverse: PTR records IP→name map करती हैं। DHCP = auto IP config; NAT = private→public।*
*[Source: RPSC Programmer 2024 Paper-1 (official key) · also CN Topic Test-02 / Medium bank] · Hard*

**Q295.** A reverse lookup in DNS means a lookup to ______ using ______ records.
*DNS में reverse lookup का अर्थ है ______ records का उपयोग करके ______ की lookup।*
- **(A)** Identify mail servers, SOA
- **(B)** Map an IP address to a domain name, PTR
- **(C)** Map domain names to IP addresses, A
- **(D)** Determine the authoritative name server, NS
✔ **(B) Map an IP address to a domain name, PTR**
★ **Nukta:** Forward: name → IP (A / AAAA). Reverse: IP → name (PTR, in-addr.arpa).
*Forward: name → IP (A / AAAA)। Reverse: IP → name (PTR, in-addr.arpa)।*
*[Source: RPSC Programmer 2024 Paper-1 (official key) · also CN Topic Test 5] · Hard*

**Q296.** The Address Resolution Protocol (ARP) is used for:
*Address Resolution Protocol (ARP) किस काम में आता है?*
- **(A)** Finding the IP address that corresponds to a MAC address
- **(B)** Finding the MAC address that corresponds to an IP address
- **(C)** Finding the IP address from the DNS name
- **(D)** Finding the IP address of the default gateway
✔ **(B) Finding the MAC address that corresponds to an IP address**
★ **Nukta:** ARP = IP→MAC (Address Resolution). RARP = MAC→IP (obsolete — replaced by BOOTP/DHCP). DNS = name→IP.
*ARP = IP→MAC (Address Resolution)। RARP = MAC→IP (अप्रचलित — BOOTP/DHCP से बदला)। DNS = name→IP।*
*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

**Q297.** Which one of the following protocols is NOT used to resolve one form of address into another?
*निम्न में से कौन-सा protocol एक प्रकार के पते को दूसरे में बदलने के लिए उपयोग नहीं होता?*
- **(A)** DNS
- **(B)** ARP
- **(C)** DHCP
- **(D)** RARP
✔ **(C) DHCP**
★ **Nukta:** Address resolvers: DNS, ARP, RARP. Address distributor: DHCP.
*Address resolvers: DNS, ARP, RARP. Address distributor: DHCP.*
*[Source: GATE CS PYQ (via Computer Science Junction / examprev)] · Hard*

# TOPIC 4 — Networking Devices

## Section A — Physical-Layer Devices (Hub, Repeater, Modem & Simple Devices)

*Layer-1 dumb devices — hub, repeater, modem, multiplexer, file server; collision-domain basics.*

**Physical layer ke devices 'dumb' devices kehlate hain — signal ko regenerate ya combine karte hain, intelligence nahi hoti.**

*Physical layer के devices 'dumb devices' कहलाते हैं — signal regenerate/combine करते हैं, intelligence नहीं होती।*

- Repeater — weak signal ko copy karke original strength tak regenerate karta hai (amplify nahi karta!); distance badhane ke liye; Layer 1.
  - *Repeater — कमज़ोर signal को regenerate करता है (amplify नहीं!); दूरी बढ़ाने के लिए; Layer 1।*
- Hub — multiport repeater; ek port par jo aata hai sab ports par bhej deta hai; sab ports = ek collision domain.
  - *Hub — multiport repeater; एक port का data सब ports पर भेजता है; सब ports = एक collision domain।*
- Hub par shared bandwidth — jitne zyada devices, utna kam speed har device ko.
  - *Hub पर shared bandwidth — जितने अधिक devices, उतनी कम speed।*
- Modem (Modulator-Demodulator) — digital ↔ analog conversion; phone line par data.
  - *Modem — digital ↔ analog रूपांतरण।*
- Multiplexer — ek hi line par kai signals ko combine karta hai (MUX/DEMUX).
  - *Multiplexer — एक line पर कई signals जोड़ता है।*
- File server — files share karne wala dedicated computer (LAN mein).
  - *File server — files साझा करने वाला dedicated computer।*
- Yaad: Repeater/Hub = Layer 1; koi filtering/intelligence nahi — bas signal level ka kaam.
  - *याद: Repeater/Hub = Layer 1; कोई filtering नहीं।*

| Device | Layer | Kaam |
|---|---|---|
| Repeater | 1 | signal regenerate (distance badhana) |
| Hub | 1 | multiport repeater — sabko bhejo |
| Modem | 1 | digital ↔ analog |
| Multiplexer | 1 | kai signals ek line par |

### Questions (Easy → Medium → Hard)

**Q298.** Which device operates only at the Physical layer (Layer 1) of the OSI model?
*OSI model की केवल Physical layer (Layer 1) पर कौन-सा device काम करता है?*
- **(A)** Switch
- **(B)** Hub
- **(C)** Router
- **(D)** Bridge
✔ **(B) Hub**
★ **Nukta:** Layer 1 = Hub, Repeater, Modem, cables. Layer 2 = Switch, Bridge, NIC. Layer 3 = Router. Gateway = all 7 (protocol converter).
*Layer 1 = Hub, Repeater, Modem, cables। Layer 2 = Switch, Bridge, NIC। Layer 3 = Router। Gateway = सभी 7 (protocol converter)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch) · also CN Topic Test-6] · Easy*

**Q299.** Which of the following pairs lists the network devices used at the physical layer?
*निम्न में से कौन-सी जोड़ी physical layer पर उपयोग होने वाले network devices बताती है?*
- **(A)** Gateway, Bridge
- **(B)** Router, Repeater
- **(C)** Hub, Switch
- **(D)** Repeater, Hub
✔ **(D) Repeater, Hub**
★ **Nukta:** Rajasthan PYQ (verified key: D). Physical-layer pair = Repeater + Hub. Switch/Bridge = L2, Gateway = L7.
*Rajasthan PYQ (verified key: D)। Physical-layer जोड़ी = Repeater + Hub। Switch/Bridge = L2, Gateway = L7।*
*[Source: Random Test- Rajasthan PYQ (OCR), p12 — Q93 (options reconstructed from screenshot)] · Medium*

**Q300.** Which of the following are network connecting devices? 1. Repeater  2. Bridge  3. Hub  4. Bluetooth
*निम्न में से कौन network connecting devices हैं? 1. Repeater  2. Bridge  3. Hub  4. Bluetooth*
- **(A)** 1, 2 and 3
- **(B)** 1, 2 and 4
- **(C)** 2, 3 and 4
- **(D)** 1, 3 and 4
✔ **(A) 1, 2 and 3**
★ **Nukta:** Devices vs technologies: repeater/bridge/hub/switch/router = devices. Bluetooth/Wi-Fi/Ethernet = technologies/standards.
*Devices बनाम technologies: repeater/bridge/hub/switch/router = devices। Bluetooth/Wi-Fi/Ethernet = technologies/standards।*
*[Source: Unit Test -2 Solutions (OCR), p11] · Medium*

**Q301.** Which of the following statements are TRUE? 1. Switch reduces collision domain. 2. Hub creates a separate collision domain for each port. 3. Router separates broadcast domains.
*निम्न में से कौन-से कथन सही हैं? 1. Switch collision domain को कम करता है। 2. Hub हर port के लिए अलग collision domain बनाता है। 3. Router broadcast domains को अलग करता है।*
- **(A)** 1 and 2 only
- **(B)** 2 and 3 only
- **(C)** 1 and 3 only
- **(D)** 1, 2 and 3
✔ **(C) 1 and 3 only**
★ **Nukta:** Switch: collision ↓ (per-port). Hub: 1 collision domain. Router: broadcast domains separated. Ye teeno golden statements hain.
*Switch: collision ↓ (per-port)। Hub: 1 collision domain। Router: broadcast domains अलग। ये तीनों golden statements हैं।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q26] · Medium*

**Q302.** Which device combines transmission from various I/O devices into one line?
*कौन-सा device विभिन्न I/O devices के transmission को एक line में मिलाता है?*
- **(A)** Modifier
- **(B)** Multiplexer
- **(C)** Concentrator
- **(D)** Gateway
✔ **(B) Multiplexer**
★ **Nukta:** MUX = many→one line (FDM/TDM/WDM). Concentrator = statistical sharing of a line. Gateway = protocol converter.
*MUX = कई→एक line (FDM/TDM/WDM)। Concentrator = line का statistical sharing। Gateway = protocol converter।*
*[Source: Unit Test-4 Solution (OCR), p22] · Medium*

**Q303.** A file server is a ______ which is used to store files received from various client machines.
*File server एक ______ है जिसका उपयोग विभिन्न client machines से प्राप्त files संग्रहित करने के लिए होता है।*
- **(A)** Specialized computer system
- **(B)** Modem
- **(C)** Router
- **(D)** Transponder
✔ **(A) Specialized computer system**
★ **Nukta:** Servers (file/print/mail/web) = specialised computers. Modem = signal converter, Router = packet forwarder, Transponder = satellite relay.
*Servers (file/print/mail/web) = विशेष computers। Modem = signal converter, Router = packet forwarder, Transponder = satellite relay।*
*[Source: Unit Test-4 Solution (OCR), p24] · Medium*

**Q304.** In a data-entry office, computer centres on the 1st and 4th floors are connected by LANs, but signals take time to travel. Which hardware can improve the data transmission?
*एक data-entry office में 1वीं और 4वीं मंज़िल के computer centres LAN से जुड़े हैं, पर signals में समय लगता है. बेहतर transmission के लिए कौन-सा hardware लगाएँ?*
- **(A)** Repeater
- **(B)** Router
- **(C)** Computer
- **(D)** Modem
✔ **(A) Repeater**
★ **Nukta:** संकेत कमज़ोर → Repeater; रास्ता चाहिए → Router; analog↔digital → Modem.
*संकेत कमज़ोर → Repeater; रास्ता चाहिए → Router; analog↔digital → Modem.*
*[Source: RSMSSB Informatics Assistant 2023 (via examsmantra solved paper)] · Medium*

**Q305.** Which of the following devices operates only in the physical layer?
*निम्न में से कौन-सा device केवल physical layer पर काम करता है?*
- **(A)** Two-layer switch
- **(B)** Router
- **(C)** Repeater
- **(D)** Bridge
✔ **(C) Repeater**
★ **Nukta:** Repeater = signal regenerator (L1). Hub = multi-port repeater (L1). Both are 'dumb' devices.
*Repeater = signal regenerator (L1)। Hub = multi-port repeater (L1)। दोनों 'dumb' devices हैं।*
*[Source: Kerala PSC repeated PYQs (via pscarivukal)] · Hard*

**Q306.** A device that operates at the physical layer of the OSI model is:
*OSI model की physical layer पर काम करने वाला device है:*
- **(A)** Bridge
- **(B)** Router
- **(C)** Repeater
- **(D)** All of these
✔ **(C) Repeater**
★ **Nukta:** Layer-device जोड़ी: L1 = Repeater/Hub, L2 = Bridge/Switch, L3 = Router, L4+ = Gateway.
*Layer-device जोड़ी: L1 = Repeater/Hub, L2 = Bridge/Switch, L3 = Router, L4+ = Gateway.*
*[Source: SBI/IBPS Computer Awareness Capsule 2018 (IBT India)] · Hard*

## Section B — Switch / NIC / Bridge

*CAM table, per-port collision domains, flooding behaviour, VLANs & broadcast domains, wireless AP as bridge.*

**Switch, NIC aur bridge Layer 2 ke devices hain — frame level par MAC addresses dekh kar kaam karte hain.**

*Switch, NIC और bridge Layer 2 के devices हैं — frame level पर MAC addresses देखकर काम करते हैं।*

- Switch = intelligent hub: MAC address table (CAM table) banata hai aur frame sirf usi port par bhejta hai jahan destination hai.
  - *Switch = intelligent hub: MAC table (CAM) बनाता है, frame सही port पर ही भेजता है।*
- Switch ke har port ka apna collision domain — full-duplex, collision khatam.
  - *Switch के हर port का अपना collision domain — collision ख़त्म।*
- Par switch ka ek hi broadcast domain (jab tak VLAN na banao).
  - *पर switch का एक broadcast domain (जब तक VLAN न बनाओ)।*
- Switching modes: Store-and-forward (poora frame lekar FCS check), Cut-through (sirf destination MAC padh kar aage — fast, no error check).
  - *Switching modes: Store-and-forward (FCS check सहित), Cut-through (तेज़, बिना error check)।*
- VLAN = virtual LAN — ek switch par alag-alag broadcast domains; security + organisation.
  - *VLAN = virtual LAN — एक switch पर अलग-अलग broadcast domains।*
- NIC (Network Interface Card) — computer ko network se jodta hai; apna MAC address rakhta hai; Layer 1–2 par kaam.
  - *NIC — computer को network से जोड़ता है; अपना MAC रखता है।*
- Bridge = 2-port switch: do network segments ko MAC addresses se connect/filter karta hai; single collision domain ko split karta hai.
  - *Bridge = 2-port switch: दो segments को MAC से जोड़ता/filter करता है।*

| Device | Kya dekhta hai | Collision domain | Broadcast domain |
|---|---|---|---|
| Hub | — (sirf signal) | sab ek | ek |
| Switch | MAC table | har port alag | ek (VLAN se zyada) |
| Bridge | MAC filter | 2 hisse | ek |

### Questions (Easy → Medium → Hard)

**Q307.** Which device stores MAC addresses in a CAM table?
*कौन-सा device MAC addresses को CAM table में संग्रहित करता है?*
- **(A)** Hub
- **(B)** Router
- **(C)** Switch
- **(D)** Modem
✔ **(C) Switch**
★ **Nukta:** Switch = MAC table (CAM). Router = routing table (IP). Hub = no table (floods). ARP cache = IP→MAC mapping (host).
*Switch = MAC table (CAM)। Router = routing table (IP)। Hub = कोई table नहीं (floods)। ARP cache = IP→MAC mapping (host)।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q308.** A router is connected between two switches. If a broadcast frame is sent on Switch-A, what will Switch-B receive?
*दो switches के बीच एक router जुड़ा है। यदि Switch-A पर broadcast frame भेजा जाए, तो Switch-B क्या प्राप्त करेगा?*
- **(A)** The broadcast
- **(B)** A unicast copy
- **(C)** Nothing
- **(D)** A multicast
✔ **(C) Nothing**
★ **Nukta:** Router = broadcast firewall. This is why routers split broadcast domains and switches don't.
*Router = broadcast firewall। इसीलिए router broadcast domains तोड़ते हैं और switches नहीं।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q309.** What does a MAC address represent?
*MAC address किसका प्रतिनिधित्व करता है?*
- **(A)** The location of the device in the network
- **(B)** The unique identity of the NIC
- **(C)** Internet connectivity
- **(D)** The routing path
✔ **(B) The unique identity of the NIC**
★ **Nukta:** MAC = NIC identity (who). IP = location in network (where). Routing path = router's job.
*MAC = NIC identity (कौन)। IP = network में स्थान (कहाँ)। Routing path = router का काम।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q310.** Which device reduces collision domains (each port has its own collision domain) but does NOT break broadcast domains?
*कौन-सा device collision domains को कम करता है (हर port का अपना collision domain) लेकिन broadcast domains को तोड़ता नहीं?*
- **(A)** Switch
- **(B)** Router
- **(C)** Hub
- **(D)** Gateway
✔ **(A) Switch**
★ **Nukta:** Switch = collision domains many, broadcast 1. Router = broadcast domains many. Hub = 1 collision + 1 broadcast. VLAN = splits broadcast on a switch.
*Switch = collision domains कई, broadcast 1। Router = broadcast domains कई। Hub = 1 collision + 1 broadcast। VLAN = switch पर broadcast तोड़ता है।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) · also CN Topic Test-6] · Medium*

**Q311.** A switch receives a frame whose destination MAC is NOT in its MAC table. What does the switch do?
*एक switch को frame मिलता है जिसका destination MAC उसके MAC table में नहीं है। Switch क्या करेगा?*
- **(A)** Send the frame to the router only
- **(B)** Flood the frame out of all its ports (same broadcast domain)
- **(C)** Drop the frame
- **(D)** Broadcast it on the entire internet
✔ **(B) Flood the frame out of all its ports (same broadcast domain)**
★ **Nukta:** Unknown unicast → flood. Known unicast → single port. Broadcast FF:FF:... → flood. Source MAC → learn/refresh in CAM.
*Unknown unicast → flood। Known unicast → एक port। Broadcast FF:FF:... → flood। Source MAC → CAM में learn/refresh।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q312.** A switch has 4 VLANs configured. How many broadcast domains exist?
*एक switch पर 4 VLANs configure हैं। कितने broadcast domains होंगे?*
- **(A)** 1
- **(B)** 2
- **(C)** 4
- **(D)** Depends on the router
✔ **(C) 4**
★ **Nukta:** VLAN = virtual switch = its own broadcast domain. Inter-VLAN communication needs a router (or L3 switch).
*VLAN = virtual switch = अपना broadcast domain। Inter-VLAN संचार के लिए router (या L3 switch) चाहिए।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q313.** In a router-on-a-stick setup with VLANs, which device handles VLAN tagging and which handles inter-VLAN routing?
*VLANs वाले router-on-a-stick setup में VLAN tagging कौन करता है और inter-VLAN routing कौन?*
- **(A)** Switch – VLAN tags, Router – routing
- **(B)** Router – VLAN tags, Switch – routing
- **(C)** Both switch and router do VLAN tagging
- **(D)** Neither does VLAN tagging
✔ **(A) Switch – VLAN tags, Router – routing**
★ **Nukta:** 802.1Q tagging = switch trunk job. Inter-VLAN routing = router (router-on-a-stick) or L3 switch.
*802.1Q tagging = switch trunk का काम। Inter-VLAN routing = router (router-on-a-stick) या L3 switch।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q314.** A packet travels: wired PC → Switch → Access Point → Wireless laptop. Which devices operate at Layer 2 only?
*एक packet यात्रा करता है: wired PC → Switch → Access Point → Wireless laptop। कौन-से devices केवल Layer 2 पर काम करते हैं?*
- **(A)** Switch only
- **(B)** Access Point only
- **(C)** Both switch and access point
- **(D)** Neither
✔ **(C) Both switch and access point**
★ **Nukta:** AP = wireless bridge (L2). Switch = L2. Router = L3. WAPs don't route unless configured as routers.
*AP = wireless bridge (L2)। Switch = L2। Router = L3। WAPs routing नहीं करते (जब तक router mode में न हों)।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q315.** Which of the following component is responsible for network communication in a computer system?
*कंप्यूटर सिस्टम में network communication के लिए कौन-सा component ज़िम्मेदार होता है?*
- **(A)** UPS
- **(B)** Ethernet card (NIC)
- **(C)** SVGA card
- **(D)** SMPS
✔ **(B) Ethernet card (NIC)**
★ **Nukta:** NIC = computer का network वाला हाथ — इसी पर MAC address बसा होता है.
*NIC = computer का network वाला हाथ — इसी पर MAC address बसा होता है.*
*[Source: Unit Test-4 Solution.pdf (OCR), p18] · Medium*

**Q316.** LANs can be connected by which of the following devices that operate on the data link layer?
*LANs को data link layer पर काम करने वाले निम्न में से किस device से जोड़ा जा सकता है?*
- **(A)** Hub
- **(B)** Bridges
- **(C)** HDLC
- **(D)** Tunnel
✔ **(B) Bridges**
★ **Nukta:** Hub = L1, Bridge/Switch = L2, Router = L3, Gateway = L4+.
*Hub = L1, Bridge/Switch = L2, Router = L3, Gateway = L4+.*
*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Medium*

## Section C — Router / Brouter

*Router functions & layers, per-hop packet changes, broadcast-domain boundaries, congestion (RED), routing basics.*

**Router Layer 3 ka device hai — packets ko best route par aage bhejta hai aur broadcast domains ko todta hai.**

*Router Layer 3 का device है — packets को best route पर भेजता है और broadcast domains को तोड़ता है।*

- Router IP addresses dekh kar routing table se best path chunta hai; har hop par forwarding decision.
  - *Router IP addresses देखकर routing table से best path चुनता है।*
- Router har packet ko aage bhejte waqt: TTL 1 kam, checksum naya, MAC addresses naye hop ke hisaab se — source IP same rehta hai.
  - *Router: TTL 1 कम, checksum नया, MAC नया — source IP वही।*
- Router broadcast domain ko todta hai — ek taraf ka broadcast doosri taraf nahi jaata.
  - *Router broadcast domain तोड़ता है।*
- Router fragmentation kar sakta hai (MTU ke hisaab se) par reassembly sirf destination karta hai.
  - *Router fragmentation कर सकता है पर reassembly सिर्फ़ destination।*
- Static routing (manual) vs Dynamic routing (protocols: RIP, OSPF, BGP).
  - *Static routing (manual) vs Dynamic (RIP, OSPF, BGP)।*
- Brouter = bridge + router: kuch traffic bridge ki tarah, kuch router ki tarah.
  - *Brouter = bridge + router का मिश्रण।*

| Device | Layer | Address | Kaam |
|---|---|---|---|
| Switch | 2 | MAC | frames ko sahi port par |
| Router | 3 | IP | packets ko best path par |
| Gateway | 5–7 / sab | — | protocol conversion |

### Questions (Easy → Medium → Hard)

**Q317.** A router performs which of the following? (1) Packet forwarding  (2) Logical addressing  (3) Collision detection  (4) Routing decision
*Router निम्न में से कौन-सा कार्य करता है? (1) Packet forwarding  (2) Logical addressing  (3) Collision detection  (4) Routing decision*
- **(A)** 1, 2 and 4
- **(B)** 2, 3 and 4
- **(C)** 1 and 3 only
- **(D)** 1, 2, 3 and 4
✔ **(A) 1, 2 and 4**
★ **Nukta:** Router = forward + route + logical addressing. NOT collision detection (that's Ethernet L2 on switches/NICs).
*Router = forward + route + logical addressing। Collision detection नहीं (वह switches/NICs पर Ethernet L2 का काम है)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch) — Q28] · Easy*

**Q318.** A router drops some packets deliberately due to congestion. What is this technique called?
*Router congestion के कारण कुछ packets जानबूझकर छोड़ देता है। इस तकनीक को क्या कहते हैं?*
- **(A)** Delay policing
- **(B)** Redundancy
- **(C)** Random Early Detection (RED)
- **(D)** Reverse flooding
✔ **(C) Random Early Detection (RED)**
★ **Nukta:** Congestion tools: RED (early random drops), Queuing (FIFO/PQ), Traffic shaping. Dropping ALL at overflow = tail drop.
*Congestion tools: RED (early random drops), Queuing (FIFO/PQ), Traffic shaping। Overflow पर सब छोड़ना = tail drop।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q319.** Which device creates a separate broadcast domain?
*कौन-सा device अलग broadcast domain बनाता है?*
- **(A)** Switch
- **(B)** Bridge
- **(C)** Router
- **(D)** Repeater
✔ **(C) Router**
★ **Nukta:** Broadcast domain boundary = router (or VLAN). Collision domain boundary = switch port/bridge.
*Broadcast domain सीमा = router (या VLAN)। Collision domain सीमा = switch port/bridge।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q320.** Which device operates at Layer 3 of the OSI model?
*OSI model की Layer 3 पर कौन-सा device काम करता है?*
- **(A)** Hub
- **(B)** Switch
- **(C)** Router
- **(D)** Repeater
✔ **(C) Router**
★ **Nukta:** Device-layer ladder: Repeater/Hub 1, Switch/Bridge/NIC 2, Router 3, Gateway 7.
*Device-layer ladder: Repeater/Hub 1, Switch/Bridge/NIC 2, Router 3, Gateway 7।*
*[Source: SSC CGL Tier-2 repeated Qs (via Oliveboard)] · Medium*

**Q321.** Consider: S1: The TTL field decreases at each router. S2: The MAC address changes at each hop. Which is correct?
*देखिए: S1: TTL field हर router पर घटती है। S2: MAC address हर hop पर बदलता है। कौन-सा सही है?*
- **(A)** Only S1
- **(B)** Only S2
- **(C)** Both S1 and S2
- **(D)** Neither S1 nor S2
✔ **(C) Both S1 and S2**
★ **Nukta:** Per-hop changes: TTL↓ + MAC rewritten. End-to-end: IP addresses unchanged (except NAT).
*Per-hop बदलाव: TTL↓ + MAC फिर से लिखा जाता है। End-to-end: IP addresses अपरिवर्तित (NAP को छोड़कर)।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

**Q322.** Which hardware forwards data packets between computer networks?
*कौन-सा hardware computer networks के बीच data packets को आगे भेजता है?*
- **(A)** Switch
- **(B)** Router
- **(C)** Cable
- **(D)** Nibble
✔ **(B) Router**
★ **Nukta:** Official KVS key. Router = between networks (L3). Switch = within a network (L2). Cable = medium. Nibble = 4 bits!
*Official KVS key। Router = networks के बीच (L3)। Switch = network के भीतर (L2)। Cable = medium। Nibble = 4 bits!*
*[Source: KVS Librarian 2023 Official Paper (via Testbook) · also CN Topic Test-03] · Hard*

**Q323.** Among these network devices — i. Repeater  ii. Hub  iii. Switch  iv. Router — which are considered intelligent devices?
*इन network devices में — i. Repeater  ii. Hub  iii. Switch  iv. Router — कौन-से intelligent devices माने जाते हैं?*
- **(A)** i and iv only
- **(B)** i and ii only
- **(C)** iii and iv only
- **(D)** ii and iii only
✔ **(C) iii and iv only**
★ **Nukta:** Intelligent = reads addresses + filters/forwards selectively (switch, router, bridge, gateway). Dumb = hub, repeater.
*Intelligent = addresses पढ़ता है + selectively filter/forward करता है (switch, router, bridge, gateway)। Dumb = hub, repeater।*
*[Source: Kerala PSC repeated PYQs (via pscarivukal)] · Hard*

**Q324.** Consider the statements about an IP router: I. A router does not modify the IP packets during forwarding. II. It is not necessary for a router to implement any routing protocol. III. A router should reassemble IP fragments if the MTU of the outgoing link is larger than the incoming fragment. Which is correct?
*IP router के बारे में कथन देखिए: I. Forwarding के दौरान router IP packets को नहीं बदलता। II. Router के लिए कोई routing protocol लागू करना आवश्यक नहीं है। III. यदि outgoing link का MTU आने वाले fragment से बड़ा हो तो router को IP fragments फिर से जोड़ने चाहिए। कौन-सा सही है?*
- **(A)** I and II only
- **(B)** I only
- **(C)** II and III only
- **(D)** II only
✔ **(D) II only**
★ **Nukta:** Advanced but classic: routers modify IP header (TTL/checksum), may run static-only, never reassemble fragments (destination does).
*उन्नत लेकिन classic: router IP header बदलता है (TTL/checksum), केवल static चला सकता है, fragments कभी नहीं जोड़ता (destination जोड़ता है)।*
*[Source: Unit Test-4 Solution (OCR), p15] · Hard*

## Section D — Gateway, Firewall & NAT Devices

*Gateway as protocol converter, firewall types (packet/stateful/proxy), NAT types, device-vs-software identification.*

**Gateway, firewall aur NAT — network ko connect aur secure karne wale special devices.**

*Gateway, firewall और NAT — network को जोड़ने और सुरक्षित करने वाले विशेष devices।*

- Gateway = protocol converter: alag architecture/network ko jodta hai (jaise e-mail gateway, VoIP gateway); sabse 'intelligent' device.
  - *Gateway = protocol converter: अलग networks को जोड़ता है; सबसे 'intelligent' device।*
- Firewall = traffic ko rules se filter karne wala guard: Packet-filter (headers dekhta hai), Stateful (connection ka state yaad rakhta hai), Proxy/Application gateway (poora message check).
  - *Firewall = rules से traffic filter: Packet-filter, Stateful, Proxy/Application gateway।*
- DMZ (Demilitarized Zone) — firewall ke andar/bahar ka beech ka area jahan public servers (web/mail) rakhte hain.
  - *DMZ — public servers रखने का बीच का क्षेत्र।*
- NAT — private ↔ public IP translation: Static (1-1 fixed), Dynamic (pool se), Overload/PAT (ek public IP, alag-alag ports).
  - *NAT — private ↔ public: Static, Dynamic, Overload/PAT।*
- NAT jaate packet mein source IP (aur zaroorat par port) badalta hai — destination nahi.
  - *NAT जाते packet में source IP बदलता है — destination नहीं।*
- Firewall = network security ki pehli deewar; antivirus/IDS alag hote hain.
  - *Firewall = security की पहली दीवार।*

| Device | Kaam | Layer |
|---|---|---|
| Gateway | protocol conversion | 5–7 (ya sab) |
| Packet-filter firewall | header rules (IP, port) | 3–4 |
| Stateful firewall | connection state tracking | 3–4 |
| Proxy firewall | poora message inspect | 7 |
| NAT | private ↔ public IP | 3 |

### Questions (Easy → Medium → Hard)

**Q325.** Which type of firewall inspects packets at the network layer and decides based on IP addresses?
*कौन-सी firewall network layer पर packets की जाँच करके IP addresses के आधार पर निर्णय लेती है?*
- **(A)** Packet Filtering Firewall
- **(B)** Stateful Firewall
- **(C)** Proxy Firewall
- **(D)** Application Firewall
✔ **(A) Packet Filtering Firewall**
★ **Nukta:** Firewall types: Packet filtering (L3/L4, stateless) → Stateful (tracks sessions) → Proxy/Application gateway (L7) → Circuit-level gateway (L5).
*Firewall types: Packet filtering (L3/L4, stateless) → Stateful (sessions याद रखती है) → Proxy/Application gateway (L7) → Circuit-level gateway (L5)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q326.** Which firewall acts as an intermediary between the client and server at the application layer?
*कौन-सी firewall application layer पर client और server के बीच मध्यस्थ (intermediary) के रूप में काम करती है?*
- **(A)** Packet Filtering Firewall
- **(B)** Stateful Firewall
- **(C)** Proxy Firewall
- **(D)** Circuit-level Gateway
✔ **(C) Proxy Firewall**
★ **Nukta:** Proxy = L7 intermediary (deep inspection, hides internals). Circuit gateway = L5 (session/relay).
*Proxy = L7 intermediary (गहरी जाँच, internals छिपाती है)। Circuit gateway = L5 (session/relay)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q327.** If two systems use DIFFERENT protocols, which device is used to link them?
*यदि दो systems भिन्न protocols उपयोग करते हैं, तो उन्हें जोड़ने के लिए कौन-सा device उपयोग होता है?*
- **(A)** Repeater
- **(B)** Gateway
- **(C)** Bridge
- **(D)** Hub
✔ **(B) Gateway**
★ **Nukta:** Gateway = protocol converter (L7). Bridge = similar LANs, same protocols (L2). Repeater/Hub = signal level (L1).
*Gateway = protocol converter (L7)। Bridge = समान LANs, समान protocols (L2)। Repeater/Hub = signal level (L1)।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Medium*

**Q328.** Which device can operate across all 7 layers of the OSI model?
*कौन-सा device OSI model की सभी 7 layers पर काम कर सकता है?*
- **(A)** Router
- **(B)** Hub
- **(C)** Gateway
- **(D)** Switch
✔ **(C) Gateway**
★ **Nukta:** Gateway = 'all 7 layers' device. Hub 1, switch/bridge 2, router 3 — exam one-liner.
*Gateway = 'सभी 7 layers' वाला device। Hub 1, switch/bridge 2, router 3 — exam one-liner।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

**Q329.** Devices on one network can communicate with devices on another network via:
*एक network के devices दूसरे network के devices से किसके माध्यम से संवाद कर सकते हैं?*
- **(A)** File server
- **(B)** Utility server
- **(C)** Printer server
- **(D)** Gateway
✔ **(D) Gateway**
★ **Nukta:** Gateway = network-to-network doorway (also default gateway = router IP used to exit the LAN).
*Gateway = network-to-network दरवाज़ा (default gateway भी = LAN से बाहर निकलने के लिए router IP)।*
*[Source: SSC CGL Internet & Networking (via EduRev bank)] · Medium*

**Q330.** What is the role of a firewall in computer networks?
*Computer networks में firewall की भूमिका क्या है?*
- **(A)** Managing IP addresses
- **(B)** Filtering and controlling network traffic
- **(C)** Resolving domain names
- **(D)** Assigning MAC addresses dynamically
✔ **(B) Filtering and controlling network traffic**
★ **Nukta:** Firewall = traffic filter between trusted & untrusted networks (screening router, DMZ...). DHCP = IP management; DNS = names.
*Firewall = trusted और untrusted networks के बीच traffic filter (screening router, DMZ...)। DHCP = IP management; DNS = names।*
*[Source: 30 important CN MCQs (Medium blog bank)] · Medium*

**Q331.** What is the purpose of a proxy server in networking?
*Networking में proxy server का उद्देश्य क्या है?*
- **(A)** Managing IP addresses
- **(B)** Filtering and forwarding network traffic
- **(C)** Assigning MAC addresses dynamically
- **(D)** Encrypting network communication
✔ **(B) Filtering and forwarding network traffic**
★ **Nukta:** Proxy = filter + forward + cache + hide client. Firewall = block/allow by rules. Both are security/traffic devices.
*Proxy = filter + forward + cache + client छिपाना। Firewall = rules से block/allow। दोनों security/traffic devices हैं।*
*[Source: 30 important CN MCQs (Medium blog bank)] · Medium*

**Q332.** Which is a network security system designed to protect a trusted private network from an untrusted outside network to which it is connected?
*कौन-सी network security system trusted private network को उस जुड़े हुए untrusted outside network से बचाने के लिए बनी है?*
- **(A)** Bridge
- **(B)** Cookies
- **(C)** Firewall
- **(D)** SSL
✔ **(C) Firewall**
★ **Nukta:** Rajasthan PYQ (verified key: C) — the classic firewall definition. Compare: bridge = L2 link, cookie = web state, SSL = encryption.
*Rajasthan PYQ (verified key: C) — firewall की classic परिभाषा। तुलना: bridge = L2 link, cookie = web state, SSL = encryption।*
*[Source: Random Test- Rajasthan PYQ (OCR), p6 — Q110 (options reconstructed from screenshot)] · Medium*

**Q333.** What kind of NAT maps one private IP to exactly one public IP?
*किस प्रकार का NAT एक private IP को ठीक एक public IP से जोड़ता है?*
- **(A)** Dynamic NAT
- **(B)** Static NAT
- **(C)** PAT (Port Address Translation)
- **(D)** Port Forwarding
✔ **(B) Static NAT**
★ **Nukta:** NAT types: Static = 1↔1 permanent. Dynamic = pool mapping. PAT/NAT-overload = many↔1 using ports.
*NAT types: Static = 1↔1 स्थायी। Dynamic = pool mapping। PAT/NAT-overload = ports से many↔1।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

**Q334.** Which of the following is NOT a networking device?
*निम्न में से कौन-सा networking device नहीं है?*
- **(A)** Gateway
- **(B)** Linux
- **(C)** Router
- **(D)** Firewall
✔ **(B) Linux**
★ **Nukta:** Device vs OS: hardware devices (hub/switch/router) vs software (OS, antivirus) vs firmware-based security devices (firewall).
*Device बनाम OS: hardware devices (hub/switch/router) बनाम software (OS, antivirus) बनाम firmware-based security devices (firewall)।*
*[Source: InstrumentationTools 150 CN MCQs] · Hard*

**Q335.** Which of the following is NOT a networking device? (Hub / Switch / Bridge / None of these)
*निम्न में से कौन-सा networking device नहीं है? (Hub / Switch / Bridge / इनमें से कोई नहीं)*
- **(A)** Hub
- **(B)** Switch
- **(C)** Bridge
- **(D)** None of these
✔ **(D) None of these**
★ **Nukta:** Mirror question of the 'Linux' variant — read the option SET carefully: here everything listed IS a device.
*'Linux' वाले प्रश्न का दर्पण — option SET ध्यान से पढ़ें: यहाँ सूचीबद्ध सब devices हैं।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Hard*

# TOPIC 5 — Transmission Medium

## Section A — Signals & Performance (Encoding, Noise, Bandwidth, Data Rate)

*Line coding (Manchester, 8B/10B, scramblers), impairments (attenuation/crosstalk/noise), signal parameters, data-rate & Shannon/Nyquist calculations.*

**Signal kya hota hai (analog/digital), data kaise encode hota hai, noise kya bigadta hai, aur bandwidth/datarate ke formulas — yeh topic ke core concepts hain.**

*Signal क्या होता है (analog/digital), data कैसे encode होता है, noise क्या बिगाड़ता है, और bandwidth/data rate के formulas।*

- Analog signal continuous (sine wave), Digital signal discrete (0/1 levels); dono analog ya digital medium par chal sakte hain.
  - *Analog signal सतत (sine wave), Digital signal discrete (0/1); दोनों medium पर चल सकते हैं।*
- Line coding: Manchester = har bit ke beech transition (self-synchronizing, Ethernet); NRZ = level constant; 8B/10B, scrambler = DC balance ke liye.
  - *Line coding: Manchester = हर bit में transition (self-synchronizing); NRZ; 8B/10B।*
- Impairments: Attenuation (signal kamzor), Distortion (shape badalna), Noise (thermal, crosstalk, impulse).
  - *Impairments: Attenuation (कमज़ोरी), Distortion (आकार बिगड़ना), Noise (thermal, crosstalk, impulse)।*
- Bandwidth = frequency range (Hz) — medium ki capacity; data rate = bits per second (bps).
  - *Bandwidth = frequency range (Hz); data rate = bps।*
- Nyquist: 2 × B × log₂(L) bps (noiseless channel, L signal levels).
  - *Nyquist: 2 × B × log₂(L) bps (noiseless channel)।*
- Shannon: C = B × log₂(1 + S/N) bps (noisy channel); SNR(dB) = 10 × log₁₀(S/N).
  - *Shannon: C = B × log₂(1 + S/N); SNR(dB) = 10 × log₁₀(S/N)।*
- Attenuation loss dB mein: 10 log₁₀(Pout/Pin); repeater se signal restore hota hai.
  - *Attenuation loss dB में: 10 log₁₀(Pout/Pin); repeater से restore।*

| Formula | Kab use | Formula |
|---|---|---|
| Nyquist | noiseless channel | 2B log₂(L) |
| Shannon | noisy channel | B log₂(1+S/N) |
| SNR (dB) | signal-to-noise | 10 log₁₀(S/N) |
| Attenuation (dB) | signal loss | 10 log₁₀(P₂/P₁) |

### Questions (Easy → Medium → Hard)

**Q336.** 'Manchester Encoding' and 'Differential Manchester Encoding' are signal encoding techniques used at which layer?
*'Manchester Encoding' और 'Differential Manchester Encoding' signal encoding techniques किस layer पर उपयोग होती हैं?*
- **(A)** Physical Layer
- **(B)** Data Link Layer
- **(C)** Network Layer
- **(D)** Presentation Layer
✔ **(A) Physical Layer**
★ **Nukta:** Physical layer = signalling & encoding (Manchester = mid-bit transition, self-clocking).
*Physical layer = signalling और encoding (Manchester = mid-bit transition, self-clocking)।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q337.** A channel has high bandwidth but suffers from high noise. Which encoding scheme gives better error resistance?
*एक channel की bandwidth अधिक है लेकिन noise बहुत है। कौन-सी encoding scheme बेहतर error resistance देगी?*
- **(A)** NRZ
- **(B)** Manchester
- **(C)** AMI
- **(D)** ASK
✔ **(B) Manchester**
★ **Nukta:** Manchester = self-clocking + DC-free + strong error visibility. NRZ = long runs → clock loss in noise.
*Manchester = self-clocking + DC-free + मज़बूत error visibility। NRZ = लंबे runs → noise में clock loss।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q338.** Reduction in signal strength over distance is called:
*दूरी के साथ signal strength में कमी को क्या कहते हैं?*
- **(A)** Distortion
- **(B)** Noise
- **(C)** Attenuation
- **(D)** Interference
✔ **(C) Attenuation**
★ **Nukta:** Impairments: Attenuation (strength loss), Distortion (shape change), Noise (unwanted signals). Attenuation ↑ with distance & frequency.
*Impairments: Attenuation (strength loss), Distortion (shape change), Noise (unwanted signals)। Attenuation ↑ distance और frequency के साथ।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) · also CN Topic Test-04] · Easy*

**Q339.** In a copper cable, attenuation increases with frequency. Which change will REDUCE attenuation?
*Copper cable में attenuation frequency के साथ बढ़ता है। कौन-सा बदलाव attenuation घटाएगा?*
- **(A)** Increase cable length
- **(B)** Use lower-category UTP
- **(C)** Use thicker copper core
- **(D)** Increase signal frequency
✔ **(C) Use thicker copper core**
★ **Nukta:** Reduce attenuation: shorter cable, thicker/better copper, higher category cable, lower frequency, or add repeaters/amplifiers.
*Attenuation घटाना: छोटी cable, मोटा/बेहतर copper, उच्च श्रेणी cable, कम frequency, या repeaters/amplifiers जोड़ें।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q340.** Which noise is caused by electromagnetic coupling between nearby cables?
*पास की cables के बीच electromagnetic coupling से कौन-सा noise होता है?*
- **(A)** Thermal noise
- **(B)** Crosstalk
- **(C)** Impulse noise
- **(D)** Quantization noise
✔ **(B) Crosstalk**
★ **Nukta:** Noise types: Thermal (random electron motion), Crosstalk (pair-to-pair coupling), Impulse (sudden spikes), Quantization (PCM sampling).
*Noise types: Thermal (random electron motion), Crosstalk (pair-to-pair coupling), Impulse (sudden spikes), Quantization (PCM sampling)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q341.** Which impairment cannot be completely eliminated but only minimised?
*कौन-सा impairment पूरी तरह समाप्त नहीं किया जा सकता, केवल कम किया जा सकता है?*
- **(A)** Attenuation
- **(B)** Distortion
- **(C)** Noise
- **(D)** Delay
✔ **(C) Noise**
★ **Nukta:** Attenuation/distortion can be fixed with repeaters/equalisers; noise is fundamental (thermal floor) — only minimised.
*Attenuation/distortion repeaters/equalisers से ठीक हो सकते हैं; noise मूलभूत है (thermal floor) — केवल कम होती है।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q342.** Which parameter of an analog signal represents the number of cycles per second?
*Analog signal का कौन-सा parameter प्रति सेकंड cycles की संख्या दर्शाता है?*
- **(A)** Amplitude
- **(B)** Phase
- **(C)** Frequency
- **(D)** Wavelength
✔ **(C) Frequency**
★ **Nukta:** Signal parameters: Amplitude (height), Frequency (cycles/sec), Phase (start position), Wavelength (distance/cycle = speed/frequency).
*Signal parameters: Amplitude (ऊँचाई), Frequency (cycles/sec), Phase (शुरुआती स्थिति), Wavelength (दूरी/cycle = speed/frequency)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q343.** Which of the following Ethernet encodings has the highest redundancy?
*निम्न में से कौन-सी Ethernet encoding की redundancy सबसे अधिक है?*
- **(A)** 1B2B
- **(B)** 4B5B
- **(C)** 5B6B
- **(D)** 8B10B
✔ **(A) 1B2B**
★ **Nukta:** Redundancy (overhead): 1B2B 100% > 4B5B/8B10B 25% > 5B6B 20%. More redundancy = better clocking/error properties, more bandwidth.
*Redundancy (overhead): 1B2B 100% > 4B5B/8B10B 25% > 5B6B 20%। ज़्यादा redundancy = बेहतर clocking/error properties, ज़्यादा bandwidth।*
*[Source: Unit Test-4 Solution (OCR), p9 (options recovered from source)] · Medium*

**Q344.** Which encoding technique is used to transmit signals in Gigabit Ethernet over fiber optic medium?
*Fiber optic medium पर Gigabit Ethernet में signal भेजने के लिए कौन-सी encoding technique उपयोग होती है?*
- **(A)** Differential Manchester encoding
- **(B)** Non-Return-to-Zero (NRZ)
- **(C)** 4B/5B
- **(D)** 8B/10B
✔ **(D) 8B/10B**
★ **Nukta:** 100BASE-TX uses 4B/5B + MLT-3; 1000BASE-X uses 8B/10B; 10GBASE-R uses 64B/66B. Ye exam favourite ladder hai.
*100BASE-TX में 4B/5B + MLT-3; 1000BASE-X में 8B/10B; 10GBASE-R में 64B/66B। यह exam favourite ladder है।*
*[Source: Unit Test-4 Solution (OCR), p30 (options recovered from source)] · Medium*

**Q345.** ______ signals are discrete and are generated by digital modulation.
*______ signals discrete होते हैं और digital modulation से बनते हैं।*
- **(A)** Analog
- **(B)** Digital
- **(C)** Noise
- **(D)** Bandwidth
✔ **(B) Digital**
★ **Nukta:** Rajasthan PYQ verified key (B). Analog = continuous; Digital = discrete. Ye sabse basic signal distinction hai.
*Rajasthan PYQ verified key (B)। Analog = continuous; Digital = discrete। यह signal का सबसे बुनियादी भेद है।*
*[Source: Random Test- Rajasthan PYQ (OCR), p5 — Q108 (options recovered)] · Medium*

**Q346.** Quantizing noise occurs in:
*Quantizing noise किसमें होती है?*
- **(A)** PCM (Pulse Code Modulation)
- **(B)** TDM
- **(C)** FDM
- **(D)** PPM
✔ **(A) PCM (Pulse Code Modulation)**
★ **Nukta:** Rajasthan PYQ verified key (A). PCM = sampling + quantizing + encoding → quantizing error = quantization noise.
*Rajasthan PYQ verified key (A)। PCM = sampling + quantizing + encoding → quantizing error = quantization noise।*
*[Source: Random Test- Rajasthan PYQ (OCR), p10 — Q39 (options recovered)] · Medium*

**Q347.** The effective bandwidth of a communication channel is primarily limited by:
*Communication channel की effective bandwidth मुख्य रूप से किससे सीमित होती है?*
- **(A)** Protocol overhead
- **(B)** Noise and attenuation
- **(C)** File size
- **(D)** MAC address filtering
✔ **(B) Noise and attenuation**
★ **Nukta:** Effective bandwidth is a physics/SNR limit. Protocol overhead reduces goodput but is not the channel's fundamental limit.
*Effective bandwidth एक physics/SNR सीमा है। Protocol overhead goodput घटाता है पर channel की मूल सीमा नहीं।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q348.** What technique allows multiple signals to share the same communication channel?
*कौन-सी technique कई signals को एक ही communication channel share करने देती है?*
- **(A)** Multiplexing
- **(B)** Phase modulation
- **(C)** Analog modulation
- **(D)** Digital modulation
✔ **(A) Multiplexing**
★ **Nukta:** Multiplexing = many share one channel. FDM = frequency bands, TDM = time slots, WDM = light wavelengths, CDM = codes.
*Multiplexing = कई एक channel share करें। FDM = frequency bands, TDM = time slots, WDM = light wavelengths, CDM = codes।*
*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

**Q349.** Communication using a modulated carrier to apply a data signal to a transmission medium in analog form is:
*Modulated carrier का उपयोग करके data signal को analog रूप में transmission medium पर डालना क्या कहलाता है?*
- **(A)** Broadband networking
- **(B)** Baseband networking
- **(C)** Modem
- **(D)** Local area network
✔ **(A) Broadband networking**
★ **Nukta:** Baseband = digital signalling (Manchester etc.). Broadband = analog carriers + modulation (FDM channels).
*Baseband = digital signalling (Manchester आदि)। Broadband = analog carriers + modulation (FDM channels)।*
*[Source: IBPS RRB PO Computer Awareness PYQ (via Meritnotes)] · Medium*

**Q350.** The amount of data transmitted in a fixed amount of time is called:
*निश्चित समय में भेजे गए data की मात्रा को क्या कहते हैं?*
- **(A)** Refresh rate
- **(B)** Resolution
- **(C)** Bandwidth
- **(D)** Frequency
✔ **(C) Bandwidth**
★ **Nukta:** Strictly: THROUGHPUT = data actually sent per second; BANDWIDTH = maximum capacity. Banks often call throughput 'bandwidth' — read options carefully.
*कठोरता से: THROUGHPUT = वास्तव में प्रति सेकंड भेजा data; BANDWIDTH = अधिकतम capacity। Banks अक्सर throughput को 'bandwidth' कहते हैं — options ध्यान से पढ़ें।*
*[Source: Unit Test-4 Solution (OCR), p23] · Medium*

**Q351.** Communication using a modulated carrier to apply a data signal to a transmission medium in analog form is called:
*Modulated carrier का उपयोग करके data signal को analog रूप में transmission medium पर भेजना कहलाता है:*
- **(A)** Broadband communication
- **(B)** Baseband communication
- **(C)** Modem
- **(D)** Local area network
✔ **(A) Broadband communication**
★ **Nukta:** Baseband = digital, सीधा; Broadband = analog, modulated. यह जोड़ी परीक्षा में बार-बार.
*Baseband = digital, सीधा; Broadband = analog, modulated. यह जोड़ी परीक्षा में बार-बार.*
*[Source: IBPS RRB PO Computer Awareness PYQ (via meritnotes)] · Medium*

**Q352.** Identify the odd one out: Optical fibre, Twisted pair wire, Microwaves, Hertz
*असंगत वस्तु पहचानें: Optical fibre, Twisted pair wire, Microwaves, Hertz*
- **(A)** Optical fibre
- **(B)** Twisted pair wire
- **(C)** Microwaves
- **(D)** Hertz
✔ **(D) Hertz**
★ **Nukta:** Media = रास्ता; Hertz = गति/आवृत्ति माप. यही अंतर पूछा गया है.
*Media = रास्ता; Hertz = गति/आवृत्ति माप. यही अंतर पूछा गया है.*
*[Source: RRB NTPC previous-year computer banks (via adda247 50-PYQ PDF)] · Medium*

**Q353.** The primary use of scramblers in line coding schemes is to:
*Line coding schemes में scramblers का मुख्य उपयोग क्या है?*
- **(A)** Make the data look random
- **(B)** Compress transmission data
- **(C)** Increase signal bandwidth
- **(D)** Decrease signal bandwidth
✔ **(A) Make the data look random**
★ **Nukta:** Official RPSC 2024 key. Scrambler = random-looking line signal (clock recovery). Not compression, not encryption.
*Official RPSC 2024 key। Scrambler = random-looking line signal (clock recovery)। Compression नहीं, encryption नहीं।*
*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

**Q354.** The period of a signal is 100 ms. What is its frequency in kilohertz?
*एक signal की period 100 ms है। इसकी frequency kilohertz में कितनी होगी?*
- **(A)** 10⁻¹ kHz
- **(B)** 10⁻² kHz
- **(C)** 10⁻³ kHz
- **(D)** 10⁻⁴ kHz
✔ **(B) 10⁻² kHz**
★ **Nukta:** f = 1/T. 100 ms = 0.1 s → 10 Hz. Convert Hz→kHz by dividing by 1000.
*f = 1/T। 100 ms = 0.1 s → 10 Hz। Hz→kHz के लिए 1000 से भाग दें।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

**Q355.** If the channel bandwidth is limited to 6 kHz and the signal-to-noise ratio is 16, what is the channel capacity?
*यदि channel bandwidth 6 kHz सीमित है और signal-to-noise ratio 16 है, तो channel capacity कितनी होगी?*
- **(A)** 15.15 kbps
- **(B)** 24.74 kbps
- **(C)** 30.12 kbps
- **(D)** 52.18 kbps
✔ **(B) 24.74 kbps**
★ **Nukta:** Rajasthan PYQ verified key (B). Shannon: C = B log₂(1+SNR). Nyquist: C = 2B log₂(L) (noiseless).
*Rajasthan PYQ verified key (B)। Shannon: C = B log₂(1+SNR)। Nyquist: C = 2B log₂(L) (noiseless)।*
*[Source: Random Test- Rajasthan PYQ (OCR), p30 — Q45 (options recovered)] · Hard*

**Q356.** Given a bit rate of b bits/sec, the time required to send 16 bits is:
*यदि bit rate b bits/sec है, तो 16 bits भेजने में कितना समय लगेगा?*
- **(A)** 16 × b sec
- **(B)** 16/b sec
- **(C)** 16b sec
- **(D)** b/16 sec
✔ **(B) 16/b sec**
★ **Nukta:** Time = size/rate. 1000 bits at 100 bps = 10 s. Units: bits ÷ (bits/sec) = sec.
*Time = size/rate। 1000 bits at 100 bps = 10 s। Units: bits ÷ (bits/sec) = sec।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

**Q357.** An analog signal carries 4 bits per signal unit. If 1000 signal units are sent per second, what are the baud rate and bit rate?
*एक analog signal प्रति signal unit 4 bits ले जाती है। यदि प्रति सेकंड 1000 signal units भेजे जाएँ, तो baud rate और bit rate क्या होंगे?*
- **(A)** 1000 bauds/sec, 4000 bps
- **(B)** 1000 bauds/sec, 500 bps
- **(C)** 4000 bauds/sec, 1000 bps
- **(D)** 2000 bauds/sec, 1000 bps
✔ **(A) 1000 bauds/sec, 4000 bps**
★ **Nukta:** Bit rate = Baud rate × bits per signal unit. Baud = signalling speed; bps = data speed.
*Bit rate = Baud rate × प्रति signal unit bits। Baud = signalling speed; bps = data speed।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

**Q358.** Consider a noiseless channel with a bandwidth of 5000 Hz transmitting a signal with two signal levels. The maximum bit rate is:
*एक noiseless channel जिसकी bandwidth 5000 Hz है, दो signal levels के साथ transmission कर रहा है. अधिकतम bit rate होगी:*
- **(A)** 2500 bps
- **(B)** 10000 bps
- **(C)** 5000 bps
- **(D)** 20000 bps
✔ **(B) 10000 bps**
★ **Nukta:** UGC NET Jan 2025 official key (ii). याद रखो: 2B log₂L (noiseless) और B log₂(1+S/N) (noisy — Shannon).
*UGC NET Jan 2025 official key (ii). याद रखो: 2B log₂L (noiseless) और B log₂(1+S/N) (noisy — Shannon).*
*[Source: UGC NET Computer Science Jan 2025 (via samagracs solved paper)] · Hard*

**Q359.** Which of the following is NOT a type of broadband internet connection?
*निम्न में से कौन-सा broadband internet connection का प्रकार नहीं है?*
- **(A)** Cable
- **(B)** DSL
- **(C)** Satellite
- **(D)** Dial-up
✔ **(D) Dial-up**
★ **Nukta:** Media = the path; Hertz = the frequency/speed measure. This distinction is what is being asked.
*Broadband = fast internet (Cable/DSL/Fibre/Satellite); Dial-up = टेलीफ़ोन वाला पुराना संस्करण.*
*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Hard*

## Section B — Guided Media (UTP, Coaxial, Fiber Optic)

*Twisted pair, coaxial and fiber — properties, connectors, distances, termination, EMI behaviour, total internal reflection.*

**Guided media = wired media: twisted pair, coaxial, fiber optic — teeno ki properties exam mein classic.**

*Guided media = तार वाला medium: twisted pair, coaxial, fiber optic।*

- UTP (Unshielded Twisted Pair) — 4 wire pairs twisted; sasta, aasan; 100 m tak; Cat5e/Cat6/Cat7/Cat8 grades; crosstalk ka issue.
  - *UTP — 4 twisted pairs; सस्ता; 100 m; Cat5e–Cat8; crosstalk की समस्या।*
- STP = shielded twisted pair — extra metal shield, EMI kam, mehenga.
  - *STP — extra shield, EMI कम, महँगा।*
- Coaxial — central copper + insulation + shield (BNC connector); 50 ohm (thin/thick Ethernet) aur 75 ohm (cable TV).
  - *Coaxial — central copper + shield (BNC); 50 Ω (Ethernet), 75 Ω (cable TV)।*
- Fiber optic — glass/plastic core mein light pulses: sabse tez, EMI immune, door tak; Single-mode (ek ray, lambi doori) vs Multi-mode (kai rays, chhoti doori).
  - *Fiber optic — रोशनी की pulses: सबसे तेज़, EMI immune; Single-mode vs Multi-mode।*
- Fiber connectors: SC, LC, ST; fiber mehenga hai aur termination mushkil.
  - *Fiber connectors: SC, LC, ST; fiber महँगा और termination कठिन।*
- Comparison: cost — UTP < coax < fiber; speed/distance — fiber sabse aage; noise immunity — fiber best.
  - *तुलना: लागत UTP < coax < fiber; गति/दूरी — fiber सर्वोत्तम।*

| Medium | Speed/Distance | Feature |
|---|---|---|
| UTP | 100 m, 1–10 Gbps | सस्ता, crosstalk |
| Coaxial | ~500 m | shielded, cable TV |
| Fiber (multi-mode) | ~2 km | light, tez |
| Fiber (single-mode) | 100 km+ | long haul, sabse tez |

### Questions (Easy → Medium → Hard)

**Q360.** Optical fiber uses reflection to guide light through a channel. At total internal reflection, the angle of incidence is ______ the critical angle.
*Optical fiber प्रकाश को channel में भेजने के लिए reflection उपयोग करती है। Total internal reflection में angle of incidence, critical angle से ______ होता है।*
- **(A)** Equal to
- **(B)** Less than
- **(C)** Greater than
- **(D)** Less than or equal to
✔ **(C) Greater than**
★ **Nukta:** TIR rule: angle of incidence > critical angle (denser → rarer medium). Ye fiber propagation ka base hai.
*TIR rule: angle of incidence > critical angle (denser → rarer medium)। यह fiber propagation का आधार है।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4) — recovered from BCI T8 Q33 options] · Easy*

**Q361.** A network uses coaxial cable but suffers from signal reflection. What is the most likely cause?
*एक network coaxial cable उपयोग करता है लेकिन signal reflection से पीड़ित है। सबसे संभावित कारण क्या है?*
- **(A)** EMI
- **(B)** Incorrect termination resistance
- **(C)** Crosstalk
- **(D)** Low bandwidth
✔ **(B) Incorrect termination resistance**
★ **Nukta:** Coax rule: proper termination (BNC/terminator) prevents reflections. Un-terminated bus = standing waves & echoes.
*Coax rule: सही termination (BNC/terminator) reflections रोकता है। Un-terminated bus = standing waves और echoes।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q362.** Which transmission medium is primarily used in modern internet backbone networks?
*आधुनिक internet backbone networks में मुख्य रूप से कौन-सा transmission medium उपयोग होता है?*
- **(A)** Twisted pair cable
- **(B)** Coaxial cable
- **(C)** Single mode fiber optic cable
- **(D)** Microwave links
✔ **(C) Single mode fiber optic cable**
★ **Nukta:** Backbone = single-mode fiber (undersea/terrestrial cables). LAN = UTP. Old cable TV = coax. Remote areas = microwave/satellite.
*Backbone = single-mode fiber (undersea/terrestrial cables)। LAN = UTP। पुराना cable TV = coax। दूरस्थ क्षेत्र = microwave/satellite।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

**Q363.** Which cable has the maximum bandwidth?
*किस cable की bandwidth अधिकतम होती है?*
- **(A)** Coaxial
- **(B)** Twisted pair
- **(C)** Optical fiber
- **(D)** USB cable
✔ **(C) Optical fiber**
★ **Nukta:** Bandwidth order: Fiber >> Coax > Twisted pair. USB is a peripheral bus, not a network cable type here.
*Bandwidth क्रम: Fiber >> Coax > Twisted pair। USB peripheral bus है, यहाँ network cable type नहीं।*
*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

**Q364.** Assertion (A): Fiber optic cable is immune to electromagnetic interference (EMI). Reason (R): It transmits data in the form of light pulses rather than electrical signals. Which option is correct?
*Assertion (A): Fiber optic cable electromagnetic interference (EMI) से मुक्त है। Reason (R): यह data electrical signals के बजाय light pulses के रूप में भेजती है। कौन-सा विकल्प सही है?*
- **(A)** Both (A) and (R) are true, and (R) is the correct explanation of (A)
- **(B)** Both (A) and (R) are true, but (R) is NOT the correct explanation
- **(C)** (A) is true, but (R) is false
- **(D)** (A) is false, but (R) is true
✔ **(A) Both (A) and (R) are true, and (R) is the correct explanation of (A)**
★ **Nukta:** Fiber = light pulses → EMI-proof + tap-proof + huge bandwidth. Copper = electrical → EMI/crosstalk prone.
*Fiber = light pulses → EMI-proof + tap-proof + विशाल bandwidth। Copper = electrical → EMI/crosstalk प्रवण।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) — Assertion-Reason] · Medium*

**Q365.** Which statements are TRUE for fiber optic cables? I. Immune to tapping  II. High bandwidth  III. Requires electrical grounding  IV. Works using total internal reflection
*Fiber optic cables के लिए कौन-से कथन सही हैं? I. Tapping से मुक्त  II. उच्च bandwidth  III. Electrical grounding चाहिए  IV. Total internal reflection से काम करती है*
- **(A)** I, II and IV
- **(B)** II and III
- **(C)** I, III and IV
- **(D)** I and II
✔ **(A) I, II and IV**
★ **Nukta:** Fiber truths: immune to tapping & EMI, highest bandwidth, TIR propagation. Myths: grounding (NO), affected by lightning (NO).
*Fiber truths: tapping और EMI से मुक्त, सर्वोच्च bandwidth, TIR propagation। Myths: grounding (नहीं), lightning (नहीं)।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) — Q33] · Medium*

**Q366.** A company needs long-distance communication (5-10 km), high data rate and immunity from electromagnetic interference. Which medium is best?
*एक कंपनी को लंबी दूरी (5-10 km) संचार, उच्च data rate और EMI से मुक्ति चाहिए। कौन-सा medium सर्वोत्तम है?*
- **(A)** UTP
- **(B)** Coaxial cable
- **(C)** Single-mode fiber
- **(D)** Multi-mode fiber
✔ **(C) Single-mode fiber**
★ **Nukta:** Fiber choices: Multi-mode = short (LANs, few hundred m). Single-mode = long haul (km) + highest rate. Copper = short & EMI-prone.
*Fiber विकल्प: Multi-mode = छोटी दूरी (LANs, कुछ सौ m)। Single-mode = लंबी (km) + उच्चतम rate। Copper = छोटी और EMI-प्रवण।*
*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

**Q367.** A UTP cable used in Gigabit Ethernet shows high delay skew. What is the cause?
*Gigabit Ethernet में उपयोग UTP cable में delay skew अधिक है। कारण क्या है?*
- **(A)** Different twist rates in the cable pairs
- **(B)** Excessive EMI
- **(C)** Fiber splice error
- **(D)** Wrong wireless channel
✔ **(A) Different twist rates in the cable pairs**
★ **Nukta:** Delay skew = pair-to-pair propagation time difference (tight twist → shorter wire → less skew). Cat6 has tighter specs for Gigabit.
*Delay skew = pair-to-pair propagation time अंतर (tight twist → छोटी wire → कम skew)। Cat6 में Gigabit के लिए कड़े specs हैं।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q368.** Which of the following best explains why fiber optic cables have a lower bit error rate than copper cables?
*Fiber optic cables की copper cables की तुलना में कम bit error rate की सबसे अच्छी व्याख्या कौन-सी है?*
- **(A)** Higher signal power
- **(B)** Immunity to electromagnetic interference
- **(C)** Simpler modulation techniques
- **(D)** Larger physical size
✔ **(B) Immunity to electromagnetic interference**
★ **Nukta:** Fiber wins on: EMI immunity, low attenuation, huge bandwidth, tap security.
*Fiber में श्रेष्ठता: EMI immunity, कम attenuation, विशाल bandwidth, tap security।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q369.** Which transmission medium works on the principle of total internal reflection?
*कौन-सा transmission medium total internal reflection के सिद्धांत पर काम करता है?*
- **(A)** Optical fiber cable
- **(B)** Shielded twisted pair
- **(C)** Unshielded twisted pair
- **(D)** Coaxial cable
✔ **(A) Optical fiber cable**
★ **Nukta:** Fiber = TIR. Copper media use electrical signals (electromagnetic fields), not light reflection.
*Fiber = TIR। Copper media electrical signals (electromagnetic fields) उपयोग करते हैं, प्रकाश reflection नहीं।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q370.** Crosstalk in twisted pair cables is typically minimised by:
*Twisted pair cables में crosstalk आमतौर पर किससे कम होता है?*
- **(A)** Increasing the power level
- **(B)** Increasing the twist rate
- **(C)** Adding shielding to the core
- **(D)** Using longer cables
✔ **(B) Increasing the twist rate**
★ **Nukta:** Anti-crosstalk tricks: tighter twists, pair separation, shielding (STP), lower power.
*Anti-crosstalk tricks: tighter twists, pair separation, shielding (STP), कम power।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q371.** Which connector is commonly used for coaxial cable in physical networks?
*Physical networks में coaxial cable के लिए सामान्यतः कौन-सा connector उपयोग होता है?*
- **(A)** RJ-45
- **(B)** USB-C
- **(C)** BNC
- **(D)** HDMI
✔ **(C) BNC**
★ **Nukta:** Connectors: RJ-45 (UTP Ethernet), BNC (coax/Thinnet), SC/ST/LC (fiber), RJ-11 (telephone).
*Connectors: RJ-45 (UTP Ethernet), BNC (coax/Thinnet), SC/ST/LC (fiber), RJ-11 (telephone)।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q372.** Which transmission medium is best for a network exposed to heavy electrical interference?
*भारी electrical interference वाले network के लिए कौन-सा transmission medium सर्वोत्तम है?*
- **(A)** Unshielded twisted pair
- **(B)** Optical fiber
- **(C)** Coaxial cable
- **(D)** Microwave
✔ **(B) Optical fiber**
★ **Nukta:** EMI-heavy areas (factories, power plants) → fiber. 'Immune to EMI' = keyword for fiber.
*EMI-भारी क्षेत्र (कारखाने, power plants) → fiber। 'Immune to EMI' = fiber के लिए keyword।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Medium*

**Q373.** Which of the following CANNOT be used as a medium for 802.3 Ethernet?
*निम्न में से कौन-सा 802.3 Ethernet के लिए medium उपयोग नहीं किया जा सकता?*
- **(A)** Thin coaxial cable
- **(B)** Twisted pair cable
- **(C)** Microwave link
- **(D)** Fiber optic cable
✔ **(C) Microwave link**
★ **Nukta:** 802.3 = Ethernet (wired: 10Base2/5, 10Base-T, 100Base-TX, 1000Base-X...). 802.11 = Wi-Fi (wireless).
*802.3 = Ethernet (wired: 10Base2/5, 10Base-T, 100Base-TX, 1000Base-X...)। 802.11 = Wi-Fi (wireless)।*
*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Medium*

**Q374.** What is the typical maximum length of a UTP cable in Ethernet before signal degradation?
*Signal degradation से पहले Ethernet में UTP cable की सामान्य अधिकतम लंबाई कितनी होती है?*
- **(A)** 50 meters
- **(B)** 100 meters
- **(C)** 150 meters
- **(D)** 200 meters
✔ **(B) 100 meters**
★ **Nukta:** Copper distance limits: UTP Ethernet 100 m, Thinnet 185 m, Thicknet 500 m, Fiber (multi-mode) ~550 m-2 km, (single-mode) tens of km.
*Copper distance limits: UTP Ethernet 100 m, Thinnet 185 m, Thicknet 500 m, Fiber (multi-mode) ~550 m-2 km, (single-mode) दसियों km।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

**Q375.** Which of the following is NOT a type of transmission medium?
*निम्न में से कौन-सा transmission medium का प्रकार नहीं है?*
- **(A)** Coaxial cable
- **(B)** Fiber optics
- **(C)** NIC
- **(D)** Twisted pair
✔ **(C) NIC**
★ **Nukta:** Media = guided (twisted pair, coax, fiber) + unguided (radio, microwave, satellite, infrared). NIC = adapter.
*Media = guided (twisted pair, coax, fiber) + unguided (radio, microwave, satellite, infrared)। NIC = adapter।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

## Section C — Unguided Media (Wireless)

*Wi-Fi standards, infrared/microwave/Bluetooth, line-of-sight, CDMA sharing and its true/false statements.*

**Unguided media = wireless: radio, microwave, infrared, satellite — air mein signals.**

*Unguided media = wireless: radio, microwave, infrared, satellite।*

- Radio waves — omnidirectional, buildings se guzar sakte hain; AM/FM, wireless LAN.
  - *Radio waves — omnidirectional, दीवारों से गुज़र सकते हैं।*
- Microwave — unidirectional, line-of-sight (towers beech 50 km); satellite = space ka microwave repeater (geostationary 36,000 km).
  - *Microwave — line-of-sight; satellite = अंतरिक्ष का repeater (36,000 km)।*
- Infrared — short range, walls se block ho jata hai (remote controls).
  - *Infrared — कम दूरी, दीवारों से रुक जाता है।*
- Bluetooth (IEEE 802.15) — PAN, 2.4 GHz, ~10 m; Zigbee — low power IoT.
  - *Bluetooth (802.15) — PAN, 2.4 GHz।*
- Wi-Fi (IEEE 802.11): a = 5 GHz/54 Mbps; b = 2.4/11; g = 2.4/54; n = 2.4+5/600 (MIMO); ac = 5 GHz/1+ Gbps; ax = Wi-Fi 6.
  - *Wi-Fi (802.11): a/b/g/n/ac/ax — 2.4 और 5 GHz bands।*
- Wireless sharing: FDMA, TDMA, CDMA — ek channel par kai users alag tareekon se.
  - *Wireless sharing: FDMA, TDMA, CDMA।*
- Wireless mein CSMA/CD kaam nahi karta (collision detect mushkil) — CSMA/CA use hota hai (Topic 6 mein).
  - *Wireless में CSMA/CD नहीं — CSMA/CA (Topic 6)।*

| Wireless Type | Range/Feature |
|---|---|
| Radio | omnidirectional, buildings se guzarta hai |
| Microwave | line-of-sight, towers ~50 km |
| Satellite | geostationary 36,000 km — long distance |
| Infrared | short range, walls block |
| Bluetooth | PAN, ~10 m, 2.4 GHz |

### Questions (Easy → Medium → Hard)

**Q376.** Which of the following is a wireless networking technology?
*निम्न में से कौन-सी wireless networking technology है?*
- **(A)** Ethernet
- **(B)** Wi-Fi
- **(C)** Fiber Optic
- **(D)** DSL
✔ **(B) Wi-Fi**
★ **Nukta:** Wireless family: Wi-Fi (802.11), Bluetooth (802.15), WiMAX (802.16), mobile (GSM/LTE/5G).
*Wireless family: Wi-Fi (802.11), Bluetooth (802.15), WiMAX (802.16), mobile (GSM/LTE/5G)।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q377.** Which wireless standard provides the highest data rate?
*कौन-सा wireless standard सर्वोच्च data rate देता है?*
- **(A)** 802.11b
- **(B)** 802.11g
- **(C)** 802.11n
- **(D)** 802.11ac
✔ **(D) 802.11ac**
★ **Nukta:** Wi-Fi rates: b = 11 Mbps, g = 54 Mbps, n = 600 Mbps, ac = multi-Gbps. Order: b < g < n < ac.
*Wi-Fi rates: b = 11 Mbps, g = 54 Mbps, n = 600 Mbps, ac = multi-Gbps। क्रम: b < g < n < ac।*
*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

**Q378.** Which type of wireless transmission requires line-of-sight?
*किस प्रकार की wireless transmission के लिए line-of-sight आवश्यक है?*
- **(A)** Wi-Fi
- **(B)** Infrared
- **(C)** Radio
- **(D)** Bluetooth
✔ **(B) Infrared**
★ **Nukta:** IR = line-of-sight (TV remotes, IrDA). Radio/RF (Wi-Fi, Bluetooth) passes through walls (with loss).
*IR = line-of-sight (TV remotes, IrDA)। Radio/RF (Wi-Fi, Bluetooth) दीवारों से गुजरते हैं (loss के साथ)।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q379.** Which transmission medium is used in Bluetooth technology?
*Bluetooth technology में कौन-सा transmission medium उपयोग होता है?*
- **(A)** Radio links
- **(B)** Microwave links
- **(C)** VSAT communication
- **(D)** Fiber optic
✔ **(A) Radio links**
★ **Nukta:** Bluetooth = 2.4 GHz radio, WPAN (802.15), ~10-100 m range, frequency hopping.
*Bluetooth = 2.4 GHz radio, WPAN (802.15), ~10-100 m range, frequency hopping।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q380.** Which physical-layer technique allows multiple users to share the same bandwidth simultaneously?
*कौन-सी physical-layer technique कई users को एक ही bandwidth साथ-साथ share करने देती है?*
- **(A)** TDMA
- **(B)** FDMA
- **(C)** CDMA
- **(D)** ARQ
✔ **(C) CDMA**
★ **Nukta:** Sharing methods: FDMA = frequency bands, TDMA = time slots, CDMA = codes (same band+time).
*Sharing methods: FDMA = frequency bands, TDMA = time slots, CDMA = codes (same band+time)।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

**Q381.** Which of the following statements is NOT true about microwaves?
*Microwaves के बारे में निम्न में से कौन-सा कथन सही नहीं है?*
- **(A)** They are electromagnetic waves with frequencies from 300 GHz to 400 THz
- **(B)** Propagation is line-of-sight
- **(C)** Very high-frequency waves cannot penetrate walls
- **(D)** Use of certain portions of the band requires permission from authorities
✔ **(A) They are electromagnetic waves with frequencies from 300 GHz to 400 THz**
★ **Nukta:** Microwaves: 300 MHz-300 GHz, line-of-sight, no wall penetration, licensed bands. Exam asks the odd range out.
*Microwaves: 300 MHz-300 GHz, line-of-sight, दीवार नहीं भेदते, licensed bands। Exam गलत range पूछता है।*
*[Source: Repo: CN Topic Test-04 (UNIT TEST-4) — options cleaned from source] · Hard*

**Q382.** Select the FALSE statement about CDMA technology: I. CDMA optimises the use of available bandwidth as it transmits over the entire frequency range. II. Each user in a CDMA system uses a different code to modulate their signal. III. CDMA offers less security compared to GSM technology. IV. A SIM card is always required for a CDMA device to work.
*CDMA technology के बारे में गलत कथन चुनिए: I. CDMA उपलब्ध bandwidth के उपयोग को अनुकूलित करता है क्योंकि यह पूरी frequency range पर transmit करता है। II. CDMA system में हर user अपने signal को modulate करने के लिए अलग code उपयोग करता है। III. CDMA, GSM की तुलना में कम security देता है। IV. CDMA device के काम करने के लिए SIM card हमेशा आवश्यक है।*
- **(A)** Only (I)
- **(B)** Only (II)
- **(C)** (I) and (II)
- **(D)** (III) and (IV)
✔ **(D) (III) and (IV)**
★ **Nukta:** Rajasthan PYQ verified key (D). True: I (spread over full band) and II (unique codes per user). False: III (CDMA more secure) and IV (SIM not mandatory).
*Rajasthan PYQ verified key (D)। सही: I (पूरे band पर spread) और II (हर user का unique code)। गलत: III (CDMA अधिक सुरक्षित) और IV (SIM अनिवार्य नहीं)।*
*[Source: Random Test- Rajasthan PYQ (OCR), p11 — Q83 (statements recovered from screenshot)] · Hard*

# TOPIC 6 — OSI Layers in Detail

## Section A — Data Link Layer: Flow & Error Control

*LLC/MAC sub-layers, flow control, ARQ protocols (Stop-and-Wait, Go-Back-N, Selective Repeat), error detection & correction (parity, CRC, checksum, Hamming) — basic to advanced.*

**Data link layer do sub-layers mein banti hai — LLC aur MAC; is layer par flow control aur error control ke protocols lagte hain.**

*Data link layer दो sub-layers में बँटती है — LLC और MAC; इस layer पर flow control और error control के protocols लगते हैं।*

- LLC (Logical Link Control) — upper layers ke saath interface, flow control; MAC (Media Access Control) — medium access + physical addressing.
  - *LLC — upper layers का interface, flow control; MAC — medium access + MAC addressing।*
- Flow control = receiver ki capacity ke hisaab se data bhejna: Stop-and-Wait (ek frame, phir ACK) aur Sliding Window (kai frames ek saath).
  - *Flow control = receiver की क्षमता के अनुसार: Stop-and-Wait और Sliding Window।*
- ARQ protocols: Stop-and-Wait ARQ; Go-Back-N (n tak frames, error par sab dobara); Selective Repeat (sirf galat frame dobara).
  - *ARQ: Stop-and-Wait; Go-Back-N (सब दोबारा); Selective Repeat (सिर्फ़ ग़लत)।*
- Error detection: Parity bit (single bit check), CRC (polynomial division — best), Internet checksum.
  - *Error detection: Parity, CRC (polynomial division), checksum।*
- Error correction: Hamming code (Hamming distance ≥ 3 for single-bit error); FEC (forward error correction) vs ARQ.
  - *Error correction: Hamming code; FEC vs ARQ।*
- Hamming distance = do codewords mein alag bits ki sankhya; error detect ke liye d ≥ e+1, correct ke liye d ≥ 2e+1.
  - *Hamming distance = भिन्न bits की संख्या; detect: d ≥ e+1; correct: d ≥ 2e+1।*
- CRC: generator polynomial G(x) se data ko divide karna; remainder = CRC bits; receiver phir se divide karke remainder 0 dekhta hai.
  - *CRC: G(x) से भाग; remainder = CRC bits; receiver में remainder 0 आना चाहिए।*
- CRC x+1 factor hone par error detect hota hai (odd-bit conditions) — GATE ka classic.
  - *CRC x+1 factor पर error detect — GATE का क्लासिक।*

| Protocol | Window | Error par kya hota hai |
|---|---|---|
| Stop-and-Wait | 1 frame | wahi frame dobara |
| Go-Back-N | n frames | error se aage ke sab dobara |
| Selective Repeat | n frames | sirf galat frame dobara |

### Questions (Easy → Medium → Hard)

**Q383.** Which sub-layer of the Data Link Layer is responsible for flow control and error control?
*Data Link Layer का कौन-सा sub-layer flow control और error control के लिए ज़िम्मेदार होता है?*
- **(A)** MAC
- **(B)** LLC (Logical Link Control)
- **(C)** PVC
- **(D)** None of the above
✔ **(B) LLC (Logical Link Control)**
★ **Nukta:** DLL = MAC + LLC — याद रखो: MAC = addressing + medium access, LLC = flow + error + interface.
*DLL = MAC + LLC — याद रखो: MAC = addressing + medium access, LLC = flow + error + interface.*
*[Source: BCI Subject Test-8.pdf] · Easy*

**Q384.** Which of the following functions are performed by the Data Link Layer? (1) Framing (2) Error Detection (3) Flow Control (4) Path Determination
*निम्न में से कौन-से कार्य Data Link Layer करता है? (1) Framing (2) Error Detection (3) Flow Control (4) Path Determination*
- **(A)** 1, 2 and 3 only
- **(B)** 1 and 4 only
- **(C)** 2 and 4 only
- **(D)** 1, 2, 3 and 4
✔ **(A) 1, 2 and 3 only**
★ **Nukta:** याद रखो: DLL में F-E-F (Framing, Error, Flow) + addressing; रास्ता चुनना (routing) Network Layer का.
*याद रखो: DLL में F-E-F (Framing, Error, Flow) + addressing; रास्ता चुनना (routing) Network Layer का.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q385.** The Frame Check Sequence (FCS) field in an Ethernet frame is used for:
*Ethernet frame में Frame Check Sequence (FCS) field किस काम आता है?*
- **(A)** Flow control
- **(B)** Address resolution
- **(C)** Error detection using CRC
- **(D)** Medium access
✔ **(C) Error detection using CRC**
★ **Nukta:** FCS = CRC = error detection. Ethernet error correct नहीं करता, बस detect करके frame drop करता है.
*FCS = CRC = error detection. Ethernet error correct नहीं करता, बस detect करके frame drop करता है.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q386.** A Stop-and-Wait ARQ channel has high latency and large bandwidth. What problem occurs?
*Stop-and-Wait ARQ channel पर latency ज़्यादा और bandwidth बड़ी हो तो क्या समस्या होती है?*
- **(A)** High throughput
- **(B)** Low channel utilization
- **(C)** CRC failure
- **(D)** Frame duplication
✔ **(B) Low channel utilization**
★ **Nukta:** Bandwidth × Delay (BDP) जितना बड़ा, Stop-and-Wait उतना बेकार.
*Bandwidth × Delay (BDP) जितना बड़ा, Stop-and-Wait उतना बेकार.*
*[Source: BCI Subject Test-8.pdf] · Easy*

**Q387.** A Go-Back-N sender uses window size 4. Frame 2 is lost. What happens after the receiver receives frames 3 and 4?
*Go-Back-N sender window size 4 उपयोग करता है. Frame 2 खो जाता है. Receiver को frames 3 और 4 मिलने के बाद क्या होता है?*
- **(A)** Receiver stores frames 3 and 4 in buffer
- **(B)** Receiver sends ACK for frame 4
- **(C)** Receiver discards frames 3 and 4
- **(D)** Receiver acts like Selective Repeat
✔ **(C) Receiver discards frames 3 and 4**
★ **Nukta:** GBN receiver dumb होता है (buffer नहीं रखता); SR receiver smart (buffer रखता है).
*GBN receiver dumb होता है (buffer नहीं रखता); SR receiver smart (buffer रखता है).*
*[Source: BCI Subject Test-8.pdf] · Easy*

**Q388.** A noisy channel uses a Hamming code with minimum distance 3. What can it guarantee?
*एक noisy channel पर minimum distance 3 वाला Hamming code क्या guarantee दे सकता है?*
- **(A)** Detect 2-bit errors
- **(B)** Correct 2-bit errors
- **(C)** Correct 3-bit errors
- **(D)** Detect 4-bit errors
✔ **(A) Detect 2-bit errors**
★ **Nukta:** d=3 → detect 2 या correct 1 — 'correct 2' के लिए d ≥ 5 चाहिए.
*d=3 → detect 2 या correct 1 — 'correct 2' के लिए d ≥ 5 चाहिए.*
*[Source: BCI Subject Test-8.pdf] · Easy*

**Q389.** Which of the following verifies the integrity of a message?
*निम्न में से कौन-सा message की integrity जाँचता है?*
- **(A)** Message Encryption
- **(B)** Message Checksum
- **(C)** Message Digest
- **(D)** None of these
✔ **(C) Message Digest**
★ **Nukta:** Digest = अंगूठा-छाप; Encryption = गोपनीयता, integrity नहीं.
*Digest = अंगूठा-छाप; Encryption = गोपनीयता, integrity नहीं.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q390.** Which of the following statements about MAC and LLC sublayers is TRUE? (1) MAC sublayer handles physical addressing (2) LLC sublayer provides error control and flow control (3) MAC sublayer performs routing
*MAC और LLC sub-layers के बारे में कौन-सा कथन सही है? (1) MAC sub-layer physical addressing संभालता है (2) LLC sub-layer error control और flow control देता है (3) MAC sub-layer routing करता है*
- **(A)** 1 and 2 only
- **(B)** 2 and 3 only
- **(C)** 1 and 3 only
- **(D)** 1, 2 and 3
✔ **(A) 1 and 2 only**
★ **Nukta:** MAC = addressing + channel access; LLC = flow + error + interface; routing = Network Layer.
*MAC = addressing + channel access; LLC = flow + error + interface; routing = Network Layer.*
*[Source: BCI Subject Test-9.pdf] · Medium*

**Q391.** Which of the following is NOT a responsibility of the LLC sublayer?
*निम्न में से कौन-सा LLC sub-layer की ज़िम्मेदारी नहीं है?*
- **(A)** Flow control
- **(B)** Error control
- **(C)** Service interface to Network layer
- **(D)** Physical addressing
✔ **(D) Physical addressing**
★ **Nukta:** MAC = Media Access Control = addressing; LLC = Logical Link Control = flow/error.
*MAC = Media Access Control = addressing; LLC = Logical Link Control = flow/error.*
*[Source: BCI Subject Test-9.pdf] · Medium*

**Q392.** Which of the following is NOT a function of the Data Link Layer?
*निम्न में से कौन-सा Data Link Layer का function नहीं है?*
- **(A)** Framing
- **(B)** Error detection
- **(C)** Error correction
- **(D)** Routing
✔ **(D) Routing**
★ **Nukta:** DLL = next-hop delivery (frame); Network = end-to-end delivery (packet + route).
*DLL = next-hop delivery (frame); Network = end-to-end delivery (packet + route).*
*[Source: BCI Subject Test-9.pdf + CN Topic Test-04.pdf] · Medium*

**Q393.** Error control is the process of detecting and correcting errors, while ______ is a mechanism to ensure the efficient delivery of data.
*Error control, errors को detect और correct करने की प्रक्रिया है, जबकि ______ data के कुशल delivery का mechanism है.*
- **(A)** Error control, Flow control
- **(B)** Process control, Network control
- **(C)** Session control, Flow control
- **(D)** OSI Control, Data control
✔ **(A) Error control, Flow control**
★ **Nukta:** Error = putting right; Flow = maintaining balance. Both are separate jobs.
*Error = सही करना; Flow = संतुलन बनाना. दोनों अलग-अलग काम हैं.*
*[Source: CN Topic Test-02.pdf] · Medium*

**Q394.** ______ control refers to a set of procedures used to restrict the amount of data that the sender can send before waiting for acknowledgment.
*______ control उन procedures का समूह है जो sender द्वारा acknowledgment की प्रतीक्षा से पहले भेजे जाने वाले data की मात्रा सीमित करते हैं.*
- **(A)** Flow
- **(B)** Error
- **(C)** Transmission
- **(D)** Access control
✔ **(A) Flow**
★ **Nukta:** Flow control = the balance between sender and receiver; this definition is asked again and again in exams.
*Flow control = sender↔receiver के बीच का संतुलन; यही definition परीक्षा में बार-बार आती है.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p17] · Medium*

**Q395.** What is the main purpose of the Sliding Window in TCP?
*TCP में Sliding Window का मुख्य उद्देश्य क्या है?*
- **(A)** Address resolution
- **(B)** Flow control
- **(C)** Error detection
- **(D)** Encryption
✔ **(B) Flow control**
★ **Nukta:** TCP window = receiver की capacity का advertisement; इसीलिए इसे flow control कहते हैं.
*TCP window = receiver की capacity का advertisement; इसीलिए इसे flow control कहते हैं.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q396.** Flow control prevents which of the following issues?
*Flow control निम्न में से किस समस्या को रोकता है?*
- **(A)** Deadlock
- **(B)** Congestion collapse
- **(C)** Overflow of the receiver's buffer
- **(D)** Packet routing error
✔ **(C) Overflow of the receiver's buffer**
★ **Nukta:** Flow control = दोनों के बीच; Congestion control = पूरे network के लिए.
*Flow control = दोनों के बीच; Congestion control = पूरे network के लिए.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q397.** In Stop-and-Wait ARQ, after sending one frame, the sender:
*Stop-and-Wait ARQ में एक frame भेजने के बाद sender:*
- **(A)** Waits for acknowledgment
- **(B)** Sends the next frame immediately
- **(C)** Stops transmission permanently
- **(D)** Sends a NAK
✔ **(A) Waits for acknowledgment**
★ **Nukta:** Because of this waiting, its name became 'Stop-and-Wait'.
*इसी waiting के कारण इसका नाम 'Stop-and-Wait' पड़ा.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q398.** In Stop-and-Wait protocol, the sender sends:
*Stop-and-Wait protocol में sender भेजता है:*
- **(A)** Multiple frames at once
- **(B)** One frame at a time
- **(C)** Acknowledgments only
- **(D)** Data without waiting
✔ **(B) One frame at a time**
★ **Nukta:** Window size = 1 — इसीलिए एक-एक frame.
*Window size = 1 — इसीलिए एक-एक frame.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q399.** What is the window size in Stop-and-Wait ARQ?
*Stop-and-Wait ARQ में window size कितनी होती है?*
- **(A)** 0
- **(B)** 1
- **(C)** N
- **(D)** 2
✔ **(B) 1**
★ **Nukta:** Window = 1 ↔ एक frame at a time — दोनों एक ही बात हैं.
*Window = 1 ↔ एक frame at a time — दोनों एक ही बात हैं.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q400.** What is the main disadvantage of Stop-and-Wait flow control?
*Stop-and-Wait flow control की मुख्य कमी क्या है?*
- **(A)** Complexity
- **(B)** Low efficiency due to waiting
- **(C)** High memory usage
- **(D)** Frame loss
✔ **(B) Low efficiency due to waiting**
★ **Nukta:** Waiting = idle time = कम utilization. इसीलिए Sliding Window आया.
*Waiting = idle time = कम utilization. इसीलिए Sliding Window आया.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q401.** In Stop-and-Wait ARQ, what happens when a frame is lost?
*Stop-and-Wait ARQ में frame खो जाए तो क्या होता है?*
- **(A)** Receiver sends NAK
- **(B)** Sender retransmits after timeout
- **(C)** Receiver retransmits
- **(D)** No retransmission
✔ **(B) Sender retransmits after timeout**
★ **Nukta:** Lost frame + timeout = retransmission. Receiver कभी retransmit नहीं करता.
*Lost frame + timeout = retransmission. Receiver कभी retransmit नहीं करता.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q402.** In Go-Back-N ARQ, if an error is detected in a frame:
*Go-Back-N ARQ में किसी frame में error मिले तो:*
- **(A)** Only that frame is retransmitted
- **(B)** All frames are ignored
- **(C)** That frame and all subsequent outstanding frames are retransmitted
- **(D)** No frame is retransmitted
✔ **(C) That frame and all subsequent outstanding frames are retransmitted**
★ **Nukta:** GBN = 'from where you slipped, start again' — in Selective Repeat only the wrong frame is resent.
*GBN = 'जहाँ चूक, वहाँ से फिर से' — Selective Repeat में सिर्फ गलत frame दोबारा जाता है.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q403.** In a Go-Back-N protocol, if the window size = 63, how many sequence number bits are required?
*Go-Back-N protocol में window size = 63 हो तो sequence number के कितने bits चाहिए?*
- **(A)** 5
- **(B)** 6
- **(C)** 7
- **(D)** 8
✔ **(B) 6**
★ **Nukta:** The reverse of the question above — memorise the formula both ways.
*उपर वाले प्रश्न का उल्टा — यही formula दोनों तरफ से याद रखो.*
*[Source: BCI Subject Test-8.pdf] · Medium*

**Q404.** A Selective Repeat sliding window protocol uses a window size of 7 with 3-bit sequence numbers. Is it valid?
*Selective Repeat sliding window protocol में 3-bit sequence numbers के साथ window size 7 क्या वैध है?*
- **(A)** Valid
- **(B)** Invalid – violates the maximum window rule
- **(C)** Valid only for piggybacking
- **(D)** Valid only with Selective Repeat
✔ **(B) Invalid – violates the maximum window rule**
★ **Nukta:** SR window ≤ 2ⁿ⁻¹; GBN window ≤ 2ⁿ − 1. यही फ़र्क याद रखो.
*SR window ≤ 2ⁿ⁻¹; GBN window ≤ 2ⁿ − 1. यही फ़र्क याद रखो.*
*[Source: BCI Subject Test-8.pdf] · Medium*

**Q405.** Which protocol has better bandwidth utilization?
*किस protocol का bandwidth utilization बेहतर होता है?*
- **(A)** Stop-and-Wait
- **(B)** Selective Repeat
- **(C)** Go-Back-N
- **(D)** None of the above
✔ **(B) Selective Repeat**
★ **Nukta:** Efficiency क्रम: Selective Repeat > Go-Back-N > Stop-and-Wait.
*Efficiency क्रम: Selective Repeat > Go-Back-N > Stop-and-Wait.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q406.** What is the Hamming distance between the two codes 10010010 and 11011001?
*दो codes 10010010 और 11011001 के बीच Hamming distance कितनी है?*
- **(A)** 3
- **(B)** 4
- **(C)** 6
- **(D)** 2
✔ **(B) 4**
★ **Nukta:** Hamming distance = XOR के बाद 1s की गिनती.
*Hamming distance = XOR के बाद 1s की गिनती.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p28] · Medium*

**Q407.** The Hamming distance between two code words can easily be found if we apply the ______ operation.
*दो code words के बीच Hamming distance आसानी से मिल जाती है यदि हम ______ operation लगाएँ.*
- **(A)** XOR
- **(B)** XNOR
- **(C)** OR
- **(D)** AND
✔ **(A) XOR**
★ **Nukta:** XOR = difference counter. दूसरे operations यह नहीं बताते.
*XOR = difference counter. दूसरे operations यह नहीं बताते.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p35] · Medium*

**Q408.** To detect or correct errors, we send extra bits with the data. These extra bits are called:
*Errors detect या correct करने के लिए data के साथ भेजे गए अतिरिक्त bits कहलाते हैं:*
- **(A)** redundancy
- **(B)** correction
- **(C)** detection
- **(D)** parity
✔ **(A) redundancy**
★ **Nukta:** Redundancy = 'extra bits sent on purpose' — this is what makes error control possible.
*Redundancy = 'जान-बूझकर भेजा अतिरिक्त' — इसी से error control संभव है.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p36] · Medium*

**Q409.** Which error detection method uses one extra bit added to the end of a byte?
*कौन-सी error detection method में byte के अंत में एक अतिरिक्त bit जोड़ी जाती है?*
- **(A)** CRC
- **(B)** Checksum
- **(C)** Hamming code
- **(D)** Parity bit
✔ **(D) Parity bit**
★ **Nukta:** Parity = 1 bit; CRC = पूरा remainder; Checksum = योग; Hamming = कई parity bits.
*Parity = 1 bit; CRC = पूरा remainder; Checksum = योग; Hamming = कई parity bits.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q410.** Which error detection method consists of a parity bit for each data unit as well as an entire data unit of parity bits?
*किस error detection method में हर data unit के लिए एक parity bit के साथ-साथ parity bits का पूरा data unit भी होता है?*
- **(A)** Simple parity check
- **(B)** CRC
- **(C)** Two-dimensional parity check
- **(D)** Checksum
✔ **(C) Two-dimensional parity check**
★ **Nukta:** 2D parity = rows + columns दोनों की parity; simple parity = बस एक bit.
*2D parity = rows + columns दोनों की parity; simple parity = बस एक bit.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p7] · Medium*

**Q411.** A simple parity-check code can detect:
*एक simple parity-check code detect कर सकता है:*
- **(A)** odd number of errors
- **(B)** even number of errors
- **(C)** positive number of errors
- **(D)** negative number of errors
✔ **(A) odd number of errors**
★ **Nukta:** Parity catches odd errors and misses even ones — that is its limit.
*Parity = odd errors पकड़ता है; even छोड़ देता है — यही इसकी सीमा है.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p34] · Medium*

**Q412.** Which of the following is an error detection technique?
*निम्न में से कौन-सी error detection technique है?*
- **(A)** ARQ
- **(B)** Parity Bit
- **(C)** Stop-and-Wait
- **(D)** Sliding Window
✔ **(B) Parity Bit**
★ **Nukta:** Detection techniques: Parity, CRC, Checksum. Control protocols: SW, GBN, SR.
*Detection techniques: Parity, CRC, Checksum. Control protocols: SW, GBN, SR.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q413.** High-level Data Link Control (HDLC) is a protocol for communication over point-to-point and multipoint links. HDLC is a ______ protocol.
*High-level Data Link Control (HDLC) point-to-point और multipoint links पर communication का protocol है. HDLC एक ______ protocol है.*
- **(A)** byte-oriented
- **(B)** character-oriented
- **(C)** bit-oriented
- **(D)** none of the above
✔ **(C) bit-oriented**
★ **Nukta:** HDLC/SDLC = bit-oriented; PPP = byte-oriented. यह जोड़ी याद रखो.
*HDLC/SDLC = bit-oriented; PPP = byte-oriented. यह जोड़ी याद रखो.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p15] · Medium*

**Q414.** The most common protocol for point-to-point access is the Point-to-Point Protocol (PPP), which is a ______ protocol.
*Point-to-point access का सबसे सामान्य protocol Point-to-Point Protocol (PPP) है, जो एक ______ protocol है.*
- **(A)** bit-oriented
- **(B)** byte-oriented
- **(C)** character-oriented
- **(D)** none of the above
✔ **(B) byte-oriented**
★ **Nukta:** PPP = byte-oriented (flag = 0x7E); HDLC = bit-oriented. परीक्षा में यह जोड़ी कई बार आ चुकी है.
*PPP = byte-oriented (flag = 0x7E); HDLC = bit-oriented. परीक्षा में यह जोड़ी कई बार आ चुकी है.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p16] · Medium*

**Q415.** Which protocol allows the sender to transmit multiple frames before needing an acknowledgment?
*कौन-सा protocol sender को acknowledgment की ज़रूरत से पहले कई frames भेजने देता है?*
- **(A)** Stop-and-Wait
- **(B)** Go-Back-N
- **(C)** ALOHA
- **(D)** CSMA/CD
✔ **(B) Go-Back-N**
★ **Nukta:** Sliding window = कई outstanding frames; Stop-and-Wait = एक.
*Sliding window = कई outstanding frames; Stop-and-Wait = एक.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q416.** Which of the following techniques uses both acknowledgments and sequence numbers?
*निम्न में से कौन-सी technique acknowledgments और sequence numbers दोनों उपयोग करती है?*
- **(A)** Go-Back-N
- **(B)** Stop-and-Wait
- **(C)** Selective Repeat
- **(D)** All of the above
✔ **(D) All of the above**
★ **Nukta:** ARQ = Automatic Repeat reQuest — बिना sequence/ack के कोई ARQ चल ही नहीं सकता.
*ARQ = Automatic Repeat reQuest — बिना sequence/ack के कोई ARQ चल ही नहीं सकता.*
*[Source: Unit Test -2 Solutions.pdf (OCR) + CN Topic Test-04.pdf] · Hard*

**Q417.** In the TCP header, the acknowledgment field value represents:
*TCP header में acknowledgment field का मान किसे दर्शाता है?*
- **(A)** Number of previous bytes received
- **(B)** Total number of bytes to receive
- **(C)** Sequence number of the next byte expected
- **(D)** Sequence of zeros and ones
✔ **(C) Sequence number of the next byte expected**
★ **Nukta:** TCP bytes गिनता है, packets नहीं — ACK = 'next byte भेजो'.
*TCP bytes गिनता है, packets नहीं — ACK = 'next byte भेजो'.*
*[Source: CN Topic Test-04.pdf] · Hard*

**Q418.** For Stop-and-Wait ARQ, for 10 data packets sent, ............ acknowledgements are needed.
*Stop-and-Wait ARQ में 10 data packets भेजने पर ............ acknowledgements चाहिए होते हैं.*
- **(A)** 9
- **(B)** 20
- **(C)** 11
- **(D)** 10
✔ **(D) 10**
★ **Nukta:** RPSC official key (d) — Stop-and-Wait में ack:packet अनुपात 1:1.
*RPSC official key (d) — Stop-and-Wait में ack:packet अनुपात 1:1.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q419.** In the ______ protocol, if no acknowledgment for a frame has arrived, we resend all outstanding frames.
*______ protocol में, किसी frame का acknowledgment न आए तो हम सभी outstanding frames दोबारा भेजते हैं.*
- **(A)** Stop-and-Wait ARQ
- **(B)** Go-Back-N ARQ
- **(C)** Selective-Repeat ARQ
- **(D)** Both B and C
✔ **(B) Go-Back-N ARQ**
★ **Nukta:** GBN = Go Back N — everything up to N is resent; SR = only the wrong one.
*GBN = Go Back N — Nवें तक सब दोबारा; SR = सिर्फ गलत वाला.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p8] · Hard*

**Q420.** In Go-Back-N ARQ, if 6 is the number of bits for the sequence number, then the maximum size of the send window must be:
*Go-Back-N ARQ में sequence number के 6 bits हों तो send window का अधिकतम आकार कितना होगा?*
- **(A)** 63
- **(B)** 61
- **(C)** 31
- **(D)** 64
✔ **(A) 63**
★ **Nukta:** GBN/SW का window formula अलग है SR से — GBN: 2ⁿ−1, SR: 2ⁿ⁻¹.
*GBN/SW का window formula अलग है SR से — GBN: 2ⁿ−1, SR: 2ⁿ⁻¹.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p9] · Hard*

**Q421.** The maximum number of outstanding frames in Selective Repeat (with N sequence numbers) is:
*Selective Repeat में outstanding frames की अधिकतम संख्या (N sequence numbers के साथ) होती है:*
- **(A)** N
- **(B)** N − 1
- **(C)** N/2
- **(D)** 2N
✔ **(C) N/2**
★ **Nukta:** SR: window N/2 (दो windows), GBN: window N−1 (एक window).
*SR: window N/2 (दो windows), GBN: window N−1 (एक window).*
*[Source: CN Topic Test-04.pdf] · Hard*

**Q422.** Any coding scheme for error control needs to have at least the parameters of:
*Error control के लिए किसी भी coding scheme में कम से कम निम्न parameters होने चाहिए:*
- **(A)** codeword size
- **(B)** dataword size
- **(C)** minimum Hamming distance
- **(D)** All of them
✔ **(D) All of them**
★ **Nukta:** Code = (n, k, d) — n = codeword, k = dataword, d = distance. तीनों से ही code की ताक़त पता चलती है.
*Code = (n, k, d) — n = codeword, k = dataword, d = distance. तीनों से ही code की ताक़त पता चलती है.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p37] · Hard*

**Q423.** The message 1001 is to be transmitted using the CRC polynomial x³ + x + 1 to protect it from errors. The codeword that should be transmitted is:
*संदेश 1001 को CRC बहुपद x³ + x + 1 से errors से बचाने के लिए भेजना है. भेजा जाने वाला codeword होगा:*
- **(A)** 1001100
- **(B)** 1001011
- **(C)** 1001110
- **(D)** 1001000
✔ **(C) 1001110**
★ **Nukta:** CRC: degree n के polynomial पर n zeros append → भाग का remainder जोड़ो. यहाँ degree 3 → 3 zeros.
*CRC: degree n के polynomial पर n zeros append → भाग का remainder जोड़ो. यहाँ degree 3 → 3 zeros.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q424.** The checksum is used in the Internet by several protocols although not at the ______ layer.
*Internet में checksum कई protocols उपयोग करते हैं, हालाँकि ______ layer पर नहीं.*
- **(A)** data link
- **(B)** transport
- **(C)** network
- **(D)** none of the above
✔ **(A) data link**
★ **Nukta:** DLL = CRC; Network/Transport = checksum. यही फ़र्क पूछा जाता है.
*DLL = CRC; Network/Transport = checksum. यही फ़र्क पूछा जाता है.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p33] · Hard*

**Q425.** Which of the following is NOT a responsibility of the network layer?
*निम्न में से कौन-सा network layer की ज़िम्मेदारी नहीं है?*
- **(A)** Congestion control
- **(B)** Error control
- **(C)** Routing
- **(D)** Inter-networking
✔ **(B) Error control**
★ **Nukta:** Network layer = रास्ता + congestion; error control यहाँ नहीं.
*Network layer = रास्ता + congestion; error control यहाँ नहीं.*
*[Source: CN Topic Test-02.pdf] · Hard*

**Q426.** The types of data services offered by an LLC (Logical Link Control) layer are:
*LLC (Logical Link Control) layer द्वारा दी जाने वाली data services के प्रकार हैं:*
- **(A)** Connectionless (fast and unreliable)
- **(B)** Connection-oriented (slow and reliable)
- **(C)** Both A and B
- **(D)** None of the above
✔ **(C) Both A and B**
★ **Nukta:** LLC types: 1 (connectionless), 2 (connection-oriented), 3 (acknowledged connectionless).
*LLC types: 1 (connectionless), 2 (connection-oriented), 3 (acknowledged connectionless).*
*[Source: Unit Test -2 Solutions.pdf (OCR), p32] · Hard*

**Q427.** The message 11001001 is to be transmitted using the CRC polynomial x³ + 1 to protect it from errors. The codeword that should be transmitted is:
*संदेश 11001001 को CRC बहुपद x³ + 1 से errors से बचाने के लिए भेजना है. भेजा जाने वाला codeword होगा:*
- **(A)** 11001001000
- **(B)** 11001001011
- **(C)** 11001010
- **(D)** 110010010011
✔ **(B) 11001001011**
★ **Nukta:** GATE official key (B). यही तरीका RPSC के x³+x+1 वाले प्रश्न में भी — degree n पर n zeros, भाग का remainder जोड़ो.
*GATE official key (B). यही तरीका RPSC के x³+x+1 वाले प्रश्न में भी — degree n पर n zeros, भाग का remainder जोड़ो.*
*[Source: GATE CS 2007] · Hard*

**Q428.** Let G(x) be the generator polynomial used for CRC checking. What condition must G(x) satisfy to detect an odd number of bits in error?
*मान लीजिए G(x), CRC जाँच में उपयोग होने वाला generator polynomial है. Odd संख्या में बिट-त्रुटियाँ पकड़ने के लिए G(x) पर क्या शर्त होनी चाहिए?*
- **(A)** G(x) contains more than two terms
- **(B)** G(x) does not divide 1 + x^k for any k within the frame length
- **(C)** 1 + x is a factor of G(x)
- **(D)** G(x) has an odd number of terms
✔ **(C) 1 + x is a factor of G(x)**
★ **Nukta:** GATE official key (C). x+1 factor ↔ even parity code ↔ odd errors detect.
*GATE official key (C). x+1 factor ↔ even parity code ↔ odd errors detect.*
*[Source: GATE CS 2009] · Hard*

**Q429.** In CRC coding, if the data word is 111111, the divisor is 1010 and the remainder is 110, which of the following is the transmitted code?
*CRC coding में, यदि data word 111111 है, divisor 1010 है और remainder 110 है, तो निम्न में से कौन-सा भेजा गया code है?*
- **(A)** 011111101
- **(B)** 001010110
- **(C)** 111111110
- **(D)** 110111111
✔ **(C) 111111110**
★ **Nukta:** CRC में codeword = data के पीछे remainder. बाकी options remainder जोड़ने का हिसाब नहीं रखते.
*CRC में codeword = data के पीछे remainder. बाकी options remainder जोड़ने का हिसाब नहीं रखते.*
*[Source: UGC NET Computer Science Dec 2022 (via samagracs)] · Hard*

**Q430.** A 2 km long broadcast LAN has 10⁷ bps bandwidth and uses CSMA/CD. The signal travels along the wire at 2 × 10⁸ m/s. What is the minimum packet size that can be used on this network?
*एक 2 km लंबे broadcast LAN की bandwidth 10⁷ bps है और यह CSMA/CD उपयोग करता है. Signal तार में 2 × 10⁸ m/s से चलता है. इस network पर उपयोग होने वाला न्यूनतम packet आकार कितना है?*
- **(A)** 50 bytes
- **(B)** 100 bytes
- **(C)** 200 bytes
- **(D)** None of the above
✔ **(D) None of the above**
★ **Nukta:** GATE 2003 और RPSC 2011 दोनों का official key (D). याद रखो: min frame = 2 × propagation delay × bandwidth (round-trip).
*GATE 2003 और RPSC 2011 दोनों का official key (D). याद रखो: min frame = 2 × propagation delay × bandwidth (round-trip).*
*[Source: GATE CS 2003 + RPSC Programmer 2011 Paper-1 (via pyqp.in)] · Hard*

**Q431.** A network using CSMA/CD has a bandwidth of 20 Mbps. If the maximum propagation time is 25 µs, what is the minimum size of the frame?
*CSMA/CD उपयोग करने वाले network की bandwidth 20 Mbps है. यदि अधिकतम propagation time 25 µs हो, तो frame का न्यूनतम आकार क्या होगा?*
- **(A)** 500 bits
- **(B)** 1000 bits
- **(C)** 1500 bits
- **(D)** 2000 bits
✔ **(B) 1000 bits**
★ **Nukta:** UGC NET Jan 2025 key (ii). यही formula ऊपर वाले GATE प्रश्न में भी — बस units बदलो.
*UGC NET Jan 2025 key (ii). यही formula ऊपर वाले GATE प्रश्न में भी — बस units बदलो.*
*[Source: UGC NET Computer Science Jan 2025 (via samagracs solved paper)] · Hard*

**Q432.** A CSMA/CD network transmits data at 100 Mbps over a 1 km cable with no repeaters. If the minimum frame size required is 1250 bytes, what is the signal speed in the cable (in km/sec)?
*एक CSMA/CD network बिना repeaters के 1 km cable पर 100 Mbps से data भेजता है. यदि आवश्यक न्यूनतम frame आकार 1250 bytes हो, तो cable में signal की गति (km/sec में) कितनी है?*
- **(A)** 8000
- **(B)** 10000
- **(C)** 16000
- **(D)** 20000
✔ **(D) 20000**
★ **Nukta:** GATE 2015 key (d) 20000 km/s. Getting the speed by inverting the formula — that is the trick of this question.
*GATE 2015 key (d) 20000 km/s. Formula को उलटकर speed निकालना — यही इस प्रश्न का खेल है.*
*[Source: GATE CSE 2015 Set 3] · Hard*

**Q433.** In the starting phase (slow start) of the TCP congestion control algorithm, the congestion window size:
*TCP congestion control algorithm के शुरुआती चरण (slow start) में congestion window का आकार:*
- **(A)** Increases linearly
- **(B)** Does not increase
- **(C)** Increases exponentially
- **(D)** Remains constant at threshold
✔ **(C) Increases exponentially**
★ **Nukta:** GATE 2008 key: exponential. क्रम याद रखो: Slow start (exponential) → Congestion avoidance (linear).
*GATE 2008 key: exponential. क्रम याद रखो: Slow start (exponential) → Congestion avoidance (linear).*
*[Source: GATE CS 2008] · Hard*

**Q434.** Consider the following statements: I. TCP connections are full duplex. II. TCP has no option for selective acknowledgment. III. TCP connections are message streams. Which of the following is correct?
*निम्न कथनों पर विचार करें: I. TCP connections full duplex होती हैं. II. TCP में selective acknowledgment का कोई विकल्प नहीं है. III. TCP connections message streams हैं. निम्न में से क्या सही है?*
- **(A)** Only I is correct
- **(B)** Only I and II are correct
- **(C)** Only II and III are correct
- **(D)** All of I, II and III are correct
✔ **(A) Only I is correct**
★ **Nukta:** GATE 2012 official key (a). याद रखो: TCP = full-duplex byte-stream + SACK उपलब्ध; UDP = message-oriented.
*GATE 2012 official key (a). याद रखो: TCP = full-duplex byte-stream + SACK उपलब्ध; UDP = message-oriented.*
*[Source: GATE CS 2012] · Hard*

## Section B — Data Link Layer: Framing & MAC Sub-layer

*Framing, bit/byte stuffing, Ethernet frame format, CSMA/CD-CA, ALOHA, token & reservation access, client-server basics.*

**Data link layer data ko frames mein baant-ti hai; medium access ke liye CSMA/CD (wired), CSMA/CA (wireless), ALOHA, token passing — yeh sab MAC methods hain.**

*Data link layer data को frames में बाँटती है; medium access के लिए CSMA/CD, CSMA/CA, ALOHA, token passing।*

- Framing methods: Byte count, Byte stuffing (DLE-ESC), Bit stuffing (0 after five 1s), Physical layer coding violation.
  - *Framing: Byte count, Byte stuffing, Bit stuffing (पाँच 1 के बाद 0), Coding violation।*
- Ethernet frame: Preamble | Destination MAC | Source MAC | Type | Data (46–1500 B) | FCS — minimum frame 64 bytes.
  - *Ethernet frame: Preamble | Dest MAC | Src MAC | Type | Data | FCS — न्यूनतम 64 bytes।*
- CSMA/CD (wired Ethernet): medium sense karke bhejo; collision par jamming + backoff; 1-persistent = sunne par turant bhejo.
  - *CSMA/CD: sense करके भेजो; collision पर jamming + backoff।*
- Collision window = 2 × propagation time; minimum frame size isi se tay hota hai (2 km/10⁷ bps → 25 B jaisa classic).
  - *Collision window = 2 × propagation time; minimum frame size इसी से।*
- CSMA/CA (wireless): collision detect nahi hota — RTS/CTS, ACK, inter-frame spacing se collision avoid; hidden terminal problem.
  - *CSMA/CA (wireless): RTS/CTS, ACK; hidden terminal problem।*
- ALOHA: Pure (jab mann kare bhejo) vs Slotted (time slots) — random access ke sabse purane tareeke.
  - *ALOHA: Pure vs Slotted — random access के पुराने तरीक़े।*
- Token passing (Token Ring/FDDI) — controlled access: token milne par hi bhejo; collision nahi.
  - *Token passing — controlled access; collision नहीं।*
- Access methods: Random (ALOHA, CSMA) vs Controlled (token, polling).
  - *Access: Random vs Controlled।*

| Method | Medium | Collision handling |
|---|---|---|
| CSMA/CD | wired Ethernet | detect + jam + backoff |
| CSMA/CA | wireless | avoid (RTS/CTS, ACK) |
| ALOHA | radio | retransmit after collision |
| Token passing | ring | collision nahi hota |

### Questions (Easy → Medium → Hard)

**Q435.** Why is bit stuffing required in bit-oriented protocols?
*Bit-oriented protocols में bit stuffing क्यों ज़रूरी है?*
- **(A)** To increase bandwidth
- **(B)** To prevent confusion between data and the flag
- **(C)** To reduce collisions
- **(D)** To detect errors
✔ **(B) To prevent confusion between data and the flag**
★ **Nukta:** Bit stuffing = data को flag से अलग पहचान दिलाना.
*Bit stuffing = data को flag से अलग पहचान दिलाना.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q436.** The correct order of fields in an Ethernet frame is:
*Ethernet frame में fields का सही क्रम है:*
- **(A)** Preamble → Destination MAC → Source MAC → Type/Length → Data → FCS
- **(B)** Destination MAC → Source MAC → FCS → Data → Preamble
- **(C)** Source MAC → Destination MAC → Data → CRC → Type
- **(D)** Preamble → Source MAC → Destination MAC → Data
✔ **(A) Preamble → Destination MAC → Source MAC → Type/Length → Data → FCS**
★ **Nukta:** Remember: after the Preamble come the RECEIVER's address (Destination) first, then the sender's — the rest later.
*याद रखो: Preamble के बाद पहले RECEIVER का पता (Destination), फिर भेजने वाले का — बाकी बाद में.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q437.** Collision detection and avoidance mechanisms are implemented in:
*Collision detection और avoidance mechanisms कहाँ लागू होते हैं?*
- **(A)** LLC Sublayer
- **(B)** Network Layer
- **(C)** MAC Sublayer
- **(D)** Physical Layer
✔ **(C) MAC Sublayer**
★ **Nukta:** MAC = Medium Access Control — नाम में ही 'medium access' लिखा है.
*MAC = Medium Access Control — नाम में ही 'medium access' लिखा है.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q438.** Which protocol requires time synchronization among nodes?
*किस protocol में nodes के बीच time synchronization चाहिए होती है?*
- **(A)** Pure ALOHA
- **(B)** Slotted ALOHA
- **(C)** CSMA
- **(D)** CSMA/CD
✔ **(B) Slotted ALOHA**
★ **Nukta:** Pure ALOHA = send whenever you like; Slotted = send only when the slot clock says so.
*Pure ALOHA = जब मन चाहे भेजो; Slotted = slot की घड़ी देखकर भेजो.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q439.** The vulnerable period of Pure ALOHA is:
*Pure ALOHA का vulnerable period होता है:*
- **(A)** T
- **(B)** 2T
- **(C)** T/2
- **(D)** 4T
✔ **(B) 2T**
★ **Nukta:** Pure ALOHA: 2T और G·e⁻²ᴳ (~18.4%); Slotted ALOHA: T और G·e⁻ᴳ (~36.8%).
*Pure ALOHA: 2T और G·e⁻²ᴳ (~18.4%); Slotted ALOHA: T और G·e⁻ᴳ (~36.8%).*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q440.** Which protocol has the highest efficiency under heavy load?
*भारी load पर किस protocol की efficiency सबसे अधिक होती है?*
- **(A)** Pure ALOHA
- **(B)** Slotted ALOHA
- **(C)** CSMA
- **(D)** CSMA/CD
✔ **(D) CSMA/CD**
★ **Nukta:** क्रम: CSMA/CD > CSMA > Slotted ALOHA > Pure ALOHA.
*क्रम: CSMA/CD > CSMA > Slotted ALOHA > Pure ALOHA.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q441.** Which protocol detects collisions while transmission is in progress?
*कौन-सा protocol transmission के दौरान ही collisions detect करता है?*
- **(A)** CSMA
- **(B)** Slotted ALOHA
- **(C)** CSMA/CD
- **(D)** CSMA/CA
✔ **(C) CSMA/CD**
★ **Nukta:** CD = detect-and-jam; CA = avoid (RTS/CTS) — wireless में.
*CD = detect-and-jam; CA = avoid (RTS/CTS) — wireless में.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q442.** Which mechanism is used by CSMA/CA to reduce collisions?
*CSMA/CA collisions कम करने के लिए कौन-सा mechanism उपयोग करता है?*
- **(A)** Collision detection
- **(B)** Slot restriction
- **(C)** RTS/CTS handshake
- **(D)** Jam signal
✔ **(C) RTS/CTS handshake**
★ **Nukta:** CA = Collision Avoidance — टकराव रोकना, पकड़ना नहीं.
*CA = Collision Avoidance — टकराव रोकना, पकड़ना नहीं.*
*[Source: BCI Subject Test-9.pdf] · Easy*

**Q443.** Bit stuffing refers to:
*Bit stuffing का अर्थ है:*
- **(A)** Inserting a '0' in the user stream to differentiate it from the flag
- **(B)** Inserting a '0' in the flag stream to avoid ambiguity
- **(C)** Appending a nibble to the flag sequence
- **(D)** Appending a nibble to the user data stream
✔ **(A) Inserting a '0' in the user stream to differentiate it from the flag**
★ **Nukta:** Stuffing is always done in DATA, never in the flag; in byte stuffing 0x7D follows 0x7E.
*Stuffing हमेशा DATA में होती है, flag में नहीं; byte stuffing में 0x7E के बाद 0x7D जुड़ता है.*
*[Source: Unit Test-4 Solution.pdf (OCR), p26] · Medium*

**Q444.** In Ethernet CSMA/CD, the special sequence transmitted by media access management to handle a collision is called:
*Ethernet CSMA/CD में collision संभालने के लिए media access management द्वारा भेजा गया विशेष sequence कहलाता है:*
- **(A)** Preamble
- **(B)** Postamble
- **(C)** Jam signal
- **(D)** None of these
✔ **(C) Jam signal**
★ **Nukta:** Jam = the siren shouting 'a collision happened!'. Preamble = announcement that a frame is starting.
*Jam = 'टकराव हो गया!' का सायरन. Preamble = frame शुरू होने की घोषणा.*
*[Source: Unit Test-4 Solution.pdf (OCR), p28] · Medium*

**Q445.** The minimum size of an Ethernet frame (excluding preamble) is:
*Ethernet frame का न्यूनतम आकार (preamble को छोड़कर) होता है:*
- **(A)** 46 bytes
- **(B)** 64 bytes
- **(C)** 72 bytes
- **(D)** 1518 bytes
✔ **(B) 64 bytes**
★ **Nukta:** 64 = minimum frame; 1518 = maximum frame; 46 = सिर्फ data का minimum.
*64 = minimum frame; 1518 = maximum frame; 46 = सिर्फ data का minimum.*
*[Source: BCI Subject Test-9.pdf] · Medium*

**Q446.** The data field size in an Ethernet frame ranges from:
*Ethernet frame में data field का आकार रहता है:*
- **(A)** 64–1518 bytes
- **(B)** 46–1500 bytes
- **(C)** 40–1480 bytes
- **(D)** 32–1500 bytes
✔ **(B) 46–1500 bytes**
★ **Nukta:** The whole frame ranges 64–1518 bytes; the data 46–1500. This pair is asked often.
*पूरे frame का range 64–1518; data का 46–1500. यह जोड़ी अक्सर पूछी जाती है.*
*[Source: BCI Subject Test-9.pdf] · Medium*

**Q447.** In Ethernet, the minimum frame size is fixed mainly to:
*Ethernet में न्यूनतम frame आकार मुख्य रूप से किसलिए तय किया गया है?*
- **(A)** Improve throughput
- **(B)** Reduce overhead
- **(C)** Detect collisions using CSMA/CD
- **(D)** Increase security
✔ **(C) Detect collisions using CSMA/CD**
★ **Nukta:** Round-trip time (slot time) तक frame ज़िंदा रहे — तभी collision पकड़ी जाएगी.
*Round-trip time (slot time) तक frame ज़िंदा रहे — तभी collision पकड़ी जाएगी.*
*[Source: BCI Subject Test-9.pdf] · Medium*

**Q448.** What is the primary function of the MAC sublayer?
*MAC sublayer का मुख्य काम क्या है?*
- **(A)** Routing
- **(B)** Error checking
- **(C)** Addressing
- **(D)** Channel access
✔ **(D) Channel access**
★ **Nukta:** MAC = addressing + channel access; पर परीक्षा में 'primary function' = channel access.
*MAC = addressing + channel access; पर परीक्षा में 'primary function' = channel access.*
*[Source: CN Topic Test-04.pdf] · Medium*

**Q449.** What is the primary role of CSMA/CD in Ethernet?
*Ethernet में CSMA/CD की मुख्य भूमिका क्या है?*
- **(A)** Error correction
- **(B)** Collision detection
- **(C)** Address resolution
- **(D)** Flow control
✔ **(B) Collision detection**
★ **Nukta:** नाम में ही Collision Detection लिखा है.
*नाम में ही Collision Detection लिखा है.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q450.** Why is CSMA/CD not suitable for wireless networks?
*CSMA/CD wireless networks के लिए उपयुक्त क्यों नहीं है?*
- **(A)** No random access
- **(B)** Collision detection is not feasible in wireless
- **(C)** High bandwidth requirement
- **(D)** Requires slot synchronization
✔ **(B) Collision detection is not feasible in wireless**
★ **Nukta:** Wired = CSMA/CD; Wireless = CSMA/CA. यह जोड़ी पक्की याद रखो.
*Wired = CSMA/CD; Wireless = CSMA/CA. यह जोड़ी पक्की याद रखो.*
*[Source: BCI Subject Test-9.pdf] · Medium*

**Q451.** What is multiple access?
*Multiple access क्या है?*
- **(A)** Accessing a computer from multiple locations
- **(B)** A kind of network (MAN)
- **(C)** Sharing of one physical link by more than one station
- **(D)** None of the above
✔ **(C) Sharing of one physical link by more than one station**
★ **Nukta:** Shared medium को संभालने वाले protocols ही Multiple Access Protocols हैं.
*Shared medium को संभालने वाले protocols ही Multiple Access Protocols हैं.*
*[Source: SSC CGL Internet & Networking (via EduRev bank)] · Medium*

**Q452.** A Token Ring implementation works on the ______ mode of medium access.
*Token Ring implementation medium access के ______ mode पर काम करती है.*
- **(A)** Contention
- **(B)** Reservation
- **(C)** Round Robin
- **(D)** None of the above
✔ **(C) Round Robin**
★ **Nukta:** MAC तरीके तीन: Contention (ALOHA/CSMA), Reservation, Round Robin (Token).
*MAC तरीके तीन: Contention (ALOHA/CSMA), Reservation, Round Robin (Token).*
*[Source: Unit Test -2 Solutions.pdf (OCR), p26] · Medium*

**Q453.** What is the MTU size for Ethernet?
*Ethernet के लिए MTU आकार कितना है?*
- **(A)** 1024 bytes
- **(B)** 1500 bytes
- **(C)** 512 bytes
- **(D)** 2048 bytes
✔ **(B) 1500 bytes**
★ **Nukta:** MTU = the data limit; 1518 = the whole frame limit. Don't confuse the two.
*MTU = data की सीमा; 1518 = पूरे frame की सीमा. भ्रम में मत आना.*
*[Source: CN Topic Test 5.pdf] · Hard*

**Q454.** In a slotted ALOHA with G stations attempting to transmit in one slot, the throughput is equal to:
*Slotted ALOHA में एक slot में G stations transmit करने का प्रयास करें तो throughput होगा:*
- **(A)** G × e⁻ᴳ
- **(B)** 2G × e⁻ᴳ
- **(C)** e⁻ᴳ
- **(D)** G × e⁻²ᴳ
✔ **(A) G × e⁻ᴳ**
★ **Nukta:** RPSC official key (a). Pure ALOHA का formula G·e⁻²ᴳ है — मिलाकर मत पढ़ना.
*RPSC official key (a). Pure ALOHA का formula G·e⁻²ᴳ है — मिलाकर मत पढ़ना.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q455.** Which of the following Multiple Access Protocols is not suitable for wired networks?
*निम्न में से कौन-सा Multiple Access Protocol wired networks के लिए उपयुक्त नहीं है?*
- **(A)** CSMA/CD
- **(B)** TDMA
- **(C)** Token passing
- **(D)** CSMA/CA
✔ **(D) CSMA/CA**
★ **Nukta:** RPSC official key (d) — wired = CSMA/CD, wireless = CSMA/CA.
*RPSC official key (d) — wired = CSMA/CD, wireless = CSMA/CA.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q456.** Network Allocation Vector (NAV) is associated with which of the following MAC technologies?
*Network Allocation Vector (NAV) निम्न में से किस MAC technology से जुड़ा है?*
- **(A)** Wi-Fi (CSMA/CA)
- **(B)** CSMA/CD
- **(C)** Bluetooth
- **(D)** Ethernet
✔ **(A) Wi-Fi (CSMA/CA)**
★ **Nukta:** RPSC official key (a) — NAV = virtual carrier sensing का हिस्सा.
*RPSC official key (a) — NAV = virtual carrier sensing का हिस्सा.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q457.** In Reservation mode of MAC, each station in the network ______ a time slot for a finite or infinite amount of time to access the shared medium.
*MAC के Reservation mode में network का हर station shared medium तक पहुँचने के लिए एक time slot ______ करता है.*
- **(A)** should reserve
- **(B)** need not reserve
- **(C)** Can't say
- **(D)** None of the above
✔ **(A) should reserve**
★ **Nukta:** Reservation = book first, travel later — contention (ALOHA/CSMA) has no booking.
*Reservation = पहले बुकिंग, फिर यात्रा — contention (ALOHA/CSMA) में बुकिंग नहीं.*
*[Source: Unit Test -2 Solutions.pdf (OCR), p25] · Hard*

**Q458.** Which one of the following is not used in media access control?
*निम्न में से कौन-सा media access control में उपयोग नहीं होता?*
- **(A)** Ethernet
- **(B)** Digital subscriber line (DSL)
- **(C)** FDDI
- **(D)** None of the mentioned
✔ **(B) Digital subscriber line (DSL)**
★ **Nukta:** MAC = LAN की बात; DSL = telephone line पर broadband.
*MAC = LAN की बात; DSL = telephone line पर broadband.*
*[Source: CN Topic Test-01.pdf] · Hard*

**Q459.** Which of the following is NOT true with respect to a transparent bridge and a router?
*Transparent bridge और router के संबंध में निम्न में से कौन-सा सही नहीं है?*
- **(A)** Both bridge and router selectively forward data packets
- **(B)** A bridge uses IP addresses while a router uses MAC addresses
- **(C)** A bridge builds its table by inspecting incoming packets
- **(D)** A router can connect between a LAN and a WAN
✔ **(B) A bridge uses IP addresses while a router uses MAC addresses**
★ **Nukta:** RPSC 2011 official key (2). याद रखो: Bridge = MAC (L2), Router = IP (L3).
*RPSC 2011 official key (2). याद रखो: Bridge = MAC (L2), Router = IP (L3).*
*[Source: RPSC Programmer 2011 Paper-1 (via pyqp.in)] · Hard*

**Q460.** Which of the following is NOT a function of the AAL (ATM Adaptation Layer)?
*निम्न में से कौन-सा AAL (ATM Adaptation Layer) का काम नहीं है?*
- **(A)** Cell header generation
- **(B)** Handling of lost and misinserted cells
- **(C)** Handling of cell delay variation
- **(D)** Segmentation and reassembly of user information
✔ **(A) Cell header generation**
★ **Nukta:** RPSC 2011 official key (1). ATM में: ATM layer = cell header/switching; AAL = segmentation+reassembly.
*RPSC 2011 official key (1). ATM में: ATM layer = cell header/switching; AAL = segmentation+reassembly.*
*[Source: RPSC Programmer 2011 Paper-1 (via pyqp.in)] · Hard*

## Section C — Network Layer: IP, ICMP, ARP & Routing Protocols

*IPv4 header & fragmentation, IPv6 fields, logical addressing, ARP/ICMP/IGMP, routing (RIP/OSPF/BGP/MPLS/STP), traceroute, DHCP & probability problems.*

**Network layer = IP addressing + routing + fragmentation + error reporting (ICMP). Routing protocols RIP/OSPF/BGP aur distance-vector vs link-state — exam ke favourites.**

*Network layer = IP addressing + routing + fragmentation + ICMP। Routing protocols RIP/OSPF/BGP।*

- IPv4 header (20–60 B): IHL, Type of Service, Total Length, TTL, Protocol, Flags, Fragment Offset, Source/Dest IP, Checksum.
  - *IPv4 header: TTL, Protocol, Flags, Fragment Offset, Source/Dest IP, Checksum।*
- Fragmentation: MTU se bada packet tootta hai; offset = 8-byte units; M bit (More fragments); reassembly sirf destination par.
  - *Fragmentation: MTU से बड़ा packet टूटता है; offset = 8-byte units; M bit; reassembly सिर्फ़ destination पर।*
- TTL = loop prevention: har router par 1 kam, 0 par drop (ICMP Time Exceeded).
  - *TTL = loop prevention: हर router पर 1 कम।*
- Routing: Static (manual) vs Dynamic; Distance Vector (RIP — hop count, periodic update, slow converge) vs Link State (OSPF — topology map, Dijkstra, fast converge).
  - *Routing: Static vs Dynamic; Distance Vector (RIP) vs Link State (OSPF)।*
- BGP = inter-domain routing (autonomous systems ke beech); EGP family.
  - *BGP = inter-domain routing।*
- ICMP = error + control messages: Echo Request/Reply (ping), Destination Unreachable, Time Exceeded, Redirect.
  - *ICMP: Echo (ping), Destination Unreachable, Time Exceeded, Redirect।*
- ARP — IP→MAC (broadcast request); IGMP — multicast group management.
  - *ARP — IP→MAC; IGMP — multicast।*
- Congestion control: choke points, backpressure; open-loop vs closed-loop.
  - *Congestion control: choke points, backpressure।*

| Protocol | Type | Convergence | Metric |
|---|---|---|---|
| RIP | distance vector | slow (count-to-infinity) | hop count (max 15) |
| OSPF | link state | fast | cost/bandwidth |
| BGP | path vector | — | policy/AS path |

### Questions (Easy → Medium → Hard)

**Q461.** What is the function of ARP?
*ARP का काम क्या है?*
- **(A)** Resolve IP address to MAC address
- **(B)** Resolve domain name to IP
- **(C)** Encrypt packets
- **(D)** Determine the route
✔ **(A) Resolve IP address to MAC address**
★ **Nukta:** ARP = IP→MAC; DNS = name→IP; RARP = MAC→IP (obsolete).
*ARP = IP→MAC; DNS = name→IP; RARP = MAC→IP (obsolete).*
*[Source: CN Topic Test 6.pdf + Unit Test -2 Solutions.pdf (OCR)] · Medium*

**Q462.** Which tool is used to view the MAC address of a system?
*किस system का MAC address देखने के लिए कौन-सा tool उपयोग होता है?*
- **(A)** ping
- **(B)** ipconfig /all
- **(C)** netstat
- **(D)** arp -a
✔ **(B) ipconfig /all**
★ **Nukta:** Windows: ipconfig /all; Linux: ip link / ifconfig. दोनों अपना NIC दिखाते हैं.
*Windows: ipconfig /all; Linux: ip link / ifconfig. दोनों अपना NIC दिखाते हैं.*
*[Source: BCI_SCI Subject Test-7.pdf] · Medium*

**Q463.** Which protocol is used for path MTU discovery?
*Path MTU discovery के लिए कौन-सा protocol उपयोग होता है?*
- **(A)** TCP
- **(B)** UDP
- **(C)** ICMP
- **(D)** ARP
✔ **(C) ICMP**
★ **Nukta:** ICMP = network का संदेशवाहक — ping, traceroute, PMTU सब इसी से.
*ICMP = network का संदेशवाहक — ping, traceroute, PMTU सब इसी से.*
*[Source: BCI_SCI Subject Test-7.pdf] · Medium*

**Q464.** What is the function of IGMP in networking?
*Networking में IGMP का काम क्या है?*
- **(A)** Manage IP address allocation
- **(B)** Route datagrams
- **(C)** Manage multicast group membership
- **(D)** Handle device discovery
✔ **(C) Manage multicast group membership**
★ **Nukta:** IGMP = multicast की member-list; Network layer protocol.
*IGMP = multicast की member-list; Network layer protocol.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q465.** What is the role of the TTL field in an IP packet?
*IP packet में TTL field की भूमिका क्या है?*
- **(A)** Authentication
- **(B)** Packet size control
- **(C)** Packet lifespan control
- **(D)** Encryption
✔ **(C) Packet lifespan control**
★ **Nukta:** TTL = loop-stopper. It is also what runs traceroute (different TTLs map the path).
*TTL = loop-रोधक. यही traceroute को भी चलाता है (अलग-अलग TTL से path बनता है).*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q466.** Which field in the IPv4 header indicates the priority of the packet?
*IPv4 header में कौन-सा field packet की प्राथमिकता बताता है?*
- **(A)** Protocol
- **(B)** TTL
- **(C)** Type of Service (ToS)
- **(D)** Flags
✔ **(C) Type of Service (ToS)**
★ **Nukta:** ToS बाद में DiffServ/DSCP बना — काम वही: priority/class.
*ToS बाद में DiffServ/DSCP बना — काम वही: priority/class.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q467.** Which of the following uses a logical addressing scheme?
*निम्न में से कौन-सा logical addressing scheme उपयोग करता है?*
- **(A)** MAC address
- **(B)** IP address
- **(C)** ARP
- **(D)** DNS
✔ **(B) IP address**
★ **Nukta:** Forouzan का नियम: Data link = physical, Network = logical, Transport = port, Application = specific (name).
*Forouzan का नियम: Data link = physical, Network = logical, Transport = port, Application = specific (name).*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q468.** Which algorithm is used by OSPF to compute the shortest path?
*OSPF shortest path निकालने के लिए कौन-सा algorithm उपयोग करता है?*
- **(A)** Bellman-Ford
- **(B)** Dijkstra
- **(C)** A*
- **(D)** Kruskal
✔ **(B) Dijkstra**
★ **Nukta:** Link-state = Dijkstra; Distance-vector = Bellman-Ford. यह जोड़ी पक्की.
*Link-state = Dijkstra; Distance-vector = Bellman-Ford. यह जोड़ी पक्की.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q469.** Which one is a distance-vector routing protocol?
*निम्न में से कौन-सा distance-vector routing protocol है?*
- **(A)** RIP
- **(B)** OSPF
- **(C)** BGP
- **(D)** IS-IS
✔ **(A) RIP**
★ **Nukta:** RIP = DV (Bellman-Ford); OSPF/IS-IS = Link-state (Dijkstra); BGP = Path-vector.
*RIP = DV (Bellman-Ford); OSPF/IS-IS = Link-state (Dijkstra); BGP = Path-vector.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q470.** What is a major drawback of distance vector routing?
*Distance vector routing की एक बड़ी कमी क्या है?*
- **(A)** High complexity
- **(B)** Count-to-infinity problem
- **(C)** Slow convergence
- **(D)** Lack of security
✔ **(B) Count-to-infinity problem**
★ **Nukta:** Count-to-infinity is the signature of DV; link-state is free of it (but uses more memory).
*DV की पहचान ही count-to-infinity; link-state इससे मुक्त है (पर ज़्यादा memory लेता है).*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q471.** BGP is mainly used for which type of routing, and it belongs to which algorithm family?
*BGP मुख्य रूप से किस प्रकार के routing के लिए उपयोग होता है और यह किस algorithm परिवार का है?*
- **(A)** Intra-AS routing; link-state
- **(B)** Inter-AS routing; path-vector (distance-vector family)
- **(C)** Static routing; flooding
- **(D)** Host routing; Dijkstra
✔ **(B) Inter-AS routing; path-vector (distance-vector family)**
★ **Nukta:** AS = Autonomous System. अंदर (AS) OSPF/RIP; बीच में (Inter-AS) BGP — Internet का glue protocol.
*AS = Autonomous System. अंदर (AS) OSPF/RIP; बीच में (Inter-AS) BGP — Internet का glue protocol.*
*[Source: CN Topic Test 5.pdf + CN Topic Test 6.pdf] · Medium*

**Q472.** In the early ARPANET, which routing method was used?
*प्रारंभिक ARPANET में कौन-सी routing method उपयोग होती थी?*
- **(A)** Distance vector routing
- **(B)** Link state routing
- **(C)** Least cost routing
- **(D)** Flooding
✔ **(A) Distance vector routing**
★ **Nukta:** इतिहास: ARPANET = distance-vector से शुरू, फिर link-state (OSPF जैसा).
*इतिहास: ARPANET = distance-vector से शुरू, फिर link-state (OSPF जैसा).*
*[Source: Unit Test-4 Solution.pdf (OCR), p8] · Medium*

**Q473.** Which of these protocols allows loop-free switching in Layer 2 networks?
*निम्न में से कौन-सा protocol Layer 2 networks में loop-free switching देता है?*
- **(A)** RIP
- **(B)** OSPF
- **(C)** STP (Spanning Tree Protocol)
- **(D)** EIGRP
✔ **(C) STP (Spanning Tree Protocol)**
★ **Nukta:** STP = Layer 2 का loop-रोधक; routing protocols Layer 3 के हैं.
*STP = Layer 2 का loop-रोधक; routing protocols Layer 3 के हैं.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q474.** MPLS operates between which two layers?
*MPLS किन दो layers के बीच काम करता है?*
- **(A)** Layer 1 and 2
- **(B)** Layer 2 and 3
- **(C)** Layer 3 and 4
- **(D)** Layer 4 and 7
✔ **(B) Layer 2 and 3**
★ **Nukta:** MPLS = 'Layer 2.5' — label-based forwarding, IP header देखे बिना.
*MPLS = 'Layer 2.5' — label-based forwarding, IP header देखे बिना.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q475.** What does the 'traceroute' command do?
*'traceroute' command क्या करता है?*
- **(A)** Lists all devices on a network
- **(B)** Tracks the path a packet takes to the destination
- **(C)** Resolves domain names
- **(D)** Opens ports on the firewall
✔ **(B) Tracks the path a packet takes to the destination**
★ **Nukta:** tracert (Windows) ICMP; traceroute (Linux) UDP — काम वही: रास्ता दिखाना.
*tracert (Windows) ICMP; traceroute (Linux) UDP — काम वही: रास्ता दिखाना.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q476.** Which protocol does traceroute use on UNIX/Linux systems?
*UNIX/Linux systems पर traceroute कौन-सा protocol उपयोग करता है?*
- **(A)** TCP
- **(B)** UDP
- **(C)** ICMP Echo
- **(D)** IGMP
✔ **(B) UDP**
★ **Nukta:** Windows tracert ICMP भेजता है; Linux traceroute UDP. दोनों का काम एक ही.
*Windows tracert ICMP भेजता है; Linux traceroute UDP. दोनों का काम एक ही.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q477.** Which command is used to see the routing table in Linux?
*Linux में routing table देखने के लिए कौन-सा command उपयोग होती है?*
- **(A)** ifconfig
- **(B)** netstat -r
- **(C)** ping
- **(D)** ipconfig
✔ **(B) netstat -r**
★ **Nukta:** Windows: route print; Linux: netstat -r / ip route.
*Windows: route print; Linux: netstat -r / ip route.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q478.** Which protocol is used for dynamic IP address assignment?
*Dynamic IP address assignment के लिए कौन-सा protocol उपयोग होता है?*
- **(A)** DNS
- **(B)** ARP
- **(C)** DHCP
- **(D)** FTP
✔ **(C) DHCP**
★ **Nukta:** DHCP = 'Plug and Play' networking — zeroconf का प्रमुख tool.
*DHCP = 'Plug and Play' networking — zeroconf का प्रमुख tool.*
*[Source: CN Topic Test-03.pdf + CN Topic Test 6.pdf] · Medium*

**Q479.** ICMP is a ............ layer protocol.
*ICMP एक ............ layer protocol है.*
- **(A)** Data link
- **(B)** Transport
- **(C)** Application
- **(D)** Network
✔ **(D) Network**
★ **Nukta:** RPSC official key (d). ICMP/IP/ARP/IGMP सब Network layer के; TCP/UDP Transport.
*RPSC official key (d). ICMP/IP/ARP/IGMP सब Network layer के; TCP/UDP Transport.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key) + Random Test- Rajasthan PYQ.pdf (OCR)] · Hard*

**Q480.** Which of the following is NOT a valid ICMP error message?
*निम्न में से कौन-सा वैध ICMP error message नहीं है?*
- **(A)** Destination Unreachable
- **(B)** Time Exceeded
- **(C)** Echo Request
- **(D)** Port Unreachable
✔ **(C) Echo Request**
★ **Nukta:** ICMP errors: Destination Unreachable, Time Exceeded, Source Quench, Redirect. Queries: Echo, Timestamp.
*ICMP errors: Destination Unreachable, Time Exceeded, Source Quench, Redirect. Queries: Echo, Timestamp.*
*[Source: CN Topic Test 5.pdf] · Hard*

**Q481.** Which field in the IP header helps in fragmentation?
*IP header में कौन-सा field fragmentation में मदद करता है?*
- **(A)** TTL
- **(B)** Header Length
- **(C)** Identification
- **(D)** Protocol
✔ **(C) Identification**
★ **Nukta:** Fragmentation के तीन tool: Identification + Flags (MF) + Fragment Offset.
*Fragmentation के तीन tool: Identification + Flags (MF) + Fragment Offset.*
*[Source: CN Topic Test 6.pdf] · Hard*

**Q482.** How many bits are there in the 'Fragment Offset' field of the IPv4 header?
*IPv4 header के 'Fragment Offset' field में कितने bits होते हैं?*
- **(A)** 16 bits
- **(B)** 10 bits
- **(C)** 13 bits
- **(D)** 32 bits
✔ **(C) 13 bits**
★ **Nukta:** RPSC official key (c). IPv4 header: Version(4)+HLen(4)+ToS(8)+TotalLen(16)+ID(16)+Flags(3)+FragOffset(13)+TTL(8)+...
*RPSC official key (c). IPv4 header: Version(4)+HLen(4)+ToS(8)+TotalLen(16)+ID(16)+Flags(3)+FragOffset(13)+TTL(8)+...*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q483.** In IPv4, packet fragmentation and reassembly is handled by:
*IPv4 में packet fragmentation और reassembly कैसे होता है?*
- **(A)** the More Fragments flag and Fragment Offset field
- **(B)** the MAC Header
- **(C)** the Header Checksum
- **(D)** encapsulating packets in larger frames
✔ **(A) the More Fragments flag and Fragment Offset field**
★ **Nukta:** RPSC official key (a). याद रखो: fragmentation sender/routers करते हैं, reassembly सिर्फ destination host.
*RPSC official key (a). याद रखो: fragmentation sender/routers करते हैं, reassembly सिर्फ destination host.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q484.** What is fragmentation in IP networking?
*IP networking में fragmentation क्या है?*
- **(A)** Splitting data into packets
- **(B)** Splitting large packets so they fit a smaller MTU link
- **(C)** Combining multiple packets
- **(D)** Encrypting packets
✔ **(B) Splitting large packets so they fit a smaller MTU link**
★ **Nukta:** Packet बनाना segmentation है; बड़े packet के टुकड़े fragmentation. IPv6 में routers fragmentation नहीं करते.
*Packet बनाना segmentation है; बड़े packet के टुकड़े fragmentation. IPv6 में routers fragmentation नहीं करते.*
*[Source: CN Topic Test 6.pdf] · Hard*

**Q485.** The size of the 'total length field' of an IPv4 datagram is:
*IPv4 datagram के 'total length field' का आकार है:*
- **(A)** 16 bits
- **(B)** 32 bits
- **(C)** 8 bits
- **(D)** 4 bits
✔ **(A) 16 bits**
★ **Nukta:** RPSC official key (a). 16 bits = 2¹⁶ − 1 = 65535.
*RPSC official key (a). 16 bits = 2¹⁶ − 1 = 65535.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q486.** What is the minimum header size of an IPv4 packet?
*IPv4 packet का न्यूनतम header आकार कितना है?*
- **(A)** 16 bytes
- **(B)** 10 bytes
- **(C)** 20 bytes
- **(D)** 32 bytes
✔ **(C) 20 bytes**
★ **Nukta:** 20 bytes = 5 words × 4 bytes — यही Header Length field की न्यूनतम गिनती.
*20 bytes = 5 words × 4 bytes — यही Header Length field की न्यूनतम गिनती.*
*[Source: Networking MCQ bank (MQuestions)] · Hard*

**Q487.** In the IPv6 header, the traffic class field is similar to which field in the IPv4 header?
*IPv6 header में traffic class field, IPv4 header के किस field जैसा है?*
- **(A)** Fragmentation field
- **(B)** Flow label
- **(C)** Type of Service (ToS) field
- **(D)** Options field
✔ **(C) Type of Service (ToS) field**
★ **Nukta:** IPv6 में fragmentation fields ही नहीं हैं — routers टुकड़े नहीं करते.
*IPv6 में fragmentation fields ही नहीं हैं — routers टुकड़े नहीं करते.*
*[Source: Sanfoundry CN MCQs — IPv6] · Hard*

**Q488.** How many maximum hops are allowed in RIP?
*RIP में अधिकतम कितने hops की अनुमति है?*
- **(A)** 8
- **(B)** 16
- **(C)** 15
- **(D)** 32
✔ **(C) 15**
★ **Nukta:** RIP: max 15 hops, metric = hop count, हर 30 sec update.
*RIP: max 15 hops, metric = hop count, हर 30 sec update.*
*[Source: CN Topic Test 6.pdf] · Hard*

**Q489.** How does RIP prevent routing loops? (A) Poison reverse (B) Sequence numbers (C) Split horizon
*RIP routing loops कैसे रोकता है? (A) Poison reverse (B) Sequence numbers (C) Split horizon*
- **(A)** A only
- **(B)** C only
- **(C)** B only
- **(D)** Both A and C
✔ **(D) Both A and C**
★ **Nukta:** Loop रोकने के तरीके: split horizon, poison reverse, hold-down timers.
*Loop रोकने के तरीके: split horizon, poison reverse, hold-down timers.*
*[Source: CN Topic Test 6.pdf] · Hard*

**Q490.** Dynamic routing protocols enable routers to:
*Dynamic routing protocols routers को सक्षम बनाते हैं:*
- **(A)** Dynamically discover and maintain routes
- **(B)** Distribute routing updates to other routers
- **(C)** Reach agreement with other routers about network topology
- **(D)** All of the above
✔ **(D) All of the above**
★ **Nukta:** Static vs Dynamic: static में admin लिखता है; dynamic में protocol खुद सीखता है.
*Static vs Dynamic: static में admin लिखता है; dynamic में protocol खुद सीखता है.*
*[Source: Unit Test-4 Solution.pdf (OCR), p27] · Hard*

**Q491.** Which of the following protocols may be used as zeroconf and plug-and-play?
*निम्न में से कौन-सा protocol zeroconf और plug-and-play के रूप में उपयोग हो सकता है?*
- **(A)** TCP
- **(B)** DHCP
- **(C)** NAT
- **(D)** ICMP
✔ **(B) DHCP**
★ **Nukta:** RPSC official key (b). Zeroconf = बिना admin के automatic network settings.
*RPSC official key (b). Zeroconf = बिना admin के automatic network settings.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q492.** There are n stations in a slotted LAN. Each station attempts to transmit with a probability p in each time slot. The probability that exactly one station transmits in a slot is:
*एक slotted LAN में n stations हैं. हर time slot में हर station p प्रायिकता से transmit करने का प्रयास करता है. किसी slot में ठीक एक station transmit करने की प्रायिकता है:*
- **(A)** n × p × (1 − p)ⁿ⁻¹
- **(B)** p × (1 − p)ⁿ⁻¹
- **(C)** 1 − (1 − p)ⁿ⁻¹
- **(D)** (1 − p)ⁿ⁻¹
✔ **(A) n × p × (1 − p)ⁿ⁻¹**
★ **Nukta:** RPSC official key (a). यही binomial का 'exactly one success' formula है.
*RPSC official key (a). यही binomial का 'exactly one success' formula है.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q493.** One of the header fields in an IP datagram is the Time to Live (TTL). Which statement best explains the need for this field?
*IP datagram के header fields में से एक Time to Live (TTL) है. निम्न में से कौन-सा कथन इस field की आवश्यकता सबसे अच्छे से बताता है?*
- **(A)** It can be used to prioritize packets
- **(B)** It can be used to reduce delays
- **(C)** It can be used to optimize throughput
- **(D)** It can be used to prevent packet looping
✔ **(D) It can be used to prevent packet looping**
★ **Nukta:** RPSC 2011 official key (4). TTL = loop-रोधक; priority ToS से, delay/throughput इससे नहीं.
*RPSC 2011 official key (4). TTL = loop-रोधक; priority ToS से, delay/throughput इससे नहीं.*
*[Source: RPSC Programmer 2011 Paper-1 (via pyqp.in)] · Hard*

**Q494.** Suppose the stop-and-wait protocol is used on a link with a bit rate of 64 kilobits per second and 20 milliseconds propagation delay. Acknowledgement transmission time and processing times are negligible. The minimum frame size in bytes to achieve a link utilisation of at least 50% is ______.
*64 kbps की link पर stop-and-wait protocol है, propagation delay 20 ms है (ACK transmission व processing नगण्य)। कम से कम 50% link utilisation के लिए न्यूनतम frame size (bytes में) कितनी हो?*
- **(A)** 160
- **(B)** 320
- **(C)** 640
- **(D)** 1280
✔ **(B) 320**
★ **Nukta:** 160 bas ek Tp ka hissa hai; 640/1280 utilisation formula ke ratio bhool jane se aate hain.
*160 एक Tp; 640/1280 ratio भूलने से आते हैं।*
*[Source: GATE CS 2015 Set-1] · Hard*

**Q495.** A link has a transmission speed of 10⁶ bits/sec. It uses data packets of size 1000 bytes each. Acknowledgements have negligible transmission delay and the same propagation delay as data; processing delays are negligible. The efficiency of the stop-and-wait protocol is exactly 25%. The one-way propagation delay (in milliseconds) is ______.
*एक link की speed 10⁶ bits/sec है और packets 1000 bytes के हैं। ACK का transmission delay नगण्य, propagation delay data के बराबर है। Stop-and-wait की efficiency ठीक 25% है। एक-तरफ़ा propagation delay (ms में) कितना है?*
- **(A)** 8
- **(B)** 10
- **(C)** 12
- **(D)** 20
✔ **(C) 12**
★ **Nukta:** 8 ms Tt hai Tp nahi; 10/20 round numbers ke jaal hain.
*8 ms Tt है; 10/20 गोल आँकड़ों के जाल।*
*[Source: GATE CS 2015 Set-2] · Hard*

**Q496.** Consider the following statements regarding the slow start phase of TCP congestion control (cwnd = congestion window, MSS = maximum segment size):
(i) cwnd increases by 2 MSS on every successful acknowledgement.
(ii) cwnd approximately doubles on every successful acknowledgement.
(iii) cwnd increases by 1 MSS every round trip time.
(iv) cwnd approximately doubles every round trip time.
Which one of the following is correct?
*TCP congestion control के slow start चरण (cwnd = congestion window, MSS = maximum segment size) के बारे में विचार कीजिए:
(i) हर successful acknowledgement पर cwnd 2 MSS बढ़ता है।
(ii) हर successful acknowledgement पर cwnd लगभग दोगुना होता है।
(iii) हर round trip time में cwnd 1 MSS बढ़ता है।
(iv) हर round trip time में cwnd लगभग दोगुना होता है।
क्या सही है?*
- **(A)** (i) and (iii) only / केवल (i) और (iii)
- **(B)** (ii) and (iv) only / केवल (ii) और (iv)
- **(C)** (iv) only / केवल (iv)
- **(D)** (ii) only / केवल (ii)
✔ **(C) (iv) only**
★ **Nukta:** Per-ACK doubling (ii) bahut tez hota; (iii) per-RTT sirf 1 MSS congestion avoidance jaisa hai.
*Per-ACK doubling (ii) असंभव-सा; (iii) तो congestion avoidance जैसा।*
*[Source: GATE CS 2018] · Hard*

## Section D — Transport Layer: TCP/UDP, Ports & Sockets

*Connection-oriented vs connectionless services, sockets, TCP header & states, 3-way handshake, flow & congestion control, security (SYN flood, hijacking).*

**Transport layer end-to-end delivery karta hai — TCP (reliable) aur UDP (fast). TCP states, handshake aur congestion control numericals ke favourites hain.**

*Transport layer end-to-end delivery करता है — TCP (reliable) और UDP (fast)।*

- TCP = connection-oriented, reliable, ordered, full-duplex, byte-stream, flow + congestion control; UDP = connectionless, unreliable, fast, message-stream.
  - *TCP = connection-oriented, reliable; UDP = connectionless, तेज़, unreliable।*
- TCP header: Source/Dest port, Sequence number, Acknowledgement number, Window size, Flags (SYN, ACK, FIN, RST, PSH, URG), Checksum.
  - *TCP header: ports, seq, ack, window, flags (SYN/ACK/FIN/RST), checksum।*
- Three-way handshake: SYN → SYN+ACK → ACK; sequence numbers random (X, Y); data X+1 se shuru.
  - *Three-way handshake: SYN → SYN+ACK → ACK।*
- TCP connection close: FIN → ACK → FIN → ACK; states: ESTABLISHED, FIN_WAIT_1/2, TIME_WAIT, CLOSE_WAIT, LAST_ACK.
  - *TCP close: FIN → ACK → FIN → ACK; states: FIN_WAIT_2, TIME_WAIT...।*
- Flow control = sliding window (receiver advertised window); unacked bytes ≤ advertised window.
  - *Flow control = sliding window।*
- Congestion control: Slow start (cwnd 1 MSS se, per RTT double), Congestion avoidance (AIMD — +1 MSS per RTT), timeout par ssthresh = cwnd/2, Fast retransmit/recovery (3 dup ACKs).
  - *Congestion control: Slow start (per RTT double), AIMD, ssthresh = cwnd/2।*
- TCP sequence numbers BYTES count karte hain — wrap-around time = 2³² bytes / bandwidth (bytes/sec).
  - *TCP sequence numbers BYTES गिनते हैं — wrap time = 2³² / bandwidth।*
- UDP header sirf 8 bytes (ports + length + checksum); DNS, DHCP, VoIP, streaming UDP use karte hain.
  - *UDP header सिर्फ़ 8 bytes; DNS, VoIP, streaming।*
- Socket = IP + port; well-known ports service identify karte hain.
  - *Socket = IP + port।*

| Fakt | TCP | UDP |
|---|---|---|
| Connection | oriented (handshake) | connectionless |
| Reliability | haan (ACK, retransmit) | nahi |
| Order | maintain hota hai | nahi |
| Header | 20 B + options | 8 B |
| Use | HTTP, FTP, SMTP | DNS, DHCP, VoIP, streaming |

### Questions (Easy → Medium → Hard)

**Q497.** A client opens a TCP connection to a web server on port 80 using source port 49152. What is the complete socket pair?
*एक client source port 49152 से port 80 वाले web server को TCP connection खोलता है. पूरा socket pair क्या होगा?*
- **(A)** 192.168.1.10:49152 ↔ 172.16.0.5:80
- **(B)** 192.168.1.10:80 ↔ 172.16.0.5:49152
- **(C)** 49152 ↔ 80
- **(D)** 80 ↔ 49152
✔ **(A) 192.168.1.10:49152 ↔ 172.16.0.5:80**
★ **Nukta:** पहचान: client का port ephemeral (बड़ा number), server का port well-known (80).
*पहचान: client का port ephemeral (बड़ा number), server का port well-known (80).*
*[Source: BCI Subject Test-8.pdf] · Easy*

**Q498.** Which port is used by a DHCP client when requesting an IP address?
*IP address माँगते समय DHCP client कौन-सा port उपयोग करता है?*
- **(A)** UDP 67
- **(B)** UDP 68
- **(C)** TCP 68
- **(D)** TCP 67
✔ **(B) UDP 68**
★ **Nukta:** जोड़ी याद रखो: server 67, client 68 — DHCP (UDP).
*जोड़ी याद रखो: server 67, client 68 — DHCP (UDP).*
*[Source: BCI Subject Test-8.pdf] · Easy*

**Q499.** Which of the following is a connectionless transport service?
*निम्न में से कौन-सी connectionless transport service है?*
- **(A)** TCP
- **(B)** ARP
- **(C)** UDP
- **(D)** FTP
✔ **(C) UDP**
★ **Nukta:** Transport layer के दो सदस्य: TCP (भरोसेमंद, connection-oriented) और UDP (तेज़, connectionless).
*Transport layer के दो सदस्य: TCP (भरोसेमंद, connection-oriented) और UDP (तेज़, connectionless).*
*[Source: BCI_SCI Subject Test-7.pdf + Oliveboard SSC CGL bank] · Medium*

**Q500.** What is a socket in networking?
*Networking में socket क्या है?*
- **(A)** IP address + MAC address
- **(B)** IP address + Port number
- **(C)** MAC address + Port number
- **(D)** IP address + DNS name
✔ **(B) IP address + Port number**
★ **Nukta:** Socket pair = (Source IP:Port, Destination IP:Port) — TCP connection इसी से बनती है.
*Socket pair = (Source IP:Port, Destination IP:Port) — TCP connection इसी से बनती है.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q501.** What term is used for an endpoint in an inter-process communication across a network?
*Network पर inter-process communication में endpoint के लिए कौन-सा term उपयोग होता है?*
- **(A)** Port
- **(B)** Machine
- **(C)** Socket
- **(D)** Pipe
✔ **(C) Socket**
★ **Nukta:** Port = address का हिस्सा; Socket = पूरा endpoint (IP+Port).
*Port = address का हिस्सा; Socket = पूरा endpoint (IP+Port).*
*[Source: CN Topic Test-02.pdf] · Medium*

**Q502.** What is the purpose of the SYN flag in TCP?
*TCP में SYN flag का उद्देश्य क्या है?*
- **(A)** To end a session
- **(B)** To initiate (open) a connection
- **(C)** To reset a connection
- **(D)** For data transmission
✔ **(B) To initiate (open) a connection**
★ **Nukta:** Remember the flags: SYN = start; FIN = end; RST = abort; ACK = confirmation.
*Flags याद रखो: SYN = शुरुआत; FIN = अंत; RST = रद्द; ACK = पुष्टि.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q503.** In which scenario will TCP's three-way handshake fail?
*किस स्थिति में TCP का three-way handshake विफल होगा?*
- **(A)** Firewall blocks the SYN-ACK
- **(B)** High latency
- **(C)** ACK is slightly delayed
- **(D)** Server is busy
✔ **(A) Firewall blocks the SYN-ACK**
★ **Nukta:** The immediate cause of a failed handshake: the messages are not getting through (firewall/filter).
*Handshake टूटने का सीधा कारण: संदेशों का न पहुँचना (firewall/filter).*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q504.** In TCP, which state follows the SYN-SENT state in the normal case?
*TCP में सामान्य स्थिति में SYN-SENT के बाद कौन-सी state आती है?*
- **(A)** SYN-RECEIVED
- **(B)** LISTEN
- **(C)** ESTABLISHED
- **(D)** CLOSED
✔ **(C) ESTABLISHED**
★ **Nukta:** सामान्य क्रम: CLOSED → SYN-SENT → ESTABLISHED. (Simultaneous open में SYN-RECEIVED बीच में आती है.)
*सामान्य क्रम: CLOSED → SYN-SENT → ESTABLISHED. (Simultaneous open में SYN-RECEIVED बीच में आती है.)*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q505.** Which one of the following attacks exploits TCP's three-way handshake?
*निम्न में से कौन-सा attack TCP के three-way handshake का फ़ायदा उठाती है?*
- **(A)** SYN Flood
- **(B)** DNS Spoofing
- **(C)** Man in the Middle
- **(D)** ARP Poisoning
✔ **(A) SYN Flood**
★ **Nukta:** Handshake पर हमला = SYN flood; sequence पर हमला = session hijacking.
*Handshake पर हमला = SYN flood; sequence पर हमला = session hijacking.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q506.** TCP initially uses which congestion control technique when a connection starts?
*Connection शुरू होने पर TCP शुरू में कौन-सी congestion control technique उपयोग करता है?*
- **(A)** Congestion avoidance
- **(B)** Fast recovery
- **(C)** Slow start
- **(D)** Leaky bucket
✔ **(C) Slow start**
★ **Nukta:** TCP क्रम: Slow start → Congestion avoidance; loss पर → Fast recovery.
*TCP क्रम: Slow start → Congestion avoidance; loss पर → Fast recovery.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q507.** What is the purpose of TCP's congestion window (cwnd)?
*TCP के congestion window (cwnd) का उद्देश्य क्या है?*
- **(A)** Track unacknowledged packets
- **(B)** Control the sending rate to avoid network congestion
- **(C)** Handle encryption
- **(D)** Prioritize packets
✔ **(B) Control the sending rate to avoid network congestion**
★ **Nukta:** TCP की effective window = min(rwnd, cwnd) — flow और congestion दोनों का संतुलन.
*TCP की effective window = min(rwnd, cwnd) — flow और congestion दोनों का संतुलन.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q508.** What kind of delay does TCP's window size help handle on a long, high-bandwidth path?
*लंबी, high-bandwidth path पर TCP का window size किस प्रकार की देर संभालने में मदद करता है?*
- **(A)** Transmission delay
- **(B)** Queuing delay
- **(C)** Propagation delay
- **(D)** Bandwidth-delay product
✔ **(D) Bandwidth-delay product**
★ **Nukta:** Window ≥ BDP हो तो link बेकार नहीं बैठती — यही high-speed long links का सूत्र है.
*Window ≥ BDP हो तो link बेकार नहीं बैठती — यही high-speed long links का सूत्र है.*
*[Source: CN Topic Test 5.pdf] · Medium*

**Q509.** In which protocol is 'port knocking' used as a security mechanism?
*किस protocol में 'port knocking' security mechanism के रूप में उपयोग होता है?*
- **(A)** TCP
- **(B)** UDP
- **(C)** SSH
- **(D)** IP
✔ **(C) SSH**
★ **Nukta:** Port knocking = 'secret door knock' — पहचान होते ही असली दरवाज़ा (SSH) खुलता है.
*Port knocking = 'secret door knock' — पहचान होते ही असली दरवाज़ा (SSH) खुलता है.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q510.** Which of the following supports QoS (Quality of Service) through label switching?
*निम्न में से कौन-सा label switching के ज़रिए QoS (Quality of Service) देता है?*
- **(A)** TCP
- **(B)** UDP
- **(C)** MPLS
- **(D)** ARP
✔ **(C) MPLS**
★ **Nukta:** MPLS = fast path + QoS classes; DiffServ/IntServ भी QoS के तरीके हैं.
*MPLS = fast path + QoS classes; DiffServ/IntServ भी QoS के तरीके हैं.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q511.** Virtual circuits are associated with which type of service?
*Virtual circuits किस प्रकार की service से जुड़े हैं?*
- **(A)** Connectionless service
- **(B)** Error-free service
- **(C)** Segmentation
- **(D)** Connection-oriented service
✔ **(D) Connection-oriented service**
★ **Nukta:** Virtual circuit = पहले connection, फिर data (connection-oriented); Datagram = हर packet अपने-आप (connectionless).
*Virtual circuit = पहले connection, फिर data (connection-oriented); Datagram = हर packet अपने-आप (connectionless).*
*[Source: CN Topic Test-02.pdf] · Medium*

**Q512.** Transport layer multiplexing allows:
*Transport layer multiplexing की अनुमति देता है:*
- **(A)** Multiple hosts to share one IP
- **(B)** Multiple processes to share one network connection
- **(C)** Multiple routers to share a routing table
- **(D)** Domain name resolution
✔ **(B) Multiple processes to share one network connection**
★ **Nukta:** Ports ही multiplexing के हथियार हैं — browser 443, mail 25, सब एक साथ.
*Ports ही multiplexing के हथियार हैं — browser 443, mail 25, सब एक साथ.*
*[Source: BCI_SCI Subject Test-7.pdf] · Medium*

**Q513.** Which protocol must use both TCP and UDP for different operations?
*कौन-सा protocol अलग-अलग कामों के लिए TCP और UDP दोनों उपयोग करता है?*
- **(A)** DNS
- **(B)** HTTP
- **(C)** POP3
- **(D)** Telnet
✔ **(A) DNS**
★ **Nukta:** DNS = port 53; UDP for small queries, TCP for big/zone transfers.
*DNS = port 53; UDP for small queries, TCP for big/zone transfers.*
*[Source: BCI Subject Test-8.pdf + CN Topic Test 5.pdf] · Medium*

**Q514.** Which transport-layer protocol is used to support electronic mail delivery between machines?
*Machines के बीच electronic mail delivery के लिए कौन-सा transport-layer protocol उपयोग होता है?*
- **(A)** SNMP
- **(B)** IP
- **(C)** SMTP
- **(D)** TCP
✔ **(D) TCP**
★ **Nukta:** प्रश्न 'transport-layer protocol' पूछ रहा है — SMTP application layer का है, TCP transport का.
*प्रश्न 'transport-layer protocol' पूछ रहा है — SMTP application layer का है, TCP transport का.*
*[Source: CN Topic Test-03.pdf] · Medium*

**Q515.** How many bits are used for port addressing at the transport layer?
*Transport layer पर port addressing के लिए कितने bits उपयोग होते हैं?*
- **(A)** 8
- **(B)** 10
- **(C)** 16
- **(D)** 32
✔ **(C) 16**
★ **Nukta:** Addresses का स्तर: Data link = 48-bit MAC; Network = 32-bit IP; Transport = 16-bit port.
*Addresses का स्तर: Data link = 48-bit MAC; Network = 32-bit IP; Transport = 16-bit port.*
*[Source: BCI_SCI Subject Test-7.pdf] · Hard*

**Q516.** The three-way handshake mechanism in TCP aims to:
*TCP का three-way handshake mechanism किस उद्देश्य से होता है?*
- **(A)** Secure the communication
- **(B)** Send bits from one device to another
- **(C)** Perform error detection and correction
- **(D)** Establish a connection and synchronize sequence numbers
✔ **(D) Establish a connection and synchronize sequence numbers**
★ **Nukta:** RPSC official key (d). SYN, SYN-ACK, ACK — तीन ही संदेश.
*RPSC official key (d). SYN, SYN-ACK, ACK — तीन ही संदेश.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q517.** What type of attack is prevented by using random initial sequence numbers in TCP?
*TCP में random initial sequence numbers उपयोग करने से किस प्रकार की attack रुकती है?*
- **(A)** Smurf attack
- **(B)** SYN Flooding
- **(C)** TCP session hijacking
- **(D)** Ping of Death
✔ **(C) TCP session hijacking**
★ **Nukta:** Predictable sequence numbers = session hijacking का दरवाज़ा.
*Predictable sequence numbers = session hijacking का दरवाज़ा.*
*[Source: CN Topic Test 5.pdf] · Hard*

**Q518.** Which field in the TCP header is used for flow control?
*TCP header में flow control के लिए कौन-सा field उपयोग होता है?*
- **(A)** Window Size
- **(B)** Sequence Number
- **(C)** Acknowledgment Number
- **(D)** Checksum
✔ **(A) Window Size**
★ **Nukta:** TCP के दो घरेलू नियंत्रण: Window (flow control) और cwnd (congestion control).
*TCP के दो घरेलू नियंत्रण: Window (flow control) और cwnd (congestion control).*
*[Source: CN Topic Test 6.pdf] · Hard*

**Q519.** Which TCP header field ensures that data arrives in order?
*TCP header का कौन-सा field सुनिश्चित करता है कि data क्रम में पहुँचे?*
- **(A)** Checksum
- **(B)** Flags
- **(C)** Sequence Number
- **(D)** Port Number
✔ **(C) Sequence Number**
★ **Nukta:** UDP has no sequence numbers — that is why it gives no ordering guarantee.
*UDP में sequence नहीं होता — इसीलिए वहाँ क्रम की guarantee नहीं.*
*[Source: CN Topic Test 5.pdf] · Hard*

**Q520.** Which field in the TCP header ensures data integrity?
*TCP header का कौन-सा field data integrity सुनिश्चित करता है?*
- **(A)** Urgent Pointer
- **(B)** Sequence Number
- **(C)** Checksum
- **(D)** Acknowledgment Number
✔ **(C) Checksum**
★ **Nukta:** Integrity = Checksum (TCP/UDP/IP); reliability = ACK + retransmission.
*Integrity = Checksum (TCP/UDP/IP); reliability = ACK + retransmission.*
*[Source: CN Topic Test 5.pdf] · Hard*

**Q521.** Which of the following is NOT a property of TCP?
*निम्न में से कौन-सा TCP का गुण नहीं है?*
- **(A)** Reliable
- **(B)** Ordered delivery
- **(C)** Connection-oriented
- **(D)** Broadcast
✔ **(D) Broadcast**
★ **Nukta:** TCP = reliable + ordered + connection-oriented; बाकी सब (broadcast) UDP की तरफ़ जाता है.
*TCP = reliable + ordered + connection-oriented; बाकी सब (broadcast) UDP की तरफ़ जाता है.*
*[Source: CN Topic Test 5.pdf] · Hard*

**Q522.** Which of the following provides reliable, connection-oriented communication?
*निम्न में से कौन-सा भरोसेमंद, connection-oriented communication देता है?*
- **(A)** TCP
- **(B)** IP
- **(C)** UDP
- **(D)** All of the above
✔ **(A) TCP**
★ **Nukta:** याद रखो: TCP = phone call (connection + guarantee); UDP = postcard (fast, no promise).
*याद रखो: TCP = phone call (connection + guarantee); UDP = postcard (fast, no promise).*
*[Source: MQuestions DCN bank + Oliveboard SSC CGL bank] · Hard*

**Q523.** Which of the following statements about TCP/IP is INCORRECT?
*TCP/IP के बारे में निम्न में से कौन-सा कथन गलत है?*
- **(A)** TCP/IP has high latency
- **(B)** Data packets sent over TCP/IP are private
- **(C)** TCP is used by Secure Shell (SSH)
- **(D)** TCP/IP uses checksums to check errors
✔ **(B) Data packets sent over TCP/IP are private**
★ **Nukta:** DSSSB का official key (b). याद रखो: Internet = open postcard, ताला (encryption) खुद लगाओ.
*DSSSB का official key (b). याद रखो: Internet = open postcard, ताला (encryption) खुद लगाओ.*
*[Source: DSSSB TGT CS (via Testbook solved)] · Hard*

**Q524.** Why are port numbers included in the TCP header of a segment?
*Segment के TCP header में port numbers क्यों रखे जाते हैं?*
- **(A)** To indicate the correct router interface for forwarding
- **(B)** To identify which switch ports should receive the frame
- **(C)** To determine which Layer 3 protocol encapsulates the data
- **(D)** To enable a receiving host to forward the data to the appropriate application
✔ **(D) To enable a receiving host to forward the data to the appropriate application**
★ **Nukta:** RPSC 2011 official key (4). यही transport-layer multiplexing है.
*RPSC 2011 official key (4). यही transport-layer multiplexing है.*
*[Source: RPSC Programmer 2011 Paper-1 (via pyqp.in)] · Hard*

**Q525.** Which one of the following fields of an IP header is NOT modified by a typical IP router?
*IP header का कौन-सा field एक सामान्य IP router द्वारा संशोधित नहीं किया जाता?*
- **(A)** Checksum
- **(B)** Source address
- **(C)** Time to Live (TTL)
- **(D)** Length
✔ **(B) Source address**
★ **Nukta:** Checksum aur TTL router ke haath badalte hain; length fragmentation se badal sakti hai.
*Checksum/TTL बदलते हैं; length fragmentation से बदल सकती है।*
*[Source: GATE CS 2015 Set-1] · Hard*

**Q526.** Which of the following fields of an IP header is/are ALWAYS modified by any router before it forwards the IP packet?
*IP packet forward करने से पहले हर router IP header के कौन-से fields हमेशा बदलता है?*
- **(A)** TTL only / केवल TTL
- **(B)** Checksum only / केवल Checksum
- **(C)** TTL and header checksum / TTL और header checksum
- **(D)** Source address and TTL / Source address और TTL
✔ **(C) TTL and header checksum**
★ **Nukta:** Checksum ko optional samajhna galti hai — TTL badalne par checksum invalid ho jata hai.
*Checksum optional नहीं — TTL बदलते ही checksum अमान्य हो जाता है।*
*[Source: GATE CS 2024 Set-2] · Hard*

**Q527.** Which of the following fields is/are modified in the IP header of a packet going out of a Network Address Translation (NAT) device from an internal network to an external network?
*NAT device से internal network से external network की तरफ़ जाते packet के IP header में कौन-से fields बदले जाते हैं?*
- **(A)** Source IP address only / केवल Source IP address
- **(B)** Destination IP address only / केवल Destination IP address
- **(C)** Source IP address and header checksum / Source IP address और header checksum
- **(D)** TTL and destination address / TTL और destination address
✔ **(C) Source IP address and header checksum**
★ **Nukta:** Destination address wahi rehta hai (jana to server ko hi hai); TTL alag cheez hai.
*Destination वही रहता है; TTL अलग चीज़ है।*
*[Source: GATE CS 2024 Set-1] · Hard*

**Q528.** Consider sending an IP datagram of size 1420 bytes (including a 20-byte IP header) over a path of two links with a router between them. The first link has MTU 542 bytes and the second link has MTU 360 bytes. The number of fragments delivered at the receiver is ______.
*1420 bytes का IP datagram (20-byte header सहित) दो links के रास्ते भेजा जा रहा है, बीच में एक router है। पहले link का MTU 542 bytes और दूसरे का 360 bytes है। Receiver पर कुल कितने fragments पहुँचेंगे?*
- **(A)** 4
- **(B)** 5
- **(C)** 6
- **(D)** 8
✔ **(C) 6**
★ **Nukta:** 5/8 fragmentation ko sirf ek baar maante hain; 4 total data ko 360 se seedha bhaag dete hain.
*5/8 fragmentation एक ही बार मानते हैं; 4 सीधे 360 से भाग देते हैं।*
*[Source: GATE CS 2024 Set-1] · Hard*

**Q529.** In an IPv4 datagram, the M bit is 0, the value of HLEN is 10, the value of total length is 400 and the fragment offset value is 300. The position of the datagram, and the sequence numbers of the first and the last bytes of the payload, respectively, are:
*एक IPv4 datagram में M bit = 0, HLEN = 10, total length = 400 और fragment offset = 300 है। इस datagram की स्थिति तथा payload के पहले और आख़िरी bytes के sequence numbers क्रमशः हैं:*
- **(A)** Last fragment, 2400 and 2759 / Last fragment, 2400 और 2759
- **(B)** First fragment, 2400 and 2759 / First fragment, 2400 और 2759
- **(C)** Last fragment, 300 and 659 / Last fragment, 300 और 659
- **(D)** Last fragment, 2400 and 2779 / Last fragment, 2400 और 2779
✔ **(A) Last fragment, 2400 and 2759**
★ **Nukta:** Offset ko byte nahi 8-byte units mein count karna zaroori hai; 2779 header ko do baar jod deta hai.
*Offset 8-byte units में होता है; 2779 header दो बार जोड़ता है।*
*[Source: GATE CS 2013] · Hard*

**Q530.** Consider the following three statements about link state and distance vector routing protocols for a large network with 500 nodes and 4000 links:
S1: The computational overhead in link state protocols is higher than in distance vector protocols.
S2: A distance vector protocol (with split horizon) avoids persistent routing loops, but a link state protocol does not.
S3: After a topology change, a link state protocol converges faster than a distance vector protocol.
Which one is correct?
*500 nodes और 4000 links वाले बड़े network के लिए link state व distance vector routing protocols के बारे में तीन कथन:
S1: Link state में computational overhead distance vector से अधिक है।
S2: Distance vector (split horizon सहित) persistent loops से बचता है, पर link state नहीं।
S3: Topology बदलने पर link state, distance vector से तेज़ converge करता है।
कौन-सा सही है?*
- **(A)** S1, S2 and S3 are all true / S1, S2, S3 तीनों सही
- **(B)** S1, S2 and S3 are all false / S1, S2, S3 तीनों गलत
- **(C)** S1 and S2 are true, S3 is false / S1 और S2 सही, S3 गलत
- **(D)** S1 and S3 are true, S2 is false / S1 और S3 सही, S2 गलत
✔ **(D) S1 and S3 are true, S2 is false**
★ **Nukta:** S2 ulta hai — split horizon count-to-infinity se poora bachata bhi nahi.
*S2 उल्टा — split horizon count-to-infinity से पूरा बचाता भी नहीं।*
*[Source: GATE CS 2014 Set-1] · Hard*

**Q531.** Which one of the following is TRUE about the interior gateway routing protocols RIP (Routing Information Protocol) and OSPF (Open Shortest Path First)?
*Interior gateway routing protocols RIP (Routing Information Protocol) और OSPF (Open Shortest Path First) के बारे में कौन-सा कथन सही है?*
- **(A)** RIP uses distance vector routing and OSPF uses link state routing / RIP distance vector और OSPF link state routing प्रयोग करता है
- **(B)** OSPF uses distance vector routing and RIP uses link state routing / OSPF distance vector और RIP link state routing प्रयोग करता है
- **(C)** Both RIP and OSPF use link state routing / दोनों link state routing प्रयोग करते हैं
- **(D)** Both RIP and OSPF use distance vector routing / दोनों distance vector routing प्रयोग करते हैं
✔ **(A) RIP uses distance vector routing and OSPF uses link state routing**
★ **Nukta:** Dono ko ek hi category mein daalna common galti hai.
*दोनों को एक श्रेणी में डालना आम गलती।*
*[Source: GATE CS 2014 Set-2] · Hard*

**Q532.** Consider the following statements about the functionality of an IP based router:
I. A router does not modify the IP packets during forwarding.
II. It is not necessary for a router to implement any routing protocol.
III. A router should reassemble IP fragments if the MTU of the outgoing link is larger than the size of the incoming IP packet.
Which of the above statement(s) is/are TRUE?
*IP आधारित router की कार्यप्रणाली के बारे में विचार:
I. Router forwarding के दौरान IP packets को संशोधित नहीं करता।
II. Router के लिए कोई routing protocol लागू करना आवश्यक नहीं है।
III. यदि outgoing link का MTU आने वाले packet से बड़ा हो तो router को fragments जोड़ने चाहिए।
इनमें कौन-सा कथन सही है?*
- **(A)** I only / केवल I
- **(B)** II only / केवल II
- **(C)** I and III only / केवल I और III
- **(D)** None of the above / कोई नहीं
✔ **(B) II only**
★ **Nukta:** Fragmentation ke baad re-fragmentation ka kaam router ka hai, jodna nahi.
*Router re-fragment कर सकता है, जोड़ता नहीं।*
*[Source: GATE CS 2020] · Hard*

**Q533.** Host A (on TCP/IPv4 network A) sends an IP datagram D to host B (on TCP/IPv4 network B) with no transmission error. When D reaches B, which of the following IP header field(s) may be different from that of the original datagram D?
I. TTL    II. Checksum    III. Fragment Offset
*Host A ने (TCP/IPv4 network A से) बिना किसी त्रुटि के IP datagram D, host B को भेजा। D के B पर पहुँचने पर निम्न में से कौन-से IP header fields मूल datagram से भिन्न हो सकते हैं?
I. TTL    II. Checksum    III. Fragment Offset*
- **(A)** I only / केवल I
- **(B)** II and III only / केवल II और III
- **(C)** I and II only / केवल I और II
- **(D)** I, II and III / I, II और III तीनों
✔ **(D) I, II and III**
★ **Nukta:** Offset ko 'sirf fragmentation ke time' samajh kar chhod dena galti hai — puchha hai 'ho sakta hai'.
*Offset को छोड़ देना गलती — पूछा है 'हो सकता है'।*
*[Source: GATE CS 2014 Set-3] · Hard*

## Section E — Session, Presentation & Application Layer

*Presentation-layer functions, application protocols & ports (HTTP/HTTPS/FTP/SMTP/DNS/SSH/Telnet/NFS/LDAP), TCP/IP layer-protocol matching.*

**Upar ki 3 layers: sessions sambhalna, data ka format, aur user ki services. Application layer ke protocols aur unke ports — exam ka constant area.**

*ऊपर की 3 layers: sessions, data format, और user services। Application protocols और उनके ports।*

- Session layer — dialog control (simplex/half/full dialogs), synchronization checkpoints (sync points) se recovery.
  - *Session layer — dialog control, synchronization checkpoints।*
- Presentation layer — translation (ASCII/EBCDIC), encryption/decryption, compression — 'data ki presentation'.
  - *Presentation layer — translation, encryption, compression।*
- Application layer — user ke liye services: HTTP (web), FTP (files), SMTP/POP3/IMAP (mail), DNS (naam), DHCP (auto IP), SNMP (management).
  - *Application layer — HTTP, FTP, SMTP/POP3/IMAP, DNS, DHCP, SNMP।*
- Ports: HTTP 80, HTTPS 443, FTP 20/21, SSH 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, POP3 110, IMAP 143, SNMP 161/162, RIP 520.
  - *Ports: HTTP 80, HTTPS 443, FTP 20/21, SMTP 25, DNS 53, POP3 110...।*
- E-mail: SMTP se bhejte hain (push), POP3 download karta hai, IMAP server par hi manage karta hai.
  - *E-mail: SMTP (भेजना), POP3 (लाना), IMAP (server पर manage)।*
- FTP — control (21) + data (20) connections; active/passive modes.
  - *FTP — control + data connections।*
- HTTP — stateless, request/response (GET, POST); HTTPS = HTTP + SSL/TLS encryption.
  - *HTTP — stateless; HTTPS = HTTP + SSL/TLS।*
- Domain name hierarchy: root → TLD (.com/.in) → domain → host; DNS resolution recursive/iterative.
  - *Domain hierarchy: root → TLD → domain; DNS resolution।*

| Protocol | Port | Kaam |
|---|---|---|
| HTTP / HTTPS | 80 / 443 | web pages |
| FTP | 20/21 | file transfer |
| SMTP / POP3 / IMAP | 25 / 110 / 143 | e-mail |
| DNS | 53 | naam → IP |
| DHCP | 67/68 | auto IP configuration |
| SNMP | 161/162 | network management |
| SSH / Telnet | 22 / 23 | remote login |

### Questions (Easy → Medium → Hard)

**Q534.** A server receives a packet with destination port 443. This implies:
*एक server को destination port 443 वाला packet मिलता है. इसका अर्थ है:*
- **(A)** HTTP request
- **(B)** HTTPS traffic
- **(C)** FTP command
- **(D)** Email traffic
✔ **(B) HTTPS traffic**
★ **Nukta:** Ports: 80=HTTP, 443=HTTPS, 21/20=FTP, 22=SSH, 23=Telnet, 25=SMTP, 53=DNS, 67/68=DHCP.
*Ports: 80=HTTP, 443=HTTPS, 21/20=FTP, 22=SSH, 23=Telnet, 25=SMTP, 53=DNS, 67/68=DHCP.*
*[Source: BCI Subject Test-8.pdf] · Easy*

**Q535.** For what application is the HTTP protocol used?
*HTTP protocol किस काम के लिए उपयोग होता है?*
- **(A)** To increase upload speed
- **(B)** To develop a website
- **(C)** To deliver data on the World Wide Web
- **(D)** To download images only
✔ **(C) To deliver data on the World Wide Web**
★ **Nukta:** SSC MTS official key (3). HTTP = web की धड़कन (port 80).
*SSC MTS official key (3). HTTP = web की धड़कन (port 80).*
*[Source: SSC MTS computer PYQ (via Testbook solved)] · Easy*

**Q536.** The structure or format of data is called:
*Data का structure या format कहलाता है:*
- **(A)** Syntax
- **(B)** Struct
- **(C)** Semantic
- **(D)** None of the above
✔ **(A) Syntax**
★ **Nukta:** Rule: Syntax = how it looks; Semantics = what it means. Both must be agreed for communication.
*नियम: Syntax = कैसा दिखे; Semantics = क्या अर्थ हो. Communication में दोनों तय होने चाहिए.*
*[Source: Unit Test-4 Solution.pdf (OCR), p14] · Medium*

**Q537.** Which protocol layer uses protocols such as WWW, HTTP, FTP, SMTP and e-mail?
*कौन-सी protocol layer WWW, HTTP, FTP, SMTP और e-mail जैसे protocols उपयोग करती है?*
- **(A)** Application layer
- **(B)** Transport layer
- **(C)** Internet layer
- **(D)** Hardware layer
✔ **(A) Application layer**
★ **Nukta:** याद रखो: Layer 7 = सेवाएँ (HTTP/FTP/SMTP/DNS); Layer 4 = TCP/UDP; Layer 3 = IP.
*याद रखो: Layer 7 = सेवाएँ (HTTP/FTP/SMTP/DNS); Layer 4 = TCP/UDP; Layer 3 = IP.*
*[Source: CN Topic Test-02.pdf + CN Topic Test-01.pdf] · Medium*

**Q538.** Which layer protocols provide user and application programme support such as passwords, resource sharing and file transfer?
*किस layer के protocols उपयोगकर्ता और application programme को passwords, resource sharing और file transfer जैसी सहायता देते हैं?*
- **(A)** Layer 2 protocols
- **(B)** Layer 5 protocols
- **(C)** Layer 7 protocols
- **(D)** Layer 10 protocols
✔ **(C) Layer 7 protocols**
★ **Nukta:** OSI has exactly 7 layers — there can be no 'Layer 10'.
*OSI में 7 layers ही हैं — 'Layer 10' तो हो ही नहीं सकती.*
*[Source: CN Topic Test-02.pdf] · Medium*

**Q539.** Which of the following protocols is primarily used for secure web browsing?
*निम्न में से कौन-सा protocol मुख्य रूप से सुरक्षित web browsing के लिए उपयोग होता है?*
- **(A)** FTP
- **(B)** HTTP
- **(C)** HTTPS
- **(D)** SMTP
✔ **(C) HTTPS**
★ **Nukta:** HTTPS का port 443; HTTP का 80. ताला (lock) वाली site = HTTPS.
*HTTPS का port 443; HTTP का 80. ताला (lock) वाली site = HTTPS.*
*[Source: CN Topic Test-01.pdf] · Medium*

**Q540.** Which protocol is generally used to encrypt data between a web browser and a web server?
*Web browser और web server के बीच data encrypt करने के लिए आमतौर पर कौन-सा protocol उपयोग होता है?*
- **(A)** SSL/TLS
- **(B)** Digital Signature
- **(C)** IPSec
- **(D)** TCP
✔ **(A) SSL/TLS**
★ **Nukta:** HTTPS = HTTP over SSL/TLS. IPSec network-level VPN के लिए होता है.
*HTTPS = HTTP over SSL/TLS. IPSec network-level VPN के लिए होता है.*
*[Source: CN Topic Test-01.pdf] · Medium*

**Q541.** Which protocol is used for secure shell (remote) login?
*Secure shell (remote) login के लिए कौन-सा protocol उपयोग होता है?*
- **(A)** FTP
- **(B)** SSH
- **(C)** Telnet
- **(D)** SNMP
✔ **(B) SSH**
★ **Nukta:** SSH = port 22 (encrypted); Telnet = port 23 (सादा, असुरक्षित).
*SSH = port 22 (encrypted); Telnet = port 23 (सादा, असुरक्षित).*
*[Source: CN Topic Test 6.pdf + Medium 30 CN MCQ bank] · Medium*

**Q542.** A firewall blocks all ports except 22. What service remains accessible?
*एक firewall port 22 को छोड़कर सब बंद कर देता है. कौन-सी सेवा अभी भी खुली है?*
- **(A)** FTP
- **(B)** SSH
- **(C)** HTTPS
- **(D)** SMTP
✔ **(B) SSH**
★ **Nukta:** Identify the port, identify the service — that is the trick of this question.
*Port पहचानो, सेवा पहचानो — यही इस प्रश्न का खेल है.*
*[Source: BCI Subject Test-8.pdf] · Medium*

**Q543.** Which port does Telnet use by default?
*Telnet डिफ़ॉल्ट रूप से कौन-सा port उपयोग करता है?*
- **(A)** 21
- **(B)** 23
- **(C)** 22
- **(D)** 25
✔ **(B) 23**
★ **Nukta:** याद रखो: 22 = SSH, 23 = Telnet, 25 = SMTP, 21 = FTP.
*याद रखो: 22 = SSH, 23 = Telnet, 25 = SMTP, 21 = FTP.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q544.** Which of the following uses port number 25?
*निम्न में से कौन-सा port number 25 उपयोग करता है?*
- **(A)** FTP
- **(B)** HTTP
- **(C)** SMTP
- **(D)** Telnet
✔ **(C) SMTP**
★ **Nukta:** Mail ports: 25 (SMTP), 110 (POP3), 143 (IMAP).
*Mail ports: 25 (SMTP), 110 (POP3), 143 (IMAP).*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q545.** Which protocol uses different ports for control and data connections?
*कौन-सा protocol control और data connections के लिए अलग-अलग ports उपयोग करता है?*
- **(A)** FTP
- **(B)** HTTP
- **(C)** DNS
- **(D)** Telnet
✔ **(A) FTP**
★ **Nukta:** FTP = double connection (control + data); HTTP/SMTP/DNS में ऐसा नहीं.
*FTP = double connection (control + data); HTTP/SMTP/DNS में ऐसा नहीं.*
*[Source: BCI_SCI Subject Test-7.pdf] · Medium*

**Q546.** Which protocol is used for file transfer over a network?
*Network पर file transfer के लिए कौन-सा protocol उपयोग होता है?*
- **(A)** FTP
- **(B)** HTTP
- **(C)** DNS
- **(D)** ARP
✔ **(A) FTP**
★ **Nukta:** HTTP से भी files मिलती हैं, पर 'file transfer' का नाम protocol FTP है.
*HTTP से भी files मिलती हैं, पर 'file transfer' का नाम protocol FTP है.*
*[Source: CN Topic Test 6.pdf + Medium 30 CN MCQ bank] · Medium*

**Q547.** Which application allows a user to access and use remote files without actually transferring them?
*कौन-सा application उपयोगकर्ता को remote files को बिना वास्तव में स्थानांतरित किए उपयोग करने देता है?*
- **(A)** DNS
- **(B)** FTP
- **(C)** NFS
- **(D)** Telnet
✔ **(C) NFS**
★ **Nukta:** NFS = remote files को local जैसा जोड़ना; FTP = files की असल copy भेजना.
*NFS = remote files को local जैसा जोड़ना; FTP = files की असल copy भेजना.*
*[Source: SSC CGL Internet & Networking (via EduRev bank)] · Medium*

**Q548.** Which protocol translates domain names to IP addresses?
*कौन-सा protocol domain names को IP addresses में बदलता है?*
- **(A)** DHCP
- **(B)** DNS
- **(C)** HTTP
- **(D)** FTP
✔ **(B) DNS**
★ **Nukta:** DNS = name→IP; ARP = IP→MAC; DHCP = IP बाँटना.
*DNS = name→IP; ARP = IP→MAC; DHCP = IP बाँटना.*
*[Source: CN Topic Test 5.pdf + CN Topic Test-01.pdf] · Medium*

**Q549.** What does a 'ping' command test?
*'ping' command क्या जाँचता है?*
- **(A)** IP configuration
- **(B)** Host reachability
- **(C)** DNS resolution
- **(D)** Port scanning
✔ **(B) Host reachability**
★ **Nukta:** ping = 'क्या तुम वहाँ हो?' — reachability + round-trip time.
*ping = 'क्या तुम वहाँ हो?' — reachability + round-trip time.*
*[Source: CN Topic Test 6.pdf] · Medium*

**Q550.** Which HTTP status code means 'Forbidden'?
*कौन-सा HTTP status code का अर्थ है 'Forbidden'?*
- **(A)** 200
- **(B)** 301
- **(C)** 403
- **(D)** 404
✔ **(C) 403**
★ **Nukta:** याद रखो: 200 OK, 301 Moved, 403 Forbidden, 404 Not Found, 500 Server Error.
*याद रखो: 200 OK, 301 Moved, 403 Forbidden, 404 Not Found, 500 Server Error.*
*[Source: Oliveboard SSC CGL Tier-2 bank] · Medium*

**Q551.** Lightweight Directory Access Protocol (LDAP) is used for:
*Lightweight Directory Access Protocol (LDAP) किस काम आता है?*
- **(A)** Routing the packets
- **(B)** Authentication and directory access
- **(C)** Obtaining an IP address
- **(D)** Domain name resolving
✔ **(B) Authentication and directory access**
★ **Nukta:** LDAP = the network's 'address book + identity-desk counter'.
*LDAP = network का 'पता-पुस्तिका + पहचान-पत्र काउंटर'.*
*[Source: Unit Test-4 Solution.pdf (OCR), p29] · Medium*

**Q552.** Which protocol is used for receiving an email?
*Email प्राप्त करने के लिए कौन-सा protocol उपयोग होता है?*
- **(A)** HTTP
- **(B)** FTP
- **(C)** POP3
- **(D)** SSH
✔ **(C) POP3**
★ **Nukta:** Mail की जोड़ी: भेजो SMTP (25), लो POP3 (110) या IMAP (143).
*Mail की जोड़ी: भेजो SMTP (25), लो POP3 (110) या IMAP (143).*
*[Source: RRB NTPC previous-year computer banks (via adda247 50-PYQ PDF)] · Medium*

**Q553.** Which of the following is the odd one out?
*निम्न में से असंगत कौन-सा है?*
- **(A)** IMAP
- **(B)** POP
- **(C)** SNMP
- **(D)** SMTP
✔ **(C) SNMP**
★ **Nukta:** Mail family: SMTP/POP3/IMAP; Management family: SNMP.
*Mail family: SMTP/POP3/IMAP; Management family: SNMP.*
*[Source: RRB NTPC previous-year computer banks (via adda247 50-PYQ PDF)] · Medium*

**Q554.** ICMP is a network-layer protocol used by devices to diagnose network issues. ICMP stands for:
*ICMP network-layer protocol है जो devices को network समस्याएँ जाँचने में सहायता करता है. ICMP का पूरा नाम है:*
- **(A)** Internet Control Manage Process
- **(B)** Internet Comfort Mass Protocol
- **(C)** Information Control Manage Protocol
- **(D)** Internet Control Message Protocol
✔ **(D) Internet Control Message Protocol**
★ **Nukta:** The other names are made up — the real name contains 'Control Message'.
*बाकी नाम बनावटी हैं — असली नाम में 'Control Message' आता है.*
*[Source: IBPS PO Computer Awareness PYQ (via Testbook solved)] · Medium*

**Q555.** POP3 stands for:
*POP3 का पूरा नाम है:*
- **(A)** Peer to Peer Protocol
- **(B)** Peer to Post Protocol
- **(C)** Peer Office Protocol
- **(D)** Post Office Protocol
✔ **(D) Post Office Protocol**
★ **Nukta:** POP = Post Office Protocol. याद रखो: POP3 mail लाता है, SMTP भेजता है.
*POP = Post Office Protocol. याद रखो: POP3 mail लाता है, SMTP भेजता है.*
*[Source: SBI/IBPS Computer Awareness Capsule 2018 (IBT India)] · Medium*

**Q556.** SLIP stands for:
*SLIP का पूरा नाम है:*
- **(A)** System Line Internet Protocol
- **(B)** Serial Line Internet Protocol
- **(C)** Signal Line Internet Protocol
- **(D)** Signal Internet Protocol
✔ **(B) Serial Line Internet Protocol**
★ **Nukta:** SLIP का उत्तराधिकारी PPP (byte-oriented) है — दोनों point-to-point.
*SLIP का उत्तराधिकारी PPP (byte-oriented) है — दोनों point-to-point.*
*[Source: IBPS/banking computer banks (via tpointtech MCQ)] · Medium*

**Q557.** The functionalities of the presentation layer include:
*Presentation layer के कार्यों में शामिल हैं:*
- **(A)** Data compression
- **(B)** Data encryption
- **(C)** Data description (translation)
- **(D)** All of the mentioned
✔ **(D) All of the mentioned**
★ **Nukta:** Presentation = data का मेकअप (रूप, रंग, सुरक्षा); Application = सेवाएँ.
*Presentation = data का मेकअप (रूप, रंग, सुरक्षा); Application = सेवाएँ.*
*[Source: CN Topic Test-02.pdf] · Hard*

**Q558.** Which of the following protocols is NOT secure?
*निम्न में से कौन-सा protocol सुरक्षित नहीं है?*
- **(A)** HTTPS
- **(B)** FTP
- **(C)** SSH
- **(D)** SFTP
✔ **(B) FTP**
★ **Nukta:** असुरक्षित की सूची: HTTP, FTP, Telnet, SMTP (बिना TLS). सुरक्षित: HTTPS, SFTP, SSH, SMTPS.
*असुरक्षित की सूची: HTTP, FTP, Telnet, SMTP (बिना TLS). सुरक्षित: HTTPS, SFTP, SSH, SMTPS.*
*[Source: CN Topic Test 6.pdf] · Hard*

**Q559.** Which of the following protocols is used for transferring email messages from one machine to another?
*निम्न में से कौन-सा protocol email संदेशों को एक machine से दूसरी में भेजने के लिए उपयोग होता है?*
- **(A)** SNMP
- **(B)** FTP
- **(C)** TELNET
- **(D)** SMTP
✔ **(D) SMTP**
★ **Nukta:** RPSC official key (d). भेजना = SMTP; लेना = POP3/IMAP.
*RPSC official key (d). भेजना = SMTP; लेना = POP3/IMAP.*
*[Source: RPSC Programmer 2024 Paper-1 (with official key)] · Hard*

**Q560.** In one of the pairs below, both protocols can use multiple TCP connections between the same client and the same server. Which pair is it?
*नीचे दिए जोड़ों में से किसमें दोनों protocols एक ही client और server के बीच कई TCP connections उपयोग कर सकते हैं?*
- **(A)** HTTP, FTP
- **(B)** HTTP, TELNET
- **(C)** FTP, SMTP
- **(D)** HTTP, SMTP
✔ **(A) HTTP, FTP**
★ **Nukta:** दोनों 'multi-connection' protocols हैं — यही जोड़ी पूछी गई है.
*दोनों 'multi-connection' protocols हैं — यही जोड़ी पूछी गई है.*
*[Source: CN Topic Test-02.pdf] · Hard*

**Q561.** Identify the true statements: (1) HTTP may use different TCP connections for different objects of a webpage if non-persistent connections are used (2) FTP uses two TCP connections, one for data and another for control (3) TELNET and FTP can only use TWO connections at a time
*सही कथन पहचानें: (1) non-persistent connections में HTTP webpage के अलग-अलग objects के लिए अलग TCP connections उपयोग कर सकता है (2) FTP दो TCP connections उपयोग करता है, एक data के लिए और दूसरा control के लिए (3) TELNET और FTP एक समय में केवल TWO connections ही उपयोग कर सकते हैं*
- **(A)** (1) only
- **(B)** (1) and (2)
- **(C)** (2) and (3)
- **(D)** (1), (2) and (3)
✔ **(B) (1) and (2)**
★ **Nukta:** HTTP = multi-connection capable; FTP = दो का जोड़ा; 'only two' का नियम कहीं नहीं.
*HTTP = multi-connection capable; FTP = दो का जोड़ा; 'only two' का नियम कहीं नहीं.*
*[Source: CN Topic Test-03.pdf] · Hard*

**Q562.** Which of the following is NOT an application layer protocol?
*निम्न में से कौन-सा application layer protocol नहीं है?*
- **(A)** HTTP
- **(B)** IP
- **(C)** TELNET
- **(D)** FTP
✔ **(B) IP**
★ **Nukta:** Layer 7 के नाम: HTTP, FTP, SMTP, DNS, Telnet, SNMP, DHCP, TFTP...
*Layer 7 के नाम: HTTP, FTP, SMTP, DNS, Telnet, SNMP, DHCP, TFTP...*
*[Source: SSC CGL Internet & Networking (via EduRev bank)] · Hard*

**Q563.** Which is the FALSE statement?
*कौन-सा कथन गलत है?*
- **(A)** Telnet is used for remote login
- **(B)** FTP can transfer files between two hosts
- **(C)** TFTP relies on TCP
- **(D)** SMTP is used to send mail messages
✔ **(C) TFTP relies on TCP**
★ **Nukta:** TFTP = छोटा भाई (UDP, port 69); FTP = बड़ा भाई (TCP, ports 20/21).
*TFTP = छोटा भाई (UDP, port 69); FTP = बड़ा भाई (TCP, ports 20/21).*
*[Source: SSC CGL Internet & Networking (via EduRev bank)] · Hard*

**Q564.** Match TCP/IP layers and protocols — (P) Transport layer (Q) Network (internet) layer (R) Application layer; (1) ICMP (2) FTP (3) UDP. Which matching is correct?
*TCP/IP layers और protocols मिलाएँ — (P) Transport layer (Q) Network (internet) layer (R) Application layer; (1) ICMP (2) FTP (3) UDP. कौन-सा मिलान सही है?*
- **(A)** P-2, Q-1, R-3
- **(B)** P-1, Q-2, R-3
- **(C)** P-3, Q-1, R-2
- **(D)** P-3, Q-2, R-1
✔ **(C) P-3, Q-1, R-2**
★ **Nukta:** Layers याद रखो: Application = FTP/HTTP/SMTP/DNS; Transport = TCP/UDP; Internet = IP/ICMP/IGMP.
*Layers याद रखो: Application = FTP/HTTP/SMTP/DNS; Transport = TCP/UDP; Internet = IP/ICMP/IGMP.*
*[Source: Random Test- Rajasthan PYQ.pdf (OCR) + answer_keys.py Q23] · Hard*

**Q565.** Which one of the following is NOT a client-server application?
*निम्न में से कौन-सा client-server application नहीं है?*
- **(A)** Internet Chat
- **(B)** Web browsing
- **(C)** E-mail
- **(D)** Ping
✔ **(D) Ping**
★ **Nukta:** RPSC 2011 official key (4). Ping = reachability जाँच, application service नहीं.
*RPSC 2011 official key (4). Ping = reachability जाँच, application service नहीं.*
*[Source: RPSC Programmer 2011 Paper-1 (via pyqp.in)] · Hard*

**Q566.** Which of the following is/are example(s) of stateful application layer protocols?
I. HTTP    II. FTP    III. TCP    IV. POP3
*निम्न में से कौन-सा stateful application layer protocol का उदाहरण है?
I. HTTP    II. FTP    III. TCP    IV. POP3*
- **(A)** I and II only / केवल I और II
- **(B)** II only / केवल II
- **(C)** I only / केवल I
- **(D)** II and III only / केवल II और III
✔ **(B) II only**
★ **Nukta:** TCP ko application protocol samajhna option jaal hai; HTTP stateful sirf modern keep-alive mein lagta hai.
*TCP application protocol नहीं; HTTP सिर्फ़ आधुनिक keep-alive में stateful लगता है।*
*[Source: GATE CS 2016 Set-1] · Hard*

**Q567.** Identify the correct sequence in which the following packets are transmitted by a host when a browser requests a web page from a remote server, assuming that the host has just been restarted:
*मान लीजिए host अभी-अभी restart हुआ है और browser एक remote server से web page माँगता है। निम्न packets सही क्रम में transmit होंगे:*
- **(A)** HTTP GET request, DNS query, TCP SYN
- **(B)** DNS query, HTTP GET request, TCP SYN
- **(C)** DNS query, TCP SYN, HTTP GET request
- **(D)** TCP SYN, DNS query, HTTP GET request
✔ **(C) DNS query, TCP SYN, HTTP GET request**
★ **Nukta:** GET pehle ja hi nahi sakta — connection bina handshake ke nahi banti; restart yaani DNS cache bhi khaali.
*GET पहले नहीं जा सकता; restart में DNS cache भी ख़ाली।*
*[Source: GATE CS 2016 Set-2] · Hard*

**Q568.** Which of the following protocol pairs can be used to send and retrieve e-mails (in that order)?
*ई-मेल भेजने और प्राप्त करने (इसी क्रम में) के लिए निम्न में से किस protocol जोड़ी का प्रयोग हो सकता है?*
- **(A)** SMTP and POP3 / SMTP और POP3
- **(B)** POP3 and SMTP / POP3 और SMTP
- **(C)** IMAP and SMTP / IMAP और SMTP
- **(D)** SMTP and IMAP only / केवल SMTP और IMAP
✔ **(A) SMTP and POP3**
★ **Nukta:** Ulti jodi (POP3 and SMTP) order ke against hai; IMAP bhi retrieve karta hai par sabse common jodi SMTP+POP3 hai.
*उल्टी जोड़ी गलत; IMAP भी retrieve करता है पर सबसे सामान्य जोड़ी SMTP+POP3।*
*[Source: GATE CS 2019] · Hard*

**Q569.** Consider a long-lived TCP session with an end-to-end bandwidth of 1 Gbps (= 10⁹ bits/second). The session starts with a sequence number of 1234. The minimum time (in seconds, rounded to the closest integer) before this sequence number can be used again is ______.
*एक लंबी TCP session की bandwidth 1 Gbps (= 10⁹ bits/second) है और वह sequence number 1234 से शुरू होती है। इस sequence number के पुनः प्रयोग से पहले न्यूनतम समय (seconds में, निकटतम पूर्णांक) कितना है?*
- **(A)** 34
- **(B)** 35
- **(C)** 43
- **(D)** 32
✔ **(A) 34**
★ **Nukta:** Bits mein hisaab karke 4 s; ya 2³² bits samajh kar galat number — bytes ka chakkar hai.
*Bits में हिसाब लगाना (4 s) या 2³² bits मानना गलत।*
*[Source: GATE CS 2018] · Hard*

**Q570.** In the TCP three-way handshake, host P sends a connection request to Q with SYN = 1, SEQ = X, ACK = 0. Q accepts the connection. Which of the following represents the information in the TCP segment header sent by Q to P?
*TCP three-way handshake में host P, Q को connection request भेजता है: SYN = 1, SEQ = X, ACK = 0। Q connection स्वीकार करता है। Q द्वारा P को भेजे segment header में क्या होगा?*
- **(A)** SYN = 1, SEQ = Y, ACK = X
- **(B)** SYN = 1, SEQ = X, ACK = Y
- **(C)** SYN = 1, SEQ = Y, ACK = X+1
- **(D)** SYN = 0, SEQ = Y, ACK = X+1
✔ **(C) SYN = 1, SEQ = Y, ACK = X+1**
★ **Nukta:** ACK = X galat (yeh khud ko X+1 expect karna hua); SYN=0 second segment jaisa hota.
*ACK = X गलत (X+1 अपेक्षित); SYN=0 दूसरे जैसा।*
*[Source: GATE CS 2021 Set-2] · Hard*

**Q571.** Consider data transfer using TCP over a 1 Gbps link. Assuming that the maximum segment lifetime (MSL) is set to 60 seconds, the minimum number of bits required for the sequence number field of the TCP header, to prevent the sequence number space from wrapping around during the MSL, is ______.
*1 Gbps link पर TCP से data transfer हो रहा है। Maximum segment lifetime (MSL) 60 seconds है। MSL के दौरान sequence number space के wrap होने से बचने के लिए TCP header के sequence number field में न्यूनतम कितने bits चाहिए?*
- **(A)** 32
- **(B)** 33
- **(C)** 34
- **(D)** 36
✔ **(B) 33**
★ **Nukta:** 32 bits mein space 60 s के लिए kam padta hai; 34/36 zyada hain (minimum pucha hai).
*32 कम पड़ता; 34/36 ज़्यादा (न्यूनतम पूछा है)।*
*[Source: GATE CS 2022] · Hard*

**Q572.** A TCP client and server complete data transfer. The client calls close; a FIN segment is sent to the server, which responds with an ACK received by the client. As per the TCP connection state diagram (RFC 793), in which state does the client-side TCP connection wait for the FIN from the server?
*TCP client-server का data transfer पूरा हुआ। Client close करता है; server को FIN जाता है; server का ACK client को मिलता है। RFC 793 की state diagram के अनुसार client-side connection server के FIN की प्रतीक्षा किस state में करती है?*
- **(A)** TIME_WAIT
- **(B)** FIN_WAIT_2
- **(C)** CLOSE_WAIT
- **(D)** LAST_ACK
✔ **(B) FIN_WAIT_2**
★ **Nukta:** TIME_WAIT aakhri state hai (dono FIN ke baad); CLOSE_WAIT server ki hoti hai.
*TIME_WAIT अंत में; CLOSE_WAIT server की।*
*[Source: GATE CS 2017 Set-1] · Hard*

**Q573.** In the TCP three-way handshake, let the three packets exchanged during connection establishment be P1, P2 and P3 in order. Which of the following is TRUE about the TCP header flags set in these packets?
*TCP three-way handshake में connection establishment के दौरान तीन packets P1, P2 और P3 (इसी क्रम में) बदले जाते हैं। इनमें सेट TCP header flags के बारे में क्या सही है?*
- **(A)** P1: SYN; P2: SYN, ACK; P3: ACK
- **(B)** P1: SYN, ACK; P2: ACK; P3: FIN
- **(C)** P1: SYN; P2: ACK; P3: FIN
- **(D)** P1: ACK; P2: SYN; P3: ACK
✔ **(A) P1: SYN; P2: SYN, ACK; P3: ACK**
★ **Nukta:** FIN connection release ka flag hai; pehle packet par ACK kabhi nahi hota.
*FIN release का flag है; पहले packet पर ACK नहीं होता।*
*[Source: GATE CS 2025 Set-1] · Hard*

**Q574.** The World Wide Web (WWW) is:
*World Wide Web (WWW) क्या है?*
- **(A)** another name for the Internet / Internet का दूसरा नाम
- **(B)** a worldwide connection of computers / कंप्यूटरों का विश्वव्यापी जुड़ाव
- **(C)** a worldwide collection of information / सूचना का विश्वव्यापी संग्रह
- **(D)** a collection of linked information residing on computers connected by the Internet / Internet से जुड़े कंप्यूटरों पर रखी link की गई सूचनाओं का संग्रह
✔ **(D) a collection of linked information residing on computers connected by the Internet**
★ **Nukta:** Internet aur WWW ko same bolna sabse common galti hai; 'connection of computers' to network ki paribhasha hai.
*Internet और WWW को एक मानना सबसे आम गलती; 'connection' तो network है।*
*[Source: EMRS PGT Computer Science] · Hard*

# TOPIC 7 — Network Security

## Section A — Security Goals & Attacks

*CIA triad, attack-goal mapping (interception/modification/DoS/spoofing), active vs passive attacks, malware phases, security tools.*

**Security ka maksad: information ko threats se bachana. Core goals = CIA triad (Confidentiality, Integrity, Availability) + Authentication + Non-repudiation.**

*Security का उद्देश्य: information को threats से बचाना। मूल लक्ष्य = CIA triad + Authentication + Non-repudiation।*

- Confidentiality — sirf authorized log dekh sakein (encryption se).
  - *Confidentiality — सिर्फ़ authorized देख सकें (encryption)।*
- Integrity — data badla na jaaye (hash, digital signature se).
  - *Integrity — data बदला न जाए (hash, digital signature)।*
- Availability — resource time par mile (DoS se bachao).
  - *Availability — समय पर उपलब्ध (DoS से बचाव)।*
- Authentication = sahi pehchaan; Non-repudiation = baad mein inkar na ho sake.
  - *Authentication = सही पहचान; Non-repudiation = इनकार न हो सके।*
- Attack goals: Interception (confidentiality par), Modification (integrity par), Interruption/DoS (availability par), Fabrication (authenticity par).
  - *Attack goals: Interception, Modification, Interruption/DoS, Fabrication।*
- Passive attack = sirf sunna/snooping (detection mushkil); Active attack = data badalna/interrupt karna (prevention).
  - *Passive attack = सिर्फ़ सुनना; Active attack = बदलना/रोकना।*
- Common threats: Spoofing (nakli pehchaan), Sniffing (packets sunna), Phishing (nakli sites), Malware: Virus (file ke saath), Worm (apne aap spread), Trojan (nakli software), Time bomb (time trigger).
  - *Threats: Spoofing, Sniffing, Phishing, Virus, Worm, Trojan, Time bomb।*
- Worm resources khaata hai (CPU/memory) — khud spread hota hai, host file ki zaroorat nahi.
  - *Worm resources खाता है — खुद फैलता है।*

| Goal | Kis par hamla | Bachav |
|---|---|---|
| Confidentiality | Interception/Sniffing | Encryption |
| Integrity | Modification | Hash, digital signature |
| Availability | DoS/DDoS | Firewall, redundancy |
| Authenticity | Spoofing/Fabrication | Authentication |

### Questions (Easy → Medium → Hard)

**Q575.** In the virus life cycle, which phase actually performs the malicious activity?
*Virus life cycle में कौन-सा phase वास्तव में malicious activity करता है?*
- **(A)** Infection Phase
- **(B)** Triggering Phase
- **(C)** Dormant Phase
- **(D)** Execution (Payload) Phase
✔ **(D) Execution (Payload) Phase**
★ **Nukta:** Virus phases: Dormant (idle) → Propagation (copy) → Triggering (condition met) → Execution (payload runs).
*Virus phases: Dormant (idle) → Propagation (copy) → Triggering (condition met) → Execution (payload runs)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q576.** Which backup medium provides Write-Once-Read-Many (WORM) functionality?
*कौन-सा backup medium Write-Once-Read-Many (WORM) functionality देता है?*
- **(A)** Hard disk
- **(B)** Magnetic tape
- **(C)** Optical disk (CD-R / DVD-R)
- **(D)** Flash drive
✔ **(C) Optical disk (CD-R / DVD-R)**
★ **Nukta:** WORM = optical write-once media (CD-R/DVD-R/BD-R). Rewritable: HDD, tape (LTO), flash, CD-RW.
*WORM = optical write-once media (CD-R/DVD-R/BD-R)। Rewritable: HDD, tape (LTO), flash, CD-RW।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q577.** Which attack becomes possible if the SAME key is reused many times in symmetric encryption?
*यदि symmetric encryption में एक ही key कई बार उपयोग हो, तो कौन-सा attack संभव हो जाता है?*
- **(A)** Replay attack
- **(B)** Known-plaintext attack
- **(C)** Man-in-the-middle attack
- **(D)** Phishing attack
✔ **(B) Known-plaintext attack**
★ **Nukta:** One-time pads are safe ONLY with a fresh key per message. Reuse → pattern analysis. Exam favourite link: key reuse → known-plaintext.
*One-time pads केवल हर message पर नई key से सुरक्षित हैं। Reuse → pattern analysis। Exam favourite link: key reuse → known-plaintext।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q578.** Which of the following tools is mainly used for password cracking?
*निम्न में से कौन-सा tool मुख्यतः password cracking के लिए उपयोग होता है?*
- **(A)** Wireshark
- **(B)** Nmap
- **(C)** Cain and Abel
- **(D)** Angry IP Scanner
✔ **(C) Cain and Abel**
★ **Nukta:** Security tools: Wireshark = packet analyser, Nmap = port scanner, Cain&Abel = password cracker, Angry IP Scanner = IP scanner, Snort = IDS.
*Security tools: Wireshark = packet analyser, Nmap = port scanner, Cain&Abel = password cracker, Angry IP Scanner = IP scanner, Snort = IDS।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q579.** Which port and IP address scanner is most famous among users?
*Users के बीच सबसे प्रसिद्ध port और IP address scanner कौन-सा है?*
- **(A)** Cain and Abel
- **(B)** Angry IP Scanner
- **(C)** Snort
- **(D)** Ettercap
✔ **(B) Angry IP Scanner**
★ **Nukta:** Cain&Abel = password cracking; Angry IP = IP/port scan; Snort = IDS; Ettercap = sniffing/ARP spoofing.
*Cain&Abel = password cracking; Angry IP = IP/port scan; Snort = IDS; Ettercap = sniffing/ARP spoofing।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q580.** The term 'CIA triad' in information security refers to:
*Information security में 'CIA triad' शब्द किसे कहते हैं?*
- **(A)** Cryptography, Integrity, Authentication
- **(B)** Confidentiality, Integrity, Availability
- **(C)** Confidentiality, Information, Access
- **(D)** Control, Information, Access
✔ **(B) Confidentiality, Integrity, Availability**
★ **Nukta:** CIA = Confidentiality, Integrity, Availability. AAA (authentication, authorisation, accounting) is a separate trio.
*CIA = Confidentiality, Integrity, Availability। AAA (authentication, authorisation, accounting) अलग trio है।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q581.** A modification attack violates which security goal?
*Modification attack कौन-से security लक्ष्य का उल्लंघन करता है?*
- **(A)** Confidentiality
- **(B)** Integrity
- **(C)** Availability
- **(D)** Authentication
✔ **(B) Integrity**
★ **Nukta:** Attack→goal: Eavesdropping/Interception → Confidentiality. Modification → Integrity. DoS/Interruption → Availability. Spoofing → Authentication.
*Attack→goal: Eavesdropping/Interception → Confidentiality। Modification → Integrity। DoS/Interruption → Availability। Spoofing → Authentication।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q582.** Which of the following attacks violates confidentiality?
*निम्न में से कौन-सा attack confidentiality का उल्लंघन करता है?*
- **(A)** Interception
- **(B)** Modification
- **(C)** Fabrication
- **(D)** Interruption
✔ **(A) Interception**
★ **Nukta:** Attack map: Interception→Confidentiality, Modification→Integrity, Fabrication→Authenticity, Interruption→Availability.
*Attack map: Interception→Confidentiality, Modification→Integrity, Fabrication→Authenticity, Interruption→Availability।*
*[Source: Subject Test Solution-1 Part-2 (CN & Security) slides] · Medium*

**Q583.** A Denial of Service (DoS) attack violates which goal?
*Denial of Service (DoS) attack कौन-से लक्ष्य का उल्लंघन करता है?*
- **(A)** Confidentiality
- **(B)** Integrity
- **(C)** Availability
- **(D)** Authentication
✔ **(C) Availability**
★ **Nukta:** DoS = Availability attack. DDoS = distributed DoS. Smurf/ SYN-flood = DoS variants.
*DoS = Availability attack। DDoS = distributed DoS। Smurf/ SYN-flood = DoS variants।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q584.** A spoofing attack targets which security aspect?
*Spoofing attack किस security पहलू को लक्षित करता है?*
- **(A)** Authentication
- **(B)** Integrity
- **(C)** Availability
- **(D)** Confidentiality
✔ **(A) Authentication**
★ **Nukta:** Spoofing/impersonation → Authentication. Phishing → steals credentials (auth). Sniffing → Confidentiality.
*Spoofing/impersonation → Authentication। Phishing → credentials चुराता है (auth)। Sniffing → Confidentiality।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q585.** Which of the following is an ACTIVE attack?
*निम्न में से कौन-सा ACTIVE attack है?*
- **(A)** Interception
- **(B)** Modification
- **(C)** Traffic analysis
- **(D)** Eavesdropping
✔ **(B) Modification**
★ **Nukta:** Passive = observe only (eavesdropping, traffic analysis). Active = change/disrupt (modification, fabrication, interruption/DoS).
*Passive = केवल देखना (eavesdropping, traffic analysis)। Active = बदलना/बाधा (modification, fabrication, interruption/DoS)।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q586.** Match the attacks with their descriptions: (a) Phishing  (b) DoS Attack  (c) Man-in-the-Middle  (d) Spoofing — (i) Flooding network traffic  (ii) Stealing user credentials  (iii) Intercepting communication  (iv) Impersonation attack
*हमलों को उनके विवरण से मिलाइए: (a) Phishing  (b) DoS Attack  (c) Man-in-the-Middle  (d) Spoofing — (i) नेटवर्क ट्रैफ़िक भरना  (ii) यूज़र जानकारी चुराना  (iii) संचार में हस्तक्षेप  (iv) पहचान की नकल*
- **(A)** a–ii, b–i, c–iii, d–iv
- **(B)** a–i, b–ii, c–iii, d–iv
- **(C)** a–iii, b–i, c–ii, d–iv
- **(D)** a–ii, b–iii, c–i, d–iv
✔ **(A) a–ii, b–i, c–iii, d–iv**
★ **Nukta:** Attack one-liners: Phishing=fake emails/sites, DoS=flood, MitM=middle interception, Spoofing=fake identity.
*Attack one-liners: Phishing=fake emails/sites, DoS=flood, MitM=middle interception, Spoofing=fake identity।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q3 match (codes recovered)] · Medium*

**Q587.** 'Junk email' is also known as:
*'Junk email' को और क्या कहते हैं?*
- **(A)** Spam
- **(B)** Spoof
- **(C)** Sniffer
- **(D)** Spool
✔ **(A) Spam**
★ **Nukta:** Spam = junk mail; Spoof = पहचान छिपाना; Sniffer = चोरी से सुनना.
*Spam = junk mail; Spoof = पहचान छिपाना; Sniffer = चोरी से सुनना.*
*[Source: RRB NTPC computer banks (via practicemock PYQ set)] · Medium*

**Q588.** The goal of 'Integrity' ensures that:
*'Integrity' का लक्ष्य सुनिश्चित करता है कि:*
- **(A)** Data can be accessed only by authorised users
- **(B)** Data is accurate and has not been modified
- **(C)** Data is always available when needed
- **(D)** Unauthorised users cannot enter the system
✔ **(B) Data is accurate and has not been modified**
★ **Nukta:** Goal map: Confidentiality = authorised access only. Integrity = no unauthorised change. Availability = always accessible.
*Goal map: Confidentiality = केवल authorised access। Integrity = बिना authorisation बदलाव नहीं। Availability = हमेशा उपलब्ध।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

**Q589.** Which of the following is NOT a goal of network security?
*निम्न में से कौन-सा network security का लक्ष्य नहीं है?*
- **(A)** Confidentiality
- **(B)** Integrity
- **(C)** Availability
- **(D)** Redundancy
✔ **(D) Redundancy**
★ **Nukta:** Security goals = CIA. Reliability goals = redundancy, fault tolerance, recovery.
*Security goals = CIA। Reliability goals = redundancy, fault tolerance, recovery।*
*[Source: Subject Test Solution-1 Part-2 (CN & Security) slides] · Hard*

**Q590.** The primary difference between active and passive attacks is:
*Active और passive attacks के बीच मुख्य अंतर क्या है?*
- **(A)** Active attacks change data; passive attacks do not
- **(B)** Passive attacks destroy hardware
- **(C)** Both are the same
- **(D)** Passive attacks are legal
✔ **(A) Active attacks change data; passive attacks do not**
★ **Nukta:** Active: modification, fabrication, interruption. Passive: eavesdropping, traffic analysis. Exam one-liner: 'change vs observe'.
*Active: modification, fabrication, interruption। Passive: eavesdropping, traffic analysis। Exam one-liner: 'change बनाम observe'।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

**Q591.** A ______ does not perform any destructive action directly; it only consumes system resources to bring the system down.
*एक ______ सीधे कोई विनाशकारी काम नहीं करता; वह सिस्टम को गिराने के लिए सिर्फ system resources खाता है.*
- **(A)** Virus
- **(B)** Worm
- **(C)** Trojan
- **(D)** Spyware
✔ **(B) Worm**
★ **Nukta:** HTET 2024 official key (b). फ़र्क: Virus = फ़ाइल में घुसता; Worm = खुद फैलता; Trojan = छिपकर; Spyware = जासूसी.
*HTET 2024 official key (b). फ़र्क: Virus = फ़ाइल में घुसता; Worm = खुद फैलता; Trojan = छिपकर; Spyware = जासूसी.*
*[Source: HTET 2024 (via KnowledgeGate solved PYQ bank)] · Hard*

## Section B — Cryptography

*Plaintext/ciphertext/key, symmetric vs asymmetric ciphers, DES/AES/RSA, stream vs block, classical ciphers, digital signatures, steganography.*

**Cryptography = message ko chhupana. Symmetric (ek key) vs Asymmetric (public-private key pair) — dono ka apna jagah hai.**

*Cryptography = संदेश को छिपाना। Symmetric (एक key) बनाम Asymmetric (public-private key)।*

- Plaintext = asli message; Ciphertext = encrypted message; Key = transformation ka secret.
  - *Plaintext = असली; Ciphertext = encrypted; Key = गुप्त कुंजी।*
- Symmetric encryption — ek hi key encrypt+decrypt (DES, 3DES, AES, RC4, Blowfish); tez, par key distribute karna mushkil.
  - *Symmetric — एक ही key (DES, AES); तेज़, पर key वितरण कठिन।*
- Asymmetric encryption — key pair: public se encrypt, private se decrypt (RSA, ECC, Diffie-Hellman); dheema, par key distribution aasan; digital signatures isi se.
  - *Asymmetric — key pair (RSA); धीमा, पर वितरण आसान; digital signatures।*
- Stream cipher (bit-by-bit, RC4) vs Block cipher (blocks, DES/AES).
  - *Stream cipher (bit-by-bit) vs Block cipher (blocks)।*
- Hash function (MD5, SHA) — message ka fixed digest; change = alag hash; integrity check ke liye.
  - *Hash (MD5, SHA) — fixed digest; integrity check।*
- Digital signature = private key se hash ko encrypt — authentication + non-repudiation.
  - *Digital signature = private key से hash encrypt — authentication + non-repudiation।*
- Certificate/CA — public key ki authenticity dene wali trusted authority (PKI).
  - *Certificate/CA — विश्वसनीय प्राधिकरण (PKI)।*
- Substitution (letters badalna — Caesar) vs Transposition (order badalna); Steganography = message chhupana image mein (encrypt nahi).
  - *Substitution vs Transposition; Steganography = छिपाना (encrypt नहीं)।*

| Fakt | Symmetric | Asymmetric |
|---|---|---|
| Keys | एक shared key | public + private pair |
| Speed | तेज़ | धीमा |
| Key distribution | कठिन | आसान |
| Use | bulk data encryption | key exchange, signatures |
| Examples | DES, 3DES, AES | RSA, ECC, Diffie-Hellman |

### Questions (Easy → Medium → Hard)

**Q592.** The text that gets transformed using a cipher algorithm is called:
*Cipher algorithm से जिस text को बदला जाता है उसे क्या कहते हैं?*
- **(A)** Complex Text
- **(B)** Transformed Text
- **(C)** Plain Text
- **(D)** Scalar Text
✔ **(C) Plain Text**
★ **Nukta:** Cryptography flow: Plain text --(cipher + key)--> Ciphertext --(decipher + key)--> Plain text.
*Cryptography flow: Plain text --(cipher + key)--> Ciphertext --(decipher + key)--> Plain text।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q9] · Easy*

**Q593.** In the digital signature technique, when the whole message is signed using an asymmetric key, the receiver uses:
*Digital signature technique में, जब पूरा संदेश asymmetric key से sign होता है, तो प्राप्तकर्ता उपयोग करता है:*
- **(A)** Her or his own public key
- **(B)** Her or his own private key
- **(C)** The sender's public key
- **(D)** None of these
✔ **(C) The sender's public key**
★ **Nukta:** Signature direction: SIGN with private → VERIFY with public. Encryption direction: ENCRYPT with public → DECRYPT with private.
*Signature दिशा: private से SIGN → public से VERIFY। Encryption दिशा: public से ENCRYPT → private से DECRYPT।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q594.** Which statement about plaintext, ciphertext and key is MOST accurate?
*Plaintext, ciphertext और key के बारे में कौन-सा कथन सबसे सही है?*
- **(A)** Plaintext is generated after decryption using a public key
- **(B)** Ciphertext is the original readable message
- **(C)** Plaintext is transformed into ciphertext using an algorithm and a key
- **(D)** Ciphertext and plaintext are always of the same length
✔ **(C) Plaintext is transformed into ciphertext using an algorithm and a key**
★ **Nukta:** Remember the 3 objects: plaintext (readable), ciphertext (scrambled), key (secret parameter). Encryption = f(plaintext, key).
*3 objects याद रखें: plaintext (पढ़ने योग्य), ciphertext (scrambled), key (गुप्त parameter)। Encryption = f(plaintext, key)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q10] · Medium*

**Q595.** Which of the following uses the SAME key for encryption and decryption?
*निम्न में से कौन-सा encryption और decryption के लिए एक ही key उपयोग करता है?*
- **(A)** Symmetric key cipher
- **(B)** Asymmetric key cipher
- **(C)** Hash function
- **(D)** Digital signature
✔ **(A) Symmetric key cipher**
★ **Nukta:** Symmetric = 1 key (fast). Asymmetric = key pair (public+private, slow). Hash = one-way digest. Signature = private-sign/public-verify.
*Symmetric = 1 key (तेज़)। Asymmetric = key pair (public+private, धीमा)। Hash = one-way digest। Signature = private-sign/public-verify।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q596.** Which of the following uses a PAIR of keys (public and private)?
*निम्न में से कौन-सा keys की एक जोड़ी (public और private) उपयोग करता है?*
- **(A)** Symmetric cipher
- **(B)** Asymmetric cipher
- **(C)** DES
- **(D)** AES
✔ **(B) Asymmetric cipher**
★ **Nukta:** Public-key examples: RSA, Diffie-Hellman, ECC, DSA. Symmetric: DES, 3DES, AES, Blowfish, RC4.
*Public-key examples: RSA, Diffie-Hellman, ECC, DSA। Symmetric: DES, 3DES, AES, Blowfish, RC4।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q597.** Which is FASTER in encryption and decryption?
*Encryption और decryption में कौन-सा तेज़ है?*
- **(A)** Symmetric key cipher
- **(B)** Asymmetric key cipher
- **(C)** Cannot decide
- **(D)** None of these
✔ **(A) Symmetric key cipher**
★ **Nukta:** Speed: Symmetric >> Asymmetric. Hybrid systems (TLS/PGP) use asymmetric KEYS to exchange a symmetric SESSION key.
*Speed: Symmetric >> Asymmetric। Hybrid systems (TLS/PGP) asymmetric KEYS से symmetric SESSION key का आदान-प्रदान करती हैं।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q598.** What is the main disadvantage of symmetric key encryption?
*Symmetric key encryption की मुख्य कमी क्या है?*
- **(A)** It is very slow
- **(B)** Key distribution is difficult
- **(C)** It uses two keys
- **(D)** It cannot encrypt text
✔ **(B) Key distribution is difficult**
★ **Nukta:** Symmetric weakness = key distribution (n users → n(n-1)/2 keys). Asymmetric weakness = slow + key authenticity (certificates).
*Symmetric कमज़ोरी = key distribution (n users → n(n-1)/2 keys)। Asymmetric कमज़ोरी = धीमा + key authenticity (certificates)।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q599.** In public-key cryptography, a message encrypted with the public key can only be decrypted by:
*Public-key cryptography में public key से encrypt किया संदेश केवल किसके द्वारा decrypt हो सकता है?*
- **(A)** Another public key
- **(B)** The same public key
- **(C)** The private key corresponding to that public key
- **(D)** A session key
✔ **(C) The private key corresponding to that public key**
★ **Nukta:** Public/private are mathematically paired — like a lock (public) and its only key (private).
*Public/private गणितीय रूप से जुड़े हैं — एक ताला (public) और उसकी एकमात्र चाबी (private) की तरह।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q600.** Data Encryption Standard (DES) is a:
*Data Encryption Standard (DES) क्या है?*
- **(A)** Block cipher
- **(B)** Stream cipher
- **(C)** Bit cipher
- **(D)** Byte cipher
✔ **(A) Block cipher**
★ **Nukta:** DES = 64-bit block, 56-bit key (symmetric). AES = 128-bit block. RC4 = stream cipher.
*DES = 64-bit block, 56-bit key (symmetric)। AES = 128-bit block। RC4 = stream cipher।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q601.** Which cipher method encrypts one bit or byte at a time?
*कौन-सी cipher method एक बार में एक bit या byte encrypt करती है?*
- **(A)** Block cipher
- **(B)** Stream cipher
- **(C)** Substitution cipher
- **(D)** Transposition cipher
✔ **(B) Stream cipher**
★ **Nukta:** Stream = 1 bit/byte at a time (RC4, A5/1). Block = fixed-size blocks (DES/AES). Substitution/Transposition = classical techniques.
*Stream = 1 bit/byte at a time (RC4, A5/1)। Block = fixed-size blocks (DES/AES)। Substitution/Transposition = classical techniques।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q602.** The Caesar Cipher is an example of which cryptographic technique?
*Caesar Cipher किस cryptographic technique का उदाहरण है?*
- **(A)** Transposition cipher
- **(B)** Substitution cipher
- **(C)** Stream cipher
- **(D)** Block cipher
✔ **(B) Substitution cipher**
★ **Nukta:** Classical types: Substitution (Caesar, Playfair) = replace; Transposition (Rail fence) = rearrange.
*Classical types: Substitution (Caesar, Playfair) = replace; Transposition (Rail fence) = rearrange।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q603.** The process of detecting hidden data inside a file is known as:
*किसी file के भीतर छिपे data का पता लगाने की प्रक्रिया को क्या कहते हैं?*
- **(A)** Cryptanalysis
- **(B)** Steganalysis
- **(C)** Data mining
- **(D)** Steganography
✔ **(B) Steganalysis**
★ **Nukta:** Steganography = HIDING data (cover file). Steganalysis = DETECTING it. Cryptography = scrambling it.
*Steganography = data छिपाना (cover file)। Steganalysis = पता लगाना। Cryptography = scramblइंग।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q604.** What is the output of a steganography process called?
*Steganography प्रक्रिया के output को क्या कहते हैं?*
- **(A)** Ciphertext
- **(B)** Stego-object
- **(C)** Encoded file
- **(D)** Key file
✔ **(B) Stego-object**
★ **Nukta:** Stego terms: cover file (original carrier), secret message (hidden data), stego-object (result).
*Stego terms: cover file (original carrier), secret message (hidden data), stego-object (result)।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

**Q605.** In steganography, the file used to hide the secret data is called:
*Steganography में secret data छिपाने के लिए जिस file का उपयोग होता है उसे क्या कहते हैं?*
- **(A)** Secret file
- **(B)** Cover file
- **(C)** Cipher file
- **(D)** Key file
✔ **(B) Cover file**
★ **Nukta:** Cover file = the disguise. Secret message = hidden data. Stego-object = cover + secret after embedding.
*Cover file = छद्म वेश। Secret message = छिपा data। Stego-object = embedding के बाद cover + secret।*
*[Source: Subject Test Solution-1 Part-2 (CN & Security) slides] · Medium*

**Q606.** Which of the following is an example of asymmetric encryption?
*निम्न में से कौन-सा asymmetric encryption का उदाहरण है?*
- **(A)** AES
- **(B)** DES
- **(C)** RSA
- **(D)** Blowfish
✔ **(C) RSA**
★ **Nukta:** Asymmetric = RSA, ECC, Diffie-Hellman, DSA. Symmetric = DES, 3DES, AES, Blowfish, RC4, IDEA.
*Asymmetric = RSA, ECC, Diffie-Hellman, DSA। Symmetric = DES, 3DES, AES, Blowfish, RC4, IDEA।*
*[Source: SSC CGL Tier-2 repeated Qs (via Oliveboard) · also BCI_SCI ST-01] · Medium*

**Q607.** The data to be encrypted at the sender's site is called ______ and the data to be decrypted at the receiver's end is called ______.
*Sender की ओर encrypt किए जाने वाले data को ______ और receiver की ओर decrypt किए जाने वाले data को ______ कहते हैं.*
- **(A)** Secret key, public key
- **(B)** Public key, secret key
- **(C)** Plain text, cipher text
- **(D)** Cipher text, plain text
✔ **(C) Plain text, cipher text**
★ **Nukta:** याद रखो: Plain (सादा) → encrypt → Cipher (गूँथा) → decrypt → Plain.
*याद रखो: Plain (सादा) → encrypt → Cipher (गूँथा) → decrypt → Plain.*
*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Medium*

**Q608.** Public key is used to:
*Public key का उपयोग किसके लिए होता है?*
- **(A)** Encrypt the data
- **(B)** Decrypt the data
- **(C)** Both encrypt and decrypt
- **(D)** Generate session keys only
✔ **(A) Encrypt the data**
★ **Nukta:** Encrypt with public → decrypt with private. SIGN with private → verify with public. Exam asks both directions!
*Encrypt public से → decrypt private से। SIGN private से → verify public से। Exam दोनों दिशाएँ पूछता है!*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

**Q609.** Which statement about symmetric and asymmetric cryptography is TRUE?
*Symmetric और asymmetric cryptography के बारे में कौन-सा कथन सही है?*
- **(A)** Symmetric cryptography provides authentication
- **(B)** Asymmetric cryptography is faster than symmetric
- **(C)** Symmetric cryptography requires secure key exchange
- **(D)** Both use two different keys
✔ **(C) Symmetric cryptography requires secure key exchange**
★ **Nukta:** True: symmetric needs secure key exchange. False: symmetric does not inherently authenticate; asymmetric is slower; symmetric uses ONE key.
*सही: symmetric को secure key exchange चाहिए। गलत: symmetric स्वयं authentication नहीं देता; asymmetric धीमा; symmetric एक key उपयोग करता है।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security) — Q33] · Hard*

**Q610.** What is the key length of AES-256 encryption?
*AES-256 encryption की key length कितनी है?*
- **(A)** 128 bits
- **(B)** 192 bits
- **(C)** 256 bits
- **(D)** 512 bits
✔ **(C) 256 bits**
★ **Nukta:** AES variants: AES-128, AES-192, AES-256 (key sizes). Block size is always 128 bits.
*AES variants: AES-128, AES-192, AES-256 (key sizes)। Block size हमेशा 128 bits।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

**Q611.** Which of the following statements is FALSE?
*निम्न में से कौन-सा कथन गलत है?*
- **(A)** AES is a block cipher
- **(B)** RSA is a symmetric cipher
- **(C)** Diffie-Hellman is used for key exchange
- **(D)** DES is symmetric
✔ **(B) RSA is a symmetric cipher**
★ **Nukta:** False-statement MCQs: check each. AES=block ✓, RSA=asymmetric ✗, DH=key exchange ✓, DES=symmetric ✓.
*False-statement MCQs: हर एक जाँचें। AES=block ✓, RSA=asymmetric ✗, DH=key exchange ✓, DES=symmetric ✓।*
*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

**Q612.** Suppose everyone in a group of N people wants to communicate secretly with the N−1 others using a symmetric-key cryptographic system. The number of keys required in the system as a whole is:
*मान लीजिए N लोगों के समूह में हर व्यक्ति बाकी N−1 लोगों से symmetric-key cryptographic system से गुप्त बातचीत करना चाहता है. कुल कितने keys चाहिए होंगी?*
- **(A)** 2N
- **(B)** N(N − 1)
- **(C)** N(N − 1)/2
- **(D)** (N − 1)²
✔ **(C) N(N − 1)/2**
★ **Nukta:** GATE key (c). Public-key में यह समस्या नहीं — इसीलिए hybrid systems आए.
*GATE key (c). Public-key में यह समस्या नहीं — इसीलिए hybrid systems आए.*
*[Source: GATE CS PYQ (via examprev)] · Hard*

## Section C — Firewalls, IPSec & Security Protocols

*DMZ design, IPSec modes (transport/tunnel), SSL/TLS & HTTPS, security-protocol and mechanism layer mapping.*

**Firewall, IPSec, SSL/TLS aur VPN — network ko secure karne ke practical tools.**

*Firewall, IPSec, SSL/TLS और VPN — network सुरक्षा के व्यावहारिक उपकरण।*

- Firewall types: Packet-filtering (header rules), Stateful (connection state), Proxy/Application gateway (message level).
  - *Firewall: Packet-filtering, Stateful, Proxy/Application gateway।*
- DMZ — public servers wala beech ka zone; andar ka LAN sabse secure.
  - *DMZ — public servers का क्षेत्र; भीतर का LAN सुरक्षित।*
- IPSec (Network layer security): AH (authentication header) + ESP (encryption + authentication).
  - *IPSec (Network layer): AH + ESP।*
- IPSec modes: Transport mode (sirf payload encrypt) vs Tunnel mode (poora packet encrypt — VPN ke liye).
  - *IPSec modes: Transport (payload) vs Tunnel (poora packet — VPN)।*
- VPN = public network par private tunnel (encryption ke saath) — IPSec/PPTP/L2TP se banta hai.
  - *VPN = public network पर private tunnel।*
- SSL/TLS — transport layer security: handshake (certificate exchange, session key) + record protocol (encryption); HTTPS = HTTP + SSL/TLS.
  - *SSL/TLS — handshake + records; HTTPS = HTTP + SSL/TLS।*
- SSH = secure remote login (Telnet ka secure version, port 22).
  - *SSH = सुरक्षित remote login (port 22)।*
- E-mail security: PGP (Pretty Good Privacy), S/MIME — encryption + signature.
  - *E-mail security: PGP, S/MIME।*
- Wireless security: WEP (kamzor) → WPA → WPA2 (AES) → WPA3.
  - *Wireless: WEP → WPA → WPA2 → WPA3।*

| Technology | Layer | Kaam |
|---|---|---|
| Firewall | 3–7 | traffic filter |
| IPSec | 3 (Network) | packet encryption/auth (VPN) |
| SSL/TLS | 4–5 (Transport) | secure web (HTTPS) |
| SSH | Application | secure remote login |
| PGP/S-MIME | Application | secure e-mail |

### Questions (Easy → Medium → Hard)

**Q613.** IPSec is MOST commonly used to implement:
*IPSec मुख्यतः किसके लिए उपयोग होता है?*
- **(A)** Secure email
- **(B)** Secure web browsing
- **(C)** Virtual Private Network (VPN)
- **(D)** Wireless security
✔ **(C) Virtual Private Network (VPN)**
★ **Nukta:** IPSec = VPN tunneling (ESP/AH). Secure email = PGP/SMIME. Secure web = SSL/TLS. Wireless = WPA2.
*IPSec = VPN tunneling (ESP/AH)। Secure email = PGP/SMIME। Secure web = SSL/TLS। Wireless = WPA2।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q614.** In IPSec Tunnel mode:
*IPSec Tunnel mode में:*
- **(A)** Only the payload is encrypted
- **(B)** Only the header is encrypted
- **(C)** The entire IP packet is encrypted
- **(D)** No encryption is used
✔ **(C) The entire IP packet is encrypted**
★ **Nukta:** Tunnel = whole packet + new header (gateway VPN). Transport = payload only (host-to-host).
*Tunnel = पूरा packet + नया header (gateway VPN)। Transport = केवल payload (host-to-host)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q615.** The SSL/TLS handshake protocol is mainly used for:
*SSL/TLS handshake protocol मुख्यतः किसके लिए उपयोग होता है?*
- **(A)** Data encryption
- **(B)** Data compression
- **(C)** Key exchange and authentication
- **(D)** Packet routing
✔ **(C) Key exchange and authentication**
★ **Nukta:** TLS parts: Handshake = keys+authentication; Record = encryption+integrity. HTTPS = HTTP over TLS (port 443).
*TLS parts: Handshake = keys+authentication; Record = encryption+integrity। HTTPS = HTTP over TLS (port 443)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

**Q616.** Match the security mechanisms with their OSI layers: (a) Firewall  (b) Digital Signature  (c) MAC Filtering  (d) Port-based Filtering — (i) Network Layer  (ii) Application Layer  (iii) Data Link Layer  (iv) Transport Layer
*Security mechanisms को OSI layers से मिलाइए: (a) Firewall  (b) Digital Signature  (c) MAC Filtering  (d) Port-based Filtering — (i) Network Layer  (ii) Application Layer  (iii) Data Link Layer  (iv) Transport Layer*
- **(A)** a–i, b–ii, c–iii, d–iv
- **(B)** a–ii, b–i, c–iii, d–iv
- **(C)** a–iv, b–ii, c–i, d–iii
- **(D)** a–i, b–iii, c–ii, d–iv
✔ **(A) a–i, b–ii, c–iii, d–iv**
★ **Nukta:** Mechanism-layers: Firewall L3/L4 (IP), Port filter L4, MAC filter L2, Digital signature L7. Packet-filtering firewall = L3/L4.
*Mechanism-layers: Firewall L3/L4 (IP), Port filter L4, MAC filter L2, Digital signature L7। Packet-filtering firewall = L3/L4।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q4 match (codes recovered)] · Medium*

**Q617.** Match the security protocols with their OSI layers: (a) IPSec  (b) SSL/TLS  (c) PGP  (d) WPA2 — (i) Application Layer  (ii) Network Layer  (iii) Transport/Presentation Layer  (iv) Data Link Layer (Wi-Fi)
*Security protocols को OSI layers से मिलाइए: (a) IPSec  (b) SSL/TLS  (c) PGP  (d) WPA2 — (i) Application Layer  (ii) Network Layer  (iii) Transport/Presentation Layer  (iv) Data Link Layer (Wi-Fi)*
- **(A)** a–ii, b–iii, c–i, d–iv
- **(B)** a–ii, b–i, c–iii, d–iv
- **(C)** a–iii, b–ii, c–i, d–iv
- **(D)** a–i, b–ii, c–iii, d–iv
✔ **(A) a–ii, b–iii, c–i, d–iv**
★ **Nukta:** Protocol layers: IPSec L3, SSL/TLS L4-7 (exam: transport/presentation), PGP L7, WPA2 L2, Kerberos L7.
*Protocol layers: IPSec L3, SSL/TLS L4-7 (exam: transport/presentation), PGP L7, WPA2 L2, Kerberos L7।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q1 match (codes recovered)] · Medium*

**Q618.** IPSec operates in which mode(s)?
*IPSec किस/किन mode(s) में काम करता है?*
- **(A)** Transport mode only
- **(B)** Tunnel mode only
- **(C)** Both transport mode and tunnel mode
- **(D)** Application mode
✔ **(C) Both transport mode and tunnel mode**
★ **Nukta:** IPSec modes: Transport (payload only, host-to-host) & Tunnel (full packet, gateway-to-gateway/VPN).
*IPSec modes: Transport (केवल payload, host-to-host) और Tunnel (पूरा packet, gateway-to-gateway/VPN)।*
*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

**Q619.** Which mode of IPSec provides end-to-end security between two hosts?
*IPSec का कौन-सा mode दो hosts के बीच end-to-end security देता है?*
- **(A)** Transport mode
- **(B)** Tunnel mode
- **(C)** Static mode
- **(D)** Gateway mode
✔ **(A) Transport mode**
★ **Nukta:** End-to-end (host↔host) = Transport mode. Gateway↔gateway (VPN) = Tunnel mode.
*End-to-end (host↔host) = Transport mode। Gateway↔gateway (VPN) = Tunnel mode।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

**Q620.** Which of the following is used in HTTPS for encryption?
*HTTPS में encryption के लिए निम्न में से क्या उपयोग होता है?*
- **(A)** SSL/TLS
- **(B)** FTP
- **(C)** ARP
- **(D)** NAT
✔ **(A) SSL/TLS**
★ **Nukta:** HTTPS = HTTP + SSL/TLS (443). HTTP = 80 (no encryption). FTP = 21. ARP = IP→MAC. NAT = address translation.
*HTTPS = HTTP + SSL/TLS (443)। HTTP = 80 (encryption नहीं)। FTP = 21। ARP = IP→MAC। NAT = address translation।*
*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

**Q621.** In which layer of the network architecture is the Secure Socket Layer (SSL) used?
*Secure Socket Layer (SSL) network architecture की किस layer में उपयोग होती है?*
- **(A)** Physical layer
- **(B)** Session layer
- **(C)** Application layer
- **(D)** Presentation layer
✔ **(B) Session layer**
★ **Nukta:** Exam convention: SSL = Session layer (secure session setup + negotiation). Note: TLS = successor of SSL.
*Exam convention: SSL = Session layer (secure session setup + negotiation)। नोट: TLS, SSL का उत्तराधिकारी है।*
*[Source: Unit Test-4 Solution (OCR), p6 (bank key)] · Medium*

**Q622.** When a logic bomb is activated by a time-related event, it is known as a:
*जब कोई logic bomb किसी समय-संबंधी घटना से सक्रिय होता है, तो उसे कहते हैं:*
- **(A)** Time-related bomb sequence
- **(B)** Virus
- **(C)** Time bomb
- **(D)** Trojan horse
✔ **(C) Time bomb**
★ **Nukta:** Logic bomb = code that explodes on a condition; if the condition is time, it is a Time bomb.
*Logic bomb = शर्त से फटने वाला कोड; शर्त समय हो तो Time bomb.*
*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Medium*

**Q623.** Verification based on a login ID and password is called:
*Login ID और password के आधार पर जाँच कहलाती है:*
- **(A)** Logging in
- **(B)** Configuration
- **(C)** Authentication
- **(D)** Confidentiality
✔ **(C) Authentication**
★ **Nukta:** Authentication = 'तुम कौन हो?'; Authorization = 'तुम्हें क्या अनुमति है?'.
*Authentication = 'तुम कौन हो?'; Authorization = 'तुम्हें क्या अनुमति है?'.*
*[Source: RBI/IBPS computer-awareness banks (via ixambee)] · Medium*

**Q624.** Access control based on a person's fingerprints is an example of:
*किसी व्यक्ति की उंगलियों के निशान पर आधारित access control का उदाहरण है:*
- **(A)** Biometric identification
- **(B)** Characteristic identification
- **(C)** Encryption
- **(D)** Logistics
✔ **(A) Biometric identification**
★ **Nukta:** Physical identity (biometric) is stronger than something known (password).
*ज्ञात (password) से बढ़कर है शारीरिक पहचान (biometric).*
*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Medium*

**Q625.** Which of the following networks extends a private network across public networks?
*निम्न में से कौन-सा network public networks के ऊपर private network का विस्तार करता है?*
- **(A)** Virtual private network (VPN)
- **(B)** Local area network
- **(C)** Enterprise private network
- **(D)** None of these
✔ **(A) Virtual private network (VPN)**
★ **Nukta:** BPSC 2024 official key (a). VPN = a private limousine on the public road.
*BPSC 2024 official key (a). VPN = सार्वजनिक सड़क पर निजी लिमोज़ीन.*
*[Source: BPSC TRE 2024 (via KnowledgeGate solved PYQ bank)] · Medium*

**Q626.** Which one of the following is a key function of a firewall?
*निम्न में से firewall का एक मुख्य काम कौन-सा है?*
- **(A)** Monitoring
- **(B)** Copying
- **(C)** Deleting
- **(D)** Moving
✔ **(A) Monitoring**
★ **Nukta:** Firewall = the network's gatekeeper — it watches, checks, stops.
*Firewall = network का चौकीदार — देखता है, जाँचता है, रोकता है.*
*[Source: RRB NTPC previous-year computer banks (via adda247 50-PYQ PDF)] · Medium*

**Q627.** What is the advantage of setting up a DMZ (Demilitarized Zone) using a firewall?
*Firewall का उपयोग करके DMZ (Demilitarized Zone) बनाने का क्या लाभ है?*
- **(A)** To create multiple zones of trust
- **(B)** Load balancing on the server
- **(C)** Improving network performance
- **(D)** Bringing internet service into a home
✔ **(A) To create multiple zones of trust**
★ **Nukta:** Official RPSC key. DMZ = buffer zone between untrusted Internet and trusted LAN (3 zones: external / DMZ / internal).
*Official RPSC key। DMZ = untrusted Internet और trusted LAN के बीच buffer zone (3 zones: external / DMZ / internal)।*
*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

# ★ Nukte Rapid-Fire — Exam Pointers

- **5 components of data communication?** — ✔ Message, Sender, Receiver, Medium, Protocol
  - *Data communication के 5 components? — Message, Sender, Receiver, Medium, Protocol*
- **3 criteria of a good network?** — ✔ Performance, Reliability, Security
  - *अच्छे network के 3 criteria? — Performance, Reliability, Security*
- **4 characteristics of data communication?** — ✔ Delivery, Accuracy, Timeliness, Jitter
  - *Data communication के 4 characteristics? — Delivery, Accuracy, Timeliness, Jitter*
- **Jitter means?** — ✔ Delay variation between packets
  - *Jitter का अर्थ? — Packets के बीच delay का बदलाव*
- **Protocol elements?** — ✔ Syntax, Semantics, Timing
  - *Protocol के elements? — Syntax, Semantics, Timing*
- **Simplex example?** — ✔ TV broadcast / keyboard→monitor (one-way)
  - *Simplex का उदाहरण? — TV broadcast / keyboard→monitor (one-way)*
- **Half-Duplex example?** — ✔ Walkie-talkie (both ways, one at a time)
  - *Half-Duplex का उदाहरण? — Walkie-talkie (दोनों तरफ़, पर एक समय में एक)*
- **Full-Duplex example?** — ✔ Telephone (both ways, same time)
  - *Full-Duplex का उदाहरण? — Telephone (दोनों तरफ़, एक साथ)*
- **Mesh cables formula?** — ✔ n(n-1)/2 cables, n-1 ports per device
  - *Mesh cables का formula? — n(n-1)/2 cables, n-1 ports per device*
- **Star / Ring / Bus cables?** — ✔ Star = n, Ring = n, Bus = 1
  - *Star / Ring / Bus cables? — Star = n, Ring = n, Bus = 1*
- **Most fault-tolerant topology?** — ✔ Mesh (redundant paths)
  - *सबसे ज़्यादा fault-tolerant topology? — Mesh (redundant paths)*
- **Easy to install & reconfigure?** — ✔ Star topology
  - *Install/reconfigure में आसान? — Star topology*
- **Multipoint topology?** — ✔ Bus (shared backbone)
  - *Multipoint topology? — Bus (shared backbone)*
- **IEEE 802.2 / 802.3 / 802.5 / 802.11?** — ✔ LLC / Ethernet(MAC) / Token Ring / Wi-Fi
  - *IEEE 802.2 / 802.3 / 802.5 / 802.11? — LLC / Ethernet(MAC) / Token Ring / Wi-Fi*
- **Network size order?** — ✔ PAN < LAN < MAN < WAN
  - *Network size का क्रम? — PAN < LAN < MAN < WAN*
- **internet vs Internet?** — ✔ Any network of networks vs THE global one
  - *internet बनाम Internet? — कोई भी network of networks बनाम वह विश्वव्यापी*
- **Intranet vs Extranet?** — ✔ Intranet = inside the organisation; Extranet = trusted outsiders (supplier)
  - *Intranet बनाम Extranet? — Intranet = संस्था के अंदर; Extranet = भरोसेमंद बाहरी (supplier)*
- **Client-Server vs P2P examples?** — ✔ ATM = Client-Server; BitTorrent = P2P
  - *Client-Server बनाम P2P उदाहरण? — ATM = Client-Server; BitTorrent = P2P*
- **ARPANET facts?** — ✔ 1969 (ARPA); TCP/IP adopted 1983; WWW 1991 (CERN, Tim Berners-Lee)
  - *ARPANET तथ्य? — 1969 (ARPA); TCP/IP adopted 1983; WWW 1991 (CERN, Tim Berners-Lee)*
- **Internet switching?** — ✔ Packet switching (data travels in packets)
  - *Internet कौन-सी switching use करता है? — Packet switching (data packets में चलता है)*
- **Circuit switching key?** — ✔ Dedicated separate physical path per connection
  - *Circuit switching की कुंजी? — हर connection का dedicated अलग physical path*
- **OSI layers mnemonic?** — ✔ Please Do Not Throw Sausage Pizza Away (L1→L7)
  - *OSI layers की mnemonic? — Please Do Not Throw Sausage Pizza Away (L1→L7)*
- **OSI kisne banaya, kab?** — ✔ ISO, in 1984 — 7 layers
  - *OSI किसने बनाया, कब? — ISO, 1984 में — 7 layers*
- **TCP/IP kisne banaya?** — ✔ Cerf & Kahn (DoD/ARPA), 1970s — adopted 1983
  - *TCP/IP किसने बनाया? — Cerf & Kahn (DoD/ARPA), 1970s — adopted 1983*
- **Layer counts?** — ✔ OSI = 7, Internet stack = 5, TCP/IP suite = 4
  - *Layer counts? — OSI = 7, Internet stack = 5, TCP/IP suite = 4*
- **TCP/IP mein kya missing?** — ✔ No separate Session & Presentation layers
  - *TCP/IP में क्या missing? — Session और Presentation की अलग layers नहीं*
- **OSI→TCP/IP mapping?** — ✔ OSI 1+2 = Network Access; OSI 5+6+7 = Application
  - *OSI→TCP/IP mapping? — OSI 1+2 = Network Access; OSI 5+6+7 = Application*
- **PDU per layer?** — ✔ Data / Segment / Packet-Datagram / Frame / Bits
  - *हर layer की PDU? — Data / Segment / Packet-Datagram / Frame / Bits*
- **Encapsulation direction?** — ✔ Sender: top→bottom (headers add); Receiver: bottom→top (remove)
  - *Encapsulation की दिशा? — Sender: top→bottom; Receiver: bottom→top*
- **4 levels of addresses?** — ✔ Physical(48-bit), IP(32/128-bit), Port(16-bit), Specific(URL)
  - *4 levels के addresses? — Physical(48-bit), IP(32/128-bit), Port(16-bit), Specific(URL)*
- **Delivery scopes?** — ✔ Bit-by-bit=Physical; Hop-to-hop=Data Link; Source-destination=Network; End-to-end/Process-process=Transport
  - *Delivery के scopes? — Bit-by-bit=Physical; Hop-to-hop=Data Link; Source-destination=Network; End-to-end=Transport*
- **Presentation layer kaam?** — ✔ Translation + Encryption + Compression
  - *Presentation layer के काम? — Translation + Encryption + Compression*
- **Session layer ke 3 kaam?** — ✔ Dialog control + Token management + Synchronization (checkpoint)
  - *Session layer के 3 काम? — Dialog control + Token management + Synchronization*
- **Data Link ka trio?** — ✔ Framing + Error detection + Physical(MAC) addressing
  - *Data Link का trio? — Framing + Error detection + MAC addressing*
- **LLC vs MAC?** — ✔ LLC (802.2) = Network layer interface; MAC (802.3) = medium access + MAC address
  - *LLC बनाम MAC? — LLC = interface; MAC = medium access + address*
- **Support layers grouping?** — ✔ Network support = 1,2,3; User support = 5,6,7; Transport(4) = bridge
  - *Support layers grouping? — Network support = 1,2,3; User support = 5,6,7; Transport = bridge*
- **Device layers?** — ✔ Repeater/Hub=L1; Bridge/Switch=L2; Router=L3; Gateway=L4+
  - *Devices की layers? — Repeater/Hub=L1; Bridge/Switch=L2; Router=L3; Gateway=L4+*
- **Reliable delivery?** — ✔ Transport layer (TCP) — IP is best-effort only
  - *Reliable delivery? — Transport layer (TCP) — IP सिर्फ best-effort*
- **Router visits formula?** — ✔ n routers: Network layer = n+2, Data Link = 2(n+1)
  - *Router visits का formula? — n routers: Network layer = n+2, Data Link = 2(n+1)*
- **Physical layer ka kaam?** — ✔ Signals, media, line/channel coding, modulation, baud rate, bit-by-bit
  - *Physical layer का काम? — Signals, media, coding, modulation, baud rate, bit-by-bit*
- **IP/ICMP/ARP kis layer ke?** — ✔ Network / Internet layer (L3)
  - *IP/ICMP/ARP किस layer के? — Network / Internet layer (L3)*
- **MAC address size?** — ✔ 48 bits (6 bytes, 12 hex digits).
  - *MAC address size? — 48 bits (6 bytes, 12 hex digits)।*
- **IPv4 size? IPv6 size? Port size?** — ✔ 32 / 128 / 16 bits.
  - *IPv4 size? IPv6 size? Port size? — 32 / 128 / 16 bits।*
- **MAC address other names?** — ✔ Physical address / hardware address / burned-in address.
  - *MAC address के अन्य नाम? — Physical address / hardware address / burned-in address।*
- **Broadcast MAC address?** — ✔ FF:FF:FF:FF:FF:FF (all 48 bits = 1).
  - *Broadcast MAC address? — FF:FF:FF:FF:FF:FF (सभी 48 bits = 1)।*
- **I/G bit trick for unicast/multicast?** — ✔ Last bit of first octet: 0 = unicast, 1 = multicast.
  - *Unicast/multicast के लिए I/G bit trick? — पहले octet का अंतिम bit: 0 = unicast, 1 = multicast।*
- **Class ranges by first octet (A/B/C/D/E)?** — ✔ 0-127 / 128-191 / 192-223 / 224-239 (multicast) / 240-255 (experimental).
  - *पहले octet से Class ranges (A/B/C/D/E)? — 0-127 / 128-191 / 192-223 / 224-239 (multicast) / 240-255 (experimental)।*
- **Default masks A/B/C?** — ✔ 255.0.0.0 /8, 255.255.0.0 /16, 255.255.255.0 /24.
  - *Default masks A/B/C? — 255.0.0.0 /8, 255.255.0.0 /16, 255.255.255.0 /24।*
- **Hosts per class (A/B/C)?** — ✔ 2^24−2 (16,777,214) / 2^16−2 (65,534) / 2^8−2 (254).
  - *प्रति class hosts (A/B/C)? — 2^24−2 (16,777,214) / 2^16−2 (65,534) / 2^8−2 (254)।*
- **Loopback address?** — ✔ 127.0.0.1 (whole 127.0.0.0/8 block).
  - *Loopback address? — 127.0.0.1 (पूरा 127.0.0.0/8 block)।*
- **APIPA range (DHCP fail)?** — ✔ 169.254.0.1 - 169.254.255.254.
  - *APIPA range (DHCP fail)? — 169.254.0.1 - 169.254.255.254।*
- **Private IP blocks (RFC 1918)?** — ✔ 10.x / 172.16-31.x / 192.168.x.
  - *Private IP blocks (RFC 1918)? — 10.x / 172.16-31.x / 192.168.x।*
- **0.0.0.0 means?** — ✔ 'This host — no IP yet' (source) or default route (0.0.0.0/0).
  - *0.0.0.0 का अर्थ? — 'यह host — अभी IP नहीं' (source) या default route (0.0.0.0/0)।*
- **Usable hosts formula?** — ✔ 2^host-bits − 2. /24→254, /25→126, /27→30, /30→2.
  - *Usable hosts सूत्र? — 2^host-bits − 2। /24→254, /25→126, /27→30, /30→2।*
- **Subnets formula?** — ✔ 2^borrowed-bits. 3 bits → 8 subnets.
  - *Subnets सूत्र? — 2^borrowed-bits। 3 bits → 8 subnets।*
- **CIDR /24 means?** — ✔ 24 network bits (mask 255.255.255.0).
  - *CIDR /24 का अर्थ? — 24 network bits (mask 255.255.255.0)।*
- **/30 used for?** — ✔ Point-to-point links (2 usable hosts).
  - */30 किसके लिए? — Point-to-point links (2 उपयोगी hosts)।*
- **Subnetting trade-off?** — ✔ More subnets ⇔ fewer hosts each.
  - *Subnetting trade-off? — ज़्यादा subnets ⇔ हर एक में कम hosts।*
- **IPv6 has broadcast?** — ✔ NO — IPv6 uses multicast + anycast, no broadcast.
  - *IPv6 में broadcast है? — नहीं — IPv6 multicast + anycast उपयोग करता है, broadcast नहीं।*
- **IPv6 transition techniques?** — ✔ Tunneling (IPv6-in-IPv4), Dual-stack, Translation (NAT64).
  - *IPv6 transition techniques? — Tunneling (IPv6-in-IPv4), Dual-stack, Translation (NAT64)।*
- **Well-known / registered / ephemeral port ranges?** — ✔ 0-1023 / 1024-49151 / 49152-65535.
  - *Well-known / registered / ephemeral port ranges? — 0-1023 / 1024-49151 / 49152-65535।*
- **Port numbers: DNS, HTTP, HTTPS, FTP, SMTP, SSH?** — ✔ 53, 80, 443, 21, 25, 22.
  - *Port numbers: DNS, HTTP, HTTPS, FTP, SMTP, SSH? — 53, 80, 443, 21, 25, 22।*
- **Socket = ?** — ✔ IP address + Port number (identifies a process).
  - *Socket = ? — IP address + Port number (process की पहचान)।*
- **DNS records: A / AAAA / PTR / MX / CNAME?** — ✔ name→IPv4 / name→IPv6 / IP→name / mail / alias.
  - *DNS records: A / AAAA / PTR / MX / CNAME? — name→IPv4 / name→IPv6 / IP→name / mail / alias।*
- **ARP vs RARP?** — ✔ ARP = IP→MAC. RARP = MAC→IP (obsolete, use DHCP).
  - *ARP vs RARP? — ARP = IP→MAC। RARP = MAC→IP (अप्रचलित, DHCP उपयोग करें)।*
- **NAT purpose?** — ✔ Map private IPs → public IP (save addresses + hide internals).
  - *NAT उद्देश्य? — Private IPs → public IP map करना (addresses बचाना + internals छिपाना)।*
- **Per-hop vs end-to-end in a routed packet?** — ✔ MAC changes per hop; IP addresses stay end-to-end.
  - *Routed packet में per-hop vs end-to-end? — MAC हर hop पर बदलता है; IP addresses end-to-end रहते हैं।*
- **Who allocates IP addresses globally?** — ✔ ICANN/IANA (with RIRs). IETF makes protocols, IEEE makes LAN standards.
  - *Global IP addresses कौन allocate करता है? — ICANN/IANA (RIRs के साथ)। IETF protocols बनाता है, IEEE LAN standards।*
- **Device-layer ladder (1/2/3/7)?** — ✔ Hub/Repeater/Modem = 1; Switch/Bridge/NIC = 2; Router = 3; Gateway = 7.
  - *Device-layer ladder (1/2/3/7)? — Hub/Repeater/Modem = 1; Switch/Bridge/NIC = 2; Router = 3; Gateway = 7।*
- **Dumb devices?** — ✔ Hub and Repeater (no address reading). Bridge/switch/router = intelligent.
  - *Dumb devices? — Hub और Repeater (address नहीं पढ़ते)। Bridge/switch/router = intelligent।*
- **Hub vs switch — collision domain?** — ✔ Hub = 1 collision domain for all ports. Switch = per-port collision domain.
  - *Hub vs switch — collision domain? — Hub = सभी ports के लिए 1 collision domain। Switch = per-port collision domain।*
- **Who separates broadcast domains?** — ✔ Router (and VLANs on a switch). Switch alone does NOT.
  - *Broadcast domains कौन अलग करता है? — Router (और switch पर VLANs)। अकेला switch नहीं।*
- **Switch CAM table stores?** — ✔ MAC addresses (learned from source MACs) — for fast frame forwarding.
  - *Switch CAM table में क्या होता है? — MAC addresses (source MACs से सीखे) — तेज़ frame forwarding के लिए।*
- **Unknown unicast at a switch?** — ✔ Flood out all ports (except source). Known = single port. Broadcast = flood.
  - *Switch पर unknown unicast? — सभी ports से flood (source को छोड़कर)। Known = एक port। Broadcast = flood।*
- **Router between two switches + broadcast?** — ✔ Broadcast does NOT cross the router — the other side receives nothing.
  - *दो switches के बीच router + broadcast? — Broadcast router पार नहीं करता — दूसरी ओर कुछ नहीं मिलता।*
- **4 VLANs = ? broadcast domains** — ✔ 4 (each VLAN is its own broadcast domain).
  - *4 VLANs = ? broadcast domains — 4 (हर VLAN अपना broadcast domain है)।*
- **Access point operates at?** — ✔ Layer 2 — it is a wireless bridge (802.3 ↔ 802.11 frames).
  - *Access point किस layer पर? — Layer 2 — यह wireless bridge है (802.3 ↔ 802.11 frames)।*
- **What does a router do per hop?** — ✔ Decrements TTL, updates checksum, rewrites BOTH MAC addresses. IP addresses stay same.
  - *हर hop पर router क्या करता है? — TTL घटाता है, checksum अपडेट करता है, दोनों MAC addresses बदलता है। IP addresses same रहते हैं।*
- **Router functions NOT included?** — ✔ Collision detection (that's Layer-2 CSMA/CD on switches/NICs).
  - *Router के काम में क्या शामिल नहीं? — Collision detection (वह Layer-2 CSMA/CD है — switches/NICs पर)।*
- **Routers reassemble fragments?** — ✔ NO — only the destination reassembles. Routers may fragment but never reassemble.
  - *Routers fragments जोड़ते हैं? — नहीं — केवल destination जोड़ता है। Routers fragment कर सकते हैं पर कभी नहीं जोड़ते।*
- **RED technique?** — ✔ Random Early Detection — drops packets early (randomly) to avoid congestion collapse.
  - *RED technique? — Random Early Detection — congestion से बचने के लिए जल्दी (randomly) packets छोड़ता है।*
- **Gateway = ?** — ✔ Protocol converter — links systems with DIFFERENT protocols (works at all 7 layers).
  - *Gateway = ? — Protocol converter — भिन्न protocols वाले systems जोड़ता है (सभी 7 layers पर)।*
- **Default gateway means?** — ✔ The router IP used to leave the local network (gateway of last resort).
  - *Default gateway का अर्थ? — Local network छोड़ने के लिए उपयोग होने वाला router IP (gateway of last resort)।*
- **Firewall = ?** — ✔ Security system between trusted private & untrusted outside networks — filters traffic.
  - *Firewall = ? — Trusted private और untrusted outside networks के बीच security system — traffic filter करता है।*
- **Packet-filtering vs stateful vs proxy firewall?** — ✔ L3/L4 IP rules (stateless) → tracks sessions → L7 intermediary (hides clients).
  - *Packet-filtering vs stateful vs proxy firewall? — L3/L4 IP rules (stateless) → sessions याद → L7 intermediary (clients छिपाती है)।*
- **Static NAT vs PAT?** — ✔ Static = 1 private ↔ 1 public (permanent). PAT = many private ↔ 1 public (ports).
  - *Static NAT vs PAT? — Static = 1 private ↔ 1 public (स्थायी)। PAT = many private ↔ 1 public (ports)।*
- **MUX = ?** — ✔ Multiplexer — combines many I/O signals into ONE line (FDM/TDM/WDM); demux splits again.
  - *MUX = ? — Multiplexer — कई I/O signals को एक line में मिलाता है (FDM/TDM/WDM); demux फिर अलग करता है।*
- **Intelligent devices?** — ✔ Switch + router (they read addresses & decide). Repeater + hub = dumb.
  - *Intelligent devices? — Switch + router (address पढ़कर निर्णय लेते हैं)। Repeater + hub = dumb।*
- **File server = ?** — ✔ A specialised computer that stores & serves files to clients.
  - *File server = ? — एक विशेष computer जो clients को files संग्रहित करके देता है।*
- **Repeaters extend network how?** — ✔ Regenerate (amplify + reshape) signals — so data can travel farther without degradation.
  - *Repeaters network कैसे बढ़ाते हैं? — Signals regenerate (amplify + reshape) करके — data बिना कमज़ोरी के दूर तक जा सकता है।*
- **Attenuation / distortion / noise?** — ✔ Strength loss / shape change / unwanted signals. Noise can only be MINIMISED, never removed.
  - *Attenuation / distortion / noise? — Strength loss / shape change / unwanted signals। Noise केवल कम होती है, कभी पूरी तरह नहीं।*
- **Crosstalk cause?** — ✔ Electromagnetic coupling between nearby pairs — minimised by tighter twists.
  - *Crosstalk का कारण? — पास की pairs के बीच electromagnetic coupling — tighter twists से कम होता है।*
- **Manchester encoding?** — ✔ Mid-bit transition = self-clocking + DC-free + noise-resistant (Physical layer).
  - *Manchester encoding? — Mid-bit transition = self-clocking + DC-free + noise-resistant (Physical layer)।*
- **Encoding redundancy order?** — ✔ 1B2B (100%) > 4B5B/8B10B (25%) > 5B6B (20%). Gigabit fiber = 8B/10B.
  - *Encoding redundancy क्रम? — 1B2B (100%) > 4B5B/8B10B (25%) > 5B6B (20%)। Gigabit fiber = 8B/10B।*
- **Scrambler use?** — ✔ Make the line signal look random (break long runs) — helps clock recovery. Not compression.
  - *Scrambler का उपयोग? — Line signal को random बनाना (लंबे runs तोड़ना) — clock recovery में मदद। Compression नहीं।*
- **Shannon & Nyquist formulas?** — ✔ C = B·log₂(1+SNR) (noisy); C = 2B·log₂(L) (noiseless).
  - *Shannon और Nyquist सूत्र? — C = B·log₂(1+SNR) (noisy); C = 2B·log₂(L) (noiseless)।*
- **Bit rate vs baud rate?** — ✔ Bit rate = baud × bits per signal unit.
  - *Bit rate बनाम baud rate? — Bit rate = baud × प्रति signal unit bits।*
- **Time to send n bits at b bps?** — ✔ t = n/b seconds.
  - *b bps पर n bits का समय? — t = n/b seconds।*
- **Analog signal parameters?** — ✔ Amplitude (height), Frequency (cycles/sec, Hz), Phase (start), Wavelength (distance/cycle).
  - *Analog signal parameters? — Amplitude (ऊँचाई), Frequency (cycles/sec, Hz), Phase (शुरुआत), Wavelength (दूरी/cycle)।*
- **Quantization noise in?** — ✔ PCM (Pulse Code Modulation) — rounding analog samples to levels.
  - *Quantization noise किसमें? — PCM (Pulse Code Modulation) — analog samples को levels पर गोल करना।*
- **Baseband vs broadband?** — ✔ Baseband = digital signals directly. Broadband = modulated analog carriers (FDM).
  - *Baseband बनाम broadband? — Baseband = digital signals सीधे। Broadband = modulated analog carriers (FDM)।*
- **Bandwidth vs throughput?** — ✔ Bandwidth = max capacity; Throughput = actual data per second (exam often mixes them).
  - *Bandwidth बनाम throughput? — Bandwidth = अधिकतम capacity; Throughput = वास्तविक data प्रति सेकंद (exam में अक्सर मिलाया जाता है)।*
- **Fiber's 3 superpowers?** — ✔ EMI-immune, tap-proof, highest bandwidth (via total internal reflection).
  - *Fiber की 3 शक्तियाँ? — EMI-मुक्त, tap-सुरक्षित, सर्वोच्च bandwidth (total internal reflection से)।*
- **TIR condition?** — ✔ Angle of incidence > critical angle (denser to rarer medium).
  - *TIR शर्त? — Angle of incidence > critical angle (denser से rarer medium)।*
- **UTP / coax / fiber distance limits?** — ✔ 100 m / 185-500 m / up to tens of km (single-mode).
  - *UTP / coax / fiber दूरी सीमाएँ? — 100 m / 185-500 m / दसियों km तक (single-mode)।*
- **Connectors?** — ✔ RJ-45 (twisted pair), BNC (coax), SC/ST/LC (fiber), RJ-11 (telephone).
  - *Connectors? — RJ-45 (twisted pair), BNC (coax), SC/ST/LC (fiber), RJ-11 (telephone)।*
- **Coax reflection cause?** — ✔ Wrong termination resistance (impedance mismatch).
  - *Coax reflection का कारण? — गलत termination resistance (impedance mismatch)।*
- **Single-mode vs multi-mode fiber?** — ✔ Single = long haul (km, backbone). Multi = short LAN distances (modal dispersion).
  - *Single-mode बनाम multi-mode fiber? — Single = लंबी दूरी (km, backbone)। Multi = छोटी LAN दूरी (modal dispersion)।*
- **Wi-Fi rate order?** — ✔ b (11 Mbps) < g (54) < n (600) < ac (multi-Gbps).
  - *Wi-Fi rate क्रम? — b (11 Mbps) < g (54) < n (600) < ac (multi-Gbps)।*
- **Line-of-sight wireless?** — ✔ Infrared (and microwave links) need LOS. Radio (Wi-Fi/Bluetooth) passes walls.
  - *Line-of-sight wireless? — Infrared (और microwave links) को LOS चाहिए। Radio (Wi-Fi/Bluetooth) दीवारों से गुजरता है।*
- **Microwave band?** — ✔ 300 MHz - 300 GHz (NOT 300 GHz-400 THz — that is infrared!).
  - *Microwave band? — 300 MHz - 300 GHz (300 GHz-400 THz नहीं — वह infrared है!)।*
- **Bluetooth = ?** — ✔ 2.4 GHz short-range radio (IEEE 802.15.1 WPAN).
  - *Bluetooth = ? — 2.4 GHz short-range radio (IEEE 802.15.1 WPAN)।*
- **FDMA / TDMA / CDMA?** — ✔ Frequency bands / time slots / unique codes (same band & time).
  - *FDMA / TDMA / CDMA? — Frequency bands / time slots / unique codes (same band और time)।*
- **DLL = ?** — ✔ MAC + LLC. MAC = physical addressing + medium access; LLC = flow/error control + interface.
  - *DLL = ? — MAC + LLC. MAC = physical addressing + medium access; LLC = flow/error control + interface.*
- **Routing किस layer का?** — ✔ Network layer (L3) का. DLL सिर्फ अगले hop तक पहुँचाता है.
  - *Routing किस layer का? — Network layer (L3) का. DLL सिर्फ अगले hop तक पहुँचाता है.*
- **SW / GBN / SR windows?** — ✔ SW = 1; GBN ≤ 2ⁿ−1; SR ≤ 2ⁿ⁻¹ (N/2). SR सिर्फ गलत frame दोहराता है.
  - *SW / GBN / SR windows? — SW = 1; GBN ≤ 2ⁿ−1; SR ≤ 2ⁿ⁻¹ (N/2). SR सिर्फ गलत frame दोहराता है.*
- **Hamming distance d=3 क्या देता है?** — ✔ 2 errors detect या 1 error correct. d ≥ 2t+1.
  - *Hamming distance d=3 क्या देता है? — 2 errors detect या 1 error correct. d ≥ 2t+1.*
- **Parity क्या पकड़ता है?** — ✔ Odd number of errors. Simple parity = 1 bit; 2D parity = rows+columns.
  - *Parity क्या पकड़ता है? — Odd number of errors. Simple parity = 1 bit; 2D parity = rows+columns.*
- **CRC vs Checksum?** — ✔ DLL = CRC (FCS field); Network/Transport = checksum. Integrity = message digest.
  - *CRC vs Checksum? — DLL = CRC (FCS field); Network/Transport = checksum. Integrity = message digest.*
- **Ethernet frame limits?** — ✔ Min 64 / Max 1518 bytes; data 46–1500 (MTU 1500). Min size = CSMA/CD collision detection.
  - *Ethernet frame limits? — Min 64 / Max 1518 bytes; data 46–1500 (MTU 1500). Min size = CSMA/CD collision detection.*
- **Frame field order?** — ✔ Preamble → Dest MAC → Source MAC → Type → Data → FCS. FCS = CRC.
  - *Frame field order? — Preamble → Dest MAC → Source MAC → Type → Data → FCS. FCS = CRC.*
- **Bit stuffing?** — ✔ Data में पाँच 1s के बाद 0 ठूँसना (flag से confusion रोकना). HDLC bit-oriented; PPP byte-oriented.
  - *Bit stuffing? — Data में पाँच 1s के बाद 0 ठूँसना (flag से confusion रोकना). HDLC bit-oriented; PPP byte-oriented.*
- **ALOHA formulas?** — ✔ Pure: 2T vulnerable, G·e⁻²ᴳ (~18.4%). Slotted: T vulnerable, G·e⁻ᴳ (~36.8%).
  - *ALOHA formulas? — Pure: 2T vulnerable, G·e⁻²ᴳ (~18.4%). Slotted: T vulnerable, G·e⁻ᴳ (~36.8%).*
- **CSMA/CD vs CSMA/CA?** — ✔ CD = wired Ethernet (jam signal); CA = wireless (RTS/CTS, NAV). Jam = collision की घोषणा.
  - *CSMA/CD vs CSMA/CA? — CD = wired Ethernet (jam signal); CA = wireless (RTS/CTS, NAV). Jam = collision की घोषणा.*
- **Token Ring mode?** — ✔ Round Robin (token passing). Reservation mode में slot पहले book करते हैं.
  - *Token Ring mode? — Round Robin (token passing). Reservation mode में slot पहले book करते हैं.*
- **IPv4 header key sizes?** — ✔ Min header 20B; Total Length 16-bit; Fragment Offset 13-bit; TTL 8-bit; ToS = priority.
  - *IPv4 header key sizes? — Min header 20B; Total Length 16-bit; Fragment Offset 13-bit; TTL 8-bit; ToS = priority.*
- **Fragmentation vs Reassembly?** — ✔ MF flag + Fragment Offset से. टुकड़े routers भी कर सकते हैं; जोड़ना सिर्फ destination.
  - *Fragmentation vs Reassembly? — MF flag + Fragment Offset से. टुकड़े routers भी कर सकते हैं; जोड़ना सिर्फ destination.*
- **ARP / RARP / DNS / DHCP?** — ✔ ARP = IP→MAC; RARP = MAC→IP (obsolete); DNS = name→IP; DHCP = automatic IP (zeroconf).
  - *ARP / RARP / DNS / DHCP? — ARP = IP→MAC; RARP = MAC→IP (obsolete); DNS = name→IP; DHCP = automatic IP (zeroconf).*
- **ICMP/IGMP किस layer के?** — ✔ Network layer. ICMP = ping/errors/PMTU; IGMP = multicast membership. Echo = query, error नहीं.
  - *ICMP/IGMP किस layer के? — Network layer. ICMP = ping/errors/PMTU; IGMP = multicast membership. Echo = query, error नहीं.*
- **Routing protocol families?** — ✔ RIP = Distance vector (Bellman-Ford, max 15 hops); OSPF/IS-IS = Link state (Dijkstra); BGP = Path vector (Inter-AS).
  - *Routing protocol families? — RIP = Distance vector (Bellman-Ford, max 15 hops); OSPF/IS-IS = Link state (Dijkstra); BGP = Path vector (Inter-AS).*
- **DV की कमी और उपाय?** — ✔ Count-to-infinity. उपाय: split horizon + poison reverse + hold-down.
  - *DV की कमी और उपाय? — Count-to-infinity. उपाय: split horizon + poison reverse + hold-down.*
- **STP और MPLS?** — ✔ STP = L2 loops रोकता है; MPLS = 'Layer 2.5' (labels, QoS).
  - *STP और MPLS? — STP = L2 loops रोकता है; MPLS = 'Layer 2.5' (labels, QoS).*
- **TCP vs UDP?** — ✔ TCP = reliable, ordered, connection-oriented, broadcast नहीं; UDP = connectionless, fast.
  - *TCP vs UDP? — TCP = reliable, ordered, connection-oriented, broadcast नहीं; UDP = connectionless, fast.*
- **Socket = ?** — ✔ IP + Port. Ports 16-bit (0–65535). Connection = socket pair.
  - *Socket = ? — IP + Port. Ports 16-bit (0–65535). Connection = socket pair.*
- **TCP handshake और flags?** — ✔ SYN → SYN-ACK → ACK (ESTABLISHED). SYN = शुरुआत, FIN = अंत, RST = रद्द.
  - *TCP handshake और flags? — SYN → SYN-ACK → ACK (ESTABLISHED). SYN = शुरुआत, FIN = अंत, RST = रद्द.*
- **TCP flow vs congestion control?** — ✔ Flow = receiver window (rwnd); Congestion = cwnd (slow start, avoidance). Effective = min(rwnd, cwnd).
  - *TCP flow vs congestion control? — Flow = receiver window (rwnd); Congestion = cwnd (slow start, avoidance). Effective = min(rwnd, cwnd).*
- **TCP attacks और बचाव?** — ✔ SYN flood (handshake), session hijacking (random ISN से बचाव).
  - *TCP attacks और बचाव? — SYN flood (handshake), session hijacking (random ISN से बचाव).*
- **Port numbers?** — ✔ 21/20 FTP, 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 67/68 DHCP, 80 HTTP, 443 HTTPS, 110 POP3, 143 IMAP.
  - *Port numbers? — 21/20 FTP, 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 67/68 DHCP, 80 HTTP, 443 HTTPS, 110 POP3, 143 IMAP.*
- **Secure vs असुरक्षित protocols?** — ✔ Secure: HTTPS, SSH, SFTP, FTPS. असुरक्षित: HTTP, FTP, Telnet. SSL/TLS = browser-server encryption.
  - *Secure vs असुरक्षित protocols? — Secure: HTTPS, SSH, SFTP, FTPS. असुरक्षित: HTTP, FTP, Telnet. SSL/TLS = browser-server encryption.*
- **Presentation layer के काम?** — ✔ Compression, encryption, translation. Syntax = format; Semantics = meaning.
  - *Presentation layer के काम? — Compression, encryption, translation. Syntax = format; Semantics = meaning.*
- **FTP की ख़ासियत?** — ✔ दो TCP connections (control 21 + data 20); TFTP UDP पर (port 69); NFS = remote files को local जैसा.
  - *FTP की ख़ासियत? — दो TCP connections (control 21 + data 20); TFTP UDP पर (port 69); NFS = remote files को local जैसा.*
- **Ping / traceroute?** — ✔ Ping = reachability (ICMP Echo); traceroute = रास्ता (Linux=UDP, Windows=ICMP). 403 = Forbidden.
  - *Ping / traceroute? — Ping = reachability (ICMP Echo); traceroute = रास्ता (Linux=UDP, Windows=ICMP). 403 = Forbidden.*
- **Multiplexing किस layer का?** — ✔ Transport layer (ports से processes share करते हैं). Presentation = data का रूप.
  - *Multiplexing किस layer का? — Transport layer (ports से processes share करते हैं). Presentation = data का रूप.*
- **CIA triad?** — ✔ Confidentiality, Integrity, Availability.
  - *CIA triad? — Confidentiality, Integrity, Availability।*
- **Goal of each: interception / modification / DoS / spoofing?** — ✔ Confidentiality / Integrity / Availability / Authentication.
  - *हर एक का लक्ष्य: interception / modification / DoS / spoofing? — Confidentiality / Integrity / Availability / Authentication।*
- **Active vs passive attack?** — ✔ Active = changes/disrupts data. Passive = only observes (eavesdrop, traffic analysis).
  - *Active बनाम passive attack? — Active = data बदलता/बाधित करता है। Passive = केवल देखता है (eavesdrop, traffic analysis)।*
- **Virus phases?** — ✔ Dormant → Propagation → Triggering → Execution (payload runs).
  - *Virus phases? — Dormant → Propagation → Triggering → Execution (payload चलता है)।*
- **WORM medium?** — ✔ Optical disk (CD-R/DVD-R) — write once, read many.
  - *WORM medium? — Optical disk (CD-R/DVD-R) — एक बार लिखें, कई बार पढ़ें।*
- **Symmetric vs asymmetric keys?** — ✔ 1 shared key (fast, key-distribution problem) vs key pair public+private (slow).
  - *Symmetric बनाम asymmetric keys? — 1 shared key (तेज़, key-distribution समस्या) बनाम key pair public+private (धीमा)।*
- **Encrypt/decrypt vs sign/verify direction?** — ✔ Encrypt public → decrypt private. Sign private → verify public.
  - *Encrypt/decrypt बनाम sign/verify दिशा? — Encrypt public → decrypt private। Sign private → verify public।*
- **DES / AES / RSA basics?** — ✔ DES = 64-bit block/56-bit key. AES = 128-bit block (128/192/256 keys). RSA = asymmetric.
  - *DES / AES / RSA basics? — DES = 64-bit block/56-bit key। AES = 128-bit block (128/192/256 keys)। RSA = asymmetric।*
- **Stream vs block cipher?** — ✔ Stream = 1 bit/byte at a time (RC4). Block = fixed blocks (DES/AES).
  - *Stream बनाम block cipher? — Stream = 1 bit/byte at a time (RC4)। Block = fixed blocks (DES/AES)।*
- **Caesar cipher type?** — ✔ Classical substitution (replace letters by shifting).
  - *Caesar cipher प्रकार? — Classical substitution (अक्षरों को खिसका कर बदलना)।*
- **Steganography terms?** — ✔ Cover file (carrier) + secret message → stego-object. Detection = steganalysis.
  - *Steganography terms? — Cover file (carrier) + secret message → stego-object। पहचान = steganalysis।*
- **False-friend: RSA is symmetric?** — ✔ NO — RSA is ASYMMETRIC. AES/DES/Blowfish are symmetric.
  - *False-friend: RSA symmetric है? — नहीं — RSA ASYMMETRIC है। AES/DES/Blowfish symmetric हैं।*
- **Security tools?** — ✔ Wireshark = sniff, Nmap = port scan, Cain&Abel = password crack, Angry IP = IP scan, Snort = IDS.
  - *Security tools? — Wireshark = sniff, Nmap = port scan, Cain&Abel = password crack, Angry IP = IP scan, Snort = IDS।*
- **Key reuse risk?** — ✔ Known-plaintext / frequency analysis attacks become possible.
  - *Key reuse जोखिम? — Known-plaintext / frequency analysis attacks संभव हो जाते हैं।*
- **DMZ?** — ✔ Buffer zone between internet & trusted LAN — public servers face outside, internals stay safe.
  - *DMZ? — Internet और trusted LAN के बीच buffer zone — public servers बाहर, internals सुरक्षित।*
- **IPSec modes?** — ✔ Transport = payload only (host-to-host end-to-end). Tunnel = whole packet (gateway VPN).
  - *IPSec modes? — Transport = केवल payload (host-to-host end-to-end)। Tunnel = पूरा packet (gateway VPN)।*
- **IPSec / SSL / PGP / WPA2 layers?** — ✔ Network / Transport-Presentation / Application / Data Link (Wi-Fi).
  - *IPSec / SSL / PGP / WPA2 layers? — Network / Transport-Presentation / Application / Data Link (Wi-Fi)।*
- **Firewall / port filter / MAC filter / signature layers?** — ✔ Network / Transport / Data Link / Application.
  - *Firewall / port filter / MAC filter / signature layers? — Network / Transport / Data Link / Application।*
- **SSL/TLS handshake does?** — ✔ Key exchange + server authentication (certificates). Record protocol does encryption.
  - *SSL/TLS handshake करता है? — Key exchange + server authentication (certificates)। Encryption Record protocol करता है।*
- **HTTPS = ?** — ✔ HTTP + SSL/TLS on port 443.
  - *HTTPS = ? — HTTP + SSL/TLS port 443 पर।*
- **DoS vs DDoS?** — ✔ Single-source flooding vs distributed (many zombies/botnet) flooding.
  - *DoS बनाम DDoS? — Single-source flooding बनाम distributed (कई zombies/botnet) flooding।*
- **Attack examples map?** — ✔ Phishing=steal credentials; MitM=intercept; Spoofing=impersonate; Smurf=DoS variant.
  - *Attack examples map? — Phishing=credentials चुराना; MitM=intercept; Spoofing=impersonate; Smurf=DoS variant।*