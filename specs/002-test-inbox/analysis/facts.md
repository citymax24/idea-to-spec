# Facts

Feature: `specs/002-test-inbox` · Extracted: 2026-09-05 · Sources: S1–S4

Every row is one atomic claim with one location. Claims are written in English; the quote keeps the source language. IDs are stable; new extractions append.

Categories: problem · user · job · scope · flow · screen · requirement · constraint · metric · market · other

| ID | Claim | Quote (verbatim, short) | Location | Category |
|----|-------|-------------------------|----------|----------|
| F-001 | Offers get lost in day-to-day work. | "Angebote gehen im Alltag unter." | S1 §1 | problem |
| F-002 | Jonas writes offers in the evening at the kitchen table, sends them by mail and forgets to follow up. | "Jonas schreibt Angebote abends am Küchentisch, schickt sie per Mail und vergisst nachzufassen." | S1 §1 | problem |
| F-003 | Petra does not know which offers are open as long as nobody asks. | "Petra weiß nicht, welche Angebote offen sind, solange niemand fragt." | S1 §1 | problem |
| F-004 | In spring an estimated 8 of 30 offers at Grünwerk fizzled out, with no rejection and no follow-up. | "geschätzt 8 von 30 Angeboten einfach verlaufen, ohne Absage und ohne Nachfrage" | S1 §1 | metric |
| F-005 | Target group is garden and landscaping companies with 5 to 50 employees. | "Garten- und Landschaftsbaubetriebe mit 5 bis 50 Mitarbeitern." | S1 §2 | user |
| F-006 | Corporations and one-person businesses are not the target group. | "Nicht Konzerne, nicht Ein-Mann-Betriebe." | S1 §2 | user |
| F-007 | Three roles: Chef (decides, wants an overview), Bauleiter (writes offers, is out on site), Büro (maintains, calls after). | "Chef (entscheidet, will Überblick), Bauleiter (schreibt Angebote, ist draußen), Büro (pflegt, telefoniert nach)" | S1 §2 | user |
| F-008 | The Bauleiter works almost exclusively on a phone, often with dirty hands. | "Bauleiter arbeitet fast nur am Handy, oft mit dreckigen Händen." | S1 §2 | constraint |
| F-009 | All open offers must be visible at a glance, sorted by the date on which follow-up is due. | "Alle offenen Angebote auf einen Blick, sortiert nach dem Datum, an dem man nachfassen sollte." | S1 §3 | requirement |
| F-010 | Each offer carries a status: sent, followed up, won, rejected, fizzled out. | "verschickt, nachgefasst, zugesagt, abgesagt, verlaufen" | S1 §3 | requirement |
| F-011 | A reminder is raised when an offer has had no answer for 7 days. | "Erinnerung, wenn ein Angebot seit 7 Tagen ohne Antwort ist." | S1 §3 | requirement |
| F-012 | A note about the customer can be kept on the offer. | "Notiz zum Kunden (\"will erst nach dem Urlaub entscheiden\")." | S1 §3 | requirement |
| F-013 | Petra wants a list to work through by phone on Monday morning. | "Petra will eine Liste zum Abtelefonieren am Montagmorgen." | S1 §3 | job |
| F-014 | Intended flow: offer is sent → appears in the list → after 7 days a reminder → Bauleiter or Büro calls → status is set → on a win it leaves the open list. | "Angebot wird verschickt → landet in der Liste → nach 7 Tagen Erinnerung → Bauleiter oder Büro ruft an → Status wird gesetzt → bei Zusage verschwindet es aus der offenen Liste." | S1 §4 | flow |
| F-015 | Version 1 contains no offer creation and no calculation; companies keep doing that in their existing program. | "Keine Angebotserstellung, keine Kalkulation." | S1 §5 | scope |
| F-016 | Version 1 has no connection to accounting or ERP. | "Keine Anbindung an Buchhaltung oder ERP." | S1 §5 | scope |
| F-017 | Version 1 has no customer management beyond what the list itself needs. | "Keine Kundenverwaltung über das hinaus, was für die Liste nötig ist." | S1 §5 | scope |
| F-018 | Open at kickoff: whether everyone has to sign in; Jonas is against it. | "Muss sich jeder anmelden? Jonas: \"Bloß kein Login-Gedöns.\"" | S1 §6 | other |
| F-019 | Open at kickoff: where the offer data comes from, since nobody wants to type it in. | "Woher kommen die Angebotsdaten rein? Abtippen will keiner." | S1 §6 | other |
| F-020 | Feature 1, priority 1: a list of all open offers sorted by follow-up date, originating from the kickoff. | "Offene Angebote Liste — Alle offenen Angebote, sortiert nach Nachfass-Datum" | S2 row 2 (sheet Features) | requirement |
| F-021 | Feature 2, priority 1: setting the status (sent / followed up / won / rejected / fizzled out) in at most 2 clicks. | "Status setzen … max. 2 Klicks" | S2 row 3 (sheet Features) | requirement |
| F-022 | Feature 3, priority 1: a follow-up reminder after 7 days without an answer; the comment asks whether the interval should be configurable. | "Nachfass-Erinnerung — Nach 7 Tagen ohne Antwort … Frist einstellbar?" | S2 row 4 (sheet Features) | requirement |
| F-023 | Feature 4, priority 2: a free-text customer note per offer. | "Kundennotiz — Freitext pro Angebot" | S2 row 5 (sheet Features) | requirement |
| F-024 | Feature 5, priority 2: a Monday call list, filterable by Bauleiter, requested by Petra. | "Montagsliste — Liste zum Abtelefonieren, filterbar nach Bauleiter" | S2 row 6 (sheet Features) | requirement |
| F-025 | Feature 6, priority 1: attach the offer as a photo or PDF instead of typing it in. | "Angebot als Foto/PDF — Datei ans Angebot hängen statt abtippen" | S2 row 7 (sheet Features) | requirement |
| F-026 | Feature 7, priority 2: a win rate — share of wins across all offers, per month, as a Chef view. | "Trefferquote — Anteil Zusagen an allen Angeboten, pro Monat … Chef-Sicht" | S2 row 8 (sheet Features) | metric |
| F-027 | Feature 8, priority 1: filter the list by status. | "Filter nach Status — Liste nach Status filtern" | S2 row 9 (sheet Features) | requirement |
| F-028 | Feature 9, priority 2: search by customer or offer number. | "Suche — Nach Kunde oder Angebotsnummer" | S2 row 10 (sheet Features) | requirement |
| F-029 | Feature 10, priority 2: multiple Bauleiter — each sees their own offers, the Chef sees all. | "Mehrere Bauleiter — Jeder sieht seine, Chef sieht alle" | S2 row 11 (sheet Features) | requirement |
| F-030 | Feature 11, priority 2: a push notification to the phone, alternatively by email. | "Push-Benachrichtigung — Erinnerung aufs Handy … oder E-Mail" | S2 row 12 (sheet Features) | requirement |
| F-031 | Feature 12, priority 3: a rejection reason — price, date, competitor or other. | "Absagegrund — Bei Absage: Preis / Termin / Wettbewerber / sonstiges" | S2 row 13 (sheet Features) | requirement |
| F-032 | Feature 13, priority 2: capture the offer amount, so the win rate can be expressed in euros. | "Angebotssumme — Betrag pro Angebot erfassen … für Trefferquote in €" | S2 row 14 (sheet Features) | requirement |
| F-033 | Feature 14, priority 3: the list is readable without a network connection; requested by Jonas. | "Offline — Liste auch ohne Netz lesbar" | S2 row 15 (sheet Features) | requirement |
| F-034 | Feature 15, priority 3: a login per user; the source is marked unknown and the comment records that Jonas is against it. | "Login — Anmeldung pro Nutzer … Jonas dagegen" | S2 row 16 (sheet Features) | requirement |
| F-035 | Feature 30, priority 2: take over the existing data from the old Excel list, once at start; the row is titled "Export nach Excel". | "Export nach Excel — Bestandsdaten aus der alten Excel-Liste übernehmen … einmalig beim Start" | S2 row 31 (sheet Features) | requirement |
| F-036 | The Chef uses phone and desktop, weekly, and his most important task is overview and win rate. | "Chef · Handy + Desktop · wöchentlich · Überblick, Trefferquote" | S2 row 2 (sheet Rollen) | user |
| F-037 | The Bauleiter uses a phone, daily, and his most important task is setting status and working through reminders. | "Bauleiter · Handy · täglich · Status setzen, Erinnerung abarbeiten" | S2 row 3 (sheet Rollen) | user |
| F-038 | The Büro uses a desktop, daily, and its most important task is the Monday list, notes and phoning after. | "Büro · Desktop · täglich · Montagsliste, Notizen, Nachtelefonieren" | S2 row 4 (sheet Rollen) | user |
| F-039 | Weber Gartenbau writes roughly 120 offers a year. | "Wir schreiben im Jahr vielleicht 120 Angebote." | S3 00:40 | metric |
| F-040 | Weber does not know how many of his offers convert and guesses about half. | "Wie viele davon durchgehen? Keine Ahnung, ehrlich. Vielleicht die Hälfte." | S3 00:40 | problem |
| F-041 | The problem is not writing the offer but staying on it; after two weeks nobody calls any more. | "Das Problem ist nicht das Schreiben, das Problem ist das Dranbleiben. Nach zwei Wochen ruft keiner mehr an." | S3 02:15 | problem |
| F-042 | Weber would get an offer into the list as a photo of the printout or by forwarding the PDF; nobody at his company types it in. | "Foto vom Ausdruck. Oder das PDF weiterleiten. Abtippen macht bei uns keiner." | S3 04:20 | requirement |
| F-043 | If nothing comes back after a week Weber wants one nudge, not three, and then wants to see whom to call. | "Wenn nach einer Woche nichts kommt, will ich einen Stups. Nicht drei. Einen." | S3 07:40 | requirement |
| F-044 | Weber already has twelve passwords and will not use the tool if he has to sign in every time. | "Ich hab schon zwölf Passwörter. Wenn ich mich jedes Mal anmelden muss, benutz ich es nicht." | S3 09:10 | constraint |
| F-045 | Weber's wife runs the office and would go through the list on Mondays. | "Meine Frau macht das Büro. Sie würde montags die Liste durchgehen." | S3 10:45 | user |
| F-046 | The people on site would at most set the status when the customer agrees on the building site. | "Die Jungs draußen setzen höchstens den Status, wenn der Kunde auf der Baustelle zusagt." | S3 10:45 | user |
| F-047 | On the building site Weber wears gloves: two taps and done, otherwise he does it in the evening and forgets it. | "Auf der Baustelle hab ich Handschuhe an. Zwei Tipper, fertig. Sonst mach ich es abends, und abends vergess ich es." | S3 12:10 | constraint |
| F-048 | The tool is worth 30 euros a month to Weber if it saves him two jobs a year. | "Wenn es mir zwei Aufträge im Jahr rettet, ist mir das 30 Euro im Monat wert." | S3 13:30 | market |
| F-049 | The market overview is dated 20.08.2026, was created by sales (Sabine) and rests on 6 conversations and 3 competitor websites. | "Stand 20.08.2026 … Grundlage: 6 Gespräche, 3 Wettbewerber-Websites" | S4 slide 1 | other |
| F-050 | HandwerkOffice is a full suite at 89 €/month that carries offer tracking as a side function. | "HandwerkOffice: Komplettpaket, 89 €/Monat, Angebotsverfolgung als Nebenfunktion" | S4 slide 2 | market |
| F-051 | Craftnote does building-site documentation and has no offer tracking. | "Craftnote: Baustellen-Doku, keine Angebotsverfolgung" | S4 slide 2 | market |
| F-052 | Excel lists are the actual competitor: free and annoying. | "Excel-Listen: der eigentliche Wettbewerber, kostenlos, nervig" | S4 slide 2 | market |
| F-053 | Companies today pay between 0 € (Excel) and 89 €/month (full suite). | "Betriebe zahlen heute 0 € (Excel) bis 89 €/Monat (Komplettpaket)" | S4 slide 3 | market |
| F-054 | The pain threshold from the conversations is 20–30 €/month for a single-purpose tool. | "Schmerzgrenze laut Gesprächen: 20–30 €/Monat für ein Einzelwerkzeug" | S4 slide 3 | market |
| F-055 | Willingness to pay rises once a lost offer becomes visible. | "Zahlungsbereitschaft steigt, wenn ein verlorenes Angebot sichtbar wird" | S4 slide 3 | market |
| F-056 | The target group is craft businesses generally: painters, roofers, landscapers, plumbing and heating. | "Handwerksbetriebe allgemein: Maler, Dachdecker, GaLaBau, SHK" | S4 slide 4 | user |
| F-057 | Company size 3 to 100 employees. | "Größe 3 bis 100 Mitarbeiter" | S4 slide 4 | user |
| F-058 | Market entry runs through GaLaBau because the contacts are there. | "Einstieg über GaLaBau, weil dort die Kontakte sind" | S4 slide 4 | market |
| F-059 | Customers demand filing the offer as a photo or PDF rather than typing it. | "Angebot als Foto oder PDF ablegen, nicht abtippen" | S4 slide 5 | requirement |
| F-060 | Customers demand a reminder by push or email. | "Erinnerung per Push oder E-Mail" | S4 slide 5 | requirement |
| F-061 | Customers demand two clicks to the status. | "Zwei Klicks bis zum Status" | S4 slide 5 | requirement |
| F-062 | The Chef wants to see the win rate: how many offers become jobs. | "Chef will Trefferquote sehen: wie viele Angebote werden Aufträge" | S4 slide 5 | metric |
| F-063 | A prototype is planned by October. | "Prototyp bis Oktober" | S4 slide 6 | other |
| F-064 | Two pilot companies are planned: Grünwerk GmbH and Weber Gartenbau. | "Zwei Pilotbetriebe: Grünwerk GmbH, Weber Gartenbau" | S4 slide 6 | other |
| F-065 | The price is to be fixed only after the pilot. | "Preis erst nach Pilot festlegen" | S4 slide 6 | other |

## Superseded by decisions

Claims that a decision record excludes. Listed so they are not rebuilt into the spec.

| Fact | Decision | Note |
|------|----------|------|
| — | — | — |

No decision records exist for this feature yet.
