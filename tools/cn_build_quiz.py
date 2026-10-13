# -*- coding: utf-8 -*-
"""
cn_build_quiz.py — EkGuru Online Test Portal (CBT-style) generator.

Layout = standard Indian online-exam interface, studied from real platforms:
  * TCS iON (IBPS/SBI/NTA) — question palette RIGHT + collapse arrow, Save & Next /
    Mark for Review & Next / Clear Response behaviour, section tabs on top bar,
    palette legend + summary above palette
  * SSC CBT 2025 new interface — action buttons at TOP of question area (above
    options), language selector just above the question, zoom in/out, answered
    count at top
  * NTA advisory — palette status colours, answered+marked considered for
    evaluation, ">" collapse of palette
Authentic exam behaviour (Exam Mode): option select = pending; answer SAVE hota
hai only on "Save & Next" / "Mark for Review & Next"; palette jump does NOT save.
Quiz Mode: instant feedback (learning mode).

Usage: python tools/cn_build_quiz.py            (all 7 topics, separate files)
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
    for pn in ("practice_new_p1", "practice_new_p2", "practice_new_p3",
               "practice_new_p4"):
        m = load(pn)
        for k in dir(m):
            if k.startswith("P") and isinstance(getattr(m, k), list):
                new_map[k] = getattr(m, k)
    items = []
    for idx, s in enumerate(d.SECTIONS):
        qs = list(s["questions"])
        nn = NEW_MAP[n][idx] if idx < len(NEW_MAP.get(n, [])) else None
        if nn:
            # base wave list + extra waves named NN_X / NN_X2 / ...
            for k2 in sorted(new_map):
                if k2 == nn or k2.startswith(nn + "_X"):
                    qs.extend(to_qdict(t) for t in new_map[k2])
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
body { font-family: 'Segoe UI', Roboto, Arial, 'Noto Sans Devanagari', sans-serif; background: #e9edf2; color: #1b2733; font-size: 15px; }
/* ===== top bar ===== */
.topbar { background: #16283f; color: #fff; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; padding: 8px 12px; position: sticky; top: 0; z-index: 50; }
.brand { font-size: 20px; font-weight: 800; }
.brand .e { color: #ff9d2e; } .brand .g { color: #fff; }
.brand small { display: block; font-size: 8.5px; letter-spacing: 2.4px; color: #9fb2c8; font-weight: 600; }
.testname { font-size: 13px; text-align: center; line-height: 1.5; }
.testname b { color: #ffd580; }
.topp { display: flex; align-items: center; gap: 7px; flex-wrap: wrap; }
.tbtn { background: #24405e; color: #fff; border: 1px solid #3d5d80; border-radius: 4px; padding: 7px 10px; font-size: 11.5px; font-weight: 700; cursor: pointer; white-space: nowrap; }
.tbtn:hover { background: #2f527a; }
.tbtn.on { background: #E97313; border-color: #E97313; }
.tbox { background: #0e1c2d; border: 1px solid #3d5d80; border-radius: 4px; padding: 4px 12px; text-align: center; }
.tbox .lbl { font-size: 8.5px; letter-spacing: 1.4px; color: #9fb2c8; font-weight: 700; }
.tbox .val { font-size: 18px; font-weight: 800; letter-spacing: 1px; }
.tbox .val.low { color: #ff7b7b; }
/* ===== section tabs ===== */
.secbar { background: #fff; border-bottom: 2px solid #d3dae4; display: flex; flex-wrap: wrap; gap: 2px; padding: 0 10px; position: sticky; top: 52px; z-index: 40; }
.stab { padding: 9px 13px; font-size: 11.5px; font-weight: 700; color: #44546a; cursor: pointer; border-bottom: 3px solid transparent; }
.stab:hover { color: #E97313; }
.stab.cur { color: #16283f; border-bottom-color: #E97313; background: #f7f9fc; }
/* ===== layout ===== */
.layout { display: flex; gap: 10px; align-items: flex-start; padding: 10px; max-width: 1280px; margin: 0 auto; }
.qcol { flex: 1; min-width: 300px; }
.pcol { width: 292px; flex-shrink: 0; position: sticky; top: 100px; }
.pcol.hidden { display: none; }
@media (max-width: 860px) { .pcol { position: static; width: 100%; } .layout { flex-direction: column; } }
/* ===== question panel ===== */
.qpanel { background: #fff; border: 1px solid #cfd7e2; border-radius: 5px; }
.qhead { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; background: #f3f6fa; border-bottom: 1px solid #dde4ec; padding: 8px 12px; font-size: 12px; color: #44546a; }
.qhead .qno { font-size: 13.5px; font-weight: 800; color: #16283f; }
.langsel { display: flex; gap: 0; border: 1px solid #b9c4d4; border-radius: 4px; overflow: hidden; }
.langsel button { border: 0; background: #fff; padding: 5px 10px; font-size: 11px; font-weight: 700; cursor: pointer; color: #44546a; }
.langsel button.on { background: #16283f; color: #fff; }
.actionbar { display: flex; flex-wrap: wrap; gap: 7px; padding: 9px 12px; border-bottom: 1px solid #dde4ec; background: #fafbfd; }
.abtn { border: 0; border-radius: 4px; padding: 8px 13px; font-size: 12px; font-weight: 800; cursor: pointer; }
.abtn.clear { background: #e8ebf0; color: #33405a; border: 1px solid #b9c4d4; }
.abtn.mark { background: #673ab7; color: #fff; }
.abtn.save { background: #1f6fb2; color: #fff; }
.abtn.prev { background: #eef1f6; color: #26364d; border: 1px solid #b9c4d4; }
.abtn.next { background: #16283f; color: #fff; }
.abtn:active { transform: scale(.98); }
.qbody { padding: 13px 14px 6px; }
.qtext { font-size: 16px; font-weight: 700; line-height: 1.55; margin-bottom: 4px; }
.qhi { font-size: 13px; color: #4d5a6e; line-height: 1.7; margin-bottom: 10px; }
.optrow { display: flex; align-items: flex-start; gap: 9px; border: 1.5px solid #c8d1de; border-radius: 5px; padding: 11px 12px; margin-bottom: 8px; cursor: pointer; background: #fff; line-height: 1.5; }
.optrow:hover { border-color: #E97313; background: #fff9f3; }
.optrow input { margin-top: 3px; }
.optrow.sel { border-color: #1f6fb2; background: #eaf2fa; }
.optrow.correct { border-color: #1b7a3d; background: #e7f5ec; }
.optrow.wrong { border-color: #c0392b; background: #fdecea; }
.optrow.dim { opacity: .55; }
.oidx { font-weight: 800; color: #2b3646; }
.otext { font-size: 14.5px; }
.oh { color: #5d6b80; font-size: 12.5px; }
.note { font-size: 11.5px; color: #7a8494; padding: 2px 14px 12px; }
.fb { margin: 6px 14px 12px; padding: 11px 12px; border: 1px solid; border-radius: 5px; font-size: 13.5px; line-height: 1.6; }
.fb.ok { background: #e9f6ee; border-color: #1b7a3d; color: #14532d; }
.fb.no { background: #fdecea; border-color: #c0392b; color: #7b1f14; }
.fb .exp { margin-top: 6px; color: #2b3646; }
.fb .exp .hi { color: #55617a; font-size: 12.5px; margin-top: 3px; }
.fb .src { margin-top: 6px; font-size: 11px; color: #7b8798; }
/* ===== palette ===== */
.ppanel { background: #fff; border: 1px solid #cfd7e2; border-radius: 5px; overflow: hidden; }
.ptitle { background: #16283f; color: #fff; font-size: 12px; font-weight: 800; letter-spacing: 1px; padding: 8px 11px; }
.legend { padding: 9px 11px 4px; font-size: 11px; color: #33405a; line-height: 1.65; }
.legend .row { display: flex; align-items: center; gap: 7px; margin-bottom: 3px; }
.sw { width: 15px; height: 15px; border-radius: 3px; border: 1.2px solid #99a; flex-shrink: 0; }
.sw.nv { background: #fff; } .sw.vis { background: #f19c8f; border-color: #d98a7d; }
.sw.ans { background: #8fd4a2; border-color: #4ca36a; } .sw.mk { background: #c6aeee; border-color: #8a63c9; }
.sw.ma { background: #c6aeee; border-color: #8a63c9; position: relative; }
.palette { display: flex; flex-wrap: wrap; gap: 6px; padding: 9px 11px; }
.pq { width: 40px; height: 35px; border-radius: 4px; border: 1.5px solid #b9c4d4; background: #fff; font-size: 12.5px; font-weight: 700; cursor: pointer; color: #2b3646; position: relative; }
.pq.nv { background: #fff; }
.pq.vis { background: #f19c8f; border-color: #d98a7d; color: #5e1a0e; }
.pq.ans { background: #8fd4a2; border-color: #4ca36a; color: #0f3d1e; }
.pq.mk { background: #c6aeee; border-color: #8a63c9; color: #2f1a5e; }
.pq.mkans { background: #c6aeee; border-color: #8a63c9; color: #2f1a5e; }
.pq.mkans::after { content: '\\2713'; position: absolute; right: 2px; bottom: 1px; font-size: 10px; color: #0f3d1e; font-weight: 900; }
.pq.cur { outline: 2.5px solid #E97313; outline-offset: 1px; }
.sumtitle { background: #eef2f7; border-top: 1px solid #dde4ec; border-bottom: 1px solid #dde4ec; padding: 6px 11px; font-size: 11px; font-weight: 800; letter-spacing: 1px; color: #33405a; }
.sumtab { width: 100%; border-collapse: collapse; font-size: 11.5px; }
.sumtab td { padding: 5px 11px; border-bottom: 1px solid #eef1f5; color: #44546a; }
.sumtab td.n { text-align: right; font-weight: 800; color: #16283f; }
.submitwrap { padding: 11px; }
.submitbtn { width: 100%; background: #1b7a3d; color: #fff; border: 0; border-radius: 5px; padding: 12px; font-size: 14.5px; font-weight: 800; cursor: pointer; }
.submitbtn:hover { background: #14632f; }
.palToggle { position: fixed; right: 0; top: 120px; z-index: 60; background: #16283f; color: #fff; border: 0; border-radius: 5px 0 0 5px; padding: 12px 7px; font-size: 13px; font-weight: 800; cursor: pointer; }
/* ===== overlays ===== */
.overlay { position: fixed; inset: 0; background: rgba(16,28,44,.55); z-index: 100; display: flex; align-items: flex-start; justify-content: center; padding: 18px 10px; overflow: auto; }
.sheet { background: #fff; border-radius: 7px; max-width: 780px; width: 100%; padding: 20px 20px 16px; }
.sheet h2 { font-size: 18px; color: #16283f; border-bottom: 2.5px solid #E97313; display: inline-block; padding-bottom: 5px; margin-bottom: 12px; }
ol.ins { margin: 4px 0 8px 22px; font-size: 12.5px; line-height: 1.85; color: #33405a; }
.fld { margin: 9px 0; }
.fld label { font-size: 12.5px; font-weight: 700; color: #33405a; display: block; margin-bottom: 4px; }
input[type=text], select { width: 100%; padding: 11px 10px; font-size: 15px; border: 1.5px solid #b9c4d4; border-radius: 5px; background: #fbfcfe; }
.btn { border: 0; border-radius: 5px; padding: 12px 22px; font-size: 14.5px; font-weight: 800; cursor: pointer; }
.btn.prime { background: #E97313; color: #fff; width: 100%; margin-top: 8px; }
.btn.blue { background: #16283f; color: #fff; }
.btn.ghost { background: #eef1f6; color: #26364d; border: 1px solid #b9c4d4; }
.chkline { font-size: 12.5px; margin: 10px 0 2px; color: #33405a; }
.hint { font-size: 11.5px; color: #66708a; line-height: 1.7; margin-top: 8px; }
/* ===== result ===== */
.resWrap { background: #fff; border: 1px solid #cfd7e2; border-radius: 5px; padding: 18px 18px; max-width: 1000px; margin: 12px auto; }
.resTitle { font-size: 18px; color: #16283f; font-weight: 800; margin: 2px 0 3px; }
.statgrid { display: grid; grid-template-columns: repeat(auto-fit, minmax(128px, 1fr)); gap: 10px; margin: 12px 0; }
.stat { border: 1px solid #d7dde6; border-radius: 6px; padding: 12px 8px; text-align: center; }
.stat .v { font-size: 22px; font-weight: 800; }
.stat .l { font-size: 10.5px; color: #66708a; font-weight: 700; letter-spacing: .5px; margin-top: 3px; }
.stat.c .v { color: #1b7a3d; } .stat.w .v { color: #c0392b; } .stat.s .v { color: #7a8494; } .stat.t .v { color: #16283f; }
table.tt { width: 100%; border-collapse: collapse; font-size: 12.5px; margin: 8px 0 12px; }
table.tt td, table.tt th { border: 1px solid #dfe5ec; padding: 6px 9px; text-align: left; }
table.tt th { background: #eef2f7; color: #2b3646; }
.rev { border-top: 1px solid #e2e7ee; padding: 13px 2px 10px; }
.st { font-size: 10.5px; font-weight: 800; border-radius: 4px; padding: 2px 8px; margin-right: 5px; }
.st.c { background: #e7f5ec; color: #14532d; border: 1px solid #4ca36a; }
.st.w { background: #fdecea; color: #7b1f14; border: 1px solid #d98a7d; }
.st.s { background: #eef1f5; color: #4a5468; border: 1px solid #aab4c2; }
.rev .qh { font-weight: 700; font-size: 14.5px; line-height: 1.5; margin: 6px 0 4px; }
.rev .qhm { color: #4d5a6e; font-size: 12.5px; line-height: 1.6; margin-bottom: 7px; }
.rev .line { font-size: 13px; margin: 3px 0; line-height: 1.55; }
.rev .okc { color: #1b7a3d; font-weight: 700; }
.rev .noc { color: #c0392b; font-weight: 700; }
.rev .exp { background: #f5f8fc; border-left: 3.5px solid #16283f; padding: 9px 11px; font-size: 12.5px; margin-top: 8px; line-height: 1.6; }
.rev .exp .hi { color: #55617a; margin-top: 4px; }
.rev .meta { font-size: 11px; color: #7b8798; margin-top: 6px; }
.foot { text-align: center; color: #7a8494; font-size: 11px; line-height: 1.8; margin: 10px 8px 6px; }
.foot b { color: #45536b; }
.btnrow { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
"""


