#!/bin/bash
# Pause the autonomous stack.
# All data remains on disk. Resume with resume-stack.sh.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
STACK_DIR="$(dirname "$SCRIPT_DIR")"

echo "Pausing autonomous stack..."
cd "$STACK_DIR"
docker compose stop

echo ""
echo "Stack paused. All containers stopped. Data is intact."
echo "To resume: ./scripts/resume-stack.sh"
