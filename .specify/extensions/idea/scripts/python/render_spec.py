#!/usr/bin/env python3
"""Render spec.md to a self-contained HTML page with anchors per heading and per ID.

Usage: python3 render_spec.py <spec.md> <out.html> [--title "Text"]

Small, dependency-free Markdown subset: headings, paragraphs, bullet and numbered
lists, pipe tables, fenced code, bold, italic, inline code, HTML comments removed.
Lines starting with an ID in bold (**FR-001**, **SCR-03**, **JOB-01**, **FLOW-01**,
**SC-001**, **A-01**, **Q-01**) get id="FR-001" so comments can point at them.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ID_RE = re.compile(r"\*\*((?:FR|SCR|JOB|FLOW|SC|A|Q|C|F|DEC)-\d+)\*\*")
HEAD_ID_RE = re.compile(r"^((?:SCR|FLOW)-\d+)")

CSS = """
:root{--ink:#1b2028;--muted:#5b6270;--line:#d9dcd6;--bg:#fbfbf8;--code:#f1f2ee;--accent:#0f6e6b}
@media (prefers-color-scheme: dark){:root{--ink:#e7e9ec;--muted:#b3b9c3;--line:#2c323b;--bg:#14171c;--code:#1c2027;--accent:#4fb8b2}}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,"IBM Plex Sans","Segoe UI",sans-serif}
main{max-width:860px;margin:0 auto;padding:40px 24px 96px}
h1{font-size:34px;line-height:1.1;margin:0 0 20px}h2{font-size:24px;margin:44px 0 12px;padding-top:12px;border-top:1px solid var(--line)}
h3{font-size:17px;margin:26px 0 8px}p{max-width:70ch}table{border-collapse:collapse;width:100%;font-size:14px;margin:12px 0 20px}
th,td{text-align:left;vertical-align:top;padding:8px 10px 8px 0;border-bottom:1px solid var(--line)}th{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.06em}
code{font-family:ui-monospace,Menlo,monospace;font-size:.9em;background:var(--code);padding:1px 5px;border-radius:3px}
pre{background:var(--code);padding:14px 16px;overflow-x:auto;border:1px solid var(--line);border-radius:4px}pre code{background:none;padding:0}
li{margin-bottom:6px}li[id],p[id]{scroll-margin-top:16px}.tag{color:var(--accent);font-family:ui-monospace,monospace;font-size:.85em}
.toc{font-size:14px;color:var(--muted);columns:2;gap:24px}.toc a{color:inherit;text-decoration:none}.toc a:hover{text-decoration:underline}
.wrap{overflow-x:auto}
"""


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"(\[(?:S\d+|R\d+-\d+|F-\d+|C-\d+|Q-\d+|ASSUMPTION)[^\]]*\])", r'<span class="tag">\1</span>', text)
    text = re.sub(r"(⟲ v\d+\.\d+ · R\d+-\d+)", r'<span class="tag">\1</span>', text)
    return text


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def render(md: str, title: str | None) -> str:
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    lines = md.splitlines()
    out: list[str] = []
    toc: list[str] = []
    i = 0
    in_list: str | None = None
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if para:
            text = " ".join(para)
            m = ID_RE.match(text)
            attr = f' id="{m.group(1)}"' if m else ""
            out.append(f"<p{attr}>{inline(text)}</p>")
            para = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            out.append(f"</{in_list}>")
            in_list = None

    page_title = title
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush_para(); close_list()
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j]); j += 1
            out.append("<pre><code>" + html.escape("\n".join(buf)) + "</code></pre>")
            i = j + 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush_para(); close_list()
            level = len(m.group(1)); text = m.group(2).strip()
            hid = HEAD_ID_RE.match(text)
            anchor = hid.group(1) if hid else slug(text)
            if level == 1 and not page_title:
                page_title = re.sub(r"^Specification:\s*", "", text)
            if level == 2:
                toc.append(f'<a href="#{anchor}">{html.escape(text)}</a>')
            out.append(f'<h{level} id="{anchor}">{inline(text)}</h{level}>')
            i += 1
            continue
        if line.startswith("|"):
            flush_para(); close_list()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            body = [r for r in cells if not all(re.match(r"^:?-{2,}:?$", c) for c in r if c)]
            if not body:
                continue
            out.append('<div class="wrap"><table>')
            out.append("<tr>" + "".join(f"<th>{inline(c)}</th>" for c in body[0]) + "</tr>")
            for r in body[1:]:
                m2 = ID_RE.match(r[0]) if r else None
                attr = f' id="{m2.group(1)}"' if m2 else ""
                out.append(f"<tr{attr}>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</table></div>")
            continue
        m = re.match(r"^\s*([-*]|\d+\.)\s+(.*)$", line)
        if m:
            flush_para()
            kind = "ol" if m.group(1)[0].isdigit() else "ul"
            if in_list != kind:
                close_list(); out.append(f"<{kind}>"); in_list = kind
            text = m.group(2)
            m2 = ID_RE.match(text)
            attr = f' id="{m2.group(1)}"' if m2 else ""
            out.append(f"<li{attr}>{inline(text)}</li>")
            i += 1
            continue
        if not line.strip():
            flush_para(); close_list()
            i += 1
            continue
        if line.strip() == "---":
            flush_para(); close_list(); out.append("<hr>")
            i += 1
            continue
        para.append(line.strip())
        i += 1
    flush_para(); close_list()
    toc_html = f'<nav class="toc">{"".join(f"<div>{t}</div>" for t in toc)}</nav>' if toc else ""
    body = "\n".join(out)
    t = html.escape(page_title or "Specification")
    return (f"<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>{t}</title><style>{CSS}</style></head><body><main>{toc_html}{body}</main></body></html>")


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__); return 2
    src, dst = Path(argv[1]), Path(argv[2])
    title = None
    if "--title" in argv:
        title = argv[argv.index("--title") + 1]
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(render(src.read_text(encoding="utf-8"), title), encoding="utf-8")
    print(dst)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
