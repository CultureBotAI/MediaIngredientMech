"""Published identities must not resurrect a reviewed source mapping rejection."""

import csv
import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "check_unified_rejections", Path(__file__).parents[1] / "scripts/check_unified_rejections.py"
)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)


@pytest.fixture
def export(tmp_path):
    ledger = tmp_path / "rejected.tsv"
    ledger.write_text(
        "ingredient_name\trejected_id\tmim_id\treason\n"
        "Trypticase\tCHEBI:78018\tMICRO:0000175\tReviewed detergent mismatch\n"
    )
    row = dict.fromkeys(("ingredient_name", *gate.IDENTITY_COLUMNS), "")
    row.update(ingredient_name="Trypticase", mim_id="MICRO:0000175")
    artifact = tmp_path / "unified.tsv"

    def write(**updates):
        with artifact.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=row, delimiter="\t")
            writer.writeheader()
            writer.writerow(row | updates)
        return artifact, ledger

    return write


@pytest.mark.parametrize("column", gate.IDENTITY_COLUMNS)
def test_rejected_id_is_caught_in_every_identity_column(export, column):
    assert gate.check(*export(**{column: "CHEBI:78018"}))


def test_fixed_row_passes(export):
    assert gate.check(*export()) == []


def test_alias_with_same_identity_is_protected(export):
    assert gate.check(*export(ingredient_name="Trypticase peptone", chebi_id="CHEBI:78018"))


def test_real_detergent_is_not_globally_banned(export):
    assert gate.check(*export(ingredient_name="Dodecylphosphocholine", mim_id="CHEBI:78018", chebi_id="CHEBI:78018")) == []


def test_lost_curated_identity_is_detected(export):
    assert gate.check(*export(mim_id=""))


def test_missing_ledger_fails_closed(export):
    artifact, ledger = export()
    ledger.unlink()
    assert gate.check(artifact, ledger)


def test_ledger_whitespace_cannot_hide_a_rejected_id(export):
    artifact, ledger = export(chebi_id="CHEBI:78018")
    ledger.write_text(ledger.read_text().replace("CHEBI:78018", " CHEBI:78018 "))
    assert gate.check(artifact, ledger)


@pytest.mark.parametrize("text", ["", "ingredient_name\tmim_id\n", "broken\n"])
def test_malformed_ledger_is_not_treated_as_no_rejections(export, text):
    artifact, ledger = export()
    ledger.write_text(text)
    assert gate.check(artifact, ledger)


def test_committed_export_respects_rejections():
    assert gate.check() == []


def test_issue_882_nine_tombstones_keep_explicit_representatives():
    import yaml

    expected = {
        "Cocl2_X_6_H2o": "CHEBI:53503",
        "Na2moo42h2o": "CHEBI:75213",
        "Mgcl2x_6_H2o": "CHEBI:86345",
        "Trisodium_Citrate_X_2_H2o": "CHEBI:32142",
        "Calcium_Chloride": "CHEBI:3312",
        "Na-glutamate": "CHEBI:64243",
        "Sodium_Citrate": "CHEBI:32142",
        "Nah2po4h2o": "CHEBI:114249",
        "Cinnamic_Acid": "CHEBI:35697",
    }
    root = Path(__file__).parents[1] / "data/ingredients/mapped"
    for slug, target in expected.items():
        record = yaml.safe_load((root / f"{slug}.yaml").read_text())
        assert record["mapping_status"] == "REJECTED", slug
        assert record.get("representative") == target, slug


