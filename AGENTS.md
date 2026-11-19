# AGENTS.md: project rules

These are the rules for any AI agent working in this repository. Claude
Code reads them through `CLAUDE.md`, which imports this file. Other
harnesses (Codex CLI, OpenCode, Gemini CLI configured to read
`AGENTS.md`) read this file directly.

The repository supports a talk on AI in research and teaching. The case
study is the physics of a water rocket. The origin and goals are in
`BRIEF.md`, which is never edited.

## 1. Start of every session

1. Read `journal/history.md`, then `live.md`, before doing anything else.
2. At the start of every turn, whatever the user writes in the chat,
   re-read `live.md` and look for new `R:` lines (section 3).

## 2. The folder is the memory of the project

| Path | Holds |
|---|---|
| `live.md` | current task, open questions, working notes |
| `journal/history.md` | decisions and their reasons, across sessions |
| `journal/figures/` | PNG plots embedded in `live.md` |
| `prompts/phase-N.md` | exact prompts used in each phase |
| `sources/<key>.md` | one note per source; `sources/pdf/` open-access PDFs |
| `sources/references.bib` | BibTeX of all sources |
| `docs/` | the physics document(s) |
| `code/` | Python simulation |
| `checks/` | reports of the verification agents |
| `method/` | documentation of the working method (phase 6) |
| `private/` | git-ignored notes; never committed |

Decisions go into the journal. Current work goes into `live.md`. Results
go into `docs/`, `code/` and `checks/`. Do not keep project state only
in the conversation.

## 3. live.md

The written counterpart of the chat, read in Obsidian next to the
terminal.

- Sections, in this order: `## Current task`, `## Open questions`,
  `## Working notes`. Keep it short: a snapshot of the current state.
- Resume block: `live.md` opens with a fixed line telling a new session
  what to read, and `## Current task` opens with a `Resume:` list (phase,
  last commit or tag, what is done, next step, what waits for the user).
  Update it at every turn that changes the state. Test: in a new session,
  with any harness, the prompt "read live.md" must be enough to restore
  the context and continue.
- Every turn writes to the chat and to `live.md`. The chat reply is terse:
  what was done, what needs the user's attention. `live.md` carries the
  fuller version: context, derivations, numbers, questions.
- Questions go under `## Open questions`, numbered, each with the context
  needed to answer it and a proposed answer.
- The user answers on a new line starting with `R:` directly below the
  question. Some questions may stay unanswered.
- The agent writes an empty `R: ` line below every question it asks; the
  user types the answer after it. An `R:` line with nothing after the
  colon is not an answer: the question stays open.
- For each answered question: act on the answer, record the decision in
  `journal/history.md`, copy the question and its `R:` answer verbatim to
  `prompts/phase-N.md` (section `Questions and answers`), then remove both
  from `live.md`. Leave unanswered questions in place and do not act on
  them. Redact private data (local paths, names of third parties) in the
  copy and mark the redaction.
- An `R:` line not under a question is a note from the user: act on it,
  record it in the journal, archive it in `prompts/phase-N.md`, remove it.
- Invariant: `live.md` contains only open questions and current work; the
  journal contains everything already decided. A commit can be made at any
  moment without extra cleanup.
- Math in Obsidian-compatible LaTeX (`$...$`, `$$...$$`). Plots as PNG in
  `journal/figures/`, embedded with a relative link.
- `live.md` is committed with every commit. It is not a source of
  history: never reconstruct context from old versions of `live.md`; use
  the journal.

## 4. journal/history.md

The record an agent reads to rebuild context. It also serves a human
reviewer.

- One entry per session: date, phase, decisions and reasons, user answers
  that constrain later work, dead ends and why they were closed, open
  issues carried over.
- Record decisions and reasons, not the conversation.
- Lessons about the method itself (a convention that worked, one that
  failed, a rule change) go on a line starting with `Method:`. These lines
  are the raw material for `method/` and survive compaction.