JS = r"""
const QUESTIONS = __DATA__;
const L = ["A","B","C","D"];
let S = { qs: [], idx: 0, mode: "quiz", name: "", t0: 0, endAt: 0, tick: null,
        pending: undefined, answers: {}, marks: {}, visited: {}, spent: [],
        enter: 0, lang: "both", palHidden: false };

function shuffle(a) { for (let i=a.length-1;i>0;i--) { const j=Math.floor(Math.random()*(i+1)); const t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function esc(s) { const d=document.createElement('div'); d.textContent = s==null?'':String(s); return d.innerHTML; }
function fmt(sec) { sec=Math.max(0,sec); const m=Math.floor(sec/60), s=sec%60; return (m<10?'0':'')+m+':'+(s<10?'0':'')+s; }

/* ---------- start ---------- */
function startTest() {
  const name = document.getElementById('nameIn').value.trim();
  if (!name) { alert('Kripya apna naam likhein.'); return; }
  if (!document.getElementById('agreeIn').checked) { alert('Kripya instructions padhkar checkbox tik karein.'); return; }
  S.name = name;
  S.mode = document.getElementById('modeIn').value;
  let count = parseInt(document.getElementById('countIn').value, 10) || QUESTIONS.length;
  count = Math.min(count, QUESTIONS.length);
  const tpq = parseInt(document.getElementById('tpqIn').value, 10) || 60;
  S.qs = shuffle(QUESTIONS.slice()).slice(0, count).map(q => {
    const ix = [0,1,2,3]; shuffle(ix);
    return { q: q.q, opts: ix.map(i => q.opts[i]), ans: ix.indexOf(q.ans), exp: q.exp, src: q.src, sec: q.sec };
  });
  S.idx = 0; S.pending = undefined; S.answers = {}; S.marks = {}; S.visited = {};
  S.spent = new Array(S.qs.length).fill(0);
  S.t0 = Date.now();
  S.endAt = S.mode === 'exam' ? S.t0 + count * tpq * 1000 : 0;
  document.getElementById('startCard').style.display = 'none';
  document.getElementById('resultCard').style.display = 'none';
  document.getElementById('examRoot').style.display = '';
  document.getElementById('whoLine').innerHTML = '<b>' + esc(S.name) + '</b> &nbsp;|&nbsp; ' + (S.mode==='quiz'?'Quiz Mode':'Exam Mode');
  clearInterval(S.tick);
  S.tick = setInterval(tickTimer, 500);
  tickTimer();
  renderTabs(); renderPalette(); renderQ();
}
function tickTimer() {
  const el = document.getElementById('timerLine');
  if (S.mode === 'exam') {
    const left = Math.round((S.endAt - Date.now())/1000);
    el.textContent = fmt(left);
    el.className = 'val' + (left <= 60 ? ' low' : '');
    if (left <= 0) { clearInterval(S.tick); submitTest(true); }
  } else {
    el.textContent = fmt(Math.floor((Date.now()-S.t0)/1000));
    el.className = 'val';
  }
}

/* ---------- language / zoom / palette toggle / fullscreen ---------- */
function toggleLang() {
  S.lang = S.lang === 'both' ? 'en' : (S.lang === 'en' ? 'hi' : 'both');
  document.getElementById('langBtn').textContent =
    S.lang === 'en' ? 'Language: English' : (S.lang === 'hi' ? 'Language: Hindi' : 'Language: Both');
  renderQ();
}
function zoom(d) {
  const b = document.body;
  let z = parseFloat(b.style.fontSize || '15');
  z = Math.min(22, Math.max(12, z + d));
  b.style.fontSize = z + 'px';
}
function togglePalette() {
  S.palHidden = !S.palHidden;
  document.getElementById('palettePanel').classList.toggle('hidden', S.palHidden);
  document.getElementById('palToggle').textContent = S.palHidden ? '«' : '»';
  document.getElementById('palToggle').title = S.palHidden ? 'Palette dikhayein' : 'Palette chhupayein';
}
function toggleFull() {
  if (!document.fullscreenElement) document.documentElement.requestFullscreen && document.documentElement.requestFullscreen();
  else document.exitFullscreen && document.exitFullscreen();
}

/* ---------- sections ---------- */
function sectionList() {
  const out = [];
  S.qs.forEach((q,i) => { if (out.indexOf(q.sec) === -1) out.push(q.sec); });
  return out;
}
function renderTabs() {
  const b = document.getElementById('secTabs'); b.innerHTML = '';
  sectionList().forEach(sec => {
    const t = document.createElement('div');
    t.className = 'stab' + (S.qs[S.idx] && S.qs[S.idx].sec === sec ? ' cur' : '');
    t.textContent = sec;
    t.onclick = () => {
      const first = S.qs.findIndex(q => q.sec === sec);
      if (first >= 0) { saveTime(false); S.idx = first; S.pending = undefined; renderQ(); }
    };
    b.appendChild(t);
  });
}

/* ---------- palette ---------- */
function paletteClass(i) {
  if (S.marks[i]) return (S.answers[i] !== undefined) ? 'pq mkans' : 'pq mk';
  if (S.answers[i] !== undefined) return 'pq ans';
  if (S.visited[i]) return 'pq vis';
  return 'pq nv';
}
function renderPalette() {
  const b = document.getElementById('dotBox'); b.innerHTML = '';
  S.qs.forEach((q,i) => {
    const d = document.createElement('button');
    d.className = paletteClass(i) + (i === S.idx ? ' cur' : '');
    d.textContent = i+1;
    d.onclick = () => { saveTime(false); S.idx = i; S.pending = undefined; renderQ(); };
    b.appendChild(d);
  });
  let ans=0, mk=0, ma=0, vis=0;
  S.qs.forEach((q,i) => {
    if (S.answers[i] !== undefined) ans++;
    if (S.marks[i]) { if (S.answers[i] !== undefined) ma++; else mk++; }
    if (S.visited[i]) vis++;
  });
  const notAns = Math.max(0, vis - ans);
  const notVis = S.qs.length - vis;
  document.getElementById('sumAns').textContent = ans;
  document.getElementById('sumNotAns').textContent = notAns;
  document.getElementById('sumMk').textContent = mk;
  document.getElementById('sumMa').textContent = ma;
  document.getElementById('sumNv').textContent = notVis;
  document.getElementById('topAns').textContent = 'Answered: ' + ans + ' / ' + S.qs.length;
}

/* ---------- question render ---------- */
function saveTime() {
  const now = Date.now();
  if (S.enter) S.spent[S.idx] += (now - S.enter)/1000;
  S.enter = now;
}
function renderQ() {
  const q = S.qs[S.idx];
  S.visited[S.idx] = true;
  S.enter = Date.now();
  document.getElementById('qNoLine').innerHTML = '<span class="qno">Question ' + (S.idx+1) + ' of ' + S.qs.length + '</span>';
  document.getElementById('secLine').textContent = q.sec;
  const showEN = (S.lang === 'en' || S.lang === 'both');
  const showHI = (S.lang === 'hi' || S.lang === 'both');
  document.getElementById('qText').innerHTML = showEN ? esc(q.q[0]) : '';
  document.getElementById('qHi').style.display = (showHI && q.q[1]) ? '' : 'none';
  document.getElementById('qHi').textContent = q.q[1] || '';
  const box = document.getElementById('optBox'); box.innerHTML = '';
  const curSel = (S.pending !== undefined) ? S.pending : S.answers[S.idx];
  q.opts.forEach((o,i) => {
    const lab = document.createElement('label');
    lab.className = 'optrow' + (curSel === i ? ' sel' : '');
    const hin = (o[1] && o[1].toLowerCase() !== o[0].toLowerCase()) ?
      (showHI ? ' <span class="oh">/ ' + esc(o[1]) + '</span>' : '') : '';
    const txt = showEN ? esc(o[0]) + hin : (o[1] ? esc(o[1]) : esc(o[0]));
    lab.innerHTML = '<input type="radio" name="qopt"' + (curSel === i ? ' checked' : '') + '>' +
      '<span class="oidx">(' + L[i] + ')</span><span class="otext">' + txt + '</span>';
    lab.onclick = () => onPick(i);
    box.appendChild(lab);
  });
  document.getElementById('fbBox').innerHTML = '';
  renderTabs(); renderPalette();
}
function onPick(i) {
  if (S.mode === 'exam') {
    S.pending = i;
    renderQ();
  } else {
    if (S.answers[S.idx] !== undefined) return;
    S.answers[S.idx] = i;
    showFeedback(i);
    renderPalette();
  }
}

/* ---------- exam actions (TCS iON behaviour) ---------- */
function clearResp() { S.pending = undefined; delete S.answers[S.idx]; renderQ(); }
function markNext() {
  if (S.pending !== undefined) S.answers[S.idx] = S.pending;
  S.pending = undefined;
  S.marks[S.idx] = true;
  saveTime();
  nextQ();
}
function saveNext() {
  if (S.pending !== undefined) S.answers[S.idx] = S.pending;
  S.pending = undefined;
  saveTime();
  nextQ();
}
function sectionEndNext() {
  /* TCS iON: last question of a section -> first question of next section */
  const sec = S.qs[S.idx].sec;
  let n = -1;
  for (let i = S.idx+1; i < S.qs.length; i++) if (S.qs[i].sec !== sec) { n = i; break; }
  return n;
}
function nextQ() {
  let n = sectionEndNext();
  if (n === -1) n = Math.min(S.idx+1, S.qs.length-1);
  S.idx = n;
  renderQ();
}
function moveQ(d) {
  saveTime(false);
  const n = S.idx + d;
  if (n < 0 || n >= S.qs.length) return;
  S.idx = n; S.pending = undefined;
  renderQ();
}

/* ---------- quiz feedback ---------- */
function showFeedback(picked) {
  const q = S.qs[S.idx];
  const ok = picked === q.ans;
  document.querySelectorAll('#optBox .optrow').forEach((el,k) => {
    if (k === q.ans) el.classList.add('correct');
    else if (k === picked) el.classList.add('wrong');
    else el.classList.add('dim');
  });
  document.getElementById('fbBox').innerHTML =
    '<div class="fb ' + (ok ? 'ok' : 'no') + '">' +
    (ok ? '<b>Sahi uttar.</b>' : '<b>Galat uttar.</b> Sahi uttar: <b>(' + L[q.ans] + ') ' + esc(q.opts[q.ans][0]) + '</b>') +
    '<div class="exp"><b>Explanation:</b> ' + esc(q.exp[0] || '') + (q.exp[1] ? '<div class="hi">' + esc(q.exp[1]) + '</div>' : '') + '</div>' +
    '<div class="src">Source: ' + esc(q.src) + '</div></div>';
  const cb = document.getElementById('quizNav');
  cb.innerHTML = '';
  const b = document.createElement('button'); b.className = 'abtn next';
  b.innerHTML = S.idx < S.qs.length-1 ? 'Agla Question  »' : 'Result Dekhein  »';
  b.onclick = () => { saveTime(false); if (S.idx < S.qs.length-1) { S.idx++; renderQ(); } else submitTest(false); };
  cb.appendChild(b);
}

/* ---------- submit + analysis ---------- */
function submitTest(auto) {
  saveTime(false);
  if (S.pending !== undefined) S.answers[S.idx] = S.pending;
  const a = Object.keys(S.answers).length;
  const un = S.qs.length - a;
  if (!auto && un > 0 && !confirm(un + ' questions ka uttar save nahi hua hai (ye SKIPPED gine jayenge, galat nahi). Submit karein?')) return;
  if (!auto && un === 0 && !confirm('Saare questions answered hain. Submit karein?')) return;
  clearInterval(S.tick);
  const secs = Math.floor((Date.now()-S.t0)/1000);
  let correct = 0, wrong = 0;
  S.qs.forEach((q,i) => {
    if (S.answers[i] === undefined) return;
    if (S.answers[i] === q.ans) correct++; else wrong++;
  });
  const skipped = S.qs.length - correct - wrong;
  const attempted = correct + wrong;
  const acc = attempted ? Math.round(correct*100/attempted) : 0;
  const avgT = attempted ? (secs/attempted).toFixed(1) : '—';
  let slow = 0;
  S.spent.forEach((t,i) => { if (t > S.spent[slow]) slow = i; });
  document.getElementById('examRoot').style.display = 'none';
  document.getElementById('resultCard').style.display = '';
  document.getElementById('resTitle').textContent = S.name + ' — ' + (S.mode==='quiz'?'Quiz Mode':'Exam Mode') + ' Result';
  document.getElementById('resSub').innerHTML = 'Topic __N__: __TITLE__ • Questions: ' + S.qs.length + ' • Unattempted questions ko SKIPPED mana gaya hai (galat nahi).';
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
    '<tr><th>Candidate</th><td>' + esc(S.name) + '</td><th>Mode</th><td>' + (S.mode==='quiz'?'Quiz':'Exam') + '</td></tr>' +
    '<tr><th>Total Questions</th><td>' + S.qs.length + '</td><th>Attempted</th><td>' + attempted + '</td></tr>' +
    '<tr><th>Correct / Wrong</th><td>' + correct + ' / ' + wrong + '</td><th>Skipped (chhode hue)</th><td>' + skipped + '</td></tr>' +
    '<tr><th>Accuracy</th><td>' + acc + '% (attempted par)</td><th>Marked for review</th><td>' + marked + '</td></tr>' +
    '<tr><th>Time taken</th><td>' + fmt(secs) + '</td><th>Avg time/question</th><td>' + avgT + 's</td></tr>';
  const rb = document.getElementById('revBox'); rb.innerHTML = '';
  S.qs.forEach((q,i) => {
    const picked = S.answers[i];
    let chip, line;
    if (picked === undefined) {
      chip = '<span class="st s">CHHODA (SKIPPED)</span>';
      line = '<div class="line">Is question ka uttar save nahi hua.</div>';
    } else if (picked === q.ans) {
      chip = '<span class="st c">SAHI</span>';
      line = '<div class="line"><span class="okc">Aapka uttar: (' + L[picked] + ') ' + esc(q.opts[picked][0]) + '</span></div>';
    } else {
      chip = '<span class="st w">GALAT</span>';
      line = '<div class="line"><span class="noc">Aapka uttar: (' + L[picked] + ') ' + esc(q.opts[picked][0]) + '</span></div>' +
             '<div class="line"><span class="okc">Sahi uttar: (' + L[q.ans] + ') ' + esc(q.opts[q.ans][0]) + '</span></div>';
    }
    const div = document.createElement('div');
    div.className = 'rev';
    div.innerHTML = chip + (S.marks[i] ? '<span class="st" style="background:#c6aeee;color:#2f1a5e;border:1px solid #8a63c9">MARKED</span>' : '') +
      '<div class="qh">Q' + (i+1) + '. ' + esc(q.q[0]) + '</div>' +
      '<div class="qhm">' + esc(q.q[1] || '') + '</div>' +
      q.opts.map((o,k) => '<div class="line">' + (k === q.ans ? '<span class="okc">(' + L[k] + ') ' + esc(o[0]) + '</span>' : '(' + L[k] + ') ' + esc(o[0])) + '</div>').join('') +
      line +
      '<div class="exp"><b>Explanation:</b> ' + esc(q.exp[0] || '—') + (q.exp[1] ? '<div class="hi">' + esc(q.exp[1]) + '</div>' : '') + '</div>' +
      '<div class="meta">Samay: ' + (S.spent[i] || 0).toFixed(0) + ' second &nbsp;|&nbsp; Source: ' + esc(q.src) + ' &nbsp;|&nbsp; ' + esc(q.sec) + '</div>';
    rb.appendChild(div);
  });
  window.scrollTo({top:0,behavior:'smooth'});
}
document.getElementById('nameIn').addEventListener('keyup', e => { if (e.key === 'Enter') startTest(); });
"""

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EkGuru Online Test — Topic __N__: __TITLE__</title>
<style>__CSS__</style>
</head>
<body>

