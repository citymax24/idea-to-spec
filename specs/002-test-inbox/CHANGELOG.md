# Changelog

One block per spec version. Every change names the feedback item that triggered it. Read newest first.

## v1.2 · 2026-09-05 · from round R3

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| FR-029 no longer ties administration to the Chef: a user holding the administrator right adds and removes users | §7 FR-029 | R3-01 | CHANGE |
| FR-031 added: an administrator can grant the administrator right to another user and withdraw it | §7 | R3-01 | ADD |
| FR-032 added: a company holds at least two administrators; removal or withdrawal is refused when it would leave fewer than two. Replaces the last-Chef rule | §7 | R3-01 | ADD |
| FR-033 added: a second administrator is named before a company starts working with the list | §7 | R3-01 | ADD |
| SCR-08 extended: the administrator right per user, a control to grant or withdraw it, an administrator count, and a setup state | §6 SCR-08 | R3-01 | CHANGE |
| FLOW-01 now runs SCR-06 → SCR-07 → SCR-08 → SCR-01; SCR-07 leads into SCR-08 | §5, §6 SCR-07 | R3-01 | CHANGE |
| §2 states that the administrator right is separate from the three roles | §2 | R3-01 | ADD |
| A-06 retired: "only the Chef administers users" was an assumption from R1-01 with no source behind it. A human has now decided, so the lines carry [R3-01] instead of [ASSUMPTION] | §10, §7 FR-029 | R3-01 | REMOVE |
| Version 1.1 → 1.2, status accepted → in-review; Approved fields kept with the note (v1.0, v1.1) | header | R3 | CHANGE |

Not changed: no QUESTION item in R3. Deferred: none. Dropped: none.
The reviewer found this by using the clickable prototype: the refusal "the last Chef cannot be removed" showed that a single administrator is a dead end. At confirmation "notwendig" was settled as *require*, not *allow* — hence FR-032 and FR-033.
Design follow-up: SCR-08 and the Benutzer screen of the prototype need rebuilding. The other seven screens are untouched.
Needs `/speckit-idea-accept` again to return to `accepted`.

Facts: 65 · Conflicts: 3 (0 unresolved) · Open questions: 0 · Assumptions: 5 (A-06 retired)

## v1.1 · 2026-09-05 · accepted by yana

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| Status in-review → accepted; version stays 1.1 (a re-acceptance keeps the current version) | header | acceptance by yana | CHANGE |
| Approved by / Approved on now name both acceptances: v1.0 and v1.1 | header | acceptance by yana | CHANGE |

Rounds since the v1.0 acceptance: R2 (recipient of the seven-day reminder) → v1.1.
Checklist at acceptance: 11 of 12 items passed mechanically; "Reviewed sections cover the whole spec" was again closed by the reviewer accepting without full coverage.
Accepted with these assumptions unread: A-05/FR-013/FR-030 (single recipient of the reminder — delegated to Claude, sources point both ways), A-06/FR-029 (only the Chef administers users), A-02/FR-008 ("abgesagt" and "verlaufen" also leave the open list). FR-021 stands against F-044 by the resolution of C-02.

## v1.1 · 2026-09-05 · from round R2

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| Q-10 answered: the seven-day reminder reaches exactly one person, the user who registered the quote. FR-013 now names the recipient | §7 FR-013 | R2-01 | CHANGE |
| FR-030 added: the office is not notified per quote and reaches due quotes through the Monday call list; SCR-04 "Satisfies" extended | §7, §6 SCR-04 | R2-01 | ADD |
| A-05 replaced: it assumed the registering user *and* the office. It now states the single recipient, names the evidence for and against, and records that the decision was delegated to Claude and never weighed by a human | §10 | R2-01 | CHANGE |
| Q-10 removed from §11; the spec now carries no open question | §11 | R2-01 | REMOVE |
| Version 1.0 → 1.1, status accepted → in-review; Approved fields kept with the note (v1.0) | header | R2 | CHANGE |

Not changed: no question was answered as a QUESTION item in R2. Deferred: none. Dropped: none.
No screens changed — the reminder is a background rule on no artboard, so the design canvas still matches.
Needs `/speckit-idea-accept` again to return to `accepted`.

Facts: 65 · Conflicts: 3 (0 unresolved) · Open questions: 0 open, 11 answered · Assumptions: 6

## v1.0 · 2026-09-05 · accepted by yana

| Change | Affects | Trigger | Type |
|--------|---------|---------|------|
| Version 0.2 → 1.0, status in-review → accepted | header | acceptance by yana | CHANGE |
| Reviewed sections recorded as accepted without section-by-section coverage, knowingly | header | acceptance by yana | CHANGE |

Rounds this spec went through: v0.1 initial draft from S1–S4 · R1 (user management) → v0.2 · accepted as v1.0.
Checklist at acceptance: 11 of 12 items passed mechanically; "Reviewed sections cover the whole spec" was closed by the reviewer accepting without full coverage.
Accepted with these assumptions unread: A-06/FR-029 (only the Chef administers users), A-05/Q-10 (recipient of the seven-day reminder, still open), A-02/FR-008 ("abgesagt" and "verlaufen" also leave the open list). FR-021 (per-user login) stands against F-044 by the resolution of C-02.

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
