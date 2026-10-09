# Data Communication & Computer Networks (CN)
## Topic 1 of 7 : Introduction of DC (Data Communication) — 91 MCQs (English + Hindi)

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** Rajasthan Govt. Competitive Exams (REET / RAS / RPSC Programmer / BCI / SCI & Others)

**Total Questions:** 91 | **Type:** MCQ (4 options each) | **Bilingual:** English + Hindi | Every question has: ✔ Correct answer (why right) + ★ Nukta (key point) + ✖ option-wise verification (why each wrong option is wrong). All answers cross-verified 4 times.

**Source files read from the repo (main branch):** CN Topic Test-01 (UNIT TEST-1), CN Topic Test-02 (UNIT TEST-2), CN Topic Test-03 (UNIT TEST-3), BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), BCI_SCI Subject Test-7 (UNIT TEST-2 BCI/SCI), BCI Subject Test-8 (UNIT TEST-3 BCI/SCI), Random Test- Rajasthan PYQ (scanned, OCR). Verification: Subject Test Solution -1 (CN & Security) + Part-2 official answer key (scanned, OCR) + Extra Forouzan-verified questions.

### Syllabus Coverage (sub-topic wise order)

| # | Sub-topic (as per syllabus) | Questions |
|---|------------------------------|-----------|
| 1 | DC Components (Message, Sender, Receiver, Transmission Medium, Protocol) | Q1 - Q14 |
| 2 | Characteristics (Delivery, Accuracy, Timeliness, Jitter) & Criteria (Performance, Reliability, Security) | Q15 - Q27 |
| 3 | Transmission Mode (Simplex, Half-Duplex, Full-Duplex) | Q28 - Q34 |
| 4 | Network Structure / Topology (Physical: Mesh, Star, Bus, Ring, Others; Logical: IEEE 802) | Q35 - Q47 |
| 5 | Types of Networks (LAN, MAN, WAN, PAN, CAN, SAN; Internet, Intranet, Extranet; Point-to-Point, Multipoint; Client-Server, P2P) | Q48 - Q72 |
| 6 | Network History (ARPANET to today's network) | Q73 - Q80 |
| 7 | General Network Basics (WWW, E-mail, Protocols, Servers, Switching) | Q81 - Q91 |

---

## Section A - DC Components & Protocol Basics (Message, Sender, Receiver, Transmission Medium, Protocol)

*Syllabus: DC Components - Message, Sender, Receiver, Transmission Medium, Protocol*

### Q1. The _______ is the physical path over which a message travels from sender to receiver.

<span lang='hi'>_______ वह भौतिक पथ (physical path) है जिस पर संदेश sender से receiver तक जाता है।</span>

- **(A)** Path / पथ
- **(B)** Medium / माध्यम ✅ **(CORRECT)**
- **(C)** Protocol / प्रोटोकॉल
- **(D)** Route / रूट (path)

**✔ Correct Answer: (B) Medium** — In data communication, the transmission medium is the physical path (twisted-pair, coaxial, fiber or radio waves) by which the message travels from sender to receiver. (Forouzan)

*Data communication में transmission medium वह physical path hai (twisted-pair, coaxial, fiber या radio waves) jis पर message sender से receiver तक जाता है। (Forouzan)*

**★ Nukta (Key Point):** Medium = physical path between sender and receiver. Remember: Message -> Sender -> Medium -> Receiver.

*Medium = sender और receiver के बीच का physical path. Yaad rakho: Message -> Sender -> Medium -> Receiver.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Path is a general word; the technical term in data communication is transmission medium. / Path एक common shabd hai; data communication में technical term transmission medium hai।
- **(C)** Protocol is the set of rules, not the physical path. / Protocol niyamon ka set hai, physical path nahi।
- **(D)** A route is a chosen path in a network (routing concept), not the physical medium itself. / Route network में chuna gaya рaste hai (routing), physical medium khud nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q35]*

---
### Q2. The information to be communicated in a data communication system is called the _______.

<span lang='hi'>Data communication system में communicate की जाने वाली information _______ कहलाती है।</span>

- **(A)** Medium / माध्यम
- **(B)** Protocol / प्रोटोकॉल
- **(C)** Message / संदेश (message) ✅ **(CORRECT)**
- **(D)** Transmission / संचरण (transmission)

**✔ Correct Answer: (C) Message** — Forouzan: The message is the data (information) to be communicated. It can be text, numbers, images, audio or video.

*Forouzan: Message = communicate की जाने वाली data (information). Ye text, numbers, images, audio या video ho sakti hai।*

**★ Nukta (Key Point):** Message = the data/information to be communicated. 5 popular forms: text, numbers, images, audio, video.

*Message = communicate की जाने वाली data. 5 popular forms: text, numbers, images, audio, video.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Medium is the physical path, not the information. / Medium physical path hai, information nahi।
- **(B)** Protocol is the set of rules, not the information. / Protocol niyam hai, information nahi।
- **(D)** Transmission is the process of sending, not the information itself. / Transmission bhejne ki prakriya hai, information khud nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q38]*

---
### Q3. Which of the following shares the data of two computers?

<span lang='hi'>निम्नलिखित में से कौन दो computers का data share (साझा) करता है?</span>

- **(A)** Library / पुस्तकालय
- **(B)** Network / नेटवर्क ✅ **(CORRECT)**
- **(C)** Grouping / समूह (grouping)
- **(D)** Integrated system / एकीकृत प्रणाली

**✔ Correct Answer: (B) Network** — A computer network is a set of devices (nodes) connected together mainly to share data, resources and information between computers.

*Computer network = devices (nodes) का aisa connection jo mainly computers के बीच data, resources aur information share karne ke liye hota hai।*

**★ Nukta (Key Point):** Network = 2 or more devices connected to share data/resources.

*Network = 2 ya zyada devices ka aapas mein judna, data/resources share karne ke liye।*

**✖ Why the other options are WRONG (verified):**
- **(A)** A library is a place/collection of books; it does not share computer data. / Library pusvajon ka sthal hai; computer data share nahi karti।
- **(C)** Grouping is just putting things together; there is no communication link. / Grouping sirf cheezein jodna hai; ismein communication link nahi hota।
- **(D)** An integrated system is one combined system, not a link between two computers. / Integrated system ek hi combined system hai, do computers ke beech link nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q13]*

---
### Q4. In a computer network, nodes are:

<span lang='hi'>Computer network में nodes होते हैं:</span>

- **(A)** the computer that originates the data / जो computer data को originate (shurua) करता है
- **(B)** the computer that routes the data / जो computer data को route करता है
- **(C)** the computer that terminates the data / जो computer data को terminate (समाप्त) करता है
- **(D)** all of the mentioned / उपर्युक्त सभी (all of the above) ✅ **(CORRECT)**

**✔ Correct Answer: (D) all of the mentioned** — A node is any device connected to the network. It can originate (sender), route (router/switch) or terminate (receiver) data, so all of the mentioned is correct.

*Node = network से juda koi bhi device. Ye data ko originate (sender), route (router/switch) ya terminate (receiver) kar sakta hai, isliye uparyukt sabhi sahi hain।*

**★ Nukta (Key Point):** Node = any connected device of the network (computer, printer, router, etc.).

*Node = network ka koi bhi connected device (computer, printer, router, ityadi).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Only originator is wrong: a node can also route or receive data. / Sirf originator galat hai: node route bhi kar sakta hai aur receive bhi।
- **(B)** Only router is wrong: a node can also be a sender or a receiver. / Sirf router galat hai: node sender bhi ho sakta hai aur receiver bhi।
- **(C)** Only terminator is wrong: a node can also originate or route data. / Sirf terminator galat hai: node originate bhi kar sakta hai aur route bhi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q30]*

---
### Q5. _______ refers to two characteristics: when data should be sent and how fast it can be sent.

<span lang='hi'>_______ दो characteristics को batata hai: data kab bheja jaye aur kitni tezi se bheja ja sakta hai।</span>

- **(A)** Semantics / अर्थ (semantics)
- **(B)** Syntax / संरचना (syntax)
- **(C)** Timing / समय-निर्धारण (timing) ✅ **(CORRECT)**
- **(D)** none of the above / इनमें से कोई नहीं

**✔ Correct Answer: (C) Timing** — The three key elements of a protocol are syntax, semantics and timing. Timing refers to two characteristics: when data should be sent and how fast it can be sent. (Forouzan)

*Protocol के 3 key elements hain: syntax, semantics aur timing. Timing do characteristics se juda hai: data kab bheja jaye aur kitni tezi se bheja ja sakta hai। (Forouzan)*

**★ Nukta (Key Point):** Protocol ke 3 elements = Syntax (format), Semantics (meaning), Timing (when & how fast).

*Protocol ke 3 elements = Syntax (format), Semantics (arth), Timing (kab aur kitni tezi se).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Semantics is the meaning of data, not when/how fast it is sent. / Semantics data ka arth hai, ye nahi batata ki kab/kitni tezi se bheja jaye।
- **(B)** Syntax is the structure/format of data, not the timing. / Syntax data ka structure/format hai, timing nahi।
- **(D)** None of the above is wrong, because Timing is exactly the correct element. / Timing hi sahi element hai, isliye inmein se koi nahi galat hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q44]*

---
### Q6. Consider the statements: S1: The physical medium of connection is known as a link. S2: The computers connected to it are known as nodes.

<span lang='hi'>कथनों पर विचार करें: S1: connection का physical medium link कहलाता है। S2: इससे जुड़े computers nodes कहलाते हैं।</span>

- **(A)** Both S1 and S2 are false / दोनों S1 और S2 galt hain
- **(B)** S1 true but S2 false / S1 sahi hai lekin S2 galt hai
- **(C)** S1 false but S2 true / S1 galt hai lekin S2 sahi hai
- **(D)** Both S1 and S2 true / दोनों S1 और S2 sahi hain ✅ **(CORRECT)**

**✔ Correct Answer: (D) Both S1 and S2 true** — In networking, the physical medium connecting devices is called a link, and the connected devices (computers) are called nodes. Both statements are true.

*Networking में devices ko jodne wala physical medium link कहलाता है, aur jude hue devices (computers) nodes कहलाते हैं। दोनों कथन sahi hain।*

**★ Nukta (Key Point):** Link = physical medium; Node = connected device (computer).

*Link = physical medium; Node = juda hua device (computer).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Both false is wrong: both statements are actually true. / Dono galt hai — dono sahi hain।
- **(B)** S2 is also true: the connected computers are indeed called nodes. / S2 bhi sahi hai: jude hue computers ko nodes hi kehte hain।
- **(C)** S1 is also true: the physical medium is indeed called a link. / S1 bhi sahi hai: physical medium ko hi link kehte hain।

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q2]*

---
### Q7. What are the main elements of a protocol? 1. Syntax  2. Semantics  3. Timing

<span lang='hi'>किसी protocol के मुख्य तत्व (elements) क्या हैं? 1. Syntax  2. Semantics  3. Timing</span>

- **(A)** 1, 2 only / sirf 1 और 2
- **(B)** 1, 3 only / sirf 1 और 3
- **(C)** 2, 3 only / sirf 2 और 3
- **(D)** 1, 2, 3 only / 1, 2 और 3 sabhi ✅ **(CORRECT)**

**✔ Correct Answer: (D) 1, 2, 3 only** — A protocol has three key elements: syntax (data format/structure), semantics (meaning of the data) and timing (when to send and how fast).

*Protocol ke 3 key elements hain: syntax (data ka format/structure), semantics (data ka arth) aur timing (kab bhejna hai aur kitni tezi se).*

**★ Nukta (Key Point):** Yaad rakho: Protocol = Syntax + Semantics + Timing.

*Yaad rakho: Protocol = Syntax + Semantics + Timing.*

**✖ Why the other options are WRONG (verified):**
- **(A)** 1,2 only misses Timing, which is also an element. / 1,2 mein Timing chhoot gaya, jo bhi ek element hai।
- **(B)** 1,3 only misses Semantics, which is also an element. / 1,3 mein Semantics chhoot gaya, jo bhi ek element hai।
- **(C)** 2,3 only misses Syntax, which is also an element. / 2,3 mein Syntax chhoot gaya, jo bhi ek element hai।

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q3]*

---
### Q8. A set of rules that governs data communication is called a:

<span lang='hi'>Data communication ko regulate (नियंत्रित) करने वाले rules का set _______ कहलाता है:</span>

- **(A)** rule / नियम (rule)
- **(B)** medium / माध्यम (medium)
- **(C)** Link / लिंक (link)
- **(D)** Protocol / प्रोटोकॉल (protocol) ✅ **(CORRECT)**

**✔ Correct Answer: (D) Protocol** — A protocol is a set of rules that governs data communication. It defines what is communicated, how it is communicated and when it is communicated. (Forouzan)

*Protocol = niyamon ka set jo data communication ko govern karta hai. Ye batata hai ki kya communicate hoga, kaise hoga aur kab hoga। (Forouzan)*

**★ Nukta (Key Point):** Protocol = rules ka set. Yaad rakho: without a protocol, two devices may be connected but cannot communicate.

*Protocol = niyamon ka set. Yaad rakho: bina protocol ke do devices jude to ho sakte hain lekin communicate nahi kar sakte।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Rule is a single rule, not the complete set of rules. / Rule ek akela niyam hai, poora set nahi।
- **(B)** Medium is the physical path, not the rules. / Medium physical path hai, niyam nahi।
- **(C)** Link is the physical connection, not the rules. / Link physical connection hai, niyam nahi।

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3), Q15]*

---
### Q9. The physical path between the sender and receiver is called:

<span lang='hi'>Sender aur receiver ke beech ka physical path _______ कहलाता है:</span>

- **(A)** Link / लिंक (link) ✅ **(CORRECT)**
- **(B)** Node / नोड (node)
- **(C)** Segment / सегмент (segment)
- **(D)** Socket / सॉकेट (socket)

**✔ Correct Answer: (A) Link** — In this context, the physical medium of connection between devices is known as a link (the devices connected to it are called nodes).

*Is context mein, devices ko jodne wala physical medium link कहलाता है (is se jude devices ko nodes kehte hain).*

**★ Nukta (Key Point):** Note: In Forouzan's 5 components, this same physical path is called the transmission medium. Both terms mean the physical path.

*Note: Forouzan ke 5 components mein isi physical path ko transmission medium kaha gaya hai। Dono ka matlab physical path hi hai।*

**✖ Why the other options are WRONG (verified):**
- **(B)** Node is the connected device, not the path between devices. / Node juda hua device hai, devices ke beech ka path nahi।
- **(C)** Segment is a part of a network path, not the whole physical medium. / Segment path ka ek hissa hai, poora physical medium nahi।
- **(D)** Socket is an IP + port endpoint, not a physical path. / Socket = IP + port ka endpoint hai, physical path nahi।

*[Source: Repo: BCI_SCI Subject Test-7 (UNIT TEST-2 BCI/SCI), Q20]*

---
### Q10. Consider: (1) Twisted pair cables (2) Microwaves and satellite signals (3) Repeaters (4) Analog transmissions (5) Fiber optics. Which of the above is considered as signal transmission medium in data communications?

<span lang='hi'>विचार करें: (1) Twisted pair cables (2) Microwaves और satellite signals (3) Repeaters (4) Analog transmissions (5) Fiber optics। उपरोक्त में से data communications में signal transmission medium के रूप में क्या माना जाता है?</span>

- **(A)** (1) and (5) / (1) aur (5)
- **(B)** (1) and (2) / (1) aur (2)
- **(C)** (1), (2) and (5) / (1), (2) aur (5) ✅ **(CORRECT)**
- **(D)** (1), (2), (3) and (5) / (1), (2), (3) aur (5)

**✔ Correct Answer: (C) (1), (2) and (5)** — Twisted pair, microwaves/satellite and fiber optics are transmission media (guided and unguided). A repeater is a device (it regenerates the signal), and analog transmission is a form of signal, not a medium.

*Twisted pair, microwaves/satellite aur fiber optics transmission media hain (guided aur unguided). Repeater ek device hai (signal regenerate karta hai), aur analog transmission signal ka ek roop hai, medium nahi।*

**★ Nukta (Key Point):** Guided media: twisted pair, coaxial, fiber. Unguided media: radio, microwave, infrared.

*Guided media: twisted pair, coaxial, fiber. Unguided media: radio, microwave, infrared.*

**✖ Why the other options are WRONG (verified):**
- **(A)** (1) and (5) misses (2): microwaves/satellite are also unguided media. / (1) aur (5) mein (2) chhoot gaya: microwave/satellite bhi unguided media hain।
- **(B)** (1) and (2) misses (5): fiber optics is also a medium. / (1) aur (2) mein (5) chhoot gaya: fiber optics bhi ek medium hai।
- **(D)** (3) Repeater is a device, not a transmission medium. / (3) Repeater ek device hai, transmission medium nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q10]*

---
### Q11. Data communication is the exchange of _______ between two devices via some form of transmission medium.

