# Readiness Checklist: Quote Tracker

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: 0.2 · **Evaluated**: 2026-09-05

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

- Evaluated with a script over `spec.md` v0.2 after applying round R1: 8 JOB, 8 FLOW, 10 SCR, 32 FR, 8 SC, 25 assumptions (4 resolved: A-01, A-02, A-04, A-13), 16 items in §11 (C-01, C-02, Q-02, Q-11 resolved; 12 open). FR-007, FR-022 and FR-032 are background rules with no screen. 29 change markers `⟲ v0.2`; no ID removed, so §13 stays empty.
- **`[NEEDS CLARIFICATION]` remains (2 markers)**: Q-01 (which priorities are in version 1, §4) and Q-09 (mandatory fields when adding a quote, FR-002). Q-02 was resolved in R1 and its marker removed. Each remaining marker carries a default assumption (A-03, A-11); the reviewer answers them in round 2.
- **Reviewed sections**: §1 (v0.1, R1-07). Every section except §1, §12 and §13 changed in v0.2 and none of them has been approved by a reviewer yet.
- **Round R1 status**: all items are `applied (v0.2)` or `answered`; nothing deferred, nothing dropped. R1 was confirmed via workflow gate `dry-run-simulated-gate` with Claude as the synthetic reviewer, so no change in v0.2 is a human decision; a human still has to look at every R1 item before acceptance.
- `decisions/` is empty (nothing removed yet), so the decision check passes trivially.
- Source weights in `inputs/INVENTORY.md` are still proposals. C-01 and C-02 are now resolved by R1-01 and R1-02 rather than by the weights, so a later weight change no longer flips A-01 or A-02.
- The feature list (S2) has no rows for Nr 16–29. If those features exist, the draft is missing them; noted at the end of §11.
