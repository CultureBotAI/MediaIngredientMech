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

# Supervisor loop. The runner already survives a single bad record, but a dead
# client (expired connection pool, laptop asleep, DNS gone) can still end the
# process. Relaunching with --skip-existing costs nothing and re-bills nothing,
# so keep going until the queue reports no work left (exit 2).
attempt=0
while :; do
    attempt=$((attempt + 1))
    echo "=== shard ${shard} attempt ${attempt} $(date -u +%FT%TZ)" >> "$log"
    set +e
    uv run --extra dev python scripts/research_ingredient_edison.py \
        --batch "$queue" \
        --template templates/ingredient_mapping_research.md \
        --out-dir research/ingredients \
        --skip-existing \
        "$@" >> "$log" 2>&1
    rc=$?
    set -e
    # 2 == "No targets to research", i.e. the shard is genuinely finished.
    if [[ $rc -eq 2 ]]; then
        echo "=== shard ${shard} complete after ${attempt} attempt(s)" >> "$log"
        break
    fi
    # 3 == account-level refusal (402/401/403). Retrying cannot help and only
    # generates rate-limit traffic against an API already saying no -- which is
    # exactly what happened when a 402 was treated as a per-record failure.
    if [[ $rc -eq 3 ]]; then
        echo "=== shard ${shard} STOPPED: account-level API error; not retrying." >> "$log"
        echo "shard ${shard}: stopped on an account-level API error (see ${log})" >&2
        exit 3
    fi
    echo "=== shard ${shard} exited rc=${rc}; retrying in 60s" >> "$log"
    sleep 60
done
