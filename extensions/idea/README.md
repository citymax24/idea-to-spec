# Idea to Spec Loop (Spec Kit extension `idea`)

Eight commands that take an idea from mixed raw inputs to an accepted, fully cited specification and a design brief.

| Command | Phase | Writes |
|---------|-------|--------|
| `/speckit-idea-intake <folder> --name <slug>` | Collect | `inputs/raw/`, `inputs/extracted/S<n>-*.md`, `inputs/INVENTORY.md` |
| `/speckit-idea-facts` | Understand | `analysis/facts.md`, `analysis/conflicts.md`, `analysis/open-questions.md` |
| `/speckit-idea-draft` | Draft | `spec.md` v0.1, `CHANGELOG.md`, `checklists/requirements.md`, git tag |
| `/speckit-idea-publish` | Review | `feedback/spec-review.html`, `feedback/PUBLISHED.md` (+ artifact URL) |
| `/speckit-idea-feedback [text | --file | --from-comments]` | Review | `feedback/R<n>.md` (items `proposed` → `confirmed`) |
| `/speckit-idea-apply [R<n>]` | Review | `spec.md` v0.x+1, `CHANGELOG.md` block, `decisions/DEC-*.md`, git tag |
| `/speckit-idea-accept` | Accept | header `accepted`, v1.0 tag |
| `/speckit-idea-brief [--draft]` | Design | `design/brief.md`, `design/README.md`, hand-off to the `design` skill |

Rules the commands enforce: nothing without provenance, feedback is confirmed before it is applied, IDs are stable, removed content gets a decision record and stays removed, one round is one version, only a human accepts.

The full process is described in `docs/process/idea-to-spec-process.md` at the repository root.
