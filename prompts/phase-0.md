# Phase 0: prompts

Prompts given in the chat, verbatim (in Italian), with a translation.
After each chat prompt, the questions asked in `live.md` and the `R:`
answers given there, verbatim. Private data is redacted and marked.

## Prompt 1

Context: the folder contains only `BRIEF.md`, already committed. In
Claude Code, `@BRIEF.md` attaches the file to the prompt.

```text
leggi @BRIEF.md e procediamo
```

Translation: "read @BRIEF.md and let's proceed".

Result: 13 questions in `live.md`, each with a proposed answer, and a
plan for phase 0. No other file written.

### Questions and answers, round 1

These questions were answered and removed before `live.md` was first
committed. This copy is the only one in the repository.

**Q1. Repository name.** Used in the README title and as the future GitHub
name. Proposal: `water-rocket-ai-workflow`.
R: ok

**Q2. Licence.** The repository mixes code and text. Proposal: MIT for
`code/`, CC BY 4.0 for documents (`docs/`, `method/`, README). One
`LICENSE` file stating both. Alternative: a single licence for everything.
R: ok except for the open access pdfs: for those, the license in the pdfs apply

**Q3. Python version and environment manager.** uv is installed.
Proposal: uv with `pyproject.toml` and `uv.lock`, `requires-python = ">=3.11"`
so that readers with older systems can run it; development on 3.13.
Dependencies: numpy, scipy, matplotlib.
R: ok

**Q4. Notebooks or plain scripts in `code/`.** Proposal: plain scripts
(a module with the physics model, one script per figure). Diffs of plain
scripts are readable in the commit history; notebook diffs are not.
R: ok

**Q5. Hook to re-read live.md at every prompt.** Proposal: yes. A
`UserPromptSubmit` hook in `.claude/settings.json` (committed) that injects
the line "Re-read live.md and look for new R: lines before acting." It
makes the rule enforced by the harness, not by memory of the model, and it
is itself a file in the repository, which fits the message of the talk.
Limit: it only works in Claude Code; other harnesses rely on AGENTS.md.
R: ok, can we put a note in AGENTS.md or the relevant file for other harnesses so that the first time the repo is opened they ask if this should be replicated, and work their way onto replicating?

**Q6. Which file holds the rules: CLAUDE.md or AGENTS.md?** The brief
says CLAUDE.md holds the rules and AGENTS.md points to it. Alternative:
rules in AGENTS.md (read natively by Codex CLI, OpenCode, Gemini CLI with
config), and CLAUDE.md contains only `@AGENTS.md` (Claude Code imports the
file). The alternative makes portability real rather than a pointer, and
matches the talk's claim that the project is portable. Proposal: the
alternative. Keep the brief's layout if you prefer.
R: ok the alternative

**Q7. Repository inside OneDrive.** The folder is under
`OneDrive_uninsubria/`. Sync clients can conflict with `.git/` (lock
files, partial sync of objects) and the `.venv/` would be synced too.
Options: (a) keep it here, put `.venv` outside via `UV_PROJECT_ENVIRONMENT`
or accept the sync; (b) move the repository outside OneDrive and keep
only the GitHub remote as backup. Proposal: (b). Your call: it changes
the working directory.
R: (a)

**Q8. Private note on a physics error (BRIEF section 8).** If the note is
committed, it stays in the history even if removed later. Proposal: write
it in `private/demo-error.md`, with `private/` in `.gitignore`. The
`.gitignore` line is visible but the content is never committed.
Alternative: keep it outside the repository.
R: ok

