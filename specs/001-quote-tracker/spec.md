# Specification: Quote Tracker

| Field | Value |
|-------|-------|
| **Version** | 0.2 |
| **Status** | in-review |
| **Created** | 2026-09-05 |
| **Sources** | S1–S4 (see `inputs/INVENTORY.md`) |
| **Reviewed sections** | §1 (v0.1, R1-07) |
| **Approved by** | — |
| **Approved on** | — |

<!--
  STATUS is one of: draft | in-review | accepted.
  Only a human sets "accepted" (via /speckit-idea-accept). The AI never does.

  PROVENANCE RULE: every requirement, screen, job and flow line ends with a
  provenance tag. Allowed tags:
    [S3 slide 7]          a source from inputs/INVENTORY.md with a location
                          (slide, row, page, timestamp mm:ss, section)
    [R1-02]               a confirmed feedback item from feedback/R1.md
    [ASSUMPTION: derived from S3 row 30]   the AI filled a gap; say from what
  A line without a tag is a defect. Facts F-### from analysis/facts.md may be
  cited in addition, e.g. [F-012 · S3 row 12].

  CHANGE MARKERS: when a line changes in a later version, append
    ⟲ v0.2 · R1-01
  so a reader sees the change without opening CHANGELOG.md.

  IDs are stable and never reused. Removed items move to §13 as tombstones.
-->

**Drafted from**: Drafted on 2026-09-05 from the Grünwerk kickoff notes (S1), the feature list (S2), the Weber Gartenbau interview transcript (S3) and the sales market overview (S4), as extracted into `analysis/facts.md` (F-001–F-076); the 2 unresolved conflicts (C-01, C-02) and 14 open questions (Q-01–Q-14) are carried as tagged assumptions in §10.

## 1 Problem and Goal *(mandatory)*

Quotes get lost in day-to-day business: the site manager writes them in the evening at the kitchen table, emails them and forgets to follow up, and the office does not know which quotes are open unless someone asks. [F-002, F-003, F-004 · S1 §1]

In spring 2026 an estimated 8 of 30 quotes at Grünwerk simply lapsed, with neither a rejection nor a follow-up. [F-005 · S1 §1]

The problem is not writing the quote but staying on it ("das Dranbleiben"); after two weeks nobody calls any more, and an owner who writes about 120 quotes a year can only guess that about half are won. [F-047, F-048, F-049 · S3 00:40, 02:15]

With this product every sent quote lands in one shared list sorted by follow-up date, triggers exactly one reminder after 7 days without an answer, and gets its status set after the call, so that no quote lapses unnoticed and the boss sees how many quotes become orders. [F-013, F-015, F-018 · S1 §3–§4; F-052 · S3 07:40; F-073 · S4 slide 5]

Willingness to pay rises once a lost quote becomes visible; saving two orders a year is worth 30 € a month to a pilot business. [F-066 · S4 slide 3; F-059 · S3 13:30]

## 2 Target Users and Roles *(mandatory)*

Target business: garden and landscaping businesses ("GaLaBau") with 5 to 50 employees; not corporations, not one-person businesses. [F-006, F-007 · S1 §2] [C-01 resolved · R1-01] [C-02 resolved · R1-02] ⟲ v0.2 · R1-01, R1-02

| Role | Who they are | What they need from this | Provenance |
|------|--------------|--------------------------|------------|
| Boss ("Chef") | Owner of a GaLaBau business with 5–50 employees; decides; phone and desktop; weekly use. In a 12-person business the owner also writes the quotes himself. | Overview of all quotes of the business and the hit rate per month. | [F-008, F-009 · S1 §2; F-043 · S2 row 2 (sheet Rollen); F-046, F-052 · S3 para 1, 07:40] |
| Site manager ("Bauleiter") | Writes the quotes, is out in the field, works almost only on the phone, often with dirty hands or gloves; daily use. | Their own open quotes in follow-up order, one reminder after 7 days, status in two taps. | [F-010, F-012 · S1 §2; F-044 · S2 row 3 (sheet Rollen); F-056, F-057 · S3 10:45, 12:10] |
| Office ("Büro") | Maintains the data and phones customers; desktop; daily use. At Weber the owner's wife runs the office. | The Monday list to phone through, notes on quotes, sight of all quotes of the business. | [F-011 · S1 §2; F-045 · S2 row 4 (sheet Rollen); F-055 · S3 10:45] |

One person can hold more than one role, for example an owner who is both boss and the person who writes quotes; field crew who only set a status on site act as site managers in this spec. [ASSUMPTION: A-17, derived from F-052, F-056 · S3 07:40, 10:45]

There is no sign-in of any kind in version 1. A business receives one access link; everyone at the business opens the product through it, and on first use on a device the person picks their name once from the business's list of people and is never asked again, because "Bloß kein Login-Gedöns" and "Wenn ich mich jedes Mal anmelden muss, benutz ich es nicht". [F-023 · S1 §6; F-054 · S3 09:10] [Q-02 resolved · R1-03, R1-04] ⟲ v0.2 · R1-03

## 3 User Jobs *(mandatory)*

Jobs the product must let a user do. Ordered by importance. Each job names the role.

