# Data Communication & Computer Networks (CN)
## Topic 6 of 7 : OSI Layers in Detail — 153 MCQs (English + Hindi)

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** RPSC Programmer • ACP • RSMSSB IA • SA • DD • BCI • SCI • REET • RAS • DSSSB • KVS • NVS • HTET • SSC CGL/CHSL • RRB • IBPS • UPSC & all Rajasthan + Central Govt. Exams (Computer Awareness)

**Total Questions:** 153 | **Type:** MCQ (4 options) | **Bilingual:** English + Hindi (technical terms in English) | Each: ✔ why the correct answer is right + ★ Nukta. Wrong options verified internally. Answers cross-verified 4×.

### Syllabus Coverage (sub-topic wise order)

| # | Sub-topic | Questions |
|---|-----------|-----------|
| 1 | Section A — Data Link Layer: Flow & Error Control | Q1 - Q44 |
| 2 | Section B — Data Link Layer: Framing & MAC Sub-layer | Q45 - Q69 |
| 3 | Section C — Network Layer: IP, ICMP, ARP & Routing Protocols | Q70 - Q101 |
| 4 | Section D — Transport Layer: TCP/UDP, Ports & Sockets | Q102 - Q128 |
| 5 | Section E — Session, Presentation & Application Layer | Q129 - Q153 |

---

## Section A — Data Link Layer: Flow & Error Control

*LLC/MAC sub-layers, flow control, ARQ protocols (Stop-and-Wait, Go-Back-N, Selective Repeat), error detection & correction (parity, CRC, checksum, Hamming) — basic to advanced.*

### Q1. Which sub-layer of the Data Link Layer is responsible for flow control and error control?

<span lang='hi'>Data Link Layer का कौन-सा sub-layer flow control और error control के लिए ज़िम्मेदार होता है?</span>

- **(A)** MAC / MAC
- **(B)** LLC (Logical Link Control) / LLC (Logical Link Control) ✅ **(CORRECT)**
- **(C)** PVC / PVC
- **(D)** None of the above / None of the above

**✔ Correct Answer: (B) LLC (Logical Link Control)** — LLC (Logical Link Control) sub-layer flow control, error control और Network layer को service interface देता है; MAC sub-layer physical addressing और channel access संभालता है.

*LLC (Logical Link Control) sub-layer flow control, error control और Network layer को service interface देता है; MAC sub-layer physical addressing और channel access संभालता है.*

**★ Nukta (Key Point):** DLL = MAC + LLC — याद रखो: MAC = addressing + medium access, LLC = flow + error + interface.

*DLL = MAC + LLC — याद रखो: MAC = addressing + medium access, LLC = flow + error + interface.*

*[Source: BCI Subject Test-8.pdf]*

---
### Q2. Which of the following functions are performed by the Data Link Layer? (1) Framing (2) Error Detection (3) Flow Control (4) Path Determination

<span lang='hi'>निम्न में से कौन-से कार्य Data Link Layer करता है? (1) Framing (2) Error Detection (3) Flow Control (4) Path Determination</span>

- **(A)** 1, 2 and 3 only / 1, 2 and 3 only ✅ **(CORRECT)**
- **(B)** 1 and 4 only / 1 and 4 only
- **(C)** 2 and 4 only / 2 and 4 only
- **(D)** 1, 2, 3 and 4 / 1, 2, 3 and 4

**✔ Correct Answer: (A) 1, 2 and 3 only** — Framing, Error Detection और Flow Control — तीनों Data Link Layer के काम हैं. Path Determination यानी routing Network Layer का काम है.

*Framing, Error Detection और Flow Control — तीनों Data Link Layer के काम हैं. Path Determination यानी routing Network Layer का काम है.*

**★ Nukta (Key Point):** याद रखो: DLL में F-E-F (Framing, Error, Flow) + addressing; रास्ता चुनना (routing) Network Layer का.

*याद रखो: DLL में F-E-F (Framing, Error, Flow) + addressing; रास्ता चुनना (routing) Network Layer का.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q3. Which of the following statements about MAC and LLC sublayers is TRUE? (1) MAC sublayer handles physical addressing (2) LLC sublayer provides error control and flow control (3) MAC sublayer performs routing

<span lang='hi'>MAC और LLC sub-layers के बारे में कौन-सा कथन सही है? (1) MAC sub-layer physical addressing संभालता है (2) LLC sub-layer error control और flow control देता है (3) MAC sub-layer routing करता है</span>

- **(A)** 1 and 2 only / 1 and 2 only ✅ **(CORRECT)**
- **(B)** 2 and 3 only / 2 and 3 only
- **(C)** 1 and 3 only / 1 and 3 only
- **(D)** 1, 2 and 3 / 1, 2 and 3

**✔ Correct Answer: (A) 1 and 2 only** — (1) सही — MAC physical (MAC) addressing संभालता है; (2) सही — LLC में flow और error control होता है; (3) गलत — MAC में routing नहीं होती, routing Network Layer का काम है.

*(1) सही — MAC physical (MAC) addressing संभालता है; (2) सही — LLC में flow और error control होता है; (3) गलत — MAC में routing नहीं होती, routing Network Layer का काम है.*

**★ Nukta (Key Point):** MAC = addressing + channel access; LLC = flow + error + interface; routing = Network Layer.

*MAC = addressing + channel access; LLC = flow + error + interface; routing = Network Layer.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q4. Which of the following is NOT a responsibility of the LLC sublayer?

<span lang='hi'>निम्न में से कौन-सा LLC sub-layer की ज़िम्मेदारी नहीं है?</span>

- **(A)** Flow control / Flow control
- **(B)** Error control / Error control
- **(C)** Service interface to Network layer / Service interface to Network layer
- **(D)** Physical addressing / Physical addressing ✅ **(CORRECT)**

**✔ Correct Answer: (D) Physical addressing** — Physical addressing (MAC address) MAC sub-layer का काम है — LLC नहीं. LLC flow control, error control और Network layer को interface देता है.

*Physical addressing (MAC address) MAC sub-layer का काम है — LLC नहीं. LLC flow control, error control और Network layer को interface देता है.*

**★ Nukta (Key Point):** MAC = Media Access Control = addressing; LLC = Logical Link Control = flow/error.

*MAC = Media Access Control = addressing; LLC = Logical Link Control = flow/error.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q5. Which of the following is NOT a function of the Data Link Layer?

<span lang='hi'>निम्न में से कौन-सा Data Link Layer का function नहीं है?</span>

- **(A)** Framing / Framing
- **(B)** Error detection / Error detection
- **(C)** Error correction / Error correction
- **(D)** Routing / Routing ✅ **(CORRECT)**

**✔ Correct Answer: (D) Routing** — Routing (रास्ता तय करना) Network Layer का function है. Data Link Layer framing, error detection/correction और flow control करता है.

*Routing (रास्ता तय करना) Network Layer का function है. Data Link Layer framing, error detection/correction और flow control करता है.*

**★ Nukta (Key Point):** DLL = next-hop delivery (frame); Network = end-to-end delivery (packet + route).

*DLL = next-hop delivery (frame); Network = end-to-end delivery (packet + route).*

*[Source: BCI Subject Test-9.pdf + CN Topic Test-04.pdf]*

---
### Q6. The Frame Check Sequence (FCS) field in an Ethernet frame is used for:

<span lang='hi'>Ethernet frame में Frame Check Sequence (FCS) field किस काम आता है?</span>

- **(A)** Flow control / Flow control
- **(B)** Address resolution / Address resolution
- **(C)** Error detection using CRC / Error detection using CRC ✅ **(CORRECT)**
- **(D)** Medium access / Medium access

**✔ Correct Answer: (C) Error detection using CRC** — FCS field में CRC (Cyclic Redundancy Check) का result होता है जिससे receiver frame की errors detect करता है.

*FCS field में CRC (Cyclic Redundancy Check) का result होता है जिससे receiver frame की errors detect करता है.*

**★ Nukta (Key Point):** FCS = CRC = error detection. Ethernet error correct नहीं करता, बस detect करके frame drop करता है.

*FCS = CRC = error detection. Ethernet error correct नहीं करता, बस detect करके frame drop करता है.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q7. Which of the following techniques uses both acknowledgments and sequence numbers?

<span lang='hi'>निम्न में से कौन-सी technique acknowledgments और sequence numbers दोनों उपयोग करती है?</span>

- **(A)** Go-Back-N / Go-Back-N
- **(B)** Stop-and-Wait / Stop-and-Wait
- **(C)** Selective Repeat / Selective Repeat
- **(D)** All of the above / All of the above ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the above** — Stop-and-Wait, Go-Back-N और Selective Repeat — तीनों ARQ protocols sequence numbers और acknowledgments दोनों उपयोग करते हैं.

*Stop-and-Wait, Go-Back-N और Selective Repeat — तीनों ARQ protocols sequence numbers और acknowledgments दोनों उपयोग करते हैं.*

**★ Nukta (Key Point):** ARQ = Automatic Repeat reQuest — बिना sequence/ack के कोई ARQ चल ही नहीं सकता.

*ARQ = Automatic Repeat reQuest — बिना sequence/ack के कोई ARQ चल ही नहीं सकता.*

*[Source: Unit Test -2 Solutions.pdf (OCR) + CN Topic Test-04.pdf]*

---
### Q8. Error control is the process of detecting and correcting errors, while ______ is a mechanism to ensure the efficient delivery of data.

<span lang='hi'>Error control, errors को detect और correct करने की प्रक्रिया है, जबकि ______ data के कुशल delivery का mechanism है.</span>

- **(A)** Error control, Flow control / Error control, Flow control ✅ **(CORRECT)**
- **(B)** Process control, Network control / Process control, Network control
- **(C)** Session control, Flow control / Session control, Flow control
- **(D)** OSI Control, Data control / OSI Control, Data control

**✔ Correct Answer: (A) Error control, Flow control** — पहला blank Error control (errors detect+correct), दूसरा Flow control (sender की speed receiver के हिसाब से) — दोनों Data Link/Transport layers में मिलते हैं.

*पहला blank Error control (errors detect+correct), दूसरा Flow control (sender की speed receiver के हिसाब से) — दोनों Data Link/Transport layers में मिलते हैं.*

**★ Nukta (Key Point):** Error = सही करना; Flow = संतुलन बनाना. दोनों अलग-अलग काम हैं.

*Error = सही करना; Flow = संतुलन बनाना. दोनों अलग-अलग काम हैं.*

*[Source: CN Topic Test-02.pdf]*

---
### Q9. ______ control refers to a set of procedures used to restrict the amount of data that the sender can send before waiting for acknowledgment.

<span lang='hi'>______ control उन procedures का समूह है जो sender द्वारा acknowledgment की प्रतीक्षा से पहले भेजे जाने वाले data की मात्रा सीमित करते हैं.</span>

- **(A)** Flow / Flow ✅ **(CORRECT)**
- **(B)** Error / Error
- **(C)** Transmission / Transmission
- **(D)** Access control / Access control

**✔ Correct Answer: (A) Flow** — Flow control sender को रोकता है ताकि receiver का buffer न भरे — इसलिए acknowledgment आने तक data सीमित रहता है.

*Flow control sender को रोकता है ताकि receiver का buffer न भरे — इसलिए acknowledgment आने तक data सीमित रहता है.*

**★ Nukta (Key Point):** Flow control = sender↔receiver के बीच का संतुलन; यही definition परीक्षा में बार-बार आती है.

*Flow control = sender↔receiver के बीच का संतुलन; यही definition परीक्षा में बार-बार आती है.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p17]*

---
### Q10. What is the main purpose of the Sliding Window in TCP?

<span lang='hi'>TCP में Sliding Window का मुख्य उद्देश्य क्या है?</span>

- **(A)** Address resolution / Address resolution
- **(B)** Flow control / Flow control ✅ **(CORRECT)**
- **(C)** Error detection / Error detection
- **(D)** Encryption / Encryption

**✔ Correct Answer: (B) Flow control** — Sliding window से receiver बताता है कि वह कितना data ले सकता है — यही flow control है.

*Sliding window से receiver बताता है कि वह कितना data ले सकता है — यही flow control है.*

**★ Nukta (Key Point):** TCP window = receiver की capacity का advertisement; इसीलिए इसे flow control कहते हैं.

*TCP window = receiver की capacity का advertisement; इसीलिए इसे flow control कहते हैं.*

*[Source: CN Topic Test 5.pdf]*

---
### Q11. Flow control prevents which of the following issues?

<span lang='hi'>Flow control निम्न में से किस समस्या को रोकता है?</span>

- **(A)** Deadlock / Deadlock
- **(B)** Congestion collapse / Congestion collapse
- **(C)** Overflow of the receiver's buffer / Overflow of the receiver's buffer ✅ **(CORRECT)**
- **(D)** Packet routing error / Packet routing error

**✔ Correct Answer: (C) Overflow of the receiver's buffer** — Flow control receiver के buffer को overflow होने से बचाता है — sender उतना ही भेजता है जितना receiver संभाल सके.

*Flow control receiver के buffer को overflow होने से बचाता है — sender उतना ही भेजता है जितना receiver संभाल सके.*

**★ Nukta (Key Point):** Flow control = दोनों के बीच; Congestion control = पूरे network के लिए.

*Flow control = दोनों के बीच; Congestion control = पूरे network के लिए.*

*[Source: CN Topic Test-04.pdf]*

---
### Q12. In the TCP header, the acknowledgment field value represents:

<span lang='hi'>TCP header में acknowledgment field का मान किसे दर्शाता है?</span>

- **(A)** Number of previous bytes received / Number of previous bytes received
- **(B)** Total number of bytes to receive / Total number of bytes to receive
- **(C)** Sequence number of the next byte expected / Sequence number of the next byte expected ✅ **(CORRECT)**
- **(D)** Sequence of zeros and ones / Sequence of zeros and ones

**✔ Correct Answer: (C) Sequence number of the next byte expected** — TCP का ACK number अगली expected byte का sequence number है — यानी अब तक सब कुछ उससे पहले मिल चुका है (cumulative acknowledgment).

*TCP का ACK number अगली expected byte का sequence number है — यानी अब तक सब कुछ उससे पहले मिल चुका है (cumulative acknowledgment).*

**★ Nukta (Key Point):** TCP bytes गिनता है, packets नहीं — ACK = 'next byte भेजो'.

*TCP bytes गिनता है, packets नहीं — ACK = 'next byte भेजो'.*

*[Source: CN Topic Test-04.pdf]*

---
### Q13. In Stop-and-Wait ARQ, after sending one frame, the sender:

<span lang='hi'>Stop-and-Wait ARQ में एक frame भेजने के बाद sender:</span>

- **(A)** Waits for acknowledgment / Waits for acknowledgment ✅ **(CORRECT)**
- **(B)** Sends the next frame immediately / Sends the next frame immediately
- **(C)** Stops transmission permanently / Stops transmission permanently
- **(D)** Sends a NAK / Sends a NAK

**✔ Correct Answer: (A) Waits for acknowledgment** — Stop-and-Wait में sender एक frame भेजकर उसके acknowledgment का इंतज़ार करता है.

*Stop-and-Wait में sender एक frame भेजकर उसके acknowledgment का इंतज़ार करता है.*

**★ Nukta (Key Point):** इसी waiting के कारण इसका नाम 'Stop-and-Wait' पड़ा.

*इसी waiting के कारण इसका नाम 'Stop-and-Wait' पड़ा.*

*[Source: CN Topic Test-04.pdf]*

---
### Q14. In Stop-and-Wait protocol, the sender sends:

<span lang='hi'>Stop-and-Wait protocol में sender भेजता है:</span>

- **(A)** Multiple frames at once / Multiple frames at once
- **(B)** One frame at a time / One frame at a time ✅ **(CORRECT)**
- **(C)** Acknowledgments only / Acknowledgments only
- **(D)** Data without waiting / Data without waiting

**✔ Correct Answer: (B) One frame at a time** — Stop-and-Wait में एक समय में सिर्फ एक frame outstanding रहता है.

*Stop-and-Wait में एक समय में सिर्फ एक frame outstanding रहता है.*

**★ Nukta (Key Point):** Window size = 1 — इसीलिए एक-एक frame.

*Window size = 1 — इसीलिए एक-एक frame.*

*[Source: CN Topic Test-04.pdf]*

---
### Q15. What is the window size in Stop-and-Wait ARQ?

<span lang='hi'>Stop-and-Wait ARQ में window size कितनी होती है?</span>

- **(A)** 0 / 0
- **(B)** 1 / 1 ✅ **(CORRECT)**
- **(C)** N / N
- **(D)** 2 / 2

**✔ Correct Answer: (B) 1** — Stop-and-Wait की window size 1 होती है — एक ही frame बिना ACK के भेजा जा सकता है.

*Stop-and-Wait की window size 1 होती है — एक ही frame बिना ACK के भेजा जा सकता है.*

**★ Nukta (Key Point):** Window = 1 ↔ एक frame at a time — दोनों एक ही बात हैं.

*Window = 1 ↔ एक frame at a time — दोनों एक ही बात हैं.*

*[Source: CN Topic Test-04.pdf]*

---
### Q16. What is the main disadvantage of Stop-and-Wait flow control?

<span lang='hi'>Stop-and-Wait flow control की मुख्य कमी क्या है?</span>

- **(A)** Complexity / Complexity
- **(B)** Low efficiency due to waiting / Low efficiency due to waiting ✅ **(CORRECT)**
- **(C)** High memory usage / High memory usage
- **(D)** Frame loss / Frame loss

**✔ Correct Answer: (B) Low efficiency due to waiting** — हर frame के बाद इंतज़ार करने से line बेकार खाली रहती है — खासकर long-distance links पर efficiency बहुत गिर जाती है.

*हर frame के बाद इंतज़ार करने से line बेकार खाली रहती है — खासकर long-distance links पर efficiency बहुत गिर जाती है.*

**★ Nukta (Key Point):** Waiting = idle time = कम utilization. इसीलिए Sliding Window आया.

*Waiting = idle time = कम utilization. इसीलिए Sliding Window आया.*

*[Source: CN Topic Test-04.pdf]*

---
### Q17. A Stop-and-Wait ARQ channel has high latency and large bandwidth. What problem occurs?

<span lang='hi'>Stop-and-Wait ARQ channel पर latency ज़्यादा और bandwidth बड़ी हो तो क्या समस्या होती है?</span>

- **(A)** High throughput / High throughput
- **(B)** Low channel utilization / Low channel utilization ✅ **(CORRECT)**
- **(C)** CRC failure / CRC failure
- **(D)** Frame duplication / Frame duplication

**✔ Correct Answer: (B) Low channel utilization** — High latency में ACK देर से आता है और बड़ी bandwidth खाली रह जाती है — channel utilization बहुत कम हो जाता है. इसीलिए high-BDP links पर Sliding Window protocols उपयोग होते हैं.

*High latency में ACK देर से आता है और बड़ी bandwidth खाली रह जाती है — channel utilization बहुत कम हो जाता है. इसीलिए high-BDP links पर Sliding Window protocols उपयोग होते हैं.*

**★ Nukta (Key Point):** Bandwidth × Delay (BDP) जितना बड़ा, Stop-and-Wait उतना बेकार.

*Bandwidth × Delay (BDP) जितना बड़ा, Stop-and-Wait उतना बेकार.*

*[Source: BCI Subject Test-8.pdf]*

---
### Q18. In Stop-and-Wait ARQ, what happens when a frame is lost?

<span lang='hi'>Stop-and-Wait ARQ में frame खो जाए तो क्या होता है?</span>

- **(A)** Receiver sends NAK / Receiver sends NAK
- **(B)** Sender retransmits after timeout / Sender retransmits after timeout ✅ **(CORRECT)**
- **(C)** Receiver retransmits / Receiver retransmits
- **(D)** No retransmission / No retransmission

**✔ Correct Answer: (B) Sender retransmits after timeout** — ACK न आने पर sender का timeout timer बजता है और वह frame दोबारा भेजता है.

*ACK न आने पर sender का timeout timer बजता है और वह frame दोबारा भेजता है.*

**★ Nukta (Key Point):** Lost frame + timeout = retransmission. Receiver कभी retransmit नहीं करता.

*Lost frame + timeout = retransmission. Receiver कभी retransmit नहीं करता.*

*[Source: CN Topic Test-04.pdf]*

---
### Q19. For Stop-and-Wait ARQ, for 10 data packets sent, ............ acknowledgements are needed.

<span lang='hi'>Stop-and-Wait ARQ में 10 data packets भेजने पर ............ acknowledgements चाहिए होते हैं.</span>

- **(A)** 9 / 9
- **(B)** 20 / 20
- **(C)** 11 / 11
- **(D)** 10 / 10 ✅ **(CORRECT)**

**✔ Correct Answer: (D) 10** — हर packet का अपना ACK चाहिए — 10 packets → 10 ACKs.

*हर packet का अपना ACK चाहिए — 10 packets → 10 ACKs.*

**★ Nukta (Key Point):** RPSC official key (d) — Stop-and-Wait में ack:packet अनुपात 1:1.

*RPSC official key (d) — Stop-and-Wait में ack:packet अनुपात 1:1.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q20. In Go-Back-N ARQ, if an error is detected in a frame:

<span lang='hi'>Go-Back-N ARQ में किसी frame में error मिले तो:</span>

