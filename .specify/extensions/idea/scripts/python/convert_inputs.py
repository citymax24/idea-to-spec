#!/usr/bin/env python3
"""Assign stable S-IDs to raw input files and convert them to Markdown.

Usage: python3 convert_inputs.py <FEATURE_DIR> [--json]

Reads  <FEATURE_DIR>/inputs/raw/*
Writes <FEATURE_DIR>/inputs/extracted/S<n>-<basename>.md
Never renumbers: existing IDs are read from inputs/INVENTORY.md and from
existing extracted file names. New files get the next free ID in sorted order.

Conversion:
  .md .txt .csv            copied (csv wrapped as a code block)
  .xlsx .xlsm              openpyxl if importable (sheet + real row numbers),
                           else markitdown CLI
  .pptx .docx .pdf .html   markitdown CLI (slide markers kept)
  audio (.m4a .mp3 .wav)   local transcriber if found (whisper / mlx_whisper),
                           else placeholder with status needs-agent
  images (.png .jpg .jpeg .webp .heic)  placeholder, status needs-agent
  anything else            markitdown CLI if available, else placeholder

Prints a JSON list with {id, file, kind, extracted, status} when --json is set.
Status: converted | copied | transcribed | needs-agent | failed | existing
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

AUDIO = {".m4a", ".mp3", ".wav", ".aac", ".ogg", ".flac"}
IMAGES = {".png", ".jpg", ".jpeg", ".webp", ".heic", ".gif", ".tiff"}
TEXT = {".md", ".txt", ".csv", ".markdown"}
MARKITDOWN = {".pptx", ".docx", ".pdf", ".html", ".htm", ".epub", ".json", ".xml", ".ipynb"}
SHEETS = {".xlsx", ".xlsm"}

KIND = {
    ".md": "notes", ".markdown": "notes", ".txt": "notes", ".csv": "spreadsheet",
    ".xlsx": "spreadsheet", ".xlsm": "spreadsheet", ".pptx": "slides", ".docx": "document",
    ".pdf": "document", ".html": "document", ".htm": "document",
}


def kind_of(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in AUDIO:
        return "audio"
    if ext in IMAGES:
        return "image"
    if ext in TEXT and re.search(r"transkript|transcript|protokoll|memo", path.stem, re.I):
        return "transcript"
    return KIND.get(ext, "other")


def which_markitdown() -> str | None:
    for candidate in ("markitdown", str(Path.home() / ".local" / "bin" / "markitdown")):
        found = shutil.which(candidate) or (candidate if Path(candidate).exists() else None)
        if found:
            return found
    return None


def run_markitdown(src: Path) -> str | None:
    exe = which_markitdown()
    if not exe:
        return None
    try:
        out = subprocess.run([exe, str(src)], capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if out.returncode != 0:
        return None
    return out.stdout


def _sheet_markdown_openpyxl(src: Path) -> str | None:
    try:
        import openpyxl  # type: ignore
    except ImportError:
        return None
    try:
        wb = openpyxl.load_workbook(src, data_only=True, read_only=True)
    except Exception:  # noqa: BLE001
        return None
    parts: list[str] = []
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue
        width = max(len(r) for r in rows)
        parts.append(f"## Sheet: {ws.title}\n")
        parts.append("Cite as `S<id> row <n> (sheet " + ws.title + ")` using the Row column (real sheet row numbers).\n")
        header = ["Row"] + [_cell(c) for c in rows[0]] + [""] * (width - len(rows[0]))
        parts.append("| " + " | ".join(header) + " |")
        parts.append("|" + "---|" * len(header))
        for i, r in enumerate(rows[1:], start=2):
            cells = [_cell(c) for c in r] + [""] * (width - len(r))
            if not any(cells):
                continue  # skip empty rows; row numbers stay real
            parts.append("| " + " | ".join([str(i)] + cells) + " |")
        parts.append("")
    return "\n".join(parts) if parts else None


def _cell(c) -> str:
    if c is None:
        return ""
    if isinstance(c, float) and c.is_integer():
        c = int(c)
    return str(c).replace("\n", " ").replace("|", "\\|")


def _sheet_markdown_via_uv(src: Path) -> str | None:
    """Re-run this script under `uv run --with openpyxl` when openpyxl is not importable."""
    uv = shutil.which("uv")
    if not uv or os.environ.get("IDEA_NO_UV"):
        return None
    try:
        out = subprocess.run([uv, "run", "--quiet", "--with", "openpyxl", "python3", str(Path(__file__).resolve()),
                              "--sheet", str(src)], capture_output=True, text=True, timeout=300,
                             env={**os.environ, "IDEA_NO_UV": "1"})
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout if out.returncode == 0 and out.stdout.strip() else None


def _clean_markitdown_table(md: str) -> str:
    """Fallback cleanup: drop pandas artefacts (NaN, 1.0) and number table lines (header = row 1)."""
    lines_out: list[str] = []
    row = 0
    for line in md.splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.match(r"^:?-{2,}:?$", c) for c in cells if c):
                lines_out.append("|---|" + "---|" * len(cells))
                continue
            row += 1
            cells = ["" if c == "NaN" else re.sub(r"^(-?\d+)\.0$", r"\1", c) for c in cells]
            if row > 1 and not any(cells):
                continue
            lines_out.append("| " + " | ".join([("Row" if row == 1 else str(row))] + cells) + " |")
        else:
            if line.startswith("## "):
                row = 0
                lines_out.append(line)
                lines_out.append("Cite as `S<id> row <n>` (table line; header = row 1).\n")
                continue
            lines_out.append(line)
    return "\n".join(lines_out)


def convert_sheet(src: Path) -> str | None:
    body = _sheet_markdown_openpyxl(src) or _sheet_markdown_via_uv(src)
    if body:
        return body
    md = run_markitdown(src)
    return _clean_markitdown_table(md) if md else None


def transcribe(src: Path) -> str | None:
    for exe in ("mlx_whisper", "whisper"):
        path = shutil.which(exe)
        if not path:
            continue
        try:
            out = subprocess.run([path, str(src), "--output-format", "txt", "--output-dir", str(src.parent / ".transcripts")],
                                 capture_output=True, text=True, timeout=1800)
        except (OSError, subprocess.TimeoutExpired):
            continue
        txt = src.parent / ".transcripts" / (src.stem + ".txt")
        if out.returncode == 0 and txt.exists():
            return txt.read_text(encoding="utf-8", errors="replace")
    return None


def existing_ids(feature: Path) -> dict[str, int]:
    """Map raw basename -> id from INVENTORY.md rows and extracted file names."""
    mapping: dict[str, int] = {}
    inv = feature / "inputs" / "INVENTORY.md"
    if inv.exists():
        for line in inv.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^\|\s*S(\d+)\s*\|\s*([^|]+?)\s*\|", line)
            if m:
                mapping[m.group(2).strip().strip("`")] = int(m.group(1))
    ext_dir = feature / "inputs" / "extracted"
    if ext_dir.exists():
        for f in ext_dir.glob("S*-*.md"):
            m = re.match(r"^S(\d+)-(.+)\.md$", f.name)
            if m:
                mapping.setdefault(m.group(2), int(m.group(1)))  # keyed by stem
    return mapping


def lookup_id(known: dict[str, int], src: Path) -> int | None:
    return known.get(src.name, known.get(src.stem))


def header(sid: int, src: Path, kind: str, cite: str) -> str:
    stamp = _dt.date.today().isoformat()
    return (f"# S{sid} · {src.name}\n\n"
            f"- **Kind**: {kind}\n- **Converted**: {stamp}\n- **Cite as**: {cite}\n\n---\n\n")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    if argv[1] == "--sheet" and len(argv) > 2:
        body = _sheet_markdown_openpyxl(Path(argv[2]))
        if body is None:
            return 1
        print(body)
        return 0
    feature = Path(argv[1]).resolve()
    as_json = "--json" in argv
    raw = feature / "inputs" / "raw"
    out_dir = feature / "inputs" / "extracted"
    if not raw.is_dir():
        print(json.dumps({"error": f"missing {raw}"}))
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)

    known = existing_ids(feature)
    next_id = (max(known.values()) + 1) if known else 1
    results = []
    files = sorted(p for p in raw.iterdir() if p.is_file() and not p.name.startswith("."))
    for src in files:
        base = src.name
        found = lookup_id(known, src)
        if found is not None:
            sid = found
            target = out_dir / f"S{sid}-{src.stem}.md"
            if target.exists():
                results.append({"id": f"S{sid}", "file": base, "kind": kind_of(src),
                                "extracted": str(target.relative_to(feature)), "status": "existing"})
                continue
        else:
            sid = next_id
            next_id += 1
            known[base] = sid
            known[src.stem] = sid
        target = out_dir / f"S{sid}-{src.stem}.md"
        kind = kind_of(src)
        ext = src.suffix.lower()
        status = "failed"
        body: str | None = None
        cite = f"S{sid} §<heading or paragraph>"
        try:
            if ext in TEXT:
                text = src.read_text(encoding="utf-8", errors="replace")
                body = f"```csv\n{text}\n```" if ext == ".csv" else text
                if ext == ".csv":
                    cite = f"S{sid} row <n>"
                elif kind == "transcript" or re.search(r"^\[?\d{1,2}:\d{2}", text, re.M):
                    kind = "transcript"
                    cite = f"S{sid} mm:ss (timestamp)"
                else:
                    cite = f"S{sid} §<heading> or S{sid} para <n>"
                status = "copied"
            elif ext in SHEETS:
                body = convert_sheet(src)
                cite = f"S{sid} row <n> (sheet <name>); the Row column holds the row number"
                status = "converted" if body else "failed"
            elif ext == ".pptx":
                body = run_markitdown(src)
                cite = f"S{sid} slide <n>"
                status = "converted" if body else "failed"
            elif ext in MARKITDOWN:
                body = run_markitdown(src)
                cite = f"S{sid} p.<n> or S{sid} §<heading>"
                status = "converted" if body else "failed"
            elif ext in AUDIO:
                body = transcribe(src)
                cite = f"S{sid} mm:ss"
                if body:
                    status = "transcribed"
                else:
                    body = ("<!-- needs-agent: audio file without transcript. Ask the human for a transcript "
                            "or install a local transcriber (whisper / mlx_whisper). Do not invent content. -->\n")
                    status = "needs-agent"
            elif ext in IMAGES:
                body = ("<!-- needs-agent: image. Describe what the image shows and transcribe visible text. "
                        "Write only what is visible. -->\n")
                cite = f"S{sid} (image)"
                status = "needs-agent"
            else:
                body = run_markitdown(src)
                if body:
                    status = "converted"
                else:
                    body = "<!-- needs-agent: unsupported file type. Inspect the raw file and extract what you can. -->\n"
                    status = "needs-agent"
        except Exception as exc:  # noqa: BLE001
            body = f"<!-- failed: {exc} -->\n"
            status = "failed"
        target.write_text(header(sid, src, kind, cite) + (body or ""), encoding="utf-8")
        results.append({"id": f"S{sid}", "file": base, "kind": kind, "extracted": str(target.relative_to(feature)), "status": status})

    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            print(f"{r['id']:>4}  {r['status']:<12} {r['file']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
