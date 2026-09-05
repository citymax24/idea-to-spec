# Design Brief: Quote Follow-Up Tracker

Derived from `spec.md` v1.2 (git tag `spec-test-inbox-v1.2`) on 2026-09-05.

This brief is a re-arrangement of the spec, not a second spec. If something here is wrong, the spec is wrong: open a feedback round, do not edit the brief.

## Product in one sentence

One list of the open quotes of a garden and landscaping company, sorted by the date follow-up is due, that raises a single reminder after seven days and takes two taps to update, so that no quote dies unanswered.

## Users, context, devices

Three roles in companies with 5 to 50 employees:

- **Bauleiter** (site manager) — writes the quotes, is out on site, uses a **phone daily**, often with dirty hands or gloves. Two taps and it has to be done, otherwise it gets put off to the evening and forgotten. He is the hardest case and the one the phone screens are designed for.
- **Büro** (office) — uses a **desktop daily**. Works the Monday call list, keeps the notes, phones after.
- **Chef** (owner) — uses **phone and desktop, weekly**. Wants the overview and the win rate.

The **administrator right** sits beside these three roles: any user can hold it, and a company holds at least two, so nobody can lock the company out.

Every screen has to work on a phone; SCR-04 and SCR-05 are used mainly on a desktop.

## Tone and brand

No brand assets and no tone of voice exist yet (assumption A-03; no source states any). Plain, workmanlike German without marketing tone. Interface language is **German only** — write the artboards in German, keeping the five status words verbatim: "verschickt", "nachgefasst", "zugesagt", "abgesagt", "verlaufen".

## Screens in flow order

FLOW-01: SCR-06 → SCR-07 → SCR-08 → SCR-01. FLOW-02: SCR-01 → SCR-02 → SCR-01. FLOW-03 and FLOW-04: SCR-01 → SCR-03 → SCR-01. FLOW-05: SCR-01 → SCR-04 → SCR-03 → SCR-04. FLOW-06: SCR-01 → SCR-05 → SCR-01. FLOW-07: SCR-01 → SCR-08 → SCR-01. Every screen sits in a flow; none is left over.

### SCR-06 · Sign in

- **Purpose**: Identify the user and the company whose quotes are shown.
- **Primary action**: Sign in.
- **Content**: Fields for the user's credentials, company context after sign-in.
- **States to show**: empty / signing in / error (wrong credentials) / offline (blocked, with a reason).
- **Satisfies**: FR-021, FR-022
- **Leads to**: SCR-07, SCR-01

**Design prompt**: The first screen a user ever sees, and the one a pilot customer already resents — he says he has twelve passwords and will not use a tool that makes him sign in every time. So draw it as small as a sign-in can be: the credential fields are the whole screen, the eye lands on them immediately, and nothing competes with the single sign-in action. After signing in the user's company is named somewhere quiet, so it is obvious whose quotes will follow. Draw the error state as a wrong-credentials message that does not clear what was typed, and the offline state as the sign-in action disabled with a plain sentence saying why.

### SCR-07 · Take over the old Excel list

- **Purpose**: Carry the existing quotes over once when a company starts.
- **Primary action**: Run the import.
- **Content**: File picker for the old Excel list, preview of the rows that were recognised, report of rows that could not be read, "skip" option.
- **States to show**: empty / preview / importing / partial error / done.
- **Satisfies**: FR-026
- **Leads to**: SCR-08

**Design prompt**: A screen seen exactly once, when a company starts. The eye lands on the file picker; the primary action is running the import. The preview of recognised rows is what earns trust, so give it room and show real quote rows, not a count. The partial-error state matters more than the happy path: some rows will not be readable, and the screen has to say which ones without making the whole import feel failed. "Skip" is always available and never the loudest thing on the screen — a company may prefer to start empty.

### SCR-01 · Open quotes

- **Purpose**: Show everything that is still open, in the order in which it needs attention.
- **Primary action**: Open a quote to set its status.
- **Content**: Table (customer, quote number, amount, sent date, follow-up date, status), status filter, search field, button "new quote", marker on quotes whose follow-up date has passed.
- **States to show**: empty / loaded / error / offline (readable, not editable).
- **Satisfies**: FR-004, FR-006, FR-007, FR-008, FR-016, FR-017, FR-024
- **Leads to**: SCR-02, SCR-03, SCR-04, SCR-05, SCR-08

