# Conflicts

Feature: `specs/002-test-inbox` · 2026-09-05

Real contradictions between sources. The AI does not decide them. Unresolved conflicts become tagged assumptions in the spec (higher-weight source wins) and appear under Open Questions.

| ID | Claim A | Claim B | What differs | Source weights | Question to the human | Resolution |
|----|---------|---------|--------------|----------------|-----------------------|------------|
| C-01 | F-005, F-006 (S1 §2) | F-056, F-057 (S4 slide 4) | Who the product is for. S1 names garden and landscaping companies with 5–50 employees and rules out one-person businesses; S4 names craft businesses in general (painters, roofers, GaLaBau, SHK) with 3–100 employees. | S1 high · S4 medium | Is version 1 for GaLaBau companies with 5–50 employees, or for craft businesses generally with 3–100 employees? | Resolved: Garden and landscaping companies with 5–50 employees (S1); the wider craft segment of S4 slide 4 stays market context, not the v1 target group (human, 2026-09-05) |
| C-02 | F-034 (S2 row 16, sheet Features) | F-044 (S3 09:10) | Whether the product has a login at all. S2 carries "Anmeldung pro Nutzer" as a feature (priority 3); Weber says he will not use the tool if he has to sign in every time. F-018 (S1 §6) records the same point as still open. | S2 high · S3 high | Does version 1 have a per-user login, or access without a repeated sign-in? | Resolved: Version 1 has a per-user login (S2 row 16) (human, 2026-09-05) |
| C-03 | F-029 (S2 row 11, sheet Features) | F-044 (S3 09:10) | Whether users are told apart. S2 requires each Bauleiter to see only their own offers and the Chef to see all, which needs an identified user; Weber rejects signing in each time. | S2 high · S3 high | If there is no sign-in, may everyone in a company see all offers, or must the per-Bauleiter view be kept by some other means? | Resolved: Everyone in a company sees all offers of that company; the per-Bauleiter restriction of F-029 does not apply in v1 (human, 2026-09-05) |

Resolution values: `open` · `Resolved: <answer> (human, YYYY-MM-DD)` · `Deferred: <reason>`