<div id="examRoot" style="display:none">
  <div class="topbar">
    <div class="brand"><span class="e">Ek</span><span class="g">Guru</span><small>ONLINE TEST PORTAL</small></div>
    <div class="testname">Topic __N__ — __TITLE__<br><span id="whoLine"></span></div>
    <div class="topp">
      <div class="tbox"><div class="lbl">ANSWERED</div><div class="val" id="topAns" style="font-size:12px; letter-spacing:0">—</div></div>
      <div class="tbox"><div class="lbl">TIME LEFT</div><div class="val" id="timerLine">00:00</div></div>
      <button class="tbtn" id="langBtn" onclick="toggleLang()">Language: Both</button>
      <button class="tbtn" onclick="zoom(1)">A+</button>
      <button class="tbtn" onclick="zoom(-1)">A-</button>
      <button class="tbtn" onclick="toggleFull()">Full Screen</button>
    </div>
  </div>
  <div class="secbar" id="secTabs"></div>
  <button class="palToggle" id="palToggle" onclick="togglePalette()" title="Palette chhupayein/dikhayein">&#187;</button>
  <div class="layout">
    <div class="qcol">
      <div class="qpanel">
        <div class="qhead">
          <span id="qNoLine"></span>
          <span id="secLine"></span>
          <span class="langsel">
            <button id="langE" onclick="setLang('en')">English</button>
            <button id="langH" onclick="setLang('hi')">Hindi</button>
            <button id="langB" onclick="setLang('both')" class="on">Both</button>
          </span>
        </div>
        <div class="actionbar">
          <button class="abtn clear" onclick="clearResp()">Clear Response</button>
          <button class="abtn prev" onclick="moveQ(-1)">« Previous</button>
          <button class="abtn mark" onclick="markNext()">Mark for Review &amp; Next</button>
          <button class="abtn save" onclick="saveNext()">Save &amp; Next &#187;</button>
          <span id="quizNav" style="display:flex; gap:7px;"></span>
        </div>
        <div class="qbody">
          <div class="qtext" id="qText"></div>
          <div class="qhi" id="qHi"></div>
          <div id="optBox"></div>
        </div>
        <div id="fbBox"></div>
        <div class="note" id="noteLine">Exam Mode: option chunne ke baad jawab "Save &amp; Next" dabakar hi save hota hai (live exam jaisa). Palette jump jawab save nahi karta.</div>
      </div>
    </div>
    <aside class="pcol" id="palettePanel">
      <div class="ppanel">
        <div class="ptitle">QUESTION PALETTE</div>
        <div class="legend">
          <div class="row"><span class="sw nv"></span> Aapne question nahi dekha (Not Visited)</div>
          <div class="row"><span class="sw vis"></span> Dekha, uttar nahi diya (Not Answered)</div>
          <div class="row"><span class="sw ans"></span> Uttar diya (Answered)</div>
          <div class="row"><span class="sw mk"></span> Marked for Review</div>
          <div class="row"><span class="sw ma"></span> Answered &amp; Marked (evaluation ke liye mana jayega)</div>
        </div>
        <div class="palette" id="dotBox"></div>
        <div class="sumtitle">SECTION SUMMARY</div>
        <table class="sumtab">
          <tr><td>Answered</td><td class="n" id="sumAns">0</td></tr>
          <tr><td>Not Answered (dekhe hue)</td><td class="n" id="sumNotAns">0</td></tr>
          <tr><td>Marked for Review</td><td class="n" id="sumMk">0</td></tr>
          <tr><td>Answered &amp; Marked</td><td class="n" id="sumMa">0</td></tr>
          <tr><td>Not Visited</td><td class="n" id="sumNv">0</td></tr>
        </table>
        <div class="submitwrap"><button class="submitbtn" onclick="submitTest(false)">Submit Test</button></div>
      </div>
    </aside>
  </div>
  <div class="foot"><b>EkGuru Learning</b> — Compiled &amp; updated by <b>PRAKASH</b> | Reference: Forouzan + India-level PYQ banks (2011–2026)</div>
