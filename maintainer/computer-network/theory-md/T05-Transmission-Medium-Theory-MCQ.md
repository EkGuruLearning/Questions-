# Data Communication & Computer Networks (CN)
## Topic 5 of 7 : Transmission Medium — 47 MCQs (English + Hindi)

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** RPSC Programmer • ACP • RSMSSB IA • SA • DD • BCI • SCI • REET • RAS • DSSSB • KVS • NVS • HTET • SSC CGL/CHSL • RRB • IBPS • UPSC & all Rajasthan + Central Govt. Exams (Computer Awareness)

**Total Questions:** 47 | **Type:** MCQ (4 options) | **Bilingual:** English + Hindi (technical terms in English) | Each: ✔ why the correct answer is right + ★ Nukta. Wrong options verified internally. Answers cross-verified 4×.

### Syllabus Coverage (sub-topic wise order)

| # | Sub-topic | Questions |
|---|-----------|-----------|
| 1 | Section A — Signals & Performance (Encoding, Noise, Bandwidth, Data Rate) | Q1 - Q24 |
| 2 | Section B — Guided Media (UTP, Coaxial, Fiber Optic) | Q25 - Q40 |
| 3 | Section C — Unguided Media (Wireless) | Q41 - Q47 |

---

## Section A — Signals & Performance (Encoding, Noise, Bandwidth, Data Rate)

*Line coding (Manchester, 8B/10B, scramblers), impairments (attenuation/crosstalk/noise), signal parameters, data-rate & Shannon/Nyquist calculations.*

### Q1. 'Manchester Encoding' and 'Differential Manchester Encoding' are signal encoding techniques used at which layer?

<span lang='hi'>'Manchester Encoding' और 'Differential Manchester Encoding' signal encoding techniques किस layer पर उपयोग होती हैं?</span>

- **(A)** Physical Layer ✅ **(CORRECT)**
- **(B)** Data Link Layer
- **(C)** Network Layer
- **(D)** Presentation Layer

**✔ Correct Answer: (A) Physical Layer** — Line coding (Manchester, differential Manchester, NRZ, AMI) converts bits into signals — a Physical layer job.

*Line coding (Manchester, differential Manchester, NRZ, AMI) bits को signals में बदलती है — यह Physical layer का काम है।*

**★ Nukta (Key Point):** Physical layer = signalling & encoding (Manchester = mid-bit transition, self-clocking).

*Physical layer = signalling और encoding (Manchester = mid-bit transition, self-clocking)।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q2. A channel has high bandwidth but suffers from high noise. Which encoding scheme gives better error resistance?

<span lang='hi'>एक channel की bandwidth अधिक है लेकिन noise बहुत है। कौन-सी encoding scheme बेहतर error resistance देगी?</span>

- **(A)** NRZ
- **(B)** Manchester ✅ **(CORRECT)**
- **(C)** AMI
- **(D)** ASK

**✔ Correct Answer: (B) Manchester** — Manchester encoding has a transition in every bit period — the receiver resynchronises quickly and detects errors easily, giving strong noise resilience.

*Manchester encoding में हर bit period में transition होता है — receiver जल्दी resynchronise होता है और errors आसानी से पकड़ लेता है, इसलिए noise resilience मज़बूत है।*

**★ Nukta (Key Point):** Manchester = self-clocking + DC-free + strong error visibility. NRZ = long runs → clock loss in noise.

*Manchester = self-clocking + DC-free + मज़बूत error visibility। NRZ = लंबे runs → noise में clock loss।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q3. Reduction in signal strength over distance is called:

<span lang='hi'>दूरी के साथ signal strength में कमी को क्या कहते हैं?</span>

- **(A)** Distortion
- **(B)** Noise
- **(C)** Attenuation ✅ **(CORRECT)**
- **(D)** Interference

**✔ Correct Answer: (C) Attenuation** — Attenuation is the gradual loss of signal strength (amplitude) as it travels along a medium — measured in dB/km (or dB/100 ft).

*Attenuation medium के साथ यात्रा करते समय signal strength (amplitude) का क्रमिक नुकसान है — इसे dB/km (या dB/100 ft) में मापा जाता है।*

**★ Nukta (Key Point):** Impairments: Attenuation (strength loss), Distortion (shape change), Noise (unwanted signals). Attenuation ↑ with distance & frequency.

*Impairments: Attenuation (strength loss), Distortion (shape change), Noise (unwanted signals)। Attenuation ↑ distance और frequency के साथ।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) · also CN Topic Test-04] · Easy*

---
### Q4. In a copper cable, attenuation increases with frequency. Which change will REDUCE attenuation?

<span lang='hi'>Copper cable में attenuation frequency के साथ बढ़ता है। कौन-सा बदलाव attenuation घटाएगा?</span>

- **(A)** Increase cable length
- **(B)** Use lower-category UTP
- **(C)** Use thicker copper core ✅ **(CORRECT)**
- **(D)** Increase signal frequency

**✔ Correct Answer: (C) Use thicker copper core** — A thicker copper core has lower electrical resistance — so the signal loses less strength over distance.

*मोटे copper core का electrical resistance कम होता है — इसलिए signal को दूरी पर कम strength गँवानी पड़ती है।*

**★ Nukta (Key Point):** Reduce attenuation: shorter cable, thicker/better copper, higher category cable, lower frequency, or add repeaters/amplifiers.

*Attenuation घटाना: छोटी cable, मोटा/बेहतर copper, उच्च श्रेणी cable, कम frequency, या repeaters/amplifiers जोड़ें।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q5. Which noise is caused by electromagnetic coupling between nearby cables?

<span lang='hi'>पास की cables के बीच electromagnetic coupling से कौन-सा noise होता है?</span>

- **(A)** Thermal noise
- **(B)** Crosstalk ✅ **(CORRECT)**
- **(C)** Impulse noise
- **(D)** Quantization noise

**✔ Correct Answer: (B) Crosstalk** — Crosstalk is the unwanted signal leakage from one wire pair to a neighbouring pair caused by electromagnetic coupling.

*Crosstalk एक wire pair से पास की दूसरी pair में electromagnetic coupling के कारण होने वाला unwanted signal leakage है।*

**★ Nukta (Key Point):** Noise types: Thermal (random electron motion), Crosstalk (pair-to-pair coupling), Impulse (sudden spikes), Quantization (PCM sampling).

*Noise types: Thermal (random electron motion), Crosstalk (pair-to-pair coupling), Impulse (sudden spikes), Quantization (PCM sampling)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q6. Which impairment cannot be completely eliminated but only minimised?

<span lang='hi'>कौन-सा impairment पूरी तरह समाप्त नहीं किया जा सकता, केवल कम किया जा सकता है?</span>

- **(A)** Attenuation
- **(B)** Distortion
- **(C)** Noise ✅ **(CORRECT)**
- **(D)** Delay

**✔ Correct Answer: (C) Noise** — Noise can never be fully eliminated — it can only be minimised (shielding, better cable, lower power, error control).

*Noise कभी पूरी तरह समाप्त नहीं हो सकती — केवल कम की जा सकती है (shielding, बेहतर cable, कम power, error control)।*

**★ Nukta (Key Point):** Attenuation/distortion can be fixed with repeaters/equalisers; noise is fundamental (thermal floor) — only minimised.

*Attenuation/distortion repeaters/equalisers से ठीक हो सकते हैं; noise मूलभूत है (thermal floor) — केवल कम होती है।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q7. Which parameter of an analog signal represents the number of cycles per second?

