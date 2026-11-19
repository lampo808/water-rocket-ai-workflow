# live.md

New session, any harness: read `AGENTS.md`, then `journal/history.md`,
then continue from `Resume` below. Answer lines start with `R:`.

## Current task

Resume:
- Phase: 1 (literature). Repository `water-rocket-ai-workflow`, branch `main`.
- State: phase 0 closed, tag `phase-0-setup`. Phase 1 output committed
  in `sources/`; review answers of round 1 archived.
- Done: 14 notes, `sources/references.bib` (14 entries), 2 PDFs
  (`qi2026research`, `ding2025dynamics`). DOIs checked against Crossref.
- Waiting for the user: Q1 (phase-1 review).
- Next step after `R: ok`: commit `journal: compact phase 1`, tag
  `phase-1-literature`, start phase 2 (physics in the main session).

## Open questions

**Q1. Phase 1 review.** 14 sources in `sources/` (13 from lit-scout,
`ding2025dynamics` written by the main session), 2 PDFs. Check the notes,
in particular `sources/ding2025dynamics.md` (problems listed at its end).
If it is fine, I compact the phase-1 journal entries, tag
`phase-1-literature` and start phase 2. Proposal: write `R: ok` or list
the corrections.
R: ok, proceed

## Working notes

- Talk: 2026-11-23. All phases 0 to 6 before the talk.

### lit-scout output

| key | category | access | PDF |
|---|---|---|---|
| barrioperotti2010theoretical | EJP; model + range measurements | full text (third-party copy) | no (closed; repo copy CC BY-NC-ND) |
| barrioperotti2009experimental | EJP; drag measurement | full text (submitted manuscript) | no (CC BY-NC-ND) |
| gommes2010more | AJP; model | full text (postprint) | no |
| romanelli2013air | AJP; P-V measurement + model | arXiv v1 only, not the AJP version | no |
| fischer2020approximation | arXiv; model, wind tunnel, 6 apogees | full text | no |
| finney2000analysis | AJP | abstract only | no |
| prusa2000hydrodynamics | SIAM Rev. | abstract only | no |
| kagan1995soda | Phys. Teach. | metadata only | no |
| thorncroft2009hydrodynamics | IJMEE; thrust-stand measurements | abstract only | no |
| watanabe2003thrust | JSASS (Japanese); thrust measurements | English abstract only | no |
| urieli2013water | lecture notes; model | page read | HTML, CC BY-NC-SA |
| nasa2023flight | technical page; qualitative | page read | HTML |
| qi2026research | J. Phys. Conf. Ser.; static force | full text | yes, CC BY 4.0 |
| ding2025dynamics | Results Phys.; simulation only | full text (main session) | yes, CC BY 4.0 |

Main-session check: the 11 DOIs resolve on Crossref with matching first
author, year, title and venue. arXiv 2001.08828 resolves.
`sources/pdf/qi2026research.pdf` is a 10-page PDF. Note contents were not
re-read; source-auditor checks them in phase 4.

Coverage by topic:
- 1 (thrust with water), 2 (air expansion), 4 (drag): covered.
- 3 (air-only thrust): Barrio-Perotti 2010 (adiabatic, choked nozzle),
  Fischer 2020 (empirical efficiency $\eta = (V_0/V_b)^{\mu}$, $\mu \approx 3$).
  No direct measurement.
- 5 (optimal fill): Barrio-Perotti 2010 (measured, range); Ding 2025
  (simulated, apogee: water volume ratio 0.498). No measured optimum for
  apogee.
- 6 (thrust curves): Open. Only Thorncroft 2009 and Watanabe 2003 report
  them, by their abstracts; full text not accessed.

Points for phase 2:
- Gauge or absolute pressure: Open in Gommes ($P_i$), Fischer ($p_0$,
  Table 2) and Qi. Each note marks it.
- Romanelli 2013, Table I: measured polytropic exponent 1.17 to 1.22,
  0.05 to 0.06 below the paper's own theory in every row. The text calls
  the agreement "very good". Own inference of lit-scout, not checked by
  the main session.
- Excluded: NASA GRC "Water Rocket" page (no quantitative content; states
  water is "about 100 times heavier than air", the ratio is about 800);
  UPenn wiki (no author or date); Thorncroft & Pascual 2005 (superseded
  by the 2009 paper); NHSJS 2025 (student journal); theses, galleries,
  commercial pages by source type.
