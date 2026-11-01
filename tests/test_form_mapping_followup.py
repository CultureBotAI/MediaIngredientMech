"""Synthetic native form-review authorities; these fixtures approve no real records."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import reviewed_sssom
from mediaingredientmech.form_mapping_review import FormFollowups
from mediaingredientmech.validation import mapping_change_receipts as mcr

ROOT = Path(__file__).resolve().parents[1]
OWNER = "data/ingredients/mapped/Fixture_hydrate.yaml"
OTHER = "data/ingredients/mapped/Other.yaml"
AUTHORITY = "reports/test-only/form-v1.json"
CAPTURE = "reports/test-only/source.txt"
PRIOR = "reports/test-only/prior.json"
PAIR = "reviews/structured/20260101T000000Z-test-only-form/review.yaml"
KINDS = ("form_parent", "primary_identity", "registry_handle")


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# Reuse the maintained strict-receipt fixture builders, including the real parser
# and replay; no hand-made proof dictionaries or patched validation functions.
chain_fixture = module("form_chain_fixture", ROOT / "tests/test_mapping_change_receipts.py")
sha, write, row, sssom = (
    chain_fixture.sha,
    chain_fixture.write,
    chain_fixture.row,
    chain_fixture.sssom,
)
receipt, change = chain_fixture.receipt, chain_fixture.change


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


def selector(mapping):
    return json.dumps(
        {key: mapping[key] for key in ("subject_id", "predicate_id", "object_id")},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def owner_link(before, after, owner=OWNER):
    return {"source_record": owner, "before_yaml_sha256": before, "after_yaml_sha256": after}


class Fixture:
    def __init__(
        self,
        root,
        *,
        token="",
        parent_predicate="skos:broadMatch",
        grade="NARROW_MATCH",
        handle_id="kgmicrobe.compound:fixture_hydrate",
        identity_id="cas:10030-67-8",
    ):
        self.root = root
        self.record = {
            "identifier": "cas:10030-67-8",
            "preferred_term": "Fixture hydrate",
            "mapping_status": "MAPPED",
            "ingredient_type": "SINGLE_INGREDIENT",
            "ontology_mapping": {
                "ontology_id": "CHEBI:6731",
                "ontology_label": "fixture parent",
                "mapping_quality": grade,
            },
            "synonyms": [],
            "functional_roles": [{"role": "CARBON_SOURCE", "confidence": 0.5}],
        }
        old_record = copy.deepcopy(self.record)
        old_record["ontology_mapping"]["mapping_quality"] = "CLOSE_MATCH"
        self.old_owner = yaml.safe_dump(old_record, sort_keys=False).encode()
        self.owner_raw = yaml.safe_dump(self.record, sort_keys=False).encode()
        write(root, OWNER, self.owner_raw)
        write(
            root,
            OTHER,
            yaml.safe_dump(
                {"identifier": "CHEBI:1", "preferred_term": "Other", "mapping_status": "MAPPED"}
            ).encode(),
        )
        old_parent = row(
            "Fixture_hydrate",
            "CHEBI:6731",
            subject_label="Fixture hydrate",
            predicate_id="skos:closeMatch",
            object_label="fixture parent",
            other=token,
        )
        identity = row(
            "Fixture_hydrate",
            identity_id,
            subject_label="Fixture hydrate",
            object_label="Fixture hydrate",
            other=token,
        )
        unrelated = row("Other", "CHEBI:1", object_label="Other")
        self.before = [old_parent, identity, unrelated]
        parent = dict(old_parent, predicate_id=parent_predicate)
        handle = dict(identity, object_id=handle_id)
        self.rows = [parent, identity, unrelated, handle]
        self.receipts = [
            receipt(
                self.before,
                self.before,
                [1, 2, 3],
                records=[owner_link(sha(self.old_owner), sha(self.old_owner))],
            ),
            receipt(
                self.before,
                self.rows,
                [1, 2, 3],
                [
                    change("changed", old_parent, parent, 1, 1),
                    change("added", None, handle, None, 4),
                ],
                sequence=2,
                records=[owner_link(sha(self.old_owner), sha(self.owner_raw))],
            ),
        ]
        self.refresh_chain()
        for path in (
            "scripts/record_review.py",
            "schema/record_review.yaml",
            "src/mediaingredientmech/form_mapping_review.py",
            "src/mediaingredientmech/synonym_policy.py",
        ):
            write(root, path, (ROOT / path).read_bytes())
        self.native = module("native_form_fixture", root / "scripts/record_review.py")
        write(
            root,
            CAPTURE,
            b"Synthetic test source: hydrate is a distinct form of its parent; no real scientific finding.\n",
        )
        self.prior = {
            "source_sssom_sha256": sha(sssom(self.before)),
            "entries": {
                kind: {
                    "owner_record": OWNER,
                    "owner_record_sha256": sha(self.old_owner),
                    "mapping": self.before[index],
                    "row_sha256": reviewed_sssom.row_sha256(self.before[index]),
                    "disposition": "WITHHOLD",
                }
                for index, kind in enumerate(KINDS[:2])
            },
        }
        write(root, PRIOR, self.prior)
        self.evidence = {name: sha((root / name).read_bytes()) for name in (CAPTURE, PRIOR)}
        for args in (
            ("init",),
            ("config", "user.name", "Synthetic form fixture"),
            ("config", "user.email", "fixture@example.invalid"),
            ("add", "."),
            ("commit", "-m", "Synthetic source endpoint"),
        ):
            git(root, *args)
        targets, assessments, decisions = [], [], []
        for kind, position in zip(KINDS, (1, 2, 4), strict=True):
            mapping = copy.deepcopy(self.rows[position - 1])
            digest = reviewed_sssom.row_sha256(mapping)
            targets.append(
                {
                    "target_id": kind,
                    "path": mcr.SSSOM_SOURCE,
                    "kind": "snapshot_row",
                    "selector": selector(mapping),
                    "label": "Synthetic " + kind,
                    "semantic_digest": {
                        "algorithm": "mim-sssom-row-sha256-v1",
                        "sha256": digest,
                        "description": "Native full-row digest, including every Unicode value.",
                    },
                    "owner_paths": [
                        {
                            "repository": "CultureBotAI/MediaIngredientMech",
                            "path": OWNER,
                            "role": "Synthetic supplied-form owner",
                        }
                    ],
                }
            )
            assessments.append(
                {
                    "assessment_id": kind,
                    "area": "identity",
                    "topic": "Synthetic " + kind,
                    "outcome": "supported",
                    "summary": "Test-only explicit claim assessment.",
                    "target_ids": [kind],
                    "evidence_ids": ["source"],
                }
            )
            entry = {
                "claim_kind": kind,
                "source_position": position,
                "mapping": mapping,
                "row_sha256": digest,
                "disposition": "SUPPORTED",
                "reason": "Synthetic fixture claim only.",
                "identity_review": "Synthetic distinct-form assessment, not production approval.",
                "token_reviews": {
                    part: "Synthetic token reviewed" for part in token.split("|") if part
                },
                "resolved_negative_reviews": [],
                "target_id": kind,
                "assessment_id": kind,
                "prior_basis": (
                    {"path": PRIOR, "evidence_key": kind} if kind != "registry_handle" else None
                ),
            }
            if kind == "form_parent":
                entry["relation_rationale"] = "Form-of parent, never identity or subclass."
            if kind == "registry_handle":
                entry["handle_rationale"] = "B1 local handle alongside distinct CAS primary."
            decisions.append(entry)
        self.review = {
            "schema_version": "1.0.0",
            "review_id": "20260101T000000Z-test-only-form",
            "kind": "batch",
            "repository": "CultureBotAI/MediaIngredientMech",
            "title": "Synthetic form admission fixture",
            "started_at": "2026-01-01T00:00:00Z",
            "finished_at": "2026-01-01T00:00:00Z",
            "reviewer": {
                "identity": "Synthetic fixture",
                "kind": "agent",
                "independence": "not_applicable",
                "independence_basis": "No real scientific review; test-only payload.",
            },
            "skill": "test-only",
            "completion": "completed",
            "verdict": "pass_with_limitations",
            "scientific_review": True,
            "summary": "Test-only native contract fixture.",
            "source": {
                "git_revision": git(root, "rev-parse", "HEAD"),
                "state": "git_commit",
                "inputs": [
                    {"path": path, "sha256": digest, "role": "Synthetic endpoint input"}
                    for path, digest in (
                        {
                            mcr.SSSOM_SOURCE: self.chain["reviewed_sha256"],
                            OWNER: sha(self.owner_raw),
                        }
                        | self.evidence
                    ).items()
                ],
            },
            "scope": {
                "description": "Exactly three test mappings.",
                "selection": "Explicit synthetic triplet.",
                "coverage": "full",
                "population_size": 3,
                "reviewed_target_ids": list(KINDS),
            },
            "targets": targets,
            "checks": [
                {
                    "check_id": "fixture",
                    "name": "Synthetic source inspection",
                    "required": True,
                    "status": "passed",
                    "summary": "Fixture bytes inspected.",
                    "target_ids": list(KINDS),
                    "evidence_ids": ["source"],
                }
            ],
            "evidence": [
                {
                    "evidence_id": "source",
                    "kind": "primary_source",
                    "reference": CAPTURE,
                    "locator": "https://example.invalid/synthetic-fixture (never retrieved)",
                    "snapshot_sha256": self.evidence[CAPTURE],
                    "accessed_at": "2026-01-01T00:00:00Z",
                    "support": "supports",
                    "summary": "Synthetic source bytes, not research.",
                }
            ],
            "assessments": assessments,
            "findings": [],
            "actions": [],
            "limitations": ["Synthetic fixture approves no real records or scientific claims."],
        }
        endpoint = self.chain["receipt_paths"][1]
        self.document = {
            "schema_version": 1,
            "owner_record": OWNER,
            "owner_record_sha256": sha(self.owner_raw),
            "checkpoint": {
                "sequence": 2,
                "path": endpoint,
                "sha256": self.chain["receipt_inputs"][endpoint],
                "after_sha256": self.chain["reviewed_sha256"],
            },
            "native_review": {},
            "evidence_inputs": self.evidence,
            "decisions": decisions,
        }
        self.save_pair()

    def refresh_chain(self):
        self.chain = chain_fixture.repository(self.root, self.before, self.rows, self.receipts)
        _, _, self.rows = reviewed_sssom.read_sssom(self.root / mcr.SSSOM_SOURCE)
        self.owners, self.records = reviewed_sssom._owners(self.root, self.rows)
        self.hashes = {name: sha((self.root / name).read_bytes()) for name in self.records}

    def save_document(self):
        write(self.root, AUTHORITY, self.document)

    def save_pair(self):
        raw = yaml.safe_dump(self.review, sort_keys=False, allow_unicode=True).encode()
        markdown = self.native.render_markdown(
            self.review, self.root / "schema/record_review.yaml"
        ).encode()
        write(self.root, PAIR, raw)
        write(self.root, str(Path(PAIR).with_name("review.md")), markdown)
        self.document["native_review"] = {
            "path": PAIR,
            "sha256": sha(raw),
            "markdown_sha256": sha(markdown),
        }
        self.save_document()

    def load(self, paths=None):
        return FormFollowups(
            self.root,
            [AUTHORITY] if paths is None else paths,
            self.chain,
            self.rows,
            self.owners,
            self.records,
            self.hashes,
        )

    def consume(self, loaded=None):
        loaded = self.load() if loaded is None else loaded
        result = {}
        for position, mapping in enumerate(self.rows, 1):
            owner = self.owners[position - 1]
            result[position] = loaded.apply(
                mapping, owner, self.hashes[owner], self.records[owner], current_position=position
            )
        loaded.finish()
        return loaded, result

    def append(self, after, positions, changes=(), records=()):
        self.receipts.append(
            receipt(
                self.rows,
                after,
                positions,
                changes,
                sequence=len(self.receipts) + 1,
                records=records,
            )
        )
        self.rows = after
        self.refresh_chain()


@pytest.fixture
def form(tmp_path):
    return Fixture(tmp_path)


def test_native_triplet_requires_three_distinct_assessments_and_keeps_roles(form):
    original = (form.root / OWNER).read_bytes()
    loaded, results = form.consume()
    assert [results[p][0] for p in (1, 2, 4)] == ["SUPPORTED"] * 3
    assert results[3] is None
    assert {results[p][2]["claim_kind"] for p in (1, 2, 4)} == set(KINDS)
    assert {
        PAIR,
        CAPTURE,
        PRIOR,
        AUTHORITY,
        OWNER,
        "scripts/record_review.py",
        "schema/record_review.yaml",
    } <= loaded.inputs.keys()
    assert (form.root / OWNER).read_bytes() == original
    assert (
        form.native.parse_review_bundle(
            PAIR,
            (form.root / PAIR).read_bytes(),
            (form.root / Path(PAIR).with_name("review.md")).read_bytes(),
            form.root / "schema/record_review.yaml",
        )
        == form.review
    )
    assert form.native.source_provenance(form.root, form.review)["status"] == "git_commit_verified"


def test_receipt_chain_without_explicit_authority_grants_no_support(form):
    loaded, results = form.consume(form.load(paths=[]))
    assert set(results.values()) == {None}
    assert loaded.inputs == {}


@pytest.mark.parametrize(
    "field",
    [
        "scientific_review",
        "source_endpoint",
        "source_owner",
        "capture",
        "target_selector",
        "target_digest",
        "target_owner",
        "assessment",
        "source_kind",
    ],
)
def test_valid_native_pair_cannot_substitute_an_unrelated_assessment(form, field):
    review = form.review
    if field == "scientific_review":
        review["scientific_review"] = False
    elif field in {"source_endpoint", "source_owner"}:
        review["source"]["state"] = "working_tree"
        path = mcr.SSSOM_SOURCE if field == "source_endpoint" else OWNER
        next(item for item in review["source"]["inputs"] if item["path"] == path)["sha256"] = sha(
            "wrong"
        )
    elif field == "capture":
        review["evidence"][0]["snapshot_sha256"] = sha("wrong")
    elif field == "target_selector":
        review["targets"][0]["selector"] = selector(dict(form.rows[0], object_id="CHEBI:999"))
    elif field == "target_digest":
        review["targets"][0]["semantic_digest"]["sha256"] = sha("wrong")
    elif field == "target_owner":
        review["targets"][0]["owner_paths"][0]["path"] = OTHER
    elif field == "assessment":
        form.document["decisions"][0]["assessment_id"] = "unrelated"
        review["assessments"].append(
            dict(copy.deepcopy(review["assessments"][1]), assessment_id="unrelated")
        )
    else:
        review["evidence"][0]["kind"] = "validation"
    form.save_pair()
    # Render and parse remain valid: it is the form-specific binding that refuses.
    form.native.parse_review_bundle(
        PAIR,
        (form.root / PAIR).read_bytes(),
        (form.root / Path(PAIR).with_name("review.md")).read_bytes(),
        form.root / "schema/record_review.yaml",
    )
    with pytest.raises(ValueError):
        form.load()


def test_mismatched_native_markdown_is_refused_even_with_matching_document_hash(form):
    path = form.root / Path(PAIR).with_name("review.md")
    path.write_bytes(path.read_bytes() + b"Invented endorsement.\n")
    form.document["native_review"]["markdown_sha256"] = sha(path.read_bytes())
    form.save_document()
    with pytest.raises(ValueError, match="Markdown does not match"):
        form.load()


@pytest.mark.parametrize(
    "field,value",
    [
        ("sequence", True),
        ("sequence", 1),
        ("path", "reports/wrong.json"),
        ("sha256", "0" * 64),
        ("after_sha256", "0" * 64),
    ],
)
def test_endpoint_is_exactly_bound(form, field, value):
    form.document["checkpoint"][field] = value
    form.save_document()
    with pytest.raises(ValueError, match="checkpoint"):
        form.load()


@pytest.mark.parametrize(
    "mutation",
    [
        "owner",
        "position",
        "row",
        "digest",
        "duplicate_kind",
        "duplicate_assessment",
        "extra",
        "unknown",
        "basis",
    ],
)
def test_authority_shape_and_freshness_refuse_ambiguous_or_stale_claims(form, mutation):
    doc, entry = form.document, form.document["decisions"][0]
    if mutation == "owner":
        doc["owner_record_sha256"] = sha(form.old_owner)
    elif mutation == "position":
        entry["source_position"] = True
    elif mutation == "row":
        entry["mapping"]["other"] = "β changed"
    elif mutation == "digest":
        entry["row_sha256"] = sha("wrong")
    elif mutation == "duplicate_kind":
        doc["decisions"][1]["claim_kind"] = "form_parent"
    elif mutation == "duplicate_assessment":
        doc["decisions"][1]["assessment_id"] = entry["assessment_id"]
    elif mutation == "extra":
        doc["decisions"].append(copy.deepcopy(entry))
    elif mutation == "unknown":
        entry["auto_approve"] = True
    else:
        entry["prior_basis"]["path"] = CAPTURE
    form.save_document()
    with pytest.raises(ValueError):
        form.load()


@pytest.mark.parametrize(
    "kwargs",
    [
        {"parent_predicate": "skos:exactMatch"},
        {"parent_predicate": "skos:narrowMatch"},
        {"grade": "CLOSE_MATCH"},
        {"handle_id": "kgmicrobe.ingredient:fixture_hydrate"},
        {"identity_id": "cas:207511-10-2"},
    ],
)
def test_complete_native_authority_cannot_override_form_structure(tmp_path, kwargs):
    form = Fixture(tmp_path, **kwargs)
    with pytest.raises(ValueError, match="parent|NARROW_MATCH|registry|identity"):
        form.load()


def test_supported_parent_requires_supported_handle(form):
    form.document["decisions"][2]["disposition"] = "WITHHOLD"
    form.save_document()
    with pytest.raises(ValueError, match="supported B1"):
        form.load()


def test_withheld_parent_does_not_inherit_supported_sibling_decisions(form):
    form.document["decisions"][0]["disposition"] = "WITHHOLD"
    form.save_document()
    _, results = form.consume()
    assert results[1][0] == "WITHHOLD"
    assert results[2][0] == results[4][0] == "SUPPORTED"


@pytest.mark.parametrize("position", [1, 4])
def test_distinct_negative_is_not_silently_resolved_on_retained_or_added_claim(form, position):
    loaded = form.load()
    with pytest.raises(ValueError, match="exact negative"):
        loaded.apply(
            form.rows[position - 1],
            OWNER,
            form.hashes[OWNER],
            form.record,
            current_position=position,
            negative_reviews=[{"reason": "Distinct open objection"}],
        )


@pytest.mark.parametrize("token", ["10% stock solution", "autoclave", "Other"])
def test_reviewed_tokens_still_cannot_bypass_preparation_or_foreign_owner_safeguards(
    tmp_path, token
):
    form = Fixture(tmp_path, token=token)
    loaded = form.load()
    for position in (1, 4):
        with pytest.raises(ValueError, match="preparation|foreign owner"):
            loaded.apply(
                form.rows[position - 1],
                OWNER,
                form.hashes[OWNER],
                form.record,
                current_position=position,
            )


def test_unicode_alias_needs_native_complete_row_digest_and_individual_review(tmp_path):
    form = Fixture(tmp_path, token="β fixture")
    form.consume()
    form.document["decisions"][0]["token_reviews"] = {}
    form.save_document()
    with pytest.raises(ValueError, match="unreviewed synonym"):
        form.consume()
    entry = form.document["decisions"][0]
    entry["row_sha256"] = sha(
        json.dumps(entry["mapping"], sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    )
    form.save_document()
    with pytest.raises(ValueError, match="endpoint row"):
        form.load()


def test_unrelated_suffix_moves_all_claims_without_rewriting_authority(form):
    immutable = {
        name: (form.root / name).read_bytes()
        for name in (AUTHORITY, PAIR, str(Path(PAIR).with_name("review.md")), PRIOR)
    }
    old = form.rows
    unrelated = dict(old[2], other="unrelated alias")
    form.append(
        [unrelated, old[3], old[0], old[1]],
        [3, 4, 1, 2],
        [change("changed", old[2], unrelated, 3, 1)],
        [owner_link(sha("other-before"), sha((form.root / OTHER).read_bytes()), OTHER)],
    )
    _, result = form.consume()
    assert [result[p][0] for p in (2, 3, 4)] == ["SUPPORTED"] * 3
    assert result[1] is None
    assert result[2][2]["continuation"][0]["before_position"] == 4
    assert result[2][2]["continuation"][0]["after_position"] == 2
    assert all((form.root / name).read_bytes() == raw for name, raw in immutable.items())


def test_same_owner_noop_link_is_admissible(form):
    form.append(
        form.rows, [1, 2, 3, 4], records=[owner_link(form.hashes[OWNER], form.hashes[OWNER])]
    )
    assert form.consume()[1][1][0] == "SUPPORTED"


@pytest.mark.parametrize(
    "mode", ["row_restore", "remove_readd", "owner_restore", "redundant_change"]
)
def test_matching_final_bytes_cannot_erase_intervening_revocation(form, mode):
    original = copy.deepcopy(form.rows)
    if mode == "owner_restore":
        current = form.hashes[OWNER]
        form.append(
            form.rows, [1, 2, 3, 4], records=[owner_link(current, sha("intermediate owner"))]
        )
        form.append(
            form.rows, [1, 2, 3, 4], records=[owner_link(sha("intermediate owner"), current)]
        )
    elif mode == "remove_readd":
        form.append(original[1:], [None, 1, 2, 3], [change("removed", original[0], None, 1, None)])
        form.append(original, [2, 3, 4], [change("added", None, original[0], None, 1)])
    else:
        altered = (
            dict(original[0], other="intermediate alias") if mode == "row_restore" else original[0]
        )
        form.append(
            [altered, *original[1:]], [1, 2, 3, 4], [change("changed", original[0], altered, 1, 1)]
        )
        if mode == "row_restore":
            form.append(original, [1, 2, 3, 4], [change("changed", altered, original[0], 1, 1)])
    assert form.rows == original
    with pytest.raises(ValueError, match="after checkpoint"):
        form.load()


def test_second_local_namespace_remains_forbidden(form):
    extra = dict(form.rows[3], object_id="kgmicrobe.ingredient:fixture_hydrate")
    form.append([*form.rows, extra], [1, 2, 3, 4], [change("added", None, extra, None, 5)])
    with pytest.raises(ValueError, match="competing local"):
        form.load()


def test_all_declared_claims_must_be_used_once(form):
    loaded = form.load()
    with pytest.raises(ValueError, match="unused declared"):
        loaded.finish()
    loaded.apply(form.rows[0], OWNER, form.hashes[OWNER], form.record, current_position=1)
    with pytest.raises(ValueError, match="consumed twice"):
        loaded.apply(form.rows[0], OWNER, form.hashes[OWNER], form.record, current_position=1)


@pytest.mark.parametrize(
    "path",
    [
        CAPTURE,
        PAIR,
        "scripts/record_review.py",
        "schema/record_review.yaml",
        "src/mediaingredientmech/form_mapping_review.py",
    ],
)
def test_captured_graph_change_is_refused_at_finish(form, path):
    loaded = form.load()
    for position in (1, 2, 4):
        loaded.apply(
            form.rows[position - 1],
            OWNER,
            form.hashes[OWNER],
            form.record,
            current_position=position,
        )
    target = form.root / path
    target.write_bytes(target.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="captured input changed"):
        loaded.finish()


def test_late_receipt_inventory_change_refuses_completion(form):
    loaded = form.load()
    for position in (1, 2, 4):
        loaded.apply(
            form.rows[position - 1],
            OWNER,
            form.hashes[OWNER],
            form.record,
            current_position=position,
        )
    form.append(form.rows, [1, 2, 3, 4])
    with pytest.raises(ValueError, match="receipt inventory changed"):
        loaded.finish()


@pytest.mark.parametrize("parent", [False, True])
def test_source_capture_symlink_is_never_credited(form, parent):
    path = form.root / ("reports/test-only" if parent else CAPTURE)
    moved = path.with_name(path.name + ".real")
    path.rename(moved)
    path.symlink_to(moved, target_is_directory=parent)
    with pytest.raises((ValueError, OSError)):
        form.load()


def test_duplicate_json_keys_are_not_silently_collapsed(form):
    target = form.root / AUTHORITY
    target.write_text(
        target.read_text().replace(
            '"schema_version": 1,', '"schema_version": 1, "schema_version": 1,', 1
        )
    )
    with pytest.raises(ValueError, match="duplicate JSON"):
        form.load()


def test_legacy_exact_and_primary_handle_guards_remain_strict(form):
    assembler = module(
        "form_legacy_assembler", ROOT / "reports/sssom_completion_20260921/assemble_review.py"
    )
    for position, added in ((1, False), (4, True)):
        mapping = form.rows[position - 1]
        entry = dict(
            form.document["decisions"][0 if not added else 2],
            owner_record=OWNER,
            owner_record_sha256=form.hashes[OWNER],
            evidence_inputs=form.evidence,
        )
        with pytest.raises(ValueError, match="non-exact|safeguards"):
            if added:
                assembler.apply_added_identity_followup(
                    entry, mapping, OWNER, form.hashes[OWNER], form.record, form.root
                )
            else:
                assembler.apply_followup(entry, mapping, OWNER, form.hashes[OWNER], [], form.root)


def assembled(form, monkeypatch, *, declared=True, negative=False):
    """Run the dated maintained assembler with real replay, owners and evidence."""
    assembler = module(
        "native_form_assembler", ROOT / "reports/sssom_completion_20260921/assemble_review.py"
    )
    here = form.root / "reports/sssom_completion_20260921"
    baseline = json.loads((form.root / mcr.BASELINE).read_bytes())
    baseline.update(
        record_inputs={OWNER: sha(form.old_owner), OTHER: form.hashes[OTHER]},
        decisions=[
            {
                "source_position": position,
                "resolution_status": "APPROVED",
                "review_reason": "Synthetic prior exact owner/row assessment",
                "review_evidence": "reports/test-only/old-review.md",
            }
            for position in (1, 2, 3)
        ],
    )
    write(form.root, mcr.BASELINE, baseline)
    for path in (mcr.TRAIT_REFRESH, mcr.PARENT_REFRESH):
        contents = json.loads((form.root / path).read_bytes())
        contents["records"] = []
        write(form.root, path, contents)
    for path in ("trait_synonyms/decisions.json", "parent_names/decisions.json"):
        write(here, path, {"records": []})
    for name in ("concern_cohorts", "nonmapping_cohorts", "changed-owner-review"):
        write(here, f"mapping_review/{name}.json", {"rows": []})
    write(
        here,
        "mapping_review/issue-intersections.json",
        {
            "issue_669_all_baseline_intersections": [],
            "issue_232_conflicting_label_intersections": [],
            "findings": [],
        },
    )
    for name in ("adversarial-findings", "synonym-adversarial-findings"):
        findings = (
            [
                {
                    "source_position": 1,
                    "reason": "Unresolved synthetic same-subject objection",
                    "id": "negative",
                }
            ]
            if negative and name == "adversarial-findings"
            else []
        )
        write(here, f"mapping_review/{name}.json", {"findings": findings})
    write(here, "mapping_review/kgmicrobe-followup.json", {"decisions": []})
    write(
        form.root,
        "reports/semantic_review_20260921/records.tsv",
        (
            f"source_record\treview_report\n{OWNER}\treports/test-only/old-review.md\n{OTHER}\treports/test-only/old-review.md\n"
        ).encode(),
    )
    write(form.root, "reports/test-only/old-review.md", b"Synthetic prior fixture only.\n")
    write(
        form.root, "reports/semantic_review_20260921/resolution/historical-review-evidence.json", {}
    )
    for path in (
        "MAPPING_SEMANTICS.md",
        "src/mediaingredientmech/export/reviewed_sssom.py",
        "src/mediaingredientmech/review_claims.py",
        "src/mediaingredientmech/synonym_policy.py",
        "src/mediaingredientmech/record_refresh.py",
        "src/mediaingredientmech/validation/mapping_change_receipts.py",
        "scripts/validate_reviewed_sssom_schema.py",
    ):
        write(form.root, path, (ROOT / path).read_bytes())
    form.chain = mcr.verify_mapping_chain(form.root)
    monkeypatch.setattr(assembler, "ROOT", form.root)
    monkeypatch.setattr(assembler, "HERE", here)
    monkeypatch.setattr(assembler, "REVIEWED_SOURCE", form.chain["reviewed_sha256"])
    monkeypatch.setattr(assembler, "FORM_FOLLOWUP_FILES", (AUTHORITY,) if declared else ())
    result = assembler.assemble()
    for name, raw in result.items():
        write(here, name, raw)
    return result, here / "review.json"


def test_actual_assembly_withdraws_old_cas_then_admits_only_fresh_triplet(form, monkeypatch):
    before_owner = (form.root / OWNER).read_bytes()
    before, review_path = assembled(form, monkeypatch, declared=False)
    old = json.loads(before["review.json"])["decisions"]
    assert [d["disposition"] for d in old] == ["WITHHOLD", "WITHHOLD", "SUPPORTED", "WITHHOLD"]
    supported, path = assembled(form, monkeypatch)
    decisions = json.loads(supported["review.json"])["decisions"]
    assert [d["disposition"] for d in decisions] == ["SUPPORTED"] * 4
    evidence = json.loads(supported["mapping-evidence.json"])["entries"]
    assert all("form_followup" in evidence[str(p)]["basis"] for p in (1, 2, 4))
    assert "form_followup" not in evidence["3"]["basis"]
    products, manifest = reviewed_sssom.expected_products(form.root, path)
    assert manifest["counts"] == {"source": 4, "supported": 4, "withhold": 0}
    assert products["ingredient_mappings.sssom.tsv"].count(b"skos:broadMatch") == 1
    assert path == review_path
    assert (form.root / OWNER).read_bytes() == before_owner


def test_actual_assembly_keeps_same_subject_negative_on_new_handle(form, monkeypatch):
    # Resolve only the existing parent objection; the newly added B1 must still
    # explicitly address its same-subject negative instead of inheriting consent.
    form.document["decisions"][0]["resolved_negative_reviews"] = [
        {
            "reason": "Unresolved synthetic same-subject objection",
            "evidence": "mapping_review/adversarial-findings.json",
            "detail": "negative",
        }
    ]
    form.save_document()
    with pytest.raises(ValueError, match="exact negative"):
        assembled(form, monkeypatch, negative=True)


def test_actual_assembly_and_export_carry_after_unrelated_row_relocation(form, monkeypatch):
    old = form.rows
    form.append([old[2], old[3], old[0], old[1]], [3, 4, 1, 2])
    result, path = assembled(form, monkeypatch)
    _, manifest = reviewed_sssom.expected_products(form.root, path)
    assert manifest["counts"]["supported"] == 4
    evidence = json.loads(result["mapping-evidence.json"])["entries"]
    assert evidence["2"]["basis"]["form_followup"]["continuation"][0]["before_position"] == 4
    assert evidence["2"]["basis"]["form_followup"]["continuation"][0]["after_position"] == 2


def test_prior_parent_basis_cannot_be_replaced_by_same_owner_cas_claim(form):
    form.document["decisions"][0]["prior_basis"]["evidence_key"] = "primary_identity"
    form.save_document()
    with pytest.raises(ValueError, match="prior|basis|claim"):
        form.load()


@pytest.mark.parametrize("mutation", ["missing_capture", "wrong_capture", "parsed_owner"])
def test_native_evidence_and_parsed_owner_must_match_captured_bytes(form, mutation):
    if mutation == "parsed_owner":
        form.records[OWNER]["preferred_term"] = "Different parsed identity"
    elif mutation == "wrong_capture":
        (form.root / CAPTURE).write_text("Changed scientific evidence")
    else:
        form.review["source"]["inputs"] = [
            item for item in form.review["source"]["inputs"] if item["path"] != CAPTURE
        ]
        form.save_pair()
    with pytest.raises(ValueError, match="captured|digest|parsed owner"):
        form.load()


def test_missing_or_misidentified_added_handle_has_no_authority(form):
    # This valid native history already contains the handle before correction.
    # The endpoint/pair/prior all bind correctly; only the required fresh B1
    # addition is absent, so the primitive addition guard is exercised directly.
    form.before.append(copy.deepcopy(form.rows[3]))
    form.receipts = [
        receipt(
            form.before,
            form.before,
            [1, 2, 3, 4],
            records=[owner_link(sha(form.old_owner), sha(form.old_owner))],
        ),
        receipt(
            form.before,
            form.rows,
            [1, 2, 3, 4],
            [change("changed", form.before[0], form.rows[0], 1, 1)],
            sequence=2,
            records=[owner_link(sha(form.old_owner), form.hashes[OWNER])],
        ),
    ]
    form.refresh_chain()
    endpoint = form.chain["receipt_paths"][1]
    form.document["checkpoint"]["sha256"] = form.chain["receipt_inputs"][endpoint]
    form.prior["source_sssom_sha256"] = sha(sssom(form.before))
    rebind_prior(form)
    with pytest.raises(ValueError, match="handle was not added"):
        form.load()


@pytest.mark.parametrize("which", ["owner", "hash", "mapping"])
def test_apply_cannot_substitute_a_different_owner_or_payload(form, which):
    loaded = form.load()
    mapping, owner, digest = form.rows[0], OWNER, form.hashes[OWNER]
    if which == "owner":
        owner = OTHER
    elif which == "hash":
        digest = sha("stale")
    else:
        mapping = dict(mapping, other="new token")
    with pytest.raises(ValueError, match="stale applied claim"):
        loaded.apply(mapping, owner, digest, form.record, current_position=1)


@pytest.mark.parametrize("mutation", ["corrected_owner_hash", "post_correction_endpoint"])
def test_prior_basis_cannot_borrow_the_corrected_owner_or_its_own_endpoint(form, mutation):
    entry = form.prior["entries"]["form_parent"]
    entry["owner_record_sha256"] = form.hashes[OWNER]
    if mutation == "post_correction_endpoint":
        form.prior["source_sssom_sha256"] = form.document["checkpoint"]["after_sha256"]
        entry["mapping"] = copy.deepcopy(form.rows[0])
        entry["row_sha256"] = reviewed_sssom.row_sha256(entry["mapping"])
    rebind_prior(form)
    form.native.parse_review_bundle(
        PAIR,
        (form.root / PAIR).read_bytes(),
        (form.root / Path(PAIR).with_name("review.md")).read_bytes(),
        form.root / "schema/record_review.yaml",
    )
    assert (
        form.native.source_provenance(form.root, form.review)["status"]
        == "working_tree_attestation"
    )
    with pytest.raises(ValueError, match="prior|admission|owner|endpoint"):
        form.load()


def rebind_prior(form):
    """Attest mutated test evidence without claiming it exists in a Git commit."""
    write(form.root, PRIOR, form.prior)
    updated_digest = sha((form.root / PRIOR).read_bytes())
    form.evidence[PRIOR] = updated_digest
    next(item for item in form.review["source"]["inputs"] if item["path"] == PRIOR)[
        "sha256"
    ] = updated_digest
    form.review["source"]["state"] = "working_tree"
    form.save_pair()


@pytest.mark.parametrize(
    "identifier,representative,expected_holder",
    [
        ("CHEBI:999", "CHEBI:1", "MIM:Other"),
        ("CHEBI:999", "cas:10030-67-8", "MIM:Fixture_hydrate"),
        ("CHEBI:1", "cas:10030-67-8", "MIM:Fixture_hydrate"),
        ("cas:10030-67-8", "CHEBI:1", "MIM:Other"),
        ("cas:10030-67-8", "__absent__", "MIM:Fixture_hydrate"),
        ("cas:10030-67-8", "", "MIM:Retired"),
        ("cas:10030-67-8", None, "MIM:Retired"),
        ("cas:10030-67-8", "CHEBI:999", "MIM:Retired"),
    ],
)
def test_native_rule_k_tombstone_credit_is_preserved(
    tmp_path, monkeypatch, identifier, representative, expected_holder
):
    form = Fixture(tmp_path, token="Archive label")
    tombstone = {
        "identifier": identifier,
        "mapping_status": "REJECTED",
        "preferred_term": "Archive label",
    }
    if representative != "__absent__":
        tombstone["representative"] = representative
    tombstone_path = "data/ingredients/mapped/Retired.yaml"
    write(form.root, tombstone_path, yaml.safe_dump(tombstone).encode())
    validator = module("form_rule_k_native", ROOT / "scripts/validate_sssom_invariants.py")
    monkeypatch.setattr(validator, "INGREDIENTS_DIR", form.root / "data/ingredients/mapped")
    monkeypatch.setattr(validator, "OTHER_BASELINE", form.root / "no-test-exemptions.tsv")
    assert validator._preferred_term_owners()["archive label"] == frozenset({expected_holder})
    rejected = list(validator.evaluate_rule_k([form.rows[0]]))
    loaded = form.load()
    assert tombstone_path in loaded.inputs
    if expected_holder == "MIM:Fixture_hydrate":
        assert not rejected
        assert form.consume(loaded)[1][1][0] == "SUPPORTED"
    else:
        assert len(rejected) == 1
        with pytest.raises(ValueError, match="foreign owner"):
            form.consume(loaded)


def add_unpublished_owner(form):
    path = "data/ingredients/mapped/No_row.yaml"
    write(
        form.root,
        path,
        yaml.safe_dump(
            {
                "identifier": "CHEBI:999",
                "mapping_status": "MAPPED",
                "preferred_term": "Unpublished owner",
            }
        ).encode(),
    )
    assert not any(mapping["subject_id"] == "MIM:No_row" for mapping in form.rows)
    return path


@pytest.mark.parametrize(
    "mutation", ["change", "add", "remove", "leaf_symlink", "directory_symlink"]
)
def test_complete_ownership_snapshot_refuses_late_mutation_without_any_canonical_row(
    form, mutation
):
    path = add_unpublished_owner(form)
    loaded = form.load()
    assert path in loaded.inputs
    for position in (1, 2, 4):
        loaded.apply(
            form.rows[position - 1],
            OWNER,
            form.hashes[OWNER],
            form.record,
            current_position=position,
        )
    target = form.root / path
    if mutation == "change":
        target.write_bytes(target.read_bytes().replace(b"Unpublished owner", b"New owner label"))
    elif mutation == "add":
        write(form.root, "data/ingredients/mapped/Added.yaml", target.read_bytes())
    elif mutation == "remove":
        target.unlink()
    elif mutation == "leaf_symlink":
        destination = target.with_suffix(".saved")
        target.rename(destination)
        target.symlink_to(destination)
    else:
        folder = target.parent
        destination = folder.with_name("saved-mapped")
        folder.rename(destination)
        folder.symlink_to(destination, target_is_directory=True)
    with pytest.raises((ValueError, OSError)):
        loaded.finish()


def test_unpublished_live_owner_blocks_alias_before_admission(tmp_path):
    form = Fixture(tmp_path, token="Unpublished owner")
    path = add_unpublished_owner(form)
    loaded = form.load()
    assert path in loaded.inputs
    with pytest.raises(ValueError, match="foreign owner"):
        form.consume(loaded)


def test_preexisting_unpublished_symlink_is_not_read_as_an_owner(form):
    path = add_unpublished_owner(form)
    target = form.root / path
    destination = target.with_suffix(".saved")
    target.rename(destination)
    target.symlink_to(destination)
    with pytest.raises((ValueError, OSError)):
        form.load()
