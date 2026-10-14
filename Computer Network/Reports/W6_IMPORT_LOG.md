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
