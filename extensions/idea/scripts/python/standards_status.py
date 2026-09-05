#!/usr/bin/env python3
"""Compare a feature's bound standard versions against the registry and report drift.

Usage:
  python3 standards_status.py [--feature <dir>] [--registry <dir>] [--json] [--strict]

Reads  <registry>/*/standard.yml            (default registry: ./standards)
       <FEATURE_DIR>/standards/BOUND.md     (the "Bound modules" table)
Prints a table, or JSON with --json.

Exit codes
  0  every non-retired module is bound at its current version
  1  drift: a bound module moved, or an applicable module was never bound
  2  no registry, or no binding yet (nothing to compare)

--strict makes exit 1 apply only to modules whose authority is "law"; internal
drift is still reported but does not change the exit code. That is the split the
acceptance checklist uses: law blocks, internal warns.

Scope is not evaluated here: `applies_to` is read and passed through in --json,
but deciding whether a module binds to a given idea is /speckit-idea-standards'
job, not arithmetic. This script answers one question only: did a bound module
move since the bind.

Version comparison is by dotted numeric components, so 0.9 < 0.10 < 1.0.
PyYAML is used when importable; otherwise the script re-runs itself under
`uv run --with pyyaml`, and failing that falls back to a flat-key reader that is
enough for the small, flat standard.yml shape.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# --------------------------------------------------------------------------- yaml


def _load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
    except ImportError:
        return _load_yaml_via_uv(path) or _load_yaml_flat(path)
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return _load_yaml_flat(path)


def _load_yaml_via_uv(path: Path) -> dict | None:
    """Re-run this script under `uv run --with pyyaml` when PyYAML is not importable."""
    uv = shutil.which("uv")
    if not uv or os.environ.get("IDEA_NO_UV"):
        return None
    try:
        out = subprocess.run(
            [uv, "run", "--quiet", "--with", "pyyaml", "python3", str(Path(__file__).resolve()),
             "--dump-yaml", str(path)],
            capture_output=True, text=True, timeout=120,
            env={**os.environ, "IDEA_NO_UV": "1"},
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if out.returncode != 0 or not out.stdout.strip():
        return None
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return None


def _load_yaml_flat(path: Path) -> dict:
    """Last resort: read `key: value` pairs two levels deep. Enough for standard.yml."""
    data: dict = {}
    section: dict | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        m = re.match(r"^(\S[^:]*):\s*(.*)$", raw)
        if m:
            key, val = m.group(1).strip(), m.group(2).strip()
            if val in ("", "|", ">-", ">", "|-"):
                section = {}
                data[key] = section
            else:
                data[key] = _scalar(val)
                section = None
            continue
        m = re.match(r"^\s+([^:#]+):\s*(.*)$", raw)
        if m and section is not None:
            section[m.group(1).strip()] = _scalar(m.group(2).strip())
    return data


def _scalar(v: str):
    v = v.strip().strip('"').strip("'")
    if v in ("null", "~", ""):
        return None
    if v == "true":
        return True
    if v == "false":
        return False
    return v


# --------------------------------------------------------------------------- versions


def _vkey(v) -> tuple:
    parts = re.findall(r"\d+", str(v or ""))
    return tuple(int(p) for p in parts) or (0,)


def _cmp(a, b) -> int:
    ka, kb = _vkey(a), _vkey(b)
    n = max(len(ka), len(kb))
    ka += (0,) * (n - len(ka))
    kb += (0,) * (n - len(kb))
    return (ka > kb) - (ka < kb)


# --------------------------------------------------------------------------- io


def read_registry(registry: Path) -> list[dict]:
    mods = []
    for yml in sorted(registry.glob("*/standard.yml")):
        raw = _load_yaml(yml)
        s = raw.get("standard") or {}
        mods.append({
            "id": s.get("id") or yml.parent.name,
            "prefix": s.get("prefix") or "?",
            "name": s.get("name") or yml.parent.name,
            "version": str(s.get("version") or "0"),
            "status": s.get("status") or "draft",
            "authority": s.get("authority") or "internal",
            "precedence": int(s.get("precedence") or 999),
            "applies_to": raw.get("applies_to") or "all",
            "dir": str(yml.parent),
        })
    mods.sort(key=lambda m: ({"law": 0, "contract": 1, "internal": 2}.get(m["authority"], 3), m["precedence"]))
    return mods


BOUND_ROW = re.compile(
    r"^\|\s*`?(STD-[A-Z0-9]+)`?\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", re.M)


def read_bound(feature: Path) -> dict[str, dict]:
    f = feature / "standards" / "BOUND.md"
    if not f.exists():
        return {}
    text = f.read_text(encoding="utf-8")
    start = text.find("## Bound modules")
    if start == -1:
        return {}
    block = text[start:]
    nxt = block.find("\n## ", 3)
    if nxt != -1:
        block = block[:nxt]
    out = {}
    for prefix, module, authority, version in BOUND_ROW.findall(block):
        version = version.strip().strip("[]")
        if not re.search(r"\d", version):
            continue
        out[prefix] = {"module": module.strip(), "authority": authority.strip(), "version": version}
    return out


# --------------------------------------------------------------------------- main


def main(argv: list[str]) -> int:
    if "--dump-yaml" in argv:                      # internal, used by the uv re-exec
        print(json.dumps(_load_yaml(Path(argv[argv.index("--dump-yaml") + 1]))))
        return 0

    root = Path.cwd()
    registry = Path(argv[argv.index("--registry") + 1]) if "--registry" in argv else root / "standards"
    if "--feature" in argv:
        feature = Path(argv[argv.index("--feature") + 1])
    else:
        try:
            feature = Path(json.load(open(".specify/feature.json"))["feature_directory"])
        except Exception:
            feature = None

    as_json = "--json" in argv
    strict_law_only = "--strict" in argv

    if not registry.is_dir():
        _out(as_json, {"status": "no-registry", "registry": str(registry), "modules": []},
             f"No standards registry at {registry}. Standards are optional; nothing to check.")
        return 2

    mods = read_registry(registry)
    if not mods:
        _out(as_json, {"status": "empty-registry", "modules": []}, f"Registry {registry} holds no modules.")
        return 2

    bound = read_bound(feature) if feature else {}
    rows, blocking, warning = [], 0, 0

    for m in mods:
        b = bound.get(m["prefix"])
        if m["status"] == "retired":
            state = "retired"
        elif not b:
            state = "never bound" if m["status"] == "active" else "not bound (module is a draft)"
        else:
            c = _cmp(b["version"], m["version"])
            state = "—" if c == 0 else ("MODULE MOVED" if c < 0 else "bound ahead of registry")
        drifting = state in ("never bound", "MODULE MOVED", "bound ahead of registry")
        if drifting:
            if m["authority"] == "law":
                blocking += 1
            else:
                warning += 1
        rows.append({**m, "bound_version": (b or {}).get("version"), "state": state, "drifting": drifting})

    if not bound:
        payload = {"status": "not-bound", "modules": rows, "blocking": blocking, "warning": warning}
        _out(as_json, payload, _table(rows, feature) +
             "\n\nNo binding yet. Run /speckit-idea-standards --bind.")
        return 2

    status = "ok" if not (blocking or warning) else "drift"
    payload = {"status": status, "modules": rows, "blocking": blocking, "warning": warning,
               "feature": str(feature)}
    _out(as_json, payload, _table(rows, feature) + _footer(blocking, warning))
    if blocking:
        return 1
    return 1 if (warning and not strict_law_only) else 0


def _table(rows: list[dict], feature) -> str:
    head = f"Standards for {feature}" if feature else "Standards"
    w = max([len(r["prefix"]) for r in rows] + [6])
    lines = [head, "",
             f"{'PREFIX'.ljust(w)}  {'AUTHORITY'.ljust(9)}  {'BOUND'.ljust(7)}  {'NOW'.ljust(7)}  STATE"]
    for r in rows:
        lines.append(f"{r['prefix'].ljust(w)}  {r['authority'].ljust(9)}  "
                     f"{str(r['bound_version'] or '—').ljust(7)}  {r['version'].ljust(7)}  {r['state']}")
    return "\n".join(lines)


def _footer(blocking: int, warning: int) -> str:
    if not blocking and not warning:
        return "\n\nNo drift."
    parts = []
    if blocking:
        parts.append(f"{blocking} law module(s) drifting — blocks acceptance")
    if warning:
        parts.append(f"{warning} internal module(s) drifting — warning")
    return "\n\n" + "; ".join(parts) + ".\nRun /speckit-idea-standards --bind to rebind, then re-accept."


def _out(as_json: bool, payload: dict, human: str) -> None:
    print(json.dumps(payload, indent=2) if as_json else human)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