- **(A)** Only that frame is retransmitted / Only that frame is retransmitted
- **(B)** All frames are ignored / All frames are ignored
- **(C)** That frame and all subsequent outstanding frames are retransmitted / That frame and all subsequent outstanding frames are retransmitted ✅ **(CORRECT)**
- **(D)** No frame is retransmitted / No frame is retransmitted

**✔ Correct Answer: (C) That frame and all subsequent outstanding frames are retransmitted** — Go-Back-N में receiver केवल in-order frames रखता है; गलत frame के बाद के सारे frames छोड़ देता है और sender उस frame से आगे के सभी outstanding frames दोबारा भेजता है.

*Go-Back-N में receiver केवल in-order frames रखता है; गलत frame के बाद के सारे frames छोड़ देता है और sender उस frame से आगे के सभी outstanding frames दोबारा भेजता है.*

**★ Nukta (Key Point):** GBN = 'जहाँ चूक, वहाँ से फिर से' — Selective Repeat में सिर्फ गलत frame दोबारा जाता है.

*GBN = 'जहाँ चूक, वहाँ से फिर से' — Selective Repeat में सिर्फ गलत frame दोबारा जाता है.*

*[Source: CN Topic Test-04.pdf]*

---
### Q21. In the ______ protocol, if no acknowledgment for a frame has arrived, we resend all outstanding frames.

<span lang='hi'>______ protocol में, किसी frame का acknowledgment न आए तो हम सभी outstanding frames दोबारा भेजते हैं.</span>

- **(A)** Stop-and-Wait ARQ / Stop-and-Wait ARQ
- **(B)** Go-Back-N ARQ / Go-Back-N ARQ ✅ **(CORRECT)**
- **(C)** Selective-Repeat ARQ / Selective-Repeat ARQ
- **(D)** Both B and C / Both B and C

**✔ Correct Answer: (B) Go-Back-N ARQ** — 'सभी outstanding frames दोबारा भेजना' Go-Back-N की पहचान है.

*'सभी outstanding frames दोबारा भेजना' Go-Back-N की पहचान है.*

**★ Nukta (Key Point):** GBN = Go Back N — Nवें तक सब दोबारा; SR = सिर्फ गलत वाला.

*GBN = Go Back N — Nवें तक सब दोबारा; SR = सिर्फ गलत वाला.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p8]*

---
### Q22. A Go-Back-N sender uses window size 4. Frame 2 is lost. What happens after the receiver receives frames 3 and 4?

<span lang='hi'>Go-Back-N sender window size 4 उपयोग करता है. Frame 2 खो जाता है. Receiver को frames 3 और 4 मिलने के बाद क्या होता है?</span>

- **(A)** Receiver stores frames 3 and 4 in buffer / Receiver stores frames 3 and 4 in buffer
- **(B)** Receiver sends ACK for frame 4 / Receiver sends ACK for frame 4
- **(C)** Receiver discards frames 3 and 4 / Receiver discards frames 3 and 4 ✅ **(CORRECT)**
- **(D)** Receiver acts like Selective Repeat / Receiver acts like Selective Repeat

**✔ Correct Answer: (C) Receiver discards frames 3 and 4** — GBN receiver सिर्फ अगली in-order frame चाहता है — frame 2 खोने पर 3 और 4 out-of-order हैं, इसलिए उन्हें discard कर दिया जाता है.

*GBN receiver सिर्फ अगली in-order frame चाहता है — frame 2 खोने पर 3 और 4 out-of-order हैं, इसलिए उन्हें discard कर दिया जाता है.*

**★ Nukta (Key Point):** GBN receiver dumb होता है (buffer नहीं रखता); SR receiver smart (buffer रखता है).

*GBN receiver dumb होता है (buffer नहीं रखता); SR receiver smart (buffer रखता है).*

*[Source: BCI Subject Test-8.pdf]*

---
### Q23. In Go-Back-N ARQ, if 6 is the number of bits for the sequence number, then the maximum size of the send window must be:

<span lang='hi'>Go-Back-N ARQ में sequence number के 6 bits हों तो send window का अधिकतम आकार कितना होगा?</span>

- **(A)** 63 / 63 ✅ **(CORRECT)**
- **(B)** 61 / 61
- **(C)** 31 / 31
- **(D)** 64 / 64

**✔ Correct Answer: (A) 63** — GBN में maximum window = 2ⁿ − 1 = 2⁶ − 1 = 63.

*GBN में maximum window = 2ⁿ − 1 = 2⁶ − 1 = 63.*

**★ Nukta (Key Point):** GBN/SW का window formula अलग है SR से — GBN: 2ⁿ−1, SR: 2ⁿ⁻¹.

*GBN/SW का window formula अलग है SR से — GBN: 2ⁿ−1, SR: 2ⁿ⁻¹.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p9]*

---
### Q24. In a Go-Back-N protocol, if the window size = 63, how many sequence number bits are required?

<span lang='hi'>Go-Back-N protocol में window size = 63 हो तो sequence number के कितने bits चाहिए?</span>

- **(A)** 5 / 5
- **(B)** 6 / 6 ✅ **(CORRECT)**
- **(C)** 7 / 7
- **(D)** 8 / 8

**✔ Correct Answer: (B) 6** — Window = 2ⁿ − 1 → 63 = 2⁶ − 1, इसलिए n = 6 bits.

*Window = 2ⁿ − 1 → 63 = 2⁶ − 1, इसलिए n = 6 bits.*

**★ Nukta (Key Point):** उपर वाले प्रश्न का उल्टा — यही formula दोनों तरफ से याद रखो.

*उपर वाले प्रश्न का उल्टा — यही formula दोनों तरफ से याद रखो.*

*[Source: BCI Subject Test-8.pdf]*

---
### Q25. The maximum number of outstanding frames in Selective Repeat (with N sequence numbers) is:

<span lang='hi'>Selective Repeat में outstanding frames की अधिकतम संख्या (N sequence numbers के साथ) होती है:</span>

- **(A)** N / N
- **(B)** N − 1 / N − 1
- **(C)** N/2 / N/2 ✅ **(CORRECT)**
- **(D)** 2N / 2N

**✔ Correct Answer: (C) N/2** — Selective Repeat में sender और receiver दोनों की windows अलग-अलग होती हैं, इसलिए window ≤ N/2 — यानी अधिकतम N/2 frames outstanding.

*Selective Repeat में sender और receiver दोनों की windows अलग-अलग होती हैं, इसलिए window ≤ N/2 — यानी अधिकतम N/2 frames outstanding.*

**★ Nukta (Key Point):** SR: window N/2 (दो windows), GBN: window N−1 (एक window).

*SR: window N/2 (दो windows), GBN: window N−1 (एक window).*

*[Source: CN Topic Test-04.pdf]*

---
### Q26. A Selective Repeat sliding window protocol uses a window size of 7 with 3-bit sequence numbers. Is it valid?

<span lang='hi'>Selective Repeat sliding window protocol में 3-bit sequence numbers के साथ window size 7 क्या वैध है?</span>

- **(A)** Valid / Valid
- **(B)** Invalid – violates the maximum window rule / Invalid – violates the maximum window rule ✅ **(CORRECT)**
- **(C)** Valid only for piggybacking / Valid only for piggybacking
- **(D)** Valid only with Selective Repeat / Valid only with Selective Repeat

**✔ Correct Answer: (B) Invalid – violates the maximum window rule** — 3-bit sequence numbers पर SR की maximum window = 2³⁻¹ = 4 होती है; 7 > 4 होने से receiver new और old frames में फ़र्क नहीं कर पाएगा — इसलिए अवैध.

*3-bit sequence numbers पर SR की maximum window = 2³⁻¹ = 4 होती है; 7 > 4 होने से receiver new और old frames में फ़र्क नहीं कर पाएगा — इसलिए अवैध.*

**★ Nukta (Key Point):** SR window ≤ 2ⁿ⁻¹; GBN window ≤ 2ⁿ − 1. यही फ़र्क याद रखो.

*SR window ≤ 2ⁿ⁻¹; GBN window ≤ 2ⁿ − 1. यही फ़र्क याद रखो.*

*[Source: BCI Subject Test-8.pdf]*

---
### Q27. Which protocol has better bandwidth utilization?

<span lang='hi'>किस protocol का bandwidth utilization बेहतर होता है?</span>

- **(A)** Stop-and-Wait / Stop-and-Wait
- **(B)** Selective Repeat / Selective Repeat ✅ **(CORRECT)**
- **(C)** Go-Back-N / Go-Back-N
- **(D)** None of the above / None of the above

**✔ Correct Answer: (B) Selective Repeat** — Selective Repeat सिर्फ खोए frames दोबारा भेजता है और out-of-order frames भी buffer कर लेता है — bandwidth सबसे ज़्यादा उपयोग होती है.

*Selective Repeat सिर्फ खोए frames दोबारा भेजता है और out-of-order frames भी buffer कर लेता है — bandwidth सबसे ज़्यादा उपयोग होती है.*

**★ Nukta (Key Point):** Efficiency क्रम: Selective Repeat > Go-Back-N > Stop-and-Wait.

*Efficiency क्रम: Selective Repeat > Go-Back-N > Stop-and-Wait.*

*[Source: CN Topic Test-04.pdf]*

---
### Q28. A noisy channel uses a Hamming code with minimum distance 3. What can it guarantee?

<span lang='hi'>एक noisy channel पर minimum distance 3 वाला Hamming code क्या guarantee दे सकता है?</span>

- **(A)** Detect 2-bit errors / Detect 2-bit errors ✅ **(CORRECT)**
- **(B)** Correct 2-bit errors / Correct 2-bit errors
- **(C)** Correct 3-bit errors / Correct 3-bit errors
- **(D)** Detect 4-bit errors / Detect 4-bit errors

**✔ Correct Answer: (A) Detect 2-bit errors** — Minimum distance d = 3 वाला code 2 errors detect या 1 error correct कर सकता है (d ≥ t + 1 for detection, d ≥ 2t + 1 for correction).

*Minimum distance d = 3 वाला code 2 errors detect या 1 error correct कर सकता है (d ≥ t + 1 for detection, d ≥ 2t + 1 for correction).*

**★ Nukta (Key Point):** d=3 → detect 2 या correct 1 — 'correct 2' के लिए d ≥ 5 चाहिए.

*d=3 → detect 2 या correct 1 — 'correct 2' के लिए d ≥ 5 चाहिए.*

*[Source: BCI Subject Test-8.pdf]*

---
### Q29. What is the Hamming distance between the two codes 10010010 and 11011001?

<span lang='hi'>दो codes 10010010 और 11011001 के बीच Hamming distance कितनी है?</span>

- **(A)** 3 / 3
- **(B)** 4 / 4 ✅ **(CORRECT)**
- **(C)** 6 / 6
- **(D)** 2 / 2

**✔ Correct Answer: (B) 4** — दोनों codes को align करके अलग-अलग bits गिनो: positions 2, 5, 7 और 8 बदलती हैं — कुल 4 अंतर. Hamming distance = अलग bits की संख्या = 4.

*दोनों codes को align करके अलग-अलग bits गिनो: positions 2, 5, 7 और 8 बदलती हैं — कुल 4 अंतर. Hamming distance = अलग bits की संख्या = 4.*

**★ Nukta (Key Point):** Hamming distance = XOR के बाद 1s की गिनती.

*Hamming distance = XOR के बाद 1s की गिनती.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p28]*

---
### Q30. The Hamming distance between two code words can easily be found if we apply the ______ operation.

<span lang='hi'>दो code words के बीच Hamming distance आसानी से मिल जाती है यदि हम ______ operation लगाएँ.</span>

- **(A)** XOR / XOR ✅ **(CORRECT)**
- **(B)** XNOR / XNOR
- **(C)** OR / OR
- **(D)** AND / AND

**✔ Correct Answer: (A) XOR** — XOR करने पर जहाँ bits अलग होती हैं वहाँ 1 आता है — 1s की गिनती ही Hamming distance है.

*XOR करने पर जहाँ bits अलग होती हैं वहाँ 1 आता है — 1s की गिनती ही Hamming distance है.*

**★ Nukta (Key Point):** XOR = difference counter. दूसरे operations यह नहीं बताते.

*XOR = difference counter. दूसरे operations यह नहीं बताते.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p35]*

---
### Q31. Any coding scheme for error control needs to have at least the parameters of:

<span lang='hi'>Error control के लिए किसी भी coding scheme में कम से कम निम्न parameters होने चाहिए:</span>

- **(A)** codeword size / codeword size
- **(B)** dataword size / dataword size
- **(C)** minimum Hamming distance / minimum Hamming distance
- **(D)** All of them / All of them ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of them** — किसी भी error-control code को परिभाषित करने के लिए codeword size, dataword size और minimum Hamming distance — तीनों ज़रूरी हैं.

*किसी भी error-control code को परिभाषित करने के लिए codeword size, dataword size और minimum Hamming distance — तीनों ज़रूरी हैं.*

**★ Nukta (Key Point):** Code = (n, k, d) — n = codeword, k = dataword, d = distance. तीनों से ही code की ताक़त पता चलती है.

*Code = (n, k, d) — n = codeword, k = dataword, d = distance. तीनों से ही code की ताक़त पता चलती है.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p37]*

---
### Q32. To detect or correct errors, we send extra bits with the data. These extra bits are called:

<span lang='hi'>Errors detect या correct करने के लिए data के साथ भेजे गए अतिरिक्त bits कहलाते हैं:</span>

- **(A)** redundancy / redundancy ✅ **(CORRECT)**
- **(B)** correction / correction
- **(C)** detection / detection
- **(D)** parity / parity

**✔ Correct Answer: (A) redundancy** — अतिरिक्त bits redundancy कहलाते हैं — यानी data के ऊपर डाला गया भार जो errors पकड़ने में मदद करता है.

*अतिरिक्त bits redundancy कहलाते हैं — यानी data के ऊपर डाला गया भार जो errors पकड़ने में मदद करता है.*

**★ Nukta (Key Point):** Redundancy = 'जान-बूझकर भेजा अतिरिक्त' — इसी से error control संभव है.

*Redundancy = 'जान-बूझकर भेजा अतिरिक्त' — इसी से error control संभव है.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p36]*

---
### Q33. Which of the following verifies the integrity of a message?

<span lang='hi'>निम्न में से कौन-सा message की integrity जाँचता है?</span>

- **(A)** Message Encryption / Message Encryption
- **(B)** Message Checksum / Message Checksum
- **(C)** Message Digest / Message Digest ✅ **(CORRECT)**
- **(D)** None of these / None of these

**✔ Correct Answer: (C) Message Digest** — Message digest (जैसे MD5/SHA) message की fingerprint बनाकर integrity verify करता है — बदलाव होते ही digest बदल जाता है. (Checksum भी integrity के लिए है, पर 'message integrity' का standard जवाब Message Digest है.)

*Message digest (जैसे MD5/SHA) message की fingerprint बनाकर integrity verify करता है — बदलाव होते ही digest बदल जाता है. (Checksum भी integrity के लिए है, पर 'message integrity' का standard जवाब Message Digest है.)*

**★ Nukta (Key Point):** Digest = अंगूठा-छाप; Encryption = गोपनीयता, integrity नहीं.

*Digest = अंगूठा-छाप; Encryption = गोपनीयता, integrity नहीं.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q34. Which error detection method uses one extra bit added to the end of a byte?

<span lang='hi'>कौन-सी error detection method में byte के अंत में एक अतिरिक्त bit जोड़ी जाती है?</span>

- **(A)** CRC / CRC
- **(B)** Checksum / Checksum
- **(C)** Hamming code / Hamming code
- **(D)** Parity bit / Parity bit ✅ **(CORRECT)**

**✔ Correct Answer: (D) Parity bit** — Parity bit हर byte के साथ एक extra bit जोड़ता है ताकि 1s की गिनती even/odd बनी रहे.

*Parity bit हर byte के साथ एक extra bit जोड़ता है ताकि 1s की गिनती even/odd बनी रहे.*

**★ Nukta (Key Point):** Parity = 1 bit; CRC = पूरा remainder; Checksum = योग; Hamming = कई parity bits.

*Parity = 1 bit; CRC = पूरा remainder; Checksum = योग; Hamming = कई parity bits.*

*[Source: CN Topic Test-04.pdf]*

---
### Q35. Which error detection method consists of a parity bit for each data unit as well as an entire data unit of parity bits?

<span lang='hi'>किस error detection method में हर data unit के लिए एक parity bit के साथ-साथ parity bits का पूरा data unit भी होता है?</span>

- **(A)** Simple parity check / Simple parity check
- **(B)** CRC / CRC
- **(C)** Two-dimensional parity check / Two-dimensional parity check ✅ **(CORRECT)**
- **(D)** Checksum / Checksum

**✔ Correct Answer: (C) Two-dimensional parity check** — Two-dimensional parity check में हर row और column की parity बनती है — इसलिए parity bits का पूरा अतिरिक्त unit जुड़ता है. यह कुछ errors correct भी कर सकता है.

*Two-dimensional parity check में हर row और column की parity बनती है — इसलिए parity bits का पूरा अतिरिक्त unit जुड़ता है. यह कुछ errors correct भी कर सकता है.*

**★ Nukta (Key Point):** 2D parity = rows + columns दोनों की parity; simple parity = बस एक bit.

*2D parity = rows + columns दोनों की parity; simple parity = बस एक bit.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p7]*

---
### Q36. A simple parity-check code can detect:

<span lang='hi'>एक simple parity-check code detect कर सकता है:</span>

- **(A)** odd number of errors / odd number of errors ✅ **(CORRECT)**
- **(B)** even number of errors / even number of errors
- **(C)** positive number of errors / positive number of errors
- **(D)** negative number of errors / negative number of errors

**✔ Correct Answer: (A) odd number of errors** — Simple parity में odd संख्या में bit errors पलटने पर parity बदल जाती है और error पकड़ में आता है; even errors छिप जाते हैं.

*Simple parity में odd संख्या में bit errors पलटने पर parity बदल जाती है और error पकड़ में आता है; even errors छिप जाते हैं.*

**★ Nukta (Key Point):** Parity = odd errors पकड़ता है; even छोड़ देता है — यही इसकी सीमा है.

*Parity = odd errors पकड़ता है; even छोड़ देता है — यही इसकी सीमा है.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p34]*

---
### Q37. Which of the following is an error detection technique?

<span lang='hi'>निम्न में से कौन-सी error detection technique है?</span>

- **(A)** ARQ / ARQ
- **(B)** Parity Bit / Parity Bit ✅ **(CORRECT)**
- **(C)** Stop-and-Wait / Stop-and-Wait
- **(D)** Sliding Window / Sliding Window

**✔ Correct Answer: (B) Parity Bit** — Parity Bit एक error detection technique है. ARQ, Stop-and-Wait और Sliding Window flow/error control के protocols हैं, detection techniques नहीं.

*Parity Bit एक error detection technique है. ARQ, Stop-and-Wait और Sliding Window flow/error control के protocols हैं, detection techniques नहीं.*

**★ Nukta (Key Point):** Detection techniques: Parity, CRC, Checksum. Control protocols: SW, GBN, SR.

*Detection techniques: Parity, CRC, Checksum. Control protocols: SW, GBN, SR.*

*[Source: CN Topic Test-04.pdf]*

---
### Q38. The message 1001 is to be transmitted using the CRC polynomial x³ + x + 1 to protect it from errors. The codeword that should be transmitted is:

<span lang='hi'>संदेश 1001 को CRC बहुपद x³ + x + 1 से errors से बचाने के लिए भेजना है. भेजा जाने वाला codeword होगा:</span>

- **(A)** 1001100 / 1001100
- **(B)** 1001011 / 1001011
- **(C)** 1001110 / 1001110 ✅ **(CORRECT)**
- **(D)** 1001000 / 1001000

**✔ Correct Answer: (C) 1001110** — Divisor x³+x+1 = 1011. Message के आगे 3 zeros लगाकर 1001000 को 1011 से भाग दो → remainder 110. यही remainder जोड़ने पर codeword = 1001110.

*Divisor x³+x+1 = 1011. Message के आगे 3 zeros लगाकर 1001000 को 1011 से भाग दो → remainder 110. यही remainder जोड़ने पर codeword = 1001110.*

**★ Nukta (Key Point):** CRC: degree n के polynomial पर n zeros append → भाग का remainder जोड़ो. यहाँ degree 3 → 3 zeros.

*CRC: degree n के polynomial पर n zeros append → भाग का remainder जोड़ो. यहाँ degree 3 → 3 zeros.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q39. The checksum is used in the Internet by several protocols although not at the ______ layer.

<span lang='hi'>Internet में checksum कई protocols उपयोग करते हैं, हालाँकि ______ layer पर नहीं.</span>

- **(A)** data link / data link ✅ **(CORRECT)**
- **(B)** transport / transport
- **(C)** network / network
- **(D)** none of the above / none of the above

**✔ Correct Answer: (A) data link** — Data link layer पर CRC (FCS) उपयोग होता है, checksum नहीं. Checksum IP, TCP और UDP headers में होता है.

*Data link layer पर CRC (FCS) उपयोग होता है, checksum नहीं. Checksum IP, TCP और UDP headers में होता है.*

**★ Nukta (Key Point):** DLL = CRC; Network/Transport = checksum. यही फ़र्क पूछा जाता है.

*DLL = CRC; Network/Transport = checksum. यही फ़र्क पूछा जाता है.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p33]*

---
### Q40. High-level Data Link Control (HDLC) is a protocol for communication over point-to-point and multipoint links. HDLC is a ______ protocol.

