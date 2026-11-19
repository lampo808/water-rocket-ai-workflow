# Phase 5: prompts

Prompts of phase 5, verbatim, with a translation where needed. After
each chat prompt, the questions asked in `live.md` and the `R:` answers
given there, verbatim. Private data is redacted and marked.

## Prompt 1

Context: same chat prompt as phase 4, prompt 2 (`vai pure`, "go
ahead"). The `R: ok` on Q2 of phase 4 fixed the list of 13 fixes
(archived in `prompts/phase-4.md`).

During the work the user asked, in the chat:

```text
a che punto siamo del lavoro?
```

Translation: "where are we with the work?". Answered in the chat with
the phase status; no change to the plan.

Result: fixes 1 to 12 applied (item 13: no change). `git diff
phase-4-source-audit phase-5-revision -- docs code` shows them.

### Questions and answers, round 1

**Q1. Phase 5 review.** `git diff phase-4-source-audit -- docs code`
shows the changes (summary in Working notes). Check in particular the
new section 6.3 and (W2h), (W6h). Proposal: `R: ok` closes phase 5.
R: ok

**Q2. Content of `method/` (phase 6).** BRIEF section 8 lists six
files, written in first person as your practice, from the `Method:`
lines of the journal, the final files and the commit history:
`README.md` (index, one-page overview), `working-files.md` (live.md,
journal, `R:`, invariant, compaction, examples with commit hashes),
`agents.md` (three agents, separation of the checkers, generation from
the brief, limits), `project-layout.md` (folders, `AGENTS.md` and
`CLAUDE.md`, prompts and tags), `starting-a-project.md` (from a phone
conversation to a brief, with a template brief), `limits.md` (what did
not work, data sent to the provider). Proposal: the six files as listed.
One addition for `agents.md`: the outcome of the demo, the error found
by both checkers independently. Then the link from `README.md` to
`method/README.md`, and the "(to be written)" markers in `README.md`
removed.
R: ok. Notice somewhere in the repo that i'm fast-forwarding with minimal check, to get at the end of the process asap. Clearly, if I was to do the same in reality, much more check, direction and personal taste would be used (less plain "ok"s and more nuanced answers)

## Prompt 2

Context: new session. In Claude Code, `@live.md` attaches the file to
the prompt.

```text
read @live.md and proceed
```

Result: Q1 closed phase 5 (journal compaction, tag
`phase-5-revision`). Q2 fixed the content of `method/` for phase 6.
