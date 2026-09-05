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

Arguments: `[--approved-by <name>] [--feature <specs/NNN-dir>] [--headless]`. `--approved-by` is for headless runs after a human gate; interactively the reviewer types their name.

## Interactive or headless

Headless means: `--headless` is among the arguments, or you cannot wait for a reply (a `claude -p` run, a workflow step). Interactive means you can ask and wait. Every "ask the human" step below applies only when interactive; headless runs leave the marker or status in the file and stop.

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
   - reviewed sections cover the spec, or the reviewer accepts without full coverage knowingly. With `--approved-by` (a human gate preceded this step) incomplete coverage counts as accepted knowingly; note it in the checklist.

3. **If anything fails:** report the failing items with what would fix them and stop. Suggest a feedback round.

4. **If everything passes:**
   - Interactive: ask "Accept spec v<version> as v<target>? Reply with your name to approve, or `no`." Wait.
   - Headless: if `--approved-by <name>` is given, treat it as approval (a human gate preceded this step); else stop with "Ready for acceptance. Approve at the workflow gate or run interactively."

5. **On approval:** target version = `1.0` if the current version is below 1.0, otherwise the current version unchanged (a re-acceptance after rounds on an accepted spec, e.g. 1.2 stays 1.2). Header Version `<target>`, Status `accepted`, Approved by `<name>`, Approved on `<date>`. Add a changelog block `## v<target> · <date> · accepted by <name>` listing the rounds it went through. Commit `spec(<slug>): v<target> accepted by <name>`; tag `spec-<slug>-v<target>` if it does not exist yet, else `spec-<slug>-v<target>-accepted`.

6. **Report.** Status, tag, next command `/speckit-idea-brief`.

## Rules

- Never set `accepted` without a name from a human.
- Never soften a failing checklist item to get to acceptance.