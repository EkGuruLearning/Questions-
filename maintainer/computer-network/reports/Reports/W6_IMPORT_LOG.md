# W6 bulk import log (new/ compiled banks)

- Raw pool (21 PDFs): 1008
- Parser-2 (2 PDFs): 178
- Clean (4 opts + key + non-trivial): 1185
- Dropped repeats: {'exact': 241, 'near90': 136, 'near-same-ans': 69}
- **Imported: 739**

## Agent verification verdicts

{'ok': 54, 'fix': 2, 'claim': 4, 'unseen': 679}

- `ok`/`fix` = agent-verified (caution removed; `fix` = source key corrected).
- `claim`/`unseen` = ⚠ CAUTION banner stays (answer NOT verified).

Zero-repeat policy: exact stem / >=0.90 overlap / >=0.75+same answer = dropped.

## Current canonical status (supersedes older rolling snapshot)

Bank build ID: `cn-014b0aa51c0651e7`; canonical SHA-256: `014b0aa51c0651e77ee8166a9f81a4daeeb0574b75b7abf6e5d72050c46feef0`; snapshot: 2026-10-14.

- Current `answer_checked`: 847
- Current `paper_and_key_checked`: 0
- Current `claimed_answer_unverified`: 707

- Current `disputed`: 0; current `pending_review`: 2

The W6 import count of 739 is a historical import event, not a current verification count. The older `ok`/`fix` agent verdicts are not official evidence. Earlier rolling totals that included 26 official-key matches were superseded after review of the community-maintained answer table.
