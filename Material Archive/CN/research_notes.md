# CN Research Notes — PYQ harvest 2011–2026 (Oct 2026)

Har source jo research mein use hua, uska takeaway. Do waves:
wave-1 = 45 items (pyq_adds_wave1.py), wave-2 = 29 items (pyq_adds_wave2.py).
Total added: 74; books ab **631 MCQs** (7 topics).

## Sources used (wave 1 + 2)

| Source | Items taken | Takeaway |
|--------|------------|----------|
| cliffsnotes.com/study-notes/7035504 (pyqp.in dump) | RPSC Programmer 2011 P1: TCP ports, TTL-loop, Ping, bridge-vs-router, AAL, CSMA/CD 25B→None | Q85230/34/57/59/42/44/56 dropped (cut/garbled options) |
| surakuacademy.com RPSC Programmer 2024 solution | DNS PTR, /21→2046 hosts, ARP | official key used |
| gateforum.com CS-GATE-2012.pdf | Class C networks = 2²¹ (C) | official key + exp |
| byjus.com/gate/computer-network-gate-questions | GATE 2015 S2 stop-wait 12ms, 2016 S2 packet seq, 2016 S1 stateful, 2014 S3 fields, 2014 S1 LS/DV, 2014 S2 RIP/OSPF | verified keys |
| questions.examside.com (network-layer, tcp-udp pages) | GATE 2013 last-fragment 2400-2759, 2016 S1 13-fragments, 2019 /30, 2019 ARP, 2020 router stmts, 2024 S1/S2 NAT+CIDR+6-fragments, 2025 S2 next-hop, 2025 S1 flags | full year coverage 2012–2025 |
| samagracs.com (GATE TCP + UGC NET pages) | GATE 2018 seq-reuse=34s, slow-start (iv), 2021 S2 handshake X+1, 2022 33-bits, UGC NET 2025 1000-bits + Nyquist 10000bps, NET 2022 CRC | computed keys cross-checked |
| computersciencejunction.in | RPSC 2011 variants (dup of above), subnet-mask /22 | partial snippets |
| adda247.com (RRB-NTPC 50-PYQ PDF + EMRS) | RRB NTPC: firewall-monitoring, POP3-recv, SNMP-odd; EMRS: WWW definition | complete items only |
| examsmantra.in RSMSSB IA 2023 | VoIP, repeater, mesh, MAC-48 (merged) | Q126/134 dups — skipped |
| testbook.com QA pages | SSC CHSL 2023 DHCP (merged), IBPS ICMP, SSC MTS HTTP; EMRS PGT bank | 5-opt/uncertain dropped |
| knowledgegate.ai blog | HTET 2024 worm, BPSC 2024 VPN (5→4 adapted) | |
| bankersadda.com, meritnotes.com, ixambee.com, ibtindia.com PDF, tpointtech.com, practicemock.com, jagranjosh.com KVS 2018/2017 | time-bomb, plain/cipher, bridges, biometric, TCP/IP-suite, broadband, SLIP, ARPANET, authentication, spam, channel-capacity; KVS 2017: 153.6 Mbps, 1000/4000 baud | jagranjosh Q172/184 dropped (bad key/cut opts) |
| UGC NET Dec-2022/Jan-2025 (samagracs) | CRC 111111, CSMA 1000 bits, Nyquist 10000 bps | June-2022 passage Qs dropped (uncertain) |

## Dropped (documented — fabricate kabhi nahi)

- Missing/cut options (RPSC 2011 Q85230/34/42/44/56, jagranjosh Q184, GATE
  figure-dependent: routing-table match, token-bucket (controversial key), myTCP seq)
- Disputed keys: practicemock "permanent address=IP" (Forouzan MAC=permanent wins)
- 5-option papers: BPSC VPN adapted (documented in src)
- Duplicates (merged src into existing instead): MAC-48-bit, mesh n(n-1)/2,
  DHCP-dynamic, UDP-connectionless, HTTP-app, FTP-full, SMTP, ARP-analogy, RARP-full

## Verified computations (recheck-able)

- /21 mask → 2046 hosts | Class B 6-bit subnet → 62 subnets/1022 hosts
- GATE 2007 CRC x³+1 → 11001001011 | GATE 2015 CSMA 100 Mbps → 20000 km/s
- UGC NET 2025 CSMA 20Mbps/25µs → 1000 bits | Nyquist 5000Hz/2L → 10000 bps
- GATE 2022 satellite 2100km → 7.08 ms | KVS: 800×600×8×40 = 153.6 Mbps
- GATE 2015 S1 stop-wait 64kbps/20ms → 320 B | GATE 2015 S2 25% → 12 ms
- GATE 2013 frag: offset 300 → 2400–2759, last (M=0)
- GATE 2024: 1420B over MTU 542→360 → 6 fragments
- GATE 2018 seq reuse 1Gbps → 34 s | GATE 2022 MSL 60s → 33 bits
- GATE 2012: Class C = 2²¹ | GATE 2024 CIDR 10.12.2.0–3.255 → /23

## Blocked sites (snippets only)

testbook, jagranjosh, scribd, most edu sites — sandbox allowlist se bahar;
content snippets se liya; papers repo mein nahi aa paye to notes mein record hai.
