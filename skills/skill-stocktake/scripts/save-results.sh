#!/usr/bin/env bash
# Shared bootstrap/merge/replace writer; Node is also used by quick-diff.
set -euo pipefail
exec node "$(dirname "$0")/save-results.cjs" "$@"