<span lang='hi'>High-level Data Link Control (HDLC) point-to-point और multipoint links पर communication का protocol है. HDLC एक ______ protocol है.</span>

- **(A)** byte-oriented / byte-oriented
- **(B)** character-oriented / character-oriented
- **(C)** bit-oriented / bit-oriented ✅ **(CORRECT)**
- **(D)** none of the above / none of the above

**✔ Correct Answer: (C) bit-oriented** — HDLC bit-oriented protocol है — इसमें flag 01111110 होती है और data में bit stuffing होती है.

*HDLC bit-oriented protocol है — इसमें flag 01111110 होती है और data में bit stuffing होती है.*

**★ Nukta (Key Point):** HDLC/SDLC = bit-oriented; PPP = byte-oriented. यह जोड़ी याद रखो.

*HDLC/SDLC = bit-oriented; PPP = byte-oriented. यह जोड़ी याद रखो.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p15]*

---
### Q41. The most common protocol for point-to-point access is the Point-to-Point Protocol (PPP), which is a ______ protocol.

<span lang='hi'>Point-to-point access का सबसे सामान्य protocol Point-to-Point Protocol (PPP) है, जो एक ______ protocol है.</span>

- **(A)** bit-oriented / bit-oriented
- **(B)** byte-oriented / byte-oriented ✅ **(CORRECT)**
- **(C)** character-oriented / character-oriented
- **(D)** none of the above / none of the above

**✔ Correct Answer: (B) byte-oriented** — PPP byte-oriented protocol है — frames byte की सीमा पर बनते हैं (HDLC के उलट).

*PPP byte-oriented protocol है — frames byte की सीमा पर बनते हैं (HDLC के उलट).*

**★ Nukta (Key Point):** PPP = byte-oriented (flag = 0x7E); HDLC = bit-oriented. परीक्षा में यह जोड़ी कई बार आ चुकी है.

*PPP = byte-oriented (flag = 0x7E); HDLC = bit-oriented. परीक्षा में यह जोड़ी कई बार आ चुकी है.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p16]*

---
### Q42. Which of the following is NOT a responsibility of the network layer?

<span lang='hi'>निम्न में से कौन-सा network layer की ज़िम्मेदारी नहीं है?</span>

- **(A)** Congestion control / Congestion control
- **(B)** Error control / Error control ✅ **(CORRECT)**
- **(C)** Routing / Routing
- **(D)** Inter-networking / Inter-networking

**✔ Correct Answer: (B) Error control** — Error control Data Link और Transport layers संभालते हैं. Network layer routing, forwarding, congestion control और inter-networking करता है.

*Error control Data Link और Transport layers संभालते हैं. Network layer routing, forwarding, congestion control और inter-networking करता है.*

**★ Nukta (Key Point):** Network layer = रास्ता + congestion; error control यहाँ नहीं.

*Network layer = रास्ता + congestion; error control यहाँ नहीं.*

*[Source: CN Topic Test-02.pdf]*

---
### Q43. The types of data services offered by an LLC (Logical Link Control) layer are:

<span lang='hi'>LLC (Logical Link Control) layer द्वारा दी जाने वाली data services के प्रकार हैं:</span>

- **(A)** Connectionless (fast and unreliable) / Connectionless (fast and unreliable)
- **(B)** Connection-oriented (slow and reliable) / Connection-oriented (slow and reliable)
- **(C)** Both A and B / Both A and B ✅ **(CORRECT)**
- **(D)** None of the above / None of the above

**✔ Correct Answer: (C) Both A and B** — LLC दोनों तरह की services देता है — connectionless (तेज़, unreliable) और connection-oriented (भरोसेमंद).

*LLC दोनों तरह की services देता है — connectionless (तेज़, unreliable) और connection-oriented (भरोसेमंद).*

**★ Nukta (Key Point):** LLC types: 1 (connectionless), 2 (connection-oriented), 3 (acknowledged connectionless).

*LLC types: 1 (connectionless), 2 (connection-oriented), 3 (acknowledged connectionless).*

*[Source: Unit Test -2 Solutions.pdf (OCR), p32]*

---
### Q44. Which protocol allows the sender to transmit multiple frames before needing an acknowledgment?

<span lang='hi'>कौन-सा protocol sender को acknowledgment की ज़रूरत से पहले कई frames भेजने देता है?</span>

- **(A)** Stop-and-Wait / Stop-and-Wait
- **(B)** Go-Back-N / Go-Back-N ✅ **(CORRECT)**
- **(C)** ALOHA / ALOHA
- **(D)** CSMA/CD / CSMA/CD

**✔ Correct Answer: (B) Go-Back-N** — Go-Back-N (और Selective Repeat) sliding window protocols हैं जो कई frames एक साथ भेजते हैं.

*Go-Back-N (और Selective Repeat) sliding window protocols हैं जो कई frames एक साथ भेजते हैं.*

**★ Nukta (Key Point):** Sliding window = कई outstanding frames; Stop-and-Wait = एक.

*Sliding window = कई outstanding frames; Stop-and-Wait = एक.*

*[Source: CN Topic Test-04.pdf]*

---

## Section B — Data Link Layer: Framing & MAC Sub-layer

*Framing, bit/byte stuffing, Ethernet frame format, CSMA/CD-CA, ALOHA, token & reservation access, client-server basics.*

### Q45. Why is bit stuffing required in bit-oriented protocols?

<span lang='hi'>Bit-oriented protocols में bit stuffing क्यों ज़रूरी है?</span>

- **(A)** To increase bandwidth / To increase bandwidth
- **(B)** To prevent confusion between data and the flag / To prevent confusion between data and the flag ✅ **(CORRECT)**
- **(C)** To reduce collisions / To reduce collisions
- **(D)** To detect errors / To detect errors

**✔ Correct Answer: (B) To prevent confusion between data and the flag** — Flag pattern (जैसे HDLC की 01111110) data में भी आ सकती है — confusion रोकने के लिए data में हर पाँच 1s के बाद एक 0 ठूँस दिया जाता है (bit stuffing).

*Flag pattern (जैसे HDLC की 01111110) data में भी आ सकती है — confusion रोकने के लिए data में हर पाँच 1s के बाद एक 0 ठूँस दिया जाता है (bit stuffing).*

**★ Nukta (Key Point):** Bit stuffing = data को flag से अलग पहचान दिलाना.

*Bit stuffing = data को flag से अलग पहचान दिलाना.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q46. Bit stuffing refers to:

<span lang='hi'>Bit stuffing का अर्थ है:</span>

- **(A)** Inserting a '0' in the user stream to differentiate it from the flag / Inserting a '0' in the user stream to differentiate it from the flag ✅ **(CORRECT)**
- **(B)** Inserting a '0' in the flag stream to avoid ambiguity / Inserting a '0' in the flag stream to avoid ambiguity
- **(C)** Appending a nibble to the flag sequence / Appending a nibble to the flag sequence
- **(D)** Appending a nibble to the user data stream / Appending a nibble to the user data stream

**✔ Correct Answer: (A) Inserting a '0' in the user stream to differentiate it from the flag** — User (data) stream में पाँच लगातार 1s के बाद एक 0 जोड़ा जाता है ताकि data, flag से अलग पहचाना जा सके.

*User (data) stream में पाँच लगातार 1s के बाद एक 0 जोड़ा जाता है ताकि data, flag से अलग पहचाना जा सके.*

**★ Nukta (Key Point):** Stuffing हमेशा DATA में होती है, flag में नहीं; byte stuffing में 0x7E के बाद 0x7D जुड़ता है.

*Stuffing हमेशा DATA में होती है, flag में नहीं; byte stuffing में 0x7E के बाद 0x7D जुड़ता है.*

*[Source: Unit Test-4 Solution.pdf (OCR), p26]*

---
### Q47. In Ethernet CSMA/CD, the special sequence transmitted by media access management to handle a collision is called:

<span lang='hi'>Ethernet CSMA/CD में collision संभालने के लिए media access management द्वारा भेजा गया विशेष sequence कहलाता है:</span>

- **(A)** Preamble / Preamble
- **(B)** Postamble / Postamble
- **(C)** Jam signal / Jam signal ✅ **(CORRECT)**
- **(D)** None of these / None of these

**✔ Correct Answer: (C) Jam signal** — Collision detect होते ही सभी stations एक Jam signal भेजते हैं ताकि बाकी stations तुरंत जान जाएँ और line खाली हो.

*Collision detect होते ही सभी stations एक Jam signal भेजते हैं ताकि बाकी stations तुरंत जान जाएँ और line खाली हो.*

**★ Nukta (Key Point):** Jam = 'टकराव हो गया!' का सायरन. Preamble = frame शुरू होने की घोषणा.

*Jam = 'टकराव हो गया!' का सायरन. Preamble = frame शुरू होने की घोषणा.*

*[Source: Unit Test-4 Solution.pdf (OCR), p28]*

---
### Q48. The correct order of fields in an Ethernet frame is:

<span lang='hi'>Ethernet frame में fields का सही क्रम है:</span>

- **(A)** Preamble → Destination MAC → Source MAC → Type/Length → Data → FCS / Preamble → Destination MAC → Source MAC → Type/Length → Data → FCS ✅ **(CORRECT)**
- **(B)** Destination MAC → Source MAC → FCS → Data → Preamble / Destination MAC → Source MAC → FCS → Data → Preamble
- **(C)** Source MAC → Destination MAC → Data → CRC → Type / Source MAC → Destination MAC → Data → CRC → Type
- **(D)** Preamble → Source MAC → Destination MAC → Data / Preamble → Source MAC → Destination MAC → Data

**✔ Correct Answer: (A) Preamble → Destination MAC → Source MAC → Type/Length → Data → FCS** — Ethernet frame: Preamble+SFD, फिर Destination MAC, Source MAC, Type/Length, Data (46–1500 bytes), और अंत में FCS (CRC).

*Ethernet frame: Preamble+SFD, फिर Destination MAC, Source MAC, Type/Length, Data (46–1500 bytes), और अंत में FCS (CRC).*

**★ Nukta (Key Point):** याद रखो: Preamble के बाद पहले RECEIVER का पता (Destination), फिर भेजने वाले का — बाकी बाद में.

*याद रखो: Preamble के बाद पहले RECEIVER का पता (Destination), फिर भेजने वाले का — बाकी बाद में.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q49. The minimum size of an Ethernet frame (excluding preamble) is:

<span lang='hi'>Ethernet frame का न्यूनतम आकार (preamble को छोड़कर) होता है:</span>

- **(A)** 46 bytes / 46 bytes
- **(B)** 64 bytes / 64 bytes ✅ **(CORRECT)**
- **(C)** 72 bytes / 72 bytes
- **(D)** 1518 bytes / 1518 bytes

**✔ Correct Answer: (B) 64 bytes** — Ethernet frame का न्यूनतम आकार 64 bytes होता है (14 header + 46 data + 4 FCS).

*Ethernet frame का न्यूनतम आकार 64 bytes होता है (14 header + 46 data + 4 FCS).*

**★ Nukta (Key Point):** 64 = minimum frame; 1518 = maximum frame; 46 = सिर्फ data का minimum.

*64 = minimum frame; 1518 = maximum frame; 46 = सिर्फ data का minimum.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q50. The data field size in an Ethernet frame ranges from:

<span lang='hi'>Ethernet frame में data field का आकार रहता है:</span>

- **(A)** 64–1518 bytes / 64–1518 bytes
- **(B)** 46–1500 bytes / 46–1500 bytes ✅ **(CORRECT)**
- **(C)** 40–1480 bytes / 40–1480 bytes
- **(D)** 32–1500 bytes / 32–1500 bytes

**✔ Correct Answer: (B) 46–1500 bytes** — Data field 46 bytes से 1500 bytes तक होता है (1500 = Ethernet MTU).

*Data field 46 bytes से 1500 bytes तक होता है (1500 = Ethernet MTU).*

**★ Nukta (Key Point):** पूरे frame का range 64–1518; data का 46–1500. यह जोड़ी अक्सर पूछी जाती है.

*पूरे frame का range 64–1518; data का 46–1500. यह जोड़ी अक्सर पूछी जाती है.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q51. What is the MTU size for Ethernet?

<span lang='hi'>Ethernet के लिए MTU आकार कितना है?</span>

- **(A)** 1024 bytes / 1024 bytes
- **(B)** 1500 bytes / 1500 bytes ✅ **(CORRECT)**
- **(C)** 512 bytes / 512 bytes
- **(D)** 2048 bytes / 2048 bytes

**✔ Correct Answer: (B) 1500 bytes** — Ethernet की MTU (Maximum Transmission Unit) 1500 bytes होती है — यानी data field में अधिकतम इतना data.

*Ethernet की MTU (Maximum Transmission Unit) 1500 bytes होती है — यानी data field में अधिकतम इतना data.*

**★ Nukta (Key Point):** MTU = data की सीमा; 1518 = पूरे frame की सीमा. भ्रम में मत आना.

*MTU = data की सीमा; 1518 = पूरे frame की सीमा. भ्रम में मत आना.*

*[Source: CN Topic Test 5.pdf]*

---
### Q52. In Ethernet, the minimum frame size is fixed mainly to:

<span lang='hi'>Ethernet में न्यूनतम frame आकार मुख्य रूप से किसलिए तय किया गया है?</span>

- **(A)** Improve throughput / Improve throughput
- **(B)** Reduce overhead / Reduce overhead
- **(C)** Detect collisions using CSMA/CD / Detect collisions using CSMA/CD ✅ **(CORRECT)**
- **(D)** Increase security / Increase security

**✔ Correct Answer: (C) Detect collisions using CSMA/CD** — CSMA/CD में sender को transmission के दौरान collision detect करना होता है — इसलिए frame इतना बड़ा होना चाहिए कि signal round-trip पूरा कर सके. 64 bytes की यही सीमा है.

*CSMA/CD में sender को transmission के दौरान collision detect करना होता है — इसलिए frame इतना बड़ा होना चाहिए कि signal round-trip पूरा कर सके. 64 bytes की यही सीमा है.*

**★ Nukta (Key Point):** Round-trip time (slot time) तक frame ज़िंदा रहे — तभी collision पकड़ी जाएगी.

*Round-trip time (slot time) तक frame ज़िंदा रहे — तभी collision पकड़ी जाएगी.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q53. Collision detection and avoidance mechanisms are implemented in:

<span lang='hi'>Collision detection और avoidance mechanisms कहाँ लागू होते हैं?</span>

- **(A)** LLC Sublayer / LLC Sublayer
- **(B)** Network Layer / Network Layer
- **(C)** MAC Sublayer / MAC Sublayer ✅ **(CORRECT)**
- **(D)** Physical Layer / Physical Layer

**✔ Correct Answer: (C) MAC Sublayer** — MAC (Media Access Control) sub-layer ही medium तक पहुँच का नियम बनाता है — CSMA/CD, CSMA/CA आदि यहीं लागू होते हैं.

*MAC (Media Access Control) sub-layer ही medium तक पहुँच का नियम बनाता है — CSMA/CD, CSMA/CA आदि यहीं लागू होते हैं.*

**★ Nukta (Key Point):** MAC = Medium Access Control — नाम में ही 'medium access' लिखा है.

*MAC = Medium Access Control — नाम में ही 'medium access' लिखा है.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q54. What is the primary function of the MAC sublayer?

<span lang='hi'>MAC sublayer का मुख्य काम क्या है?</span>

- **(A)** Routing / Routing
- **(B)** Error checking / Error checking
- **(C)** Addressing / Addressing
- **(D)** Channel access / Channel access ✅ **(CORRECT)**

**✔ Correct Answer: (D) Channel access** — MAC sub-layer का मुख्य काम channel (medium) तक पहुँच नियंत्रित करना है — कब कौन भेजेगा.

*MAC sub-layer का मुख्य काम channel (medium) तक पहुँच नियंत्रित करना है — कब कौन भेजेगा.*

**★ Nukta (Key Point):** MAC = addressing + channel access; पर परीक्षा में 'primary function' = channel access.

*MAC = addressing + channel access; पर परीक्षा में 'primary function' = channel access.*

*[Source: CN Topic Test-04.pdf]*

---
### Q55. Which protocol requires time synchronization among nodes?

<span lang='hi'>किस protocol में nodes के बीच time synchronization चाहिए होती है?</span>

- **(A)** Pure ALOHA / Pure ALOHA
- **(B)** Slotted ALOHA / Slotted ALOHA ✅ **(CORRECT)**
- **(C)** CSMA / CSMA
- **(D)** CSMA/CD / CSMA/CD

**✔ Correct Answer: (B) Slotted ALOHA** — Slotted ALOHA में time को slots में बाँटा जाता है और transmission सिर्फ slot की शुरुआत में होती है — इसलिए सभी nodes synchronized होने चाहिए.

*Slotted ALOHA में time को slots में बाँटा जाता है और transmission सिर्फ slot की शुरुआत में होती है — इसलिए सभी nodes synchronized होने चाहिए.*

**★ Nukta (Key Point):** Pure ALOHA = जब मन चाहे भेजो; Slotted = slot की घड़ी देखकर भेजो.

*Pure ALOHA = जब मन चाहे भेजो; Slotted = slot की घड़ी देखकर भेजो.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q56. The vulnerable period of Pure ALOHA is:

<span lang='hi'>Pure ALOHA का vulnerable period होता है:</span>

- **(A)** T / T
- **(B)** 2T / 2T ✅ **(CORRECT)**
- **(C)** T/2 / T/2
- **(D)** 4T / 4T

**✔ Correct Answer: (B) 2T** — Pure ALOHA में कोई भी frame T समय तक टकरा सकता है — vulnerable period 2T होता है (इसीलिए efficiency G·e⁻²ᴳ, अधिकतम ~18.4%).

*Pure ALOHA में कोई भी frame T समय तक टकरा सकता है — vulnerable period 2T होता है (इसीलिए efficiency G·e⁻²ᴳ, अधिकतम ~18.4%).*

**★ Nukta (Key Point):** Pure ALOHA: 2T और G·e⁻²ᴳ (~18.4%); Slotted ALOHA: T और G·e⁻ᴳ (~36.8%).

*Pure ALOHA: 2T और G·e⁻²ᴳ (~18.4%); Slotted ALOHA: T और G·e⁻ᴳ (~36.8%).*

*[Source: BCI Subject Test-9.pdf]*

---
### Q57. In a slotted ALOHA with G stations attempting to transmit in one slot, the throughput is equal to:

<span lang='hi'>Slotted ALOHA में एक slot में G stations transmit करने का प्रयास करें तो throughput होगा:</span>

- **(A)** G × e⁻ᴳ / G × e⁻ᴳ ✅ **(CORRECT)**
- **(B)** 2G × e⁻ᴳ / 2G × e⁻ᴳ
- **(C)** e⁻ᴳ / e⁻ᴳ
- **(D)** G × e⁻²ᴳ / G × e⁻²ᴳ

**✔ Correct Answer: (A) G × e⁻ᴳ** — Slotted ALOHA की throughput = G·e⁻ᴳ है (अधिकतम 1/e ≈ 36.8% जब G = 1).

*Slotted ALOHA की throughput = G·e⁻ᴳ है (अधिकतम 1/e ≈ 36.8% जब G = 1).*

**★ Nukta (Key Point):** RPSC official key (a). Pure ALOHA का formula G·e⁻²ᴳ है — मिलाकर मत पढ़ना.

*RPSC official key (a). Pure ALOHA का formula G·e⁻²ᴳ है — मिलाकर मत पढ़ना.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q58. Which protocol has the highest efficiency under heavy load?

<span lang='hi'>भारी load पर किस protocol की efficiency सबसे अधिक होती है?</span>

- **(A)** Pure ALOHA / Pure ALOHA
- **(B)** Slotted ALOHA / Slotted ALOHA
- **(C)** CSMA / CSMA
- **(D)** CSMA/CD / CSMA/CD ✅ **(CORRECT)**

**✔ Correct Answer: (D) CSMA/CD** — CSMA/CD (Ethernet) carrier sense और collision detection से medium का उपयोग सबसे कुशल करता है — heavy load पर सबसे अच्छा.

*CSMA/CD (Ethernet) carrier sense और collision detection से medium का उपयोग सबसे कुशल करता है — heavy load पर सबसे अच्छा.*

**★ Nukta (Key Point):** क्रम: CSMA/CD > CSMA > Slotted ALOHA > Pure ALOHA.

*क्रम: CSMA/CD > CSMA > Slotted ALOHA > Pure ALOHA.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q59. Which protocol detects collisions while transmission is in progress?

<span lang='hi'>कौन-सा protocol transmission के दौरान ही collisions detect करता है?</span>

- **(A)** CSMA / CSMA
- **(B)** Slotted ALOHA / Slotted ALOHA
- **(C)** CSMA/CD / CSMA/CD ✅ **(CORRECT)**
- **(D)** CSMA/CA / CSMA/CA

**✔ Correct Answer: (C) CSMA/CD** — CSMA/CD = Carrier Sense Multiple Access with Collision Detection — transmission चलते समय ही voltage बढ़ने से collision पकड़ लेता है.

*CSMA/CD = Carrier Sense Multiple Access with Collision Detection — transmission चलते समय ही voltage बढ़ने से collision पकड़ लेता है.*

**★ Nukta (Key Point):** CD = detect-and-jam; CA = avoid (RTS/CTS) — wireless में.

*CD = detect-and-jam; CA = avoid (RTS/CTS) — wireless में.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q60. What is the primary role of CSMA/CD in Ethernet?

