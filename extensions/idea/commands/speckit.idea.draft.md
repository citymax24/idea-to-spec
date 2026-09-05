---
description: Write spec.md v0.1 from the cited facts; every line carries a provenance tag. Creates CHANGELOG.md, the readiness checklist and the first git tag. With --template standard-spec-template it drafts a standards module instead of an idea.
---

## User Input

```text
$ARGUMENTS
```

Optional: `--feature <dir>`, `--name "<Idea name>"` for the spec title, `--template <name>`, `--headless`.

`--template` selects the skeleton. Without it the idea template is used and everything below reads as written. With `--template standard-spec-template` this command drafts a **standards module** instead of an idea — see "Drafting a standards module" at the end.

## Interactive or headless

Headless means: `--headless` is among the arguments, or you cannot wait for a reply (a `claude -p` run, a workflow step). Interactive means you can ask and wait. Every "ask the human" step below applies only when interactive; headless runs leave the marker or status in the file and stop.

## Goal

Phase 3 of the idea-to-spec loop. A first complete draft that a reviewer can react to. Every statement can be traced to a source, a resolved question, or an explicitly marked assumption.

## Steps

1. **Resolve `FEATURE_DIR`.** Require `analysis/facts.md`. If `spec.md` already exists, stop: "spec.md exists. Change it through `/speckit-idea-feedback` and `/speckit-idea-apply`, not by redrafting."

2. **Load context.** `inputs/INVENTORY.md`, `analysis/facts.md`, `analysis/conflicts.md`, `analysis/open-questions.md`, every `decisions/*.md`, `.specify/memory/constitution.md` if it exists, and the standards registry `standards/` if it exists.

3. **Resolve the template.** Run `.specify/scripts/bash/resolve-template.sh <name>` — `spec-template` unless `--template` names another — and use its output as the skeleton. Keep section order and headings exactly. Read the HTML comments in the template; they are the rules. If the resolver exits non-zero, stop and say which template could not be resolved; do not fall back to a different one.

4. **Fill every section from the facts.**
   - Every JOB, FLOW, SCR, FR, SC and constraint line ends with a provenance tag: `[F-012 · S3 row 12]`, `[C-02 resolved]`, `[Q-03 resolved]`, or `[ASSUMPTION: derived from …]`. A line without a tag is a defect.
   - Unresolved conflict: take the claim from the higher-weight source, tag it `[ASSUMPTION: C-01 unresolved, S1 high over S2 medium]`, and list the conflict in §11 under its analysis ID (`C-01`).
   - Unanswered open question: use the suggested default as an assumption in §10, cite it as `[ASSUMPTION: Q-02 default]`, keep the question in §11 under its analysis ID (`Q-02`).
   - §11 keeps the IDs from `analysis/`. New questions that arise later continue numbering above the highest Q in `analysis/open-questions.md` and `spec.md`.
   - Decisions: content excluded by a decision record does not appear anywhere, not even as an assumption.
   - Screen catalog: derive screens from jobs and flows. Every FR maps to at least one SCR in "Satisfies", or the FR ends with "(no screen: background rule)". Every flow starts and ends at an SCR.
   - `[NEEDS CLARIFICATION: …]`: at most 3, only for gaps that change scope. Everything else becomes an assumption.
   - Header: Version `0.1`, Status `draft`, Created today, Sources `S1–S<n>`, "Drafted from" sentence.
   - Language: English. Keep source-language terms in quotes where a translation would lose meaning.

5. **Bind the standards.** If `standards/` exists, run the binding half of `/speckit-idea-standards --bind` as part of this draft: select the modules that apply, resolve conflicts between them by authority, materialise every rule whose "Shapes the spec" is yes into the section it attaches to with the tag `[STD-<PREFIX>-<nnn> · v<module version>]`, write the §8 binding line, and write `standards/BOUND.md`. This is part of v0.1, so it does not bump the version. If there is no registry, skip this step silently — standards are optional.

6. **Write `CHANGELOG.md`** from `.specify/extensions/idea/templates/changelog-template.md` with the v0.1 block and the counts.

7. **Write `checklists/requirements.md`** from `readiness-checklist-template.md` and evaluate it against the draft. Fix what fails (missing tags, incomplete SCR blocks, flows not anchored, empty "Out of scope") and re-evaluate, at most 3 passes. Leave honest unchecked boxes with a note if something cannot be fixed from the sources.

8. **Git.** If the project is a git repository: `git add FEATURE_DIR`, commit `spec(<slug>): v0.1 initial draft`, tag `spec-<slug>-v0.1`. The slug is the feature directory name without its numeric prefix. If not a repository, say so and skip; the version history then exists only in `CHANGELOG.md`.

9. **Report.** Spec path, counts (JOB, FLOW, SCR, FR, SC, assumptions, open questions, clarification markers), checklist result, the standards bound with their versions (or that there is no registry), next command `/speckit-idea-publish`.

## Drafting a standards module

With `--template standard-spec-template` the subject is a law, a norm or an internal manual, not an idea. `--feature` points at the module — `standards/accessibility-eaa`, not `specs/NNN-slug`. Steps 1, 2 and 3 hold as written; these replace steps 4 to 9.

- **Do not touch `.specify/feature.json`.** It points at the active idea. A module is drafted by explicit `--feature` and never becomes the active feature.
- **Sources are the module's own namespace.** `inputs/INVENTORY.md` here holds `EAA1…EAA5` or `CD1…CD9`, never `S1…Sn`. A tag citing `S3` in a module spec is a defect: it would resolve against whatever idea happens to be active.
- **Fill the module template**: §1 purpose and legal basis, §2 applicability including any relief the source itself grants, §3 one block per requirement with Severity, Bites, Shapes the spec, Check and Source, §4 success criteria, §5 assumptions, §6 open questions, §7 tombstones. Requirement IDs are `STD-<PREFIX>-001` upward, with 101 upward for anything above the bound conformance level.
- **A requirement must be judgeable at the stage this loop reaches.** "The product is accessible" is not a requirement. If a rule can only be decided in built software, keep it and set `Bites: build`, so nobody later reads a green prototype as proof of it.
- **Header**: Version `0.1`, Status `draft`, Prefix, Authority, Source version, Sources, "Derived from" sentence. Status stays `draft`; only a human sets `active`.
- **Do not write `checklists/requirements.md`.** That checklist asks about screens and flows, which a module does not have. A module's readiness is decided at its own acceptance.
- **`CHANGELOG.md`**: create it, or add the `v0.1` block if the module already has one from being set up by hand.
- **Git**: commit `std(<module-id>): v0.1 initial draft`, tag `std-<module-id>-v0.1` — a namespace parallel to the `spec-<slug>-v<x.y>` tags of ideas, so module versions and idea versions never collide.
- **Report**: module path, requirement count by severity, how many carry `Bites: build`, assumptions, open questions, and that the module stays `draft` until a human accepts it.

## Rules

- Do not invent users, features or numbers. If a section has no facts, write the assumption and the open question, not a plausible story.
- Do not include technology, architecture or implementation.
- Never let a standards module cite an idea's sources, or an idea cite a module's. The namespaces exist to keep that impossible.
- Do not ask the reviewer questions here beyond the 3 clarification markers; the review round is the place for that.
