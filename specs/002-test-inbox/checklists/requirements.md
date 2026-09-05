# Readiness Checklist: Quote Follow-Up Tracker

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: 0.2 · **Evaluated**: 2026-09-05

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

- **`[NEEDS CLARIFICATION]` cleared in v0.2**: Q-11 (user management) was answered in round R1 and applied as SCR-08, FR-027 to FR-029. No clarification marker remains.
- **Reviewed sections still empty**: R1 produced no `OK` item, so no section is recorded as reviewed. This is cleared when a reviewer approves sections in a later round, or explicitly accepts without full coverage at `/speckit-idea-accept`.
- **Deferred feedback items**: none in R1.
- **Open assumptions a reviewer should look at**:
  - **A-06 / FR-029** — only the Chef administers users. R1-01 asked for the screen but named no role, and no source covers user administration; this is derived from F-007 (S1 §2). It is the weakest line in v0.2.
  - **A-05 / Q-10** — who receives the seven-day reminder. Still open, derived from F-014 (S1 §4 "Bauleiter oder Büro ruft an").
  - **FR-021 vs F-044** — the per-user login stands against the pilot customer's "twelve passwords already, then I won't use it" (S3 09:10). Resolved in favour of the login by C-02; the constraint stays recorded in §8.