<span lang='hi'>Ethernet में CSMA/CD की मुख्य भूमिका क्या है?</span>

- **(A)** Error correction / Error correction
- **(B)** Collision detection / Collision detection ✅ **(CORRECT)**
- **(C)** Address resolution / Address resolution
- **(D)** Flow control / Flow control

**✔ Correct Answer: (B) Collision detection** — CSMA/CD का काम collisions का पता लगाकर उन्हें संभालना है — ताकि shared medium पर frames टकराएँ नहीं या टकराने पर दोबारा भेजे जाएँ.

*CSMA/CD का काम collisions का पता लगाकर उन्हें संभालना है — ताकि shared medium पर frames टकराएँ नहीं या टकराने पर दोबारा भेजे जाएँ.*

**★ Nukta (Key Point):** नाम में ही Collision Detection लिखा है.

*नाम में ही Collision Detection लिखा है.*

*[Source: CN Topic Test 5.pdf]*

---
### Q61. Why is CSMA/CD not suitable for wireless networks?

<span lang='hi'>CSMA/CD wireless networks के लिए उपयुक्त क्यों नहीं है?</span>

- **(A)** No random access / No random access
- **(B)** Collision detection is not feasible in wireless / Collision detection is not feasible in wireless ✅ **(CORRECT)**
- **(C)** High bandwidth requirement / High bandwidth requirement
- **(D)** Requires slot synchronization / Requires slot synchronization

**✔ Correct Answer: (B) Collision detection is not feasible in wireless** — Wireless में station अपना signal सुनकर दूसरे की collision detect नहीं कर पाता (hidden node problem) — इसलिए wireless में CSMA/CA उपयोग होता है.

*Wireless में station अपना signal सुनकर दूसरे की collision detect नहीं कर पाता (hidden node problem) — इसलिए wireless में CSMA/CA उपयोग होता है.*

**★ Nukta (Key Point):** Wired = CSMA/CD; Wireless = CSMA/CA. यह जोड़ी पक्की याद रखो.

*Wired = CSMA/CD; Wireless = CSMA/CA. यह जोड़ी पक्की याद रखो.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q62. Which mechanism is used by CSMA/CA to reduce collisions?

<span lang='hi'>CSMA/CA collisions कम करने के लिए कौन-सा mechanism उपयोग करता है?</span>

- **(A)** Collision detection / Collision detection
- **(B)** Slot restriction / Slot restriction
- **(C)** RTS/CTS handshake / RTS/CTS handshake ✅ **(CORRECT)**
- **(D)** Jam signal / Jam signal

**✔ Correct Answer: (C) RTS/CTS handshake** — CSMA/CA में RTS/CTS (Request to Send / Clear to Send) handshake से stations बारी-बारी medium लेती हैं और collisions कम होती हैं (Wi-Fi में).

*CSMA/CA में RTS/CTS (Request to Send / Clear to Send) handshake से stations बारी-बारी medium लेती हैं और collisions कम होती हैं (Wi-Fi में).*

**★ Nukta (Key Point):** CA = Collision Avoidance — टकराव रोकना, पकड़ना नहीं.

*CA = Collision Avoidance — टकराव रोकना, पकड़ना नहीं.*

*[Source: BCI Subject Test-9.pdf]*

---
### Q63. Which of the following Multiple Access Protocols is not suitable for wired networks?

<span lang='hi'>निम्न में से कौन-सा Multiple Access Protocol wired networks के लिए उपयुक्त नहीं है?</span>

- **(A)** CSMA/CD / CSMA/CD
- **(B)** TDMA / TDMA
- **(C)** Token passing / Token passing
- **(D)** CSMA/CA / CSMA/CA ✅ **(CORRECT)**

**✔ Correct Answer: (D) CSMA/CA** — CSMA/CA wireless (Wi-Fi) के लिए बना है; wired Ethernet में CSMA/CD उपयोग होता है.

*CSMA/CA wireless (Wi-Fi) के लिए बना है; wired Ethernet में CSMA/CD उपयोग होता है.*

**★ Nukta (Key Point):** RPSC official key (d) — wired = CSMA/CD, wireless = CSMA/CA.

*RPSC official key (d) — wired = CSMA/CD, wireless = CSMA/CA.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q64. Network Allocation Vector (NAV) is associated with which of the following MAC technologies?

<span lang='hi'>Network Allocation Vector (NAV) निम्न में से किस MAC technology से जुड़ा है?</span>

- **(A)** Wi-Fi (CSMA/CA) / Wi-Fi (CSMA/CA) ✅ **(CORRECT)**
- **(B)** CSMA/CD / CSMA/CD
- **(C)** Bluetooth / Bluetooth
- **(D)** Ethernet / Ethernet

**✔ Correct Answer: (A) Wi-Fi (CSMA/CA)** — NAV — Wi-Fi (802.11 CSMA/CA) की वह टाइमर है जो बताती है कि medium कितनी देर busy रहेगा; बाकी stations इतनी देर चुप रहते हैं.

*NAV — Wi-Fi (802.11 CSMA/CA) की वह टाइमर है जो बताती है कि medium कितनी देर busy रहेगा; बाकी stations इतनी देर चुप रहते हैं.*

**★ Nukta (Key Point):** RPSC official key (a) — NAV = virtual carrier sensing का हिस्सा.

*RPSC official key (a) — NAV = virtual carrier sensing का हिस्सा.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q65. What is multiple access?

<span lang='hi'>Multiple access क्या है?</span>

- **(A)** Accessing a computer from multiple locations / Accessing a computer from multiple locations
- **(B)** A kind of network (MAN) / A kind of network (MAN)
- **(C)** Sharing of one physical link by more than one station / Sharing of one physical link by more than one station ✅ **(CORRECT)**
- **(D)** None of the above / None of the above

**✔ Correct Answer: (C) Sharing of one physical link by more than one station** — Multiple access का अर्थ है — एक ही physical medium/link कई stations में बाँटा जाए, जैसे ALOHA/CSMA/TDMA.

*Multiple access का अर्थ है — एक ही physical medium/link कई stations में बाँटा जाए, जैसे ALOHA/CSMA/TDMA.*

**★ Nukta (Key Point):** Shared medium को संभालने वाले protocols ही Multiple Access Protocols हैं.

*Shared medium को संभालने वाले protocols ही Multiple Access Protocols हैं.*

*[Source: SSC CGL Internet & Networking (via EduRev bank)]*

---
### Q66. In Reservation mode of MAC, each station in the network ______ a time slot for a finite or infinite amount of time to access the shared medium.

<span lang='hi'>MAC के Reservation mode में network का हर station shared medium तक पहुँचने के लिए एक time slot ______ करता है.</span>

- **(A)** should reserve / should reserve ✅ **(CORRECT)**
- **(B)** need not reserve / need not reserve
- **(C)** Can't say / Can't say
- **(D)** None of the above / None of the above

**✔ Correct Answer: (A) should reserve** — Reservation protocols में stations पहले अपना slot reserve करती हैं, फिर बारी आने पर बिना टकराव के भेजती हैं.

*Reservation protocols में stations पहले अपना slot reserve करती हैं, फिर बारी आने पर बिना टकराव के भेजती हैं.*

**★ Nukta (Key Point):** Reservation = पहले बुकिंग, फिर यात्रा — contention (ALOHA/CSMA) में बुकिंग नहीं.

*Reservation = पहले बुकिंग, फिर यात्रा — contention (ALOHA/CSMA) में बुकिंग नहीं.*

*[Source: Unit Test -2 Solutions.pdf (OCR), p25]*

---
### Q67. A Token Ring implementation works on the ______ mode of medium access.

<span lang='hi'>Token Ring implementation medium access के ______ mode पर काम करती है.</span>

- **(A)** Contention / Contention
- **(B)** Reservation / Reservation
- **(C)** Round Robin / Round Robin ✅ **(CORRECT)**
- **(D)** None of the above / None of the above

**✔ Correct Answer: (C) Round Robin** — Token Ring में token एक-एक station तक घूमता है और जिसके पास token हो वही भेजता है — यह Round Robin (बारी-बारी) तरीका है.

*Token Ring में token एक-एक station तक घूमता है और जिसके पास token हो वही भेजता है — यह Round Robin (बारी-बारी) तरीका है.*

**★ Nukta (Key Point):** MAC तरीके तीन: Contention (ALOHA/CSMA), Reservation, Round Robin (Token).

*MAC तरीके तीन: Contention (ALOHA/CSMA), Reservation, Round Robin (Token).*

*[Source: Unit Test -2 Solutions.pdf (OCR), p26]*

---
### Q68. Which one of the following is not used in media access control?

<span lang='hi'>निम्न में से कौन-सा media access control में उपयोग नहीं होता?</span>

- **(A)** Ethernet / Ethernet
- **(B)** Digital subscriber line (DSL) / Digital subscriber line (DSL) ✅ **(CORRECT)**
- **(C)** FDDI / FDDI
- **(D)** None of the mentioned / None of the mentioned

**✔ Correct Answer: (B) Digital subscriber line (DSL)** — Ethernet और FDDI दोनों अपना MAC protocol उपयोग करते हैं; DSL एक access (last-mile) technology है जिसका अपना MAC sub-layer नहीं होता.

*Ethernet और FDDI दोनों अपना MAC protocol उपयोग करते हैं; DSL एक access (last-mile) technology है जिसका अपना MAC sub-layer नहीं होता.*

**★ Nukta (Key Point):** MAC = LAN की बात; DSL = telephone line पर broadband.

*MAC = LAN की बात; DSL = telephone line पर broadband.*

*[Source: CN Topic Test-01.pdf]*

---
### Q69. Which of the following is an example of Client–Server architecture?

<span lang='hi'>निम्न में से कौन-सा Client–Server architecture का उदाहरण है?</span>

- **(A)** Chat between two Bluetooth devices / Chat between two Bluetooth devices
- **(B)** Web browser accessing a website / Web browser accessing a website ✅ **(CORRECT)**
- **(C)** File transfer via USB cable / File transfer via USB cable
- **(D)** Two laptops connected directly / Two laptops connected directly

**✔ Correct Answer: (B) Web browser accessing a website** — Web browser (client) website के server से request करता है — यही classic client–server model है.

*Web browser (client) website के server से request करता है — यही classic client–server model है.*

**★ Nukta (Key Point):** Client–Server: एक सेवा देता है, दूसरा लेता है. Bluetooth chat = peer-to-peer.

*Client–Server: एक सेवा देता है, दूसरा लेता है. Bluetooth chat = peer-to-peer.*

*[Source: BCI_SCI Subject Test-01 (CN and Security)]*

---

## Section C — Network Layer: IP, ICMP, ARP & Routing Protocols

*IPv4 header & fragmentation, IPv6 fields, logical addressing, ARP/ICMP/IGMP, routing (RIP/OSPF/BGP/MPLS/STP), traceroute, DHCP & probability problems.*

### Q70. What is the function of ARP?

<span lang='hi'>ARP का काम क्या है?</span>

- **(A)** Resolve IP address to MAC address / Resolve IP address to MAC address ✅ **(CORRECT)**
- **(B)** Resolve domain name to IP / Resolve domain name to IP
- **(C)** Encrypt packets / Encrypt packets
- **(D)** Determine the route / Determine the route

**✔ Correct Answer: (A) Resolve IP address to MAC address** — ARP (Address Resolution Protocol) IP address का matching MAC address निकालता है — ताकि frame LAN पर भेजा जा सके.

*ARP (Address Resolution Protocol) IP address का matching MAC address निकालता है — ताकि frame LAN पर भेजा जा सके.*

**★ Nukta (Key Point):** ARP = IP→MAC; DNS = name→IP; RARP = MAC→IP (obsolete).

*ARP = IP→MAC; DNS = name→IP; RARP = MAC→IP (obsolete).*

*[Source: CN Topic Test 6.pdf + Unit Test -2 Solutions.pdf (OCR)]*

---
### Q71. Which tool is used to view the MAC address of a system?

<span lang='hi'>किस system का MAC address देखने के लिए कौन-सा tool उपयोग होता है?</span>

- **(A)** ping / ping
- **(B)** ipconfig /all / ipconfig /all ✅ **(CORRECT)**
- **(C)** netstat / netstat
- **(D)** arp -a / arp -a

**✔ Correct Answer: (B) ipconfig /all** — ipconfig /all चलाने पर 'Physical Address' के रूप में NIC का MAC address दिखता है. (arp -a में पड़ोसियों के MAC दिखते हैं.)

*ipconfig /all चलाने पर 'Physical Address' के रूप में NIC का MAC address दिखता है. (arp -a में पड़ोसियों के MAC दिखते हैं.)*

**★ Nukta (Key Point):** Windows: ipconfig /all; Linux: ip link / ifconfig. दोनों अपना NIC दिखाते हैं.

*Windows: ipconfig /all; Linux: ip link / ifconfig. दोनों अपना NIC दिखाते हैं.*

*[Source: BCI_SCI Subject Test-7.pdf]*

---
### Q72. ICMP is a ............ layer protocol.

<span lang='hi'>ICMP एक ............ layer protocol है.</span>

- **(A)** Data link / Data link
- **(B)** Transport / Transport
- **(C)** Application / Application
- **(D)** Network / Network ✅ **(CORRECT)**

**✔ Correct Answer: (D) Network** — ICMP (Internet Control Message Protocol) Network layer पर काम करता है — ping और error messages इसी से जाते हैं.

*ICMP (Internet Control Message Protocol) Network layer पर काम करता है — ping और error messages इसी से जाते हैं.*

**★ Nukta (Key Point):** RPSC official key (d). ICMP/IP/ARP/IGMP सब Network layer के; TCP/UDP Transport.

*RPSC official key (d). ICMP/IP/ARP/IGMP सब Network layer के; TCP/UDP Transport.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key) + Random Test- Rajasthan PYQ.pdf (OCR)]*

---
### Q73. Which protocol is used for path MTU discovery?

<span lang='hi'>Path MTU discovery के लिए कौन-सा protocol उपयोग होता है?</span>

- **(A)** TCP / TCP
- **(B)** UDP / UDP
- **(C)** ICMP / ICMP ✅ **(CORRECT)**
- **(D)** ARP / ARP

**✔ Correct Answer: (C) ICMP** — Path MTU Discovery में ICMP 'Fragmentation Needed' messages से पता चलता है कि रास्ते की सबसे छोटी MTU क्या है.

*Path MTU Discovery में ICMP 'Fragmentation Needed' messages से पता चलता है कि रास्ते की सबसे छोटी MTU क्या है.*

**★ Nukta (Key Point):** ICMP = network का संदेशवाहक — ping, traceroute, PMTU सब इसी से.

*ICMP = network का संदेशवाहक — ping, traceroute, PMTU सब इसी से.*

*[Source: BCI_SCI Subject Test-7.pdf]*

---
### Q74. Which of the following is NOT a valid ICMP error message?

<span lang='hi'>निम्न में से कौन-सा वैध ICMP error message नहीं है?</span>

- **(A)** Destination Unreachable / Destination Unreachable
- **(B)** Time Exceeded / Time Exceeded
- **(C)** Echo Request / Echo Request ✅ **(CORRECT)**
- **(D)** Port Unreachable / Port Unreachable

**✔ Correct Answer: (C) Echo Request** — Echo Request/Reply ICMP के query messages हैं — error messages नहीं. Destination Unreachable, Time Exceeded आदि error messages हैं.

*Echo Request/Reply ICMP के query messages हैं — error messages नहीं. Destination Unreachable, Time Exceeded आदि error messages हैं.*

**★ Nukta (Key Point):** ICMP errors: Destination Unreachable, Time Exceeded, Source Quench, Redirect. Queries: Echo, Timestamp.

*ICMP errors: Destination Unreachable, Time Exceeded, Source Quench, Redirect. Queries: Echo, Timestamp.*

*[Source: CN Topic Test 5.pdf]*

---
### Q75. What is the function of IGMP in networking?

<span lang='hi'>Networking में IGMP का काम क्या है?</span>

- **(A)** Manage IP address allocation / Manage IP address allocation
- **(B)** Route datagrams / Route datagrams
- **(C)** Manage multicast group membership / Manage multicast group membership ✅ **(CORRECT)**
- **(D)** Handle device discovery / Handle device discovery

**✔ Correct Answer: (C) Manage multicast group membership** — IGMP (Internet Group Management Protocol) multicast groups की membership संभालता है — कौन-सा host किस multicast group में शामिल है.

*IGMP (Internet Group Management Protocol) multicast groups की membership संभालता है — कौन-सा host किस multicast group में शामिल है.*

**★ Nukta (Key Point):** IGMP = multicast की member-list; Network layer protocol.

*IGMP = multicast की member-list; Network layer protocol.*

*[Source: CN Topic Test 5.pdf]*

---
### Q76. Which field in the IP header helps in fragmentation?

<span lang='hi'>IP header में कौन-सा field fragmentation में मदद करता है?</span>

- **(A)** TTL / TTL
- **(B)** Header Length / Header Length
- **(C)** Identification / Identification ✅ **(CORRECT)**
- **(D)** Protocol / Protocol

**✔ Correct Answer: (C) Identification** — Identification field fragmentation में टुकड़ों को एक ही original datagram का हिस्सा पहचानने में मदद करता है.

*Identification field fragmentation में टुकड़ों को एक ही original datagram का हिस्सा पहचानने में मदद करता है.*

**★ Nukta (Key Point):** Fragmentation के तीन tool: Identification + Flags (MF) + Fragment Offset.

*Fragmentation के तीन tool: Identification + Flags (MF) + Fragment Offset.*

*[Source: CN Topic Test 6.pdf]*

---
### Q77. How many bits are there in the 'Fragment Offset' field of the IPv4 header?

<span lang='hi'>IPv4 header के 'Fragment Offset' field में कितने bits होते हैं?</span>

- **(A)** 16 bits / 16 bits
- **(B)** 10 bits / 10 bits
- **(C)** 13 bits / 13 bits ✅ **(CORRECT)**
- **(D)** 32 bits / 32 bits

**✔ Correct Answer: (C) 13 bits** — Fragment Offset 13 bits का होता है — यह बताता है कि टुकड़ा original datagram में कहाँ बैठेगा.

*Fragment Offset 13 bits का होता है — यह बताता है कि टुकड़ा original datagram में कहाँ बैठेगा.*

**★ Nukta (Key Point):** RPSC official key (c). IPv4 header: Version(4)+HLen(4)+ToS(8)+TotalLen(16)+ID(16)+Flags(3)+FragOffset(13)+TTL(8)+...

*RPSC official key (c). IPv4 header: Version(4)+HLen(4)+ToS(8)+TotalLen(16)+ID(16)+Flags(3)+FragOffset(13)+TTL(8)+...*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q78. In IPv4, packet fragmentation and reassembly is handled by:

<span lang='hi'>IPv4 में packet fragmentation और reassembly कैसे होता है?</span>

- **(A)** the More Fragments flag and Fragment Offset field / the More Fragments flag and Fragment Offset field ✅ **(CORRECT)**
- **(B)** the MAC Header / the MAC Header
- **(C)** the Header Checksum / the Header Checksum
- **(D)** encapsulating packets in larger frames / encapsulating packets in larger frames

**✔ Correct Answer: (A) the More Fragments flag and Fragment Offset field** — More Fragments (MF) flag बताता है कि और टुकड़े आने हैं और Fragment Offset बताता है कि टुकड़ा कहाँ रखना है — इन्हीं से reassembly होता है.

*More Fragments (MF) flag बताता है कि और टुकड़े आने हैं और Fragment Offset बताता है कि टुकड़ा कहाँ रखना है — इन्हीं से reassembly होता है.*

**★ Nukta (Key Point):** RPSC official key (a). याद रखो: fragmentation sender/routers करते हैं, reassembly सिर्फ destination host.

*RPSC official key (a). याद रखो: fragmentation sender/routers करते हैं, reassembly सिर्फ destination host.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q79. What is fragmentation in IP networking?

<span lang='hi'>IP networking में fragmentation क्या है?</span>

- **(A)** Splitting data into packets / Splitting data into packets
- **(B)** Splitting large packets so they fit a smaller MTU link / Splitting large packets so they fit a smaller MTU link ✅ **(CORRECT)**
- **(C)** Combining multiple packets / Combining multiple packets
- **(D)** Encrypting packets / Encrypting packets

**✔ Correct Answer: (B) Splitting large packets so they fit a smaller MTU link** — Fragmentation का अर्थ है बड़े packet के छोटे-छोटे टुकड़े करना ताकि वे रास्ते की छोटी MTU वाली link से गुज़र सकें.

*Fragmentation का अर्थ है बड़े packet के छोटे-छोटे टुकड़े करना ताकि वे रास्ते की छोटी MTU वाली link से गुज़र सकें.*

**★ Nukta (Key Point):** Packet बनाना segmentation है; बड़े packet के टुकड़े fragmentation. IPv6 में routers fragmentation नहीं करते.

*Packet बनाना segmentation है; बड़े packet के टुकड़े fragmentation. IPv6 में routers fragmentation नहीं करते.*

*[Source: CN Topic Test 6.pdf]*

---
### Q80. The size of the 'total length field' of an IPv4 datagram is:

<span lang='hi'>IPv4 datagram के 'total length field' का आकार है:</span>

- **(A)** 16 bits / 16 bits ✅ **(CORRECT)**
- **(B)** 32 bits / 32 bits
- **(C)** 8 bits / 8 bits
- **(D)** 4 bits / 4 bits

