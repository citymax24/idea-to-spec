# Readiness Checklist: Quote Follow-Up Tracker

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: 1.2 · **Evaluated**: 2026-09-05

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

Re-evaluated against v1.2 after round R3: 0 untagged lines, 0 clarification markers, 8 screens complete, 7 flows anchored, all 33 FRs mapped to a screen or marked as a background rule, 8 entries under "Out of scope", all three rounds applied (R1-01 → v0.2, R2-01 → v1.1, R3-01 → v1.2), no open questions.

**Review coverage is open again.** The v1.1 acceptance covered v1.1; R3 changed FR-029 and added FR-031 to FR-033 after it. The spec is back at `in-review` until yana accepts v1.2.

**One assumption fewer.** A-06 ("only the Chef administers users") is retired. It was never backed by a source, and the reviewer found it by using the prototype: the refusal "the last Chef cannot be removed" showed that a single administrator locks a company out. FR-029 and SCR-08 now carry [R3-01], a human decision, instead of [ASSUMPTION].

**Assumptions still riding along**: A-05/FR-013/FR-030 (single recipient of the reminder — delegated to Claude, sources point both ways), A-02/FR-008 ("abgesagt" and "verlaufen" also leave the open list), A-01, A-03, A-04. FR-021 still stands against F-044 by the resolution of C-02.

**Design is behind the spec.** SCR-08 in the canvas and the Benutzer screen of the clickable prototype still show the v1.1 rule (Chef only, last Chef cannot be removed). They need rebuilding against FR-031 to FR-033 before the design matches again.