<span lang='hi'>Data communication = do devices ke beech _______ ka exchange, kisi transmission medium ke through।</span>

- **(A)** only text messages / sirf text messages
- **(B)** data (the message) - text, numbers, images, audio or video / data (message) - text, numbers, images, audio ya video ✅ **(CORRECT)**
- **(C)** only electrical signals / sirf electrical signals
- **(D)** only hardware devices / sirf hardware devices

**✔ Correct Answer: (B) data (the message) - text, numbers, images, audio or video** — Forouzan: Data communications is the exchange of data between two devices via some form of transmission medium. The data exchanged is called the message.

*Forouzan: Data communications = do devices ke beech kisi transmission medium ke through data ka exchange. Exchange hone wale data ko message kehte hain।*

**★ Nukta (Key Point):** Data communication = exchange of DATA (message) between two devices over a medium.

*Data communication = do devices ke beech DATA (message) ka exchange, medium ke through।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Too narrow: a message can also be numbers, images, audio and video. / Bahut sankuchit hai: message numbers, images, audio aur video bhi ho sakta hai।
- **(C)** Electrical/electromagnetic signals are only the form in which data travels, not what is exchanged. / Electrical/electromagnetic signals sirf woh roop hain jis mein data jaata hai, exchange nahi hota।
- **(D)** Hardware (sender/receiver) is the means of communication, not the content exchanged. / Hardware (sender/receiver) toh{HCl sadhan hai, exchange hone wala content nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q12. Which one of the following is NOT one of the five basic components of a data communication system?

<span lang='hi'>निम्नलिखित में से कौन data communication system के five basic components में से एक नहीं है?</span>

- **(A)** Message / Message (संदेश)
- **(B)** Protocol / Protocol (प्रोटोकॉल)
- **(C)** Router / Router (राउटर) ✅ **(CORRECT)**
- **(D)** Transmission medium / Transmission medium (माध्यम)

**✔ Correct Answer: (C) Router** — The five basic components are: message, sender, receiver, transmission medium and protocol. A router is a networking device (Network layer), not one of the five fundamental components.

*Five basic components hain: message, sender, receiver, transmission medium aur protocol. Router ek networking device hai (Network layer), five fundamental components mein se nahi।*

**★ Nukta (Key Point):** Yaad rakho 5 components: Message, Sender, Receiver, Transmission Medium, Protocol. Router = device, component nahi।

*Yaad rakho 5 components: Message, Sender, Receiver, Transmission Medium, Protocol. Router = device hai, component nahi।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Message IS a component: it is the data (information) to be communicated. / Message ek component hai: ye communicate ki jane wali data hai।
- **(B)** Protocol IS a component: the set of rules that governs the communication. / Protocol ek component hai: ye communication ke niyam hai।
- **(D)** Transmission medium IS a component: the physical path from sender to receiver. / Transmission medium ek component hai: sender se receiver tak ka physical path।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q13. The device that sends the data message in a data communication system is called the _______.

<span lang='hi'>Data communication system में jo device data message bhejta hai, use _______ kehte hain।</span>

- **(A)** Receiver / Receiver (प्राप्तकर्ता)
- **(B)** Sender / Sender (प्रेषक) ✅ **(CORRECT)**
- **(C)** Protocol / Protocol (प्रोटोकॉल)
- **(D)** Hub / Hub (हब)

**✔ Correct Answer: (B) Sender** — The sender is the device (computer, workstation, mobile phone, camera, TV, etc.) that sends the data message.

*Sender woh device hai (computer, workstation, mobile phone, camera, TV, ityadi) jo data message bhejta hai।*

**★ Nukta (Key Point):** Sender = source device; Receiver = destination device.

*Sender = source device; Receiver = destination device.*

**✖ Why the other options are WRONG (verified):**
- **(A)** The receiver is the destination: it receives the message, it does not send it. / Receiver destination hai: ye message receive karta hai, bhejta nahi।
- **(C)** A protocol is a set of rules, not a device. / Protocol niyam ka set hai, device nahi।
- **(D)** A hub is a Physical-layer device that joins cables; it is not defined as the sender of the message. / Hub ek Physical-layer device hai jo cables jodta hai; ye message ka sender nahi kehlaata।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q14. Which of the following best lists the popular forms of information (message) in data communication?

<span lang='hi'>Data communication में information (message) के popular forms ko sabse achhe se kaun batata hai?</span>

- **(A)** Only text and numbers / sirf text aur numbers
- **(B)** Only audio and video / sirf audio aur video
- **(C)** Text, numbers, images, audio and video / text, numbers, images, audio aur video ✅ **(CORRECT)**
- **(D)** Only binary digits / sirf binary digits

**✔ Correct Answer: (C) Text, numbers, images, audio and video** — Forouzan: The popular forms of information are text, numbers, images, audio, and video.

*Forouzan: Information ke popular forms hain text, numbers, images, audio, aur video.*

**★ Nukta (Key Point):** 5 popular forms of message: text, numbers, images, audio, video.

*Message ke 5 popular forms: text, numbers, images, audio, video.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Incomplete: images, audio and video are also valid forms. / Adhura hai: images, audio aur video bhi valid forms hain।
- **(B)** Incomplete: text, numbers and images are also valid forms. / Adhura hai: text, numbers aur images bhi valid forms hain।
- **(D)** Bits are the representation/encoding of data, not a separate popular form of message. / Bits data ka representation/encoding hai, koi alag popular form nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---

## Section B - Characteristics (Delivery, Accuracy, Timeliness, Jitter) & Criteria (Performance, Reliability, Security)

*Syllabus: Characteristics - Delivery, Accuracy, Timeliness, Jitter | Properties/Criteria - Performance, Reliability, Security*

### Q15. What does jitter refer to in data communication?

<span lang='hi'>Data communication में jitter ka matlab kya hota hai?</span>

- **(A)** Loss of data / data ka loss
- **(B)** Delay variation in packets / packets mein delay ka antar (variation) ✅ **(CORRECT)**
- **(C)** Data synchronization / data ka synchronization
- **(D)** Data encoding / data ka encoding

**✔ Correct Answer: (B) Delay variation in packets** — Jitter is the variation in packet arrival time. It is the uneven delay in the delivery of audio or video packets (e.g., video packets sent every 30 ms but arriving with 30 ms and 40 ms delays). (Forouzan)

*Jitter = packets ke pahunchne ke samay mein antar (variation). Ye audio ya video packets ki delivery mein uneven delay hai (jaise video packets har 30 ms par bheje jaate hain lekin 30 ms aur 40 ms ke delay se pahunchte hain). (Forouzan)*

**★ Nukta (Key Point):** Jitter = uneven delay in packet arrival -> distorted audio/video playback.

*Jitter = packet pahunchne mein uneven delay -> audio/video playback kharab ho jaati hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Loss of data is packet loss, not jitter. / Data ka loss = packet loss hai, jitter nahi।
- **(C)** Synchronization is about aligning data, not the variation in arrival time. / Synchronization data ko align karne ke baare mein hai, arrival time ke antar ke nahi।
- **(D)** Encoding is converting data into a suitable form, not a delay variation. / Encoding data ko suitable form mein badalna hai, delay ka antar nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q1]*

---
### Q16. Which of the following is a characteristic of data communication?

<span lang='hi'>निम्नलिखित में से कौन data communication की एक characteristic (विशेषता) है?</span>

- **(A)** Timeliness / समयपालन (timeliness) ✅ **(CORRECT)**
- **(B)** Delay / деری (delay)
- **(C)** Speed / गति (speed)
- **(D)** Size / आकार (size)

**✔ Correct Answer: (A) Timeliness** — The four fundamental characteristics of effective data communication are delivery, accuracy, timeliness and jitter. Timeliness means data must be delivered in a timely manner; data delivered late is useless.

*Effective data communication ki 4 fundamental characteristics hain: delivery, accuracy, timeliness aur jitter. Timeliness ka matlab hai data time par pahunchna; der se pahunchne wala data bekaar hai।*

**★ Nukta (Key Point):** 4 characteristics yaad rakho: Delivery, Accuracy, Timeliness, Jitter.

*4 characteristics yaad rakho: Delivery, Accuracy, Timeliness, Jitter.*

**✖ Why the other options are WRONG (verified):**
- **(B)** Delay itself is not a characteristic; jitter is the variation in delay. / Delay khud characteristic nahi; jitter delay ka antar hai।
- **(C)** Speed is a performance measure, not one of the four characteristics. / Speed ek performance measure hai, 4 characteristics mein nahi aata।
- **(D)** Size is not one of the four fundamental characteristics. / Size 4 fundamental characteristics mein nahi aata।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q6]*

---
### Q17. Accuracy in data communication means:

<span lang='hi'>Data communication में accuracy का अर्थ है:</span>

- **(A)** Data is sent quickly / data tezi se bheja jata hai
- **(B)** Data is not corrupted / data corrupted (खराब) नहीं होता ✅ **(CORRECT)**
- **(C)** Data is encrypted / data encrypt hota hai
- **(D)** Data reaches the receiver / data receiver tak pahunchta hai

**✔ Correct Answer: (B) Data is not corrupted** — Accuracy means the system must deliver the data accurately. Data that has been altered in transmission and left uncorrected is useless.

*Accuracy ka matlab hai system data ko accurately (sahi) pahunchaye. Jo data transmission mein badal gaya aur sudhara nahi gaya, bekaar hai।*

**★ Nukta (Key Point):** Accuracy = error-free data; altered/corrupted data is useless.

*Accuracy = error-free data; badal gaya/corrupt data bekaar hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Sending quickly is timeliness/speed, not accuracy. / Tezi se bhejna timeliness/speed hai, accuracy nahi।
- **(C)** Encryption is a security function, not accuracy. / Encryption ek security function hai, accuracy nahi।
- **(D)** Reaching the receiver is delivery, not accuracy. / Receiver tak pahunchna = delivery hai, accuracy nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q8]*

---
### Q18. What is the maximum data rate of a transmission medium known as?

<span lang='hi'>Transmission medium ki adhikatam data rate ko kya kaha jata hai?</span>

- **(A)** Bandwidth / bandwidth ✅ **(CORRECT)**
- **(B)** Throughput / throughput
- **(C)** Latency / latency
- **(D)** Jitter / jitter

**✔ Correct Answer: (A) Bandwidth** — Bandwidth is the maximum data rate (transmission capacity) of a communication channel/medium, usually measured in bits per second (bps).

*Bandwidth = kisi communication channel/medium ki adhikatam data rate (transmission capacity) hai, jise aam taur par bits per second (bps) mein maapa jata hai।*

**★ Nukta (Key Point):** Bandwidth = maximum capacity of the channel (in bps). Throughput = actual rate achieved (usually less).

*Bandwidth = channel ki adhikatam capacity (bps mein). Throughput = asli mein hasil hone wali rate (aam taur par kam).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Throughput is the actual data rate achieved, which is usually less than bandwidth. / Throughput asli mein hasil hone wali data rate hai, jo aam taur par bandwidth se kam hoti hai।
- **(C)** Latency is the delay before data transfer begins, not the maximum rate. / Latency data transfer shuru hone se pehle ki dely hai, adhikatam rate nahi।
- **(D)** Jitter is the variation in packet arrival time, not a data rate. / Jitter packet pahunchne ke samay ka antar hai, data rate nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q9]*

---
### Q19. Frequency of failure and network recovery time after a failure are measures of the _______ of a network.

<span lang='hi'>Failure ki aavritti (frequency) aur failure ke baad network recovery time kis cheez ke measures hain?</span>

- **(A)** Performance / performance
- **(B)** Reliability / reliability ✅ **(CORRECT)**
- **(C)** Security / security
- **(D)** Feasibility / feasibility

**✔ Correct Answer: (B) Reliability** — Reliability is measured by the frequency of failure (how often the network fails), the time it takes to recover after a failure, and robustness in a catastrophe. (Forouzan)

*Reliability ko failure ki frequency (network kitni baar fail hota hai), failure ke baad recover hone ka time, aur catastrophe mein robustness se maapa jata hai। (Forouzan)*

**★ Nukta (Key Point):** Reliability = failure frequency + recovery time + robustness. Performance = transit time, response time, throughput, delay.

*Reliability = failure frequency + recovery time + robustness. Performance = transit time, response time, throughput, delay.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Performance is measured by transit time, response time, throughput and delay. / Performance ko transit time, response time, throughput aur delay se maapa jata hai।
- **(C)** Security is about protection from unauthorized access and data integrity. / Security unauthorized access se bachav aur data integrity ke baare mein hai।
- **(D)** Feasibility is not one of the three network criteria. / Feasibility 3 network criteria mein se nahi hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q39]*

---
### Q20. An unauthorized user is a network _______ issue.

<span lang='hi'>An unauthorized user ek network _______ issue hai.</span>

- **(A)** Performance / performance
- **(B)** Reliability / reliability
- **(C)** Security / security ✅ **(CORRECT)**
- **(D)** All of the above / upar Sabhi

**✔ Correct Answer: (C) Security** — Security means protecting data from unauthorized access, protecting data from damage, and ensuring confidentiality and data integrity. An unauthorized user is a security issue.

*Security ka matlab hai data ko unauthorized access se bachana, damage se bachana, aur confidentiality aur data integrity sunishchit karna। Unauthorized user ek security issue hai।*

**★ Nukta (Key Point):** Security = unauthorized access se bachav + confidentiality + integrity (CIA triad).

*Security = unauthorized access se bachav + confidentiality + integrity (CIA triad).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Performance is about speed/throughput/delay, not unauthorized users. / Performance speed/throughput/delay ke baare mein hai, unauthorized users ke nahi।
- **(B)** Reliability is about failure frequency and recovery, not unauthorized users. / Reliability failure frequency aur recovery ke baare mein hai, unauthorized users ke nahi।
- **(D)** It is specifically a security issue, not all of the above. / Ye specifically ek security issue hai, sabhi nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q40]*

---
### Q21. What is the criteria to check the reliability of a network? 1. Downtime  2. Failure Frequency  3. Fault Tolerance  4. Security

<span lang='hi'>Network ki reliability check karne ke criteria kya hain? 1. Downtime  2. Failure Frequency  3. Fault Tolerance  4. Security</span>

- **(A)** 1, 2, 3 only / sirf 1, 2, 3 ✅ **(CORRECT)**
- **(B)** 2, 3, 4 only / sirf 2, 3, 4
- **(C)** 1, 2, 4 only / sirf 1, 2, 4
- **(D)** 1, 2, 3, 4 only / 1, 2, 3, 4 sabhi

**✔ Correct Answer: (A) 1, 2, 3 only** — Reliability is measured by downtime/frequency of failure, recovery time and fault tolerance (robustness). Security is a separate criterion of a network, not a reliability measure.

*Reliability ko downtime/failure frequency, recovery time aur fault tolerance (robustness) se maapa jata hai। Security ek alag criterion hai, reliability measure nahi।*

**★ Nukta (Key Point):** 3 network criteria: Performance, Reliability, Security. Reliability = failure frequency + recovery time + fault tolerance.

*3 network criteria: Performance, Reliability, Security. Reliability = failure frequency + recovery time + fault tolerance.*

**✖ Why the other options are WRONG (verified):**
- **(B)** 2,3,4 includes Security, which is a separate criterion, not reliability. / 2,3,4 mein Security hai, jo alag criterion hai, reliability nahi।
- **(C)** 1,2,4 includes Security, which is a separate criterion, not reliability. / 1,2,4 mein Security hai, jo alag criterion hai, reliability nahi।
- **(D)** Security (4) is not a reliability measure; the correct set is 1,2,3. / Security (4) reliability measure nahi hai; sahi set 1,2,3 hai।

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q1]*

---
### Q22. Which physical layer impairment mainly causes jitter in VoIP traffic?

<span lang='hi'>VoIP traffic mein jitter ka mukhya kaaran kaun sa physical layer impairment hai?</span>

- **(A)** Attenuation / attenuation (signal ki shakti kam hona)
- **(B)** Delay variation / delay ka antar (variation) ✅ **(CORRECT)**
- **(C)** Distortion / distortion (vikriti)
- **(D)** Crosstalk / crosstalk

**✔ Correct Answer: (B) Delay variation** — Jitter is caused by delay variation: packets experience different queuing/transmission delays, so they arrive at uneven intervals, distorting real-time VoIP/video.

*Jitter delay variation se hota hai: packets ko alag-alag queuing/transmission delays milte hain, isliye woh uneven intervals par pahunchte hain, jisse real-time VoIP/video kharab hota hai।*

**★ Nukta (Key Point):** Jitter = delay variation. Attenuation = signal weakening; distortion = signal shape change; crosstalk = interference from nearby cables.

