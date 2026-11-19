# Physics review

- Reviewed: `docs/physics.md`, `code/rocket.py`, `code/fig_trajectory.py`, `code/fig_apogee_vs_fill.py`, commit 7032b5b
- Files opened: `.claude/agents/physics-referee.md` (the referee instructions), `docs/physics.md`, `code/rocket.py`, `code/fig_trajectory.py`, `code/fig_apogee_vs_fill.py`, `pyproject.toml`. Directory listings of `docs/`, `docs/figures/` and `code/`. `docs/README.md` and `code/README.md` were not opened, because the restriction on `README.md` may cover them. No restricted file was opened. The only git command used was `git rev-parse --short HEAD`.
- Execution: the figure scripts write into `docs/figures/`, so they were not run. Their printed quantities were reproduced by calling `rocket.simulate` from `uv run python -c`. No file in `docs/` or `code/` was modified.

## Summary

The document models the vertical flight of a 2 L water rocket in three phases: quasi-steady Bernoulli water thrust with polytropic air, compressible air thrust through a convergent nozzle, and a ballistic coast with quadratic drag. It reports one reference flight and the apogee as a function of the fill fraction for 1 to 5 bar gauge. The code reproduces every number in the document. The exit-velocity relation (W2) uses the absolute bottle pressure $p$ where the pressure difference $p - p_a$ is required. This inflates the water thrust by a factor $p/(p-p_a)$, gives a nonzero thrust at zero gauge pressure, contradicts the end-of-water condition (W7), and changes every result of section 6: with $p - p_a$ the reference apogee falls from 38.1 m to 26.6 m and the optimum fill moves from 0.33-0.43 to 0.22-0.30. The comparisons and observations in sections 6.1 and 6.2 that rest on these numbers do not hold. The remaining issues are a missing estimate of the inertial head and a few numerical and wording points.

## Issues

### P1. Exit velocity uses absolute instead of gauge pressure [error]

- Location: `docs/physics.md`:86, equation (W2); `code/rocket.py`:98.
- Issue: (W2) reads $u_e = \sqrt{2p/(\rho_w[1-(A_n/A_b)^2])}$ with $p$ absolute (line 44: "Pressures in the equations are absolute"). The code implements this. Bernoulli from the water surface (pressure $p$) to the nozzle exit (pressure $p_a$, line 84) gives
  $$u_e = \sqrt{\frac{2\,(p - p_a)}{\rho_w\left[1 - (A_n/A_b)^2\right]}}.$$
- Reason:
  - Derivation: $p + \tfrac12\rho_w u_s^2 = p_a + \tfrac12\rho_w u_e^2$ with $u_s = u_e A_n/A_b$. The $p_a$ term is dropped in (W2).
  - Limit $p_g = 0$: (W2) gives $u_e = \sqrt{2p_a/\rho_w} = 14.3$ m/s and $F_T = 2p_aA_n = 74$ N, larger than the weight of the filled rocket (6.3 N). An unpressurised bottle would take off. Running `simulate(fill=0.25, p_g=0)` gives an apogee of 1.75 m and `water_left = -0.135` kg: the end event never fires because $V_{end} = V_0$, the water volume overshoots $V_b$ and the mass becomes negative.
  - Internal consistency: (W7) and the code (lines 91-92) end the water phase at $p = p_a$ "with water still in the bottle". Under (W2) the jet still leaves at 14.3 m/s at that instant, so the phase is cut while the model still delivers 74 N of thrust. The condition (W7) only follows from the corrected relation, where $u_e \to 0$ as $p \to p_a$.
  - Numbers: peak thrust $\rho_w A_n u_e^2 = 2pA_n/k = 2(3.02\times10^5)(3.63\times10^{-4})/0.998 = 219.7$ N (table, line 204). With $p - p_a$: 145.5 N.
