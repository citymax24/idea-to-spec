# The Idea-to-Spec Process

**Status**: v0.4 · 2026-09-05 · Owner: Max Bollich

From a heterogeneous set of inputs about an idea to a specification a human has accepted, with every change traceable to the feedback that caused it, and from there to a clickable prototype built straight out of that spec. The spec is the one document that survives the prototype phase.

There is no design brief and no design canvas in this loop. Once the spec is accepted it is a finished hand-off on its own: the human can take `spec.md` into Claude Design by hand, or ask for `/speckit-idea-prototype` and get something to click through instead of another document to read.

## Eight rules

1. **Nothing without provenance.** Every JOB, FLOW, SCR, FR, SC and constraint line ends with a tag: a source (`[S3 slide 7]`), a fact (`[F-012 · S3 row 12]`), a resolved conflict or question (`[C-02 resolved]`, `[Q-03 resolved]`), a feedback item (`[R1-02]`) or an explicit assumption (`[ASSUMPTION: derived from S3 row 30]`). What the AI added is visibly added.
2. **Feedback is understood before it is applied.** The AI rewrites each piece of feedback into a numbered item and shows it. The human confirms or corrects. The spec never changes directly from raw feedback.
3. **IDs are stable.** Requirements, screens, sources, feedback items and decisions have IDs that are never reassigned. A removed requirement stays as a tombstone: ID, one line, pointer to the decision.
4. **Removed stays removed.** Every removal is logged as a decision. Before proposing anything from the sources again, the AI checks the decision log.
5. **One round, one version.** Each feedback round yields exactly one new spec version with a git tag. The changelog names the triggering feedback item for every change.
6. **Only the human accepts.** The AI never sets the status to accepted, for the spec or for the prototype. Acceptance is a deliberate step with name and date in the spec header.
7. **Standards are not negotiable in a round.** Project-wide rules enter from `standards/`, carry the tag `[STD-…]`, and a reviewer cannot remove one with feedback. A rule that cannot apply needs a signed exemption. See `standards.md`.
8. **The prototype holds nothing the spec does not.** Every screen, field, column and action in the prototype traces to §6 of the spec. A gap in the prototype is a rebuild; a gap in the spec is a feedback round.

## Phases

| Phase | Command | Actor | Produces |
|-------|---------|-------|----------|
| 1 Collect | `/speckit-idea-intake` | AI, human sets weights | `inputs/raw/`, `inputs/extracted/S<n>-*.md`, `inputs/INVENTORY.md` |
| 2 Understand | `/speckit-idea-facts` | AI, human resolves conflicts | `analysis/facts.md`, `conflicts.md`, `open-questions.md` |
| 3 Draft | `/speckit-idea-draft` | AI | `spec.md` v0.1 bound to the standards, `standards/BOUND.md`, `CHANGELOG.md`, `checklists/requirements.md`, tag |
| 4 Review loop | `/speckit-idea-publish` → `/speckit-idea-feedback` → `/speckit-idea-apply` | human + AI | `feedback/R<n>.md`, `spec.md` v0.n+1, changelog block, `decisions/DEC-*.md`, tag |
| 5 Accept | `/speckit-idea-accept` | human | `checklists/standards.md`, header `accepted`, v1.0 tag |
| 6 Prototype *(optional)* | `/speckit-idea-prototype` → `/speckit-idea-accept --prototype` | AI builds, human clicks and accepts | `prototype/prototype.html` (published, stable URL), `prototype/README.md`, `PUBLISHED.md`, `checklists/prototype.md`, tag `proto-<slug>-v<x.y>` |

Phase 6 is optional. Stopping at phase 5 with an accepted spec is a complete result; the prototype exists because a reviewer sees more in thirty seconds of clicking than in thirty minutes of reading.

Prototype feedback that concerns content or flow (not looks) goes back into phase 4 as a new round; the spec version rises to 1.1 (status back to in-review), is re-accepted at 1.1 through `/speckit-idea-accept`, and the prototype is rebuilt. Feedback about looks alone is a `VISUAL` item: it never reaches the spec and is honoured on the next build.

