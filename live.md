# live.md

New session, any harness: read `AGENTS.md`, then `journal/history.md`,
then continue from `Resume` below. Answer lines start with `R:`.

## Current task

Resume:
- Phase: 3 (physics check). Repository `water-rocket-ai-workflow`,
  branch `main`. Last tag `phase-2-physics`.
- Done: `physics-referee` run once on commit `7032b5b`; report
  committed as `checks/physics-review.md`. It found the deliberate
  error (P1).
- Waiting for the user: Q1 (phase-3 review).
- Next step after `R: ok`: commit `journal: compact phase 3`, tag
  `phase-3-physics-check`, start phase 4 (run source-auditor).
- Talk: 2026-11-23. Phases 3 to 6 still to do.

## Open questions

**Q1. Phase 3 review.** Read `checks/physics-review.md` (summary in
Working notes). The referee found the deliberate error as P1, with a
derivation, a limit and the corrected numbers. Nothing is fixed in this
phase: fixes go in phase 5 with the source audit. Proposal: `R: ok`
closes phase 3 as it is; otherwise list what to rerun or change.
R: 

## Working notes

### physics-referee report (commit `7032b5b`)

1 error, 1 questionable, 4 minor. Files opened: only allowed ones; it
also skipped `docs/README.md` and `code/README.md` to be safe.

- P1 [error] (W2) uses absolute $p$ instead of $p - p_a$. This is the
  deliberate error. Found by derivation, by the limit $p_g = 0$ (74 N
  of thrust on an unpressurised bottle) and by the conflict with (W7).
  Its corrected numbers (apogee 26.6 m, peak thrust 145.5 N, optimum
  0.22 to 0.30) equal those of the correct model, commit `6f96f51`.
  Main session reproduced: `simulate(fill=0.25, p_g=0)` gives apogee
  1.75 m and `water_left = -0.135` kg.
- P2 [questionable] inertial head $ho_w(g+a)h$ not estimated:
  about 13 kPa at launch, 6 % of the driving pressure. Proposes a
  sensitivity case. Same point as limit 1, now with a number.
- P3 [minor] water-phase end event can fail to fire; `sol.status` not
  checked. Real, independent of P1.
- P4 [minor] $\delta_h = 0.4$ mm not reproducible: air diffusivity gives
  0.8 to 1.5 mm. Own inference (main session): the 0.4 mm follows from
  $\chi = 0.014$ cm$^2$/s, the value in `sources/gommes2010more.md`; air
  at 1 to 3 bar has 0.07 to 0.22 cm$^2$/s. Open: whether the value is
  Gommes's or a transcription error of the note. For source-auditor.
- P5 [minor] exponent effect "6 % to 7 %": 5.9 % at 5 bar from the
  rounded table.
- P6 [minor] Ding comparison at 0.75 MPa, outside the sweep, gauge or
  absolute not stated.

Checks passed include dimensions of all equations, signs, the
variable-mass balance, the nozzle relations, (W7), (B2) against the
integration.
