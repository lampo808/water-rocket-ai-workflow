# romanelli2013air

- Title: Air expansion in a water rocket
- Authors: Alejandro Romanelli, Italo Bove, Federico González Madina
- Year: 2013
- Venue: American Journal of Physics, 81(10), 762-766
- DOI: 10.1119/1.4811116
- URL: https://doi.org/10.1119/1.4811116 ; preprint https://arxiv.org/abs/1211.1923
- Verification: verified (Crossref: title, first author, year, journal match), 2026-11-19
- Access: full text read of the arXiv preprint v1 (8 Nov 2012, title "Air expansion in the water rocket", 5 pp.). The published AJP version was not read. Differences between versions: Open.
- PDF: not downloaded (arXiv non-exclusive distribution licence 1.0, not CC; publisher version closed)

## What the source supports

All equation numbers refer to the arXiv v1 preprint.

- Eq. (1): $dQ/dT = Nc$ (polytropic process: constant specific heat $c$).
- Eq. (3): $PV^\beta = \text{const}$; eq. (4): $\beta = \dfrac{c_p - c}{c_v - c}$. Adiabatic $c = 0$, $\beta = \gamma$; isothermal $c = \infty$, $\beta = 1$.
- Eq. (5): $c = \dfrac{c_p - \beta c_v}{1-\beta}$; eq. (6): $Q = cN(T - T_0)$.
- Eq. (9): $P_v = P_{v0}\,e^{\frac{L_v}{R_v}\left(\frac{1}{T_0}-\frac1T\right)}$ (Clausius-Clapeyron, constant $L_v$).
- Eq. (18), theoretical exponent:
  $\beta = \dfrac{c_p/R + (L_v/R_vT_0)^2 (P_{v0}/P_0)}{c_v/R + (L_v/R_vT_0)^2(P_{v0}/P_0) - (L_v/R_vT_0)(P_{v0}/P_0)}$
- Eq. (19): restates the empirical fit of gommes2010more, $\beta = 1.15 + (1.4-1.15)\exp(-36P_{v0}/P_0)$.
- Conclusion: $\beta$ depends only on initial thermodynamic conditions; vapour condensation is the main heat source; heat exchange through walls neglected (experiment lasts < 1 s).

Assumptions:

- Air saturated with vapour at start ($\varepsilon = 1$), justified by compressor heating then cooling.
- Ideal gas for air and vapour; relative change of total moles negligible ($\delta N_v/N \sim 10^{-3}$, eq. 14).

Experiment (section III), stationary bottle:

- Acrylic cylinder, inner diameter 5.40 cm, wall 0.30 cm, length 1 m, vertical; conical bottom with 0.5" faucet; manometer 0-4 bar (WIKA EN 837-1).
- About 1400 cm$^3$ water; initial gas volume $V_0 = 928.6$ cm$^3$.
- Video at 50 frames/s, 10 ms exposure; pressure and gas volume read from video.
- $T_0 = 292$ K; $P_{v0} = 2.3$ kPa; $L_v = 2500$ kJ/kg; $R_v = 0.4615$ kJ/(kg K).
- Each initial pressure repeated five times.
- Table I ($P_A$ = atmospheric pressure, so $P_0/P_A$ is an absolute ratio):

| $P_0/P_A$ | $\beta$ (measured) | $\beta^*$ (eq. 18) | $c/R$ | $t$ (s) | $Q$ (J) |
|---|---|---|---|---|---|
| 4.8 | 1.22 | 1.27 | -2.0 | 0.64 | 161.7 |
| 4.4 | 1.21 | 1.26 | -2.2 | 0.66 | 158.3 |
| 4.0 | 1.20 | 1.25 | -2.6 | 0.75 | 154.7 |
| 3.6 | 1.19 | 1.24 | -2.7 | 0.75 | 144.8 |
| 3.2 | 1.17 | 1.23 | -3.5 | 0.88 | 144.9 |

- Ejection time 0.64-0.88 s, compared with 0.1 s for a usual water rocket (citing Kagan et al.).
- Nozzle area: stationary bottle $a_1 = 0.4\,a_2$, with soda bottle nozzle $a_2 = 3.46\times10^{-4}$ m$^2$.

Own inference (not stated by the source): in Table I the measured $\beta$ is below $\beta^*$ by 0.05-0.06 in every row; the text calls the agreement "very good".

## What the source does not support

- No flying rocket: the bottle is fixed, so the apparent gravity and the ejection time (0.7 s vs 0.1 s) differ from a launch. The authors argue $\beta$ transfers to the flying rocket because $\beta^*$ does not depend on ejection rate; this transfer is not measured.
- No thrust, trajectory, drag or fill-fraction results.
- No air-only phase.

## Category

Peer-reviewed. Measurement (pressure-volume curve of the expanding gas, stationary bottle) plus model.
