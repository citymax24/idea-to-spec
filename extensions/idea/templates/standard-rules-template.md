# Rules: STD-[SHORT] · [Standard name]

Module version [0.1] · [written against <source version> | self-versioned] · see `standard.yml` for scope and legal review.

Each rule carries four fields:

- **Severity** — `required` (inside the bound level; a breach blocks acceptance when the module's authority is `law`) or `recommended` (never a blocker).
- **Bites** — `spec` (decidable while writing the spec), `prototype` (checkable in the built prototype), `build` (only checkable in real software; recorded so nobody claims the prototype proved it).
- **Shapes the spec** — whether `--bind` materialises the rule as a tagged line in the spec (a state, a content element, an FR) or leaves it in the registry as a check only.
- **Source** — the clause, criterion or manual section it comes from.

---

### STD-[SHORT]-001 · [The rule as one plain sentence a reviewer can judge]

[Two or three sentences: what it demands and what it forbids. No motivation, no history.]

- **Severity**: required
- **Bites**: spec · prototype
- **Shapes the spec**: yes — [what it writes into the spec, and where]
- **Check**: [what someone looks at to decide pass or fail, in the terms of this repository: an SCR, a FLOW, an element in the prototype]
- **Source**: [clause or section]

### STD-[SHORT]-002 · [...]

- **Severity**: required
- **Bites**: prototype
- **Shapes the spec**: no
- **Check**: [...]
- **Source**: [...]

---

## Above the bound level

[Rules that are good practice or that a newer version of the source is expected to require. Number them from 101 so they never collide with the required set. Never blockers.]

### STD-[SHORT]-101 · [...]

- **Severity**: recommended
- **Bites**: [...]
- **Shapes the spec**: no
- **Source**: [...] — outside the level bound in `standard.yml`
