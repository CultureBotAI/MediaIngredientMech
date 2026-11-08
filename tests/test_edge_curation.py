"""Native adapter contracts: exact payload scope, inherited review and immutable pins."""

import copy
import io
import importlib
import json
import os
import tarfile

import pytest

from mediaingredientmech.export import edge_curation as adapter
from mediaingredientmech.export import reviewed_sssom as reviewed
from tests.test_reviewed_sssom import reviewed_fixture  # noqa: F401


@pytest.fixture
def native_fixture(reviewed_fixture, tmp_path):
    # The optional shared runtime is installed by EdgeMech/CLAW callers. The
    # native repository's non-EdgeMech test tiers do not install that project.
    if os.environ.get("MIM_REQUIRE_EDGE_CONTRACT") == "1":
        importlib.import_module("kg_microbe_curation.native")
    else:
        pytest.importorskip(
            "kg_microbe_curation.native",
            reason="requires the shared CLAW native assertion contract",
        )
    root, review_path, bundle = reviewed_fixture
    (root / adapter.SEMANTICS).write_text("Exact lexical SSSOM mapping scope.\n")
    schema = root / adapter.SCHEMA
    schema.parent.mkdir(parents=True)
    schema.write_text("id: https://example.org/mim\n")
    reviewed.export_reviewed(root, review_path, bundle)
    archive = tmp_path / "native.tar.gz"
    commit = "1" * 40
    inputs = ["source.sssom.tsv", "review.json", "evidence.json", "data", "src", adapter.SEMANTICS]

    def pack(extra=None):
        with tarfile.open(archive, "w:gz") as handle:
            for name in inputs:
                handle.add(root / name, arcname=f"MediaIngredientMech-{commit}/{name}")
            if extra is not None:
                name, content, kind = extra
                member = tarfile.TarInfo(f"MediaIngredientMech-{commit}/{name}")
                member.size = len(content)
                member.type = kind
                if kind == tarfile.SYMTYPE:
                    member.linkname = "../../outside"
                handle.addfile(member, io.BytesIO(content))

    pack()
    arguments = {
        "archive": archive,
        "bundle": bundle,
        "source_commit": commit,
        "archive_sha256": reviewed.digest(archive),
        "manifest_sha256": reviewed.digest(bundle / "manifest.json"),
        "review_path": "review.json",
        "positions": (1, 2),
    }
    return arguments, root, pack


def test_preserves_complete_payload_review_and_withheld_scope(native_fixture):
    from kg_microbe_curation.native import validate_native_assertion

    arguments, root, _ = native_fixture
    actual = adapter.build_native_assertions(**arguments)
    _, _, rows = reviewed.read_sssom(root / "source.sssom.tsv")
    native_review = json.loads((root / "review.json").read_text())
    assert len(actual) == 2
    assert [item["assurance"] for item in actual] == [
        "inherited_native_review",
        "native_withheld_decision",
    ]
    for position, item in enumerate(actual, 1):
        validate_native_assertion(item)
        assert item["payload"]["native_payload"] == rows[position - 1]
        assert item["native_review"]["payload"] == native_review["decisions"][position - 1]
        assert item["native_locator"]["selector"] == {"source_position": position}
        assert item["native_locator"]["commit"] == arguments["source_commit"]
        assert item["payload"]["context"]["scope"] == "native_mapping_payload_only"
        assert item["payload"]["context"]["withheld_is_global_ban"] is False
        assert item["independent_scientific_review"] is False
        assert "decision_state" not in item
        assert {entry["locator"]["path"] for entry in item["evidence"]} >= {
            "source.sssom.tsv",
            "review.json",
            "evidence.json",
            native_review["decisions"][position - 1]["owner_record"],
        }
    assert adapter.build_native_assertions(**arguments) == actual


@pytest.mark.parametrize("pin", ["archive_sha256", "manifest_sha256"])
def test_wrong_trusted_pin_fails(native_fixture, pin):
    arguments, _, _ = native_fixture
    with pytest.raises(ValueError, match="hash mismatch"):
        adapter.build_native_assertions(**{**arguments, pin: "0" * 64})


@pytest.mark.parametrize(
    "target",
    [
        "source.sssom.tsv",
        "evidence.json",
        "data/ingredients/mapped/Alpha.yaml",
        "data/ingredients/mapped/Beta.yaml",
    ],
)
def test_all_native_inputs_are_verified_even_outside_selection(native_fixture, target):
    arguments, root, pack = native_fixture
    with (root / target).open("a") as handle:
        handle.write("\n")
    pack()
    with pytest.raises(ValueError, match="Stale"):
        adapter.build_native_assertions(
            **{
                **arguments,
                "archive_sha256": reviewed.digest(arguments["archive"]),
                "positions": (1,),
            }
        )


def test_bundle_partition_cannot_change_even_with_rehashed_manifest(native_fixture):
    arguments, _, _ = native_fixture
    manifest = json.loads((arguments["bundle"] / "manifest.json").read_text())
    output = arguments["bundle"] / reviewed.PRODUCTS[0]
    output.write_text(
        output.read_text().replace("Historical annotation; unnormalized.", "Altered scope")
    )
    manifest["files"][reviewed.PRODUCTS[0]] = reviewed.digest(output)
    (arguments["bundle"] / "manifest.json").write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="partition changed native payloads"):
        adapter.build_native_assertions(
            **{
                **arguments,
                "manifest_sha256": reviewed.digest(arguments["bundle"] / "manifest.json"),
            }
        )


@pytest.mark.parametrize(
    "extra",
    [
        ("source.sssom.tsv", b"duplicate", tarfile.REGTYPE),
        ("../escape", b"escape", tarfile.REGTYPE),
        ("data/ingredients/mapped/Foreign.yaml", b"", tarfile.SYMTYPE),
    ],
)
def test_untrusted_archive_members_fail_closed(native_fixture, extra):
    arguments, _, pack = native_fixture
    pack(extra)
    with pytest.raises(ValueError, match="archive|archived"):
        adapter.build_native_assertions(
            **{**arguments, "archive_sha256": reviewed.digest(arguments["archive"])}
        )


@pytest.mark.parametrize("positions", [(), (1, 1), (0,), (3,), (True,)])
def test_positions_must_identify_exact_source_rows(native_fixture, positions):
    arguments, _, _ = native_fixture
    with pytest.raises(ValueError, match="Source positions"):
        adapter.build_native_assertions(**{**arguments, "positions": positions})


def test_payload_or_evidence_change_invalidates_assertion_identity(native_fixture):
    from kg_microbe_curation.identity import CurationError
    from kg_microbe_curation.native import validate_native_assertion

    arguments, _, _ = native_fixture
    item = adapter.build_native_assertions(**arguments)[0]
    for mutate in (
        lambda changed: changed["payload"]["native_payload"].update(other="new scope"),
        lambda changed: changed["evidence"][0].update(sha256="0" * 64),
        lambda changed: changed.update(independent_scientific_review=True),
    ):
        changed = copy.deepcopy(item)
        mutate(changed)
        with pytest.raises(CurationError):
            validate_native_assertion(changed)