</div>

<div class="overlay" id="startCard">
  <div class="sheet">
    <h2>Test Instructions</h2>
    <ol class="ins">
      <li>Apna naam likhein, mode chunein aur <b>Test Shuru Karein</b> dabayein.</li>
      <li><b>Quiz Mode:</b> har question par uttar chunte hi sahi/galat + explanation turant dikhta hai (seekhne ke liye).</li>
      <li><b>Exam Mode:</b> live exam jaisa — option chunne ke baad <b>Save &amp; Next</b> dabakar jawab save karein. Sirf option chunne se jawab save nahi hota.</li>
      <li><b>Clear Response</b> — chuna hua jawab hataata hai. <b>Mark for Review &amp; Next</b> — baad mein dekhne ke liye mark karta hai.</li>
      <li><b>Question Palette</b> (dayiin taraf): har question ka rang batata hai ki uska kya status hai. Neeche <b>Section Summary</b> bhi hai.</li>
      <li>Upar <b>section tabs</b> se kisi bhi section mein ja sakte hain. <b>Language</b> button se English/Hindi/Both kar sakte hain. <b>A+/A-</b> se text bada-chhota.</li>
      <li>Samay poora hone par test apne aap submit hoga.</li>
      <li>Submit ke baad <b>Correct / Wrong / Chhode hue</b> alag gine jayenge; unattempted questions galat nahi gine jaate.</li>
      <li>Result ke baad <b>har question ka explanation</b> (solution) diya jayega.</li>
      <li>Questions aur options har baar kram badal kar aate hain.</li>
    </ol>
    <div class="fld"><label>Apka naam / Candidate name</label>
      <input type="text" id="nameIn" maxlength="40" placeholder="Naam likhein"></div>
    <div style="display:flex; gap:10px; flex-wrap:wrap">
      <div class="fld" style="flex:1; min-width:180px"><label>Mode</label>
        <select id="modeIn">
          <option value="quiz">Quiz Mode — instant answer + explanation</option>
          <option value="exam">Exam Mode — live CBT style</option>
        </select></div>
      <div class="fld" style="flex:1; min-width:150px"><label>Questions</label>
        <select id="countIn">
          <option value="10">10</option>
          <option value="25">25</option>
          <option value="50">50</option>
          <option value="0">Sabhi (__COUNT__)</option>
        </select></div>
      <div class="fld" style="flex:1; min-width:170px"><label>Har question ka samay (Exam)</label>
        <select id="tpqIn">
          <option value="45">45 second</option>
          <option value="60" selected>60 second</option>
          <option value="90">90 second</option>
          <option value="120">2 minute</option>
        </select></div>
    </div>
    <div class="chkline"><input type="checkbox" id="agreeIn"> <label for="agreeIn" style="display:inline">Maine instructions padh li hain.</label></div>
    <button class="btn prime" onclick="startTest()">Test Shuru Karein</button>
    <div class="hint">Questions: repo exam papers + Forouzan + India-level PYQ banks (GATE, UGC NET, RPSC, KVS, EMRS, SSC, RRB, IBPS — 2011–2026) + original practice set. Sabhi uttar verify kiye gaye hain.</div>
  </div>
