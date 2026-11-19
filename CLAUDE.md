# CLAUDE.md

The project rules live in `AGENTS.md`, so that every harness reads the
same file. Claude Code imports it here:

@AGENTS.md

## Claude Code specifics

- Subagents: `.claude/agents/lit-scout.md`, `physics-referee.md`,
  `source-auditor.md`. Run each in its own context; read its output files
  afterwards, then update `live.md` and the journal.
- Hook: `.claude/settings.json` runs `.claude/hooks/live-reminder.sh` at
  every user prompt. Its output is a reminder, not an answer: still
  re-read `live.md`.
- Python environment: on this machine `UV_PROJECT_ENVIRONMENT` may be set
  in `.claude/settings.local.json` to keep the virtual environment outside
  the synced folder. Use `uv run`; do not hard-code the environment path.
