# Data Communication & Computer Networks (CN)
## Topic 7 of 7 : Network Security — 53 MCQs (English + Hindi)

**Reference Book:** Data Communications and Networking — Behrouz A. Forouzan

**Prepared for:** RPSC Programmer • ACP • RSMSSB IA • SA • DD • BCI • SCI • REET • RAS • DSSSB • KVS • NVS • HTET • SSC CGL/CHSL • RRB • IBPS • UPSC & all Rajasthan + Central Govt. Exams (Computer Awareness)

**Total Questions:** 53 | **Type:** MCQ (4 options) | **Bilingual:** English + Hindi (technical terms in English) | Each: ✔ why the correct answer is right + ★ Nukta. Wrong options verified internally. Answers cross-verified 4×.

### Syllabus Coverage (sub-topic wise order)

| # | Sub-topic | Questions |
|---|-----------|-----------|
| 1 | Section A — Security Goals & Attacks | Q1 - Q17 |
| 2 | Section B — Cryptography | Q18 - Q38 |
| 3 | Section C — Firewalls, IPSec & Security Protocols | Q39 - Q53 |

---

## Section A — Security Goals & Attacks

*CIA triad, attack-goal mapping (interception/modification/DoS/spoofing), active vs passive attacks, malware phases, security tools.*

### Q1. In the virus life cycle, which phase actually performs the malicious activity?

<span lang='hi'>Virus life cycle में कौन-सा phase वास्तव में malicious activity करता है?</span>

- **(A)** Infection Phase
- **(B)** Triggering Phase
- **(C)** Dormant Phase
- **(D)** Execution (Payload) Phase ✅ **(CORRECT)**

**✔ Correct Answer: (D) Execution (Payload) Phase** — The execution phase runs the payload — the actual damage (deleting files, corrupting data).

*Execution phase payload चलाता है — वास्तविक नुकसान (files delete करना, data खराब करना)।*

**★ Nukta (Key Point):** Virus phases: Dormant (idle) → Propagation (copy) → Triggering (condition met) → Execution (payload runs).

*Virus phases: Dormant (idle) → Propagation (copy) → Triggering (condition met) → Execution (payload runs)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q2. Which backup medium provides Write-Once-Read-Many (WORM) functionality?

<span lang='hi'>कौन-सा backup medium Write-Once-Read-Many (WORM) functionality देता है?</span>

- **(A)** Hard disk
- **(B)** Magnetic tape
- **(C)** Optical disk (CD-R / DVD-R) ✅ **(CORRECT)**
- **(D)** Flash drive

**✔ Correct Answer: (C) Optical disk (CD-R / DVD-R)** — CD-R/DVD-R optical disks are WORM — data is written once and cannot be altered, making them tamper-proof archives.

*CD-R/DVD-R optical disks WORM हैं — data एक बार लिखा जाता है और बदला नहीं जा सकता, इसलिए ये tamper-proof archives हैं।*

**★ Nukta (Key Point):** WORM = optical write-once media (CD-R/DVD-R/BD-R). Rewritable: HDD, tape (LTO), flash, CD-RW.

*WORM = optical write-once media (CD-R/DVD-R/BD-R)। Rewritable: HDD, tape (LTO), flash, CD-RW।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q3. Which attack becomes possible if the SAME key is reused many times in symmetric encryption?

<span lang='hi'>यदि symmetric encryption में एक ही key कई बार उपयोग हो, तो कौन-सा attack संभव हो जाता है?</span>

- **(A)** Replay attack
- **(B)** Known-plaintext attack ✅ **(CORRECT)**
- **(C)** Man-in-the-middle attack
- **(D)** Phishing attack

**✔ Correct Answer: (B) Known-plaintext attack** — With many ciphertexts under one key, an attacker can compare them with known plaintexts and deduce the key — a known-plaintext (or frequency-analysis) attack.

*एक key के अंतर्गत अनेक ciphertexts होने पर attacker उन्हें known plaintexts से मिलाकर key निकाल सकता है — known-plaintext (या frequency-analysis) attack।*

**★ Nukta (Key Point):** One-time pads are safe ONLY with a fresh key per message. Reuse → pattern analysis. Exam favourite link: key reuse → known-plaintext.

*One-time pads केवल हर message पर नई key से सुरक्षित हैं। Reuse → pattern analysis। Exam favourite link: key reuse → known-plaintext।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q4. Which of the following tools is mainly used for password cracking?

<span lang='hi'>निम्न में से कौन-सा tool मुख्यतः password cracking के लिए उपयोग होता है?</span>

- **(A)** Wireshark
- **(B)** Nmap
- **(C)** Cain and Abel ✅ **(CORRECT)**
- **(D)** Angry IP Scanner

**✔ Correct Answer: (C) Cain and Abel** — Cain and Abel is a well-known password-recovery/cracking tool (sniffing, dictionary & brute-force attacks).

*Cain and Abel एक प्रसिद्ध password-recovery/cracking tool है (sniffing, dictionary और brute-force attacks)।*

**★ Nukta (Key Point):** Security tools: Wireshark = packet analyser, Nmap = port scanner, Cain&Abel = password cracker, Angry IP Scanner = IP scanner, Snort = IDS.

*Security tools: Wireshark = packet analyser, Nmap = port scanner, Cain&Abel = password cracker, Angry IP Scanner = IP scanner, Snort = IDS।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q5. Which port and IP address scanner is most famous among users?

<span lang='hi'>Users के बीच सबसे प्रसिद्ध port और IP address scanner कौन-सा है?</span>

- **(A)** Cain and Abel
- **(B)** Angry IP Scanner ✅ **(CORRECT)**
- **(C)** Snort
- **(D)** Ettercap

**✔ Correct Answer: (B) Angry IP Scanner** — Angry IP Scanner is the popular free tool for scanning IP ranges and open ports.

*Angry IP Scanner IP ranges और open ports scan करने वाला लोकप्रिय free tool है।*

**★ Nukta (Key Point):** Cain&Abel = password cracking; Angry IP = IP/port scan; Snort = IDS; Ettercap = sniffing/ARP spoofing.

*Cain&Abel = password cracking; Angry IP = IP/port scan; Snort = IDS; Ettercap = sniffing/ARP spoofing।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q6. The term 'CIA triad' in information security refers to:

<span lang='hi'>Information security में 'CIA triad' शब्द किसे कहते हैं?</span>

- **(A)** Cryptography, Integrity, Authentication
- **(B)** Confidentiality, Integrity, Availability ✅ **(CORRECT)**
- **(C)** Confidentiality, Information, Access
- **(D)** Control, Information, Access

**✔ Correct Answer: (B) Confidentiality, Integrity, Availability** — The CIA triad = Confidentiality (only authorised access), Integrity (no unauthorised change), Availability (accessible when needed) — the three core security goals.

*CIA triad = Confidentiality (केवल authorised access), Integrity (बिना authorisation बदलाव नहीं), Availability (ज़रूरत पर उपलब्ध) — तीन मूल security goals।*

**★ Nukta (Key Point):** CIA = Confidentiality, Integrity, Availability. AAA (authentication, authorisation, accounting) is a separate trio.

*CIA = Confidentiality, Integrity, Availability। AAA (authentication, authorisation, accounting) अलग trio है।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q7. A modification attack violates which security goal?

<span lang='hi'>Modification attack कौन-से security लक्ष्य का उल्लंघन करता है?</span>

- **(A)** Confidentiality
- **(B)** Integrity ✅ **(CORRECT)**
- **(C)** Availability
- **(D)** Authentication

