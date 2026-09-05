---
description: Run the acceptance checklist and, on the reviewer's explicit approval, set the spec status to accepted with name, date and a v1.0 tag; with --prototype, accept the built prototype the same way. The AI never accepts on its own.
---

## User Input

```text
$ARGUMENTS
```

Arguments: `[--prototype] [--approved-by <name>] [--feature <specs/NNN-dir>] [--headless]`. `--approved-by` is for headless runs after a human gate; interactively the reviewer types their name. `--prototype` switches to prototype acceptance (see "Prototype acceptance" below); without it this command accepts the spec.

## Interactive or headless

Headless means: `--headless` is among the arguments, or you cannot wait for a reply (a `claude -p` run, a workflow step). Interactive means you can ask and wait. Every "ask the human" step below applies only when interactive; headless runs leave the marker or status in the file and stop.

## Goal

Phase 5 of the idea-to-spec loop, and the closing gate of phase 6. The gate between review and the prototype, and later the gate that ends the loop. The checklist is evaluated by you; the decision is the human's.

## Steps (spec acceptance)

1. **Resolve `FEATURE_DIR`.** Read `spec.md`, all `feedback/R*.md`, `CHANGELOG.md`, `decisions/*.md`, and — if `standards/` exists — `standards/BOUND.md` and `checklists/standards.md`.

2. **Evaluate the checklist** from `.specify/extensions/idea/templates/readiness-checklist-template.md` and write the result to `checklists/requirements.md`:
   - every JOB, FLOW, SCR, FR, SC and constraint line has a provenance tag; no `[NEEDS CLARIFICATION]` left;
   - no assumption contradicts a decision record;
   - every SCR has purpose, primary action, content, states, at least one FR, comes-from and leads-to;
   - every FLOW starts and ends at an SCR; every SCR is reached by a FLOW;
   - every FR maps to an SCR or is marked "no screen (background rule)";
   - §4 "Out of scope" is not empty;
   - no feedback item is `proposed` or `confirmed` without being applied; deferred items are in §11;
   - **standards**: run `python3 .specify/extensions/idea/scripts/python/standards_status.py --strict` and `/speckit-idea-standards --check`. Read the exit code: `0` no blocking drift, `1` a `law` module moved since the bind, `2` there is no registry **or the spec was never bound at all**. Exit `2` is not a pass — check which of the two it is, and treat an unbound spec as a failing checklist item whose fix is `/speckit-idea-standards --bind`. A `required` rule of a `law` module that is `fail`, or a `law` module that drifted since the bind, blocks acceptance and can only be cleared by meeting the rule or by a signed exemption. An internal module that fails or drifts does not block: it goes into the checklist as a named warning the reviewer accepts knowingly. A rule reported `not verifiable` is listed as such, never counted as passed. Skip this bullet entirely when there is no registry;
   - reviewed sections cover the spec, or the reviewer accepts without full coverage knowingly. With `--approved-by` (a human gate preceded this step) incomplete coverage counts as accepted knowingly; note it in the checklist.

3. **If anything fails:** report the failing items with what would fix them and stop. Suggest a feedback round, or `/speckit-idea-standards --exempt` when the blocker is a standard rule that genuinely does not apply.

4. **If everything passes:**
   - Interactive: name the standards warnings out loud before asking, so the reviewer's name goes onto them knowingly. Then ask "Accept spec v<version> as v<target>? Reply with your name to approve, or `no`." Wait.
   - Headless: if `--approved-by <name>` is given, treat it as approval (a human gate preceded this step); else stop with "Ready for acceptance. Approve at the workflow gate or run interactively."

5. **On approval:** target version = `1.0` if the current version is below 1.0, otherwise the current version unchanged (a re-acceptance after rounds on an accepted spec, e.g. 1.2 stays 1.2). Header Version `<target>`, Status `accepted`, Approved by `<name>`, Approved on `<date>`. Add a changelog block `## v<target> · <date> · accepted by <name>` listing the rounds it went through. Commit `spec(<slug>): v<target> accepted by <name>`; tag `spec-<slug>-v<target>` if it does not exist yet, else `spec-<slug>-v<target>-accepted`.

6. **Report.** Status, tag, and what the reviewer can do next in one sentence: `/speckit-idea-prototype` to get a clickable prototype built from this spec, or take `spec.md` into Claude Design by hand. There is no design brief step.

## Prototype acceptance (`--prototype`)

Same shape, different subject: the spec stays as it is and the prototype is what gets accepted.

1. **Resolve `FEATURE_DIR`.** Require `spec.md` with status `accepted` and a built `prototype/prototype.html`. If the prototype is missing, stop with "No prototype yet. Run /speckit-idea-prototype." Read `prototype/PUBLISHED.md` and every `feedback/R*.md` written after the prototype was first built.

2. **Evaluate the prototype checklist** from `.specify/extensions/idea/templates/prototype-checklist-template.md` against `prototype/prototype.html` and the spec, and write the result to `checklists/prototype.md`: every SCR built and badged, every FLOW clickable end to end, every primary action wired to its "Leads to", every listed state reachable, nothing shown that the spec does not contain, nothing from §4 or §13, the UI language of §8, and the prototype built from the current spec version.

   Then re-run `/speckit-idea-standards --check`, which is where the prototype-level rules are actually decided — contrast measured, keyboard order walked, labels bound. The same split applies: a failed `required` rule of a `law` module blocks the prototype acceptance; an internal one warns.

3. **If anything fails:** report the failing items with what would fix them and stop. A gap in the prototype is a rebuild (`/speckit-idea-prototype`); a gap in the spec is a feedback round.

4. **If everything passes:**
   - Interactive: ask "Accept the prototype of spec v<version>? Reply with your name to approve, or `no`." Wait.
   - Headless: `--approved-by <name>` counts as approval; else stop with "Ready for prototype acceptance."

5. **On approval:** set the spec header row `Prototype` to `accepted by <name> on <date> (spec v<version>)`; add the row after `Approved on` if the header does not have it yet. Add a changelog block `## Prototype v<version> · <date> · accepted by <name>` naming the rounds that ran after the prototype was first built. Commit `proto(<slug>): v<version> accepted by <name>`; tag `proto-<slug>-v<version>`.

6. **Report.** Prototype URL or path, the tag, and that the loop is finished for this version. A later change starts a new feedback round and a rebuild.

## Rules

- Never set `accepted` without a name from a human, for the spec or for the prototype.
- Never soften a failing checklist item to get to acceptance, and never turn a standards failure into a warning by reclassifying the module.
- `--prototype` never changes the spec's own status, version or content beyond the `Prototype` header row.
