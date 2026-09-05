# Prototype Checklist: [IDEA NAME]

**Purpose**: Decide whether the prototype is a faithful, complete rendering of the accepted spec. The AI evaluates, the human accepts.
**Spec version**: [1.x] · **Prototype built**: [YYYY-MM-DD] · **Evaluated**: [YYYY-MM-DD]

## Coverage

- [ ] Every SCR in §6 of the spec exists as a screen in the prototype, badged with its SCR-ID
- [ ] Every FLOW in §5 can be clicked from its first screen to its last
- [ ] Every screen's primary action is present and leads where "Leads to" says
- [ ] Every state listed for a screen can be shown

## Fidelity

- [ ] No screen, field, column, action or rule appears that the spec does not contain
- [ ] Nothing from §4 "Out of scope" or from a §13 tombstone is shown
- [ ] Labels are in the UI language §8 fixes, and terms §8 pins down appear verbatim
- [ ] Device context per §8 is respected (phone-context screens in a phone frame, desktop screens wide)

## Standards

Skip this block when the project has no `standards/` registry. The rule-by-rule verdicts live in `checklists/standards.md`; these boxes are the summary.

- [ ] Every `required` rule of a `law` module whose `Bites` includes `prototype` is `pass`, with named evidence, or exempted
- [ ] Contrast ratios were measured on the colours the prototype actually uses, not asserted
- [ ] Every flow is walkable by keyboard alone, with a visible focus indicator throughout
- [ ] Corporate-design tokens and assets are the only styling input, and every embedded asset has a cleared licence row
- [ ] Substituted assets and decisions made without cover (draft module) are named in the prototype report

## Currency

- [ ] The prototype was built from the current spec version, not an older one
- [ ] No prototype feedback item is `proposed` or `confirmed` without being applied or deferred
- [ ] The spec is `accepted` at the version the prototype was built from
- [ ] No bound module has moved since the prototype was built

## Notes

- [Failing items and what would fix them]
