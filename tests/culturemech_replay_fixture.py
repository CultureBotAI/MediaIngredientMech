"""Authentic tiny source fixtures for #1882; never a real campaign invocation."""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

import yaml

ASSETS = Path(__file__).parent / "fixtures/native_cm_v3_replay"


def fingerprint(path):
    raw = Path(path).read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def write_tsv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", newline="") as stream:
        writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def synthetic_recipe():
    water = {"preferred_term": "water", "term": {"id": "CHEBI:15377"}}
    modifications = [
        "Set water to 0.25 g per synthetic batch; final volume is unasserted.",
        "Remove Synthetic unresolved material.",
        "Add water, with its supplied identity form unresolved in this synthetic source.",
    ]
    changes = []
    for index, (action, ingredient) in enumerate(
        [("SET_AMOUNT", water), ("REMOVE", {"preferred_term": "Synthetic unresolved material"})]
    ):
        change = {
            "action": action,
            "ingredient": copy.deepcopy(ingredient),
            "stage": "synthetic assay",
            "source_modification_index": index,
            "source_text": modifications[index],
            "evidence": [
                {
                    "reference": "https://example.invalid/synthetic-cm-v3",
                    "supports": "SUPPORT",
                    "snippet": modifications[index],
                    "explanation": "Explicit synthetic fixture statement, not scientific approval.",
                }
            ],
        }
        if action == "SET_AMOUNT":
            change["amount"] = {
                "value": "0.25",
                "unit": "G",
                "basis": "PER_BATCH",
                "basis_statement": "Literal synthetic batch amount; final volume unasserted.",
            }
        changes.append(change)
    return {
        "id": "CultureMech:000001",
        "name": "Synthetic native replay fixture",
        "physical_state": "LIQUID",
        "category": "bacterial",
        "ingredients": [copy.deepcopy(water)],
        "variants": [
            {
                "name": "Synthetic assay",
                "modifications": modifications,
                "ingredient_changes": changes,
                "ingredient_mentions": [
                    {
                        "source_label": "water",
                        "reported_action": "ADD",
                        "stage": "synthetic assay",
                        "source_modification_index": 2,
                        "source_text": modifications[2],
                        "reason": "Synthetic source leaves supplied identity form unresolved.",
                        "held_fields": ["IDENTITY_FORM"],
                        "evidence": [],
                    }
                ],
            }
        ],
    }