**✔ Correct Answer: (A) 16 bits** — Total Length field 16 bits का होता है — इसीलिए IPv4 datagram अधिकतम 65535 bytes का हो सकता है.

*Total Length field 16 bits का होता है — इसीलिए IPv4 datagram अधिकतम 65535 bytes का हो सकता है.*

**★ Nukta (Key Point):** RPSC official key (a). 16 bits = 2¹⁶ − 1 = 65535.

*RPSC official key (a). 16 bits = 2¹⁶ − 1 = 65535.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q81. What is the minimum header size of an IPv4 packet?

<span lang='hi'>IPv4 packet का न्यूनतम header आकार कितना है?</span>

- **(A)** 16 bytes / 16 bytes
- **(B)** 10 bytes / 10 bytes
- **(C)** 20 bytes / 20 bytes ✅ **(CORRECT)**
- **(D)** 32 bytes / 32 bytes

**✔ Correct Answer: (C) 20 bytes** — बिना options के IPv4 header 20 bytes का होता है; options जुड़ने पर 60 bytes तक बढ़ सकता है.

*बिना options के IPv4 header 20 bytes का होता है; options जुड़ने पर 60 bytes तक बढ़ सकता है.*

**★ Nukta (Key Point):** 20 bytes = 5 words × 4 bytes — यही Header Length field की न्यूनतम गिनती.

*20 bytes = 5 words × 4 bytes — यही Header Length field की न्यूनतम गिनती.*

*[Source: Networking MCQ bank (MQuestions)]*

---
### Q82. What is the role of the TTL field in an IP packet?

<span lang='hi'>IP packet में TTL field की भूमिका क्या है?</span>

- **(A)** Authentication / Authentication
- **(B)** Packet size control / Packet size control
- **(C)** Packet lifespan control / Packet lifespan control ✅ **(CORRECT)**
- **(D)** Encryption / Encryption

**✔ Correct Answer: (C) Packet lifespan control** — TTL (Time To Live) packet का जीवन-काल है — हर hop पर 1 घटता है; 0 पर packet छोड़ दिया जाता है. इसी से routing loops रुकते हैं.

*TTL (Time To Live) packet का जीवन-काल है — हर hop पर 1 घटता है; 0 पर packet छोड़ दिया जाता है. इसी से routing loops रुकते हैं.*

**★ Nukta (Key Point):** TTL = loop-रोधक. यही traceroute को भी चलाता है (अलग-अलग TTL से path बनता है).

*TTL = loop-रोधक. यही traceroute को भी चलाता है (अलग-अलग TTL से path बनता है).*

*[Source: CN Topic Test 6.pdf]*

---
### Q83. Which field in the IPv4 header indicates the priority of the packet?

<span lang='hi'>IPv4 header में कौन-सा field packet की प्राथमिकता बताता है?</span>

- **(A)** Protocol / Protocol
- **(B)** TTL / TTL
- **(C)** Type of Service (ToS) / Type of Service (ToS) ✅ **(CORRECT)**
- **(D)** Flags / Flags

**✔ Correct Answer: (C) Type of Service (ToS)** — Type of Service (ToS) field quality of service और priority बताती है — किस packet को पहले भेजना है.

*Type of Service (ToS) field quality of service और priority बताती है — किस packet को पहले भेजना है.*

**★ Nukta (Key Point):** ToS बाद में DiffServ/DSCP बना — काम वही: priority/class.

*ToS बाद में DiffServ/DSCP बना — काम वही: priority/class.*

*[Source: CN Topic Test 6.pdf]*

---
### Q84. In the IPv6 header, the traffic class field is similar to which field in the IPv4 header?

<span lang='hi'>IPv6 header में traffic class field, IPv4 header के किस field जैसा है?</span>

- **(A)** Fragmentation field / Fragmentation field
- **(B)** Flow label / Flow label
- **(C)** Type of Service (ToS) field / Type of Service (ToS) field ✅ **(CORRECT)**
- **(D)** Options field / Options field

**✔ Correct Answer: (C) Type of Service (ToS) field** — IPv6 का Traffic Class field IPv4 के ToS जैसा है — दोनों priority/QoS बताते हैं.

*IPv6 का Traffic Class field IPv4 के ToS जैसा है — दोनों priority/QoS बताते हैं.*

**★ Nukta (Key Point):** IPv6 में fragmentation fields ही नहीं हैं — routers टुकड़े नहीं करते.

*IPv6 में fragmentation fields ही नहीं हैं — routers टुकड़े नहीं करते.*

*[Source: Sanfoundry CN MCQs — IPv6]*

---
### Q85. Which of the following uses a logical addressing scheme?

<span lang='hi'>निम्न में से कौन-सा logical addressing scheme उपयोग करता है?</span>

- **(A)** MAC address / MAC address
- **(B)** IP address / IP address ✅ **(CORRECT)**
- **(C)** ARP / ARP
- **(D)** DNS / DNS

**✔ Correct Answer: (B) IP address** — IP address logical (सॉफ़्टवेयर द्वारा नियुक्त) पता है; MAC physical (hardware में बसा) पता. Network layer logical addressing उपयोग करती है.

*IP address logical (सॉफ़्टवेयर द्वारा नियुक्त) पता है; MAC physical (hardware में बसा) पता. Network layer logical addressing उपयोग करती है.*

**★ Nukta (Key Point):** Forouzan का नियम: Data link = physical, Network = logical, Transport = port, Application = specific (name).

*Forouzan का नियम: Data link = physical, Network = logical, Transport = port, Application = specific (name).*

*[Source: CN Topic Test 5.pdf]*

---
### Q86. Which algorithm is used by OSPF to compute the shortest path?

<span lang='hi'>OSPF shortest path निकालने के लिए कौन-सा algorithm उपयोग करता है?</span>

- **(A)** Bellman-Ford / Bellman-Ford
- **(B)** Dijkstra / Dijkstra ✅ **(CORRECT)**
- **(C)** A* / A*
- **(D)** Kruskal / Kruskal

**✔ Correct Answer: (B) Dijkstra** — OSPF (link-state protocol) हर router का पूरा नक्शा रखता है और Dijkstra algorithm से सबसे छोटा रास्ता निकालता है.

*OSPF (link-state protocol) हर router का पूरा नक्शा रखता है और Dijkstra algorithm से सबसे छोटा रास्ता निकालता है.*

**★ Nukta (Key Point):** Link-state = Dijkstra; Distance-vector = Bellman-Ford. यह जोड़ी पक्की.

*Link-state = Dijkstra; Distance-vector = Bellman-Ford. यह जोड़ी पक्की.*

*[Source: CN Topic Test 6.pdf]*

---
### Q87. Which one is a distance-vector routing protocol?

<span lang='hi'>निम्न में से कौन-सा distance-vector routing protocol है?</span>

- **(A)** RIP / RIP ✅ **(CORRECT)**
- **(B)** OSPF / OSPF
- **(C)** BGP / BGP
- **(D)** IS-IS / IS-IS

**✔ Correct Answer: (A) RIP** — RIP (Routing Information Protocol) classic distance-vector protocol है — पड़ोसियों से सुनकर रास्ते तय करता है.

*RIP (Routing Information Protocol) classic distance-vector protocol है — पड़ोसियों से सुनकर रास्ते तय करता है.*

**★ Nukta (Key Point):** RIP = DV (Bellman-Ford); OSPF/IS-IS = Link-state (Dijkstra); BGP = Path-vector.

*RIP = DV (Bellman-Ford); OSPF/IS-IS = Link-state (Dijkstra); BGP = Path-vector.*

*[Source: CN Topic Test 6.pdf]*

---
### Q88. How many maximum hops are allowed in RIP?

<span lang='hi'>RIP में अधिकतम कितने hops की अनुमति है?</span>

- **(A)** 8 / 8
- **(B)** 16 / 16
- **(C)** 15 / 15 ✅ **(CORRECT)**
- **(D)** 32 / 32

**✔ Correct Answer: (C) 15** — RIP में hop count 15 तक मान्य है — 16 का अर्थ 'पहुँच से बाहर'. इसीलिए RIP बड़े networks के लिए नहीं.

*RIP में hop count 15 तक मान्य है — 16 का अर्थ 'पहुँच से बाहर'. इसीलिए RIP बड़े networks के लिए नहीं.*

**★ Nukta (Key Point):** RIP: max 15 hops, metric = hop count, हर 30 sec update.

*RIP: max 15 hops, metric = hop count, हर 30 sec update.*

*[Source: CN Topic Test 6.pdf]*

---
### Q89. How does RIP prevent routing loops? (A) Poison reverse (B) Sequence numbers (C) Split horizon

<span lang='hi'>RIP routing loops कैसे रोकता है? (A) Poison reverse (B) Sequence numbers (C) Split horizon</span>

- **(A)** A only / A only
- **(B)** C only / C only
- **(C)** B only / B only
- **(D)** Both A and C / Both A and C ✅ **(CORRECT)**

**✔ Correct Answer: (D) Both A and C** — Split horizon (जहाँ से सीखा, वहाँ वापस न बताना) और poison reverse (रास्ते को 16 hops घोषित कर देना) — दोनों loop-रोधक तकनीकें हैं.

*Split horizon (जहाँ से सीखा, वहाँ वापस न बताना) और poison reverse (रास्ते को 16 hops घोषित कर देना) — दोनों loop-रोधक तकनीकें हैं.*

**★ Nukta (Key Point):** Loop रोकने के तरीके: split horizon, poison reverse, hold-down timers.

*Loop रोकने के तरीके: split horizon, poison reverse, hold-down timers.*

*[Source: CN Topic Test 6.pdf]*

---
### Q90. What is a major drawback of distance vector routing?

<span lang='hi'>Distance vector routing की एक बड़ी कमी क्या है?</span>

- **(A)** High complexity / High complexity
- **(B)** Count-to-infinity problem / Count-to-infinity problem ✅ **(CORRECT)**
- **(C)** Slow convergence / Slow convergence
- **(D)** Lack of security / Lack of security

**✔ Correct Answer: (B) Count-to-infinity problem** — Distance vector protocols में गलत जानकारी पड़ोसियों से गोल-गोल घूमती रहती है और hop counts बढ़ते जाते हैं — यही count-to-infinity समस्या है.

*Distance vector protocols में गलत जानकारी पड़ोसियों से गोल-गोल घूमती रहती है और hop counts बढ़ते जाते हैं — यही count-to-infinity समस्या है.*

**★ Nukta (Key Point):** DV की पहचान ही count-to-infinity; link-state इससे मुक्त है (पर ज़्यादा memory लेता है).

*DV की पहचान ही count-to-infinity; link-state इससे मुक्त है (पर ज़्यादा memory लेता है).*

*[Source: CN Topic Test 5.pdf]*

---
### Q91. BGP is mainly used for which type of routing, and it belongs to which algorithm family?

<span lang='hi'>BGP मुख्य रूप से किस प्रकार के routing के लिए उपयोग होता है और यह किस algorithm परिवार का है?</span>

- **(A)** Intra-AS routing; link-state / Intra-AS routing; link-state
- **(B)** Inter-AS routing; path-vector (distance-vector family) / Inter-AS routing; path-vector (distance-vector family) ✅ **(CORRECT)**
- **(C)** Static routing; flooding / Static routing; flooding
- **(D)** Host routing; Dijkstra / Host routing; Dijkstra

**✔ Correct Answer: (B) Inter-AS routing; path-vector (distance-vector family)** — BGP (Border Gateway Protocol) अलग-अलग Autonomous Systems के बीच routing करता है (Inter-AS) — यह path-vector protocol है जो distance-vector परिवार से निकला है.

*BGP (Border Gateway Protocol) अलग-अलग Autonomous Systems के बीच routing करता है (Inter-AS) — यह path-vector protocol है जो distance-vector परिवार से निकला है.*

**★ Nukta (Key Point):** AS = Autonomous System. अंदर (AS) OSPF/RIP; बीच में (Inter-AS) BGP — Internet का glue protocol.

*AS = Autonomous System. अंदर (AS) OSPF/RIP; बीच में (Inter-AS) BGP — Internet का glue protocol.*

*[Source: CN Topic Test 5.pdf + CN Topic Test 6.pdf]*

---
### Q92. In the early ARPANET, which routing method was used?

<span lang='hi'>प्रारंभिक ARPANET में कौन-सी routing method उपयोग होती थी?</span>

- **(A)** Distance vector routing / Distance vector routing ✅ **(CORRECT)**
- **(B)** Link state routing / Link state routing
- **(C)** Least cost routing / Least cost routing
- **(D)** Flooding / Flooding

**✔ Correct Answer: (A) Distance vector routing** — ARPANET का पहला (1969) adaptive algorithm distributed distance-vector जैसा था; बाद में (1979) link-state अपनाया गया.

*ARPANET का पहला (1969) adaptive algorithm distributed distance-vector जैसा था; बाद में (1979) link-state अपनाया गया.*

**★ Nukta (Key Point):** इतिहास: ARPANET = distance-vector से शुरू, फिर link-state (OSPF जैसा).

*इतिहास: ARPANET = distance-vector से शुरू, फिर link-state (OSPF जैसा).*

*[Source: Unit Test-4 Solution.pdf (OCR), p8]*

---
### Q93. Dynamic routing protocols enable routers to:

<span lang='hi'>Dynamic routing protocols routers को सक्षम बनाते हैं:</span>

- **(A)** Dynamically discover and maintain routes / Dynamically discover and maintain routes
- **(B)** Distribute routing updates to other routers / Distribute routing updates to other routers
- **(C)** Reach agreement with other routers about network topology / Reach agreement with other routers about network topology
- **(D)** All of the above / All of the above ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the above** — Dynamic routing protocols रास्ते खुद ढूँढते हैं, updates बाँटते हैं और topology पर सहमति बनाते हैं — तीनों काम होते हैं.

*Dynamic routing protocols रास्ते खुद ढूँढते हैं, updates बाँटते हैं और topology पर सहमति बनाते हैं — तीनों काम होते हैं.*

**★ Nukta (Key Point):** Static vs Dynamic: static में admin लिखता है; dynamic में protocol खुद सीखता है.

*Static vs Dynamic: static में admin लिखता है; dynamic में protocol खुद सीखता है.*

*[Source: Unit Test-4 Solution.pdf (OCR), p27]*

---
### Q94. Which of these protocols allows loop-free switching in Layer 2 networks?

<span lang='hi'>निम्न में से कौन-सा protocol Layer 2 networks में loop-free switching देता है?</span>

- **(A)** RIP / RIP
- **(B)** OSPF / OSPF
- **(C)** STP (Spanning Tree Protocol) / STP (Spanning Tree Protocol) ✅ **(CORRECT)**
- **(D)** EIGRP / EIGRP

**✔ Correct Answer: (C) STP (Spanning Tree Protocol)** — STP (Spanning Tree Protocol, 802.1D) अतिरिक्त links को block करके bridged/switched network में loops रोकता है.

*STP (Spanning Tree Protocol, 802.1D) अतिरिक्त links को block करके bridged/switched network में loops रोकता है.*

**★ Nukta (Key Point):** STP = Layer 2 का loop-रोधक; routing protocols Layer 3 के हैं.

*STP = Layer 2 का loop-रोधक; routing protocols Layer 3 के हैं.*

*[Source: CN Topic Test 6.pdf]*

---
### Q95. MPLS operates between which two layers?

<span lang='hi'>MPLS किन दो layers के बीच काम करता है?</span>

- **(A)** Layer 1 and 2 / Layer 1 and 2
- **(B)** Layer 2 and 3 / Layer 2 and 3 ✅ **(CORRECT)**
- **(C)** Layer 3 and 4 / Layer 3 and 4
- **(D)** Layer 4 and 7 / Layer 4 and 7

**✔ Correct Answer: (B) Layer 2 and 3** — MPLS (Multiprotocol Label Switching) packets पर labels लगाकर तेज़ switching करता है — इसलिए इसे Layer 2.5 कहते हैं (Layer 2 और 3 के बीच).

*MPLS (Multiprotocol Label Switching) packets पर labels लगाकर तेज़ switching करता है — इसलिए इसे Layer 2.5 कहते हैं (Layer 2 और 3 के बीच).*

**★ Nukta (Key Point):** MPLS = 'Layer 2.5' — label-based forwarding, IP header देखे बिना.

*MPLS = 'Layer 2.5' — label-based forwarding, IP header देखे बिना.*

*[Source: CN Topic Test 5.pdf]*

---
### Q96. What does the 'traceroute' command do?

<span lang='hi'>'traceroute' command क्या करता है?</span>

- **(A)** Lists all devices on a network / Lists all devices on a network
- **(B)** Tracks the path a packet takes to the destination / Tracks the path a packet takes to the destination ✅ **(CORRECT)**
- **(C)** Resolves domain names / Resolves domain names
- **(D)** Opens ports on the firewall / Opens ports on the firewall

**✔ Correct Answer: (B) Tracks the path a packet takes to the destination** — Traceroute रास्ते के हर router (hop) का पता और delay दिखाता है — अलग-अलग TTL वाले packets भेजकर.

*Traceroute रास्ते के हर router (hop) का पता और delay दिखाता है — अलग-अलग TTL वाले packets भेजकर.*

**★ Nukta (Key Point):** tracert (Windows) ICMP; traceroute (Linux) UDP — काम वही: रास्ता दिखाना.

*tracert (Windows) ICMP; traceroute (Linux) UDP — काम वही: रास्ता दिखाना.*

*[Source: CN Topic Test 5.pdf]*

---
### Q97. Which protocol does traceroute use on UNIX/Linux systems?

<span lang='hi'>UNIX/Linux systems पर traceroute कौन-सा protocol उपयोग करता है?</span>

- **(A)** TCP / TCP
- **(B)** UDP / UDP ✅ **(CORRECT)**
- **(C)** ICMP Echo / ICMP Echo
- **(D)** IGMP / IGMP

**✔ Correct Answer: (B) UDP** — Linux/UNIX का traceroute छोटे TTL वाले UDP packets भेजता है और रास्ते के routers के ICMP 'Time Exceeded' messages से रास्ता बनाता है.

*Linux/UNIX का traceroute छोटे TTL वाले UDP packets भेजता है और रास्ते के routers के ICMP 'Time Exceeded' messages से रास्ता बनाता है.*

**★ Nukta (Key Point):** Windows tracert ICMP भेजता है; Linux traceroute UDP. दोनों का काम एक ही.

*Windows tracert ICMP भेजता है; Linux traceroute UDP. दोनों का काम एक ही.*

*[Source: CN Topic Test 5.pdf]*

---
### Q98. Which command is used to see the routing table in Linux?

<span lang='hi'>Linux में routing table देखने के लिए कौन-सा command उपयोग होती है?</span>

- **(A)** ifconfig / ifconfig
- **(B)** netstat -r / netstat -r ✅ **(CORRECT)**
- **(C)** ping / ping
- **(D)** ipconfig / ipconfig

**✔ Correct Answer: (B) netstat -r** — netstat -r (या ip route / route -n) Linux में routing table दिखाता है.

*netstat -r (या ip route / route -n) Linux में routing table दिखाता है.*

**★ Nukta (Key Point):** Windows: route print; Linux: netstat -r / ip route.

*Windows: route print; Linux: netstat -r / ip route.*

*[Source: CN Topic Test 5.pdf]*

---
### Q99. Which protocol is used for dynamic IP address assignment?

<span lang='hi'>Dynamic IP address assignment के लिए कौन-सा protocol उपयोग होता है?</span>

- **(A)** DNS / DNS
- **(B)** ARP / ARP
- **(C)** DHCP / DHCP ✅ **(CORRECT)**
- **(D)** FTP / FTP

**✔ Correct Answer: (C) DHCP** — DHCP (Dynamic Host Configuration Protocol) नए devices को अपने-आप IP address, subnet mask, gateway और DNS दे देता है.

*DHCP (Dynamic Host Configuration Protocol) नए devices को अपने-आप IP address, subnet mask, gateway और DNS दे देता है.*

**★ Nukta (Key Point):** DHCP = 'Plug and Play' networking — zeroconf का प्रमुख tool.

*DHCP = 'Plug and Play' networking — zeroconf का प्रमुख tool.*

*[Source: CN Topic Test-03.pdf + CN Topic Test 6.pdf]*

---
### Q100. Which of the following protocols may be used as zeroconf and plug-and-play?

<span lang='hi'>निम्न में से कौन-सा protocol zeroconf और plug-and-play के रूप में उपयोग हो सकता है?</span>

- **(A)** TCP / TCP
- **(B)** DHCP / DHCP ✅ **(CORRECT)**
- **(C)** NAT / NAT
- **(D)** ICMP / ICMP

**✔ Correct Answer: (B) DHCP** — DHCP नए host को बिना manual configuration के network से जुड़ने देता है — यही plug-and-play/zeroconf व्यवहार है.

*DHCP नए host को बिना manual configuration के network से जुड़ने देता है — यही plug-and-play/zeroconf व्यवहार है.*

**★ Nukta (Key Point):** RPSC official key (b). Zeroconf = बिना admin के automatic network settings.

*RPSC official key (b). Zeroconf = बिना admin के automatic network settings.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q101. There are n stations in a slotted LAN. Each station attempts to transmit with a probability p in each time slot. The probability that exactly one station transmits in a slot is:

<span lang='hi'>एक slotted LAN में n stations हैं. हर time slot में हर station p प्रायिकता से transmit करने का प्रयास करता है. किसी slot में ठीक एक station transmit करने की प्रायिकता है:</span>

