# Data Communication & Computer Networks (CN)
## Topic 3 of 7 : Addressing (MAC, IPv4, IPv6, Port, DNS) — 93 MCQs (English + Hindi)

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** RPSC Programmer • ACP • RSMSSB IA • SA • DD • BCI • SCI • REET • RAS • DSSSB • KVS • NVS • HTET • SSC CGL/CHSL • RRB • IBPS • UPSC & all Rajasthan + Central Govt. Exams (Computer Awareness)

**Total Questions:** 93 | **Type:** MCQ (4 options) | **Bilingual:** English + Hindi (technical terms in English) | Each: ✔ why the correct answer is right + ★ Nukta. Wrong options verified internally. Answers cross-verified 4×.

### Syllabus Coverage (sub-topic wise order)

| # | Sub-topic | Questions |
|---|-----------|-----------|
| 1 | Section A — Address Levels & MAC Address (Physical Address) | Q1 - Q10 |
| 2 | Section B — IPv4 Addressing (Format, Classes & Special Addresses) | Q11 - Q43 |
| 3 | Section C — Subnetting & CIDR | Q44 - Q70 |
| 4 | Section D — IPv6 Addressing | Q71 - Q79 |
| 5 | Section E — Port Numbers, DNS/URL & Address Resolution (ARP) | Q80 - Q93 |

---

## Section A — Address Levels & MAC Address (Physical Address)

*Forouzan's four address levels; the 48-bit burned-in MAC address, unicast/multicast/broadcast MAC.*

### Q1. Which of the following is a static hardware address?

<span lang='hi'>निम्न में से कौन-सा static hardware address है?</span>

- **(A)** IP address
- **(B)** MAC address ✅ **(CORRECT)**
- **(C)** Port number
- **(D)** Domain name

**✔ Correct Answer: (B) MAC address** — The MAC address is static — it is assigned by the manufacturer and does not normally change; IP addresses, ports and domain names are all dynamic/logical.

*MAC address static होता है — यह manufacturer द्वारा दिया जाता है और सामान्यतः नहीं बदलता; IP addresses, ports और domain names सब dynamic/logical हैं।*

**★ Nukta (Key Point):** Static = burned into hardware (MAC). Dynamic/logical = configured (IP via DHCP, port per connection, name via DNS).

*Static = hardware में burned (MAC)। Dynamic/logical = configure होते हैं (IP via DHCP, port per connection, name via DNS)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q2. A MAC address is also called a ______ address.

<span lang='hi'>MAC address को ______ address भी कहा जाता है।</span>

- **(A)** Physical address ✅ **(CORRECT)**
- **(B)** Logical address
- **(C)** Source address
- **(D)** Destination address

**✔ Correct Answer: (A) Physical address** — The MAC address is permanently burned into the NIC — it is the physical (hardware) address of the device, unlike the logical IP address which is configured by software.

*MAC address NIC में permanently burn होता है — यह device का physical (hardware) address है, logical IP address के विपरीत जो software से configure होता है।*

**★ Nukta (Key Point):** MAC = physical/hardware address (burned-in, 48-bit). IP = logical address (configured). Both change hands at different layers.

*MAC = physical/hardware address (burned-in, 48-bit)। IP = logical address (configured)।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1) · also BCI_SCI ST-7] · Medium*

---
### Q3. The address used in the Data Link Layer is called:

<span lang='hi'>Data Link Layer में उपयोग होने वाले address को क्या कहते हैं?</span>

- **(A)** Logical address
- **(B)** Port address
- **(C)** MAC address ✅ **(CORRECT)**
- **(D)** IP address

**✔ Correct Answer: (C) MAC address** — The data link layer uses the MAC (physical/hardware) address for frame delivery on the local link.

*Data link layer local link पर frame delivery के लिए MAC (physical/hardware) address उपयोग करती है।*

**★ Nukta (Key Point):** Layer-address map again: Data link→MAC, Network→IP, Transport→Port, Application→socket.

*Layer-address map: Data link→MAC, Network→IP, Transport→Port, Application→socket।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q4. Which address identifies a unique device on a local network segment?

<span lang='hi'>Local network segment पर कौन-सा address एक unique device की पहचान करता है?</span>

- **(A)** IP address
- **(B)** MAC address ✅ **(CORRECT)**
- **(C)** Gateway
- **(D)** Subnet mask

**✔ Correct Answer: (B) MAC address** — Within a local network segment (LAN), frames are delivered using the MAC address — the unique 48-bit hardware address of each NIC.

*Local network segment (LAN) के भीतर frames की delivery MAC address से होती है — हर NIC का unique 48-bit hardware address।*

**★ Nukta (Key Point):** L2 delivery (same network) = MAC. L3 delivery (across networks) = IP. Exam loves this pair.

*L2 delivery (same network) = MAC। L3 delivery (across networks) = IP। Exam इस जोड़ी को बहुत पूछता है।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

---
### Q5. What type of MAC address is FF:FF:FF:FF:FF:FF?

<span lang='hi'>FF:FF:FF:FF:FF:FF किस प्रकार का MAC address है?</span>

- **(A)** Unicast
- **(B)** Multicast
- **(C)** Broadcast ✅ **(CORRECT)**
- **(D)** Loopback

**✔ Correct Answer: (C) Broadcast** — FF:FF:FF:FF:FF:FF is the broadcast MAC address — a frame sent to it is received by every device on the LAN segment.

*FF:FF:FF:FF:FF:FF broadcast MAC address है — इसे भेजा frame LAN segment के हर device को मिलता है।*

**★ Nukta (Key Point):** MAC broadcast = FF:FF:FF:FF:FF:FF (all 48 bits 1). Unicast = first byte's last bit 0; multicast = first byte's last bit 1.

*MAC broadcast = FF:FF:FF:FF:FF:FF (सभी 48 bits 1)। Unicast = first byte का अंतिम bit 0; multicast = first byte का अंतिम bit 1।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

---
### Q6. Which addresses are used in an internet employing the TCP/IP protocols?

<span lang='hi'>TCP/IP protocols वाले internet में कौन-से addresses उपयोग होते हैं?</span>

- **(A)** Physical address and logical address
- **(B)** Port address
- **(C)** Specific address
- **(D)** All of these ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of these** — TCP/IP communication uses all four levels of addresses: physical (MAC), logical (IP), port, and specific (socket = MAC+IP+port) — depending on the layer.

*TCP/IP communication में चारों levels के addresses लगते हैं: physical (MAC), logical (IP), port, और specific (socket = MAC+IP+port) — layer के अनुसार।*

**★ Nukta (Key Point):** Forouzan's 4 address levels: Physical(48-bit MAC) at data link, IP(32-bit) at network, Port(16-bit) at transport, Specific (socket) at application.

*Forouzan की 4 address levels: Physical(48-bit MAC) data link पर, IP(32-bit) network पर, Port(16-bit) transport पर, Specific (socket) application पर।*

*[Source: LMT MCQ bank (Computer Communication Networks)] · Hard*

---
### Q7. What is the size (length) of a MAC address?

<span lang='hi'>MAC address का size (लंबाई) कितना होता है?</span>

- **(A)** 42 bits
- **(B)** 48 bits ✅ **(CORRECT)**
- **(C)** 24 bits
- **(D)** 36 bits

**✔ Correct Answer: (B) 48 bits** — A MAC (Media Access Control) address is 48 bits (6 bytes) long, usually written as 12 hex digits like 00:1A:2B:3C:4D:5E.

*MAC (Media Access Control) address 48 bits (6 bytes) का होता है, जिसे आमतौर पर 12 hex digits में लिखा जाता है — जैसे 00:1A:2B:3C:4D:5E।*

**★ Nukta (Key Point):** MAC = 48 bits (6 bytes / 12 hex digits). IPv4 = 32 bits, IPv6 = 128 bits, Port = 16 bits. Ye char sizes exam में बार-बार आते हैं।

*MAC = 48 bits (6 bytes / 12 hex digits)। IPv4 = 32 bits, IPv6 = 128 bits, Port = 16 bits। ये चार sizes exam में बार-बार आते हैं।*

*[Source: RPSC Programmer 2024 Paper-1 (official key) · also BCI_SCI ST-7 / Sanfoundry / InstrumentationTools] · Hard*

---
### Q8. An Ethernet destination address 0A-01-12-03-04-05 is a:

<span lang='hi'>Ethernet destination address 0A-01-12-03-04-05 कौन-सा address है?</span>

- **(A)** Unicast address ✅ **(CORRECT)**
- **(B)** Multicast address
- **(C)** Broadcast address
- **(D)** All of these

**✔ Correct Answer: (A) Unicast address** — The first byte 0A = 0000 1010 has its last bit (I/G bit) = 0, which marks a unicast address; multicast addresses have this bit = 1.

*पहला byte 0A = 0000 1010 का अंतिम bit (I/G bit) = 0 है, जो unicast address दर्शाता है; multicast में यह bit = 1 होता है।*

**★ Nukta (Key Point):** I/G bit (last bit of first octet): 0 = unicast, 1 = multicast. All-ones (FF:FF...) = broadcast.

*I/G bit (पहले octet का अंतिम bit): 0 = unicast, 1 = multicast। All-ones (FF:FF...) = broadcast।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

---
### Q9. Consider the statements: S1: Every computer or Internet device has a unique MAC address. S2: Every computer or Internet device has a unique IP address. Which is correct?

<span lang='hi'>कथन देखिए: S1: हर computer या Internet device का unique MAC address होता है। S2: हर computer या Internet device का unique IP address होता है। कौन-सा सही है?</span>

- **(A)** S1 is true and S2 is false ✅ **(CORRECT)**
- **(B)** Both S1 and S2 are false
- **(C)** S1 is false and S2 is true
- **(D)** Both S1 and S2 are true

**✔ Correct Answer: (A) S1 is true and S2 is false** — S1 is true — MAC addresses are globally unique (burned in by the manufacturer). S2 is false — IP addresses are logical and can be duplicated in different private networks (and change via DHCP).

*S1 सही है — MAC addresses globally unique होते हैं (manufacturer द्वारा burn किए गए)। S2 गलत है — IP addresses logical होते हैं और अलग-अलग private networks में duplicate हो सकते हैं (और DHCP से बदलते हैं)।*

**★ Nukta (Key Point):** MAC = permanent + globally unique. IP = logical + can repeat across private networks (NAT handles the overlap).

*MAC = स्थायी + globally unique। IP = logical + private networks में दोहराया जा सकता है (NAT overlap संभालता है)।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Hard*

---
### Q10. Which header field is rewritten (not removed) when an IP packet passes through a router?

<span lang='hi'>जब एक IP packet router से गुजरता है तो कौन-सा header field बदला (rewrite) जाता है?</span>

- **(A)** Source IP address
- **(B)** Destination IP address
- **(C)** MAC (Media Access Control) address ✅ **(CORRECT)**
- **(D)** Subnet mask

**✔ Correct Answer: (C) MAC (Media Access Control) address** — At each hop the router strips the old frame and writes NEW source and destination MAC addresses in the new frame; the IP addresses stay unchanged end-to-end.

*हर hop पर router पुराना frame हटाकर नए frame में नए source और destination MAC addresses लिखता है; IP addresses end-to-end अपरिवर्तित रहते हैंं।*

**★ Nukta (Key Point):** Per hop: MAC header changes. End-to-end: IP addresses stay the same. TTL also decrements (a router function).

*Per hop: MAC header बदलता है। End-to-end: IP addresses same रहते हैं। TTL भी घटता है (router का काम)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---

## Section B — IPv4 Addressing (Format, Classes & Special Addresses)

*32-bit dotted-decimal, octets, classes A-E, default masks, loopback/APIPA/private/special addresses, NAT.*

### Q11. The first octet of a Class A IP address ranges from:

<span lang='hi'>Class A IP address का पहला octet किस range में होता है?</span>

- **(A)** 0-127 ✅ **(CORRECT)**
- **(B)** 128-191
- **(C)** 192-223
- **(D)** 224-239

**✔ Correct Answer: (A) 0-127** — Class A covers first-octet values 0-127 (binary 0xxxxxxx) — though 0 and 127 are reserved, so usable Class A networks are 1-126.

*Class A में पहले octet के मान 0-127 (binary 0xxxxxxx) होते हैं — हालाँकि 0 और 127 reserved हैं, इसलिए उपयोगी Class A networks 1-126 हैं।*

**★ Nukta (Key Point):** Class ranges by first octet: A 0-127, B 128-191, C 192-223, D 224-239 (multicast), E 240-255 (experimental).

*पहले octet से Class ranges: A 0-127, B 128-191, C 192-223, D 224-239 (multicast), E 240-255 (experimental)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q12. Which class of IP address is used for multicasting?

<span lang='hi'>Multicasting के लिए किस class का IP address उपयोग होता है?</span>

- **(A)** Class A
- **(B)** Class B
- **(C)** Class C
- **(D)** Class D ✅ **(CORRECT)**

