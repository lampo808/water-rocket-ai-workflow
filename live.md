# live.md

New session, any harness: read `AGENTS.md`, then `journal/history.md`,
then continue from `Resume` below. Answer lines start with `R:`.

## Current task

Resume:
- Phase: 5 (revision). Repository `water-rocket-ai-workflow`, branch
  `main`. Last tag `phase-4-source-audit`.
- Done: fixes 1 to 12 of the phase-5 list applied and committed
  (`d89c081` code, `b3eb98a` docs, `473f8ad` sources). Results equal
  those of the correct model of phase 2 (commit `6f96f51`).
- Waiting for the user: Q1 (phase-5 review), Q2 (content of `method/`).
- Next step after `R: ok` on Q1: commit `journal: compact phase 5`, tag
  `phase-5-revision`, then phase 6 as answered in Q2.
- Talk: 2026-11-23. Phases 5 and 6 still to do.

## Open questions

**Q1. Phase 5 review.** `git diff phase-4-source-audit -- docs code`
shows the changes (summary in Working notes). Check in particular the
new section 6.3 and (W2h), (W6h). Proposal: `R: ok` closes phase 5.
R: 

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
R: 

## Working notes

### Phase 5 changes

- (W2) restored to $p - p_a$; code and figures regenerated. Apogee
  26.6 m at $f = 0.25$, 2 bar; optimum 0.22 to 0.28 ($n = 1.4$).
- (W2h), (W6h), section 6.3, figure 3 (`code/fig_inertial_head.py`):
  inertial head with a cylindrical column. +13.8 kPa at launch; apogee
  +1.7 % (5 bar) to +3.8 % (1 bar); optimum moves by at most 0.01.
  Conclusions of section 6.2 unchanged. Unsteady term still Open.
- Guards: early return when $p_0 \le p_a$; error if the water phase
  ends without an event. $p_g = 0$ now gives apogee 0.
- $C_D$: "same rocket" removed; equal mass and diameter stated, value
  applied as own inference; Barrio-Perotti 2010 used 0.36.
- Gommes $\chi$: his value stated, air value added as own inference.
- Gommes section II B argument rephrased (unsteady vs kinetic, head vs
  pressure).
- Kagan: launch pressures stated; added to References with Thorncroft
  2009 and Watanabe 2003 (abstract only, thrust-stand data not read).
- Urieli page 3 URL in the document and in `references.bib`.
- Air phase: choked relations stated as textbook, not from
  Barrio-Perotti 2010.
- Own-inference labels: Romanelli "contested" reading, two-phase
  transition, nose-down fall; discharge coefficient 1 stated as an
  assumption. Ding: numerical comparison removed.
- (B2): Fischer uses the empty mass in $\psi$; noted.

`private/demo-error.md` is git-ignored and not in the history. Remove it
before publishing if you want the folder clean.
