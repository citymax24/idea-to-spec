# Rules: STD-A11Y · Accessibility (EAA / BFSG, EN 301 549 → WCAG 2.1 AA)

Module version 1.0 · written against EN 301 549 v3.2.1 · see `standard.yml` for scope and the outstanding legal review.

Each rule carries four fields:

- **Severity** — `required` (inside the bound conformance level, WCAG 2.1 AA) or `recommended` (above it; never a blocker).
- **Bites** — `spec` (decidable while writing the spec), `prototype` (checkable in the built prototype), `build` (only checkable in real software; recorded here so nobody claims the prototype proved it).
- **Shapes the spec** — whether `--bind` materialises this rule as a tagged line inside the spec (a state, a content element, an FR) or leaves it in the registry as a check only.
- **Source** — the criterion it comes from. WCAG numbers are success criteria of WCAG 2.1.

---

### STD-A11Y-001 · The UI language is declared and stated in the spec

The spec names the UI language in §8; the prototype declares it on the root element, and any passage in another language is marked.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — §8 "Language" may not be empty or an untagged assumption
- **Check**: §8 names a language; `<html lang>` is set; passages in another language carry their own `lang`
- **Source**: WCAG 2.1 SC 3.1.1 Language of Page (A), SC 3.1.2 Language of Parts (AA)

### STD-A11Y-002 · Every screen has a unique, descriptive title

Each SCR has a name that says what the screen is, not what it is called internally, and the prototype shows it as the document title and the first heading.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: no — §6 already requires a screen name; this rule makes it a checked one
- **Check**: no two SCRs share a name; every prototype screen exposes its name as an `h1`
- **Source**: WCAG 2.1 SC 2.4.2 Page Titled (A)

### STD-A11Y-003 · Structure is carried by markup, not by looks

Landmarks (`header`, `nav`, `main`, `footer`), headings in order without skipping a level, lists as lists, tables with real header cells.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: one `main` per screen; heading levels do not skip; every table in a §6 content list is a `table` with `th` and a `caption` or accessible name
- **Source**: WCAG 2.1 SC 1.3.1 Info and Relationships (A)

### STD-A11Y-004 · Text contrast is at least 4.5:1

Body text at least 4.5:1 against its background; text from 18.66 px bold or 24 px at least 3:1.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no — but it is the rule that most often collides with a corporate-design colour, and that collision is resolved in favour of this one
- **Check**: every foreground/background pair used for text in the prototype computes to the ratio; state the measured value, do not assert it
- **Source**: WCAG 2.1 SC 1.4.3 Contrast (Minimum) (AA)

### STD-A11Y-005 · Interface and focus contrast is at least 3:1

Borders of inputs, icons that carry meaning, the focus indicator, and the parts of a graphic needed to understand it.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: input borders, meaningful icons and the focus ring reach 3:1 against their surroundings
- **Source**: WCAG 2.1 SC 1.4.11 Non-text Contrast (AA)

### STD-A11Y-006 · Nothing means anything by colour alone

A status, an error, a required field or a difference in a chart is never carried by colour on its own; there is a word, a shape or a pattern next to it.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — a §6 content element described only as a coloured marker gains its text label in the spec
- **Check**: every colour-coded element in the prototype has a non-colour carrier; in greyscale the screen still reads
- **Source**: WCAG 2.1 SC 1.4.1 Use of Color (A)

### STD-A11Y-007 · Every form field has a visible, associated label

The label is visible text, not only a placeholder, and it is bound to the field. Required fields say so in text.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — a screen whose §6 content contains form fields gets those fields named in the spec, not left as "a form"
- **Check**: every input has a `label for`; no field relies on a placeholder as its label; required fields are marked in text as well as programmatically
- **Source**: WCAG 2.1 SC 3.3.2 Labels or Instructions (A), SC 1.3.1 (A), SC 4.1.2 Name, Role, Value (A)

### STD-A11Y-008 · Errors are named in text and say how to fix them

An error identifies the field it belongs to, in words, near the field, and suggests the correction where one is knowable.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — every SCR that takes input lists an error state, and that state is field-level text, not a banner alone
- **Check**: the prototype's error state per input screen shows text at the field; the message says what to do
- **Source**: WCAG 2.1 SC 3.3.1 Error Identification (A), SC 3.3.3 Error Suggestion (AA)