</div>

<div id="resultCard" style="display:none">
  <div class="resWrap">
    <h2 style="font-size:18px; color:#16283f; border-bottom:2.5px solid #E97313; display:inline-block; padding-bottom:5px; margin-bottom:10px;">Result &amp; Analysis</h2>
    <div class="resTitle" id="resTitle"></div>
    <div class="hint" id="resSub"></div>
    <div class="statgrid" id="statGrid"></div>
    <table class="tt" id="resTable"></table>
    <div class="btnrow">
      <button class="btn blue" onclick="window.print()">Print / Save Result</button>
      <button class="btn ghost" onclick="location.reload()">Naya Test</button>
    </div>
    <h2 style="font-size:18px; color:#16283f; border-bottom:2.5px solid #E97313; display:inline-block; padding-bottom:5px; margin:20px 0 10px;">Question-wise Solutions</h2>
    <div id="revBox"></div>
  </div>
  <div class="foot"><b>EkGuru Learning</b> — Compiled &amp; updated by <b>PRAKASH</b> | Topic __N__: __TITLE__</div>
</div>

<script>__JS__</script>
</body>
</html>
"""


def build_html(n, items):
    js = JS.replace("__DATA__", json.dumps(items, ensure_ascii=False).replace("</", "<\\/"))
    html = (HTML.replace("__CSS__", CSS)
                .replace("__JS__", js)
                .replace("__N__", str(n))
                .replace("__TITLE__", TOPICS[n])
                .replace("__COUNT__", str(len(items))))
    # per-question language buttons need setLang()
    html = html.replace("function toggleLang() {",
        "function setLang(v) {\n"
        "  S.lang = v;\n"
        "  document.getElementById('langE').classList.toggle('on', v==='en');\n"
        "  document.getElementById('langH').classList.toggle('on', v==='hi');\n"
        "  document.getElementById('langB').classList.toggle('on', v==='both');\n"
        "  document.getElementById('langBtn').textContent = v==='en'?'Language: English':(v==='hi'?'Language: Hindi':'Language: Both');\n"
        "  renderQ();\n"
        "}\n"
        "function toggleLang() {")
    return html


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
