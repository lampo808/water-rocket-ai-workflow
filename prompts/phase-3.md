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

Result: `checks/physics-review.md`, 1 error (the deliberate one), 1
questionable, 4 minor. Phase-3 review question in `live.md`.

### Questions and answers, round 1

**Q1. Phase 3 review.** Read `checks/physics-review.md` (summary in
Working notes). The referee found the deliberate error as P1, with a
derivation, a limit and the corrected numbers. Nothing is fixed in this
phase: fixes go in phase 5 with the source audit. Proposal: `R: ok`
closes phase 3 as it is; otherwise list what to rerun or change.
R: ok. I've modified the review file for a rendering problem with Obsidian: need to delete the spaces before |

## Prompt 2

```text
procedi pure
```

Translation: "go ahead".

Result: the user's table fix in `checks/physics-review.md` committed;
rule on unindented tables added to `AGENTS.md` section 6; phase-3
journal compacted; tag `phase-3-physics-check`; source-auditor started.
