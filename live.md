# live.md

New session, any harness: read `AGENTS.md`, then `journal/history.md`,
then continue from `Resume` below. Answer lines start with `R:`.

## Current task

Resume:
- Phase: 1 (literature). Repository `water-rocket-ai-workflow`, branch `main`.
- State: phase 0 closed, tag `phase-0-setup`. lit-scout finished; its
  output is committed in `sources/`.
- Done: 13 notes, `sources/references.bib` (13 entries), 1 PDF. DOIs
  re-checked by the main session against Crossref.
- Waiting for the user: Q1 to Q5 below.
- Next step after the answers: act on them, then stop for the phase-1
  review (compaction, tag `phase-1-literature`).

## Open questions

**Q1. Source list.** 13 sources, table in Working notes. All pass the
identity check. 6 were read in full; the other 7 are abstract or metadata
only, and their notes attribute nothing beyond that. Proposal: accept the
list as it is.

**Q2. CC BY-NC-ND copies.** Both Barrio-Perotti papers (2009, 2010) have
repository copies under CC BY-NC-ND. ND allows redistribution of
unchanged copies, but the rule in force (phase 0, Q4) lists only CC BY,
CC BY-SA, CC BY-NC, CC0, public domain. Proposal: keep the rule and link
the copies. The notes already record the URLs.

**Q3. Ding et al. 2025.** Results in Physics 76, 108420,
DOI 10.1016/j.rinp.2025.108420, CC BY. It covers fill-fraction
optimisation (topic 5, the weakest). The publisher returned 403 to the
agent. Not verified by the main session. Proposal: you download the PDF
in a browser and put it in `sources/pdf/ding2025.pdf`; I then verify the
DOI and write its note from the full text. If you skip it, phase 2
proceeds without it.

**Q4. qi2026research.** The only downloaded PDF (CC BY 4.0). Problems
recorded in its note: the introduction reuses the Gommes 2010 abstract
almost verbatim without citing it; "accelerations" are peak tether force
over initial mass; labelling errors (e.g. "atmospheric pressure fixed at
500 kPa"). Proposal: keep the note, do not cite it in `docs/` for any
value.

**Q5. Optimal fill fraction in phase 2.** No source read in full gives a
measured optimum for vertical apogee. The only measured optimum is for
horizontal range on a 45 degree ramp (Barrio-Perotti 2010: 0.5 to 0.6 L
in a 2 L bottle at 2 bar gauge). Proposal: in phase 2 the optimum for
apogee is a model result, labelled as own inference, and compared with
the Barrio-Perotti range result as a check of trend only.

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

Main-session check: the 10 DOIs resolve on Crossref with matching first
author, year, title and venue. arXiv 2001.08828 resolves.
`sources/pdf/qi2026research.pdf` is a 10-page PDF. Note contents were not
re-read; source-auditor checks them in phase 4.

Coverage by topic:
- 1 (thrust with water), 2 (air expansion), 4 (drag): covered.
- 3 (air-only thrust): Barrio-Perotti 2010 (adiabatic, choked nozzle),
  Fischer 2020 (empirical efficiency $\eta = (V_0/V_b)^{\mu}$, $\mu \approx 3$).
  No direct measurement.
- 5 (optimal fill): see Q5.
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