def test_issue_894_hydrate_and_tombstone_identities():
    with gate.ARTIFACT.open(encoding="utf-8", newline="") as handle:
        rows = {r["ingredient_name"]: r for r in csv.DictReader(handle, delimiter="\t")}

    for label in ("MgSO4·H2O", "MgSO4 x H2O", "MgSO4 . H2O", "MgSO4・H2O"):
        row = rows[label]
        assert row["mapping_status"] == "MAPPED"
        assert row["mim_id"] == "cas:14168-73-1"
        assert row["cas_rn"] == "14168-73-1"
        assert row["chebi_id"] == ""
        assert row["culturemech_term_id"] == ""
        assert row["kg_microbe_node_id"] == ""

    mgso4_7h2o = rows["MgSO .7H O"]
    assert mgso4_7h2o["mapping_status"] == "MAPPED"
    assert mgso4_7h2o["mim_id"] == "CHEBI:31795"
    assert mgso4_7h2o["chebi_id"] == "CHEBI:31795"
    assert mgso4_7h2o["cas_rn"] == "10034-99-8"

    for label in ("L-Cysteine hydrochloride monohydrate", "L--Cysteine・HCL・H2O"):
        row = rows[label]
        assert row["mapping_status"] == "MAPPED"
        assert row["mim_id"] == "CHEBI:91248"
        assert row["chebi_id"] == "CHEBI:91248"


def test_issue_882_merge_tombstones_and_unified_identities():
    import yaml

    merge_actions = {"MERGED_INTO", "MERGED_INTO_EXISTING", "MERGED"}

    def mim_merge_target(data: dict) -> str:
        representative = (data.get("representative") or "").strip()
        if representative:
            return representative
        for event in reversed(data.get("curation_history") or []):
            if event.get("action") in merge_actions:
                return (data.get("identifier") or "").strip()
            if event.get("new_status") == "REJECTED":
                return ""
        return ""

    root = Path(__file__).parents[1]
    live_ids: set[str] = set()
    tombstones: list[tuple[str, dict]] = []

    for sub in ("mapped", "unmapped"):
        for path in sorted((root / "data" / "ingredients" / sub).glob("*.yaml")):
            rec = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            status = rec.get("mapping_status")
            if status in ("MAPPED", "UNMAPPED"):
                for oid in (
                    rec.get("identifier"),
                    (rec.get("ontology_mapping") or {}).get("ontology_id"),
                ):
                    if oid:
                        live_ids.add(oid)
            elif status == "REJECTED":
                events = rec.get("curation_history") or []
                if rec.get("representative") or any(ev.get("action") in merge_actions for ev in events):
                    tombstones.append((path.name, rec))

    assert len(tombstones) >= 70

    for name, rec in tombstones:
        target = mim_merge_target(rec)
        assert target in live_ids, f"Merge tombstone {name} fails to resolve to a live record (target={target!r})"

    with gate.ARTIFACT.open(encoding="utf-8", newline="") as handle:
        rows = {r["ingredient_name"]: r for r in csv.DictReader(handle, delimiter="\t")}

    rejected_rows = [k for k, r in rows.items() if r["mapping_status"] == "REJECTED"]
    assert rejected_rows == [], f"Unexpected REJECTED rows in UNIFIED_INGREDIENT_MAPPING.tsv: {rejected_rows}"

    expected_mapped = {
        "CoCl2 x 6 H2O": ("CHEBI:53503", "CHEBI:53503"),
        "CoCl2·6H2O": ("CHEBI:53503", "CHEBI:53503"),
        "CoCl2・6H2O": ("CHEBI:53503", "CHEBI:53503"),
        "CoCl2 x 6H2O": ("CHEBI:53503", "CHEBI:53503"),
        "CoCl2 . 6H2O": ("CHEBI:53503", "CHEBI:53503"),
        "CoCl2.6H2O": ("CHEBI:53503", "CHEBI:53503"),
        "CoCl2 · 6H2O": ("CHEBI:53503", "CHEBI:53503"),
        "CoCl2 × 6H2O": ("CHEBI:53503", "CHEBI:53503"),
        "Na2MoO4·2H2O": ("CHEBI:75213", "CHEBI:75213"),
        "Na2MoO4・2H2O": ("CHEBI:75213", "CHEBI:75213"),
        "Na2MoO4 x 2H2O": ("CHEBI:75213", "CHEBI:75213"),
        "Na2MoO4 . 2H2O": ("CHEBI:75213", "CHEBI:75213"),
        "Na2MoO4 · 2H2O": ("CHEBI:75213", "CHEBI:75213"),
        "Na2MoO4. 2H2O": ("CHEBI:75213", "CHEBI:75213"),
        "Sodium citrate": ("CHEBI:32142", "CHEBI:32142"),
        "Sodium Citrate": ("CHEBI:32142", "CHEBI:32142"),
        "sodium citrate": ("CHEBI:32142", "CHEBI:32142"),
        "Trisodium citrate x 2 H2O": ("CHEBI:32142", "CHEBI:32142"),
        "Trisodium citrate・2H2O": ("CHEBI:32142", "CHEBI:32142"),
        "Calcium chloride": ("CHEBI:3312", "CHEBI:3312"),
        "calcium chloride": ("CHEBI:3312", "CHEBI:3312"),
        "Calcium Chloride": ("CHEBI:3312", "CHEBI:3312"),
        "MgCl2x 6 H2O": ("CHEBI:86345", "CHEBI:86345"),
        "MgCl2 x 7H2O": ("kgmicrobe.compound:mgcl2_x_7_h2o", ""),
        "Na-glutamate": ("CHEBI:64243", "CHEBI:64243"),
    }
    for label, (exp_mim, exp_chebi) in expected_mapped.items():
        row = rows[label]
        assert row["mapping_status"] == "MAPPED", label
        assert row["mim_id"] == exp_mim, label
        assert row["chebi_id"] == exp_chebi, label

    expected_unmapped = {
        "Na2MoO4 x H2O": "UNMAPPED_0851",
        "Na2MoO4.H2O": "UNMAPPED_0851",
        "Na2MoO4 × H2O": "UNMAPPED_0851",
        "Na2MoO4 . H2O": "UNMAPPED_0851",
        "Na2MoO4 · H2O": "UNMAPPED_0851",
        "Trisodium citrate・3H2O": "UNMAPPED_0852",
        "Trisodium citrate x 3 H2O": "UNMAPPED_0852",
    }
    for label, exp_mim in expected_unmapped.items():
        row = rows[label]
        assert row["mapping_status"] == "UNMAPPED", label
        assert row["mim_id"] == exp_mim, label
        assert row["chebi_id"] == "", label
        assert row["culturemech_term_id"] == "", label