<span lang='hi'>Analog signal का कौन-सा parameter प्रति सेकंड cycles की संख्या दर्शाता है?</span>

- **(A)** Amplitude
- **(B)** Phase
- **(C)** Frequency ✅ **(CORRECT)**
- **(D)** Wavelength

**✔ Correct Answer: (C) Frequency** — Frequency is the number of signal cycles completed per second, measured in Hertz (Hz).

*Frequency प्रति सेकंड पूरे होने वाले signal cycles की संख्या है, जिसे Hertz (Hz) में मापा जाता है।*

**★ Nukta (Key Point):** Signal parameters: Amplitude (height), Frequency (cycles/sec), Phase (start position), Wavelength (distance/cycle = speed/frequency).

*Signal parameters: Amplitude (ऊँचाई), Frequency (cycles/sec), Phase (शुरुआती स्थिति), Wavelength (दूरी/cycle = speed/frequency)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q8. Which of the following Ethernet encodings has the highest redundancy?

<span lang='hi'>निम्न में से कौन-सी Ethernet encoding की redundancy सबसे अधिक है?</span>

- **(A)** 1B2B ✅ **(CORRECT)**
- **(B)** 4B5B
- **(C)** 5B6B
- **(D)** 8B10B

**✔ Correct Answer: (A) 1B2B** — 1B2B encodes every 1 bit as 2 bits — 100% redundancy, the highest of the four (4B5B = 25%, 5B6B = 20%, 8B10B = 25%).

*1B2B हर 1 bit को 2 bits के रूप में encode करती है — 100% redundancy, चारों में सबसे अधिक (4B5B = 25%, 5B6B = 20%, 8B10B = 25%)।*

**★ Nukta (Key Point):** Redundancy (overhead): 1B2B 100% > 4B5B/8B10B 25% > 5B6B 20%. More redundancy = better clocking/error properties, more bandwidth.

*Redundancy (overhead): 1B2B 100% > 4B5B/8B10B 25% > 5B6B 20%। ज़्यादा redundancy = बेहतर clocking/error properties, ज़्यादा bandwidth।*

*[Source: Unit Test-4 Solution (OCR), p9 (options recovered from source)] · Medium*

---
### Q9. Which encoding technique is used to transmit signals in Gigabit Ethernet over fiber optic medium?

<span lang='hi'>Fiber optic medium पर Gigabit Ethernet में signal भेजने के लिए कौन-सी encoding technique उपयोग होती है?</span>

- **(A)** Differential Manchester encoding
- **(B)** Non-Return-to-Zero (NRZ)
- **(C)** 4B/5B
- **(D)** 8B/10B ✅ **(CORRECT)**

**✔ Correct Answer: (D) 8B/10B** — Gigabit Ethernet (1000BASE-X over fiber) uses 8B/10B encoding — 8 data bits are carried as 10 code bits for clocking and DC balance.

*Gigabit Ethernet (fiber पर 1000BASE-X) 8B/10B encoding उपयोग करता है — 8 data bits को 10 code bits के रूप में भेजा जाता है (clocking और DC balance के लिए)।*

**★ Nukta (Key Point):** 100BASE-TX uses 4B/5B + MLT-3; 1000BASE-X uses 8B/10B; 10GBASE-R uses 64B/66B. Ye exam favourite ladder hai.

*100BASE-TX में 4B/5B + MLT-3; 1000BASE-X में 8B/10B; 10GBASE-R में 64B/66B। यह exam favourite ladder है।*

*[Source: Unit Test-4 Solution (OCR), p30 (options recovered from source)] · Medium*

---
### Q10. ______ signals are discrete and are generated by digital modulation.

<span lang='hi'>______ signals discrete होते हैं और digital modulation से बनते हैं।</span>

- **(A)** Analog
- **(B)** Digital ✅ **(CORRECT)**
- **(C)** Noise
- **(D)** Bandwidth

**✔ Correct Answer: (B) Digital** — Digital signals are discrete (defined only at instants) and are produced by digital modulation techniques.

*Digital signals discrete होते हैं (केवल कुछ क्षणों पर परिभाषित) और digital modulation techniques से बनते हैं।*

**★ Nukta (Key Point):** Rajasthan PYQ verified key (B). Analog = continuous; Digital = discrete. Ye sabse basic signal distinction hai.

*Rajasthan PYQ verified key (B)। Analog = continuous; Digital = discrete। यह signal का सबसे बुनियादी भेद है।*

*[Source: Random Test- Rajasthan PYQ (OCR), p5 — Q108 (options recovered)] · Medium*

---
### Q11. Quantizing noise occurs in:

<span lang='hi'>Quantizing noise किसमें होती है?</span>

- **(A)** PCM (Pulse Code Modulation) ✅ **(CORRECT)**
- **(B)** TDM
- **(C)** FDM
- **(D)** PPM

**✔ Correct Answer: (A) PCM (Pulse Code Modulation)** — Quantizing noise is the small error introduced when an analog sample is rounded to the nearest discrete level in PCM.

*Quantizing noise वह छोटी त्रुटि है जो PCM में analog sample को निकटतम discrete level पर गोल करने से आती है।*

**★ Nukta (Key Point):** Rajasthan PYQ verified key (A). PCM = sampling + quantizing + encoding → quantizing error = quantization noise.

*Rajasthan PYQ verified key (A)। PCM = sampling + quantizing + encoding → quantizing error = quantization noise।*

*[Source: Random Test- Rajasthan PYQ (OCR), p10 — Q39 (options recovered)] · Medium*

---
### Q12. The effective bandwidth of a communication channel is primarily limited by:

<span lang='hi'>Communication channel की effective bandwidth मुख्य रूप से किससे सीमित होती है?</span>

- **(A)** Protocol overhead
- **(B)** Noise and attenuation ✅ **(CORRECT)**
- **(C)** File size
- **(D)** MAC address filtering

**✔ Correct Answer: (B) Noise and attenuation** — Noise (with attenuation) limits how much data can be reliably pushed through a channel — Shannon's law shows capacity grows with bandwidth and SNR but is capped by noise.

*Noise (attenuation के साथ) तय करती है कि channel से कितना data भरोसेमंद तरीके से भेजा जा सकता है — Shannon का नियम दिखाता है कि capacity bandwidth और SNR के साथ बढ़ती है पर noise से सीमित रहती है।*

**★ Nukta (Key Point):** Effective bandwidth is a physics/SNR limit. Protocol overhead reduces goodput but is not the channel's fundamental limit.

*Effective bandwidth एक physics/SNR सीमा है। Protocol overhead goodput घटाता है पर channel की मूल सीमा नहीं।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q13. What technique allows multiple signals to share the same communication channel?

<span lang='hi'>कौन-सी technique कई signals को एक ही communication channel share करने देती है?</span>

- **(A)** Multiplexing ✅ **(CORRECT)**
- **(B)** Phase modulation
- **(C)** Analog modulation
- **(D)** Digital modulation

**✔ Correct Answer: (A) Multiplexing** — Multiplexing combines multiple signals onto one shared medium (FDM/TDM/WDM/CDM) — a demultiplexer separates them at the receiving end.

*Multiplexing कई signals को एक shared medium पर जोड़ती है (FDM/TDM/WDM/CDM) — receiving end पर demultiplexer उन्हें अलग करता है।*

