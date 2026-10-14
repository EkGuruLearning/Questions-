# Unresolved geographic and administrative discrepancies

**Deliverable 17** · **Date:** 2026-10-14 · **Status: 7 OPEN items, none hidden**

Every item below is a real, measured conflict. None has been smoothed over by
quietly picking one side. The map shows the GIS-verified truth; where that
contradicts common study material, the contradiction is printed on the sheet
itself.

---

## D-1 — The Pakistani "nine districts" list is wrong in its composition

| | Districts |
|---|---|
| **Commonly published list** | Bahawalnagar, Bahawalpur, Rahim Yar Khan, **Dera Ghazi Khan**, **Muzaffargarh**, **Rajanpur**, Sanghar, Umerkot, Tharparkar |
| **GIS-derived list** | Bahawalnagar, Bahawalpur, Rahim Yar Khan, **Ghotki**, **Khairpur**, **Sukkur**, Sanghar, Umerkot, Tharparkar |

**Finding.** Dera Ghazi Khan, Muzaffargarh and Rajanpur lie west of Bahawalpur
district and the Sutlej–Indus belt; they do **not** share a single metre of
boundary with Rajasthan. Ghotki, Khairpur and Sukkur (all Sindh) do.

**Evidence.** Three independent methods agree: bidirectional boundary length at
1 000 m tolerance; one-directional length at 250 m tolerance; symmetric
buffered-overlap area at 600 m. All three produce the same nine districts.

**Action taken on the sheet.** Dera Ghazi Khan, Muzaffargarh and Rajanpur are
drawn, labelled and hatched in red, with a footnote on the sheet stating that
they are named in study material but do not touch Rajasthan.

**Why unresolved.** This cannot be "resolved" — it is not a data error, it is a
geometric fact. It is listed here because it contradicts the brief's checklist,
and the brief explicitly asked for the discrepancy to be explained rather than
silently corrected.

---

## D-2 — Published border **lengths** are not reproducible from GIS data

| Neighbour | GIS-measured | Commonly published | Delta |
|---|---|---|---|
| Pakistan | 1,036 km | 1,070 km | −3 % |
| Punjab | 90 km | 89 km | +1 % |
| Haryana | 1,039 km | 1,262 km | −18 % |
| Uttar Pradesh | 462 km | 877 km | −47 % |
| Madhya Pradesh | 2,110 km | 1,600 km | +32 % |
| Gujarat | 723 km | 1,022 km | −29 % |
| **Total outline** | **5,518 km** | **5,920 km** | −7 % |

**Finding.** Two fully independent datasets agree with each other and disagree
with the published figures:

| Dataset | Rajasthan area | Rajasthan outline |
|---|---|---|
| Survey-of-India-derived (used here) | 341,870 km² | 5,518 km |
| Census 2011 / DataMeet (independent) | 341,826 km² | 5,487 km |
| Official figure | 342,239 km² | — |

Areas agree to within 0.1 %; outlines to within 0.6 %. The published 5,920 km
total does not match either.

**Action taken.** The sheet reports GIS lengths. `BORDER_LENGTH_CROSSCHECK.csv`
carries both columns side by side so you can see the gap rather than inherit a
number you cannot defend.

**Why unresolved.** Reconciling this needs the original measurement
specification behind the published figures (which map scale, which vintage,
whether river centrelines were followed). Not available in this environment.

**Important for exams:** the **district counts** in the same published sources
are correct — Punjab 2, Haryana 7, Uttar Pradesh 2, Madhya Pradesh 10, Gujarat 6,
Pakistan 9. Only the lengths diverge.

---

## D-3 — Cross-source seam between the Indian and Pakistani layers

The two layers are independent, so their lines do not coincide. Measured by
sampling the Pakistan-facing Rajasthan boundary every 1 km (1,109 samples):

| Offset | Share of the seam |
|---|---|
| < 100 m | 55.3 % |
| < 250 m | 70.2 % |
| < 500 m | 86.2 % |
| < 1 000 m | 93.6 % |
| < 2 000 m | 93.9 % |

