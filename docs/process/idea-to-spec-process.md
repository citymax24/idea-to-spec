# The Idea-to-Spec Process

**Status**: v0.2 · 2026-09-05 · Owner: Max Bollich

From a heterogeneous set of inputs about an idea to a specification a human has accepted, with every change traceable to the feedback that caused it, and from there to a design brief for Claude Design. The spec is the one document that survives the mockup phase.

## Six rules

1. **Nothing without provenance.** Every statement in the spec carries a source tag (`[S3 slide 7]`), a feedback tag (`[R1-02]`) or an explicit assumption tag (`[ASSUMPTION: derived from S3 row 30]`). What the AI added is visibly added.
2. **Feedback is understood before it is applied.** The AI rewrites each piece of feedback into a numbered item and shows it. The human confirms or corrects. The spec never changes directly from raw feedback.
3. **IDs are stable.** Requirements, screens, sources, feedback items and decisions have IDs that are never reassigned. A removed requirement stays as a tombstone: ID, one line, pointer to the decision.
4. **Removed stays removed.** Every removal is logged as a decision. Before proposing anything from the sources again, the AI checks the decision log.
5. **One round, one version.** Each feedback round yields exactly one new spec version with a git tag. The changelog names the triggering feedback item for every change.
6. **Only the human accepts.** The AI never sets the status to accepted. Acceptance is a deliberate step with name and date in the spec header.

## Phases

| Phase | Command | Actor | Produces |
|-------|---------|-------|----------|
| 1 Collect | `/speckit-idea-intake` | AI, human sets weights | `inputs/raw/`, `inputs/extracted/S<n>-*.md`, `inputs/INVENTORY.md` |
| 2 Understand | `/speckit-idea-facts` | AI, human resolves conflicts | `analysis/facts.md`, `conflicts.md`, `open-questions.md` |
| 3 Draft | `/speckit-idea-draft` | AI | `spec.md` v0.1, `CHANGELOG.md`, `checklists/requirements.md`, tag |
| 4 Review loop | `/speckit-idea-publish` → `/speckit-idea-feedback` → `/speckit-idea-apply` | human + AI | `feedback/R<n>.md`, `spec.md` v0.n+1, changelog block, `decisions/DEC-*.md`, tag |
| 5 Accept | `/speckit-idea-accept` | human | header `accepted`, v1.0 tag |
| 6 Design | `/speckit-idea-brief` → `design` skill | AI + Claude Design | `design/brief.md`, artboards named by SCR-ID |

Mockup feedback that concerns content or flow (not looks) goes back into phase 4 as a new round; the spec version rises to 1.1 and the affected artboards are regenerated.

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

Status path of an item: `proposed` → `confirmed` | `dropped` | `deferred` → `applied (v0.x)`; questions end as `answered`.

## Acceptance criteria

The AI evaluates, the human decides. All must hold:

- no feedback item `proposed` or `confirmed` without being applied; deferred items are in §11;
- every screen has purpose, primary action, content, states, at least one requirement, comes-from and leads-to;
- every flow starts and ends at a catalogued screen; every screen is reached by a flow;
- every requirement, job and criterion line has a provenance tag; no `[NEEDS CLARIFICATION]` remains;
- no assumption contradicts a decision;
- "Out of scope" is not empty.

## Why this shape

Spec Kit gives the skeleton (template with stable IDs, clarify, analyze, checklist) and the mechanics (workflow engine with gates and loops, presets, extensions). It does not give heterogeneous intake with citations, feedback-as-data with a confirmation step, or the trace from feedback to change. Those three are what the preset and the extension add. See `spec-kit-mapping.md`.