- **(A)** n × p × (1 − p)ⁿ⁻¹ / n × p × (1 − p)ⁿ⁻¹ ✅ **(CORRECT)**
- **(B)** p × (1 − p)ⁿ⁻¹ / p × (1 − p)ⁿ⁻¹
- **(C)** 1 − (1 − p)ⁿ⁻¹ / 1 − (1 − p)ⁿ⁻¹
- **(D)** (1 − p)ⁿ⁻¹ / (1 − p)ⁿ⁻¹

**✔ Correct Answer: (A) n × p × (1 − p)ⁿ⁻¹** — कोई एक station transmit करे (p) और बाकी n−1 न करें (1−p)ⁿ⁻¹; ऐसे n तरीके हैं — इसलिए n·p·(1−p)ⁿ⁻¹.

*कोई एक station transmit करे (p) और बाकी n−1 न करें (1−p)ⁿ⁻¹; ऐसे n तरीके हैं — इसलिए n·p·(1−p)ⁿ⁻¹.*

**★ Nukta (Key Point):** RPSC official key (a). यही binomial का 'exactly one success' formula है.

*RPSC official key (a). यही binomial का 'exactly one success' formula है.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---

## Section D — Transport Layer: TCP/UDP, Ports & Sockets

*Connection-oriented vs connectionless services, sockets, TCP header & states, 3-way handshake, flow & congestion control, security (SYN flood, hijacking).*

### Q102. Which of the following is a connectionless transport service?

<span lang='hi'>निम्न में से कौन-सी connectionless transport service है?</span>

- **(A)** TCP / TCP
- **(B)** ARP / ARP
- **(C)** UDP / UDP ✅ **(CORRECT)**
- **(D)** FTP / FTP

**✔ Correct Answer: (C) UDP** — UDP (User Datagram Protocol) connectionless है — बिना connection बनाए datagrams भेज देता है. TCP connection-oriented है.

*UDP (User Datagram Protocol) connectionless है — बिना connection बनाए datagrams भेज देता है. TCP connection-oriented है.*

**★ Nukta (Key Point):** Transport layer के दो सदस्य: TCP (भरोसेमंद, connection-oriented) और UDP (तेज़, connectionless).

*Transport layer के दो सदस्य: TCP (भरोसेमंद, connection-oriented) और UDP (तेज़, connectionless).*

*[Source: BCI_SCI Subject Test-7.pdf + Oliveboard SSC CGL bank]*

---
### Q103. How many bits are used for port addressing at the transport layer?

<span lang='hi'>Transport layer पर port addressing के लिए कितने bits उपयोग होते हैं?</span>

- **(A)** 8 / 8
- **(B)** 10 / 10
- **(C)** 16 / 16 ✅ **(CORRECT)**
- **(D)** 32 / 32

**✔ Correct Answer: (C) 16** — Port numbers 16 bits के होते हैं — इसीलिए 0 से 65535 तक ports बनते हैं.

*Port numbers 16 bits के होते हैं — इसीलिए 0 से 65535 तक ports बनते हैं.*

**★ Nukta (Key Point):** Addresses का स्तर: Data link = 48-bit MAC; Network = 32-bit IP; Transport = 16-bit port.

*Addresses का स्तर: Data link = 48-bit MAC; Network = 32-bit IP; Transport = 16-bit port.*

*[Source: BCI_SCI Subject Test-7.pdf]*

---
### Q104. What is a socket in networking?

<span lang='hi'>Networking में socket क्या है?</span>

- **(A)** IP address + MAC address / IP address + MAC address
- **(B)** IP address + Port number / IP address + Port number ✅ **(CORRECT)**
- **(C)** MAC address + Port number / MAC address + Port number
- **(D)** IP address + DNS name / IP address + DNS name

**✔ Correct Answer: (B) IP address + Port number** — Socket = IP address + Port number — यही combination एक connection का endpoint पहचानती है.

*Socket = IP address + Port number — यही combination एक connection का endpoint पहचानती है.*

**★ Nukta (Key Point):** Socket pair = (Source IP:Port, Destination IP:Port) — TCP connection इसी से बनती है.

*Socket pair = (Source IP:Port, Destination IP:Port) — TCP connection इसी से बनती है.*

*[Source: CN Topic Test 6.pdf]*

---
### Q105. What term is used for an endpoint in an inter-process communication across a network?

<span lang='hi'>Network पर inter-process communication में endpoint के लिए कौन-सा term उपयोग होता है?</span>

- **(A)** Port / Port
- **(B)** Machine / Machine
- **(C)** Socket / Socket ✅ **(CORRECT)**
- **(D)** Pipe / Pipe

**✔ Correct Answer: (C) Socket** — IPC endpoint socket कहलाता है — दो processes इन्हीं sockets के ज़रिए बात करती हैं.

*IPC endpoint socket कहलाता है — दो processes इन्हीं sockets के ज़रिए बात करती हैं.*

**★ Nukta (Key Point):** Port = address का हिस्सा; Socket = पूरा endpoint (IP+Port).

*Port = address का हिस्सा; Socket = पूरा endpoint (IP+Port).*

*[Source: CN Topic Test-02.pdf]*

---
### Q106. A client opens a TCP connection to a web server on port 80 using source port 49152. What is the complete socket pair?

<span lang='hi'>एक client source port 49152 से port 80 वाले web server को TCP connection खोलता है. पूरा socket pair क्या होगा?</span>

- **(A)** 192.168.1.10:49152 ↔ 172.16.0.5:80 / 192.168.1.10:49152 ↔ 172.16.0.5:80 ✅ **(CORRECT)**
- **(B)** 192.168.1.10:80 ↔ 172.16.0.5:49152 / 192.168.1.10:80 ↔ 172.16.0.5:49152
- **(C)** 49152 ↔ 80 / 49152 ↔ 80
- **(D)** 80 ↔ 49152 / 80 ↔ 49152

**✔ Correct Answer: (A) 192.168.1.10:49152 ↔ 172.16.0.5:80** — Socket pair में पहले जोड़े में client का IP:Port और दूसरे में server का IP:Port होता है — client:49152 ↔ server:80.

*Socket pair में पहले जोड़े में client का IP:Port और दूसरे में server का IP:Port होता है — client:49152 ↔ server:80.*

**★ Nukta (Key Point):** पहचान: client का port ephemeral (बड़ा number), server का port well-known (80).

*पहचान: client का port ephemeral (बड़ा number), server का port well-known (80).*

*[Source: BCI Subject Test-8.pdf]*

---
### Q107. What is the purpose of the SYN flag in TCP?

<span lang='hi'>TCP में SYN flag का उद्देश्य क्या है?</span>

- **(A)** To end a session / To end a session
- **(B)** To initiate (open) a connection / To initiate (open) a connection ✅ **(CORRECT)**
- **(C)** To reset a connection / To reset a connection
- **(D)** For data transmission / For data transmission

**✔ Correct Answer: (B) To initiate (open) a connection** — TCP connection शुरू करने के लिए तीन-तरफ़ा handshake (SYN → SYN-ACK → ACK) होता है — SYN यही connection request है.

*TCP connection शुरू करने के लिए तीन-तरफ़ा handshake (SYN → SYN-ACK → ACK) होता है — SYN यही connection request है.*

**★ Nukta (Key Point):** Flags याद रखो: SYN = शुरुआत; FIN = अंत; RST = रद्द; ACK = पुष्टि.

*Flags याद रखो: SYN = शुरुआत; FIN = अंत; RST = रद्द; ACK = पुष्टि.*

*[Source: CN Topic Test 6.pdf]*

---
### Q108. The three-way handshake mechanism in TCP aims to:

<span lang='hi'>TCP का three-way handshake mechanism किस उद्देश्य से होता है?</span>

- **(A)** Secure the communication / Secure the communication
- **(B)** Send bits from one device to another / Send bits from one device to another
- **(C)** Perform error detection and correction / Perform error detection and correction
- **(D)** Establish a connection and synchronize sequence numbers / Establish a connection and synchronize sequence numbers ✅ **(CORRECT)**

**✔ Correct Answer: (D) Establish a connection and synchronize sequence numbers** — तीन-तरफ़ा handshake से दोनों तरफ़ connection बनती है और sequence numbers का आदान-प्रदान होता है (सिंक्रोनाइज़ेशन).

*तीन-तरफ़ा handshake से दोनों तरफ़ connection बनती है और sequence numbers का आदान-प्रदान होता है (सिंक्रोनाइज़ेशन).*

**★ Nukta (Key Point):** RPSC official key (d). SYN, SYN-ACK, ACK — तीन ही संदेश.

*RPSC official key (d). SYN, SYN-ACK, ACK — तीन ही संदेश.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q109. In which scenario will TCP's three-way handshake fail?

<span lang='hi'>किस स्थिति में TCP का three-way handshake विफल होगा?</span>

- **(A)** Firewall blocks the SYN-ACK / Firewall blocks the SYN-ACK ✅ **(CORRECT)**
- **(B)** High latency / High latency
- **(C)** ACK is slightly delayed / ACK is slightly delayed
- **(D)** Server is busy / Server is busy

**✔ Correct Answer: (A) Firewall blocks the SYN-ACK** — यदि firewall SYN-ACK को रोक दे तो handshake पूरा नहीं होता और connection नहीं बनती.

*यदि firewall SYN-ACK को रोक दे तो handshake पूरा नहीं होता और connection नहीं बनती.*

**★ Nukta (Key Point):** Handshake टूटने का सीधा कारण: संदेशों का न पहुँचना (firewall/filter).

*Handshake टूटने का सीधा कारण: संदेशों का न पहुँचना (firewall/filter).*

*[Source: CN Topic Test 5.pdf]*

---
### Q110. In TCP, which state follows the SYN-SENT state in the normal case?

<span lang='hi'>TCP में सामान्य स्थिति में SYN-SENT के बाद कौन-सी state आती है?</span>

- **(A)** SYN-RECEIVED / SYN-RECEIVED
- **(B)** LISTEN / LISTEN
- **(C)** ESTABLISHED / ESTABLISHED ✅ **(CORRECT)**
- **(D)** CLOSED / CLOSED

**✔ Correct Answer: (C) ESTABLISHED** — SYN भेजने (SYN-SENT) के बाद जब SYN-ACK आता है और ACK भेजा जाता है, connection ESTABLISHED हो जाती है.

*SYN भेजने (SYN-SENT) के बाद जब SYN-ACK आता है और ACK भेजा जाता है, connection ESTABLISHED हो जाती है.*

**★ Nukta (Key Point):** सामान्य क्रम: CLOSED → SYN-SENT → ESTABLISHED. (Simultaneous open में SYN-RECEIVED बीच में आती है.)

*सामान्य क्रम: CLOSED → SYN-SENT → ESTABLISHED. (Simultaneous open में SYN-RECEIVED बीच में आती है.)*

*[Source: CN Topic Test 6.pdf]*

---
### Q111. Which one of the following attacks exploits TCP's three-way handshake?

<span lang='hi'>निम्न में से कौन-सा attack TCP के three-way handshake का फ़ायदा उठाती है?</span>

- **(A)** SYN Flood / SYN Flood ✅ **(CORRECT)**
- **(B)** DNS Spoofing / DNS Spoofing
- **(C)** Man in the Middle / Man in the Middle
- **(D)** ARP Poisoning / ARP Poisoning

**✔ Correct Answer: (A) SYN Flood** — SYN Flood में attacker ढेरों SYN भेजकर half-open connections बना देता है और server के resources खत्म हो जाते हैं.

*SYN Flood में attacker ढेरों SYN भेजकर half-open connections बना देता है और server के resources खत्म हो जाते हैं.*

**★ Nukta (Key Point):** Handshake पर हमला = SYN flood; sequence पर हमला = session hijacking.

*Handshake पर हमला = SYN flood; sequence पर हमला = session hijacking.*

*[Source: CN Topic Test 5.pdf]*

---
### Q112. What type of attack is prevented by using random initial sequence numbers in TCP?

<span lang='hi'>TCP में random initial sequence numbers उपयोग करने से किस प्रकार की attack रुकती है?</span>

- **(A)** Smurf attack / Smurf attack
- **(B)** SYN Flooding / SYN Flooding
- **(C)** TCP session hijacking / TCP session hijacking ✅ **(CORRECT)**
- **(D)** Ping of Death / Ping of Death

**✔ Correct Answer: (C) TCP session hijacking** — Random sequence numbers से attacker अगला sequence number अनुमान नहीं लगा पाता और session hijacking (और spoofed ACK) रुकती है.

*Random sequence numbers से attacker अगला sequence number अनुमान नहीं लगा पाता और session hijacking (और spoofed ACK) रुकती है.*

**★ Nukta (Key Point):** Predictable sequence numbers = session hijacking का दरवाज़ा.

*Predictable sequence numbers = session hijacking का दरवाज़ा.*

*[Source: CN Topic Test 5.pdf]*

---
### Q113. Which field in the TCP header is used for flow control?

<span lang='hi'>TCP header में flow control के लिए कौन-सा field उपयोग होता है?</span>

- **(A)** Window Size / Window Size ✅ **(CORRECT)**
- **(B)** Sequence Number / Sequence Number
- **(C)** Acknowledgment Number / Acknowledgment Number
- **(D)** Checksum / Checksum

**✔ Correct Answer: (A) Window Size** — Window Size field बताता है कि receiver कितने bytes और ले सकता है — यही TCP का flow control है.

*Window Size field बताता है कि receiver कितने bytes और ले सकता है — यही TCP का flow control है.*

**★ Nukta (Key Point):** TCP के दो घरेलू नियंत्रण: Window (flow control) और cwnd (congestion control).

*TCP के दो घरेलू नियंत्रण: Window (flow control) और cwnd (congestion control).*

*[Source: CN Topic Test 6.pdf]*

---
### Q114. Which TCP header field ensures that data arrives in order?

<span lang='hi'>TCP header का कौन-सा field सुनिश्चित करता है कि data क्रम में पहुँचे?</span>

- **(A)** Checksum / Checksum
- **(B)** Flags / Flags
- **(C)** Sequence Number / Sequence Number ✅ **(CORRECT)**
- **(D)** Port Number / Port Number

**✔ Correct Answer: (C) Sequence Number** — हर byte का sequence number होता है — receiver इन्हीं से bytes को सही क्रम में जोड़ता है.

*हर byte का sequence number होता है — receiver इन्हीं से bytes को सही क्रम में जोड़ता है.*

**★ Nukta (Key Point):** UDP में sequence नहीं होता — इसीलिए वहाँ क्रम की guarantee नहीं.

*UDP में sequence नहीं होता — इसीलिए वहाँ क्रम की guarantee नहीं.*

*[Source: CN Topic Test 5.pdf]*

---
### Q115. Which field in the TCP header ensures data integrity?

<span lang='hi'>TCP header का कौन-सा field data integrity सुनिश्चित करता है?</span>

- **(A)** Urgent Pointer / Urgent Pointer
- **(B)** Sequence Number / Sequence Number
- **(C)** Checksum / Checksum ✅ **(CORRECT)**
- **(D)** Acknowledgment Number / Acknowledgment Number

**✔ Correct Answer: (C) Checksum** — Checksum पूरे segment का जोड़ निकालकर integrity जाँचता है — रास्ते में कुछ बदला तो packet छोड़ दिया जाता है.

*Checksum पूरे segment का जोड़ निकालकर integrity जाँचता है — रास्ते में कुछ बदला तो packet छोड़ दिया जाता है.*

**★ Nukta (Key Point):** Integrity = Checksum (TCP/UDP/IP); reliability = ACK + retransmission.

*Integrity = Checksum (TCP/UDP/IP); reliability = ACK + retransmission.*

*[Source: CN Topic Test 5.pdf]*

---
### Q116. Which of the following is NOT a property of TCP?

<span lang='hi'>निम्न में से कौन-सा TCP का गुण नहीं है?</span>

- **(A)** Reliable / Reliable
- **(B)** Ordered delivery / Ordered delivery
- **(C)** Connection-oriented / Connection-oriented
- **(D)** Broadcast / Broadcast ✅ **(CORRECT)**

**✔ Correct Answer: (D) Broadcast** — TCP point-to-point reliable protocol है — broadcast/multicast नहीं करता. Broadcast का काम UDP/UDP-lite जैसे protocols करते हैं.

*TCP point-to-point reliable protocol है — broadcast/multicast नहीं करता. Broadcast का काम UDP/UDP-lite जैसे protocols करते हैं.*

**★ Nukta (Key Point):** TCP = reliable + ordered + connection-oriented; बाकी सब (broadcast) UDP की तरफ़ जाता है.

*TCP = reliable + ordered + connection-oriented; बाकी सब (broadcast) UDP की तरफ़ जाता है.*

*[Source: CN Topic Test 5.pdf]*

---
### Q117. Which of the following provides reliable, connection-oriented communication?

<span lang='hi'>निम्न में से कौन-सा भरोसेमंद, connection-oriented communication देता है?</span>

- **(A)** TCP / TCP ✅ **(CORRECT)**
- **(B)** IP / IP
- **(C)** UDP / UDP
- **(D)** All of the above / All of the above

**✔ Correct Answer: (A) TCP** — TCP ही reliable और connection-oriented transport protocol है.

*TCP ही reliable और connection-oriented transport protocol है.*

**★ Nukta (Key Point):** याद रखो: TCP = phone call (connection + guarantee); UDP = postcard (fast, no promise).

*याद रखो: TCP = phone call (connection + guarantee); UDP = postcard (fast, no promise).*

*[Source: MQuestions DCN bank + Oliveboard SSC CGL bank]*

---
### Q118. TCP initially uses which congestion control technique when a connection starts?

<span lang='hi'>Connection शुरू होने पर TCP शुरू में कौन-सी congestion control technique उपयोग करता है?</span>

- **(A)** Congestion avoidance / Congestion avoidance
- **(B)** Fast recovery / Fast recovery
- **(C)** Slow start / Slow start ✅ **(CORRECT)**
- **(D)** Leaky bucket / Leaky bucket

**✔ Correct Answer: (C) Slow start** — Connection शुरू में TCP Slow start उपयोग करता है — congestion window छोटा रखकर धीरे-धीरे बढ़ाया जाता है.

*Connection शुरू में TCP Slow start उपयोग करता है — congestion window छोटा रखकर धीरे-धीरे बढ़ाया जाता है.*

**★ Nukta (Key Point):** TCP क्रम: Slow start → Congestion avoidance; loss पर → Fast recovery.

*TCP क्रम: Slow start → Congestion avoidance; loss पर → Fast recovery.*

*[Source: CN Topic Test 6.pdf]*

---
### Q119. What is the purpose of TCP's congestion window (cwnd)?

<span lang='hi'>TCP के congestion window (cwnd) का उद्देश्य क्या है?</span>

- **(A)** Track unacknowledged packets / Track unacknowledged packets
- **(B)** Control the sending rate to avoid network congestion / Control the sending rate to avoid network congestion ✅ **(CORRECT)**
- **(C)** Handle encryption / Handle encryption
- **(D)** Prioritize packets / Prioritize packets

**✔ Correct Answer: (B) Control the sending rate to avoid network congestion** — cwnd network की क्षमता के हिसाब से sender की गति नियंत्रित करता है — ज़्यादा loss हो तो घटता है, सब ठीक हो तो बढ़ता है.

*cwnd network की क्षमता के हिसाब से sender की गति नियंत्रित करता है — ज़्यादा loss हो तो घटता है, सब ठीक हो तो बढ़ता है.*

**★ Nukta (Key Point):** TCP की effective window = min(rwnd, cwnd) — flow और congestion दोनों का संतुलन.

*TCP की effective window = min(rwnd, cwnd) — flow और congestion दोनों का संतुलन.*

*[Source: CN Topic Test 5.pdf]*

---
### Q120. What kind of delay does TCP's window size help handle on a long, high-bandwidth path?

<span lang='hi'>लंबी, high-bandwidth path पर TCP का window size किस प्रकार की देर संभालने में मदद करता है?</span>

- **(A)** Transmission delay / Transmission delay
- **(B)** Queuing delay / Queuing delay
- **(C)** Propagation delay / Propagation delay
- **(D)** Bandwidth-delay product / Bandwidth-delay product ✅ **(CORRECT)**

**✔ Correct Answer: (D) Bandwidth-delay product** — Bandwidth × Delay (BDP) जितना बड़ा हो, window उतनी बड़ी चाहिए — तभी पूरी pipe भरी रहती है और propagation delay छिप जाता है.

*Bandwidth × Delay (BDP) जितना बड़ा हो, window उतनी बड़ी चाहिए — तभी पूरी pipe भरी रहती है और propagation delay छिप जाता है.*

**★ Nukta (Key Point):** Window ≥ BDP हो तो link बेकार नहीं बैठती — यही high-speed long links का सूत्र है.

*Window ≥ BDP हो तो link बेकार नहीं बैठती — यही high-speed long links का सूत्र है.*

*[Source: CN Topic Test 5.pdf]*

---
### Q121. In which protocol is 'port knocking' used as a security mechanism?

<span lang='hi'>किस protocol में 'port knocking' security mechanism के रूप में उपयोग होता है?</span>

- **(A)** TCP / TCP
- **(B)** UDP / UDP
- **(C)** SSH / SSH ✅ **(CORRECT)**
- **(D)** IP / IP

**✔ Correct Answer: (C) SSH** — Port knocking में बंद ports पर तय क्रम से connection attempts किए जाते हैं, जिसके बाद firewall SSH जैसी सेवा खोल देता है — यह अक्सर SSH servers के साथ उपयोग होता है.

