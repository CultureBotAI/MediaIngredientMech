"""Retain the complete historical companion cohort when a current mapping is held.

This opt-in extension never admits a held claim to the existing active consumer
arrays. Historical approvals are replayed only as history. Current full-payload
decisions and owner evidence are independently required for every obligation.
"""

from __future__ import annotations

from copy import deepcopy

import yaml  # type: ignore[import-untyped]

from mediaingredientmech import identity_projection_inventory as inventory
from mediaingredientmech import ingredient_bundle_contract as native
from mediaingredientmech.identity_projection import MANIFEST
from mediaingredientmech.identity_projection_bundle import OLD_REVIEW_SHA, declared_sources
from mediaingredientmech.mapping_scope import profile_metadata, scope_profile, validate_scope_row
from mediaingredientmech.review_claims import validate_review_decision
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    Registry,
    parse_registry,
    validate_records,
)

CAPABILITY = "retained-companion-obligations-v1"
ARTIFACT = "retained_companion_obligations.json"


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError("Retained companion: " + message)


def _document(ref: dict, verified: dict[str, bytes]) -> dict:
    _require(isinstance(ref, dict) and set(ref) == {"path", "sha256"}, "invalid evidence reference")
    raw = verified.get(ref["path"])
    if raw is None:
        raise ValueError("Retained companion: evidence missing")
    _require(native.content_sha256(raw) == ref["sha256"], "evidence differs")
    value = native.read_json(raw)
    if not isinstance(value, dict):
        raise ValueError("Retained companion: evidence must be an object")
    return value


def _history(config: dict, verified: dict[str, bytes]) -> tuple[list[dict], dict[str, bytes]]:
    prior = _document(config["historical_review"], verified)
    _require(
        config["historical_review"]["sha256"] == OLD_REVIEW_SHA,
        "fixed historical authority differs",
    )
    declared = declared_sources(prior)
    transport = config["historical_sources"]
    _require(
        isinstance(transport, dict) and set(transport) == set(declared),
        "historical input inventory differs",
    )
    historical = {}
    for name, expected in declared.items():
        ref = transport[name]
        _require(
            isinstance(ref, dict) and set(ref) == {"path", "sha256"}, "invalid history transport"
        )
        raw = verified.get(ref["path"])
        if raw is None:
            raise ValueError("Retained companion: historical bytes missing")
        _require(
            ref["sha256"] == expected and native.content_sha256(raw) == expected,
            "historical bytes differ",
        )
        historical[name] = raw
    # The fixed original report and all its original claims remain genuine native
    # inputs. No new status or identity is inferred from this historical replay.
    native.reviewed_products(prior, historical)
    return native.read_json(historical[prior["claims_file"]])["claims"], historical


def _registered_owners(verified: dict[str, bytes]) -> dict[str, str]:
    """Bind original owner addresses to the independently pinned mint inventory."""
    registry = parse_registry(
        verified[REGISTRY_PATH.as_posix()], verified[LIFECYCLE_PATH.as_posix()]
    )
    records = {
        name: yaml.safe_load(raw)
        for name, raw in verified.items()
        if name.startswith("data/ingredients/") and name.endswith(".yaml")
    }
    validate_records(registry, records)
    manifest = native.read_json(verified[MANIFEST])
    count = len(manifest["records"])
    inventory.validate(verified[inventory.INVENTORY], manifest, Registry(registry.entries[:count]))
    return {entry["path"]: entry["mim_id"] for entry in manifest["records"]}


