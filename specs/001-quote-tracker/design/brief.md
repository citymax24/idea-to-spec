# Design Brief: Quote Tracker

Derived from `spec.md` v0.3 (git tag `spec-quote-tracker-v0.3`, commit 89c1329) on 2026-09-05. **DRAFT: derived from an unaccepted spec (status `in-review`) — for an early look only.** Screens, fields and rules can still change through feedback rounds; two clarification markers (Q-01, Q-09) are open, see "Gaps a designer may hit".

This brief is a re-arrangement of the spec, not a second spec. If something here is wrong, the spec is wrong: open a feedback round, do not edit the brief.

## Product in one sentence

Every sent quote of a garden and landscaping business lands in one shared list sorted by follow-up date, triggers exactly one reminder after 7 days without an answer, and gets its status set after the call, so that no quote lapses unnoticed. [§1: F-013, F-015, F-018 · S1 §3–§4; F-052 · S3 07:40]

§1 also names "the boss sees how many quotes become orders" as the longer-term goal. That is the hit rate, a version-2 reporting topic removed from version 1 by DEC-001; nothing in the mockups shows it. See "Do not show".

## Users, context, devices

Target business: garden and landscaping businesses ("GaLaBau") with 5 to 50 employees; not corporations, not one-person businesses. Pilot businesses are Grünwerk GmbH and Weber Gartenbau; the prototype is due by October 2026. [§2; §8 Timeline and pilots]

| Role | Who they are | Device and situation | What they need from this |
|------|--------------|----------------------|--------------------------|
| Boss ("Chef") | Owner of a GaLaBau business with 5–50 employees; decides; weekly use. In a 12-person business the owner also writes the quotes himself. | Phone and desktop. | Overview of all quotes of the business. |
| Site manager ("Bauleiter") | Writes the quotes, is out in the field; daily use. | Almost only the phone, in the field, often with dirty hands or gloves: one-handed, large touch targets. | Their own open quotes in follow-up order, one reminder after 7 days, status in two taps. |
| Office ("Büro") | Maintains the data and phones customers; daily use. At Weber the owner's wife runs the office. | Desktop. | The Monday list to phone through, notes on quotes, sight of all quotes of the business. |

[§2 table: F-008–F-012 · S1 §2; F-043–F-045 · S2 rows 2–4 (sheet Rollen); F-046, F-052, F-055–F-057 · S3; §8 Devices / context]

One person can hold more than one role, for example an owner who is both boss and the person who writes quotes; field crew who only set a status on site act as site managers. [§2, A-17]

There is no sign-in of any kind. A business receives one access link; on first use on a device the person picks their name once from the business's list of people and is never asked again ("Bloß kein Login-Gedöns", "Wenn ich mich jedes Mal anmelden muss, benutz ich es nicht"). [§2, FR-029; F-023 · S1 §6; F-054 · S3 09:10]

Which screen belongs to which device (§8 Devices / context):

| Phone, one-handed, glove-sized targets | Desktop | Either device |
|---|---|---|
| SCR-01 Open quotes list, SCR-02 Add quote, SCR-03 Quote detail, SCR-04 Set status, SCR-05 Reminder | SCR-06 Monday list, SCR-10 Take over existing quotes | SCR-08 First use is opened on whatever device the person has (FLOW-07); SCR-09 People belongs to the boss, who uses both. The boss and office also open the phone screens on a desktop. |

## Tone and brand

No brand assets exist in any source. The tone is plain trade language as the users speak it ("Stups", "abtelefonieren", "nachfassen"), short labels, no jargon. [§8 Brand / tone; A-23]

The user interface is German. [§8 Language; A-14] The spec is written in English; the only German labels it fixes are the five statuses: verschickt (sent), nachgefasst (followed up), zugesagt (accepted), abgesagt (declined), verlaufen (lapsed). [FR-014, SCR-04] Every other label in the mockups is the designer's German wording in the tone above.

Colours, fonts and layout are not fixed by the spec.

## Screens in flow order

FLOW-01: SCR-01 → SCR-02 → SCR-03 → SCR-01. Then FLOW-02 adds SCR-05 and SCR-04, FLOW-04 adds SCR-06, FLOW-07 adds SCR-09 and SCR-08, FLOW-08 adds SCR-10. FLOW-03 and FLOW-06 add no new screen. No screen is outside a flow. Nine screens, in this order:

