# live.md

## Current task

Phase 0 (setup), done except for the items in the open questions. Then
stop for your review, compaction, tag `phase-0-setup`.

Committed (`git log --oneline`): `.gitignore`, `AGENTS.md` and
`CLAUDE.md`, journal and live.md, folder skeleton, `LICENSE`,
`pyproject.toml` with `uv.lock`, `README.md`, `prompts/phase-0.md`.

Not committed, waiting for you:
- `.claude/agents/lit-scout.md`, `physics-referee.md`,
  `source-auditor.md` (Q1).
- `.claude/hooks/live-reminder.sh` (tested: prints the reminder and the
  count of `R:` lines). Committed together with `.claude/settings.json`
  (Q2).

## Open questions

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

**Q4. PDFs: only redistributable licences.** In the public repository a
free-to-read PDF without an open licence cannot be redistributed. lit-scout
downloads only CC BY, CC BY-SA, CC BY-NC, CC0 or public domain PDFs, and
links the others. Proposal: keep this rule.

**Q5. The 13 setup questions in the history.** They were answered and
removed before the first commit of `live.md`, so the repository does not
contain them. Proposal: add them verbatim to `prompts/phase-0.md` as an
appendix (Q12 answer redacted). It gives the reader the full first
exchange, which is the clearest example of the `R:` method.

## Working notes

- Talk: 2026-11-23. All phases 0 to 6 before the talk.
