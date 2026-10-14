# data/catalog/ — editable catalogue inputs

Yahan likho, phir `python3 tools/build_catalog.py` chalao. `data/site.json` inhi inputs se banta hai.

| File | Kaam |
|---|---|
| `subjects.json` | Brand, subject (EN/HI title, tagline, intro, `has_material`/`has_test`/`has_maps`), `folders` ke labels (icon, EN/HI naam + note, order), topic titles |
| `materials.json` | Har downloadable file ka record: `file`, `subject`, `topic` (ya `null`), `order`, `title_en`, `title_hi`, `note_en`, `note_hi`. Picture (map/PNG) ke liye **`alt_en`, `alt_hi`, `description_en`, `description_hi`** bhi — yahi SEO text page par aur image alt me jata hai |
| `site-routes.txt` | Published pages ki list (link validator isi se check karta hai) |

Folder path hi website ka folder ban jata hai: `content/computer-network/answers/x.pdf` → folder
`answers` → "Answers & explanations" card. Isliye folder ka label `subjects.json` ke `folders` me
hona chahiye.

Builder ke rules (fail-fast):

1. `materials.json` me likhi **har** file disk par honi chahiye (typo protection). Iske ilawa
   `content/` me jo bhi file hai wo bina registration ke bhi publish hoti hai — naam se title ban jata hai.
2. Registered **har** path exist karna chahiye, `content/<subject>/<folder>/` ke andar hona chahiye.
3. `subjects.json` me likha har folder disk par hona chahiye; baaki folders apne naam se label le lete hain
   (aur khali folder bhi site par dikhta hai — file daalte hi bhar jata hai).
4. `topic` sirf `T01`–`T07` ya `null`.
5. Har topic ka naam question-bank manifest se match karna chahiye.
6. Har picture ka `alt_en`/`alt_hi` (200 akshar tak) aur `description_en`/`description_hi` (120+ akshar)
   hona chahiye — alt text search engines padhte hain aur description page par dikhti hai.
7. Byte size aur SHA-256 asli file se aate hain — haath se nahi likhte.
