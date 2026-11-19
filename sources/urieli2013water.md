# urieli2013water

- Title: Water Rocket Analysis (Page 2) and Water Rocket Analysis (Page 3), part of "Engineering Thermodynamics"
- Authors: Israel Urieli
- Year: 2013 (page 2 "Updated 3/18/2013"; page 3 "Updated 6/21/09"; page 1 "Updated 3/18/2013")
- Venue: lecture notes web site "Engineering Thermodynamics", hosted at people.ohio.edu. Institution not stated on the pages; Ohio University inferred from the domain (own inference).
- DOI: none
- URL: https://people.ohio.edu/urieli/thermo/property_tables/gas/adiabatic/rocket/analysis2.html ; https://people.ohio.edu/urieli/thermo/property_tables/gas/adiabatic/rocket/analysis3.html ; page 1: https://people.ohio.edu/urieli/thermo/property_tables/gas/adiabatic/rocket/rocket.html
- Verification: verified (pages load; title and author I. Urieli match), 2026-11-19
- Access: page read (equations are GIF images; read from the images)
- PDF: not downloaded (HTML pages, no PDF; licence CC BY-NC-SA 3.0 US stated on the pages)

## What the source supports

Equations (numbers as on the pages):

- Eq. (2): $F_{thrust} = \dot m\,u_{ex} = \rho_w A_N u_{ex}^2$
- Eq. (3): $\dfrac{P-P_a}{\rho_w} = \dfrac{u_{ex}^2}{2}$ (Bernoulli, no term for the velocity of the free surface)
- Eq. (4): $F_{thrust} = 2(P-P_a)A_N$
- Eq. (5): $P = P_0\left(\dfrac{V_0}{V}\right)^k$ (adiabatic, $k = 1.4$ for air)
- Eq. (7) (page text numbers it 6 and 7 inconsistently): $\dfrac{dV}{dt} = A_N\sqrt{\dfrac{2\left[P_0(V_0/V)^k - P_a\right]}{\rho_w}}$
- Eq. (8): $m = M_s + \rho_w(V_{total} - V)$ (compressed-air mass ignored)
- Eq. (9): $F_{drag} = \tfrac12\rho_{air}C_d A_{bottle}\,u|u|$
- Eq. (10): $\dfrac{du}{dt} = a = \dfrac{F_{thrust} - F_{drag}}{m} - g$
- Projectile phase after water is exhausted: $F_{thrust} = 0$, $m = M_s$ (page 3).

Assumptions stated: adiabatic expansion; $P$ varies non-linearly with $V$; equations valid while water is expelled; $P_0$ is the initial absolute pressure.

Numerical values: $k = 1.4$; $\rho_{air} = 1.2$ kg/m$^3$; $\rho_w = 1000$ kg/m$^3$; $g = 9.81$ m/s$^2$. Default rocket parameters are in a linked document (Nielsen_Rocket.pdf) that was not read: Open.

## What the source does not support

- No air-only thrust: the model sets thrust to zero when water is exhausted.
- No values of $C_d$, nozzle area, bottle volume or initial pressure on the pages read.
- No measurements.
- No unsteady flow or water inertia in the bottle.

## Category

Lecture notes. Model only.