**✔ Correct Answer: (B) Integrity** — A modification attack changes data in transit — that breaks INTEGRITY (data is no longer accurate/unaltered).

*Modification attack रास्ते में data बदल देता है — यह INTEGRITY तोड़ता है (data अब सही/अपरिवर्तित नहीं)।*

**★ Nukta (Key Point):** Attack→goal: Eavesdropping/Interception → Confidentiality. Modification → Integrity. DoS/Interruption → Availability. Spoofing → Authentication.

*Attack→goal: Eavesdropping/Interception → Confidentiality। Modification → Integrity। DoS/Interruption → Availability। Spoofing → Authentication।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q8. Which of the following attacks violates confidentiality?

<span lang='hi'>निम्न में से कौन-सा attack confidentiality का उल्लंघन करता है?</span>

- **(A)** Interception ✅ **(CORRECT)**
- **(B)** Modification
- **(C)** Fabrication
- **(D)** Interruption

**✔ Correct Answer: (A) Interception** — Interception (eavesdropping) lets an unauthorised party READ the data — breaking confidentiality.

*Interception (eavesdropping) से unauthorised पक्ष data पढ़ लेता है — confidentiality टूटती है।*

**★ Nukta (Key Point):** Attack map: Interception→Confidentiality, Modification→Integrity, Fabrication→Authenticity, Interruption→Availability.

*Attack map: Interception→Confidentiality, Modification→Integrity, Fabrication→Authenticity, Interruption→Availability।*

*[Source: Subject Test Solution-1 Part-2 (CN & Security) slides] · Medium*

---
### Q9. A Denial of Service (DoS) attack violates which goal?

<span lang='hi'>Denial of Service (DoS) attack कौन-से लक्ष्य का उल्लंघन करता है?</span>

- **(A)** Confidentiality
- **(B)** Integrity
- **(C)** Availability ✅ **(CORRECT)**
- **(D)** Authentication

**✔ Correct Answer: (C) Availability** — A DoS attack floods a server/network so legitimate users cannot access the service — breaking AVAILABILITY.

*DoS attack server/network को flood करके legitimate users को service से रोकता है — Availability टूटती है।*

**★ Nukta (Key Point):** DoS = Availability attack. DDoS = distributed DoS. Smurf/ SYN-flood = DoS variants.

*DoS = Availability attack। DDoS = distributed DoS। Smurf/ SYN-flood = DoS variants।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q10. A spoofing attack targets which security aspect?

<span lang='hi'>Spoofing attack किस security पहलू को लक्षित करता है?</span>

- **(A)** Authentication ✅ **(CORRECT)**
- **(B)** Integrity
- **(C)** Availability
- **(D)** Confidentiality

**✔ Correct Answer: (A) Authentication** — Spoofing pretends to be someone else (fake IP/MAC/email id) — it attacks AUTHENTICATION (who you claim to be).

*Spoofing किसी और का रूप धारण करता है (fake IP/MAC/email id) — यह AUTHENTICATION पर हमला है (आप कौन हैं)।*

**★ Nukta (Key Point):** Spoofing/impersonation → Authentication. Phishing → steals credentials (auth). Sniffing → Confidentiality.

*Spoofing/impersonation → Authentication। Phishing → credentials चुराता है (auth)। Sniffing → Confidentiality।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q11. Which of the following is an ACTIVE attack?

<span lang='hi'>निम्न में से कौन-सा ACTIVE attack है?</span>

- **(A)** Interception
- **(B)** Modification ✅ **(CORRECT)**
- **(C)** Traffic analysis
- **(D)** Eavesdropping

**✔ Correct Answer: (B) Modification** — Modification is an active attack — the attacker CHANGES the data stream; interception/traffic analysis/eavesdropping are passive (they only observe).

*Modification एक active attack है — attacker data stream बदलता है; interception/traffic analysis/eavesdropping passive हैं (केवल देखते हैं)।*

**★ Nukta (Key Point):** Passive = observe only (eavesdropping, traffic analysis). Active = change/disrupt (modification, fabrication, interruption/DoS).

*Passive = केवल देखना (eavesdropping, traffic analysis)। Active = बदलना/बाधा (modification, fabrication, interruption/DoS)।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q12. Match the attacks with their descriptions: (a) Phishing  (b) DoS Attack  (c) Man-in-the-Middle  (d) Spoofing — (i) Flooding network traffic  (ii) Stealing user credentials  (iii) Intercepting communication  (iv) Impersonation attack

<span lang='hi'>हमलों को उनके विवरण से मिलाइए: (a) Phishing  (b) DoS Attack  (c) Man-in-the-Middle  (d) Spoofing — (i) नेटवर्क ट्रैफ़िक भरना  (ii) यूज़र जानकारी चुराना  (iii) संचार में हस्तक्षेप  (iv) पहचान की नकल</span>

- **(A)** a–ii, b–i, c–iii, d–iv ✅ **(CORRECT)**
- **(B)** a–i, b–ii, c–iii, d–iv
- **(C)** a–iii, b–i, c–ii, d–iv
- **(D)** a–ii, b–iii, c–i, d–iv

**✔ Correct Answer: (A) a–ii, b–i, c–iii, d–iv** — Phishing steals credentials (ii), DoS floods traffic (i), MitM intercepts communication (iii), Spoofing is impersonation (iv).

*Phishing credentials चुराता है (ii), DoS traffic flood करता है (i), MitM संचार intercept करता है (iii), Spoofing impersonation है (iv)।*

**★ Nukta (Key Point):** Attack one-liners: Phishing=fake emails/sites, DoS=flood, MitM=middle interception, Spoofing=fake identity.

*Attack one-liners: Phishing=fake emails/sites, DoS=flood, MitM=middle interception, Spoofing=fake identity।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q3 match (codes recovered)] · Medium*

---
### Q13. 'Junk email' is also known as:

<span lang='hi'>'Junk email' को और क्या कहते हैं?</span>

- **(A)** Spam ✅ **(CORRECT)**
- **(B)** Spoof
- **(C)** Sniffer
- **(D)** Spool

**✔ Correct Answer: (A) Spam** — अवांछित भारी-भरकम email = Spam. यह inbox भर देती है और कई बार धोखाधड़ी का ज़रिया होती है.

*अवांछित भारी-भरकम email = Spam. यह inbox भर देती है और कई बार धोखाधड़ी का ज़रिया होती है.*

**★ Nukta (Key Point):** Spam = junk mail; Spoof = पहचान छिपाना; Sniffer = चोरी से सुनना.

*Spam = junk mail; Spoof = पहचान छिपाना; Sniffer = चोरी से सुनना.*

*[Source: RRB NTPC computer banks (via practicemock PYQ set)] · Medium*

---
### Q14. The goal of 'Integrity' ensures that:

<span lang='hi'>'Integrity' का लक्ष्य सुनिश्चित करता है कि:</span>

- **(A)** Data can be accessed only by authorised users
- **(B)** Data is accurate and has not been modified ✅ **(CORRECT)**
- **(C)** Data is always available when needed
- **(D)** Unauthorised users cannot enter the system

**✔ Correct Answer: (B) Data is accurate and has not been modified** — Integrity means data remains accurate and unaltered except by authorised people — checksums/digital signatures protect it.

*Integrity का अर्थ है data सही और अपरिवर्तित रहे (केवल authorised लोग ही बदलें) — इसे checksums/digital signatures सुरक्षित रखते हैं।*

**★ Nukta (Key Point):** Goal map: Confidentiality = authorised access only. Integrity = no unauthorised change. Availability = always accessible.

