#!/usr/bin/env python3
"""Exit 0 if the active feature's spec.md has the expected status, else 1.

Usage: python3 spec_status.py --expect accepted [--feature <dir>]
Reads .specify/feature.json when --feature is not given. Prints the status found.
"""
import json, re, sys
from pathlib import Path

args = sys.argv[1:]
expect = args[args.index("--expect") + 1] if "--expect" in args else "accepted"
feature = args[args.index("--feature") + 1] if "--feature" in args else json.load(open(".specify/feature.json"))["feature_directory"]
text = Path(feature, "spec.md").read_text(encoding="utf-8")
m = re.search(r"\|\s*\*\*Status\*\*\s*\|\s*([a-z-]+)\s*\|", text)
status = m.group(1) if m else "unknown"
print(status, end="")
sys.exit(0 if status == expect else 1)