**✔ Correct Answer: (D) Class D** — Class D (224.0.0.0-239.255.255.255) is reserved for multicast group addresses — one packet is received by all members of the group.

*Class D (224.0.0.0-239.255.255.255) multicast group addresses के लिए reserved है — एक packet group के सभी सदस्यों को मिलता है।*

**★ Nukta (Key Point):** D = Multicast (one-to-group). E = Experimental (240-255). Broadcast (255.255.255.255) is separate.

*D = Multicast (one-to-group)। E = Experimental (240-255)। Broadcast (255.255.255.255) अलग है।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch) · also CN Topic Test-6] · Easy*

---
### Q13. Which class of address is reserved for experimental purposes?

<span lang='hi'>प्रायोगिक (experimental) उद्देश्यों के लिए किस class का address reserved है?</span>

- **(A)** Class C
- **(B)** Class B
- **(C)** Class D
- **(D)** Class E ✅ **(CORRECT)**

**✔ Correct Answer: (D) Class E** — Class E (240.0.0.0-255.255.255.255) is reserved for experimental/research use and is not used on the public Internet.

*Class E (240.0.0.0-255.255.255.255) प्रायोगिक/अनुसंधान उपयोग के लिए reserved है और public Internet पर उपयोग नहीं होता।*

**★ Nukta (Key Point):** Class E = Experimental (240-255). Remember: A-ny (0), B-128, C-192, D-224 (multicast), E-240 (experiment).

*Class E = Experimental (240-255)। याद रखें: A-ny (0), B-128, C-192, D-224 (multicast), E-240 (experiment)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q14. The IP address 127.0.0.1 is used for:

<span lang='hi'>IP address 127.0.0.1 किस काम में आती है?</span>

- **(A)** Broadcast
- **(B)** Class D network
- **(C)** Loopback testing ✅ **(CORRECT)**
- **(D)** APIPA

**✔ Correct Answer: (C) Loopback testing** — 127.0.0.1 is the loopback address — a host sends packets to it to test its own TCP/IP stack and NIC software path without leaving the machine.

*127.0.0.1 loopback address है — अपने TCP/IP stack को परखने के लिए host इसे packet भेजता है, बिना machine से बाहर गए।*

**★ Nukta (Key Point):** Whole 127.0.0.0/8 block = loopback. `ping 127.0.0.1` tests the local IP stack.

*पूरा 127.0.0.0/8 block = loopback। `ping 127.0.0.1` से local IP stack जाँचते हैं।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) · also CN Topic Test-03 / CN Topic Test-04] · Easy*

---
### Q15. What is the maximum number of unique IPv4 addresses?

<span lang='hi'>Unique IPv4 addresses की अधिकतम संख्या कितनी है?</span>

- **(A)** 2^16
- **(B)** 2^24
- **(C)** 2^32 ✅ **(CORRECT)**
- **(D)** 2^64

**✔ Correct Answer: (C) 2^32** — With 32 bits there are 2^32 (about 4.29 billion) possible IPv4 addresses — which is why IPv6 (2^128) was introduced.

*32 bits के साथ 2^32 (लगभग 4.29 billion) संभावित IPv4 addresses हैं — इसीलिए IPv6 (2^128) लाया गया।*

**★ Nukta (Key Point):** 2^32 ≈ 4.29 billion IPv4 addresses. IPv6 = 2^128 ≈ 3.4 × 10^38.

*2^32 ≈ 4.29 billion IPv4 addresses। IPv6 = 2^128 ≈ 3.4 × 10^38।*

*[Source: IP Addressing quiz (Studocu bank, with keys)] · Medium*

---
### Q16. An IPv4 address is divided into how many parts?

<span lang='hi'>IPv4 address कितने भागों में बाँटा जाता है?</span>

- **(A)** 2 ✅ **(CORRECT)**
- **(B)** 3
- **(C)** 4
- **(D)** 5

**✔ Correct Answer: (A) 2** — An IPv4 address has two parts: the network (prefix) part and the host (interface) part — the boundary is set by the subnet mask.

*IPv4 address के दो भाग होते हैं: network (prefix) भाग और host (interface) भाग — इनकी सीमा subnet mask तय करता है।*

**★ Nukta (Key Point):** 2 parts = network + host. IPv4 CLASSIC division; subnetting borrows bits from host to make sub-networks.

*2 parts = network + host। Subnetting में host bits से bits उधार लेकर sub-networks बनते हैं।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

---
### Q17. The first octet of a Class B IP address falls between:

<span lang='hi'>Class B IP address का पहला octet किस range में आता है?</span>

- **(A)** 0-127
- **(B)** 128-191 ✅ **(CORRECT)**
- **(C)** 192-223
- **(D)** 224-239

**✔ Correct Answer: (B) 128-191** — Class B uses first-octet values 128-191 (binary 10xxxxxx) with a default mask of 255.255.0.0.

*Class B में पहले octet के मान 128-191 (binary 10xxxxxx) होते हैं और default mask 255.255.0.0 होता है।*

**★ Nukta (Key Point):** B = 128-191 (default /16). Trick: A starts 0, B starts 128, C starts 192, D starts 224, E starts 240.

*B = 128-191 (default /16)। Trick: A 0 से, B 128 से, C 192 से, D 224 से, E 240 से।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q18. How many bits are used for the network portion in a Class C IP address?

<span lang='hi'>Class C IP address में network भाग के लिए कितने bits उपयोग होते हैं?</span>

- **(A)** 8
- **(B)** 16
- **(C)** 24 ✅ **(CORRECT)**
- **(D)** 32

**✔ Correct Answer: (C) 24** — Class C has a default mask of 255.255.255.0 — the first 24 bits are the network portion, leaving 8 bits for hosts (254 usable).

*Class C का default mask 255.255.255.0 होता है — पहले 24 bits network भाग होते हैं, 8 bits hosts के लिए बचते हैं (254 उपयोगी)।*

**★ Nukta (Key Point):** Class C = /24 network (24 bits) + 8 host bits. Class B = /16, Class A = /8.

*Class C = /24 network (24 bits) + 8 host bits। Class B = /16, Class A = /8।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Medium*

---
### Q19. Which IP address class provides the largest number of hosts per network?

<span lang='hi'>कौन-सी IP address class प्रति network सबसे अधिक hosts देती है?</span>

- **(A)** Class A ✅ **(CORRECT)**
- **(B)** Class B
- **(C)** Class C
- **(D)** Class D

**✔ Correct Answer: (A) Class A** — Class A reserves 7 bits for hosts (2^24 − 2 ≈ 16.7 million hosts per network) — the largest of the classes.

*Class A में hosts के लिए 24 bits होते हैं (2^24 − 2 ≈ 16.7 million hosts प्रति network) — सबसे बड़ी class।*

**★ Nukta (Key Point):** Hosts per class: A = 2^24−2, B = 2^16−2 (65,534), C = 2^8−2 (254). D/E have no hosts (multicast/experimental).

*प्रति class hosts: A = 2^24−2, B = 2^16−2 (65,534), C = 2^8−2 (254)। D/E में hosts नहीं (multicast/experimental)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q20. Which class of IP addresses supports 65,534 hosts per network?

<span lang='hi'>कौन-सी IP address class प्रति network 65,534 hosts support करती है?</span>

- **(A)** Class A
- **(B)** Class B ✅ **(CORRECT)**
- **(C)** Class C
- **(D)** Class D

**✔ Correct Answer: (B) Class B** — Class B has 16 host bits: 2^16 − 2 = 65,534 usable hosts per network (minus network and broadcast addresses).

*Class B में 16 host bits होती हैं: 2^16 − 2 = 65,534 उपयोगी hosts प्रति network (network और broadcast address घटाने के बाद)।*

**★ Nukta (Key Point):** 65,534 = 2^16−2 = Class B hosts. 254 = 2^8−2 = Class C. 16,777,214 = 2^24−2 = Class A.

*65,534 = 2^16−2 = Class B hosts। 254 = 2^8−2 = Class C। 16,777,214 = 2^24−2 = Class A।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q21. What is the maximum number of IP addresses in a Class C network?

<span lang='hi'>Class C network में IP addresses की अधिकतम संख्या कितनी होती है?</span>

- **(A)** 254
- **(B)** 256 ✅ **(CORRECT)**
- **(C)** 1024
- **(D)** 65536

**✔ Correct Answer: (B) 256** — A Class C network has 8 host bits, so 2^8 = 256 total addresses — of which 254 are usable hosts (one network ID + one broadcast address are reserved).

*Class C network में 8 host bits होती हैं, इसलिए 2^8 = कुल 256 addresses — जिनमें से 254 उपयोगी hosts हैं (एक network ID + एक broadcast address reserved रहते हैं)।*

**★ Nukta (Key Point):** Total addresses = 2^host-bits. Usable hosts = total − 2. Exam asks BOTH — read 'addresses' vs 'hosts' carefully!

*कुल addresses = 2^host-bits। उपयोगी hosts = कुल − 2। Exam दोनों पूछता है — 'addresses' और 'hosts' में ध्यान से फर्क पढ़ें!*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

---
### Q22. Which of the following is a Class D address?

<span lang='hi'>निम्न में से कौन-सा Class D address है?</span>

- **(A)** 224.1.1.1
- **(B)** 233.0.0.10
- **(C)** 239.5.5.5
- **(D)** All of the above ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the above** — Class D covers 224.0.0.0-239.255.255.255 — all three addresses (224.x, 233.x, 239.x) fall in this multicast range.

*Class D की range 224.0.0.0-239.255.255.255 है — तीनों addresses (224.x, 233.x, 239.x) इसी multicast range में आती हैं।*

**★ Nukta (Key Point):** Class D = 224-239 (multicast). Any address in this range is Class D — exam often gives mixed octets like these.

*Class D = 224-239 (multicast)। इस range का कोई भी address Class D है — exam में अक्सर ऐसे मिश्रित octets दिए जाते हैं।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

---
### Q23. Which IP address is reserved for future use and experimental purposes?

<span lang='hi'>कौन-सा IP address भविष्य के उपयोग और प्रायोगिक उद्देश्यों के लिए reserved है?</span>

- **(A)** 127.0.0.1
- **(B)** 224.0.0.1
- **(C)** 240.0.0.0 ✅ **(CORRECT)**
- **(D)** 192.168.0.1

**✔ Correct Answer: (C) 240.0.0.0** — 240.0.0.0 is the start of the Class E block (240-255) reserved for future/experimental use.

*240.0.0.0, Class E block (240-255) की शुरुआत है जो भविष्य/प्रायोगिक उपयोग के लिए reserved है।*

**★ Nukta (Key Point):** 240.0.0.0/4 = Class E = future use. 127.x = loopback, 224.x = multicast, 192.168.x = private.

*240.0.0.0/4 = Class E = future use। 127.x = loopback, 224.x = multicast, 192.168.x = private।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q24. Which of the following is a Class B host address?

<span lang='hi'>निम्न में से कौन-सा Class B host address है?</span>

- **(A)** 230.0.0.0
- **(B)** 130.4.5.6 ✅ **(CORRECT)**
- **(C)** 230.7.6.5
- **(D)** 30.4.5.6

**✔ Correct Answer: (B) 130.4.5.6** — 130.4.5.6 has first octet 130 (in 128-191) so it is Class B — and it is a valid host address in that block.

*130.4.5.6 का पहला octet 130 (128-191 में) है इसलिए यह Class B है — और यह उस block का वैध host address है।*

**★ Nukta (Key Point):** 230.x = Class D (multicast). 30.x = Class A. 130.x = Class B — look at the FIRST octet.

*230.x = Class D (multicast)। 30.x = Class A। 130.x = Class B — पहले octet को देखें।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q25. Which of the following is a valid IPv4 address?

<span lang='hi'>निम्न में से कौन-सा वैध IPv4 address है?</span>

- **(A)** 192.256.1.1
- **(B)** 172.31.0.1 ✅ **(CORRECT)**
- **(C)** 300.100.50.25
- **(D)** 500.10.5.2

**✔ Correct Answer: (B) 172.31.0.1** — Each octet must be 0-255; only 172.31.0.1 has all octets in range (the others use 256, 300 or 500).

*हर octet 0-255 के बीच होना चाहिए; केवल 172.31.0.1 के सभी octets range में हैं (बाकियों में 256, 300 या 500 हैं)।*

**★ Nukta (Key Point):** Octet range check: 0-255 only. 172.16-172.31.x is also the private Class B range (bonus!).

*Octet range check: केवल 0-255। 172.16-172.31.x private Class B range भी है (bonus!)।*

*[Source: 30 important CN MCQs (Medium blog bank)] · Medium*

---
### Q26. The address 255.255.255.255 is used for:

<span lang='hi'>Address 255.255.255.255 किसके लिए उपयोग होती है?</span>

- **(A)** A public IP
- **(B)** A default gateway
- **(C)** A network ID
- **(D)** Broadcast to all nodes ✅ **(CORRECT)**