*Goal map: Confidentiality = केवल authorised access। Integrity = बिना authorisation बदलाव नहीं। Availability = हमेशा उपलब्ध।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

---
### Q15. Which of the following is NOT a goal of network security?

<span lang='hi'>निम्न में से कौन-सा network security का लक्ष्य नहीं है?</span>

- **(A)** Confidentiality
- **(B)** Integrity
- **(C)** Availability
- **(D)** Redundancy ✅ **(CORRECT)**

**✔ Correct Answer: (D) Redundancy** — Redundancy (duplicate links/equipment) improves fault tolerance — it is a reliability technique, not a security goal.

*Redundancy (duplicate links/equipment) fault tolerance बढ़ाती है — यह reliability तकनीक है, security लक्ष्य नहीं।*

**★ Nukta (Key Point):** Security goals = CIA. Reliability goals = redundancy, fault tolerance, recovery.

*Security goals = CIA। Reliability goals = redundancy, fault tolerance, recovery।*

*[Source: Subject Test Solution-1 Part-2 (CN & Security) slides] · Hard*

---
### Q16. The primary difference between active and passive attacks is:

<span lang='hi'>Active और passive attacks के बीच मुख्य अंतर क्या है?</span>

- **(A)** Active attacks change data; passive attacks do not ✅ **(CORRECT)**
- **(B)** Passive attacks destroy hardware
- **(C)** Both are the same
- **(D)** Passive attacks are legal

**✔ Correct Answer: (A) Active attacks change data; passive attacks do not** — Active attacks intercept AND modify/disrupt the communication; passive attacks only eavesdrop without changing anything.

*Active attacks संचार को intercept करके बदलते/बाधित करते हैं; passive attacks केवल सुनते हैं, कुछ नहीं बदलते।*

**★ Nukta (Key Point):** Active: modification, fabrication, interruption. Passive: eavesdropping, traffic analysis. Exam one-liner: 'change vs observe'.

*Active: modification, fabrication, interruption। Passive: eavesdropping, traffic analysis। Exam one-liner: 'change बनाम observe'।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

---
### Q17. A ______ does not perform any destructive action directly; it only consumes system resources to bring the system down.

<span lang='hi'>एक ______ सीधे कोई विनाशकारी काम नहीं करता; वह सिस्टम को गिराने के लिए सिर्फ system resources खाता है.</span>

- **(A)** Virus
- **(B)** Worm ✅ **(CORRECT)**
- **(C)** Trojan
- **(D)** Spyware

**✔ Correct Answer: (B) Worm** — Worm अपनी प्रतियाँ बनाकर network में फैलता है और bandwidth/memory खा जाता है — सीधा डेटा नष्ट नहीं करता.

*Worm अपनी प्रतियाँ बनाकर network में फैलता है और bandwidth/memory खा जाता है — सीधा डेटा नष्ट नहीं करता.*

**★ Nukta (Key Point):** HTET 2024 official key (b). फ़र्क: Virus = फ़ाइल में घुसता; Worm = खुद फैलता; Trojan = छिपकर; Spyware = जासूसी.

*HTET 2024 official key (b). फ़र्क: Virus = फ़ाइल में घुसता; Worm = खुद फैलता; Trojan = छिपकर; Spyware = जासूसी.*

*[Source: HTET 2024 (via KnowledgeGate solved PYQ bank)] · Hard*

---

## Section B — Cryptography

*Plaintext/ciphertext/key, symmetric vs asymmetric ciphers, DES/AES/RSA, stream vs block, classical ciphers, digital signatures, steganography.*

### Q18. The text that gets transformed using a cipher algorithm is called:

<span lang='hi'>Cipher algorithm से जिस text को बदला जाता है उसे क्या कहते हैं?</span>

- **(A)** Complex Text
- **(B)** Transformed Text
- **(C)** Plain Text ✅ **(CORRECT)**
- **(D)** Scalar Text

**✔ Correct Answer: (C) Plain Text** — The INPUT to the cipher is the plaintext; after transformation it becomes ciphertext.

*Cipher का INPUT plaintext है; बदलने के बाद वह ciphertext बनता है।*

**★ Nukta (Key Point):** Cryptography flow: Plain text --(cipher + key)--> Ciphertext --(decipher + key)--> Plain text.

*Cryptography flow: Plain text --(cipher + key)--> Ciphertext --(decipher + key)--> Plain text।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q9] · Easy*

---
### Q19. In the digital signature technique, when the whole message is signed using an asymmetric key, the receiver uses:

<span lang='hi'>Digital signature technique में, जब पूरा संदेश asymmetric key से sign होता है, तो प्राप्तकर्ता उपयोग करता है:</span>

- **(A)** Her or his own public key
- **(B)** Her or his own private key
- **(C)** The sender's public key ✅ **(CORRECT)**
- **(D)** None of these

**✔ Correct Answer: (C) The sender's public key** — The sender signs with their PRIVATE key; the receiver verifies the signature using the SENDER'S PUBLIC key.

*भेजने वाला अपनी PRIVATE key से sign करता है; प्राप्तकर्ता भेजने वाले की PUBLIC key से signature सत्यापित करता है।*

**★ Nukta (Key Point):** Signature direction: SIGN with private → VERIFY with public. Encryption direction: ENCRYPT with public → DECRYPT with private.

*Signature दिशा: private से SIGN → public से VERIFY। Encryption दिशा: public से ENCRYPT → private से DECRYPT।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q20. Which statement about plaintext, ciphertext and key is MOST accurate?

<span lang='hi'>Plaintext, ciphertext और key के बारे में कौन-सा कथन सबसे सही है?</span>

- **(A)** Plaintext is generated after decryption using a public key
- **(B)** Ciphertext is the original readable message
- **(C)** Plaintext is transformed into ciphertext using an algorithm and a key ✅ **(CORRECT)**
- **(D)** Ciphertext and plaintext are always of the same length

**✔ Correct Answer: (C) Plaintext is transformed into ciphertext using an algorithm and a key** — Encryption transforms plaintext into ciphertext using a cipher algorithm together with a key — this is the precise description.

*Encryption एक cipher algorithm और key के साथ plaintext को ciphertext में बदलता है — यही सटीक विवरण है।*

**★ Nukta (Key Point):** Remember the 3 objects: plaintext (readable), ciphertext (scrambled), key (secret parameter). Encryption = f(plaintext, key).

*3 objects याद रखें: plaintext (पढ़ने योग्य), ciphertext (scrambled), key (गुप्त parameter)। Encryption = f(plaintext, key)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q10] · Medium*

---
### Q21. Which of the following uses the SAME key for encryption and decryption?

<span lang='hi'>निम्न में से कौन-सा encryption और decryption के लिए एक ही key उपयोग करता है?</span>

- **(A)** Symmetric key cipher ✅ **(CORRECT)**
- **(B)** Asymmetric key cipher
- **(C)** Hash function
- **(D)** Digital signature

**✔ Correct Answer: (A) Symmetric key cipher** — Symmetric cryptography uses one shared secret key for both encryption and decryption (AES, DES, Blowfish).

*Symmetric cryptography encryption और decryption दोनों के लिए एक ही shared secret key उपयोग करता है (AES, DES, Blowfish)।*

**★ Nukta (Key Point):** Symmetric = 1 key (fast). Asymmetric = key pair (public+private, slow). Hash = one-way digest. Signature = private-sign/public-verify.

*Symmetric = 1 key (तेज़)। Asymmetric = key pair (public+private, धीमा)। Hash = one-way digest। Signature = private-sign/public-verify।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q22. Which of the following uses a PAIR of keys (public and private)?

