# Test case: quote tracker (dry run, 2026-09-05)

A synthetic idea used to run the loop once end to end before a real one. All inputs were generated for this purpose; the "reviewer feedback" in round 1 was written by Claude in the reviewer role, not by a human. Nothing in `specs/001-quote-tracker/` is a real product decision.

## The idea

A tool for small landscaping firms to keep track of sent quotes: which are open, when to follow up, what the customer said. Inputs are in German because real inputs will be.

## Inputs (`examples/quote-tracker/inbox/`)

| File | Kind | What it contains | Planted trap |
|------|------|------------------|--------------|
| `2026-08-12_Kickoff_Notizen.md` | meeting notes | problem, target group (GaLaBau, 5–50 staff), three roles, must-haves, flow, explicit non-goals, open questions | — |
| `Marktueberblick_v3.pptx` | 6 slides | competitors, price ranges, target group, customer demands, next steps | slide 4 widens the target group to all trades and 3–100 staff, contradicting the kickoff |
| `Feature_Liste.xlsx` | spreadsheet, 2 sheets | 15 features with priority and origin, roles sheet | row 31 is titled "Export nach Excel" but describes a one-time import of the old list |
| `Kundengespraech_Weber_Transkript.txt` | call transcript with timestamps | customer objections: no typing, one reminder, no login, gloves on site, price ceiling | login rejection vs. per-user views in the feature list |

## What the run should show

- Intake assigns S1–S4, converts all four, proposes weights, flags the empty rows in the spreadsheet.
- Facts finds the slide-4 conflict (C-01/C-02), carries the export/import ambiguity as an open question, and does not treat login as a conflict.
- Draft tags every line, keeps the unresolved conflicts as assumptions in favour of the kickoff notes (higher weight), and puts the ambiguous export in as an assumption or question.
- Round 1 (`examples/quote-tracker/feedback-round1.txt`) exercises all six item types: CHANGE (target group), ADD/CHANGE (no login in v1), REMOVE + MISREAD (export), QUESTION (offline), OK (problem and goal).
- Apply produces v0.2 with change markers, one tombstone, one decision record and a changelog block naming R1-xx per change.

## Results

Filled in below after the run.
