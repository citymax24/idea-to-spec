---
name: speckit-idea-accept
description: Run the acceptance checklist and, on the reviewer's explicit approval, set the spec status to accepted with name, date and a v1.0 tag. The AI never accepts on its own.
compatibility: Requires spec-kit project structure with .specify/ directory
metadata:
  author: github-spec-kit
  source: idea:commands/speckit.idea.accept.md
---

## User Input

```text
$ARGUMENTS
```

Arguments: `[--approved-by <name>] [--feature <specs/NNN-dir>]`. `--approved-by` is for non-interactive runs after a human gate; interactively the reviewer types their name.

## Goal

Phase 5 of the idea-to-spec loop. The gate between review and design. The checklist is evaluated by you; the decision is the human's.

## Steps

1. **Resolve `FEATURE_DIR`.** Read `spec.md`, all `feedback/R*.md`, `CHANGELOG.md`, `decisions/*.md`.

2. **Evaluate the checklist** from `.specify/extensions/idea/templates/readiness-checklist-template.md` and write the result to `checklists/requirements.md`:
   - every JOB, FLOW, SCR, FR, SC and constraint line has a provenance tag; no `[NEEDS CLARIFICATION]` left;
   - no assumption contradicts a decision record;
   - every SCR has purpose, primary action, content, states, at least one FR, comes-from and leads-to;
   - every FLOW starts and ends at an SCR; every SCR is reached by a FLOW;
   - every FR maps to an SCR or is marked "no screen (background rule)";
   - §4 "Out of scope" is not empty;
   - no feedback item is `proposed` or `confirmed` without being applied; deferred items are in §11;
   - reviewed sections cover the spec, or the reviewer accepts without full coverage knowingly.

3. **If anything fails:** report the failing items with what would fix them and stop. Suggest a feedback round.

4. **If everything passes:**
   - Interactive: ask "Accept spec v<version> as v1.0? Reply with your name to approve, or `no`." Wait.
   - Non-interactive: if `--approved-by <name>` is given, treat it as approval (a human gate preceded this step); else stop with "Ready for acceptance. Approve at the workflow gate or run interactively."

5. **On approval:** header Version `1.0`, Status `accepted`, Approved by `<name>`, Approved on `<date>`. Add a changelog block `## v1.0 · <date> · accepted by <name>` listing the rounds it went through. Commit `spec(<slug>): v1.0 accepted by <name>` and tag `spec-<slug>-v1.0`.

6. **Report.** Status, tag, next command `/speckit-idea-brief`.

## Rules

- Never set `accepted` without a name from a human.
- Never soften a failing checklist item to get to acceptance.