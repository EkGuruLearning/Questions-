# RPSC Programmer — Data Communication & Computer Networks (source extract)

**Source:** *RPSC PROGRAMMER (Paper-I & II) Solved Papers & Practice Book*, YCT
Publications (Chief Editor A.K. Mahajan). Fetched from
`https://www.yctfastbook.com/upload/1726202413_RPSC%20Pragrammer%20.pdf`
(text extracted via web fetch; the site is not reachable from the build sandbox, so
this is a captured extract — fetch the full PDF on your machine for the complete set).

This is the **official RPSC Programmer syllabus** for the CN section, plus one solved
previous-year CN question captured from it. Use it as a trusted reference for RPSC
Programmer-level Data Communication & Computer Networks questions.

---

## RPSC Programmer — Syllabus, Paper-I, Section 3: Data Communication and Computer Networks

> Computer Network Architecture, Circuit Switching, Packet And Message Switching,
> Network Structure. Physical Layer, Data Link Layer, Framing. Retransmission algorithms.
> Multiple access and Aloha. CSMA/CD and Ethernet. High Speed LANs and topologies.
> Broadcast routing and spanning trees.
> TCP/IP Stack. IP Networks and Internet. DNS and Firewalls. Intrusion Detection and Prevention.
> Transport layer and TCP/IP. Network Management and Interoperability.

(This maps onto the 7-topic structure: T1 intro/switching, T2 models (TCP/IP stack),
T3 addressing (IP networks), T4 devices/firewalls, T5 medium, T6 OSI layers detail
(Physical, Data Link, framing, retransmission, multiple access/Aloha/CSMA/CD/Ethernet,
topologies, routing/spanning trees, transport layer/TCP), T7 security (DNS & firewalls,
intrusion detection & prevention).)

---

## Solved PYQ captured (RPSC Programmer)

**Q. Four bits are used for packet sequence numbering in a sliding window protocol
used in a computer network. What is the maximum window size?**
- (a) 4
- (b) 8
- (c) 15
- (d) 16

**✔ Correct Answer: (c) 15**

**Why:** With `m` bits for sequence numbers there are `2^m` distinct sequence numbers
(here `2^4 = 16`, i.e. 0–15). To keep the receiver unambiguous about which sequence
number a frame belongs to, a sliding-window (Go-Back-N) sender window can use at most
`2^m − 1` sequence numbers. So max window size = `2^4 − 1 = 15`.
(Selective Repeat is more restrictive: max window = `2^(m−1)` = 8; the question asks the
*maximum* window size, which is the Go-Back-N bound `2^m − 1`.)

**★ Nukta:** max sliding-window size = `2^m − 1` (m = seq bits). 4 bits → 15. (SR: `2^(m−1)`.)

**✖ Why the others are WRONG:**
- (a) 4 — that is just the number of bits, not the window size.
- (b) 8 — that is `2^(m−1)`, the **Selective Repeat** limit, not the maximum (GBN) limit.
- (d) 16 — that is `2^m` (all sequence numbers); using all of them makes old/new frames
  ambiguous, so the window can be at most `2^m − 1`.

*[Source: RPSC Programmer PYQ — YCT Solved Papers book (yctfastbook.com)]*
