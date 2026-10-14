# EkGuru Learning — Online Test Portal (by Prakash)

**🌐 Live:** https://ekgurulearning.github.io/Questions-/

Rajasthan Govt. exams ke liye free online test portal.
Jo subject verify ho gaya woh **LIVE** hai, jo ban raha hai us par saaf **Coming Soon** likha hai.

## Abhi kya live hai
| Subject | Status | Questions |
|---|---|---|
| Computer Network | ✅ LIVE | 1,556 bilingual MCQ · 7 topics · Practice + Exam mode |
| DBMS, Java, SAD, OS, DS, C, Computer Fundamentals, Geography | ⏳ Coming Soon | Cards par progress dikhta hai |

## Visitor kya kar sakta hai
- Topic-wise / full **Practice Test** (turant jawab + ★ Nukta) aur **Exam Test** (timer, palette, negative marking)
- EN / हिंदी / dono bhasha, difficulty filter, 10–100 question
- Result: score, topic-wise analysis, galat sawal dobara dene ka option, purana record (browser me hi)
- Har topic ki **Theory+MCQ PDF** aur **Practice Booklet PDF** download, purane 7 Full-CBT pages ke link

## File map (future changes ke liye)
```
index.html                     ← poori website (ek hi file, koi framework nahi)
assets/cn-questions.min.json   ← website wala halka question bank (auto-generated, haath se mat chhedo)
Computer Network/data/cn_questions.json  ← asal bank (source of truth)
tools/build_site_data.py       ← bank badle to ye chalao, website data taza ho jayega
SITE_GUIDE.md                  ← naya subject/topic jodne ki kitab
```
👉 Kuch bhi badalna ho to pehle **SITE_GUIDE.md** padh lo — 5 minute lagegi, galti nahi hogi.
