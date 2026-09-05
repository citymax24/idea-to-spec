# Readiness Checklist: [IDEA NAME]

**Purpose**: Decide whether the spec is ready for design. The AI evaluates, the human accepts.
**Spec version**: [0.x] · **Evaluated**: [YYYY-MM-DD]

## Provenance

- [ ] Every JOB, FLOW, SCR, FR, SC and constraint line ends with a provenance tag (source, feedback item, or ASSUMPTION)
- [ ] No `[NEEDS CLARIFICATION]` markers remain
- [ ] No assumption contradicts a decision record in `decisions/`

## Screens and flows

- [ ] Every SCR has purpose, primary action, content, states, at least one FR in "Satisfies", and comes-from / leads-to
- [ ] Every FLOW starts and ends at an SCR from the catalog
- [ ] Every SCR is reached by at least one FLOW
- [ ] Every FR maps to at least one SCR or is marked "no screen (background rule)"

## Scope and review

- [ ] §4 "Out of scope" is not empty
- [ ] No feedback item is `proposed` or `confirmed` without being applied
- [ ] Deferred feedback items are listed in §11 with a reason
- [ ] Reviewed sections cover the whole spec, or the reviewer accepts explicitly without full coverage

## Notes

- [Failing items and what would fix them]
