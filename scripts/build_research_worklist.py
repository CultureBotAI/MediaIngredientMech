#!/usr/bin/env python3
"""Build the Edison deep-research worklist for every ingredient record.

The goal is one research bundle per record in ``data/ingredients/{mapped,unmapped}/``
so each record's contents can be validated (and corrected) against source-backed
literature. A record counts as *done* only when its bundle is actually usable:

  * ``<stem>-edison-literature-meta.yaml`` exists,
  * its ``status`` is ``success`` (``in progress`` / ``fail`` get requeued), and
  * ``<stem>-edison-literature.md`` exists and is non-empty.

That last check matters. ``status: success`` with ``answer_chars: 0`` has happened,
and a zero-length answer is not evidence — requeue it rather than counting it.

The runner (``research_ingredient_edison.py``) is serial, so the worklist is
emitted as N shards that can be launched as N concurrent processes. Shards are
dealt round-robin, not in contiguous blocks, so a slow cluster of large complex
media does not land entirely in one shard.

    python scripts/build_research_worklist.py --shards 6
    python scripts/build_research_worklist.py --shards 6 --status unmapped --out-dir /tmp/q
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INGREDIENTS = ROOT / "data" / "ingredients"
RESEARCH = ROOT / "research" / "ingredients"
STATUSES = ("mapped", "unmapped")

# The meta yaml is small and regular; a full yaml.safe_load per file over ~3k
# files is needless overhead when two top-level scalars are all we need.
STATUS_RE = re.compile(r"^status:\s*(.+?)\s*$", re.M)


def index_bundles(research_dir: Path, job_short: str = "literature") -> dict[str, Path]:
    """Map lowercased slug -> meta yaml path.

    Matching is case-insensitive *on purpose*, not by accident of the local
    filesystem: 81 bundles predate a slug re-casing (see #299), so
    ``B-glucan_from_yeast`` and ``B-glucan_From_Yeast`` are the same ingredient
    researched once. Doing it explicitly keeps the count identical on a
    case-sensitive filesystem (CI) instead of silently requeuing 81 paid runs.
    No two record stems collide case-insensitively, so the fold is unambiguous.
    """
    suffix = f"-edison-{job_short}-meta.yaml"
    return {p.name[: -len(suffix)].lower(): p
            for p in research_dir.glob(f"*{suffix}")}


def bundle_status(stem: str, bundles: dict[str, Path], job_short: str = "literature") -> str:
    """Return ``done``, or a reason the record still needs researching."""
    meta = bundles.get(stem.lower())
    if meta is None:
        return "never-run"
    m = STATUS_RE.search(meta.read_text(encoding="utf-8", errors="replace"))
    status = (m.group(1) if m else "").strip().strip("'\"").lower()
    if status != "success":
        return f"status:{status or 'unknown'}"
    md = meta.parent / meta.name.replace(f"-{job_short}-meta.yaml", f"-{job_short}.md")
    if not md.exists() or not md.stat().st_size:
        return "empty-answer"
    return "done"


def collect(statuses: tuple[str, ...], research_dir: Path) -> tuple[list[dict], dict[str, int]]:
    todo: list[dict] = []
    tally: dict[str, int] = {}
    bundles = index_bundles(research_dir)
    for status in statuses:
        for path in sorted((INGREDIENTS / status).glob("*.yaml")):
            reason = bundle_status(path.stem, bundles)
            tally[reason] = tally.get(reason, 0) + 1
            if reason != "done":
                todo.append({"status": status, "slug": path.stem,
                             "path": str(path.relative_to(ROOT)), "reason": reason})
    return todo, tally


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shards", type=int, default=6, help="Number of concurrent queues to emit.")
    ap.add_argument("--status", choices=STATUSES, action="append",
                    help="Restrict to one status dir (repeatable). Default: both.")
    ap.add_argument("--out-dir", type=Path, default=ROOT / "research" / "queues")
    ap.add_argument("--research-dir", type=Path, default=RESEARCH)
    ap.add_argument("--limit", type=int, default=None, help="Cap the total queued records.")
    args = ap.parse_args(argv)

    if args.shards < 1:
        raise SystemExit("--shards must be >= 1")

    statuses = tuple(args.status) if args.status else STATUSES
    todo, tally = collect(statuses, args.research_dir)
    if args.limit is not None:
        todo = todo[: args.limit]

    args.out_dir.mkdir(parents=True, exist_ok=True)
    # Round-robin deal: neighbouring slugs (often the same chemical family, and
    # so similar in cost) spread across shards instead of clumping.
    shards: list[list[dict]] = [[] for _ in range(args.shards)]
    for i, entry in enumerate(todo):
        shards[i % args.shards].append(entry)

    for i, shard in enumerate(shards):
        # The runner takes a JSON list of target strings; paths are unambiguous
        # where a bare slug could collide across mapped/ and unmapped/.
        (args.out_dir / f"shard-{i:02d}.json").write_text(
            json.dumps([e["path"] for e in shard], indent=2) + "\n", encoding="utf-8")
    (args.out_dir / "worklist.json").write_text(
        json.dumps(todo, indent=2) + "\n", encoding="utf-8")

    total = sum(tally.values())
    print(f"records scanned : {total}")
    for reason in sorted(tally, key=lambda r: -tally[r]):
        print(f"  {reason:<24} {tally[reason]}")
    print(f"queued          : {len(todo)} across {args.shards} shards -> {args.out_dir}")
    if todo:
        print(f"  shard sizes     : {[len(s) for s in shards]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
