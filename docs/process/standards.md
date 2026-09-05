# Project standards

**Status**: v1.0 · 2026-09-05 · Owner: Max Bollich

Rules that bind every idea in this repository regardless of what the idea is about. Two are set up — accessibility (external law) and corporate design (internal manual) — but they are not two special cases: they are the first two modules of one mechanism that also has to carry data protection, security and tone of voice later.

## Why standards are not sources and not feedback

The loop already has two ways for a statement to enter a spec. An input source (`S3 slide 7`) is something someone told us about this idea. Feedback (`R1-02`) is something a reviewer wants changed. Both are specific to the idea, and both are negotiable.

A standard is neither. It is decided once for the whole project, it applies to ideas nobody has had yet, and a reviewer cannot talk it away in a round — a colour that fails a contrast rule stays failed however much the brand prefers it. So standards are a third source of truth with their own tag, their own place, and one deliberate asymmetry: `/speckit-idea-apply` refuses a feedback item that would drop a standard line, and offers an exemption instead.

## The registry

```
standards/
├── README.md                what the registry is, how to add a module
├── REGISTRY.md              the index over all modules
├── accessibility-eaa/
│   ├── standard.yml         authority, own version, source version, scope
│   ├── rules.md             STD-A11Y-001 … , one block per rule
│   └── CHANGELOG.md         one block per module version
└── branding-cd/
    ├── standard.yml
    ├── rules.md             STD-CD-001 …
    ├── CHANGELOG.md
    └── assets/              logo, fonts, tokens.json + a licence table
```

`standards/` sits at the repository root, next to `specs/`, not inside `.specify/`: it is project content, not tooling. It is optional — a clone without it runs the whole loop unchanged, and every command skips its standards step silently.

This document explains why the mechanism has the shape it has. `standards/README.md` is the operational reference next to the files themselves: what a module must contain, and the steps to add one.

### What a module declares

| Field | What it decides |
|-------|-----------------|
| `prefix` | the rule ID namespace, `STD-A11Y-007`. Never reused, not even by a retired module |
| `version` | the version of *this module*. Bumped on every change to `rules.md` or `assets/` |
| `source_version` | for external modules: the version of the law or norm the rules were written against |
| `status` | `draft` \| `active` \| `retired`. A `draft` module binds, but none of its rules can ever be reported `pass` |
| `authority` | `law` > `contract` > `internal`. Decides conflicts, and decides whether a breach blocks |
| `precedence` | tiebreaker inside one authority band; lower wins |
| `applies_to` | which ideas it binds. An idea outside the scope needs an exemption, not an assumption |
| `review_by` | the date by which someone must check whether the source moved. With `source_version`, this is what keeps an external standard from drifting silently |
| `owner`, `updated` | who answers for the module, and when it last changed |
| `assets` | files the rules point at; the prototype embeds them, it cannot link them |

### What a rule declares

Every rule block carries **Severity** (`required` inside the bound level, or `recommended` above it), **Bites** (`spec` decidable while writing, `prototype` checkable in the built prototype, `build` only checkable in real software), and **Shapes the spec** (whether binding writes it into `spec.md` or keeps it as a check).

`bites: build` is the honest field. A prototype cannot prove that a screen reader announces a live region in a real browser on a real device. Recording that in the module means the checklist says `not verifiable` instead of a comfortable `pass`.

## What `accessibility-eaa` does not promise

`accessibility-eaa` has `status: active`, not `draft` — but active is not a conformance claim. Its `standard.yml` records `legal_review: ASSUMED`: for the MVP no legal review was commissioned, and the module is treated as cleared so the loop can be used. That is a decision recorded as a decision (`standards/README.md`, "Assumed legal review"), not a review that happened. The fifteen required rules remain an engineering reading of EN 301 549 → WCAG 2.1 AA, not legal advice, and four questions were never asked: whether a given product is in scope at all, the current EN 301 549 version and the WCAG level it references (a newer EN 301 549 already points at WCAG 2.2), the German transposition (BFSG/BFSGV) and its information duties, and whether the micro-enterprise relief applies. Before anything built from this repository is placed on a market, that review has to happen for real.

