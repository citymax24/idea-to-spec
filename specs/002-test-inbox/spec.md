# Specification: Quote Follow-Up Tracker

| Field | Value |
|-------|-------|
| **Version** | 1.1 |
| **Status** | in-review |
| **Created** | 2026-09-05 |
| **Sources** | S1–S4 (see `inputs/INVENTORY.md`) |
| **Reviewed sections** | accepted without section-by-section coverage (v0.2, knowingly) |
| **Approved by** | yana (v1.0) |
| **Approved on** | 2026-09-05 (v1.0) |

**Drafted from**: kickoff notes of 2026-08-12 (S1), the feature list (S2), the customer interview with Weber Gartenbau of 2026-09-02 (S3) and the market overview of 2026-08-20 (S4), drafted on 2026-09-05 from 65 extracted facts with all three conflicts and all nine open questions resolved by the human.

## 1 Problem and Goal *(mandatory)*

Quotes get lost in day-to-day work at small garden and landscaping companies. — [F-001 · S1 §1]
The site manager writes quotes in the evening, sends them by mail and forgets to follow up, while the office does not know which quotes are still open unless somebody asks. — [F-002 · S1 §1]
At one company an estimated 8 of 30 quotes fizzled out in spring, with neither a rejection nor a single follow-up. — [F-004 · S1 §1]
The problem is not writing the quote but staying on it; after two weeks nobody calls any more. — [F-041 · S3 02:15]
The goal is a single list of open quotes, sorted by the date follow-up is due, that raises one reminder after seven days and takes two taps to update, so that no quote dies unanswered. — [F-009 · S1 §3]

## 2 Target Users and Roles *(mandatory)*

Version 1 targets garden and landscaping companies with 5 to 50 employees. One-person businesses and corporations are not the target group; the wider craft segment named in the market overview stays context, not scope. — [C-01 resolved]

| Role | Who they are | What they need from this | Provenance |
|------|--------------|--------------------------|------------|
| Chef | Owner of a company with 5–50 employees, uses phone and desktop, looks weekly | An overview of what is open and how many quotes become jobs | [F-036 · S2 row 2 (sheet Rollen)] |
| Bauleiter | Site manager, writes the quotes, is out on site, uses a phone daily, often with dirty hands or gloves | To register a quote without typing it and to set its status in two taps | [F-037 · S2 row 3 (sheet Rollen)] |
| Büro | Office, uses a desktop daily, at Weber Gartenbau this is the owner's wife | A call list on Monday morning, notes, and a record of who was phoned | [F-038 · S2 row 4 (sheet Rollen)] |

## 3 User Jobs *(mandatory)*

Jobs the product must let a user do. Ordered by importance. Each job names the role.

- **JOB-01** · Bauleiter · When I have sent a quote, I want to file it as a photo or PDF instead of typing it in, so that it lands in the list at all. — [F-042 · S3 04:20]
- **JOB-02** · Bauleiter · When a customer decides on the building site, I want to set the status in two taps with gloves on, so that I do not put it off to the evening and forget it. — [F-047 · S3 12:10]
- **JOB-03** · Bauleiter, Büro · When a quote has had no answer for a week, I want one nudge and then to see whom to call, so that nothing sits unanswered. — [F-043 · S3 07:40]
- **JOB-04** · Büro · When I start Monday morning, I want a list to phone through, so that following up is a routine instead of a memory exercise. — [F-013 · S1 §3]
- **JOB-05** · Chef · When I look at the month, I want to see how many of my quotes became jobs, so that I know whether following up pays. — [F-026 · S2 row 8]
- **JOB-06** · Büro · When we start using the tool, I want the quotes from the old Excel list taken over once, so that we do not begin with an empty list. — [Q-02 resolved]

## 4 Scope *(mandatory)*

### In scope

