# Source Inventory

Feature: `standards/accessibility-eaa` · Last intake: 2026-09-05

IDs are stable. A source keeps its ID forever, even if it is later judged irrelevant.
Weight is set by the human and decides which source wins when two conflict: `high | medium | low`. Rows marked `(proposed)` are the AI's suggestion and still need confirmation.

This is a **standards module**, so the ID namespace is `EAA`, not `S`. A citation `[EAA4 Art. 4]` resolves against this inventory and never against an idea's own sources. Checksums and licence position for every file are in `SOURCES.md`.

Citation formats: `EAA1 § 3` · `EAA4 Art. 4(3)` · `EAA4 Annex I § I` · `EAA5 SC 1.4.3` · `EAA2 § 2`

| ID | File | Kind | Date | From | Content in one sentence | Weight |
|----|------|------|------|------|-------------------------|--------|
| EAA1 | `BFSG.pdf` | document | 2021-07-16, last amended 2024-05-06 | Bundesministerium der Justiz (gesetze-im-internet.de) | German transposition of the EAA: who is bound, which products and services, the accessibility obligation, the disproportionate-burden and micro-enterprise relief, market surveillance | medium (proposed) |
| EAA2 | `BFSGV.pdf` | document | 2022-06-15, amended 2026-07-10 | Bundesministerium der Justiz (gesetze-im-internet.de) | The regulation that makes the BFSG's accessibility requirements concrete for products and services | medium (proposed) |
| EAA3 | `EAA-Directive-2019-882-DE.html` | document | 2019-04-17 | EUR-Lex, Publications Office of the EU | German-language text of the same directive as EAA4; kept for terminology, never cited as independent corroboration | low (proposed) |
| EAA4 | `EAA-Directive-2019-882-EN.html` | document | 2019-04-17, applies from 2025-06-28 | EUR-Lex, Publications Office of the EU | Directive (EU) 2019/882: scope, definitions, the accessibility requirements in Annex I, the disproportionate-burden criteria in Annex VI | medium (proposed) |
| EAA5 | `WCAG-2.1-Recommendation.html` | document | 2025-05-06 (latest revision) | W3C, Accessibility Guidelines Working Group | The success criteria at levels A, AA and AAA that EN 301 549 incorporates by reference for web content — the only source here that is directly testable | high (proposed) |

The weights follow the rule that the concrete outranks the abstract where they overlap. A success criterion states a testable threshold; a directive article states an aim. Where EAA5 and EAA4 speak about the same thing, EAA5 decides what is checked and EAA4 decides whether it is owed at all.

EAA3 is deliberately `low`: it is the same instrument as EAA4 in another language, not a second opinion.

## Needs attention

- **EN 301 549 V3.2.1 is not in this inventory** because it is not stored (ETSI copyright, see `SOURCES.md`). It is the document that formally binds WCAG 2.1 level AA into European law, so its absence is a real gap in the citation chain: claims that would cite it cite EAA5 for the criterion and EAA4/EAA1 for the obligation instead. Fetch it locally when working on this module.
- **EAA2 was amended on 2026-07-10**, two months before this intake. The amendment is included in the stored text, but nobody has yet checked what it changed.
