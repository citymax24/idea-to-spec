# Sources: accessibility-eaa

Where the rules of this module come from. Retrieved 2026-09-05. Checksums are SHA-256 of the file as downloaded, so a later change to a source is detectable rather than assumed.

The proposed weights follow the rule that the concrete outranks the abstract where they overlap: a testable success criterion beats a recital. They are a proposal for `inputs/INVENTORY.md`, to be confirmed by a human at intake like any other source weighting.

| ID | Proposed weight | Document | Version / status | Stored | SHA-256 |
|----|-----------------|----------|------------------|--------|---------|
| EAA5 | high | WCAG 2.1 | W3C Recommendation, latest revision 2025-05-06 | `raw/WCAG-2.1-Recommendation.html` | `233ac31974ce8575c08932ee1bd71c93879cf9b8426b2bc9b961b3ea8afb8ab6` |
| — | high | EN 301 549 V3.2.1 | ETSI, 2021-03 | **not stored — see below** | `1eee3a1841a94567da8e59f3b19a782ce9ab081c386b6a2a763b8cde13ff5b49` |
| EAA1 | medium | BFSG | Barrierefreiheitsstärkungsgesetz, gesetze-im-internet.de | `raw/BFSG.pdf` | `af2398b7e1fbf694d7966091df75aafa8339e93e4e3ec804ad08194d6bac33c4` |
| EAA2 | medium | BFSGV | Verordnung zum BFSG | `raw/BFSGV.pdf` | `f4a351b5e9379a394fd4f35d27b1cfc032b6544c8b9cf766269da9fecabe72dd` |
| EAA4 | medium | Directive (EU) 2019/882 (EAA), English | adopted 2019-04-17, applies from 2025-06-28 | `raw/EAA-Directive-2019-882-EN.html` | `52be6dbfa4c480f16e4b69271cff305701046e7f420b0b762a44e7a3ba21e6b9` |
| EAA3 | reference | Directive (EU) 2019/882 (EAA), German | same instrument | `raw/EAA-Directive-2019-882-DE.html` | `7793b85de9bed22f3b0c5d999d40b994c4b66f5a38bc7b2a1b2068b6dc268753` |

Source IDs come from `convert_inputs.py --prefix EAA`, so this module's sources are `EAA1…EAA5` and can never be confused with the `S1…Sn` of an idea. A citation `[EAA4 Art. 4]` resolves here and nowhere else.

The German directive text is the same instrument as the English one, not a second source. It is kept for terminology, so a German UI label can be traced to the wording the law itself uses. It must never be cited as independent corroboration of the English text.

## Retrieval

```bash
curl -sSL -o raw/EAA-Directive-2019-882-EN.html "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019L0882"
curl -sSL -o raw/EAA-Directive-2019-882-DE.html "https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32019L0882"
curl -sSL -o raw/BFSG.pdf   "https://www.gesetze-im-internet.de/bfsg/BFSG.pdf"
curl -sSL -o raw/BFSGV.pdf  "https://www.gesetze-im-internet.de/bfsgv/BFSGV.pdf"
curl -sSL -o raw/WCAG-2.1-Recommendation.html "https://www.w3.org/TR/WCAG21/"
```

## Why the directive is stored as HTML and not as PDF

The EUR-Lex PDF was tried first and rejected. Its text layer does not come out: the converter reads the PDF's bookmarks, succeeds, and returns 5 KB of table of contents from an 850 KB document — a file that looks like a source and cites like a source while containing almost none of the law. The EUR-Lex HTML rendition of the same CELEX document converts to 186 KB of actual articles and recitals.

This is the reason `convert_inputs.py` now reports a `thin` status: a large source whose conversion yields under 5 % of its size is flagged instead of being passed off as converted. The two national statutes are kept as PDF because gesetze-im-internet.de PDFs do carry a readable text layer — 100 KB out of 162 KB for the BFSG.

## Why EN 301 549 is not in this repository

This repository is public. EU legislation is reusable under the Commission's reuse decision, German statutes are `amtliche Werke` under §5 UrhG and carry no copyright, and WCAG 2.1 is published under the W3C Document License, which permits redistributing the unmodified document. All of those can be stored here.

ETSI deliverables cannot. EN 301 549 is free to **download** but remains ETSI's copyright; the notice in the PDF itself limits reproduction and forbids modification without ETSI's written authorisation. Committing a 2.3 MB copy of it into a public repository is not covered by that.

So the module carries the reference, not the file. Fetch it locally when working on this module:

```bash
curl -sSL -o raw/en_301549v030201p.pdf \
  "https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf"
shasum -a 256 raw/en_301549v030201p.pdf   # must match the checksum in the table above
```

`raw/.gitignore` keeps it out of commits if it is present locally.

The practical loss is smaller than it looks: EN 301 549 incorporates WCAG 2.1 level AA **by reference** for web content, and WCAG 2.1 itself is stored here in full. What the ETSI document adds beyond that — the ICT requirements for hardware, documentation and support services, and the clause-by-clause mapping — is what has to be read from the fetched copy.

## Version watch

EN 301 549 V3.2.1 (WCAG 2.1 AA) is the version in force and the one this module is written against. A revision referencing WCAG 2.2 has been expected since 2025; it was **not** published at the time of retrieval. When it appears and is cited in the Official Journal, this module's `review_by` date is the trigger to re-derive the rules, bump the module version, and let every bound idea drift into a deliberate decision.
