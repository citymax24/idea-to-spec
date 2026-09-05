---
description: Capture reviewer feedback (chat text, transcript, file, or comments on the published page), normalise it into numbered items with type and target, and get the reviewer's confirmation before anything changes.
---

## User Input

```text
$ARGUMENTS
```

Arguments: `[--from-comments] [--file <path>] [--inbox] [--reviewer <name>] [--feature <specs/NNN-dir>] [--headless] [free-text feedback]`. Several sources can be combined in one round.

## Interactive or headless

Headless means: `--headless` is among the arguments, or you cannot wait for a reply (a `claude -p` run, a workflow step). Interactive means you can ask and wait. Every "ask the human" step below applies only when interactive; headless runs leave the marker or status in the file and stop.

## Goal

Phase 4, step 1 and 2 of the idea-to-spec loop. Feedback becomes data: one row per intended change, the reviewer's words kept verbatim, your reading of it written next to them, and a status that only moves to `confirmed` when the reviewer says so. Nothing in the spec changes in this command.

## Steps

1. **Resolve `FEATURE_DIR`.** Require `spec.md`. Read its header for version and status.

2. **Collect raw feedback.**
   - Free text from the arguments.
   - `--file`: read the file (voice transcript, notes, an email).
   - `--from-comments`: read the current URL from `feedback/PUBLISHED.md` and fetch the page's comment threads with the artifact comments tool. One thread is one raw item; keep the anchored text as the target hint and note the thread id and author. If the latest PUBLISHED row is a local path, or no comments tool exists, or there are no comments, this lane simply contributes nothing.
   - `--inbox`: read `FEATURE_DIR/feedback/inbox.txt` if it exists and is not empty (the workflow's review gate asks the reviewer to write there). After the round file is written, rename it to `feedback/R<n>-inbox.txt` so it is not read twice.
   - If nothing was provided and the session is interactive: ask the reviewer to paste or dictate the feedback now.
   - If nothing was provided and the session is headless: stop with "No feedback given." and write no round file.

3. **Open the round.** Round number = highest existing `feedback/R<n>.md` + 1. Create `feedback/R<n>.md` from `.specify/extensions/idea/templates/feedback-round-template.md`. Header: spec version reviewed, today, reviewer (from `--reviewer`, the comment author, or ask; else `unknown`), channel.

4. **Split into atomic items.** One item = one intended change or one question. A sentence like "target group is wrong, onboarding is missing, and drop the export" is three items. Keep the reviewer's exact words in the Verbatim column, in the original language, quoted.

5. **Classify each item.**
   - Type: `ADD` · `CHANGE` · `REMOVE` · `MISREAD` · `QUESTION` · `OK` · `VISUAL`.
   - Target: a section (`§2`), an ID (`FR-014`, `SCR-03`, `JOB-02`, `FLOW-01`), or `whole spec`. If the reviewer did not name one, find the section their words refer to and say so.
   - "Understood as": one precise English sentence describing the change you would make, naming the IDs that would be added, changed or removed.
   - `QUESTION`: answer it right there with provenance ("FR-009 comes from S3 row 14, priority 1"). Status `answered`. If the answer reveals a real problem, add a second item of the right type.
   - `MISREAD`: also write in the Notes what the spec currently says and which source location it was read from, so the reviewer sees the misreading.
   - `OK`: list the sections covered.
   - `VISUAL`: feedback on how the prototype looks rather than on what it holds - size, colour, density, spacing, wording of a label the spec does not fix. Target is the SCR-ID or `whole prototype`, status `prototype-only`; the next `/speckit-idea-prototype` run picks it up and the spec never changes for it. If one sentence carries both lanes ("this table is too dense and the customer name is missing"), split it into a `VISUAL` item and a spec item.
   - **Collides with a standard**: if an item would drop or weaken a line tagged `[STD-…]`, keep the item and its type, and write into "Understood as" that it collides with that rule and cannot be applied as a spec change. Name the two ways out: meet the rule differently, or a signed exemption via `/speckit-idea-standards --exempt`. Do not silently reclassify it and do not promise the change.
   - Status for everything else: `proposed`.

6. **Confirm.**
   - Interactive: show the table, say which items are the prototype lane (`VISUAL`) and which are the spec lane, and ask: "Did I understand each item correctly? Reply `confirm`, correct by ID (`R1-02: also the detail screen`), `drop R1-05`, or `defer R1-03: <reason>`." Apply corrections to the round file. Dropped items stay with status `dropped` and the reason; deferred items get status `deferred` and the reason in Notes. Repeat until the reviewer says `confirm`. Then set all remaining `proposed` items to `confirmed`, set the header `Confirmation` to `confirmed by <reviewer> on <date>`, and tell the reviewer: "Run `/speckit-idea-apply R<n>`."
   - Headless: leave every item `proposed`, print the table, do not ask, and stop. The workflow shows the file at a human gate; `/speckit-idea-apply --gate-confirmed <run_id>` then records that approval.

7. **Report.** Round file path, counts per type, whether confirmation is done, next command.

## Rules

- Never modify `spec.md`, `CHANGELOG.md` or `decisions/` in this command.
- Never soften or reinterpret the reviewer's words in the Verbatim column.
- Do not derive changes from side remarks. If it is not clearly a request, make it a `QUESTION` back to the reviewer.