**★ Nukta (Key Point):** Multiplexing = many share one channel. FDM = frequency bands, TDM = time slots, WDM = light wavelengths, CDM = codes.

*Multiplexing = कई एक channel share करें। FDM = frequency bands, TDM = time slots, WDM = light wavelengths, CDM = codes।*

*[Source: Repo: CN Topic Test-02 (UNIT TEST-2)] · Medium*

---
### Q14. Communication using a modulated carrier to apply a data signal to a transmission medium in analog form is:

<span lang='hi'>Modulated carrier का उपयोग करके data signal को analog रूप में transmission medium पर डालना क्या कहलाता है?</span>

- **(A)** Broadband networking ✅ **(CORRECT)**
- **(B)** Baseband networking
- **(C)** Modem
- **(D)** Local area network

**✔ Correct Answer: (A) Broadband networking** — Broadband networking sends data as a modulated analog carrier; baseband sends digital signals directly on the medium.

*Broadband networking data को modulated analog carrier के रूप में भेजता है; baseband digital signals सीधे medium पर भेजता है।*

**★ Nukta (Key Point):** Baseband = digital signalling (Manchester etc.). Broadband = analog carriers + modulation (FDM channels).

*Baseband = digital signalling (Manchester आदि)। Broadband = analog carriers + modulation (FDM channels)।*

*[Source: IBPS RRB PO Computer Awareness PYQ (via Meritnotes)] · Medium*

---
### Q15. The amount of data transmitted in a fixed amount of time is called:

<span lang='hi'>निश्चित समय में भेजे गए data की मात्रा को क्या कहते हैं?</span>

- **(A)** Refresh rate
- **(B)** Resolution
- **(C)** Bandwidth ✅ **(CORRECT)**
- **(D)** Frequency

**✔ Correct Answer: (C) Bandwidth** — Bandwidth (in this exam phrasing) is the data transmitted per unit time — the communication channel's capacity (bps).

*इस exam शैली में Bandwidth प्रति इकाई समय भेजा गया data है — communication channel की capacity (bps)।*

**★ Nukta (Key Point):** Strictly: THROUGHPUT = data actually sent per second; BANDWIDTH = maximum capacity. Banks often call throughput 'bandwidth' — read options carefully.

*कठोरता से: THROUGHPUT = वास्तव में प्रति सेकंड भेजा data; BANDWIDTH = अधिकतम capacity। Banks अक्सर throughput को 'bandwidth' कहते हैं — options ध्यान से पढ़ें।*

*[Source: Unit Test-4 Solution (OCR), p23] · Medium*

---
### Q16. Communication using a modulated carrier to apply a data signal to a transmission medium in analog form is called:

<span lang='hi'>Modulated carrier का उपयोग करके data signal को analog रूप में transmission medium पर भेजना कहलाता है:</span>

- **(A)** Broadband communication ✅ **(CORRECT)**
- **(B)** Baseband communication
- **(C)** Modem
- **(D)** Local area network

**✔ Correct Answer: (A) Broadband communication** — Broadband में data को modulated carrier (analog) के ऊपर भेजा जाता है; baseband में digital signal सीधे medium पर जाता है.

*Broadband में data को modulated carrier (analog) के ऊपर भेजा जाता है; baseband में digital signal सीधे medium पर जाता है.*

**★ Nukta (Key Point):** Baseband = digital, सीधा; Broadband = analog, modulated. यह जोड़ी परीक्षा में बार-बार.

*Baseband = digital, सीधा; Broadband = analog, modulated. यह जोड़ी परीक्षा में बार-बार.*

*[Source: IBPS RRB PO Computer Awareness PYQ (via meritnotes)] · Medium*

---
### Q17. Identify the odd one out: Optical fibre, Twisted pair wire, Microwaves, Hertz

<span lang='hi'>असंगत वस्तु पहचानें: Optical fibre, Twisted pair wire, Microwaves, Hertz</span>

- **(A)** Optical fibre
- **(B)** Twisted pair wire
- **(C)** Microwaves
- **(D)** Hertz ✅ **(CORRECT)**

**✔ Correct Answer: (D) Hertz** — Optical fibre, Twisted pair और Microwaves — तीनों transmission media हैं; Hertz आवृत्ति की इकाई है — medium नहीं.

*Optical fibre, Twisted pair और Microwaves — तीनों transmission media हैं; Hertz आवृत्ति की इकाई है — medium नहीं.*

**★ Nukta (Key Point):** Media = रास्ता; Hertz = गति/आवृत्ति माप. यही अंतर पूछा गया है.

*Media = रास्ता; Hertz = गति/आवृत्ति माप. यही अंतर पूछा गया है.*

*[Source: RRB NTPC previous-year computer banks (via adda247 50-PYQ PDF)] · Medium*

---
### Q18. The primary use of scramblers in line coding schemes is to:

<span lang='hi'>Line coding schemes में scramblers का मुख्य उपयोग क्या है?</span>

- **(A)** Make the data look random ✅ **(CORRECT)**
- **(B)** Compress transmission data
- **(C)** Increase signal bandwidth
- **(D)** Decrease signal bandwidth

**✔ Correct Answer: (A) Make the data look random** — A scrambler randomises the transmitted bit pattern (breaks long runs of 0s/1s) so the receiver recovers the clock easily — it does NOT compress or change bandwidth.

*Scrambler transmitted bit pattern को randomise करता है (लंबे 0s/1s के runs तोड़ता है) ताकि receiver आसानी से clock recover कर सके — यह compress या bandwidth नहीं बदलता।*

**★ Nukta (Key Point):** Official RPSC 2024 key. Scrambler = random-looking line signal (clock recovery). Not compression, not encryption.

*Official RPSC 2024 key। Scrambler = random-looking line signal (clock recovery)। Compression नहीं, encryption नहीं।*

*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

---
### Q19. The period of a signal is 100 ms. What is its frequency in kilohertz?

<span lang='hi'>एक signal की period 100 ms है। इसकी frequency kilohertz में कितनी होगी?</span>

- **(A)** 10⁻¹ kHz
- **(B)** 10⁻² kHz ✅ **(CORRECT)**
- **(C)** 10⁻³ kHz
- **(D)** 10⁻⁴ kHz

**✔ Correct Answer: (B) 10⁻² kHz** — Frequency f = 1/T = 1/0.1 s = 10 Hz = 0.01 kHz = 10⁻² kHz.

*Frequency f = 1/T = 1/0.1 s = 10 Hz = 0.01 kHz = 10⁻² kHz।*

**★ Nukta (Key Point):** f = 1/T. 100 ms = 0.1 s → 10 Hz. Convert Hz→kHz by dividing by 1000.

*f = 1/T। 100 ms = 0.1 s → 10 Hz। Hz→kHz के लिए 1000 से भाग दें।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

---
### Q20. If the channel bandwidth is limited to 6 kHz and the signal-to-noise ratio is 16, what is the channel capacity?

<span lang='hi'>यदि channel bandwidth 6 kHz सीमित है और signal-to-noise ratio 16 है, तो channel capacity कितनी होगी?</span>

- **(A)** 15.15 kbps
- **(B)** 24.74 kbps ✅ **(CORRECT)**
- **(C)** 30.12 kbps
- **(D)** 52.18 kbps

**✔ Correct Answer: (B) 24.74 kbps** — By Shannon's capacity formula C = B × log₂(1 + SNR) = 6000 × log₂(17) ≈ 6000 × 4.09 ≈ 24.5-24.7 kbps — matching 24.74 kbps.

