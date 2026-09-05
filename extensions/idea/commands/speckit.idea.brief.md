---
description: Turn the accepted spec into a design brief for Claude Design - screens in flow order, one block per screen with a plain-language design prompt, constraints, and what must not be shown - then hand off to the design skill.
---

## User Input

```text
$ARGUMENTS
```

Arguments: `[--draft] [--feature <specs/NNN-dir>] [--headless]`. `--draft` allows a brief from an `in-review` spec for an early look; the brief is then marked DRAFT.

## Interactive or headless

Headless means: `--headless` is among the arguments, or you cannot wait for a reply (a `claude -p` run, a workflow step). Interactive means you can ask and wait. Every "ask the human" step below applies only when interactive; headless runs leave the marker or status in the file and stop.

## Goal

Phase 6 of the idea-to-spec loop. The brief is a re-arrangement of the spec for a designer or for Claude Design, not a second spec. Artboards are named after SCR-IDs so mockup feedback can find its way back into the spec.

## Steps

1. **Resolve `FEATURE_DIR`.** Read `spec.md`. Require status `accepted` unless `--draft`. Note version and git tag.

2. **Write `design/brief.md`** from `.specify/extensions/idea/templates/brief-template.md`:
   - product in one sentence (§1); users, context, devices (§2, §8); tone and brand (§8);
   - screens in the order of FLOW-01, then the remaining flows, then screens not in any flow;
   - per screen the SCR block copied verbatim, followed by a **Design prompt** paragraph in plain language: what the screen is for, what the eye should land on first, the one primary action, the content list, which states to draw. No colours, fonts or layouts unless §8 fixes them;
   - constraints (§8); "Do not show" from §4 out-of-scope and §13 tombstones;
   - spec version and tag it was derived from; DRAFT marker if applicable.

3. **Write `design/README.md`** from `design-readme-template.md` if it does not exist.

4. **Hand off.** If a design skill or Claude Design canvas is available in this session, invoke it with `design/brief.md` and these instructions: one artboard per screen, named exactly `<SCR-ID> <Screen name>`; flow order left to right; states as separate artboards where the brief lists them; exports to `design/mockups/v<spec-version>/`. If not available, print those instructions for the human together with the brief path.

5. **Report.** Brief path, number of screens, hand-off status, and the two-lane rule for mockup feedback in one sentence (visual stays in the canvas; content or flow goes back through `/speckit-idea-feedback`).

## Rules

- Never add a screen, field or rule that is not in the spec. If the spec is missing something the designer needs, say so and recommend a feedback round.
- Never edit `spec.md` here.
