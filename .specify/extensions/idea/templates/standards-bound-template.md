# Standards bound: [IDEA NAME]

The authoritative record of which project standards this idea is bound to and at which version. §8 of `spec.md` names the same versions in one line for a reader; this file is what `/speckit-idea-standards` and the acceptance checklist read.

| Field | Value |
|-------|-------|
| **Spec version at last bind** | [0.x] |
| **Bound on** | [YYYY-MM-DD] |
| **Drift** | none / [n] module(s) moved since the bind |

## Bound modules

| Prefix | Module | Authority | Version bound | Version now | Drift |
|--------|--------|-----------|---------------|-------------|-------|
| `STD-A11Y` | accessibility-eaa | law | [1.0] | [1.0] | — |
| `STD-CD` | branding-cd | internal | [0.1] | [0.1] | — |

## Materialised into the spec

Rules whose "Shapes the spec" is yes and that found something to attach to. Every line named here carries the rule's tag in `spec.md`.

| Rule | Landed in |
|------|-----------|
| [STD-A11Y-007] | [SCR-02 States, SCR-05 States] |
| [STD-A11Y-009] | [FR-018] |

## Carried as a check only

Rules that bind but write nothing into the spec, because they are decided in the prototype. Listed so nobody mistakes their absence from `spec.md` for their absence from the idea.

| Rule | Decided at |
|------|-----------|
| [STD-A11Y-004] | prototype |

## Conflicts between standards

Resolved by authority (`law` > `contract` > `internal`), then by `precedence`. Recorded once, not re-argued.

| Rule | Loses to | Resolution | Recorded |
|------|----------|------------|----------|
| [STD-CD-004] | [STD-A11Y-004] | [what may no longer be used, concretely] | [YYYY-MM-DD] |

## Exemptions

A rule that does not apply to this idea. Only a human grants one; the record carries the reasoning.

| Rule | Record | Reason in one line | Approved by | Date |
|------|--------|--------------------|-------------|------|
| [STD-CD-006] | [EXM-001] | [...] | [name] | [YYYY-MM-DD] |

## Not verifiable

Rules from a module whose `status` is `draft`, or rules whose `bites` is `build`. Neither passed nor failed; named so the gap is visible.

| Rule | Why |
|------|-----|
| [STD-CD-003] | module branding-cd is a draft; values are placeholders |
| [STD-A11Y-015] | bites: build — cannot be decided in a prototype |