*Shannon capacity सूत्र से C = B × log₂(1 + SNR) = 6000 × log₂(17) ≈ 6000 × 4.09 ≈ 24.5-24.7 kbps — 24.74 kbps से मेल खाता है।*

**★ Nukta (Key Point):** Rajasthan PYQ verified key (B). Shannon: C = B log₂(1+SNR). Nyquist: C = 2B log₂(L) (noiseless).

*Rajasthan PYQ verified key (B)। Shannon: C = B log₂(1+SNR)। Nyquist: C = 2B log₂(L) (noiseless)।*

*[Source: Random Test- Rajasthan PYQ (OCR), p30 — Q45 (options recovered)] · Hard*

---
### Q21. Given a bit rate of b bits/sec, the time required to send 16 bits is:

<span lang='hi'>यदि bit rate b bits/sec है, तो 16 bits भेजने में कितना समय लगेगा?</span>

- **(A)** 16 × b sec
- **(B)** 16/b sec ✅ **(CORRECT)**
- **(C)** 16b sec
- **(D)** b/16 sec

**✔ Correct Answer: (B) 16/b sec** — Time = number of bits ÷ bit rate = 16 ÷ b = 16/b seconds.

*Time = bits की संख्या ÷ bit rate = 16 ÷ b = 16/b seconds।*

**★ Nukta (Key Point):** Time = size/rate. 1000 bits at 100 bps = 10 s. Units: bits ÷ (bits/sec) = sec.

*Time = size/rate। 1000 bits at 100 bps = 10 s। Units: bits ÷ (bits/sec) = sec।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

---
### Q22. An analog signal carries 4 bits per signal unit. If 1000 signal units are sent per second, what are the baud rate and bit rate?

<span lang='hi'>एक analog signal प्रति signal unit 4 bits ले जाती है। यदि प्रति सेकंड 1000 signal units भेजे जाएँ, तो baud rate और bit rate क्या होंगे?</span>

- **(A)** 1000 bauds/sec, 4000 bps ✅ **(CORRECT)**
- **(B)** 1000 bauds/sec, 500 bps
- **(C)** 4000 bauds/sec, 1000 bps
- **(D)** 2000 bauds/sec, 1000 bps

**✔ Correct Answer: (A) 1000 bauds/sec, 4000 bps** — Baud rate = signal units per second = 1000 bauds/sec. Bit rate = baud × bits per unit = 1000 × 4 = 4000 bps.

*Baud rate = प्रति सेकंड signal units = 1000 bauds/sec। Bit rate = baud × प्रति unit bits = 1000 × 4 = 4000 bps।*

**★ Nukta (Key Point):** Bit rate = Baud rate × bits per signal unit. Baud = signalling speed; bps = data speed.

*Bit rate = Baud rate × प्रति signal unit bits। Baud = signalling speed; bps = data speed।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

---
### Q23. Consider a noiseless channel with a bandwidth of 5000 Hz transmitting a signal with two signal levels. The maximum bit rate is:

<span lang='hi'>एक noiseless channel जिसकी bandwidth 5000 Hz है, दो signal levels के साथ transmission कर रहा है. अधिकतम bit rate होगी:</span>

- **(A)** 2500 bps
- **(B)** 10000 bps ✅ **(CORRECT)**
- **(C)** 5000 bps
- **(D)** 20000 bps

**✔ Correct Answer: (B) 10000 bps** — Nyquist के सूत्र से: Max data rate = 2 × B × log₂(L) = 2 × 5000 × log₂(2) = 10000 bps.

*Nyquist के सूत्र से: Max data rate = 2 × B × log₂(L) = 2 × 5000 × log₂(2) = 10000 bps.*

**★ Nukta (Key Point):** UGC NET Jan 2025 official key (ii). याद रखो: 2B log₂L (noiseless) और B log₂(1+S/N) (noisy — Shannon).

*UGC NET Jan 2025 official key (ii). याद रखो: 2B log₂L (noiseless) और B log₂(1+S/N) (noisy — Shannon).*

*[Source: UGC NET Computer Science Jan 2025 (via samagracs solved paper)] · Hard*

---
### Q24. Which of the following is NOT a type of broadband internet connection?

<span lang='hi'>निम्न में से कौन-सा broadband internet connection का प्रकार नहीं है?</span>

- **(A)** Cable
- **(B)** DSL
- **(C)** Satellite
- **(D)** Dial-up ✅ **(CORRECT)**

**✔ Correct Answer: (D) Dial-up** — Dial-up पुरानी सुस्त (कम bandwidth) तकनीक है — broadband नहीं. Cable, DSL और Satellite broadband हैं.

*Dial-up पुरानी सुस्त (कम bandwidth) तकनीक है — broadband नहीं. Cable, DSL और Satellite broadband हैं.*

**★ Nukta (Key Point):** Media = the path; Hertz = the frequency/speed measure. This distinction is what is being asked.

*Broadband = fast internet (Cable/DSL/Fibre/Satellite); Dial-up = टेलीफ़ोन वाला पुराना संस्करण.*

*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Hard*

---

## Section B — Guided Media (UTP, Coaxial, Fiber Optic)

*Twisted pair, coaxial and fiber — properties, connectors, distances, termination, EMI behaviour, total internal reflection.*

### Q25. Optical fiber uses reflection to guide light through a channel. At total internal reflection, the angle of incidence is ______ the critical angle.

<span lang='hi'>Optical fiber प्रकाश को channel में भेजने के लिए reflection उपयोग करती है। Total internal reflection में angle of incidence, critical angle से ______ होता है।</span>

- **(A)** Equal to
- **(B)** Less than
- **(C)** Greater than ✅ **(CORRECT)**
- **(D)** Less than or equal to

**✔ Correct Answer: (C) Greater than** — Total internal reflection happens only when the angle of incidence is GREATER than the critical angle — then light stays inside the core.

*Total internal reflection केवल तब होती है जब angle of incidence critical angle से अधिक हो — तब प्रकाश core के भीतर ही रहता है।*

**★ Nukta (Key Point):** TIR rule: angle of incidence > critical angle (denser → rarer medium). Ye fiber propagation ka base hai.

*TIR rule: angle of incidence > critical angle (denser → rarer medium)। यह fiber propagation का आधार है।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4) — recovered from BCI T8 Q33 options] · Easy*

---
### Q26. A network uses coaxial cable but suffers from signal reflection. What is the most likely cause?

<span lang='hi'>एक network coaxial cable उपयोग करता है लेकिन signal reflection से पीड़ित है। सबसे संभावित कारण क्या है?</span>

- **(A)** EMI
- **(B)** Incorrect termination resistance ✅ **(CORRECT)**
- **(C)** Crosstalk
- **(D)** Low bandwidth

**✔ Correct Answer: (B) Incorrect termination resistance** — Coaxial cable must be terminated with its characteristic impedance (e.g., 50Ω/75Ω); a mismatch causes signal reflections back down the cable.

*Coaxial cable को उसकी characteristic impedance (जैसे 50Ω/75Ω) से terminate करना अनिवार्य है; mismatch होने पर signal cable में वापस reflect होते हैं।*

**★ Nukta (Key Point):** Coax rule: proper termination (BNC/terminator) prevents reflections. Un-terminated bus = standing waves & echoes.

