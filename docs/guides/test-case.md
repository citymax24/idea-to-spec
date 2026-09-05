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

## Results (headless, `claude -p`, 2026-09-05)

| Step | Duration | Outcome |
|------|----------|---------|
| intake | ~2 min | S1–S4 assigned, all four converted, weights proposed (S1 high, S2 medium, S3 high, S4 medium), empty rows 17–30 in the spreadsheet flagged, transcript kind corrected by the agent |
| facts | ~6 min | 76 facts with locations, C-01 (trades) and C-02 (size band) found, 14 open questions with defaults including Q-11 (export vs import), login correctly listed as "checked and not a conflict" |
| draft | ~8 min | spec v0.1: 8 JOB, 8 FLOW, 10 SCR, 32 FR, 8 SC, 25 assumptions, 3 clarification markers; zero untagged lines; commit + tag `spec-quote-tracker-v0.1` |
| publish | ~1 min | `feedback/spec-review.html`, frozen `spec-v0.1.html`, `PUBLISHED.md` with a local path (no publishing tool in a headless run) |
| feedback R1 | ~3 min | `feedback/R1.md`: 7 items from 5 sentences (3 CHANGE, 1 MISREAD, 2 QUESTION of which one asked back by the AI, 1 OK); all `proposed`; spec untouched |
| apply R1 | ~10 min | v0.2, status in-review, 29 `⟲ v0.2` markers, changelog block with a trigger per row, §1 recorded as reviewed, tag `spec-quote-tracker-v0.2`; no tombstone because the "export" turned out to be already read as an import |
| feedback R2 | ~3 min | `feedback/R2.md`: 2 REMOVE (hit rate feature and its screen) plus 2 questions the AI asked back (what happens to the quote-amount field, and to the §1 goal sentence) |
| apply R2 | ~7 min | v0.3, tombstones for FR-026, FR-027, FLOW-05, SC-005, SCR-07 in §13, `decisions/DEC-001.md` with the reviewer's words and how the sources are read from now on, facts file updated ("Superseded by decisions"), tag `spec-quote-tracker-v0.3` |
| brief `--draft` | ~5 min | `design/brief.md` (DRAFT) with 9 screens in flow order, one design prompt each, "Do not show" from §4 and §13, and the gaps a designer would hit (Q-01, Q-09); `design/README.md` with the two-lane rule |

This run also predates the `standards/` registry. `specs/001-quote-tracker/` has never been bound: it carries no `standards/BOUND.md` and no `[STD-…]` tags, and it is still v0.3 `in-review`. Running `/speckit-idea-accept` on it today would meet the standards bullet of the readiness checklist for the first time and stop, because a `law` module that was never bound blocks. Binding it with `/speckit-idea-standards --bind` would produce v0.4 — which is a fine way to exercise the mechanism, and the reason it has not been done here is that nothing in this dry run is a human decision to begin with.

The brief step was removed from the loop after this run and replaced by `/speckit-idea-prototype`, which builds a clickable HTML prototype from the accepted spec instead of a document for a designer. `specs/001-quote-tracker/design/` was deleted with it; the run above is kept as the record of what the step produced. The prototype step has not been dry-run yet.

Three things worth knowing from this run:

- The "export" trap was already defused at draft time: the draft read the ambiguous row as an import, put the export under "Out of scope" and carried the ambiguity as Q-11. The reviewer's REMOVE therefore became a MISREAD item that resolves Q-11 rather than a tombstone. The round file documents what the spec said and where it was read from.
- Removing the login had a consequence the reviewer had not thought about (per-person views, reminders, assignment). The feedback step raised it as a question back (R1-04) instead of guessing. The same happened in round 2 for the quote-amount field that only existed for the removed hit rate (R2-03).
- Every gate in this run was simulated: Claude answered R1-04, R2-03 and R2-04 in the reviewer's role, and `--gate-confirmed` was passed by hand. The round files, the changelog and DEC-001 all say so. Nothing in `specs/001-quote-tracker/` is a human decision; a real reviewer must read R1 and R2 before that spec could ever be accepted.

## What was fixed because of the run

- Converter: real spreadsheet row numbers via openpyxl (re-executed under `uv run` when the system Python lacks it), stable S-IDs on a rerun, transcripts detected by name or timestamps.
- Commands: an explicit "interactive or headless" rule (`--headless`), the `--inbox` lane for workflow runs, `defer` during confirmation, version rules for re-acceptance, DEC numbering, Q-ID namespace, duplicate-safe re-intake.
- Workflow: `reviewer` is required, every step passes `--headless`, the round file is shown at the confirmation gate, the step after acceptance only runs when the spec is actually `accepted`.
