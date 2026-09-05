# Design Brief: [IDEA NAME]

Derived from `spec.md` v[1.0] (git tag `[tag]`) on [YYYY-MM-DD]. [DRAFT: derived from an unaccepted spec — for an early look only.]

This brief is a re-arrangement of the spec, not a second spec. If something here is wrong, the spec is wrong: open a feedback round, do not edit the brief.

## Product in one sentence

[§1]

## Users, context, devices

[§2 and §8: who, where, on what device, in what situation]

## Tone and brand

[§8]

## Screens in flow order

FLOW-01: SCR-01 → SCR-03 → SCR-04. Remaining screens after the main flow.

### SCR-01 · [Screen name]

- **Purpose**: [...]
- **Primary action**: [...]
- **Content**: [...]
- **States to show**: [empty / loaded / error]
- **Satisfies**: FR-001, FR-002
- **Leads to**: SCR-03

**Design prompt**: [Plain-language paragraph for the designer or Claude Design: what this screen is for, what the eye should land on first, the one primary action, the content list, and which states to draw. No colours or fonts unless §8 fixes them.]

## Constraints

[§8: devices, language, brand, legal]

## Do not show

[§4 out of scope and §13 tombstones, so the mockup does not resurrect removed ideas]

## Hand-off

- One artboard per screen, named exactly `<SCR-ID> <Screen name>`.
- Flow order left to right.
- States as separate artboards where listed.
- Exports go to `design/mockups/v[spec-version]/`.
