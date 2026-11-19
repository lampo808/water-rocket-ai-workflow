# Phase 2: prompts

Prompts of phase 2, verbatim, with a translation where needed. After
each chat prompt, the questions asked in `live.md` and the `R:` answers
given there, verbatim. Private data is redacted and marked.

## Prompt 1

Context: same chat prompt as phase 1, prompt 3 (`read @live.md and
proceed`). The `R: ok, proceed` on the phase-1 review authorised the
start of phase 2.

Result: model choices and parameter set proposed in `live.md` as
questions Q1 to Q7, with an outline of the equations. No file in `docs/`
or `code/` written before the answers.

### Questions and answers, round 1

**Q1. Reference rocket.** Every parameter must come from a saved
source. Barrio-Perotti 2010 gives one rocket with all values measured:
2 L bottle, $m_b = 133.2$ g, $D = 106.0$ mm, nozzle $d = 21.5$ mm,
ambient 1020 mbar and 22 °C. Its drag coefficient was measured on the
same rocket by free fall: $C_D = 0.345 \pm 0.004$ (Barrio-Perotti 2009;
the 2010 paper uses 0.36). Proposal: use this rocket, $C_D = 0.345$,
vertical launch.
R: ok

**Q2. Launch pressure.** The model uses absolute pressure
$p_0 = p_a + p_g$, with gauge $p_g$ as input. Proposal: $p_g = 2$ bar
for the trajectory (Barrio-Perotti measured case); apogee vs fill at
$p_g = 1, 2, 3, 5$ bar (3 bar: their student limit; 5 bar: their model
limit).
R: ok

**Q3. Water phase.** Proposal: quasi-steady Bernoulli with gauge
pressure and area-ratio correction, eq. (W2) below. Neglected, stated as
limits: unsteady term and inertial head of the water column (Gommes
2010 shows they are of the same order as the pressure term at start:
contested point), nozzle losses (discharge coefficient 1), launch tube.
R: ok

**Q4. Air expansion exponent.** Proposal: baseline dry adiabat,
$n = \gamma = 1.4$ (BRIEF). Sensitivity: apogee curve also with $n = 1.2$
(Romanelli 2013 measured 1.17 to 1.22, stationary bottle). Moist-air
fit of Gommes 2010, eq. (6), cited but not used.
R: ok

**Q5. Air-only phase.** Two options in the sources:
(a) quasi-steady isentropic flow through a convergent nozzle, choked
while $p_a/p < 0.528$ (Barrio-Perotti 2010 approach, textbook
relations); (b) the empirical efficiency $\eta = (V_0/V_b)^{\mu}$ fitted
by Fischer 2020. Proposal: (a). It has no fitted parameter.
R: ok

**Q6. Check against measured apogees.** Fischer 2020, Table 2, gives
measured apogees (14.1 to 17.5 m) for a 1 L rocket. Open for that
rocket: nozzle diameter of the launched rocket (9 mm is stated only for
the reference calculation) and gauge or absolute $p_0$. BRIEF scope does
not include a validation. Proposal: no validation in phase 2; state in
`docs/physics.md` that the model is not validated against apogee
measurements. Alternative: run it with both pressure readings and the
9 mm nozzle labelled as an assumption.
R: ok

**Q7. Files.** Proposal: `code/rocket.py` (model module),
`code/fig_trajectory.py`, `code/fig_apogee_vs_fill.py`; figures saved in
`docs/figures/` with the script's name; `docs/physics.md` with numbered
equations and a section "Assumptions and limits".
R: ok

## Prompt 2

```text
procedi. Prepara già tu le righe R: dopo ogni risposta, salvalo come regola. Off topic, la mia statusline non aggiorna più contesto e uso sessione
```

Translation: "go ahead. Prepare the R: lines yourself after each
answer [read as: below each question], save it as a rule. Off topic, my
status line no longer updates context and session usage".

Result: rule added to `AGENTS.md` section 3 (empty `R:` line below each
question); hook counts answered and empty `R:` lines apart. The status
line fix concerned a user file outside the repository and is not
recorded here. `code/rocket.py`, two figure scripts, `docs/physics.md`
written; phase-2 review questions in `live.md`.

### Questions and answers, round 2

**Q1. Phase 2 review.** Read `docs/physics.md` (results in section 6,
limits in section 7) and the two figures. Points to check: limit 1
(water inertia neglected: initial acceleration 22 $g$ here, about 70 $g$
in Barrio-Perotti 2010) and limit 6 (air phase with $\gamma$ in the
nozzle, $n$ in the bottle). Proposal: `R: ok` closes phase 2 as it is;
otherwise list corrections.
R: ok

**Q2. Error for the live check.** BRIEF section 8: a physics error made
in phase 2 is left unfixed for the referee. I have not found one. One
error of mine was caught before the commit (a number read off a plot,
not physics; journal, `Method:` line). BRIEF: if there is none, you
introduce one in a separate commit `demo: introduce deliberate error for
the live check`. Proposal: you choose the error and write it here; I
make that commit and record it in `private/demo-error.md`. Example of a
plausible one: thrust in (W5) written as $\rho_w A_n u_e^2/2$, or the
absolute pressure $p$ in place of $p - p_a$ in (W2).
R: let's go with the absolute pressure instead of p-pa

## Prompt 3

```text
procedi
```

Translation: "go ahead".

Result: deliberate error introduced (commit `demo: introduce deliberate
error for the live check`), README notice added, phase-2 journal
compacted, tag `phase-2-physics`. Phase 3 started.
