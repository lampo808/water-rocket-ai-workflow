# live.md

New session, any harness: read `AGENTS.md`, then `journal/history.md`,
then continue from `Resume` below. Answer lines start with `R:`.

## Current task

Resume:
- Phase: 0 (setup). Repository `water-rocket-ai-workflow`, branch `main`.
- State: all phase-0 files committed (`git log --oneline`). No tag yet.
- Done: rules (`AGENTS.md`, imported by `CLAUDE.md`), journal, folder
  skeleton, `LICENSE`, uv environment, `README.md` skeleton, three agents
  in `.claude/agents/`, hook and `.claude/settings.json`,
  `prompts/phase-0.md` with all questions and answers.
- Waiting for the user: review of phase 0 (Q1).
- Next step after review: commit `journal: compact phase 0`, tag
  `phase-0-setup`, then phase 1 (run lit-scout).

## Open questions

**Q1. Phase 0 review.** Everything is committed. Check `git log
--oneline` and the files. If it is fine, I compact the phase-0 journal
entries in a separate commit, tag `phase-0-setup` and start phase 1 by
running lit-scout. Proposal: write `R: ok` or list the corrections.

## Working notes

- Talk: 2026-11-23. All phases 0 to 6 before the talk.
- Claude Code restart: needed to load `UV_PROJECT_ENVIRONMENT` from
  `.claude/settings.local.json` (env is read at start). The hook is
  already active.