*Jitter = delay variation. Attenuation = signal ki shakti kam hona; distortion = signal ka roop badalna; crosstalk = paas ki cables se interference.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Attenuation weakens the signal; it does not cause uneven arrival times. / Attenuation signal ko kamzor karta hai; uneven arrival times nahi banata।
- **(C)** Distortion changes the signal shape; it is not the cause of jitter. / Distortion signal ka roop badalta hai; ye jitter ka kaaran nahi।
- **(D)** Crosstalk is interference from adjacent cables, not delay variation. / Crosstalk adjacent cables se interference hai, delay variation nahi।

*[Source: Repo: BCI Subject Test-8 (UNIT TEST-3 BCI/SCI), Q36]*

---
### Q23. What network property is achieved through the use of the Automatic Repeat reQuest (ARQ) mechanism?

<span lang='hi'>Automatic Repeat reQuest (ARQ) mechanism se network ki kaun si property hasil hoti hai?</span>

- **(A)** Reliability / reliability ✅ **(CORRECT)**
- **(B)** Availability / availability
- **(C)** Confidentiality / confidentiality
- **(D)** Scalability / scalability

**✔ Correct Answer: (A) Reliability** — ARQ (Automatic Repeat reQuest) is an error-control mechanism: lost/corrupted frames are retransmitted, so reliable data transfer is achieved. Reliability is thus the property achieved.

*ARQ (Automatic Repeat reQuest) ek error-control mechanism hai: khoye/corrupt frames dobara bheje jaate hain, jisse reliable data transfer hota hai। Isliye reliability property hasil hoti hai।*

**★ Nukta (Key Point):** ARQ = error control -> Reliability. Flow control = efficient delivery (no overflow).

*ARQ = error control -> Reliability. Flow control = efficient delivery (receiver ka buffer overflow nahi hona).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Availability means the network is up/accessible, not error-free delivery. / Availability ka matlab network up/accessible hona hai, error-free delivery nahi।
- **(C)** Confidentiality means data is kept secret, not error-free delivery. / Confidentiality ka matlab data secret rakha jana hai, error-free delivery nahi।
- **(D)** Scalability means the network can grow, not error-free delivery. / Scalability ka matlab network badh sakta hai, error-free delivery nahi।

*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)]*

---
### Q24. For effective data communication, the system must deliver data to the correct destination. This characteristic is called _______.

<span lang='hi'>Effective data communication ke liye system ko data sahi destination par pahunchana chahiye। Is characteristic ko _______ kehte hain।</span>

- **(A)** Accuracy / accuracy
- **(B)** Timeliness / timeliness
- **(C)** Delivery / delivery ✅ **(CORRECT)**
- **(D)** Jitter / jitter

**✔ Correct Answer: (C) Delivery** — Delivery: the system must deliver data to the correct destination. Data must be received by the intended device or user and only by that device or user. (Forouzan)

*Delivery: system ko data sahi destination par pahunchana chahiye। Data sirf usi intended device/user ko pahunchna chahiye jis ke liye hai। (Forouzan)*

**★ Nukta (Key Point):** 4 characteristics: Delivery (right destination), Accuracy (error-free), Timeliness (on time), Jitter (even delay).

*4 characteristics: Delivery (sahi jagah), Accuracy (error-free), Timeliness (time par), Jitter (even delay).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Accuracy means data is delivered correctly (un-altered). / Accuracy ka matlab data bina badle (un-altered) pahunchana hai।
- **(B)** Timeliness means data is delivered in a timely manner. / Timeliness ka matlab data time par pahunchana hai।
- **(D)** Jitter is the variation in packet arrival time. / Jitter packet pahunchne ke samay ka antar hai।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q25. Data delivered late is useless (especially in real-time audio/video). Delivering data in a timely manner is called _______.

<span lang='hi'>Der se pahunchne wala data bekaar hai (khaas kar real-time audio/video mein)। Time par data pahunchane ko _______ kehte hain।</span>

- **(A)** Delivery / delivery
- **(B)** Accuracy / accuracy
- **(C)** Timeliness / timeliness ✅ **(CORRECT)**
- **(D)** Jitter / jitter

**✔ Correct Answer: (C) Timeliness** — Timeliness: the system must deliver data in a timely manner. Data delivered late is useless. For video/audio, timely delivery means delivering data as they are produced, in the same order, without significant delay (real-time transmission). (Forouzan)

*Timeliness: system ko data time par pahunchana chahiye। Der se pahunchne wala data bekaar hai। Video/audio ke liye timely delivery ka matlab hai data jis tarah produce hue hain usi tarah, bina kisi bade delay ke pahunchana (real-time transmission). (Forouzan)*

**★ Nukta (Key Point):** Timeliness = on-time delivery; late data is useless -> real-time transmission (audio/video).

*Timeliness = time par pahunchana; der wala data bekaar hai -> real-time transmission (audio/video).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Delivery = correct destination. / Delivery = sahi destination।
- **(B)** Accuracy = error-free data. / Accuracy = error-free data।
- **(D)** Jitter = uneven delay in arrival, a separate characteristic. / Jitter = arrival mein uneven delay, ek alag characteristic।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q26. The network criterion measured by transit time, response time, throughput and delay is called _______.

<span lang='hi'>Transit time, response time, throughput aur delay se maape jane wale network criterion ko _______ kehte hain।</span>

- **(A)** Performance / performance ✅ **(CORRECT)**
- **(B)** Reliability / reliability
- **(C)** Security / security
- **(D)** Delivery / delivery

**✔ Correct Answer: (A) Performance** — Performance of a network is measured by transit time (time for a message to travel from one device to another), response time (time between request and response), throughput and delay. (Forouzan)

*Network ki performance ko transit time (ek device se doosre tak message pahunchne ka time), response time (request aur response ke beech ka time), throughput aur delay se maapa jata hai। (Forouzan)*

**★ Nukta (Key Point):** Performance = transit time + response time (throughput & delay are related measures).

*Performance = transit time + response time (throughput aur delay isse jude measures hain).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Reliability = failure frequency and recovery time. / Reliability = failure frequency aur recovery time hai।
- **(C)** Security = protection from unauthorized access and data integrity. / Security = unauthorized access se bachav aur data integrity hai।
- **(D)** Delivery is a data-communication characteristic (correct destination), not a network criterion. / Delivery ek data-communication characteristic hai (sahi destination), network criterion nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q27. Which of the following is NOT one of the three fundamental criteria (properties) that a network must meet?

<span lang='hi'>Nimnlikhit mein se kaun network ke teen fundamental criteria (properties) mein se ek nahi hai?</span>

- **(A)** Performance / performance
- **(B)** Reliability / reliability
- **(C)** Security / security
- **(D)** Topology / topology ✅ **(CORRECT)**

**✔ Correct Answer: (D) Topology** — Forouzan: a network must meet certain criteria; the most important are performance, reliability, and security. Topology is a structure/arrangement, not one of the three criteria.

*Forouzan: ek network ko kuch criteria poore karne chahiye; sabse zaroori hain performance, reliability aur security. Topology ek structure/arrangement hai, teen criteria mein se nahi।*

**★ Nukta (Key Point):** Network criteria = 3: Performance, Reliability, Security.

*Network criteria = 3: Performance, Reliability, Security.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Performance IS a criterion (transit time, response time, throughput, delay). / Performance ek criterion hai (transit time, response time, throughput, delay).
- **(B)** Reliability IS a criterion (failure frequency, recovery time). / Reliability ek criterion hai (failure frequency, recovery time).
- **(C)** Security IS a criterion (unauthorized access, data integrity). / Security ek criterion hai (unauthorized access, data integrity).

*[Source: Extra (Forouzan) - fills syllabus gap]*

---

## Section C - Transmission Mode (Direction of Data Flow: Simplex, Half-Duplex, Full-Duplex)

*Syllabus: Transmission Mode - Simplex, Half-Duplex, Full-Duplex*

### Q28. Which of the following transmission directions listed is not a legitimate channel?

<span lang='hi'>निम्नलिखित में से kaun sa transmission direction ek legitimate (vaidh) channel nahi hai?</span>

- **(A)** Simplex / simplex
- **(B)** Half Duplex / half duplex
- **(C)** Full Duplex / full duplex
- **(D)** Double Duplex / double duplex ✅ **(CORRECT)**

**✔ Correct Answer: (D) Double Duplex** — The three legitimate directions of data flow are simplex (one way only), half-duplex (both ways, one at a time) and full-duplex (both ways simultaneously). Double duplex is not a standard term.

*Data flow ke teen legitimate directions hain: simplex (ek hi taraf), half-duplex (dono taraf, ek samay mein ek), full-duplex (dono taraf, ek saath). Double duplex koi standard term nahi hai।*

**★ Nukta (Key Point):** 3 transmission modes: Simplex, Half-Duplex, Full-Duplex. Double duplex = galat.

*3 transmission modes: Simplex, Half-Duplex, Full-Duplex. Double duplex = galat hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Simplex is a legitimate mode (one direction only). / Simplex ek legitimate mode hai (ek hi direction).
- **(B)** Half-duplex is a legitimate mode (both directions, one at a time). / Half-duplex ek legitimate mode hai (dono direction, ek samay mein ek).
- **(C)** Full-duplex is a legitimate mode (both directions simultaneously). / Full-duplex ek legitimate mode hai (dono direction, ek saath).

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q3]*

---
### Q29. Communication between a computer and a keyboard involves ______________ transmission.

<span lang='hi'>Computer aur keyboard ke beech communication mein ______________ transmission hota hai।</span>

- **(A)** Automatic / automatic
- **(B)** Half-duplex / half-duplex
- **(C)** Half-duplex (variant) / half-duplex
- **(D)** Simplex / simplex ✅ **(CORRECT)**

**✔ Correct Answer: (D) Simplex** — A keyboard only sends data to the computer; the computer does not send data back to the keyboard. So the communication is unidirectional = simplex.

*Keyboard sirf computer ko data bhejta hai; computer keyboard ko data wapas nahi bhejta. Isliye communication ek hi direction mein hai = simplex.*

**★ Nukta (Key Point):** Keyboard -> Computer = simplex (one way). Examples: keyboard-monitor, TV broadcast.

*Keyboard -> Computer = simplex (ek taraf). Examples: keyboard-monitor, TV broadcast.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Automatic is not a transmission direction/mode. / Automatic koi transmission direction/mode nahi hai।
- **(B)** Half-duplex allows both directions (one at a time); keyboard never sends data back. / Half-duplex dono direction ki anumati deta hai; keyboard wapas data nahi bhejta।
- **(C)** Half-duplex is still two-way (one at a time); keyboard is strictly one-way. / Half-duplex abhi bhi two-way hai (ek samay mein ek); keyboard poori tarah one-way hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q33]*

---
### Q30. A television broadcast is an example of _______ transmission.

<span lang='hi'>Television broadcast _______ transmission ka ek example hai।</span>

- **(A)** simplex / simplex ✅ **(CORRECT)**
- **(B)** half-duplex / half-duplex
- **(C)** full-duplex / full-duplex
- **(D)** automatic / automatic

**✔ Correct Answer: (A) simplex** — TV broadcast is unidirectional: the TV station only transmits and the TV set only receives. One direction only = simplex.

*TV broadcast ek direction ka hai: TV station sirf transmit karta hai aur TV set sirf receive karta hai। Ek hi direction = simplex.*

**★ Nukta (Key Point):** TV/radio broadcast = simplex (station -> TV only, wapas nahi).

*TV/radio broadcast = simplex (station -> TV hi, wapas nahi).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Half-duplex needs two-way capability; the TV cannot send back. / Half-duplex mein two-way capability chahiye; TV wapas nahi bhej sakta।
- **(C)** Full-duplex needs simultaneous two-way; not possible in broadcast. / Full-duplex mein ek saath two-way chahiye; broadcast mein nahi ho sakta।
- **(D)** Automatic is not a transmission mode. / Automatic koi transmission mode nahi hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q41]*

---
### Q31. What is the mode of transmission where data flows in only one direction?

<span lang='hi'>Wo transmission mode kaunsa hai jismein data sirf ek direction mein flow karta hai?</span>

- **(A)** Simplex / simplex ✅ **(CORRECT)**
- **(B)** Half-Duplex / half-duplex
- **(C)** Full-Duplex / full-duplex
- **(D)** Multiplex / multiplex

**✔ Correct Answer: (A) Simplex** — Simplex: communication is unidirectional, like a one-way street. Only one of the two devices on a link can transmit; the other can only receive. (Forouzan)

*Simplex: communication ek hi direction ka hota hai, jaise one-way street. Link ke do devices mein se sirf ek transmit kar sakta hai; doosra sirf receive karta hai। (Forouzan)*

**★ Nukta (Key Point):** Simplex = one-way only (keyboard to monitor, TV broadcast).

*Simplex = sirf ek taraf (keyboard to monitor, TV broadcast).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Half-duplex allows both directions, but only one at a time. / Half-duplex dono direction ki anumati deta hai, lekin ek samay mein ek hi।
- **(C)** Full-duplex allows both stations to transmit and receive simultaneously. / Full-duplex dono stations ko ek saath transmit aur receive karne deta hai।
- **(D)** Multiplexing is sharing a link among multiple signals, not a direction mode. / Multiplexing ek link ko kai signals mein share karna hai, direction mode nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q3]*

---
### Q32. Which transmission mode is used in walkie-talkie communication?

<span lang='hi'>Walkie-talkie communication mein kaun sa transmission mode use hota hai?</span>

- **(A)** Simplex / simplex
- **(B)** Half-Duplex / half-duplex ✅ **(CORRECT)**
- **(C)** Full-Duplex / full-duplex
- **(D)** Multiplex / multiplex

**✔ Correct Answer: (B) Half-Duplex** — A walkie-talkie is the classic example of half-duplex: both sides can talk, but only one at a time (push-to-talk). (Forouzan)

*Walkie-talkie half-duplex ka classic example hai: dono taraf baat kar sakte hain, lekin ek samay mein sirf ek (push-to-talk). (Forouzan)*

**★ Nukta (Key Point):** Walkie-talkie = half-duplex (push-to-talk, ek samay mein ek hi bolega).

*Walkie-talkie = half-duplex (push-to-talk, ek samay mein ek hi bolega).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Simplex would allow only one side to ever transmit. / Simplex mein sirf ek taraf hi kabhi transmit kar sakta hai।
- **(C)** Full-duplex would let both talk simultaneously. / Full-duplex dono ko ek saath bolne deta।
- **(D)** Multiplexing is sharing a link, not a direction mode. / Multiplexing link share karna hai, direction mode nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q10]*

---
### Q33. Data flow between two devices can occur in a _______ way.

<span lang='hi'>Do devices ke beech data flow _______ tareeke se ho sakta hai।</span>

- **(A)** simplex / simplex
- **(B)** half-duplex / half-duplex
- **(C)** full-duplex / full-duplex
- **(D)** all of the above / upar Sabhi ✅ **(CORRECT)**

**✔ Correct Answer: (D) all of the above** — Data flow between two devices can be simplex (one way), half-duplex (both ways, one at a time) or full-duplex (both ways at the same time). Hence all of the above.

*Do devices ke beech data flow simplex (ek taraf), half-duplex (dono taraf, ek samay mein ek) ya full-duplex (dono taraf, ek saath) ho sakta hai। Isliye upar sabhi sahi hain।*

**★ Nukta (Key Point):** 3 ways of data flow: simplex, half-duplex, full-duplex.

*Data flow ke 3 tareeke: simplex, half-duplex, full-duplex.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Simplex is only one of the possible ways, not the only way. / Simplex sirf ek possible way hai, eklauta nahi।
- **(B)** Half-duplex is only one of the possible ways, not the only way. / Half-duplex sirf ek possible way hai, eklauta nahi।
- **(C)** Full-duplex is only one of the possible ways, not the only way. / Full-duplex sirf ek possible way hai, eklauta nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q45]*

---
### Q34. In a telephone conversation, both persons can speak and hear each other at the same time. This is an example of _______.

<span lang='hi'>Telephone conversation mein dono persons ek saath bol aur sun sakte hain। Ye _______ ka example hai।</span>

- **(A)** Simplex / simplex
- **(B)** Half-duplex / half-duplex
- **(C)** Full-duplex / full-duplex ✅ **(CORRECT)**
- **(D)** Unicast / unicast

**✔ Correct Answer: (C) Full-duplex** — Full-duplex: both stations can transmit and receive simultaneously. The telephone network is Forouzan's example of full-duplex.

*Full-duplex: dono stations ek saath transmit aur receive kar sakte hain। Telephone network full-duplex ka Forouzan ka example hai।*

**★ Nukta (Key Point):** Telephone = full-duplex (dono ek saath bol aur sun sakte hain).

*Telephone = full-duplex (dono ek saath bol aur sun sakte hain).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Simplex = one-way only; telephone is two-way. / Simplex = sirf ek taraf; telephone two-way hai।
- **(B)** Half-duplex = one at a time; telephone allows both at once. / Half-duplex = ek samay mein ek; telephone ek saath dono ki anumati deta hai।
- **(D)** Unicast = one-to-one addressing, not a direction-of-transmission mode. / Unicast = one-to-one addressing hai, direction-of-transmission mode nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---