<span lang='hi'>निम्न में से कौन-सा keys की एक जोड़ी (public और private) उपयोग करता है?</span>

- **(A)** Symmetric cipher
- **(B)** Asymmetric cipher ✅ **(CORRECT)**
- **(C)** DES
- **(D)** AES

**✔ Correct Answer: (B) Asymmetric cipher** — Asymmetric (public-key) cryptography uses a mathematically linked key pair — public key to encrypt, private key to decrypt (RSA, ECC, Diffie-Hellman).

*Asymmetric (public-key) cryptography गणितीय रूप से जुड़ी key pair उपयोग करता है — encrypt के लिए public key, decrypt के लिए private key (RSA, ECC, Diffie-Hellman)।*

**★ Nukta (Key Point):** Public-key examples: RSA, Diffie-Hellman, ECC, DSA. Symmetric: DES, 3DES, AES, Blowfish, RC4.

*Public-key examples: RSA, Diffie-Hellman, ECC, DSA। Symmetric: DES, 3DES, AES, Blowfish, RC4।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q23. Which is FASTER in encryption and decryption?

<span lang='hi'>Encryption और decryption में कौन-सा तेज़ है?</span>

- **(A)** Symmetric key cipher ✅ **(CORRECT)**
- **(B)** Asymmetric key cipher
- **(C)** Cannot decide
- **(D)** None of these

**✔ Correct Answer: (A) Symmetric key cipher** — Symmetric ciphers (AES/DES) are orders of magnitude faster than asymmetric ones (RSA) — that's why bulk data uses symmetric encryption.

*Symmetric ciphers (AES/DES), asymmetric (RSA) से कई गुना तेज़ होते हैं — इसीलिए bulk data में symmetric encryption होती है।*

**★ Nukta (Key Point):** Speed: Symmetric >> Asymmetric. Hybrid systems (TLS/PGP) use asymmetric KEYS to exchange a symmetric SESSION key.

*Speed: Symmetric >> Asymmetric। Hybrid systems (TLS/PGP) asymmetric KEYS से symmetric SESSION key का आदान-प्रदान करती हैं।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q24. What is the main disadvantage of symmetric key encryption?

<span lang='hi'>Symmetric key encryption की मुख्य कमी क्या है?</span>

- **(A)** It is very slow
- **(B)** Key distribution is difficult ✅ **(CORRECT)**
- **(C)** It uses two keys
- **(D)** It cannot encrypt text

**✔ Correct Answer: (B) Key distribution is difficult** — Both sides must share the SAME secret key securely — key distribution over an insecure channel is the classic problem.

*दोनों पक्षों को एक ही secret key सुरक्षित रूप से साझा करनी होती है — insecure channel पर key distribution ही classic समस्या है।*

**★ Nukta (Key Point):** Symmetric weakness = key distribution (n users → n(n-1)/2 keys). Asymmetric weakness = slow + key authenticity (certificates).

*Symmetric कमज़ोरी = key distribution (n users → n(n-1)/2 keys)। Asymmetric कमज़ोरी = धीमा + key authenticity (certificates)।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q25. In public-key cryptography, a message encrypted with the public key can only be decrypted by:

<span lang='hi'>Public-key cryptography में public key से encrypt किया संदेश केवल किसके द्वारा decrypt हो सकता है?</span>

- **(A)** Another public key
- **(B)** The same public key
- **(C)** The private key corresponding to that public key ✅ **(CORRECT)**
- **(D)** A session key

**✔ Correct Answer: (C) The private key corresponding to that public key** — Only the matching private key of the key pair can decrypt what the public key encrypted.

*केवल उस key pair की मेल खाती private key ही public key से encrypt किए गए संदेश को decrypt कर सकती है।*

**★ Nukta (Key Point):** Public/private are mathematically paired — like a lock (public) and its only key (private).

*Public/private गणितीय रूप से जुड़े हैं — एक ताला (public) और उसकी एकमात्र चाबी (private) की तरह।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q26. Data Encryption Standard (DES) is a:

<span lang='hi'>Data Encryption Standard (DES) क्या है?</span>

- **(A)** Block cipher ✅ **(CORRECT)**
- **(B)** Stream cipher
- **(C)** Bit cipher
- **(D)** Byte cipher

**✔ Correct Answer: (A) Block cipher** — DES encrypts data in 64-bit blocks using a 56-bit key — a classic symmetric BLOCK cipher.

*DES data को 64-bit blocks में 56-bit key से encrypt करता है — एक classic symmetric BLOCK cipher।*

**★ Nukta (Key Point):** DES = 64-bit block, 56-bit key (symmetric). AES = 128-bit block. RC4 = stream cipher.

*DES = 64-bit block, 56-bit key (symmetric)। AES = 128-bit block। RC4 = stream cipher।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q27. Which cipher method encrypts one bit or byte at a time?

<span lang='hi'>कौन-सी cipher method एक बार में एक bit या byte encrypt करती है?</span>

- **(A)** Block cipher
- **(B)** Stream cipher ✅ **(CORRECT)**
- **(C)** Substitution cipher
- **(D)** Transposition cipher

**✔ Correct Answer: (B) Stream cipher** — A stream cipher encrypts the data one bit (or byte) at a time as a continuous stream (e.g., RC4).

*Stream cipher data को एक समय में एक bit (या byte) encrypt करती है, एक निरंतर धारा के रूप में (जैसे RC4)।*

**★ Nukta (Key Point):** Stream = 1 bit/byte at a time (RC4, A5/1). Block = fixed-size blocks (DES/AES). Substitution/Transposition = classical techniques.

*Stream = 1 bit/byte at a time (RC4, A5/1)। Block = fixed-size blocks (DES/AES)। Substitution/Transposition = classical techniques।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q28. The Caesar Cipher is an example of which cryptographic technique?

<span lang='hi'>Caesar Cipher किस cryptographic technique का उदाहरण है?</span>

- **(A)** Transposition cipher
- **(B)** Substitution cipher ✅ **(CORRECT)**
- **(C)** Stream cipher
- **(D)** Block cipher

**✔ Correct Answer: (B) Substitution cipher** — The Caesar cipher replaces each letter by another a fixed number of places down the alphabet — a classical SUBSTITUTION cipher.

*Caesar cipher में हर अक्षर को वर्णमाला में कुछ स्थान आगे वाले अक्षर से बदला जाता है — एक classical SUBSTITUTION cipher।*

**★ Nukta (Key Point):** Classical types: Substitution (Caesar, Playfair) = replace; Transposition (Rail fence) = rearrange.

*Classical types: Substitution (Caesar, Playfair) = replace; Transposition (Rail fence) = rearrange।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q29. The process of detecting hidden data inside a file is known as:

<span lang='hi'>किसी file के भीतर छिपे data का पता लगाने की प्रक्रिया को क्या कहते हैं?</span>

- **(A)** Cryptanalysis
- **(B)** Steganalysis ✅ **(CORRECT)**
- **(C)** Data mining
- **(D)** Steganography

**✔ Correct Answer: (B) Steganalysis** — Steganalysis is the art of detecting/extracting data hidden by steganography.

*Steganalysis, steganography से छिपाए गए data का पता लगाने/निकालने की कला है।*

**★ Nukta (Key Point):** Steganography = HIDING data (cover file). Steganalysis = DETECTING it. Cryptography = scrambling it.

*Steganography = data छिपाना (cover file)। Steganalysis = पता लगाना। Cryptography = scramblइंग।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q30. What is the output of a steganography process called?

<span lang='hi'>Steganography प्रक्रिया के output को क्या कहते हैं?</span>