*Port knocking में बंद ports पर तय क्रम से connection attempts किए जाते हैं, जिसके बाद firewall SSH जैसी सेवा खोल देता है — यह अक्सर SSH servers के साथ उपयोग होता है.*

**★ Nukta (Key Point):** Port knocking = 'secret door knock' — पहचान होते ही असली दरवाज़ा (SSH) खुलता है.

*Port knocking = 'secret door knock' — पहचान होते ही असली दरवाज़ा (SSH) खुलता है.*

*[Source: CN Topic Test 6.pdf]*

---
### Q122. Which of the following supports QoS (Quality of Service) through label switching?

<span lang='hi'>निम्न में से कौन-सा label switching के ज़रिए QoS (Quality of Service) देता है?</span>

- **(A)** TCP / TCP
- **(B)** UDP / UDP
- **(C)** MPLS / MPLS ✅ **(CORRECT)**
- **(D)** ARP / ARP

**✔ Correct Answer: (C) MPLS** — MPLS labels के ज़रिए traffic को classes में बाँटकर QoS देता है — routers बार-बार पूरा IP header नहीं देखते.

*MPLS labels के ज़रिए traffic को classes में बाँटकर QoS देता है — routers बार-बार पूरा IP header नहीं देखते.*

**★ Nukta (Key Point):** MPLS = fast path + QoS classes; DiffServ/IntServ भी QoS के तरीके हैं.

*MPLS = fast path + QoS classes; DiffServ/IntServ भी QoS के तरीके हैं.*

*[Source: CN Topic Test 6.pdf]*

---
### Q123. Virtual circuits are associated with which type of service?

<span lang='hi'>Virtual circuits किस प्रकार की service से जुड़े हैं?</span>

- **(A)** Connectionless service / Connectionless service
- **(B)** Error-free service / Error-free service
- **(C)** Segmentation / Segmentation
- **(D)** Connection-oriented service / Connection-oriented service ✅ **(CORRECT)**

**✔ Correct Answer: (D) Connection-oriented service** — Virtual circuit (जैसे X.25, ATM, Frame Relay) में पहले रास्ता तय होता है, फिर सारे packets उसी रास्ते से जाते हैं — यह connection-oriented model है.

*Virtual circuit (जैसे X.25, ATM, Frame Relay) में पहले रास्ता तय होता है, फिर सारे packets उसी रास्ते से जाते हैं — यह connection-oriented model है.*

**★ Nukta (Key Point):** Virtual circuit = पहले connection, फिर data (connection-oriented); Datagram = हर packet अपने-आप (connectionless).

*Virtual circuit = पहले connection, फिर data (connection-oriented); Datagram = हर packet अपने-आप (connectionless).*

*[Source: CN Topic Test-02.pdf]*

---
### Q124. Transport layer multiplexing allows:

<span lang='hi'>Transport layer multiplexing की अनुमति देता है:</span>

- **(A)** Multiple hosts to share one IP / Multiple hosts to share one IP
- **(B)** Multiple processes to share one network connection / Multiple processes to share one network connection ✅ **(CORRECT)**
- **(C)** Multiple routers to share a routing table / Multiple routers to share a routing table
- **(D)** Domain name resolution / Domain name resolution

**✔ Correct Answer: (B) Multiple processes to share one network connection** — Transport layer multiplexing/demultiplexing से एक ही IP connection पर कई applications (processes) अपने-अपने ports से चल सकते हैं.

*Transport layer multiplexing/demultiplexing से एक ही IP connection पर कई applications (processes) अपने-अपने ports से चल सकते हैं.*

**★ Nukta (Key Point):** Ports ही multiplexing के हथियार हैं — browser 443, mail 25, सब एक साथ.

*Ports ही multiplexing के हथियार हैं — browser 443, mail 25, सब एक साथ.*

*[Source: BCI_SCI Subject Test-7.pdf]*

---
### Q125. Which protocol must use both TCP and UDP for different operations?

<span lang='hi'>कौन-सा protocol अलग-अलग कामों के लिए TCP और UDP दोनों उपयोग करता है?</span>

- **(A)** DNS / DNS ✅ **(CORRECT)**
- **(B)** HTTP / HTTP
- **(C)** POP3 / POP3
- **(D)** Telnet / Telnet

**✔ Correct Answer: (A) DNS** — DNS queries आमतौर पर UDP (port 53) पर जाती हैं, पर बड़े transfers और zone transfers TCP पर — इसलिए DNS दोनों उपयोग करता है.

*DNS queries आमतौर पर UDP (port 53) पर जाती हैं, पर बड़े transfers और zone transfers TCP पर — इसलिए DNS दोनों उपयोग करता है.*

**★ Nukta (Key Point):** DNS = port 53; UDP for small queries, TCP for big/zone transfers.

*DNS = port 53; UDP for small queries, TCP for big/zone transfers.*

*[Source: BCI Subject Test-8.pdf + CN Topic Test 5.pdf]*

---
### Q126. Which port is used by a DHCP client when requesting an IP address?

<span lang='hi'>IP address माँगते समय DHCP client कौन-सा port उपयोग करता है?</span>

- **(A)** UDP 67 / UDP 67
- **(B)** UDP 68 / UDP 68 ✅ **(CORRECT)**
- **(C)** TCP 68 / TCP 68
- **(D)** TCP 67 / TCP 67

**✔ Correct Answer: (B) UDP 68** — DHCP client UDP port 68 से request भेजता है और server UDP port 67 से जवाब देता है.

*DHCP client UDP port 68 से request भेजता है और server UDP port 67 से जवाब देता है.*

**★ Nukta (Key Point):** जोड़ी याद रखो: server 67, client 68 — DHCP (UDP).

*जोड़ी याद रखो: server 67, client 68 — DHCP (UDP).*

*[Source: BCI Subject Test-8.pdf]*

---
### Q127. Which transport-layer protocol is used to support electronic mail delivery between machines?

<span lang='hi'>Machines के बीच electronic mail delivery के लिए कौन-सा transport-layer protocol उपयोग होता है?</span>

- **(A)** SNMP / SNMP
- **(B)** IP / IP
- **(C)** SMTP / SMTP
- **(D)** TCP / TCP ✅ **(CORRECT)**

**✔ Correct Answer: (D) TCP** — Mail की सेवा SMTP (application) देती है, पर वह अपना data TCP के ज़रिए ही भेजती है — इसलिए transport layer पर TCP.

*Mail की सेवा SMTP (application) देती है, पर वह अपना data TCP के ज़रिए ही भेजता है — इसलिए transport layer पर TCP.*

**★ Nukta (Key Point):** प्रश्न 'transport-layer protocol' पूछ रहा है — SMTP application layer का है, TCP transport का.

*प्रश्न 'transport-layer protocol' पूछ रहा है — SMTP application layer का है, TCP transport का.*

*[Source: CN Topic Test-03.pdf]*

---
### Q128. Which of the following statements about TCP/IP is INCORRECT?

<span lang='hi'>TCP/IP के बारे में निम्न में से कौन-सा कथन गलत है?</span>

- **(A)** TCP/IP has high latency / TCP/IP has high latency
- **(B)** Data packets sent over TCP/IP are private / Data packets sent over TCP/IP are private ✅ **(CORRECT)**
- **(C)** TCP is used by Secure Shell (SSH) / TCP is used by Secure Shell (SSH)
- **(D)** TCP/IP uses checksums to check errors / TCP/IP uses checksums to check errors

**✔ Correct Answer: (B) Data packets sent over TCP/IP are private** — TCP/IP पर भेजे packets स्वाभाविक रूप से private नहीं होते — रास्ते में देखे जा सकते हैं; गोपनीयता के लिए TLS/SSH/VPN लगाना पड़ता है.

*TCP/IP पर भेजे packets स्वाभाविक रूप से private नहीं होते — रास्ते में देखे जा सकते हैं; गोपनीयता के लिए TLS/SSH/VPN लगाना पड़ता है.*

**★ Nukta (Key Point):** DSSSB का official key (b). याद रखो: Internet = open postcard, ताला (encryption) खुद लगाओ.

*DSSSB का official key (b). याद रखो: Internet = open postcard, ताला (encryption) खुद लगाओ.*

*[Source: DSSSB TGT CS (via Testbook solved)]*

---

## Section E — Session, Presentation & Application Layer

*Presentation-layer functions, application protocols & ports (HTTP/HTTPS/FTP/SMTP/DNS/SSH/Telnet/NFS/LDAP), TCP/IP layer-protocol matching.*

### Q129. The functionalities of the presentation layer include:

<span lang='hi'>Presentation layer के कार्यों में शामिल हैं:</span>

- **(A)** Data compression / Data compression
- **(B)** Data encryption / Data encryption
- **(C)** Data description (translation) / Data description (translation)
- **(D)** All of the mentioned / All of the mentioned ✅ **(CORRECT)**

**✔ Correct Answer: (D) All of the mentioned** — Presentation layer data का रूप संभालती है — compression, encryption और translation (जैसे ASCII/EBCDIC) — तीनों.

*Presentation layer data का रूप संभालती है — compression, encryption और translation (जैसे ASCII/EBCDIC) — तीनों.*

**★ Nukta (Key Point):** Presentation = data का मेकअप (रूप, रंग, सुरक्षा); Application = सेवाएँ.

*Presentation = data का मेकअप (रूप, रंग, सुरक्षा); Application = सेवाएँ.*

*[Source: CN Topic Test-02.pdf]*

---
### Q130. The structure or format of data is called:

<span lang='hi'>Data का structure या format कहलाता है:</span>

- **(A)** Syntax / Syntax ✅ **(CORRECT)**
- **(B)** Struct / Struct
- **(C)** Semantic / Semantic
- **(D)** None of the above / None of the above

**✔ Correct Answer: (A) Syntax** — Forouzan के अनुसार: Syntax = data का structure/format; Semantics = sections का अर्थ.

*Forouzan के अनुसार: Syntax = data का structure/format; Semantics = sections का अर्थ.*

**★ Nukta (Key Point):** नियम: Syntax = कैसा दिखे; Semantics = क्या अर्थ हो. Communication में दोनों तय होने चाहिए.

*नियम: Syntax = कैसा दिखे; Semantics = क्या अर्थ हो. Communication में दोनों तय होने चाहिए.*

*[Source: Unit Test-4 Solution.pdf (OCR), p14]*

---
### Q131. Which protocol layer uses protocols such as WWW, HTTP, FTP, SMTP and e-mail?

<span lang='hi'>कौन-सी protocol layer WWW, HTTP, FTP, SMTP और e-mail जैसे protocols उपयोग करती है?</span>

- **(A)** Application layer / Application layer ✅ **(CORRECT)**
- **(B)** Transport layer / Transport layer
- **(C)** Internet layer / Internet layer
- **(D)** Hardware layer / Hardware layer

**✔ Correct Answer: (A) Application layer** — HTTP, FTP, SMTP, e-mail आदि Application layer के protocols हैं — यही उपयोगकर्ता की सेवाएँ देती हैं.

*HTTP, FTP, SMTP, e-mail आदि Application layer के protocols हैं — यही उपयोगकर्ता की सेवाएँ देती हैं.*

**★ Nukta (Key Point):** याद रखो: Layer 7 = सेवाएँ (HTTP/FTP/SMTP/DNS); Layer 4 = TCP/UDP; Layer 3 = IP.

*याद रखो: Layer 7 = सेवाएँ (HTTP/FTP/SMTP/DNS); Layer 4 = TCP/UDP; Layer 3 = IP.*

*[Source: CN Topic Test-02.pdf + CN Topic Test-01.pdf]*

---
### Q132. Which layer protocols provide user and application programme support such as passwords, resource sharing and file transfer?

<span lang='hi'>किस layer के protocols उपयोगकर्ता और application programme को passwords, resource sharing और file transfer जैसी सहायता देते हैं?</span>

- **(A)** Layer 2 protocols / Layer 2 protocols
- **(B)** Layer 5 protocols / Layer 5 protocols
- **(C)** Layer 7 protocols / Layer 7 protocols ✅ **(CORRECT)**
- **(D)** Layer 10 protocols / Layer 10 protocols

**✔ Correct Answer: (C) Layer 7 protocols** — Layer 7 (Application) ही users की सेवाएँ संभालती है — passwords, file transfer, resource sharing आदि.

*Layer 7 (Application) ही users की सेवाएँ संभालती है — passwords, file transfer, resource sharing आदि.*

**★ Nukta (Key Point):** OSI में 7 layers ही हैं — 'Layer 10' तो हो ही नहीं सकती.

*OSI में 7 layers ही हैं — 'Layer 10' तो हो ही नहीं सकती.*

*[Source: CN Topic Test-02.pdf]*

---
### Q133. Which of the following protocols is primarily used for secure web browsing?

<span lang='hi'>निम्न में से कौन-सा protocol मुख्य रूप से सुरक्षित web browsing के लिए उपयोग होता है?</span>

- **(A)** FTP / FTP
- **(B)** HTTP / HTTP
- **(C)** HTTPS / HTTPS ✅ **(CORRECT)**
- **(D)** SMTP / SMTP

**✔ Correct Answer: (C) HTTPS** — HTTPS = HTTP + TLS/SSL encryption — browser और server के बीच सारा व्यवहार encrypted रहता है.

*HTTPS = HTTP + TLS/SSL encryption — browser और server के बीच सारा व्यवहार encrypted रहता है.*

**★ Nukta (Key Point):** HTTPS का port 443; HTTP का 80. ताला (lock) वाली site = HTTPS.

*HTTPS का port 443; HTTP का 80. ताला (lock) वाली site = HTTPS.*

*[Source: CN Topic Test-01.pdf]*

---
### Q134. A server receives a packet with destination port 443. This implies:

<span lang='hi'>एक server को destination port 443 वाला packet मिलता है. इसका अर्थ है:</span>

- **(A)** HTTP request / HTTP request
- **(B)** HTTPS traffic / HTTPS traffic ✅ **(CORRECT)**
- **(C)** FTP command / FTP command
- **(D)** Email traffic / Email traffic

**✔ Correct Answer: (B) HTTPS traffic** — Port 443 HTTPS (सुरक्षित web) का standard port है.

*Port 443 HTTPS (सुरक्षित web) का standard port है.*

**★ Nukta (Key Point):** Ports: 80=HTTP, 443=HTTPS, 21/20=FTP, 22=SSH, 23=Telnet, 25=SMTP, 53=DNS, 67/68=DHCP.

*Ports: 80=HTTP, 443=HTTPS, 21/20=FTP, 22=SSH, 23=Telnet, 25=SMTP, 53=DNS, 67/68=DHCP.*

*[Source: BCI Subject Test-8.pdf]*

---
### Q135. Which protocol is generally used to encrypt data between a web browser and a web server?

<span lang='hi'>Web browser और web server के बीच data encrypt करने के लिए आमतौर पर कौन-सा protocol उपयोग होता है?</span>

- **(A)** SSL/TLS / SSL/TLS ✅ **(CORRECT)**
- **(B)** Digital Signature / Digital Signature
- **(C)** IPSec / IPSec
- **(D)** TCP / TCP

**✔ Correct Answer: (A) SSL/TLS** — SSL/TLS (आजकल TLS) browser-server के बीच encryption देता है — इसी पर HTTPS चलता है.

*SSL/TLS (आजकल TLS) browser-server के बीच encryption देता है — इसी पर HTTPS चलता है.*

**★ Nukta (Key Point):** HTTPS = HTTP over SSL/TLS. IPSec network-level VPN के लिए होता है.

*HTTPS = HTTP over SSL/TLS. IPSec network-level VPN के लिए होता है.*

*[Source: CN Topic Test-01.pdf]*

---
### Q136. Which of the following protocols is NOT secure?

<span lang='hi'>निम्न में से कौन-सा protocol सुरक्षित नहीं है?</span>

- **(A)** HTTPS / HTTPS
- **(B)** FTP / FTP ✅ **(CORRECT)**
- **(C)** SSH / SSH
- **(D)** SFTP / SFTP

**✔ Correct Answer: (B) FTP** — सादा FTP data और passwords सादे रूप में भेजता है — यह असुरक्षित है. इसके सुरक्षित रूप SFTP/FTPS हैं.

*सादा FTP data और passwords सादे रूप में भेजता है — यह असुरक्षित है. इसके सुरक्षित रूप SFTP/FTPS हैं.*

**★ Nukta (Key Point):** असुरक्षित की सूची: HTTP, FTP, Telnet, SMTP (बिना TLS). सुरक्षित: HTTPS, SFTP, SSH, SMTPS.

*असुरक्षित की सूची: HTTP, FTP, Telnet, SMTP (बिना TLS). सुरक्षित: HTTPS, SFTP, SSH, SMTPS.*

*[Source: CN Topic Test 6.pdf]*

---
### Q137. Which protocol is used for secure shell (remote) login?

<span lang='hi'>Secure shell (remote) login के लिए कौन-सा protocol उपयोग होता है?</span>

- **(A)** FTP / FTP
- **(B)** SSH / SSH ✅ **(CORRECT)**
- **(C)** Telnet / Telnet
- **(D)** SNMP / SNMP

**✔ Correct Answer: (B) SSH** — SSH (Secure Shell) encrypted remote login देता है — Telnet का सुरक्षित विकल्प.

*SSH (Secure Shell) encrypted remote login देता है — Telnet का सुरक्षित विकल्प.*

**★ Nukta (Key Point):** SSH = port 22 (encrypted); Telnet = port 23 (सादा, असुरक्षित).

*SSH = port 22 (encrypted); Telnet = port 23 (सादा, असुरक्षित).*

*[Source: CN Topic Test 6.pdf + Medium 30 CN MCQ bank]*

---
### Q138. A firewall blocks all ports except 22. What service remains accessible?

<span lang='hi'>एक firewall port 22 को छोड़कर सब बंद कर देता है. कौन-सी सेवा अभी भी खुली है?</span>

- **(A)** FTP / FTP
- **(B)** SSH / SSH ✅ **(CORRECT)**
- **(C)** HTTPS / HTTPS
- **(D)** SMTP / SMTP

**✔ Correct Answer: (B) SSH** — Port 22 SSH का है — इसलिए SSH सेवा ही खुली रहेगी.

*Port 22 SSH का है — इसलिए SSH सेवा ही खुली रहेगी.*

**★ Nukta (Key Point):** Port पहचानो, सेवा पहचानो — यही इस प्रश्न का खेल है.

*Port पहचानो, सेवा पहचानो — यही इस प्रश्न का खेल है.*

*[Source: BCI Subject Test-8.pdf]*

---
### Q139. Which port does Telnet use by default?

<span lang='hi'>Telnet डिफ़ॉल्ट रूप से कौन-सा port उपयोग करता है?</span>

- **(A)** 21 / 21
- **(B)** 23 / 23 ✅ **(CORRECT)**
- **(C)** 22 / 22
- **(D)** 25 / 25

**✔ Correct Answer: (B) 23** — Telnet का default port 23 है (सादा remote login).

*Telnet का default port 23 है (सादा remote login).*

**★ Nukta (Key Point):** याद रखो: 22 = SSH, 23 = Telnet, 25 = SMTP, 21 = FTP.

*याद रखो: 22 = SSH, 23 = Telnet, 25 = SMTP, 21 = FTP.*

*[Source: CN Topic Test 6.pdf]*

---
### Q140. Which of the following uses port number 25?

<span lang='hi'>निम्न में से कौन-सा port number 25 उपयोग करता है?</span>

- **(A)** FTP / FTP
- **(B)** HTTP / HTTP
- **(C)** SMTP / SMTP ✅ **(CORRECT)**
- **(D)** Telnet / Telnet

**✔ Correct Answer: (C) SMTP** — SMTP (Simple Mail Transfer Protocol) mail भेजने के लिए port 25 उपयोग करता है.

*SMTP (Simple Mail Transfer Protocol) mail भेजने के लिए port 25 उपयोग करता है.*

**★ Nukta (Key Point):** Mail ports: 25 (SMTP), 110 (POP3), 143 (IMAP).

*Mail ports: 25 (SMTP), 110 (POP3), 143 (IMAP).*

*[Source: CN Topic Test 6.pdf]*

---
### Q141. Which of the following protocols is used for transferring email messages from one machine to another?

<span lang='hi'>निम्न में से कौन-सा protocol email संदेशों को एक machine से दूसरी में भेजने के लिए उपयोग होता है?</span>

- **(A)** SNMP / SNMP
- **(B)** FTP / FTP
- **(C)** TELNET / TELNET
- **(D)** SMTP / SMTP ✅ **(CORRECT)**

**✔ Correct Answer: (D) SMTP** — SMTP ही mail servers के बीच संदेश भेजने का मानक protocol है (port 25).

*SMTP ही mail servers के बीच संदेश भेजने का मानक protocol है (port 25).*

**★ Nukta (Key Point):** RPSC official key (d). भेजना = SMTP; लेना = POP3/IMAP.

*RPSC official key (d). भेजना = SMTP; लेना = POP3/IMAP.*

*[Source: RPSC Programmer 2024 Paper-1 (with official key)]*

---
### Q142. Which protocol uses different ports for control and data connections?

<span lang='hi'>कौन-सा protocol control और data connections के लिए अलग-अलग ports उपयोग करता है?</span>

- **(A)** FTP / FTP ✅ **(CORRECT)**
- **(B)** HTTP / HTTP
- **(C)** DNS / DNS
- **(D)** Telnet / Telnet

