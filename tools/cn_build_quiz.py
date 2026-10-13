# -*- coding: utf-8 -*-
"""
cn_build_quiz.py — Online Quiz/Exam HTML generator (single-file, offline, mobile).

Per user spec:
  * Quiz mode  : click -> turant right/wrong + correct answer + explanation
  * Exam mode  : pehle solve -> Submit -> score + accuracy + time + analysis
                 (har question ka explanation solution submit ke baad)
  * Name entry before start; branding "by PRAKASH" + "EkGuru"
  * Questions + options shuffle EVERY time (aage-peechhe, upar-neeche)
  * Responsive (phone par bhi chale), single HTML file, offline
  * Topic-wise separate files (abhi Topic 1 & 2; baaki baad mein)
Usage: python tools/cn_build_quiz.py 1 2
"""
import os, sys, json, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT_DIR = os.path.abspath(os.path.join(HERE, "..", "Computer Network", "Online Quiz"))

TOPICS = {
    1: "Introduction of Data Communication",
    2: "Network Models (OSI & TCP/IP)",
    3: "Addressing (MAC, IPv4, IPv6, Port, DNS)",
    4: "Networking Devices",
    5: "Transmission Medium",
    6: "OSI Layers in Detail",
    7: "Network Security",
}
NEW_MAP = {
    1: ["P1_A", "P1_B", "P1_C", "P1_D", "P1_E", "P1_F", "P1_G"],
    2: ["P2_A", "P2_B", "P2_C", "P2_D"],
    3: ["P3_A", "P3_B", "P3_C", "P3_D", "P3_E"],
    4: ["P4_A", "P4_B", "P4_C", "P4_D"],
    5: ["P5_A", "P5_B", "P5_C"],
    6: ["P6_A", "P6_B", "P6_C", "P6_D", "P6_E"],
    7: ["P7_A", "P7_B", "P7_C"],
}


