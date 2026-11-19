# Project brief: water rockets, physics, and a folder-based AI workflow

This file is the starting point of the repository. It was drafted in a
conversation with Claude on a phone, then copied into an empty folder and
handed to Claude Code as the first prompt. Commit it unchanged as the first
commit of the repository: it documents where the project came from.

## 1. Context

The repository supports a 15-minute talk (23 November 2026, Department of
Science and High Technology, University of Insubria, Como) on the use of AI
in research and teaching. The audience mixes faculty, researchers and
students. Some use AI coding agents daily, most have only used chat
interfaces.

The message of the talk: the harness matters at least as much as the model
or the provider. When an AI agent works on a local project folder, the
project is a set of files the user owns and structures, not a chat history
living on someone else's server. Files can be read, edited and versioned
with git; agents are themselves files in the repository; independent agents
communicate through the folder; the conversation itself can live in a file;
and the whole project is portable to other harnesses (Codex CLI, Gemini CLI,
OpenCode, etc.).

Caveat to state in the repository: a local folder does not mean local data.
Whatever the agent reads is sent to the model provider, unless a locally
hosted model is used.

The case study is the physics of a water rocket (a PET bottle partly filled
with water and pressurized with air).

## 2. What the repository must show

1. How the project was built, through a readable commit history.
2. A sequence of phases, from setup to final document, each reproducible
   with copy-and-paste prompts.
3. A git tag at the end of each phase, to inspect the state of the project
   at that point without running anything.
4. Agent definitions are not written by hand: Claude Code generates them
   from a brief like this one, and the user reviews them.
5. A working method built on two kinds of files: a live working file that
   extends the chat, and a journal that records decisions across sessions.
6. A short documentation of the method, written at the end from how the
   files were actually used, that a new reader can follow to understand
   the repository and reuse the approach in their own projects.

Everything in the repository is in English.

## 3. Folder structure (proposal, adjust if needed)

```
BRIEF.md            this file, unchanged
README.md           overview and step-by-step phases
CLAUDE.md           project rules for Claude Code
AGENTS.md           short pointer to CLAUDE.md for other harnesses
live.md             live working file for the current session
journal/history.md  compact record of sessions and decisions
journal/figures/    plots referenced from live.md
.claude/agents/     the three subagent definitions
prompts/            the exact prompts used in each phase
sources/            one note file per retrieved source, plus open-access PDFs
sources/references.bib
docs/               the physics document(s)
code/               Python simulation
checks/             reports written by the two verification agents
method/             documentation of the working method (written last)
```

## 4. Working files: live.md and the journal

### live.md

The written counterpart of the chat, opened in Obsidian next to the
terminal. It holds what does not fit well in a terminal: questions that need
context, derivations in LaTeX, intermediate numbers, plots.

Rules:

- Every turn writes both to the chat and to live.md. The chat reply is
  terse: what was done, what needs my attention. live.md carries the
  fuller version: context, derivations, numbers, questions. Still concise.
- Questions go under `## Open questions`, numbered, each with the context
  needed to answer it.
- I answer inline on a new line starting with `R:` directly below the
  question. I may answer only some questions; the rest stay open.
- At the start of every turn, whatever I write in the chat, re-read
  live.md and look for new `R:` lines. For each answered question: act on
  the answer, record the decision in `journal/history.md`, then remove the
  question and its answer from live.md. Leave unanswered questions in
  place and do not act on them.
- Invariant: at any moment, live.md contains only open questions and
  current work; the journal contains everything already decided. A commit
  can be made at any time without extra cleanup.
- Math in Obsidian-compatible LaTeX (`$...$`, `$$...$$`). Plots saved as
  PNG in `journal/figures/` and embedded with a relative link.
- Sections: `## Current task`, `## Open questions`, `## Working notes`.
  Keep it short; it is a snapshot of the current state.
- live.md is committed with every commit, so each commit shows what was
  open at that moment. It is not a source of history: never reconstruct
  context from old versions of live.md, use the journal.

### journal/history.md

The record an agent reads to rebuild context at the start of a session. It
must also serve a human reviewer.

- One entry per session: date, phase, decisions taken and why, answers I
  gave that constrain later work, dead ends and the reason they were closed,
  open issues carried over.
- Record decisions and reasons, not the conversation.
- At the start of each session, read the journal and live.md before doing
  anything else.
- When something about the method itself is learned (a convention that
  worked, one that failed, a change to the rules), record it in the journal
  with a line starting with `Method:`. These lines are the raw material for
  the `method/` documentation and survive compaction.

### Compaction

At the end of each phase, before tagging, rewrite the journal entries of
that phase in compact form. Merge entries on the same topic. Reduce a dead
end explored over several sessions to one line: what was tried, why it was
dropped. Keep every decision still in force. Commit the compaction
separately (`journal: compact phase N`), so the full version stays in the
git history. If the journal grows too long, split it by phase
(`journal/phase-N.md`) with a short index.

## 5. Writing style (for live.md, the journal, reports and commit messages)

- Short declarative sentences. One fact per sentence where possible.
- No adverbs unless they change the meaning. No intensifiers, no hedging
  formulas, no filler ("honestly", "genuinely", "it is worth noting",
  "importantly", "let's dive in", "great question").
- State uncertainty as a fact: "Not verified: ..." or "Open: ...".
- Do not argue in terms of credibility, persuasiveness or how the work will
  be perceived. The criterion is the quality of the work: correct,
  original, careful. Justify choices by what they do for the work.
- Prefer numbers, file paths and equation labels to descriptions.
- Example of a good journal line:
  `Thrust phase: air expansion modelled as adiabatic (gamma = 1.4). Isothermal rejected: expansion time << heat exchange time.`

## 6. Project rules for CLAUDE.md

