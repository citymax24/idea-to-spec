---
name: speckit-idea-prototype
description: Build a clickable HTML prototype directly from the accepted spec - one screen per SCR-ID, navigation along the FLOWs, states from the spec - and publish it as a private page the reviewer can click through and comment on.
compatibility: Requires spec-kit project structure with .specify/ directory
metadata:
  author: github-spec-kit
  source: idea:commands/speckit.idea.prototype.md
---

## User Input

```text
$ARGUMENTS
```

Arguments: `[--draft] [--feature <specs/NNN-dir>] [--headless]`. `--draft` allows a prototype from a spec that is not `accepted` (an early look, or a rebuild inside a review round). It only lifts the requirement: the DRAFT marker appears when the spec is in fact not accepted, and not when it is.

## Interactive or headless

Headless means: `--headless` is among the arguments, or you cannot wait for a reply (a `claude -p` run, a workflow step). Interactive means you can ask and wait. Every "ask the human" step below applies only when interactive; headless runs leave the marker or status in the file and stop.

## Goal

Phase 6 of the idea-to-spec loop, and the only step after acceptance. The prototype is the spec made clickable, not a second spec and not a design: the reviewer walks the flows, sees what each screen holds, and reacts to something real instead of to a document. Screens carry their SCR-ID so every reaction finds its way back into the spec.

There is no design brief and no design canvas in this loop. A reviewer who wants a visual design takes the accepted `spec.md` into Claude Design by hand; everything this loop builds is the prototype.

## Steps

1. **Resolve `FEATURE_DIR`.** Read `spec.md`. Require status `accepted` unless `--draft` is given; without it and without acceptance, stop and say `Run /speckit-idea-accept first, or pass --draft for an early look.` Note version and git tag. Read `prototype/PUBLISHED.md` if it exists.

2. **Read the spec for what the prototype holds.** §2 users, context and devices; §4 out of scope; §5 flows; §6 screen catalog; §7 functional requirements; §8 constraints; §13 tombstones. The screens, their content lists, their primary actions and their states are the entire material for the content.

   Then read `standards/BOUND.md` and, for every bound module, its `rules.md` and `assets/`. Standards are not optional decoration here: rules whose `Bites` includes `prototype` are build instructions. Corporate-design tokens and assets are where the prototype's looks come from at all — without an active CD module the styling stays plain and neutral, with one it follows the tokens. Where a corporate-design rule and an accessibility rule collide, `standards/BOUND.md` has already recorded which one wins; follow that record rather than deciding again.

   Then read every `feedback/R*.md` for items of type `VISUAL` with status `prototype-only`. Those are the reviewer's notes on how the prototype looks, the one thing that never reaches the spec; honour them in this build and list them in the report as applied.

