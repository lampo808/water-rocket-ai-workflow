# Source audit

- Audited: docs/physics.md (docs/README.md holds no claims), against sources/ as of 2026-11-19
- Files opened:
  - `.claude/agents/source-auditor.md` (own instructions)
  - `docs/physics.md`, `docs/README.md`
  - `sources/README.md`, `sources/references.bib`
  - Notes: `sources/barrioperotti2010theoretical.md`, `barrioperotti2009experimental.md`, `gommes2010more.md`, `romanelli2013air.md`, `fischer2020approximation.md`, `urieli2013water.md`, `ding2025dynamics.md`. Access lines only (Grep) of `thorncroft2009hydrodynamics.md`, `watanabe2003thrust.md`, `qi2026research.md`, `kagan1995soda.md`, `prusa2000hydrodynamics.md`, `finney2000analysis.md`, `nasa2023flight.md`.
  - `sources/pdf/ding2025dynamics.pdf` (pp. 1-10)
  - Full texts fetched from the web and read as downloaded copies: Barrio-Perotti 2010, publisher PDF (iypt.ru copy, all 17 pp.); Barrio-Perotti 2009, submitted manuscript (Universidad de Oviedo repository, 15 pp.); Gommes 2010, publisher PDF (ORBi, 8 pp.); Romanelli arXiv:1211.1923v1 (5 pp.); Fischer arXiv:2001.08828v2 (pp. 1-18); Urieli pages 2 and 3 (HTML) and equation images `bern2_eqn.gif` (eq. 3) and `dudt1_eqn.gif` (eq. 10).
  - Metadata: Crossref API for 6 DOIs, DataCite API for the arXiv DOI.
  - No restricted file was opened. `CLAUDE.md` and `AGENTS.md` were loaded into context by the harness.

## Summary

31 attributed claims: 24 supported, 6 partly supported, 1 not supported, 0 cannot check. 3 uncited claims need a citation. All 8 references checked resolve and match title, first author and year.

Main problems:

1. Eq. (W2) has numerator $2p$ with $p$ absolute (physics.md:44-45). Fischer eq. 7, Urieli eq. 3 and Ding eq. 10, cited as using "the same relation", all have the pressure difference $p - p_a$. Ding also uses the two-phase density $\rho_{mix}$, not $\rho_w$.
2. $C_D = 0.345$ is presented as measured "on the same rocket" as Barrio-Perotti 2010. Neither paper states that the rocket is the same. Barrio-Perotti 2010 (p. 1141) used $C_D = 0.36$ for its rocket, not 0.345.
3. The Gommes section II B claim misstates the order-of-magnitude argument. Gommes compares the unsteady term with the kinetic term, and the pressure term with the gravity term.
4. physics.md:227-228 says the launch conditions of the Kagan 100 g measurement are not in the note. The note and Gommes give the Kagan launch pressures (3.4 and 6.8 bar). What neither states is which launch produced 100 g.

## Attributed claims

