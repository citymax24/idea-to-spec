# Readiness Checklist: Quote Follow-Up Tracker

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: 1.0 · **Evaluated**: 2026-09-05

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
- [x] Reviewed sections cover the whole spec, or the reviewer accepts explicitly without full coverage

## Notes

Evaluated mechanically against v0.2: 0 untagged lines, 0 clarification markers, 8 screens all complete (purpose, primary action, content, states, ≥1 FR, comes-from, leads-to), 7 flows all starting and ending at a catalogued screen, every screen reached by a flow, all 29 FRs mapped to a screen (24) or marked as a background rule (5), 8 entries under "Out of scope", and the only feedback item (R1-01) at `applied (v0.2)`. No decision records exist, so no assumption can contradict one.

**Review coverage — closed by acceptance, not by coverage.** yana accepted v0.2 as v1.0 on 2026-09-05 without a section-by-section review pass, knowingly and after being shown the three assumptions below.

**How that box stood before acceptance.** The header's "Reviewed sections" is `—`. Round R1 produced no `OK` item, so no section is on record as reviewed; the spec has never been published for a reading pass. This box cannot be ticked by fixing the spec. It closes either by a reviewer approving sections in a round, or by the reviewer accepting without full coverage knowingly, which is a decision only the human makes.

**What a reviewer would be accepting unread.** Three lines rest on assumption rather than a source:

- **FR-029 / A-06** — only the Chef administers users. R1-01 asked for the screen but named no role, and no source covers user administration at all. Derived from F-007 (S1 §2). The weakest line in the spec.
- **A-05 / Q-10** — who receives the seven-day reminder. Still the only open question; A-05 assumes the registering user and the office, derived from F-014 (S1 §4 "Bauleiter oder Büro ruft an").
- **FR-008 / A-02** — "abgesagt" and "verlaufen" also remove a quote from the open list. Only "zugesagt" is stated in S1 §4.

**One tension carried deliberately.** FR-021 (per-user login) stands against F-044, where the pilot customer says he already has twelve passwords and will not use the tool if he has to sign in every time. C-02 was resolved in favour of the login, so the constraint is recorded in §8 rather than dropped.