**Q9. Commit attribution.** My commits will end with
`Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; author is your
git identity. This makes visible in `git log` which commits the agent made.
Proposal: keep it. Commits you make by hand (e.g. the demo error) will not
have it.
R: ok

**Q10. Subagent models.** Options: `model: inherit` for all three (same
model as the main session), or a smaller model for lit-scout. Proposal:
`inherit` for all three. A single model makes the phases easier to compare
and to describe in the talk.
R: ok

**Q11. Branch name.** The repository is on `master`. GitHub defaults to
`main`. Proposal: rename to `main` now, before any tag. Leave as is if you
prefer.
R: ok

**Q12. Other repository with the same method (BRIEF section 10).** If you
want me to reuse its conventions, give the link or local path. Otherwise I
proceed from the brief alone.
R: the other repositoy is [local path to another repository of the user, redacted]

**Q13. Schedule.** Talk on 2026-11-23, today is 2026-11-19. Phase 3 is
shown live, so phases 0 to 2 must be tagged before the talk. Must phases 4
to 6 also be finished before the talk, or can they follow it? This decides
whether phase 2 is kept short (fewer sources, simpler model) to fit.
R: all needs to be completed before the talk

## Prompt 2

```text
ho risposto in live.md, procedi
```

Translation: "I answered in live.md, go ahead".

Result: rules, journal, folder skeleton, licence, Python environment,
README, the three agents (uncommitted, for review). The write of
`.claude/settings.json` was blocked by Claude Code. 5 review questions in
`live.md`.

### Questions and answers, round 2

**Q1. Review of the three agents.** Files in `.claude/agents/`. Points to
check:
- lit-scout: Bash allowed only for `curl` and `file`, by instruction. Key
  format `surnameYEARword`. A note states `Access: full text read |
  abstract only`; from an abstract, no equations or values are attributed.
- physics-referee: forbidden to read `sources/`, `journal/`, `live.md`,
  `checks/`, `prompts/`, `private/`, `method/`, `BRIEF.md`, `README.md`
  and the git history. It lists the files it opened in its report. It
  may run the code with `uv run`.
- source-auditor: checks each claim against the source text (PDF or web
  full text), not against lit-scout's note; marks `checked against note
  only` otherwise. Forbidden `checks/physics-review.md`, `code/`,
  `live.md`, `journal/`.
Proposal: commit as they are. Write corrections here or edit the files
directly; I will read the diff.
R: they seem fine to me, let's keep them like they are. This is mostly for the purpose of the demo, in a real world case we'd test them now or during the work, and fine tune

**Q2. `.claude/settings.json`, to be created by you.** Claude Code
blocked my write of this file (an agent cannot change its own
permissions). Proposed content: the hook and a permission list reused
from your other repository (web search, fetch on DOI and metadata
services, `uv run` and `uv sync` without a prompt).

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "sh \"$CLAUDE_PROJECT_DIR/.claude/hooks/live-reminder.sh\""
          }
        ]
      }
    ]
  },
  "permissions": {
    "allow": [
      "WebSearch",
      "WebFetch(domain:doi.org)",
      "WebFetch(domain:api.crossref.org)",
      "WebFetch(domain:api.openalex.org)",
      "WebFetch(domain:arxiv.org)",
      "Bash(uv run:*)",
      "Bash(uv sync:*)"
    ]
  }
}
```

Proposal: create it with this content, then restart Claude Code (hooks
are loaded at start). Drop the `permissions` block if you prefer to
approve each call.
R: done

**Q3. `.claude/settings.local.json`, to be created by you (git-ignored).**
Keeps the virtual environment outside OneDrive for every `uv` command
run by Claude Code. The environment already exists at that path
(`~/.cache/uv-envs/water-rocket-ai-workflow`). The path must be absolute
in the JSON file.

```json
{
  "env": {
    "UV_PROJECT_ENVIRONMENT": "<absolute path of your home>/.cache/uv-envs/water-rocket-ai-workflow"
  }
}
```

In your own terminal, `uv run` creates `.venv/` inside the folder (git
ignores it, OneDrive syncs it) unless you export the same variable in
your shell profile.
R: done

**Q4. PDFs: only redistributable licences.** In the public repository a
free-to-read PDF without an open licence cannot be redistributed. lit-scout
downloads only CC BY, CC BY-SA, CC BY-NC, CC0 or public domain PDFs, and
links the others. Proposal: keep this rule.
R: ok

**Q5. The 13 setup questions in the history.** They were answered and
removed before the first commit of `live.md`, so the repository does not
contain them. Proposal: add them verbatim to `prompts/phase-0.md` as an
appendix (Q12 answer redacted). It gives the reader the full first
exchange, which is the clearest example of the `R:` method.
R: yes, add. keep track of the anskers also in the future

R: a note (unrelated to the questions): the initial part of live.md must be always kept updated so that if I restart the session, i just write "read live.md" and claude code (or any other harness) knows how to restore the context and proceed with the job

## Prompt 3

```text
risposto, fai quello che serve prima che rilanci claude
```

Translation: "answered, do what is needed before I restart Claude".