- Every bibliographic reference must have a DOI or a verifiable URL checked
  to resolve to the cited work. If verification fails, mark the reference
  as unverified; never fill in a plausible-looking one.
- Never invent numerical data, measured values or parameters. Physical
  constants and textbook relations are fine; experimental values must come
  from a saved source, cited.
- Distinguish established results, contested points and the model's own
  inferences.
- The folder is the memory of the project: decisions go into the journal,
  current work into live.md, results into docs/, code/ and checks/.
- Apply the writing style of section 5 and the live.md rules of section 4.
- Formulas in LaTeX. Code in Python (numpy, scipy, matplotlib), commented
  and modular, no emoji.
- Small, meaningful commits with descriptive messages.

## 7. The three agents

Write them as Claude Code subagents in `.claude/agents/`, with a restricted
tool set for each one. Agents do not edit live.md or the journal; the main
session updates them after reading the agents' output.

**lit-scout** (literature search). Searches the web for sources on water
rocket physics: peer-reviewed papers (e.g. physics education journals),
lecture notes, reputable technical pages. For each source writes
`sources/<key>.md` with full metadata, DOI or URL, verification status, and
a short summary of what the source supports (equations, assumptions,
numerical values with units). Downloads PDFs only when they are open
access. Updates `sources/references.bib`. Target: 8 to 15 sources.

**physics-referee** (blind physics check). Reads only the physics document
and the code it refers to. Must not read `sources/`, `journal/`, live.md or
previous reports: it judges the physics on its own merits. Checks
dimensional consistency, stated and unstated assumptions, limits and
special cases, signs, and whether conclusions follow. Writes
`checks/physics-review.md`, each issue classified as error, questionable or
minor, with its exact location. Note in the README that the blindness is an
instruction plus a fresh context, not an enforced sandbox.

**source-auditor** (consistency with sources). Reads the physics document
and `sources/`. For every claim, equation or number attributed to a source,
checks that the source supports it; flags uncited claims that need a
citation and citations that do not match. Re-checks that DOIs resolve.
Writes `checks/source-audit.md`.

The two checkers are separate on purpose: one has no access to sources, the
other works only from sources. Each runs in a fresh context and
communicates with the main session only through the files it writes.

## 8. Phases

Each phase ends with a journal compaction commit, then a tag. The exact
prompts used go into `prompts/phase-N.md`, and the README quotes them.

- **phase-0-setup**: folder structure, CLAUDE.md, AGENTS.md, live.md and
  journal templates, the three agents, README skeleton.
- **phase-1-literature**: run lit-scout; review the results with me.
- **phase-2-physics**: discussion and drafting in the main session, no
  subagents, using live.md for derivations and questions. Target content of
  `docs/physics.md`: thrust phase with water expulsion (Bernoulli with
  gauge pressure, variable mass), adiabatic expansion of the air, air-only
  thrust after the water is exhausted, ballistic phase with quadratic drag,
  optimal water fill fraction. A simulation in `code/` producing trajectory
  and apogee versus fill fraction. Assumptions and their limits stated.
- **phase-3-physics-check**: run physics-referee. This phase is shown live
  in the talk.
- **phase-4-source-audit**: run source-auditor.
- **phase-5-revision**: the main session revises the document using both
  reports; the commit diff shows what changed.
- **phase-6-method**: write `method/` from the journal (`Method:` lines
  first), the final state of the files and the commit history. Written in
  first person, as my working practices. Proposed content, to be confirmed
  with me before drafting:
  - `method/README.md`: index, and a one-page overview of how the
    repository works.
  - `method/working-files.md`: live.md and the journal, the `R:`
    convention, the invariant, compaction, with real examples taken from
    this repository's history (commit hashes or tags).
  - `method/agents.md`: why three agents, why the two checkers are kept
    separate, how they were generated from the brief and reviewed, their
    limits (blindness by instruction, non-determinism).
  - `method/project-layout.md`: the folder structure and why each folder
    exists; CLAUDE.md and AGENTS.md; prompts/ and tags for reproducibility.
  - `method/starting-a-project.md`: how to start a new project with this
    method, from a phone conversation to a brief to the first commit, with
    a template brief stripped of the water-rocket content.
  - `method/limits.md`: what did not work or needed correction during this
    project, and the caveat on data sent to the provider.
  Same writing style as section 5. Short files; link between them rather
  than repeat.

### The error found in the demo

If the model makes a physics mistake during phase 2, do not fix it: record
it in a private note I will remove before publishing, and let the referee
find it in phase 3. If there is none, I will introduce one in a separate,
labelled commit (`demo: introduce deliberate error for the live check`),
and the README will say so.

## 9. README structure

At the top, a link to `method/README.md` as the entry point for new
readers (added in phase 6). Then a short introduction (the message, the
caveat on data), requirements and installation, then one section per phase with: goal, prompt to paste,
output files, and `git checkout <tag>` to see my result. A section on the
working method (live.md, journal, compaction), with a short example of a
question answered with `R:`. A note that re-running the phases gives
different sources and text, because the models are not deterministic. A
section explaining how the repository started from BRIEF.md.

## 10. How to work with me

- Read this brief first. Before writing anything, ask me the questions you
  need answered, in live.md, then propose a plan for phase 0.
- Stop at the end of each phase and wait for my review before compacting,
  tagging and moving on.
- Do not push to GitHub; I will do it.
- I may give you the link to another repository where I use the same
  live.md and journal method. Read its conventions and reuse what fits.
  Where they conflict with this brief, ask me in live.md.
- Open points to ask me about: repository name, licence, Python version and
  environment manager, notebooks or plain scripts in `code/`, and whether
  to add a hook that reminds you to re-read live.md at every prompt.
