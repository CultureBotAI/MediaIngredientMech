"""Two synthetic FORM authorities; no real ingredient receives scientific approval."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import yaml

from mediaingredientmech.export import reviewed_sssom
from mediaingredientmech.record_refresh import RecordRefreshes
from mediaingredientmech.validation import mapping_change_receipts as mcr
from tests.test_form_mapping_followup import (
    AUTHORITY,
    CAPTURE,
    KINDS,
    OTHER,
    OWNER,
    PAIR,
    PRIOR,
    ROOT,
    Fixture,
    assembled,
    change,
    git,
    module,
    owner_link,
    receipt,
    row,
    selector,
    sha,
    sssom,
    write,
)

SECOND_OWNER = "data/ingredients/mapped/Synthetic_sodium_hydrate.yaml"
SECOND_AUTHORITY = "reports/test-only/second-form.json"
SECOND_CAPTURE = "reports/test-only/second-source.txt"
SECOND_PRIOR = "reports/test-only/second-prior.json"
SECOND_PAIR = "reviews/structured/20260101T000001Z-test-only-second-form/review.yaml"


def save_second_pair(form, old_rows, old_owner):
    """Reuse native fixture shape with separate exact inputs, targets and checkpoint."""
    write(
        form.root,
        SECOND_CAPTURE,
        b"Synthetic sodium-like test fixture only; no source was fetched or reviewed.\n",
    )
    write(
        form.root,
        SECOND_PRIOR,
        {
            "source_sssom_sha256": sha(sssom(old_rows)),
            "entries": {
                kind: {
                    "owner_record": SECOND_OWNER,
                    "owner_record_sha256": sha(old_owner),
                    "mapping": old_rows[position - 1],
                    "row_sha256": reviewed_sssom.row_sha256(old_rows[position - 1]),
                    "disposition": "WITHHOLD",
                }
                for kind, position in zip(KINDS[:2], (5, 6), strict=True)
            },
        },
    )
    evidence = {
        path: sha((form.root / path).read_bytes()) for path in (SECOND_CAPTURE, SECOND_PRIOR)
    }
    git(form.root, "add", ".")
    git(form.root, "commit", "-m", "Second synthetic source endpoint")
    review = copy.deepcopy(form.review)
    review["review_id"] = Path(SECOND_PAIR).parent.name
    review["finished_at"] = "2026-01-01T00:00:01Z"
    review["title"] = "Second synthetic form admission; no real sodium review"
    review["source"] = {
        "git_revision": git(form.root, "rev-parse", "HEAD"),
        "state": "git_commit",
        "inputs": [
            {"path": path, "sha256": digest, "role": "Synthetic endpoint input"}
            for path, digest in (
                {
                    mcr.SSSOM_SOURCE: form.chain["reviewed_sha256"],
                    SECOND_OWNER: form.hashes[SECOND_OWNER],
                }
                | evidence
            ).items()
        ],
    }
    review["evidence"][0].update(reference=SECOND_CAPTURE, snapshot_sha256=evidence[SECOND_CAPTURE])
    decisions = copy.deepcopy(form.document["decisions"])
    for target, entry, position in zip(review["targets"], decisions, (5, 6, 7), strict=True):
        mapping = copy.deepcopy(form.rows[position - 1])
        digest = reviewed_sssom.row_sha256(mapping)
        target["selector"] = selector(mapping)
        target["semantic_digest"]["sha256"] = digest
        target["owner_paths"][0]["path"] = SECOND_OWNER
        entry.update(source_position=position, mapping=mapping, row_sha256=digest)
        if entry["prior_basis"] is not None:
            entry["prior_basis"]["path"] = SECOND_PRIOR
    raw = yaml.safe_dump(review, sort_keys=False, allow_unicode=True).encode()
    markdown = form.native.render_markdown(review, form.root / "schema/record_review.yaml").encode()
    write(form.root, SECOND_PAIR, raw)
    write(form.root, str(Path(SECOND_PAIR).with_name("review.md")), markdown)
    assert (
        form.native.parse_review_bundle(
            SECOND_PAIR, raw, markdown, form.root / "schema/record_review.yaml"
        )
        == review
    )
    assert form.native.source_provenance(form.root, review)["status"] == "git_commit_verified"
    endpoint = form.chain["receipt_paths"][2]
    write(
        form.root,
        SECOND_AUTHORITY,
        {
            "schema_version": 1,
            "owner_record": SECOND_OWNER,
            "owner_record_sha256": form.hashes[SECOND_OWNER],
            "checkpoint": {
                "sequence": 3,
                "path": endpoint,
                "sha256": form.chain["receipt_inputs"][endpoint],
                "after_sha256": form.chain["reviewed_sha256"],
            },
            "native_review": {
                "path": SECOND_PAIR,
                "sha256": sha(raw),
                "markdown_sha256": sha(markdown),
            },
            "evidence_inputs": evidence,
            "decisions": decisions,
        },
    )


def test_sequential_forms_admit_only_second_triplet_and_never_renew_role(tmp_path, monkeypatch):
    form = Fixture(tmp_path)
    # Reuse the existing native assembly input scaffolding, not patched validators.
    assembled(form, monkeypatch)
    second_record = {
        "identifier": "cas:7791-07-3",
        "preferred_term": "Synthetic sodium hydrate",
        "mapping_status": "MAPPED",
        "ingredient_type": "SINGLE_INGREDIENT",
        "ontology_mapping": {
            "ontology_id": "CHEBI:132103",
            "ontology_label": "synthetic sodium parent",
            "mapping_quality": "CLOSE_MATCH",
        },
        "synonyms": [],
        "cellular_metabolic_roles": [{"role": "ELECTRON_ACCEPTOR", "confidence": 0.6}],
    }
    old_owner = yaml.safe_dump(second_record, sort_keys=False).encode()
    write(tmp_path, SECOND_OWNER, old_owner)
    second_parent = row(
        "Synthetic_sodium_hydrate",
        "CHEBI:132103",
        subject_label=second_record["preferred_term"],
        object_label="synthetic sodium parent",
        predicate_id="skos:closeMatch",
    )
    second_identity = dict(
        second_parent,
        object_id=second_record["identifier"],
        object_label=second_record["preferred_term"],
        predicate_id="skos:exactMatch",
    )
    form.before += [second_parent, second_identity]
    form.rows += [second_parent, second_identity]
    form.receipts = [
        receipt(form.before, form.before, range(1, 6)),
        receipt(
            form.before,
            form.rows,
            [1, 2, 3, 5, 6],
            [
                change("changed", form.before[0], form.rows[0], 1, 1),
                change("added", None, form.rows[3], None, 4),
            ],
            sequence=2,
            records=[owner_link(sha(form.old_owner), sha(form.owner_raw))],
        ),
    ]
    form.refresh_chain()
    form.prior["source_sssom_sha256"] = sha(sssom(form.before))
    write(tmp_path, PRIOR, form.prior)
    form.evidence[PRIOR] = sha((tmp_path / PRIOR).read_bytes())
    for item in form.review["source"]["inputs"]:
        item["sha256"] = sha((tmp_path / item["path"]).read_bytes())
    endpoint = form.chain["receipt_paths"][1]
    form.document["checkpoint"].update(
        sha256=form.chain["receipt_inputs"][endpoint],
        after_sha256=form.chain["reviewed_sha256"],
    )
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-m", "First synthetic endpoint includes withheld second owner")
    form.review["source"]["git_revision"] = git(tmp_path, "rev-parse", "HEAD")
    form.save_pair()
    first_files = {
        name: (tmp_path / name).read_bytes()
        for name in (AUTHORITY, PAIR, str(Path(PAIR).with_name("review.md")), CAPTURE, PRIOR, OWNER)
    }

    old_rows = copy.deepcopy(form.rows)
    second_record["ontology_mapping"]["mapping_quality"] = "NARROW_MATCH"
    new_owner = yaml.safe_dump(second_record, sort_keys=False).encode()
    write(tmp_path, SECOND_OWNER, new_owner)
    new_parent = dict(second_parent, predicate_id="skos:broadMatch")
    handle = dict(second_identity, object_id="kgmicrobe.compound:synthetic_sodium_hydrate")
    form.append(
        form.rows[:4] + [new_parent, second_identity, handle],
        range(1, 7),
        [
            change("changed", second_parent, new_parent, 5, 5),
            change("added", None, handle, None, 7),
        ],
        [owner_link(sha(old_owner), sha(new_owner), SECOND_OWNER)],
    )
    save_second_pair(form, old_rows, old_owner)

    baseline = json.loads((tmp_path / mcr.BASELINE).read_bytes())
    baseline.update(
        record_inputs={
            OWNER: sha(form.old_owner),
            OTHER: form.hashes[OTHER],
            SECOND_OWNER: sha(old_owner),
        },
        decisions=[
            {
                "source_position": position,
                "resolution_status": "APPROVED" if position <= 3 else "OPEN",
                "review_reason": "Synthetic baseline; second owner has no mapping approval.",
                "review_evidence": "reports/test-only/old-review.md",
            }
            for position in range(1, 6)
        ],
    )
    write(tmp_path, mcr.BASELINE, baseline)
    assembler = module(
        "sequential_forms_assembler", ROOT / "reports/sssom_completion_20260921/assemble_review.py"
    )
    here = tmp_path / "reports/sssom_completion_20260921"
    monkeypatch.setattr(assembler, "ROOT", tmp_path)
    monkeypatch.setattr(assembler, "HERE", here)
    monkeypatch.setattr(assembler, "REVIEWED_SOURCE", form.chain["reviewed_sha256"])
    monkeypatch.setattr(assembler, "FORM_FOLLOWUP_FILES", (AUTHORITY,))
    before = assembler.assemble()
    first_decisions = json.loads(before["review.json"])["decisions"]
    assert [d["disposition"] for d in first_decisions] == ["SUPPORTED"] * 4 + ["WITHHOLD"] * 3

    monkeypatch.setattr(assembler, "FORM_FOLLOWUP_FILES", (AUTHORITY, SECOND_AUTHORITY))
    after = assembler.assemble()
    admitted = json.loads(after["review.json"])["decisions"]
    assert admitted[:4] == first_decisions[:4]
    assert [d["disposition"] for d in admitted[4:]] == ["SUPPORTED"] * 3
    evidence = json.loads(after["mapping-evidence.json"])["entries"]
    for position in (1, 2, 4, 5, 6, 7):
        authority = evidence[str(position)]["basis"]["form_followup"]
        assert authority["file"] == (AUTHORITY if position <= 4 else SECOND_AUTHORITY)
    for name, raw in after.items():
        write(here, name, raw)
    _, manifest = reviewed_sssom.expected_products(tmp_path, here / "review.json")
    assert manifest["counts"] == {"source": 7, "supported": 7, "withhold": 0}
    assert all((tmp_path / name).read_bytes() == raw for name, raw in first_files.items())
    assert (tmp_path / SECOND_OWNER).read_bytes() == new_owner
    assert (
        yaml.safe_load(old_owner)["cellular_metabolic_roles"]
        == second_record["cellular_metabolic_roles"]
    )
    assert not RecordRefreshes(tmp_path).matches(SECOND_OWNER, sha(old_owner))
    withdrawal = mcr.record_supersession(
        form.chain,
        owner=SECOND_OWNER,
        reviewed_sha256=sha(old_owner),
        current_sha256=sha(new_owner),
    )
    assert withdrawal is not None and "no approval" in withdrawal["reason"]
    assert all(d["owner_record"] in (OWNER, OTHER, SECOND_OWNER) for d in admitted)
    assert all("role" not in d for d in admitted)
