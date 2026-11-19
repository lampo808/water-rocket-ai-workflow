# fischer2020approximation

- Title: On the approximation of D.I.Y. water rocket dynamics including air drag
- Authors: L. Fischer, T. Günther, L. Herzig, T. Jarzina, F. Klinker, S. Knipper, F.-G. Schürmann, M. Wollek
- Year: 2020 (arXiv v2, 31 Jan 2020; v1 16 Jan 2020)
- Venue: arXiv:2001.08828 [physics.pop-ph]. The arXiv page gives journal-ref "Int. J. of Sci. Research in Mathematical and Statistical Sciences 6 (2019) no. 6, 1-13". Not verified: journal version not checked. The preprint states the journal text "contains several formatting errors" and recommends the preprint.
- DOI: 10.48550/arXiv.2001.08828 (arXiv DataCite DOI)
- URL: https://arxiv.org/abs/2001.08828
- Verification: verified (arXiv page loads; title and authors match), 2026-11-19
- Access: full text read (arXiv v2, 26 pp.)
- PDF: not downloaded (arXiv non-exclusive distribution licence 1.0, not CC)

## What the source supports

Flight divided into water thrust, air thrust, upward coasting (section 4).

Water thrust phase:

- Eq. (3)-(4): $D := \tfrac12\rho_{air}c_D A_R$, $a_D = (D/m)v^2$.
- Eq. (6): $m = M + m_{air} + \rho(V_b - V(t))$; mass of air treated as constant in this phase.
- Eq. (7): $v_e = \sqrt{2(p(V)-p_a)/\rho}$ (Bernoulli, water velocity in bottle neglected). Correction for finite nozzle: factor $1/\sqrt{1-(r/R)^4}$; with $R \approx 10r$ error about 0.005% (p. 5).
- Eq. (10): $a = \dfrac{2A(p(V)-p_a) - Dv^2}{M + m_{air} + \rho(V_b - V)} - g$
- Eq. (11): $p(V) = p_0 (V_0/V)^n$
- Eq. (13): $\dfrac{dV}{dt} = A\sqrt{\dfrac{2(p_0V_0^nV^{-n}-p_a)}{\rho}}$
- Eq. (14): $t_b = \dfrac1A\sqrt{\dfrac\rho2}\displaystyle\int_{V_0}^{V_b}\frac{dV}{\sqrt{p_0V_0^nV^{-n}-p_a}}$
- Eq. (15): Buck saturation vapour pressure, $p_v = K\exp\!\left[\left(18.678-\frac{T}{234.5}\right)\left(\frac{T}{257.14+T}\right)\right]$, $K = 611.21$ N/m$^2$, $T$ in °C.
- Eq. (16): $n = 1.15 + (1.4-1.15)\exp(-36 p_v/p_0)$, taken from gommes2010more / romanelli2013air. Example: $p_0 = 3$ bar, $T = 15$ °C gives $n \approx 1.35$; 10 bar gives $n \approx 1.39$ (figure 2). Stated range for moist air: $1.1 \le n \le 1.4$.
- Eq. (18): implicit analytic solution of eq. (13) via the Gauss hypergeometric function.
- Eq. (22)-(24): linear $V(t)$ approximation; drag-free estimate $v_{nb}$, $h_{nb} = v_{nb}t_b/2$.

Air thrust phase (section 5):

- Eq. (25): $m_{air} = \rho_{air}\sqrt[n]{p_0/p_a}\,V_0$; $\rho_{air} \approx 1.23$ g/dm$^3$.
- Eq. (26): $p_b = p_0(V_0/V_b)^n$, $\rho_b = \rho_{air}\dfrac{V_0}{V_b}\sqrt[n]{p_0/p_a}$
- Eq. (28): $v_{max} = v_e\ln\!\left(\dfrac{M+\eta\,m_{air}}{M}\right) + v_b$, drag and gravity neglected, constant $v_e$.
- Eq. (29): efficiency factor $\eta = (V_0/V_b)^\mu$; $\mu = 1$ first estimate; $\mu \approx 3$ fitted to their rocket. $\eta$ is an empirical fit parameter.
- Eq. (30): $v_e = \sqrt{\dfrac{2n p_a}{(n-1)\rho_{air}}\left[\left(\dfrac{p_0}{p_a}\right)^{1-\frac1n}\left(\dfrac{V_0}{V_b}\right)^{n-1} - 1\right]}$ (compressible Bernoulli, $p\propto\rho^n$; no choking considered).
- Test: rocket filled with air only at about 2 bar lifted off and reached at least 2 m (section 5.1).

