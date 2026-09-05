# Standards Mechanism — Handoff from the Test Environment

**Status**: PROPOSAL — nothing here is implemented · 2026-09-05 · Owner: Max Bollich

> **Editor's note, 2026-09-05.** This document is kept as the record of how the standards mechanism was argued for. Three things about it are now out of date, and none of them is corrected in the text below:
>
> - **The mechanism has been built**, and differs from this design in several places — where module provenance comes from, where a conflict is recorded, and how tightly a version is pinned. `docs/process/standards.md` describes what actually runs; this page is the origin of the idea, not a description of it.
> - **The design-brief step this document builds on no longer exists.** `/speckit-idea-brief`, `brief-template.md` and the Claude Design canvas were removed and replaced by `/speckit-idea-prototype`. §4.6 and two rows of §5 therefore target files that are gone; their intent maps onto the prototype step.
> - **`specs/002-test-inbox/design/` was deleted** — it was 5.1 MB of canvas output from that removed step. §1 and §7 still refer to it. What the test run produced is unchanged as a matter of history; the folder is simply no longer in the repository, and the `spec-test-inbox-*` tags still reach it.

This document is a handoff from a test-environment session to the main project, where the described mechanism would actually be built. It describes a design, not current behaviour. Nothing in `presets/`, `extensions/`, `.specify/memory/constitution.md` or `CLAUDE.md` has changed because of it. A reader who wants the process as it actually runs today should read `docs/process/idea-to-spec-process.md` and `docs/process/spec-kit-mapping.md`; this page is not part of that process description.

## 1 What the test environment validated

The test environment ran the full idea-to-spec loop end to end on a second synthetic idea, `specs/002-test-inbox/` ("Quote Follow-Up Tracker"), beyond the first dry run recorded in `docs/guides/test-case.md`. Confirmed from the repository:

- Versions `v0.1 → v0.2 (R1) → accepted v1.0 → v1.1 (R2, in-review) → accepted v1.1 → v1.2 (R3, in-review) → accepted v1.2`, each with a git tag (`spec-test-inbox-v0.1` … `spec-test-inbox-v1.2`, plus `-accepted` tags for the two re-acceptances).
- Three feedback rounds (`feedback/R1.md`, `R2.md`, `R3.md`), each confirmed by a named reviewer before being applied.
- A design brief (`specs/002-test-inbox/design/brief.md`) and a Claude Design canvas with artboards for all eight screens and their states (`specs/002-test-inbox/design/canvas/`).
- One assumption retired by a human decision through a feedback item rather than silently overwritten (A-06, replaced by R3-01), which is the mechanism rule 3/4 exist for — but note under "Not verified" below: this run produced no tombstoned requirement and no `decisions/DEC-*.md` file, so the decision-record path itself is not exercised by this run.

This confirms the loop itself is solid. It does not yet cover what follows: carrying project-wide, cross-idea standards (accessibility, branding) into every idea. That gap is the subject of this proposal.

## 2 The requirement

Every idea that becomes a prototype in this project must honour two standing, project-wide standards:

| Standard | Nature | Source of change |
|----------|--------|-------------------|
| **Accessibility** | European Accessibility Act (Directive (EU) 2019/882), transposed nationally (BFSG/BFSGV in Germany), technically testable via EN 301 549 / WCAG 2.1 AA | External law, versioned by others |
| **Branding / Corporate Design** | Internal company manual: rules plus assets (logo, fonts, colour values) | Self-versioned, changes more often than law |

Further modules are plausible later (GDPR, security, tone of voice). The goal is one standards mechanism that both current cases fit, not two special cases.

## 3 Why a standard cannot just be another spec under `specs/`

Three collisions rule out building a standard as an ordinary idea spec and copying lines out of it into every idea spec.

| Collision | Where it comes from |
|-----------|----------------------|
| **S-ID collision.** `extensions/idea/scripts/python/convert_inputs.py` assigns `S1, S2, S3…` per feature directory, starting at `S1` and never renumbering (`existing_ids()` / `next_id` in `main()`). A standards module under `specs/` would get its own `S1…Sn`, colliding with the `S1…Sn` every idea already has. A line copied from the module into an idea spec, e.g. `[F-012 · S2 Art. 9]`, would then point at whatever the idea's own `S2` happens to be — a source tag that resolves, but to the wrong place. That is worse than a missing tag: it passes the provenance check in rule 1 of `CLAUDE.md` while being false. | `extensions/idea/scripts/python/convert_inputs.py` |
| **Requirement-ID collision.** Rule 3 of `CLAUDE.md` requires IDs to be stable and never reused. A module spec and an idea spec would each independently produce `FR-001, FR-002, …` — the same IDs, different meanings, if module requirements were ever pasted into an idea spec. | `CLAUDE.md`, rule 3 |
| **Template mismatch.** In `presets/idea-to-spec/templates/spec-template.md`, §3 (User Jobs), §5 (User Flows) and §6 (Screen Catalog) are marked `*(mandatory)*`. A law or a CD manual has none of these — no user jobs, no flows, no screens. Drafting a module through `/speckit-idea-draft` as if it were an idea would press screens out of facts that describe no screens, and `checklists/requirements.md` (item: "every FR maps to at least one SCR") would never turn green. | `presets/idea-to-spec/templates/spec-template.md` §3/§5/§6 |

