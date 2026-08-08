#!/usr/bin/env python3
"""Render Claude-lane research prompts for ingredient records.

The Claude lane runs alongside the Edison/PaperQA3 lane. Edison mines primary
literature; Claude resolves identifiers directly against OLS/ChEBI/PubChem --
the question Edison reports repeatedly say they could not answer. Two lanes
disagreeing about a record is itself a finding, so both write into the same
auditable shape.

This script only *renders* prompts and stamps the audit trail. Execution is the
caller's (a Claude subagent per ingredient, writing its report to the path this
script names). Keeping rendering here means both lanes derive their prompt from
the same `template_vars()`, so a difference between lanes is a difference in
evidence, not in what each was told.

    python scripts/render_claude_research_prompt.py --queue research/queues/claude-priority.json
    python scripts/render_claude_research_prompt.py --slug Fumarate --print
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml  # noqa: E402
import research_ingredient as ri  # noqa: E402
from research_ingredient_edison import render_query, resolve_target  # noqa: E402

DEFAULT_TEMPLATE = ROOT / "templates" / "ingredient_claude_research.md"
DEFAULT_OUT_DIR = ROOT / "research" / "ingredients-claude"
LANE = "claude"


def stem_for(slug: str) -> str:
    return f"{slug}-{LANE}-research"


def has_report(slug: str, out_dir: Path) -> bool:
    """True when this slug already has a non-empty Claude report.

    Mirrors the Edison lane's `--skip-existing`: a rerun after a partial fan-out
    must not redo finished work, and an empty file is not a result.
    """
    md = out_dir / f"{stem_for(slug)}.md"
    return md.exists() and md.stat().st_size > 0


def render_one(path: Path, template: Path, out_dir: Path) -> dict:
    doc = ri.load_ingredient(path)
    status, slug = ri.infer_status_slug(path)
    query, variables = render_query(path, template, doc)
    stem = stem_for(slug)
    meta = {
        "slug": slug,
        "lane": LANE,
        "status_dir": status,
        "record": str(path.relative_to(ROOT)),
        "template": str(template.relative_to(ROOT)),
        "rendered_at": datetime.now(timezone.utc).isoformat(),
        "query_sha256": hashlib.sha256(query.encode("utf-8")).hexdigest(),
        "query_chars": len(query),
        "report": str((out_dir / f"{stem}.md").relative_to(ROOT)),
        "template_vars": variables,
        "query": query,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{stem}-meta.yaml").write_text(
        yaml.safe_dump(meta, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return meta


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--slug", help="Single ingredient slug or YAML path.")
    src.add_argument("--queue", type=Path, help="JSON list of slugs/paths.")
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--skip-existing", action="store_true",
                    help="Drop targets that already have a non-empty report.")
    ap.add_argument("--print", dest="show", action="store_true",
                    help="Print the rendered prompt (single --slug only).")
    ap.add_argument("--manifest", type=Path,
                    help="Write a JSON manifest of {slug, record, report, query} for dispatch.")
    args = ap.parse_args(argv)

    targets = [resolve_target(args.slug)] if args.slug else \
        [resolve_target(t) for t in json.loads(args.queue.read_text())]

    if args.skip_existing:
        before = len(targets)
        targets = [p for p in targets if not has_report(p.stem, args.out_dir)]
        if before != len(targets):
            print(f"Skipping {before - len(targets)} target(s) with an existing report.")

    metas = [render_one(p, args.template, args.out_dir) for p in targets]

    if args.show and metas:
        print(metas[0]["query"])
        return 0
    if args.manifest:
        args.manifest.write_text(json.dumps(
            [{k: m[k] for k in ("slug", "record", "report", "query")} for m in metas],
            indent=2) + "\n", encoding="utf-8")
        print(f"manifest: {args.manifest} ({len(metas)} entries)")
    print(f"rendered {len(metas)} prompt(s) -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
