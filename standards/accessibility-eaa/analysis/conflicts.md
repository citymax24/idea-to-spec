# Conflicts

Feature: `standards/accessibility-eaa` · 2026-09-05

Real contradictions between sources. The AI does not decide them. Unresolved conflicts become tagged assumptions in the spec (higher-weight source wins) and appear under Open Questions.

| ID | Claim A | Claim B | What differs | Source weights | Question to the human | Resolution |
|----|---------|---------|--------------|----------------|-----------------------|------------|
| — | — | — | — | — | — | — |

Resolution values: `open` · `Resolved: <answer> (human, YYYY-MM-DD)` · `Deferred: <reason>`

## No contradictions found

Across the parts of EAA1, EAA2, EAA4 and EAA5 that were read, no two sources make claims that cannot both be true. That is the expected result and not a sign the check was skipped: EAA1 and EAA2 are the German transposition of EAA4, so they are meant to agree, and EAA5 is the technical criterion set the other three point at rather than a competing account.

What the sources do show is a **difference in level of detail**, which the template is explicit is not a conflict:

| Level | Source | What it fixes |
|-------|--------|---------------|
| Obligation | EAA4 Art. 4, Annex I § III(c); EAA1 § 3 | *that* a website or app must be perceivable, operable, understandable and robust |
| Concretisation | EAA2 § 3, § 12 | that the state of the art decides *how*, and that the federal office publishes which standards apply |
| Test | EAA5 | *what exactly* is measured — 4.5:1, a label bound to its field, a visible focus indicator |

That chain has one link this module cannot cite, because the document is not in the repository: EN 301 549 is what formally binds WCAG level AA into the European obligation. Everything here therefore cites EAA5 for the criterion and EAA4 or EAA1 for the duty, with the bridge between them asserted rather than quoted. That is recorded as Q-03 in `open-questions.md`, not as a conflict, because no source contradicts another — one source is simply absent.