The finding that makes a different design possible: `.specify/scripts/bash/resolve-template.sh` accepts any template name — it is not hardcoded to `spec-template`. A preset can register a template that is provided *additionally*, without replacing the core one (`provides.templates` in `presets/idea-to-spec/preset.yml`, which today registers exactly one template with `replaces: spec-template`). Only `extensions/idea/commands/speckit.idea.draft.md`, step 3, hardcodes `resolve-template.sh spec-template` — that is the one place that would need to change if module specs were drafted through a command rather than by hand (see §6).

## 4 Proposed mechanism

### 4.1 Directory and registry

Standard modules are not ideas and would not live under `specs/`:

```
standards/
  REGISTRY.md                # slug | version | git tag | rank | mandatory | scope, one sentence
  accessibility-eaa/         # source prefix EAA*, requirement prefix A11Y-###
    inputs/  analysis/  spec.md  CHANGELOG.md  decisions/
  branding-cd/                # source prefix CD*, requirement prefix BRD-###
    inputs/  analysis/  spec.md  CHANGELOG.md  decisions/
    assets/                  # logo SVG, font files — referenced, not run through facts.md;
                              # an asset is not a claim
    tokens.md                # colours, type scale, spacing — machine-readable for the design brief
```

Module git tags follow `std-<slug>-v<x.y>`, parallel to the existing `spec-<slug>-v<x.y>` idea tags.

### 4.2 Namespaces

- `convert_inputs.py` would get a `--prefix` switch (default `S`, unchanged for existing ideas) so a module's sources are named `EAA1`, `CD1`, … instead of colliding with an idea's `S1…Sn`. S-IDs are never renumbered, in modules any more than in ideas.
- Module requirements get their own prefix (`A11Y-###`, `BRD-###`) so they can never collide with an idea's `FR-###`.

### 4.3 One additional provenance-tag form

Rule 1 of `CLAUDE.md` would gain one more allowed tag form, alongside the existing ones:

```
[STD <slug> v<x> §<id>]        e.g. [STD branding-cd v1 §2]
```

This does not weaken rule 1. The tag still points at a concrete, findable location — a section of a module `spec.md` — just in a module instead of a source document.

### 4.4 Inclusion by reference, not by copy

Each idea spec would carry a fixed `Standards` block in §8 (Constraints), with one pinned line per `mandatory` module from `REGISTRY.md`. Module requirements are never copied into an idea spec's body: copying them would mean chasing every legal or CD change through every idea spec individually.

**Pinning**: pin to the module's major version, let minor versions flow through automatically. `branding-cd v1` named in the spec; a new accent colour released as `v1.2` reaches every idea automatically without a spec change; a rebrand is `v2` and forces every spec that pins `branding-cd` into a deliberate, visible decision at the next touch.

### 4.5 Conflict handling

Accessibility and branding will collide — corporate colours routinely fail the 4.5:1 contrast requirement for text. Without a rule, this gets re-argued inside every idea, or silently settled by whoever happens to be building that idea's mockup.

`.specify/memory/constitution.md` — loaded by `/speckit-idea-draft` (step 2) and today still the unfilled Spec Kit template — would carry three things:

1. the obligation that every idea spec pins all `mandatory` modules from `REGISTRY.md`, each with a version;
2. a fixed precedence order, e.g. law > accessibility standard > corporate design > convention;
3. the rule that a conflict between two modules is resolved once, at module level, as a `decisions/DEC-*.md` in the **yielding** (lower-ranked) module, citing the winning requirement.

Example: a decision recorded inside `standards/branding-cd/decisions/` — "CD green #7BC043 stays decorative and non-text only, at 3:1 contrast or better; text and controls use CD dark #1F4D0C instead — [A11Y-014]." Every idea that pins `branding-cd` then inherits the already-resolved colour choice; nobody re-litigates it while building a mockup.

This is the actual gain of the mechanism — not the file format, but that an unavoidable contradiction becomes **one** documented decision instead of being re-decided (or silently decided) fifteen times, once per idea.

### 4.6 Branding belongs mostly in the brief, not the spec

`extensions/idea/commands/speckit.idea.brief.md`, step 2, already states as a rule for the design prompt: *"No colours, fonts or layouts unless §8 fixes them."* The branding module is precisely what would fix them.

- **In the spec**: only the version pin, plus the few brand rules that genuinely constrain content or screens — e.g. "logo top left on every screen" is a screen requirement, not a visual nicety.
- **In the brief**: expanded per screen from `tokens.md` (colour values, type scale, spacing), plus the states and behaviour that come from the accessibility module (focus order, error messages rendered as text rather than colour alone, keyboard operability).

