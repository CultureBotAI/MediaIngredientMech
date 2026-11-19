"""#1265 identity-only proof rejects any accompanying scientific change."""

import pytest
import yaml

from mediaingredientmech import identity_projection as ip
from mediaingredientmech.stable_ids import Mint, Registry, dump_lifecycle, dump_registry, MIM_PREFIX


def fixture():
    name = "data/ingredients/mapped/Water.yaml"
    old = {"preferred_term": "Water", "identifier": "CHEBI:15377", "mapping_status": "MAPPED",
           "curation_history": [{"action": "REVIEWED", "changes": "Historical review remains exact"}],
           "scientific_flag": True}
    event = {"timestamp": "2026-11-08T22:01:42+00:00", "curator": "codex",
             "action": "ASSIGNED_MIM_ID", "llm_assisted": True,
             "changes": "#1265: assigned permanent MIM:0000001; retained mapping identifier and legacy aliases."}
    new = dict(old, mim_id="MIM:0000001", legacy_identifiers=["MIM:Water", "CHEBI:15377"],
               curation_history=[*old["curation_history"], event])
    table = ("# mapping_set_id: test:mappings\n# predicate_semantics: skos\n# curie_map:\n"
             "#   MIM: https://example.test/legacy/\n"
             "subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tother\n"
             "MIM:Water\tWater\tskos:exactMatch\tCHEBI:15377\twater\t\n").encode()
    migrated = table.replace(b"https://example.test/legacy/", MIM_PREFIX.encode()).replace(b"MIM:Water\t", b"MIM:0000001\t")
    registry = Registry((Mint("MIM:0000001", "Water", "2026-11-08"),))
    before = {name: yaml.safe_dump(old).encode(), ip.SOURCE: table}
    after = {name: yaml.safe_dump(new).encode(), ip.SOURCE: migrated,
             ip.REGISTRY: dump_registry(registry), ip.LIFECYCLE: dump_lifecycle(registry)}
    manifest = {"schema_version": 1, "kind": ip.KIND, "source_commit": ip.BASE_COMMIT,
                "minted_on": "2026-11-08", "timestamp": event["timestamp"], "approval": "NONE",
                "scientific_approval_added": False, "registry_path": ip.REGISTRY,
                "lifecycle_path": ip.LIFECYCLE, "records": [{"path": name, "mim_id": "MIM:0000001",
                    "legacy_identifiers": new["legacy_identifiers"], "before_sha256": ip.sha(before[name]),
                    "after_sha256": ip.sha(after[name])}],
                "before_sssom_sha256": ip.sha(table), "after_sssom_sha256": ip.sha(migrated),
                "registry_sha256": ip.sha(after[ip.REGISTRY]), "lifecycle_sha256": ip.sha(after[ip.LIFECYCLE])}
    return manifest, before, after, name


def test_identity_only_transition_preserves_semantics_and_positions():
    manifest, before, after, _ = fixture()
    proof = ip.verify_transition(manifest, before, after)
    assert proof["aliases"] == {"MIM:Water": "MIM:0000001"}
    assert proof["rows"][0] == dict(proof["old_rows"][0], subject_id="MIM:0000001")
    assert manifest["scientific_approval_added"] is False


@pytest.mark.parametrize("change", ["biology", "history", "extra_event", "wrong_event", "alias_loss", "bool_type", "event_bool_type"])
def test_rehashed_record_mutations_are_not_identity_only(change):
    manifest, before, after, name = fixture()
    record = yaml.safe_load(after[name])
    if change == "biology":
        record["identifier"] = "CHEBI:999"
    elif change == "history":
        record["curation_history"][0]["changes"] = "Rewritten review"
    elif change == "extra_event":
        record["curation_history"].append(record["curation_history"][-1])
    elif change == "wrong_event":
        record["curation_history"][-1]["action"] = "REVIEWED"
    elif change == "alias_loss":
        record["legacy_identifiers"].pop()
        manifest["records"][0]["legacy_identifiers"] = record["legacy_identifiers"]
    elif change == "bool_type":
        record["scientific_flag"] = 1
    else:
        record["curation_history"][-1]["llm_assisted"] = 1
    after[name] = yaml.safe_dump(record).encode()
    manifest["records"][0]["after_sha256"] = ip.sha(after[name])
    with pytest.raises(ValueError, match="Identity projection"):
        ip.verify_transition(manifest, before, after)


