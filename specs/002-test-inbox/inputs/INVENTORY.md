# Source Inventory

Feature: `specs/002-test-inbox` · Last intake: 2026-09-05

IDs are stable. A source keeps its ID forever, even if it is later judged irrelevant.
Weight is set by the human and decides which source wins when two conflict: `high | medium | low`. Rows marked `(proposed)` are the AI's suggestion and still need confirmation.

Citation formats: `S2 slide 7` · `S3 row 12` (sheet name in the extracted file) · `S1 §3` · `S4 07:40` · `S5 p.3`

| ID | File | Kind | Date | From | Content in one sentence | Weight |
|----|------|------|------|------|-------------------------|--------|
| S1 | 2026-08-12_Kickoff_Notizen.md | notes | 2026-08-12 | Max, Jonas (Grünwerk GmbH), Petra (Grünwerk) | Kickoff notes recording the problem, target group, roles, intended flow and the explicit non-goals of the offer-tracking idea. | high |
| S2 | Feature_Liste.xlsx | spreadsheet | 2026-09-05 | — | Working feature backlog with priorities, originating source and comments per feature, plus a sheet describing the three user roles. | high |
| S3 | Kundengespraech_Weber_Transkript.txt | transcript | 2026-09-02 | Herr Weber (Weber Gartenbau), recorded by Max | Transcript of a customer interview about how offers are followed up today, device and login constraints, and willingness to pay. | high |
| S4 | Marktueberblick_v3.pptx | slides | 2026-08-20 | Vertrieb (Sabine) | Market overview deck covering competitors, price ranges, target segment, customer demands and next steps, based on six interviews and three competitor websites. | medium |

## Needs attention

- S2: the file states no date and no author; the date above is the file's modification time. Correct it if you know the real one.
