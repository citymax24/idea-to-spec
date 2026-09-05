# Changelog

One block per spec version. Every change names the feedback item that triggered it. Read newest first.

## v0.2 · 2026-09-05 · from round R1

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| Q-11 answered: version 1 administers its own user accounts. Screen SCR-08 · User management added | §6 SCR-08, §5 FLOW-07 | R1-01 | ADD |
| FR-027 (add a user to a company) and FR-028 (remove a user of a company) added | §7 | R1-01 | ADD |
| FR-029 added: only the Chef administers users. No source names a role, so this carries an ASSUMPTION tag derived from F-007 (S1 §2) and assumption A-06 | §7, §10 | R1-01 | ADD |
| FLOW-07 added so SCR-08 is reached by a flow; SCR-01 "Leads to" and "Comes from" extended by SCR-08 | §5, §6 SCR-01 | R1-01 | ADD |
| Q-11 and its `[NEEDS CLARIFICATION]` marker removed from §11; the spec now carries no clarification marker | §11 | R1-01 | REMOVE |
| Version 0.1 → 0.2, status draft → in-review | header | R1 | CHANGE |

Not changed: nothing answered as a question in R1. Deferred: none. Dropped: none.
Still open: Q-10 (who receives the seven-day reminder), carried by assumption A-05.

Facts: 65 · Conflicts: 3 (0 unresolved) · Open questions: 1 open (Q-10), 10 answered · Assumptions: 6

## v0.1 · 2026-09-05 · initial draft

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| Initial draft from S1–S4 | whole spec | facts F-001–F-065 | ADD |
| Target group fixed to garden and landscaping companies with 5–50 employees; the wider craft segment of S4 slide 4 kept as context only | §2, §4 | C-01 resolved (human, 2026-09-05) | ADD |
| Per-user login taken into version 1 | §4, §6 SCR-06, FR-021 | C-02 resolved (human, 2026-09-05) | ADD |
| Per-Bauleiter visibility dropped; everyone in a company sees all of its quotes, so F-029 (S2 row 11) is not in scope | §4 out of scope, FR-022 | C-03 resolved (human, 2026-09-05) | ADD |
| Seven-day follow-up interval fixed, not configurable | FR-011 | Q-01 resolved (human, 2026-09-05) | ADD |
| Old Excel list read as a one-time import, not an export | JOB-06, FLOW-01, SCR-07, FR-026 | Q-02 resolved (human, 2026-09-05) | ADD |
| Customer, amount and sent date entered by hand; no OCR on the attachment | FR-002, §4 out of scope | Q-03 resolved (human, 2026-09-05) | ADD |
| "verlaufen" set by hand only | FR-009 | Q-04 resolved (human, 2026-09-05) | ADD |
| German-only interface | §8 | Q-05 resolved (human, 2026-09-05) | ADD |
| EU hosting with a processing agreement | §8 | Q-06 resolved (human, 2026-09-05) | ADD |
| Offline is read-only | FR-024, FR-025 | Q-07 resolved (human, 2026-09-05) | ADD |
| One tenant per company | FR-023, §8 | Q-08 resolved (human, 2026-09-05) | ADD |
| No price stated in the spec | §4 out of scope | Q-09 resolved (human, 2026-09-05) | ADD |
| Two new questions raised by the draft: reminder recipient (Q-10) and user management (Q-11) | §11 | drafting | ADD |

Facts: 65 · Conflicts: 3 (0 unresolved) · Open questions: 11 (9 resolved, 2 raised in this draft) · Assumptions: 5
