# EkGuru Portal — Implementation Release Notes

**Bank build ID:** `cn-014b0aa51c0651e7`<br>
**Canonical SHA-256:** `014b0aa51c0651e77ee8166a9f81a4daeeb0574b75b7abf6e5d72050c46feef0`<br>
**Snapshot date:** 2026-10-14

## Current implementation snapshot

- Canonical CN bank: 1,556 records across 7 topics; 1,554 practice-payload records.
- 2 record(s) marked disputed/pending are omitted from practice chunks; source records remain in the canonical bank.
- Only the root data-driven portal is the current production candidate; other subjects remain unavailable until their review gates pass.
- Official paper + final-key match: 0 records in the current evidence register.
- Answer checked: 847; claimed answer unverified: 707; pending review: 2.
- All current exam profiles are practice or suggested-fit mappings, not exact simulations.

## User-facing changes in this branch

- Provenance-aware topic chunks, catalog, source register and generated counts.
- Accessible responsive navigation and same-tab internal routes.
- Source/verification filters, honest language fallbacks, local attempt recovery, deterministic scoring, question review and report-copy flow.
- Legacy source files, original PDFs and historical quiz snapshots are preserved.

## Deployment

This report is generated on a feature branch. It is not evidence of a merge, GitHub Pages deployment or live-site smoke test.
