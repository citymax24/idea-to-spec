# Changelog

One block per spec version. Every change names the feedback item that triggered it. Read newest first.

## v0.2 · 2026-09-05 · from round R1

Round R1 was confirmed via workflow gate `dry-run-simulated-gate` (dry run, synthetic reviewer, no human decision; see `feedback/R1.md`, Notes). Status: draft → in-review.

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| C-01 resolved as "GaLaBau only"; the unresolved-conflict assumption tags became `[C-01 resolved · R1-01]`, wording unchanged | §2 target line, §4 Out of scope "Other trades", A-01, §11 C-01, `analysis/conflicts.md` | R1-01 | CHANGE |
| C-02 resolved as "5 to 50 employees"; S4 slide 4 (F-067–F-069) set aside as a requirement source for version 1, wording unchanged | §2 target line, A-02, §11 C-02, `analysis/conflicts.md`, `analysis/facts.md` (set-aside note) | R1-02 | CHANGE |
| Q-02 resolved: no sign-in of any kind, one access link per business, a person picks their name once per device; invite flow reshaped, clarification marker under FR-029 removed | §2 identity paragraph, §8 Identity, FR-029, FR-030, SCR-08 (now "First use (pick your name)"), SCR-09, FLOW-07 (now "Set up the people and first use"), SC-007, A-04, A-18, §11 Q-02; wording in FR-020 and A-05 ("at first use"); `analysis/open-questions.md` | R1-03, shaped by the R1-04 answer (b) | CHANGE |
| Q-11 resolved: one-time import at the start, no export; no misreading found, so wording unchanged and the Q-11 default tags became `[Q-11 resolved · R1-05]` | JOB-08, §4 In scope "One-time takeover", §4 Out of scope "Export to Excel", FR-031, SCR-10, FLOW-08, A-13, §11 Q-11; `analysis/open-questions.md` | R1-05 | CHANGE (filed as MISREAD) |
| §1 recorded as reviewed | header "Reviewed sections" | R1-07 | OK |

Not changed: R1-04 (question, answered: b), R1-06 (question, answered)
Deferred: none
Removed: none (no tombstones, no decision records)

Facts: 76 · Conflicts: 2 (0 unresolved) · Open questions: 14 (12 open) · Assumptions: 25 (4 resolved: A-01, A-02, A-04, A-13)

Counts in this version: JOB 8 · FLOW 8 · SCR 10 · FR 32 · SC 8 · clarification markers 2 (Q-01, Q-09)

## v0.1 · 2026-09-05 · initial draft

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| Initial draft from S1–S4 | whole spec | facts F-001–F-076 | ADD |

Facts: 76 · Conflicts: 2 (2 unresolved) · Open questions: 14 · Assumptions: 25

Counts in this version: JOB 8 · FLOW 8 · SCR 10 · FR 32 · SC 8 · clarification markers 3 (Q-01, Q-02, Q-09)
