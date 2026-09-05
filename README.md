# idea-to-spec

From a heap of mixed inputs (spreadsheets, slides, meeting notes, call transcripts) to an accepted, fully cited specification that is bound to the project's standards, and from there to a clickable prototype built straight out of that spec. Built on [GitHub Spec Kit](https://github.com/github/spec-kit) 1.0 with one preset and one extension.

## What is in this repository

| Path | What it is |
|------|------------|
| `presets/idea-to-spec/` | Spec Kit preset: the spec template (screen catalog, provenance tags, tombstones, acceptance header) |
| `extensions/idea/` | Spec Kit extension: nine `/speckit-idea-*` commands, artifact templates, converter/renderer/status-check scripts |
| `standards/` | Project-wide rules every idea is bound to: accessibility (EAA/BFSG) and corporate design today, data protection or security later. One versioned module per directory |
| `workflows/idea-to-spec/` | Spec Kit workflow that chains the commands with human gates and the review loop |
| `specs/<NNN>-<slug>/` | One directory per idea: inputs, analysis, `spec.md`, feedback rounds, decisions, standards binding, prototype |
| `examples/quote-tracker/` | Synthetic test inputs used for the first dry run |
| `docs/` | Process description, Spec Kit mapping, how-to guides |

## Quick start

The clone already carries its installed state (`.specify/`, `.claude/skills/`), so only the tools are needed:

```bash
git clone https://github.com/citymax24/idea-to-spec.git
cd idea-to-spec
bash scripts/setup.sh
```

The script installs `uv`, the Spec Kit CLI and markitdown if they are missing, repairs the registered preset, extension and workflow if needed, and prints what it found. `--check` verifies without changing anything. In a devcontainer or a cloud session it runs on its own after the container is created.

This needs Claude Code (terminal, desktop app, IDE extension or a cloud session). A project in the Claude app has no shell and cannot run the loop. See `docs/guides/install.md`.

Then, inside Claude Code in this directory:

```
/speckit-idea-intake examples/quote-tracker/inbox --name quote-tracker
/speckit-idea-facts
/speckit-idea-draft
/speckit-idea-publish
/speckit-idea-feedback "<what the reviewer said>"      # or --from-comments
/speckit-idea-apply
/speckit-idea-standards                                # where this idea stands against the standards
/speckit-idea-accept
/speckit-idea-prototype                                # then click through it and comment
/speckit-idea-accept --prototype                       # when the prototype stands
```

The prototype is optional: the accepted `spec.md` is a finished hand-off on its own, and you can take it into Claude Design yourself instead.

Or let the workflow drive it: `specify workflow run idea-to-spec -i inbox=examples/quote-tracker/inbox -i name=quote-tracker -i reviewer=Max`.

See `docs/guides/install.md` to set it up on another machine, `docs/guides/running-the-loop.md` for the details of a run, and `docs/process/idea-to-spec-process.md` for the rules behind it.
