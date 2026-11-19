# Limits

What did not work, what needed correction, and what this run does not
show.

## This run was fast-forwarded

I ran phases 1 to 6 with minimal checks, to reach the end before the
talk. In phases 1 to 5, 17 of my 20 `R:` answers were a plain `ok`
(`prompts/phase-1.md` to `prompts/phase-5.md`). I did not read every
source note, every line of `docs/physics.md` or every line of code.

In a real project I would check much more, give more direction and
apply my own judgement and taste: fewer plain `ok`s, more answers that
correct, restrict or redirect a proposal. The `R:` channel supports
that; this run used little of it. Read the repository as a
demonstration of the workflow, not as a reviewed piece of physics.

## Corrections during the project

- **An inference ratified as fact.** In phase 2 the main session wrote
  "$C_D$ measured on the same rocket", inferred from equal mass and
  diameter. The question stated it as fact; I answered `ok`. The source
  audit caught it (phase 4). Rule: a proposal labels its own
  inferences, or `R: ok` ratifies them unseen.
- **A number read off a plot.** A draft gave the flat optimum as "0.20
  to 0.35", read from the figure. The sweep gives 0.17 to 0.38. Numbers
  in `docs/` now come from script output.
- **Tables indented under a list item** did not render in Obsidian. I
  fixed the report by hand (`c9e76f3`); the fix became a rule in
  `AGENTS.md` section 6 (`c8c105a`).
- **Ambiguous instruction.** I wrote "after each answer" for "below
  each question". The agent applied the reading that fits the `R:`
  convention and stated the reading in the archive.
- **No natural error for the demo.** The main session made no physics
  error the referee could find, so I introduced one ([agents.md](agents.md)).
  The demo shows the checkers find a planted error; it does not show
  how often they find unplanted ones.

## Limits of the method

- The agents were accepted as generated, without a test run. The first
  real test of each was its phase.
- Each agent ran once. Results vary between runs.
- The checkers' blindness is an instruction, not a sandbox.
- The hook and the subagents are Claude Code specific. No port to
  another harness was tried in this run.
- The agent cannot write its own permission settings in Claude Code.
  The hook configuration was created by me.
- Some sources were available only as abstracts. One PDF the agent
  could not fetch (HTTP 403) I downloaded in a browser.
- There is no validation of the model against measured apogees
  (`docs/physics.md`, limit 10).
- Compaction barely reduced the journal after phase 0
  ([working-files.md](working-files.md)). Its value is not tested by a
  project this short.

## A local folder does not mean local data

The folder is mine, and the files are versioned locally. But whatever
the agent reads (the brief, `live.md`, sources, code, the journal) is
sent to the model provider, unless a locally hosted model is used. The
same holds for the subagents and for the web pages they fetch.

In this repository nothing confidential was involved. Private notes in
`private/` stay out of git, not out of the provider's reach: the
content of `private/demo-error.md` passed through the provider when the
agent wrote it. For unpublished data, manuscripts under review or
student work, check the provider's terms
and your institution's rules before pointing an agent at the folder.
