# live.md

New session, any harness: read `AGENTS.md`, then `journal/history.md`,
then continue from `Resume` below. Answer lines start with `R:`.

## Current task

Resume:
- Phase: 4 (source audit). Repository `water-rocket-ai-workflow`,
  branch `main`. Last tag `phase-3-physics-check`.
- Done: `source-auditor` run once; report committed as
  `checks/source-audit.md`. It found the deliberate error from the
  source side (W2 does not match the three equations it cites).
- Waiting for the user: Q1 (phase-4 review), Q2 (phase-5 fix list).
- Next step after `R: ok` on Q1: commit `journal: compact phase 4`, tag
  `phase-4-source-audit`. Then phase 5 with the fix list of Q2.
- Talk: 2026-11-23. Phases 4 to 6 still to do.

## Open questions

**Q1. Phase 4 review.** Read `checks/source-audit.md` (summary in
Working notes). Proposal: `R: ok` closes phase 4 as it is.
R: 

**Q2. Phase 5: fixes.** One list from both reports. P = physics review,
S = source audit (mismatched citations, numbered as in the report).
Proposal: apply all, as described.

1. P1, S1: restore $p - p_a$ in (W2) and in the code; rerun both
   scripts; restore the numbers. Fixes the "same relation" sentence.
2. P2: inertial head $\rho_w (g + a) h$ added to the driving pressure
   as a sensitivity case, $h = (V_b - V)/A_b$ (cylinder, neck ignored,
   labelled). Report the change in apogee and $f_{opt}$. Alternative:
   only the referee's 13 kPa estimate in limit 1, no code.
3. P3: guards in `water_phase`: return when $p_0 \le p_a$, assert the
   event was reached.
4. P4: state $\chi = 0.014$ cm$^2$/s as Gommes's value; add that air
   at 1 to 3 bar has 0.07 to 0.22 cm$^2$/s, giving 0.8 to 1.5 mm (own
   inference); the conclusion is unchanged.
5. P5: exponent effect quoted from the recomputed table.
6. P6: drop the numerical comparison with Ding (different rocket,
   gauge or absolute pressure unstated); keep that both are model
   results.
7. S2: "measured on the same rocket" was my inference from equal mass
   and diameter (133 g vs 133.2 g; 106.0 mm in both), written as fact
   in phase 2. Rewrite: same mass and diameter, identity not stated;
   Barrio-Perotti 2010 used 0.36 in its model.
8. S3: rephrase the Gommes argument: unsteady term vs kinetic term,
   pressure term vs apparent-gravity term.
9. S4: Kagan: launch pressures 3.4 and 6.8 bar; which launch gave
   100 $g$ is not stated. Add `kagan1995soda` to References, "as cited
   in Gommes 2010".
10. S5: add the Urieli page 3 URL to the document and to
    `references.bib`.
11. S8 and "contested" label on Romanelli: say the choked-flow relations
    are textbook, not taken from Barrio-Perotti 2010; mark the
    "contested" reading of Romanelli's Table I as own inference.
12. Uncited claims: two-phase transition labelled own inference;
    discharge coefficient 1 stated as an assumption; thrust curves:
    "Thorncroft 2009 and Watanabe 2003 report thrust-stand data; their
    full texts were not read". "Nose down": from the sketch, figure 2.
13. Not changed: S7 (Romanelli read in arXiv v1) is already stated in
    the References.

R: 

## Working notes

### source-auditor report

31 attributed claims: 24 supported, 6 partly supported, 1 not
supported, 0 cannot check, 0 against note only. 3 uncited claims.
8 mismatched-citation entries. All 8 references resolve and match.
Full texts read from the web or `sources/pdf/`; no restricted file
opened.

- Not supported: (W2) cites Fischer eq. 7, Urieli eq. 3, Ding eq. 10;
  all three use $p - p_a$. This is the deliberate error, found from the
  sources without the physics review.
- P4 of the physics review resolved: Gommes, p. 237, eq. 1, states
  $\chi = 0.014$ cm$^2$/s and $\delta_h = 0.04$ cm. The note is
  faithful. Own inference: the value is low for air; the referee's
  point stands against the source, not against the note.
- Main other finding: S2, the "same rocket" claim (fix 7 in Q2).
