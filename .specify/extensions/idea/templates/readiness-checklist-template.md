# Readiness Checklist: [IDEA NAME]

**Purpose**: Decide whether the spec is ready to be accepted and built into a prototype. The AI evaluates, the human accepts.
**Spec version**: [0.x] · **Evaluated**: [YYYY-MM-DD]

## Provenance

- [ ] Every JOB, FLOW, SCR, FR, SC and constraint line ends with a provenance tag (source `S#`, fact `F-###`, resolved `C-##`/`Q-##`, feedback `R#-##`, or `ASSUMPTION`)
- [ ] No `[NEEDS CLARIFICATION]` markers remain
- [ ] No assumption contradicts a decision record in `decisions/`

## Screens and flows

- [ ] Every SCR has purpose, primary action, content, states, at least one FR in "Satisfies", and comes-from / leads-to
- [ ] Every FLOW starts and ends at an SCR from the catalog
- [ ] Every SCR is reached by at least one FLOW
- [ ] Every FR maps to at least one SCR or is marked "no screen (background rule)"

## Standards

Skip this block when the project has no `standards/` registry.

- [ ] The spec is bound to every module that applies, at that module's current version (`standards/BOUND.md`)
- [ ] No `law` module has moved since the bind
- [ ] Every `required` rule of a `law` module is `pass` or carries a signed exemption (`decisions/EXM-*.md`)
- [ ] Conflicts between modules are recorded with a resolution, not left open
- [ ] Warnings from internal modules are listed below and the reviewer accepts them knowingly
- [ ] Rules reported `not verifiable` are named, with what would make them verifiable

## Scope and review

- [ ] §4 "Out of scope" is not empty
- [ ] No feedback item is `proposed` or `confirmed` without being applied
- [ ] Deferred feedback items are listed in §11 with a reason
- [ ] Reviewed sections cover the whole spec, or the reviewer accepts explicitly without full coverage

## Notes

- [Failing items and what would fix them]
- [Standards warnings the reviewer is accepting knowingly, one line each]
