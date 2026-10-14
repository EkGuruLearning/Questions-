# SITE GUIDE — EkGuru Website kaise badlein (Prakash ke liye)

Website = sirf `index.html` (design + test engine) + `assets/cn-questions.min.json` (data).
GitHub Pages repo ke root se `index.html` serve karta hai. `.nojekyll` rakha hai taaki
file/folder naam (space wale bhi) waise hi serve hon jaise hain.

## 1) CN me naye question judenge tab (sabse aam kaam)
Purana pipeline hi chalega:
```bash
python tools/cn_pipeline.py ingest      # naya PDF -> Incoming/ se bank me
python tools/cn_pipeline.py rebuild --all
python3 tools/build_site_data.py        # ★ website ka data taza (yeh bhoolna mat)
```
Phir commit + push. 2-3 minute me site live.

## 2) Naya subject LIVE karna ho (jaise DBMS)
1. Uska bank banao: `Subject/data/xx_questions.json` (CN wale format me).
2. `tools/build_site_data.py` me us subject ka slim file bhi nikalo (`assets/xx-questions.min.json`).
3. `index.html` me:
   - `SUBJECTS` list me us subject ka `st:"soon"` → `st:"live"`, `pct:100`, chips me asli ginti likho.
   - Test Centre ke `fSubject` dropdown me option jodo, aur subject badalne par uska data load karo
     (abhi CN wala `fetch(...)` ek hi hai — wahi pattern copy karna hai).
   - Hero/Register ke number badlo.
4. Pehle mobile par test karke dekho, phir push.

## 3) Sirf likhai/design badalna ho
Sab kuch `index.html` ke `<style>` aur body me hai. Rang: Navy `#16283f`, kesariya `#E97313` —
EkGuru ki pehchan yahi hai, yahi rakho taaki saari kitaabein/site ek parivar lagein.

## 4) Dhyaan rahe
- `assets/cn-questions.min.json` haath se kabhi edit mat karo — hamesha script se banao.
- Nayi file ke naam me space ho to link me `%20` likho (books table me udaharan hai).
- Push se pehle browser me `index.html` khol kar ek 10-question test pura karke dekho.
