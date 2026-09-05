# Running the loop

Two ways to run it: command by command inside Claude Code (interactive, recommended for the first ideas), or as a Spec Kit workflow with gates (for repeatable runs).

## Interactive, inside Claude Code

Open Claude Code in the repository root. The skills `speckit-idea-*` are available.

### 1 Collect

```
/speckit-idea-intake <folder with your files> --name <2-4-word-slug>
```

Drop everything into the folder first: spreadsheets, slides, notes, transcripts, screenshots. Do not tidy. The command copies the files into `specs/<NNN>-<slug>/inputs/raw/`, converts them, assigns `S1…Sn` and asks you to confirm the weights (`high | medium | low`). The weight decides which source wins a conflict.

Audio needs a transcript: drop a `.txt` with the same base name next to the audio file, or install a local transcriber (`whisper` or `mlx_whisper`).

### 2 Understand

```
/speckit-idea-facts
```

Produces `analysis/facts.md` (one cited claim per row), `analysis/conflicts.md` and `analysis/open-questions.md`. The command shows you conflicts and questions. Answer the ones you can in one line each, or say `draft with assumptions`.

### 3 Draft

```
/speckit-idea-draft
```

Writes `spec.md` v0.1 with a provenance tag on every line, `CHANGELOG.md`, the readiness checklist and the git tag `spec-<slug>-v0.1`.

If the repository has a `standards/` registry, the draft is bound to it in the same step: §8 gets a `Standards bound` line, the rules that shape content land in the sections they belong to tagged `[STD-A11Y-007 · v1.0]`, and `standards/BOUND.md` records which modules at which versions. Nothing to do; it happens. Without a registry the step is skipped silently.

### 4 Review rounds

```
/speckit-idea-publish
```

Renders the spec to `feedback/spec-review.html` and, in a session with artifact publishing, publishes it as a private page. The URL stays the same across versions. Read it, comment on the page (naming the ID helps), or collect your feedback any way you like: a voice memo transcript, a few sentences in chat, an email.

```
/speckit-idea-feedback --from-comments
/speckit-idea-feedback --file notes/round1.txt
/speckit-idea-feedback "Target group is wrong, those are the small firms. Onboarding is missing. Drop the Excel export."
```

The command writes `feedback/R<n>.md`: one row per item, your words verbatim, the AI's reading next to it, a type (ADD, CHANGE, REMOVE, MISREAD, QUESTION, OK, and VISUAL once a prototype exists) and a target. It then asks: "Did I understand each item correctly?" Reply `confirm`, correct by ID (`R1-02: also the detail screen`), or `drop R1-05`. Nothing in the spec has changed yet.

```
/speckit-idea-apply
```

Applies the confirmed round as one new version: edits with `⟲ v0.2 · R1-01` markers, tombstones plus `decisions/DEC-*.md` for removals, a changelog block naming the trigger of every change, and a git tag. Then publish again and repeat. Two to four rounds are normal.

### 5 Accept

```
/speckit-idea-standards --check     # optional: see the rule-by-rule verdicts first
/speckit-idea-accept
```

Evaluates the readiness checklist. If everything passes it asks for your name; the spec becomes v1.0 with status `accepted`. If something fails you get the list.

Standards are part of that gate, split by authority: a failed required rule of a law module (accessibility) blocks acceptance, and so does a law module that has moved since the idea was bound. A corporate-design failure does not block — it is named as a warning, and your name goes on it knowingly. The mechanism behind all of this — modules, authority, drift, exemptions — is described in `docs/process/standards.md`.

A rule that genuinely cannot apply to this idea needs a signed exemption:

```
/speckit-idea-standards --exempt STD-CD-008 --reason "this product ships white-label under the customer's name; the manual's product name cannot appear in it"
```

That writes `decisions/EXM-001.md` for you to approve by name. It stops the rule blocking; it does not make it pass, and it lapses when the module is bumped.

### 6 Prototype (optional)

The accepted spec is a finished hand-off. You can stop here and take `spec.md` into Claude Design yourself, or have the prototype built:

```
/speckit-idea-prototype
```

Writes `prototype/prototype.html` — one screen per SCR badged with its ID, navigation along the FLOWs, the content lists of §6, the states of §6 switchable, placeholder data in the UI language of §8 — and publishes it as a private page you can click through and comment on. The URL stays the same across spec versions.