- Registering a quote by attaching a photo or a PDF file — [F-025 · S2 row 7]
- Entering customer, quote amount and sent date by hand at registration — [Q-03 resolved]
- One list of all open quotes, sorted by the date follow-up is due — [F-009 · S1 §3]
- Five statuses per quote: "verschickt", "nachgefasst", "zugesagt", "abgesagt", "verlaufen" — [F-010 · S1 §3]
- One follow-up reminder after seven days without an answer, delivered by push or email — [F-011 · S1 §3]
- A free-text note on the customer per quote — [F-012 · S1 §3]
- A rejection reason on "abgesagt": price, date, competitor, other — [F-031 · S2 row 13]
- A Monday call list, filterable by Bauleiter — [F-024 · S2 row 6]
- Filtering the list by status — [F-027 · S2 row 9]
- Searching by customer or quote number — [F-028 · S2 row 10]
- A monthly win rate for the Chef, in count and in euros — [F-032 · S2 row 14]
- Reading the open quote list without a network connection — [F-033 · S2 row 15]
- A per-user login, one tenant per company — [C-02 resolved]
- A one-time import of the existing quotes from the old Excel list — [Q-02 resolved]

### Out of scope

- Writing or calculating quotes; companies keep doing that in their existing program — [F-015 · S1 §5]
- Any connection to accounting or ERP — [F-016 · S1 §5]
- Customer management beyond what the list itself needs — [F-017 · S1 §5]
- Reading text out of the attached photo or PDF (no OCR) — [Q-03 resolved]
- Restricting a site manager to his own quotes; everyone in a company sees all of that company's quotes — [C-03 resolved]
- Changing a status or registering a quote while offline — [Q-07 resolved]
- A configurable follow-up interval; seven days is fixed in version 1 — [Q-01 resolved]
- Naming a price for the product; the price is fixed only after the pilot — [Q-09 resolved]

## 5 User Flows *(mandatory)*

Every flow starts and ends at a screen from §6.

### FLOW-01 · First run: sign in and take over the old list — [Q-02 resolved]

SCR-06 → SCR-07 → SCR-01 → done. The user signs in, points the import at the existing Excel list, and lands on a list that already holds the open quotes. If the import fails, SCR-07 stays and reports which rows could not be read; the user can continue with an empty list.

### FLOW-02 · Register a sent quote — [F-042 · S3 04:20]

SCR-01 → SCR-02 → SCR-01 → done. The user attaches a photo or PDF, types customer, amount and sent date, and the quote appears in the list with its follow-up date seven days out. If there is no connection the quote cannot be saved and SCR-02 says so.

### FLOW-03 · Follow up after the seven-day reminder — [F-043 · S3 07:40]

SCR-01 → SCR-03 → SCR-01 → done. The reminder points the user at the list, the user opens the quote, phones the customer and sets the new status. If the customer cannot be reached, the note carries what was agreed and the quote stays open.

### FLOW-04 · Set the status on the building site — [F-047 · S3 12:10]

SCR-01 → SCR-03 → SCR-01 → done. The user finds the quote, sets "zugesagt" or "abgesagt" in two taps, and it leaves the open list. Without a connection the list is readable but the status cannot be changed.

### FLOW-05 · Monday phone round — [F-013 · S1 §3]

SCR-01 → SCR-04 → SCR-03 → SCR-04 → done. The office opens the call list, works through it quote by quote, sets a status or writes a note on each, and returns to the list. A quote that is set to "zugesagt" or "abgesagt" drops out of the call list.

### FLOW-06 · Check the win rate — [F-026 · S2 row 8]

SCR-01 → SCR-05 → SCR-01 → done. The Chef opens the win rate for a month and sees the share of quotes that became jobs, by count and in euros. A month without quotes shows an empty state, not a zero rate.

### FLOW-07 · Manage the users of a company — [R1-01]

SCR-01 → SCR-08 → SCR-01 → done. The Chef opens user management, adds a new site manager or removes someone who has left, and returns to the list. Removing the last remaining Chef of a company is refused, so a company cannot lock itself out.

## 6 Screen Catalog *(mandatory)*

One block per screen. This section becomes the design brief.

### SCR-01 · Open quotes — [F-009 · S1 §3]