- **JOB-01** · Site manager · When I have sent a quote, I want it in the shared list without typing it in, so that it is not forgotten. — [F-018 · S1 §4; F-032 · S2 row 7 (sheet Features); F-050, F-051 · S3 04:20; F-070 · S4 slide 5]
- **JOB-02** · Site manager · When a quote has had no answer for 7 days, I want exactly one nudge ("einen Stups, nicht drei") and to see whom to call, so that I follow up before the customer goes cold. — [F-015 · S1 §3; F-028 · S2 row 4 (sheet Features); F-052, F-053 · S3 07:40]
- **JOB-03** · Site manager · When a customer accepts or declines on site, I want to set the status in two taps with gloves on, so that I do not have to remember it in the evening and forget. — [F-027 · S2 row 3 (sheet Features); F-056, F-057, F-058 · S3 10:45, 12:10; F-072 · S4 slide 5]
- **JOB-04** · Office · When Monday morning comes, I want a list of quotes to phone through ("abtelefonieren"), filterable by site manager, so that I can follow up in one sitting. — [F-017 · S1 §3; F-031 · S2 row 6 (sheet Features); F-045 · S2 row 4 (sheet Rollen); F-055 · S3 10:45]
- **JOB-05** · Office · When I have spoken to a customer, I want to note what they said on the quote (for example "will erst nach dem Urlaub entscheiden"), so that whoever calls next knows. — [F-016 · S1 §3; F-030 · S2 row 5 (sheet Features)]
- **JOB-06** · Boss · When I look at the business each week, I want to see all open quotes and the share of accepted quotes per month, so that I know how many quotes become orders instead of guessing. — [F-009 · S1 §2; F-033 · S2 row 8 (sheet Features); F-043 · S2 row 2 (sheet Rollen); F-048 · S3 00:40; F-073 · S4 slide 5]
- **JOB-07** · Office · When a customer calls or I need a specific quote, I want to find it by customer or quote number, so that I do not scroll through the list. — [F-035 · S2 row 10 (sheet Features)]
- **JOB-08** · Office · When we start using the product, I want to take over the existing open quotes from our old Excel list once, so that we do not keep two lists. — [F-042 · S2 row 31 (sheet Features); F-063 · S4 slide 2] [Q-11 resolved · R1-05] ⟲ v0.2 · R1-05

## 4 Scope *(mandatory)*

### In scope

Version 1 contains the feature-list priorities 1 and 2; priority 3 is out. [ASSUMPTION: Q-01 default, see A-03]

- [NEEDS CLARIFICATION: Q-01 — no source maps a feature-list priority to a version. Are the priority-2 features below (customer note, Monday list, hit rate, search, multiple site managers, push reminder, quote amount, Excel takeover) part of version 1, or only priority 1?]
- Open quotes list, sorted by follow-up date (priority 1). — [F-013 · S1 §3; F-025 · S2 row 2 (sheet Features)]
- Status per quote: sent, followed up, accepted, declined, lapsed; set in at most two clicks (priority 1). — [F-014 · S1 §3; F-026, F-027 · S2 row 3 (sheet Features)]
- Follow-up reminder after 7 days without answer (priority 1). — [F-015 · S1 §3; F-028 · S2 row 4 (sheet Features); F-052 · S3 07:40]
- Quote attached as photo or PDF instead of typing it in (priority 1). — [F-032 · S2 row 7 (sheet Features); F-050 · S3 04:20; F-070 · S4 slide 5]
- Filter the list by status (priority 1). — [F-034 · S2 row 9 (sheet Features)]
- Free-text note per quote about the customer (priority 2). — [F-016 · S1 §3; F-030 · S2 row 5 (sheet Features)]
- Monday list to phone through, filterable by site manager (priority 2). — [F-017 · S1 §3; F-031 · S2 row 6 (sheet Features)]
- Hit rate: share of accepted quotes among all quotes, per month, for the boss (priority 2). — [F-033 · S2 row 8 (sheet Features); F-073 · S4 slide 5]
- Search by customer or quote number (priority 2). — [F-035 · S2 row 10 (sheet Features)]
- Multiple site managers: each sees their own quotes, the boss sees all (priority 2). — [F-036 · S2 row 11 (sheet Features)]
- Reminder as push notification to the phone, or by email (priority 2). — [F-037 · S2 row 12 (sheet Features); F-071 · S4 slide 5]
- Quote amount per quote, so the hit rate can be shown in euros (priority 2). — [F-039 · S2 row 14 (sheet Features)]
- One-time takeover of existing quotes from the old Excel list at the start (priority 2). — [F-042 · S2 row 31 (sheet Features)] [Q-11 resolved · R1-05] ⟲ v0.2 · R1-05

### Out of scope

- Quote creation and calculation; businesses keep doing that in their existing program. — [F-020 · S1 §5]
- Connection to accounting or ERP. — [F-021 · S1 §5]
- Customer management beyond what the list needs; the customer is a name on the quote, not a record of its own. — [F-022 · S1 §5]
- Rejection reason on decline (price, date, competitor, other); priority 3. — [F-038 · S2 row 13 (sheet Features)] [ASSUMPTION: Q-01 default, see A-03]
- Offline reading of the list without network; priority 3. — [F-040 · S2 row 15 (sheet Features)] [ASSUMPTION: Q-01 default, see A-03]
- Sign-in per user with a password; priority 3, origin unknown, rejected by Jonas and by Weber. — [F-041 · S2 row 16 (sheet Features); F-023 · S1 §6; F-054 · S3 09:10]
- Export to Excel; the feature-list row with this title describes a one-time import, not an export. — [F-042 · S2 row 31 (sheet Features)] [Q-11 resolved · R1-05] ⟲ v0.2 · R1-05
- Configurable reminder period; the feature list only asks the question. — [F-029 · S2 row 4 (sheet Features)] [ASSUMPTION: Q-05 default, see A-07]
- Automatic text recognition of the attached photo or PDF. — [ASSUMPTION: Q-10 default, see A-12; no source asks for it]
- Automatic lapsing of a quote after a period without answer; "lapsed" is set by hand. — [ASSUMPTION: Q-08 default, see A-10]
- Pricing, billing and subscriptions inside the product; the price is set only after the pilot. — [F-076 · S4 slide 6]
- Other trades (painters, roofers, plumbing/heating) as target users of this version; GaLaBau is the entry market in both sources. — [F-067, F-069 · S4 slide 4] [C-01 resolved · R1-01] ⟲ v0.2 · R1-01

