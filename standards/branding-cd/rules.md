# Rules: STD-CD · Corporate Design

Module version 0.1 · **status draft** · self-versioned.

> This module is a skeleton. The rule IDs, the fields and the wiring are real; the values are `[FILL: ...]` placeholders taken from nothing. While `standard.yml` says `status: draft`, `/speckit-idea-standards --check` reports every rule here as **not verifiable** and the prototype reports which visual decisions it had to make on its own. Nothing in this module can be reported as passed until it is filled and set to `active`.

Field meanings are the same as in every module: **Severity** `required` | `recommended`, **Bites** `spec` | `prototype` | `build`, **Shapes the spec** whether `--bind` writes it into the spec as a tagged line.

Internal authority: every rule here loses against a `law` rule it contradicts. The loss is recorded in the idea's `standards/BOUND.md`, not argued each time.

---

### STD-CD-001 · The logo is used as delivered

The approved file, unaltered: not redrawn, not recoloured, not stretched, not set in a box it was not made for.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: the prototype embeds `assets/[FILL: logo-primary.svg]` inline and applies no transform to it beyond uniform scaling
- **Source**: CD manual [FILL: section]

### STD-CD-002 · The logo keeps its clear space and minimum size

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: clear space `[FILL: e.g. 1x cap height on all sides]`, minimum `[FILL: e.g. 24 px height on screen]`
- **Source**: CD manual [FILL: section]

### STD-CD-003 · Colour comes from the tokens, never from a raw value

Every colour in the prototype resolves to a name in `assets/tokens.json`. A hex value written directly into a screen is a defect even when it happens to match.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: no literal colour in the prototype outside the token block at the top of the file
- **Source**: CD manual [FILL: section]

### STD-CD-004 · Only approved foreground/background pairings are used

The manual fixes which text colour may sit on which surface. This is the rule that collides with `STD-A11Y-004`: a pairing the manual allows but that measures below 4.5:1 may not be used for text, and the pairing is recorded as unusable in the idea's binding.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: every text pairing is in the approved list **and** clears the contrast rule; conflicts resolve in favour of `STD-A11Y-004`
- **Source**: CD manual [FILL: section]

### STD-CD-005 · Typography follows the fixed families, weights and scale

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: headline and body families as in `tokens.json`; only the weights the manual names; sizes from the scale
- **Source**: CD manual [FILL: section]

### STD-CD-006 · Fonts are embedded only when the licence allows it

A licensed typeface goes into the prototype as a subset `data:` URI, and only when `assets/README.md` records it as cleared for embedding. Otherwise the fallback stack is used and the substitution is reported.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: every embedded face has a cleared row in `assets/README.md`; uncleared faces are absent and their substitution is named in the prototype report
- **Source**: CD manual [FILL: section] · font licence [FILL: foundry, licence type]

### STD-CD-007 · Spacing, radii and elevation come from the scale

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: no spacing, corner radius or shadow outside the values in `tokens.json`
- **Source**: CD manual [FILL: section]

### STD-CD-008 · The product is named the way the manual spells it

One spelling, one capitalisation, everywhere, including inside sentences.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — the spec's product name and any name in a screen label follow the manual
- **Check**: the exact string `[FILL: product name]` appears; no variant spelling anywhere
- **Source**: CD manual [FILL: section]

### STD-CD-009 · The address form and tone are the ones the manual fixes

`[FILL: e.g. formal "Sie" throughout, sentence case for buttons, no exclamation marks]`.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — §8 "Brand / tone" carries the address form, so screen labels are written to it from the start
- **Check**: every label and message in the prototype uses the fixed address form and casing
- **Source**: CD manual [FILL: section]

### STD-CD-010 · Icons and imagery follow the fixed style

- **Severity**: recommended
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: one icon family, the stroke weight the manual names; no stock imagery in a prototype unless it is licensed and cleared like a font
- **Source**: CD manual [FILL: section]