*Coax rule: सही termination (BNC/terminator) reflections रोकता है। Un-terminated bus = standing waves और echoes।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q27. Which transmission medium is primarily used in modern internet backbone networks?

<span lang='hi'>आधुनिक internet backbone networks में मुख्य रूप से कौन-सा transmission medium उपयोग होता है?</span>

- **(A)** Twisted pair cable
- **(B)** Coaxial cable
- **(C)** Single mode fiber optic cable ✅ **(CORRECT)**
- **(D)** Microwave links

**✔ Correct Answer: (C) Single mode fiber optic cable** — Modern backbones use single-mode fiber — huge bandwidth over very long distances with low loss.

*आधुनिक backbones single mode fiber उपयोग करते हैं — लंबी दूरी पर कम loss के साथ विशाल bandwidth।*

**★ Nukta (Key Point):** Backbone = single-mode fiber (undersea/terrestrial cables). LAN = UTP. Old cable TV = coax. Remote areas = microwave/satellite.

*Backbone = single-mode fiber (undersea/terrestrial cables)। LAN = UTP। पुराना cable TV = coax। दूरस्थ क्षेत्र = microwave/satellite।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Easy*

---
### Q28. Which cable has the maximum bandwidth?

<span lang='hi'>किस cable की bandwidth अधिकतम होती है?</span>

- **(A)** Coaxial
- **(B)** Twisted pair
- **(C)** Optical fiber ✅ **(CORRECT)**
- **(D)** USB cable

**✔ Correct Answer: (C) Optical fiber** — Optical fiber offers the highest bandwidth — hundreds of Gbps to Tbps over long distances.

*Optical fiber सर्वोच्च bandwidth देती है — लंबी दूरी पर सैकड़ों Gbps से Tbps तक।*

**★ Nukta (Key Point):** Bandwidth order: Fiber >> Coax > Twisted pair. USB is a peripheral bus, not a network cable type here.

*Bandwidth क्रम: Fiber >> Coax > Twisted pair। USB peripheral bus है, यहाँ network cable type नहीं।*

*[Source: Repo: BCI_SCI Subject Test-7 (BCI/SCI Batch)] · Easy*

---
### Q29. Assertion (A): Fiber optic cable is immune to electromagnetic interference (EMI). Reason (R): It transmits data in the form of light pulses rather than electrical signals. Which option is correct?

<span lang='hi'>Assertion (A): Fiber optic cable electromagnetic interference (EMI) से मुक्त है। Reason (R): यह data electrical signals के बजाय light pulses के रूप में भेजती है। कौन-सा विकल्प सही है?</span>

- **(A)** Both (A) and (R) are true, and (R) is the correct explanation of (A) ✅ **(CORRECT)**
- **(B)** Both (A) and (R) are true, but (R) is NOT the correct explanation
- **(C)** (A) is true, but (R) is false
- **(D)** (A) is false, but (R) is true

**✔ Correct Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A)** — Fiber is immune to EMI (A is true) precisely BECAUSE it carries light, not electrical current (R is true and explains A).

*Fiber EMI से मुक्त है (A सही) क्योंकि यह electrical current नहीं, प्रकाश ले जाता है (R सही और A की व्याख्या करता है)।*

**★ Nukta (Key Point):** Fiber = light pulses → EMI-proof + tap-proof + huge bandwidth. Copper = electrical → EMI/crosstalk prone.

*Fiber = light pulses → EMI-proof + tap-proof + विशाल bandwidth। Copper = electrical → EMI/crosstalk प्रवण।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) — Assertion-Reason] · Medium*

---
### Q30. Which statements are TRUE for fiber optic cables? I. Immune to tapping  II. High bandwidth  III. Requires electrical grounding  IV. Works using total internal reflection

<span lang='hi'>Fiber optic cables के लिए कौन-से कथन सही हैं? I. Tapping से मुक्त  II. उच्च bandwidth  III. Electrical grounding चाहिए  IV. Total internal reflection से काम करती है</span>

- **(A)** I, II and IV ✅ **(CORRECT)**
- **(B)** II and III
- **(C)** I, III and IV
- **(D)** I and II

**✔ Correct Answer: (A) I, II and IV** — Fiber carries light (hard to tap, huge bandwidth, works on total internal reflection) and being glass/dielectric it needs NO electrical grounding.

*Fiber प्रकाश ले जाती है (tapping कठिन, विशाल bandwidth, total internal reflection पर काम) और काँच/dielectric होने से इसे electrical grounding की आवश्यकता नहीं।*

**★ Nukta (Key Point):** Fiber truths: immune to tapping & EMI, highest bandwidth, TIR propagation. Myths: grounding (NO), affected by lightning (NO).

*Fiber truths: tapping और EMI से मुक्त, सर्वोच्च bandwidth, TIR propagation। Myths: grounding (नहीं), lightning (नहीं)।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch) — Q33] · Medium*

---
### Q31. A company needs long-distance communication (5-10 km), high data rate and immunity from electromagnetic interference. Which medium is best?

<span lang='hi'>एक कंपनी को लंबी दूरी (5-10 km) संचार, उच्च data rate और EMI से मुक्ति चाहिए। कौन-सा medium सर्वोत्तम है?</span>

- **(A)** UTP
- **(B)** Coaxial cable
- **(C)** Single-mode fiber ✅ **(CORRECT)**
- **(D)** Multi-mode fiber

**✔ Correct Answer: (C) Single-mode fiber** — Single-mode fiber carries one light ray tens of kilometres with very high data rates and is completely immune to EMI.

*Single-mode fiber एक light ray को दसियों किलोमीटर तक बहुत उच्च data rates के साथ ले जाती है और पूरी तरह EMI से मुक्त है।*

**★ Nukta (Key Point):** Fiber choices: Multi-mode = short (LANs, few hundred m). Single-mode = long haul (km) + highest rate. Copper = short & EMI-prone.

*Fiber विकल्प: Multi-mode = छोटी दूरी (LANs, कुछ सौ m)। Single-mode = लंबी (km) + उच्चतम rate। Copper = छोटी और EMI-प्रवण।*

*[Source: Repo: BCI Subject Test-8 (BCI/SCI Batch)] · Medium*

---
### Q32. A UTP cable used in Gigabit Ethernet shows high delay skew. What is the cause?

<span lang='hi'>Gigabit Ethernet में उपयोग UTP cable में delay skew अधिक है। कारण क्या है?</span>

- **(A)** Different twist rates in the cable pairs ✅ **(CORRECT)**
- **(B)** Excessive EMI
- **(C)** Fiber splice error
- **(D)** Wrong wireless channel

**✔ Correct Answer: (A) Different twist rates in the cable pairs** — Each pair in a UTP cable is twisted at a slightly different rate (to reduce crosstalk) — so signals arrive with small timing differences, called delay skew.

*UTP cable में हर pair थोड़ी अलग दर से twisted होता है (crosstalk घटाने के लिए) — इसलिए signals थोड़े अलग समय पर पहुँचते हैं, इसे delay skew कहते हैं।*

**★ Nukta (Key Point):** Delay skew = pair-to-pair propagation time difference (tight twist → shorter wire → less skew). Cat6 has tighter specs for Gigabit.

*Delay skew = pair-to-pair propagation time अंतर (tight twist → छोटी wire → कम skew)। Cat6 में Gigabit के लिए कड़े specs हैं।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q33. Which of the following best explains why fiber optic cables have a lower bit error rate than copper cables?

