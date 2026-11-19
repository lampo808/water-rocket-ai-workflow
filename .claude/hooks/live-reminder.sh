#!/bin/sh
# UserPromptSubmit hook (Claude Code). Runs at every user prompt.
# Its standard output is added to the agent's context, so the rule
# "re-read live.md at every turn" (AGENTS.md section 1) is enforced by the
# harness and not left to the model.
#
# It counts the lines of live.md that start with "R:" and have text after
# the colon (answers from the user), and separately the empty "R:" lines
# the agent prepares below each question (AGENTS.md section 3). It does
# not parse the answers: the agent still has to re-read the file.

LIVE="${CLAUDE_PROJECT_DIR:-.}/live.md"

if [ ! -f "$LIVE" ]; then
    echo "Reminder: live.md not found at $LIVE."
    exit 0
fi

# grep -c prints 0 and exits with status 1 when nothing matches.
N=$(grep -c '^R:[[:space:]]*[^[:space:]]' "$LIVE" || true)
E=$(grep -c '^R:[[:space:]]*$' "$LIVE" || true)

echo "Reminder (hook): re-read live.md before acting. It contains $N answered R: line(s) and $E empty R: line(s)."
exit 0
