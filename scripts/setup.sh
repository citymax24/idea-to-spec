#!/usr/bin/env bash
# Set up the idea-to-spec project on a fresh machine.
#
#   bash scripts/setup.sh          install what is missing, then verify
#   bash scripts/setup.sh --check  verify only, change nothing
#
# Idempotent: anything already installed is left alone. The repository carries
# its own .specify/ and .claude/skills/, so only command-line tools are needed.

set -euo pipefail

CHECK_ONLY=false
[[ "${1:-}" == "--check" ]] && CHECK_ONLY=true

cd "$(dirname "${BASH_SOURCE[0]}")/.."
export PATH="$HOME/.local/bin:$PATH"

ok()   { printf '  \033[32m✓\033[0m %s\n' "$1"; }
info() { printf '  \033[34m→\033[0m %s\n' "$1"; }
warn() { printf '  \033[33m!\033[0m %s\n' "$1"; }
fail() { printf '  \033[31m✗\033[0m %s\n' "$1"; }

missing=0

echo
echo "Tools"

if command -v python3 >/dev/null 2>&1; then
  ok "python3 $(python3 --version 2>&1 | cut -d' ' -f2)"
else
  fail "python3 not found — install it from your package manager"; missing=1
fi

if command -v git >/dev/null 2>&1; then
  ok "git $(git --version | cut -d' ' -f3)"
else
  fail "git not found — spec versions are git tags, install it"; missing=1
fi

if command -v uv >/dev/null 2>&1; then
  ok "uv $(uv --version | cut -d' ' -f2)"
elif $CHECK_ONLY; then
  fail "uv not found"; missing=1
else
  info "installing uv"
  curl -LsSf https://astral.sh/uv/install.sh | sh >/dev/null 2>&1 || true
  export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
  command -v uv >/dev/null 2>&1 && ok "uv installed" || { fail "uv install failed — see https://astral.sh/uv"; missing=1; }
fi

if command -v specify >/dev/null 2>&1; then
  ok "specify $(specify --version 2>/dev/null | tail -1)"
elif $CHECK_ONLY; then
  fail "specify not found"; missing=1
elif command -v uv >/dev/null 2>&1; then
  info "installing specify-cli"
  uv tool install specify-cli >/dev/null 2>&1
  command -v specify >/dev/null 2>&1 && ok "specify installed" || { fail "specify install failed"; missing=1; }
fi

if command -v markitdown >/dev/null 2>&1; then
  ok "markitdown $(markitdown --version 2>/dev/null | tail -1)"
elif $CHECK_ONLY; then
  warn "markitdown not found — pptx, docx and pdf inputs cannot be converted"
elif command -v uv >/dev/null 2>&1; then
  info "installing markitdown"
  uv tool install "markitdown[all]" >/dev/null 2>&1
  command -v markitdown >/dev/null 2>&1 && ok "markitdown installed" || warn "markitdown install failed — pptx, docx and pdf inputs cannot be converted"
fi

if command -v whisper >/dev/null 2>&1 || command -v mlx_whisper >/dev/null 2>&1; then
  ok "local transcriber found — audio inputs are transcribed automatically"
else
  warn "no local transcriber — audio inputs need a transcript file (optional)"
fi

echo
echo "Project"

if [[ -d .specify && -d .claude/skills ]]; then
  ok "installed state present (.specify, .claude/skills)"
else
  fail "run this from the repository root"; exit 1
fi

# The CLI renders with rich, which hard-wraps at 80 columns, so a long path can
# be split across lines. Collapse newlines before matching. Output is captured
# into a variable rather than piped, because `grep -q` closes the pipe early and
# `pipefail` would then report the CLI as failed.
say() { specify "$@" 2>/dev/null | tr -d '\n' || true; }

if command -v specify >/dev/null 2>&1; then
  if [[ "$(say preset resolve spec-template)" == *"presets/idea-to-spec"* ]]; then
    ok "spec template resolves to the idea-to-spec preset"
  else
    warn "spec template does not resolve to the preset"
    if ! $CHECK_ONLY; then
      info "reinstalling preset, extension and workflow from ./presets, ./extensions, ./workflows"
      specify preset remove idea-to-spec >/dev/null 2>&1 || true
      specify preset add --dev ./presets/idea-to-spec --priority 5 >/dev/null 2>&1 || true
      specify extension add --dev ./extensions/idea --force >/dev/null 2>&1 || true
      specify workflow add ./workflows/idea-to-spec >/dev/null 2>&1 || true
      if [[ "$(say preset resolve spec-template)" == *"presets/idea-to-spec"* ]]; then
        ok "reinstalled"
      else
        fail "reinstall failed — see docs/guides/install.md"; missing=1
      fi
    fi
  fi

  if [[ "$(say extension list)" == *"Idea to Spec Loop"* ]]; then
    ok "extension registered"
  else
    warn "extension not registered"; missing=1
  fi

  if [[ "$(say workflow list)" == *"idea-to-spec"* ]]; then
    ok "workflow registered"
  else
    warn "workflow not registered"
  fi
fi

skills=$(ls .claude/skills 2>/dev/null | grep -c '^speckit-idea-' || true)
if [[ "$skills" == "9" ]]; then
  ok "9 idea skills installed"
else
  warn "$skills of 9 idea skills present"; missing=1
fi

if git rev-parse --git-dir >/dev/null 2>&1; then
  ok "git repository — spec versions get tags"
else
  warn "not a git repository — run 'git init' or versions live only in CHANGELOG.md"
fi

echo
if [[ "$missing" == "0" ]]; then
  echo "Ready. Open Claude Code here and start with:"
  echo "  /speckit-idea-intake <folder with your files> --name <2-4-word-slug>"
  echo "Guides: docs/guides/running-the-loop.md · docs/guides/install.md"
else
  echo "Some checks failed. See docs/guides/install.md."
  exit 1
fi
echo
