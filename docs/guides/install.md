# Installing on another machine

The repository carries its own installed state under `.specify/` and `.claude/skills/`, and the registries hold no absolute paths. A plain clone is therefore already a working project: the preset, the extension and the workflow are registered, and the eight `/speckit-idea-*` skills are present. Only the command-line tools have to exist on the machine.

## 1 Tools

| Tool | Needed for | Install |
|------|------------|---------|
| Claude Code | running the skills | see claude.com/claude-code |
| git | versions and tags per spec round | preinstalled on macOS and most Linux distributions |
| Python 3 | the three helper scripts | preinstalled on macOS and most Linux distributions |
| `uv` | installs the Spec Kit CLI; also used to convert spreadsheets | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Spec Kit CLI | preset, extension, workflow management | `uv tool install specify-cli` |
| markitdown | converts pptx, docx, pdf and html inputs | `uv tool install "markitdown[all]"` |

Both `uv tool install` commands put their executables in `~/.local/bin`, so that directory has to be on the `PATH`.

Optional: a local transcriber (`whisper` or `mlx_whisper`) if audio files should be transcribed automatically. Without one, intake asks for a transcript instead of inventing content.

## 2 Clone and set up in one go

```bash
git clone https://github.com/citymax24/idea-to-spec.git
cd idea-to-spec
bash scripts/setup.sh
```

The script installs what is missing (`uv`, the Spec Kit CLI, markitdown), repairs the registered preset, extension and workflow if they are out of step, and prints what it found. It is idempotent, so running it again is harmless. `bash scripts/setup.sh --check` verifies without changing anything.

Everything below is what the script does and checks, for when you would rather do it by hand or something failed.

## 3 Verify

```bash
specify preset resolve spec-template   # must point at .specify/presets/idea-to-spec/…
specify extension list                 # Idea to Spec Loop, Commands: 8, Enabled
specify workflow list                  # Idea to Spec (idea-to-spec)
ls .claude/skills | grep idea          # eight speckit-idea-* skills
```

If all four answer as described, open Claude Code in the directory and start with `/speckit-idea-intake`. See `running-the-loop.md`.

## 4 If something is missing

A different Spec Kit version, a manual edit or a partial clone can leave the registries out of step. Reinstalling from the sources in the repository fixes it and is always safe:

```bash
specify preset remove idea-to-spec
specify preset add --dev ./presets/idea-to-spec --priority 5
specify extension add --dev ./extensions/idea --force
specify workflow add ./workflows/idea-to-spec
```

This rewrites `.specify/presets/`, `.specify/extensions/idea/`, `.specify/workflows/idea-to-spec/` and the eight skills under `.claude/skills/`. The three registry files change as a side effect; committing them is optional and harmless.

## 5 Automatic setup in a container or a cloud session

`.devcontainer/devcontainer.json` runs `scripts/setup.sh` after the container is created. Anything that reads devcontainers (VS Code "Reopen in Container", GitHub Codespaces, a Claude Code cloud session on a container image) therefore arrives with the tools installed and the project registered. Nothing has to be typed.

## 6 Where this can and cannot run

| Place | Works | Why |
|-------|-------|-----|
| Claude Code in the terminal | yes | shell, git and the Spec Kit CLI are available |
| Claude Code desktop app, VS Code and JetBrains extensions | yes | same environment |
| Claude Code on the web (cloud sessions) | yes | clones the repository and runs the setup script |
| Projects in the Claude app (claude.ai) | no | a project there is a knowledge base for chats: no shell, no git, no CLI, so the commands cannot run and no version can be tagged |

A project in the Claude app can still hold the repository as reading material through the GitHub connector, which is useful for discussing the process. Running the loop needs Claude Code.

## 7 Starting a project of your own

The clone contains the dry-run idea under `specs/001-quote-tracker/`. To keep the tooling but drop the example:

```bash
rm -rf specs/001-quote-tracker examples
rm -f .specify/feature.json
```

For a repository of your own rather than a clone of this one, point the remote at it and keep the commit history or start fresh:

```bash
git remote set-url origin <your repository>
```

Specs live in `specs/` in the same repository as the tooling. Keeping them in a separate repository also works: copy `presets/`, `extensions/`, `workflows/`, `.specify/` and `.claude/skills/` into it, or run `specify init` there and then the four commands from section 4.