def make_cm_handoff(root):
    """Run genuine archived generation on one newly created synthetic recipe."""
    root.mkdir(parents=True, exist_ok=False)
    provenance = json.loads((ASSETS / "provenance.json").read_text())
    archive = ASSETS / "cm-producer-code.tar.gz"
    assert fingerprint(archive)["sha256"] == provenance["fixture_archive_sha256"]
    with tarfile.open(archive) as stream:
        members = stream.getmembers()
        expected = {"producer/" + name for name in provenance["members"]}
        assert len(members) == len(expected)
        assert {member.name for member in members} == expected
        assert all(member.isfile() and not member.islnk() for member in members)
        stream.extractall(root, filter="data")
    producer = root / "producer"
    for name, expected in provenance["members"].items():
        assert fingerprint(producer / name) == expected
    recipe = synthetic_recipe()
    before = copy.deepcopy(recipe)
    del before["variants"][0]["ingredient_changes"]
    del before["variants"][0]["ingredient_mentions"]
    preimage = root / "synthetic-preimage.yaml"
    preimage.write_text(yaml.safe_dump(before, sort_keys=False))
    relative = "bacterial/tiny.yaml"
    path = producer / "data/normalized_yaml" / relative
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(recipe, sort_keys=False))
    for args in (
        ("init",),
        ("config", "user.name", "Synthetic fixture"),
        ("config", "user.email", "fixture@example.invalid"),
        ("add", "."),
        ("commit", "-m", "Synthetic CM v3 fixture; no real recipes"),
    ):
        subprocess.run(["git", *args], cwd=producer, check=True, capture_output=True, timeout=30)
    handoff = root / "handoff"
    handoff.mkdir()
    bundle = handoff / "bundle"
    command = [
        sys.executable,
        "-B",
        "scripts/ingredient_release_bundle.py",
        "build",
        "--input-dir",
        str(producer / "data/normalized_yaml"),
        "--output-dir",
        str(bundle),
    ]
    result = subprocess.run(command, cwd=producer, capture_output=True, timeout=300)
    (root / "build.stdout").write_bytes(result.stdout)
    (root / "build.stderr").write_bytes(result.stderr)
    write_json(root / "build-command.json", {"argv": command, "exit": result.returncode})
    assert result.returncode == 0, result.stderr.decode(errors="replace")
    manifest = json.loads((bundle / "manifest.json").read_text())
    assert manifest["scope"] == "full_catalog_direct_ingredients"
    assert manifest["git"]["dirty"] is False
    assert manifest["counts"]["scanned_records"] == 1
    verify_command = [
        sys.executable,
        "-I",
        "-S",
        "-B",
        "scripts/ingredient_release_bundle.py",
        "verify",
        "--bundle-dir",
        str(bundle),
        "--expected-manifest-sha256",
        fingerprint(bundle / "manifest.json")["sha256"],
    ]
    verified = subprocess.run(verify_command, cwd=producer, capture_output=True, timeout=300)
    (root / "verify.stdout").write_bytes(verified.stdout)
    (root / "verify.stderr").write_bytes(verified.stderr)
    write_json(root / "verify-command.json", {"argv": verify_command, "exit": verified.returncode})
    assert verified.returncode == 0, verified.stderr.decode(errors="replace")
    verified_value = json.loads(verified.stdout)
    assert verified_value["status"] == "VERIFIED_CANDIDATE"
    assert verified_value["assurance"] == "externally_pinned_manifest"
    assert verified_value["counts"] == manifest["counts"]
    source_archive = handoff / "producer-source.tar.gz"
    subprocess.run(
        [
            "git",
            "archive",
            "--format=tar.gz",
            "--prefix=producer/",
            "--output",
            str(source_archive),
            "HEAD",
        ],
        cwd=producer,
        check=True,
        capture_output=True,
        timeout=30,
    )
    queue = handoff / "original-review-queue.tsv"
    write_tsv(
        queue,
        ["source_path", "source_sha256"],
        [{"source_path": relative, "source_sha256": fingerprint(preimage)["sha256"]}],
    )
    coverage_path = handoff / "coverage/coverage.tsv"
    write_tsv(
        coverage_path,
        ["source_path", "status"],
        [{"source_path": relative, "status": "STRUCTURED_WITH_HOLD"}],
    )
    coverage = {
        "result": "PASS",
        "mode": "postapply",
        "applied_assertions": manifest["counts"]["variant_change_events"],
        "held_mentions": manifest["counts"]["variant_held_mentions"],
        "coverage_sha256": fingerprint(coverage_path)["sha256"],
        "queue_sha256": fingerprint(queue)["sha256"],
        "record_snapshots": [
            {
                "path": "data/normalized_yaml/" + relative,
                "base_sha256": fingerprint(preimage)["sha256"],
                "current_sha256": fingerprint(path)["sha256"],
            }
        ],
        "queue_rows": 1,
        "queue_recipes": 1,
        "dispositions": {"STRUCTURED_WITH_HOLD": 1},
    }
    write_json(handoff / "coverage/summary.json", coverage)
    receipt = {
        "status": "VERIFIED_SOURCE_CANDIDATE_PENDING_ADOPTION",
        "contract": manifest["contract"],
        "producer_commit": manifest["git"]["commit"],
        "manifest_sha256": fingerprint(bundle / "manifest.json")["sha256"],
        "source_archive_sha256": fingerprint(source_archive)["sha256"],
        "coverage_summary_sha256": fingerprint(handoff / "coverage/summary.json")["sha256"],
        "queue_sha256": fingerprint(queue)["sha256"],
    }
    write_json(handoff / "handoff.json", receipt)
    return {
        "root": root,
        "producer": producer,
        "handoff": handoff,
        "manifest": manifest,
        "pin": fingerprint(handoff / "handoff.json")["sha256"],
    }


class FixtureInputs:
    """Small capture adapter for constructing synthetic historical fixtures only."""

    def __init__(self, root):
        self.root = root
        self.bytes = {}
        self.hashes = {}

    def read(self, name, expected=None):
        raw = (self.root / name).read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assert expected is None or digest == expected
        assert name not in self.bytes or self.bytes[name] == raw
        self.bytes[name], self.hashes[name] = raw, digest
        return raw

    def recheck(self):
        for name, raw in self.bytes.items():
            assert (self.root / name).read_bytes() == raw


