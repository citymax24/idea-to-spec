---
name: speckit-idea-standards
description: Bind an idea to the project's standards (accessibility, corporate design, and whatever comes later), check it against them rule by rule, record exemptions a human signs, and report when a standard has moved since the idea was bound.
compatibility: Requires spec-kit project structure with .specify/ directory
metadata:
  author: github-spec-kit
  source: idea:commands/speckit.idea.standards.md
---

## User Input

```text
$ARGUMENTS
```

Arguments: `[--bind] [--check] [--exempt <RULE-ID> --reason "<text>"] [--approved-by <name>] [--registry <dir>] [--feature <specs/NNN-dir>] [--headless]`. With no mode flag the command reports status and changes nothing.

## Interactive or headless

Headless means: `--headless` is among the arguments, or you cannot wait for a reply (a `claude -p` run, a workflow step). Interactive means you can ask and wait. Every "ask the human" step below applies only when interactive; headless runs leave the marker or status in the file and stop.

## Goal

Standards are the third source of truth in this loop, next to the input sources (`S#`) and the reviewer's feedback (`R#-##`). They are decided once for the whole project, in `standards/`, and then carried into every idea. Nobody proposes them in a review round and no reviewer can talk them away; a rule that cannot apply to an idea needs a signed exemption, not a quiet omission.

An idea is *bound* to a module at a *version*. That is what makes a later change to the module visible as drift instead of silently assumed away.

## Reading the registry

The registry is `standards/` at the repository root unless `--registry` says otherwise. Each subdirectory with a `standard.yml` is a module: `prefix`, `version`, `status`, `authority` (`law` > `contract` > `internal`), `precedence` (tiebreaker inside a band, lower wins), `applies_to`, and `assets`. `rules.md` holds the rules, one block per rule, each with **Severity** (`required` | `recommended`), **Bites** (`spec` | `prototype` | `build`) and **Shapes the spec** (yes | no).

If there is no registry, say so in one line and stop successfully. Standards are optional; a clone without them runs the whole loop unchanged.

Run this for the version arithmetic instead of comparing versions yourself:

```bash
python3 .specify/extensions/idea/scripts/python/standards_status.py --json
```

Pass `--registry <dir>` and `--feature <dir>` through to it whenever they were given to this command.

## Status (no mode flag)

1. **Resolve `FEATURE_DIR`** and the registry. Run the status script.
2. **Report**, in this order: which modules apply and at which version this idea is bound; drift, naming which module moved from which version to which; open exemptions with their record IDs; conflicts already resolved; anything `not verifiable` because a module is a draft. End with the one command that would fix the most: `--bind` for drift, `--check` for an unevaluated spec, `--exempt` for a rule that cannot apply.

## `--bind`

1. **Resolve `FEATURE_DIR`.** Require `spec.md`.

2. **Select the modules.** Every module whose `status` is `active` or `draft` and whose `applies_to` covers this idea. A module in status `retired` does not bind. A module in status `draft` binds, but every one of its rules is later reported `not verifiable` — never `pass`.

3. **Resolve conflicts between modules before touching the spec.** Two rules conflict when satisfying one breaks the other (the classic: a corporate-design colour pairing that measures below the contrast rule). Decide by `authority` first, then by `precedence`; the losing rule is not deleted, it is constrained. Write each conflict into `standards/BOUND.md` under "Conflicts between standards" with what concretely may no longer be used. Never re-argue a conflict already recorded there.

4. **Materialise the rules whose "Shapes the spec" is yes**, and only where they have something to attach to:
   - a rule about form labels attaches to the `Content` of screens that take input, not to every screen;
   - a rule about error text attaches to those screens' `States`;
   - a rule that constrains behaviour across the product becomes a functional requirement in §7;
   - a rule about language or tone attaches to §8.
   Each materialised line ends with the tag `[STD-<PREFIX>-<nnn> · v<module version>]`, which is a provenance tag like any other. Never invent a screen or a field to give a rule a home: if a rule has nothing to attach to, it goes into "Carried as a check only".

5. **Write the §8 binding line**, replacing any earlier one:
   `- **Standards bound**: STD-A11Y v1.0 · STD-CD v0.1 (draft) — [STD-BINDING]`

