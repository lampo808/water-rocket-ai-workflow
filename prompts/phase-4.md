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

### Questions and answers, round 1

**Q1. Phase 4 review.** Read `checks/source-audit.md` (summary in
Working notes). Proposal: `R: ok` closes phase 4 as it is.
R: ok

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

R: ok

## Prompt 2

```text
vai pure
```

Translation: "go ahead".

Result: phase-4 journal compacted, tag `phase-4-source-audit`; phase 5
started with the fix list of Q2 (prompt recorded in `prompts/phase-5.md`).
