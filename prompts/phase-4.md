# Phase 4: prompts

Prompts of phase 4, verbatim, with a translation where needed. After
each chat prompt, the questions asked in `live.md` and the `R:` answers
given there, verbatim. Private data is redacted and marked.

## Prompt 1

Context: same chat prompt as phase 3, prompt 2 (`procedi pure`, "go
ahead"). The `R: ok` on the phase-3 review authorised the start of
phase 4.

## Prompt to source-auditor

Written by the main session and passed to the `source-auditor`
subagent. It says nothing about the content of the document, the
deliberate error or the physics review.

```text
Run the source audit defined in your instructions
(.claude/agents/source-auditor.md) on docs/physics.md against sources/.
Follow the reading restrictions in that file exactly. Write
checks/source-audit.md in the format given there, with Markdown tables
starting at column 0, and return the final message described in your
instructions.
```

Result: `checks/source-audit.md`: 31 attributed claims (24 supported,
6 partly, 1 not supported), 3 uncited claims, 8 mismatched citations,
all references resolve. Questions Q1 (review) and Q2 (phase-5 fix list)
in `live.md`.
