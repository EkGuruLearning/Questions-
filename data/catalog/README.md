# data/catalog/ — editable catalogue inputs

Yahan likho, phir `python3 tools/build_catalog.py` chalao. `data/site.json` inhi inputs se banta hai.

| File | Kaam |
|---|---|
| `subjects.json` | Brand, subject (EN/HI title, tagline, intro, `has_material`/`has_test`/`has_maps`), `folders` ke labels (icon, EN/HI naam + note, order), topic titles |
| `materials.json` | Har downloadable file ka record: `file`, `subject`, `topic` (ya `null`), `order`, `title_en`, `title_hi`, `note_en`, `note_hi` |
| `site-routes.txt` | Published pages ki list (link validator isi se check karta hai) |

Folder path hi website ka folder ban jata hai: `content/computer-network/answers/x.pdf` → folder
`answers` → "Answers & explanations" card. Isliye folder ka label `subjects.json` ke `folders` me
hona chahiye.

Builder ke rules (fail-fast):

1. `content/` ke andar ki **har** file register honi chahiye.
2. Registered **har** path exist karna chahiye, `content/<subject>/<folder>/` ke andar hona chahiye.
3. Jis folder me file hai, uska label `subjects.json` me hona chahiye — aur config me likha har
   label asli folder se match karna chahiye.
4. `topic` sirf `T01`–`T07` ya `null`.
5. Har topic ka naam question-bank manifest se match karna chahiye.
6. Byte size aur SHA-256 asli file se aate hain — haath se nahi likhte.
