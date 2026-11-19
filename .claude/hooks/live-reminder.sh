#!/bin/sh
# UserPromptSubmit hook (Claude Code). Runs at every user prompt.
# Its standard output is added to the agent's context, so the rule
# "re-read live.md at every turn" (AGENTS.md section 1) is enforced by the
# harness and not left to the model.
#
# It counts the lines of live.md that start with "R:" (answers from the
# user). It does not parse them: the agent still has to re-read the file.

LIVE="${CLAUDE_PROJECT_DIR:-.}/live.md"

if [ ! -f "$LIVE" ]; then
    echo "Reminder: live.md not found at $LIVE."
    exit 0
fi

# grep -c prints 0 and exits with status 1 when nothing matches.
N=$(grep -c '^R:' "$LIVE" || true)

echo "Reminder (hook): re-read live.md before acting. It contains $N line(s) starting with R:."
exit 0
