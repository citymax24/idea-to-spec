# Command reference

All commands are Claude Code skills installed by the `idea` extension. They resolve the active feature from `.specify/feature.json` unless `--feature <specs/NNN-dir>` is given. `--headless` tells a command it cannot ask anything and must leave markers or statuses in the files instead (workflow runs pass it on every step).

| Command | Arguments | Reads | Writes |
|---------|-----------|-------|--------|
| `/speckit-idea-intake` | `<folder or files> [--name <slug>] [--feature <dir>] [--headless]` | the given files, `.specify/init-options.json` | `specs/<NNN>-<slug>/inputs/raw/`, `inputs/extracted/S<n>-*.md`, `inputs/INVENTORY.md`, `.specify/feature.json` |
| `/speckit-idea-facts` | `[--feature <dir>] [--headless]` | `inputs/extracted/`, `inputs/INVENTORY.md`, `decisions/` | `analysis/facts.md`, `analysis/conflicts.md`, `analysis/open-questions.md` |
| `/speckit-idea-draft` | `[--name "<Idea name>"] [--feature <dir>] [--headless]` | `analysis/`, `decisions/`, `.specify/memory/constitution.md`, resolved `spec-template` | `spec.md` v0.1, `CHANGELOG.md`, `checklists/requirements.md`, git commit + tag `spec-<slug>-v0.1` |
| `/speckit-idea-publish` | `[--feature <dir>] [--headless]` | `spec.md` | `feedback/spec-review.html`, `feedback/spec-v<x.y>.html`, `feedback/PUBLISHED.md`, artifact page when a publishing tool exists |
| `/speckit-idea-feedback` | `[--from-comments] [--file <path>] [--inbox] [--reviewer <name>] [--feature <dir>] [--headless] [free text]` | `spec.md`, `feedback/PUBLISHED.md`, `feedback/inbox.txt`, page comments | `feedback/R<n>.md` (items `proposed`, then `confirmed` after the reviewer confirms) |
| `/speckit-idea-apply` | `[R<n>] [--gate-confirmed <run_id>] [--feature <dir>] [--headless]` | `feedback/R<n>.md`, `spec.md`, `CHANGELOG.md`, `decisions/`, `analysis/` | `spec.md` v0.x+1, `CHANGELOG.md` block, `decisions/DEC-<nnn>.md`, updated round file and checklist, git commit + tag |
| `/speckit-idea-accept` | `[--approved-by <name>] [--feature <dir>] [--headless]` | `spec.md`, `feedback/R*.md`, `CHANGELOG.md`, `decisions/` | `checklists/requirements.md`; on approval the header (`accepted`, name, date, v1.0 on first acceptance), changelog block, commit + tag |
| `/speckit-idea-brief` | `[--draft] [--feature <dir>] [--headless]` | `spec.md` (status `accepted` unless `--draft`) | `design/brief.md`, `design/README.md`, hand-off to the `design` skill |

## Scripts used by the commands

| Script | Called by | Purpose |
|--------|-----------|---------|
| `.specify/extensions/idea/scripts/python/convert_inputs.py <FEATURE_DIR> [--json]` | intake | assign S-IDs, convert raw files to Markdown (markitdown; openpyxl via `uv run` for spreadsheets) |
| `.specify/extensions/idea/scripts/python/render_spec.py <spec.md> <out.html>` | publish | render the spec to a self-contained HTML page with anchors per heading and ID |
| `.specify/extensions/idea/scripts/python/spec_status.py --expect <status>` | workflow (`accepted-check`) | exit 0 when the active spec has the expected status |

## Workflow

`specify workflow run idea-to-spec -i inbox=<folder> -i name=<slug> -i reviewer=<name>` runs intake → gate (weights) → facts → gate (conflicts) → draft → publish → review loop [gate (revise/accept) → feedback `--inbox --from-comments` → gate (confirm round) → apply `--gate-confirmed` → publish] → accept → status check → brief. Resume a paused run with `specify workflow resume <run_id>`.
