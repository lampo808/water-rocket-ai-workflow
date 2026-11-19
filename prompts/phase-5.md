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
