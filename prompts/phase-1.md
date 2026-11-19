# Phase 1: prompts

Prompts of phase 1, verbatim, with a translation where needed. After
each chat prompt, the questions asked in `live.md` and the `R:` answers
given there, verbatim. Private data is redacted and marked.

## Prompt 1

Context: same chat prompt as phase 0, prompt 4 (`read live.md`). The
`R: ok` on the phase-0 review authorised the start of phase 1.

## Prompt to lit-scout

Written by the main session and passed to the `lit-scout` subagent.

```text
Run the literature search defined in your instructions
(.claude/agents/lit-scout.md) for this repository. Scope, verification,
PDF licence rule, note format and BibTeX rules are all in that file;
follow them exactly. sources/ currently holds only README.md,
references.bib and an empty pdf/ folder: read sources/README.md first.
Target 8 to 15 sources. Return the final report described in your
instructions.
```