| # | Location | Claim | Cited | Status | Evidence |
|---|---|---|---|---|---|
| 1 | physics.md:21-33 | $V_b$ = 2 L, $m_b$ = 133.2 g, $D$ = 106.0 mm, $d$ = 21.5 mm, $p_a$ = 1020 mbar, $T_a$ = 22 °C, measured by the authors | Barrio-Perotti 2010, sec. 5 | supported | p. 1141: "V = 2 l"; $m_b = 133.2 \pm 0.1$ g; $D = 106.0 \pm 0.1$ mm; $d = 21.5 \pm 0.1$ mm; "1020 ± 1 mbar and 22 ± 1 °C". |
| 2 | physics.md:23, :31, :304 | $C_D$ = 0.345, reference area $\pi D^2/4$ | Barrio-Perotti 2009 | supported | Manuscript p. 10: "$C_d$=0.345"; p. 14, eq. 6: "$C_d$=0.345 ±0.004". p. 5: $A$ is the frontal area. p. 6: $A$ is obtained from the cross-sectional diameter $D$. |
| 3 | physics.md:22-23 | $C_D$ measured "on the same rocket" as Barrio-Perotti 2010 | Barrio-Perotti 2009 | partly supported | The 2009 rocket has $m^* = 133 \pm 1$ g and $D = 106.0$ mm and was "borrowed from one of our students" (p. 10). These values are consistent with the 2010 rocket, but neither paper states that it is the same rocket. Barrio-Perotti 2010 p. 1141: "Based on previous experiences [14], the drag coefficient of this particular water rocket was estimated to be $C_D$ = 0.36". The 2010 model used 0.36, not 0.345. |
| 4 | physics.md:52-54, (D1) | $F_D = \tfrac12\rho_a C_D A_b v\,\mathrm{abs}(v)$ | Barrio-Perotti 2009, eq. 1 | supported | Eq. 1: $F_d = 0.5 C_d \rho A v^2$ (magnitude form). The signed $v\,\mathrm{abs}(v)$ form is the document's convention. |
| 5 | physics.md:60-63 | $\tau \approx 0.1$ s, $\delta_h \approx \sqrt{\chi\tau} \approx 0.4$ mm, small compared with the bottle radius | Gommes 2010, eq. 1 | supported | p. 237, eq. 1: $\chi$ = 0.014 cm²/s and $\tau$ = 0.1 s give $\delta_h$ = 0.04 cm, "much smaller than the radius of the rocket". |
| 6 | physics.md:68-70 | Condensation of vapour releases heat and lowers the effective exponent | Gommes 2010 (same paragraph) | supported | p. 237: condensation is exothermic and keeps the pressure above $PV^\gamma$. p. 238: moist adiabats are approximated by $PV^\beta$ with $\beta < \gamma$. |
| 7 | physics.md:71-72 | $\beta = 1.15 + 0.25\exp(-36 P_V/P_i)$ | Gommes 2010, eq. 6 | supported | p. 238, eq. 6: $\beta = 1.15 + (1.4-1.15)\exp(-36 P_V(T_i)/P_i)$. |
| 8 | physics.md:72-74 | Measured $\beta$ = 1.17 to 1.22 in a stationary bottle | Romanelli 2013, Table I | supported | arXiv v1, p. 4, Table I: $\beta$ = 1.22, 1.21, 1.20, 1.19, 1.17. Stationary bottle: sec. III, Fig. 2. Read in the arXiv v1. Table numbering in the AJP version not verified. |
| 9 | physics.md:74-75 | Measured values are 0.05 to 0.06 below $\beta^*$ in every row | Romanelli 2013, Table I | supported | Table I, $\beta^*$ = 1.27, 1.26, 1.25, 1.24, 1.23. The differences are 0.05, 0.05, 0.05, 0.05 and 0.06. |
| 10 | physics.md:75 | Label "(contested)" for the Romanelli values | Romanelli 2013 | partly supported | The offset is in the data. The authors call the agreement "very good" (p. 4, sec. III) and say the expression "agrees reasonably" (p. 4, sec. IV). The source does not present it as a disagreement. The "contested" reading is the document's own inference and should be labelled as such. |
| 11 | physics.md:86-91, (W2) | $u_e = \sqrt{2p/(\rho_w[1-(A_n/A_b)^2])}$. The same relation, with or without the correction, is used by Fischer eq. 7, Urieli eq. 3 and Ding eq. 10 | Fischer 2020 eq. 7; Urieli 2013 eq. 3; Ding 2025 eq. 10 | not supported | Fischer p. 5, eq. 7: $v_e = \sqrt{2(p(V)-p_a)/\rho}$; the area correction $1/\sqrt{1-(r/R)^4}$ is unnumbered on p. 5. Urieli page 2, eq. 3: $(P-P_a)/\rho_w = u_{ex}^2/2$. Ding p. 6, eq. 10: $v_e = \sqrt{2(P_i-P_e)/(\rho_{mix}[1-(A_e/A_i)^2])}$. All three use a pressure difference. (W2) has $2p$, and physics.md:44-45 states that pressures are absolute. Ding also uses $\rho_{mix}$ (eq. 2), not $\rho_w$. |
| 12 | physics.md:111-113, (W6) | $m\,dv/dt = F_T - F_D - mg$ | Fischer 2020 eq. 10; Urieli 2013 eq. 10 | supported | Fischer p. 6, eq. 10: $a = [2A(p-p_a) - Dv^2]/(M+m_{air}+\rho(V_b-V)) - g$. Urieli page 3 (analysis3.html), eq. 10: $du/dt = a = (F_{thrust}-F_{drag})/m - g$. |
| 13 | physics.md:140-143 | Air phase: quasi-steady isentropic nozzle flow, bottle state taken as the stagnation state; "the same approach as Barrio-Perotti 2010, section 4.2" | Barrio-Perotti 2010, sec. 4.2 | partly supported | Sec. 4.2 (pp. 1138-1140) uses adiabatic expansion and "compressible flow through a convergent nozzle" (p. 1139, eqs. 26-31). Choking is mentioned only in sec. 6 (p. 1144: initial 306 m/s, sonic). The paper does not write explicit choked-flow relations like (A3)-(A4) or a pressure-thrust term like (A7). It keeps unsteady energy terms ($m_a\,du_a/dt$, eqs. 25-26), and "quasi-steady" is not stated. |
| 14 | physics.md:178-180, (B2) | $h_c = \frac{1}{2\psi}\ln(1+\psi v_1^2/g)$, $\psi = \rho_a C_D A_b/(2m_1)$ | Fischer 2020, eq. 35 | supported | p. 16, eq. 35. $\psi$ is defined in eq. 32 (p. 15) with the empty mass $M$. The document uses $m_1$, which includes the residual air and water. |
| 15 | physics.md:215-217 | Barrio-Perotti 2010 fig. 12: same rocket, same water volume and pressure, 45° ramp | Barrio-Perotti 2010, fig. 12 | supported | p. 1143, fig. 12 caption: $V_{w0}$ = 0.5 l, $p_{r0}$ = 2 bar, $\theta$ = 45°. |
| 16 | physics.md:219 | Pressure during the water phase falls from 3 to 2 bar absolute | Barrio-Perotti 2010, fig. 12 | supported | pp. 1143-1144: "The absolute pressure $p_a$ decreases gradually from 3 to 2 bar". |
| 17 | physics.md:220-221 | 26.7 m/s at the end of the water phase, 30.7 m/s at the end of the air phase | Barrio-Perotti 2010, fig. 12 | supported | p. 1144: "a velocity of 26.7 m s⁻¹" and "reach 30.7 m s⁻¹ at the end of the stage". |
| 18 | physics.md:222 | Air phase gain about 15 % | Barrio-Perotti 2010 | supported | p. 1147, conclusions: "an increment in the velocity of the rocket of about 15% was observed". |
| 19 | physics.md:223 | Initial acceleration slightly above 70 $g$ | Barrio-Perotti 2010, fig. 12 | supported | p. 1143: "The initial acceleration a is very high (slightly above 70 g)". |
| 20 | physics.md:224-225 | Their model keeps the inertia of the water in the bottle (eqs. 5, 6, 19, 20) | Barrio-Perotti 2010 | supported | Eqs. 5-6 (p. 1136) and 19-20 (p. 1138). The p. 1144 discussion and the p. 1146 conclusions name the inertial effects of the water. |
| 21 | physics.md:225-226 | Kagan et al. measured about 100 $g$ on a 2 L bottle, as reported by Gommes | Gommes 2010 (secondary citation of Kagan 1995) | supported | Gommes p. 236: "A more accurate measurement² with a high-speed camera leads to an acceleration of 100g's". p. 240: "These authors used a 2-l soda bottle". |
| 22 | physics.md:226-228 | "Launch conditions of that measurement are not in the note" | `sources/gommes2010more.md` | partly supported | The note (line 24) gives the Kagan launches: $P_i$ = 3.4 and 6.8 bar, $T_i$ = 25 °C. Gommes gives the same values on p. 238 and in fig. 6 (p. 240). Neither states which launch gave 100 $g$, and whether $P_i$ is gauge or absolute is not stated. The sentence should say that. |
| 23 | physics.md:267-268 | Measured maximum range at 0.5 to 0.6 L, 2 bar gauge, 45° ramp | Barrio-Perotti 2010, fig. 10 | supported | p. 1141: "until $V_{w0}$ = 0.5 − 0.6 l (where maximum distances are reached)"; $p_{r0} = p_{a0} - p_{atm}$ = 2 bar, $\theta$ = 45°. Fig. 10 shows both test and model points. |
| 24 | physics.md:269-270 | Model optimum 0.5 to 0.6 L for 1 to 5 bar | Barrio-Perotti 2010, fig. 14 | supported | p. 1146: the optimum volume "lies between 0.5 and 0.6 l" for the pressure interval considered (1 to 5 bar, fig. 14). |
| 25 | physics.md:273-275 | Simulated optimum water volume ratio 0.498 for a 2.13 L rocket, 0.75 MPa, 1 cm nozzle | Ding 2025 | supported | p. 9: "the initial water volume is about 0.498 of the internal total volume". Table 5 (p. 5): 2.13 L, 0.75 MPa, 1 cm. The abstract rounds the value to 0.50. Gauge or absolute pressure is not stated in Ding. |
| 26 | physics.md:275-276 | Ding's dry mass and drag coefficient are not stated | Ding 2025 | supported | Table 1 (p. 2) defines $M_k$ and $C_d$. Tables 4-8 give no values. The 0.55 kg on p. 8 belongs to the ref. [8] validation case only. |
| 27 | physics.md:281-284 | Gommes estimates the unsteady term and the inertial head to be of the same order as the pressure term at the start of the thrust | Gommes 2010, sec. II B | partly supported | p. 239: the unsteady term $HU/\tau$ "is equal to the magnitude of the second term $U^2$". For the "last two terms" (pressure and apparent-gravity head, with $P-P_a = 10^5$ Pa and $g$ = 1000 m/s²) "they are found to be comparable". The inertial head ~ pressure part is supported. The paper does not compare the unsteady term with the pressure term. Own inference: with Gommes' values the unsteady term is about 1 m²/s² and the pressure term about 100 m²/s². The estimate uses $\tau$ = 0.1 s for the whole ejection, not specifically the start of the thrust. |
| 28 | physics.md:284-286 | Barrio-Perotti keep the inertia of the confined water and obtain about twice this model's initial acceleration | Barrio-Perotti 2010 | supported | Source value: slightly above 70 $g$ (p. 1143). The factor 2 is a comparison with the document's own 34 $g$. |
| 29 | physics.md:288-290 | Measured exponents come from a stationary bottle with ejection time 0.64 to 0.88 s | Romanelli 2013 | supported | arXiv v1, p. 4: "The ejection of water from the bottle lasted between 0.64 s to 0.88 s"; Table I, column $t$. |
| 30 | physics.md:304-305 | $C_D$ = 0.345 measured for $10^3 < Re < 2\times10^5$ on the empty rocket | Barrio-Perotti 2009 | supported | p. 14: "$C_d$=0.345 ±0.004 for values of the Reynolds number above $10^3$ and below $2\cdot10^5$". The text does not say "empty". $m^*$ = 133 g (p. 10) matches the empty mass. |
| 31 | physics.md:305-306 | The rocket fell nose down | Barrio-Perotti 2009 | partly supported | The text does not state the orientation. Fig. 2 (p. 7) sketches the bottle base down, and p. 6 measures $h$ "from the base of the bottle to the ground". Nose down is inferred from these, not stated. |

