# Working files: live.md and the journal

Two files carry the state of the project. The rules are in `AGENTS.md`
sections 3 and 4; this file explains how I use them and shows examples
from this repository.

## live.md

The written counterpart of the chat. I keep it open in Obsidian next to
the terminal. It holds what a terminal shows badly: questions with
context, derivations in LaTeX, numbers, plots.

Three sections, in this order: `## Current task`, `## Open questions`,
`## Working notes`. It is a snapshot, not a log.

Each turn the agent writes twice. The chat reply is short: what was
done, what needs me. `live.md` carries the full version.

### The resume block

`live.md` opens with a fixed line telling a new session what to read,
and `## Current task` opens with a `Resume:` list: phase, last tag, what
is done, next step, what waits for me. The agent updates it at every
turn that changes the state.

I added this rule with a free `R:` note during phase 0 (commit
`bb802a0`). The test: a new session, any harness, prompt "read
live.md". It passed in phase 0 (journal) and at the start of session 4
(`prompts/phase-5.md`, prompt 2).

### Questions and the R: convention

The agent asks questions under `## Open questions`, numbered, each with
the context needed to answer it and a proposed answer. It writes an
empty `R: ` line below each one. I answer after the colon.

```markdown
**Q11. Branch name.** The repository is on `master`. GitHub defaults to
`main`. Proposal: rename to `main` now, before any tag. Leave as is if you
prefer.
R: ok
```

What I learned:

- Questions asked in a file before any work let me answer 13 points in
  one pass at the start of phase 0, each with its context.
- The proposed answer makes `R: ok` possible. It also makes it easy to
  ratify something I did not read closely (see [limits.md](limits.md)).
- An `R:` line not under a question works as a note. I used it to add
  the resume block (`bb802a0`). The archive of answers in `prompts/`
  came from an answer that extended the agent's proposal ("keep track
  of the answers also in the future", same commit).
- An empty `R:` line is not an answer. I made this a rule in phase 2
  (`5d3e04f`), after asking the agent to prepare the `R:` lines itself.
- A question can stay open. The agent leaves it in place and does not
  act on it.

### What happens to an answer

For each answered question the agent:

1. acts on the answer;
2. records the decision and its reason in the journal;
3. copies question and answer verbatim to `prompts/phase-N.md`,
   redacting private data (local paths, third-party names) and marking
   the redaction;
4. removes both from `live.md`.

Step 3 was not in the brief. Without it the exchange is lost when the
question is removed. With it, `prompts/` holds every question and
answer of the project, in order.

## The invariant

`live.md` contains only open questions and current work. The journal
contains everything already decided. So a commit can be made at any
moment without cleanup, and `live.md` is committed with every commit.

`live.md` is not a source of history. A session never reconstructs
context from old versions of it; it reads the journal.

## The journal

`journal/history.md` is what an agent reads first to rebuild context.
One entry per session: phase, decisions and reasons, answers that
constrain later work, dead ends, open issues.

It records decisions, not the conversation. A good line, from the
brief:

```text
Thrust phase: air expansion modelled as adiabatic (gamma = 1.4). Isothermal rejected: expansion time << heat exchange time.
```

Lines starting with `Method:` record lessons about the method. They
survive compaction. This folder was written from them.

## Compaction

At the end of each phase, after my review and before the tag, the agent
rewrites the entries of that phase in compact form: decisions in force,
one line per dead end, `Method:` lines kept. It commits the result
alone (`journal: compact phase N`), so `git diff` of that commit shows
what was dropped.

Compaction commits in this repository: `227b394` (phase 0), `d03456e`,
`1b37124`, `04b044b`, `31b040e`, `05dda11` (phase 5). Phase 0 went from
122 to 79 lines. The later ones did not shrink the file: the session
entries were already written in compact form, and the compaction added
the approval line. Compaction matters most when a phase runs over
several sessions with dead ends; this project had few.

The journal is 251 lines after phase 5. The brief allows a split by
phase (`journal/phase-N.md`) if it grows too long. It was not needed.
