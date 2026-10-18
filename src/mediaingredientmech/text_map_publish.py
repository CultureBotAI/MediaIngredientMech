"""Stage a validated map and update the static site's navigation status."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

from mediaingredientmech.text_map_site import prepare_text_map


def publish(root: Path, *, allow_stale_corpus: bool = False) -> dict:
    """Validate before site writes; expose the link only after successful staging."""
    context = (
        prepare_text_map(root, allow_stale_corpus=True)
        if allow_stale_corpus
        else prepare_text_map(root)
    )
    with context as ready:
        site = root / "docs"
        if ready is not None:
            ready.stage(site)
        status = {"enabled": ready is not None}
        destination = site / "data" / "text_map_status.json"
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=destination.parent,
                prefix=".text-map-status-",
                delete=False,
            ) as stream:
                temporary = Path(stream.name)
                json.dump(status, stream, sort_keys=True)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        return status


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument(
        "--allow-stale-corpus",
        action="store_true",
        default=os.environ.get("PAGES_ALLOW_STALE_CORPUS") == "1",
        help="Skip staging the semantic text map when corpus inputs moved ahead of the committed bundle (#685)",
    )
    args = parser.parse_args(argv)
    print(
        json.dumps(
            publish(args.root.resolve(), allow_stale_corpus=args.allow_stale_corpus),
            sort_keys=True,
        )
    )
    return 0