Median offset **50 m**; total cross-source overlap **113 km²** across 26 slivers
(largest 14.8 km²).

**Action taken.** Nothing. Snapping the Pakistani polygons to the Indian line
would mean altering one authoritative source to match another, which the brief
forbids. The 1 000 m adjacency tolerance is the 94th percentile of the measured
seam error — derived from the data, not chosen as a round number.

**Why unresolved.** It is irreducible conflation error between two datasets.
Resolving it requires a single authoritative bilateral boundary dataset, which
is unavailable here.

---

## D-4 — 22 disputed Rajasthan–Gujarat slivers

The Indian source layer contains 22 features explicitly marked
`DISPUTED (RAJASTHAN & GUJARAT)`, totalling **28 km²** with **55 km** of contact
with Rajasthan.

**Action taken.** Excluded from the sheet **and** from `BOUNDARY_RELATIONS.csv`
— they are contested pockets, not districts. Listed in
`data/metadata/DISPUTED_SLIVERS.csv` so nothing is silently dropped.

**Why unresolved.** Their ownership is genuinely contested. Assigning them to
either state without the underlying gazette description would be a fabrication.

---

## D-5 — Gazette notification not retrievable

The 41-district / 7-division count rests on the 28 December 2024 cabinet
decision, corroborated by **six** independent contemporaneous reports
(Hindustan Times, India TV, IANS, Rajasthan Patrika, TV9 Bharatvarsh, plus a
September 2026 Hindi reference page confirming nothing has changed since).

The underlying gazette notification could not be fetched: outbound network
access in this environment is limited to `github.com`, `codeload.github.com`,
`api.github.com`, `registry.npmjs.org`, `pypi.org` and
`files.pythonhosted.org`. `revenue.rajasthan.gov.in`, Bhuvan and the LGD portal
are all outside that list.

**Why unresolved.** Network restriction. **This is the weakest evidentiary link
in the project** and is disclosed on the sheet.

---

## D-6 — Pakistan administrative snapshot is dated 2022-09-09

The Pakistani districts come from WFP / OCHA COD-AB **v01**, valid
**2022-09-09**. Any Pakistani district created or reorganised after that date
is absent.

**Mitigation.** The nine districts that matter here are long-established and
none of them is known to have changed since 2022, but I am not asserting that
as verified.

**Why unresolved.** A newer COD-AB release would be needed; GitHub release
assets and Git-LFS payloads are both blocked here.

---

## D-7 — No human has looked at the printed sheet

I cannot display images in this environment. Every "visual" property was
measured numerically: label placement, glyph coverage, page boxes, colour
presence, ink density in each furniture panel.

**What was verified numerically:** all 41 Rajasthan labels placed; all 36
border-sharing neighbours placed; 237/237 label anchors inside their own
polygon; 0 duplicate labels; 0 missing glyphs across 6,155 font codepoints;
A1/A2/A3 page boxes exact to < 1 mm; red and yellow border pixels present on
all three sheets.

**What was NOT verified:** aesthetic judgement — whether the composition looks
right, whether any leader line reads confusingly, whether two nearby labels of
the same size feel crowded.

**Action required from you.** Open `exports/Rajasthan_Border_District_Atlas_A1.pdf`
at 100 % zoom before printing. Two labels (0.8 %) were displaced by the
collision engine and carry leader lines; check those first.

---

## Summary

| ID | Issue | Blocks delivery? |
|---|---|---|
| D-1 | Pakistani nine-district list has the wrong composition | No — geometry shown, contradiction footnoted |
| D-2 | Published border lengths unreproducible | No — GIS lengths shown, both tabulated |
| D-3 | Cross-source seam, 50 m median | No — disclosed, not snapped |
| D-4 | 22 disputed slivers | No — excluded and listed |
| D-5 | Gazette not retrievable | No — six corroborating reports instead |
| D-6 | Pakistan snapshot 2022-09-09 | No — disclosed |
| D-7 | No human visual check | **Yes, for printing** — you must open the A1 PDF |