## Uncited claims that need a citation

| # | Location | Claim | Why a citation is needed |
|---|---|---|---|
| 1 | physics.md:295-296 | "A two-phase mixture leaves the nozzle at the transition in a real launch" | This is an observation about real launches. Available support: Romanelli arXiv v1 p. 1 (fog ejection after the water), Fischer p. 4 (mixture of water and air expelled), Ding p. 3 (gas-liquid mixed jet). Thorncroft 2009 reports two-phase flow, checked against note only (abstract). |
| 2 | physics.md:310-311 | "No source read in full gives thrust versus time for a flying rocket" | Claim about the literature. It should name the sources checked. It should also state that thrust-stand measurements exist but were not read in full: thorncroft2009hydrodynamics and watanabe2003thrust (checked against note only, abstract access). |
| 3 | physics.md:293 | Discharge coefficient 1 | A parameter value. It is labelled as an assumption, but no source gives a measured discharge coefficient for a PET nozzle to bound its effect. Either cite a value or state that it is an idealization with no source value. |

## Mismatched citations

1. physics.md:86-91, (W2). The cited equations (Fischer eq. 7, Urieli eq. 3, Ding eq. 10) use $p - p_a$, but (W2) prints $2p$ with $p$ absolute. Ding eq. 10 also uses $\rho_{mix}$, not $\rho_w$. As written, the citation does not support the equation.
2. physics.md:22-23 and :31. "Measured on the same rocket" is not stated by either Barrio-Perotti paper. Barrio-Perotti 2010 used $C_D$ = 0.36 (p. 1141), not 0.345. The document should report both values, or attribute 0.345 to the 2009 rocket only.
3. physics.md:281-284. Gommes sec. II B is cited for a comparison it does not make: unsteady term versus pressure term. See row 27.
4. physics.md:226-228. The sentence about the note is inaccurate. The note and Gommes give the Kagan launch pressures; what is missing is which launch produced 100 $g$.
5. physics.md:113 and the References entry for Urieli (physics.md:340-342). Urieli eq. 10 is on page 3 (`analysis3.html`, updated 2009-06-21). The reference lists only the page 2 URL. `references.bib` names pages 2 and 3 in the title but gives only the page 2 URL.
6. physics.md:225-226. Kagan et al. is cited through Gommes, but `kagan1995soda` is not in the References list of physics.md. Either add it, marked "as cited in Gommes 2010", or keep the secondary citation explicit. Kagan full text was not read (note: metadata only).
7. physics.md:73, :290, :337-339. Romanelli is cited as AJP 2013, but the version read is the arXiv v1 preprint (2012). Table I and the ejection times are verified in v1 only. The document states this in its References entry. Equivalence with the AJP version is not verified.
8. physics.md:142-143. "The same approach as Barrio-Perotti 2010, section 4.2" overstates the match. See row 13.