3. **Write `prototype/prototype.html`** — one self-contained file, no external scripts, stylesheets, fonts or network calls:
   - **One screen per SCR**, in the order of FLOW-01, then the remaining flows, then screens in no flow. Each screen carries a visible `SCR-<nn>` badge and its name from §6.
   - **Navigation is the flows.** A flow picker lists every FLOW-ID with its name; picking one walks its screens in order. "Leads to" targets are the clickable elements; "Comes from" is the back step. A screen that is in no flow is reachable from an index.
   - **The primary action is the one dominant control** on its screen and it navigates where §6 says it leads.
   - **Content** is exactly the elements §6 lists — every column of a named table, every form field, every filter. Nothing else.
   - **States** from §6 (empty / loaded / error / loading / offline …) are switchable per screen, so the reviewer sees each one.
   - **Placeholder data** fills tables and fields so the screen reads like the real thing: plausible values from the trade and the users in §2, in the UI language of §8. Placeholder *values* are required; placeholder *fields* are forbidden — never a column, field or button the spec does not list.
   - **Device and language** follow §8: a phone-context screen is drawn in a phone-width frame, a desktop screen wide; all labels are in the UI language §8 fixes, not English, and any term §8 pins down is used verbatim.
   - **A spec lane the reviewer can toggle**: off by default, on it shows per screen the SCR-ID, the FRs from "Satisfies" and their provenance tags, so a reviewer can see why an element is there.
   - **Standards applied**: every rule of a bound module whose `Bites` includes `prototype` is built in, not bolted on afterwards — semantic landmarks and heading order, a visible label bound to every input, field-level error text in the error state, keyboard operability with a visible focus ring, text alternatives, a live region for status messages, reflow at 320 px, and colours that clear the contrast rule. Corporate-design tokens define the colours, type and spacing; a token whose pairing lost a recorded conflict is not used for text.
   - **Assets are embedded, never linked.** The published page blocks external stylesheets, fonts, images and media, and a linked asset silently does not appear. Inline SVG for the logo, subset `data:` URIs for fonts — and only for a face whose licence row in the module's `assets/README.md` says it is cleared for embedding. An uncleared or missing face falls back to the token's fallback stack, and the substitution goes in the report. Keep the whole page under 16 MB, remembering that base64 adds about a third.
   - **A header** with the idea name, `Prototype of spec v<version>` and the tag, `DRAFT — built from a spec that is not accepted` when that applies, and one line telling the reviewer that looks are not the subject: comment on what is missing, wrong or in the wrong order.
   - Responsive, theme-aware, keyboard-reachable. State lives in the page; there is no backend and nothing is stored.

4. **Freeze a snapshot.** Copy the result to `prototype/prototype-v<spec-version>.html`. The fixed name `prototype.html` is what gets republished, so the prototype URL stays the same across versions.

5. **Write `prototype/README.md`** from `.specify/extensions/idea/templates/prototype-readme-template.md` if it does not exist.

6. **Publish.** If an Artifact publishing tool is available in this session, publish `prototype/prototype.html`. If `prototype/PUBLISHED.md` already names a URL, read that artifact first and republish to the same URL so the link the reviewer holds keeps working; on the first publish use the favicon 🖱️, the title `<Idea name> Prototype` and the description `Clickable prototype of spec v<version> — comment on anything missing or wrong`. Headless runs usually have no publishing tool; then the local file is the prototype and the reviewer opens it in a browser.

7. **Record.** Append a row to `prototype/PUBLISHED.md` (create it with the header `| Spec version | Date | URL | Git tag |` if missing): spec version, today, URL or `local: prototype/prototype.html`, the git tag if one exists.

8. **Report.** The URL or path, the number of screens and flows built, any screen the spec left too thin to draw honestly (say which and what the spec is missing — do not fill it in), and then the standards lines: which prototype-level rules were built in, which assets were embedded and which were substituted and why, and every visual decision made without cover because a module is still a draft. Close with the two lanes for prototype feedback in one sentence (visual stays in the prototype; content or flow goes back through `/speckit-idea-feedback`), and the next commands: `/speckit-idea-standards --check` to get the rule-by-rule verdict, `/speckit-idea-feedback --from-comments` to open a round, or `/speckit-idea-accept --prototype` when the prototype stands.

## Rules

- Never add a screen, field, column, action or rule that is not in the spec. If the spec is too thin to build a screen, say so and recommend a feedback round; do not invent your way past it.
- Never show anything from §4 "Out of scope" or from a §13 tombstone.
- Never edit `spec.md`, `CHANGELOG.md` or `decisions/` here.
- Never treat this as a design exercise. Plain, neutral, legible; the spec's constraints and the bound corporate-design tokens are the only styling input. Where no CD module is active, or it is a draft, choose the plainest thing that works and say in the report which decisions you had to make uncovered.
- Never claim a standard rule is met. Build to it, then let `/speckit-idea-standards --check` decide with evidence.
- No backend, no login, no persistence, no external requests. Everything the prototype does happens in the page.