WCAG 2.1 AA itself runs to roughly fifty success criteria; this module carries only the subset that can be decided while there is an idea, a spec and a clickable prototype — nothing that only shows up in built software with real assistive technology. A `pass` on every rule here means nothing was designed in that would have to be undone later. It does not mean the product conforms to the EAA, and no report or checklist produced by this loop should be read, quoted or repeated as a conformance or compliance claim.

## Binding, and why the version is recorded

An idea is bound to a module *at a version*, written into `specs/<NNN>-<slug>/standards/BOUND.md`. `spec.md` §8 carries the same versions in one readable line tagged `[STD-BINDING]`; `BOUND.md` is the authoritative copy.

Recording the version is the whole point. The corporate design will move — that is what internal manuals do — and the EAA's conformance norm will move without asking this repository. An idea accepted against `STD-CD v4.1` does not silently become an idea about `v4.2`. It drifts, `standards_status.py` says so, and a human decides whether to rebind and re-accept.

Rules whose **Shapes the spec** is yes are materialised into the spec where they actually attach — a label rule into the `Content` of the screens that take input, an error-text rule into those screens' `States`, a keyboard rule into §7 as a requirement — each with the tag `[STD-A11Y-007 · v1.0]`. Everything else stays in the registry and is listed in `BOUND.md` under "Carried as a check only", so the absence of a rule from `spec.md` is never mistaken for its absence from the idea.

A rebind that changes `spec.md` is a version like any other change: `0.x` → `0.x+1`, or on an accepted spec `1.y` → `1.y+1` with the status back to `in-review`. A rebind that only refreshes `BOUND.md` is not a version.

## Conflicts between modules

The corporate design fixes a colour pairing; the accessibility rule demands 4.5:1; the pairing measures 3.8:1. This is not an exception to handle each time — it is the ordinary case, and the mechanism decides it the way the loop already decides a contradiction between two input sources: by weight.

`law` beats `contract` beats `internal`, then `precedence`. The losing rule is not deleted, it is constrained: the colour keeps existing, it just may not carry text. The resolution is written once into `BOUND.md` under "Conflicts between standards" and never re-argued — including by the prototype, which reads that record instead of deciding again.

## Exemptions

A rule that genuinely cannot apply gets `decisions/EXM-<nnn>.md`: the rule quoted in full so the record still reads correctly after the module moves, why it does not apply, what is done instead, and what it costs. Only a human signs one, in any mode.

An exemption stops a rule from blocking. It does not make it pass, and it lapses when the module is bumped, because a new version of a rule is a new question.

For a `law` module the bar is deliberately high: either the idea is outside the standard's scope, or the requirement is met by other means that the record names. "We decided not to" is not a reason, and the command refuses it.

## Blocking, warning, not verifiable

| Situation | At acceptance |
|-----------|---------------|
| `required` rule of a `law` module fails | blocks |
| `law` module drifted since the bind | blocks |
| Anything in a `contract` or `internal` module | warning the reviewer accepts by name |
| `recommended` rule anywhere | warning |
| Module is a `draft`, or rule `bites: build` | `not verifiable`, listed, never counted as passed |
| Signed exemption exists at the bound version | stops blocking |

The split follows the authority field rather than a per-case judgement: accessibility is a legal duty, corporate design is a house rule, and a house rule should not be able to hold up a finished spec.

## Commands

`/speckit-idea-standards` with no flag reports where an idea stands. `--bind` binds or rebinds. `--check` writes the rule-by-rule verdicts to `checklists/standards.md`, with measured evidence rather than assertions. `--exempt <RULE-ID> --reason "…"` opens an exemption for a human to sign.

The other commands carry it without being asked: `draft` binds as part of v0.1, `feedback` flags an item that collides with a rule, `apply` refuses to weaken a standard line, `prototype` builds to the prototype-level rules and embeds the assets, and `accept` gates on the split above.

## Adding the next module

The steps are in `standards/README.md`, where the templates and the files are. The part that belongs here is what happens to work already done: ideas already accepted do not change on their own. They drift, the drift is reported, and a human decides whether to rebind and re-accept. A new module binds to new ideas silently and to old ones only when someone says so.

That is the test of whether this was built once or twice. `STD-GDPR`, `STD-SEC` and `STD-TONE` are held in `REGISTRY.md` for exactly that reason: adding one should be filling two templates, not touching a command.