- **Purpose**: Show everything that is still open, in the order in which it needs attention.
- **Primary action**: Open a quote to set its status.
- **Content**: Table (customer, quote number, amount, sent date, follow-up date, status), status filter, search field, button "new quote", marker on quotes whose follow-up date has passed.
- **States**: empty / loaded / error / offline (readable, not editable).
- **Satisfies**: FR-004, FR-006, FR-007, FR-008, FR-016, FR-017, FR-024
- **Comes from**: SCR-06, SCR-07, SCR-02, SCR-03, SCR-05, SCR-08 · **Leads to**: SCR-02, SCR-03, SCR-04, SCR-05, SCR-08 ⟲ v0.2 · R1-01

### SCR-02 · New quote — [F-025 · S2 row 7]

- **Purpose**: Get a quote that has already been sent into the list without typing the quote itself.
- **Primary action**: Attach the photo or PDF and save.
- **Content**: File picker and camera capture, fields customer, quote number, amount, sent date; the follow-up date is shown as derived, not entered.
- **States**: empty / filled / saving / error / offline (blocked, with a reason).
- **Satisfies**: FR-001, FR-002, FR-003
- **Comes from**: SCR-01 · **Leads to**: SCR-01

### SCR-03 · Quote detail — [F-010 · S1 §3]

- **Purpose**: See one quote in full and record what happened with it.
- **Primary action**: Set the status.
- **Content**: Customer and quote data, the attached photo or PDF, status control with the five values, free-text note, rejection reason (only on "abgesagt"), follow-up date.
- **States**: loaded / saving / error / offline (readable, status control disabled).
- **Satisfies**: FR-005, FR-006, FR-009, FR-014, FR-015, FR-025
- **Comes from**: SCR-01, SCR-04 · **Leads to**: SCR-01, SCR-04

### SCR-04 · Monday call list — [F-024 · S2 row 6]

- **Purpose**: Give the office one list to phone through.
- **Primary action**: Open the next quote to be phoned.
- **Content**: Quotes due for follow-up with customer, phone-relevant data, note and last status change; filter by Bauleiter.
- **States**: empty (nothing due) / loaded / error.
- **Satisfies**: FR-018, FR-030 ⟲ v1.1 · R2-01
- **Comes from**: SCR-01, SCR-03 · **Leads to**: SCR-03, SCR-01

### SCR-05 · Win rate — [F-062 · S4 slide 5]

- **Purpose**: Show the Chef how many quotes become jobs.
- **Primary action**: Pick the month to look at.
- **Content**: Share of "zugesagt" across all quotes of the month by count and in euros, count of quotes in the month, month selector.
- **States**: empty (no quotes in the month) / loaded / error.
- **Satisfies**: FR-019, FR-020
- **Comes from**: SCR-01 · **Leads to**: SCR-01

### SCR-06 · Sign in — [C-02 resolved]

- **Purpose**: Identify the user and the company whose quotes are shown.
- **Primary action**: Sign in.
- **Content**: Fields for the user's credentials, company context after sign-in.
- **States**: empty / signing in / error (wrong credentials) / offline (blocked, with a reason).
- **Satisfies**: FR-021, FR-022
- **Comes from**: — · **Leads to**: SCR-07, SCR-01

### SCR-07 · Take over the old Excel list — [Q-02 resolved]

- **Purpose**: Carry the existing quotes over once when a company starts.
- **Primary action**: Run the import.
- **Content**: File picker for the old Excel list, preview of the rows that were recognised, report of rows that could not be read, "skip" option.
- **States**: empty / preview / importing / partial error / done.
- **Satisfies**: FR-026
- **Comes from**: SCR-06 · **Leads to**: SCR-01

### SCR-08 · User management — [R1-01]

- **Purpose**: Administer the per-user accounts of one company.
- **Primary action**: Add a user to the company.
- **Content**: List of the company's users with name and role, "add user" action, "remove user" action per row, note that a removed user keeps no access.
- **States**: loaded / adding / removing / error / offline (blocked, with a reason).
- **Satisfies**: FR-027, FR-028, FR-029
- **Comes from**: SCR-01 · **Leads to**: SCR-01

## 7 Functional Requirements *(mandatory)*

Each requirement is testable and ends with a provenance tag.