**✔ Correct Answer: (D) Broadcast to all nodes** — 255.255.255.255 is the limited (local) broadcast address — the packet is delivered to all devices on the local network segment.

*255.255.255.255 limited (local) broadcast address है — packet local network segment के सभी devices तक पहुँचता है।*

**★ Nukta (Key Point):** Limited broadcast = 255.255.255.255 (this network only). Directed broadcast = last address of a subnet (e.g., 192.168.1.255).

*Limited broadcast = 255.255.255.255 (केवल यह network)। Directed broadcast = subnet का अंतिम address (जैसे 192.168.1.255)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q27. What is the purpose of the reserved IP address 0.0.0.0?

<span lang='hi'>Reserved IP address 0.0.0.0 का उद्देश्य क्या है?</span>

- **(A)** Default gateway
- **(B)** Used for DHCP servers
- **(C)** Default route or 'any network' ✅ **(CORRECT)**
- **(D)** Multicast address

**✔ Correct Answer: (C) Default route or 'any network'** — 0.0.0.0 means 'this host on this network' as a source (e.g., during boot) and, as a destination with mask /0, it is the default route (any network).

*0.0.0.0 का अर्थ है 'इस network पर यह host' (source के रूप में, जैसे boot के दौरान), और /0 mask के साथ destination के रूप में यह default route (कोई भी network) है।*

**★ Nukta (Key Point):** 0.0.0.0/0 = default route (gateway of last resort). As source = 'not yet assigned an IP'.

*0.0.0.0/0 = default route (gateway of last resort)। Source के रूप में = 'अभी IP नहीं मिला'।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q28. The IP address used by a host's packets as the source while the host is being booted (before it gets an IP) is:

<span lang='hi'>जब host boot हो रहा होता है (IP मिलने से पहले) तो उसके packets का source IP address कौन-सा होता है?</span>

- **(A)** 0.0.0.0 ✅ **(CORRECT)**
- **(B)** 1.0.0.0
- **(C)** 1.1.1.1
- **(D)** 255.255.255.255

**✔ Correct Answer: (A) 0.0.0.0** — Before receiving an IP (e.g., in DHCP DISCOVER), the host uses 0.0.0.0 as the source address to mean 'this host — no IP yet'.

*IP मिलने से पहले (जैसे DHCP DISCOVER में) host source address के रूप में 0.0.0.0 उपयोग करता है — अर्थ 'यह host — अभी IP नहीं'।*

**★ Nukta (Key Point):** Boot/DHCP phase: source 0.0.0.0, destination 255.255.255.255 (broadcast). Ye DHCP handshake ka classic pattern hai.

*Boot/DHCP चरण: source 0.0.0.0, destination 255.255.255.255 (broadcast)। यह DHCP handshake का classic pattern है।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q29. What is the range of addresses for APIPA (Automatic Private IP Addressing)?

<span lang='hi'>APIPA (Automatic Private IP Addressing) की address range क्या है?</span>

- **(A)** 169.254.0.1 to 169.254.255.254 ✅ **(CORRECT)**
- **(B)** 10.0.0.0 to 10.255.255.255
- **(C)** 192.168.0.0 to 192.168.255.255
- **(D)** 172.16.0.0 to 172.31.255.255

**✔ Correct Answer: (A) 169.254.0.1 to 169.254.255.254** — When DHCP fails, Windows hosts self-assign an APIPA address in 169.254.0.1-169.254.255.254 (link-local).

*जब DHCP fail होता है, तो Windows hosts स्वयं को 169.254.0.1-169.254.255.254 (link-local) में APIPA address देते हैं।*

**★ Nukta (Key Point):** APIPA = 169.254.x.x (link-local, auto). Private blocks: 10.x / 172.16-31.x / 192.168.x (RFC 1918).

*APIPA = 169.254.x.x (link-local, auto)। Private blocks: 10.x / 172.16-31.x / 192.168.x (RFC 1918)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q30. Which IP address can be used in a WAN (public network)?

<span lang='hi'>कौन-सा IP address WAN (public network) में उपयोग हो सकता है?</span>

- **(A)** 256.0.0.1
- **(B)** 172.16.0.10
- **(C)** 15.1.5.6 ✅ **(CORRECT)**
- **(D)** 127.256.0.118

**✔ Correct Answer: (C) 15.1.5.6** — 15.1.5.6 is a valid PUBLIC address (Class A). 172.16.0.10 is private (RFC 1918), 256.0.0.1 and 127.256.0.118 are invalid octets.

*15.1.5.6 एक वैध PUBLIC address (Class A) है। 172.16.0.10 private (RFC 1918) है, 256.0.0.1 और 127.256.0.118 अवैध octets हैं।*

**★ Nukta (Key Point):** WAN needs public IPs. Private ranges (10.x, 172.16-31.x, 192.168.x) + loopback + invalid octets — sab hatana seekho.

*WAN के लिए public IPs चाहिए। Private ranges (10.x, 172.16-31.x, 192.168.x) + loopback + invalid octets — सब हटाना सीखें।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q31. Each computer connected to the internet must:

<span lang='hi'>Internet से जुड़े प्रत्येक computer को क्या होना चाहिए?</span>

- **(A)** Be an IBM PC
- **(B)** Have a unique IP address ✅ **(CORRECT)**
- **(C)** Be internet compatible
- **(D)** Have a modem connection

**✔ Correct Answer: (B) Have a unique IP address** — Every device on the Internet needs a unique IP address so that packets can be routed to it uniquely.

*Internet पर हर device को unique IP address चाहिए ताकि packets उस तक uniquely route हो सकें।*

**★ Nukta (Key Point):** Unique IP = the fundamental Internet requirement (IPv4 32-bit or IPv6 128-bit).

*Unique IP = Internet की मूल आवश्यकता (IPv4 32-bit या IPv6 128-bit)।*

*[Source: SSC CGL Internet & Networking (via EduRev bank)] · Medium*

---
### Q32. Which organization is responsible for managing IP address allocation globally?

<span lang='hi'>वैश्विक स्तर पर IP address allocation का प्रबंधन कौन-सा संगठन करता है?</span>

- **(A)** IEEE
- **(B)** ICANN ✅ **(CORRECT)**
- **(C)** IETF
- **(D)** ISO

**✔ Correct Answer: (B) ICANN** — ICANN (Internet Corporation for Assigned Names and Numbers) — through IANA/RIRs — coordinates global IP address and domain-name allocation.

*ICANN (Internet Corporation for Assigned Names and Numbers) — IANA/RIRs के माध्यम से — वैश्विक IP address और domain-name allocation का समन्वय करता है।*

**★ Nukta (Key Point):** ICANN/IANA = addresses + names. IETF = protocols (RFCs). IEEE = LAN standards (802.x). ISO = OSI model.

*ICANN/IANA = addresses + names। IETF = protocols (RFCs)। IEEE = LAN standards (802.x)। ISO = OSI model।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q33. What is the size of each octet in an IPv4 address?

<span lang='hi'>IPv4 address के प्रत्येक octet का size कितना होता है?</span>

- **(A)** 4 bits
- **(B)** 8 bits ✅ **(CORRECT)**
- **(C)** 16 bits
- **(D)** 32 bits

**✔ Correct Answer: (B) 8 bits** — An IPv4 address has 4 octets and each octet is 8 bits — 4 × 8 = 32 bits total.

*IPv4 address में 4 octets होते हैं और हर octet 8 bits का होता है — 4 × 8 = कुल 32 bits।*

**★ Nukta (Key Point):** Octet = 8 bits (0-255 in decimal). 4 octets = 32 bits = dotted-decimal notation.

*Octet = 8 bits (decimal में 0-255)। 4 octets = 32 bits = dotted-decimal notation।*

*[Source: IP Addressing quiz (Studocu bank, with keys)] · Hard*

---
### Q34. An IPv4 address is of size:

<span lang='hi'>IPv4 address कितने bits का होता है?</span>

- **(A)** 8 bit
- **(B)** 16 bit
- **(C)** 32 bit ✅ **(CORRECT)**
- **(D)** 64 bit

**✔ Correct Answer: (C) 32 bit** — IPv4 uses 32-bit addresses written in dotted-decimal as four 0-255 octets (e.g., 192.168.1.1).

*IPv4 में 32-bit addresses होते हैं जिन्हें dotted-decimal में चार 0-255 octets के रूप में लिखा जाता है (जैसे 192.168.1.1)।*

**★ Nukta (Key Point):** Size shortcut: MAC 48, IPv4 32, IPv6 128, Port 16 (bits).

*Size shortcut: MAC 48, IPv4 32, IPv6 128, Port 16 (bits)।*

*[Source: Networking MCQ bank (MQuestions blog)] · Hard*

---
### Q35. If the number of networks and number of hosts in Class B are 2^m and (2^n − 2) respectively, then the relation between m and n is:

<span lang='hi'>यदि Class B में networks और hosts की संख्या क्रमशः 2^m और (2^n − 2) है, तो m और n के बीच क्या संबंध है?</span>

- **(A)** 3m = 2n
- **(B)** 7m = 8n
- **(C)** 8m = 7n ✅ **(CORRECT)**
- **(D)** 2m = 3n

**✔ Correct Answer: (C) 8m = 7n** — Class B has 2^14 networks (m = 14) and 2^16 − 2 hosts (n = 16): 8 × 14 = 7 × 16 = 112, so 8m = 7n.

*Class B में 2^14 networks (m = 14) और 2^16 − 2 hosts (n = 16) होते हैं: 8 × 14 = 7 × 16 = 112, अतः 8m = 7n।*

**★ Nukta (Key Point):** Class B classful counts: networks 2^14, hosts 2^16−2. So m=14, n=16 → 8m=7n. (Class A: 2^7 nets, 2^24−2 hosts; Class C: 2^21 nets, 2^8−2 hosts.)

*Class B classful counts: networks 2^14, hosts 2^16−2। अतः m=14, n=16 → 8m=7n। (Class A: 2^7 nets, 2^24−2 hosts; Class C: 2^21 nets, 2^8−2 hosts।)*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q36. Which subnet mask is the default for the Class B IP address range?

<span lang='hi'>Class B IP address range के लिए default subnet mask कौन-सा है?</span>

- **(A)** 255.255.255.0
- **(B)** 255.0.0.0
- **(C)** 255.255.0.0 ✅ **(CORRECT)**
- **(D)** 255.255.255.255

**✔ Correct Answer: (C) 255.255.0.0** — Class B uses a default mask of 255.255.0.0 (/16) — first 16 bits network, last 16 bits host.

*Class B का default mask 255.255.0.0 (/16) होता है — पहले 16 bits network, अंतिम 16 bits host।*

**★ Nukta (Key Point):** Default masks: A 255.0.0.0 (/8), B 255.255.0.0 (/16), C 255.255.255.0 (/24).

*Default masks: A 255.0.0.0 (/8), B 255.255.0.0 (/16), C 255.255.255.0 (/24)।*

*[Source: 30 important CN MCQs (Medium blog bank) · also CN Topic Test-6] · Hard*

---
### Q37. What is the primary purpose of NAT (Network Address Translation) in IPv4?

<span lang='hi'>IPv4 में NAT (Network Address Translation) का मुख्य उद्देश्य क्या है?</span>

- **(A)** To map private IP addresses to a public IP address ✅ **(CORRECT)**
- **(B)** To increase the security of IP addresses
- **(C)** To facilitate communication between different subnets
- **(D)** All of the above

**✔ Correct Answer: (A) To map private IP addresses to a public IP address** — NAT translates private (RFC 1918) addresses to a public IP (and back) at the router, so many private hosts can share one public address.

*NAT router पर private (RFC 1918) addresses को public IP में (और वापस) बदलता है, जिससे कई private hosts एक public address share कर सकें।*

**★ Nukta (Key Point):** NAT core = private→public mapping. Bonus effects: hides internal IPs (security), helps address exhaustion. Some banks key 'All of these' — the PRIMARY purpose is the mapping.

*NAT का core = private→public mapping। अतिरिक्त प्रभाव: internal IPs छिपती हैं (security), address exhaustion कम होती है। कुछ banks 'All of these' key करते हैं — मुख्य उद्देश्य mapping ही है।*

*[Source: IP Addressing quiz (Studocu bank, with keys)] · Hard*

---
### Q38. A host is connected to a department network which is part of a university network; the university network in turn is part of the Internet. Which is the LARGEST network among these?

<span lang='hi'>एक host department network से जुड़ा है जो university network का हिस्सा है; university network बदले में Internet का हिस्सा है। इनमें सबसे बड़ा network कौन-सा है?</span>

- **(A)** The subnet to which the host belongs
- **(B)** The department network
- **(C)** The university network
- **(D)** The Internet ✅ **(CORRECT)**

**✔ Correct Answer: (D) The Internet** — The Internet is the inter-network of all these — a network of networks — so it is the largest in the hierarchy.

