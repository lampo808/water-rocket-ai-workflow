# barrioperotti2010theoretical

- Title: Theoretical and experimental analysis of the physics of water rockets
- Authors: R. Barrio-Perotti, E. Blanco-Marigorta, J. Fernández-Francos, M. Galdo-Vega
- Year: 2010
- Venue: European Journal of Physics, 31(5), 1131-1147
- DOI: 10.1088/0143-0807/31/5/015
- URL: https://doi.org/10.1088/0143-0807/31/5/015
- Verification: verified (Crossref: title, first author, year, journal match), 2026-11-19
- Access: full text read. Read from a copy of the publisher PDF hosted by a third party (https://iypt.ru/wp-content/uploads/2024/10/Theoretical-and-experimental-analysis-of-the-physics-of-water-rockets.pdf). The publisher version is not open access (OpenAlex). A submitted version is listed in the Universidad de Oviedo repository (http://hdl.handle.net/10651/10241, CC BY-NC-ND per OpenAlex); no file link visible on the repository page.
- PDF: not downloaded (publisher copy has no open licence; repository copy is CC BY-NC-ND, not in the allowed licence list)

## What the source supports

Model in three stages: water propulsion, air propulsion, ballistic flight (section 3, figures 2-4). Control-volume approach with Reynolds transport theorem. Launch from an inclined ramp at angle $\theta$.

Equations, water propulsion (section 4.1). Notation: $m_w$ water mass, $m_a$ air mass, $m_b$ empty rocket mass, $v_b$ rocket velocity, $v_{wn}$ water velocity relative to nozzle, $S$ nozzle section, $S_b$ bottle section, $p_a$ absolute air pressure, $V$ bottle volume, $V_{w0}$ initial water volume.

- Eq. (2), (18): $\dfrac{dm_w}{dt} = -\rho_w v_{wn} S$
- Eq. (5): $v_w = v_b - v_{wr}$; eq. (6): $v_{wr} = v_{wn} S/S_b$
- Eq. (7): $F_D = 0.5\,\rho_{atm} C_D S_b v_b^2$
- Eq. (8): $F_M = \mu (m_b+m_a+m_w) g\cos\theta$ (ramp friction)
- Eq. (9): $W_x = (m_b+m_a+m_w) g\sin\theta$
- Eq. (15): $p_{a0}/\rho_{a0}^{\gamma} = p_a/\rho_a^{\gamma}$ (adiabatic)
- Eq. (16): $m_a = \rho_{a0}(V-V_{w0}) = \rho_a (V - V_w)$
- Eq. (19): $\dfrac{dv_b}{dt} = -\dfrac{F_D+F_M+W_x}{m_b+m_a} + \dfrac{1}{m_b+m_a}\left[S_b(p_a-p_{atm}) - \dfrac{(S_b-S)^2}{2S_b}\rho_w v_{wn}^2\right]$
- Eq. (20): $\dfrac{dv_{wn}}{dt} = \dfrac{S_b^2(p_a-p_{atm})}{S}\left(\dfrac{1}{m_w}+\dfrac{1}{m_b+m_a}\right) - \dfrac{v_{wn}^2\rho_w}{2S}\left[\dfrac{S_b^2-S^2}{m_w} + \dfrac{(S_b-S)^2}{m_b+m_a}\right] - \dfrac{S_b}{S(m_b+m_a)}(F_D+F_M+W_x)$
- Eq. (21): $\dfrac{dp_a}{dt} = \dfrac{-\gamma\, p_a^{(\gamma+1)/\gamma}}{(V-V_{w0})\,p_{a0}^{1/\gamma}}\, v_{wn} S$

Equations, air propulsion (section 4.2). $p_{an}$, $\rho_{an}$, $v_{an}$ at the nozzle. Compressible flow through a convergent nozzle, adiabatic expansion.

- Eq. (22): $\dfrac{dm_a}{dt} = V\dfrac{d\rho_a}{dt} = -\rho_{an} S v_{an}$
- Eq. (28): $v_{an}^2 = \dfrac{2\gamma}{\gamma-1}\dfrac{p_{a0}^{1/\gamma}}{\rho_0}\left(p_a^{(\gamma-1)/\gamma} - p_{an}^{(\gamma-1)/\gamma}\right)$
- Eq. (29), transcribed as printed: $\dfrac{dv_b}{dt} = \dfrac{S}{m_b+m_a+m_w}\dfrac{2\gamma}{\gamma-1}\left(p_a^{(\gamma-1)/\gamma} - p_{an}^{(\gamma-1)/\gamma}\right)p_{an}^{1/\gamma} - \dfrac{1}{m_b+m_a+m_w}(F_D+F_M+W_x)$
- Eq. (30): $\dfrac{dm_a}{dt} = -S p_{an}^{1/\gamma}\left[\dfrac{2\gamma}{\gamma-1}\dfrac{\rho_{a0}}{p_{a0}^{1/\gamma}}\left(p_a^{(\gamma-1)/\gamma} - p_{an}^{(\gamma-1)/\gamma}\right)\right]^{1/2}$
- Eq. (31): $\dfrac{dp_a}{dt} = -\dfrac{S}{V}\left(\dfrac{2\gamma}{\gamma-1}\right)^{1/2}\left(\dfrac{p_{a0}^{1/\gamma}}{\rho_0}\right)^{1/2} p_a^{(\gamma-1)/\gamma} p_{an}^{1/\gamma}\left(p_a^{(\gamma-1)/\gamma} - p_{an}^{(\gamma-1)/\gamma}\right)^{1/2}$
- Valid while $p_a \ge p_{atm}$.
- Open: the symbol $\rho_0$ in eqs. (27)-(31) is not defined in the text read; it may denote $\rho_{a0}$. Eq. (29) as printed lacks a visible $p_{a0}^{1/\gamma}/\rho_0$ factor that appears in eq. (28); not resolved.

Equations, ballistic flight (section 4.3), quadratic drag:

- Eq. (32): $\dfrac{dv_{bx}}{dt} = -\dfrac{\rho_{atm} C_D A}{2 m_b} v_{bx}\left(v_{bx}^2+v_{by}^2\right)^{1/2}$
- Eq. (33): $\dfrac{dv_{by}}{dt} = -g - \dfrac{\rho_{atm} C_D A}{2 m_b} v_{by}\left(v_{bx}^2+v_{by}^2\right)^{1/2}$

Assumptions stated:

- Water expulsion adiabatic, $dQ = 0$ (p. 1137).
- Air mass constant during the water stage (eq. 16).
- Water velocity in the bottle not equal to $v_b$: inertia of confined water retained (eqs. 5-6).
- Pressure of the water jet at the nozzle equals atmospheric pressure (p. 1137).
- During air propulsion, air velocity inside the rocket equals $v_b$ (p. 1138).

Numerical values (section 5, field tests):

- Bottle volume $V = 2$ l (carbonated-drink bottle).
- $m_b = 133.2 \pm 0.1$ g; $D = 106.0 \pm 0.1$ mm; nozzle $d = 21.5 \pm 0.1$ mm.
- $C_D = 0.36$, estimated from ref. [14] (= barrioperotti2009experimental). $C_D$ of similar bodies "typically between 0.2 and 0.4" (ref. [10], White).
- Water volume precision $\pm 5\times10^{-3}$ l (burette). Distance precision $\pm 0.1$ m. Manometer precision $\pm 0.1$ bar (relative pressure).
- Ambient: $1020 \pm 1$ mbar, $22 \pm 1$ °C.
- Ramp length 1.5-2 m; angle set to $\pm 1°$.
- Student field practice limited to 3 bar (p. 1133); model study limited to 5 bar (p. 1146).
- Figure 9: horizontal distance vs relative pressure $p_{r0}$ (1 to 3.5 bar), $V_{w0} = 0.5$ l, $\theta = 45°$. Model vs test differences below 6%.
- Figure 10: distance vs $V_{w0}$ (0 to 1 l), $p_{r0} = 2$ bar, $\theta = 45°$. Maximum distance at $V_{w0} = 0.5$-$0.6$ l. With $V_{w0} = 0$ (air only, 2 bar) the rocket reaches about 10 m. Differences below 6%.
- Figure 11: distance vs $\theta$, $V_{w0} = 0.5$ l, $p_{r0} = 2$ bar. Maximum near 40°. Differences below 4%.
- Figure 12 (model, $V_{w0} = 0.5$ l, $p_{r0} = 2$ bar, $\theta = 45°$): initial acceleration slightly above 70 g; $v_b \approx 26$ m/s after 60 ms; $p_a$ from 3 to 2 bar (absolute) during the water stage; $v_{wn}$ peaks slightly above 30 m/s; transient of about 40 ms; $S/S_b = 4\%$; $v_b = 26.7$ m/s at end of water stage, 30.7 m/s at end of air stage; initial air exit velocity 306 m/s (sonic, choked).
- Conclusions: air stage adds about 15% to rocket velocity in the reported tests (p. 1147).
- Optimum water volume (model, figure 13): about 0.6 l for $p_{r0} = 2$ bar. Figure 14: optimum $V_{w0}$ increases with $p_{r0}$ and lies between 0.5 and 0.6 l for 1-5 bar; optimum launch angle decreases from 40° to 30° at 5 bar.

## What the source does not support

- No direct measurement of thrust, internal pressure or trajectory vs time. Validation is by horizontal range only.
- No measured polytropic exponent. $\gamma$ is assumed; its numerical value is not stated in the pages read.
- Optimum fill is for horizontal range at a launch angle, not for vertical apogee.
- Ramp friction coefficient $\mu$: Open (value not stated in the pages read).
- Tables of the individual range measurements are not given; values are only in figures.

## Category

Peer-reviewed. Model plus field measurements (horizontal range vs pressure, water volume, angle).