## Reference resolution

| Key | DOI or URL | Resolves | Matches title / author / year |
|---|---|---|---|
| barrioperotti2009experimental | 10.1088/0143-0807/30/5/012 | yes (Crossref) | yes: "Experimental evaluation of the drag coefficient of water rockets by a simple free-fall test", Barrio-Perotti R., 2009, Eur. J. Phys. 30, 1039-1048 |
| barrioperotti2010theoretical | 10.1088/0143-0807/31/5/015 | yes (Crossref) | yes: "Theoretical and experimental analysis of the physics of water rockets", Barrio-Perotti R., 2010, Eur. J. Phys. 31, 1131-1147 |
| ding2025dynamics | 10.1016/j.rinp.2025.108420 | yes (Crossref) | yes: "Dynamics model and simulation optimization analysis of single stage water rocket", Ding Shaozhe, 2025, Results Phys. 76, 108420 |
| fischer2020approximation | 10.48550/arXiv.2001.08828 | yes (DataCite) | yes: "On the approximation of D.I.Y. water rocket dynamics including air drag", Fischer Laura, 2020. Journal version (IJSRMSS 6 (2019)) not verified, as stated in the bib note. |
| gommes2010more | 10.1119/1.3257702 | yes (Crossref) | yes: title as cited, Gommes Cedric J., 2010, Am. J. Phys. 78, 236-243 |
| romanelli2013air | 10.1119/1.4811116 | yes (Crossref) | yes: "Air expansion in a water rocket", Romanelli Alejandro, 2013, Am. J. Phys. 81, 762-766 |
| urieli2013water | https://people.ohio.edu/urieli/thermo/property_tables/gas/adiabatic/rocket/analysis2.html | yes | yes: "Water Rocket Analysis (Page 2)", I. Urieli, updated 3/18/2013. Page 3 (eq. 10) is at analysis3.html, updated 6/21/09, and is not in the cited URL. |
| kagan1995soda (secondary, via Gommes) | 10.1119/1.2344175 | yes (Crossref) | yes: "Soda-bottle water rockets", Kagan David, 1995, Phys. Teach. 33, 150-157 |