*Internet इन सब का inter-network — networks का network — है, इसलिए यह पदानुक्रम (hierarchy) में सबसे बड़ा है।*

**★ Nukta (Key Point):** Hierarchy: subnet ⊂ department LAN ⊂ university CAN ⊂ Internet. Addressing mirrors this (network prefix lengths).

*पदानुक्रम: subnet ⊂ department LAN ⊂ university CAN ⊂ Internet। Addressing भी इसी तरह (network prefix lengths)।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Hard*

---
### Q39. Which IP address type is used to communicate with all devices on a subnet?

<span lang='hi'>Subnet के सभी devices से संवाद करने के लिए किस type का IP address उपयोग होता है?</span>

- **(A)** Unicast
- **(B)** Broadcast ✅ **(CORRECT)**
- **(C)** Multicast
- **(D)** Anycast

**✔ Correct Answer: (B) Broadcast** — Broadcast (e.g., 192.168.1.255 for a /24) delivers a packet to every device on the subnet.

*Broadcast (जैसे /24 के लिए 192.168.1.255) packet को subnet के हर device तक पहुँचाता है।*

**★ Nukta (Key Point):** IP communication types: Unicast (one-to-one), Broadcast (one-to-all-on-subnet), Multicast (one-to-group), Anycast (one-to-nearest).

*IP communication types: Unicast (one-to-one), Broadcast (one-to-all-on-subnet), Multicast (one-to-group), Anycast (one-to-nearest)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q40. Which of the following is NOT a valid private (RFC-1918) IP address?

<span lang='hi'>निम्न में से कौन-सा वैध private (RFC-1918) IP पता नहीं है?</span>

- **(A)** 10.0.0.1
- **(B)** 172.16.5.4
- **(C)** 192.168.1.10
- **(D)** 11.0.0.1 / 11.0.0.1 ✅ **(CORRECT)**

**✔ Correct Answer: (D) 11.0.0.1** — RFC-1918 के private blocks हैं — 10.0.0.0/8, 172.16.0.0/12 और 192.168.0.0/16. 11.0.0.1 इनमें से किसी भी block में नहीं आता, इसलिए यह public IP है — private नहीं.

*RFC-1918 के private blocks हैं — 10.0.0.0/8, 172.16.0.0/12 और 192.168.0.0/16. 11.0.0.1 इनमें से किसी भी block में नहीं आता, इसलिए यह public IP है — private नहीं.*

**★ Nukta (Key Point):** Private ranges याद रखो: 10.x (Class A), 172.16–172.31.x (Class B), 192.168.x (Class C) — बाकी सब public.

*Private ranges याद रखो: 10.x (Class A), 172.16–172.31.x (Class B), 192.168.x (Class C) — बाकी सब public.*

*[Source: CN Topic Test 5.pdf] · Hard*

---
### Q41. In the IPv4 addressing format, the number of networks allowed under Class C addresses is:

<span lang='hi'>IPv4 addressing में Class C addresses के अंतर्गत कुल कितने networks allowed हैं?</span>

- **(A)** 2¹⁴ / 2¹⁴
- **(B)** 2⁷ / 2⁷
- **(C)** 2²¹ / 2²¹ ✅ **(CORRECT)**
- **(D)** 2²⁴ / 2²⁴

**✔ Correct Answer: (C) 2²¹** — Class C mein network ID ke liye 24 bits hote hain, par pehle 3 bits fixed (110) hain — isliye 2⁴⁻³ = 2²¹ networks bante hain (GATE 2012 official key).

*Class C में network ID 24 bits की, पर पहले 3 bits fix (110) — इसलिए 2⁴⁻³ = 2²¹ networks (GATE 2012 official key).*

**★ Nukta (Key Point):** 2²⁴ poore network field ka size hai (fixed 3 bits bhool kar); 2⁷ aur 2¹⁴ host/other class ke figures hain.

*2²⁴ poora field (3 fixed bits bhool kar); 2⁷/2¹⁴ doosre figures hain.*

*[Source: GATE CS 2012] · Hard*

---
### Q42. Which one of the following CIDR prefixes exactly represents the range of IP addresses 10.12.2.0 to 10.12.3.255?

<span lang='hi'>CIDR prefix में से कौन-सा 10.12.2.0 से 10.12.3.255 तक की IP range को ठीक-ठीक दर्शाता है?</span>

- **(A)** 10.12.2.0/24 / 10.12.2.0/24
- **(B)** 10.12.2.0/23 / 10.12.2.0/23 ✅ **(CORRECT)**
- **(C)** 10.12.0.0/22 / 10.12.0.0/22
- **(D)** 10.12.3.0/25 / 10.12.3.0/25

**✔ Correct Answer: (B) 10.12.2.0/23** — Range mein 512 addresses hain (2⁹) aur 10.12.2.0 9 host-bits ke liye properly aligned hai — /32−9 = /23, yaani 10.12.2.0/23.

*Range में 512 addresses (2⁹) और 10.12.2.0 alignment सही — /32−9 = /23, यानी 10.12.2.0/23.*

**★ Nukta (Key Point):** /24 sirf 2.0–2.255 cover karta hai; /22 bahut bada (4 blocks); /25 aadha block.

*/24 sirf 2.x; /22 bahut bada; /25 aadha block.*

*[Source: GATE CS 2024 Set-2] · Hard*

---
### Q43. Three machines M, N and P have IP addresses 100.10.5.2, 100.10.5.5 and 100.10.5.6 respectively. The subnet mask is set to 255.255.255.252 for all three machines. Which one of the following is true?

<span lang='hi'>तीन machines M, N, P के IP addresses क्रमशः 100.10.5.2, 100.10.5.5 और 100.10.5.6 हैं। तीनों का subnet mask 255.255.255.252 है। निम्न में से कौन-सा कथन सही है?</span>

- **(A)** All three belong to the same subnet / तीनों एक ही subnet में हैं
- **(B)** M and N belong to the same subnet / M और N एक ही subnet में हैं
- **(C)** N and P belong to the same subnet / N और P एक ही subnet में हैं ✅ **(CORRECT)**
- **(D)** M and P belong to the same subnet / M और P एक ही subnet में हैं

**✔ Correct Answer: (C) N and P belong to the same subnet** — Mask /30 ke 4-address blocks banata hai: 100.10.5.0–.3, .4–.7; M (.2) pehle block mein, N (.5) aur P (.6) doosre block mein — N aur P ek hi subnet ke hain.

*Mask /30 se 4-address blocks: .0–.3, .4–.7; M (.2) पहले में, N (.5), P (.6) दूसरे में — N और P एक ही subnet के।*

**★ Nukta (Key Point):** Adjacent numbers ka matlab same subnet nahi — /30 par block boundary .3/.4 par hoti hai.

*पास के numbers = एक subnet नहीं; /30 में boundary .3/.4 पर है।*

*[Source: GATE CS 2019] · Hard*

---

## Section C — Subnetting & CIDR

*Subnet masks, /n notation, usable hosts & subnet counts, block arithmetic — basic to advanced calculations.*

### Q44. A subnet /30 is MOST commonly used for:

<span lang='hi'>Subnet /30 सबसे अधिक किसके लिए उपयोग होती है?</span>

- **(A)** Two-host networks ✅ **(CORRECT)**
- **(B)** Four-host networks
- **(C)** Loopback only
- **(D)** VPN networks

**✔ Correct Answer: (A) Two-host networks** — A /30 gives exactly 2 usable hosts — the classic choice for point-to-point links between two routers.

*/30 में ठीक 2 उपयोगी hosts मिलते हैं — दो routers के बीच point-to-point links के लिए classic विकल्प।*

**★ Nukta (Key Point):** Link between 2 routers = /30. WAN links ya tunnel endpoints ke liye standard.

*2 routers के बीच link = /30। WAN links या tunnel endpoints के लिए standard।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

---
### Q45. Which part of the IP address 172.16.5.4/24 identifies the network?

<span lang='hi'>IP address 172.16.5.4/24 का कौन-सा भाग network पहचानता है?</span>

- **(A)** 172
- **(B)** 172.16
- **(C)** 172.16.5 ✅ **(CORRECT)**
- **(D)** 172.16.5.4

**✔ Correct Answer: (C) 172.16.5** — /24 keeps the first 24 bits (three octets: 172.16.5) as the network part; .4 is the host part.

*/24 में पहले 24 bits (तीन octets: 172.16.5) network भाग होते हैं; .4 host भाग है।*

**★ Nukta (Key Point):** Visual trick: /8 → 1 octet, /16 → 2 octets, /24 → 3 octets network.

*Visual trick: /8 → 1 octet, /16 → 2 octets, /24 → 3 octets network।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q46. A network ID (address with all host bits = 0) cannot be assigned to:

<span lang='hi'>Network ID (सभी host bits = 0 वाला address) किसे assign नहीं किया जा सकता?</span>

- **(A)** A router
- **(B)** A switch
- **(C)** A host device ✅ **(CORRECT)**
- **(D)** The entire network

**✔ Correct Answer: (C) A host device** — The network ID identifies the network itself and is reserved — like the broadcast address, it is never assigned to a host device's interface.

*Network ID स्वयं network की पहचान करता है और reserved होता है — broadcast address की तरह, इसे कभी किसी host device के interface पर assign नहीं किया जाता।*

**★ Nukta (Key Point):** Network ID = first address of the block (host bits 0). Broadcast = last (host bits 1). Both reserved; usable hosts = middle addresses only.

*Network ID = block का पहला address (host bits 0)। Broadcast = अंतिम (host bits 1)। दोनों reserved; उपयोगी hosts = बीच के addresses ही।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q47. A host has IP 192.168.10.45/27. Which statement is TRUE?

<span lang='hi'>एक host का IP 192.168.10.45/27 है। कौन-सा कथन सही है?</span>

- **(A)** Broadcast address = 192.168.10.63
- **(B)** Network ID = 192.168.10.32
- **(C)** First usable host = 192.168.10.33
- **(D)** All of the above ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the above** — /27 = block size 32: the subnet is .32-.63 — network .32, first host .33, broadcast .63. All three statements are true.

*/27 = block size 32: subnet .32-.63 है — network .32, पहला host .33, broadcast .63। तीनों कथन सही हैं।*

**★ Nukta (Key Point):** Block arithmetic: 45 ÷ 32 → block 32. Network = block start; broadcast = next block − 1.

*Block arithmetic: 45 ÷ 32 → block 32। Network = block की शुरुआत; broadcast = अगला block − 1।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) · also CN Topic Test-03] · Medium*

---
### Q48. What does the term 'subnetting' refer to in networking?

<span lang='hi'>Networking में 'subnetting' शब्द का क्या अर्थ है?</span>

- **(A)** Dividing a large network into smaller logical networks ✅ **(CORRECT)**
- **(B)** Allocating IP addresses to devices
- **(C)** Filtering network traffic
- **(D)** Assigning MAC addresses

**✔ Correct Answer: (A) Dividing a large network into smaller logical networks** — Subnetting divides one large network into several smaller sub-networks by borrowing bits from the host part of the address.

*Subnetting address के host भाग से bits उधार लेकर एक बड़े network को कई छोटे sub-networks में बाँटती है।*

**★ Nukta (Key Point):** Subnetting = big network → smaller networks (better performance, security, less broadcast).

*Subnetting = बड़ा network → छोटे networks (बेहतर performance, security, कम broadcast)।*

*[Source: 30 important CN MCQs (Medium blog bank) · also CN Topic Test-03] · Hard*

---
### Q49. When IPv4 addressing is manually configured, which property identifies the network and host portions of the address?

<span lang='hi'>जब IPv4 addressing manually configure होती है, तो कौन-सा property address के network और host भाग पहचानती है?</span>

- **(A)** DNS server address
- **(B)** Subnet mask ✅ **(CORRECT)**
- **(C)** Default gateway
- **(D)** DHCP server address

**✔ Correct Answer: (B) Subnet mask** — The subnet mask (e.g., 255.255.255.0) marks which bits of the IP address are the network part (1s) and which are the host part (0s).

*Subnet mask (जैसे 255.255.255.0) बताता है कि IP address के कौन-से bits network भाग (1s) हैं और कौन-से host भाग (0s)।*

**★ Nukta (Key Point):** Mask = boundary between network and host. /24 = 255.255.255.0 = 24 network bits + 8 host bits.

*Mask = network और host के बीच सीमा। /24 = 255.255.255.0 = 24 network bits + 8 host bits।*

*[Source: IP Addressing quiz (Studocu bank, with keys)] · Hard*

---
### Q50. In a subnet mask, the number of 1's represents:

<span lang='hi'>Subnet mask में 1's की संख्या किसका प्रतिनिधित्व करती है?</span>

- **(A)** Host bits
- **(B)** Network bits ✅ **(CORRECT)**
- **(C)** Broadcast bits
- **(D)** Subnet bits