def test_issue_869_and_808_no_stale_chebi_on_local_or_hydrate_records(export):
    with gate.ARTIFACT.open(encoding="utf-8", newline="") as handle:
        all_rows = list(csv.DictReader(handle, delimiter="\t"))

    kgm_compound_with_chebi = [
        (r["ingredient_name"], r["mim_id"], r["chebi_id"])
        for r in all_rows
        if r["mim_id"].startswith("kgmicrobe.compound:") and r["chebi_id"]
    ]
    assert kgm_compound_with_chebi == [], (
        f"kgmicrobe.compound rows still publishing a stale chebi_id (#869): {kgm_compound_with_chebi}"
    )

    rows_by_name = {r["ingredient_name"]: r for r in all_rows}
    for label, exp_mim in (
        ("Adenine hydrochloride hydrate", "cas:2922-28-3"),
        ("Maltose monohydrate", "cas:6363-53-7"),
        ("a-Ketoglutaric acid disodium salt hydrate", "cas:305-72-6"),
        ("Trisodium citrate x H2O", "mesh:C514290"),
    ):
        row = rows_by_name[label]
        assert row["mapping_status"] == "MAPPED", label
        assert row["mim_id"] == exp_mim, label
        assert row["chebi_id"] == "", label
        assert row["culturemech_term_id"] == "", label

    artifact, ledger = export()
    ledger.write_text(
        "ingredient_name\trejected_id\tmim_id\treason\n"
        "Na2MoO4 x H2O\tCHEBI:75215\tUNMAPPED_0851\tunmapped rejection not allowed\n"
    )
    assert gate.check(artifact, ledger) == [f"{ledger}: duplicate or invalid rejection"]