def make_historical_review(consumer, native):
    """A legacy owner/canonical review, separate from current permanent owners."""
    owner = "data/ingredients/mapped/Water.yaml"
    path = consumer / owner
    path.parent.mkdir(parents=True)
    path.write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:15377",
                "preferred_term": "water",
                "mapping_status": "MAPPED",
                "synonyms": [],
            }
        )
    )
    row = {
        "subject_id": "MIM:Water",
        "subject_label": "water",
        "predicate_id": "skos:exactMatch",
        "object_id": "CHEBI:15377",
        "object_label": "water",
        "other": "",
        "confidence": "1",
        "comment": "Synthetic historical exact row; retain commentary.",
    }
    source = consumer / "mappings/historical.sssom.tsv"
    source.parent.mkdir()
    source.write_bytes(
        b"# mapping_set_id: https://example.invalid/synthetic-canonical\n# predicate_semantics: skos\n# license: https://creativecommons.org/publicdomain/zero/1.0/\n# curie_map:\n#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_\n"
        + native._tsv(list(row), [row])
    )
    decision = {
        "source_position": 1,
        "row_sha256": native.row_sha256(row),
        "owner_record": owner,
        "disposition": "SUPPORTED",
        "review_reason": "Explicit synthetic exact water identity; not a scientific approval.",
        "review_evidence": "reviews/canonical-evidence.json",
        "evidence_key": "water",
    }
    entry = {key: decision[key] for key in ("row_sha256", "disposition", "review_reason")}
    entry["owner_record_sha256"] = native.digest(path)
    write_json(consumer / "reviews/canonical-evidence.json", {"entries": {"water": entry}})
    review = {
        "schema_version": 1,
        "source_sssom": "mappings/historical.sssom.tsv",
        "source_sha256": native.digest(source),
        "inputs": {
            "reviews/canonical-evidence.json": native.digest(
                consumer / "reviews/canonical-evidence.json"
            )
        },
        "record_inputs": {owner: native.digest(path)},
        "decisions": [decision],
    }
    write_json(consumer / "reviews/canonical.json", review)
    return "reviews/canonical.json"


def make_binding_review(consumer, prepared, pin, intake):
    packet = json.loads((prepared / "review-packet.json").read_text())
    decisions, entries = [], {}
    for case in packet["cases"]:
        candidate = case["candidate"]
        supported = (
            case["positive_occurrences"] > 0
            and case["context"]["preferred_term"] == "water"
            and not set(case["context"].get("held_fields", [])) & {"SOURCE_CLAIM", "IDENTITY_FORM"}
        )
        decision = {
            "case_id": case["case_id"],
            "row_sha256": intake.payload_sha256(case),
            "owner_record": candidate.get("owner_record", "source/bundle/manifest.json"),
            "disposition": "SUPPORTED" if supported else "WITHHOLD",
            "review_reason": "Synthetic fixture: preserve unresolved removal and supplied-form hold.",
            "review_evidence": "reviews/binding-evidence.json",
            "evidence_key": case["case_id"],
        }
        if supported:
            decision["canonical_row_sha256"] = candidate["supported_canonical_rows"][0][
                "row_sha256"
            ]
        entry = {
            key: decision[key]
            for key in ("row_sha256", "owner_record", "disposition", "review_reason")
        }
        entry["owner_record_sha256"] = candidate.get(
            "owner_record_sha256", packet["source_manifest_sha256"]
        )
        decisions.append(decision)
        entries[case["case_id"]] = entry
    write_json(consumer / "reviews/binding-evidence.json", {"entries": entries})
    review = {
        "schema_version": 1,
        "intake_sha256": pin,
        "decisions": decisions,
        "inputs": {
            "reviews/binding-evidence.json": fingerprint(
                consumer / "reviews/binding-evidence.json"
            )["sha256"]
        },
    }
    write_json(consumer / "reviews/binding-review.json", review)
    return "reviews/binding-review.json"


