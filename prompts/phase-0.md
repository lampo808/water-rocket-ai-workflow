# Phase 0: prompts

Prompts given in the chat, verbatim (in Italian), with a translation.
Answers given in `live.md` with `R:` lines are quoted after the chat
prompt that followed them.

## Prompt 1

Context: the folder contains only `BRIEF.md`, already committed. In
Claude Code, `@BRIEF.md` attaches the file to the prompt.

```text
leggi @BRIEF.md e procediamo
```

Translation: "read @BRIEF.md and let's proceed".

Result: 13 questions in `live.md`, each with a proposed answer, and a
plan for phase 0. No other file written.

## Answers in live.md

| Question | Answer |
|---|---|
| Q1 repository name | ok |
| Q2 licence | ok except for the open access pdfs: for those, the license in the pdfs apply |
| Q3 Python and uv | ok |
| Q4 plain scripts | ok |
| Q5 hook | ok, can we put a note in AGENTS.md or the relevant file for other harnesses so that the first time the repo is opened they ask if this should be replicated, and work their way onto replicating? |
| Q6 rules in AGENTS.md | ok the alternative |
| Q7 OneDrive | (a) |
| Q8 private notes | ok |
| Q9 commit attribution | ok |
| Q10 subagent models | ok |
| Q11 branch name | ok |
| Q12 reference repository | `[local path to another repository of the user, redacted]` |
| Q13 schedule | all needs to be completed before the talk |

The questions are in the version of `live.md` before commit `ebb4198`;
they were not committed. Their content is summarized as decisions in
`journal/history.md`.

## Prompt 2

```text
ho risposto in live.md, procedi
```

Translation: "I answered in live.md, go ahead".