**✔ Correct Answer: (B) Network bits** — In a subnet mask the 1-bits mark the network (and subnet) portion; the 0-bits mark the host portion.

*Subnet mask में 1-bits network (और subnet) भाग दर्शाते हैं; 0-bits host भाग दर्शाते हैं।*

**★ Nukta (Key Point):** Count of 1s = prefix length (/n). Example: 255.255.255.0 has 24 ones = /24.

*1s की गिनती = prefix length (/n)। उदाहरण: 255.255.255.0 में 24 ones = /24।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q51. In CIDR notation, what does /16 represent?

<span lang='hi'>CIDR notation में /16 का क्या अर्थ है?</span>

- **(A)** 16 host bits
- **(B)** 16 network bits ✅ **(CORRECT)**
- **(C)** 16 bytes
- **(D)** 16 subnets

**✔ Correct Answer: (B) 16 network bits** — The number after the slash is the count of network (prefix) bits — /16 means the first 16 bits identify the network.

*Slash के बाद की संख्या network (prefix) bits की गिनती है — /16 का अर्थ पहले 16 bits network पहचानते हैं।*

**★ Nukta (Key Point):** CIDR /n = n network bits. Host bits = 32 − n. /16 → 2^16 − 2 hosts.

*CIDR /n = n network bits। Host bits = 32 − n। /16 → 2^16 − 2 hosts।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q52. What does /24 denote in CIDR?

<span lang='hi'>CIDR में /24 किसे दर्शाता है?</span>

- **(A)** 24 bits are used for the host portion
- **(B)** 24 bits are used for the network portion ✅ **(CORRECT)**
- **(C)** 24 subnets are created
- **(D)** 24 addresses are available in the subnet

**✔ Correct Answer: (B) 24 bits are used for the network portion** — /24 means the first 24 bits are the network portion (mask 255.255.255.0), leaving 8 host bits.

*/24 का अर्थ पहले 24 bits network भाग (mask 255.255.255.0) हैं, 8 host bits बचती हैं।*

**★ Nukta (Key Point):** Official RPSC 2024 key: /24 = 24 network bits. Same idea: /27 = 27 network bits, /30 = 30.

*Official RPSC 2024 key: /24 = 24 network bits। वैसे ही: /27 = 27 network bits, /30 = 30।*

*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

---
### Q53. How many USABLE hosts are there in a /24 subnet?

<span lang='hi'>/24 subnet में कितने उपयोगी (usable) hosts होते हैं?</span>

- **(A)** 128
- **(B)** 256
- **(C)** 254 ✅ **(CORRECT)**
- **(D)** 512

**✔ Correct Answer: (C) 254** — /24 leaves 8 host bits: 2^8 = 256 addresses, minus the network ID and broadcast address = 254 usable hosts.

*/24 में 8 host bits बचती हैं: 2^8 = 256 addresses, network ID और broadcast address घटाने पर = 254 उपयोगी hosts।*

**★ Nukta (Key Point):** Formula: usable hosts = 2^host_bits − 2. /24 → 254, /25 → 126, /26 → 62, /27 → 30, /28 → 14, /29 → 6, /30 → 2.

*सूत्र: उपयोगी hosts = 2^host_bits − 2। /24 → 254, /25 → 126, /26 → 62, /27 → 30, /28 → 14, /29 → 6, /30 → 2।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5) · also CN Topic Test-03] · Hard*

---
### Q54. How many usable hosts are there in a /30 subnet?

<span lang='hi'>/30 subnet में कितने उपयोगी hosts होते हैं?</span>

- **(A)** 2 ✅ **(CORRECT)**
- **(B)** 4
- **(C)** 6
- **(D)** 14

**✔ Correct Answer: (A) 2** — /30 leaves 2 host bits: 2^2 = 4 addresses − network − broadcast = 2 usable hosts — perfect for point-to-point WAN links.

*/30 में 2 host bits बचती हैं: 2^2 = 4 addresses − network − broadcast = 2 उपयोगी hosts — point-to-point WAN links के लिए एकदम सही।*

**★ Nukta (Key Point):** /30 = 2 hosts (router-to-router links). /29 = 6 hosts (small office).

*/30 = 2 hosts (router-to-router links)। /29 = 6 hosts (छोटा office)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q55. A subnet mask of 255.255.255.248 allows how many usable hosts?

<span lang='hi'>Subnet mask 255.255.255.248 कितने उपयोगी hosts की अनुमति देता है?</span>

- **(A)** 2
- **(B)** 6 ✅ **(CORRECT)**
- **(C)** 14
- **(D)** 30

**✔ Correct Answer: (B) 6** — 255.255.255.248 = /29 → 3 host bits → 2^3 − 2 = 6 usable hosts.

*255.255.255.248 = /29 → 3 host bits → 2^3 − 2 = 6 उपयोगी hosts।*

**★ Nukta (Key Point):** .248 = /29 = 6 hosts. Remember the /30-/29-/28 ladder: 2, 6, 14.

*.248 = /29 = 6 hosts। /30-/29-/28 ladder याद रखें: 2, 6, 14।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Hard*

---
### Q56. The subnet mask 255.255.255.128 provides how many subnets for a Class C network?

<span lang='hi'>Subnet mask 255.255.255.128, Class C network के लिए कितने subnets देता है?</span>

- **(A)** 1
- **(B)** 2 ✅ **(CORRECT)**
- **(C)** 4
- **(D)** 8

**✔ Correct Answer: (B) 2** — 255.255.255.128 borrows 1 host bit from Class C's 8: 2^1 = 2 subnets (each with 126 hosts).

*255.255.255.128, Class C की 8 host bits में से 1 bit उधार लेता है: 2^1 = 2 subnets (हर एक में 126 hosts)।*

**★ Nukta (Key Point):** Borrowed bits n → 2^n subnets. .128 = 1 bit borrowed → 2 subnets.

*उधार bits n → 2^n subnets। .128 = 1 bit उधार → 2 subnets।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q57. A network needs 5 subnets, each with at least 16 hosts. Which subnet mask (Class C) should be used?

<span lang='hi'>एक network को 5 subnets चाहिए, हर एक में कम से कम 16 hosts। कौन-सा subnet mask (Class C) उपयोग करें?</span>

- **(A)** 255.255.255.192
- **(B)** 255.255.255.248
- **(C)** 255.255.255.240
- **(D)** 255.255.255.224 ✅ **(CORRECT)**

**✔ Correct Answer: (D) 255.255.255.224** — 255.255.255.224 (/27) borrows 3 bits: 2^3 = 8 subnets (≥ 5) and leaves 5 host bits: 2^5 − 2 = 30 hosts (≥ 16).

*255.255.255.224 (/27) 3 bits उधार लेता है: 2^3 = 8 subnets (≥ 5) और 5 host bits बचती हैं: 2^5 − 2 = 30 hosts (≥ 16)।*

**★ Nukta (Key Point):** Subnetting trade-off: more subnets → fewer hosts each. Borrow just enough bits (3 here).

*Subnetting trade-off: ज़्यादा subnets → हर एक में कम hosts। बस पर्याप्त bits उधार लें (यहाँ 3)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q58. A subnet mask for Class C can have how many 1's by default (remaining bits 0)?

<span lang='hi'>Class C के लिए subnet mask में डिफ़ॉल्ट रूप से कितने 1's हो सकते हैं (बाकी bits 0)?</span>

- **(A)** 10
- **(B)** 24 ✅ **(CORRECT)**
- **(C)** 12
- **(D)** 7

**✔ Correct Answer: (B) 24** — The default Class C mask 255.255.255.0 has 24 one-bits and 8 zero-bits.

*डिफ़ॉल्ट Class C mask 255.255.255.0 में 24 one-bits और 8 zero-bits होते हैं।*

**★ Nukta (Key Point):** Class C default = /24 = 24 ones. (With subnetting it can go up to /30 practically.)

*Class C default = /24 = 24 ones। (Subnetting के साथ यह व्यावहारिक रूप से /30 तक जा सकता है।)*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q59. What is the valid host range for the subnet 192.168.1.0/25?

<span lang='hi'>Subnet 192.168.1.0/25 के लिए वैध host range क्या है?</span>

- **(A)** 192.168.1.0 - 192.168.1.255
- **(B)** 192.168.1.1 - 192.168.1.126 ✅ **(CORRECT)**
- **(C)** 192.168.1.1 - 192.168.1.254
- **(D)** 192.168.1.0 - 192.168.1.127

**✔ Correct Answer: (B) 192.168.1.1 - 192.168.1.126** — /25 splits the block into halves of 128: the first subnet is .0-.127 — network .0, broadcast .127, so usable hosts are .1-.126.

*/25 block को 128 की दो आधा-आधा भागों में बाँटता है: पहला subnet .0-.127 — network .0, broadcast .127, इसलिए उपयोगी hosts .1-.126 हैं।*

**★ Nukta (Key Point):** Host range = network+1 to broadcast−1. For /25: .1-.126 (first subnet) and .129-.254 (second).

*Host range = network+1 से broadcast−1। /25 के लिए: .1-.126 (पहला subnet) और .129-.254 (दूसरा)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q60. In subnetting, reducing the number of host bits does what?

<span lang='hi'>Subnetting में host bits की संख्या घटाने से क्या होता है?</span>

- **(A)** Increases the broadcast domain
- **(B)** Decreases the number of subnets
- **(C)** Increases the number of subnets ✅ **(CORRECT)**
- **(D)** Increases the number of hosts

**✔ Correct Answer: (C) Increases the number of subnets** — Borrowing host bits (reducing host bits) increases the number of subnets — each subnet then has fewer hosts.

*Host bits उधार लेने (host bits घटाने) से subnets की संख्या बढ़ती है — हर subnet में hosts कम हो जाते हैं।*

**★ Nukta (Key Point):** More subnet bits ⇔ more subnets ⇔ fewer hosts each. Ye subnetting ka basic trade-off hai.

*ज़्यादा subnet bits ⇔ ज़्यादा subnets ⇔ हर एक में कम hosts। यह subnetting का मूल trade-off है।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Hard*

---
### Q61. In a class B subnet: IP address 125.134.112.66, mask 255.255.224.0. What is the first address (network address)?

<span lang='hi'>Class B subnet में: IP address 125.134.112.66, mask 255.255.224.0। पहला address (network address) क्या होगा?</span>

- **(A)** 125.134.96.0 ✅ **(CORRECT)**
- **(B)** 125.134.112.0
- **(C)** 125.134.112.66
- **(D)** 125.134.0.0

**✔ Correct Answer: (A) 125.134.96.0** — Mask 255.255.224.0 = /19 with block size 32 in the third octet: 112 = 3×32+16 → block start 96 → network 125.134.96.0.

*Mask 255.255.224.0 = /19, third octet में block size 32: 112 = 3×32+16 → block की शुरुआत 96 → network 125.134.96.0।*

**★ Nukta (Key Point):** Block size = 256 − last non-255 octet (256−224 = 32). Floor(112/32)×32 = 96.

*Block size = 256 − अंतिम गैर-255 octet (256−224 = 32)। Floor(112/32)×32 = 96।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q62. A Class B network is to be split into subnets with a 3-bit subnet number. What is the maximum number of subnets and hosts in each subnet?

<span lang='hi'>एक Class B network को 3-bit subnet number में बाँटना है। प्रत्येक subnet में subnets और hosts की अधिकतम संख्या कितनी होगी?</span>

- **(A)** 8 subnets and 262141 hosts
- **(B)** 6 subnets and 262141 hosts
- **(C)** 6 subnets and 1022 hosts
- **(D)** None of the above ✅ **(CORRECT)**

**✔ Correct Answer: (D) None of the above** — With a 3-bit subnet number: 2^3 = 8 subnets (6 usable in old classful rules) and 2^13 − 2 = 8190 hosts per subnet — none of the printed options matches.

*3-bit subnet number के साथ: 2^3 = 8 subnets (पुराने classful नियमों में 6 उपयोगी) और प्रति subnet 2^13 − 2 = 8190 hosts — दिए गए विकल्पों में से कोई मेल नहीं खाता।*

**★ Nukta (Key Point):** Class B /16 + 3 subnet bits = /19: 8 subnets × 8190 hosts each. Since options are unusual, the correct choice is 'None of the above'.

*Class B /16 + 3 subnet bits = /19: 8 subnets × 8190 hosts। विकल्प असामान्य हैं इसलिए सही विकल्प 'None of the above' है।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q63. IP address 172.16.123.213 has subnet mask 255.255.255.240. What is its network (first) address?

<span lang='hi'>IP address 172.16.123.213 का subnet mask 255.255.255.240 है। इसका network (पहला) address क्या है?</span>

- **(A)** 172.16.123.240
- **(B)** 172.16.123.208 ✅ **(CORRECT)**
- **(C)** 172.16.123.213
- **(D)** 172.16.123.245

**✔ Correct Answer: (B) 172.16.123.208** — 255.255.255.240 = /28 with block size 16: 213 = 13×16+5 → block start 208 → network 172.16.123.208 (range .208-.223).