A spec lane in the page, off by default, shows per screen the SCR-ID, the requirements it satisfies and their provenance tags, so you can see why an element is there without opening the spec.

`--draft` builds from a spec that is not accepted yet — an early look mid-review, or a rebuild between an `/speckit-idea-apply` and the next acceptance. The prototype then carries a DRAFT marker, and only then.

Prototype feedback has two lanes. Looks stay in the prototype: those become `VISUAL` items, the spec never changes for them, and the next build honours them. Anything about content or flow goes back through `/speckit-idea-feedback`; after `/speckit-idea-apply` the spec is v1.1, is re-accepted with `/speckit-idea-accept`, and `/speckit-idea-prototype` rebuilds.

```
/speckit-idea-accept --prototype
```

Runs the prototype checklist (every SCR built, every FLOW clickable, nothing beyond the spec) and, on your name, records the acceptance in the spec header row `Prototype` with a `proto-<slug>-v<x.y>` tag. That is the end of the loop.

## As a workflow

```bash
specify workflow run idea-to-spec -i inbox=<folder> -i name=<slug> -i reviewer=<your name>
```

The engine runs each command headless through the `claude` CLI (every step gets `--headless`, so no command tries to ask you anything) and stops at five kinds of gates: source weights, conflicts and open questions, the review decision (`revise` or `accept`), the confirmation of a normalised feedback round (the round file is shown), and the choice of whether to build a prototype after acceptance. Standards do not add a gate: the drift check and the rule-by-rule check run as ordinary steps before acceptance, and the acceptance step itself blocks or warns on the result. In a terminal a gate prompts inline. Started without a terminal (CI, another tool) the run pauses and must be resumed from a terminal:

```bash
specify workflow resume <run_id>
```

State and a step log live under `.specify/workflows/runs/<run_id>/`. Because headless runs cannot ask questions, confirmation happens by approving the gate; `speckit.idea.apply` records that as `confirmed via workflow gate <run_id>`. Feedback in a workflow run comes from two lanes: comments on the published page (when a publishing tool was available) and the file `<feature-dir>/feedback/inbox.txt`, which the review gate asks you to write. The acceptance step needs the `reviewer` input as the approver's name. After acceptance, the workflow checks `spec.md`'s status with `spec_status.py --expect accepted`; if the checklist did not actually pass, it reports that and stops instead of building a prototype from an unready spec. If it did pass, a fifth gate asks whether to build the prototype at all (`prototype` or `done`). Choosing `prototype` builds it and opens a second review loop with the same shape as the spec loop: a gate to click through it (`revise` or `accept`), a feedback round, the confirmation gate, apply, re-acceptance, rebuild. Choosing `accept` there runs `speckit.idea.accept --prototype`.

## Where things end up

```
specs/003-quote-tracker/
├── inputs/            INVENTORY.md · raw/ · extracted/S1-*.md …
├── analysis/          facts.md · conflicts.md · open-questions.md
├── standards/         BOUND.md — which modules at which version, conflicts, exemptions
├── spec.md            always the current version
├── CHANGELOG.md       one block per version, trigger per change
├── feedback/          R1.md R2.md … · inbox.txt (workflow lane) · spec-review.html · spec-v0.1.html … (frozen) · PUBLISHED.md
├── decisions/         DEC-001.md … · EXM-001.md …
├── checklists/        requirements.md · standards.md · prototype.md
└── prototype/         prototype.html (republished) · prototype-v1.0.html (frozen) · README.md · PUBLISHED.md
```

## When something goes wrong

- `spec-template` resolves to the core template: reinstall the preset (`specify preset add --dev ./presets/idea-to-spec --priority 5`).
- A skill is missing under `.claude/skills/`: reinstall the extension with `--force`.
- Spreadsheet cells show `NaN` or `1.0`: `uv` was not found, so the converter fell back to markitdown. Install `uv` or `pip install openpyxl` for the system Python.
- The AI proposes something you removed earlier: check that `decisions/DEC-*.md` exists for it; `facts` and `draft` read that folder.
- A feedback item is refused with "collides with STD-…": that is deliberate. A standard is not the reviewer's to remove. Meet the rule another way, or request an exemption.
- Acceptance is blocked by a standard that has moved: `/speckit-idea-standards --bind` rebinds to the current version, which makes a new spec version, then accept again.
- Every corporate-design rule reports "not verifiable": the `branding-cd` module is still a draft with placeholder values. Fill it from the CD manual, set `status: active`, bump the version and rebind.
