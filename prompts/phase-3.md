# Phase 3: prompts

Prompts of phase 3, verbatim, with a translation where needed. After
each chat prompt, the questions asked in `live.md` and the `R:` answers
given there, verbatim. Private data is redacted and marked.

## Prompt 1

Context: same chat prompt as phase 2, prompt 3 (`procedi`, "go ahead").
The `R: ok` on the phase-2 review authorised the start of phase 3.

## Prompt to physics-referee

Written by the main session and passed to the `physics-referee`
subagent. It says nothing about the content of the document or about
the deliberate error.

```text
Run the physics review defined in your instructions
(.claude/agents/physics-referee.md) on docs/physics.md and the code it
refers to. Follow the reading restrictions in that file exactly. Write
checks/physics-review.md in the format given there and return the final
message described in your instructions.
```
