# data/catalog/ — editable catalogue inputs

Yahan likho, phir `python3 tools/build_catalog.py` chalao. `data/site.json` inhi inputs se banta hai.

| File | Kaam |
|---|---|
| `subjects.json` | Brand text, subjects, topic titles (English + Hindi), tagline/intro, `has_material` / `has_test` / `has_maps` |
| `materials.json` | Har downloadable file ka record: `file`, `subject`, `topic`, `kind`, `order`, `title_en`, `title_hi`, `note_en`, `note_hi`. `groups` se material page ke sections bante hain |
| `site-routes.txt` | Published pages ki list (link validator isi se check karta hai) |

`kind` allowed values: `theory`, `practice`, `test`, `reference`, `map`.

Builder ke rules (fail-fast):

1. `content/` ke andar ki **har** file register honi chahiye.
2. Registered **har** path exist karna chahiye aur `content/` ke andar hona chahiye.
3. `topic` sirf `T01`–`T07` ya `null`.
4. Har topic ka naam question-bank manifest se match karna chahiye.
5. Byte size aur SHA-256 asli file se aate hain — haath se nahi likhte.
