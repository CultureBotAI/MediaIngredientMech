#!/usr/bin/env bash
# Launch one Edison research shard. Every shard -- and the canary that cleared
# the way for them -- goes through this one path, so what the canary proved
# (credentials reach the child process, sidecars land) holds for the fan-out.
#
# --skip-existing makes a relaunch cheap and safe: a shard that dies partway
# through, or one relaunched after a worklist rebuild, re-bills nothing that
# already produced an answer.
#
#   scripts/run_research_shard.sh 00
#   scripts/run_research_shard.sh 00 --job literature-high
set -euo pipefail

cd "$(dirname "$0")/.."

shard="${1:?usage: run_research_shard.sh <shard-number> [extra args...]}"
shift || true

queue="research/queues/shard-${shard}.json"
log="research/logs/shard-${shard}.log"
[[ -f "$queue" ]] || { echo "no such queue: $queue" >&2; exit 2; }
mkdir -p research/logs

echo "shard ${shard}: $(python3 -c "import json;print(len(json.load(open('${queue}'))))") queued -> ${log}"
exec uv run --extra dev python scripts/research_ingredient_edison.py \
    --batch "$queue" \
    --template templates/ingredient_mapping_research.md \
    --out-dir research/ingredients \
    --skip-existing \
    "$@" >> "$log" 2>&1
