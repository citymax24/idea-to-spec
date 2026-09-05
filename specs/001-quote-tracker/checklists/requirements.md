# Readiness Checklist: Quote Tracker

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: 0.3 · **Evaluated**: 2026-09-05

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

- Evaluated with a script over `spec.md` v0.3 after applying round R2: 8 JOB, 7 FLOW, 9 SCR, 30 FR, 7 SC, 25 assumptions (4 resolved: A-01, A-02, A-04, A-13; 1 removed: A-19), 16 items in §11 (C-01, C-02, Q-02, Q-11 resolved; 12 open). FR-007, FR-022 and FR-032 are background rules with no screen. 16 change markers `⟲ v0.3` on top of 29 `⟲ v0.2`. Every remaining flow starts and ends at an existing SCR; every remaining SCR is reached by a flow; no "Satisfies" list names a removed FR.
- **§13 now holds 5 tombstones**: FR-026, FR-027, FLOW-05, SC-005 (R2-01) and SCR-07 (R2-02), all pointing to `decisions/DEC-001.md`. The removed IDs appear outside §13 only in three pointers to §13: the §4 Out-of-scope line, the §7 group label "Quote amount" and A-19's "was used in" note. None is a live reference.
- **Decision check**: DEC-001 takes the hit rate out of version 1. A-03 (priorities 1 and 2 in version 1) was updated in v0.3 to except the hit rate, so no assumption contradicts the record. A-19 has nothing left to apply to and is marked removed. Q-01 stays open for the other priority-2 features.
- **`[NEEDS CLARIFICATION]` remains (2 markers)**: Q-01 (which priorities are in version 1, §4; the hit rate no longer counts among them) and Q-09 (mandatory fields when adding a quote, FR-002). Each carries a default assumption (A-03, A-11); the reviewer answers them in a later round.
- **Reviewed sections**: §1 (v0.1, R1-07); kept under review coverage by the R2-04 default (a), although its goal clause "the boss sees how many quotes become orders" is now delivered by nothing in version 1. Every other section either changed in v0.2 or v0.3 or has never been approved by a reviewer.
- **Round R2 status**: all items are `applied (v0.3)` or `answered`; nothing deferred, nothing dropped. R2 was confirmed via workflow gate `dry-run-simulated-gate-2` with Claude as the synthetic reviewer and no answers passed for R2-03 and R2-04, so the defaults (a) applied; no change in v0.3 is a human decision. A human still has to look at every R1 and R2 item, and at DEC-001, before acceptance.
- Source weights in `inputs/INVENTORY.md` are still proposals.
- The feature list (S2) has no rows for Nr 16–29. If those features exist, the draft is missing them; noted at the end of §11.