**✔ Correct Answer: (A) FTP** — FTP दो connections रखता है — control के लिए port 21 और data के लिए port 20.

*FTP दो connections रखता है — control के लिए port 21 और data के लिए port 20.*

**★ Nukta (Key Point):** FTP = double connection (control + data); HTTP/SMTP/DNS में ऐसा नहीं.

*FTP = double connection (control + data); HTTP/SMTP/DNS में ऐसा नहीं.*

*[Source: BCI_SCI Subject Test-7.pdf]*

---
### Q143. Which protocol is used for file transfer over a network?

<span lang='hi'>Network पर file transfer के लिए कौन-सा protocol उपयोग होता है?</span>

- **(A)** FTP / FTP ✅ **(CORRECT)**
- **(B)** HTTP / HTTP
- **(C)** DNS / DNS
- **(D)** ARP / ARP

**✔ Correct Answer: (A) FTP** — FTP (File Transfer Protocol) files भेजने-लाने का मानक protocol है.

*FTP (File Transfer Protocol) files भेजने-लाने का मानक protocol है.*

**★ Nukta (Key Point):** HTTP से भी files मिलती हैं, पर 'file transfer' का नाम protocol FTP है.

*HTTP से भी files मिलती हैं, पर 'file transfer' का नाम protocol FTP है.*

*[Source: CN Topic Test 6.pdf + Medium 30 CN MCQ bank]*

---
### Q144. In one of the pairs below, both protocols can use multiple TCP connections between the same client and the same server. Which pair is it?

<span lang='hi'>नीचे दिए जोड़ों में से किसमें दोनों protocols एक ही client और server के बीच कई TCP connections उपयोग कर सकते हैं?</span>

- **(A)** HTTP, FTP / HTTP, FTP ✅ **(CORRECT)**
- **(B)** HTTP, TELNET / HTTP, TELNET
- **(C)** FTP, SMTP / FTP, SMTP
- **(D)** HTTP, SMTP / HTTP, SMTP

**✔ Correct Answer: (A) HTTP, FTP** — HTTP non-persistent connections में हर object के लिए अलग connection खोल सकता है; FTP में control के अलावा हर transfer की अलग data connection होती है.

*HTTP non-persistent connections में हर object के लिए अलग connection खोल सकता है; FTP में control के अलावा हर transfer की अलग data connection होती है.*

**★ Nukta (Key Point):** दोनों 'multi-connection' protocols हैं — यही जोड़ी पूछी गई है.

*दोनों 'multi-connection' protocols हैं — यही जोड़ी पूछी गई है.*

*[Source: CN Topic Test-02.pdf]*

---
### Q145. Identify the true statements: (1) HTTP may use different TCP connections for different objects of a webpage if non-persistent connections are used (2) FTP uses two TCP connections, one for data and another for control (3) TELNET and FTP can only use TWO connections at a time

<span lang='hi'>सही कथन पहचानें: (1) non-persistent connections में HTTP webpage के अलग-अलग objects के लिए अलग TCP connections उपयोग कर सकता है (2) FTP दो TCP connections उपयोग करता है, एक data के लिए और दूसरा control के लिए (3) TELNET और FTP एक समय में केवल TWO connections ही उपयोग कर सकते हैं</span>

- **(A)** (1) only / (1) only
- **(B)** (1) and (2) / (1) and (2) ✅ **(CORRECT)**
- **(C)** (2) and (3) / (2) and (3)
- **(D)** (1), (2) and (3) / (1), (2) and (3)

**✔ Correct Answer: (B) (1) and (2)** — (1) सही — non-persistent HTTP हर object के लिए नया connection; (2) सही — FTP में control + data connections; (3) गलत — ऐसी 'केवल दो' सीमा नहीं.

*(1) सही — non-persistent HTTP हर object के लिए नया connection; (2) सही — FTP में control + data connections; (3) गलत — ऐसी 'केवल दो' सीमा नहीं.*

**★ Nukta (Key Point):** HTTP = multi-connection capable; FTP = दो का जोड़ा; 'only two' का नियम कहीं नहीं.

*HTTP = multi-connection capable; FTP = दो का जोड़ा; 'only two' का नियम कहीं नहीं.*

*[Source: CN Topic Test-03.pdf]*

---
### Q146. Which application allows a user to access and use remote files without actually transferring them?

<span lang='hi'>कौन-सा application उपयोगकर्ता को remote files को बिना वास्तव में स्थानांतरित किए उपयोग करने देता है?</span>

- **(A)** DNS / DNS
- **(B)** FTP / FTP
- **(C)** NFS / NFS ✅ **(CORRECT)**
- **(D)** Telnet / Telnet

**✔ Correct Answer: (C) NFS** — NFS (Network File System) remote files को ऐसे दिखाता है जैसे वे आपके अपने computer पर हों — असल transfer नहीं होता.

*NFS (Network File System) remote files को ऐसे दिखाता है जैसे वे आपके अपने computer पर हों — असल transfer नहीं होता.*

**★ Nukta (Key Point):** NFS = remote files को local जैसा जोड़ना; FTP = files की असल copy भेजना.

*NFS = remote files को local जैसा जोड़ना; FTP = files की असल copy भेजना.*

*[Source: SSC CGL Internet & Networking (via EduRev bank)]*

---
### Q147. Which of the following is NOT an application layer protocol?

<span lang='hi'>निम्न में से कौन-सा application layer protocol नहीं है?</span>

- **(A)** HTTP / HTTP
- **(B)** IP / IP ✅ **(CORRECT)**
- **(C)** TELNET / TELNET
- **(D)** FTP / FTP

**✔ Correct Answer: (B) IP** — IP network layer का protocol है — HTTP, TELNET, FTP सब application layer के हैं.

*IP network layer का protocol है — HTTP, TELNET, FTP सब application layer के हैं.*

**★ Nukta (Key Point):** Layer 7 के नाम: HTTP, FTP, SMTP, DNS, Telnet, SNMP, DHCP, TFTP...

*Layer 7 के नाम: HTTP, FTP, SMTP, DNS, Telnet, SNMP, DHCP, TFTP...*

*[Source: SSC CGL Internet & Networking (via EduRev bank)]*

---
### Q148. Which is the FALSE statement?

<span lang='hi'>कौन-सा कथन गलत है?</span>

- **(A)** Telnet is used for remote login / Telnet is used for remote login
- **(B)** FTP can transfer files between two hosts / FTP can transfer files between two hosts
- **(C)** TFTP relies on TCP / TFTP relies on TCP ✅ **(CORRECT)**
- **(D)** SMTP is used to send mail messages / SMTP is used to send mail messages

**✔ Correct Answer: (C) TFTP relies on TCP** — TFTP (Trivial FTP) UDP पर चलता है, TCP पर नहीं — यही कथन गलत है.

*TFTP (Trivial FTP) UDP पर चलता है, TCP पर नहीं — यही कथन गलत है.*

**★ Nukta (Key Point):** TFTP = छोटा भाई (UDP, port 69); FTP = बड़ा भाई (TCP, ports 20/21).

*TFTP = छोटा भाई (UDP, port 69); FTP = बड़ा भाई (TCP, ports 20/21).*

*[Source: SSC CGL Internet & Networking (via EduRev bank)]*

---
### Q149. Which protocol translates domain names to IP addresses?

<span lang='hi'>कौन-सा protocol domain names को IP addresses में बदलता है?</span>

- **(A)** DHCP / DHCP
- **(B)** DNS / DNS ✅ **(CORRECT)**
- **(C)** HTTP / HTTP
- **(D)** FTP / FTP

**✔ Correct Answer: (B) DNS** — DNS (Domain Name System) नाम → IP address का translation करता है — Internet की phonebook.

*DNS (Domain Name System) नाम → IP address का translation करता है — Internet की phonebook.*

**★ Nukta (Key Point):** DNS = name→IP; ARP = IP→MAC; DHCP = IP बाँटना.

*DNS = name→IP; ARP = IP→MAC; DHCP = IP बाँटना.*

*[Source: CN Topic Test 5.pdf + CN Topic Test-01.pdf]*

---
### Q150. What does a 'ping' command test?

<span lang='hi'>'ping' command क्या जाँचता है?</span>

- **(A)** IP configuration / IP configuration
- **(B)** Host reachability / Host reachability ✅ **(CORRECT)**
- **(C)** DNS resolution / DNS resolution
- **(D)** Port scanning / Port scanning

**✔ Correct Answer: (B) Host reachability** — Ping ICMP Echo भेजकर जाँचता है कि दूसरा host पहुँच में है या नहीं और कितनी देर लगी.

*Ping ICMP Echo भेजकर जाँचता है कि दूसरा host पहुँच में है या नहीं और कितनी देर लगी.*

**★ Nukta (Key Point):** ping = 'क्या तुम वहाँ हो?' — reachability + round-trip time.

*ping = 'क्या तुम वहाँ हो?' — reachability + round-trip time.*

*[Source: CN Topic Test 6.pdf]*

---
### Q151. Which HTTP status code means 'Forbidden'?

<span lang='hi'>कौन-सा HTTP status code का अर्थ है 'Forbidden'?</span>

- **(A)** 200 / 200
- **(B)** 301 / 301
- **(C)** 403 / 403 ✅ **(CORRECT)**
- **(D)** 404 / 404

**✔ Correct Answer: (C) 403** — HTTP 403 का अर्थ है server ने request समझी, पर access की अनुमति नहीं है.

*HTTP 403 का अर्थ है server ने request समझी, पर access की अनुमति नहीं है.*

**★ Nukta (Key Point):** याद रखो: 200 OK, 301 Moved, 403 Forbidden, 404 Not Found, 500 Server Error.

*याद रखो: 200 OK, 301 Moved, 403 Forbidden, 404 Not Found, 500 Server Error.*

*[Source: Oliveboard SSC CGL Tier-2 bank]*

---
### Q152. Lightweight Directory Access Protocol (LDAP) is used for:

<span lang='hi'>Lightweight Directory Access Protocol (LDAP) किस काम आता है?</span>

- **(A)** Routing the packets / Routing the packets
- **(B)** Authentication and directory access / Authentication and directory access ✅ **(CORRECT)**
- **(C)** Obtaining an IP address / Obtaining an IP address
- **(D)** Domain name resolving / Domain name resolving

**✔ Correct Answer: (B) Authentication and directory access** — LDAP directory services (users, groups, permissions की सूची) तक पहुँच देता है और authentication के लिए उपयोग होता है.

*LDAP directory services (users, groups, permissions की सूची) तक पहुँच देता है और authentication के लिए उपयोग होता है.*

**★ Nukta (Key Point):** LDAP = network का 'पता-पुस्तिका + पहचान-पत्र काउंटर'.

*LDAP = network का 'पता-पुस्तिका + पहचान-पत्र काउंटर'.*

*[Source: Unit Test-4 Solution.pdf (OCR), p29]*

---
### Q153. Match TCP/IP layers and protocols — (P) Transport layer (Q) Network (internet) layer (R) Application layer; (1) ICMP (2) FTP (3) UDP. Which matching is correct?

<span lang='hi'>TCP/IP layers और protocols मिलाएँ — (P) Transport layer (Q) Network (internet) layer (R) Application layer; (1) ICMP (2) FTP (3) UDP. कौन-सा मिलान सही है?</span>

- **(A)** P-2, Q-1, R-3 / P-2, Q-1, R-3
- **(B)** P-1, Q-2, R-3 / P-1, Q-2, R-3
- **(C)** P-3, Q-1, R-2 / P-3, Q-1, R-2 ✅ **(CORRECT)**
- **(D)** P-3, Q-2, R-1 / P-3, Q-2, R-1

**✔ Correct Answer: (C) P-3, Q-1, R-2** — UDP Transport का है (P-3), ICMP Network का है (Q-1), FTP Application का है (R-2) — इसलिए P-3, Q-1, R-2.

*UDP Transport का है (P-3), ICMP Network का है (Q-1), FTP Application का है (R-2) — इसलिए P-3, Q-1, R-2.*

**★ Nukta (Key Point):** Layers याद रखो: Application = FTP/HTTP/SMTP/DNS; Transport = TCP/UDP; Internet = IP/ICMP/IGMP.

*Layers याद रखो: Application = FTP/HTTP/SMTP/DNS; Transport = TCP/UDP; Internet = IP/ICMP/IGMP.*

*[Source: Random Test- Rajasthan PYQ.pdf (OCR) + answer_keys.py Q23]*

---

## ★ Nukte Rapid-Fire — Exam Pointers

- **DLL = ?** *(DLL = ?)* → **MAC + LLC. MAC = physical addressing + medium access; LLC = flow/error control + interface.** *(MAC + LLC. MAC = physical addressing + medium access; LLC = flow/error control + interface.)*
- **Routing किस layer का?** *(Routing किस layer का?)* → **Network layer (L3) का. DLL सिर्फ अगले hop तक पहुँचाता है.** *(Network layer (L3) का. DLL सिर्फ अगले hop तक पहुँचाता है.)*
- **SW / GBN / SR windows?** *(SW / GBN / SR windows?)* → **SW = 1; GBN ≤ 2ⁿ−1; SR ≤ 2ⁿ⁻¹ (N/2). SR सिर्फ गलत frame दोहराता है.** *(SW = 1; GBN ≤ 2ⁿ−1; SR ≤ 2ⁿ⁻¹ (N/2). SR सिर्फ गलत frame दोहराता है.)*
- **Hamming distance d=3 क्या देता है?** *(Hamming distance d=3 क्या देता है?)* → **2 errors detect या 1 error correct. d ≥ 2t+1.** *(2 errors detect या 1 error correct. d ≥ 2t+1.)*
- **Parity क्या पकड़ता है?** *(Parity क्या पकड़ता है?)* → **Odd number of errors. Simple parity = 1 bit; 2D parity = rows+columns.** *(Odd number of errors. Simple parity = 1 bit; 2D parity = rows+columns.)*
- **CRC vs Checksum?** *(CRC vs Checksum?)* → **DLL = CRC (FCS field); Network/Transport = checksum. Integrity = message digest.** *(DLL = CRC (FCS field); Network/Transport = checksum. Integrity = message digest.)*
- **Ethernet frame limits?** *(Ethernet frame limits?)* → **Min 64 / Max 1518 bytes; data 46–1500 (MTU 1500). Min size = CSMA/CD collision detection.** *(Min 64 / Max 1518 bytes; data 46–1500 (MTU 1500). Min size = CSMA/CD collision detection.)*
- **Frame field order?** *(Frame field order?)* → **Preamble → Dest MAC → Source MAC → Type → Data → FCS. FCS = CRC.** *(Preamble → Dest MAC → Source MAC → Type → Data → FCS. FCS = CRC.)*
- **Bit stuffing?** *(Bit stuffing?)* → **Data में पाँच 1s के बाद 0 ठूँसना (flag से confusion रोकना). HDLC bit-oriented; PPP byte-oriented.** *(Data में पाँच 1s के बाद 0 ठूँसना (flag से confusion रोकना). HDLC bit-oriented; PPP byte-oriented.)*
- **ALOHA formulas?** *(ALOHA formulas?)* → **Pure: 2T vulnerable, G·e⁻²ᴳ (~18.4%). Slotted: T vulnerable, G·e⁻ᴳ (~36.8%).** *(Pure: 2T vulnerable, G·e⁻²ᴳ (~18.4%). Slotted: T vulnerable, G·e⁻ᴳ (~36.8%).)*
- **CSMA/CD vs CSMA/CA?** *(CSMA/CD vs CSMA/CA?)* → **CD = wired Ethernet (jam signal); CA = wireless (RTS/CTS, NAV). Jam = collision की घोषणा.** *(CD = wired Ethernet (jam signal); CA = wireless (RTS/CTS, NAV). Jam = collision की घोषणा.)*
- **Token Ring mode?** *(Token Ring mode?)* → **Round Robin (token passing). Reservation mode में slot पहले book करते हैं.** *(Round Robin (token passing). Reservation mode में slot पहले book करते हैं.)*
- **IPv4 header key sizes?** *(IPv4 header key sizes?)* → **Min header 20B; Total Length 16-bit; Fragment Offset 13-bit; TTL 8-bit; ToS = priority.** *(Min header 20B; Total Length 16-bit; Fragment Offset 13-bit; TTL 8-bit; ToS = priority.)*
- **Fragmentation vs Reassembly?** *(Fragmentation vs Reassembly?)* → **MF flag + Fragment Offset से. टुकड़े routers भी कर सकते हैं; जोड़ना सिर्फ destination.** *(MF flag + Fragment Offset से. टुकड़े routers भी कर सकते हैं; जोड़ना सिर्फ destination.)*
- **ARP / RARP / DNS / DHCP?** *(ARP / RARP / DNS / DHCP?)* → **ARP = IP→MAC; RARP = MAC→IP (obsolete); DNS = name→IP; DHCP = automatic IP (zeroconf).** *(ARP = IP→MAC; RARP = MAC→IP (obsolete); DNS = name→IP; DHCP = automatic IP (zeroconf).)*
- **ICMP/IGMP किस layer के?** *(ICMP/IGMP किस layer के?)* → **Network layer. ICMP = ping/errors/PMTU; IGMP = multicast membership. Echo = query, error नहीं.** *(Network layer. ICMP = ping/errors/PMTU; IGMP = multicast membership. Echo = query, error नहीं.)*
- **Routing protocol families?** *(Routing protocol families?)* → **RIP = Distance vector (Bellman-Ford, max 15 hops); OSPF/IS-IS = Link state (Dijkstra); BGP = Path vector (Inter-AS).** *(RIP = Distance vector (Bellman-Ford, max 15 hops); OSPF/IS-IS = Link state (Dijkstra); BGP = Path vector (Inter-AS).)*
- **DV की कमी और उपाय?** *(DV की कमी और उपाय?)* → **Count-to-infinity. उपाय: split horizon + poison reverse + hold-down.** *(Count-to-infinity. उपाय: split horizon + poison reverse + hold-down.)*
- **STP और MPLS?** *(STP और MPLS?)* → **STP = L2 loops रोकता है; MPLS = 'Layer 2.5' (labels, QoS).** *(STP = L2 loops रोकता है; MPLS = 'Layer 2.5' (labels, QoS).)*
- **TCP vs UDP?** *(TCP vs UDP?)* → **TCP = reliable, ordered, connection-oriented, broadcast नहीं; UDP = connectionless, fast.** *(TCP = reliable, ordered, connection-oriented, broadcast नहीं; UDP = connectionless, fast.)*
- **Socket = ?** *(Socket = ?)* → **IP + Port. Ports 16-bit (0–65535). Connection = socket pair.** *(IP + Port. Ports 16-bit (0–65535). Connection = socket pair.)*
- **TCP handshake और flags?** *(TCP handshake और flags?)* → **SYN → SYN-ACK → ACK (ESTABLISHED). SYN = शुरुआत, FIN = अंत, RST = रद्द.** *(SYN → SYN-ACK → ACK (ESTABLISHED). SYN = शुरुआत, FIN = अंत, RST = रद्द.)*
- **TCP flow vs congestion control?** *(TCP flow vs congestion control?)* → **Flow = receiver window (rwnd); Congestion = cwnd (slow start, avoidance). Effective = min(rwnd, cwnd).** *(Flow = receiver window (rwnd); Congestion = cwnd (slow start, avoidance). Effective = min(rwnd, cwnd).)*
- **TCP attacks और बचाव?** *(TCP attacks और बचाव?)* → **SYN flood (handshake), session hijacking (random ISN से बचाव).** *(SYN flood (handshake), session hijacking (random ISN से बचाव).)*
- **Port numbers?** *(Port numbers?)* → **21/20 FTP, 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 67/68 DHCP, 80 HTTP, 443 HTTPS, 110 POP3, 143 IMAP.** *(21/20 FTP, 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 67/68 DHCP, 80 HTTP, 443 HTTPS, 110 POP3, 143 IMAP.)*
- **Secure vs असुरक्षित protocols?** *(Secure vs असुरक्षित protocols?)* → **Secure: HTTPS, SSH, SFTP, FTPS. असुरक्षित: HTTP, FTP, Telnet. SSL/TLS = browser-server encryption.** *(Secure: HTTPS, SSH, SFTP, FTPS. असुरक्षित: HTTP, FTP, Telnet. SSL/TLS = browser-server encryption.)*
- **Presentation layer के काम?** *(Presentation layer के काम?)* → **Compression, encryption, translation. Syntax = format; Semantics = meaning.** *(Compression, encryption, translation. Syntax = format; Semantics = meaning.)*
- **FTP की ख़ासियत?** *(FTP की ख़ासियत?)* → **दो TCP connections (control 21 + data 20); TFTP UDP पर (port 69); NFS = remote files को local जैसा.** *(दो TCP connections (control 21 + data 20); TFTP UDP पर (port 69); NFS = remote files को local जैसा.)*
- **Ping / traceroute?** *(Ping / traceroute?)* → **Ping = reachability (ICMP Echo); traceroute = रास्ता (Linux=UDP, Windows=ICMP). 403 = Forbidden.** *(Ping = reachability (ICMP Echo); traceroute = रास्ता (Linux=UDP, Windows=ICMP). 403 = Forbidden.)*
- **Multiplexing किस layer का?** *(Multiplexing किस layer का?)* → **Transport layer (ports से processes share करते हैं). Presentation = data का रूप.** *(Transport layer (ports से processes share करते हैं). Presentation = data का रूप.)*

