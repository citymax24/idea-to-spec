# Standards registry

Project-wide rules that every idea in this repository is bound to, whatever the idea is about. A standard is not a source (`S#`) and not feedback (`R#-##`): nobody proposes it in a review round and no reviewer can talk it away. It is decided once, here, and then carried into every spec and every prototype.

Two are set up: `accessibility-eaa` (external law) and `branding-cd` (internal corporate design). The mechanism is the same for anything that comes later — data protection, security, tone of voice.

## Anatomy of a standard

```
standards/<id>/
├── standard.yml     what it is: authority, own version, source version, scope
├── rules.md         the rules, one block per rule, stable IDs STD-<PREFIX>-<nnn>
├── CHANGELOG.md     one block per version of this module
└── assets/          files the rules refer to (logo, fonts, tokens) — internal standards only
```

`REGISTRY.md` is the index over all of them.

## The five ideas it rests on

1. **Stable rule IDs.** `STD-A11Y-007` means the same thing forever, exactly like `FR-014` or `S3`. A rule that is withdrawn becomes a tombstone in its module's `CHANGELOG.md`; its ID is never reused.
2. **Two versions per external standard.** The module has its own `version` (what this repository says) and records the `source_version` it was written against (what the law or norm says). The EAA can move without this repository noticing — the `source_version` and `review_by` fields are what make that visible instead of silent.
3. **Authority decides conflicts.** `law` beats `contract` beats `internal`. When a corporate-design colour fails a contrast rule, the accessibility rule wins and the resolution is recorded in the idea's binding — the same shape as a conflict between two input sources, decided by weight.
4. **Bound, not copied.** An idea records which standards it is bound to *at which version* (`specs/<NNN>-<slug>/standards/BOUND.md`). When a module is bumped afterwards, that idea drifts, and the drift is visible instead of assumed away.
5. **Only a human exempts.** A rule that cannot apply to an idea needs a signed exemption record (`decisions/EXM-<nnn>.md`), never a quiet omission. Required rules of a `law` standard block acceptance until they are met or exempted; internal standards warn.

## Assumed legal review

`accessibility-eaa` derives from law, and law is normally something a lawyer signs off. For this MVP that step is deliberately skipped.

**Decision, Max Bollich, 2026-09-05**: no legal review is commissioned for the MVP. The `accessibility-eaa` module is treated as cleared so the loop can be used end to end, and `standard.yml` records this as `legal_review: ASSUMED` rather than as a review that happened.

What that buys and what it does not:

- The module is complete and usable. `/speckit-idea-standards --check` produces real verdicts, and a failed required rule really does block acceptance.
- It is **not** a conformance claim, and nothing this loop prints may be quoted as one. An assumption recorded as an assumption is honest; the same assumption reported as a cleared review would be a false record that outlives whoever made it.
- Four questions were never asked: whether a given product is in scope at all, which EN 301 549 version applies and which WCAG level it references, what the German transposition demands in the way of information duties, and whether the micro-enterprise relief applies.

Before anything built from this repository is placed on a market, that review has to happen for real. When it does, replace the assumption in `standard.yml` with the finding, bump the module version, and write the block in `CHANGELOG.md` — which makes every idea bound to v1.0 drift, which is exactly the point.

## Adding a module

```bash
mkdir -p standards/<id>
cp .specify/extensions/idea/templates/standard-yml-template.yml standards/<id>/standard.yml
cp .specify/extensions/idea/templates/standard-rules-template.md standards/<id>/rules.md
```

Fill both, add a row to `REGISTRY.md`, pick a free `prefix` and a `precedence` that does not collide inside its authority band. Then `/speckit-idea-standards --bind` on each active idea picks it up. Ideas already accepted do not change on their own: they drift, the drift is reported, and a human decides whether to rebind and re-accept.

## What a rule must be

Checkable at the stage this loop works at — an idea, a spec, a clickable prototype. "The product is accessible" is not a rule. "Every form field has a visible label that is programmatically associated with it" is. If a rule can only be checked in built software, it still belongs here, but mark it `bites: build` so nobody pretends the prototype proved it.
