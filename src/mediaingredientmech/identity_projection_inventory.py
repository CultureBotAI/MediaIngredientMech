"""Issue #1269: independently pinned complete #1265 mint-order authority.

The digest below is derived from every regular ingredient preimage at fixed Git
commit 0dac278466699129a083343a921c2e0ca18a9ab4, independently of the migration
manifest and registry. It is not a digest supplied by the portable bundle itself.
"""

from __future__ import annotations

from mediaingredientmech.identity_projection import (
    BASE_COMMIT,
    REPORT_ROOT,
    Proof,
    document,
    encode,
    require,
    sha,
)

INVENTORY = REPORT_ROOT + "/baseline-record-inventory.json"
INVENTORY_SHA256 = "fcf0c5a1bfcd8568e1f269d7f13c53ef3cebfa9956a60ac21cb129dc636fc91a"


def products(proof: Proof) -> dict[str, bytes]:
    value = {
        "schema_version": 1,
        "source_commit": BASE_COMMIT,
        "records": [
            {
                "path": name,
                "sha256": sha(proof.before[name]),
                "preferred_term": proof.transition["old_records"][name]["preferred_term"],
            }
            for name in sorted(proof.transition["old_records"])
        ],
    }
    raw = encode(value)
    require(
        sha(raw) == INVENTORY_SHA256, "complete baseline inventory differs from fixed Git authority"
    )
    return {INVENTORY: raw}


def validate(raw: bytes, manifest: dict, registry) -> None:
    """Bind every mint's position, source identity and label, including non-cohort owners."""
    require(sha(raw) == INVENTORY_SHA256, "complete baseline inventory authority differs")
    inventory = document(raw)
    require(
        set(inventory) == {"schema_version", "source_commit", "records"}
        and type(inventory["schema_version"]) is int
        and inventory["schema_version"] == 1
        and inventory["source_commit"] == BASE_COMMIT,
        "complete baseline inventory shape differs",
    )
    expected = inventory["records"]
    require(
        [entry["path"] for entry in manifest["records"]] == [entry["path"] for entry in expected]
        and len(registry.entries) == len(expected),
        "complete baseline mint inventory differs",
    )
    for index, (prior, entry, mint) in enumerate(
        zip(expected, manifest["records"], registry.entries, strict=True), 1
    ):
        identifier = f"MIM:{index:07d}"
        require(
            entry["before_sha256"] == prior["sha256"]
            and entry["mim_id"] == identifier
            and mint.mim_id == identifier
            and mint.label_at_minting == prior["preferred_term"]
            and mint.minted_on == manifest["minted_on"]
            and mint.status == "active"
            and not mint.replaced_by,
            "complete baseline mint assignment differs",
        )
