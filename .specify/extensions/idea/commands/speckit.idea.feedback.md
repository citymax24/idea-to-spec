---
description: Capture reviewer feedback (chat text, transcript, file, or comments on the published page), normalise it into numbered items with type and target, and get the reviewer's confirmation before anything changes.
---

## User Input

```text
$ARGUMENTS
```

Arguments: `[--from-comments] [--file <path>] [--reviewer <name>] [--feature <specs/NNN-dir>] [free-text feedback]`. Several sources can be combined in one round.

## Goal

Phase 4, step 1 and 2 of the idea-to-spec loop. Feedback becomes data: one row per intended change, the reviewer's words kept verbatim, your reading of it written next to them, and a status that only moves to `confirmed` when the reviewer says so. Nothing in the spec changes in this command.

## Steps

1. **Resolve `FEATURE_DIR`.** Require `spec.md`. Read its header for version and status.

2. **Collect raw feedback.**
   - Free text from the arguments.
   - `--file`: read the file (voice transcript, notes, an email).
   - `--from-comments`: read the current URL from `feedback/PUBLISHED.md` and fetch the page's comment threads with the artifact comments tool. One thread is one raw item; keep the anchored text as the target hint and note the thread id and author.
   - If nothing was provided and the session is interactive: ask the reviewer to paste or dictate the feedback now.
   - If nothing was provided and the session is not interactive: stop with "No feedback given."

3. **Open the round.** Round number = highest existing `feedback/R<n>.md` + 1. Create `feedback/R<n>.md` from `.specify/extensions/idea/templates/feedback-round-template.md`. Header: spec version reviewed, today, reviewer (from `--reviewer`, the comment author, or ask; else `unknown`), channel.

4. **Split into atomic items.** One item = one intended change or one question. A sentence like "target group is wrong, onboarding is missing, and drop the export" is three items. Keep the reviewer's exact words in the Verbatim column, in the original language, quoted.

5. **Classify each item.**
   - Type: `ADD` · `CHANGE` · `REMOVE` · `MISREAD` · `QUESTION` · `OK`.
   - Target: a section (`§2`), an ID (`FR-014`, `SCR-03`, `JOB-02`, `FLOW-01`), or `whole spec`. If the reviewer did not name one, find the section their words refer to and say so.
   - "Understood as": one precise English sentence describing the change you would make, naming the IDs that would be added, changed or removed.
   - `QUESTION`: answer it right there with provenance ("FR-009 comes from S3 row 14, priority 1"). Status `answered`. If the answer reveals a real problem, add a second item of the right type.
   - `MISREAD`: also write in the Notes what the spec currently says and which source location it was read from, so the reviewer sees the misreading.
   - `OK`: list the sections covered.
   - Status for everything else: `proposed`.

6. **Confirm.**
   - Interactive session: show the table and ask: "Did I understand each item correctly? Reply `confirm`, correct by ID (`R1-02: also the detail screen`), or `drop R1-05`." Apply corrections to the round file. Dropped items stay in the file with status `dropped` and the reason. Repeat until the reviewer says `confirm`. Then set all remaining `proposed` items to `confirmed`, set the header `Confirmation` to `confirmed by <reviewer> on <date>`, and tell the reviewer: "Run `/speckit-idea-apply R<n>`."
   - Non-interactive session (headless run, workflow): leave every item `proposed`, print the table, and stop. The workflow shows the file at a human gate; `/speckit-idea-apply --gate-confirmed <run-id>` records that approval.

7. **Report.** Round file path, counts per type, whether confirmation is done, next command.

## Rules

- Never modify `spec.md`, `CHANGELOG.md` or `decisions/` in this command.
- Never soften or reinterpret the reviewer's words in the Verbatim column.
- Do not derive changes from side remarks. If it is not clearly a request, make it a `QUESTION` back to the reviewer.
