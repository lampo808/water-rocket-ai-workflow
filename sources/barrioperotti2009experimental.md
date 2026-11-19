# barrioperotti2009experimental

- Title: Experimental evaluation of the drag coefficient of water rockets by a simple free-fall test
- Authors: R. Barrio-Perotti, E. Blanco-Marigorta, K. Argüelles-Díaz, J. Fernández-Oro
- Year: 2009
- Venue: European Journal of Physics, 30(5), 1039-1048
- DOI: 10.1088/0143-0807/30/5/012
- URL: https://doi.org/10.1088/0143-0807/30/5/012
- Verification: verified (Crossref: title, first author, year, journal match), 2026-11-19
- Access: full text read, submitted manuscript (header "Submitted to: European Journal of Physics", 15 pp.), from the Universidad de Oviedo repository: https://portalinvestigacion.uniovi.es/documentos/5e89101a2999520e7008c2b0/f/65df8586087935365e53ad14.pdf ; repository record http://hdl.handle.net/10651/6609 (file labelled "Postprint"). Manuscript title writes "free fall" without hyphen. Differences from the published version: Open.
- PDF: not downloaded (repository licence CC BY-NC-ND 4.0, not in the allowed licence list; publisher copy is free to read, "bronze", no licence)

## What the source supports

- Eq. (1): $F_d = 0.5\, C_d \rho A v^2$
- Eq. (3): $m\dfrac{dv_y}{dt} = m g - V_b \rho g - 0.5\rho A C_d v_y^2 = m^* g - 0.5\rho A C_d v_y^2$, with $m^* = m - V_b\rho$ (buoyancy-corrected mass).
- Eq. (4): $\dfrac{d^2y}{dt^2} = k_1 g - k_2\left(\dfrac{dy}{dt}\right)^2$, $k_1 = m^*/m$, $k_2 = 0.5\rho A C_d/m$.
- Eq. (5): $y(t) = k_1' \ln[\cosh(k_2' t)]$ (analytic solution form; $k_1'$, $k_2'$ not defined further in the text).
- Eq. (6): global precision $e = \sqrt{\sum_i e_i^2} = 1.14\%$.

Assumptions:

- $C_d$ constant over $10^3 < Re < 2\cdot10^5$ (figure 1, section 4).
- Bodies did not reach terminal velocity; $C_d$ treated as constant because $Re$ stays in that range after 0.02 s.

Numerical values:

- Fall height $h = 14.360 \pm 0.002$ m (stairwell). Fall time from audio recording, precision $2\cdot10^{-4}$ s.
- Validation ball: $m^* = 68 \pm 1$ g, $D = 126.0 \pm 0.1$ mm; $t_F = 1.9539$ s; $C_d = 0.484$ vs typical sphere 0.47.
- Air at test: 1012 mbar, 15 °C; $\rho = 1.225 \pm 0.004$ kg m$^{-3}$; $\nu = (1.453 \pm 0.005)\cdot10^{-5}$ m$^2$ s$^{-1}$.
- Water rocket (2 l soft-drink bottle, empty): $m^* = 133 \pm 1$ g, $D = 106.0 \pm 0.1$ mm, 10 drops, mean $t_F = 1.7842$ s.
- Result: $C_d = 0.345 \pm 0.004$ for $10^3 < Re < 2\cdot10^5$ (section 5, conclusions). Reference area: frontal area from maximum diameter $D$.
- Comparison: ellipsoid $L/D = 1.5$ has $C_d = 0.37$ (figure 8).
- Fall time differs by 6% from drag-free fall for the rocket, 15% for the ball (section 4).
- Terminal velocity of the rocket would need $h > 36$ m.
- Sensitivity: 0.01 s error in $t_F$ changes $C_d$ by about 17%; $h$ and $t_F$ need 0.6% and 0.3% precision for 10% in $C_d$ (section 5).

## What the source does not support

- No powered flight; only free fall of an empty rocket, nose down (figure 2 sketch). Orientation during fall: Open.
- No $C_d$ above $Re = 2\cdot10^5$. No wind-tunnel data.
- The quoted uncertainty $\pm 0.004$ is a propagated measurement precision; it does not include model error (constant $C_d$ assumption).
- Rocket geometry (fins, nose) not specified beyond figure 8 sketch.

## Category

Peer-reviewed. Measurement (drag coefficient of one water rocket by free fall).
