# live.md

New session, any harness: read `AGENTS.md`, then `journal/history.md`,
then continue from `Resume` below. Answer lines start with `R:`.

## Current task

Resume:
- Phase: 2 (physics, main session, no subagents). Repository
  `water-rocket-ai-workflow`, branch `main`.
- State: phase 1 closed, tag `phase-1-literature` (on commit
  `journal: compact phase 1`). Phase-2 prompts started in
  `prompts/phase-2.md`.
- Done: model outline and parameter proposal below. Nothing written yet
  in `docs/` or `code/`.
- Waiting for the user: Q1 to Q7 (model choices, parameters, files).
- Next step after the answers: write `code/rocket.py` and the figure
  scripts, run them, write `docs/physics.md`, report numbers here.
- Talk: 2026-11-23. Phases 2 to 6 still to do.

## Open questions

**Q1. Reference rocket.** Every parameter must come from a saved
source. Barrio-Perotti 2010 gives one rocket with all values measured:
2 L bottle, $m_b = 133.2$ g, $D = 106.0$ mm, nozzle $d = 21.5$ mm,
ambient 1020 mbar and 22 °C. Its drag coefficient was measured on the
same rocket by free fall: $C_D = 0.345 \pm 0.004$ (Barrio-Perotti 2009;
the 2010 paper uses 0.36). Proposal: use this rocket, $C_D = 0.345$,
vertical launch.

**Q2. Launch pressure.** The model uses absolute pressure
$p_0 = p_a + p_g$, with gauge $p_g$ as input. Proposal: $p_g = 2$ bar
for the trajectory (Barrio-Perotti measured case); apogee vs fill at
$p_g = 1, 2, 3, 5$ bar (3 bar: their student limit; 5 bar: their model
limit).

**Q3. Water phase.** Proposal: quasi-steady Bernoulli with gauge
pressure and area-ratio correction, eq. (W2) below. Neglected, stated as
limits: unsteady term and inertial head of the water column (Gommes
2010 shows they are of the same order as the pressure term at start:
contested point), nozzle losses (discharge coefficient 1), launch tube.

**Q4. Air expansion exponent.** Proposal: baseline dry adiabat,
$n = \gamma = 1.4$ (BRIEF). Sensitivity: apogee curve also with $n = 1.2$
(Romanelli 2013 measured 1.17 to 1.22, stationary bottle). Moist-air
fit of Gommes 2010, eq. (6), cited but not used.

**Q5. Air-only phase.** Two options in the sources:
(a) quasi-steady isentropic flow through a convergent nozzle, choked
while $p_a/p < 0.528$ (Barrio-Perotti 2010 approach, textbook
relations); (b) the empirical efficiency $\eta = (V_0/V_b)^{\mu}$ fitted
by Fischer 2020. Proposal: (a). It has no fitted parameter.

**Q6. Check against measured apogees.** Fischer 2020, Table 2, gives
measured apogees (14.1 to 17.5 m) for a 1 L rocket. Open for that
rocket: nozzle diameter of the launched rocket (9 mm is stated only for
the reference calculation) and gauge or absolute $p_0$. BRIEF scope does
not include a validation. Proposal: no validation in phase 2; state in
`docs/physics.md` that the model is not validated against apogee
measurements. Alternative: run it with both pressure readings and the
9 mm nozzle labelled as an assumption.

**Q7. Files.** Proposal: `code/rocket.py` (model module),
`code/fig_trajectory.py`, `code/fig_apogee_vs_fill.py`; figures saved in
`docs/figures/` with the script's name; `docs/physics.md` with numbered
equations and a section "Assumptions and limits".

## Working notes

### Model outline (proposal, depends on Q1 to Q5)

1D vertical flight, height $z$, velocity $v$. Bottle volume $V_b$,
water volume $V_{w0} = f V_b$, nozzle area $A_n$, bottle section $A_b$,
ambient $p_a$, $\rho_a$.

Water phase (air volume $V$ from $V_0 = V_b - V_{w0}$ to $V_b$):

$$p = p_0\left(\frac{V_0}{V}\right)^{n} \tag{W1}$$
$$u_e = \sqrt{\frac{2(p - p_a)}{\rho_w\left[1 - (A_n/A_b)^2\right]}} \tag{W2}$$
$$\frac{dV}{dt} = A_n u_e \tag{W3}$$
$$m = m_b + m_{air} + \rho_w (V_b - V) \tag{W4}$$
$$m\frac{dv}{dt} = \rho_w A_n u_e^2 - m g - \tfrac12 \rho_a C_D A_b\, v|v| \tag{W5}$$

Ends when $V = V_b$, or when $p = p_a$ with water left (overfill: no
air phase, the residual water stays as dead mass).

Air phase: bottle gas starts at $p_1 = p_0 (V_0/V_b)^n$, temperature
from the adiabat. Choked if $p_a/p < (2/(\gamma+1))^{\gamma/(\gamma-1)} = 0.528$:
sonic exit, $p_e > p_a$, thrust $\dot m u_e + (p_e - p_a)A_n$.
Unchoked: $p_e = p_a$. Ends when $p = p_a$.

Ballistic phase: (W5) without thrust, $m = m_b$. Apogee at $v = 0$.
Analytic check of the coast height (Fischer 2020, eq. 35):
$h_c = \frac{1}{2\psi}\ln(1 + \psi v_{max}^2/g)$,
$\psi = \rho_a C_D A_b / (2 m_b)$.

Derived numbers (textbook relations applied to Q1 values):
$A_n/A_b = (21.5/106.0)^2 = 0.041$; the correction in (W2) is 0.2 %.
$\rho_a = p_a/(R T) = 1.20$ kg m$^{-3}$ at 1020 mbar, 22 °C.

Optimal fill: apogee vs $f$ from 0 to 0.9. Labelled own inference.
Trend compared with Barrio-Perotti 2010 (range, 45 degrees: optimum 0.5
to 0.6 L in 2 L) and Ding 2025 (simulated, $f = 0.498$).