6. **Write `standards/BOUND.md`** from `.specify/extensions/idea/templates/standards-bound-template.md`: bound modules with their versions, which rules were materialised and where, which are carried as a check only, the resolved conflicts, existing exemptions, and everything `not verifiable`. This file is authoritative; the §8 line is the reader's copy of it.

7. **Version the change, but only if `spec.md` actually changed.**
   - Called from `/speckit-idea-draft` as part of the first draft: no bump, it is part of v0.1.
   - A later bind that changes `spec.md`: one new version exactly like a feedback round — `0.x` → `0.x+1`, or on an accepted spec `1.y` → `1.y+1` with status back to `in-review`. Changelog block `## v<new> · <date> · standards rebound` with a row per changed line whose Trigger is the rule ID. Commit `spec(<slug>): v<new> standards rebound`, tag `spec-<slug>-v<new>`.
   - A bind that only refreshes `BOUND.md`: no version, no tag. Say so.

8. **Report.** Modules bound with versions, rules materialised and where, conflicts resolved, whether the spec version moved, and that a rebind on an accepted spec needs `/speckit-idea-accept` again.

## `--check`

1. **Resolve `FEATURE_DIR`** and read `standards/BOUND.md`. If there is no binding, say `Not bound yet. Run /speckit-idea-standards --bind.` and stop.

2. **Evaluate every bound rule** against `spec.md` and, when it exists, `prototype/prototype.html`. One verdict per rule:
   - `pass` — name the evidence: the SCR, the FR, the element in the prototype. A verdict without evidence is not a verdict.
   - `fail` — name what is missing and what would fix it.
   - `not verifiable` — the module is a draft, or the rule's `Bites` is `build`. Never dress this up as a pass.
   - `exempted (EXM-nnn)` — a signed record exists for this rule at this module version.
   - `n/a` — the rule has nothing to bite on here (no forms in the whole product, say). Justify it in the evidence column; "n/a" without a reason is a `fail`.
   For measurable rules, measure. A contrast rule is checked by computing the ratio of the two colours the prototype actually uses and writing the number down, not by looking at them.

3. **Write `checklists/standards.md`** from `.specify/extensions/idea/templates/standards-checklist-template.md`, one table per module, then the summary counts.

4. **Report** the summary first: blocking failures, warnings, not verifiable, exempted. Then the blocking failures in full, since those are what stop acceptance.

## `--exempt <RULE-ID> --reason "<text>"`

1. **Resolve the rule** in the registry. If the ID does not exist, stop and say so; do not guess a neighbour.

2. **Refuse the easy ones.** An exemption is for a rule that genuinely does not apply to this idea, or that is met by other means. "Inconvenient", "later", "the reviewer prefers it" are not reasons. For a module whose authority is `law`, "we decided not to" is not a reason either: either the idea is outside the standard's scope, or the requirement is met another way and that way is named. If the reason does not clear this bar, say what is missing and stop.

3. **Get a human.** Interactive: show the rule, the reason and what a user loses, then ask "Grant this exemption? Reply with your name to approve, or `no`." Wait. Headless: `--approved-by <name>` counts as approval after a gate; without it, write nothing and stop with "Exemption needs a human."

4. **Write `decisions/EXM-<nnn>.md`** from `.specify/extensions/idea/templates/exemption-template.md` — `nnn` is the highest existing EXM number plus one, starting at 001, counted independently of `DEC-` records. Record the module version it was granted against.

5. **Add the row** to the "Exemptions" table in `standards/BOUND.md`, and re-run the check so `checklists/standards.md` reflects it.

6. **Report** the record path, and that the exemption stops the rule from blocking without making it pass — and that it lapses when the module is bumped.

## Rules

- Never grant an exemption on your own, for any module, in any mode.
- Never edit anything under `standards/` from a feature. A rule that is wrong is fixed in its module by whoever owns it, with a version bump and a changelog block — never per idea.
- Never report a rule of a `draft` module as `pass`.
- Never drop or weaken a materialised standard line in `spec.md` because a reviewer asked. That path is an exemption, and `/speckit-idea-apply` refuses it.
- A rule whose `Bites` is `build` is never passed by a prototype. Say `not verifiable` and mean it.
- Assets are embedded, never linked: the prototype is one self-contained file and its page blocks external fonts, images and stylesheets. An asset without a cleared licence row is not embedded; the substitution is reported.