## Section D - Network Structure / Topology (Physical: Mesh, Star, Bus, Ring, Others; Logical: IEEE 802)

*Syllabus: Physical Topology - Mesh, Star, Bus, Ring, Others (Hybrid, Tree) | Logical Topology - IEEE 802*

### Q35. What are the advantages of star topology?

<span lang='hi'>Star topology ke kya advantages (लाभ) hain?</span>

- **(A)** Less number of cables are required / kam number mein cables chahiye ✅ **(CORRECT)**
- **(B)** More number of cables are required / zyada number mein cables chahiye
- **(C)** It is a distributed topology / ye ek distributed topology hai
- **(D)** Security is high / security zyada hai

**✔ Correct Answer: (A) Less number of cables are required** — In a star topology, each device has a dedicated point-to-point link only to a central hub, so far fewer cables are required than in a mesh. It is also easy to install and reconfigure.

*Star topology mein har device ka sirf central hub se dedicated point-to-point link hota hai, isliye mesh ki tulna mein kaafi kam cables chahiye. Ise install aur reconfigure karna bhi aasaan hai।*

**★ Nukta (Key Point):** Star = hub at centre, dedicated links, fewer cables (vs mesh), easy to install. But if hub fails, whole network goes down.

*Star = centre mein hub, dedicated links, kam cables (mesh ke muqable), install karna aasaan. Lekin hub fail ho gaya toh poora network band ho jata hai।*

**✖ Why the other options are WRONG (verified):**
- **(B)** More cables is a disadvantage of mesh, not star. / Zyada cables mesh ka disadvantage hai, star ka nahi।
- **(C)** Star is not a distributed topology; it is centralised around the hub. / Star distributed topology nahi hai; ye hub ke around centralised hai।
- **(D)** Star does not inherently provide high security; security depends on configuration. / Star khud se high security nahi deta; security configuration par nirbhar hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q1]*

---
### Q36. Which type of topology is best suited for large businesses which must carefully control and coordinate the operation of distributed branch outlets?

<span lang='hi'>Large businesses ke liye kaun si topology sabse upayukt hai, jahan distributed branch outlets ke operation ko carefully control aur coordinate karna ho?</span>

- **(A)** Ring / ring
- **(B)** Local area / local area
- **(C)** Hierarchical / hierarchical (tree) ✅ **(CORRECT)**
- **(D)** Star / star

**✔ Correct Answer: (C) Hierarchical** — A hierarchical (tree) topology is best for large organisations with distributed branch outlets because it is a hierarchy of stars and allows central control and coordination at each level.

*Hierarchical (tree) topology large organisations ke liye sabse upayukt hai jahan distributed branch outlets hon, kyunki ye stars ki hierarchy hai aur har level par central control/coordination ki anumati deti hai।*

**★ Nukta (Key Point):** Tree = hierarchical star. Large orgs with branches -> hierarchical/tree topology.

*Tree = hierarchical star. Badi sansthaon mein branches ke liye -> hierarchical/tree topology.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Ring connects neighbours in a loop; it does not give hierarchical control of branches. / Ring neighbours ko loop mein jodta hai; branches ka hierarchical control nahi deta।
- **(B)** Local area is a network type (LAN), not a topology. / Local area ek network type (LAN) hai, topology nahi।
- **(D)** A plain star has a single central hub; it cannot manage many distributed branches hierarchically. / Plain star mein ek hi central hub hota hai; kai distributed branches ko hierarchically manage nahi kar sakta।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q2]*

---
### Q37. Which one of the following is not a network topology?

<span lang='hi'>निम्नलिखित में से kaun ek network topology nahi hai?</span>

- **(A)** Star / star
- **(B)** Ring / ring
- **(C)** Bus / bus
- **(D)** Peer to Peer / peer to peer ✅ **(CORRECT)**

**✔ Correct Answer: (D) Peer to Peer** — Star, ring and bus are physical topologies. Peer-to-peer is a network architecture (how devices share resources), not a topology.

*Star, ring aur bus physical topologies hain। Peer-to-peer ek network architecture hai (devices kaise resources share karenge), topology nahi।*

**★ Nukta (Key Point):** Topologies = mesh, star, bus, ring, hybrid, tree. P2P = architecture (not topology).

*Topologies = mesh, star, bus, ring, hybrid, tree. P2P = architecture hai (topology nahi).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Star is a topology (central hub). / Star ek topology hai (central hub).
- **(B)** Ring is a topology (closed loop). / Ring ek topology hai (closed loop).
- **(C)** Bus is a topology (shared backbone). / Bus ek topology hai (shared backbone).

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q9]*

---
### Q38. The repeater is used in _______ topology.

<span lang='hi'>Repeater ka use _______ topology mein hota hai।</span>

- **(A)** Mesh Topology / mesh topology
- **(B)** Ring Topology / ring topology
- **(C)** Bus Topology / bus topology ✅ **(CORRECT)**
- **(D)** Star Topology / star topology

**✔ Correct Answer: (C) Bus Topology** — In a bus topology, one long backbone cable carries the signal over the whole length; a repeater is used to regenerate/amplify the signal so it can travel the long distance without degradation.

*Bus topology mein ek lamba backbone cable poori length par signal le jaata hai; repeater ka use signal ko regenerate/amplify karne ke liye hota hai taaki woh lambi doori bina kharab hue ja sake।*

**★ Nukta (Key Point):** Bus = long backbone -> signal weak ho jata hai -> repeater use hota hai. (Ring mein bhi har device repeater ki tarah kaam karta hai.)

*Bus = lamba backbone -> signal kamzor ho jata hai -> repeater use hota hai। (Ring mein bhi har device repeater ki tarah kaam karta hai.)*

**✖ Why the other options are WRONG (verified):**
- **(A)** Mesh uses dedicated links between every pair; it does not need repeaters on a shared backbone. / Mesh mein har pair ke beech dedicated links hote hain; shared backbone par repeater ki zaroorat nahi।
- **(B)** In a ring each device itself acts as a repeater, but the classic exam answer for a separate repeater on a long cable is bus topology. / Ring mein har device khud repeater ki tarah kaam karta hai, lekin lambi cable par alag repeater ka classic exam answer bus topology hai।
- **(D)** Star uses dedicated links to a hub; no shared backbone needs a repeater. / Star mein hub tak dedicated links hote hain; shared backbone ko repeater ki zaroorat nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q50]*

---
### Q39. What type of topology connects each node in a closed loop?

<span lang='hi'>Kaun si topology har node ko ek closed loop mein jodti hai?</span>

- **(A)** Star / star
- **(B)** Mesh / mesh
- **(C)** Ring / ring ✅ **(CORRECT)**
- **(D)** Bus / bus

**✔ Correct Answer: (C) Ring** — In a ring topology, each device is connected to its two neighbours (one on each side), forming a closed loop. Data travels in one direction and each device regenerates the signal (token passing).

*Ring topology mein har device apne dono neighbours se juda hota hai (ek dono taraf), jisse ek closed loop banta hai। Data ek hi direction mein jaata hai aur har device signal ko regenerate karta hai (token passing).*

**★ Nukta (Key Point):** Ring = closed loop, one direction, token passing, each device = repeater.

*Ring = closed loop, ek direction, token passing, har device = repeater.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Star connects each device to a central hub, not in a loop. / Star har device ko central hub se jodta hai, loop mein nahi।
- **(B)** Mesh connects every device to every other device (full interconnection), not a single loop. / Mesh har device ko har device se jodta hai (full interconnection), ek loop mein nahi।
- **(D)** Bus connects all devices to one shared backbone, not a loop. / Bus sabhi devices ko ek shared backbone se jodta hai, loop mein nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q4]*

---
### Q40. In a _______ topology, every device has a dedicated point-to-point link to every other device. For n devices, the number of links is n(n-1)/2 and each device needs n-1 I/O ports.

<span lang='hi'>_______ topology mein har device ka har doosre device se dedicated point-to-point link hota hai। n devices ke liye links ki sankhya n(n-1)/2 hoti hai aur har device ko n-1 I/O ports chahiye।</span>

- **(A)** Bus / bus
- **(B)** Star / star
- **(C)** Ring / ring
- **(D)** Mesh / mesh ✅ **(CORRECT)**

**✔ Correct Answer: (D) Mesh** — Mesh: every device has a dedicated point-to-point link to every other device. Number of links = n(n-1)/2; each device needs n-1 I/O ports. (Forouzan)

*Mesh: har device ka har doosre device se dedicated point-to-point link hota hai। Links ki sankhya = n(n-1)/2; har device ko n-1 I/O ports chahiye। (Forouzan)*

**★ Nukta (Key Point):** Mesh formula (EXAM favourite): links = n(n-1)/2, ports per device = n-1. E.g., 5 devices -> 10 links.

*Mesh formula (EXAM favourite): links = n(n-1)/2, har device ke ports = n-1. Jaise 5 devices -> 10 links.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Bus = one shared backbone cable; no dedicated links. / Bus = ek shared backbone cable; dedicated links nahi।
- **(B)** Star = each device links only to a central hub. / Star = har device sirf central hub se link hota hai।
- **(C)** Ring = each device links only to its two neighbours. / Ring = har device sirf apne do neighbours se link hota hai।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q41. In a _______ topology, each device has a dedicated point-to-point link only to a central controller, usually called a hub (or switch).

<span lang='hi'>_______ topology mein har device ka sirf ek central controller (hub/switch) se dedicated point-to-point link hota hai।</span>

- **(A)** Mesh / mesh
- **(B)** Ring / ring
- **(C)** Star / star ✅ **(CORRECT)**
- **(D)** Bus / bus

**✔ Correct Answer: (C) Star** — Star: each device has a dedicated point-to-point link only to a central controller, usually called a hub. The hub relays frames to the destination. (Forouzan)

*Star: har device ka sirf ek central controller (usually hub) se dedicated point-to-point link hota hai। Hub frames ko destination tak relay karta hai। (Forouzan)*

**★ Nukta (Key Point):** Star = hub/switch at centre; easy to install & reconfigure; but if hub fails, the WHOLE network goes down.

*Star = centre mein hub/switch; install aur reconfigure karna aasaan; lekin hub fail ho gaya toh POORA network band ho jata hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Mesh = links between every pair of devices, no central hub. / Mesh = har pair of devices ke beech links, central hub nahi।
- **(B)** Ring = links only between neighbours, no hub. / Ring = sirf neighbours ke beech links, hub nahi।
- **(D)** Bus = shared backbone, no dedicated links and no hub. / Bus = shared backbone, dedicated links nahi aur hub bhi nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q42. In a _______ topology, one long cable acts as a backbone to link all the devices; devices connect via drop lines and taps, and terminators are needed at both ends of the backbone.

<span lang='hi'>_______ topology mein ek lamba cable backbone ki tarah sabhi devices ko jodta hai; devices drop lines aur taps se connect hote hain, aur backbone ke dono ends par terminators chahiye।</span>

- **(A)** Bus / bus ✅ **(CORRECT)**
- **(B)** Star / star
- **(C)** Ring / ring
- **(D)** Mesh / mesh

**✔ Correct Answer: (A) Bus** — Bus: one long cable acts as a backbone to link all the devices. Nodes are connected to the bus cable by drop lines and taps. Terminators at both ends absorb the signal to prevent reflection. (Forouzan)

*Bus: ek lamba cable backbone ki tarah sabhi devices ko jodta hai। Nodes ko bus cable se drop lines aur taps ke through joda jata hai। Dono ends par terminators signal ko absorb karte hain taaki reflection na ho। (Forouzan)*

**★ Nukta (Key Point):** Bus = one backbone + drop lines + taps + terminators at both ends. Fault isolation is difficult; a backbone break stops everything.

*Bus = ek backbone + drop lines + taps + dono ends par terminators. Fault isolation mushkil hai; backbone tootne se sab kuch band ho jata hai।*

**✖ Why the other options are WRONG (verified):**
- **(B)** Star = dedicated links to a central hub. / Star = central hub tak dedicated links.
- **(C)** Ring = neighbours connected in a loop. / Ring = neighbours loop mein jude hote hain।
- **(D)** Mesh = every device connected to every other device. / Mesh = har device har device se juda hota hai।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q43. In a _______ topology, each device is connected to its two neighbours, data travels in one direction around the loop, and each device regenerates (repeats) the signal - this is called token passing.

<span lang='hi'>_______ topology mein har device apne do neighbours se juda hota hai, data loop mein ek hi direction mein jaata hai, aur har device signal ko regenerate (repeat) karta hai - ise token passing kehte hain।</span>

- **(A)** Bus / bus
- **(B)** Ring / ring ✅ **(CORRECT)**
- **(C)** Star / star
- **(D)** Mesh / mesh

**✔ Correct Answer: (B) Ring** — Ring: each device is connected to its two neighbours. Data travels in one direction. Each device in the ring incorporates a repeater; it regenerates the bits and passes them along. Access is typically by token passing. (Forouzan)

*Ring: har device apne do neighbours se juda hota hai। Data ek hi direction mein jaata hai। Ring ka har device ek repeater ki tarah kaam karta hai; ye bits ko regenerate karke aage pass karta hai। Access aam taur par token passing se hota hai। (Forouzan)*

**★ Nukta (Key Point):** Ring = loop, one direction, token passing, each device = repeater.

*Ring = loop, ek direction, token passing, har device = repeater.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Bus = shared backbone cable. / Bus = shared backbone cable hai।
- **(C)** Star = central hub. / Star = central hub hai।
- **(D)** Mesh = full interconnection of all devices. / Mesh = sabhi devices ki full interconnection hai।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q44. A network in which two or more different topologies are combined (e.g., a star connected to another star) is called a _______ topology, while a _______ topology is a hierarchy of stars (a variation of the star topology).

<span lang='hi'>Jismein do ya zyada alag topologies combine ho (jaise ek star doosre star se juda ho), use _______ topology kehte hain, aur _______ topology stars ki hierarchy hai (star topology ka variation).</span>

- **(A)** Hybrid ; Tree / hybrid ; tree ✅ **(CORRECT)**
- **(B)** Tree ; Hybrid / tree ; hybrid
- **(C)** Mesh ; Ring / mesh ; ring
- **(D)** Bus ; Star / bus ; star

**✔ Correct Answer: (A) Hybrid ; Tree** — Hybrid = a combination of two or more different topologies (e.g., a star of stars). Tree = a hierarchical arrangement of stars, a variation of the star topology.

*Hybrid = do ya zyada alag topologies ka combination hai (jaise star of stars). Tree = stars ki hierarchical arrangement hai, star topology ka ek variation.*

**★ Nukta (Key Point):** Hybrid = mix of topologies; Tree = star of stars (hierarchical star).

*Hybrid = topologies ka mix; Tree = star of stars (hierarchical star).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Reverses the two definitions. / Dono definitions ko ulta kar diya hai।
- **(C)** Mesh and Ring are basic physical topologies, not combinations/hierarchies. / Mesh aur Ring basic physical topologies hain, combinations/hierarchies nahi।
- **(D)** Bus and Star are basic topologies, not combination/hierarchy. / Bus aur Star basic topologies hain, combination/hierarchy nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q45. The ______ topology of a network defines how the devices are physically laid out/connected, whereas the ______ topology defines how the data actually flow / how the devices access the network to transmit.

<span lang='hi'>Network ki _______ topology batati hai ki devices physically kaise jude hain, jabki _______ topology batati hai ki data asal mein kaise flow karta hai / devices transmit karne ke liye network ko kaise access karte hain।</span>

- **(A)** Logical ; Physical / logical ; physical
- **(B)** Physical ; Logical / physical ; logical ✅ **(CORRECT)**
- **(C)** Star ; Bus / star ; bus
- **(D)** Mesh ; Ring / mesh ; ring

**✔ Correct Answer: (B) Physical ; Logical** — Physical topology = the actual layout of devices and cables. Logical topology = the way data flows / how devices access the medium. Two networks can have the same logical topology but different physical topologies.

*Physical topology = devices aur cables ka asli layout. Logical topology = data kaise flow karta hai / devices medium ko kaise access karte hain। Do networks ki logical topology same ho sakti hai lekin physical alag ho sakti hai।*

**★ Nukta (Key Point):** Physical = kaise jude (cables); Logical = data kaise flow karta hai (access). Same logical, different physical possible.

*Physical = kaise jude (cables); Logical = data kaise flow karta hai (access). Same logical, different physical ho sakta hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Reverses the two definitions. / Dono definitions ko ulta kar diya hai।
- **(C)** Star and Bus are specific topology types, not the physical/logical distinction. / Star aur Bus specific topology types hain, physical/logical antar nahi।
- **(D)** Mesh and Ring are specific topology types. / Mesh aur Ring specific topology types hain।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q46. The IEEE 802 standards (such as 802.3 for Ethernet, 802.5 for Token Ring, 802.11 for Wi-Fi) primarily define the ______ of LANs/MANs.

