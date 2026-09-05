# Changelog

One block per spec version. Every change names the feedback item that triggered it. Read newest first.

## v0.3 · 2026-09-05 · from round R2

Round R2 was confirmed via workflow gate `dry-run-simulated-gate-2` (dry run, synthetic reviewer, no human decision; see `feedback/R2.md`, Notes). R2-03 and R2-04 got no answer at the gate, so their stated defaults (a) apply. Status: in-review (unchanged). First removals: five tombstones in §13 and the first decision record, `decisions/DEC-001.md`.

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| Hit rate removed from version 1: FR-026, FR-027, FLOW-05 and SC-005 became tombstones in §13 with decision record DEC-001 (reason: a reporting topic, version 2 at the earliest, once there is enough data); A-19 marked removed; the §4 In-scope line "Hit rate …" moved to §4 Out of scope citing `[R2-01 · DEC-001]`; JOB-06 narrowed to "see all open quotes of the business" (F-033, F-048, F-073 dropped, F-009 and F-043 stay); §2 Boss row lost "and the hit rate per month"; SCR-01 lost the content entry "hit rate (boss)"; §8 Devices lost "so the hit rate works on either"; the §4 intro line, the Q-01 marker and A-03 no longer count the hit rate among the priority-2 features of version 1 (Q-01 itself stays open) | §13, `decisions/DEC-001.md`, A-19, §4 In scope and Out of scope, JOB-06, §2, SCR-01, §8, A-03; `analysis/facts.md` (superseded-by-decision row) | R2-01 | REMOVE |
| Consistency edits that follow from R2-01 and are not separate items: FR-016 and A-20 derivation trimmed to the Q-06 restart rule (F-033 dropped as a reason); the §4 quote-amount line and the Q-09 marker under FR-002 now say the hit rate comes in version 2; the §7 group label "Hit rate" became "Quote amount" and points to §13; the amount field itself is untouched | FR-016, A-20, §4 In scope (amount line), FR-002 marker, §7 group label | R2-01, shaped by the R2-03 answer (a) | CHANGE |
| SCR-07 "Hit rate" removed: tombstone in §13 pointing to DEC-001 (same decision as R2-01); SCR-01 "Comes from" and "Leads to" drop SCR-07; no other screen or flow referenced it | §6 SCR-07, SCR-01, §13 | R2-02 | REMOVE |

Not changed: R2-03 (question, answered: a by default at the gate; the quote amount stays an optional field, so FR-028, FR-002, A-11, SCR-02, SCR-03, FR-031, SCR-10 and FLOW-08 keep their wording), R2-04 (question, answered: a by default at the gate; §1 and the header "Reviewed sections" untouched)
Deferred: none
Removed: FR-026, FR-027, FLOW-05, SC-005 (R2-01) and SCR-07 (R2-02); 5 tombstones, 1 decision record (DEC-001)

Facts: 76 · Conflicts: 2 (0 unresolved) · Open questions: 14 (12 open) · Assumptions: 25 (4 resolved: A-01, A-02, A-04, A-13; 1 removed: A-19) · Decisions: 1 (DEC-001)

Counts in this version: JOB 8 · FLOW 7 · SCR 9 · FR 30 · SC 7 · clarification markers 2 (Q-01, Q-09) · change markers `⟲ v0.3` 16 · tombstones 5

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