*255.255.255.240 = /28, block size 16: 213 = 13×16+5 → block की शुरुआत 208 → network 172.16.123.208 (range .208-.223)।*

**★ Nukta (Key Point):** /28 = 16-address blocks: .208-.223 here. Network = .208, broadcast = .223, hosts = .209-.222 (14 hosts).

*/28 = 16-address blocks: यहाँ .208-.223। Network = .208, broadcast = .223, hosts = .209-.222 (14 hosts)।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Hard*

---
### Q64. An organization has a Class B network and wishes to form subnets for 64 departments. The subnet mask would be:

<span lang='hi'>एक संगठन के पास Class B network है और वह 64 departments के लिए subnets बनाना चाहता है। Subnet mask क्या होगा?</span>

- **(A)** 255.255.128.0
- **(B)** 255.255.0.0
- **(C)** 255.255.64.0
- **(D)** 255.255.252.0 ✅ **(CORRECT)**

**✔ Correct Answer: (D) 255.255.252.0** — 64 subnets need 2^6 subnets → borrow 6 host bits from Class B's 16: mask = 255.255.252.0 (/22).

*64 subnets के लिए 2^6 subnets → Class B की 16 host bits में से 6 bits उधार: mask = 255.255.252.0 (/22)।*

**★ Nukta (Key Point):** Borrow 6 bits: 16+6 = 22 network bits = 255.255.252.0. RPSC 2024 official key.

*6 bits उधार: 16+6 = 22 network bits = 255.255.252.0। RPSC 2024 official key।*

*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

---
### Q65. A Class B network has a subnet mask of 255.255.248.0. What is the maximum number of hosts per subnet?

<span lang='hi'>एक Class B network का subnet mask 255.255.248.0 है। प्रति subnet hosts की अधिकतम संख्या कितनी है?</span>

- **(A)** 2046 ✅ **(CORRECT)**
- **(B)** 1022
- **(C)** 1023
- **(D)** 1024

**✔ Correct Answer: (A) 2046** — 255.255.248.0 = /21 → 32−21 = 11 host bits → 2^11 − 2 = 2046 usable hosts.

*255.255.248.0 = /21 → 32−21 = 11 host bits → 2^11 − 2 = 2046 उपयोगी hosts।*

**★ Nukta (Key Point):** Official key (RPSC 2024 + Rajasthan PYQ): 2046 hosts. /21 → 2^11−2 = 2046.

*Official key (RPSC 2024 + Rajasthan PYQ): 2046 hosts। /21 → 2^11−2 = 2046।*

*[Source: RPSC Programmer 2024 Paper-1 (official key) · Rajasthan PYQ Q56] · Hard*

---
### Q66. An IP address 156.233.42.56 is configured with a 7-bit subnet mask (7 bits borrowed from the host part of the classful network). How many hosts and subnets are possible?

<span lang='hi'>IP address 156.233.42.56 को 7-bit subnet mask (classful network के host भाग से 7 bits उधार) के साथ configure किया गया है। कितने hosts और subnets संभव हैं?</span>

- **(A)** 126 hosts, 510 subnets ✅ **(CORRECT)**
- **(B)** 128 hosts, 512 subnets
- **(C)** 510 hosts, 126 subnets
- **(D)** 512 hosts, 128 subnets

**✔ Correct Answer: (A) 126 hosts, 510 subnets** — 156.233.x is Class B (default /16). With 7 bits for HOSTS: 2^7 − 2 = 126 hosts; the remaining 9 borrowed subnet bits give 2^9 − 2 = 510 usable subnets.

*156.233.x Class B है (default /16)। HOSTS के लिए 7 bits: 2^7 − 2 = 126 hosts; बची 9 subnet bits से 2^9 − 2 = 510 उपयोगी subnets।*

**★ Nukta (Key Point):** Bank key pattern: 7 host bits → 126 hosts; 9 subnet bits → 510 usable subnets (both −2).

*Bank key pattern: 7 host bits → 126 hosts; 9 subnet bits → 510 उपयोगी subnets (दोनों −2)।*

*[Source: Unit Test -2 Solutions (OCR), p5] · Hard*

---
### Q67. If a Class B network on the internet has a subnet mask of 255.255.248.0, what is the maximum number of hosts per subnet?

<span lang='hi'>यदि internet पर किसी Class B network की subnet mask 255.255.248.0 हो, तो हर subnet में अधिकतम hosts कितने होंगे?</span>

- **(A)** 1023
- **(B)** 1022
- **(C)** 1024
- **(D)** 2046 ✅ **(CORRECT)**

**✔ Correct Answer: (D) 2046** — 255.255.248.0 = /21 — यानी host bits = 32 − 21 = 11. अधिकतम hosts = 2¹¹ − 2 = 2046.

*255.255.248.0 = /21 — यानी host bits = 32 − 21 = 11. अधिकतम hosts = 2¹¹ − 2 = 2046.*

**★ Nukta (Key Point):** 248 = 11111000 → तीसरे octet में 5 subnet bits. हमेशा 2^hostbits − 2 (network और broadcast हटाकर).

*248 = 11111000 → तीसरे octet में 5 subnet bits. हमेशा 2^hostbits − 2 (network और broadcast हटाकर).*

*[Source: RPSC Programmer 2024 Paper-1 (via Suraku Academy official-key solutions)] · Hard*

---
### Q68. The address of a Class B host is to be split into subnets with a 6-bit subnet number. What is the maximum number of subnets and the maximum number of hosts in each subnet?

<span lang='hi'>Class B host के पते को 6-bit subnet number से subnets में बाँटना है. अधिकतम subnets और हर subnet में अधिकतम hosts कितने होंगे?</span>

- **(A)** 62 subnets and 262142 hosts
- **(B)** 64 subnets and 262142 hosts
- **(C)** 62 subnets and 1022 hosts ✅ **(CORRECT)**
- **(D)** 64 subnets and 1024 hosts

**✔ Correct Answer: (C) 62 subnets and 1022 hosts** — Class B में host bits 16 होती हैं; 6 bits subnet में जाने पर बचीं 10 host bits → hosts = 2¹⁰ − 2 = 1022. Subnets = 2⁶ − 2 = 62 (subnet-zero और all-ones हटाकर).

*Class B में host bits 16 होती हैं; 6 bits subnet में जाने पर बचीं 10 host bits → hosts = 2¹⁰ − 2 = 1022. Subnets = 2⁶ − 2 = 62 (subnet-zero और all-ones हटाकर).*

**★ Nukta (Key Point):** RPSC 2011 और GATE 2005 दोनों में यही प्रश्न — official key (C) 62 subnets, 1022 hosts.

*RPSC 2011 और GATE 2005 दोनों में यही प्रश्न — official key (C) 62 subnets, 1022 hosts.*

*[Source: RPSC Programmer 2011 Paper-1 (via pyqp.in) + GATE CS 2005] · Hard*

---
### Q69. Suppose that in an IP-over-Ethernet network, a machine X wishes to find the MAC address of another machine Y in its subnet. Which one of the following techniques can be used for this?

<span lang='hi'>IP-over-Ethernet network में machine X को अपने ही subnet की machine Y का MAC address जानना है। इसके लिए निम्न में से कौन-सी technique प्रयोग होगी?</span>

- **(A)** ARP request broadcast / ARP request broadcast ✅ **(CORRECT)**
- **(B)** RARP request broadcast / RARP request broadcast
- **(C)** DNS query / DNS query
- **(D)** ICMP query / ICMP query

**✔ Correct Answer: (A) ARP request broadcast** — X ARP request ko broadcast karta hai (Y ki IP puch kar); Y unicast ARP reply mein apna MAC deta hai — ARP hi IP→MAC resolution ka tarika hai.

*X ARP request broadcast karta hai (Y ki IP); Y unicast reply mein MAC deta hai — ARP = IP→MAC resolution.*

**★ Nukta (Key Point):** RARP ulta (MAC→IP) hai; DNS naam→IP; ICMP error/control — koi bhi MAC nahi deta.

*RARP उल्टा (MAC→IP); DNS नाम→IP; ICMP error — MAC कोई नहीं देता।*

*[Source: GATE CS 2019] · Hard*

---
### Q70. Node X has a TCP connection open to node Y. Packets from X to Y go through an intermediate IP router R; Ethernet switch S is the first switch on the path. For a packet sent from X, which of the following is TRUE about its destination IP and MAC addresses at the time it leaves X?

<span lang='hi'>Node X की node Y से TCP connection है; packets router R से होकर जाते हैं और पहला Ethernet switch S है। X से निकलते packet के destination IP और MAC addresses के बारे में क्या सही है?</span>

- **(A)** Destination IP = Y's IP; destination MAC = R's MAC / Destination IP = Y का IP; destination MAC = R का MAC ✅ **(CORRECT)**
- **(B)** Destination IP = R's IP; destination MAC = R's MAC / Destination IP = R का IP; destination MAC = R का MAC
- **(C)** Destination IP = Y's IP; destination MAC = Y's MAC / Destination IP = Y का IP; destination MAC = Y का MAC
- **(D)** Destination IP = R's IP; destination MAC = S's MAC / Destination IP = R का IP; destination MAC = S का MAC

**✔ Correct Answer: (A) Destination IP = Y's IP; destination MAC = R's MAC** — IP address end-to-end hota hai — destination IP hamesha Y ka; MAC har hop par badalta hai, isliye pehle hop (router R) ka MAC lagta hai — ARP se gateway ka MAC mila hota hai.

*IP end-to-end होता है — destination IP सदा Y का; MAC हर hop पर बदलता है, पहले hop (router R) का MAC लगता है।*

**★ Nukta (Key Point):** IP ko hop-by-hop badalna common galti hai; switch MAC forwarding karta hai par packet ka destination MAC router ka hi rehta hai.

*IP को hop-by-hop बदलना आम गलती; packet का destination MAC router का ही रहता है।*

*[Source: GATE CS 2025 Set-2] · Hard*

---

## Section D — IPv6 Addressing

*128-bit addresses, address types (no broadcast), IPv6-only header changes, transition (tunneling), AAAA records.*

### Q71. Which IPv6 address type is globally unique and globally routable?

<span lang='hi'>कौन-सा IPv6 address type globally unique और globally routable होता है?</span>

- **(A)** Link-Local
- **(B)** Multicast
- **(C)** Unique Local
- **(D)** Global Unicast ✅ **(CORRECT)**

**✔ Correct Answer: (D) Global Unicast** — Global Unicast addresses (2000::/3) are the public, globally routable IPv6 addresses — like public IPv4 addresses.

*Global Unicast addresses (2000::/3) public, globally routable IPv6 addresses हैं — जैसे public IPv4 addresses।*

**★ Nukta (Key Point):** IPv6 unicast scopes: Link-Local (fe80::/10) = this link only; Unique-Local (fc00::/7) = like private; Global (2000::/3) = Internet.

*IPv6 unicast scopes: Link-Local (fe80::/10) = केवल यह link; Unique-Local (fc00::/7) = private जैसा; Global (2000::/3) = Internet।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

---
### Q72. IPv6 was developed by:

<span lang='hi'>IPv6 किसने develop किया?</span>

- **(A)** IETF ✅ **(CORRECT)**
- **(B)** ANSI
- **(C)** ISO
- **(D)** IEEE

**✔ Correct Answer: (A) IETF** — The IETF (Internet Engineering Task Force) developed IPv6 (published as RFC 2460, 1998) to overcome IPv4 address exhaustion.

*IETF (Internet Engineering Task Force) ने IPv6 develop किया (RFC 2460, 1998) — IPv4 address exhaustion को दूर करने के लिए।*

**★ Nukta (Key Point):** IPv4/IPv6 = IETF (RFCs). OSI = ISO. LAN standards = IEEE (802). ANSI = US standards body.

*IPv4/IPv6 = IETF (RFCs)। OSI = ISO। LAN standards = IEEE (802)। ANSI = US standards body।*

*[Source: Repo: CN Topic Test-03 (UNIT TEST-3)] · Medium*

---
### Q73. Two IPv6 nodes must interoperate but are connected through intervening IPv4 routers. The best solution is:

<span lang='hi'>दो IPv6 nodes को interoperable होना है लेकिन वे बीच में आने वाले IPv4 routers से जुड़े हैं। सबसे अच्छा समाधान क्या है?</span>

- **(A)** Use the dual-stack approach
- **(B)** Tunneling ✅ **(CORRECT)**
- **(C)** No solution
- **(D)** Replace the system

**✔ Correct Answer: (B) Tunneling** — Tunneling wraps IPv6 packets inside IPv4 packets so they can cross the IPv4-only routers (IPv6-in-IPv4).

*Tunneling IPv6 packets को IPv4 packets के अंदर लपेटती है ताकि वे IPv4-only routers पार कर सकें (IPv6-in-IPv4)।*

