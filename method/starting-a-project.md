# Starting a project

How this repository started, and how I would start the next one.

## From a conversation to a brief

1. I planned the project in a conversation with Claude on a phone: the
   goal, the phases, the files, the agents, the rules.
2. The conversation produced `BRIEF.md`. I copied it into an empty
   folder and committed it unchanged (`b3e9432`).
3. The first prompt to Claude Code was `leggi @BRIEF.md e procediamo`
   ("read @BRIEF.md and let's proceed"), in `prompts/phase-0.md`.
4. The agent asked 13 questions in `live.md`, each with a proposed
   answer, and wrote nothing else. I answered on `R:` lines.
5. Phase 0 built the skeleton: `AGENTS.md`, `CLAUDE.md`, `.gitignore`,
   folders, environment, agents, README. Then my review, compaction,
   tag.

The brief stays unchanged. Where the project deviated from it (rules in
`AGENTS.md` instead of `CLAUDE.md`), the journal records the deviation
and the reason.

## What the brief should contain

- Context and goal. What the project must produce, for whom.
- Phases, each with an output I can review.
- Rules: references, data, labels, writing style.
- The working files and their rules, or a pointer to a repository that
  already has them.
- Agents, if any: role, inputs, outputs, what each must not read.
- Open points: things I want to be asked about before work starts.
- How to work with me: stop at the end of each phase; never push.

## Template brief

Copy, fill in, delete what does not apply.

```markdown
# Project brief: <title>

This file is the starting point of the repository. Commit it unchanged
as the first commit.

## 1. Context

<What the project is for, who reads the output, the deadline.>

## 2. What the repository must show

<Outputs, in a list.>

## 3. Folder structure (proposal, adjust if needed)

BRIEF.md            this file, unchanged
README.md           overview and phases
AGENTS.md           project rules (CLAUDE.md imports it)
live.md             live working file
journal/history.md  decisions across sessions
prompts/            exact prompts of each phase
<project folders>
private/            git-ignored notes

## 4. Working files

Use live.md and journal/history.md as described in <link to method/
working-files.md of an existing repository>, with:
- questions in live.md, numbered, with context and a proposed answer,
  and an empty `R: ` line below each;
- answered questions: act, record in the journal, archive verbatim in
  prompts/phase-N.md, remove from live.md;
- a resume block at the top of live.md;
- `Method:` lines in the journal;
- journal compaction at the end of each phase, in its own commit.

## 5. Writing style

<Short declarative sentences; uncertainty as `Open:` or `Not verified:`;
language of the repository.>

## 6. Project rules

<References with DOI or checked URL; no invented data; established,
contested and own inference labelled; code conventions.>

## 7. Agents

<For each: name, role, what it reads, what it must not read, what it
writes. Agents never edit live.md or the journal.>

## 8. Phases

<phase-0-setup, then one phase per reviewable output. Each ends with my
review, compaction, tag.>

## 9. How to work with me

- Read this brief. Before writing anything, ask me your questions in
  live.md, then propose a plan for phase 0.
- Stop at the end of each phase and wait for my review.
- Do not push.
- Open points to ask me about: <list>.
```

## For the next project

Not tried yet. I would reuse `AGENTS.md`, the hook and the structure
of `live.md` from this repository, and point the brief at them instead
of restating them. The project-specific parts of the brief are sections 1, 2, 6, 7
and 8.
