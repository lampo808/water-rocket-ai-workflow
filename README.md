# water-rocket-ai-workflow

<!-- Phase 6: link to method/README.md here, as the entry point for new readers. -->

This repository supports a 15-minute talk on AI in research and teaching
(23 November 2026, Department of Science and High Technology, University
of Insubria, Como). The case study is the physics of a water rocket: a PET
bottle partly filled with water, pressurized with air.

## The message

The harness matters at least as much as the model or the provider. When
an AI agent works on a local project folder, the project is a set of
files you own and structure, not a chat history on someone else's server:

- Files can be read, edited and versioned with git.
- The agents are themselves files in the repository (`.claude/agents/`).
- Independent agents communicate through the folder (`sources/`,
  `checks/`).
- The conversation extends into a file (`live.md`), and decisions are kept
  in another (`journal/history.md`).
- The project rules are in `AGENTS.md`, read by Claude Code (through
  `CLAUDE.md`), Codex CLI, OpenCode and other harnesses.

**A local folder does not mean local data.** Whatever the agent reads is
sent to the model provider, unless a locally hosted model is used.

## Requirements

- git
- [uv](https://docs.astral.sh/uv/) (installs Python and the dependencies)
- [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) to
  re-run the phases as they were run here. Other harnesses can read
  `AGENTS.md`; see its section 10 for the Claude Code specific parts.
- Optional: [Obsidian](https://obsidian.md) to read `live.md` with
  rendered LaTeX and images.

```sh
git clone <repository-url>
cd water-rocket-ai-workflow
uv sync
```

## Phases

Each phase ends with a tag. `git checkout <tag>` shows the state of the
project at the end of that phase, without running anything. The exact
prompts are in `prompts/phase-N.md`.

Re-running a phase gives different sources and different text: the models
are not deterministic. The tags record the result obtained here.

### Phase 0: setup

- Goal: folder structure, rules (`AGENTS.md`, `CLAUDE.md`), `live.md` and
  journal, the three agents, this README skeleton.
- Prompts: `prompts/phase-0.md`.
- Output: everything outside `docs/`, `code/`, `sources/`, `checks/`,
  `method/`.
- Result: `git checkout phase-0-setup`

### Phase 1: literature

- Goal: run `lit-scout`; review the sources with the user.
- Prompts: `prompts/phase-1.md` (to be written).
- Output: `sources/<key>.md`, `sources/references.bib`, `sources/pdf/`.
- Result: `git checkout phase-1-literature`

### Phase 2: physics

- Goal: derive the model in the main session, no subagents, with
  derivations and questions in `live.md`. Thrust with water expulsion,
  adiabatic expansion of the air, air-only thrust, ballistic phase with
  quadratic drag, optimal fill fraction. A simulation of trajectory and
  apogee versus fill fraction.
- Prompts: `prompts/phase-2.md` (to be written).
- Output: `docs/physics.md`, `code/`.
- Result: `git checkout phase-2-physics`

### Phase 3: physics check (shown live in the talk)

- Goal: run `physics-referee` on `docs/` and `code/`.
- Prompts: `prompts/phase-3.md` (to be written).
- Output: `checks/physics-review.md`.
- Result: `git checkout phase-3-physics-check`

### Phase 4: source audit

- Goal: run `source-auditor` on `docs/` against `sources/`.
- Prompts: `prompts/phase-4.md` (to be written).
- Output: `checks/source-audit.md`.
- Result: `git checkout phase-4-source-audit`

### Phase 5: revision

- Goal: revise the document from both reports.
- Prompts: `prompts/phase-5.md` (to be written).
- Output: `docs/`, `code/`. `git diff phase-4-source-audit phase-5-revision -- docs code`
  shows what changed.
- Result: `git checkout phase-5-revision`

### Phase 6: method

- Goal: document the working method from the journal, the final files and
  the commit history.
- Prompts: `prompts/phase-6.md` (to be written).
- Output: `method/`.
- Result: `git checkout phase-6-method`

## The agents

| Agent | Reads | Writes | Tools |
|---|---|---|---|
| `lit-scout` | the web | `sources/` | web search and fetch, files, `curl` |
| `physics-referee` | `docs/`, `code/` only | `checks/physics-review.md` | files, runs the code |
| `source-auditor` | `docs/`, `sources/` only | `checks/source-audit.md` | files, fetch (DOI check) |

The two checkers are separate on purpose. One has no access to the
sources and judges the physics on its own merits. The other works only
from the sources. Each runs in a fresh context and communicates with the
main session only through the file it writes. The agents never edit
`live.md` or the journal.

The blindness of the checkers is an instruction plus a fresh context,
not an enforced sandbox. The agent could open a forbidden file; it is
told not to, and to list the files it opened in its report.

The agent definitions were not written by hand. Claude Code generated
them from `BRIEF.md` section 7; the user reviewed them before the commit.

## Working method

Two files carry the state of the project across turns and sessions.

- `live.md` is the written counterpart of the chat: current task, open
  questions, working notes, derivations in LaTeX, plots. It contains only
  what is open now.
- `journal/history.md` records decisions and their reasons, session by
  session. An agent reads it to rebuild context.

Questions go in `live.md`, each with a proposed answer. The user answers
on a line starting with `R:` below the question. At the next turn the
agent acts on the answer, records the decision in the journal and removes
the question from `live.md`. Example from phase 0:

```markdown
**Q11. Branch name.** The repository is on `master`. GitHub defaults to
`main`. Proposal: rename to `main` now, before any tag. Leave as is if you
prefer.
R: ok
```

Journal line produced: `Branch renamed from master to main before any tag.`

At the end of each phase the journal entries of that phase are compacted
in a separate commit (`journal: compact phase N`), so the full version
stays in the history.

In Claude Code, a hook (`.claude/settings.json`,
`.claude/hooks/live-reminder.sh`) reminds the agent at every prompt to
re-read `live.md`.

## How the repository started

The project was planned in a conversation with Claude on a phone. The
result is `BRIEF.md`, copied into an empty folder and committed unchanged
as the first commit. The first prompt to Claude Code was to read it and
proceed. Everything after that commit was built from the brief, phase by
phase.

## Licence

MIT for code, CC BY 4.0 for text. PDFs in `sources/pdf/` keep their own
licence. See `LICENSE`.