**★ Nukta (Key Point):** Transition mechanisms: Tunneling (IPv6 over IPv4), Dual-stack (both), Translation (NAT64).

*Transition mechanisms: Tunneling (IPv6 over IPv4), Dual-stack (दोनों), Translation (NAT64)।*

*[Source: Sanfoundry CN MCQs — IPv6] · Medium*

---
### Q74. Which DNS resource record should be queried to retrieve the IPv6 address associated with a name?

<span lang='hi'>किसी name से जुड़ा IPv6 address पाने के लिए कौन-सी DNS resource record query करनी चाहिए?</span>

- **(A)** The AAAA record ✅ **(CORRECT)**
- **(B)** The A record
- **(C)** The NS record
- **(D)** The MX record

**✔ Correct Answer: (A) The AAAA record** — The AAAA ('quad-A') record maps a domain name to an IPv6 address; the A record maps to IPv4.

*AAAA ('quad-A') record domain name को IPv6 address से जोड़ती है; A record IPv4 से जोड़ती है।*

**★ Nukta (Key Point):** DNS records: A = name→IPv4, AAAA = name→IPv6, PTR = IP→name, MX = mail, NS = name server.

*DNS records: A = name→IPv4, AAAA = name→IPv6, PTR = IP→name, MX = mail, NS = name server।*

*[Source: cnp3 MCQ (Bonaventure CN textbook), DNS1] · Medium*

---
### Q75. IPv6 addresses are ______ bit addresses.

<span lang='hi'>IPv6 addresses ______ bit के पते होते हैं.</span>

- **(A)** 32
- **(B)** 64
- **(C)** 16
- **(D)** 128 ✅ **(CORRECT)**

**✔ Correct Answer: (D) 128** — IPv4 के 32 bits के उलट IPv6 addresses 128 bits के होते हैं — इसीलिए IPv6 में पतों की कमी नहीं.

*IPv4 के 32 bits के उलट IPv6 addresses 128 bits के होते हैं — इसीलिए IPv6 में पतों की कमी नहीं.*

**★ Nukta (Key Point):** IPv4 = 32-bit (4 numbers); IPv6 = 128-bit (8 groups).

*IPv4 = 32-bit (4 numbers); IPv6 = 128-bit (8 groups).*

*[Source: SBI/IBPS Computer Awareness Capsule 2018 (IBT India)] · Medium*

---
### Q76. In IPv6, how many bits are in the address?

<span lang='hi'>IPv6 में address कितने bits का होता है?</span>

- **(A)** 32
- **(B)** 64
- **(C)** 128 ✅ **(CORRECT)**
- **(D)** 256

**✔ Correct Answer: (C) 128** — IPv6 addresses are 128 bits — written as 8 groups of 4 hex digits (e.g., 2001:DB8::1).

*IPv6 addresses 128 bits के होते हैं — 4 hex digits के 8 groups में लिखे जाते हैं (जैसे 2001:DB8::1)।*

**★ Nukta (Key Point):** Size line: IPv4 32, IPv6 128, MAC 48, Port 16. 128 bits = 2^128 ≈ 3.4 × 10^38 addresses.

*Size line: IPv4 32, IPv6 128, MAC 48, Port 16। 128 bits = 2^128 ≈ 3.4 × 10^38 addresses।*

*[Source: Repo: CN Topic Test-6 (UNIT TEST-6) · Sanfoundry / Medium / MQuestions banks] · Hard*

---
### Q77. IPv6 does NOT use which type of address?

<span lang='hi'>IPv6 किस type का address उपयोग नहीं करता?</span>

- **(A)** Broadcast ✅ **(CORRECT)**
- **(B)** Multicast
- **(C)** Anycast
- **(D)** None of the mentioned

**✔ Correct Answer: (A) Broadcast** — IPv6 eliminated broadcast — it uses multicast (and anycast) for group communication instead.

*IPv6 ने broadcast हटा दिया है — group communication के लिए multicast (और anycast) उपयोग होता है।*

**★ Nukta (Key Point):** IPv4: unicast + broadcast + multicast. IPv6: unicast + multicast + anycast (NO broadcast).

*IPv4: unicast + broadcast + multicast। IPv6: unicast + multicast + anycast (broadcast नहीं)।*

*[Source: Sanfoundry CN MCQs — IPv6] · Hard*

---
### Q78. Which features are present in IPv4 but NOT in IPv6?

<span lang='hi'>कौन-सी features IPv4 में हैं लेकिन IPv6 में नहीं?</span>

- **(A)** Fragmentation by routers
- **(B)** Header checksum
- **(C)** Options
- **(D)** All of the mentioned ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the mentioned** — IPv6 simplified the header: routers do not fragment packets (source does), the header checksum was removed, and the Options field became extension headers.

*IPv6 ने header सरल बनाया: routers packets fragment नहीं करते (source करता है), header checksum हटा दिया गया, और Options field extension headers बन गया।*

**★ Nukta (Key Point):** IPv6 header = fixed 40 bytes, 8 fields, NO checksum / NO router fragmentation / NO options field.

*IPv6 header = fixed 40 bytes, 8 fields, कोई checksum नहीं / कोई router fragmentation नहीं / कोई options field नहीं।*

*[Source: Sanfoundry CN MCQs — IPv6] · Hard*

---
### Q79. Which of the following is TRUE for IPv6?

<span lang='hi'>IPv6 के लिए निम्न में से क्या सही है?</span>

- **(A)** Uses 32-bit addresses
- **(B)** Includes a header checksum
- **(C)** Supports anycast addressing ✅ **(CORRECT)**
- **(D)** Does not support multicast

**✔ Correct Answer: (C) Supports anycast addressing** — IPv6 natively supports anycast (one-to-nearest) along with unicast and multicast.

*IPv6 मूल रूप से anycast (one-to-nearest) को unicast और multicast के साथ support करता है।*

**★ Nukta (Key Point):** IPv6 address types: Unicast, Multicast, Anycast. No broadcast, no header checksum.

*IPv6 address types: Unicast, Multicast, Anycast। Broadcast नहीं, header checksum नहीं।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Hard*

---

## Section E — Port Numbers, DNS/URL & Address Resolution (ARP)

*16-bit ports & ranges, socket addressing, DNS records & lookups, ARP/RARP, URL layer.*

### Q80. Which of the following sets of port numbers belongs to the 'well-known' ports category?

<span lang='hi'>निम्न में से कौन-से port numbers 'well-known' ports category में आते हैं?</span>

- **(A)** 80, 443, 8080
- **(B)** 49152, 110, 53
- **(C)** 22, 25, 80 ✅ **(CORRECT)**
- **(D)** 1024, 3306, 8080

**✔ Correct Answer: (C) 22, 25, 80** — Well-known ports are 0-1023 — 22 (SSH), 25 (SMTP) and 80 (HTTP) all lie in this range; the other sets contain ports above 1023.

*Well-known ports 0-1023 होते हैं — 22 (SSH), 25 (SMTP) और 80 (HTTP) तीनों इसी range में हैं; बाकी sets में 1023 से ऊपर के ports हैं।*

**★ Nukta (Key Point):** Port ranges: Well-known 0-1023, Registered 1024-49151, Ephemeral (dynamic) 49152-65535.

*Port ranges: Well-known 0-1023, Registered 1024-49151, Ephemeral (dynamic) 49152-65535।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q81. What is the typical range of ephemeral (dynamic) ports?

<span lang='hi'>Ephemeral (dynamic) ports की सामान्य range क्या है?</span>

- **(A)** 0-1023
- **(B)** 1024-49151
- **(C)** 49152-65535 ✅ **(CORRECT)**
- **(D)** 100-200

**✔ Correct Answer: (C) 49152-65535** — Ephemeral (client-side dynamic) ports are assigned from 49152-65535 by the OS for each new connection.

*Ephemeral (client-side dynamic) ports OS द्वारा हर नए connection के लिए 49152-65535 से दिए जाते हैं।*

**★ Nukta (Key Point):** Well-known 0-1023 (services), Registered 1024-49151 (apps), Ephemeral 49152-65535 (clients).

*Well-known 0-1023 (services), Registered 1024-49151 (apps), Ephemeral 49152-65535 (clients)।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) · also CN Topic Test 5] · Easy*

---
### Q82. The transport layer uses which type of addressing?

<span lang='hi'>Transport layer किस प्रकार की addressing उपयोग करता है?</span>

- **(A)** IP address
- **(B)** MAC address
- **(C)** Port number ✅ **(CORRECT)**
- **(D)** Domain name

**✔ Correct Answer: (C) Port number** — The transport layer uses 16-bit port numbers for service-point addressing — to deliver data to the correct process (e.g., port 80 for a web server).

*Transport layer service-point addressing के लिए 16-bit port numbers उपयोग करता है — data सही process तक पहुँचाने के लिए (जैसे web server के लिए port 80)।*

**★ Nukta (Key Point):** Layer addressing: Data link = MAC (48), Network = IP (32), Transport = Port (16), Application = specific/socket.

*Layer addressing: Data link = MAC (48), Network = IP (32), Transport = Port (16), Application = specific/socket।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q83. A URL (like www.example.com) belongs to which layer?

<span lang='hi'>URL (जैसे www.example.com) किस layer से संबंधित है?</span>

- **(A)** Presentation
- **(B)** Application ✅ **(CORRECT)**
- **(C)** Transport
- **(D)** Network

**✔ Correct Answer: (B) Application** — URLs/user-friendly addresses work at the application layer — DNS resolves them to IP addresses before lower layers take over.

*URLs/user-friendly addresses application layer पर काम करते हैं — DNS उन्हें IP addresses में बदलता है, फिर निचली layers काम करती हैं।*

**★ Nukta (Key Point):** Address levels at layers: specific (app) → port (transport) → IP (network) → MAC (data link).

*Layers पर address levels: specific (app) → port (transport) → IP (network) → MAC (data link)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q84. DNS works at which layer of the OSI model?

<span lang='hi'>DNS, OSI model की किस layer पर काम करता है?</span>

- **(A)** Transport
- **(B)** Application ✅ **(CORRECT)**
- **(C)** Network
- **(D)** Data link

**✔ Correct Answer: (B) Application** — DNS is an application-layer protocol (using UDP/TCP port 53) that resolves domain names to IP addresses.

*DNS एक application-layer protocol है (UDP/TCP port 53 उपयोग करता है) जो domain names को IP addresses में बदलता है।*

**★ Nukta (Key Point):** Application layer examples: DNS, HTTP, FTP, SMTP, SNMP, DHCP. Transport carries them (UDP 53 for DNS).

*Application layer के उदाहरण: DNS, HTTP, FTP, SMTP, SNMP, DHCP। Transport उन्हें ले जाता है (DNS के लिए UDP 53)।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q85. Which of the following uniquely identifies a process on a host?

<span lang='hi'>Host पर किसी process की unique पहचान कौन करता है?</span>

- **(A)** IP address only
- **(B)** Port number only
- **(C)** IP address + Port number ✅ **(CORRECT)**
- **(D)** MAC address

**✔ Correct Answer: (C) IP address + Port number** — A socket = IP address + port number uniquely identifies a process on a host (e.g., 192.168.1.5:80).

*Socket = IP address + port number किसी host पर एक process की unique पहचान करता है (जैसे 192.168.1.5:80)।*

**★ Nukta (Key Point):** IP = the host (machine). IP + Port = the specific process (socket/specific address).

*IP = host (machine)। IP + Port = विशिष्ट process (socket/specific address)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

---
### Q86. What is the default port number for DNS?

<span lang='hi'>DNS का default port number क्या है?</span>

- **(A)** 80
- **(B)** 21
- **(C)** 53 ✅ **(CORRECT)**
- **(D)** 110

**✔ Correct Answer: (C) 53** — DNS uses port 53 — UDP 53 for queries and TCP 53 for large transfers (zone transfers).

*DNS port 53 उपयोग करता है — queries के लिए UDP 53 और बड़े transfers (zone transfers) के लिए TCP 53।*

**★ Nukta (Key Point):** Port one-liners: DNS 53, HTTP 80, HTTPS 443, FTP 21/20, SMTP 25, POP3 110, Telnet 23, SSH 22, DHCP 67/68.

*Port one-liners: DNS 53, HTTP 80, HTTPS 443, FTP 21/20, SMTP 25, POP3 110, Telnet 23, SSH 22, DHCP 67/68।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

---
### Q87. DNS is the abbreviation of:

<span lang='hi'>DNS का पूरा नाम (full form) क्या है?</span>

- **(A)** Dynamic Name System
- **(B)** Dynamic Network System
- **(C)** Domain Name System ✅ **(CORRECT)**
- **(D)** Domain Network Service

**✔ Correct Answer: (C) Domain Name System** — DNS = Domain Name System — the hierarchical directory that maps domain names to IP addresses.

*DNS = Domain Name System — एक पदानुक्रमित directory जो domain names को IP addresses से जोड़ती है।*

