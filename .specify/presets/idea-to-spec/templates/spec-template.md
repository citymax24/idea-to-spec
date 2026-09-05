# Specification: [IDEA NAME]

| Field | Value |
|-------|-------|
| **Version** | 0.1 |
| **Status** | draft |
| **Created** | [DATE] |
| **Sources** | S1–S[n] (see `inputs/INVENTORY.md`) |
| **Reviewed sections** | — |
| **Approved by** | — |
| **Approved on** | — |

<!--
  STATUS is one of: draft | in-review | accepted.
  Only a human sets "accepted" (via /speckit-idea-accept). The AI never does.

  PROVENANCE RULE: every JOB, FLOW, SCR, FR, SC and constraint line ends with
  a provenance tag. Allowed tags:
    [S3 slide 7]          a source from inputs/INVENTORY.md with a location
                          (slide, row, page, timestamp mm:ss, section)
    [F-012 · S3 row 12]   a fact from analysis/facts.md with its source location
    [C-02 resolved]       a conflict the human resolved in analysis/conflicts.md
    [Q-03 resolved]       an open question the human answered in analysis/
    [R1-02]               a confirmed feedback item from feedback/R1.md
    [ASSUMPTION: derived from S3 row 30]   the AI filled a gap; say from what
  A line without a tag is a defect.

  CHANGE MARKERS: when a line changes in a later version, append
    ⟲ v0.2 · R1-01
  so a reader sees the change without opening CHANGELOG.md.

  IDs are stable and never reused. Removed items move to §13 as tombstones.
-->

**Drafted from**: [one sentence: which inputs this spec was drafted from and when]

## 1 Problem and Goal *(mandatory)*

[What is broken or missing today, for whom, and what changes when this exists. 2–5 sentences, each with a provenance tag.]

## 2 Target Users and Roles *(mandatory)*

| Role | Who they are | What they need from this | Provenance |
|------|--------------|--------------------------|------------|
| [Role A] | [size of business, context, device] | [one line] | [S1 §2] |

## 3 User Jobs *(mandatory)*

Jobs the product must let a user do. Ordered by importance. Each job names the role.

- **JOB-01** · [Role] · [When … I want to … so that …] — [S1 §3]
- **JOB-02** · [Role] · [...] — [S4 07:40]

## 4 Scope *(mandatory)*

### In scope

- [capability] — [S3 row 4]

### Out of scope

- [capability, and why it is out] — [S1 §5]

<!-- "Out of scope" must not be empty at acceptance. An empty list means scope was never discussed. -->

## 5 User Flows *(mandatory)*

Every flow starts and ends at a screen from §6.

### FLOW-01 · [Name] — [S1 §4]

SCR-01 → SCR-03 → SCR-04 → done. [One sentence on the happy path and the one thing that can go wrong.]

## 6 Screen Catalog *(mandatory)*

One block per screen. This section becomes the design brief.

### SCR-01 · [Screen name] — [S1 §4]

- **Purpose**: [what the user achieves here, one sentence]
- **Primary action**: [the one thing this screen is for]
- **Content**: [list of elements: table (columns …), filter, search, form fields …]
- **States**: empty / loaded / error [/ loading / offline as relevant]
- **Satisfies**: FR-001, FR-002
- **Comes from**: — · **Leads to**: SCR-03

## 7 Functional Requirements *(mandatory)*

Each requirement is testable and ends with a provenance tag.

- **FR-001**: [Role] can [capability]. — [S3 row 12]
- **FR-002**: The system [behaviour]. — [S4 07:40]
- **FR-003**: [...] — [ASSUMPTION: derived from S1 §3; no source states this]

## 8 Constraints

- **Devices / context**: [phone on site, desktop in office …] — [S1 §2]
- **Language**: [UI language(s)] — [S1]
- **Brand / tone**: [tone of voice, existing brand assets] — [S2 slide 2]
- **Legal / data**: [personal data, retention, consent] — [ASSUMPTION: …]

## 9 Success Criteria

Measurable, technology-agnostic outcomes.

- **SC-001**: [e.g. "A foreman can record a new quote status in under 30 seconds on a phone"] — [S4 12:10]
- **SC-002**: [...] — [ASSUMPTION: …]

## 10 Assumptions

Everything the AI filled in without a source. Each item names what it was derived from and which section uses it.

- **A-01**: [assumption] — derived from [S3 row 30]; used in FR-003

## 11 Open Questions

Questions no source answers. Each names the section that carries an assumption until answered.

- **Q-01**: [question] — affects §2, FR-004

## 12 Clarifications

<!-- /speckit-clarify appends "### Session YYYY-MM-DD" blocks here. Leave the heading in place. -->

## 13 Removed (Tombstones)

Items removed after review. The ID stays reserved; the line points to the round and the decision.

- **FR-0xx** · [one-line summary] · Removed in v0.x · R1-04 · DEC-002