@pytest.mark.parametrize("old,new", [(b"CHEBI:15377", b"CHEBI:999"), (b"skos:exactMatch", b"skos:broadMatch"),
                                     (b"\twater\t", b"\tother\t"), (b"MIM:0000001", b"MIM:0000002")])
def test_rehashed_mapping_mutation_refused(old, new):
    manifest, before, after, _ = fixture()
    after[ip.SOURCE] = after[ip.SOURCE].replace(old, new)
    manifest["after_sssom_sha256"] = ip.sha(after[ip.SOURCE])
    with pytest.raises(ValueError, match="administrative subject ID"):
        ip.verify_transition(manifest, before, after)


@pytest.mark.parametrize("change", ["unlisted_record", "missing_record", "registry_reassignment", "authority", "status"])
def test_complete_scope_and_no_new_authority(change):
    manifest, before, after, name = fixture()
    if change == "unlisted_record":
        after["data/ingredients/mapped/Other.yaml"] = after[name]
    elif change == "missing_record":
        del after[name]
    elif change == "registry_reassignment":
        after[ip.REGISTRY] = after[ip.REGISTRY].replace(b"MIM:0000001", b"MIM:0000002")
        manifest["registry_sha256"] = ip.sha(after[ip.REGISTRY])
    elif change == "authority":
        manifest["scientific_approval_added"] = True
    else:
        manifest["approval"] = "SUPPORTED"
    with pytest.raises(ValueError):
        ip.verify_transition(manifest, before, after)


def test_projection_header_keeps_original_authority_separate():
    manifest, before, after, _ = fixture()
    proof = ip.Proof(None, manifest, before, after, {}, {ip.MANIFEST: ip.encode(manifest)})
    original = b'{"historical":"bytes"}'
    header = ip.projection_header(proof, "reports/original.json", original)
    assert header["original_report_sha256"] == ip.sha(original)
    assert header["manifest_sha256"] == ip.sha(ip.encode(manifest))
    assert header["scientific_approval_added"] is False
    assert "approval" not in header


def test_native_review_ownership_uses_permanent_id_after_filename_change(tmp_path):
    from mediaingredientmech.export.reviewed_sssom import _owners, registry_identity_candidates
    path = tmp_path / "data/ingredients/mapped/New_Name.yaml"
    path.parent.mkdir(parents=True)
    record = {"mim_id": "MIM:0000001", "preferred_term": "Water", "mapping_status": "MAPPED",
              "identifier": "kgmicrobe.compound:old_name", "legacy_identifiers": ["MIM:Old_Name"]}
    path.write_text(yaml.safe_dump(record))
    owners, _ = _owners(tmp_path, [{"subject_id": "MIM:0000001", "subject_label": "Water"}])
    assert owners == ["data/ingredients/mapped/New_Name.yaml"]
    candidates = registry_identity_candidates(record, "MIM:0000001")
    assert "kgmicrobe.compound:old_name" in candidates
    assert "kgmicrobe.compound:0000001" not in candidates
    with pytest.raises(ValueError, match="No unique independent owner"):
        _owners(tmp_path, [{"subject_id": "MIM:New_Name", "subject_label": "Water"}])


@pytest.mark.parametrize("nested", [False, True])
def test_rehashed_duplicate_scientific_yaml_key_is_refused(nested):
    manifest, before, after, name = fixture()
    if nested:
        needle = b"  llm_assisted: true"
        assert needle in after[name]
        after[name] = after[name].replace(needle, b"  llm_assisted: false\n" + needle, 1)
    else:
        after[name] = b"preferred_term: Unreviewed duplicate value\n" + after[name]
    manifest["records"][0]["after_sha256"] = ip.sha(after[name])
    with pytest.raises(ValueError, match="duplicate YAML record key"):
        ip.verify_transition(manifest, before, after)
