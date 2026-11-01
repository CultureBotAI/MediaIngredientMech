#!/usr/bin/env python3
"""Repair #1031's frozen membership cohort after #875; dry-run by default.

Only the existing membership identifier changes. This neither rebuilds the
CultureMech cohort nor changes historical YAML counts or scientific approval.
Use the isolated Claw environment for the native transaction and caller lock.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from scripts import promote_heptahydrate_ncit as guarded  # noqa: E402

MEMBERSHIP = Path("mappings/culturemech_recipe_membership.tsv")
BEFORE_SHA = "6537498d833f45295193865d6cd5f98ad31200c5dbe4a706c6f541dcf30a5064"
AFTER_SHA = "55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897"
ANCHORS = {
    guarded.OWNER: "6e816ef6a1dad8dab9c3ddd711ca84d8a3489bedb175d540ea3cb618c7068873",
    guarded.LEDGER: "717289ca0e45046dcb96f6839b843838a6636fd8e120cf4d9b9ac48de3d9016d",
    guarded.SSSOM: "68552edd452d5dccf1262b5d03190a6b668341952a554f349149f269403cca67",
}
RECIPES = frozenset(
    f"CultureMech:{number}" for number in (
        "000015", "000086", "000167", "000256", "000359", "000692", "000970",
        "000984", "001147", "001148", "001953", "002128", "003989", "006526",
        "006888", "006889", "006890", "006891", "006892", "006893", "008858",
        "009013", "009061", "011101", "011366", "011825", "012186", "012325",
        "012342", "012577", "012579", "014768",
    )
)
APPROVAL = "NONE: existing membership identity migration only; no scientific approval."


def repaired_membership(before: bytes) -> bytes:
    """Preserve every row's bytes except the selected identity cell and order."""
    current_sha = guarded.digest(before)
    if current_sha == AFTER_SHA:
        return before
    if current_sha != BEFORE_SHA:
        raise ValueError("Membership differs from the frozen preimage or complete repair")
    lines = before.splitlines(keepends=True)
    header = []
    while lines and lines[0].startswith(b"#"):
        header.append(lines.pop(0))
    if not lines or lines[0] != b"mim_identifier\trecipe_id\toccurrences\n":
        raise ValueError("Unexpected membership columns")
    header.append(lines.pop(0))
    rows = []
    selected = set()
    for line in lines:
        fields = line.rstrip(b"\r\n").decode().split("\t")
        if len(fields) != 3 or not all(fields):
            raise ValueError("Malformed membership row")
        identifier, recipe, count = fields
        if identifier == guarded.NEW:
            raise ValueError("Destination membership exists or migration is partial")
        if identifier == guarded.OLD:
            if recipe in selected or recipe not in RECIPES or count != "1":
                raise ValueError("Frozen membership recipe/count cohort changed")
            selected.add(recipe)
            identifier = guarded.NEW
            line = identifier.encode() + b"\t" + line.split(b"\t", 1)[1]
        rows.append(((identifier, recipe), line))
    if selected != RECIPES or len({key for key, _ in rows}) != len(rows):
        raise ValueError("Incomplete frozen cohort or duplicate membership key")
    after = b"".join(header) + b"".join(line for _, line in sorted(rows))
    if guarded.digest(after) != AFTER_SHA:
        raise ValueError("Membership repair differs from the bounded expected output")
    return after


def repair(root: Path, log: Path, *, apply: bool = False) -> dict:
    inputs = {root / path: (root / path).read_bytes() for path in (*ANCHORS, MEMBERSHIP)}
    for path, expected in ANCHORS.items():
        if guarded.digest(inputs[root / path]) != expected:
            raise ValueError(f"Corrected identity anchor changed: {path}")
    # Also search ignored/nested YAML: a conflicting new owner is not safe.
    guarded.unique_destination(root)
    before = inputs[root / MEMBERSHIP]
    after = repaired_membership(before)
    if after == before:
        return {"applied": False, "changed": False, "approval": APPROVAL}
    result = {
        "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1031",
        "phase": "membership_identity_repair",
        "curator": "Codex", "llm_assisted": True, "llm_model": "gpt-6",
        "approval": APPROVAL,
        "scope": "Preserve the frozen CultureMech cohort, recipe IDs, counts and source header; change only its MIM identity key.",
        "input_sha256": {str(path.relative_to(root)): guarded.digest(data)
                         for path, data in inputs.items()},
        "artifact": MEMBERSHIP.as_posix(),
        "before_sha256": BEFORE_SHA, "after_sha256": AFTER_SHA,
        "before_identifier": guarded.OLD, "after_identifier": guarded.NEW,
        "memberships": [{"recipe_id": recipe, "occurrences": 1} for recipe in sorted(RECIPES)],
    }
    return guarded.publish(
        root, {MEMBERSHIP: after}, inputs, log,
        {log.with_suffix(".before-membership.tsv"): before}, result, apply=apply,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--log", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    if target.path.resolve() != args.root.resolve():
        raise ValueError("Configured MIM root differs from the requested worktree")
    target.open()
    with LockManager().lock("mediaingredientmech", "#1031 membership identity repair"):
        result = repair(target.path.resolve(), args.log, apply=args.apply)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
