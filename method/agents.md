# Agents

Three subagents, defined as files in `.claude/agents/`. Each runs in a
fresh context, with a restricted tool set, and writes only its own
output files. None edits `live.md` or the journal: the main session
reads their output and updates both.

| Agent | Phase | Reads | Writes |
|---|---|---|---|
| `lit-scout` | 1 | the web | `sources/<key>.md`, `sources/references.bib`, `sources/pdf/` |
| `physics-referee` | 3 | `docs/`, the code it refers to | `checks/physics-review.md` |
| `source-auditor` | 4 | `docs/`, `sources/` | `checks/source-audit.md` |

## Why three

Each agent does one job that benefits from a fresh context. The main
session wrote the physics in phase 2 and carries its own reasoning. A
reviewer with the same context tends to repeat it. A fresh agent sees
only the files.

## Why the two checkers are separate

They have disjoint inputs on purpose.

- `physics-referee` has no access to sources, journal, `live.md`,
  `README.md`, `BRIEF.md`, `prompts/` or the git history. It judges the
  physics on its own merits: dimensions, limits, signs, consistency.
- `source-auditor` does not judge the physics. It checks that each
  claim attributed to a source is in the source, and that each DOI
  resolves. It checks against the source text, not against lit-scout's
  notes, which may be wrong.

An error can then be found by two independent routes.

## The demo outcome

The main session found no physics error in phase 2. I introduced one in
a labelled commit (`db9a551`): absolute pressure $p$ in place of
$p - p_a$ in equation (W2). The numbers and figures were regenerated
with it, so the document was self-consistent. Neither checker was told.

- `physics-referee` (phase 3, `995d917`) classified it as an error. It
  derived the relation, took the limit $p_g = 0$ (no pressure, yet
  thrust) and found the conflict with (W7). Its corrected numbers
  matched the correct model of `6f96f51`.
- `source-auditor` (phase 4, `1be8be8`) marked (W2) as the one claim
  not supported: the three cited sources write $p - p_a$.

Both found it, by different routes. The fix is in `d89c081` (phase 5).

The source audit also found an error that was not planned: an
inference of the main session ("$C_D$ measured on the same rocket")
written as fact in phase 2. I had accepted it with `R: ok` because the
question stated it as fact.

## How they were generated

The brief (section 7) describes each agent in a paragraph. Claude Code
wrote the definitions from it (`4a9e30d`). I read them and committed
them unchanged. In a real project I would run each on a test case and
tune it before relying on it. Here the first real test of each agent
was its phase.

## Limits

- Blindness is an instruction plus a fresh context, not a sandbox. The
  referee could open a forbidden file. It is told not to, and to list
  the files it opened in its report. The list shows what it read; it
  cannot show what it would have read without the instruction.
- The referee read its restrictions conservatively: it skipped
  `docs/README.md` and `code/README.md` because the ban on `README.md`
  might cover them.
- The referee did not run the figure scripts, because they write into
  `docs/`, which it must not modify. It called the model directly. A
  read-only checker needs scripts that do not write output, or an
  option to write elsewhere.
- Each agent ran once. A second run would find a different set of
  issues: the models are not deterministic. One run is a sample, not a
  certification.
- The subagent format is specific to Claude Code. `AGENTS.md` section
  10 tells another harness to ask whether to port the agents, using its
  own documentation.
