# method: how I work with an AI agent on a project folder

This folder describes my working method, as it was used to build this
repository. It was written last (phase 6), from the `Method:` lines of
`journal/history.md`, the final files and the commit history.

## Files

| File | Content |
|---|---|
| [working-files.md](working-files.md) | `live.md`, the journal, the `R:` convention, the invariant, compaction |
| [agents.md](agents.md) | the three agents, why the checkers are separate, the demo outcome |
| [project-layout.md](project-layout.md) | folders, `AGENTS.md` and `CLAUDE.md`, prompts and tags |
| [starting-a-project.md](starting-a-project.md) | from a phone conversation to a brief to the first commit; template brief |
| [limits.md](limits.md) | what did not work, what this run did not test, data sent to the provider |

## Overview

The project is a folder I own, versioned with git. The agent works in
it; the chat is one of several channels, and the least durable one.

1. I plan the project in a conversation and write the result as a brief
   (`BRIEF.md`). The brief is the first commit and is never edited.
2. The agent reads the brief and asks its questions in a file
   (`live.md`), each with a proposed answer. I answer on `R:` lines
   below each question.
3. Decisions move from `live.md` to the journal (`journal/history.md`)
   with their reasons. `live.md` holds only what is open now.
4. The work is split into phases. Each phase ends with my review, a
   compaction of the journal and a git tag. The prompts of each phase
   are archived verbatim in `prompts/`.
5. Agents are files (`.claude/agents/`). Two checkers with disjoint
   inputs review the main session's work. They communicate only through
   the reports they write in `checks/`.
6. The rules are in `AGENTS.md`, so other harnesses can read them.

A new session needs one prompt: "read live.md". The resume block at the
top of `live.md` and the journal restore the context.

## This run in numbers

- Phases 0 to 5 in one day (2026-11-19): `BRIEF.md` committed at 11:12, tag
  `phase-4-source-audit` at 13:04, `phase-5-revision` at 21:13. `method/`
  written the same evening.
- Phase 6 approved on 2026-11-22, in a fifth session.
- 5 sessions, 7 phases (0 to 6), one tag per phase.
- 41 `R:` answers archived in `prompts/`, the last one closing phase 6.
  In phases 1 to 5, 17 of 20 were a plain `ok`. See
  [limits.md](limits.md) for what that means.
