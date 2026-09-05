# Conflicts

Feature: `specs/001-quote-tracker` · 2026-09-05

Real contradictions between sources. The AI does not decide them. Unresolved conflicts become tagged assumptions in the spec (higher-weight source wins) and appear under Open Questions.

Weights are the proposed values from `inputs/INVENTORY.md`; they have not been confirmed yet.

| ID | Claim A | Claim B | What differs | Source weights | Question to the human | Resolution |
|----|---------|---------|--------------|----------------|-----------------------|------------|
| C-01 | F-006 (S1 §2): target group is garden and landscaping businesses (GaLaBau). | F-067, F-069 (S4 slide 4): trades in general (painters, roofers, GaLaBau, SHK), with GaLaBau only as the entry market. | Whether the spec is written for GaLaBau alone or for all trades with GaLaBau first. Affects role names, wording and examples throughout. | S1 high (proposed) · S4 medium (proposed) | Is this spec for GaLaBau only, or for all trades with GaLaBau as the first market? | Resolved: GaLaBau only (R1-01, confirmed via workflow gate dry-run-simulated-gate, 2026-09-05; no human decision) |
| C-02 | F-006 (S1 §2): 5 to 50 employees; F-007 excludes one-person businesses and corporations. | F-068 (S4 slide 4): 3 to 100 employees. | The size band of the target business. Affects how many site managers the list must handle and whether the multi-user feature (F-036) is core. | S1 high (proposed) · S4 medium (proposed) | Which size band applies: 5–50 employees (S1) or 3–100 (S4)? | Resolved: 5–50 employees; S4 slide 4 set aside as a requirement source for version 1 (R1-02, confirmed via workflow gate dry-run-simulated-gate, 2026-09-05; no human decision) |

Resolution values: `open` · `Resolved: <answer> (human, YYYY-MM-DD)` · `Deferred: <reason>`

## Checked and not a conflict

Pairs that look contradictory but can both be true. Listed so they are not re-raised; where a decision is still needed it is an open question.

- **Login** — F-023 (S1 §6) and F-054 (S3 09:10) reject a login "every time"; F-041 (S2 row 16) lists login at priority 3 with "Jonas against"; F-036 (S2 row 11) needs per-user views. A one-time setup with no repeated sign-in satisfies all four. Carried as Q-02.
- **Reminder count** — F-015 (S1 §3) "reminder after 7 days" and F-052 (S3 07:40) "one nudge, not three" agree; how the timer behaves after a follow-up is unstated. Carried as Q-06.
- **Note on the customer vs. per quote** — F-016 (S1 §3) "Notiz zum Kunden" and F-030 (S2 row 5) "Freitext pro Angebot" differ in detail, not in substance; a note about the customer stored on the quote satisfies both and respects F-022 (no customer management).
- **Who writes and who follows up** — at Grünwerk the site manager writes quotes (F-010) and site manager or office calls (F-018); at Weber the owner writes and wants the nudge (F-052) while the crew only sets status (F-056). Different businesses, not contradicting claims about the product. Carried as Q-04.