def _lineage(
    previous: dict, current: dict, old_owner: dict, owner: dict, registered: dict[str, str]
) -> None:
    _require(
        previous["kind"] == current["kind"] and previous["owner_record"] == current["owner_record"],
        "claim kind or owning record changed",
    )
    old_id = native._owner_id(previous["owner_record"], old_owner)
    new_id = native._owner_id(current["owner_record"], owner)
    _require(
        registered.get(current["owner_record"]) == new_id,
        "owner differs from authenticated original mint assignment",
    )
    _require(
        old_id == new_id or old_id in owner.get("legacy_identifiers", []),
        "owner address lacks retained alias",
    )
    if current["kind"] == "mapping":
        # Complete current row and scope are assessed below, not copied from the
        # historical approval. Natural keys may change with the real endpoints.
        return
    expected = deepcopy(previous["payload"])
    owner_field = "owner_id" if current["kind"] == "identifier" else "ingredient_id"
    if expected[owner_field] == old_id:
        expected[owner_field] = new_id
    if current["kind"] == "identifier":
        expected["annotation_id"] = native.annotation_id(expected)
    status = current["payload"].get("review_status")
    _require(
        status == expected["review_status"]
        or (expected["review_status"] == "SUPPORTED" and status == "WITHHOLD"),
        "historical negative disposition promoted",
    )
    expected["review_status"] = status
    # Eligibility can only be withdrawn when the current complete scientific
    # review withdraws this claim; original reported chemistry is not rewritten.
    if current["kind"] == "identifier" and status == "WITHHOLD":
        expected["xref_eligible"] = False
    _require(
        native.canonical_json(expected) == native.canonical_json(current["payload"]),
        "nonmapping raw payload changed beyond address/status withdrawal",
    )