1. SCR-01 Open quotes list
2. SCR-02 Add quote
3. SCR-03 Quote detail
4. SCR-05 Reminder (push notification or email)
5. SCR-04 Set status
6. SCR-06 Monday list
7. SCR-09 People
8. SCR-08 First use (pick your name)
9. SCR-10 Take over existing quotes

The flows from §5, for the left-to-right order on the canvas:

| Flow | Screens |
|------|---------|
| FLOW-01 · Add a sent quote | SCR-01 → SCR-02 → SCR-03 → SCR-01 |
| FLOW-02 · Follow up after a reminder | SCR-05 → SCR-03 → SCR-04 → SCR-03 → SCR-01 |
| FLOW-03 · Set the status on site | SCR-01 → SCR-04 → SCR-01 |
| FLOW-04 · Monday phone-through | SCR-06 → SCR-04 → SCR-06 → SCR-03 → SCR-06 → SCR-01 |
| FLOW-06 · Find a quote | SCR-01 → SCR-03 → SCR-01 |
| FLOW-07 · Set up the people and first use | SCR-01 → SCR-09 → SCR-08 → SCR-01 |
| FLOW-08 · Take over existing quotes | SCR-01 → SCR-10 → SCR-01 |

FLOW-05 (hit rate) and SCR-07 (hit rate screen) were removed in v0.3; they are tombstones in §13 and must not be drawn.

### SCR-01 · Open quotes list — [F-013 · S1 §3; F-025 · S2 row 2 (sheet Features)] ⟲ v0.3 · R2-01, R2-02

- **Purpose**: See every open quote (own quotes for a site manager, all quotes of the business for boss and office) in the order they need a follow-up call, and act on one directly.
- **Primary action**: Set the status of a quote (tap the row, tap the status).
- **Content**: List rows with customer name, quote number (if present), sent date, follow-up date with an overdue marker, status, site manager (boss and office only), latest note in one line; fixed sort by follow-up date ascending; filter by status (default: open); filter by site manager (boss and office only); search field for customer or quote number; "Add quote" button; entries to the Monday list (office), people (boss) and takeover (office). ⟲ v0.3 · R2-01
- **States**: empty (no open quotes: nothing to follow up) / loaded / loading / filtered or searched with no match / error (list cannot be loaded).
- **Satisfies**: FR-004, FR-006, FR-008, FR-009, FR-010, FR-011, FR-012, FR-013, FR-015, FR-024
- **Comes from**: SCR-02, SCR-03, SCR-04, SCR-06, SCR-08, SCR-09, SCR-10 · **Leads to**: SCR-02, SCR-03, SCR-04, SCR-06, SCR-09, SCR-10 ⟲ v0.3 · R2-02

**Design prompt**: This is the home screen and the one a site manager opens in the field with gloves on, so draw it for a phone held in one hand. It shows the quotes that still need a follow-up call, most urgent first: the list is always sorted by follow-up date ascending, and every quote whose follow-up date is today or in the past carries an overdue marker, so the eye should land on the top rows and their markers. The one primary action is setting a status: tap a row, tap a status on SCR-04, done; the row itself is a glove-sized target. Each row shows customer name, quote number if there is one, sent date, follow-up date with the overdue marker, status, the site manager (boss and office only) and the latest note in one line. Around the list: a status filter with "open" as default, a site manager filter (boss and office only), a search field for customer name or quote number, an "Add quote" button, and entries to the Monday list (office), People (boss) and Take over (office). Draw two loaded variants: the site manager's view (own quotes only, no site manager column, no site manager filter, none of the three entries) and the boss or office view (all quotes, site manager column and filter, the entries). Also draw: empty (no open quotes, and the screen says there is nothing to follow up), loading, filtered or searched with no match, and error (list cannot be loaded). The boss and office also open this list on a desktop; if you draw a desktop artboard, keep the same content and order.

### SCR-02 · Add quote — [F-032 · S2 row 7 (sheet Features); F-050 · S3 04:20; F-070 · S4 slide 5]

