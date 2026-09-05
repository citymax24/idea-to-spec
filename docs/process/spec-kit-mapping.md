# How the process maps onto Spec Kit 1.0

Spec Kit 1.0.0 shipped on 2026-08-21; this project was built against 1.0.4. The table shows, per phase, what Spec Kit provides and what this repository adds.

| Phase | Spec Kit core | Community extension considered | What this repo adds |
|-------|---------------|--------------------------------|---------------------|
| Collect | — | `intake` (PRDs, PDFs, design images, Figma; no xlsx/pptx/audio listed) | `speckit.idea.intake` + `convert_inputs.py` (markitdown, openpyxl via uv, stable S-IDs, inventory with human weights) |
| Understand | `[NEEDS CLARIFICATION]` markers, max 3 | `keel` (interview evidence E-00x / A-00x) | `speckit.idea.facts`: atomic claims with locations, conflicts and open questions the human resolves |
| Draft | `/speckit-specify`, `spec-template.md` with FR-###, SC-###, P1–P3 stories | — | Preset `idea-to-spec`: template with JOB/FLOW/SCR sections, provenance tags, tombstones, acceptance header. `speckit.idea.draft` fills it from facts |
| Review: capture | `/speckit-clarify` (AI asks human, records Q→A under `## Clarifications`) | `taco` (offline HTML with anchored comments, no rounds or IDs) | `speckit.idea.publish` (HTML with anchors per ID, artifact page for comments) and `speckit.idea.feedback` (rounds, item IDs, types, confirmation step) |
| Review: apply | — | `changelog` (what changed per requirement from git, not why); `intent` (append-only decisions.md) | `speckit.idea.apply`: one version per round, change markers, tombstones, decision records, changelog rows naming the trigger |
| Standards | `.specify/memory/constitution.md` (one prose file, unversioned, no per-feature binding) | — | `standards/` registry: versioned modules with authority bands, stable rule IDs, per-idea binding with drift detection, signed exemptions. `speckit.idea.standards` |
| Accept | `/speckit-analyze` (read-only findings), `/speckit-checklist`, workflow `gate` | — | `speckit.idea.accept`: readiness checklist, standards gate (law blocks, internal warns), human name and date, v1.0 tag |
| Prototype | — | `wireframe` (SVG from spec, sign-off into `## UI Mockup`); `figma` (Figma → spec only) | `speckit.idea.prototype`: a clickable HTML prototype built from §6, published for comments, with the two-lane rule (`VISUAL` items never reach the spec) and `speckit.idea.accept --prototype` as its own checklist and gate |
| Whole loop | Workflow engine: `gate`, `do-while`, `if`, `command`, run log under `.specify/workflows/runs/` | — | `workflows/idea-to-spec/workflow.yml` |

## Where the pieces are installed

| Source in this repo | Installed copy | Command |
|---------------------|----------------|---------|
| `presets/idea-to-spec/` | `.specify/presets/idea-to-spec/` | `specify preset add --dev ./presets/idea-to-spec --priority 5` |
| `extensions/idea/` | `.specify/extensions/idea/` and `.claude/skills/speckit-idea-*/SKILL.md` | `specify extension add --dev ./extensions/idea --force` |
| `workflows/idea-to-spec/` | `.specify/workflows/idea-to-spec/` | `specify workflow add ./workflows/idea-to-spec` |

`specify preset resolve spec-template` must point at the preset copy; if it points at `.specify/templates/spec-template.md`, the preset is not installed.

## Known limits

- Spec Kit's own `/speckit-specify` still exists and writes the core-style spec from a one-line description. Use `/speckit-idea-draft` for this process; `specify` is for the classic code-first path.
- `/speckit-clarify`, `/speckit-analyze` and `/speckit-checklist` work on the idea-to-spec template but were written for the core one; their reports may reference sections by the core names.
- Headless runs (`specify workflow run`, `claude -p`) cannot ask the reviewer anything. The workflow therefore confirms feedback at a gate that shows the round file, and `speckit.idea.apply --gate-confirmed` records that.
- Community extensions listed above are single-maintainer and early (intake 0.2, taco 0.4, wireframe 0.1). None is required here.
