# qi2026research

- Title: Research method on the relationship between water bottle rocket acceleration and key parameters based on elastic force
- Authors: Ligeer Qi, Boyu Liu, Yibo Du
- Year: 2026
- Venue: Journal of Physics: Conference Series, 3213(1), 012051 (ICMMAP-2025)
- DOI: 10.1088/1742-6596/3213/1/012051
- URL: https://doi.org/10.1088/1742-6596/3213/1/012051
- Verification: verified (Crossref: title, first author, year, journal match), 2026-11-19
- Access: full text read
- PDF: sources/pdf/qi2026research.pdf (licence: CC BY 4.0, per Crossref, OpenAlex and the article footer)

## What the source supports

Setup (sections 2-3): 500 mL bottle, vertical (90°), tied by zip ties to a pointer spring dynamometer under the launcher; rocket held stationary. Peak force read from video of the dynamometer (low-resolution camera). Four repeats per setting.

Equations as printed:

- Eq. (1): $m = m_0 + \rho S_2 l$; eq. (2): $V = (l_0 - l)S_2$
- Eq. (3): $F_1 = -mg - F_2$; eq. (4): $F_1 = -v_1\,dm/dt$
- Eq. (6): $a = -F_2/m$
- Eq. (7): $v_1 S_1 = v_2 S_2$; eq. (8): $v_2 = dl/dt$
- Eq. (9): $pV^\gamma = p_iV_i^\gamma = C_0$ (adiabatic)
- Eq. (10): $m\,dv/dt = -mg - F_r$, $F_r = 0.5\,C_r\rho_0 S_2 v^2$ (coast phase, theory only)

Table 1 parameters: $m_0 = 0.15$ kg (empty rocket plus counterweight); bottle length $l_0 = 19.0$ cm; nozzle $d_1 = 1.0$ cm; bottle diameter $d_2 = 6.0$ cm; $P_0 = 101$ kPa; $\gamma = 1.4$; $\rho_0 = 1.23$ kg/m$^3$; $\rho = 1000$ kg/m$^3$; $g = 9.8$ m/s$^2$.

Ranges (Table 2): water 50-300 mL in 50 mL steps; pressure 200-600 kPa in 100 kPa steps.

Table 3, mean maximum net force (N); rows water volume (mL), columns pressure (kPa):

| water \ p | 200 | 300 | 400 | 500 | 600 |
|---|---|---|---|---|---|
| 50 | 36.04 | - | - | - | - |
| 100 | 33.32 | 47.54 | 62.50 | 76.44 | 92.50 |
| 150 | 30.26 | 44.58 | 59.26 | 73.82 | 88.28 |
| 200 | 26.56 | 41.60 | 55.54 | 69.54 | 83.54 |
| 250 | 24.58 | 38.58 | 52.34 | 65.40 | 79.06 |
| 300 | 21.40 | 35.42 | 48.60 | 61.72 | 70.42 (leak) |

Raw data of the four repeats: Appendix A, Tables A1-A4.

Derived "maximum acceleration": Table 4 (500 kPa; 100-300 mL: 305.76, 246.07, 198.69, 163.50, 137.16 m/s$^2$), fit $a = 9114\,V^{-0.7288}$, $R^2 = 0.9825$. Table 5 (100 mL; 200-600 kPa: 133.28, 190.16, 250.00, 305.76, 370.00 m/s$^2$), fit $a = 0.589P + 14.22$, $R^2 = 0.9995$.

Observations reported (section 4.2): at 50 mL water disperses as mist and thrust is mainly from air; above 300 mL a "water hammer effect" at the end of drainage; above 600 kPa nozzle seal failure; leak causes 2-5% pressure drop; pre-test pressure drop < 3% in 5 min. Section 5: 0.5 cm nozzle gave the largest acceleration of 0.5, 1.0, 1.5 cm (no data table).

## What the source does not support

- Whether pressures are gauge or absolute: Open (not stated).
- No time-resolved thrust curve; only peak force from a pointer dynamometer whose dynamic response is not characterized.
- "Acceleration" is not measured. Own inference: Table 4 and 5 values equal Table 3 force divided by initial mass ($m_0$ + water mass), e.g. $76.44/0.25 = 305.76$. They are not accelerations of a free rocket.
- No apogee, no drag measurement, no optimal fill for flight.

Quality concerns (own assessment, for the main session):

- The last paragraph of section 1 reproduces the abstract of gommes2010more almost word for word without citing it.
- Table 4 caption reads "atmospheric pressure fixed at 500 kPa"; it means the launch pressure.
- Section 5 refers to "maximum horizontal rocket acceleration" for a vertical, tethered setup.
- Sign convention of eqs. (3)-(6) is not consistent with $F = -F_2$ as written.
- Conference proceedings; peer review depth unknown.

## Category

Peer-reviewed conference proceedings (depth of review unknown). Static measurements of peak tether force vs water volume and pressure. Use with the quality concerns above.