- **FR-001**: A user can register a quote by attaching a photo or a PDF file to it. — [F-025 · S2 row 7]
- **FR-002**: At registration the user enters customer, quote amount and the date the quote was sent by hand. — [Q-03 resolved]
- **FR-003**: A user can record a quote number on a quote. — [ASSUMPTION: derived from F-028 · S2 row 10; searching by quote number needs the field]
- **FR-004**: The system shows all open quotes in one list, sorted by the date on which follow-up is due. — [F-009 · S1 §3]
- **FR-005**: Every quote carries exactly one of five statuses: "verschickt", "nachgefasst", "zugesagt", "abgesagt", "verlaufen". — [F-010 · S1 §3]
- **FR-006**: A user can set the status of a quote in at most two taps. — [F-021 · S2 row 3]
- **FR-007**: A quote whose status is set to "zugesagt" leaves the open list. — [F-014 · S1 §4]
- **FR-008**: A quote whose status is set to "abgesagt" or "verlaufen" also leaves the open list. — [ASSUMPTION: derived from F-009 and F-014 · S1 §3–§4; the list holds open quotes and both are closed outcomes]
- **FR-009**: The status "verlaufen" is set by hand; the system never sets it on its own. — [Q-04 resolved]
- **FR-010**: The system raises a follow-up reminder for a quote that has had no answer for 7 days. (no screen: background rule) — [F-011 · S1 §3]
- **FR-011**: The seven-day interval is fixed and cannot be configured by a company. (no screen: background rule) — [Q-01 resolved]
- **FR-012**: A quote produces exactly one reminder, not a repeating series. (no screen: background rule) — [F-043 · S3 07:40]
- **FR-013**: The reminder reaches exactly one person, the user who registered the quote, as a push notification on the phone or as an email. (no screen: background rule) — [ASSUMPTION: recipient derived from F-037 · S2 row 3 (sheet Rollen) and F-043 · S3 07:40; channel from F-030 · S2 row 12] ⟲ v1.1 · R2-01
- **FR-014**: A user can keep a free-text note on each quote. — [F-012 · S1 §3]
- **FR-015**: On the status "abgesagt" a user can record a rejection reason: price, date, competitor or other. — [F-031 · S2 row 13]
- **FR-016**: A user can filter the quote list by status. — [F-027 · S2 row 9]
- **FR-017**: A user can search quotes by customer or quote number. — [F-028 · S2 row 10]
- **FR-018**: The office gets a call list of the quotes due for follow-up, filterable by Bauleiter. — [F-024 · S2 row 6]
- **FR-019**: The Chef sees, per month, the share of quotes with status "zugesagt" across all quotes of that month. — [F-026 · S2 row 8]
- **FR-020**: The win rate is also shown in euros, from the recorded quote amounts. — [F-032 · S2 row 14]
- **FR-021**: Every user of a company signs in with their own account. — [C-02 resolved]
- **FR-022**: Every signed-in user of a company sees all quotes of that company. — [C-03 resolved]
- **FR-023**: Quotes of one company are never visible to another company. (no screen: background rule) — [Q-08 resolved]
- **FR-024**: The open quote list can be read without a network connection. — [F-033 · S2 row 15]
- **FR-025**: Registering a quote and changing a status require a network connection; offline the affected control is disabled and says why. — [Q-07 resolved]
- **FR-026**: When a company starts, the quotes from its old Excel list can be imported once. — [Q-02 resolved]
- **FR-027**: A user can be added to a company. — [R1-01]
- **FR-028**: A user of a company can be removed. — [R1-01]
- **FR-029**: Only the Chef can add or remove users of his company. — [ASSUMPTION: derived from F-007 · S1 §2; R1-01 named no role]
- **FR-030**: The office is not notified per quote; quotes due for follow-up reach the office through the Monday call list. — [ASSUMPTION: derived from F-024 · S2 row 6 and F-043 · S3 07:40; R2-01] ⟲ v1.1 · R2-01

## 8 Constraints