def load(name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, os.path.join(DATA, f"{name}.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def to_qdict(t):
    src, qen, qhi, opts, ans, wr, nk, ww = t
    o2 = [(list(o) if isinstance(o, (tuple, list)) else [o, o]) for o in opts]
    return dict(src=src, q=[qen, qhi], opts=o2, ans=ans, wr=list(wr), nk=list(nk), ww={})


def collect(n):
    d = load(f"topic{n}_data")
    new_map = {}
    for pn in ("practice_new_p1", "practice_new_p2", "practice_new_p3"):
        m = load(pn)
        for k in dir(m):
            if k.startswith("P") and isinstance(getattr(m, k), list):
                new_map[k] = getattr(m, k)
    items = []
    for idx, s in enumerate(d.SECTIONS):
        qs = list(s["questions"])
        nn = NEW_MAP[n][idx] if idx < len(NEW_MAP.get(n, [])) else None
        if nn and nn in new_map:
            qs.extend(to_qdict(t) for t in new_map[nn])
        for q in qs:
            opts = [[(o[0] or ""), (o[1] or "")] for o in q["opts"]]
            exp_en = (q["wr"][0] or "").strip()
            exp_hi = (q["wr"][1] or "").strip()
            nk = (q["nk"][0] or "").strip()
            if nk:
                exp_en = (exp_en + "  ★ " + nk) if exp_en else ("★ " + nk)
            nkh = (q["nk"][1] or "").strip()
            if nkh:
                exp_hi = (exp_hi + "  ★ " + nkh) if exp_hi else ("★ " + nkh)
            items.append({
                "q": [q["q"][0], q["q"][1] or ""],
                "opts": opts,
                "ans": q["ans"],
                "exp": [exp_en, exp_hi],
                "src": q["src"],
                "sec": s["title"],
            })
    return items


def build_html(n, items):
    title = TOPICS[n]
    data = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EkGuru — Topic {n} Online Quiz &amp; Exam (by PRAKASH)</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, 'Segoe UI', Roboto, 'Noto Sans', 'Noto Sans Devanagari', sans-serif; background: #eef2f8; color: #16213a; }}
.hd {{ background: linear-gradient(135deg, #1F3864 0%, #2E5C9A 100%); color: #fff; padding: 14px 16px 12px; }}
.hd .brand {{ font-size: 13px; letter-spacing: 2px; opacity: .9; font-weight: 700; }}
.hd h1 {{ font-size: 19px; margin: 4px 0 2px; line-height: 1.3; }}
.hd .by {{ font-size: 12px; opacity: .92; }}
.wrap {{ max-width: 860px; margin: 0 auto; padding: 14px 12px 30px; }}
.card {{ background: #fff; border-radius: 14px; box-shadow: 0 2px 10px rgba(20,40,80,.10); padding: 18px 16px; margin-bottom: 14px; }}
label {{ font-size: 13px; font-weight: 700; color: #1F3864; display: block; margin: 10px 0 5px; }}
input[type=text], select {{ width: 100%; padding: 12px; font-size: 16px; border: 1.6px solid #c6d2e4; border-radius: 10px; }}
.btn {{ display: inline-block; border: 0; border-radius: 11px; padding: 13px 22px; font-size: 16px; font-weight: 800; cursor: pointer; margin: 8px 6px 2px 0; }}
.btn.main {{ background: #1F3864; color: #fff; width: 100%; }}
.btn.alt {{ background: #E8EEF8; color: #1F3864; }}
.btn.green {{ background: #0B6623; color: #fff; }}
.btn:active {{ transform: scale(.98); }}
.hint {{ font-size: 12.5px; color: #5b6b84; margin-top: 6px; line-height: 1.5; }}
.topbar {{ display: flex; justify-content: space-between; align-items: center; font-size: 13px; font-weight: 700; color: #1F3864; margin-bottom: 10px; flex-wrap: wrap; gap: 6px; }}
.progress {{ height: 8px; background: #dfe7f2; border-radius: 6px; overflow: hidden; margin-bottom: 12px; }}
.progress > div {{ height: 100%; background: linear-gradient(90deg,#0B6623,#3E9E58); width: 0%; transition: width .25s; }}
.qtext {{ font-size: 17px; font-weight: 800; line-height: 1.45; margin-bottom: 6px; }}
.qhi {{ font-size: 14.5px; color: #444; line-height: 1.55; margin-bottom: 12px; }}
.opt {{ display: block; width: 100%; text-align: left; background: #f6f8fc; border: 1.8px solid #cfd9ea; border-radius: 11px; padding: 12px 13px; font-size: 15px; margin-bottom: 9px; cursor: pointer; line-height: 1.45; }}
.opt .oh {{ color: #555; font-size: 13px; }}
.opt.sel {{ border-color: #1F3864; background: #e5ecf8; }}
.opt.correct {{ border-color: #0B6623; background: #e3f4e8; }}
.opt.wrong {{ border-color: #b3261e; background: #fbe6e4; }}
.opt.dim {{ opacity: .55; }}
.fb {{ border-radius: 11px; padding: 12px 13px; margin: 10px 0 4px; font-size: 14px; line-height: 1.55; }}
.fb.ok {{ background: #e3f4e8; border: 1.5px solid #0B6623; color: #0B4418; }}
.fb.no {{ background: #fbe6e4; border: 1.5px solid #b3261e; color: #7a1a14; }}
.fb .lbl {{ font-weight: 800; }}
.fb .hi {{ color: #333; font-size: 13px; margin-top: 5px; }}
.navrow {{ display: flex; justify-content: space-between; gap: 8px; margin-top: 12px; flex-wrap: wrap; }}
.dots {{ display: flex; flex-wrap: wrap; gap: 5px; margin: 10px 0; }}
.dot {{ width: 34px; height: 32px; border-radius: 8px; border: 1.5px solid #c6d2e4; background: #fff; font-size: 12px; font-weight: 700; cursor: pointer; color: #33415c; }}
.dot.done {{ background: #d8e6f7; border-color: #1F3864; color: #1F3864; }}
.dot.cur {{ background: #1F3864; color: #fff; border-color: #1F3864; }}
.statgrid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; margin: 12px 0; }}
.stat {{ background: #f2f6fc; border-radius: 12px; padding: 13px 10px; text-align: center; }}
.stat .v {{ font-size: 23px; font-weight: 800; color: #1F3864; }}
.stat .l {{ font-size: 11.5px; color: #5b6b84; font-weight: 700; margin-top: 3px; }}
.rev {{ border-top: 1.4px solid #dde5f0; padding: 13px 2px; }}
.rev .qh {{ font-weight: 800; font-size: 15px; line-height: 1.45; }}
.rev .qhm {{ color: #444; font-size: 13px; margin: 4px 0 7px; line-height: 1.5; }}
.rev .line {{ font-size: 13.5px; margin: 3px 0; line-height: 1.5; }}
.rev .okc {{ color: #0B6623; font-weight: 700; }}
.rev .noc {{ color: #b3261e; font-weight: 700; }}
.rev .exp {{ background: #f2f6fc; border-left: 4px solid #1F3864; border-radius: 8px; padding: 9px 11px; font-size: 13px; margin-top: 8px; line-height: 1.55; }}
.rev .exp .hi {{ color: #444; margin-top: 4px; }}
.rev .meta {{ font-size: 11px; color: #8592a8; margin-top: 6px; }}
.badge {{ display: inline-block; background: #1F3864; color: #fff; border-radius: 6px; font-size: 10.5px; padding: 2px 8px; font-weight: 700; margin-right: 5px; }}
.foot {{ text-align: center; color: #7b8aa3; font-size: 11.5px; margin: 18px 0 8px; line-height: 1.6; }}
.titleSec {{ color: #1F3864; font-size: 13px; font-weight: 800; margin-bottom: 6px; }}
@media (max-width: 520px) {{
  .hd h1 {{ font-size: 16.5px; }}
  .qtext {{ font-size: 15.5px; }}
  .opt {{ font-size: 14px; padding: 11px 11px; }}
  .btn {{ padding: 12px 16px; font-size: 15px; }}
}}
</style>
</head>
<body>
<div class="hd">
  <div class="brand">EK GURU &nbsp;•&nbsp; COMPUTER NETWORKS</div>
  <h1>Topic {n} — {title}</h1>
  <div class="by">Online Quiz &amp; Exam &nbsp;|&nbsp; <b>by PRAKASH</b> &nbsp;•&nbsp; EkGuru Learning</div>
</div>
<div class="wrap">

<div class="card" id="startCard">
  <div class="titleSec">📝 TEST SHURU KARNE SE PEHLE</div>
  <label>Apna naam likho / Your name</label>
  <input type="text" id="nameIn" placeholder="Jaise: Rahul Sharma" maxlength="40">
  <label>Mode chuno / Choose mode</label>
  <select id="modeIn">
    <option value="quiz">Quiz Mode — click karte hi answer + explanation (seekhne ke liye)</option>
    <option value="exam">Exam Mode — submit ke baad score, accuracy, time + analysis</option>
  </select>
  <label>Kitne questions? / Number of questions</label>
  <select id="countIn">
    <option value="10">10 (Quick test)</option>
    <option value="25">25</option>
    <option value="50">50</option>
    <option value="0">Saare ({len(items)})</option>
  </select>
  <button class="btn main" onclick="startTest()">🚀 START TEST</button>
  <div class="hint">✅ Questions aur options <b>har baar shuffle</b> hote hain (upar-neeche, aage-peechhe) — ratna nahi chalega! ✅ Answers verified hain. ✅ Phone / laptop / kahin bhi chalega (offline bhi).</div>
</div>

<div class="card" id="testCard" style="display:none">
  <div class="topbar">
    <span id="whoLine"></span>
    <span id="timerLine">⏱ 00:00</span>
    <span id="scoreLine"></span>
  </div>
  <div class="progress"><div id="progBar"></div></div>
  <div id="dotBox" class="dots"></div>
  <div class="titleSec" id="secLine"></div>
  <div class="qtext" id="qText"></div>
  <div class="qhi" id="qHi"></div>
  <div id="optBox"></div>
  <div id="fbBox"></div>
  <div class="navrow">
    <button class="btn alt" id="prevBtn" onclick="move(-1)">← Pichhla</button>
    <button class="btn green" id="nextBtn" onclick="move(1)">Agla →</button>
    <button class="btn main" id="submitBtn" onclick="submitTest()" style="display:none; width:auto">✅ TEST SUBMIT KARO</button>
  </div>
</div>

<div class="card" id="resultCard" style="display:none">
  <div class="titleSec">📊 RESULT &amp; ANALYSIS</div>
  <h2 id="resTitle" style="color:#1F3864; margin: 6px 0 2px;"></h2>
  <div class="hint" id="resSub"></div>
  <div class="statgrid" id="statGrid"></div>
  <button class="btn alt" onclick="location.reload()">🔁 Naya Test (shuffle ke saath)</button>
  <div class="titleSec" style="margin-top:16px">📖 HAR QUESTION KA EXPLANATION (submit ke baad)</div>
  <div id="revBox"></div>
</div>

<div class="foot">
  © <b>EkGuru Learning</b> &nbsp;|&nbsp; Computer Networks (Forouzan) Practice &nbsp;|&nbsp; Updated &amp; designed <b>by PRAKASH</b><br>
  Questions: repo exam papers + Forouzan + India-level PYQ banks (2011–2026) + original practice set — sab verified.
</div>
</div>

<script>
const QUESTIONS = {data};
const LETTERS = ["A","B","C","D"];
let S = {{ qs: [], idx: 0, mode: "quiz", name: "", t0: 0, timerId: null, locked: false, answered: {{}} }};

function shuffle(a) {{ for (let i = a.length - 1; i > 0; i--) {{ const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }} return a; }}
function esc(s) {{ const d = document.createElement('div'); d.textContent = s == null ? '' : String(s); return d.innerHTML; }}
function fmtTime(sec) {{ const m = Math.floor(sec/60), s = sec%60; return (m<10?'0':'')+m+':'+(s<10?'0':'')+s; }}

function startTest() {{
  const name = document.getElementById('nameIn').value.trim();
  if (!name) {{ alert('Pehle apna naam likho ✍️'); return; }}
  S.name = name;
  S.mode = document.getElementById('modeIn').value;
  let count = parseInt(document.getElementById('countIn').value, 10) || QUESTIONS.length;
  count = Math.min(count, QUESTIONS.length);
  S.qs = shuffle(QUESTIONS.slice()).slice(0, count).map(q => {{
    const idx = [0,1,2,3]; shuffle(idx);
    return {{ q: q.q, opts: idx.map(i => q.opts[i]), ans: idx.indexOf(q.ans), exp: q.exp, src: q.src, sec: q.sec }};
  }});
  S.idx = 0; S.answered = {{}}; S.locked = false;
  S.t0 = Date.now();
  document.getElementById('startCard').style.display = 'none';
  document.getElementById('testCard').style.display = '';
  document.getElementById('resultCard').style.display = 'none';
  document.getElementById('whoLine').textContent = '👤 ' + S.name + '  •  ' + (S.mode === 'quiz' ? 'Quiz Mode' : 'Exam Mode');
  clearInterval(S.timerId);
  S.timerId = setInterval(() => {{
    document.getElementById('timerLine').textContent = '⏱ ' + fmtTime(Math.floor((Date.now()-S.t0)/1000));
  }}, 1000);
  renderDots();
  renderQ();
}}

function renderDots() {{
  const b = document.getElementById('dotBox'); b.innerHTML = '';
  S.qs.forEach((q, i) => {{
    const d = document.createElement('button');
    d.className = 'dot' + (S.answered[i] !== undefined ? ' done' : '') + (i === S.idx ? ' cur' : '');
    d.textContent = i + 1;
    d.onclick = () => {{ S.idx = i; S.locked = (S.mode === 'quiz' && S.answered[i] !== undefined); renderDots(); renderQ(); }};
    b.appendChild(d);
  }});
}}

function renderQ() {{
  const q = S.qs[S.idx];
  document.getElementById('secLine').textContent = q.sec;
  document.getElementById('qText').innerHTML = '<b>Q' + (S.idx+1) + '.</b> ' + esc(q.q[0]);
  document.getElementById('qHi').textContent = q.q[1] || '';
  const box = document.getElementById('optBox'); box.innerHTML = '';
  q.opts.forEach((o, i) => {{
    const b = document.createElement('button');
    b.className = 'opt';
    b.innerHTML = '<b>(' + LETTERS[i] + ')</b> ' + esc(o[0]) + (o[1] && o[1].toLowerCase() !== o[0].toLowerCase() ? ' <span class="oh">/ ' + esc(o[1]) + '</span>' : '');
    b.onclick = () => onPick(i);
    box.appendChild(b);
  }});
  document.getElementById('fbBox').innerHTML = '';
  document.getElementById('prevBtn').style.visibility = S.idx === 0 ? 'hidden' : 'visible';
  const isLast = S.idx === S.qs.length - 1;
  document.getElementById('nextBtn').style.display = isLast ? 'none' : '';
  document.getElementById('submitBtn').style.display = isLast && S.mode === 'exam' ? '' : (isLast && S.mode === 'quiz' ? '' : 'none');
  if (S.mode === 'quiz' && S.answered[S.idx] !== undefined) {{
    showFeedback(S.answered[S.idx], true);
  }} else if (S.mode === 'exam' && S.answered[S.idx] !== undefined) {{
    markExamSel(S.answered[S.idx]);
  }}
  const pct = (Object.keys(S.answered).length / S.qs.length) * 100;
  document.getElementById('progBar').style.width = pct + '%';
  document.getElementById('scoreLine').textContent = S.mode === 'quiz'
    ? ('✅ ' + scoreNow().c + ' / ' + S.qs.length) : (Object.keys(S.answered).length + '/' + S.qs.length + ' answered');
}}

function markExamSel(i) {{
  document.querySelectorAll('#optBox .opt').forEach((el, k) => el.classList.toggle('sel', k === i));
}}

function onPick(i) {{
  if (S.mode === 'quiz') {{
    if (S.locked || S.answered[S.idx] !== undefined) return;
    S.answered[S.idx] = i; S.locked = true;
    showFeedback(i, false);
    document.getElementById('scoreLine').textContent = '✅ ' + scoreNow().c + ' / ' + S.qs.length;
    renderDots();
  }} else {{
    S.answered[S.idx] = i;
    markExamSel(i);
    document.getElementById('scoreLine').textContent = Object.keys(S.answered).length + '/' + S.qs.length + ' answered';
    renderDots();
  }}
}}

function showFeedback(picked, replay) {{
  const q = S.qs[S.idx];
  const ok = picked === q.ans;
  document.querySelectorAll('#optBox .opt').forEach((el, k) => {{
    if (k === q.ans) el.classList.add('correct');
    else if (k === picked) el.classList.add('wrong');
    else el.classList.add('dim');
  }});
  const fb = document.getElementById('fbBox');
  fb.innerHTML = '<div class="fb ' + (ok ? 'ok' : 'no') + '">' +
    '<span class="lbl">' + (ok ? '✅ SAHI!' : '❌ GALAT') + '</span> &nbsp; Sahi uttar: <b>(' + LETTERS[q.ans] + ') ' + esc(q.opts[q.ans][0]) + '</b>' +
    (q.exp[0] ? '<div class="hi">💡 ' + esc(q.exp[0]) + (q.exp[1] ? '<br>' + esc(q.exp[1]) : '') + '</div>' : '') +
    '<div class="hi" style="margin-top:5px">📚 Source: ' + esc(q.src) + '</div></div>';
  if (!replay && S.idx < S.qs.length - 1) {{
    setTimeout(() => {{ S.idx++; S.locked = false; renderDots(); renderQ(); }}, ok ? 650 : 1400);
  }}
}}

function scoreNow() {{
  let c = 0;
  for (const i in S.answered) {{ if (S.answered[i] === S.qs[i].ans) c++; }}
  return {{ c: c }};
}}

function move(d) {{
  const n = S.idx + d;
  if (n < 0 || n >= S.qs.length) return;
  S.idx = n; S.locked = (S.mode === 'quiz' && S.answered[n] !== undefined);
  renderDots(); renderQ();
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

function submitTest() {{
  const unanswered = S.qs.length - Object.keys(S.answered).length;
  if (unanswered > 0 && !confirm(unanswered + ' questions chhoote hain. Phir bhi submit karein?')) return;
  clearInterval(S.timerId);
  const secs = Math.floor((Date.now() - S.t0) / 1000);
  const sc = scoreNow().c, tot = S.qs.length;
  const acc = tot ? Math.round(sc * 100 / tot) : 0;
  document.getElementById('testCard').style.display = 'none';
  document.getElementById('resultCard').style.display = '';
  document.getElementById('resTitle').textContent = 'Well done, ' + S.name + '! 🎯';
  document.getElementById('resSub').innerHTML = (S.mode === 'quiz' ? 'Quiz Mode' : 'Exam Mode') + ' • ' + tot + ' questions • Answers verified (Forouzan + official keys)';
  document.getElementById('statGrid').innerHTML =
    '<div class="stat"><div class="v">' + sc + '/' + tot + '</div><div class="l">SCORE</div></div>' +
    '<div class="stat"><div class="v">' + acc + '%</div><div class="l">ACCURACY</div></div>' +
    '<div class="stat"><div class="v">' + fmtTime(secs) + '</div><div class="l">TIME TAKEN</div></div>' +
    '<div class="stat"><div class="v">' + (tot - sc) + '</div><div class="l">GALAT</div></div>';
  const rb = document.getElementById('revBox'); rb.innerHTML = '';
  S.qs.forEach((q, i) => {{
    const picked = S.answered[i];
    const ok = picked === q.ans;
    const div = document.createElement('div');
    div.className = 'rev';
    div.innerHTML = '<div class="qh">' + (ok ? '✅' : (picked === undefined ? '⬜' : '❌')) + ' Q' + (i+1) + '. ' + esc(q.q[0]) + '</div>' +
      '<div class="qhm">' + esc(q.q[1] || '') + '</div>' +
      q.opts.map((o, k) => '<div class="line">' + (k === q.ans ? '<span class="okc">✔ (' + LETTERS[k] + ') ' + esc(o[0]) + '</span>' : (k === picked ? '<span class="noc">✗ (' + LETTERS[k] + ') ' + esc(o[0]) + ' — aapka jawab</span>' : '(' + LETTERS[k] + ') ' + esc(o[0]))) + '</div>').join('') +
      '<div class="exp">💡 <b>Explanation:</b> ' + esc(q.exp[0] || '—') + (q.exp[1] ? '<div class="hi">' + esc(q.exp[1]) + '</div>' : '') + '</div>' +
      '<div class="meta"><span class="badge">' + esc(q.sec) + '</span>📚 ' + esc(q.src) + '</div>';
    rb.appendChild(div);
  }});
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

document.getElementById('nameIn').addEventListener('keyup', e => {{ if (e.key === 'Enter') startTest(); }});
</script>
</body>
</html>
"""


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    nums = [int(a) for a in sys.argv[1:]] or [1, 2]
    for n in nums:
        items = collect(n)
        out = os.path.join(OUT_DIR, f"Topic {n} - Online Quiz & Exam (by PRAKASH - EkGuru).html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(build_html(n, items))
        print(f"Topic {n}: {len(items)} questions -> {os.path.basename(out)} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