def reviewed_products(review: dict, sources: dict[str, bytes]) -> tuple[dict[str, bytes], dict]:
    """Validate all original obligations and derive active and retained partitions."""
    _require(globals().get("_RETAINED_CAPTURE") is not None, "captured native entry required")
    _require("identity_projection" not in review, "current review cannot be projected")
    _require(
        type(review.get("schema_version")) is int and review["schema_version"] == 1,
        "invalid review version",
    )
    config = review["retained_obligations"]
    _require(
        isinstance(config, dict)
        and set(config) == {"capability", "historical_review", "historical_sources", "lineage"},
        "invalid extension fields",
    )
    _require(config["capability"] == CAPABILITY, "unsupported capability")
    declared = declared_sources(review)
    _require(set(declared) == set(sources), "current source inventory differs")
    _require(
        all(native.content_sha256(sources[n]) == h for n, h in declared.items()),
        "current source bytes differ",
    )
    verified = {n: sources[n] for n in review["inputs"]}
    previous, historical = _history(config, verified)
    registered = _registered_owners(verified)
    document = native.read_json(sources[review["claims_file"]])
    _require(
        set(document) == {"schema_version", "claims"}
        and type(document["schema_version"]) is int
        and document["schema_version"] == 1,
        "invalid current claims document",
    )
    claims = document["claims"]
    links = config["lineage"]
    _require(
        isinstance(claims, list)
        and isinstance(links, list)
        and len(previous) == len(claims) == len(links),
        "complete historical cohort omitted",
    )
    decisions = review["decisions"]
    indexed = {d["claim_id"]: d for d in decisions}
    _require(len(indexed) == len(decisions) == len(claims), "duplicate or incomplete decisions")
    ids = [c["claim_id"] for c in claims]
    _require(
        len(set(ids)) == len(ids) and set(ids) == set(indexed),
        "duplicate or unreviewed current claim",
    )
    owners = {c["owner_record"] for c in claims}
    _require(
        set(review["record_inputs"]) == owners == {c["owner_record"] for c in previous},
        "complete owner cohort differs",
    )
    records = {name: yaml.safe_load(sources[name]) for name in owners}
    old_records = {name: yaml.safe_load(historical[name]) for name in owners}
    proofs: dict = {}
    documents = {"urn:sha256:" + native.content_sha256(raw) for raw in verified.values()}
    base = native.read_json(sources[review["base_review"]])
    _require(
        type(base.get("schema_version")) is int
        and base["schema_version"] == 1
        and native.content_sha256(sources[base["source_sssom"]]) == base["source_sha256"],
        "current complete base differs",
    )
    metadata, fields, rows = native._base_table(sources[base["source_sssom"]])
    metadata = profile_metadata(metadata)
    metadata["curie_map"]["sha256"] = "urn:sha256:"
    extensions = [x["slot_name"] for x in scope_profile()["extension_definitions"]]
    positions = {
        native.content_sha256(native.canonical_json(row)): i for i, row in enumerate(rows, 1)
    }
    _require(
        all(type(d.get("source_position")) is int for d in base["decisions"]),
        "base position must be an integer",
    )
    base_decisions = {d["source_position"]: d for d in base["decisions"]}
    _require(
        len(base_decisions) == len(rows) == len(base["decisions"])
        and set(base_decisions) == set(range(1, len(rows) + 1)),
        "complete base decisions differ",
    )
    held: dict[str, str] = {}
    mapping_owners: dict[str, str] = {}
    for old, claim, link in zip(previous, claims, links, strict=True):
        _require(
            set(claim) == {"claim_id", "kind", "owner_record", "payload"}, "invalid claim envelope"
        )
        expected_link = {
            "previous_claim_id": old["claim_id"],
            "previous_sha256": native.content_sha256(native.canonical_json(old)),
            "claim_id": claim["claim_id"],
            "sha256": native.content_sha256(native.canonical_json(claim)),
        }
        _require(link == expected_link, "complete ordered lineage differs")
        owner, payload = claim["owner_record"], claim["payload"]
        record = records[owner]
        _require(
            isinstance(record, dict) and record.get("mapping_status") == "MAPPED",
            "owner is not mapped",
        )
        owner_id = native._owner_id(owner, record)
        _lineage(old, claim, old_records[owner], record, registered)
        decision = indexed[claim["claim_id"]]
        validate_review_decision(
            decision,
            claim,
            owner,
            review["record_inputs"][owner],
            verified,
            proofs,
            require_owner_path=True,
        )
        if claim["kind"] != "mapping":
            native.validate_payload(claim["kind"], payload)
            identity = {
                "identifier": "annotation_id",
                "product": "product_id",
                "occurrence": "occurrence_id",
            }[claim["kind"]]
            owner_field = "owner_id" if claim["kind"] == "identifier" else "ingredient_id"
            _require(
                claim["claim_id"] == payload[identity]
                and decision["disposition"] == payload["review_status"],
                "claim identity or scientific status differs",
            )
            _require(
                payload[owner_field] == owner_id
                or (
                    claim["kind"] == "identifier"
                    and payload[owner_field].startswith("MIM.product:")
                ),
                "claim belongs to another owner",
            )
            _require(
                all(e["document_id"] in documents for e in payload["evidence"]),
                "source evidence omitted",
            )
            continue
        _require(owner not in mapping_owners, "duplicate owner scope")
        mapping_owners[owner] = claim["claim_id"]
        _require(
            claim["claim_id"]
            == native.stable_id(
                "mapping", [payload[k] for k in ("subject_id", "predicate_id", "object_id")]
            ),
            "mapping natural key differs",
        )
        _require(
            set(payload) == set(fields + extensions)
            and payload["subject_id"] == owner_id
            and payload["subject_label"] == record.get("preferred_term"),
            "complete scoped row or owner differs",
        )
        row = {k: payload[k] for k in fields}
        base_decision = base_decisions.get(
            positions.get(native.content_sha256(native.canonical_json(row)))
        )
        if base_decision is None:
            raise ValueError("Retained companion: current base row missing")
        _require(
            base["record_inputs"].get(owner) == review["record_inputs"][owner],
            "base row or owner differs",
        )
        evidence = base_decision["review_evidence"]
        _require(
            evidence in base["inputs"]
            and evidence in verified
            and native.content_sha256(verified[evidence]) == base["inputs"][evidence],
            "base evidence differs",
        )
        validate_review_decision(
            base_decision, row, owner, review["record_inputs"][owner], verified, proofs
        )
        validate_scope_row(payload, metadata)
        _require(
            payload["ext_scope_evidence"].replace("sha256:", "urn:sha256:", 1) in documents,
            "scope evidence omitted",
        )
        if decision["disposition"] == "WITHHOLD":
            _require(
                base_decision["disposition"] == "WITHHOLD"
                and payload["ext_scope_review_status"] == "WITHHOLD"
                and payload["ext_identity_authorized"] == "false",
                "held mapping has positive base/scope/identity",
            )
            held[owner] = claim["claim_id"]
    _require(set(mapping_owners) == owners and bool(held), "missing scope or no held mapping")
    _dependencies(claims)
    active = [c for c in claims if c["owner_record"] not in held]
    retained = [c for c in claims if c["owner_record"] in held]
    # Reuse the unchanged positive admission path on a derived internal view.
    # Every selected full claim/evidence/decision is unchanged. This view is not
    # a saved approval or a replacement for the complete 51-claim review.
    view = deepcopy(review)
    del view["retained_obligations"]
    active_bytes = native.canonical_json({"schema_version": 1, "claims": active})
    view["claims_sha256"] = native.content_sha256(active_bytes)
    if view["claims_file"] in view["inputs"]:
        view["inputs"][view["claims_file"]] = view["claims_sha256"]
    view["decisions"] = [indexed[c["claim_id"]] for c in active]
    view["record_inputs"] = {n: h for n, h in review["record_inputs"].items() if n not in held}
    active_sources = dict(sources, **{view["claims_file"]: active_bytes})
    active_sources = {n: active_sources[n] for n in declared_sources(view)}
    products, loaded = native.reviewed_products(view, active_sources)
    entries = []
    for old, claim in zip(previous, claims, strict=True):
        entries.append(
            {
                "previous_claim": old,
                "claim": claim,
                "decision": indexed[claim["claim_id"]],
                "partition": "retained" if claim["owner_record"] in held else "emitted",
                "blocked_by": (
                    [held[claim["owner_record"]]] if claim["owner_record"] in held else []
                ),
            }
        )
    accounting = {
        "schema_version": 1,
        "capability": CAPABILITY,
        "historical_review": config["historical_review"],
        "claim_count": len(claims),
        "owner_count": len(owners),
        "emitted_claim_count": len(active),
        "retained_claim_count": len(retained),
        "entries": entries,
    }
    products[ARTIFACT] = native.canonical_json(accounting) + b"\n"
    loaded["owners"] = {native._owner_id(n, records[n]): n for n in owners}
    loaded["retained_obligations"] = accounting
    return products, loaded


def _dependencies(claims: list[dict]) -> None:
    """Validate the whole product graph before deriving an owner-wide partition."""
    products = {c["claim_id"]: c for c in claims if c["kind"] == "product"}
    for claim in claims:
        payload = claim["payload"]
        refs = []
        if claim["kind"] == "identifier" and payload["owner_id"].startswith("MIM.product:"):
            refs = [payload["owner_id"]]
        elif claim["kind"] == "occurrence":
            refs = ([payload["product_id"]] if payload["product_id"] else []) + [
                m["product_id"] for g in payload["alternatives"] for m in g["members"]
            ]
        for ref in refs:
            _require(
                ref in products and products[ref]["owner_record"] == claim["owner_record"],
                "missing or cross-owner product dependency",
            )
            if claim["kind"] == "occurrence" and payload["review_status"] == "SUPPORTED":
                _require(
                    products[ref]["payload"]["review_status"] == "SUPPORTED",
                    "supported occurrence references withheld product",
                )
            if claim["kind"] == "identifier" and payload["xref_eligible"]:
                _require(
                    products[ref]["payload"]["review_status"] == "SUPPORTED",
                    "active xref references withheld product",
                )