## 5 User Flows *(mandatory)*

Every flow starts and ends at a screen from §6.

### FLOW-01 · Add a sent quote — [F-018 · S1 §4; F-050 · S3 04:20]

SCR-01 → SCR-02 → SCR-03 → SCR-01. The user takes a photo of the printout or hands over the PDF, types the customer name, confirms today as sent date and saves; the quote appears at the end of the open list with status "sent". If the file cannot be attached, the quote is saved without it and the file is attached later from SCR-03. — [F-032 · S2 row 7 (sheet Features); F-051 · S3 04:20] [ASSUMPTION: Q-09 default, Q-10 default, see A-11, A-12]

### FLOW-02 · Follow up after a reminder — [F-018 · S1 §4; F-052, F-053 · S3 07:40]

SCR-05 → SCR-03 → SCR-04 → SCR-03 → SCR-01. The assigned site manager gets one reminder after 7 days without answer, opens the quote, sees whom to call, calls, sets the status "followed up" (or "accepted", "declined") and optionally leaves a note. If the customer is not reached, the status "followed up" still restarts the 7-day period, so the next reminder comes a week later, not tomorrow. — [F-015 · S1 §3] [ASSUMPTION: Q-04 default, Q-06 default, see A-06, A-08]

### FLOW-03 · Set the status on site — [F-027 · S2 row 3 (sheet Features); F-057 · S3 12:10]

SCR-01 → SCR-04 → SCR-01. The site manager opens the list, taps the quote and taps the status: two taps with gloves on. On "accepted" the quote disappears from the open list. A wrong tap is corrected by setting the status again. — [F-019 · S1 §4; F-056 · S3 10:45] [ASSUMPTION: derived from F-018 · S1 §4, see A-20]

### FLOW-04 · Monday phone-through — [F-017 · S1 §3; F-031 · S2 row 6 (sheet Features); F-055 · S3 10:45]

SCR-06 → SCR-04 → SCR-06 → SCR-03 → SCR-06 → SCR-01. The office opens the Monday list, filters by site manager if needed, phones each customer whose quote is due, sets the status from the row and adds a note where the customer said something worth keeping; a quote that got a status leaves the list. If nothing is due, the list is empty and says so. — [F-045 · S2 row 4 (sheet Rollen)] [ASSUMPTION: derived from F-013 · S1 §3 for the due rule, see A-21]

### FLOW-05 · Check the hit rate — [F-033 · S2 row 8 (sheet Features); F-073 · S4 slide 5]

SCR-01 → SCR-07 → SCR-01. The boss opens the hit rate, reads accepted quotes as a share of all quotes per month, in count and, where amounts were captured, in euros. A month with no quotes shows no share rather than zero. — [F-039 · S2 row 14 (sheet Features)] [ASSUMPTION: derived from F-033 · S2 row 8 (sheet Features), see A-19]

### FLOW-06 · Find a quote — [F-035 · S2 row 10 (sheet Features)]

SCR-01 → SCR-03 → SCR-01. The office types a customer name or quote number into the search on the open list, opens the matching quote, reads or edits it and returns. Closed quotes are found too; no match shows an empty result with the search term. — [F-035 · S2 row 10 (sheet Features)] [ASSUMPTION: Q-07 default, see A-09]

### FLOW-07 · Set up the people and first use — [F-036 · S2 row 11 (sheet Features); F-023 · S1 §6; F-054 · S3 09:10] ⟲ v0.2 · R1-03

SCR-01 → SCR-09 → SCR-08 → SCR-01. The boss adds the people of the business with their roles and shares the one access link of the business; each person opens it on their own phone or desktop, picks their name from the list, chooses push or email for reminders and lands in the list; from then on the device knows who they are and nobody ever signs in. An invalid link shows an error and asks for the business's current link; a name missing from the list asks the person to have the boss add it. — [Q-02 resolved · R1-03, R1-04] [ASSUMPTION: Q-03 default, see A-05, A-18] ⟲ v0.2 · R1-03

### FLOW-08 · Take over existing quotes — [F-042 · S2 row 31 (sheet Features)]

SCR-01 → SCR-10 → SCR-01. The office uploads the old Excel list once, matches its columns to customer, sent date, quote number, amount and site manager, checks the preview and confirms; the rows become open quotes with status "sent". Rows that cannot be read are listed and skipped, the rest are imported. — [F-063 · S4 slide 2] [Q-11 resolved · R1-05] [ASSUMPTION: takeover mechanics, see A-24] ⟲ v0.2 · R1-05

## 6 Screen Catalog *(mandatory)*

One block per screen. This section becomes the design brief.

### SCR-01 · Open quotes list — [F-013 · S1 §3; F-025 · S2 row 2 (sheet Features)]

- **Purpose**: See every open quote (own quotes for a site manager, all quotes of the business for boss and office) in the order they need a follow-up call, and act on one directly.
- **Primary action**: Set the status of a quote (tap the row, tap the status).
- **Content**: List rows with customer name, quote number (if present), sent date, follow-up date with an overdue marker, status, site manager (boss and office only), latest note in one line; fixed sort by follow-up date ascending; filter by status (default: open); filter by site manager (boss and office only); search field for customer or quote number; "Add quote" button; entries to the Monday list (office), hit rate (boss), people (boss) and takeover (office).
- **States**: empty (no open quotes: nothing to follow up) / loaded / loading / filtered or searched with no match / error (list cannot be loaded).
- **Satisfies**: FR-004, FR-006, FR-008, FR-009, FR-010, FR-011, FR-012, FR-013, FR-015, FR-024
- **Comes from**: SCR-02, SCR-03, SCR-04, SCR-06, SCR-07, SCR-08, SCR-09, SCR-10 · **Leads to**: SCR-02, SCR-03, SCR-04, SCR-06, SCR-07, SCR-09, SCR-10

