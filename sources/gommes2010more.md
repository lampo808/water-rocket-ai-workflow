# gommes2010more

- Title: A more thorough analysis of water rockets: Moist adiabats, transient flows, and inertial forces in a soda bottle
- Authors: Cedric J. Gommes
- Year: 2010
- Venue: American Journal of Physics, 78(3), 236-243
- DOI: 10.1119/1.3257702
- URL: https://doi.org/10.1119/1.3257702
- Verification: verified (Crossref: title, author, year, journal match), 2026-11-19
- Access: full text read, publisher PDF deposited in ORBi (University of Liège): https://orbi.uliege.be/handle/2268/36471
- PDF: not downloaded (OpenAlex: "bronze" at publisher, "other-oa" at ORBi; ORBi states a repository user licence, no CC licence found)

## What the source supports

Air expansion (section II A):

- Eq. (1): $\delta_h^2 \approx \chi\tau$. With $\chi = 0.014$ cm$^2$/s and $\tau = 0.1$ s, $\delta_h = 0.04$ cm, much smaller than the bottle radius. Conclusion: expansion is adiabatic.
- Adiabatic is not $PV^\gamma$ = const for moist air: condensation of water vapour releases heat.
- Eq. (5), entropy conservation of dry air + vapour + liquid:
  $\left[1-\dfrac{P_V(T_i)}{P_i}\right]c_V \ln\!\left(\dfrac{T}{T_i}\left(\dfrac{V}{V_i}\right)^{\gamma-1}\right) + \dfrac{T_i}{T}\dfrac{V}{V_i}\dfrac{P_V(T)}{P_i}\dfrac{\Delta h_V}{T} + \dfrac{P_V(T_i)}{P_i}\left(c_P^l\ln\dfrac{T}{T_i} - \dfrac{\Delta h_V}{T_i}\right) = 0$
- Eq. (6), empirical fit of the polytropic exponent of moist adiabats: $\beta = 1.15 + (1.4-1.15)\exp\!\left(-36\,\dfrac{P_V(T_i)}{P_i}\right)$. Reduces to 1.4 for dry air.
- Constants used: $c_V = 20$ J/(mol K), $c_P^l = 75.3$ J/(mol K), $\Delta h_V = 45\,051$ J/mol, $\gamma = 1.4$; $P_V$ from Clausius-Clapeyron with $P_V = 1$ bar at 100 °C.
- Figure 4: air at 3 bar saturated at 70 °C does 20% more work than dry air when doubling its volume.
- For the Kagan et al. launches ($P_i = 3.4$ and 6.8 bar, $T_i = 25$ °C): $\beta = 1.31$ and 1.35; extra work "only a few percent".

Water ejection (section II B):

- Eq. (7): $\delta_\nu^2 \approx \nu\tau$; $\nu = 0.01$ cm$^2$/s, $\tau = 0.1$ s gives $\delta_\nu = 0.3$ mm. Water treated as inviscid.
- Eq. (9), unsteady Bernoulli along the axis: $\displaystyle\int_0^h \frac{\partial u_c}{\partial t}dz + \frac{u_c^2(h)-u_c^2(0)}{2} + \frac{P-P_a}{\rho} + g h = 0$, with $g$ including the non-inertial contribution.
- The unsteady term is of the same order as the others ($P-P_a = 10^5$ Pa, $H = 0.1$ m, apparent $g = 1000$ m/s$^2$): steady Bernoulli cannot be assumed a priori.
- Eq. (11): $\dfrac{dV}{dt} = -\langle f\rangle\,\Omega(h)\dfrac{dh}{dt}$
- Eq. (12): $I(h)\dfrac{d}{dt}\!\left(\Omega(h)\dfrac{dh}{dt}\right) + \dfrac12\left(1-\left(\dfrac{\Omega(h)}{\Omega_0}\right)^2\right)\left(\dfrac{dh}{dt}\right)^2 + \dfrac1\rho\left(P_i\left(\dfrac{V_i}{V(t)}\right)^\beta - P_a\right) + g h = 0$
- Eq. (13): $I(h) = \displaystyle\int_0^h \frac{dz}{\Omega(z)}$

Rocket momentum (section II C):

- Eq. (14): $\dfrac{d}{dt}MU = \mathrm{Th} - W - D$
- Eq. (16): $MU = [m+\rho V_w]\dfrac{dZ}{dt} + \rho\langle f\rangle h\,\Omega(h)\dfrac{dh}{dt}$ (second term: water moves slower than the rocket).
- Eq. (17): $\mathrm{Th} = \rho\dfrac{\Omega(h)^2}{\Omega_0}\left(\dfrac{dh}{dt}\right)^2\langle f^2\rangle + \rho\,\Omega(h)\dfrac{dh}{dt}\dfrac{dZ}{dt}\langle f\rangle$
- Eq. (18): $W = (m+\rho V_w)g_0$
- Eq. (19): $D = C_A\,\Omega_{max}\dfrac{\rho_a}{2}\left(\dfrac{dZ}{dt}\right)^2$; "$C_A$ is about 0.75" for a circular cross-section without wings (citing Landau-Lifshitz); order 1 is sufficient for the analysis.
- Eq. (24), maximum ejection rate: $\dfrac{dh}{dt} \approx -\dfrac{\sqrt{2\Delta P/\rho}}{\Omega/\Omega_0 - 1}$. Initial acceleration $d^2Z/dt^2 \approx \Omega\Delta P/m$.
- Appendix A: $\Gamma_0 = 0.02$ for $H = 0.2$ m and $\rho_a/\rho = 0.001$: gravity and drag negligible during water ejection.

Observations cited from other work:

- Kagan et al. (kagan1995soda): 2 l soda bottle, high-speed camera; measured acceleration 100 g; ejection time 0.1 s.
- Finney (finney2000analysis): isothermal model predicts time of flight within 0.2 s.

Results: model curves (figure 6) still underpredict the measured height vs time of Kagan et al. at $P_i = 3.4$ and 6.8 bar. The author states a discrepancy persists that is larger than the experimental uncertainty (section IV).

## What the source does not support

- No new measurements. Experimental data are those of Kagan et al. (figure 6).
- No air-only thrust phase after water exhaustion.
- No ballistic phase or apogee prediction beyond the thrust phase.
- No optimal fill fraction.
- Whether $P_i$ values are absolute or gauge: Open (not stated in the passages read).

## Category

Peer-reviewed. Model only; compares with published measurements.
