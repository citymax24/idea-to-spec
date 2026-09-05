---
description: Collect raw input files (spreadsheets, slides, notes, transcripts, images) into a feature directory, convert them to Markdown and build the source inventory with stable S-IDs (or a module's own ID namespace via --prefix).
---

## User Input

```text
$ARGUMENTS
```

Arguments: `<path to a folder or to files> [--name <2-4 word slug>] [--feature <specs/NNN-dir>] [--prefix <P>] [--headless]`. The path is required unless `--feature` points at a directory that already has `inputs/raw/`.

`--prefix` sets the source-ID namespace and defaults to `S`, which is what every idea uses. Pass it only when collecting the sources of a **standards module** rather than of an idea: `--feature standards/accessibility-eaa --prefix EAA` numbers them `EAA1…EAA5`, so a citation like `[EAA4 Art. 4]` can never be confused with some idea's own `S4`.

## Interactive or headless

Headless means: `--headless` is among the arguments, or you cannot wait for a reply (a `claude -p` run, a workflow step). Interactive means you can ask and wait. Every "ask the human" step below applies only when interactive; headless runs leave the marker or status in the file and stop.

## Goal

Phase 1 of the idea-to-spec loop. Nothing gets lost, every source gets a stable ID and a readable text version, and the human sets the weight that decides conflicts. Understanding happens later in `/speckit-idea-facts`; this command only collects and labels.

## Steps

1. **Resolve the feature directory.**
   - If `--feature` is given, use it.
   - Else if `.specify/feature.json` exists, its `feature_directory` has an `inputs/` folder and no `spec.md`, reuse it (a second intake into the same idea).
   - Else create a new one: read `.specify/init-options.json` for `feature_numbering`. `sequential` (or absent): next 3-digit number after scanning `specs/`. `timestamp`: `YYYYMMDD-HHMMSS`. Slug from `--name`, else from the input folder name, kebab-case, 2–4 words. Create `specs/<prefix>-<slug>/` with `inputs/raw`, `inputs/extracted`, `analysis`, `feedback`, `decisions`, `design`, `checklists`. Write `.specify/feature.json` as `{"feature_directory": "specs/<prefix>-<slug>"}`.
   - Set `FEATURE_DIR`. The slug is the directory name without its numeric prefix (`specs/001-quote-tracker` → `quote-tracker`); commits and tags use it.

2. **Copy the inputs.** Copy (never move) every file from the given path into `FEATURE_DIR/inputs/raw/`. Skip hidden files and `.DS_Store`. If a file with the same name and identical content already exists in `raw/`, skip it (a rerun of intake must not duplicate sources). If the name exists but the content differs, keep both by appending `-2` before the extension. Do not rename otherwise; the inventory refers to the original names.

3. **Convert.** Run:
   ```bash
   python3 .specify/extensions/idea/scripts/python/convert_inputs.py FEATURE_DIR --json [--prefix <P>]
   ```
   The script assigns S-IDs (continuing from any existing inventory, never renumbering), writes `inputs/extracted/S<n>-<basename>.md` for each raw file (spreadsheets as one table per sheet with real row numbers, slides with slide markers, documents with page markers where available, text copied, audio transcribed if a local transcriber exists) and prints a JSON list of `{id, file, kind, extracted, status}`. If `python3` or the script is missing, stop and say so.

4. **Fill the gaps yourself.** For every entry with `status: "needs-agent"` or `"failed"`, open the raw file: for images, describe what is visible and transcribe visible text; for audio without a transcript, tell the human that the file needs a transcript and how to provide one (paste it, or drop a `.txt` with the same base name next to it and rerun intake); for other failures, extract what you can. Replace the placeholder comment in the extracted file with your result. Write only what is actually there. Never invent.

5. **Write the inventory.** Create or update `FEATURE_DIR/inputs/INVENTORY.md` from `.specify/extensions/idea/templates/inventory-template.md`. One row per source: ID, file, kind, date (from the content if it states one, else from the file's modification time), from (author if the content shows one, else `—`), one-sentence summary of what the source is about (not what it says), weight. Weight is `high | medium | low` and is the human's call: propose a value and mark it `(proposed)`. Existing rows keep ID and weight. List everything that still needs attention under "Needs attention".

6. **Confirm weights.** Interactive: show the inventory table and ask: "Weights okay? Reply `ok`, or correct like `S3 high, S2 low`." Apply the answer and drop `(proposed)` for confirmed rows. Headless: leave the markers, do not ask, and move on; the workflow shows the inventory at a gate.

7. **Report.** Feature directory, number of sources, which still need attention, and the next command: `/speckit-idea-facts`.

## Rules

- Never edit files in `inputs/raw/`.
- Never renumber S-IDs, never reuse an ID for a different file.
- Do not summarise or interpret sources beyond the one-line inventory entry.