Coasting phase with quadratic drag (section 6):

- Eq. (32): $\psi = \dfrac{\rho_{air}c_DA_R}{2M}$
- Eq. (33): $v(t) = \sqrt{g/\psi}\,\tan\!\left(\arctan\!\left(\sqrt{\psi/g}\,v_{max}\right) - \sqrt{\psi g}\,t\right)$
- Eq. (34): $t_c = \dfrac{1}{\sqrt{\psi g}}\arctan\!\left(\sqrt{\psi/g}\,v_{max}\right)$
- Eq. (35): $h_c = \dfrac{1}{2\psi}\ln\!\left(1+\dfrac{\psi}{g}v_{max}^2\right)$; $h_{max} = h_b + h_c$.

Drag coefficient (section 8):

- Component build-up after Gregorek (Estes, 1970), eqs. (37)-(43). Estimate $c_D = 0.57 \pm 0.06$ (rocket diameter 8 cm, $A_{cs} \approx 0.005$ m$^2$, 3 fins, root chord 7.5 cm, fin area $\approx 0.0035$ m$^2$, half tennis ball as nose, $\bar c_f \approx 0.005$, max $Re \approx 4\cdot10^5$).
- Wind tunnel (TU Dortmund), Table 1: wind speed 9.6-20.0 m/s, drag force 0.20-0.70 N ($\pm 0.1$ N), $c_D$ per point 0.5-0.7. Result $c_D = 0.6 \pm 0.2$.

Numerical values, reference case (Remark 1, section 4): empty mass 1/8 kg, bottle 1 dm$^3$, nozzle diameter 9 mm, rocket radius 4 cm, $V_0 = 0.35$ dm$^3$ (stated as propellant volume; figure 2 uses 0.65 dm$^3$ air, 0.35 dm$^3$ water), $p_0 = 3$ bar, 15 °C, air mass about 1.8 g, $c_D = 1$. Result: $v_b \approx 15.32$ m/s, $h_b \approx 2.71$ m at end of water thrust; burn time about 0.36 s (figure 3).

Launch measurements (section 9, Table 2): rocket mass 143 g, bottle 1000 ml, radius 40 mm; altitude from video against a measuring rod, $\Delta h = 0.5$ m; $\Delta p = 0.05$ bar; $\Delta V = 10$ ml.

| # | $T$ (°C) | $V_l$ (ml) | $V_0$ (ml) | $p_0$ (bar) | $h_{mes}$ (m) | $h_{calc}$ (m) | $h_{est}$ (m) |
|---|---|---|---|---|---|---|---|
| 1 | 17 | 350 | 650 | 3.5 | 17.5 | 17.2 | 17.5 |
| 2 | 17 | 325 | 675 | 3.5 | 17.1 | 17.4 | 17.6 |
| 3 | 17 | 255 | 745 | 3.0 | 14.1 | 13.3 | 13.4 |
| 4 | 17 | 255 | 745 | 3.5 | 17.4 | 17.2 | 17.3 |
| 5 | 20 | 0 | 1000 | 2.5 | > 2 | 2.4 | 2.4 |
| 6 | 35 | 250 | 750 | 2.5 | 7.6 | 9.5 | 9.5 |

Calculations use $c_D = 0.6$, $\mu = 3$. Launch 5 hit the ceiling. Launch 6 disagrees; authors report lift-off problems and leaks.

## What the source does not support

- Whether $p_0$ in Table 2 is absolute or gauge: Open. The text defines the overpressure as $p_0 - p_a$ with $p_a \approx 1$ bar, which suggests absolute, but the manometer reading is not specified.
- No measured thrust or pressure vs time.
- Air thrust model uses a fitted efficiency $\eta$; it is not derived. No choked-flow treatment.
- No optimal fill fraction study.
- Peer review status of the journal version: Not verified.

## Category

Preprint (arXiv) with a stated journal version that was not verified. Model plus measurements (wind-tunnel drag, apogees of 6 launches).
