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

The command writes `feedback/R<n>.md`: one row per item, your words verbatim, the AI's reading next to it, a type (ADD, CHANGE, REMOVE, MISREAD, QUESTION, OK) and a target. It then asks: "Did I understand each item correctly?" Reply `confirm`, correct by ID (`R1-02: also the detail screen`), or `drop R1-05`. Nothing in the spec has changed yet.

```
/speckit-idea-apply
```

Applies the confirmed round as one new version: edits with `⟲ v0.2 · R1-01` markers, tombstones plus `decisions/DEC-*.md` for removals, a changelog block naming the trigger of every change, and a git tag. Then publish again and repeat. Two to four rounds are normal.

### 5 Accept

```
/speckit-idea-accept
```

Evaluates the readiness checklist. If everything passes it asks for your name; the spec becomes v1.0 with status `accepted`. If something fails you get the list.

### 6 Design

```
/speckit-idea-brief
```

Writes `design/brief.md` (screens in flow order, one block and one plain-language design prompt per screen, constraints, "do not show") and hands off to the `design` skill: one artboard per screen, named `<SCR-ID> <Screen name>`.

Mockup feedback: looks stay in the canvas; anything about content or flow goes back through `/speckit-idea-feedback`. After `/speckit-idea-apply` the spec is v1.1 and the affected artboards are regenerated.

## As a workflow

```bash
specify workflow run idea-to-spec -i inbox=<folder> -i name=<slug> -i reviewer=<your name>
```

The engine runs each command headless through the `claude` CLI (every step gets `--headless`, so no command tries to ask you anything) and stops at four kinds of gates: source weights, conflicts and open questions, the review decision (`revise` or `accept`), and the confirmation of a normalised feedback round (the round file is shown). In a terminal a gate prompts inline. Started without a terminal (CI, another tool) the run pauses and must be resumed from a terminal:

```bash
specify workflow resume <run_id>
```

State and a step log live under `.specify/workflows/runs/<run_id>/`. Because headless runs cannot ask questions, confirmation happens by approving the gate; `speckit.idea.apply` records that as `confirmed via workflow gate <run_id>`. Feedback in a workflow run comes from two lanes: comments on the published page (when a publishing tool was available) and the file `<feature-dir>/feedback/inbox.txt`, which the review gate asks you to write. The acceptance step needs the `reviewer` input as the approver's name. After acceptance, the workflow checks `spec.md`'s status with `spec_status.py --expect accepted` before running `speckit.idea.brief`; if the checklist did not actually pass, it reports that and skips the design step instead of running it against an unready spec.

## Where things end up

```
specs/003-quote-tracker/
├── inputs/            INVENTORY.md · raw/ · extracted/S1-*.md …
├── analysis/          facts.md · conflicts.md · open-questions.md
├── spec.md            always the current version
├── CHANGELOG.md       one block per version, trigger per change
├── feedback/          R1.md R2.md … · inbox.txt (workflow lane) · spec-review.html · spec-v0.1.html … (frozen) · PUBLISHED.md
├── decisions/         DEC-001.md …
├── checklists/        requirements.md
└── design/            brief.md · README.md · mockups/v1.0/
```

## When something goes wrong

- `spec-template` resolves to the core template: reinstall the preset (`specify preset add --dev ./presets/idea-to-spec --priority 5`).
- A skill is missing under `.claude/skills/`: reinstall the extension with `--force`.
- Spreadsheet cells show `NaN` or `1.0`: `uv` was not found, so the converter fell back to markitdown. Install `uv` or `pip install openpyxl` for the system Python.
- The AI proposes something you removed earlier: check that `decisions/DEC-*.md` exists for it; `facts` and `draft` read that folder.