- **(A)** Ciphertext
- **(B)** Stego-object ✅ **(CORRECT)**
- **(C)** Encoded file
- **(D)** Key file

**✔ Correct Answer: (B) Stego-object** — The carrier file that now contains the hidden message is called the stego-object.

*वह carrier file जिसमें अब छिपा संदेश है, stego-object कहलाती है।*

**★ Nukta (Key Point):** Stego terms: cover file (original carrier), secret message (hidden data), stego-object (result).

*Stego terms: cover file (original carrier), secret message (hidden data), stego-object (result)।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Medium*

---
### Q31. In steganography, the file used to hide the secret data is called:

<span lang='hi'>Steganography में secret data छिपाने के लिए जिस file का उपयोग होता है उसे क्या कहते हैं?</span>

- **(A)** Secret file
- **(B)** Cover file ✅ **(CORRECT)**
- **(C)** Cipher file
- **(D)** Key file

**✔ Correct Answer: (B) Cover file** — The innocent-looking carrier (image/audio/document) that hides the secret data is called the cover file.

*वह मासूम दिखने वाली carrier (image/audio/document) जो secret data छिपाती है, cover file कहलाती है।*

**★ Nukta (Key Point):** Cover file = the disguise. Secret message = hidden data. Stego-object = cover + secret after embedding.

*Cover file = छद्म वेश। Secret message = छिपा data। Stego-object = embedding के बाद cover + secret।*

*[Source: Subject Test Solution-1 Part-2 (CN & Security) slides] · Medium*

---
### Q32. Which of the following is an example of asymmetric encryption?

<span lang='hi'>निम्न में से कौन-सा asymmetric encryption का उदाहरण है?</span>

- **(A)** AES
- **(B)** DES
- **(C)** RSA ✅ **(CORRECT)**
- **(D)** Blowfish

**✔ Correct Answer: (C) RSA** — RSA is the classic public-key (asymmetric) algorithm; AES, DES and Blowfish are all symmetric.

*RSA classic public-key (asymmetric) algorithm है; AES, DES और Blowfish सब symmetric हैं।*

**★ Nukta (Key Point):** Asymmetric = RSA, ECC, Diffie-Hellman, DSA. Symmetric = DES, 3DES, AES, Blowfish, RC4, IDEA.

*Asymmetric = RSA, ECC, Diffie-Hellman, DSA। Symmetric = DES, 3DES, AES, Blowfish, RC4, IDEA।*

*[Source: SSC CGL Tier-2 repeated Qs (via Oliveboard) · also BCI_SCI ST-01] · Medium*

---
### Q33. The data to be encrypted at the sender's site is called ______ and the data to be decrypted at the receiver's end is called ______.

<span lang='hi'>Sender की ओर encrypt किए जाने वाले data को ______ और receiver की ओर decrypt किए जाने वाले data को ______ कहते हैं.</span>

- **(A)** Secret key, public key
- **(B)** Public key, secret key
- **(C)** Plain text, cipher text ✅ **(CORRECT)**
- **(D)** Cipher text, plain text

**✔ Correct Answer: (C) Plain text, cipher text** — मूल data = Plain text; encrypt होने के बाद = Cipher text. Receiver पर cipher text decrypt होकर फिर plain text बनता है.

*मूल data = Plain text; encrypt होने के बाद = Cipher text. Receiver पर cipher text decrypt होकर फिर plain text बनता है.*

**★ Nukta (Key Point):** याद रखो: Plain (सादा) → encrypt → Cipher (गूँथा) → decrypt → Plain.

*याद रखो: Plain (सादा) → encrypt → Cipher (गूँथा) → decrypt → Plain.*

*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Medium*

---
### Q34. Public key is used to:

<span lang='hi'>Public key का उपयोग किसके लिए होता है?</span>

- **(A)** Encrypt the data ✅ **(CORRECT)**
- **(B)** Decrypt the data
- **(C)** Both encrypt and decrypt
- **(D)** Generate session keys only

**✔ Correct Answer: (A) Encrypt the data** — In public-key cryptography anyone can use the recipient's PUBLIC key to encrypt; only the recipient's PRIVATE key can decrypt.

*Public-key cryptography में कोई भी प्राप्तकर्ता की PUBLIC key से encrypt कर सकता है; केवल प्राप्तकर्ता की PRIVATE key से decrypt होता है।*

**★ Nukta (Key Point):** Encrypt with public → decrypt with private. SIGN with private → verify with public. Exam asks both directions!

*Encrypt public से → decrypt private से। SIGN private से → verify public से। Exam दोनों दिशाएँ पूछता है!*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

---
### Q35. Which statement about symmetric and asymmetric cryptography is TRUE?

<span lang='hi'>Symmetric और asymmetric cryptography के बारे में कौन-सा कथन सही है?</span>

- **(A)** Symmetric cryptography provides authentication
- **(B)** Asymmetric cryptography is faster than symmetric
- **(C)** Symmetric cryptography requires secure key exchange ✅ **(CORRECT)**
- **(D)** Both use two different keys

**✔ Correct Answer: (C) Symmetric cryptography requires secure key exchange** — Symmetric cryptography requires a SECURE key exchange between the parties — that is its defining practical challenge.

*Symmetric cryptography के लिए पक्षों के बीच सुरक्षित key exchange आवश्यक है — यही इसकी मुख्य व्यावहारिक चुनौती है।*

**★ Nukta (Key Point):** True: symmetric needs secure key exchange. False: symmetric does not inherently authenticate; asymmetric is slower; symmetric uses ONE key.

*सही: symmetric को secure key exchange चाहिए। गलत: symmetric स्वयं authentication नहीं देता; asymmetric धीमा; symmetric एक key उपयोग करता है।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security) — Q33] · Hard*

---
### Q36. What is the key length of AES-256 encryption?

<span lang='hi'>AES-256 encryption की key length कितनी है?</span>

- **(A)** 128 bits
- **(B)** 192 bits
- **(C)** 256 bits ✅ **(CORRECT)**
- **(D)** 512 bits

**✔ Correct Answer: (C) 256 bits** — AES-256 uses a 256-bit key (the number in the name is the key length).

*AES-256 में 256-bit key उपयोग होती है (नाम में संख्या key length है)।*

**★ Nukta (Key Point):** AES variants: AES-128, AES-192, AES-256 (key sizes). Block size is always 128 bits.

*AES variants: AES-128, AES-192, AES-256 (key sizes)। Block size हमेशा 128 bits।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

---
### Q37. Which of the following statements is FALSE?

<span lang='hi'>निम्न में से कौन-सा कथन गलत है?</span>

- **(A)** AES is a block cipher
- **(B)** RSA is a symmetric cipher ✅ **(CORRECT)**
- **(C)** Diffie-Hellman is used for key exchange
- **(D)** DES is symmetric

**✔ Correct Answer: (B) RSA is a symmetric cipher** — RSA is an ASYMMETRIC (public-key) cipher — the statement 'RSA is symmetric' is false.

*RSA एक ASYMMETRIC (public-key) cipher है — 'RSA symmetric है' कथन गलत है।*

**★ Nukta (Key Point):** False-statement MCQs: check each. AES=block ✓, RSA=asymmetric ✗, DH=key exchange ✓, DES=symmetric ✓.

*False-statement MCQs: हर एक जाँचें। AES=block ✓, RSA=asymmetric ✗, DH=key exchange ✓, DES=symmetric ✓।*

*[Source: Repo: BCI_SCI Subject Test-01 (CN and Security)] · Hard*

---
### Q38. Suppose everyone in a group of N people wants to communicate secretly with the N−1 others using a symmetric-key cryptographic system. The number of keys required in the system as a whole is:

