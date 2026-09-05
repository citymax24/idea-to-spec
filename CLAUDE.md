# CLAUDE.md — idea-to-spec

Spec Kit 1.0 project. Turns mixed inputs into a cited spec through traceable human feedback rounds, then into a design brief. Read `docs/process/idea-to-spec-process.md` before changing commands or templates.

## Layout

- `presets/idea-to-spec/` — spec template (installed copy lives in `.specify/presets/`)
- `extensions/idea/` — commands, templates, scripts (installed copy in `.specify/extensions/idea/`, skills in `.claude/skills/speckit-idea-*`)
- `workflows/idea-to-spec/workflow.yml` — the loop with gates
- `specs/<NNN>-<slug>/` — one idea: `inputs/`, `analysis/`, `spec.md`, `CHANGELOG.md`, `feedback/`, `decisions/`, `checklists/`, `design/`
- `docs/` — English only; process in `docs/process/`, how-tos in `docs/guides/`

## Rules that the commands enforce (do not weaken them)

1. Nothing without provenance: every JOB, FLOW, SCR, FR, SC and constraint line ends with `[S# loc]`, `[F-### · S# loc]`, `[C-## resolved]`, `[Q-## resolved]`, `[R#-##]` or `[ASSUMPTION: …]`.
2. Feedback is confirmed before it is applied. `/speckit-idea-feedback` never edits `spec.md`.
3. IDs are stable and never reused. Removed items become tombstones in §13 plus a `decisions/DEC-*.md`.
4. One round = one spec version = one commit + tag `spec-<slug>-v<x.y>` (slug = feature dir without numeric prefix; needs a git repo).
5. Only a human sets `accepted`, with name and date. First acceptance is v1.0; later re-acceptances keep the current version.
6. Mockup feedback has two lanes: visual stays in the canvas; content or flow goes back through a feedback round.

## Editing the preset or extension

Edit the sources under `presets/` and `extensions/`, then reinstall so the copies under `.specify/` and `.claude/skills/` update:

```bash
specify preset add --dev ./presets/idea-to-spec --priority 5
specify extension add --dev ./extensions/idea --force
specify workflow add ./workflows/idea-to-spec
```

Never edit the installed copies directly. Spec language is English; inputs may be in any language and are quoted verbatim.

## Tools

`specify` (uv tool), `markitdown` (uv tool), `python3`, `uv` (the converter re-runs itself under `uv run --with openpyxl` for spreadsheets), `git`.
