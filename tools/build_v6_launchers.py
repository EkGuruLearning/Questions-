#!/usr/bin/env python3
"""Create versioned topic launchers without touching the legacy quiz pages."""
from __future__ import annotations
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "Computer Network/Online Quiz/v6"
TOPICS = {
    "T01": "Introduction of Data Communication",
    "T02": "Network Models (OSI & TCP/IP)",
    "T03": "Addressing (MAC, IPv4, IPv6, Port, DNS)",
    "T04": "Networking Devices",
    "T05": "Transmission Medium",
    "T06": "OSI Layers in Detail",
    "T07": "Network Security",
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for topic_id, name in TOPICS.items():
        number = int(topic_id[1:])
        # Each versioned route is a same-tab launcher into the shared practice app.
        target = f"../../../practice/index.html?subject=cn&topic={topic_id}&mode=practice#practice"
        # Build the query with JS as well, so the fallback and redirect stay in sync.
        fallback = html.escape(target, quote=True)
        document = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <meta name="theme-color" content="#16283f">
  <title>EkGuru Computer Networks — Topic {number} practice</title>
  <style>
    :root {{ color-scheme: light; font-family: system-ui, sans-serif; background: #f2f5f9; color: #17253a; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; min-height: 100vh; display: grid; place-items: center; padding: 1rem; }}
    main {{ max-width: 38rem; width: 100%; padding: clamp(1.25rem, 5vw, 2.5rem); background: #fff; border: 1px solid #d7dee8; border-radius: 1rem; box-shadow: 0 12px 36px #16283f18; }}
    h1 {{ margin: .35rem 0 .75rem; font-size: clamp(1.5rem, 5vw, 2.2rem); }}
    .brand {{ color: #b75000; font-weight: 800; letter-spacing: .05em; }}
    p {{ line-height: 1.65; }}
    a {{ color: #154d94; font-weight: 700; }}
    .notice {{ padding: .9rem 1rem; border-left: 4px solid #e97313; background: #fff7ed; border-radius: .35rem; }}
    .fallback {{ display: inline-flex; align-items: center; min-height: 44px; margin-top: .5rem; padding: .65rem 1rem; border-radius: .5rem; background: #16283f; color: #fff; text-decoration: none; }}
  </style>
</head>
<body>
  <main>
    <div class="brand">EkGuru Learning</div>
    <h1>Topic {number}: {html.escape(name)}</h1>
    <p>This versioned link opens the shared, source-labelled Computer Network practice portal in this tab. It does not use the older standalone quiz snapshot.</p>
    <p class="notice" role="status">Opening the shared portal… If it does not open automatically, use the button below.</p>
    <a class="fallback" id="openPortal" href="{fallback}">Open Topic {number} practice</a>
  </main>
  <script>
    (function () {{
      var target = new URL("../../../practice/index.html", window.location.href);
      target.searchParams.set("subject", "cn");
      target.searchParams.set("topic", "{topic_id}");
      target.searchParams.set("mode", "practice");
      document.getElementById("openPortal").href = target.href;
      window.location.replace(target.href);
    }}());
  </script>
</body>
</html>
'''
        name_out = f"Topic {number} - EkGuru v6 CBT.html"
        (OUT / name_out).write_text(document, encoding="utf-8")
    print(f"Created {len(TOPICS)} versioned launchers under {OUT.relative_to(ROOT)}; legacy pages untouched.")


if __name__ == "__main__":
    main()