<span lang='hi'>मान लीजिए N लोगों के समूह में हर व्यक्ति बाकी N−1 लोगों से symmetric-key cryptographic system से गुप्त बातचीत करना चाहता है. कुल कितने keys चाहिए होंगी?</span>

- **(A)** 2N
- **(B)** N(N − 1)
- **(C)** N(N − 1)/2 ✅ **(CORRECT)**
- **(D)** (N − 1)²

**✔ Correct Answer: (C) N(N − 1)/2** — Symmetric keys जोड़ों में बँटती हैं — हर जोड़े की एक key. N लोगों के जोड़े = N(N−1)/2.

*Symmetric keys जोड़ों में बँटती हैं — हर जोड़े की एक key. N लोगों के जोड़े = N(N−1)/2.*

**★ Nukta (Key Point):** GATE key (c). Public-key में यह समस्या नहीं — इसीलिए hybrid systems आए.

*GATE key (c). Public-key में यह समस्या नहीं — इसीलिए hybrid systems आए.*

*[Source: GATE CS PYQ (via examprev)] · Hard*

---

## Section C — Firewalls, IPSec & Security Protocols

*DMZ design, IPSec modes (transport/tunnel), SSL/TLS & HTTPS, security-protocol and mechanism layer mapping.*

### Q39. IPSec is MOST commonly used to implement:

<span lang='hi'>IPSec मुख्यतः किसके लिए उपयोग होता है?</span>

- **(A)** Secure email
- **(B)** Secure web browsing
- **(C)** Virtual Private Network (VPN) ✅ **(CORRECT)**
- **(D)** Wireless security

**✔ Correct Answer: (C) Virtual Private Network (VPN)** — IPSec provides encrypted tunnels over the internet — the foundation of most site-to-site and remote-access VPNs.

*IPSec internet पर encrypted tunnels देता है — अधिकांश site-to-site और remote-access VPNs की नींव।*

**★ Nukta (Key Point):** IPSec = VPN tunneling (ESP/AH). Secure email = PGP/SMIME. Secure web = SSL/TLS. Wireless = WPA2.

*IPSec = VPN tunneling (ESP/AH)। Secure email = PGP/SMIME। Secure web = SSL/TLS। Wireless = WPA2।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q40. In IPSec Tunnel mode:

<span lang='hi'>IPSec Tunnel mode में:</span>

- **(A)** Only the payload is encrypted
- **(B)** Only the header is encrypted
- **(C)** The entire IP packet is encrypted ✅ **(CORRECT)**
- **(D)** No encryption is used

**✔ Correct Answer: (C) The entire IP packet is encrypted** — Tunnel mode encrypts the ENTIRE original IP packet (header + payload) and adds a new header — used for VPN gateways.

*Tunnel mode पूरे original IP packet (header + payload) को encrypt करके नया header जोड़ता है — VPN gateways के लिए उपयोग।*

**★ Nukta (Key Point):** Tunnel = whole packet + new header (gateway VPN). Transport = payload only (host-to-host).

*Tunnel = पूरा packet + नया header (gateway VPN)। Transport = केवल payload (host-to-host)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q41. The SSL/TLS handshake protocol is mainly used for:

<span lang='hi'>SSL/TLS handshake protocol मुख्यतः किसके लिए उपयोग होता है?</span>

- **(A)** Data encryption
- **(B)** Data compression
- **(C)** Key exchange and authentication ✅ **(CORRECT)**
- **(D)** Packet routing

**✔ Correct Answer: (C) Key exchange and authentication** — The handshake negotiates cipher suites, authenticates the server (certificates) and exchanges keys for the session.

*Handshake cipher suites का निर्णय करता है, server को authenticate करता है (certificates) और session के लिए keys का आदान-प्रदान करता है।*

**★ Nukta (Key Point):** TLS parts: Handshake = keys+authentication; Record = encryption+integrity. HTTPS = HTTP over TLS (port 443).

*TLS parts: Handshake = keys+authentication; Record = encryption+integrity। HTTPS = HTTP over TLS (port 443)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Easy*

---
### Q42. Match the security mechanisms with their OSI layers: (a) Firewall  (b) Digital Signature  (c) MAC Filtering  (d) Port-based Filtering — (i) Network Layer  (ii) Application Layer  (iii) Data Link Layer  (iv) Transport Layer

<span lang='hi'>Security mechanisms को OSI layers से मिलाइए: (a) Firewall  (b) Digital Signature  (c) MAC Filtering  (d) Port-based Filtering — (i) Network Layer  (ii) Application Layer  (iii) Data Link Layer  (iv) Transport Layer</span>

- **(A)** a–i, b–ii, c–iii, d–iv ✅ **(CORRECT)**
- **(B)** a–ii, b–i, c–iii, d–iv
- **(C)** a–iv, b–ii, c–i, d–iii
- **(D)** a–i, b–iii, c–ii, d–iv

**✔ Correct Answer: (A) a–i, b–ii, c–iii, d–iv** — Firewall rules work at the network layer (IP), digital signatures are application-level, MAC filtering is data-link, and port filtering is transport-level (TCP/UDP ports).

*Firewall rules network layer (IP) पर, digital signatures application level पर, MAC filtering data-link पर, और port filtering transport level (TCP/UDP ports) पर काम करते हैं।*

**★ Nukta (Key Point):** Mechanism-layers: Firewall L3/L4 (IP), Port filter L4, MAC filter L2, Digital signature L7. Packet-filtering firewall = L3/L4.

*Mechanism-layers: Firewall L3/L4 (IP), Port filter L4, MAC filter L2, Digital signature L7। Packet-filtering firewall = L3/L4।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q4 match (codes recovered)] · Medium*

---
### Q43. Match the security protocols with their OSI layers: (a) IPSec  (b) SSL/TLS  (c) PGP  (d) WPA2 — (i) Application Layer  (ii) Network Layer  (iii) Transport/Presentation Layer  (iv) Data Link Layer (Wi-Fi)

<span lang='hi'>Security protocols को OSI layers से मिलाइए: (a) IPSec  (b) SSL/TLS  (c) PGP  (d) WPA2 — (i) Application Layer  (ii) Network Layer  (iii) Transport/Presentation Layer  (iv) Data Link Layer (Wi-Fi)</span>

- **(A)** a–ii, b–iii, c–i, d–iv ✅ **(CORRECT)**
- **(B)** a–ii, b–i, c–iii, d–iv
- **(C)** a–iii, b–ii, c–i, d–iv
- **(D)** a–i, b–ii, c–iii, d–iv

**✔ Correct Answer: (A) a–ii, b–iii, c–i, d–iv** — IPSec secures at the network layer (L3), SSL/TLS at transport/presentation, PGP is an application-layer mail security tool, and WPA2 protects Wi-Fi at the data-link layer.

*IPSec network layer (L3) पर, SSL/TLS transport/presentation पर, PGP application-layer mail security tool है, और WPA2 Wi-Fi को data-link layer पर सुरक्षित करता है।*

**★ Nukta (Key Point):** Protocol layers: IPSec L3, SSL/TLS L4-7 (exam: transport/presentation), PGP L7, WPA2 L2, Kerberos L7.

*Protocol layers: IPSec L3, SSL/TLS L4-7 (exam: transport/presentation), PGP L7, WPA2 L2, Kerberos L7।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch) — Q1 match (codes recovered)] · Medium*

---
### Q44. IPSec operates in which mode(s)?

<span lang='hi'>IPSec किस/किन mode(s) में काम करता है?</span>

