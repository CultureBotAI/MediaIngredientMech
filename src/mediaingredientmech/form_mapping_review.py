"""Explicit, mapping-only review of a CAS-primary supplied-form triplet (#1070).

Receipts establish history, never scientific approval. Each of the three claims
needs its own completed native scientific assessment at the same receipt endpoint.
Later unrelated receipts may move rows; any intervening change withdraws authority.
"""

from __future__ import annotations

import hashlib
import json
import re
import tempfile
import types
from pathlib import Path

from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.export.reviewed_sssom import (
    _safe_identifiers,
    _safe_synonyms,
    row_sha256,
)
from mediaingredientmech.synonym_policy import preferred_term_owners
from mediaingredientmech.validation.mapping_change_receipts import receipt_paths

SOURCE = "mappings/ingredient_mappings.sssom.tsv"
KINDS = {"form_parent", "primary_identity", "registry_handle"}
HELPER = "scripts/record_review.py"
SCHEMA = "schema/record_review.yaml"
PREPARATION = re.compile(
    r"(?i)\d\s*%|\d\s*(?:mg/ml|g/l)|autoclave|\bif needed\b|\bstock solution\b"
)


def require(condition, message):
    if not condition:
        raise ValueError("Form mapping review: " + message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def keys(value, required, optional=()):
    require(isinstance(value, dict), "expected object")
    require(
        set(required) <= value.keys() <= set(required) | set(optional), "unexpected/missing fields"
    )


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def selector(row):
    return json.dumps(
        {key: row[key] for key in ("subject_id", "predicate_id", "object_id")},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


class FormFollowups:
    """Load only explicitly registered authorities and consume every declared claim."""

    def __init__(self, root, paths, chain, mappings, owners, records, record_hashes):
        self.root = Path(root)
        self.chain = chain
        self.inputs = {}
        self.captured = {}
        self.claims = {}
        self.used = set()
        self.native = None
        self.ownership_paths = []
        self.owner_index = {}
        require(len(paths) == len(set(paths)), "duplicate authority path")
        if not paths:
            return
        # Bootstrap the already maintained safe reader; execute precisely these
        # captured helper bytes, then use its descriptor-based reader throughout.
        helper_path = self.root / HELPER
        require(not helper_path.is_symlink(), "native helper is a symlink")
        raw = helper_path.read_bytes()
        native = types.ModuleType("form_review_native")
        native.__file__ = str(helper_path)
        exec(compile(raw, str(helper_path), "exec"), native.__dict__)
        self.native = native
        require(native.read_bytes(self.root, HELPER) == raw, "native helper changed")
        self.capture(HELPER, sha(raw))
        self.capture(SCHEMA)
        self.capture("src/mediaingredientmech/form_mapping_review.py")
        self.capture("src/mediaingredientmech/synonym_policy.py")
        self.ownership_paths = self.mapped_paths()
        ownership_records = {}
        for name in self.ownership_paths:
            record = native.yaml.safe_load(self.capture(name)) or {}
            require(isinstance(record, dict), "invalid ownership record")
            subject = mim_curie_for_stem(Path(name).stem)
            require(subject not in ownership_records, "ambiguous ownership subject")
            ownership_records[subject] = record
        self.owner_index = preferred_term_owners(ownership_records)
        for path in paths:
            document = json.loads(self.capture(path), object_pairs_hook=pairs)
            self.load(path, document, mappings, owners, records, record_hashes)
        self.recheck()

    def capture(self, path, expected=None):
        if self.native is None:
            raise ValueError("Form mapping review reader is not initialized")
        require(isinstance(path, str), "invalid input path")
        if path not in self.captured:
            raw = self.native.read_bytes(self.root, path)
            self.captured[path] = raw
            self.inputs[path] = sha(raw)
        require(
            expected is None or self.inputs[path] == expected,
            "input digest conflict or stale evidence",
        )
        return self.captured[path]

    def mapped_paths(self):
        folder = self.root / "data/ingredients/mapped"
        require(
            not any(p.is_symlink() for p in (folder, *folder.parents)),
            "aliased ownership directory",
        )
        require(folder.is_dir(), "missing ownership directory")
        return sorted(str(p.relative_to(self.root)) for p in folder.glob("*.yaml"))

    def recheck(self):
        if self.native is None:
            raise ValueError("Form mapping review reader is not initialized")
        require(self.mapped_paths() == self.ownership_paths, "ownership inventory changed")
        for path, raw in self.captured.items():
            require(self.native.read_bytes(self.root, path) == raw, "captured input changed")
        require(
            receipt_paths(self.root) == self.chain["receipt_paths"], "receipt inventory changed"
        )
        for path, expected in self.chain["input_hashes"].items():
            require(
                sha(self.native.read_bytes(self.root, path)) == expected,
                "receipt chain input changed",
            )

    def load(self, path, doc, mappings, owners, records, record_hashes):
        if self.native is None:
            raise ValueError("Form mapping review reader is not initialized")
        keys(
            doc,
            {
                "schema_version",
                "owner_record",
                "owner_record_sha256",
                "checkpoint",
                "native_review",
                "evidence_inputs",
                "decisions",
            },
        )
        require(
            type(doc["schema_version"]) is int and doc["schema_version"] == 1, "unsupported version"
        )
        owner, owner_hash = doc["owner_record"], doc["owner_record_sha256"]
        require(owner in records and record_hashes.get(owner) == owner_hash, "stale owner")
        require(
            self.native.load_document(self.capture(owner, owner_hash)) == records[owner],
            "parsed owner differs from captured bytes",
        )
        checkpoint = doc["checkpoint"]
        keys(checkpoint, {"sequence", "path", "sha256", "after_sha256"})
        sequence = checkpoint["sequence"]
        require(
            type(sequence) is int and 1 <= sequence <= len(self.chain["receipts"]),
            "invalid checkpoint",
        )
        receipt = self.chain["receipts"][sequence - 1]
        require(
            self.chain["receipt_paths"][sequence - 1] == checkpoint["path"]
            and self.chain["receipt_inputs"].get(checkpoint["path"]) == checkpoint["sha256"]
            and receipt["after_sha256"] == checkpoint["after_sha256"],
            "checkpoint differs",
        )
        links = self.chain["owner_chains"].get(owner, [])
        earlier = [link for link in links if link["sequence"] <= sequence]
        require(earlier and earlier[-1]["after_sha256"] == owner_hash, "checkpoint owner differs")
        require(
            not any(
                link["sequence"] > sequence and link["before_sha256"] != link["after_sha256"]
                for link in links
            ),
            "owner changed after checkpoint",
        )
        evidence = doc["evidence_inputs"]
        require(isinstance(evidence, dict) and evidence, "missing captured scientific evidence")
        require(
            SOURCE not in evidence
            and owner not in evidence
            and not any(
                p.endswith(("/mapping-evidence.json", "/current-review.json")) for p in evidence
            ),
            "evidence must be immutable, not a live generated review",
        )
        for name, expected in evidence.items():
            require(
                isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected),
                "invalid evidence digest",
            )
            self.capture(name, expected)
        pair = doc["native_review"]
        keys(pair, {"path", "sha256", "markdown_sha256"})
        raw = self.capture(pair["path"], pair["sha256"])
        markdown = self.capture(
            str(Path(pair["path"]).with_name("review.md")), pair["markdown_sha256"]
        )
        # Native parser/rendering use exactly the captured, self-contained schema.
        with tempfile.TemporaryDirectory(prefix="mim-form-review-") as directory:
            schema = Path(directory) / "record_review.yaml"
            schema.write_bytes(self.captured[SCHEMA])
            review = self.native.parse_review_bundle(pair["path"], raw, markdown, schema)
        provenance = self.native.source_provenance(self.root, review)
        require(
            provenance["status"] not in {"invalid", "unverified"},
            "invalid native review provenance",
        )
        require(
            review["repository"] == "CultureBotAI/MediaIngredientMech"
            and review["completion"] == "completed"
            and review["scientific_review"] is True
            and review["verdict"] in {"pass", "pass_with_limitations"},
            "requires completed passing scientific review",
        )
        source_inputs = {item["path"]: item["sha256"] for item in review["source"]["inputs"]}
        require(
            source_inputs.get(SOURCE) == checkpoint["after_sha256"]
            and source_inputs.get(owner) == owner_hash,
            "native review endpoint inputs differ",
        )
        require(
            all(source_inputs.get(name) == expected for name, expected in evidence.items()),
            "native review does not bind captured evidence",
        )
        decisions = doc["decisions"]
        require(
            isinstance(decisions, list) and len(decisions) == 3, "requires exactly three claims"
        )
        kinds, targets, assessments = set(), set(), set()
        for entry in decisions:
            keys(
                entry,
                {
                    "claim_kind",
                    "source_position",
                    "mapping",
                    "row_sha256",
                    "disposition",
                    "reason",
                    "identity_review",
                    "token_reviews",
                    "resolved_negative_reviews",
                    "target_id",
                    "assessment_id",
                    "prior_basis",
                },
                {"relation_rationale", "handle_rationale"},
            )
            kind = entry["claim_kind"]
            require(kind in KINDS and kind not in kinds, "duplicate/unknown claim kind")
            kinds.add(kind)
            require(
                entry["target_id"] not in targets and entry["assessment_id"] not in assessments,
                "duplicate target or assessment binding",
            )
            targets.add(entry["target_id"])
            assessments.add(entry["assessment_id"])
            require(
                entry["disposition"] in {"SUPPORTED", "WITHHOLD"}
                and all(nonblank(entry[name]) for name in ("reason", "identity_review")),
                "invalid scientific decision",
            )
            require(
                isinstance(entry["resolved_negative_reviews"], list), "invalid negative reviews"
            )
            row, position, continuation = self.continue_row(entry, sequence)
            require(
                mappings[position - 1] == row and owners[position - 1] == owner,
                "current row or owner differs",
            )
            require(position not in self.claims, "duplicate claim authority")
            self.check_native_claim(entry, review, evidence, owner)
            self.check_prior(entry, evidence, owner, receipt)
            self.claims[position] = (entry, doc, path, continuation)
        self.check_triplet(doc, records[owner], receipt)

    def continue_row(self, entry, sequence):
        row, position = entry["mapping"], entry["source_position"]
        state = self.chain["states_after_sequence"][sequence]
        require(type(position) is int and 1 <= position <= len(state), "invalid endpoint position")
        require(
            state[position - 1] == row and row_sha256(row) == entry["row_sha256"],
            "endpoint row differs",
        )
        continuation = []
        for index in range(sequence, len(self.chain["receipts"])):
            receipt = self.chain["receipts"][index]
            require(
                not any(change.get("before_position") == position for change in receipt["changes"]),
                "reviewed row changed or removed after checkpoint",
            )
            target = receipt["position_map"][position - 1]
            require(target is not None, "reviewed row removed after checkpoint")
            path = self.chain["receipt_paths"][index]
            continuation.append(
                {
                    "sequence": receipt["sequence"],
                    "path": path,
                    "sha256": self.chain["receipt_inputs"][path],
                    "before_position": position,
                    "after_position": target,
                }
            )
            position = target
        require(self.chain["state"][position - 1] == row, "continued row differs")
        return row, position, continuation

    def check_native_claim(self, entry, review, evidence, owner):
        targets = {item["target_id"]: item for item in review["targets"]}
        assessments = {item["assessment_id"]: item for item in review["assessments"]}
        target = targets.get(entry["target_id"], {})
        assessment = assessments.get(entry["assessment_id"], {})
        require(
            target.get("kind") == "snapshot_row"
            and target.get("path") == SOURCE
            and target.get("selector") == selector(entry["mapping"])
            and target.get("semantic_digest", {}).get("algorithm") == "mim-sssom-row-sha256-v1"
            and target.get("semantic_digest", {}).get("sha256") == entry["row_sha256"]
            and entry["target_id"] in review["scope"]["reviewed_target_ids"],
            "native target differs",
        )
        require(
            assessment.get("target_ids") == [entry["target_id"]], "native assessment target differs"
        )
        require(
            [(item["repository"], item["path"]) for item in target.get("owner_paths", [])]
            == [("CultureBotAI/MediaIngredientMech", owner)],
            "native target owner differs",
        )
        if entry["disposition"] == "SUPPORTED":
            require(assessment.get("outcome") == "supported", "native assessment is not supported")
            sources = {item["evidence_id"]: item for item in review["evidence"]}
            require(
                any(
                    sources[key]["kind"] in {"primary_source", "database", "authority"}
                    and sources[key]["support"] == "supports"
                    and sources[key]["reference"] in evidence
                    and sources[key].get("snapshot_sha256") == evidence[sources[key]["reference"]]
                    for key in assessment.get("evidence_ids", [])
                ),
                "assessment lacks captured supporting source evidence",
            )
            require(
                not any(
                    entry["target_id"] in finding["target_ids"]
                    and finding["status"] in {"open", "deferred"}
                    for finding in review["findings"]
                ),
                "native claim has unresolved findings",
            )

    def check_prior(self, entry, evidence, owner, receipt):
        prior = entry["prior_basis"]
        if entry["claim_kind"] == "registry_handle":
            require(prior is None, "new handle cannot inherit prior authority")
            return
        keys(prior, {"path", "evidence_key"})
        require(prior["path"] in evidence, "prior basis must be captured")
        archive = json.loads(self.captured[prior["path"]], object_pairs_hook=pairs)
        old = archive["entries"][prior["evidence_key"]]
        require(
            old["owner_record"] == owner
            and old["mapping"]["subject_id"] == entry["mapping"]["subject_id"]
            and old["row_sha256"] == row_sha256(old["mapping"]),
            "prior basis claim differs",
        )
        positions = [
            i
            for i, target in enumerate(receipt["position_map"], 1)
            if target == entry["source_position"]
        ]
        require(len(positions) == 1, "retained claim has no unique prior position")
        prior_row = self.chain["states_after_sequence"][receipt["sequence"] - 1][positions[0] - 1]
        require(
            archive["source_sssom_sha256"] == receipt["before_sha256"]
            and old["mapping"] == prior_row,
            "prior claim or pre-admission endpoint differs",
        )
        owner_changes = [
            change for change in receipt["records"] if change["source_record"] == owner
        ]
        require(
            len(owner_changes) == 1
            and old["owner_record_sha256"] == owner_changes[0]["before_yaml_sha256"],
            "prior owner differs from the pre-admission endpoint",
        )

    def check_triplet(self, doc, record, receipt):
        entries = {entry["claim_kind"]: entry for entry in doc["decisions"]}
        rows = {kind: entry["mapping"] for kind, entry in entries.items()}
        parent, identity, handle = (
            rows[k] for k in ("form_parent", "primary_identity", "registry_handle")
        )
        mapping = record.get("ontology_mapping") or {}
        subject = parent["subject_id"]
        require(
            subject.startswith("MIM:")
            and all(row["subject_id"] == subject for row in rows.values()),
            "triplet has different subjects",
        )
        require(
            record.get("identifier", "").startswith("cas:")
            and mapping.get("mapping_quality") == "NARROW_MATCH",
            "requires CAS-primary NARROW_MATCH owner",
        )
        require(
            record.get("ingredient_type") == "SINGLE_INGREDIENT",
            "compound handle requires a single chemical",
        )
        require(
            parent["predicate_id"] == "skos:broadMatch"
            and parent["object_id"] == mapping.get("ontology_id")
            and parent["object_label"] == mapping.get("ontology_label")
            and parent["object_id"].startswith("CHEBI:"),
            "wrong parent relation, target or label",
        )
        require(
            identity["predicate_id"] == "skos:exactMatch"
            and identity["object_id"] == record["identifier"]
            and identity["object_label"] == record["preferred_term"],
            "wrong primary identity",
        )
        require(
            handle["predicate_id"] == "skos:exactMatch"
            and handle["object_id"] == "kgmicrobe.compound:" + subject[4:].lower()
            and handle["object_label"] == record["preferred_term"],
            "wrong registry handle",
        )
        require(
            all(row["subject_label"] == record["preferred_term"] for row in rows.values()),
            "wrong subject label",
        )
        require(
            nonblank(entries["form_parent"].get("relation_rationale"))
            and nonblank(entries["registry_handle"].get("handle_rationale")),
            "missing form/handle rationale",
        )
        require(
            any(
                c["kind"] == "added"
                and c["after"] == handle
                and c["after_position"] == entries["registry_handle"]["source_position"]
                for c in receipt["changes"]
            ),
            "handle was not added by the admission receipt",
        )
        locals_ = [
            row
            for row in self.chain["state"]
            if row["subject_id"] == subject
            and row["object_id"]
            .lower()
            .startswith(("kgmicrobe.compound:", "kgmicrobe.ingredient:"))
        ]
        require(locals_ == [handle], "competing local registry namespace or row")
        require(
            entries["form_parent"]["disposition"] != "SUPPORTED"
            or entries["registry_handle"]["disposition"] == "SUPPORTED",
            "supported parent requires supported B1",
        )

    def apply(self, mapping, owner, owner_hash, record, *, current_position, negative_reviews=()):
        claim = self.claims.get(current_position)
        if claim is None:
            return None
        entry, doc, path, continuation = claim
        require(current_position not in self.used, "claim consumed twice")
        require(
            mapping == entry["mapping"]
            and owner == doc["owner_record"]
            and owner_hash == doc["owner_record_sha256"],
            "stale applied claim",
        )
        if entry["disposition"] == "SUPPORTED":
            require(
                entry["resolved_negative_reviews"] == list(negative_reviews),
                "exact negative reviews not resolved",
            )
            tokens = {token for token in mapping["other"].split("|") if token}
            require(
                isinstance(entry["token_reviews"], dict)
                and set(entry["token_reviews"]) == tokens
                and all(nonblank(v) for v in entry["token_reviews"].values()),
                "unreviewed synonym token",
            )
            require(
                not any(PREPARATION.search(token) for token in tokens),
                "preparation token safeguard",
            )
            require(
                not any(
                    (holders := self.owner_index.get(token.strip().casefold()))
                    and mapping["subject_id"] not in holders
                    for token in tokens
                ),
                "foreign owner token safeguard",
            )
            _safe_identifiers(mapping)
            _safe_synonyms(mapping, record)
        self.used.add(current_position)
        return (
            entry["disposition"],
            entry["reason"],
            {
                "file": path,
                "claim_kind": entry["claim_kind"],
                "row_sha256": entry["row_sha256"],
                "native_review": doc["native_review"],
                "assessment_id": entry["assessment_id"],
                "checkpoint": doc["checkpoint"],
                "prior_basis": entry["prior_basis"],
                "continuation": continuation,
            },
        )

    def finish(self):
        require(self.used == set(self.claims), "unused declared claim")
        if self.native is not None:
            self.recheck()