<span lang='hi'>IEEE 802 standards (jaise 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi) primarily LANs/MANs ki _______ define karte hain।</span>

- **(A)** Physical and Data Link layers (including the logical topology / MAC) / Physical aur Data Link layers (logical topology / MAC sahit) ✅ **(CORRECT)**
- **(B)** Only the Application layer / sirf Application layer
- **(C)** Only IP addressing / sirf IP addressing
- **(D)** Only WAN routing / sirf WAN routing

**✔ Correct Answer: (A) Physical and Data Link layers (including the logical topology / MAC)** — IEEE 802 is the family of standards for LANs and MANs; it covers the Physical layer and the Data Link layer (split into LLC - 802.2 - and MAC sublayers). 802.3 = Ethernet, 802.5 = Token Ring, 802.11 = Wireless LAN. The logical topology (bus/ring) is a Data-Link/MAC concern.

*IEEE 802 LANs aur MANs ke liye standards ka family hai; ye Physical layer aur Data Link layer ko cover karta hai (LLC - 802.2 - aur MAC sublayers mein banta hai). 802.3 = Ethernet, 802.5 = Token Ring, 802.11 = Wireless LAN. Logical topology (bus/ring) ek Data-Link/MAC concern hai।*

**★ Nukta (Key Point):** IEEE 802 = LAN/MAN standards (Physical + Data Link). 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi.

*IEEE 802 = LAN/MAN standards (Physical + Data Link). 802.3 Ethernet, 802.5 Token Ring, 802.11 Wi-Fi.*

**✖ Why the other options are WRONG (verified):**
- **(B)** The Application layer is covered by TCP/IP protocols (HTTP, FTP...), not IEEE 802. / Application layer TCP/IP protocols (HTTP, FTP...) cover karte hain, IEEE 802 nahi।
- **(C)** IP addressing is a Network-layer function (IEEE 802 deals with MAC/physical addressing). / IP addressing ek Network-layer function hai (IEEE 802 MAC/physical addressing se sambandhit hai).
- **(D)** WAN routing (OSPF, BGP) is a Network-layer function, not IEEE 802. / WAN routing (OSPF, BGP) ek Network-layer function hai, IEEE 802 nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q47. Which physical topology offers the highest robustness (fault tolerance) because of multiple redundant paths, but is also the most expensive and hardest to install because of the huge amount of cabling?

<span lang='hi'>Kaun si physical topology sabse zyada robust (fault tolerant) hai kyunki ismein kai redundant paths hote hain, lekin sabse mehengi aur install karne mein sabse mushkil bhi hai kyunki bahut zyada cabling chahiye?</span>

- **(A)** Bus / bus
- **(B)** Ring / ring
- **(C)** Star / star
- **(D)** Mesh / mesh ✅ **(CORRECT)**

**✔ Correct Answer: (D) Mesh** — Mesh has a dedicated link between every pair of devices, so the failure of one link does not affect the others - it is the most robust. But n(n-1)/2 links make it the most expensive and hardest to install/wire.

*Mesh mein har pair of devices ke beech dedicated link hota hai, isliye ek link fail hone se doosre affected nahi hote - ye sabse robust hai। Lekin n(n-1)/2 links ki wajah se ye sabse mehengi aur install karne mein sabse mushkil hai।*

**★ Nukta (Key Point):** Mesh = most robust + most costly (n(n-1)/2 cables). Star = cheap & easy but hub is a single point of failure. Bus = cheapest, hardest fault isolation.

*Mesh = sabse robust + sabse mehengi (n(n-1)/2 cables). Star = sasti aur aasaan lekin hub single point of failure hai. Bus = sabse sasti, fault isolation sabse mushkil.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Bus is cheap, but a backbone break stops everything - least robust. / Bus sasti hai, lekin backbone tootne se sab kuch band ho jata hai - sabse kam robust.
- **(B)** Ring: failure of one link/device can bring down the loop - not the most robust. / Ring: ek link/device fail hone se poora loop band ho sakta hai - sabse robust nahi.
- **(C)** Star depends on the central hub - a single point of failure, not the most robust. / Star central hub par nirbhar hai - single point of failure, sabse robust nahi.

*[Source: Extra (Forouzan) - fills syllabus gap]*

---

## Section E - Types of Networks (LAN, MAN, WAN, PAN, CAN, SAN; Internet, Intranet, Extranet; Point-to-Point, Multipoint; Client-Server, P2P)

*Syllabus: Types of Networks - Geographical (LAN, MAN, WAN, PAN, CAN, SAN) | Accessibility (Internet, Intranet, Extranet) | Architecture (Point-to-Point, Multipoint)*

### Q48. The term WAN stands for?

<span lang='hi'>WAN ka poora naam (full form) kya hai?</span>

- **(A)** Wide Area Net / Wide Area Net
- **(B)** Wide Access Network / Wide Access Network
- **(C)** Wide Area Network / Wide Area Network ✅ **(CORRECT)**
- **(D)** Wide Access Net / Wide Access Net

**✔ Correct Answer: (C) Wide Area Network** — WAN = Wide Area Network. It spans a large geographical area - a country, continent or the whole world. The Internet is the largest WAN.

*WAN = Wide Area Network. Ye ek bade geographical area ko span karta hai - ek desh, continent ya poori duniya। Internet sabse bada WAN hai।*

**★ Nukta (Key Point):** WAN = Wide Area Network. Internet sabse bada WAN hai.

*WAN = Wide Area Network. Internet sabse bada WAN hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Wide Area Net is incomplete (missing the full word Network). / Wide Area Net adhura hai (poora shabd nahi hai).
- **(B)** Wide Access Network is incorrect. / Wide Access Network galat hai।
- **(D)** Wide Access Net is incorrect and incomplete. / Wide Access Net galat aur adhura hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q11 / BCI_SCI Subject Test-01, Q11]*

---
### Q49. Which network is suitable for a building?

<span lang='hi'>Kisi ek building ke liye kaun sa network upayukt (suitable) hai?</span>

- **(A)** WAN / WAN
- **(B)** LAN / LAN ✅ **(CORRECT)**
- **(C)** MAN / MAN
- **(D)** PAN / PAN

**✔ Correct Answer: (B) LAN** — A LAN (Local Area Network) is usually privately owned and covers a small geographical area - a single office, building, or campus. So a building -> LAN.

*LAN (Local Area Network) aam taur par privately owned hota hai aur ek chhote geographical area - ek office, building, ya campus - ko cover karta hai। Isliye building ke liye LAN upayukt hai।*

**★ Nukta (Key Point):** LAN = Local Area Network - chhota area (office/building/campus), private, high speed.

*LAN = Local Area Network - chhota area (office/building/campus), private, high speed.*

**✖ Why the other options are WRONG (verified):**
- **(A)** WAN covers countries/continents, not a single building. / WAN desh/continents cover karta hai, ek building nahi।
- **(C)** MAN covers a whole city, not a single building. / MAN poore city cover karta hai, ek building nahi।
- **(D)** PAN covers the area around one person, not a building. / PAN ek vyakti ke aas-paas ka area cover karta hai, building nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q27]*

---
### Q50. Bluetooth is an example of:

<span lang='hi'>Bluetooth iska example hai:</span>

- **(A)** personal area network / personal area network (PAN) ✅ **(CORRECT)**
- **(B)** local area network / local area network (LAN)
- **(C)** virtual private network / virtual private network (VPN)
- **(D)** none of the mentioned / inmein se koi nahi

**✔ Correct Answer: (A) personal area network** — Bluetooth connects devices around one person (mobile phone with earphones/headset). A network organized around an individual person is a PAN (Personal Area Network).

*Bluetooth ek vyakti ke aas-paas ke devices ko jodta hai (mobile phone ko earphones/headset se). Ek vyakti ke around organized network ko PAN (Personal Area Network) kehte hain।*

**★ Nukta (Key Point):** PAN = Personal Area Network - ek person ke around (Bluetooth: phone <-> earphones).

*PAN = Personal Area Network - ek person ke around (Bluetooth: phone <-> earphones).*

**✖ Why the other options are WRONG (verified):**
- **(B)** LAN covers a building/campus, not a person's devices. / LAN ek building/campus cover karta hai, ek person ke devices nahi।
- **(C)** VPN extends a private network over a public network; it is not what Bluetooth is. / VPN ek private network ko public network par extend karta hai; Bluetooth ye nahi hai।
- **(D)** Bluetooth is indeed an example of PAN, so none-of-these is wrong. / Bluetooth waqayi PAN ka example hai, isliye koi-nahi galat hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q31]*

---
### Q51. Which one of the following extends a private network across public networks?

<span lang='hi'>Nimnlikhit mein se kaun ek private network ko public networks ke paar (across) extend karta hai?</span>

- **(A)** local area network / local area network (LAN)
- **(B)** virtual private network / virtual private network (VPN) ✅ **(CORRECT)**
- **(C)** enterprise private network / enterprise private network
- **(D)** storage area network / storage area network (SAN)

**✔ Correct Answer: (B) virtual private network** — A Virtual Private Network (VPN) extends a private network across a public network (e.g., the Internet) using tunneling and encryption, so data travels securely as if on a private network.

*Virtual Private Network (VPN) ek private network ko ek public network (jaise Internet) ke paar extend karta hai, tunneling aur encryption ke through, taaki data private network ki tarah securely travel kare।*

**★ Nukta (Key Point):** VPN = Virtual Private Network - private network ko public (Internet) par extend karta hai, securely.

*VPN = Virtual Private Network - private network ko public (Internet) par extend karta hai, securely.*

**✖ Why the other options are WRONG (verified):**
- **(A)** LAN is a small private network itself; it does not extend across public networks. / LAN khud ek chhota private network hai; ye public networks par extend nahi hota।
- **(C)** Enterprise private network is a private network, but it does not extend across public networks. / Enterprise private network ek private network hai, lekin public networks par extend nahi hota।
- **(D)** SAN connects storage devices/servers; it does not extend a private network across public networks. / SAN storage devices/servers ko jodta hai; ye private network ko public networks par extend nahi karta।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q32]*

---
### Q52. ______ is a network that covers geographic areas that are larger, such as districts or cities.

<span lang='hi'>______ ek aisa network hai jo bade geographical areas, jaise districts ya cities, ko cover karta hai।</span>

- **(A)** LAN / LAN
- **(B)** MAN / MAN ✅ **(CORRECT)**
- **(C)** WAN / WAN
- **(D)** None of these / inmein se koi nahi

**✔ Correct Answer: (B) MAN** — MAN (Metropolitan Area Network) covers a metropolitan area, usually a city - larger than a LAN but smaller than a WAN. Example: cable TV network of a city.

*MAN (Metropolitan Area Network) ek metropolitan area, aam taur par ek city, ko cover karta hai - LAN se bada lekin WAN se chhota। Example: ek city ka cable TV network.*

**★ Nukta (Key Point):** MAN = Metropolitan Area Network - city level (cable TV network).

*MAN = Metropolitan Area Network - city level (cable TV network).*

**✖ Why the other options are WRONG (verified):**
- **(A)** LAN covers a building/campus, not a city. / LAN ek building/campus cover karta hai, city nahi।
- **(C)** WAN covers a country/continent, larger than a city. / WAN ek desh/continent cover karta hai, city se bada।
- **(D)** MAN is indeed the correct answer, so none-of-these is wrong. / MAN hi sahi answer hai, isliye koi-nahi galat hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q49]*

---
### Q53. In terms of the size of the network, the correct order (ascending) is:

<span lang='hi'>Network ke size ke hisaab se sahi kram (badhta hua/ascending order) kya hai?</span>

- **(A)** PAN, MAN, LAN, WAN / PAN, MAN, LAN, WAN
- **(B)** LAN, MAN, WAN, PAN / LAN, MAN, WAN, PAN
- **(C)** PAN, LAN, MAN, WAN / PAN, LAN, MAN, WAN ✅ **(CORRECT)**
- **(D)** LAN, PAN, MAN, WAN / LAN, PAN, MAN, WAN

**✔ Correct Answer: (C) PAN, LAN, MAN, WAN** — Ascending order of size: PAN (around a person, smallest) < LAN (building/campus) < MAN (city) < WAN (country/world, largest).

*Size ke hisaab se badhta kram: PAN (ek person ke around, sabse chhota) < LAN (building/campus) < MAN (city) < WAN (desh/duniya, sabse bada).*

**★ Nukta (Key Point):** Yaad rakho: PAN < LAN < MAN < WAN (chhota se bada).

*Yaad rakho: PAN < LAN < MAN < WAN (chhota se bada).*

**✖ Why the other options are WRONG (verified):**
- **(A)** PAN, MAN, LAN, WAN: MAN aur LAN ka order galat hai (LAN < MAN). / PAN, MAN, LAN, WAN: MAN aur LAN ka order galat hai (LAN < MAN).
- **(B)** LAN, MAN, WAN, PAN: PAN sabse chhota hai, sabse bada nahi. / LAN, MAN, WAN, PAN: PAN sabse chhota hai, sabse bada nahi।
- **(D)** LAN, PAN, MAN, WAN: PAN aur LAN ka order galat hai (PAN < LAN). / LAN, PAN, MAN, WAN: PAN aur LAN ka order galat hai (PAN < LAN).

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2), Q42]*

---
### Q54. Which type of network covers an entire city or campus?

<span lang='hi'>Kaun sa network poore ek city ya campus ko cover karta hai?</span>

- **(A)** LAN / LAN
- **(B)** MAN / MAN ✅ **(CORRECT)**
- **(C)** WAN / WAN
- **(D)** PAN / PAN

**✔ Correct Answer: (B) MAN** — MAN (Metropolitan Area Network) covers an entire city; a large campus can also be of MAN scale. (Official answer key: MAN)

*MAN (Metropolitan Area Network) ek poore city ko cover karta hai; ek bada campus bhi MAN scale ka ho sakta hai। (Official answer key: MAN)*

**★ Nukta (Key Point):** MAN = city level. Note: a single building/campus LAN is usually LAN/CAN; an entire city = MAN.

*MAN = city level. Note: ek building/campus ka LAN aam taur par LAN/CAN hota hai; poori city = MAN.*

**✖ Why the other options are WRONG (verified):**
- **(A)** LAN covers a building/campus, not an entire city. / LAN ek building/campus cover karta hai, poori city nahi।
- **(C)** WAN covers a country/continent, much larger than a city. / WAN ek desh/continent cover karta hai, city se bahut bada।
- **(D)** PAN covers the area around one person. / PAN ek vyakti ke aas-paas ka area cover karta hai।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q2]*

---
### Q55. Which of these is NOT a type of network?

<span lang='hi'>Inmein se kaun network ka ek prakar (type) nahi hai?</span>

- **(A)** LAN / LAN
- **(B)** MAN / MAN
- **(C)** WAN / WAN
- **(D)** TAN / TAN ✅ **(CORRECT)**

**✔ Correct Answer: (D) TAN** — LAN, MAN and WAN are standard network types (by geographical area). TAN is not a standard type of network.

*LAN, MAN aur WAN standard network types hain (geographical area ke aadhar par). TAN koi standard network type nahi hai।*

**★ Nukta (Key Point):** Network types: PAN, LAN, MAN, WAN (+ CAN, SAN). TAN = nahi hai.

*Network types: PAN, LAN, MAN, WAN (+ CAN, SAN). TAN = nahi hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** LAN is a standard network type. / LAN ek standard network type hai।
- **(B)** MAN is a standard network type. / MAN ek standard network type hai।
- **(C)** WAN is a standard network type. / WAN ek standard network type hai।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q7]*

---
### Q56. The Internet is an example of:

<span lang='hi'>Internet iska example hai:</span>

- **(A)** LAN / LAN
- **(B)** MAN / MAN
- **(C)** WAN / WAN ✅ **(CORRECT)**
- **(D)** PAN / PAN

**✔ Correct Answer: (C) WAN** — The Internet is a global system of interconnected networks - it is the largest WAN (Wide Area Network).

*Internet interconnected networks ka ek global system hai - ye sabse bada WAN (Wide Area Network) hai।*

**★ Nukta (Key Point):** Internet = sabse bada WAN (network of networks).

*Internet = sabse bada WAN (network of networks).*

**✖ Why the other options are WRONG (verified):**
- **(A)** LAN is a small private network, not the global Internet. / LAN ek chhota private network hai, global Internet nahi।
- **(B)** MAN covers only a city, not the globe. / MAN sirf ek city cover karta hai, globe nahi।
- **(D)** PAN is around one person, not the Internet. / PAN ek vyakti ke around hai, Internet nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q12]*

---
### Q57. SAN is mainly used for:

<span lang='hi'>SAN ka mukhya upyog kiske liye hota hai?</span>

- **(A)** File Sharing / file sharing
- **(B)** Storage Management / storage management ✅ **(CORRECT)**
- **(C)** Internet Access / internet access
- **(D)** Printing Documents / documents print karna

**✔ Correct Answer: (B) Storage Management** — SAN (Storage Area Network) is a dedicated high-speed private network used for storage management - connecting servers to storage devices in data centres.

