# Idea to Spec Loop (Spec Kit extension `idea`)

Eight commands that take an idea from mixed raw inputs to an accepted, fully cited specification and a design brief.

| Command | Phase | Writes |
|---------|-------|--------|
| `/speckit-idea-intake <folder> --name <slug>` | Collect | `inputs/raw/`, `inputs/extracted/S<n>-*.md`, `inputs/INVENTORY.md` |
| `/speckit-idea-facts` | Understand | `analysis/facts.md`, `analysis/conflicts.md`, `analysis/open-questions.md` |
| `/speckit-idea-draft` | Draft | `spec.md` v0.1, `CHANGELOG.md`, `checklists/requirements.md`, git tag |
| `/speckit-idea-publish` | Review | `feedback/spec-review.html` (republished, stable URL), `feedback/spec-v<x.y>.html` (frozen), `feedback/PUBLISHED.md` |
| `/speckit-idea-feedback [text | --file | --inbox | --from-comments]` | Review | `feedback/R<n>.md` (items `proposed` → `confirmed`) |
| `/speckit-idea-apply [R<n>]` | Review | `spec.md` v0.x+1, `CHANGELOG.md` block, `decisions/DEC-*.md`, git tag |
| `/speckit-idea-accept` | Accept | header `accepted`, v1.0 on first acceptance |
| `/speckit-idea-brief [--draft]` | Design | `design/brief.md`, `design/README.md`, hand-off to the `design` skill |

## Scripts

| Script | Used by | Does |
|--------|---------|------|
| `scripts/python/convert_inputs.py` | `/speckit-idea-intake` | Assigns stable S-IDs to raw inputs and converts them to Markdown |
| `scripts/python/render_spec.py` | `/speckit-idea-publish` | Renders `spec.md` to a self-contained HTML page with an anchor per ID |
| `scripts/python/spec_status.py` | the `idea-to-spec` workflow | Exits 0 when `spec.md` has the expected status; gates whether `speckit.idea.brief` runs after acceptance |

Rules the commands enforce: nothing without provenance, feedback is confirmed before it is applied, IDs are stable, removed content gets a decision record and stays removed, one round is one version, only a human accepts.

The full process is described in `docs/process/idea-to-spec-process.md` at the repository root.
