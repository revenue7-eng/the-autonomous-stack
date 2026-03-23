#!/bin/bash
# Resume the autonomous stack after a pause.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
STACK_DIR="$(dirname "$SCRIPT_DIR")"

echo "Resuming autonomous stack..."
cd "$STACK_DIR"
docker compose start

echo ""
echo "Stack resumed. All containers running."
echo "To pause: ./scripts/pause-stack.sh"