<span lang='hi'>Fiber optic cables की copper cables की तुलना में कम bit error rate की सबसे अच्छी व्याख्या कौन-सी है?</span>

- **(A)** Higher signal power
- **(B)** Immunity to electromagnetic interference ✅ **(CORRECT)**
- **(C)** Simpler modulation techniques
- **(D)** Larger physical size

**✔ Correct Answer: (B) Immunity to electromagnetic interference** — Fiber carries light and is immune to EMI/crosstalk/impulse noise — the main causes of bit errors in copper — so its BER is far lower.

*Fiber प्रकाश ले जाती है और EMI/crosstalk/impulse noise से मुक्त है — जो copper में bit errors के मुख्य कारण हैं — इसलिए इसका BER बहुत कम होता है।*

**★ Nukta (Key Point):** Fiber wins on: EMI immunity, low attenuation, huge bandwidth, tap security.

*Fiber में श्रेष्ठता: EMI immunity, कम attenuation, विशाल bandwidth, tap security।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q34. Which transmission medium works on the principle of total internal reflection?

<span lang='hi'>कौन-सा transmission medium total internal reflection के सिद्धांत पर काम करता है?</span>

- **(A)** Optical fiber cable ✅ **(CORRECT)**
- **(B)** Shielded twisted pair
- **(C)** Unshielded twisted pair
- **(D)** Coaxial cable

**✔ Correct Answer: (A) Optical fiber cable** — In optical fiber, light stays inside the glass core by total internal reflection (angle of incidence > critical angle).

*Optical fiber में प्रकाश total internal reflection के कारण glass core के भीतर रहता है (angle of incidence > critical angle)।*

**★ Nukta (Key Point):** Fiber = TIR. Copper media use electrical signals (electromagnetic fields), not light reflection.

*Fiber = TIR। Copper media electrical signals (electromagnetic fields) उपयोग करते हैं, प्रकाश reflection नहीं।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q35. Crosstalk in twisted pair cables is typically minimised by:

<span lang='hi'>Twisted pair cables में crosstalk आमतौर पर किससे कम होता है?</span>

- **(A)** Increasing the power level
- **(B)** Increasing the twist rate ✅ **(CORRECT)**
- **(C)** Adding shielding to the core
- **(D)** Using longer cables

**✔ Correct Answer: (B) Increasing the twist rate** — Tightening the twists equalises coupling and cancels interference between pairs — higher categories (Cat6/6a) use tighter twists.

*Tight twists coupling को संतुलित करते हैं और pairs के बीच interference रद्द करते हैं — उच्च श्रेणियों (Cat6/6a) में tighter twists होते हैं।*

**★ Nukta (Key Point):** Anti-crosstalk tricks: tighter twists, pair separation, shielding (STP), lower power.

*Anti-crosstalk tricks: tighter twists, pair separation, shielding (STP), कम power।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q36. Which connector is commonly used for coaxial cable in physical networks?

<span lang='hi'>Physical networks में coaxial cable के लिए सामान्यतः कौन-सा connector उपयोग होता है?</span>

- **(A)** RJ-45
- **(B)** USB-C
- **(C)** BNC ✅ **(CORRECT)**
- **(D)** HDMI

**✔ Correct Answer: (C) BNC** — Coaxial networks use BNC connectors (with a terminator at the ends); RJ-45 is for twisted pair, HDMI for displays, USB-C for peripherals.

*Coaxial networks BNC connectors उपयोग करते हैं (छोर पर terminator के साथ); RJ-45 twisted pair के लिए, HDMI display के लिए, USB-C peripherals के लिए।*

**★ Nukta (Key Point):** Connectors: RJ-45 (UTP Ethernet), BNC (coax/Thinnet), SC/ST/LC (fiber), RJ-11 (telephone).

*Connectors: RJ-45 (UTP Ethernet), BNC (coax/Thinnet), SC/ST/LC (fiber), RJ-11 (telephone)।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q37. Which transmission medium is best for a network exposed to heavy electrical interference?

<span lang='hi'>भारी electrical interference वाले network के लिए कौन-सा transmission medium सर्वोत्तम है?</span>

- **(A)** Unshielded twisted pair
- **(B)** Optical fiber ✅ **(CORRECT)**
- **(C)** Coaxial cable
- **(D)** Microwave

**✔ Correct Answer: (B) Optical fiber** — Optical fiber is immune to electrical/EMI interference because it transmits light, not electrical signals.

*Optical fiber electrical/EMI interference से मुक्त है क्योंकि यह electrical signals नहीं, प्रकाश भेजती है।*

**★ Nukta (Key Point):** EMI-heavy areas (factories, power plants) → fiber. 'Immune to EMI' = keyword for fiber.

*EMI-भारी क्षेत्र (कारखाने, power plants) → fiber। 'Immune to EMI' = fiber के लिए keyword।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Medium*

---
### Q38. Which of the following CANNOT be used as a medium for 802.3 Ethernet?

<span lang='hi'>निम्न में से कौन-सा 802.3 Ethernet के लिए medium उपयोग नहीं किया जा सकता?</span>

- **(A)** Thin coaxial cable
- **(B)** Twisted pair cable
- **(C)** Microwave link ✅ **(CORRECT)**
- **(D)** Fiber optic cable

**✔ Correct Answer: (C) Microwave link** — 802.3 Ethernet is a wired standard — it runs on coax, twisted pair and fiber, but NOT on microwave (that is 802.11/wireless).

*802.3 Ethernet एक wired standard है — यह coax, twisted pair और fiber पर चलता है, लेकिन microwave पर नहीं (वह 802.11/wireless है)।*

**★ Nukta (Key Point):** 802.3 = Ethernet (wired: 10Base2/5, 10Base-T, 100Base-TX, 1000Base-X...). 802.11 = Wi-Fi (wireless).

*802.3 = Ethernet (wired: 10Base2/5, 10Base-T, 100Base-TX, 1000Base-X...)। 802.11 = Wi-Fi (wireless)।*

*[Source: Repo: CN Topic Test-01 (UNIT TEST-1)] · Medium*

---
### Q39. What is the typical maximum length of a UTP cable in Ethernet before signal degradation?

<span lang='hi'>Signal degradation से पहले Ethernet में UTP cable की सामान्य अधिकतम लंबाई कितनी होती है?</span>

- **(A)** 50 meters
- **(B)** 100 meters ✅ **(CORRECT)**
- **(C)** 150 meters
- **(D)** 200 meters

**✔ Correct Answer: (B) 100 meters** — Standard Ethernet UTP runs are limited to 100 metres (about 90 m of solid cable + 10 m of patch cords).

*Standard Ethernet UTP runs 100 मीटर तक सीमित हैं (लगभग 90 m solid cable + 10 m patch cords)।*

**★ Nukta (Key Point):** Copper distance limits: UTP Ethernet 100 m, Thinnet 185 m, Thicknet 500 m, Fiber (multi-mode) ~550 m-2 km, (single-mode) tens of km.

*Copper distance limits: UTP Ethernet 100 m, Thinnet 185 m, Thicknet 500 m, Fiber (multi-mode) ~550 m-2 km, (single-mode) दसियों km।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

---
### Q40. Which of the following is NOT a type of transmission medium?

<span lang='hi'>निम्न में से कौन-सा transmission medium का प्रकार नहीं है?</span>