**Design prompt**: The home of the product and the screen everyone opens first. It shows only open quotes, sorted so that whatever needs attention soonest is at the top; a quote whose follow-up date has passed carries a marker that is readable at arm's length on a phone in daylight. The eye lands on the top row, not on the filters. The primary action is opening a quote to set its status, so rows are large touch targets — remember the gloves. Status filter and search sit above the list without dominating it; "new quote" is a distinct action, reachable with one thumb. Draw the empty state as a real first-run screen for a company that has not registered a quote yet, and the offline state with the list fully readable and every editing affordance visibly disabled.

### SCR-02 · New quote

- **Purpose**: Get a quote that has already been sent into the list without typing the quote itself.
- **Primary action**: Attach the photo or PDF and save.
- **Content**: File picker and camera capture, fields customer, quote number, amount, sent date; the follow-up date is shown as derived, not entered.
- **States to show**: empty / filled / saving / error / offline (blocked, with a reason).
- **Satisfies**: FR-001, FR-002, FR-003
- **Leads to**: SCR-01

**Design prompt**: Nobody will retype a quote — the photo or the PDF is the quote. So the camera and file picker come first and largest, and the four typed fields (customer, quote number, amount, sent date) follow as a short, obviously finite list. The follow-up date appears as a derived value the user reads rather than a field they fill; show it as seven days after the sent date. The eye lands on the capture action. Draw the filled state with a real attachment thumbnail visible, and the offline state as blocked with a plain sentence: this needs a connection.

### SCR-03 · Quote detail

- **Purpose**: See one quote in full and record what happened with it.
- **Primary action**: Set the status.
- **Content**: Customer and quote data, the attached photo or PDF, status control with the five values, free-text note, rejection reason (only on "abgesagt"), follow-up date.
- **States to show**: loaded / saving / error / offline (readable, status control disabled).
- **Satisfies**: FR-005, FR-006, FR-009, FR-014, FR-015, FR-025
- **Leads to**: SCR-01, SCR-04

**Design prompt**: This is where the two taps happen, standing on a building site with gloves on. The status control carries all five values — "verschickt", "nachgefasst", "zugesagt", "abgesagt", "verlaufen" — and is the first thing the eye lands on, above the quote data, not below it. Setting a status must be reachable in two taps from arriving on the screen. The rejection reason (price, date, competitor, other) appears only once "abgesagt" is chosen; draw both the before and after. The attached photo or PDF is viewable but secondary. The note is a plain free-text field. Draw the offline state with everything readable and the status control visibly disabled, saying why.

### SCR-04 · Monday call list

- **Purpose**: Give the office one list to phone through.
- **Primary action**: Open the next quote to be phoned.
- **Content**: Quotes due for follow-up with customer, phone-relevant data, note and last status change; filter by Bauleiter.
- **States to show**: empty (nothing due) / loaded / error.
- **Satisfies**: FR-018
- **Leads to**: SCR-03, SCR-01

**Design prompt**: A desktop screen for Monday morning: someone sits down with the phone and works top to bottom. Each row carries what a caller needs before dialling — customer, the note from last time, when the status last changed — so nothing has to be opened first to know what to say. The eye lands on the first quote to call. The filter by Bauleiter is a convenience above the list, not a gate. Draw the empty state as a good outcome, not a failure: nothing is due today.

### SCR-05 · Win rate

- **Purpose**: Show the Chef how many quotes become jobs.
- **Primary action**: Pick the month to look at.
- **Content**: Share of "zugesagt" across all quotes of the month by count and in euros, count of quotes in the month, month selector.
- **States to show**: empty (no quotes in the month) / loaded / error.
- **Satisfies**: FR-019, FR-020
- **Leads to**: SCR-01