## ID schemes

| Prefix | Meaning | Lives in |
|--------|---------|----------|
| `S1` | Source (file) | `inputs/INVENTORY.md` |
| `F-001` | Atomic claim with location | `analysis/facts.md` |
| `C-01`, `Q-01` | Conflict between sources, open question | `analysis/` |
| `JOB-01`, `FLOW-01`, `SCR-01` | User job, flow, screen | `spec.md` §3, §5, §6 |
| `FR-001`, `SC-001` | Functional requirement, success criterion (Spec Kit convention) | `spec.md` §7, §9 |
| `A-01` | Assumption | `spec.md` §10 |
| `R1-03` | Feedback item 3 in round 1 | `feedback/R1.md` |
| `DEC-002` | Decision record | `decisions/` |
| `EXM-001` | Signed exemption from a standard rule | `decisions/` |
| `STD-A11Y-007` | Rule of a project standard, bound at a version | `standards/<id>/rules.md` |

Location formats inside a source tag: `slide 7`, `row 12 (sheet Features)`, `§3`, `para 4`, `07:40`, `p.3`.

## Feedback item types

| Type | Reviewer says | Effect |
|------|---------------|--------|
| `ADD` | "Something is missing." | New FR / SCR / section with a `[R<n>-<nn>]` tag |
| `CHANGE` | "Different from what is written." | Edited in place, ID kept, marker `⟲ v0.2 · R1-01` |
| `REMOVE` | "Out entirely." | Tombstone in §13 plus `DEC-<nnn>.md` |
| `MISREAD` | "You misunderstood the source." | Like CHANGE; the round file records what was read from where |
| `QUESTION` | "Why is this here?" | Answered with provenance; no change |
| `OK` | "This part is fine." | Section recorded as reviewed in the header |
| `VISUAL` | "Too dense", "button too small". | Prototype lane only. Status `prototype-only`; the spec never changes; the next `/speckit-idea-prototype` run honours it |

Status path of an item: `proposed` → `confirmed` | `dropped` | `deferred` → `applied (v0.x)`; questions end as `answered`, `VISUAL` items as `prototype-only`.

## Acceptance criteria

The AI evaluates, the human decides. All must hold:

- no feedback item `proposed` or `confirmed` without being applied; deferred items are in §11;
- every screen has purpose, primary action, content, states, at least one requirement, comes-from and leads-to;
- every flow starts and ends at a catalogued screen; every screen is reached by a flow;
- every JOB, FLOW, SCR, FR, SC and constraint line has a provenance tag; no `[NEEDS CLARIFICATION]` remains;
- no assumption contradicts a decision;
- "Out of scope" is not empty;
- every `required` rule of a `law` standard passes or carries a signed exemption, and no `law` module has drifted since the bind (see `standards.md`).

## Prototype acceptance criteria

Evaluated by `/speckit-idea-accept --prototype` against `prototype/prototype.html` and written to `checklists/prototype.md`. All must hold:

- every SCR in §6 exists as a screen in the prototype, badged with its SCR-ID;
- every FLOW can be clicked from its first screen to its last, and every primary action leads where "Leads to" says;
- every state a screen lists can be shown;
- nothing appears that the spec does not contain, and nothing from §4 or from a §13 tombstone;
- labels are in the UI language §8 fixes, and the device context of §8 is respected;
- the prototype was built from the current spec version, and that version is `accepted`;
- every `required` prototype-level rule of a `law` standard passes with measured evidence or is exempted.

On approval the spec header row `Prototype` records name, date and the spec version; the loop is finished for that version.

## Why this shape

Spec Kit gives the skeleton (template with stable IDs, clarify, analyze, checklist) and the mechanics (workflow engine with gates and loops, presets, extensions). It does not give heterogeneous intake with citations, feedback-as-data with a confirmation step, the trace from feedback to change, project standards that a review round cannot erode, or a prototype that cannot drift from the spec. Those five are what the preset and the extension add. See `spec-kit-mapping.md` and `standards.md`.