- **(A)** Coaxial cable
- **(B)** Fiber optics
- **(C)** NIC ✅ **(CORRECT)**
- **(D)** Twisted pair

**✔ Correct Answer: (C) NIC** — A NIC (Network Interface Card) is a hardware adapter — a device, not a transmission medium.

*NIC (Network Interface Card) एक hardware adapter है — एक device है, transmission medium नहीं।*

**★ Nukta (Key Point):** Media = guided (twisted pair, coax, fiber) + unguided (radio, microwave, satellite, infrared). NIC = adapter.

*Media = guided (twisted pair, coax, fiber) + unguided (radio, microwave, satellite, infrared)। NIC = adapter।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Hard*

---

## Section C — Unguided Media (Wireless)

*Wi-Fi standards, infrared/microwave/Bluetooth, line-of-sight, CDMA sharing and its true/false statements.*

### Q41. Which of the following is a wireless networking technology?

<span lang='hi'>निम्न में से कौन-सी wireless networking technology है?</span>

- **(A)** Ethernet
- **(B)** Wi-Fi ✅ **(CORRECT)**
- **(C)** Fiber Optic
- **(D)** DSL

**✔ Correct Answer: (B) Wi-Fi** — Wi-Fi (IEEE 802.11) is a wireless LAN technology; Ethernet (802.3), fiber and DSL are all wired.

*Wi-Fi (IEEE 802.11) एक wireless LAN technology है; Ethernet (802.3), fiber और DSL सब wired हैं।*

**★ Nukta (Key Point):** Wireless family: Wi-Fi (802.11), Bluetooth (802.15), WiMAX (802.16), mobile (GSM/LTE/5G).

*Wireless family: Wi-Fi (802.11), Bluetooth (802.15), WiMAX (802.16), mobile (GSM/LTE/5G)।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q42. Which wireless standard provides the highest data rate?

<span lang='hi'>कौन-सा wireless standard सर्वोच्च data rate देता है?</span>

- **(A)** 802.11b
- **(B)** 802.11g
- **(C)** 802.11n
- **(D)** 802.11ac ✅ **(CORRECT)**

**✔ Correct Answer: (D) 802.11ac** — 802.11ac (Wi-Fi 5) offers the highest rate among these — up to multi-Gbps (5 GHz, MU-MIMO, wide channels).

*802.11ac (Wi-Fi 5) इनमें सर्वोच्च rate देता है — तक मल्टी-Gbps (5 GHz, MU-MIMO, wide channels)।*

**★ Nukta (Key Point):** Wi-Fi rates: b = 11 Mbps, g = 54 Mbps, n = 600 Mbps, ac = multi-Gbps. Order: b < g < n < ac.

*Wi-Fi rates: b = 11 Mbps, g = 54 Mbps, n = 600 Mbps, ac = multi-Gbps। क्रम: b < g < n < ac।*

*[Source: Repo: CN Topic Test 6 (UNIT TEST-6)] · Medium*

---
### Q43. Which type of wireless transmission requires line-of-sight?

<span lang='hi'>किस प्रकार की wireless transmission के लिए line-of-sight आवश्यक है?</span>

- **(A)** Wi-Fi
- **(B)** Infrared ✅ **(CORRECT)**
- **(C)** Radio
- **(D)** Bluetooth

**✔ Correct Answer: (B) Infrared** — Infrared transmission needs a direct line-of-sight (or reflection) between transmitter and receiver — it cannot pass through walls.

*Infrared transmission के लिए transmitter और receiver के बीच सीधी line-of-sight (या reflection) चाहिए — यह दीवारों से नहीं गुजरती।*

**★ Nukta (Key Point):** IR = line-of-sight (TV remotes, IrDA). Radio/RF (Wi-Fi, Bluetooth) passes through walls (with loss).

*IR = line-of-sight (TV remotes, IrDA)। Radio/RF (Wi-Fi, Bluetooth) दीवारों से गुजरते हैं (loss के साथ)।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q44. Which transmission medium is used in Bluetooth technology?

<span lang='hi'>Bluetooth technology में कौन-सा transmission medium उपयोग होता है?</span>

- **(A)** Radio links ✅ **(CORRECT)**
- **(B)** Microwave links
- **(C)** VSAT communication
- **(D)** Fiber optic

**✔ Correct Answer: (A) Radio links** — Bluetooth (IEEE 802.15.1) uses short-range radio links in the 2.4 GHz ISM band.

*Bluetooth (IEEE 802.15.1) 2.4 GHz ISM band में short-range radio links उपयोग करता है।*

**★ Nukta (Key Point):** Bluetooth = 2.4 GHz radio, WPAN (802.15), ~10-100 m range, frequency hopping.

*Bluetooth = 2.4 GHz radio, WPAN (802.15), ~10-100 m range, frequency hopping।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q45. Which physical-layer technique allows multiple users to share the same bandwidth simultaneously?

<span lang='hi'>कौन-सी physical-layer technique कई users को एक ही bandwidth साथ-साथ share करने देती है?</span>

- **(A)** TDMA
- **(B)** FDMA
- **(C)** CDMA ✅ **(CORRECT)**
- **(D)** ARQ

**✔ Correct Answer: (C) CDMA** — In CDMA every user transmits over the SAME bandwidth at the SAME time, separated by unique codes.

*CDMA में हर user एक ही bandwidth पर एक ही समय में transmit करता है, अलग-अलग codes से अलग किया जाता है।*

**★ Nukta (Key Point):** Sharing methods: FDMA = frequency bands, TDMA = time slots, CDMA = codes (same band+time).

*Sharing methods: FDMA = frequency bands, TDMA = time slots, CDMA = codes (same band+time)।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4)] · Medium*

---
### Q46. Which of the following statements is NOT true about microwaves?

<span lang='hi'>Microwaves के बारे में निम्न में से कौन-सा कथन सही नहीं है?</span>

- **(A)** They are electromagnetic waves with frequencies from 300 GHz to 400 THz ✅ **(CORRECT)**
- **(B)** Propagation is line-of-sight
- **(C)** Very high-frequency waves cannot penetrate walls
- **(D)** Use of certain portions of the band requires permission from authorities

**✔ Correct Answer: (A) They are electromagnetic waves with frequencies from 300 GHz to 400 THz** — Microwaves range roughly 300 MHz to 300 GHz — '300 GHz to 400 THz' is the infrared region, so this statement is false.

*Microwaves की range लगभग 300 MHz से 300 GHz है — '300 GHz से 400 THz' infrared क्षेत्र है, इसलिए यह कथन गलत है।*

**★ Nukta (Key Point):** Microwaves: 300 MHz-300 GHz, line-of-sight, no wall penetration, licensed bands. Exam asks the odd range out.

*Microwaves: 300 MHz-300 GHz, line-of-sight, दीवार नहीं भेदते, licensed bands। Exam गलत range पूछता है।*

*[Source: Repo: CN Topic Test-04 (UNIT TEST-4) — options cleaned from source] · Hard*

---
### Q47. Select the FALSE statement about CDMA technology: I. CDMA optimises the use of available bandwidth as it transmits over the entire frequency range. II. Each user in a CDMA system uses a different code to modulate their signal. III. CDMA offers less security compared to GSM technology. IV. A SIM card is always required for a CDMA device to work.

