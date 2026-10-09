# -*- coding: utf-8 -*-
"""Topic 2 curated question bank — CURATION IN PROGRESS.

Format (same as topic1_data.py):
  q   = [en, hi]                  # question, bilingual
  opts= [[en,hi] x 4]             # options (A)-(D), bilingual
  ans = int 0..3                  # correct option index
  wr  = [en, hi]                  # why the correct answer is right
  nk  = [en, hi]                  # nukta / key exam point
  ww  = {wrong_idx: [en, hi]}     # why each wrong option is wrong
  src = source paper / book tag

SECTIONS = list of {title, note, questions}. Sub-topic order follows cn_taxonomy.

Auto-extracted candidate questions live in topic2_pending.py (Pending Review) and are
rendered at the end of the PDF. Verify + promote them here (add nukte/Hindi/ww), then
rebuild with: python tools/cn_build_topic.py 2
"""

SECTIONS = []
