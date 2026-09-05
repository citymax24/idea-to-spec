---
name: speckit-idea-publish
description: Publish the current spec version as a private web page so a reviewer can read it and leave comments; records the link per version.
compatibility: Requires spec-kit project structure with .specify/ directory
metadata:
  author: github-spec-kit
  source: idea:commands/speckit.idea.publish.md
---

## User Input

```text
$ARGUMENTS
```

Optional: `--feature <specs/NNN-dir>`.

## Goal

Give the reviewer a readable page with anchors per ID, so feedback can point at `FR-014` or `SCR-03`. Comments on the page are read back by `/speckit-idea-feedback --from-comments`.

## Steps

1. **Resolve `FEATURE_DIR`**, read the header of `spec.md` for name, version and status.

2. **Render.** Run:
   ```bash
   python3 .specify/extensions/idea/scripts/python/render_spec.py FEATURE_DIR/spec.md FEATURE_DIR/feedback/spec-review.html
   ```
   Also copy the result to `FEATURE_DIR/feedback/spec-v<version>.html` as a frozen snapshot. The fixed name `spec-review.html` is what gets republished, so the review URL stays the same across versions.

3. **Publish.** If an Artifact publishing tool is available in this session, publish `feedback/spec-review.html` (same file path on every version so the URL is stable; on the first publish use the favicon 📐 and the description "Spec v<version> for review — comment on any ID"). If no such tool exists (headless run, other agent), skip publishing and say where the HTML is; the reviewer can open it locally or the human can publish it from an interactive session.

4. **Record.** Append a row to `FEATURE_DIR/feedback/PUBLISHED.md` (create it with the header `| Version | Date | URL | Git tag |` if missing): version, today, URL or `local: feedback/spec-review.html`, the git tag if one exists.

5. **Report.** The URL (or path), a one-line instruction for the reviewer ("Select any text and comment. Naming the ID, like FR-014, makes the round faster."), and the next command: `/speckit-idea-feedback --from-comments` after commenting, or `/speckit-idea-feedback "<your feedback>"` if the reviewer prefers chat.

## Rules

- Never change `spec.md` here.
- Never publish a version whose status is `accepted` under a new URL; republish the same page.