- Consequences, recomputed with $p - p_a$ in (W2) and nothing else changed (same integrator, same events):

  | Quantity, $f = 0.25$, $p_g = 2$ bar, $n = 1.4$ | Document | Corrected |
  |---|---|---|
  | peak thrust | 219.7 N | 145.5 N |
  | initial acceleration | 34.1 $g$ | 22.3 $g$ |
  | end of water phase | 62.3 ms, 32.3 m/s | 82.2 ms, 23.9 m/s |
  | thrust at end of water phase, water / air | 147 N / 56 N | 72.6 N / 55.9 N |
  | end of air phase | 83.8 ms, 34.9 m/s | 103.7 ms, 26.6 m/s |
  | velocity gain in air phase | 8 % | 11.5 % |
  | apogee | 38.1 m at 2.60 s | 26.6 m at 2.25 s |

  | $p_g$ (bar) | $n$ | $f_{opt}$ doc | apogee doc (m) | $f_{opt}$ corrected | apogee corrected (m) | within 10 % of max, corrected |
  |---|---|---|---|---|---|---|
  | 1 | 1.4 | 0.38 | 29.8 | 0.22 | 11.3 | 0.15-0.29 |
  | 1 | 1.2 | 0.43 | 31.8 | 0.24 | 12.7 | 0.16-0.32 |
  | 2 | 1.4 | 0.39 | 40.7 | 0.27 | 26.7 | 0.17-0.38 |
  | 2 | 1.2 | 0.41 | 43.3 | 0.29 | 29.3 | 0.17-0.41 |
  | 3 | 1.4 | 0.36 | 50.6 | 0.28 | 39.9 | 0.16-0.42 |
  | 3 | 1.2 | 0.38 | 53.8 | 0.30 | 43.3 | 0.16-0.46 |
  | 5 | 1.4 | 0.33 | 67.4 | 0.28 | 60.6 | 0.14-0.46 |
  | 5 | 1.2 | 0.34 | 71.4 | 0.30 | 65.0 | 0.14-0.49 |

- Conclusions that no longer follow (section 6):
  - "The optimum lies between 0.33 and 0.43. Above 2 bar it moves down with pressure." Corrected: 0.22 to 0.30, and it does not move down above 2 bar (0.27, 0.28, 0.28 for $n = 1.4$).
  - "At 1 bar the optimum lies at $f^*$." Corrected: 0.22, well below $f^* = 0.386$. In the document the optimum sits at $f^*$ because the water phase is truncated there while (W2) still gives 74 N of thrust; the steep drop at $f^*$ is enhanced by this artefact.
  - "At 2 bar, $f$ from 0.22 to 0.54 gives apogees within 10 %." Corrected: 0.17 to 0.38.
  - Comparison with Barrio-Perotti 2010 (lines 219-228): end-of-water velocity 23.9 m/s (not 32.3), air-phase gain 11.5 % (not 8 %), initial acceleration 22 $g$ (not 34 $g$). The factor between their 70 $g$ and this model becomes about 3, not 2 (section 7, item 1).
  - Lines 268-272: the corrected optimum water volume, 0.44 to 0.60 L, lies inside the 0.5 to 0.6 L range of Barrio-Perotti 2010, not above it.
  - The thrust drop at the water-air transition (line 211) is 72.6 N to 55.9 N, not 147 N to 56 N.
  - The check (B2) at line 191 still passes as a numerical check, but with a different value (corrected coast height to be recomputed).
- Suggested check or fix: replace $p$ by $p - p_a$ in (W2) and in `u_exit` (`code/rocket.py`:98), guard the square root for $p \le p_a$, regenerate both figures and every number in section 6, and rewrite the observations. Add the limit $p_g = 0$ (no lift-off) as a test.

### P2. Inertial and hydrostatic head of the water in the accelerating frame is not estimated [questionable]

- Location: `docs/physics.md`:80-91, equation (W2); section 7, item 1.
- Issue: (W2) neglects the head $\rho_w (g + a) h$ of the water column in the rocket frame. Item 1 says the effect on apogee is not quantified and leaves it open.
- Reason: at launch with $f = 0.25$ the column height in a cylinder of area $A_b$ is $h \approx 0.5\times10^{-3}/8.82\times10^{-3} = 5.7$ cm. With the corrected acceleration $a \approx 22\,g$, $\rho_w (g+a) h \approx 997.8 \times 23 \times 9.81 \times 0.057 \approx 13$ kPa, 6 % of the 2 bar driving pressure at $t = 0$. The term grows relative to $p - p_a$ as the pressure falls, and it keeps water flowing after $p = p_a$, which changes the overfilled branch near $f^*$ where the optimum lies at low pressure. The bottle neck tapers, so the cylindrical $h$ is an approximation.
- Suggested check or fix: add $\rho_w (g + a) h(V)$ to the driving pressure in (W2) as a sensitivity case, with $h(V)$ from the bottle geometry, and report the change in apogee and $f_{opt}$. This settles whether item 1 can stay "Open" or changes the conclusions.

### P3. Missing guard on the water-phase event and solver status [minor]

- Location: `code/rocket.py`:110-121.
- Issue: when $V_{pa} \le V_0$ ($p_g = 0$) the event `end` starts positive and never crosses zero with direction $+1$. The integration is not stopped and `sol.status` is not checked. Nothing prevents $V > V_b$.
- Reason: `simulate(fill=0.25, p_g=0)` returns `water_left = -0.135` kg (see P1). After the fix of P1 the flow is zero at $p_g = 0$ and the symptom disappears, but the code still relies on the event to keep $V \le V_b$.
- Suggested check or fix: return early when $p_0 \le p_a$, clip $V$ at $V_{end}$ in `rhs`, and assert `sol.status == 1` (event reached).

