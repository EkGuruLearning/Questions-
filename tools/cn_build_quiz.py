# -*- coding: utf-8 -*-
"""
cn_build_quiz.py — EkGuru Online Test Portal (Quiz + Exam) generator.

Design goals (user spec):
  * Looks hand-made (coaching-portal style), NOT AI-generated — clean headings,
    proper title/footer, no decorative junk
  * LIVE-EXAM features (CBT style): Mark for Review & Next, Clear Response,
    Save & Next, question palette with colour codes, countdown timer, summary
  * Quiz mode: click -> instant ✔/✗ + answer + explanation
  * Exam mode: submit -> Correct / Wrong / SKIPPED (separate!) + accuracy +
    time taken + time-per-question + full solutions after submit
  * Name entry; branding EkGuru + by PRAKASH; questions+options shuffle every run
  * Mobile-friendly, single-file offline HTML
Usage: python tools/cn_build_quiz.py            (all 7 topics)
       python tools/cn_build_quiz.py 3 5
"""
import os, sys, json

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
                exp_en = (exp_en + " | Nukta: " + nk) if exp_en else ("Nukta: " + nk)
            nkh = (q["nk"][1] or "").strip()
            if nkh:
                exp_hi = (exp_hi + " | " + nkh) if exp_hi else nkh
            items.append({
                "q": [q["q"][0], q["q"][1] or ""],
                "opts": opts,
                "ans": q["ans"],
                "exp": [exp_en, exp_hi],
                "src": q["src"],
                "sec": s["title"],
            })
    return items


CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Roboto, Arial, 'Noto Sans Devanagari', sans-serif; background: #f0f2f5; color: #1c2733; font-size: 15px; }
.topstrip { background: #1F3864; color: #fff; padding: 7px 14px; font-size: 12.5px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 6px; }
.topstrip b { color: #ffd580; }
.nav { background: #fff; border-bottom: 3px solid #E97313; padding: 10px 14px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; }
.logo { font-size: 24px; font-weight: 800; letter-spacing: .3px; }
.logo .e { color: #E97313; } .logo .g { color: #1F3864; }
.logo small { display: block; font-size: 10px; font-weight: 600; letter-spacing: 2.2px; color: #667; }
.navtitle { font-size: 14.5px; font-weight: 700; color: #1F3864; text-align: right; }
.wrap { max-width: 980px; margin: 0 auto; padding: 12px 10px 26px; }
.card { background: #fff; border: 1px solid #d7dde6; border-radius: 6px; padding: 16px 16px; margin-bottom: 12px; }
h2 { font-size: 17px; color: #1F3864; border-bottom: 2px solid #E97313; display: inline-block; padding-bottom: 4px; margin-bottom: 12px; }
.fld { margin: 10px 0; }
.fld label { font-size: 13px; font-weight: 700; color: #34435a; display: block; margin-bottom: 5px; }
input[type=text], select { width: 100%; padding: 11px 10px; font-size: 15px; border: 1.5px solid #b9c4d4; border-radius: 5px; background: #fbfcfe; }
ol.ins { margin: 6px 0 6px 20px; font-size: 13px; line-height: 1.8; color: #33405a; }
.chkline { font-size: 13px; margin: 10px 0 4px; color: #33405a; }
.btn { border: 0; border-radius: 5px; padding: 12px 20px; font-size: 14.5px; font-weight: 700; cursor: pointer; }
.btn.prime { background: #E97313; color: #fff; }
.btn.blue { background: #1F3864; color: #fff; }
.btn.ghost { background: #eef1f6; color: #26364d; border: 1px solid #b9c4d4; }
.btn.violet { background: #673ab7; color: #fff; }
.btn:active { transform: scale(.985); }
.btnrow { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
.tbar { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; background: #1F3864; color: #fff; border-radius: 5px; padding: 9px 12px; margin-bottom: 10px; font-size: 13px; }
.tbar .timer { font-size: 19px; font-weight: 800; letter-spacing: 1px; }
.tbar .timer.low { color: #ffb3b3; }
.layout { display: flex; gap: 12px; align-items: flex-start; }
.qcol { flex: 1.8; min-width: 300px; }
.pcol { flex: 1; min-width: 230px; }
@media (max-width: 720px) { .layout { flex-direction: column; } .qcol, .pcol { width: 100%; min-width: 0; } }
.qhead { background: #f5f7fa; border: 1px solid #e2e7ee; border-radius: 5px; padding: 8px 10px; font-size: 12.5px; color: #45536b; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }
.qtext { font-size: 16.5px; font-weight: 700; line-height: 1.5; margin: 4px 2px 8px; }
.qhi { font-size: 13.5px; color: #4d5a6e; line-height: 1.65; margin: 0 2px 12px; }
.opt { display: block; width: 100%; text-align: left; background: #fff; border: 1.5px solid #c4cddc; border-radius: 5px; padding: 12px 12px; font-size: 14.5px; margin-bottom: 8px; cursor: pointer; line-height: 1.5; }
.opt:hover { border-color: #E97313; background: #fff8f1; }
.opt .oh { color: #5d6b80; font-size: 12.5px; }
.opt.sel { border-color: #1F3864; background: #eaf0f9; }
.opt.correct { border-color: #1b7a3d; background: #e7f5ec; }
.opt.wrong { border-color: #c0392b; background: #fdecea; }
.opt.dim { opacity: .5; }
.fb { border-radius: 5px; padding: 11px 12px; margin: 8px 0 2px; font-size: 13.5px; line-height: 1.6; border: 1px solid; }
.fb.ok { background: #e9f6ee; border-color: #1b7a3d; color: #14532d; }
.fb.no { background: #fdecea; border-color: #c0392b; color: #7b1f14; }
.fb .exp { margin-top: 6px; color: #2b3646; }
.fb .exp .hi { color: #55617a; font-size: 12.5px; margin-top: 3px; }
.fb .src { margin-top: 6px; font-size: 11px; color: #7b8798; }
.legend { font-size: 11.5px; color: #45536b; margin: 8px 0 10px; line-height: 2; }
.legend .sw { display: inline-block; width: 13px; height: 13px; border-radius: 3px; margin: 0 5px 0 8px; vertical-align: -2px; border: 1px solid #99a; }
.palette { display: flex; flex-wrap: wrap; gap: 6px; }
.pq { width: 38px; height: 34px; border-radius: 4px; border: 1.5px solid #b9c4d4; background: #fff; font-size: 12.5px; font-weight: 700; cursor: pointer; color: #2b3646; position: relative; }
.pq.nv { background: #fff; }
.pq.vis { background: #f6c9c2; border-color: #d98a7d; color: #7b2718; }
.pq.ans { background: #b7e2c3; border-color: #4ca36a; color: #14532d; }
.pq.mk { background: #d9c8f2; border-color: #8a63c9; color: #3d2472; }
.pq.mkans { background: #d9c8f2; border-color: #8a63c9; color: #3d2472; }
.pq.mkans::after { content: '\\2713'; position: absolute; right: 2px; bottom: 0px; font-size: 10px; color: #1b7a3d; }
.pq.cur { outline: 2.5px solid #1F3864; outline-offset: 1px; }
.summary { margin-top: 10px; border-top: 1px solid #e2e7ee; padding-top: 9px; font-size: 12px; color: #45536b; line-height: 1.9; }
.statgrid { display: grid; grid-template-columns: repeat(auto-fit, minmax(128px, 1fr)); gap: 10px; margin: 12px 0 4px; }
.stat { border: 1px solid #d7dde6; border-radius: 6px; padding: 12px 8px; text-align: center; background: #fff; }
.stat .v { font-size: 22px; font-weight: 800; }
.stat .l { font-size: 11px; color: #66708a; font-weight: 700; letter-spacing: .6px; margin-top: 3px; }
.stat.c .v { color: #1b7a3d; } .stat.w .v { color: #c0392b; } .stat.s .v { color: #7a8494; } .stat.t .v { color: #1F3864; }
table.tt { width: 100%; border-collapse: collapse; font-size: 12.5px; margin: 8px 0; }
table.tt td, table.tt th { border: 1px solid #dfe5ec; padding: 6px 8px; text-align: left; }
table.tt th { background: #eef2f7; color: #2b3646; }
.rev { border-top: 1px solid #e2e7ee; padding: 13px 2px 10px; }
.rev .st { font-size: 11px; font-weight: 800; border-radius: 4px; padding: 2px 8px; margin-right: 6px; }
.st.c { background: #e7f5ec; color: #14532d; border: 1px solid #4ca36a; }
.st.w { background: #fdecea; color: #7b1f14; border: 1px solid #d98a7d; }
.st.s { background: #eef1f5; color: #4a5468; border: 1px solid #aab4c2; }
.rev .qh { font-weight: 700; font-size: 14.5px; line-height: 1.5; margin: 6px 0 4px; }
.rev .qhm { color: #4d5a6e; font-size: 12.5px; line-height: 1.6; margin-bottom: 7px; }
.rev .line { font-size: 13px; margin: 3px 0; line-height: 1.55; }
.rev .okc { color: #1b7a3d; font-weight: 700; }
.rev .noc { color: #c0392b; font-weight: 700; }
.rev .exp { background: #f5f8fc; border-left: 3.5px solid #1F3864; padding: 9px 11px; font-size: 12.5px; margin-top: 8px; line-height: 1.6; }
.rev .exp .hi { color: #55617a; margin-top: 4px; }
.rev .meta { font-size: 11px; color: #7b8798; margin-top: 6px; }
.foot { text-align: center; color: #7a8494; font-size: 11.5px; line-height: 1.8; margin: 16px 6px 4px; border-top: 1px solid #d7dde6; padding-top: 12px; }
.foot b { color: #45536b; }
.hint { font-size: 12px; color: #66708a; line-height: 1.65; margin-top: 8px; }
.resTitle { font-size: 18px; color: #1F3864; font-weight: 800; margin: 4px 0 2px; }
"""


def build_html(n, items):
    title = TOPICS[n]
    data = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EkGuru Online Test — Topic {n}: {title}</title>
<style>{CSS}</style>
</head>
<body>
<div class="topstrip">
  <span>EkGuru Learning &nbsp;|&nbsp; Computer Networks (Forouzan) &nbsp;|&nbsp; Online Test Portal</span>
  <span>Compiled &amp; updated <b>by PRAKASH</b></span>
</div>
<div class="nav">
  <div class="logo"><span class="e">Ek</span><span class="g">Guru</span><small>ONLINE TEST PORTAL</small></div>
  <div class="navtitle">Topic {n} — {title}<br><span style="font-weight:400; font-size:11.5px; color:#667">Practice Questions &nbsp;•&nbsp; Quiz Mode / Exam Mode</span></div>
</div>
<div class="wrap">

<div class="card" id="startCard">
  <h2>Test Instructions</h2>
  <ol class="ins">
    <li>Test shuru karne ke liye apna naam likhein aur mode chunein.</li>
    <li><b>Quiz Mode:</b> har question ke baad sahi uttar aur explanation turant dikhayi degi — seekhne ke liye.</li>
    <li><b>Exam Mode:</b> sabse pehle saare questions karein, phir <b>Submit</b> karein. Result mein Correct / Wrong / Chhode hue alag gine jayenge.</li>
    <li>Exam Mode mein <b>Mark for Review</b>, <b>Clear Response</b>, <b>Save &amp; Next</b> aur question palette milte hain — bilkul live exam jaisa.</li>
    <li>Questions aur options har baar doosre kram mein aate hain.</li>
    <li>Samay poora hone par test apne aap submit ho jayega.</li>
    <li>Submit ke baad har question ka explanation (solution) diya jayega.</li>
  </ol>
  <div class="fld"><label>Apka naam / Candidate name</label>
    <input type="text" id="nameIn" maxlength="40" placeholder="Naam likhein"></div>
  <div class="fld"><label>Mode</label>
    <select id="modeIn">
      <option value="quiz">Quiz Mode — instant answer + explanation</option>
      <option value="exam">Exam Mode — submit ke baad result + analysis</option>
    </select></div>
  <div class="fld"><label>Questions ki sankhya</label>
    <select id="countIn">
      <option value="10">10</option>
      <option value="25">25</option>
      <option value="50">50</option>
      <option value="0">Sabhi ({len(items)})</option>
    </select></div>
  <div class="fld"><label>Har question ka samay (Exam Mode — total timer isi se banega)</label>
    <select id="tpqIn">
      <option value="45">45 second per question</option>
      <option value="60" selected>60 second per question</option>
      <option value="90">90 second per question</option>
      <option value="120">2 minute per question</option>
    </select></div>
  <div class="chkline"><input type="checkbox" id="agreeIn"> <label for="agreeIn" style="display:inline">Maine instructions padh li hain.</label></div>
  <button class="btn prime" onclick="startTest()">Test Shuru Karein</button>
  <div class="hint">Questions repo exam papers, Forouzan tatha India-level PYQ banks (2011–2026) se liye gaye hain. Sabhi uttar verify kiye gaye hain.</div>
</div>

<div class="card" id="testCard" style="display:none">
  <div class="tbar">
    <span id="whoLine"></span>
    <span id="timerLine" class="timer">00:00</span>
    <span id="progLine"></span>
  </div>
  <div class="layout">
    <div class="qcol">
      <div class="qhead">
        <span id="qNoLine"><b>Question 1</b></span>
        <span id="secLine"></span>
      </div>
      <div class="qtext" id="qText"></div>
      <div class="qhi" id="qHi"></div>
      <div id="optBox"></div>
      <div id="fbBox"></div>
      <div class="btnrow" id="ctrlBox"></div>
    </div>
    <div class="pcol">
      <div class="card" style="margin:0">
        <div class="legend">
          <span class="sw" style="background:#fff"></span> Not visited
          <span class="sw" style="background:#f6c9c2"></span> Dekha, uttar nahi
          <span class="sw" style="background:#b7e2c3"></span> Uttar diya
          <span class="sw" style="background:#d9c8f2"></span> Marked for review
          <span class="sw" style="background:#d9c8f2"></span><b style="color:#1b7a3d">&#10003;</b> Uttar + marked
        </div>
        <div class="palette" id="dotBox"></div>
        <div class="summary" id="sumBox"></div>
      </div>
    </div>
  </div>
</div>

<div class="card" id="resultCard" style="display:none">
  <h2>Result Summary</h2>
  <div class="resTitle" id="resTitle"></div>
  <div class="hint" id="resSub"></div>
  <div class="statgrid" id="statGrid"></div>
  <table class="tt" id="resTable"></table>
  <div class="btnrow">
    <button class="btn blue" onclick="window.print()">Print / Save Result</button>
    <button class="btn ghost" onclick="location.reload()">Naya Test</button>
  </div>
  <h2 style="margin-top:20px">Question-wise Solutions</h2>
  <div id="revBox"></div>
</div>

<div class="foot">
  <b>EkGuru Learning</b> — Computer Networks Practice Portal (Reference: Forouzan, Data Communications &amp; Networking)<br>
  Questions: repo exam papers + India-level PYQ banks (GATE, UGC NET, RPSC, KVS, EMRS, SSC, RRB, IBPS — 2011–2026) + original practice set.<br>
  Compiled &amp; updated <b>by PRAKASH</b> &nbsp;|&nbsp; Topic {n}: {title}
</div>
</div>

<script>
const QUESTIONS = {data};
const L = ["A","B","C","D"];
let S = {{ qs: [], idx: 0, mode: "quiz", name: "", t0: 0, endAt: 0, tick: null,
        answers: {{}}, marks: {{}}, visited: {{}}, spent: [], enter: 0, locked: false }};

function shuffle(a) {{ for (let i=a.length-1;i>0;i--) {{ const j=Math.floor(Math.random()*(i+1)); const t=a[i]; a[i]=a[j]; a[j]=t; }} return a; }}
function esc(s) {{ const d=document.createElement('div'); d.textContent = s==null?'':String(s); return d.innerHTML; }}
function fmt(sec) {{ sec=Math.max(0,sec); const m=Math.floor(sec/60), s=sec%60; return (m<10?'0':'')+m+':'+(s<10?'0':'')+s; }}

function startTest() {{
  const name = document.getElementById('nameIn').value.trim();
  if (!name) {{ alert('Kripya apna naam likhein.'); return; }}
  if (!document.getElementById('agreeIn').checked) {{ alert('Kripya instructions padhkar checkbox tik karein.'); return; }}
  S.name = name;
  S.mode = document.getElementById('modeIn').value;
  let count = parseInt(document.getElementById('countIn').value, 10) || QUESTIONS.length;
  count = Math.min(count, QUESTIONS.length);
  const tpq = parseInt(document.getElementById('tpqIn').value, 10) || 60;
  S.qs = shuffle(QUESTIONS.slice()).slice(0, count).map(q => {{
    const ix = [0,1,2,3]; shuffle(ix);
    return {{ q: q.q, opts: ix.map(i => q.opts[i]), ans: ix.indexOf(q.ans), exp: q.exp, src: q.src, sec: q.sec }};
  }});
  S.idx = 0; S.answers = {{}}; S.marks = {{}}; S.visited = {{}}; S.locked = false;
  S.spent = new Array(S.qs.length).fill(0);
  S.t0 = Date.now();
  S.endAt = S.mode === 'exam' ? S.t0 + count * tpq * 1000 : 0;
  document.getElementById('startCard').style.display = 'none';
  document.getElementById('testCard').style.display = '';
  document.getElementById('resultCard').style.display = 'none';
  document.getElementById('whoLine').innerHTML = '<b>' + esc(S.name) + '</b> &nbsp;|&nbsp; ' + (S.mode === 'quiz' ? 'Quiz Mode' : 'Exam Mode');
  clearInterval(S.tick);
  S.tick = setInterval(tickTimer, 500);
  tickTimer();
  renderPalette(); renderQ();
}}

function tickTimer() {{
  const el = document.getElementById('timerLine');
  if (S.mode === 'exam') {{
    const left = Math.round((S.endAt - Date.now())/1000);
    el.textContent = fmt(left);
    el.className = 'timer' + (left <= 60 ? ' low' : '');
    if (left <= 0) {{ clearInterval(S.tick); submitTest(true); }}
  }} else {{
    el.textContent = fmt(Math.floor((Date.now()-S.t0)/1000));
    el.className = 'timer';
  }}
}}

function paletteClass(i) {{
  if (S.marks[i]) return (S.answers[i] !== undefined) ? 'pq mkans' : 'pq mk';
  if (S.answers[i] !== undefined) return 'pq ans';
  if (S.visited[i]) return 'pq vis';
  return 'pq nv';
}}
function renderPalette() {{
  const b = document.getElementById('dotBox'); b.innerHTML = '';
  S.qs.forEach((q,i) => {{
    const d = document.createElement('button');
    d.className = paletteClass(i) + (i === S.idx ? ' cur' : '');
    d.textContent = i+1;
    d.onclick = () => jumpTo(i);
    b.appendChild(d);
  }});
  let a=0, m=0, v=0;
  S.qs.forEach((q,i) => {{
    if (S.answers[i] !== undefined) a++;
    if (S.marks[i]) m++;
    if (S.visited[i]) v++;
  }});
  const notAns = v - a < 0 ? 0 : v - a;
  document.getElementById('sumBox').innerHTML =
    'Questions: <b>' + S.qs.length + '</b> &nbsp;|&nbsp; Uttar diye: <b style="color:#1b7a3d">' + a + '</b><br>' +
    'Uttar nahi diye (dekhe hue): <b style="color:#c0392b">' + notAns + '</b> &nbsp;|&nbsp; Marked: <b style="color:#673ab7">' + m + '</b><br>' +
    'Bina dekhe: <b>' + (S.qs.length - v) + '</b>';
  document.getElementById('progLine').textContent = a + ' / ' + S.qs.length + ' answered';
}}

function saveTime() {{
  const now = Date.now();
  if (S.enter) {{ S.spent[S.idx] += (now - S.enter)/1000; }}
  S.enter = now;
}}

function renderQ() {{
  const q = S.qs[S.idx];
  S.visited[S.idx] = true;
  S.enter = Date.now();
  document.getElementById('qNoLine').innerHTML = '<b>Question ' + (S.idx+1) + '</b> / ' + S.qs.length;
  document.getElementById('secLine').textContent = q.sec;
  document.getElementById('qText').innerHTML = esc(q.q[0]);
  document.getElementById('qHi').textContent = q.q[1] || '';
  const box = document.getElementById('optBox'); box.innerHTML = '';
  q.opts.forEach((o,i) => {{
    const b = document.createElement('button');
    b.className = 'opt' + (S.answers[S.idx] === i ? ' sel' : '');
    b.innerHTML = '<b>(' + L[i] + ')</b> ' + esc(o[0]) + (o[1] && o[1].toLowerCase() !== o[0].toLowerCase() ? ' <span class="oh">/ ' + esc(o[1]) + '</span>' : '');
    b.onclick = () => onPick(i);
    box.appendChild(b);
  }});
  document.getElementById('fbBox').innerHTML = '';
  const cb = document.getElementById('ctrlBox'); cb.innerHTML = '';
  function addBtn(txt, cls, fn) {{
    const b = document.createElement('button'); b.className = 'btn ' + cls; b.innerHTML = txt; b.onclick = fn; cb.appendChild(b);
  }}
  if (S.mode === 'exam') {{
    addBtn('Clear Response', 'ghost', clearResp);
    addBtn('Mark for Review &amp; Next', 'violet', markNext);
    addBtn('Save &amp; Next', 'blue', saveNext);
    addBtn('Submit Test', 'prime', () => submitTest(false));
    if (S.answers[S.idx] !== undefined) showAnsweredOnly();
  }} else {{
    if (S.answers[S.idx] !== undefined) {{
      showFeedback(S.answers[S.idx]);
    }} else {{
      addBtn('Chhod kar agla', 'ghost', () => {{ saveTime(); S.idx = Math.min(S.idx+1, S.qs.length-1); renderPalette(); renderQ(); }});
    }}
    addBtn('Submit &amp; Result', 'prime', () => submitTest(false));
  }}
  renderPalette();
}}

function showAnsweredOnly() {{
  const i = S.answers[S.idx];
  document.querySelectorAll('#optBox .opt').forEach((el,k) => el.classList.toggle('sel', k === i));
}}

function onPick(i) {{
  if (S.mode === 'quiz') {{
    if (S.locked) return;
    if (S.answers[S.idx] !== undefined) return;
    S.answers[S.idx] = i; S.locked = true;
    showFeedback(i);
    renderPalette();
  }} else {{
    S.answers[S.idx] = i;
    showAnsweredOnly();
    renderPalette();
  }}
}}

function showFeedback(picked) {{
  const q = S.qs[S.idx];
  const ok = picked === q.ans;
  document.querySelectorAll('#optBox .opt').forEach((el,k) => {{
    if (k === q.ans) el.classList.add('correct');
    else if (k === picked) el.classList.add('wrong');
    else el.classList.add('dim');
  }});
  document.getElementById('fbBox').innerHTML =
    '<div class="fb ' + (ok ? 'ok' : 'no') + '">' +
    (ok ? '<b>Sahi uttar.</b>' : '<b>Galat uttar.</b> Sahi uttar: <b>(' + L[q.ans] + ') ' + esc(q.opts[q.ans][0]) + '</b>') +
    '<div class="exp"><b>Explanation:</b> ' + esc(q.exp[0] || '') + (q.exp[1] ? '<div class="hi">' + esc(q.exp[1]) + '</div>' : '') + '</div>' +
    '<div class="src">Source: ' + esc(q.src) + '</div></div>';
  const cb = document.getElementById('ctrlBox'); cb.innerHTML = '';
  const b = document.createElement('button'); b.className = 'btn blue';
  b.innerHTML = S.idx < S.qs.length-1 ? 'Agla Question' : 'Result Dekhein';
  b.onclick = () => {{ saveTime(); if (S.idx < S.qs.length-1) {{ S.idx++; S.locked = (S.answers[S.idx] !== undefined); renderQ(); }} else submitTest(false); }};
  cb.appendChild(b);
}}

function clearResp() {{ delete S.answers[S.idx]; renderQ(); }}
function markNext() {{ S.marks[S.idx] = true; saveTime(); nextQ(); }}
function saveNext() {{ saveTime(); nextQ(); }}
function nextQ() {{
  let n = -1;
  for (let i = S.idx+1; i < S.qs.length; i++) if (S.visited[i] === undefined) {{ n = i; break; }}
  if (n === -1) n = Math.min(S.idx+1, S.qs.length-1);
  S.idx = n; S.locked = false;
  renderQ();
}}
function jumpTo(i) {{ saveTime(); S.idx = i; S.locked = false; renderQ(); window.scrollTo({{top:0,behavior:'smooth'}}); }}

function submitTest(auto) {{
  saveTime();
  const a = Object.keys(S.answers).length;
  const un = S.qs.length - a;
  if (!auto && un > 0 && !confirm(un + ' questions ka uttar nahi diya gaya hai (ye galat nahi gine jayenge, bas chhode hue rahenge). Submit karein?')) return;
  if (!auto && un === 0 && !confirm('Saare questions answered hain. Submit karein?')) return;
  clearInterval(S.tick);
  const secs = Math.floor((Date.now()-S.t0)/1000);
  let correct = 0, wrong = 0;
  S.qs.forEach((q,i) => {{
    if (S.answers[i] === undefined) return;
    if (S.answers[i] === q.ans) correct++; else wrong++;
  }});
  const skipped = S.qs.length - correct - wrong;
  const attempted = correct + wrong;
  const acc = attempted ? Math.round(correct*100/attempted) : 0;
  const avgT = attempted ? (secs/attempted).toFixed(1) : '—';
  let slow = 0;
  S.spent.forEach((t,i) => {{ if (t > S.spent[slow]) slow = i; }});
  document.getElementById('testCard').style.display = 'none';
  document.getElementById('resultCard').style.display = '';
  document.getElementById('resTitle').textContent = S.name + ' — ' + (S.mode === 'quiz' ? 'Quiz Mode' : 'Exam Mode') + ' Result';
  document.getElementById('resSub').innerHTML = 'Topic {n}: {title} • Questions: ' + S.qs.length + ' • Unattempted questions galat nahi gine gaye.';
  document.getElementById('statGrid').innerHTML =
    '<div class="stat t"><div class="v">' + correct + ' / ' + S.qs.length + '</div><div class="l">SCORE</div></div>' +
    '<div class="stat c"><div class="v">' + correct + '</div><div class="l">SAHI (CORRECT)</div></div>' +
    '<div class="stat w"><div class="v">' + wrong + '</div><div class="l">GALAT (WRONG)</div></div>' +
    '<div class="stat s"><div class="v">' + skipped + '</div><div class="l">CHHODE HUE (SKIPPED)</div></div>' +
    '<div class="stat t"><div class="v">' + acc + '%</div><div class="l">ACCURACY (attempted)</div></div>' +
    '<div class="stat t"><div class="v">' + fmt(secs) + '</div><div class="l">SAMAY (TIME)</div></div>' +
    '<div class="stat t"><div class="v">' + avgT + 's</div><div class="l">AVG TIME / QUESTION</div></div>' +
    '<div class="stat t"><div class="v">' + (attempted ? (slow+1) : '—') + '</div><div class="l">SABSE ZYADA SAMAY (Q.no)</div></div>';
  let marked = 0; for (const k in S.marks) if (S.marks[k]) marked++;
  document.getElementById('resTable').innerHTML =
    '<tr><th>Candidate</th><td>' + esc(S.name) + '</td><th>Mode</th><td>' + (S.mode === 'quiz' ? 'Quiz' : 'Exam') + '</td></tr>' +
    '<tr><th>Total Questions</th><td>' + S.qs.length + '</td><th>Attempted</th><td>' + attempted + '</td></tr>' +
    '<tr><th>Correct / Wrong</th><td>' + correct + ' / ' + wrong + '</td><th>Skipped (chhode hue)</th><td>' + skipped + '</td></tr>' +
    '<tr><th>Accuracy</th><td>' + acc + '% (attempted par)</td><th>Marked for review</th><td>' + marked + '</td></tr>' +
    '<tr><th>Time taken</th><td>' + fmt(secs) + '</td><th>Avg time/question</th><td>' + avgT + 's</td></tr>';
  const rb = document.getElementById('revBox'); rb.innerHTML = '';
  S.qs.forEach((q,i) => {{
    const picked = S.answers[i];
    let chip, line;
    if (picked === undefined) {{
      chip = '<span class="st s">CHHODA (SKIPPED)</span>';
      line = '<div class="line">Is question ka uttar nahi diya gaya.</div>';
    }} else if (picked === q.ans) {{
      chip = '<span class="st c">SAHI</span>';
      line = '<div class="line"><span class="okc">Aapka uttar: (' + L[picked] + ') ' + esc(q.opts[picked][0]) + '</span></div>';
    }} else {{
      chip = '<span class="st w">GALAT</span>';
      line = '<div class="line"><span class="noc">Aapka uttar: (' + L[picked] + ') ' + esc(q.opts[picked][0]) + '</span></div>' +
             '<div class="line"><span class="okc">Sahi uttar: (' + L[q.ans] + ') ' + esc(q.opts[q.ans][0]) + '</span></div>';
    }}
    const div = document.createElement('div');
    div.className = 'rev';
    div.innerHTML = chip + (S.marks[i] ? '<span class="st" style="background:#d9c8f2;color:#3d2472;border:1px solid #8a63c9">MARKED</span>' : '') +
      '<div class="qh">Q' + (i+1) + '. ' + esc(q.q[0]) + '</div>' +
      '<div class="qhm">' + esc(q.q[1] || '') + '</div>' +
      q.opts.map((o,k) => '<div class="line">' + (k === q.ans ? '<span class="okc">(' + L[k] + ') ' + esc(o[0]) + '</span>' : '(' + L[k] + ') ' + esc(o[0])) + '</div>').join('') +
      line +
      '<div class="exp"><b>Explanation:</b> ' + esc(q.exp[0] || '—') + (q.exp[1] ? '<div class="hi">' + esc(q.exp[1]) + '</div>' : '') + '</div>' +
      '<div class="meta">Samay: ' + (S.spent[i] || 0).toFixed(0) + ' second &nbsp;|&nbsp; Source: ' + esc(q.src) + ' &nbsp;|&nbsp; ' + esc(q.sec) + '</div>';
    rb.appendChild(div);
  }});
  window.scrollTo({{top:0,behavior:'smooth'}});
}}

document.getElementById('nameIn').addEventListener('keyup', e => {{ if (e.key === 'Enter') startTest(); }});
</script>
</body>
</html>
"""


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    nums = [int(a) for a in sys.argv[1:]] or list(TOPICS)
    for n in nums:
        items = collect(n)
        out = os.path.join(OUT_DIR, f"Topic {n} - Online Quiz & Exam (by PRAKASH - EkGuru).html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(build_html(n, items))
        print(f"Topic {n}: {len(items)} questions -> {os.path.basename(out)} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
