"""Verify portable bytes and reconstruct the bounded application, without writes."""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    here = Path(__file__).resolve().parent
    sources = json.loads((here / "portable-sources.json").read_text())["files"]
    for entry in sources:
        content = (here / entry["portable_path"]).read_bytes()
        if entry.get("encoding") == "gzip":
            content = gzip.decompress(content)
            expected = entry["original_sha256"]
        else:
            expected = entry["sha256"]
        if sha(content) != expected:
            raise ValueError(f"Portable evidence differs: {entry['portable_path']}")
    inventory_path = here / "inventory.json"
    if inventory_path.exists():
        inventory = json.loads(inventory_path.read_text())
        actual_files = {
            str(path.relative_to(here))
            for path in here.rglob("*")
            if path.is_file() and path != inventory_path
        }
        if actual_files != set(inventory["files"]):
            raise ValueError("Frozen artifact inventory does not cover exactly the package")
        for name, expected in inventory["files"].items():
            if sha((here / name).read_bytes()) != expected["sha256"]:
                raise ValueError(f"Frozen artifact differs: {name}")

    receipt = json.loads((here / "application/apply.json").read_text())
    before = gzip.decompress((here / "application/apply.before-membership.tsv.gz").read_bytes())
    journal = json.loads(gzip.decompress((here / "application/journal.json.gz").read_bytes()))
    if journal["status"] != "complete" or len(journal["previous"]) != 1:
        raise ValueError("Unexpected native journal scope")
    if next(iter(journal["previous"].values())).encode() != before:
        raise ValueError("Native journal and standalone beforeimage differ")
    if sha(before) != receipt["before_sha256"]:
        raise ValueError("Beforeimage does not match application receipt")
    lines = before.splitlines(keepends=True)
    header = []
    while lines and lines[0].startswith(b"#"):
        header.append(lines.pop(0))
    if not lines or lines[0] != b"mim_identifier\trecipe_id\toccurrences\n":
        raise ValueError("Unexpected membership columns")
    header.append(lines.pop(0))
    selected = {}
    transformed = []
    for line in lines:
        identifier, recipe, count = line.decode().rstrip("\r\n").split("\t")
        if identifier == receipt["after_identifier"]:
            raise ValueError("Destination existed in the frozen beforeimage")
        if identifier == receipt["before_identifier"]:
            if recipe in selected:
                raise ValueError("Duplicate selected recipe")
            selected[recipe] = int(count)
            identifier = receipt["after_identifier"]
            line = identifier.encode() + b"\t" + line.split(b"\t", 1)[1]
        transformed.append(((identifier, recipe), line))
    if selected != {entry["recipe_id"]: entry["occurrences"] for entry in receipt["memberships"]}:
        raise ValueError("Application receipt does not preserve the frozen recipe/count pairs")
    after = b"".join(header) + b"".join(line for _, line in sorted(transformed))
    if sha(after) != receipt["after_sha256"]:
        raise ValueError("Bounded reconstructed artifact differs from the applied output")
    print(json.dumps({
        "portable_source_files_verified": len(sources),
        "frozen_inventory_checked": inventory_path.exists(),
        "membership_rows": len(lines),
        "migrated_recipe_count_pairs": len(selected),
        "unchanged_other_rows": len(lines) - len(selected),
        "selected_occurrences": sum(selected.values()),
        "journal_beforeimage_verified": True,
        "reconstructed_after_sha256": sha(after),
        "scientific_approval": False,
    }, indent=2))


if __name__ == "__main__":
    main()
