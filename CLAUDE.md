# CLAUDE.md — idea-to-spec

Spec Kit 1.0 project. Turns mixed inputs into a cited spec through traceable human feedback rounds, binds it to the project standards, then builds a clickable prototype from it. Read `docs/process/idea-to-spec-process.md` before changing commands or templates.

## Layout

- `presets/idea-to-spec/` — spec template (installed copy lives in `.specify/presets/`)
- `extensions/idea/` — commands, templates, scripts (installed copy in `.specify/extensions/idea/`, skills in `.claude/skills/speckit-idea-*`)
- `standards/` — project-wide rules bound into every idea: one directory per module (`standard.yml`, `rules.md`, `CHANGELOG.md`, optional `assets/`). Repo content, not tooling; not installed into `.specify/`. Optional — without it every standards step is skipped
- `workflows/idea-to-spec/workflow.yml` — the loop with gates
- `specs/<NNN>-<slug>/` — one idea: `inputs/`, `analysis/`, `spec.md`, `CHANGELOG.md`, `feedback/`, `decisions/` (`DEC-*`, `EXM-*`), `checklists/`, `standards/BOUND.md`, `prototype/`
- `docs/` — English only; process in `docs/process/`, how-tos in `docs/guides/`

## Rules that the commands enforce (do not weaken them)

1. Nothing without provenance: every JOB, FLOW, SCR, FR, SC and constraint line ends with `[S# loc]`, `[F-### · S# loc]`, `[C-## resolved]`, `[Q-## resolved]`, `[R#-##]` or `[ASSUMPTION: …]`.
2. Feedback is confirmed before it is applied. `/speckit-idea-feedback` never edits `spec.md`.
3. IDs are stable and never reused. Removed items become tombstones in §13 plus a `decisions/DEC-*.md`.
4. One round = one spec version = one commit + tag `spec-<slug>-v<x.y>` (slug = feature dir without numeric prefix; needs a git repo).
5. Only a human sets `accepted`, with name and date. First acceptance is v1.0; later re-acceptances keep the current version.
6. Prototype feedback has two lanes: `VISUAL` items stay in the prototype and never touch the spec; content or flow goes back through a feedback round.
7. After acceptance there is no design brief and no canvas. The only next step is `/speckit-idea-prototype`, or the human takes `spec.md` into Claude Design alone.
8. Standards (`standards/`) are a third source of truth next to sources and feedback. A line tagged `[STD-… · v<x.y>]` cannot be removed by a feedback round — `/speckit-idea-apply` refuses it — only by a human-signed `decisions/EXM-*.md`. Authority decides conflicts: `law` > `contract` > `internal`. At acceptance a failed required rule of a `law` module blocks; internal modules warn. A `draft` module never reports `pass`. Never edit `standards/` from inside a feature. Details: `docs/process/standards.md`.

## Editing the preset or extension

Edit the sources under `presets/` and `extensions/`, then reinstall so the copies under `.specify/` and `.claude/skills/` update:

```bash
specify preset add --dev ./presets/idea-to-spec --priority 5
specify extension add --dev ./extensions/idea --force
specify workflow add ./workflows/idea-to-spec
```

Never edit the installed copies directly. Spec language is English; inputs may be in any language and are quoted verbatim.

## Installing elsewhere

A clone works as is: `.specify/` and `.claude/skills/` are committed and the registries hold no absolute paths. `bash scripts/setup.sh` installs the missing tools and repairs the registrations; `.devcontainer/` runs it automatically. Needs Claude Code, not a Claude-app project. Details: `docs/guides/install.md`.

## Tools

`specify` (uv tool), `markitdown` (uv tool), `python3`, `uv` (the converter re-runs itself under `uv run --with openpyxl` for spreadsheets), `git`.