A desirable side effect: the existing two-lane rule for mockup feedback (visual stays in the canvas; content or flow goes back through a feedback round) gets sharper. "This colour is too harsh" stops being a canvas-only question and becomes a question addressed to the branding module — otherwise several prototypes drift apart visually over time, each fixed locally in its own canvas.

## 5 Files that would change

| File | Change |
|------|--------|
| `presets/idea-to-spec/templates/spec-template.md` | §8 gains the `Standards` block (one pinned line per mandatory module) |
| `extensions/idea/templates/readiness-checklist-template.md` | New item: every mandatory module from `REGISTRY.md` is pinned with a version |
| `extensions/idea/templates/brief-template.md` | Standards expansion per screen (from `tokens.md` and the accessibility module) |
| `extensions/idea/commands/speckit.idea.draft.md` | Fill the §8 Standards block from `REGISTRY.md` |
| `extensions/idea/commands/speckit.idea.brief.md` | Expand standards per screen from `tokens.md` and the accessibility module |
| `extensions/idea/scripts/python/convert_inputs.py` | Add `--prefix` (default `S`, existing ideas unaffected) |
| `.specify/memory/constitution.md` | Add the pin obligation, the precedence order, and the conflict-resolution rule |
| `CLAUDE.md` | Extend rule 1 with the `[STD <slug> v<x> §<id>]` tag form |
| new: a standards template for module specs | §1 Purpose/legal basis, §2 Applicability, §3 Requirements, §4 Success criteria, §5 Assumptions, §6 Open questions, §7 Tombstones — provided by the preset **additionally**, without `replaces`, so `spec-template` for ideas is untouched |

As with any change to the preset or the extension, sources under `presets/` and `extensions/` would be edited and then reinstalled, per the existing rule in `CLAUDE.md`:

```bash
specify preset add --dev ./presets/idea-to-spec --priority 5
specify extension add --dev ./extensions/idea --force
```

The installed copies under `.specify/` and `.claude/skills/` are never edited directly.

## 6 One open decision — for the human, not the AI

Two ways to produce a module `spec.md`:

- **(a)** Extend `/speckit-idea-draft` with a `--template` switch and draft module specs the regular way. Cleaner, more rework to the command.
- **(b)** Hand-write the module spec once from `analysis/facts.md` against the new standards template. Faster, no change to `speckit.idea.draft.md`.

Argument for (b): a module is written once, not weekly, unlike an idea spec which goes through repeated review rounds. The actual automation gain in this loop is in `intake` + `facts` — turning 100+ atomic, cited claims out of a legal text or a CD manual into `analysis/facts.md` is not something anyone wants to do by hand — and in the acceptance/tag discipline that keeps a module's version trustworthy. Neither of those depends on the draft step being automated. This is a judgment call about where to spend the rework, not a technical constraint, so it belongs with the human implementing this, not decided here.

## 7 Order of work

1. **Accessibility first.** The stricter, externally versioned module. Building it first shows whether the namespace (`--prefix`), the `[STD …]` tag, and the registry actually hold up against a real, dense source (a legal text with hundreds of testable clauses).
2. **Branding second**, against the same mechanism, unchanged. If it fits without rework, the design is right. If accessibility were built second instead, the simpler case would validate first and accessibility would likely force a rebuild.
3. **Only then** pull an existing idea spec (e.g. `specs/002-test-inbox/`) onto the mechanism — through `/speckit-idea-feedback` + `/speckit-idea-apply`, exactly like any other change. Never by editing `spec.md` directly, per the existing rules.

## 8 Questions to settle before implementation starts

- Which source files exist for EAA / BFSG / EN 301 549 and for the CD manual, and in what format (PDF, HTML, DOCX)?
- The accessibility sources carry three levels of concreteness — an abstract directive, a national law, and a concretely testable standard. The weights in `inputs/INVENTORY.md` must reflect that: EN 301 549 (concrete) should outweigh the directive (abstract) where they overlap. That is exactly the case `analysis/conflicts.md` exists to record, not a special case to build around.
- Which precedence order is binding: is "law > accessibility standard > corporate design > convention" actually correct for this organisation, or does it need adjustment?
- Which modules are `mandatory` for every idea, and which are optional?

Because this rework touches the project's core rules — provenance (rule 1), stable IDs (rule 3), and the spec template itself — the implementing session should present a plan before changing anything, not start editing `presets/`, `extensions/`, `.specify/memory/constitution.md` or `CLAUDE.md` directly.

## Not verified in this handoff

- **Decision records from the test run.** `specs/002-test-inbox/decisions/` exists but is empty; this run produced no `decisions/DEC-*.md` and no §13 tombstone. The mechanism that rule 3/4 describes (tombstone + decision record on removal) was exercised by the first dry run (`docs/guides/test-case.md`, `DEC-001.md` under `specs/001-quote-tracker/`), not by this second run. Do not read §1 above as claiming this run produced a decision record; it did not.