- **(A)** Transport mode only
- **(B)** Tunnel mode only
- **(C)** Both transport mode and tunnel mode ✅ **(CORRECT)**
- **(D)** Application mode

**✔ Correct Answer: (C) Both transport mode and tunnel mode** — IPSec has two modes — transport mode (protects the payload, end-to-end) and tunnel mode (protects the whole IP packet, gateway-to-gateway).

*IPSec के दो modes हैं — transport mode (payload सुरक्षित, end-to-end) और tunnel mode (पूरा IP packet सुरक्षित, gateway-to-gateway)।*

**★ Nukta (Key Point):** IPSec modes: Transport (payload only, host-to-host) & Tunnel (full packet, gateway-to-gateway/VPN).

*IPSec modes: Transport (केवल payload, host-to-host) और Tunnel (पूरा packet, gateway-to-gateway/VPN)।*

*[Source: Repo: BCI Subject Test-9 (BCI/SCI Batch)] · Medium*

---
### Q45. Which mode of IPSec provides end-to-end security between two hosts?

<span lang='hi'>IPSec का कौन-सा mode दो hosts के बीच end-to-end security देता है?</span>

- **(A)** Transport mode ✅ **(CORRECT)**
- **(B)** Tunnel mode
- **(C)** Static mode
- **(D)** Gateway mode

**✔ Correct Answer: (A) Transport mode** — Transport mode secures communication directly between two hosts (end-to-end) — only the payload is protected.

*Transport mode दो hosts के बीच सीधे संचार सुरक्षित करता है (end-to-end) — केवल payload सुरक्षित होता है।*

**★ Nukta (Key Point):** End-to-end (host↔host) = Transport mode. Gateway↔gateway (VPN) = Tunnel mode.

*End-to-end (host↔host) = Transport mode। Gateway↔gateway (VPN) = Tunnel mode।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

---
### Q46. Which of the following is used in HTTPS for encryption?

<span lang='hi'>HTTPS में encryption के लिए निम्न में से क्या उपयोग होता है?</span>

- **(A)** SSL/TLS ✅ **(CORRECT)**
- **(B)** FTP
- **(C)** ARP
- **(D)** NAT

**✔ Correct Answer: (A) SSL/TLS** — HTTPS = HTTP over SSL/TLS — the TLS layer encrypts the HTTP traffic (port 443).

*HTTPS = HTTP over SSL/TLS — TLS layer HTTP traffic को encrypt करता है (port 443)।*

**★ Nukta (Key Point):** HTTPS = HTTP + SSL/TLS (443). HTTP = 80 (no encryption). FTP = 21. ARP = IP→MAC. NAT = address translation.

*HTTPS = HTTP + SSL/TLS (443)। HTTP = 80 (encryption नहीं)। FTP = 21। ARP = IP→MAC। NAT = address translation।*

*[Source: Repo: CN Topic Test 5 (UNIT TEST-5)] · Medium*

---
### Q47. In which layer of the network architecture is the Secure Socket Layer (SSL) used?

<span lang='hi'>Secure Socket Layer (SSL) network architecture की किस layer में उपयोग होती है?</span>

- **(A)** Physical layer
- **(B)** Session layer ✅ **(CORRECT)**
- **(C)** Application layer
- **(D)** Presentation layer

**✔ Correct Answer: (B) Session layer** — Exam banks place SSL at the Session layer — it establishes a secure session between application and transport (technically it sits between L4 and L7).

*Exam banks SSL को Session layer पर रखते हैं — यह application और transport के बीच secure session बनाती है (तकनीकी रूप से यह L4 और L7 के बीच है)।*

**★ Nukta (Key Point):** Exam convention: SSL = Session layer (secure session setup + negotiation). Note: TLS = successor of SSL.

*Exam convention: SSL = Session layer (secure session setup + negotiation)। नोट: TLS, SSL का उत्तराधिकारी है।*

*[Source: Unit Test-4 Solution (OCR), p6 (bank key)] · Medium*

---
### Q48. When a logic bomb is activated by a time-related event, it is known as a:

<span lang='hi'>जब कोई logic bomb किसी समय-संबंधी घटना से सक्रिय होता है, तो उसे कहते हैं:</span>

- **(A)** Time-related bomb sequence
- **(B)** Virus
- **(C)** Time bomb ✅ **(CORRECT)**
- **(D)** Trojan horse

**✔ Correct Answer: (C) Time bomb** — समय/तारीख़ से चलने वाला logic bomb = Time bomb (जैसे शुक्रवार-13 वायरस).

*समय/तारीख़ से चलने वाला logic bomb = Time bomb (जैसे शुक्रवार-13 वायरस).*

**★ Nukta (Key Point):** Logic bomb = शर्त से फटने वाला कोड; शर्त समय हो तो Time bomb.

*Logic bomb = शर्त से फटने वाला कोड; शर्त समय हो तो Time bomb.*

*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Medium*

---
### Q49. Verification based on a login ID and password is called:

<span lang='hi'>Login ID और password के आधार पर जाँच कहलाती है:</span>

- **(A)** Logging in
- **(B)** Configuration
- **(C)** Authentication ✅ **(CORRECT)**
- **(D)** Confidentiality

**✔ Correct Answer: (C) Authentication** — पहचान (ID+password) की जाँच = Authentication. यही सुरक्षा का पहला दरवाज़ा है.

*पहचान (ID+password) की जाँच = Authentication. यही सुरक्षा का पहला दरवाज़ा है.*

**★ Nukta (Key Point):** Authentication = 'तुम कौन हो?'; Authorization = 'तुम्हें क्या अनुमति है?'.

*Authentication = 'तुम कौन हो?'; Authorization = 'तुम्हें क्या अनुमति है?'.*

*[Source: RBI/IBPS computer-awareness banks (via ixambee)] · Medium*

---
### Q50. Access control based on a person's fingerprints is an example of:

<span lang='hi'>किसी व्यक्ति की उंगलियों के निशान पर आधारित access control का उदाहरण है:</span>

- **(A)** Biometric identification ✅ **(CORRECT)**
- **(B)** Characteristic identification
- **(C)** Encryption
- **(D)** Logistics

**✔ Correct Answer: (A) Biometric identification** — उंगली-छाप, आँख की पुतली, चेहरा — ये सब biometric identification हैं.

*उंगली-छाप, आँख की पुतली, चेहरा — ये सब biometric identification हैं.*

**★ Nukta (Key Point):** ज्ञात (password) से बढ़कर है शारीरिक पहचान (biometric).

*ज्ञात (password) से बढ़कर है शारीरिक पहचान (biometric).*

*[Source: SBI PO Computer Awareness PYQ (via bankersadda)] · Medium*

---
### Q51. Which of the following networks extends a private network across public networks?

<span lang='hi'>निम्न में से कौन-सा network public networks के ऊपर private network का विस्तार करता है?</span>

- **(A)** Virtual private network (VPN) ✅ **(CORRECT)**
- **(B)** Local area network
- **(C)** Enterprise private network
- **(D)** None of these

**✔ Correct Answer: (A) Virtual private network (VPN)** — VPN (Virtual Private Network) tunneling और encryption से public Internet पर एक सुरक्षित private रास्ता बनाता है.

*VPN (Virtual Private Network) tunneling और encryption से public Internet पर एक सुरक्षित private रास्ता बनाता है.*

**★ Nukta (Key Point):** BPSC 2024 official key (a). VPN = सार्वजनिक सड़क पर निजी लिमोज़ीन.

*BPSC 2024 official key (a). VPN = सार्वजनिक सड़क पर निजी लिमोज़ीन.*