### SCR-02 · Add quote — [F-032 · S2 row 7 (sheet Features); F-050 · S3 04:20; F-070 · S4 slide 5]

- **Purpose**: Get a quote that was just sent into the list as a photo or PDF with the least possible typing.
- **Primary action**: Attach the file and save.
- **Content**: File input that accepts a photo taken now, a photo from the device, or a PDF, including a PDF handed over from another app (forwarded mail); preview of the attached file; fields: customer name (required), sent date (required, preset to today), quote number (optional), amount in euros (optional), site manager (preset to the current user if they are a site manager, otherwise chosen from the business's site managers); "Save" and "Save without file".
- **States**: empty form / file attached with preview / saving / saved / error (file cannot be attached: offer "Save without file").
- **Satisfies**: FR-001, FR-002, FR-003, FR-005, FR-028
- **Comes from**: SCR-01 · **Leads to**: SCR-03

### SCR-03 · Quote detail — [F-016 · S1 §3; F-053 · S3 07:40]

- **Purpose**: See everything about one quote, add a note, change its status or attach the missing file.
- **Primary action**: Set the status.
- **Content**: Attached photo or PDF, viewable at full size, or "No file yet" with an attach action; customer name, quote number, amount, sent date, follow-up date, site manager, all editable; current status as a large button that opens SCR-04; notes in date order with an "Add note" field; dates of the status changes so far.
- **States**: loaded / no file attached / loading / error (quote cannot be loaded or saved).
- **Satisfies**: FR-003, FR-014, FR-016, FR-021, FR-023, FR-028
- **Comes from**: SCR-01, SCR-02, SCR-05, SCR-06 · **Leads to**: SCR-04, SCR-01, SCR-06

### SCR-04 · Set status — [F-027 · S2 row 3 (sheet Features); F-057 · S3 12:10; F-072 · S4 slide 5]

- **Purpose**: Change the status of one quote with one tap after the quote was picked.
- **Primary action**: Tap one of the five statuses; the tap saves.
- **Content**: Customer name and quote number of the quote; five large buttons: sent ("verschickt"), followed up ("nachgefasst"), accepted ("zugesagt"), declined ("abgesagt"), lapsed ("verlaufen"); the current status is marked; no further confirmation step.
- **States**: open (buttons shown) / saved (short confirmation, returns to the calling screen) / error (could not save: buttons stay, error shown).
- **Satisfies**: FR-014, FR-015, FR-017
- **Comes from**: SCR-01, SCR-03, SCR-06 · **Leads to**: SCR-01, SCR-03, SCR-06 (the screen it was opened from)

### SCR-05 · Reminder (push notification or email) — [F-015 · S1 §3; F-052 · S3 07:40; F-037 · S2 row 12 (sheet Features)]

- **Purpose**: Nudge the responsible person exactly once that a quote has waited 7 days without an answer.
- **Primary action**: Open the quote.
- **Content**: Customer name, quote number if present, sent date, "7 days without answer", and the quote as the target of the tap or link; as email the same content with a link to the quote.
- **States**: push delivered / email delivered / opened (leads to SCR-03).
- **Satisfies**: FR-018, FR-019, FR-020, FR-021
- **Comes from**: — (triggered by the 7-day rule) · **Leads to**: SCR-03

### SCR-06 · Monday list — [F-017 · S1 §3; F-031 · S2 row 6 (sheet Features); F-045 · S2 row 4 (sheet Rollen)]

- **Purpose**: Let the office work through every quote that is due for a follow-up call in one sitting at the desktop.
- **Primary action**: Set the status of a row after the call.
- **Content**: Table of open quotes whose follow-up date is today or earlier: customer name, quote number, sent date, days waiting, site manager, latest note, status; filter by site manager; count of rows; per row: set status (opens SCR-04), open quote to add a note (opens SCR-03); a row that got a new status leaves the table.
- **States**: empty (nothing due today) / loaded / loading / filtered with no match / error.
- **Satisfies**: FR-010, FR-011, FR-013, FR-024, FR-025
- **Comes from**: SCR-01, SCR-03, SCR-04 · **Leads to**: SCR-03, SCR-04, SCR-01

### SCR-07 · Hit rate — [F-033 · S2 row 8 (sheet Features); F-073 · S4 slide 5]

- **Purpose**: Show the boss how many quotes become orders, month by month.
- **Primary action**: Read the share for the current and past months.
- **Content**: One row per month for the last 12 months: quotes sent, accepted, declined, lapsed, still open; hit rate as accepted divided by sent; where amounts were captured, quoted euros, accepted euros and the share in euros; months without quotes show no share.
- **States**: loaded / no quotes yet (empty) / amounts missing (euro columns hidden or marked incomplete) / loading / error.
- **Satisfies**: FR-026, FR-027
- **Comes from**: SCR-01 · **Leads to**: SCR-01

### SCR-08 · First use (pick your name) — [F-023 · S1 §6; F-054 · S3 09:10] [Q-02 resolved · R1-03, R1-04] [ASSUMPTION: Q-03 default, see A-05] ⟲ v0.2 · R1-03

- **Purpose**: Let a person who opened the business's access link on a device say once who they are, without a password or any sign-in.
- **Primary action**: Pick your name and reminder channel and enter the list.
- **Content**: Business name from the link; the business's list of people to pick from, each with name and role as set by the boss, role shown but not editable; reminder channel: push on this device or email, with an email field; "Start" button.
- **States**: valid link / invalid link (error, ask the boss for the business's current link) / name not in the list (hint, ask the boss to add you) / notifications not allowed on this device (hint, email offered) / done (this device remembers the pick).
- **Satisfies**: FR-020, FR-029
- **Comes from**: — (opened from the business's access link) · **Leads to**: SCR-01

### SCR-09 · People — [F-008 · S1 §2; F-036 · S2 row 11 (sheet Features)] [Q-02 resolved · R1-03, R1-04] [ASSUMPTION: derived from F-009 · S1 §2 (the boss decides); no source describes how people are added, see A-18] ⟲ v0.2 · R1-03

- **Purpose**: Let the boss see who belongs to the business, add people with their roles and share the business's one access link.
- **Primary action**: Add a person with a name and a role.
- **Content**: The business's access link with a copy or share action; list of people with name, role (boss, site manager, office) and date of first use; "Add person" with name and role picker; change a role; remove a person.
- **States**: only me / loaded / person added / error.
- **Satisfies**: FR-010, FR-030
- **Comes from**: SCR-01 · **Leads to**: SCR-01

### SCR-10 · Take over existing quotes — [F-042 · S2 row 31 (sheet Features)] [Q-11 resolved · R1-05] [ASSUMPTION: takeover mechanics, see A-24] ⟲ v0.2 · R1-05

- **Purpose**: Bring the open quotes from the old Excel list into the product once at the start.
- **Primary action**: Upload the file and confirm the takeover.
- **Content**: File upload; column matching for customer, sent date, quote number, amount and site manager; preview of the rows with unreadable rows marked; "Take over" button; result summary with the number imported and skipped.
- **States**: empty / file loaded (matching) / preview / done / error (file cannot be read).
- **Satisfies**: FR-031
- **Comes from**: SCR-01 · **Leads to**: SCR-01

## 7 Functional Requirements *(mandatory)*

Each requirement is testable and ends with a provenance tag.

Adding quotes

- **FR-001**: A site manager, office member or boss can add a quote to the list by attaching a photo of the printout or a PDF; typing the content of the quote is never required. — [F-032 · S2 row 7 (sheet Features); F-050, F-051 · S3 04:20; F-070 · S4 slide 5] [ASSUMPTION: any role can add, see A-25]
- **FR-002**: When adding a quote the user enters the customer name and the sent date, which is preset to today; quote number and amount are optional. — [ASSUMPTION: Q-09 default, derived from F-013 · S1 §3, F-035 and F-039 · S2 rows 10, 14 (sheet Features) against F-024 · S1 §6 and F-051 · S3 04:20, see A-11]
  - [NEEDS CLARIFICATION: Q-09 — which fields must be typed when a quote is added as photo or PDF? Sorting, search and the hit rate need typed data, yet "Abtippen macht bei uns keiner".]
- **FR-003**: A quote can be saved without its file when the file cannot be attached; the file can be attached later from the quote detail. — [ASSUMPTION: Q-10 default, see A-12]
- **FR-004**: A newly added quote gets the status "sent" and appears in the open list. — [F-018 · S1 §4]
- **FR-005**: Every quote is assigned to exactly one site manager: the person adding it if they are a site manager, otherwise the site manager chosen while adding; boss and office can reassign it. — [ASSUMPTION: derived from F-036 · S2 row 11 and F-031 · S2 row 6 (sheet Features), see A-17]

Open list

- **FR-006**: The open list shows all quotes with status "sent" or "followed up", sorted ascending by follow-up date. — [F-013 · S1 §3; F-025 · S2 row 2 (sheet Features)] [ASSUMPTION: Q-07 default for which statuses count as open, see A-09]
- **FR-007**: The follow-up date of a quote is 7 days after its sent date, or 7 days after the last time its status was set to "followed up". (no screen: background rule) — [F-015 · S1 §3; F-028 · S2 row 4 (sheet Features)] [ASSUMPTION: Q-05 default (fixed period), Q-06 default (restart), see A-07, A-08]
- **FR-008**: The list can be filtered by status, including the closed statuses accepted, declined and lapsed. — [F-034 · S2 row 9 (sheet Features)] [ASSUMPTION: Q-07 default, see A-09]
- **FR-009**: The list can be searched by customer name or quote number; closed quotes are found too. — [F-035 · S2 row 10 (sheet Features)] [ASSUMPTION: Q-07 default, see A-09]
- **FR-010**: A site manager sees only the quotes assigned to them; the boss and the office see all quotes of the business. — [F-036 · S2 row 11 (sheet Features)] [ASSUMPTION: Q-14 default for the office, see A-16]
- **FR-011**: The boss and the office can filter the open list and the Monday list by site manager. — [F-031 · S2 row 6 (sheet Features); F-036 · S2 row 11 (sheet Features)]
- **FR-012**: A quote whose status becomes accepted, declined or lapsed leaves the open list at once and stays reachable through search and the status filter. — [F-019 · S1 §4] [ASSUMPTION: Q-07 default for declined and lapsed, see A-09]
- **FR-013**: The open list and the Monday list mark every quote whose follow-up date is today or in the past. — [ASSUMPTION: derived from F-013 · S1 §3 (sorted by follow-up date) and F-053 · S3 07:40 (see whom to call), see A-22]

Status

- **FR-014**: Each quote has exactly one status out of sent ("verschickt"), followed up ("nachgefasst"), accepted ("zugesagt"), declined ("abgesagt"), lapsed ("verlaufen"). — [F-014 · S1 §3; F-026 · S2 row 3 (sheet Features)]
- **FR-015**: From the open list, setting a status takes at most two taps or clicks: one to pick the quote, one to pick the status. — [F-027 · S2 row 3 (sheet Features); F-057 · S3 12:10; F-072 · S4 slide 5]
- **FR-016**: A status can be set again after it was set, and the date of every status change is kept and shown on the quote. — [ASSUMPTION: derived from F-033 · S2 row 8 (sheet Features) (hit rate per month) and Q-06 default (restart on "followed up"), see A-20]
- **FR-017**: "Lapsed" is set by a person; the system never changes a status on its own. — [ASSUMPTION: Q-08 default, see A-10]

Reminder

- **FR-018**: When a quote has had no status change for 7 days since it was sent or last followed up, the system sends exactly one reminder. — [F-015 · S1 §3; F-028 · S2 row 4 (sheet Features); F-052 · S3 07:40]
- **FR-019**: The reminder goes to the site manager the quote is assigned to. — [ASSUMPTION: Q-04 default, derived from F-052 · S3 07:40 and F-018 · S1 §4, see A-06]
- **FR-020**: A reminder is delivered as a push notification on the phone, or by email when the person chose email at first use. — [F-037 · S2 row 12 (sheet Features); F-071 · S4 slide 5] [ASSUMPTION: Q-03 default, see A-05] ⟲ v0.2 · R1-03
- **FR-021**: The reminder names the customer and the 7 days without answer, and opens the quote so the user sees whom to call. — [F-053 · S3 07:40]
- **FR-022**: No second reminder is sent for a quote until its status is set to "followed up", which restarts the 7-day period, or the quote leaves the open list. (no screen: background rule) — [F-052 · S3 07:40] [ASSUMPTION: Q-06 default, see A-08]

Notes

- **FR-023**: A user can add a free-text note to a quote about the customer, for example that they will decide only after their holiday; notes keep their date and are shown in order. — [F-016 · S1 §3; F-030 · S2 row 5 (sheet Features)]
- **FR-024**: The latest note of a quote is visible in its row of the open list and the Monday list. — [ASSUMPTION: derived from F-017 · S1 §3 and F-045 · S2 row 4 (sheet Rollen): the caller needs the note without opening each quote, see A-21]

Monday list

- **FR-025**: The office can open a Monday list containing all open quotes of the business whose follow-up date is today or earlier, filterable by site manager, with status and note reachable from each row. — [F-017 · S1 §3; F-031 · S2 row 6 (sheet Features); F-045 · S2 row 4 (sheet Rollen)] [ASSUMPTION: derived from F-013 · S1 §3 for the due rule, see A-21]

Hit rate

- **FR-026**: The boss can see the hit rate per month: the number of accepted quotes as a share of all quotes sent in that month, for at least the last 12 months. — [F-033 · S2 row 8 (sheet Features); F-073 · S4 slide 5] [ASSUMPTION: month of the sent date, denominator includes quotes still open, see A-19]
- **FR-027**: Where amounts are captured, the hit rate is also shown in euros: accepted amount as a share of the total quoted amount per month. — [F-039 · S2 row 14 (sheet Features)]
- **FR-028**: The amount of a quote can be captured when adding it or later on the quote detail. — [F-039 · S2 row 14 (sheet Features)]

People

- **FR-029**: A business receives one access link; opening it is the only access step. On first use on a device the person picks their name once from the business's list of people; there is no password and nobody is asked again on that device. — [F-023 · S1 §6; F-054 · S3 09:10; F-036 · S2 row 11 (sheet Features)] [Q-02 resolved · R1-03, R1-04] ⟲ v0.2 · R1-03
- **FR-030**: The boss maintains the business's list of people: add a person by name with a role (boss, site manager, office), change a role, remove a person, and share the business's access link; there are no per-person invites. — [Q-02 resolved · R1-03, R1-04] [ASSUMPTION: derived from F-008, F-009 · S1 §2 and F-036 · S2 row 11 (sheet Features); no source names who administers people, see A-18] ⟲ v0.2 · R1-03

Data

- **FR-031**: The office can take over the existing open quotes from the old Excel list once at the start by uploading the file, matching its columns to customer, sent date, quote number, amount and site manager, and confirming a preview; unreadable rows are listed and skipped, imported rows become open quotes with status "sent". — [F-042 · S2 row 31 (sheet Features)] [Q-11 resolved · R1-05] [ASSUMPTION: takeover mechanics, see A-24] ⟲ v0.2 · R1-05
- **FR-032**: Quotes, files, notes and people of one business are visible only to that business. (no screen: background rule) — [ASSUMPTION: Q-13 default, derived from F-075 · S4 slide 6 (two pilot businesses share the product), see A-15]

## 8 Constraints

- **Devices / context**: The site manager uses only the phone, in the field, often with dirty hands or gloves, so the open list, add quote, quote detail, status and reminder must work one-handed on a phone with large touch targets; the office works at a desktop, so the Monday list and the takeover are desktop screens; the boss uses both, so the hit rate works on either. — [F-012 · S1 §2; F-043, F-044, F-045 · S2 rows 2–4 (sheet Rollen); F-057 · S3 12:10]
- **Language**: German user interface; all sources and both pilot businesses are German-speaking. — [ASSUMPTION: Q-12 default, see A-14]
- **Brand / tone**: No brand assets exist in any source; the tone is plain trade language as the users speak it ("Stups", "abtelefonieren", "nachfassen"), short labels, no jargon. — [ASSUMPTION: derived from S1 §3 and S3 07:40, 10:45, see A-23]
- **Legal / data**: Quotes, photos, PDFs and notes contain customer personal data; each business sees only its own data, the data is kept until the business deletes it, and it is hosted in the EU. — [ASSUMPTION: Q-13 default, see A-15]
- **Identity**: No sign-in of any kind: one access link per business, and a person picks their name once per device from the business's list; no password, never asked again. — [F-023 · S1 §6; F-054 · S3 09:10; F-041 · S2 row 16 (sheet Features)] [Q-02 resolved · R1-03, R1-04] ⟲ v0.2 · R1-03
- **Timeline and pilots**: Prototype by October 2026; pilot businesses are Grünwerk GmbH and Weber Gartenbau. — [F-074, F-075 · S4 slide 6]
- **Price**: No pricing inside the product; the price is set after the pilot, against a stated pain threshold of 20–30 € per month for a single-purpose tool and a stated value of 30 € per month for two saved orders a year. — [F-076, F-065 · S4 slides 6, 3; F-059 · S3 13:30]

## 9 Success Criteria

Measurable, technology-agnostic outcomes.

- **SC-001**: A site manager can set the status of any quote from the open list in at most two taps on a phone while wearing gloves. — [F-027 · S2 row 3 (sheet Features); F-057 · S3 12:10; F-072 · S4 slide 5]
- **SC-002**: Nobody at a pilot business has to type the content of a quote to get it into the list; the only typed input is the customer name and, if not today, the sent date. — [F-050, F-051 · S3 04:20; F-070 · S4 slide 5] [ASSUMPTION: Q-09 default, see A-11]
- **SC-003**: Every quote with 7 days without answer produces exactly one reminder, and no quote receives a second reminder before its status is set to "followed up". — [F-015 · S1 §3; F-052 · S3 07:40]
- **SC-004**: During the pilot, every quote that ends as "lapsed" has at least one "followed up" before it; today an estimated 8 of 30 quotes lapse with no follow-up at all. — [F-005 · S1 §1; F-049 · S3 02:15]
- **SC-005**: The boss can read the hit rate of the last full month from the product instead of guessing ("vielleicht die Hälfte"). — [F-048 · S3 00:40; F-073 · S4 slide 5]
- **SC-006**: The office can work through the Monday list without asking anyone which quotes are open. — [F-004 · S1 §1; F-017 · S1 §3]
- **SC-007**: Nobody signs in during the pilot; the only access steps a person ever takes are opening the business's link and picking their name once per device. — [F-054 · S3 09:10; F-023 · S1 §6] [Q-02 resolved · R1-03, R1-04] ⟲ v0.2 · R1-03
- **SC-008**: At a pilot business, at least two quotes per year that received a reminder and a follow-up end as "accepted"; that is the value Weber named for 30 € a month. — [F-059 · S3 13:30; F-066 · S4 slide 3]

## 10 Assumptions

Everything the AI filled in without a source. Each item names what it was derived from and which section uses it.

- **A-01**: This spec is written for GaLaBau businesses only; other trades are a later market. — Resolved in v0.2: C-01 settled as "GaLaBau only" by R1-01, no longer an assumption (was: C-01 unresolved, S1 high over S4 medium, F-006 · S1 §2 against F-067, F-069 · S4 slide 4); was used in §2, §4 Out of scope ⟲ v0.2 · R1-01
- **A-02**: The target business has 5 to 50 employees. — Resolved in v0.2: C-02 settled as "5 to 50 employees" by R1-02, which sets S4 slide 4 aside as a requirement source for version 1; no longer an assumption (was: C-02 unresolved, S1 high over S4 medium, F-006, F-007 · S1 §2 against F-068 · S4 slide 4); was used in §2 ⟲ v0.2 · R1-02
- **A-03**: Version 1 contains feature-list priorities 1 and 2; priority 3 (rejection reason, offline, login) is out. — Q-01 default, derived from S2 rows 2–16, 31 (sheet Features); used in §4
- **A-04**: Replaced in v0.2: one access link per business, a person picks their name once per device, no sign-in of any kind; decided by R1-03 with the R1-04 answer (b), no longer an assumption (was: a person is identified by a one-time join per device through an invite link, Q-02 default, derived from F-036 · S2 row 11 (sheet Features), F-023 · S1 §6, F-054 · S3 09:10); was used in §2, §8, FR-029, SCR-08, FLOW-07, SC-007 ⟲ v0.2 · R1-03
- **A-05**: Reminders arrive as push on the phone, or by email if the person chose email at first use. — Q-03 default, derived from F-037 · S2 row 12 (sheet Features) and F-071 · S4 slide 5; used in FR-020, SCR-05, SCR-08 ⟲ v0.2 · R1-03
- **A-06**: The reminder goes to the site manager the quote is assigned to; the office sees the same quote in the Monday list. — Q-04 default, derived from F-052 · S3 07:40 and F-018 · S1 §4; used in FR-019, FLOW-02
- **A-07**: The reminder period is fixed at 7 days in version 1. — Q-05 default, derived from F-015 · S1 §3 and the open question in F-029 · S2 row 4 (sheet Features); used in FR-007, §4 Out of scope
- **A-08**: The 7-day period restarts when the status is set to "followed up"; at most one reminder per period. — Q-06 default, derived from F-052 · S3 07:40; used in FR-007, FR-018, FR-022, FLOW-02
- **A-09**: "Open" means status sent or followed up; accepted, declined and lapsed quotes leave the open list but remain findable through search and the status filter. — Q-07 default, derived from F-019 · S1 §4; used in FR-006, FR-008, FR-009, FR-012, FLOW-06
- **A-10**: "Lapsed" is set by hand; nothing lapses automatically. — Q-08 default; used in FR-017, §4 Out of scope
- **A-11**: Customer name and sent date are mandatory when adding a quote, the sent date preset to today; quote number and amount are optional. — Q-09 default, derived from F-013 · S1 §3, F-035, F-039 · S2 rows 10, 14 (sheet Features) against F-024 · S1 §6, F-051 · S3 04:20; used in FR-002, SCR-02, SC-002
- **A-12**: A quote can be saved without its file and the file attached later; there is no automatic text recognition. — Q-10 default; used in FR-003, FLOW-01, §4 Out of scope
- **A-13**: The feature-list row titled "Export nach Excel" means a one-time import of existing quotes at the start; there is no export in version 1. — Resolved in v0.2: Q-11 settled as "import only" by R1-05, no longer an assumption (was: Q-11 default, derived from the description in F-042 · S2 row 31 (sheet Features)); was used in JOB-08, §4, FR-031, SCR-10, FLOW-08 ⟲ v0.2 · R1-05
- **A-14**: The user interface is German only. — Q-12 default, derived from the language of S1–S4; used in §8
- **A-15**: Each business sees only its own data; data is kept until the business deletes it; hosting is in the EU. — Q-13 default, derived from F-075 · S4 slide 6; used in FR-032, §8
- **A-16**: The office sees all quotes of its business, like the boss. — Q-14 default, derived from F-031 · S2 row 6 (sheet Features); used in FR-010
- **A-17**: Every quote is assigned to exactly one site manager, by default the person adding it; one person can hold more than one role, and field crew who only set a status act as site managers. — derived from F-036, F-031 · S2 rows 11, 6 (sheet Features) and F-052, F-056 · S3 07:40, 10:45; used in §2, FR-005
- **A-18**: The boss maintains the business's list of people and their roles and shares the access link. — derived from F-008, F-009 · S1 §2 (the boss decides); used in FR-030, SCR-09, FLOW-07 ⟲ v0.2 · R1-03
- **A-19**: The hit rate month is the month of the sent date; the denominator is all quotes sent in that month, including those still open. — derived from "pro Monat" in F-033 · S2 row 8 (sheet Features); used in FR-026, FLOW-05
- **A-20**: A status can be set again to correct it, and the date of every status change is kept. — derived from F-033 · S2 row 8 (sheet Features) and Q-06 default; used in FR-016, FLOW-03
- **A-21**: The Monday list holds the open quotes whose follow-up date is today or earlier, and shows the latest note per row. — derived from F-017 · S1 §3, F-031 · S2 row 6 (sheet Features), F-045 · S2 row 4 (sheet Rollen) and F-013 · S1 §3; used in FR-024, FR-025, SCR-06, FLOW-04
- **A-22**: The lists mark quotes whose follow-up date is today or past. — derived from F-013 · S1 §3 and F-053 · S3 07:40; used in FR-013
- **A-23**: There are no brand assets; the tone is plain trade language. — derived from the wording in S1 §3 and S3 07:40, 10:45; used in §8
- **A-24**: The takeover works by uploading the file, matching columns, previewing and confirming; unreadable rows are skipped; imported quotes get status "sent" and their follow-up date from their sent date. — derived from F-042 · S2 row 31 (sheet Features); used in FR-031, SCR-10, FLOW-08
- **A-25**: Any role can add a quote, not only the site manager. — derived from F-050 · S3 04:20 (the owner forwards the PDF) and F-018 · S1 §4 (office is part of the flow); used in FR-001

## 11 Open Questions

Questions no source answers. Each names the section that carries an assumption until answered.

- **C-01**: Is this spec for GaLaBau only, or for all trades with GaLaBau as the first market? — Resolved in v0.2 (R1-01): GaLaBau only; S1 §2 stands, S4 slide 4 is set aside for version 1. Affected §2, §4 Out of scope, A-01 ⟲ v0.2 · R1-01
- **C-02**: Which size band applies: 5–50 employees (S1) or 3–100 (S4)? — Resolved in v0.2 (R1-02): 5–50 employees; S4 slide 4 is not a requirement source for version 1. Affected §2, A-02 ⟲ v0.2 · R1-02
- **Q-01**: Which feature-list priorities are in version 1: only priority 1, or priorities 1 and 2? — affects §4, A-03; carries a clarification marker
- **Q-02**: How does the product know who is using it, given that a login every time is rejected? — Resolved in v0.2 (R1-03, R1-04 answer b): one access link per business, a person picks their name once per device, no sign-in of any kind. Affected §2, §8, FR-029, SCR-08, SCR-09, A-04; clarification marker removed ⟲ v0.2 · R1-03
- **Q-03**: Reminder channel: push, email, or both? — affects FR-020, SCR-05, SCR-08, A-05
- **Q-04**: Who receives the 7-day reminder: the person who added the quote, the office, the boss, or all of them? — affects FR-019, FLOW-02, A-06
- **Q-05**: Is the 7-day period fixed or configurable per business? — affects FR-007, §4 Out of scope, A-07
- **Q-06**: Does the reminder timer restart on "followed up", and can one quote get more than one reminder? — affects FR-007, FR-018, FR-022, A-08
- **Q-07**: Which statuses count as "open"? — affects FR-006, FR-008, FR-009, FR-012, SCR-01, A-09
- **Q-08**: Is "lapsed" set by hand or automatically? — affects FR-017, A-10
- **Q-09**: Which fields are mandatory when a quote is added as photo or PDF? — affects FR-002, SCR-02, SC-002, A-11; carries a clarification marker
- **Q-10**: What happens when the photo or PDF cannot be attached? — affects FR-003, FLOW-01, A-12
- **Q-11**: Does the feature-list row "Export nach Excel" mean import at start, export, or both? — Resolved in v0.2 (R1-05): one-time import at the start, no export in version 1. Affected JOB-08, §4, FR-031, SCR-10, A-13 ⟲ v0.2 · R1-05
- **Q-12**: UI language: German only, or more? — affects §8, A-14
- **Q-13**: Data protection: separation between businesses, hosting region, retention, deletion? — affects FR-032, §8, A-15
- **Q-14**: Does the office see the quotes of all site managers, like the boss? — affects FR-010, A-16

Note from the source inventory, not a spec question: the feature list (S2, sheet Features) jumps from Nr 15 to Nr 30; features 16–29 are either not yet written or were deleted. If they exist, they are missing from this draft. See `inputs/INVENTORY.md`, "Needs attention".

## 12 Clarifications

<!-- /speckit-clarify appends "### Session YYYY-MM-DD" blocks here. Leave the heading in place. -->

## 13 Removed (Tombstones)

Items removed after review. The ID stays reserved; the line points to the round and the decision.

- None in v0.1 or v0.2.