### P4. Thermal penetration depth not reproducible from the stated data [minor]

- Location: `docs/physics.md`:60-63.
- Issue: $\delta_h \approx \sqrt{\chi\tau} \approx 0.4$ mm is given without the value of $\chi$.
- Reason: for air at 295 K, $\chi \approx 2.2\times10^{-5}$ m$^2$ s$^{-1}$ at 1 bar and $\approx 7\times10^{-6}$ m$^2$ s$^{-1}$ at 3 bar (scaling $\chi \propto 1/p$). With $\tau = 0.1$ s this gives 0.8 to 1.5 mm. 0.4 mm requires $\chi \approx 1.6\times10^{-6}$ m$^2$ s$^{-1}$. The conclusion $\delta_h \ll D/2 = 53$ mm holds for either value.
- Suggested check or fix: state $\chi$ and its source, or correct the number.

### P5. Range of the exponent effect [minor]

- Location: `docs/physics.md`:256.
- Issue: "A lower exponent raises the apogee by 6 % to 7 %."
- Reason: from the document's own table, the ratios are 31.8/29.8 = 1.067, 43.3/40.7 = 1.064, 53.8/50.6 = 1.063, 71.4/67.4 = 1.059. The 5 bar case is 5.9 %. After P1 the ratios are 12 %, 10 %, 9 %, 7 %.
- Suggested check or fix: recompute after P1 and quote the range from the table.

### P6. Ding et al. comparison at a pressure outside the sweep [minor]

- Location: `docs/physics.md`:273-277.
- Issue: the 0.498 optimum of Ding et al. at 0.75 MPa is compared with "0.33", the 5 bar result. 0.75 MPa is above the largest pressure in the sweep (5 bar gauge) and the document does not say whether it is absolute or gauge.
- Reason: the optimum depends on pressure (table, section 6.2), so a comparison at a different pressure does not isolate the parameters named.
- Suggested check or fix: state whether 0.75 MPa is absolute or gauge and run the model at that pressure before comparing.

## Checks passed

- Dimensions of (D1), (W1), (W3)-(W7), (A0)-(A8), (B1), (B2): consistent. (W2) is dimensionally consistent; its error is physical (P1).
- Sign of drag: $v|v|$ opposes motion in all phases, code `Rocket.drag` and all `rhs` subtract it.
- Thrust sign and gravity sign in (W6), (A8), (B1) and in the code.
- Variable-mass balance (W5)-(W6): control volume attached to the rocket, jet at ambient pressure, relative exit velocity. Correct for the quasi-steady model.
- Thrust with pressure term (A7) for a choked convergent nozzle: correct form and sign.
- Choking criterion (A3), value 0.528; choked exit state (A4); subsonic exit state (A5); mass flow (A6): standard isentropic relations, matched by `nozzle()`.
- Air mass continuity across the water-air transition: $m_1 = p_1V_b/(RT_1)$ with (A0) equals $p_0V_0/(RT_a)$ for any $n$.
- (W7): $f^* = 0.539$ ($n = 1.4$) and 0.595 ($n = 1.2$) at 2 bar, as stated.
- Gommes fit at $p_0 = 3.02$ bar: $\beta = 1.15 + 0.25\,e^{-36 \times 0.00874} = 1.33$, as stated.
- Area correction in (W2): $1/\sqrt{1-0.00169} - 1 = 0.085$ %, consistent with "0.1 %".
- Derived quantities: $A_n = 3.63\times10^{-4}$ m$^2$, $A_b = 8.82\times10^{-3}$ m$^2$, $\rho_a = 1.204$ kg m$^{-3}$.
- (B2) is the exact upward solution of $\dot v = -g - \psi v^2$; numerical coast 36.552 m equals analytic 36.552 m.
- Code reproduces every number of section 6 as written (table 6.1, optimum table 6.2, 10 % band 0.22-0.54 at 2 bar, $f = 0$ apogee 2.8 m).
- Pad hold: acceleration set to zero while the net force is downward at $z = 0$; consistent with the text.
- Event detection: end of water at $V_{end}$, end of air at $m(p_a)$, apogee at $v = 0$ with direction $-1$. Correct apart from P3.
- Solver settings (RK45, tolerances, max steps) match section 5.
- Overfilled case: residual water carried as dead mass in air and ballistic phases; burnout mass includes $m_{air}$ at $p_a$.
- Reynolds number at 34.9 m/s: $2.5\times10^5$, as stated in section 7, item 9.
- Section 7 item 6 (nozzle with $\gamma$, bottle with $n$) is disclosed by the authors; not counted as an issue.
