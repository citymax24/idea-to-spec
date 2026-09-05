# Facts

Feature: `specs/001-quote-tracker` · Extracted: 2026-09-05 · Sources: S1–S4

Every row is one atomic claim with one location. Claims are written in English; the quote keeps the source language. IDs are stable; new extractions append.

Categories: problem · user · job · scope · flow · screen · requirement · constraint · metric · market · other

Source weights at extraction (all still proposed, see `inputs/INVENTORY.md`): S1 high · S2 medium · S3 high · S4 medium.

| ID | Claim | Quote (verbatim, short) | Location | Category |
|----|-------|-------------------------|----------|----------|
| F-001 | Kickoff participants were Max (idea), Jonas (site manager at Grünwerk GmbH) and Petra (office at Grünwerk). | "Max (Idee), Jonas (Bauleiter bei Grünwerk GmbH), Petra (Büro Grünwerk)" | S1 para 1 | other |
| F-002 | Quotes get lost in day-to-day business. | "Angebote gehen im Alltag unter." | S1 §1 | problem |
| F-003 | The site manager writes quotes in the evening at the kitchen table, emails them and forgets to follow up. | "schreibt Angebote abends am Küchentisch, schickt sie per Mail und vergisst nachzufassen" | S1 §1 | problem |
| F-004 | The office does not know which quotes are open unless someone asks. | "Petra weiß nicht, welche Angebote offen sind, solange niemand fragt." | S1 §1 | problem |
| F-005 | In spring an estimated 8 of 30 quotes at Grünwerk lapsed with neither a rejection nor a follow-up. | "geschätzt 8 von 30 Angeboten einfach verlaufen, ohne Absage und ohne Nachfrage" | S1 §1 | metric |
| F-006 | Target group: garden and landscaping businesses (GaLaBau) with 5 to 50 employees. | "Garten- und Landschaftsbaubetriebe mit 5 bis 50 Mitarbeitern" | S1 §2 | user |
| F-007 | Corporations and one-person businesses are not in the target group. | "Nicht Konzerne, nicht Ein-Mann-Betriebe." | S1 §2 | scope |
| F-008 | There are three roles: boss, site manager, office. | "Drei Rollen: Chef …, Bauleiter …, Büro …" | S1 §2 | user |
| F-009 | The boss decides and wants an overview. | "Chef (entscheidet, will Überblick)" | S1 §2 | user |
| F-010 | The site manager writes the quotes and is out in the field. | "Bauleiter (schreibt Angebote, ist draußen)" | S1 §2 | user |
| F-011 | The office maintains the data and phones customers. | "Büro (pflegt, telefoniert nach)" | S1 §2 | user |
| F-012 | The site manager works almost only on the phone, often with dirty hands. | "arbeitet fast nur am Handy, oft mit dreckigen Händen" | S1 §2 | constraint |
| F-013 | All open quotes at a glance, sorted by the date on which follow-up is due. | "Alle offenen Angebote auf einen Blick, sortiert nach dem Datum, an dem man nachfassen sollte." | S1 §3 | requirement |
| F-014 | Each quote has a status: sent, followed up, accepted, declined, lapsed. | "verschickt, nachgefasst, zugesagt, abgesagt, verlaufen" | S1 §3 | requirement |
| F-015 | A reminder when a quote has had no answer for 7 days. | "Erinnerung, wenn ein Angebot seit 7 Tagen ohne Antwort ist." | S1 §3 | requirement |
| F-016 | A note about the customer, for example that they will decide only after their holiday. | "Notiz zum Kunden (\"will erst nach dem Urlaub entscheiden\")" | S1 §3 | requirement |
| F-017 | The office wants a list to phone through on Monday morning. | "Petra will eine Liste zum Abtelefonieren am Montagmorgen." | S1 §3 | job |
| F-018 | Intended flow: quote is sent, lands in the list, reminder after 7 days, site manager or office calls, status is set. | "Angebot wird verschickt → landet in der Liste → nach 7 Tagen Erinnerung → Bauleiter oder Büro ruft an → Status wird gesetzt" | S1 §4 | flow |
| F-019 | On acceptance the quote disappears from the open list. | "bei Zusage verschwindet es aus der offenen Liste" | S1 §4 | flow |
| F-020 | Version 1 has no quote creation and no calculation; businesses keep doing that in their existing program. | "Keine Angebotserstellung, keine Kalkulation. Das machen die Betriebe weiter in ihrem Programm." | S1 §5 | scope |
| F-021 | Version 1 has no connection to accounting or ERP. | "Keine Anbindung an Buchhaltung oder ERP." | S1 §5 | scope |
| F-022 | Version 1 has no customer management beyond what the list needs. | "Keine Kundenverwaltung über das hinaus, was für die Liste nötig ist." | S1 §5 | scope |
| F-023 | Whether every user must sign in is open; Jonas rejects any login fuss. | "Muss sich jeder anmelden? Jonas: \"Bloß kein Login-Gedöns.\"" | S1 §6 | constraint |
| F-024 | Where the quote data comes from is open; nobody wants to type it in. | "Woher kommen die Angebotsdaten rein? Abtippen will keiner." | S1 §6 | constraint |
| F-025 | Feature 1 "open quotes list": all open quotes sorted by follow-up date; priority 1; origin kickoff. | "Alle offenen Angebote, sortiert nach Nachfass-Datum" | S2 row 2 (sheet Features) | requirement |
| F-026 | Feature 2 "set status" with the values sent, followed up, accepted, declined, lapsed; priority 1; origin kickoff. | "verschickt / nachgefasst / zugesagt / abgesagt / verlaufen" | S2 row 3 (sheet Features) | requirement |
| F-027 | Setting a status takes at most 2 clicks. | "max. 2 Klicks" | S2 row 3 (sheet Features) | requirement |
| F-028 | Feature 3 "follow-up reminder" after 7 days without answer; priority 1; origin kickoff and Weber. | "Nach 7 Tagen ohne Antwort" | S2 row 4 (sheet Features) | requirement |
| F-029 | The feature list asks whether the reminder period should be configurable. | "Frist einstellbar?" | S2 row 4 (sheet Features) | other |
| F-030 | Feature 4 "customer note": free text per quote; priority 2; origin kickoff. | "Freitext pro Angebot" | S2 row 5 (sheet Features) | requirement |
| F-031 | Feature 5 "Monday list": list for phoning through, filterable by site manager; priority 2; origin Petra. | "Liste zum Abtelefonieren, filterbar nach Bauleiter" | S2 row 6 (sheet Features) | requirement |
| F-032 | Feature 6 "quote as photo/PDF": attach a file to the quote instead of typing it in; priority 1; origin Weber and sales. | "Datei ans Angebot hängen statt abtippen" | S2 row 7 (sheet Features) | requirement |
| F-033 | Feature 7 "hit rate": share of accepted quotes among all quotes, per month; priority 2; origin sales; boss's view. | "Anteil Zusagen an allen Angeboten, pro Monat" · "Chef-Sicht" | S2 row 8 (sheet Features) | metric |
| F-034 | Feature 8 "filter by status": filter the list by status; priority 1; origin kickoff. | "Liste nach Status filtern" | S2 row 9 (sheet Features) | requirement |
| F-035 | Feature 9 "search" by customer or quote number; priority 2; origin Petra. | "Nach Kunde oder Angebotsnummer" | S2 row 10 (sheet Features) | requirement |
| F-036 | Feature 10 "multiple site managers": each sees their own quotes, the boss sees all; priority 2; origin kickoff. | "Jeder sieht seine, Chef sieht alle" | S2 row 11 (sheet Features) | requirement |
| F-037 | Feature 11 "push notification": reminder to the phone, or by email; priority 2; origin sales. | "Erinnerung aufs Handy" · "oder E-Mail" | S2 row 12 (sheet Features) | requirement |
| F-038 | Feature 12 "rejection reason": on decline record price, date, competitor or other; priority 3; origin sales. | "Bei Absage: Preis / Termin / Wettbewerber / sonstiges" | S2 row 13 (sheet Features) | requirement |
| F-039 | Feature 13 "quote amount": capture the amount per quote, for the hit rate in euros; priority 2; origin sales. | "Betrag pro Angebot erfassen" · "für Trefferquote in €" | S2 row 14 (sheet Features) | requirement |
| F-040 | Feature 14 "offline": list readable without network; priority 3; origin Jonas. | "Liste auch ohne Netz lesbar" | S2 row 15 (sheet Features) | requirement |
| F-041 | Feature 15 "login": sign-in per user; priority 3; origin unknown; Jonas is against it. | "Anmeldung pro Nutzer" · "?" · "Jonas dagegen" | S2 row 16 (sheet Features) | requirement |
| F-042 | Feature 30 is titled "Export nach Excel" but describes taking over existing data from the old Excel list, once at the start; priority 2; origin Petra. | "Export nach Excel" · "Bestandsdaten aus der alten Excel-Liste übernehmen" · "einmalig beim Start" | S2 row 31 (sheet Features) | requirement |
| F-043 | Boss: phone and desktop, weekly use, main task overview and hit rate. | "Handy + Desktop" · "wöchentlich" · "Überblick, Trefferquote" | S2 row 2 (sheet Rollen) | user |
| F-044 | Site manager: phone, daily use, main task set status and work through reminders. | "Handy" · "täglich" · "Status setzen, Erinnerung abarbeiten" | S2 row 3 (sheet Rollen) | user |
| F-045 | Office: desktop, daily use, main tasks Monday list, notes, phoning back. | "Desktop" · "täglich" · "Montagsliste, Notizen, Nachtelefonieren" | S2 row 4 (sheet Rollen) | user |
| F-046 | Interviewee: Herr Weber of Weber Gartenbau, a business with 12 employees; recorded by Max on 2026-09-02. | "Weber Gartenbau, 12 Mitarbeiter" | S3 para 1 | user |
| F-047 | Weber writes about 120 quotes per year. | "Wir schreiben im Jahr vielleicht 120 Angebote." | S3 00:40 | metric |
| F-048 | Weber does not know how many quotes are won; he guesses about half. | "Wie viele davon durchgehen? Keine Ahnung, ehrlich. Vielleicht die Hälfte." | S3 00:40 | problem |
| F-049 | The problem is not writing quotes but staying on them; after two weeks nobody calls any more. | "Das Problem ist nicht das Schreiben, das Problem ist das Dranbleiben. Nach zwei Wochen ruft keiner mehr an." | S3 02:15 | problem |
| F-050 | A quote gets into the list as a photo of the printout or by forwarding the PDF. | "Foto vom Ausdruck. Oder das PDF weiterleiten." | S3 04:20 | requirement |
| F-051 | Nobody at Weber types quotes in; a product that requires it can be dropped. | "Abtippen macht bei uns keiner, da können Sie das gleich lassen." | S3 04:20 | constraint |
| F-052 | After one week without response Weber wants exactly one nudge, not three. | "Wenn nach einer Woche nichts kommt, will ich einen Stups. Nicht drei. Einen." | S3 07:40 | requirement |
| F-053 | After the nudge he wants to see whom to call. | "Und dann sehe ich, wen ich anrufe." | S3 07:40 | requirement |
| F-054 | Weber already has twelve passwords; if he has to log in every time he will not use the product. | "Ich hab schon zwölf Passwörter. Wenn ich mich jedes Mal anmelden muss, benutz ich es nicht." | S3 09:10 | constraint |
| F-055 | Weber's wife runs the office and would go through the list on Mondays. | "Meine Frau macht das Büro. Sie würde montags die Liste durchgehen." | S3 10:45 | user |
| F-056 | The field crew would at most set the status, when a customer accepts on site. | "Die Jungs draußen setzen höchstens den Status, wenn der Kunde auf der Baustelle zusagt." | S3 10:45 | user |
| F-057 | On site he wears gloves; two taps and done. | "Auf der Baustelle hab ich Handschuhe an. Zwei Tipper, fertig." | S3 12:10 | constraint |
| F-058 | If he cannot do it on site he does it in the evening and then forgets. | "Sonst mach ich es abends, und abends vergess ich es." | S3 12:10 | problem |
| F-059 | If the product saves him two orders a year, it is worth 30 euros per month to him. | "Wenn es mir zwei Aufträge im Jahr rettet, ist mir das 30 Euro im Monat wert." | S3 13:30 | market |
| F-060 | The market overview is dated 2026-08-20, was made by sales (Sabine) and rests on 6 conversations and 3 competitor websites. | "Grundlage: 6 Gespräche, 3 Wettbewerber-Websites" | S4 slide 1 | other |
| F-061 | Competitor HandwerkOffice: complete package at 89 €/month with quote tracking as a side function. | "Komplettpaket, 89 €/Monat, Angebotsverfolgung als Nebenfunktion" | S4 slide 2 | market |
| F-062 | Competitor Craftnote: site documentation, no quote tracking. | "Baustellen-Doku, keine Angebotsverfolgung" | S4 slide 2 | market |
| F-063 | Excel lists are the real competitor: free and annoying. | "der eigentliche Wettbewerber, kostenlos, nervig" | S4 slide 2 | market |
| F-064 | Businesses pay today between 0 € (Excel) and 89 €/month (complete package). | "0 € (Excel) bis 89 €/Monat (Komplettpaket)" | S4 slide 3 | market |
| F-065 | Pain threshold according to the conversations: 20–30 €/month for a single-purpose tool. | "Schmerzgrenze laut Gesprächen: 20–30 €/Monat für ein Einzelwerkzeug" | S4 slide 3 | market |
| F-066 | Willingness to pay rises when a lost quote becomes visible. | "Zahlungsbereitschaft steigt, wenn ein verlorenes Angebot sichtbar wird" | S4 slide 3 | market |
| F-067 | Target group: trades in general, namely painters, roofers, GaLaBau and plumbing/heating (SHK). | "Handwerksbetriebe allgemein: Maler, Dachdecker, GaLaBau, SHK" | S4 slide 4 | user |
| F-068 | Business size 3 to 100 employees. | "Größe 3 bis 100 Mitarbeiter" | S4 slide 4 | user |
| F-069 | Market entry via GaLaBau because the contacts are there. | "Einstieg über GaLaBau, weil dort die Kontakte sind" | S4 slide 4 | market |
| F-070 | Customers demand storing the quote as photo or PDF, not typing it in. | "Angebot als Foto oder PDF ablegen, nicht abtippen" | S4 slide 5 | requirement |
| F-071 | Customers demand a reminder by push or email. | "Erinnerung per Push oder E-Mail" | S4 slide 5 | requirement |
| F-072 | Customers demand two clicks to the status. | "Zwei Klicks bis zum Status" | S4 slide 5 | requirement |
| F-073 | The boss wants to see the hit rate: how many quotes become orders. | "Chef will Trefferquote sehen: wie viele Angebote werden Aufträge" | S4 slide 5 | metric |
| F-074 | Prototype by October. | "Prototyp bis Oktober" | S4 slide 6 | constraint |
| F-075 | Two pilot businesses: Grünwerk GmbH and Weber Gartenbau. | "Zwei Pilotbetriebe: Grünwerk GmbH, Weber Gartenbau" | S4 slide 6 | other |
| F-076 | The price is set only after the pilot. | "Preis erst nach Pilot festlegen" | S4 slide 6 | constraint |

## Set aside by feedback

Claims a confirmed feedback item excludes as a requirement source. The facts stay for the record; do not rebuild them into the spec without a new source or feedback item.

| Facts | Feedback item | Note |
|-------|---------------|------|
| F-067, F-068, F-069 | R1-02 (spec v0.2, 2026-09-05) | S4 slide 4 is not a requirement source for version 1. C-01 resolved as "GaLaBau only" (R1-01) and C-02 as "5–50 employees" (R1-02) in favour of S1 §2. Slides 2, 3, 5 and 6 of S4 remain cited. |

## Superseded by decisions

Claims that a decision record excludes. Listed so they are not rebuilt into the spec.

| Fact | Decision | Note |
|------|----------|------|
| — | — | No decision records exist yet (`decisions/` is empty). |