*SAN (Storage Area Network) ek dedicated high-speed private network hai jo storage management ke liye use hota hai - servers ko storage devices se jodne ke liye (data centres mein).*

**★ Nukta (Key Point):** SAN = Storage Area Network - servers <-> storage devices, data centre.

*SAN = Storage Area Network - servers <-> storage devices, data centre.*

**✖ Why the other options are WRONG (verified):**
- **(A)** File sharing is a function of file servers/LAN, not the main purpose of SAN. / File sharing file servers/LAN ka kaam hai, SAN ka mukhya purpose nahi।
- **(C)** Internet access is provided by ISPs, not by a SAN. / Internet access ISPs provide karte hain, SAN nahi।
- **(D)** Printing documents is a LAN/office function, not SAN. / Documents print karna LAN/office function hai, SAN nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q13]*

---
### Q58. PAN is used for connecting:

<span lang='hi'>PAN kiske connect karne ke liye use hota hai?</span>

- **(A)** Personal devices like mobile, laptop, Bluetooth headset / personal devices jaise mobile, laptop, Bluetooth headset ✅ **(CORRECT)**
- **(B)** Computers in a company / ek company ke computers
- **(C)** Computers in a city / ek city ke computers
- **(D)** Global offices / global offices

**✔ Correct Answer: (A) Personal devices like mobile, laptop, Bluetooth headset** — PAN (Personal Area Network) is a network organized around an individual person - connecting personal devices like mobile, laptop, Bluetooth headset.

*PAN (Personal Area Network) ek vyakti ke around organized ek network hai - personal devices jaise mobile, laptop, Bluetooth headset ko jodne ke liye।*

**★ Nukta (Key Point):** PAN = Personal Area Network - ek person ke devices (mobile, laptop, headset).

*PAN = Personal Area Network - ek person ke devices (mobile, laptop, headset).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Computers in a company = LAN (office network). / Company ke computers = LAN (office network).
- **(C)** Computers in a city = MAN. / City ke computers = MAN.
- **(D)** Global offices = WAN. / Global offices = WAN.

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q14]*

---
### Q59. A school has four computer labs in the same building. Each lab has 20 computers connected to a central server. Students can share files and print from any lab. Which type of network is implemented in this school?

<span lang='hi'>Ek school mein ek hi building mein chaar computer labs hain. Har lab mein 20 computers ek central server se jude hain। Students kisi bhi lab se files share aur print kar sakte hain। School mein kaun sa network implemented hai?</span>

- **(A)** WAN / WAN
- **(B)** MAN / MAN
- **(C)** LAN / LAN ✅ **(CORRECT)**
- **(D)** CAN / CAN

**✔ Correct Answer: (C) LAN** — All four labs are in the same building and share a central server - this is a small, privately-owned, single-site network = LAN (Local Area Network).

*Chaaron labs ek hi building mein hain aur ek central server share karte hain - ye ek chhota, privately-owned, single-site network hai = LAN (Local Area Network).*

**★ Nukta (Key Point):** LAN = single building/campus, private, high speed. Example: school lab, office.

*LAN = ek building/campus, private, high speed. Example: school lab, office.*

**✖ Why the other options are WRONG (verified):**
- **(A)** WAN spans countries/continents, not one school building. / WAN desh/continents span karta hai, ek school building nahi।
- **(B)** MAN covers a city, not one building. / MAN ek city cover karta hai, ek building nahi।
- **(D)** CAN covers a campus of multiple buildings; here all labs are in one building, so LAN. / CAN kai buildings ke campus ko cover karta hai; yahan sab labs ek hi building mein hain, isliye LAN।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q15]*

---
### Q60. A university has different departments in separate buildings like Engineering, Arts, and Commerce. Each department has its own LAN. All these LANs are connected together for communication. Which type of network connects all these LANs?

<span lang='hi'>Ek university mein alag-alag departments alag buildings mein hain jaise Engineering, Arts, Commerce। Har department ka apna LAN hai। Ye sab LANs communication ke liye aapas mein jude hain। Kaun sa network in sab LANs ko jodta hai?</span>

- **(A)** LAN / LAN
- **(B)** CAN / CAN ✅ **(CORRECT)**
- **(C)** MAN / MAN
- **(D)** WAN / WAN

**✔ Correct Answer: (B) CAN** — A CAN (Campus Area Network) interconnects the LANs of different buildings across a campus (university/corporate). Here, multiple departmental LANs are joined = CAN.

*CAN (Campus Area Network) ek campus (university/corporate) ki alag buildings mein maujood LANs ko interconnect karta hai। Yahan kai departmental LANs jude hain = CAN.*

**★ Nukta (Key Point):** CAN = Campus Area Network - ek campus ki multiple buildings ke LANs ko jodta hai.

*CAN = Campus Area Network - ek campus ki kai buildings ke LANs ko jodta hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** LAN is a single building/site; here multiple buildings are connected. / LAN ek single building/site hai; yahan multiple buildings connected hain।
- **(C)** MAN covers a whole city, larger than a campus. / MAN poori city cover karta hai, campus se bada।
- **(D)** WAN spans countries/continents, much larger than a campus. / WAN desh/continents span karta hai, campus se bahut bada।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q16]*

---
### Q61. An international bank connects its main office in New York with branches in Delhi, London, and Tokyo. Which network type is used here?

<span lang='hi'>Ek international bank apne main office (New York) ko Delhi, London, aur Tokyo ki branches se jodta hai। Yahan kaun sa network type use hota hai?</span>

- **(A)** MAN / MAN
- **(B)** WAN / WAN ✅ **(CORRECT)**
- **(C)** CAN / CAN
- **(D)** LAN / LAN

**✔ Correct Answer: (B) WAN** — Branches in different cities and countries (New York, Delhi, London, Tokyo) are connected over long distances - this is a WAN (Wide Area Network).

*Alag-alag cities aur deshon mein branches (New York, Delhi, London, Tokyo) lambi doori par jude hain - ye WAN (Wide Area Network) hai।*

**★ Nukta (Key Point):** WAN = long distance (city/country/continent). Bank branches worldwide = WAN.

*WAN = lambi doori (city/desh/continent). Worldwide bank branches = WAN.*

**✖ Why the other options are WRONG (verified):**
- **(A)** MAN covers one city, but the bank spans multiple countries. / MAN sirf ek city cover karta hai, lekin bank kai deshon tak faila hai।
- **(C)** CAN covers a campus, not international branches. / CAN ek campus cover karta hai, international branches nahi।
- **(D)** LAN covers a single site, not international branches. / LAN ek single site cover karta hai, international branches nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q17]*

---
### Q62. A company has several servers that store and manage large volumes of data. All storage devices are interconnected for high-speed data access. Which type of network is this?

<span lang='hi'>Ek company ke paas kai servers hain jo badi matra mein data store aur manage karte hain। Sab storage devices high-speed data access ke liye interconnected hain। Ye kaun sa network hai?</span>

- **(A)** LAN / LAN
- **(B)** SAN / SAN ✅ **(CORRECT)**
- **(C)** CAN / CAN
- **(D)** WAN / WAN

**✔ Correct Answer: (B) SAN** — Servers plus storage devices, all interconnected for high-speed data access = SAN (Storage Area Network), a dedicated network for storage.

*Servers + storage devices, sab high-speed data access ke liye interconnected = SAN (Storage Area Network), storage ke liye ek dedicated network.*

**★ Nukta (Key Point):** SAN = Storage Area Network - storage devices ko high-speed access dene ke liye.

*SAN = Storage Area Network - storage devices ko high-speed access dene ke liye।*

**✖ Why the other options are WRONG (verified):**
- **(A)** LAN is the general office network, not a dedicated storage network. / LAN general office network hai, dedicated storage network nahi।
- **(C)** CAN covers a campus, not a storage interconnect. / CAN ek campus cover karta hai, storage interconnect nahi।
- **(D)** WAN spans long distances, not a data-centre storage interconnect. / WAN lambi doori span karta hai, data-centre storage interconnect nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q18]*

---
### Q63. A supplier accessing a company's order tracking system uses:

<span lang='hi'>Ek supplier jo company ke order tracking system ko access karta hai, kaun sa network use karta hai?</span>

- **(A)** Internet / Internet
- **(B)** Intranet / Intranet
- **(C)** Extranet / Extranet ✅ **(CORRECT)**
- **(D)** VPN / VPN

**✔ Correct Answer: (C) Extranet** — An Extranet is an intranet extended to authorized outsiders (suppliers, partners, customers). A supplier accessing the company's order tracking system = Extranet.

*Extranet ek aisa intranet hai jo authorized outsiders (suppliers, partners, customers) ke liye extend kiya gaya ho। Company ke order tracking system ko access karne wala supplier = Extranet.*

**★ Nukta (Key Point):** Extranet = intranet + authorized outsiders (suppliers/partners/customers).

*Extranet = intranet + authorized outsiders (suppliers/partners/customers).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Plain Internet is public; the supplier uses the company's specific system, which is an extranet. / Plain Internet public hai; supplier company ke specific system ka use karta hai, jo extranet hai।
- **(B)** Intranet is only for internal members, not outsiders like suppliers. / Intranet sirf internal members ke liye hai, suppliers jaise outsiders ke liye nahi।
- **(D)** VPN is a technology for secure extension, but the network type here is Extranet. / VPN ek technology hai secure extension ki, lekin yahan network type Extranet hai।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q19]*

---
### Q64. Which network type provides maximum security and privacy?

<span lang='hi'>Kaun sa network type adhikatam (maximum) security aur privacy provide karta hai?</span>

- **(A)** Internet / Internet
- **(B)** Intranet / Intranet ✅ **(CORRECT)**
- **(C)** Extranet / Extranet
- **(D)** None / None

**✔ Correct Answer: (B) Intranet** — An Intranet is a private network inside an organization, accessible only to its members - so it provides maximum security and privacy. Internet is public; extranet is shared with outsiders.

*Intranet ek organization ke andar ka private network hai, sirf uske members ke liye accessible - isliye ye maximum security aur privacy provide karta hai। Internet public hai; extranet outsiders ke saath share hota hai।*

**★ Nukta (Key Point):** Security order: Intranet (sabse secure/private) > Extranet > Internet (public).

*Security order: Intranet (sabse secure/private) > Extranet > Internet (public).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Internet is public - least secure. / Internet public hai - sabse kam secure.
- **(C)** Extranet is shared with outsiders, so less private than an intranet. / Extranet outsiders ke saath share hota hai, isliye intranet se kam private hai।
- **(D)** Intranet does provide maximum security, so None is wrong. / Intranet zaroor maximum security provide karta hai, isliye None galat hai।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q20]*

---
### Q65. A software company shares project reports and progress updates with its clients through a secure online portal that requires login credentials. Which network type is this?

<span lang='hi'>Ek software company apne clients ke saath project reports aur progress updates ek secure online portal ke through share karti hai jismein login credentials chahiye। Ye kaun sa network type hai?</span>

- **(A)** Internet / Internet
- **(B)** Intranet / Intranet
- **(C)** Extranet / Extranet ✅ **(CORRECT)**
- **(D)** MAN / MAN

**✔ Correct Answer: (C) Extranet** — Sharing internal project information with clients (outsiders) through a secure login portal = Extranet (the company's intranet extended to authorized clients).

*Clients (outsiders) ke saath internal project information share karna, ek secure login portal ke through = Extranet (company ka intranet authorized clients ke liye extend kiya gaya).*

**★ Nukta (Key Point):** Clients ko secure portal se share karna = Extranet.

*Clients ko secure portal se share karna = Extranet.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Plain Internet is public; here access is restricted by login, so it is an extranet. / Plain Internet public hai; yahan access login se restricted hai, isliye ye extranet hai।
- **(B)** Intranet is only for internal staff, not clients. / Intranet sirf internal staff ke liye hai, clients ke liye nahi।
- **(D)** MAN is a geographical network type, not relevant here. / MAN ek geographical network type hai, yahan relevant nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q21]*

---
### Q66. Bank employees access internal financial databases, while customers access their accounts through online banking websites. Which networks are being used by employees and customers respectively?

<span lang='hi'>Bank employees internal financial databases access karte hain, jabki customers online banking websites ke through apne accounts access karte hain। Employees aur customers kramashah kaun se networks use kar rahe hain?</span>

- **(A)** Employees - Intranet; Customers - Extranet / employees - Intranet; customers - Extranet ✅ **(CORRECT)**
- **(B)** Employees - Internet; Customers - Intranet / employees - Internet; customers - Intranet
- **(C)** Employees - Extranet; Customers - Internet / employees - Extranet; customers - Internet
- **(D)** Both - Internet / dono - Internet

**✔ Correct Answer: (A) Employees - Intranet; Customers - Extranet** — Employees use the bank's internal private network = Intranet. Customers access the bank's system from outside = Extranet (per the official key: the bank's online banking is its intranet extended to customers).

*Employees bank ke internal private network = Intranet use karte hain। Customers bahar se bank ke system ko access karte hain = Extranet (official key ke anusaar: bank ka online banking uske intranet ka customers ke liye extension hai).*

**★ Nukta (Key Point):** Employees -> Intranet (internal). Outsiders (customers/suppliers) -> Extranet. Public -> Internet.

*Employees -> Intranet (internal). Outsiders (customers/suppliers) -> Extranet. Public -> Internet.*

**✖ Why the other options are WRONG (verified):**
- **(B)** Employees do not use the public Internet for internal databases; customers do not use the intranet. / Employees internal databases ke liye public Internet use nahi karte; customers intranet use nahi karte।
- **(C)** Reversed: employees are internal (intranet), customers are outside (extranet). / Ulta hai: employees internal (intranet) hain, customers bahar (extranet) hain।
- **(D)** Not both Internet: employees use the private intranet. / Dono Internet nahi: employees private intranet use karte hain।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q22]*

---
### Q67. Three or more devices share a link in ________ connection.

<span lang='hi'>Teen ya adhik devices ek link ________ connection mein share karte hain।</span>

- **(A)** Unipoint / unipoint
- **(B)** Multipoint / multipoint ✅ **(CORRECT)**
- **(C)** Point to point / point to point
- **(D)** None of the mentioned / inmein se koi nahi

**✔ Correct Answer: (B) Multipoint** — A multipoint (multidrop) connection is one in which more than two devices share a single link; the capacity of the channel is shared spatially or temporally. (Forouzan)

*Multipoint (multidrop) connection mein do se zyada devices ek single link share karte hain; channel ki capacity spatially ya temporally share hoti hai। (Forouzan)*

**★ Nukta (Key Point):** Multipoint = ek link, kai devices; capacity shared. Point-to-point = dedicated link, sirf 2 devices.

*Multipoint = ek link, kai devices; capacity shared. Point-to-point = dedicated link, sirf 2 devices.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Unipoint is not a standard connection type. / Unipoint koi standard connection type nahi hai।
- **(C)** Point-to-point is a dedicated link between exactly two devices. / Point-to-point exactly do devices ke beech ek dedicated link hai।
- **(D)** Multipoint is indeed the correct answer, so none-of-these is wrong. / Multipoint hi sahi answer hai, isliye koi-nahi galat hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q36]*

---
### Q68. A _______ connection provides a dedicated link between two devices.

<span lang='hi'>Ek _______ connection do devices ke beech ek dedicated link provide karta hai।</span>

- **(A)** point-to-point / point-to-point ✅ **(CORRECT)**
- **(B)** multipoint / multipoint
- **(C)** primary / primary
- **(D)** secondary / secondary

**✔ Correct Answer: (A) point-to-point** — A point-to-point connection provides a dedicated link between two devices; the entire capacity of the link is reserved for transmission between those two devices. (Forouzan)

*Point-to-point connection do devices ke beech ek dedicated link provide karta hai; link ki poori capacity sirf unhi do devices ke liye reserved hoti hai। (Forouzan)*

**★ Nukta (Key Point):** Point-to-point = dedicated link, poori capacity sirf 2 devices ke liye. Example: TV remote (IR), leased line.

*Point-to-point = dedicated link, poori capacity sirf 2 devices ke liye. Example: TV remote (IR), leased line.*

**✖ Why the other options are WRONG (verified):**
- **(B)** Multipoint = more than two devices share a single link. / Multipoint = do se zyada devices ek single link share karte hain।
- **(C)** Primary is not a connection architecture type. / Primary koi connection architecture type nahi hai।
- **(D)** Secondary is not a connection architecture type. / Secondary koi connection architecture type nahi hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q42]*

---
### Q69. Which of the following is an example of Client-Server architecture?

<span lang='hi'>Nimnlikhit mein se kaun Client-Server architecture ka example hai?</span>

- **(A)** Chat between two Bluetooth devices / do Bluetooth devices ke beech chat
- **(B)** Web browser accessing a website / web browser jo ek website access kar raha hai ✅ **(CORRECT)**
- **(C)** File transfer via USB cable / USB cable se file transfer
- **(D)** Two laptops connected directly / do laptops directly connected

