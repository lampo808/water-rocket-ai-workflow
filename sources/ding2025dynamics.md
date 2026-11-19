# ding2025dynamics

- Title: Dynamics model and simulation optimization analysis of single stage water rocket
- Authors: Shaozhe Ding, Mengyang Fan, Longbin Liu
- Year: 2025
- Venue: Results in Physics, 76, 108420
- DOI: 10.1016/j.rinp.2025.108420
- URL: https://doi.org/10.1016/j.rinp.2025.108420
- Verification: verified (Crossref: title, first author, year, journal, volume, article number match), 2026-11-19
- Access: full text read (PDF text extracted with pdftotext; equations read from the extracted layout)
- PDF: sources/pdf/ding2025dynamics.pdf (licence: CC BY 4.0, per the article footer and Crossref). Downloaded by the user in a browser; the publisher returned 403 to lit-scout.

Note written by the main session, not by lit-scout.

## What the source supports

Model (propulsion phase only, "active section"). Assumptions, section
"Water rocket dynamics model":
- Thrust from the liquid jet only. The air-only phase at the end of the
  active section is neglected ("the special thrust received at the end
  of the active section can be ignored").
- Inner and outer diameters equal (wall thickness neglected).
- Isentropic adiabatic expansion of the internal gas.

Equations as printed (numbering of the paper):
- Mixture density, eq. (2): $\rho_{mix} = \alpha\rho_g + (1-\alpha)\rho_w$,
  with void fraction $\alpha = V_g/V_{total}$, eq. (3).
- Ejected mass per step, eq. (1): $\Delta m = \rho_{mix} A_e v_e \Delta t$.
- Adiabat, eq. (6)-(7): $P_i(t)V_g^{\gamma}(t) = P_i(0)V_g^{\gamma}(0)$,
  $V_g = V_{total} - m_w/\rho_w$.
- Bernoulli with internal velocity, gravity head neglected, eq. (9)-(10):
  $$v_e = \sqrt{\frac{2(P_i - P_e)}{\rho_{mix}\left[1-(A_e/A_i)^2\right]}}$$
- Momentum balance with drag $\tfrac12 \rho_g V_{cv}^2 A_s C_d$, gravity
  and nozzle pressure term $P_e A_e$, eq. (14)-(21); explicit Euler update,
  eq. (22)-(24), $\Delta t = 0.001$ s.

Numerical results (simulation only, no measurements):
- Optimum fill for maximum altitude: water volume ratio 0.498, water mass
  ratio 0.66 of initial total mass (section "The effect of initial water
  loading"; Table 5: total volume 2.13 L, initial pressurization 0.75 MPa,
  nozzle diameter 1 cm, water 0.7 to 1.3 kg in 0.01 kg steps).
- Table 6 (water 0.96 to 1.26 kg): maximum height 42.38, 43.12, 42.32,
  40.31 m; maximum speed 25.38, 25.31, 24.68, 23.61 m/s; propulsion
  duration 0.454, 0.531, 0.62, 0.73 s.
- Table 8 (water 1.06 kg, nozzle 1.67 cm, 2.13 L): initial pressure 0.7 to
  0.9 MPa gives maximum height 45.04 to 60.23 m, about 7.66 m per 0.1 MPa.
  Residual pressure ratio 0.382 for all pressures.
- Optimal nozzle diameter 1.67 cm, maximum height 46.25 m (Table 4
  conditions: 0.92 kg water, 0.75 MPa, 2.13 L).
- Validation is against other models only: ref. [6] (Table 2 vs 3) and
  ref. [8] (Utsav et al. 2020, ASET): maximum body speed 25.35 vs 22.34
  m/s (13.46 %), propulsion-phase altitude 5.33 vs 4.8 m (10.95 %). The
  paper calls this "good agreement".

## What the source does not support

- No measurements. All values are simulation outputs.
- No air-only thrust phase; assumed negligible.
- Whether "maximum height" in Tables 6 and 8 includes the coast phase:
  Open. The coast phase is not described in the model section.
- Drag coefficient $C_d$ and dry mass $M_k$ used in Tables 4 to 8: Open,
  not stated. Ref. [8] conditions list a structural mass of 0.55 kg.
- Gauge or absolute pressure for "initial pressurization": Open in the
  text. Own inference: the model uses $P_i$ as absolute, since the
  adiabat (6) is applied to it and $P_i - P_e$ drives the jet. Check:
  $(1 - 1.06/2.13)^{1.4} = 0.381$, matching the Table 8 residual ratio
  0.382 with $\gamma = 1.4$.

## Problems noted (main session, own reading)

- Wall thickness "0.02 mm" compared with "diameters of 30 mm". Both
  values are implausible for a 2.13 L PET bottle; ref. [8] conditions
  give a rocket diameter of 0.1 m.
- Nozzle diameters in Table 4 are 1, 0.75, 0.5 cm (25 % and 50 %
  reductions), but the text reports results for 25 % and "30 %"
  reductions. The 30 % case (speed -48.5 %, height -53.0 %) does not
  match the tabulated diameters.
- The text cites "formula (11)" for the nozzle velocity; it is eq. (10).
- Validation against other simulations with 11 to 13 % deviation is
  called "good agreement".

## Category

Peer-reviewed (Results in Physics). Model and simulation only, no
measurements. Topic 5 (optimal fill fraction), topic 1 (thrust with
water), topic 2 (adiabatic expansion).
