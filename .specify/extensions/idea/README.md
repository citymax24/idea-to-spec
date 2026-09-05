# Idea to Spec Loop (Spec Kit extension `idea`)

Nine commands that take an idea from mixed raw inputs to an accepted, fully cited specification, bound to the project's standards, and a clickable prototype built from it.

| Command | Phase | Writes |
|---------|-------|--------|
| `/speckit-idea-intake <folder> --name <slug>` | Collect | `inputs/raw/`, `inputs/extracted/S<n>-*.md`, `inputs/INVENTORY.md` |
| `/speckit-idea-facts` | Understand | `analysis/facts.md`, `analysis/conflicts.md`, `analysis/open-questions.md` |
| `/speckit-idea-draft` | Draft | `spec.md` v0.1, `CHANGELOG.md`, `checklists/requirements.md`, git tag |
| `/speckit-idea-publish` | Review | `feedback/spec-review.html` (republished, stable URL), `feedback/spec-v<x.y>.html` (frozen), `feedback/PUBLISHED.md` |
| `/speckit-idea-feedback [text | --file | --inbox | --from-comments]` | Review | `feedback/R<n>.md` (items `proposed` → `confirmed`) |
| `/speckit-idea-apply [R<n>]` | Review | `spec.md` v0.x+1, `CHANGELOG.md` block, `decisions/DEC-*.md`, git tag |
| `/speckit-idea-standards [--bind\|--check\|--exempt]` | Standards | `standards/BOUND.md`, `checklists/standards.md`, `decisions/EXM-<nnn>.md`, the `[STD-…]` lines in `spec.md` |
| `/speckit-idea-accept` | Accept | header `accepted`, v1.0 on first acceptance; law standards block, internal ones warn |
| `/speckit-idea-prototype [--draft]` | Prototype | `prototype/prototype.html` (republished, stable URL), `prototype-v<x.y>.html` (frozen), `prototype/README.md`, `prototype/PUBLISHED.md` |
| `/speckit-idea-accept --prototype` | Prototype accept | `checklists/prototype.md`, spec header row `Prototype`, tag `proto-<slug>-v<x.y>` |

## Scripts

| Script | Used by | Does |
|--------|---------|------|
| `scripts/python/convert_inputs.py` | `/speckit-idea-intake` | Assigns stable S-IDs to raw inputs and converts them to Markdown |
| `scripts/python/render_spec.py` | `/speckit-idea-publish` | Renders `spec.md` to a self-contained HTML page with an anchor per ID |
| `scripts/python/spec_status.py` | the `idea-to-spec` workflow | Exits 0 when `spec.md` has the expected status; gates whether `speckit.idea.prototype` runs after acceptance |
| `scripts/python/standards_status.py` | `/speckit-idea-standards`, the workflow, accept | Compares the idea's bound standard versions against `standards/`; `--strict` fails only on a `law` module's drift |

Rules the commands enforce: nothing without provenance, feedback is confirmed before it is applied, IDs are stable, removed content gets a decision record and stays removed, one round is one version, only a human accepts, the prototype never contains anything the spec does not, and a project standard cannot be eroded by a review round.

The full process is described in `docs/process/idea-to-spec-process.md` at the repository root; the standards mechanism in `docs/process/standards.md`. Standards are optional: without a `standards/` registry every standards step is skipped and the loop runs unchanged.