**✔ Correct Answer: (B) Web browser accessing a website** — A web browser (client) requesting and receiving a web page from a web server is the classic client-server architecture: the client requests a service and the server provides it.

*Web browser (client) jo ek web server se web page request karta hai aur receive karta hai - ye classic client-server architecture hai: client service request karta hai aur server use provide karta hai।*

**★ Nukta (Key Point):** Client-Server = client request karta hai, server service provide karta hai. Example: web browser - website.

*Client-Server = client request karta hai, server service provide karta hai। Example: web browser - website.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Bluetooth chat between two devices is peer-to-peer (both are equal peers). / Do Bluetooth devices ke beech chat peer-to-peer hai (dono equal peers hain).
- **(C)** USB file transfer is a direct wired transfer, not client-server over a network. / USB file transfer ek direct wired transfer hai, network par client-server nahi।
- **(D)** Two laptops connected directly are peers (P2P), not client-server. / Do directly connected laptops peers (P2P) hain, client-server nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q23]*

---
### Q70. Which of the following uses Peer-to-Peer (P2P) architecture, not Client-Server?

<span lang='hi'>Nimnlikhit mein se kaun Peer-to-Peer (P2P) architecture use karta hai, Client-Server nahi?</span>

- **(A)** BitTorrent file sharing / BitTorrent file sharing ✅ **(CORRECT)**
- **(B)** Google search / Google search
- **(C)** Gmail / Gmail
- **(D)** YouTube / YouTube

**✔ Correct Answer: (A) BitTorrent file sharing** — BitTorrent is peer-to-peer: users (peers) share file pieces directly with each other without a central server. Google search, Gmail and YouTube are client-server services.

*BitTorrent peer-to-peer hai: users (peers) file ke tukde directly aapas mein share karte hain bina kisi central server ke। Google search, Gmail aur YouTube client-server services hain।*

**★ Nukta (Key Point):** P2P = peers aapas mein directly share karte hain (BitTorrent). Client-Server = server service deta hai (Google, Gmail, YouTube).

*P2P = peers aapas mein directly share karte hain (BitTorrent). Client-Server = server service deta hai (Google, Gmail, YouTube).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Google search is client-server (you request, Google's servers respond). / Google search client-server hai (aap request karte ho, Google ke servers respond karte hain).
- **(C)** Gmail is client-server (your mail client talks to Google's mail servers). / Gmail client-server hai (aapka mail client Google ke mail servers se baat karta hai).
- **(D)** YouTube is client-server (your browser requests videos from YouTube servers). / YouTube client-server hai (aapka browser YouTube servers se videos request karta hai).

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q24]*

---
### Q71. In a bank, customers use ATMs to check balance or withdraw cash. ATM machines send the request to a central computer for verification and processing. Which type of architecture is used here?

<span lang='hi'>Ek bank mein customers ATMs se balance check ya cash withdraw karte hain। ATM machines request ek central computer ko verification aur processing ke liye bhejte hain। Yahan kaun si architecture use hoti hai?</span>

- **(A)** Peer-to-Peer / peer-to-peer
- **(B)** Client-Server / client-server ✅ **(CORRECT)**
- **(C)** Multipoint / multipoint
- **(D)** Point-to-Point / point-to-point

**✔ Correct Answer: (B) Client-Server** — The ATM (client) sends a request to a central computer (server) for verification and processing - the client requests a service and the server provides it = client-server architecture.

*ATM (client) request ek central computer (server) ko verification aur processing ke liye bhejta hai - client service request karta hai aur server use provide karta hai = client-server architecture.*

**★ Nukta (Key Point):** ATM -> central server = client-server (client request, server verify/process).

*ATM -> central server = client-server (client request, server verify/process).*

**✖ Why the other options are WRONG (verified):**
- **(A)** ATM and the central computer are not equal peers; the server processes requests. / ATM aur central computer equal peers nahi hain; server requests process karta hai।
- **(C)** Multipoint is a connection type (one link, many devices), not an architecture. / Multipoint ek connection type hai (ek link, kai devices), architecture nahi।
- **(D)** Point-to-point is a dedicated link between two devices, not the ATM-server model. / Point-to-point do devices ke beech ek dedicated link hai, ATM-server model nahi।

*[Source: Repo: BCI_SCI Subject Test-01 (UNIT TEST-1 CN & Security), Q25]*

---
### Q72. In a LAN, connectivity can be created using Wi-Fi or _______.

<span lang='hi'>Ek LAN mein connectivity Wi-Fi ya _______ se banayi ja sakti hai।</span>

- **(A)** TV / TV
- **(B)** Radio / radio
- **(C)** Mobile / mobile
- **(D)** Ethernet / Ethernet ✅ **(CORRECT)**

**✔ Correct Answer: (D) Ethernet** — LAN connectivity is created using Wi-Fi (wireless) or Ethernet cables (wired). TV, radio and mobile are not LAN connectivity media.

*LAN connectivity Wi-Fi (wireless) ya Ethernet cables (wired) se banayi jaati hai। TV, radio aur mobile LAN connectivity media nahi hain।*

**★ Nukta (Key Point):** LAN connectivity = Wi-Fi (wireless) + Ethernet (wired cable).

*LAN connectivity = Wi-Fi (wireless) + Ethernet (wired cable).*

**✖ Why the other options are WRONG (verified):**
- **(A)** TV is a broadcast device, not a LAN connectivity medium. / TV ek broadcast device hai, LAN connectivity medium nahi।
- **(B)** Radio is a broadcast medium, not a LAN connectivity medium. / Radio ek broadcast medium hai, LAN connectivity medium nahi।
- **(C)** Mobile is a device, not a LAN connectivity medium (though it can connect via Wi-Fi). / Mobile ek device hai, LAN connectivity medium nahi (haalaanki ye Wi-Fi se connect ho sakta hai).

*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)]*

---

## Section F - Network History (ARPANET to Today's Network)

*Syllabus: Network History - ARPANET to today's network*

### Q73. ARPANET stands for _______.

<span lang='hi'>ARPANET ka poora naam hai _______.</span>

- **(A)** Advanced Recheck Projects Agency Internet / Advanced Recheck Projects Agency Internet
- **(B)** Advanced Recheck Projects Agency Network / Advanced Recheck Projects Agency Network
- **(C)** Advanced Research Projects Agency Network / Advanced Research Projects Agency Network ✅ **(CORRECT)**
- **(D)** Advanced Research Projects Agency Internet / Advanced Research Projects Agency Internet

**✔ Correct Answer: (C) Advanced Research Projects Agency Network** — ARPANET = Advanced Research Projects Agency Network. It was created by ARPA (Advanced Research Projects Agency) of the U.S. Department of Defense.

*ARPANET = Advanced Research Projects Agency Network. Ise ARPA (Advanced Research Projects Agency) of U.S. Department of Defense ne banaya tha।*

**★ Nukta (Key Point):** ARPANET = Advanced Research Projects Agency Network (U.S. Dept. of Defense).

*ARPANET = Advanced Research Projects Agency Network (U.S. Dept. of Defense).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Recheck is wrong; also Internet is wrong - it is a Network. / Recheck galat hai; aur Internet bhi galat hai - ye Network hai।
- **(B)** Recheck is wrong (it is Research), though Network is right. / Recheck galat hai (sahi shabd Research hai), haalaanki Network sahi hai।
- **(D)** Internet is wrong - ARPANET is a Network. / Internet galat hai - ARPANET ek Network hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q26]*

---
### Q74. The first network was:

<span lang='hi'>Sabse pehla network tha:</span>

- **(A)** CNNET / CNNET
- **(B)** NSFNET / NSFNET
- **(C)** ASAPNET / ASAPNET
- **(D)** ARPANET / ARPANET ✅ **(CORRECT)**

**✔ Correct Answer: (D) ARPANET** — The first network was ARPANET (1969), created by ARPA of the U.S. Department of Defense. NSFNET (1986) came later as a backbone.

*Sabse pehla network ARPANET (1969) tha, jise ARPA of U.S. Department of Defense ne banaya tha। NSFNET (1986) baad mein ek backbone ke roop mein aaya tha।*

**★ Nukta (Key Point):** First network = ARPANET (1969). NSFNET = 1986 (backbone).

*First network = ARPANET (1969). NSFNET = 1986 (backbone).*

**✖ Why the other options are WRONG (verified):**
- **(A)** CNNET is not a real/standard network. / CNNET koi real/standard network nahi hai।
- **(B)** NSFNET came later (1986), it was not the first network. / NSFNET baad mein aaya (1986), ye pehla network nahi tha।
- **(C)** ASAPNET is not a real/standard network. / ASAPNET koi real/standard network nahi hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q34]*

---
### Q75. In the original ARPANET, _______ were directly connected together.

<span lang='hi'>Original ARPANET mein, _______ aapas mein directly connected the।</span>

- **(A)** IMPs / IMPs (Interface Message Processors) ✅ **(CORRECT)**
- **(B)** host computers / host computers
- **(C)** networks / networks
- **(D)** routers / routers

**✔ Correct Answer: (A) IMPs** — In the original ARPANET, the IMPs (Interface Message Processors - the packet switches) were directly connected together; the host computers connected to the IMPs.

*Original ARPANET mein, IMPs (Interface Message Processors - packet switches) aapas mein directly connected the; host computers IMPs se connect hote the।*

**★ Nukta (Key Point):** Original ARPANET: IMPs (packet switches) directly connected; hosts attached to IMPs.

*Original ARPANET: IMPs (packet switches) directly connected the; hosts IMPs se attach hote the।*

**✖ Why the other options are WRONG (verified):**
- **(B)** Host computers connected to the IMPs, not directly to each other. / Host computers IMPs se connect hote the, aapas mein directly nahi।
- **(C)** Networks were connected later; originally it was IMPs. / Networks baad mein connect hui; originally IMPs hi the।
- **(D)** Routers as we know them came later; the original packet switches were IMPs. / Routers jaise aaj jaante hain baad mein aaye; original packet switches IMPs the।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q43]*

---
### Q76. The first operational computer network in the world was the _________ for the United States Department of Defense.

<span lang='hi'>Duniya ka pehla operational computer network, United States Department of Defense ke liye _________ tha।</span>

- **(A)** ARPANET / ARPANET ✅ **(CORRECT)**
- **(B)** ERNET / ERNET
- **(C)** SKYNET / SKYNET
- **(D)** DARPANET / DARPANET

**✔ Correct Answer: (A) ARPANET** — ARPANET was the first operational computer network in the world, created for the U.S. Department of Defense (1969).

*ARPANET duniya ka pehla operational computer network tha, jo U.S. Department of Defense ke liye banaya gaya tha (1969).*

**★ Nukta (Key Point):** First operational network = ARPANET (1969, U.S. DoD).

*First operational network = ARPANET (1969, U.S. DoD).*

**✖ Why the other options are WRONG (verified):**
- **(B)** ERNET is India's education/research network, not the first. / ERNET India ka education/research network hai, pehla nahi।
- **(C)** SKYNET is fictional (not a real first network). / SKYNET kalpanik hai (real pehla network nahi).
- **(D)** DARPANET is not a standard/real network. / DARPANET koi standard/real network nahi hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q48]*

---
### Q77. ARPANET - the precursor of today's Internet - was created in ______ by ARPA (Advanced Research Projects Agency) of the U.S. Department of Defense, starting with four nodes (UCLA, SRI, UC Santa Barbara, University of Utah).

<span lang='hi'>ARPANET - aaj ke Internet ka purvaj - ______ mein ARPA (Advanced Research Projects Agency), U.S. Department of Defense dwara banaya gaya tha, chaar nodes se shuruaat hui (UCLA, SRI, UC Santa Barbara, University of Utah).</span>

- **(A)** 1957 / 1957
- **(B)** 1969 / 1969 ✅ **(CORRECT)**
- **(C)** 1983 / 1983
- **(D)** 1991 / 1991

**✔ Correct Answer: (B) 1969** — ARPANET was born in 1969 with four nodes: UCLA, Stanford Research Institute (SRI), UC Santa Barbara and the University of Utah. The first message was sent on 29 October 1969 (the LO of LOGIN).

*ARPANET 1969 mein chaar nodes ke saath bana tha: UCLA, Stanford Research Institute (SRI), UC Santa Barbara aur University of Utah. Pehla message 29 October 1969 ko bheja gaya tha (LOGIN ka LO).*

**★ Nukta (Key Point):** ARPANET = 1969, 4 nodes (UCLA, SRI, UCSB, Utah); first message 29 Oct 1969 (LO of LOGIN).

*ARPANET = 1969, 4 nodes (UCLA, SRI, UCSB, Utah); pehla message 29 Oct 1969 (LOGIN ka LO).*

**✖ Why the other options are WRONG (verified):**
- **(A)** 1957 = Sputnik era; ARPA itself was created in 1958 - ARPANET came later. / 1957 = Sputnik ka zamana; ARPA khud 1958 mein bana tha - ARPANET baad mein aaya।
- **(C)** 1983 = the year ARPANET adopted TCP/IP (flag day). / 1983 = jis saal ARPANET ne TCP/IP adopt kiya (flag day).
- **(D)** 1991 = the year the World Wide Web was invented. / 1991 = jis saal World Wide Web ka invention hua।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q78. TCP/IP (developed by Vint Cerf and Bob Kahn) was adopted by ARPANET as its official protocol suite on 1 January ______ - an event known as the flag day.

<span lang='hi'>TCP/IP (Vint Cerf aur Bob Kahn dwara develop kiya gaya) ko ARPANET ne apna official protocol suite banaya tha 1 January ______ ko - is event ko flag day kaha jata hai।</span>

- **(A)** 1969 / 1969
- **(B)** 1972 / 1972
- **(C)** 1983 / 1983 ✅ **(CORRECT)**
- **(D)** 1995 / 1995

**✔ Correct Answer: (C) 1983** — On 1 January 1983, ARPANET officially switched to TCP/IP - the flag day - making TCP/IP the common language of the network. Cerf and Kahn developed TCP/IP in the 1970s (publicly demonstrated in 1972).

*1 January 1983 ko ARPANET officially TCP/IP par switch ho gaya - flag day - jisse TCP/IP network ki common language ban gaya। Cerf aur Kahn ne TCP/IP 1970s mein develop kiya tha (1972 mein publicly demonstrate hua).*

**★ Nukta (Key Point):** Flag day = 1 Jan 1983 (ARPANET -> TCP/IP). TCP/IP developed by Cerf & Kahn in 1970s (demo 1972). Syllabus ka TCP/IP model 1972 = development era.

*Flag day = 1 Jan 1983 (ARPANET -> TCP/IP). TCP/IP Cerf & Kahn ne 1970s mein develop kiya (demo 1972). Syllabus ka TCP/IP model 1972 = development era.*

**✖ Why the other options are WRONG (verified):**
- **(A)** 1969 = ARPANET creation. / 1969 = ARPANET ki creation.
- **(B)** 1972 = ARPANET public demonstration / TCP first demonstrated - not the adoption date. / 1972 = ARPANET public demonstration / TCP pehli baar demonstrate hua - adoption date nahi।
- **(D)** 1995 = Windows 95 / commercial Internet boom era - not the flag day. / 1995 = Windows 95 / commercial Internet boom ka zamana - flag day nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q79. NSFNET, created by the U.S. National Science Foundation in ______, became a major backbone of the Internet, connecting universities and research centres.

<span lang='hi'>NSFNET, U.S. National Science Foundation dwara ______ mein banaya gaya, Internet ka ek major backbone ban gaya, universities aur research centres ko jodta tha।</span>

- **(A)** 1969 / 1969
- **(B)** 1983 / 1983
- **(C)** 1986 / 1986 ✅ **(CORRECT)**
- **(D)** 1991 / 1991

**✔ Correct Answer: (C) 1986** — NSFNET was created in 1986 by the National Science Foundation; it connected universities and research centres with T1 lines (1.544 Mbps) and became a major Internet backbone.

*NSFNET 1986 mein National Science Foundation dwara banaya gaya tha; isne universities aur research centres ko T1 lines (1.544 Mbps) se joda aur ek major Internet backbone ban gaya।*

**★ Nukta (Key Point):** NSFNET = 1986 (National Science Foundation), T1 backbone -> Internet backbone.

*NSFNET = 1986 (National Science Foundation), T1 backbone -> Internet backbone.*

**✖ Why the other options are WRONG (verified):**
- **(A)** 1969 = ARPANET. / 1969 = ARPANET.
- **(B)** 1983 = TCP/IP flag day. / 1983 = TCP/IP flag day.
- **(D)** 1991 = WWW invented. / 1991 = WWW ka invention hua।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---
### Q80. The World Wide Web (WWW) was invented in 1991 at CERN by ______, and it made the Internet popular among the general public.

<span lang='hi'>World Wide Web (WWW) ka invention 1991 mein CERN mein ______ ne kiya tha, aur isne Internet ko aam public ke beech popular banaya।</span>

