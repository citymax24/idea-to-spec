# idea-to-spec

From a heap of mixed inputs (spreadsheets, slides, meeting notes, call transcripts) to an accepted, fully cited specification, then to a design brief for Claude Design. Built on [GitHub Spec Kit](https://github.com/github/spec-kit) 1.0 with one preset and one extension.

## What is in this repository

| Path | What it is |
|------|------------|
| `presets/idea-to-spec/` | Spec Kit preset: the spec template (screen catalog, provenance tags, tombstones, acceptance header) |
| `extensions/idea/` | Spec Kit extension: eight `/speckit-idea-*` commands, artifact templates, converter and renderer scripts |
| `workflows/idea-to-spec/` | Spec Kit workflow that chains the commands with human gates and the review loop |
| `specs/<NNN>-<slug>/` | One directory per idea: inputs, analysis, `spec.md`, feedback rounds, decisions, design brief |
| `examples/quote-tracker/` | Synthetic test inputs used for the first dry run |
| `docs/` | Process description, Spec Kit mapping, how-to guides |

## Quick start

```bash
uv tool install specify-cli            # Spec Kit CLI (1.0.4 or newer)
uv tool install "markitdown[all]"      # converts xlsx, pptx, docx, pdf
cd idea-to-spec
specify preset add --dev ./presets/idea-to-spec --priority 5
specify extension add --dev ./extensions/idea
specify workflow add ./workflows/idea-to-spec
```

Then, inside Claude Code in this directory:

```
/speckit-idea-intake examples/quote-tracker/inbox --name quote-tracker
/speckit-idea-facts
/speckit-idea-draft
/speckit-idea-publish
/speckit-idea-feedback "<what the reviewer said>"      # or --from-comments
/speckit-idea-apply
/speckit-idea-accept
/speckit-idea-brief
```

Or let the workflow drive it: `specify workflow run idea-to-spec -i inbox=examples/quote-tracker/inbox -i name=quote-tracker -i reviewer=Max`.

See `docs/guides/running-the-loop.md` for the details and `docs/process/idea-to-spec-process.md` for the rules behind it.