def make_package(current_root, *, cm=None):
    """Create genuine prepared/reviewed synthetic intake for replay qualification."""
    from mediaingredientmech.export import culturemech_replay as replay
    from mediaingredientmech.export import culturemech_replay_process as process

    if cm is None:
        cm = make_cm_handoff(current_root / ".temp/cm-source-origin")
    inputs = FixtureInputs(current_root)
    plan = process.prepare_plan(
        cm["producer"] / "scripts/ingredient_release_bundle.py",
        cm["handoff"] / "bundle",
        fingerprint(cm["handoff"] / "bundle/manifest.json")["sha256"],
    )
    facade = process.VerifierProcess(plan, sys.executable, cm["producer"])
    modules = replay.load_historical_modules(inputs, current_root / ".temp/fixture-capsule", facade)
    old, later = modules["prepare"], modules["review"]
    package = current_root / "cm-package"
    consumer = package / "consumer"
    consumer.mkdir(parents=True)
    canonical_review = make_historical_review(consumer, old.reviewed_sssom)
    prepared = consumer / ".temp/prepared"
    manifest = old.prepare(
        cm["handoff"],
        cm["pin"],
        prepared,
        Path(sys.executable),
        root=consumer,
        producer_root=cm["producer"],
        review=canonical_review,
    )
    assert manifest["consumer_implementation"] == {"sha256": replay.PREPARATION_SHA, "bytes": 47572}
    pin = fingerprint(prepared / "intake.json")["sha256"]
    review = make_binding_review(consumer, prepared, pin, later)
    reviewed = consumer / ".temp/reviewed"
    final = later.finalize(prepared, pin, review, reviewed, root=consumer)
    # The synthetic package retains actual historical helper resources and origin.
    for resource in replay.RESOURCES:
        target = consumer / resource
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(current_root / resource, target)
    source_archive = package / "consumer-source.tar.gz"
    with tarfile.open(source_archive, "w:gz") as stream:
        stream.add(consumer, arcname="consumer")
    index = {
        "schema_version": 1,
        "status": "ISOLATED_REVIEWED_INTAKE_VERIFICATION_PACKAGE",
        "consumer_commit": replay.VERIFICATION_REVISION,
        "files": {
            p.relative_to(package).as_posix(): fingerprint(p)
            for p in sorted(package.rglob("*"))
            if p.is_file()
        },
        "intake_path": ".temp/prepared",
        "intake_sha256": pin,
        "review_path": review,
        "reviewed_path": ".temp/reviewed",
        "reviewed_sha256": fingerprint(reviewed / "reviewed-intake.json")["sha256"],
        "limitations": "Entirely synthetic data fixture; authentic historical implementation origin only, not a real accepted release or owner adoption.",
    }
    write_json(package / "package.json", index)
    return {
        "reference": {
            "path": "cm-package/package.json",
            "sha256": fingerprint(package / "package.json")["sha256"],
        },
        "package": package,
        "consumer": consumer,
        "prepared": prepared,
        "reviewed": reviewed,
        "intake": manifest,
        "final": final,
        "cm": cm,
        "modules": modules,
    }


def reseal_package_inventory(package):
    """Update only inventory pins after an intentional adversarial fixture edit.

    This grants no native validity: tests must still execute the real replay and
    prove that freshly pinned but non-reproducible content is refused.
    """
    for directory, manifest_name in (
        (package["prepared"], "intake.json"),
        (package["reviewed"], "reviewed-intake.json"),
    ):
        path = directory / manifest_name
        manifest = json.loads(path.read_bytes())
        manifest["files"] = {
            p.relative_to(directory).as_posix(): fingerprint(p)
            for p in sorted(directory.rglob("*"))
            if p.is_file() and p != path
        }
        write_json(path, manifest)
    index_path = package["package"] / "package.json"
    index = json.loads(index_path.read_bytes())
    index["intake_sha256"] = fingerprint(package["prepared"] / "intake.json")["sha256"]
    index["reviewed_sha256"] = fingerprint(package["reviewed"] / "reviewed-intake.json")["sha256"]
    index["files"] = {
        p.relative_to(package["package"]).as_posix(): fingerprint(p)
        for p in sorted(package["package"].rglob("*"))
        if p.is_file() and p != index_path
    }
    write_json(index_path, index)
    package["reference"]["sha256"] = fingerprint(index_path)["sha256"]


def refresh_canonical_review_reference(package):
    """Rebind adversarial canonical inputs without granting native validity."""
    pin = fingerprint(package["consumer"] / "reviews/canonical.json")["sha256"]
    for name in ("intake.json", "review-packet.json"):
        path = package["prepared"] / name
        value = json.loads(path.read_bytes())
        value["canonical_review_sha256"] = pin
        write_json(path, value)
    reseal_package_inventory(package)
