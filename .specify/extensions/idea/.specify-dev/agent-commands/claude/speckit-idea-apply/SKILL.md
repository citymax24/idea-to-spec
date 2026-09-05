---
name: speckit-idea-apply
description: Apply a confirmed feedback round to the spec as one new version - edits with change markers, tombstones and decision records for removals, a changelog block naming the triggering feedback IDs, and a git tag.
compatibility: Requires spec-kit project structure with .specify/ directory
metadata:
  author: github-spec-kit
  source: idea:commands/speckit.idea.apply.md
---

## User Input

```text
$ARGUMENTS
```

Arguments: `[R<n>] [--gate-confirmed <run_id>] [--feature <specs/NNN-dir>] [--headless]`. Without `R<n>`, the highest round with unapplied items is used. If no round has unapplied items, stop: "Nothing to apply."

## Goal

Phase 4, step 3 and 4 of the idea-to-spec loop. One round becomes exactly one new spec version. Every change is traceable to a feedback item in both directions, and everything removed gets a decision record so it stays removed.

## Steps

1. **Resolve `FEATURE_DIR` and the round.** Read `feedback/R<n>.md`.

2. **Preconditions.** Every item must be `confirmed`, `answered`, `dropped`, `deferred` or `prototype-only`.
   - If items are still `proposed` and `--gate-confirmed <run_id>` is given: set them to `confirmed` and write `confirmed via workflow gate <run_id> on <date>` into the round header.
   - If items are still `proposed` without that flag: stop and list them. "Run `/speckit-idea-feedback` to confirm first."

3. **Load** `spec.md`, `CHANGELOG.md`, `decisions/*.md`, `inputs/INVENTORY.md`, `analysis/facts.md`.

4. **Compute the new version.** Status `draft` or `in-review`: `0.x` → `0.x+1`, status becomes `in-review`. Status `accepted`: `1.y` → `1.y+1`, status becomes `in-review` and the header's Approved fields are kept with the note `(v1.y)`.

5. **Apply items in ID order.** Before applying any item, check whether its target line carries a `[STD-<PREFIX>-<nnn> · v<x.y>]` tag. A standard is not the reviewer's to change: a `REMOVE` or a `CHANGE` that would drop or weaken such a line is refused here. Leave the item `confirmed`, note in the round file's Notes which rule it collides with, and tell the reviewer the two ways out — meet the rule differently, or request an exemption with `/speckit-idea-standards --exempt <RULE-ID> --reason "…"`, which a human must sign. Everything else in the round still applies.
   - `ADD`: allocate the next free number per prefix (scan the whole spec including §13 tombstones; never reuse). Provenance tag `[R<n>-<nn>]`, plus the source if the reviewer cited one. New screens get the complete SCR block; update flows if the item says so.
   - `CHANGE`: edit the line or section in place, keep the ID, append ` ⟲ v<new> · R<n>-<nn>`.
   - `MISREAD`: re-read the cited source location, replace the misreading, mark as `CHANGE`; record in the round file's Notes: "was: <old text> (read from <location>)".
   - `REMOVE`: delete the item from its section; add a tombstone line in §13 (`FR-014 · <one line> · Removed in v<new> · R<n>-<nn> · DEC-<nnn>`); create `decisions/DEC-<nnn>.md` (nnn = highest existing DEC number + 1, starting at 001) from `.specify/extensions/idea/templates/decision-template.md` with the reviewer's words as the reason and, if the item came from a source, how that source location is to be read from now on. Remove references in "Satisfies" lists and flows and note them in the changelog row.
   - `QUESTION`: no change.
   - `VISUAL` (status `prototype-only`): no change. It belongs to the prototype lane and is picked up by the next `/speckit-idea-prototype` run.
   - `OK`: add the sections to the header's "Reviewed sections" as `§1, §3 (v<reviewed>, R<n>-<nn>)`.
   - `deferred`: add to §11 as `Q-<nn>: <question> — deferred R<n>-<nn>: <reason>`, with nn above the highest Q in `analysis/open-questions.md` and `spec.md`.
   - `dropped`: nothing.

6. **Consistency pass.** Every materialised standard line is still present and still tagged; a new screen that takes input gets the standard lines its siblings carry (run `/speckit-idea-standards --bind` if the round added screens). Every FR still maps to an SCR or is marked "no screen"; every flow still starts and ends at an existing SCR; no reference to a removed ID remains outside §13; header Version and Status updated; every new or changed line has its tag or marker; §10 assumptions that a feedback item resolved are removed or updated.

7. **Changelog.** Insert a new block directly under the intro paragraph of `CHANGELOG.md`, above the previous newest block: `## v<new> · <date> · from round R<n>` with a table `Change | Affects | Trigger | Type`, one row per applied item, then `Not changed: R<n>-03 (question, answered)`, `Prototype only: R<n>-05 (visual)`, `Refused (standard): R<n>-06 collides with STD-A11Y-007` and `Deferred: …` lines.

8. **Round file.** Set applied items to `applied (v<new>)`; keep `answered`, `dropped`, `deferred`, `prototype-only`.

9. **Checklist.** Re-evaluate `checklists/requirements.md` and update the boxes.

10. **Git.** If a repository: `git add FEATURE_DIR`, commit `spec(<slug>): v<new> from R<n>`, tag `spec-<slug>-v<new>` (slug = feature directory name without its numeric prefix).

11. **Report** in one line first: "Round R<n> applied: <k> changes, <q> questions answered, <d> deferred, <v> prototype-only, <o> open. Spec v<new>." Then: next command `/speckit-idea-publish` for the next round, or `/speckit-idea-accept` if the reviewer signalled acceptance. If a prototype exists, say that `/speckit-idea-prototype` rebuilds it after re-acceptance.

## Rules

- Apply only what is in the round file. No opportunistic improvements.
- Never renumber or reuse IDs. Never delete a tombstone.
- One round, one version, one commit.