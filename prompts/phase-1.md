# Phase 1: prompts

Prompts of phase 1, verbatim, with a translation where needed. After
each chat prompt, the questions asked in `live.md` and the `R:` answers
given there, verbatim. Private data is redacted and marked.

## Prompt 1

Context: same chat prompt as phase 0, prompt 4 (`read live.md`). The
`R: ok` on the phase-0 review authorised the start of phase 1.

## Prompt to lit-scout

Written by the main session and passed to the `lit-scout` subagent.

```text
Run the literature search defined in your instructions
(.claude/agents/lit-scout.md) for this repository. Scope, verification,
PDF licence rule, note format and BibTeX rules are all in that file;
follow them exactly. sources/ currently holds only README.md,
references.bib and an empty pdf/ folder: read sources/README.md first.
Target 8 to 15 sources. Return the final report described in your
instructions.
```

Result: 13 notes in `sources/`, 13 BibTeX entries, 1 PDF
(`qi2026research`, CC BY 4.0). The main session re-checked the 10 DOIs
on Crossref. 5 review questions in `live.md`.

### Questions and answers, round 1

**Q1. Source list.** 13 sources, table in Working notes. All pass the
identity check. 6 were read in full; the other 7 are abstract or metadata
only, and their notes attribute nothing beyond that. Proposal: accept the
list as it is.
R: ok

**Q2. CC BY-NC-ND copies.** Both Barrio-Perotti papers (2009, 2010) have
repository copies under CC BY-NC-ND. ND allows redistribution of
unchanged copies, but the rule in force (phase 0, Q4) lists only CC BY,
CC BY-SA, CC BY-NC, CC0, public domain. Proposal: keep the rule and link
the copies. The notes already record the URLs.
R: ok

**Q3. Ding et al. 2025.** Results in Physics 76, 108420,
DOI 10.1016/j.rinp.2025.108420, CC BY. It covers fill-fraction
optimisation (topic 5, the weakest). The publisher returned 403 to the
agent. Not verified by the main session. Proposal: you download the PDF
in a browser and put it in `sources/pdf/ding2025.pdf`; I then verify the
DOI and write its note from the full text. If you skip it, phase 2
proceeds without it.
R: ok, done

**Q4. qi2026research.** The only downloaded PDF (CC BY 4.0). Problems
recorded in its note: the introduction reuses the Gommes 2010 abstract
almost verbatim without citing it; "accelerations" are peak tether force
over initial mass; labelling errors (e.g. "atmospheric pressure fixed at
500 kPa"). Proposal: keep the note, do not cite it in `docs/` for any
value.
R: ok

**Q5. Optimal fill fraction in phase 2.** No source read in full gives a
measured optimum for vertical apogee. The only measured optimum is for
horizontal range on a 45 degree ramp (Barrio-Perotti 2010: 0.5 to 0.6 L
in a 2 L bottle at 2 bar gauge). Proposal: in phase 2 the optimum for
apogee is a model result, labelled as own inference, and compared with
the Barrio-Perotti range result as a check of trend only.
R: ok

## Prompt 2

```text
risposto, procedi
```

Translation: "answered, go ahead".

Result: the user placed the Ding et al. 2025 PDF in `sources/pdf/`. The
main session verified the DOI, read the full text, wrote
`sources/ding2025dynamics.md` and its BibTeX entry, and renamed the PDF
to `ding2025dynamics.pdf` (key convention of lit-scout).
