# Source Inventory

Feature: `specs/001-quote-tracker` · Last intake: 2026-09-05

IDs are stable. A source keeps its ID forever, even if it is later judged irrelevant.
Weight is set by the human and decides which source wins when two conflict: `high | medium | low`. Rows marked `(proposed)` are the AI's suggestion and still need confirmation.

Citation formats: `S2 slide 7` · `S3 row 12` (sheet name in the extracted file) · `S1 §3` · `S4 07:40` · `S5 p.3`

| ID | File | Kind | Date | From | Content in one sentence | Weight |
|----|------|------|------|------|-------------------------|--------|
| S1 | 2026-08-12_Kickoff_Notizen.md | notes | 2026-08-12 | — | Kickoff meeting notes with Grünwerk GmbH covering the problem, target group, must-haves, intended flow, exclusions for version 1 and open questions. | high (proposed) |
| S2 | Feature_Liste.xlsx | spreadsheet | 2026-09-05 | — | Numbered feature list with priority, origin and comments (sheet Features) plus a sheet of the three roles with device and frequency (sheet Rollen). | medium (proposed) |
| S3 | Kundengespraech_Weber_Transkript.txt | transcript | 2026-09-02 | Max (recorded) | Timestamped transcript of a customer interview with Herr Weber of Weber Gartenbau about quote follow-up, data entry, reminders, login and price. | high (proposed) |
| S4 | Marktueberblick_v3.pptx | slides | 2026-08-20 | Sabine (Vertrieb) | Six-slide sales market overview on competitors, price ranges, target group, customer demands and next steps. | medium (proposed) |

Citation formats for this feature: `S1 §3` (heading number) · `S2 row 7 (sheet Features)` · `S3 07:40` (timestamp) · `S4 slide 5`

## Needs attention

- Weights are proposals; confirm or correct them (`ok`, or e.g. `S4 low`).
- S2: the Features sheet jumps from row 16 (Nr 15) to row 31 (Nr 30); rows 17–30 are empty in the workbook, so features 16–29 are either not yet written or were deleted. Confirm nothing is missing.
- S2 date is the file modification time; the workbook states no date.