*[Source: BPSC TRE 2024 (via KnowledgeGate solved PYQ bank)] · Medium*

---
### Q52. Which one of the following is a key function of a firewall?

<span lang='hi'>निम्न में से firewall का एक मुख्य काम कौन-सा है?</span>

- **(A)** Monitoring ✅ **(CORRECT)**
- **(B)** Copying
- **(C)** Deleting
- **(D)** Moving

**✔ Correct Answer: (A) Monitoring** — Firewall आने-जाने वाले traffic की monitoring करता है और अनधिकृत पहुँच को रोकता है.

*Firewall आने-जाने वाले traffic की monitoring करता है और अनधिकृत पहुँच को रोकता है.*

**★ Nukta (Key Point):** Firewall = network का चौकीदार — देखता है, जाँचता है, रोकता है.

*Firewall = network का चौकीदार — देखता है, जाँचता है, रोकता है.*

*[Source: RRB NTPC previous-year computer banks (via adda247 50-PYQ PDF)] · Medium*

---
### Q53. What is the advantage of setting up a DMZ (Demilitarized Zone) using a firewall?

<span lang='hi'>Firewall का उपयोग करके DMZ (Demilitarized Zone) बनाने का क्या लाभ है?</span>

- **(A)** To create multiple zones of trust ✅ **(CORRECT)**
- **(B)** Load balancing on the server
- **(C)** Improving network performance
- **(D)** Bringing internet service into a home

**✔ Correct Answer: (A) To create multiple zones of trust** — A DMZ creates separate trust zones — public servers (web/mail) sit in the DMZ so attackers don't directly reach the internal trusted network.

*DMZ अलग trust zones बनाता है — public servers (web/mail) DMZ में रहते हैं ताकि attackers सीधे internal trusted network तक न पहुँचें।*

**★ Nukta (Key Point):** Official RPSC key. DMZ = buffer zone between untrusted Internet and trusted LAN (3 zones: external / DMZ / internal).

*Official RPSC key। DMZ = untrusted Internet और trusted LAN के बीच buffer zone (3 zones: external / DMZ / internal)।*

*[Source: RPSC Programmer 2024 Paper-1 (official key)] · Hard*

---

## ★ Nukte Rapid-Fire — Exam Pointers

- **CIA triad?** *(CIA triad?)* → **Confidentiality, Integrity, Availability.** *(Confidentiality, Integrity, Availability।)*
- **Goal of each: interception / modification / DoS / spoofing?** *(हर एक का लक्ष्य: interception / modification / DoS / spoofing?)* → **Confidentiality / Integrity / Availability / Authentication.** *(Confidentiality / Integrity / Availability / Authentication।)*
- **Active vs passive attack?** *(Active बनाम passive attack?)* → **Active = changes/disrupts data. Passive = only observes (eavesdrop, traffic analysis).** *(Active = data बदलता/बाधित करता है। Passive = केवल देखता है (eavesdrop, traffic analysis)।)*
- **Virus phases?** *(Virus phases?)* → **Dormant → Propagation → Triggering → Execution (payload runs).** *(Dormant → Propagation → Triggering → Execution (payload चलता है)।)*
- **WORM medium?** *(WORM medium?)* → **Optical disk (CD-R/DVD-R) — write once, read many.** *(Optical disk (CD-R/DVD-R) — एक बार लिखें, कई बार पढ़ें।)*
- **Symmetric vs asymmetric keys?** *(Symmetric बनाम asymmetric keys?)* → **1 shared key (fast, key-distribution problem) vs key pair public+private (slow).** *(1 shared key (तेज़, key-distribution समस्या) बनाम key pair public+private (धीमा)।)*
- **Encrypt/decrypt vs sign/verify direction?** *(Encrypt/decrypt बनाम sign/verify दिशा?)* → **Encrypt public → decrypt private. Sign private → verify public.** *(Encrypt public → decrypt private। Sign private → verify public।)*
- **DES / AES / RSA basics?** *(DES / AES / RSA basics?)* → **DES = 64-bit block/56-bit key. AES = 128-bit block (128/192/256 keys). RSA = asymmetric.** *(DES = 64-bit block/56-bit key। AES = 128-bit block (128/192/256 keys)। RSA = asymmetric।)*
- **Stream vs block cipher?** *(Stream बनाम block cipher?)* → **Stream = 1 bit/byte at a time (RC4). Block = fixed blocks (DES/AES).** *(Stream = 1 bit/byte at a time (RC4)। Block = fixed blocks (DES/AES)।)*
- **Caesar cipher type?** *(Caesar cipher प्रकार?)* → **Classical substitution (replace letters by shifting).** *(Classical substitution (अक्षरों को खिसका कर बदलना)।)*
- **Steganography terms?** *(Steganography terms?)* → **Cover file (carrier) + secret message → stego-object. Detection = steganalysis.** *(Cover file (carrier) + secret message → stego-object। पहचान = steganalysis।)*
- **False-friend: RSA is symmetric?** *(False-friend: RSA symmetric है?)* → **NO — RSA is ASYMMETRIC. AES/DES/Blowfish are symmetric.** *(नहीं — RSA ASYMMETRIC है। AES/DES/Blowfish symmetric हैं।)*
- **Security tools?** *(Security tools?)* → **Wireshark = sniff, Nmap = port scan, Cain&Abel = password crack, Angry IP = IP scan, Snort = IDS.** *(Wireshark = sniff, Nmap = port scan, Cain&Abel = password crack, Angry IP = IP scan, Snort = IDS।)*
- **Key reuse risk?** *(Key reuse जोखिम?)* → **Known-plaintext / frequency analysis attacks become possible.** *(Known-plaintext / frequency analysis attacks संभव हो जाते हैं।)*
- **DMZ?** *(DMZ?)* → **Buffer zone between internet & trusted LAN — public servers face outside, internals stay safe.** *(Internet और trusted LAN के बीच buffer zone — public servers बाहर, internals सुरक्षित।)*
- **IPSec modes?** *(IPSec modes?)* → **Transport = payload only (host-to-host end-to-end). Tunnel = whole packet (gateway VPN).** *(Transport = केवल payload (host-to-host end-to-end)। Tunnel = पूरा packet (gateway VPN)।)*
- **IPSec / SSL / PGP / WPA2 layers?** *(IPSec / SSL / PGP / WPA2 layers?)* → **Network / Transport-Presentation / Application / Data Link (Wi-Fi).** *(Network / Transport-Presentation / Application / Data Link (Wi-Fi)।)*
- **Firewall / port filter / MAC filter / signature layers?** *(Firewall / port filter / MAC filter / signature layers?)* → **Network / Transport / Data Link / Application.** *(Network / Transport / Data Link / Application।)*
- **SSL/TLS handshake does?** *(SSL/TLS handshake करता है?)* → **Key exchange + server authentication (certificates). Record protocol does encryption.** *(Key exchange + server authentication (certificates)। Encryption Record protocol करता है।)*
- **HTTPS = ?** *(HTTPS = ?)* → **HTTP + SSL/TLS on port 443.** *(HTTP + SSL/TLS port 443 पर।)*
- **DoS vs DDoS?** *(DoS बनाम DDoS?)* → **Single-source flooding vs distributed (many zombies/botnet) flooding.** *(Single-source flooding बनाम distributed (कई zombies/botnet) flooding।)*
- **Attack examples map?** *(Attack examples map?)* → **Phishing=steal credentials; MitM=intercept; Spoofing=impersonate; Smurf=DoS variant.** *(Phishing=credentials चुराना; MitM=intercept; Spoofing=impersonate; Smurf=DoS variant।)*