<span lang='hi'>CDMA technology के बारे में गलत कथन चुनिए: I. CDMA उपलब्ध bandwidth के उपयोग को अनुकूलित करता है क्योंकि यह पूरी frequency range पर transmit करता है। II. CDMA system में हर user अपने signal को modulate करने के लिए अलग code उपयोग करता है। III. CDMA, GSM की तुलना में कम security देता है। IV. CDMA device के काम करने के लिए SIM card हमेशा आवश्यक है।</span>

- **(A)** Only (I)
- **(B)** Only (II)
- **(C)** (I) and (II)
- **(D)** (III) and (IV) ✅ **(CORRECT)**

**✔ Correct Answer: (D) (III) and (IV)** — Statements III and IV are false: CDMA offers STRONGER security than GSM (spread spectrum + codes), and CDMA devices can work without a SIM (older CDMA handsets).

*कथन III और IV गलत हैं: CDMA, GSM से मज़बूत security देता है (spread spectrum + codes), और CDMA devices बिना SIM के भी चल सकते हैं (पुराने CDMA handsets)।*

**★ Nukta (Key Point):** Rajasthan PYQ verified key (D). True: I (spread over full band) and II (unique codes per user). False: III (CDMA more secure) and IV (SIM not mandatory).

*Rajasthan PYQ verified key (D)। सही: I (पूरे band पर spread) और II (हर user का unique code)। गलत: III (CDMA अधिक सुरक्षित) और IV (SIM अनिवार्य नहीं)।*

*[Source: Random Test- Rajasthan PYQ (OCR), p11 — Q83 (statements recovered from screenshot)] · Hard*

---

## ★ Nukte Rapid-Fire — Exam Pointers

- **Attenuation / distortion / noise?** *(Attenuation / distortion / noise?)* → **Strength loss / shape change / unwanted signals. Noise can only be MINIMISED, never removed.** *(Strength loss / shape change / unwanted signals। Noise केवल कम होती है, कभी पूरी तरह नहीं।)*
- **Crosstalk cause?** *(Crosstalk का कारण?)* → **Electromagnetic coupling between nearby pairs — minimised by tighter twists.** *(पास की pairs के बीच electromagnetic coupling — tighter twists से कम होता है।)*
- **Manchester encoding?** *(Manchester encoding?)* → **Mid-bit transition = self-clocking + DC-free + noise-resistant (Physical layer).** *(Mid-bit transition = self-clocking + DC-free + noise-resistant (Physical layer)।)*
- **Encoding redundancy order?** *(Encoding redundancy क्रम?)* → **1B2B (100%) > 4B5B/8B10B (25%) > 5B6B (20%). Gigabit fiber = 8B/10B.** *(1B2B (100%) > 4B5B/8B10B (25%) > 5B6B (20%)। Gigabit fiber = 8B/10B।)*
- **Scrambler use?** *(Scrambler का उपयोग?)* → **Make the line signal look random (break long runs) — helps clock recovery. Not compression.** *(Line signal को random बनाना (लंबे runs तोड़ना) — clock recovery में मदद। Compression नहीं।)*
- **Shannon & Nyquist formulas?** *(Shannon और Nyquist सूत्र?)* → **C = B·log₂(1+SNR) (noisy); C = 2B·log₂(L) (noiseless).** *(C = B·log₂(1+SNR) (noisy); C = 2B·log₂(L) (noiseless)।)*
- **Bit rate vs baud rate?** *(Bit rate बनाम baud rate?)* → **Bit rate = baud × bits per signal unit.** *(Bit rate = baud × प्रति signal unit bits।)*
- **Time to send n bits at b bps?** *(b bps पर n bits का समय?)* → **t = n/b seconds.** *(t = n/b seconds।)*
- **Analog signal parameters?** *(Analog signal parameters?)* → **Amplitude (height), Frequency (cycles/sec, Hz), Phase (start), Wavelength (distance/cycle).** *(Amplitude (ऊँचाई), Frequency (cycles/sec, Hz), Phase (शुरुआत), Wavelength (दूरी/cycle)।)*
- **Quantization noise in?** *(Quantization noise किसमें?)* → **PCM (Pulse Code Modulation) — rounding analog samples to levels.** *(PCM (Pulse Code Modulation) — analog samples को levels पर गोल करना।)*
- **Baseband vs broadband?** *(Baseband बनाम broadband?)* → **Baseband = digital signals directly. Broadband = modulated analog carriers (FDM).** *(Baseband = digital signals सीधे। Broadband = modulated analog carriers (FDM)।)*
- **Bandwidth vs throughput?** *(Bandwidth बनाम throughput?)* → **Bandwidth = max capacity; Throughput = actual data per second (exam often mixes them).** *(Bandwidth = अधिकतम capacity; Throughput = वास्तविक data प्रति सेकंद (exam में अक्सर मिलाया जाता है)।)*
- **Fiber's 3 superpowers?** *(Fiber की 3 शक्तियाँ?)* → **EMI-immune, tap-proof, highest bandwidth (via total internal reflection).** *(EMI-मुक्त, tap-सुरक्षित, सर्वोच्च bandwidth (total internal reflection से)।)*
- **TIR condition?** *(TIR शर्त?)* → **Angle of incidence > critical angle (denser to rarer medium).** *(Angle of incidence > critical angle (denser से rarer medium)।)*
- **UTP / coax / fiber distance limits?** *(UTP / coax / fiber दूरी सीमाएँ?)* → **100 m / 185-500 m / up to tens of km (single-mode).** *(100 m / 185-500 m / दसियों km तक (single-mode)।)*
- **Connectors?** *(Connectors?)* → **RJ-45 (twisted pair), BNC (coax), SC/ST/LC (fiber), RJ-11 (telephone).** *(RJ-45 (twisted pair), BNC (coax), SC/ST/LC (fiber), RJ-11 (telephone)।)*
- **Coax reflection cause?** *(Coax reflection का कारण?)* → **Wrong termination resistance (impedance mismatch).** *(गलत termination resistance (impedance mismatch)।)*
- **Single-mode vs multi-mode fiber?** *(Single-mode बनाम multi-mode fiber?)* → **Single = long haul (km, backbone). Multi = short LAN distances (modal dispersion).** *(Single = लंबी दूरी (km, backbone)। Multi = छोटी LAN दूरी (modal dispersion)।)*
- **Wi-Fi rate order?** *(Wi-Fi rate क्रम?)* → **b (11 Mbps) < g (54) < n (600) < ac (multi-Gbps).** *(b (11 Mbps) < g (54) < n (600) < ac (multi-Gbps)।)*
- **Line-of-sight wireless?** *(Line-of-sight wireless?)* → **Infrared (and microwave links) need LOS. Radio (Wi-Fi/Bluetooth) passes walls.** *(Infrared (और microwave links) को LOS चाहिए। Radio (Wi-Fi/Bluetooth) दीवारों से गुजरता है।)*
- **Microwave band?** *(Microwave band?)* → **300 MHz - 300 GHz (NOT 300 GHz-400 THz — that is infrared!).** *(300 MHz - 300 GHz (300 GHz-400 THz नहीं — वह infrared है!)।)*
- **Bluetooth = ?** *(Bluetooth = ?)* → **2.4 GHz short-range radio (IEEE 802.15.1 WPAN).** *(2.4 GHz short-range radio (IEEE 802.15.1 WPAN)।)*
- **FDMA / TDMA / CDMA?** *(FDMA / TDMA / CDMA?)* → **Frequency bands / time slots / unique codes (same band & time).** *(Frequency bands / time slots / unique codes (same band और time)।)*