### STD-A11Y-009 · Everything is operable by keyboard, with no trap

Every action a screen offers can be reached and triggered from the keyboard, and focus can always leave a component.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — as a functional requirement, because it constrains what a screen may demand (no drag-only interaction without an alternative)
- **Check**: every primary action and every navigation step in the prototype is reachable by Tab and triggered by Enter or Space; no component holds focus
- **Source**: WCAG 2.1 SC 2.1.1 Keyboard (A), SC 2.1.2 No Keyboard Trap (A)

### STD-A11Y-010 · Focus is visible and its order follows the flow

The focused element is always plainly visible, and the tab order runs in the reading order of the screen and of the FLOW.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: no `outline: none` without a replacement; tabbing through a screen follows its visual order; the order matches the FLOW the screen sits in
- **Source**: WCAG 2.1 SC 2.4.7 Focus Visible (AA), SC 2.4.3 Focus Order (A)

### STD-A11Y-011 · Every image and icon has a text alternative

Meaningful images carry a description; decorative ones are hidden from assistive technology instead of getting an empty-sounding name.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — a §6 content element that is an image gets, in the spec, what the image has to convey
- **Check**: every `img` has `alt`; decorative graphics are `alt=""` or `aria-hidden`; icon-only buttons have an accessible name
- **Source**: WCAG 2.1 SC 1.1.1 Non-text Content (A)

### STD-A11Y-012 · Content reflows and text can be enlarged

At 320 CSS px width there is no two-dimensional scrolling, and text survives being enlarged to 200% without loss of content or function.

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no — but a §8 device context of "phone on site" makes it the first thing to check
- **Check**: the prototype at 320 px scrolls in one direction only; at 200% text zoom nothing is cut off or overlapped
- **Source**: WCAG 2.1 SC 1.4.10 Reflow (AA), SC 1.4.4 Resize Text (AA)

### STD-A11Y-013 · Status messages are announced without stealing focus

"Saved", "3 results", "upload failed" reach assistive technology without the user having to find them and without focus jumping.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — the loading and success states a screen lists in §6 are what this rule attaches to
- **Check**: status output uses a live region; focus does not move when a status appears
- **Source**: WCAG 2.1 SC 4.1.3 Status Messages (AA)

### STD-A11Y-014 · Time limits are adjustable, and nothing flashes

No session or interaction limit that cannot be turned off, extended or generously set, and no content flashing more than three times a second.

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — if the spec introduces a timeout anywhere, it must state how the user extends it
- **Check**: no time limit in the spec without an extension path; nothing in the prototype flashes
- **Source**: WCAG 2.1 SC 2.2.1 Timing Adjustable (A), SC 2.3.1 Three Flashes or Below Threshold (A)

### STD-A11Y-015 · The product says what it does about accessibility

There is a reachable place stating which requirements are met, where the known gaps are, and how a user reports a barrier.

- **Severity**: required
- **Bites**: spec · build
- **Shapes the spec**: yes — as a screen or a functional requirement, so it is not remembered on launch day
- **Check**: the spec contains the statement and a feedback channel for barriers
- **Source**: EAA information duties (Directive (EU) 2019/882, Annex I) as transposed nationally. The exact form and wording is the part of this module most in need of the legal review named in `standard.yml`.

---

## Above the bound level

Not blockers. Recorded because the next EN 301 549 version is expected to reference WCAG 2.2, which would make the first two `required`.

### STD-A11Y-101 · Touch targets are at least 24 × 24 px

- **Severity**: recommended
- **Bites**: prototype
- **Shapes the spec**: no
- **Source**: WCAG 2.2 SC 2.5.8 Target Size (Minimum) (AA) — outside WCAG 2.1 AA, the level bound here

### STD-A11Y-102 · Anything done by dragging can also be done by a single tap

- **Severity**: recommended
- **Bites**: spec · prototype
- **Shapes the spec**: no
- **Source**: WCAG 2.2 SC 2.5.7 Dragging Movements (AA) — outside the bound level

### STD-A11Y-103 · Help is in the same place on every screen that offers it

- **Severity**: recommended
- **Bites**: spec
- **Shapes the spec**: no
- **Source**: WCAG 2.2 SC 3.2.6 Consistent Help (A) — outside the bound level
