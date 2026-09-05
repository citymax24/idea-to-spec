# Readiness Checklist: Quote Tracker

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: 0.1 · **Evaluated**: 2026-09-05

## Provenance

- [x] Every JOB, FLOW, SCR, FR, SC and constraint line ends with a provenance tag (source, feedback item, or ASSUMPTION)
- [ ] No `[NEEDS CLARIFICATION]` markers remain
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

- Evaluated with a script over `spec.md` v0.1 (pass 1 of 3, no fixes needed): 8 JOB, 8 FLOW, 10 SCR, 32 FR, 8 SC, 25 assumptions, 16 open items in §11 (C-01, C-02, Q-01–Q-14). FR-007, FR-022 and FR-032 are background rules with no screen.
- **`[NEEDS CLARIFICATION]` remains (3 markers)**: Q-01 (which priorities are in version 1, §4), Q-02 (identity without repeated sign-in, FR-029) and Q-09 (mandatory fields when adding a quote, FR-002). These change scope and cannot be settled from the sources; the reviewer answers them in round 1. Each carries a default assumption (A-03, A-04, A-11) so the draft is complete without them.
- **Reviewed sections**: none yet; no review round has happened. Fixed by `/speckit-idea-publish` and the first feedback round.
- `decisions/` is empty, so the decision check passes trivially.
- Source weights in `inputs/INVENTORY.md` are still proposals; C-01 and C-02 are resolved in the draft by the proposed weights (S1 high over S4 medium). If the reviewer lowers S1 or raises S4, A-01 and A-02 flip.
- The feature list (S2) has no rows for Nr 16–29. If those features exist, the draft is missing them; noted at the end of §11.