- Compaction, at the end of each phase and before tagging: rewrite the
  entries of that phase in compact form. Merge entries on the same topic.
  Reduce a dead end to one line: what was tried, why it was dropped. Keep
  every decision still in force. Commit it alone as
  `journal: compact phase N`. If the journal grows too long, split it by
  phase (`journal/phase-N.md`) with a short index.

## 5. Research rules

- Every bibliographic reference has a DOI or a URL checked to resolve to
  the cited work. If verification fails, mark the reference
  `Not verified` and say why. Never fill in a plausible-looking DOI,
  author list, year or title.
- Never invent numerical data, measured values or parameters. Physical
  constants and textbook relations are fine. Experimental values come
  from a saved source in `sources/`, cited. A missing value is written as
  `Open: <what is missing>` and asked for in `live.md`.
- Distinguish three categories and label them: established results,
  contested points, own inferences.
- Formulas in LaTeX, with equation labels where they are referred to.

## 6. Writing style

Applies to `live.md`, the journal, reports, documents and commit messages.

- Short declarative sentences. One fact per sentence where possible.
- No adverbs unless they change the meaning. No intensifiers, no hedging
  formulas, no filler ("honestly", "genuinely", "it is worth noting",
  "importantly", "let's dive in", "great question").
- State uncertainty as a fact: `Not verified: ...` or `Open: ...`.
- Justify choices by what they do for the work (correct, original,
  careful), not by credibility, persuasiveness or how the work will be
  perceived.
- Prefer numbers, file paths and equation labels to descriptions.
- Example of a good journal line:
  `Thrust phase: air expansion modelled as adiabatic (gamma = 1.4). Isothermal rejected: expansion time << heat exchange time.`
- Everything in the repository is in English. The chat with the user may
  be in Italian.
- No emoji anywhere.

## 7. Code

- Python, with numpy, scipy, matplotlib. Plain scripts, no notebooks: a
  module with the physics model, one script per figure, named after the
  figure it produces.
- Commented and modular. SI units throughout; units stated in comments.
- Environment managed with uv: `uv sync`, then `uv run python code/<script>.py`.
- Figures carry labels, not conclusions.

## 8. Git

- Small, meaningful commits with descriptive messages, prefixed by area
  (`setup:`, `sources:`, `docs:`, `code:`, `checks:`, `journal:`, `method:`).
- Never push. The user pushes.
- Each phase ends with a journal compaction commit, then a tag
  (`phase-N-<name>`, see `README.md`). Stop at the end of each phase and
  wait for the user's review before compacting and tagging.
- The repository lives in a OneDrive-synced folder. If git reports a
  locked file, the sync client is working: wait and retry; do not delete
  lock files.

## 9. Verification agents

Three agents are defined in `.claude/agents/` (Claude Code format):
`lit-scout`, `physics-referee`, `source-auditor`. Each one writes only to
its own output files. Agents never edit `live.md` or the journal; the
main session updates them after reading the agents' output.

## 10. First session in a harness other than Claude Code

Two parts of this repository are specific to Claude Code:

- `.claude/agents/*.md`: the three subagent definitions (role, allowed
  tools, instructions).
- `.claude/settings.json` and `.claude/hooks/live-reminder.sh`: a hook
  that, at every user prompt, reminds the agent to re-read `live.md` and
  reports how many `R:` lines it contains with an answer after the
  colon (empty `R:` lines are counted apart).

If you are not Claude Code and `journal/history.md` has no `Method:` line
recording a port to your harness:

1. Before any other work, ask the user in `live.md` whether these parts
   should be replicated in your harness.
2. If yes, read your harness's own documentation for its equivalents
   (subagents or custom agents, hooks or plugins, project instructions
   file). Do not assume a format from memory: state which documentation
   page you used.
3. Create the equivalents without modifying the `.claude/` files. Keep
   the instructions of each agent identical in substance, including the
   reading restrictions of the two checkers.
4. Where your harness has no equivalent (e.g. no per-agent tool
   restriction, no prompt hook), say so in `live.md` and propose the
   closest substitute.
5. Record the port in the journal with a `Method:` line.
