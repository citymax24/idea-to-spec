# Readiness Checklist: Quote Follow-Up Tracker

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: 1.1 · **Evaluated**: 2026-09-05

## Provenance

- [x] Every JOB, FLOW, SCR, FR, SC and constraint line ends with a provenance tag (source `S#`, fact `F-###`, resolved `C-##`/`Q-##`, feedback `R#-##`, or `ASSUMPTION`)
- [x] No `[NEEDS CLARIFICATION]` markers remain
- [x] No assumption contradicts a decision record in `decisions/`

## Screens and flows

- [x] Every SCR has purpose, primary action, content, states, at least one FR in "Satisfies", and comes-from / leads-to
- [x] Every FLOW starts and ends at an SCR from the catalog
- [x] Every SCR is reached by at least one FLOW
- [x] Every FR maps to at least one SCR or is marked "no screen (background rule)"

## Scope and review

- [x] §4 "Out of scope" is not empty
- [x] No feedback item is `proposed` or `confirmed` without being applied
- [x] Deferred feedback items are listed in §11 with a reason
- [ ] Reviewed sections cover the whole spec, or the reviewer accepts explicitly without full coverage

## Notes

Re-evaluated against v1.1 after round R2: 0 untagged lines, 0 clarification markers, 8 screens complete, 7 flows anchored, all 30 FRs mapped to a screen (25) or marked as a background rule (5), 8 entries under "Out of scope", both rounds fully applied (R1-01 → v0.2, R2-01 → v1.1), and §11 now carries no open question at all.

**Review coverage is open again.** The v1.0 acceptance covered v1.0. R2 changed FR-013, added FR-030 and rewrote A-05 after that acceptance, so the spec is back at `in-review` and the box reopens until yana accepts v1.1.

**The one line a re-acceptance should look at.** FR-013 / FR-030 / A-05 rest on a decision the reviewer delegated to Claude rather than made. The sources point both ways and the assumption says so: F-037 and F-043 argue for a single recipient, F-014 (S1 §4 "Bauleiter oder Büro ruft an") names both roles as callers. If that trade-off deserves a human's judgement, this is the moment.

**Other assumptions unchanged from v1.0**: A-06/FR-029 (only the Chef administers users, no source names a role) and A-02/FR-008 ("abgesagt" and "verlaufen" also leave the open list, where only "zugesagt" is stated). FR-021 still stands against F-044 by the resolution of C-02.
