# Project layout

Every folder exists because something must outlive the chat. The table
in `AGENTS.md` section 2 is the reference; this file gives the reasons.

| Path | Why it exists |
|---|---|
| `BRIEF.md` | where the project came from; first commit, never edited |
| `AGENTS.md` | the rules, in the file most harnesses read |
| `CLAUDE.md` | imports `AGENTS.md` for Claude Code; adds Claude-specific notes |
| `live.md` | current work and open questions ([working-files.md](working-files.md)) |
| `journal/history.md` | decisions and reasons across sessions |
| `journal/figures/` | plots shown in `live.md` |
| `prompts/phase-N.md` | exact prompts, questions and answers of each phase |
| `.claude/agents/` | the agents, as files ([agents.md](agents.md)) |
| `.claude/settings.json`, `.claude/hooks/` | the hook that reminds the agent to re-read `live.md` |
| `sources/` | one note per source, BibTeX, redistributable PDFs |
| `docs/`, `code/` | the results: document and simulation |
| `checks/` | the reports of the two checkers |
| `method/` | this documentation |
| `private/` | git-ignored notes; never in the history |

## AGENTS.md and CLAUDE.md

The brief proposed the rules in `CLAUDE.md`, with `AGENTS.md` as a
pointer. I inverted it: rules in `AGENTS.md`, and `CLAUDE.md` imports
it with `@AGENTS.md`. Codex CLI, OpenCode and others read `AGENTS.md`
directly. Portability is then a property of the files.

Two parts do not port: the subagent definitions and the hook. `AGENTS.md`
section 10 tells another harness, on its first session, to ask me
whether to replicate them, to read its own documentation first, and to
record the port in the journal.

## The hook

`.claude/hooks/live-reminder.sh` runs at every prompt. It reminds the
agent to re-read `live.md` and counts the answered and the empty `R:`
lines. The rule "re-read `live.md` at every turn" is then enforced by
the harness, not left to the model. It does not parse the answers.

I created `.claude/settings.json` myself. Claude Code refused to let
the agent write it: it classifies that as the agent changing its own
permissions.

## Prompts and tags

`prompts/phase-N.md` holds, verbatim, every chat prompt of the phase,
every prompt the main session passed to a subagent, and every question
and `R:` answer. Italian prompts carry a translation.

Each phase ends with a tag (`phase-0-setup` to `phase-6-method`).
`git checkout <tag>` shows the state at the end of that phase without
running anything. `git diff phase-4-source-audit phase-5-revision --
docs code` shows what the two reports changed.

Re-running a phase from its prompts gives different sources and text.
The tags record the result I obtained, not a reproducible output.

## Commits

Small commits, prefixed by area (`setup:`, `sources:`, `docs:`,
`code:`, `checks:`, `journal:`, `prompts:`, `method:`, `demo:`). The
agent never pushes. Journal compaction is always its own commit.

## private/

A file removed in a later commit stays in the history. The note on the
deliberate error had to stay out of it, so `private/` is git-ignored
from the first commit after the brief.

## OneDrive

The repository lives in a synced folder. The virtual environment is
kept outside it (`UV_PROJECT_ENVIRONMENT` in the git-ignored
`.claude/settings.local.json`). A git locked-file error means the sync
client is working: wait and retry.