- **Purpose**: Get a quote that was just sent into the list as a photo or PDF with the least possible typing.
- **Primary action**: Attach the file and save.
- **Content**: File input that accepts a photo taken now, a photo from the device, or a PDF, including a PDF handed over from another app (forwarded mail); preview of the attached file; fields: customer name (required), sent date (required, preset to today), quote number (optional), amount in euros (optional), site manager (preset to the current user if they are a site manager, otherwise chosen from the business's site managers); "Save" and "Save without file".
- **States**: empty form / file attached with preview / saving / saved / error (file cannot be attached: offer "Save without file").
- **Satisfies**: FR-001, FR-002, FR-003, FR-005, FR-028
- **Comes from**: SCR-01 · **Leads to**: SCR-03

**Design prompt**: This screen exists so that a quote that was just sent gets into the list without typing it in: a photo of the printout or the PDF is the quote. Draw it for the phone. The eye lands on the file input, which offers three ways in: take a photo now, pick a photo from the device, or pick a PDF; the same screen opens with the file already attached when a PDF is handed over from another app, for example a forwarded mail. The one primary action is attach the file and save. The rest of the content: a preview of the attached file, and the fields customer name (required, and in the normal case the only thing typed), sent date (required, preset to today), quote number (optional), amount in euros (optional) and site manager (preset to the current user if they are a site manager, otherwise a pick from the business's site managers). Two buttons: "Save" and "Save without file". Draw: empty form, file attached with preview, saving, saved, and error where the file cannot be attached and "Save without file" is offered. Saving leads to SCR-03.

### SCR-03 · Quote detail — [F-016 · S1 §3; F-053 · S3 07:40]

- **Purpose**: See everything about one quote, add a note, change its status or attach the missing file.
- **Primary action**: Set the status.
- **Content**: Attached photo or PDF, viewable at full size, or "No file yet" with an attach action; customer name, quote number, amount, sent date, follow-up date, site manager, all editable; current status as a large button that opens SCR-04; notes in date order with an "Add note" field; dates of the status changes so far.
- **States**: loaded / no file attached / loading / error (quote cannot be loaded or saved).
- **Satisfies**: FR-003, FR-014, FR-016, FR-021, FR-023, FR-028
- **Comes from**: SCR-01, SCR-02, SCR-05, SCR-06 · **Leads to**: SCR-04, SCR-01, SCR-06

**Design prompt**: One quote, everything about it. The site manager arrives here from a reminder to see whom to call and, after the call, to set the status; the office arrives here to add a note. Draw it for the phone; the office also reads it at a desktop. The eye should land on the customer name and the current status, which is a large button that opens SCR-04; that button is the one primary action. The rest of the content: the attached photo or PDF, viewable at full size, or "No file yet" with an attach action; the fields customer name, quote number, amount, sent date, follow-up date and site manager, all editable; the notes in date order with an "Add note" field; and the dates of the status changes so far. Draw: loaded, no file attached, loading, and error (quote cannot be loaded or saved).

### SCR-05 · Reminder (push notification or email) — [F-015 · S1 §3; F-052 · S3 07:40; F-037 · S2 row 12 (sheet Features)]

- **Purpose**: Nudge the responsible person exactly once that a quote has waited 7 days without an answer.
- **Primary action**: Open the quote.
- **Content**: Customer name, quote number if present, sent date, "7 days without answer", and the quote as the target of the tap or link; as email the same content with a link to the quote.
- **States**: push delivered / email delivered / opened (leads to SCR-03).
- **Satisfies**: FR-018, FR-019, FR-020, FR-021
- **Comes from**: — (triggered by the 7-day rule) · **Leads to**: SCR-03

**Design prompt**: This is not an app screen but the nudge itself: exactly one push notification on the phone, or one email if the person chose email at first use, sent to the site manager the quote is assigned to when the quote has waited 7 days without an answer. Draw both: the push notification as it appears on a phone, and the email. Both carry the customer name, the quote number if present, the sent date and the line that says 7 days without answer; the whole notification, or a link in the email, opens the quote (SCR-03). The one primary action is open the quote. The eye lands on the customer name: that is whom to call. Tone: a "Stups", one short nudge, not an alarm and not a series. Draw: push delivered and email delivered; the opened state is SCR-03 and needs no artboard of its own.

### SCR-04 · Set status — [F-027 · S2 row 3 (sheet Features); F-057 · S3 12:10; F-072 · S4 slide 5]

- **Purpose**: Change the status of one quote with one tap after the quote was picked.
- **Primary action**: Tap one of the five statuses; the tap saves.
- **Content**: Customer name and quote number of the quote; five large buttons: sent ("verschickt"), followed up ("nachgefasst"), accepted ("zugesagt"), declined ("abgesagt"), lapsed ("verlaufen"); the current status is marked; no further confirmation step.
- **States**: open (buttons shown) / saved (short confirmation, returns to the calling screen) / error (could not save: buttons stay, error shown).
- **Satisfies**: FR-014, FR-015, FR-017
- **Comes from**: SCR-01, SCR-03, SCR-06 · **Leads to**: SCR-01, SCR-03, SCR-06 (the screen it was opened from)

**Design prompt**: The second of the two taps. The quote was picked on the previous screen; here the status is set with one tap, and that tap saves, with no confirmation step. Draw it for a phone used with gloves: the eye lands on five large buttons with the German labels the spec fixes, verschickt, nachgefasst, zugesagt, abgesagt, verlaufen; the current status is marked. The customer name and quote number of the quote are on the screen so the user knows what they are setting. Draw: open (buttons shown), saved (a short confirmation, then return to the screen it was opened from: SCR-01, SCR-03 or SCR-06), and error (could not save: buttons stay, error shown). The screen is also opened from the Monday list at the desktop; keep the same five buttons there.

### SCR-06 · Monday list — [F-017 · S1 §3; F-031 · S2 row 6 (sheet Features); F-045 · S2 row 4 (sheet Rollen)]

- **Purpose**: Let the office work through every quote that is due for a follow-up call in one sitting at the desktop.
- **Primary action**: Set the status of a row after the call.
- **Content**: Table of open quotes whose follow-up date is today or earlier: customer name, quote number, sent date, days waiting, site manager, latest note, status; filter by site manager; count of rows; per row: set status (opens SCR-04), open quote to add a note (opens SCR-03); a row that got a new status leaves the table.
- **States**: empty (nothing due today) / loaded / loading / filtered with no match / error.
- **Satisfies**: FR-010, FR-011, FR-013, FR-024, FR-025
- **Comes from**: SCR-01, SCR-03, SCR-04 · **Leads to**: SCR-03, SCR-04, SCR-01

**Design prompt**: The office's Monday morning at the desktop: every open quote of the business whose follow-up date is today or earlier, worked through in one sitting by phone ("abtelefonieren"). Draw it as a desktop table. The eye should land on the count of rows and the first row to call. The one primary action is setting the status of a row after the call, which opens SCR-04; from each row the office can also open the quote to add a note (SCR-03). Columns: customer name, quote number, sent date, days waiting, site manager, latest note, status. A filter by site manager. A row that got a new status leaves the table, so the list shrinks as the morning goes on. Draw: empty (nothing due today, and the screen says so), loaded, loading, filtered with no match, and error.

### SCR-09 · People — [F-008 · S1 §2; F-036 · S2 row 11 (sheet Features)] [Q-02 resolved · R1-03, R1-04] [ASSUMPTION: derived from F-009 · S1 §2 (the boss decides); no source describes how people are added, see A-18] ⟲ v0.2 · R1-03

- **Purpose**: Let the boss see who belongs to the business, add people with their roles and share the business's one access link.
- **Primary action**: Add a person with a name and a role.
- **Content**: The business's access link with a copy or share action; list of people with name, role (boss, site manager, office) and date of first use; "Add person" with name and role picker; change a role; remove a person.
- **States**: only me / loaded / person added / error.
- **Satisfies**: FR-010, FR-030
- **Comes from**: SCR-01 · **Leads to**: SCR-01

**Design prompt**: The boss's screen for who belongs to the business and how they get in. The eye lands on the list of people, each with name, role (boss, site manager, office) and date of first use, and on "Add person", the one primary action: a name and a role picker, nothing else. The business's one access link is shown with a copy or share action, because sharing that link is how everyone gets in; there are no per-person invites and no passwords. Also on the screen: change a role, remove a person. The boss uses phone and desktop; draw the phone version and make sure nothing in it depends on a wide screen. Draw: only me (the boss alone, right after the start), loaded, person added, and error.

### SCR-08 · First use (pick your name) — [F-023 · S1 §6; F-054 · S3 09:10] [Q-02 resolved · R1-03, R1-04] [ASSUMPTION: Q-03 default, see A-05] ⟲ v0.2 · R1-03

- **Purpose**: Let a person who opened the business's access link on a device say once who they are, without a password or any sign-in.
- **Primary action**: Pick your name and reminder channel and enter the list.
- **Content**: Business name from the link; the business's list of people to pick from, each with name and role as set by the boss, role shown but not editable; reminder channel: push on this device or email, with an email field; "Start" button.
- **States**: valid link / invalid link (error, ask the boss for the business's current link) / name not in the list (hint, ask the boss to add you) / notifications not allowed on this device (hint, email offered) / done (this device remembers the pick).
- **Satisfies**: FR-020, FR-029
- **Comes from**: — (opened from the business's access link) · **Leads to**: SCR-01

**Design prompt**: The only thing a person ever does to get in: open the business's link on their own device, say who they are, choose how reminders reach them, and enter the list. Seen once per device, never again. Draw it for the phone first, because site managers open it there; the office opens it on a desktop. The eye lands on the business name from the link and the list of the business's people to pick from, each with name and role as set by the boss, role shown but not editable. Then the reminder channel, push on this device or email, with an email field, and a "Start" button, the one primary action: pick your name and channel, tap Start, land in SCR-01. No password, no account, no registration field of any kind. Draw: valid link, invalid link (error, ask the boss for the business's current link), name not in the list (hint, ask the boss to add you), notifications not allowed on this device (hint, email offered), and done (this device remembers the pick).

### SCR-10 · Take over existing quotes — [F-042 · S2 row 31 (sheet Features)] [Q-11 resolved · R1-05] [ASSUMPTION: takeover mechanics, see A-24] ⟲ v0.2 · R1-05

- **Purpose**: Bring the open quotes from the old Excel list into the product once at the start.
- **Primary action**: Upload the file and confirm the takeover.
- **Content**: File upload; column matching for customer, sent date, quote number, amount and site manager; preview of the rows with unreadable rows marked; "Take over" button; result summary with the number imported and skipped.
- **States**: empty / file loaded (matching) / preview / done / error (file cannot be read).
- **Satisfies**: FR-031
- **Comes from**: SCR-01 · **Leads to**: SCR-01

**Design prompt**: A one-time desktop screen for the office at the start: the old Excel list of open quotes comes in once, so nobody keeps two lists. The eye lands on the file upload; the one primary action is upload the file and confirm the takeover. Content, following the states: the upload; the matching of the file's columns to customer, sent date, quote number, amount and site manager; a preview of the rows with unreadable rows marked; the "Take over" button; and a result summary with the number imported and the number skipped. Imported rows become open quotes with status "sent". There is no export in the other direction. Draw: empty, file loaded (matching), preview, done, and error (file cannot be read).

## Constraints

From §8, verbatim:

- **Devices / context**: The site manager uses only the phone, in the field, often with dirty hands or gloves, so the open list, add quote, quote detail, status and reminder must work one-handed on a phone with large touch targets; the office works at a desktop, so the Monday list and the takeover are desktop screens; the boss uses both phone and desktop. — [F-012 · S1 §2; F-043, F-044, F-045 · S2 rows 2–4 (sheet Rollen); F-057 · S3 12:10] [R2-01] ⟲ v0.3 · R2-01
- **Language**: German user interface; all sources and both pilot businesses are German-speaking. — [ASSUMPTION: Q-12 default, see A-14]
- **Brand / tone**: No brand assets exist in any source; the tone is plain trade language as the users speak it ("Stups", "abtelefonieren", "nachfassen"), short labels, no jargon. — [ASSUMPTION: derived from S1 §3 and S3 07:40, 10:45, see A-23]
- **Legal / data**: Quotes, photos, PDFs and notes contain customer personal data; each business sees only its own data, the data is kept until the business deletes it, and it is hosted in the EU. — [ASSUMPTION: Q-13 default, see A-15]
- **Identity**: No sign-in of any kind: one access link per business, and a person picks their name once per device from the business's list; no password, never asked again. — [F-023 · S1 §6; F-054 · S3 09:10; F-041 · S2 row 16 (sheet Features)] [Q-02 resolved · R1-03, R1-04] ⟲ v0.2 · R1-03
- **Timeline and pilots**: Prototype by October 2026; pilot businesses are Grünwerk GmbH and Weber Gartenbau. — [F-074, F-075 · S4 slide 6]
- **Price**: No pricing inside the product; the price is set after the pilot, against a stated pain threshold of 20–30 € per month for a single-purpose tool and a stated value of 30 € per month for two saved orders a year. — [F-076, F-065 · S4 slides 6, 3; F-059 · S3 13:30]

Two rules that shape every list without being a screen: the follow-up date is 7 days after the sent date, or 7 days after the last time the status was set to "followed up" (FR-007); "open" means status sent or followed up, and a quote that becomes accepted, declined or lapsed leaves the open list at once but stays findable through search and the status filter (FR-006, FR-012).

## Do not show

From §4 Out of scope. None of these gets a screen, a field, a button or a menu entry:

- Quote creation or calculation; no editor for the content of a quote. Businesses keep their existing program. [F-020 · S1 §5]
- Connection to accounting or ERP. [F-021 · S1 §5]
- Customer records or customer management; the customer is a name on the quote, not a record of its own. [F-022 · S1 §5]
- Rejection reason on decline (price, date, competitor, other); priority 3. [F-038 · S2 row 13; A-03]
- Offline reading of the list, offline indicators; priority 3. [F-040 · S2 row 15; A-03]
- Sign-in per user with a password, accounts, registration, "forgot password"; rejected by Jonas and by Weber. [F-041 · S2 row 16; F-023 · S1 §6; F-054 · S3 09:10]
- Export to Excel; the takeover (SCR-10) is import only. [F-042 · S2 row 31; Q-11 resolved · R1-05]
- A configurable reminder period; 7 days is fixed, there is no setting for it. [F-029 · S2 row 4; A-07]
- Automatic text recognition of the attached photo or PDF; no fields pre-filled from the scan. [A-12]
- Automatic lapsing of a quote; "lapsed" is set by hand. [A-10]
- Pricing, billing and subscriptions inside the product. [F-076 · S4 slide 6]
- Other trades (painters, roofers, plumbing/heating) as target users; GaLaBau only. [F-067, F-069 · S4 slide 4; C-01 resolved · R1-01]
- Hit rate per month for the boss, in count or in euros: no chart, no KPI, no "won" share anywhere. [F-033 · S2 row 8; F-073 · S4 slide 5; R2-01 · DEC-001]

From §13 Tombstones (removed in v0.3, decision DEC-001; do not resurrect from the same sources):

- FR-026 · Hit rate per month for the boss: accepted quotes as a share of all quotes sent in that month
- FR-027 · Hit rate in euros where amounts were captured
- FLOW-05 · Check the hit rate (SCR-01 → SCR-07 → SCR-01)
- SC-005 · The boss reads the hit rate of the last full month instead of guessing
- SCR-07 · Hit rate screen: one row per month with counts, share and euros

The quote amount stays as an optional field on SCR-02, SCR-03 and in the SCR-10 column matching (FR-028, R2-03 answer a); nothing is computed or shown from it.

## Gaps a designer may hit

Say so, do not fill them in the canvas; each is a feedback round (`/speckit-idea-feedback`).

- **Q-01 is open** (clarification marker in §4): no source maps a feature-list priority to a version. The brief follows the spec's default, priorities 1 and 2 in version 1 except the hit rate. If the answer is "priority 1 only", SCR-06 Monday list, SCR-09 People, SCR-10 Take over, the search field, the site manager filter, the quote amount and the push channel leave the mockups.
- **Q-09 is open** (clarification marker under FR-002): which fields must be typed when a quote is added as photo or PDF. SCR-02 follows the default: customer name and sent date required, quote number and amount optional.
- **Product name**: "Quote Tracker" is the working title of the spec; no source names the product, and the UI is German. Use the working title as a placeholder in the mockups.
- **German labels** other than the five statuses are not fixed by the spec. The designer writes them in plain trade language; if the reviewer wants specific words fixed, that is a feedback round, not a canvas edit.
- **"Days waiting"** on SCR-06 has no definition in the spec (since the sent date, or since the last "followed up"). The mockup can show a number; the definition needs a feedback round before anyone builds it.
- **Desktop versions** of SCR-01, SCR-03 and SCR-09 for the boss and office: §8 fixes the phone for the site manager's screens and the desktop for the office's, but does not say what changes on a desktop. Keep the content identical; desktop-only content would be a spec change.

## Hand-off

- One artboard per screen, named exactly `<SCR-ID> <Screen name>`: `SCR-01 Open quotes list`, `SCR-02 Add quote`, `SCR-03 Quote detail`, `SCR-05 Reminder (push notification or email)`, `SCR-04 Set status`, `SCR-06 Monday list`, `SCR-09 People`, `SCR-08 First use (pick your name)`, `SCR-10 Take over existing quotes`.
- Flow order left to right: FLOW-01 first, then the flow table above.
- States as separate artboards where the design prompts list them.
- Exports go to `design/mockups/v0.3/`.
- Mockup feedback has two lanes (see `design/README.md`): visual stays in the canvas; content or flow goes back through `/speckit-idea-feedback`, and after `/speckit-idea-apply` the affected artboards are regenerated. Because this brief is a DRAFT, expect the spec to move before acceptance; artboards drawn now are an early look, not the v1.0 mockups.