- **(A)** Vint Cerf / Vint Cerf
- **(B)** Tim Berners-Lee / Tim Berners-Lee ✅ **(CORRECT)**
- **(C)** Bob Kahn / Bob Kahn
- **(D)** Marc Andreessen / Marc Andreessen

**✔ Correct Answer: (B) Tim Berners-Lee** — Tim Berners-Lee invented the WWW at CERN in 1991 (using HTML, HTTP and URLs). The Mosaic browser (1993) later made the web popular; the Internet opened to commercial use in the 1990s.

*Tim Berners-Lee ne 1991 mein CERN mein WWW ka invention kiya tha (HTML, HTTP aur URLs ka use karke). Mosaic browser (1993) ne baad mein web ko popular banaya; Internet 1990s mein commercial use ke liye khula।*

**★ Nukta (Key Point):** WWW = 1991, Tim Berners-Lee @ CERN. Mosaic browser 1993. Vint Cerf & Bob Kahn = fathers of the Internet (TCP/IP).

*WWW = 1991, Tim Berners-Lee @ CERN. Mosaic browser 1993. Vint Cerf & Bob Kahn = Internet ke fathers (TCP/IP).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Vint Cerf co-developed TCP/IP - father of the Internet, not the WWW. / Vint Cerf ne TCP/IP co-develop kiya - Internet ke father, WWW ke nahi।
- **(C)** Bob Kahn co-developed TCP/IP - not the WWW. / Bob Kahn ne TCP/IP co-develop kiya - WWW nahi।
- **(D)** Marc Andreessen co-created the Mosaic browser (1993) - not the inventor of the WWW. / Marc Andreessen ne Mosaic browser (1993) co-create kiya - WWW ke inventor nahi।

*[Source: Extra (Forouzan) - fills syllabus gap]*

---

## Section G - General Network Basics (WWW, E-mail, Protocols, Servers, Switching - from repo intro tests)

*Syllabus: Introduction of DC - general basics asked in BCI/RPSC exams (Specific Address/URL, Application services, Switching)*

### Q81. A collection of hyperlinked documents on the internet forms the?

<span lang='hi'>Internet par hyperlinked documents ka sangrah (collection) kya banata hai?</span>

- **(A)** World Wide Web (WWW) / World Wide Web (WWW) ✅ **(CORRECT)**
- **(B)** E-mail system / e-mail system
- **(C)** Mailing list / mailing list
- **(D)** Hypertext markup language / hypertext markup language (HTML)

**✔ Correct Answer: (A) World Wide Web (WWW)** — A collection of hyperlinked documents on the Internet forms the World Wide Web (WWW). HTML is the markup language used to create those documents.

*Internet par hyperlinked documents ka sangrah World Wide Web (WWW) banata hai। HTML woh markup language hai jis se ye documents bante hain।*

**★ Nukta (Key Point):** WWW = hyperlinked documents ka collection. HTML = un documents ki language (WWW nahi).

*WWW = hyperlinked documents ka collection. HTML = un documents ki language hai (WWW nahi).*

**✖ Why the other options are WRONG (verified):**
- **(B)** An e-mail system is for sending/receiving mail, not a collection of documents. / E-mail system mail bhejne/paane ke liye hai, documents ka collection nahi।
- **(C)** A mailing list is a list of e-mail addresses for group messages. / Mailing list group messages ke liye e-mail addresses ki ek list hai।
- **(D)** HTML is the markup language used to write web pages, not the collection itself. / HTML web pages likhne ki markup language hai, collection khud nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q5]*

---
### Q82. Which one of the following is a valid email address?

<span lang='hi'>Nimnlikhit mein se kaun sa ek valid email address hai?</span>

- **(A)** computech@academy.com / computech@academy.com ✅ **(CORRECT)**
- **(B)** gmail.com / gmail.com
- **(C)** compu@.com / compu@.com
- **(D)** computech@books / computech@books

**✔ Correct Answer: (A) computech@academy.com** — A valid email address has a local part, the @ symbol, and a domain with a top-level domain (TLD). computech@academy.com follows this format.

*Ek valid email address mein local part, @ symbol, aur ek domain with top-level domain (TLD) hota hai। computech@academy.com ye format follow karta hai।*

**★ Nukta (Key Point):** Valid email = local@domain.TLD (e.g., name@site.com).

*Valid email = local@domain.TLD (jaise name@site.com).*

**✖ Why the other options are WRONG (verified):**
- **(B)** gmail.com has no @ and no local part - invalid. / gmail.com mein @ nahi hai aur local part bhi nahi - invalid.
- **(C)** compu@.com has an empty domain - invalid. / compu@.com mein domain khaali hai - invalid.
- **(D)** computech@books has no top-level domain (like .com) - invalid. / computech@books mein top-level domain (jaise .com) nahi hai - invalid.

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q6]*

---
### Q83. Which of the following best describes uploading information?

<span lang='hi'>Nimnlikhit mein se kaun uploading information ko sabse achhe se describe karta hai?</span>

- **(A)** Sorting data on a disk drive / disk drive par data ko sort karna
- **(B)** Sending information to a host computer / information ko ek host computer ko bhejna ✅ **(CORRECT)**
- **(C)** Receiving information from a host computer / ek host computer se information receive karna
- **(D)** Sorting data on a hard drive / hard drive par data ko sort karna

**✔ Correct Answer: (B) Sending information to a host computer** — Uploading means sending/transferring information from a local device to a host/remote computer over a network.

*Uploading ka matlab hai information ko ek local device se ek host/remote computer ko network ke through bhejna।*

**★ Nukta (Key Point):** Uploading = local se remote/host ko bhejna. Downloading = remote se local ko lena.

*Uploading = local se remote/host ko bhejna. Downloading = remote se local ko lena.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Sorting data on a disk is organising files, not uploading. / Disk par data sort karna files ko organise karna hai, uploading nahi।
- **(C)** Receiving information from a host is downloading, not uploading. / Host se information receive karna = downloading hai, uploading nahi।
- **(D)** Sorting data on a hard drive is organising files, not uploading. / Hard drive par data sort karna files ko organise karna hai, uploading nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q7]*

---
### Q84. Which one of the following is the most common internet protocol?

<span lang='hi'>Nimnlikhis mein se kaun sa sabse common internet protocol hai?</span>

- **(A)** HTML / HTML
- **(B)** NetBEUI / NetBEUI
- **(C)** TCP/IP / TCP/IP ✅ **(CORRECT)**
- **(D)** IPX/SPX / IPX/SPX

**✔ Correct Answer: (C) TCP/IP** — TCP/IP is the core protocol suite of the Internet - it is the most common protocol used on the Internet. HTML is a markup language, not a protocol.

*TCP/IP Internet ka core protocol suite hai - ye Internet par sabse common protocol hai। HTML ek markup language hai, protocol nahi।*

**★ Nukta (Key Point):** Internet ka core protocol = TCP/IP. HTML = language, protocol nahi.

*Internet ka core protocol = TCP/IP. HTML = language hai, protocol nahi.*

**✖ Why the other options are WRONG (verified):**
- **(A)** HTML is a markup language for web pages, not a protocol. / HTML web pages ke liye ek markup language hai, protocol nahi।
- **(B)** NetBEUI is an old Microsoft LAN protocol, not the common Internet protocol. / NetBEUI ek purana Microsoft LAN protocol hai, common Internet protocol nahi।
- **(D)** IPX/SPX is an old Novell protocol, not the common Internet protocol. / IPX/SPX ek purana Novell protocol hai, common Internet protocol nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q8]*

---
### Q85. The dial-up connections to access the internet use ___ protocol.

<span lang='hi'>Internet access ke liye dial-up connections ___ protocol use karte hain।</span>

- **(A)** PPP (Point to Point protocol) / PPP (Point to Point protocol) ✅ **(CORRECT)**
- **(B)** X.25 protocol / X.25 protocol
- **(C)** PLIP protocol / PLIP protocol
- **(D)** None of the above / inmein se koi nahi

**✔ Correct Answer: (A) PPP (Point to Point protocol)** — Dial-up connections to access the Internet use PPP (Point-to-Point Protocol), which carries IP traffic over the telephone line.

*Internet access ke liye dial-up connections PPP (Point-to-Point Protocol) use karte hain, jo telephone line par IP traffic carry karta hai।*

**★ Nukta (Key Point):** Dial-up Internet = PPP (Point-to-Point Protocol).

*Dial-up Internet = PPP (Point-to-Point Protocol).*

**✖ Why the other options are WRONG (verified):**
- **(B)** X.25 is an old packet-switching WAN protocol, not used for dial-up Internet access. / X.25 ek purana packet-switching WAN protocol hai, dial-up Internet access ke liye nahi।
- **(C)** PLIP is a Linux parallel-port IP protocol, not for dial-up. / PLIP ek Linux parallel-port IP protocol hai, dial-up ke liye nahi।
- **(D)** PPP is indeed the correct protocol, so none-of-these is wrong. / PPP hi sahi protocol hai, isliye koi-nahi galat hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q18]*

---
### Q86. Home broadband connections that work on DSL (Digital Subscriber Line) use ___ protocol.

<span lang='hi'>DSL (Digital Subscriber Line) par kaam karne wale home broadband connections ___ protocol use karte hain।</span>

- **(A)** PPPoE (PPP over Ethernet) / PPPoE (PPP over Ethernet) ✅ **(CORRECT)**
- **(B)** PPPoA (PPP over ATM) / PPPoA (PPP over ATM)
- **(C)** Bridge protocol / bridge protocol
- **(D)** All of the above / upar Sabhi

**✔ Correct Answer: (A) PPPoE (PPP over Ethernet)** — Home DSL broadband connections typically use PPPoE (PPP over Ethernet) to carry PPP traffic over the DSL/Ethernet connection.

*Home DSL broadband connections aam taur par PPPoE (PPP over Ethernet) use karte hain taaki PPP traffic DSL/Ethernet connection par carry ho sake।*

**★ Nukta (Key Point):** Home DSL broadband = PPPoE (PPP over Ethernet).

*Home DSL broadband = PPPoE (PPP over Ethernet).*

**✖ Why the other options are WRONG (verified):**
- **(B)** PPPoA (PPP over ATM) is used on ATM-based DSL, not the typical home Ethernet setup. / PPPoA (PPP over ATM) ATM-based DSL par use hota hai, typical home Ethernet setup par nahi।
- **(C)** Bridge protocol is a bridging mode, not the typical home broadband protocol. / Bridge protocol ek bridging mode hai, typical home broadband protocol nahi।
- **(D)** All of the above is wrong because the standard home DSL protocol is PPPoE. / Upar sabhi galat hai kyunki standard home DSL protocol PPPoE hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q19]*

---
### Q87. Which of the following servers allows LAN users to share data?

<span lang='hi'>Nimnlikhit mein se kaun sa server LAN users ko data share karne ki anumati deta hai?</span>

- **(A)** Data server / data server
- **(B)** Point server / point server
- **(C)** File server / file server ✅ **(CORRECT)**
- **(D)** Communication server / communication server

**✔ Correct Answer: (C) File server** — A file server stores files and allows LAN users to share/access data (files) over the network.

*Ek file server files store karta hai aur LAN users ko network par data (files) share/access karne ki anumati deta hai।*

**★ Nukta (Key Point):** File server = files store + LAN users ko share karne deta hai.

*File server = files store karta hai + LAN users ko share karne deta hai।*

**✖ Why the other options are WRONG (verified):**
- **(A)** Data server is a general term; the specific server for sharing files is a file server. / Data server ek general term hai; files share karne wala specific server file server hai।
- **(B)** Point server is not a standard server type. / Point server koi standard server type nahi hai।
- **(D)** Communication server handles communication services (e.g., mail/chat), not file sharing. / Communication server communication services (jaise mail/chat) handle karta hai, file sharing nahi।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q22]*

---
### Q88. EDI stands for ____.

<span lang='hi'>EDI ka poora naam hai ____.</span>

- **(A)** Electronic Data Interchange / Electronic Data Interchange ✅ **(CORRECT)**
- **(B)** Electronic Digital Internet / Electronic Digital Internet
- **(C)** Electronic Digital Interchange / Electronic Digital Interchange
- **(D)** Electronic Data Internet / Electronic Data Internet

**✔ Correct Answer: (A) Electronic Data Interchange** — EDI = Electronic Data Interchange - the computer-to-computer exchange of business documents (orders, invoices) in a standard electronic format.

*EDI = Electronic Data Interchange - business documents (orders, invoices) ka computer-to-computer exchange, ek standard electronic format mein.*

**★ Nukta (Key Point):** EDI = Electronic Data Interchange (business documents ka e-exchange).

*EDI = Electronic Data Interchange (business documents ka e-exchange).*

**✖ Why the other options are WRONG (verified):**
- **(B)** Electronic Digital Internet is not the correct expansion. / Electronic Digital Internet sahi expansion nahi hai।
- **(C)** Electronic Digital Interchange is not the correct expansion. / Electronic Digital Interchange sahi expansion nahi hai।
- **(D)** Electronic Data Internet is not the correct expansion. / Electronic Data Internet sahi expansion nahi hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q25]*

---
### Q89. A computer network permits sharing of:

<span lang='hi'>Ek computer network kis cheez ki sharing ki anumati deta hai?</span>

- **(A)** Resources / resources (printer, disk, etc.)
- **(B)** Information / information (data)
- **(C)** Both a & b / dono a aur b ✅ **(CORRECT)**
- **(D)** None of these / inmein se koi nahi

**✔ Correct Answer: (C) Both a & b** — A computer network permits sharing of both resources (printers, storage, devices) and information (data/messages) among connected users.

*Ek computer network dono cheezon ki sharing ki anumati deta hai: resources (printers, storage, devices) aur information (data/messages), connected users ke beech।*

**★ Nukta (Key Point):** Network = resources + information sharing.

*Network = resources + information sharing.*

**✖ Why the other options are WRONG (verified):**
- **(A)** Resources only is incomplete - information/data is also shared. / Sirf resources adhura hai - information/data bhi share hota hai।
- **(B)** Information only is incomplete - resources are also shared. / Sirf information adhura hai - resources bhi share hote hain।
- **(D)** Both are shared, so none-of-these is wrong. / Dono share hote hain, isliye koi-nahi galat hai।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q47 / CN Topic Test-02 (UNIT TEST-2), Q47]*

---
### Q90. How many digits of the Data Network Identification Code (DNIC) identify the country?

<span lang='hi'>Data Network Identification Code (DNIC) ke kitne digits desh (country) ki pehchan karte hain?</span>

- **(A)** first three / pehle teen ✅ **(CORRECT)**
- **(B)** first four / pehle chaar
- **(C)** first five / pehle paanch
- **(D)** first six / pehle chhah

**✔ Correct Answer: (A) first three** — In the DNIC (used in X.121 addressing), the first three digits are the country code and the fourth digit identifies the network within that country. So the first three digits identify the country.

*DNIC (X.121 addressing mein use hota hai) mein pehle teen digits country code hote hain aur chautha digit us desh ke andar ke network ki pehchan karta hai। Isliye pehle teen digits desh ki pehchan karte hain।*

**★ Nukta (Key Point):** DNIC: first 3 digits = country code, 4th digit = network code.

*DNIC: pehle 3 digits = country code, chautha digit = network code.*

**✖ Why the other options are WRONG (verified):**
- **(B)** Four digits include the network digit; only the first three are the country code. / Chaar digits mein network digit bhi aata hai; sirf pehle teen country code hain।
- **(C)** Five digits are more than the DNIC country+network code. / Paanch digits DNIC ke country+network code se zyada hain।
- **(D)** Six digits are more than the DNIC country+network code. / Chhah digits DNIC ke country+network code se zyada hain।

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1), Q15]*

---
### Q91. All the information on the internet is passed using _______ switching method.

<span lang='hi'>Internet par saari information _______ switching method se pass hoti hai।</span>

- **(A)** Portable / portable
- **(B)** Packets / packets ✅ **(CORRECT)**
- **(C)** Pouch / pouch
- **(D)** Primary / primary

**✔ Correct Answer: (B) Packets** — The Internet uses packet switching: data is broken into small packets that travel independently over the network and are reassembled at the destination.

*Internet packet switching use karta hai: data ko chhote packets mein tod kar bheja jata hai jo network par independently travel karte hain aur destination par reassemble hote hain।*

**★ Nukta (Key Point):** Internet = packet switching. Circuit switching = dedicated path (old telephone).

*Internet = packet switching. Circuit switching = dedicated path (purana telephone).*

**✖ Why the other options are WRONG (verified):**
- **(A)** Portable is not a switching method. / Portable koi switching method nahi hai।
- **(C)** Pouch is not a switching method. / Pouch koi switching method nahi hai।
- **(D)** Primary is not a switching method. / Primary koi switching method nahi hai।

*[Source: Repo: Random Test- Rajasthan PYQ (RPSC/RSSB)]*

---
