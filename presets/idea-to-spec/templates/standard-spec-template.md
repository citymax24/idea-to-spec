# Standard: [MODULE NAME]

| Field | Value |
|-------|-------|
| **Prefix** | STD-[SHORT] |
| **Version** | 0.1 |
| **Status** | draft |
| **Authority** | law \| accessibility-standard \| corporate-design \| convention |
| **Created** | [DATE] |
| **Sources** | [PREFIX]1–[PREFIX][n] (see `inputs/INVENTORY.md`) |
| **Source version** | [the version of the law, norm or manual this was written against, or — for internal] |
| **Approved by** | — |
| **Approved on** | — |

<!--
  A standards module is not an idea. It has no user jobs, no flows and no
  screens, so it does not use spec-template; it uses this one. What it shares
  with an idea spec is everything that makes a statement trustworthy: stable
  IDs, a provenance tag on every line, tombstones instead of deletions, and a
  human who accepts.

  STATUS is one of: draft | active | retired.
    draft   binds to ideas, but none of its rules can ever be reported "pass"
    active  in force
    retired does not bind to new ideas; existing bindings drift and are decided
  Only a human sets "active" (via /speckit-idea-accept). The AI never does.

  AUTHORITY decides two things: who wins a conflict between two modules, and
  whether a breach blocks acceptance. The order is
      law > accessibility-standard > corporate-design > convention
  The upper two block; the lower two warn.

  PROVENANCE RULE: every requirement, success criterion and applicability line
  ends with a provenance tag. Allowed tags:
    [EAA4 Art. 4]         a source from this module's inputs/INVENTORY.md with
                          a location. The prefix is the module's own namespace,
                          never S1..Sn - those belong to ideas.
    [F-012 · EAA5 §1.4.3] a fact from analysis/facts.md with its source location
    [C-02 resolved]       a conflict the human resolved in analysis/conflicts.md
    [Q-03 resolved]       an open question the human answered
    [ASSUMPTION: …]       no source states this; say what it was derived from
  A line without a tag is a defect. "Everyone knows this is required" is not a
  tag; if no source says it, it is an assumption and is marked as one.

  REQUIREMENT IDS are STD-<PREFIX>-<nnn>, numbered from 001, with 101 upwards
  reserved for requirements above the bound conformance level. They are stable
  and never reused; a withdrawn requirement becomes a tombstone in §7.
  (The handoff proposal suggested bare A11Y-### / BRD-###. The STD- prefix is
  kept so the tag is self-identifying wherever it lands in an idea's spec.)
-->

**Derived from**: [one sentence: which sources this module was derived from and when]

## 1 Purpose and legal basis *(mandatory)*

[What this module exists to enforce, and what makes it binding — the law, the contract, or the internal decision. 2–5 sentences, each with a provenance tag. For an external standard, name the instrument, its version, and the conformance level actually bound.]

## 2 Applicability *(mandatory)*

[Which ideas this module binds, and what an idea would have to be for it not to apply. Being out of scope is an exemption a human signs, never an assumption made while drafting.]

- **Binds**: [all ideas | the condition] — [tag]
- **Relief / exception in the source**: [e.g. a size threshold the law itself grants, or "none"] — [tag]
- **Decided elsewhere**: [what this module deliberately leaves to another module, so the boundary is explicit]

## 3 Requirements *(mandatory)*

One block per requirement. The four fields are what make a requirement usable by the rest of the loop: whether it blocks, where it can be judged, whether it writes itself into an idea's spec, and where it comes from.

### STD-[SHORT]-001 · [The requirement as one sentence a reviewer can judge]

[Two or three sentences: what it demands and what it forbids. No motivation, no history.]

- **Severity**: required | recommended
- **Bites**: spec | prototype | build
- **Shapes the spec**: yes — [what it writes into an idea's spec, and where] | no
- **Check**: [what someone looks at to decide pass or fail, in the terms of this repository: an SCR, a FLOW, an element in the prototype]
- **Source**: [tag]

## 4 Success Criteria

Measurable outcomes for the module as a whole, not per requirement.

- **SC-001**: [e.g. "every screen of a bound idea can be operated to completion with the keyboard alone"] — [tag]

## 5 Assumptions

Everything filled in without a source. Each names what it was derived from and which requirement uses it.

- **A-01**: [assumption] — derived from [tag]; used in STD-[SHORT]-00x

## 6 Open Questions

Questions no source answers. Each names the requirement that carries an assumption until answered.

- **Q-01**: [question] — affects STD-[SHORT]-00x

## 7 Removed (Tombstones)

Requirements withdrawn after review. The ID stays reserved; the line points to the version and the decision.

- **STD-[SHORT]-0xx** · [one-line summary] · Removed in v0.x · [trigger] · DEC-00x