**★ Nukta (Key Point):** DNS = Domain Name System (port 53). Hierarchical: root → TLD → authoritative servers.

*DNS = Domain Name System (port 53)। पदानुक्रम: root → TLD → authoritative servers।*

*[Source: Networking MCQ bank (MQuestions blog)] · Medium*

---
### Q88. Which DNS record type maps a domain name to an IPv4 address?

<span lang='hi'>कौन-सी DNS record type domain name को IPv4 address से जोड़ती है?</span>

- **(A)** CNAME
- **(B)** A ✅ **(CORRECT)**
- **(C)** MX
- **(D)** PTR

**✔ Correct Answer: (B) A** — The A (address) record maps a domain name to its IPv4 address (AAAA does the same for IPv6).

*A (address) record domain name को उसके IPv4 address से जोड़ती है (IPv6 के लिए यही काम AAAA करती है)।*

**★ Nukta (Key Point):** Records quick map: A = name→IPv4, AAAA = name→IPv6, PTR = IP→name, CNAME = alias, MX = mail.

*Records quick map: A = name→IPv4, AAAA = name→IPv6, PTR = IP→name, CNAME = alias, MX = mail।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6) · also cnp3 DNS2] · Medium*

---
### Q89. What is the role of DNS? It is best described as:

<span lang='hi'>DNS की भूमिका क्या है? सबसे सही विवरण है:</span>

- **(A)** Maps a domain name to an IP address ✅ **(CORRECT)**
- **(B)** Translates a host's private IP to a public IP
- **(C)** Translates a host's IPv6 address to an IPv4 address
- **(D)** Maps a MAC address to an IP address

**✔ Correct Answer: (A) Maps a domain name to an IP address** — DNS resolves (maps) domain names like www.example.com to IP addresses — 'the phonebook of the Internet'.

*DNS domain names (जैसे www.example.com) को IP addresses से resolve (map) करता है — 'Internet की phonebook'।*

**★ Nukta (Key Point):** Official RPSC 2024 key. Reverse: PTR records map IP→name. DHCP = auto IP config; NAT = private→public.

*Official RPSC 2024 key। Reverse: PTR records IP→name map करती हैं। DHCP = auto IP config; NAT = private→public।*

*[Source: RPSC Programmer 2024 Paper-1 (official key) · also CN Topic Test-02 / Medium bank] · Hard*

---
### Q90. A reverse lookup in DNS means a lookup to ______ using ______ records.

<span lang='hi'>DNS में reverse lookup का अर्थ है ______ records का उपयोग करके ______ की lookup।</span>

- **(A)** Identify mail servers, SOA
- **(B)** Map an IP address to a domain name, PTR ✅ **(CORRECT)**
- **(C)** Map domain names to IP addresses, A
- **(D)** Determine the authoritative name server, NS

**✔ Correct Answer: (B) Map an IP address to a domain name, PTR** — A reverse lookup resolves an IP address back to a domain name using PTR (pointer) records — e.g., for mail-server verification.

*Reverse lookup PTR (pointer) records का उपयोग करके IP address को वापस domain name में बदलती है — जैसे mail-server verification के लिए।*

**★ Nukta (Key Point):** Forward: name → IP (A / AAAA). Reverse: IP → name (PTR, in-addr.arpa).

*Forward: name → IP (A / AAAA)। Reverse: IP → name (PTR, in-addr.arpa)।*

*[Source: RPSC Programmer 2024 Paper-1 (official key) · also CN Topic Test 5] · Hard*

---
### Q91. The Address Resolution Protocol (ARP) is used for:

<span lang='hi'>Address Resolution Protocol (ARP) किस काम में आता है?</span>

- **(A)** Finding the IP address that corresponds to a MAC address
- **(B)** Finding the MAC address that corresponds to an IP address ✅ **(CORRECT)**
- **(C)** Finding the IP address from the DNS name
- **(D)** Finding the IP address of the default gateway

**✔ Correct Answer: (B) Finding the MAC address that corresponds to an IP address** — ARP resolves a known IP address to the unknown MAC (physical) address of the next hop on the local network.

*ARP ज्ञात IP address को local network पर अगली hop के अज्ञात MAC (physical) address से जोड़ता है।*

**★ Nukta (Key Point):** ARP = IP→MAC (Address Resolution). RARP = MAC→IP (obsolete — replaced by BOOTP/DHCP). DNS = name→IP.

*ARP = IP→MAC (Address Resolution)। RARP = MAC→IP (अप्रचलित — BOOTP/DHCP से बदला)। DNS = name→IP।*

*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

---
### Q92. Which one of the following protocols is NOT used to resolve one form of address into another?

<span lang='hi'>निम्न में से कौन-सा protocol एक प्रकार के पते को दूसरे में बदलने के लिए उपयोग नहीं होता?</span>

- **(A)** DNS
- **(B)** ARP
- **(C)** DHCP ✅ **(CORRECT)**
- **(D)** RARP

**✔ Correct Answer: (C) DHCP** — DNS नाम→IP, ARP IP→MAC, RARP MAC→IP बदलते हैं. DHCP तो नए device को IP देता है — किसी पते का translation नहीं करता.

*DNS नाम→IP, ARP IP→MAC, RARP MAC→IP बदलते हैं. DHCP तो नए device को IP देता है — किसी पते का translation नहीं करता.*

**★ Nukta (Key Point):** Address resolvers: DNS, ARP, RARP. Address distributor: DHCP.

*Address resolvers: DNS, ARP, RARP. Address distributor: DHCP.*

*[Source: GATE CS PYQ (via Computer Science Junction / examprev)] · Hard*

---
### Q93. A reverse lookup in DNS means a lookup to ______ using ______ records.

<span lang='hi'>DNS में reverse lookup का अर्थ है ______ records का उपयोग करके ______ की खोज.</span>

- **(A)** map domain names to IP address, A
- **(B)** map IP address to domain name, PTR ✅ **(CORRECT)**
- **(C)** determine the authoritative name servers, CNAME
- **(D)** identify mail servers, SOA

**✔ Correct Answer: (B) map IP address to domain name, PTR** — Reverse lookup में IP address से domain name निकाला जाता है और इसमें PTR (Pointer) records उपयोग होते हैं.

*Reverse lookup में IP address से domain name निकाला जाता है और इसमें PTR (Pointer) records उपयोग होते हैं.*

**★ Nukta (Key Point):** Normal: name→IP = A record; Reverse: IP→name = PTR record. यह जोड़ी परीक्षा में बार-बार आती है.

*Normal: name→IP = A record; Reverse: IP→name = PTR record. यह जोड़ी परीक्षा में बार-बार आती है.*

*[Source: RPSC Programmer 2024 Paper-1 (via Suraku Academy official-key solutions)] · Hard*

---

## ★ Nukte Rapid-Fire — Exam Pointers

- **MAC address size?** *(MAC address size?)* → **48 bits (6 bytes, 12 hex digits).** *(48 bits (6 bytes, 12 hex digits)।)*
- **IPv4 size? IPv6 size? Port size?** *(IPv4 size? IPv6 size? Port size?)* → **32 / 128 / 16 bits.** *(32 / 128 / 16 bits।)*
- **MAC address other names?** *(MAC address के अन्य नाम?)* → **Physical address / hardware address / burned-in address.** *(Physical address / hardware address / burned-in address।)*
- **Broadcast MAC address?** *(Broadcast MAC address?)* → **FF:FF:FF:FF:FF:FF (all 48 bits = 1).** *(FF:FF:FF:FF:FF:FF (सभी 48 bits = 1)।)*
- **I/G bit trick for unicast/multicast?** *(Unicast/multicast के लिए I/G bit trick?)* → **Last bit of first octet: 0 = unicast, 1 = multicast.** *(पहले octet का अंतिम bit: 0 = unicast, 1 = multicast।)*
- **Class ranges by first octet (A/B/C/D/E)?** *(पहले octet से Class ranges (A/B/C/D/E)?)* → **0-127 / 128-191 / 192-223 / 224-239 (multicast) / 240-255 (experimental).** *(0-127 / 128-191 / 192-223 / 224-239 (multicast) / 240-255 (experimental)।)*
- **Default masks A/B/C?** *(Default masks A/B/C?)* → **255.0.0.0 /8, 255.255.0.0 /16, 255.255.255.0 /24.** *(255.0.0.0 /8, 255.255.0.0 /16, 255.255.255.0 /24।)*
- **Hosts per class (A/B/C)?** *(प्रति class hosts (A/B/C)?)* → **2^24−2 (16,777,214) / 2^16−2 (65,534) / 2^8−2 (254).** *(2^24−2 (16,777,214) / 2^16−2 (65,534) / 2^8−2 (254)।)*
- **Loopback address?** *(Loopback address?)* → **127.0.0.1 (whole 127.0.0.0/8 block).** *(127.0.0.1 (पूरा 127.0.0.0/8 block)।)*
- **APIPA range (DHCP fail)?** *(APIPA range (DHCP fail)?)* → **169.254.0.1 - 169.254.255.254.** *(169.254.0.1 - 169.254.255.254।)*
- **Private IP blocks (RFC 1918)?** *(Private IP blocks (RFC 1918)?)* → **10.x / 172.16-31.x / 192.168.x.** *(10.x / 172.16-31.x / 192.168.x।)*
- **0.0.0.0 means?** *(0.0.0.0 का अर्थ?)* → **'This host — no IP yet' (source) or default route (0.0.0.0/0).** *('यह host — अभी IP नहीं' (source) या default route (0.0.0.0/0)।)*
- **Usable hosts formula?** *(Usable hosts सूत्र?)* → **2^host-bits − 2. /24→254, /25→126, /27→30, /30→2.** *(2^host-bits − 2। /24→254, /25→126, /27→30, /30→2।)*
- **Subnets formula?** *(Subnets सूत्र?)* → **2^borrowed-bits. 3 bits → 8 subnets.** *(2^borrowed-bits। 3 bits → 8 subnets।)*
- **CIDR /24 means?** *(CIDR /24 का अर्थ?)* → **24 network bits (mask 255.255.255.0).** *(24 network bits (mask 255.255.255.0)।)*
- **/30 used for?** *(/30 किसके लिए?)* → **Point-to-point links (2 usable hosts).** *(Point-to-point links (2 उपयोगी hosts)।)*
- **Subnetting trade-off?** *(Subnetting trade-off?)* → **More subnets ⇔ fewer hosts each.** *(ज़्यादा subnets ⇔ हर एक में कम hosts।)*
- **IPv6 has broadcast?** *(IPv6 में broadcast है?)* → **NO — IPv6 uses multicast + anycast, no broadcast.** *(नहीं — IPv6 multicast + anycast उपयोग करता है, broadcast नहीं।)*
- **IPv6 transition techniques?** *(IPv6 transition techniques?)* → **Tunneling (IPv6-in-IPv4), Dual-stack, Translation (NAT64).** *(Tunneling (IPv6-in-IPv4), Dual-stack, Translation (NAT64)।)*
- **Well-known / registered / ephemeral port ranges?** *(Well-known / registered / ephemeral port ranges?)* → **0-1023 / 1024-49151 / 49152-65535.** *(0-1023 / 1024-49151 / 49152-65535।)*
- **Port numbers: DNS, HTTP, HTTPS, FTP, SMTP, SSH?** *(Port numbers: DNS, HTTP, HTTPS, FTP, SMTP, SSH?)* → **53, 80, 443, 21, 25, 22.** *(53, 80, 443, 21, 25, 22।)*
- **Socket = ?** *(Socket = ?)* → **IP address + Port number (identifies a process).** *(IP address + Port number (process की पहचान)।)*
- **DNS records: A / AAAA / PTR / MX / CNAME?** *(DNS records: A / AAAA / PTR / MX / CNAME?)* → **name→IPv4 / name→IPv6 / IP→name / mail / alias.** *(name→IPv4 / name→IPv6 / IP→name / mail / alias।)*
- **ARP vs RARP?** *(ARP vs RARP?)* → **ARP = IP→MAC. RARP = MAC→IP (obsolete, use DHCP).** *(ARP = IP→MAC। RARP = MAC→IP (अप्रचलित, DHCP उपयोग करें)।)*
- **NAT purpose?** *(NAT उद्देश्य?)* → **Map private IPs → public IP (save addresses + hide internals).** *(Private IPs → public IP map करना (addresses बचाना + internals छिपाना)।)*
- **Per-hop vs end-to-end in a routed packet?** *(Routed packet में per-hop vs end-to-end?)* → **MAC changes per hop; IP addresses stay end-to-end.** *(MAC हर hop पर बदलता है; IP addresses end-to-end रहते हैं।)*
- **Who allocates IP addresses globally?** *(Global IP addresses कौन allocate करता है?)* → **ICANN/IANA (with RIRs). IETF makes protocols, IEEE makes LAN standards.** *(ICANN/IANA (RIRs के साथ)। IETF protocols बनाता है, IEEE LAN standards।)*