- **Devices / context**: The Bauleiter works almost only on a phone, often with dirty hands. — [F-008 · S1 §2]
- **Devices / context**: The Chef uses phone and desktop weekly, the Bauleiter a phone daily, the Büro a desktop daily. — [S2 rows 2–4 (sheet Rollen)]
- **Devices / context**: On the building site the user wears gloves: two taps and it has to be done, otherwise it is put off to the evening and forgotten. — [F-047 · S3 12:10]
- **Language**: German only in version 1. — [Q-05 resolved]
- **Brand / tone**: No source names brand assets or a tone of voice; plain, workmanlike German without marketing tone. — [ASSUMPTION: no source states brand or tone]
- **Legal / data**: Quotes hold customer names, notes and amounts, so third-party personal data is processed; hosting in the EU, processing agreement (AVV) available. — [Q-06 resolved]
- **Legal / data**: One tenant per company, data separated between companies. — [Q-08 resolved]
- **Adoption**: A pilot customer states he already has twelve passwords and will not use the tool if he has to sign in every time, while version 1 does have a per-user login. — [F-044 · S3 09:10]
- **Market**: Companies pay between 0 € (Excel) and 89 €/month (full suite) today, with a stated pain threshold of 20–30 €/month for a single-purpose tool. — [F-054 · S4 slide 3]

## 9 Success Criteria

Measurable, technology-agnostic outcomes.

- **SC-001**: A Bauleiter can set the status of a quote on a phone in at most two taps. — [F-021 · S2 row 3]
- **SC-002**: A quote with no answer for seven days produces exactly one reminder, not three. — [F-043 · S3 07:40]
- **SC-003**: In a pilot company, no quote ends a season as "verlaufen" without at least one recorded follow-up. — [ASSUMPTION: derived from F-004 · S1 §1; 8 of 30 fizzled with no follow-up at all]
- **SC-004**: The Chef can read the win rate of a month without asking anybody. — [F-026 · S2 row 8]
- **SC-005**: The Büro can produce the Monday call list in one step. — [F-013 · S1 §3]
- **SC-006**: A quote can be registered without typing the quote text: photo or PDF plus three fields. — [F-042 · S3 04:20]
- **SC-007**: The open quote list is readable with no network connection. — [F-033 · S2 row 15]

## 10 Assumptions

Everything the AI filled in without a source. Each item names what it was derived from and which section uses it.

- **A-01**: A quote number is a field on the quote — derived from F-028 (search by quote number); used in FR-003, SCR-02
- **A-02**: "abgesagt" and "verlaufen" also remove a quote from the open list; only "zugesagt" is stated — derived from F-009 and F-014; used in FR-008, SCR-01
- **A-03**: No brand assets or tone of voice exist yet — derived from the absence of any statement in S1–S4; used in §8
- **A-04**: "No quote fizzles without a follow-up" is the measurable form of the spring loss — derived from F-004; used in SC-003
- **A-05**: The seven-day reminder goes to exactly one person, the user who registered the quote; the office is not notified per quote — derived from F-037 (the Bauleiter's daily task is working through reminders) and F-043 ("einen Stups. Nicht drei."), against F-014 (S1 §4 "Bauleiter oder Büro ruft an", which settles who calls, not who is notified); used in FR-013, FR-030; the decision was delegated to Claude in R2-01 and was not weighed by a human ⟲ v1.1 · R2-01
- **A-06**: Only the Chef administers users, since he is the role described as deciding — derived from F-007 (S1 §2); used in FR-029, SCR-08; R1-01 named no role ⟲ v0.2 · R1-01

## 11 Open Questions

Questions no source answers. Each names the section that carries an assumption until answered.

No open questions. Q-10 was answered in round R2 and applied in v1.1 as FR-013 and FR-030. ⟲ v1.1 · R2-01

Q-01 to Q-09 and C-01 to C-03 were resolved by the human on 2026-09-05 and are cited in place; see `analysis/open-questions.md` and `analysis/conflicts.md`. Q-11 (user management) was answered in round R1 and applied in v0.2 as SCR-08, FR-027 to FR-029. ⟲ v0.2 · R1-01

## 12 Clarifications

## 13 Removed (Tombstones)

Nothing removed yet.
