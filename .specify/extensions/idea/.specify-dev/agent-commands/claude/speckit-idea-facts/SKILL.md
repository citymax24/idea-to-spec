---
name: speckit-idea-facts
description: Break every source into atomic, cited claims; surface conflicts between sources and open questions for the human before any spec is written.
compatibility: Requires spec-kit project structure with .specify/ directory
metadata:
  author: github-spec-kit
  source: idea:commands/speckit.idea.facts.md
---

## User Input

```text
$ARGUMENTS
```

Optional: `--feature <specs/NNN-dir>`. Otherwise the active feature from `.specify/feature.json` is used.

## Goal

Phase 2 of the idea-to-spec loop. The spec will cite these facts, so every claim needs one location. Conflicts between sources are decided by the human, never by you.

## Steps

1. **Resolve `FEATURE_DIR`** (argument, else `.specify/feature.json`). Require `inputs/INVENTORY.md` and at least one file in `inputs/extracted/`. If missing, stop: "Run `/speckit-idea-intake` first."

2. **Read closed decisions.** If `decisions/*.md` exist, read them. Content a decision excludes must not be rebuilt into the spec. Such claims still get extracted, but they are listed under "Superseded by decisions" in `facts.md`, not in the main table.

3. **Read every extracted source** in ID order, together with its inventory weight.

4. **Extract atomic claims.** One statement, one location. Location formats: `S2 slide 7` · `S3 row 12 (sheet Features)` · `S1 §3` (heading) or `S1 para 4` · `S4 07:40` · `S5 p.3`. Write the claim in English; keep a short verbatim quote in the source language. Do not merge two sources into one claim. Do not add anything the source does not say. Categories: `problem · user · job · scope · flow · screen · requirement · constraint · metric · market · other`.

5. **Write `analysis/facts.md`** from `.specify/extensions/idea/templates/facts-template.md`. IDs `F-001…` sequential. If the file exists, keep existing IDs and append new claims; never renumber.

6. **Write `analysis/conflicts.md`** from `conflicts-template.md`. Only real contradictions (two sources cannot both be true), not different levels of detail. Each row names both facts, what differs, the weights of the two sources, and a plain question the human can answer in one line. Keep existing rows and their resolutions.

7. **Write `analysis/open-questions.md`** from `open-questions-template.md`. Gaps no source fills and that the spec cannot leave open silently: target users, scope boundaries, devices, language, legal constraints, what happens on error. Each row names the spec section that will carry an assumption until answered and a suggested default.

8. **Ask the human.** If the session is interactive, present conflicts and open questions compactly (ID, one line, suggested default) and ask: answer now, or say `draft with assumptions`. Record answers in the `Resolution` column as `Resolved: <answer> (human, YYYY-MM-DD)`. Resolved rows can be cited in the spec as `[C-02 resolved]` or `[Q-03 resolved]`. If not interactive, leave `open` and move on.

9. **Report.** Counts (facts, conflicts, open questions, resolved), anything superseded by decisions, next command `/speckit-idea-draft`.

## Rules

- No claim without a location. No location, no fact.
- Do not resolve conflicts yourself. Do not pick the "better" source.
- Do not write any spec content here.