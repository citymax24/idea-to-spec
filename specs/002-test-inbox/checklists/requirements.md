# Readiness Checklist: Quote Follow-Up Tracker

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: 0.1 · **Evaluated**: 2026-09-05

## Provenance

- [x] Every JOB, FLOW, SCR, FR, SC and constraint line ends with a provenance tag (source `S#`, fact `F-###`, resolved `C-##`/`Q-##`, feedback `R#-##`, or `ASSUMPTION`)
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

- **`[NEEDS CLARIFICATION]` remains — 1 marker, on Q-11 (§11)**: the resolution of C-02 puts a per-user login into version 1, which implies accounts that somebody creates and removes. No source covers user management, and guessing it would either invent a screen or silently drop one, so it stays a marker. It is fixed by one answer: does version 1 administer users, and who does it.
- **Reviewed sections empty**: no review round has run yet. This is expected at v0.1 and is cleared by `/speckit-idea-publish` followed by `/speckit-idea-feedback`.
- **Deferred feedback items**: none exist yet; the box holds because §11 carries no deferred item, not because a review has happened.
- **Watch in review**: FR-021 (per-user login) stands against F-044 (S3 09:10), where the pilot customer says he will not use the tool if he has to sign in every time. The conflict was resolved in favour of the login, so the constraint is recorded in §8 rather than dropped, but it is the most likely thing a reviewer will push back on.