**Design prompt**: The Chef looks at this weekly, often on a phone, and wants one number to land: the share of his quotes that became jobs this month. Show that share first and largest, with the same rate in euros beside it and the count of quotes in the month as context. The month selector is the primary action but sits quietly — the number is the screen. Draw the empty state for a month with no quotes as an honest "no quotes in this month", never a zero percent, which would read as a total loss.

### SCR-08 · User management

- **Purpose**: Administer the per-user accounts of one company and who may administer them.
- **Primary action**: Add a user to the company.
- **Content**: List of the company's users with name, role and whether they hold the administrator right; "add user" action; "remove user" action per row; a control per row to grant or withdraw the administrator right; a count of the company's administrators; note that a removed user keeps no access.
- **States to show**: loaded / adding / removing / setup (a second administrator is still missing) / error / offline (blocked, with a reason).
- **Satisfies**: FR-027, FR-028, FR-029, FR-031, FR-032, FR-033
- **Leads to**: SCR-01

**Design prompt**: Reached by any administrator, and rarely — when someone joins or leaves, or when the right moves. The eye lands on the list of the company's users; each row says plainly whether that person may administer. Adding a user is the primary action. Two things must be unmissable. First, the company's administrator count, because the rule is a minimum of two: show it, and show it as a warning while it stands at exactly two. Second, the refusal — with only two administrators left, neither removing one nor withdrawing the right is possible, and the screen has to say why rather than just disabling a control silently. Draw the setup state as its own screen: a fresh company has one administrator, the list invites naming a second, and nothing continues to the quote list until that is done. Nothing here needs to be quick; it needs to be unambiguous about who can currently see and administer the company's quotes.

## Constraints

- **Devices**: The Bauleiter works almost only on a phone, often with dirty hands; on site he wears gloves — two taps and it has to be done. The Chef uses phone and desktop weekly, the Bauleiter a phone daily, the Büro a desktop daily.
- **Language**: German only in version 1.
- **Brand / tone**: No brand assets or tone of voice exist; plain, workmanlike German without marketing tone (assumption A-03).
- **Legal / data**: Quotes hold customer names, notes and amounts — third-party personal data. Hosting in the EU, processing agreement available. One tenant per company, data separated between companies.
- **Adoption**: A pilot customer states he already has twelve passwords and will not use the tool if he has to sign in every time, while version 1 does have a per-user login. The sign-in screen should cost as little as a sign-in can.

## Do not show

From §4 "Out of scope" — a mockup must not resurrect any of these:

- Writing or calculating a quote. Companies keep doing that in their existing program; there is no quote editor anywhere.
- Any connection to accounting or ERP.
- Customer management beyond what the list itself needs — no customer records, no address book.
- Any sign that text is read out of the attached photo or PDF. There is no OCR: the fields are typed.
- Any per-Bauleiter restriction of visibility. Everyone in a company sees all of that company's quotes; the filter on SCR-04 is a convenience, never a permission.
- Editing anything while offline. The list is readable, nothing more.
- A setting for the follow-up interval. Seven days is fixed.
- Any price, plan or billing screen. The price is fixed only after the pilot.

§13 holds no tombstones — nothing has been removed from the spec yet.

## Open points a designer will hit

These are assumptions in the spec, not settled facts. Draw them as written; if the mockup makes one look wrong, that is a feedback round, not a brief edit. One assumption that used to stand here — "only the Chef administers users" — was found wrong exactly that way, by a reviewer using the prototype, and is now a decided requirement (FR-029, FR-031 to FR-033).

- **Who receives the seven-day reminder** is still open (Q-10). No screen shows the reminder itself; it arrives as a push notification or an email (FR-013) and drops the user on SCR-01.
- **"abgesagt" and "verlaufen" also remove a quote from the open list** (FR-008, assumption A-02) — only "zugesagt" is stated in the sources.

## Hand-off

- One artboard per screen, named exactly `<SCR-ID> <Screen name>` — e.g. `SCR-01 Open quotes`.
- Flow order left to right: SCR-06, SCR-07, SCR-01, SCR-02, SCR-03, SCR-04, SCR-05, SCR-08.
- States as separate artboards where listed above.
- Exports go to `design/mockups/v1.0/`.
