"""Read-only owner transition reconstruction for the portable semantic gate (#1387).

Original receipt paths identify captured evidence, not the current filesystem.
This checks semantic continuity; it does not replay or attest original writer,
lease, profiling, allocation authority, or scientific acquisition environments.
"""

from __future__ import annotations

import copy
from pathlib import Path
from types import SimpleNamespace

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_id_adoption as adoption
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    allocate_ids,
    build_record_index,
    dump_lifecycle,
    dump_registry,
    parse_registry,
    validate_records,
)
from mediaingredientmech.validation.write_validated import validate_ingredient

LEDGERS = (str(REGISTRY_PATH), str(LIFECYCLE_PATH))


def require(value, message):
    if not value:
        raise ValueError("Semantic owner transition: " + message)


def hashes(files):
    return {name: adoption.sha(raw) for name, raw in files.items()}


def owner_path(name):
    path = adoption.relative(name)
    require(
        len(path.parts) == 4
        and path.parts[:2] == ("data", "ingredients")
        and path.parts[2] in {"mapped", "unmapped"}
        and path.suffix == ".yaml",
        "invalid owner path",
    )


def _records(owners, ledgers):
    require(set(ledgers) == set(LEDGERS), "complete ID ledgers required")
    for name in owners:
        owner_path(name)
    records = {name: adoption.load_yaml(raw) for name, raw in owners.items()}
    registry = parse_registry(*(ledgers[name] for name in LEDGERS))
    validate_records(registry, records)
    build_record_index(records)
    return records, registry


def _aggregate_check(outputs, records, schema_root):
    excluded = adoption._CAPTURE.script("scripts/aggregate_records.py").PER_RECORD_ONLY_FIELDS
    for category, name in zip(("mapped", "unmapped"), adoption.AGGREGATES, strict=True):
        collection = adoption.load_yaml(outputs[name])
        expected = [
            {k: v for k, v in record.items() if k not in excluded}
            for path, record in records.items()
            if path.split("/")[2] == category
        ]
        require(
            sorted(collection["ingredients"], key=lambda x: x["mim_id"])
            == sorted(expected, key=lambda x: x["mim_id"])
            and collection["total_count"] == len(expected)
            and collection["mapped_count"] == sum(r["mapping_status"] == "MAPPED" for r in expected)
            and collection["unmapped_count"]
            == sum(r["mapping_status"] == "UNMAPPED" for r in expected),
            "aggregate lost or changed owner semantics",
        )
        require(
            not validate_ingredient(
                collection,
                target_class="IngredientCollection",
                schema_path=schema_root / adoption.SCHEMA,
            ),
            "invalid aggregate",
        )


def _legacy_inventory(
    request, manifest, stable_before, plan, application, source_owners, get, root
):
    """#1392 reconstruct selected operations and the unchanged source complement."""
    legacy_root = request["legacy"]["root"]
    before = adoption.document(get(legacy_root, plan["before_inventory"]))["owners"]
    after = adoption.document(get(legacy_root, plan["after_inventory"]))["owners"]
    require(
        before == application["before_inventory"] and after == application["after_inventory"],
        "legacy plan/application inventories differ",
    )
    migration = adoption.document(
        get(root, {"path": adoption.MIGRATION, "sha256": manifest["inputs"][adoption.MIGRATION]})
    )
    minted = {row["path"]: row for row in migration["records"]}
    require(
        len(minted) == len(migration["records"])
        and set(minted) == set(stable_before)
        and before == {n: r["before_sha256"] for n, r in minted.items()}
        and hashes(stable_before) == {n: r["after_sha256"] for n, r in minted.items()},
        "source baseline differs from verified pre-ID science",
    )
    operations = {row["operation_id"]: row for row in plan["records"]}
    applied = {row["operation_id"]: row for row in application["records"]}
    require(
        len(operations) == len(plan["records"])
        and len(applied) == len(application["records"])
        and set(applied) == set(operations)
        and len(application["completed_operations"]) == len(operations)
        and set(application["completed_operations"]) == set(operations),
        "incomplete legacy operation membership",
    )
    acceptance = adoption.document(get(legacy_root, application["acceptance"]))
    require(
        acceptance["scope"] == "source_application_only"
        and acceptance["plan_sha256"] == request["legacy"]["plan"]["sha256"]
        and acceptance["baseline_commit"]
        == application["baseline_commit"]
        == plan["baseline_commit"]
        and acceptance["intake_heads"] == plan["intake_heads"]
        and acceptance["binding_sha256"] == {b["binding_id"]: b["sha256"] for b in plan["bindings"]}
        and acceptance["accepted_operations"]
        == {k: o["after_capture"]["sha256"] for k, o in operations.items()},
        "legacy source-only acceptance differs",
    )
    replay, originals, selected, destinations = dict(before), {}, set(), set()
    for key, op in operations.items():
        row = applied[key]
        require(all(row.get(k) == v for k, v in op.items()), "legacy application operation differs")
        old, new = op["before_source_record"], op["source_record"]
        owner_path(new)
        require(new not in destinations, "duplicate legacy destination")
        destinations.add(new)
        if old is None:
            require(
                op["kind"] == "create" and row["before_capture"] is None and new not in before,
                "invalid legacy create",
            )
        else:
            require(
                op["kind"] != "create" and old in before and old not in selected,
                "invalid legacy selected beforeimage",
            )
            owner_path(old)
            require(row["before_capture"] is not None, "legacy recovery archive omitted")
            raw = get(legacy_root, row["before_capture"])
            require(adoption.sha(raw) == before[old], "legacy recovery archive differs")
            originals[old] = raw
            selected.add(old)
            require(old == new or new not in before, "legacy move overwrites an owner")
            del replay[old]
        raw = get(legacy_root, op["after_capture"])
        require(
            new in source_owners and raw == source_owners[new], "legacy operation capture differs"
        )
        replay[new] = adoption.sha(raw)
    require(replay == after, "unselected legacy owner changed or inventory differs")
    for name, expected in before.items():
        raw = originals.get(name, source_owners.get(name))
        require(
            raw is not None and adoption.sha(raw) == expected,
            "unselected legacy owner bytes changed",
        )
        old, stable = adoption.load_yaml(raw), adoption.load_yaml(stable_before[name])
        require(
            "mim_id" not in old and "legacy_identifiers" not in old, "pre-ID source already minted"
        )
        history, prior = stable.get("curation_history", []), old.get("curation_history", [])
        suffix = history[len(prior) :]
        require(
            history[: len(prior)] == prior
            and suffix
            and stable["mim_id"] == minted[name]["mim_id"]
            and all(
                e.get("action") == "ASSIGNED_MIM_ID" and stable["mim_id"] in e.get("changes", "")
                for e in suffix
            ),
            "original source/mint history differs",
        )
        restored = copy.deepcopy(stable)
        del restored["mim_id"], restored["legacy_identifiers"]
        if "curation_history" in old:
            restored["curation_history"] = prior
        else:
            del restored["curation_history"]
        require(restored == old, "source baseline science differs from permanent-ID baseline")
    return operations


def _original_adoption_reviews(
    request, manifest, context, intake, operations, source_owners, get, root, schema_root
):
    """#1392 native historical review semantics and genuine retained Git proof.

    The consumer checkout supplies same-MIM commit objects and the schema. Its
    path is never substituted into original reports; working-tree source stays
    an attestation. These checks grant no current graph release approval.
    """
    parser = adoption._CAPTURE.script("scripts/record_review.py")
    require(
        parser.repository_identity(schema_root).lower() == adoption.REPOSITORY.lower(),
        "review Git authority is not MIM",
    )
    pins = dict(manifest["inputs"])
    require(
        all(pins.get(n) == p for n, p in request["review_inputs"].items()),
        "original review pin differs from manifest",
    )

    class CapturedReviewInputs:
        def __init__(self):
            self.root = schema_root

        def read(self, name, expected=None):
            require(
                name in pins and (expected is None or pins[name] == expected),
                "original native review input closure differs",
            )
            return get(root, {"path": name, "sha256": pins[name]})

    candidates = {row["candidate_key"]: row for row in intake["candidates"]}
    decisions = {row["operation_id"]: row for row in request["decisions"]}
    payloads = [
        {
            "operation_id": key,
            "context_sha256": adoption.digest(context),
            "proposal_scope": {"operation_id": key},
            "original_eligibility_context": candidates[key],
            "owner": adoption.load_yaml(source_owners[operations[key]["source_record"]]),
            "owner_sha256": adoption.sha(source_owners[operations[key]["source_record"]]),
            "origins": operations[key]["origins"],
        }
        for key in sorted(decisions)
    ]
    require(
        adoption.document(get(root, request["payloads"])) == payloads,
        "original complete concept payloads differ",
    )
    review_context = SimpleNamespace(
        inputs=CapturedReviewInputs(), request=request, decisions=decisions
    )
    references = []
    for payload in payloads:
        decision = decisions[payload["operation_id"]]
        pair = [decision["primary"], decision["skeptic"]]
        # Uses actual parse_review_bundle/source_provenance, target/digest,
        # required input, residual hold, evidence and independent-pair checks.
        adoption._reviews(review_context, pair, payload)
        references.append(
            {
                "operation_id": payload["operation_id"],
                "original_root": root,
                "references": copy.deepcopy(pair),
                "role": "historical disposition and hold evidence; no current release approval",
            }
        )
    return references


def _adoption(request, manifest, before, get, root, schema_root):
    """Reconstruct the native administrative overlay on captured source science."""
    context = adoption.document(get(root, request["context"]))
    legacy = request["legacy"]
    legacy_root = legacy["root"]
    plan = adoption.document(get(legacy_root, legacy["plan"]))
    application = adoption.document(get(legacy_root, legacy["application"]))
    cases = adoption.document(get(legacy_root, legacy["cases"]))
    require(
        application["state"] == "complete"
        and application["recovery_required"] is False
        and application["plan"] == legacy["plan"]
        and context["legacy_plan"] == plan
        and context["legacy_application"] == legacy["application"]
        and context["cases"] == cases
        and context["legacy_inventory"] == application["after_inventory"],
        "captured legacy source context differs",
    )
    require(
        manifest["decisions"] == request["decisions"]
        and manifest["source_cases"] == [case["case_id"] for case in cases]
        and context["existing"] == request["existing"]
        and context["target_inventory"] == manifest["before_inventory"],
        "adoption decisions/source cases differ",
    )
    source_owners = {
        name: get(legacy_root, {"path": name, "sha256": pin})
        for name, pin in application["after_inventory"].items()
    }
    for name, raw in source_owners.items():
        owner_path(name)
        require(manifest["legacy_inputs"].get(name) == adoption.sha(raw), "unbound legacy owner")
    operations = _legacy_inventory(
        request, manifest, before, plan, application, source_owners, get, root
    )
    for op in operations.values():
        require(
            op["source_record"] in source_owners
            and op["after_capture"]["sha256"] == adoption.sha(source_owners[op["source_record"]]),
            "source operation afterimage differs",
        )
        get(legacy_root, op["after_capture"])
    before_records = {name: adoption.load_yaml(raw) for name, raw in before.items()}
    existing = {row["mim_id"]: row for row in request["existing"]}
    require(
        len(existing) == len(request["existing"])
        and set(existing) == {record["mim_id"] for record in before_records.values()},
        "complete existing permanent identity lineage required",
    )
    records, moves = {}, {}
    for identifier, row in existing.items():
        old, new = row["stable_path"], row["legacy_path"]
        require(old in before_records and new in source_owners, "existing owner omitted")
        stable = before_records[old]
        require(stable["mim_id"] == identifier, "existing permanent identity retargeted")
        owner_operations = [op for op in operations.values() if op["before_source_record"] == old]
        require(
            len(owner_operations) <= 1
            and new == (owner_operations[0]["source_record"] if owner_operations else old),
            "existing owner move lacks source lineage",
        )
        scientific = adoption.load_yaml(source_owners[new])
        old_history = stable.get("curation_history", [])
        split = len(old_history)
        while split and old_history[split - 1].get("action") == "ASSIGNED_MIM_ID":
            split -= 1
        prefix, administrative = old_history[:split], old_history[split:]
        require(
            administrative
            and all(identifier in event.get("changes", "") for event in administrative)
            and scientific.get("curation_history", [])[:split] == prefix,
            "original science/mint history differs",
        )
        result = copy.deepcopy(scientific)
        result["mim_id"] = identifier
        result["legacy_identifiers"] = list(
            dict.fromkeys(
                [
                    *stable.get("legacy_identifiers", []),
                    *scientific.get("legacy_identifiers", []),
                    scientific["identifier"],
                    mim_curie_for_stem(Path(new).stem),
                ]
            )
        )
        result["curation_history"] = [
            *scientific.get("curation_history", []),
            *copy.deepcopy(administrative),
        ]
        if result != stable or old != new:
            record_curation_event(
                result,
                curator="stable_id_adoption",
                action="ADOPTED_CAMPAIGN_MIM_ID",
                timestamp=request["timestamp"],
                llm_assisted=True,
                changes=f"#1303: retained {identifier}; adopted exact current legacy owner and preserved original mint/source history; no scientific approval transferred.",
            )
        require(new not in records and (old == new or new not in before), "owner merge/collision")
        records[new] = result
        if old != new:
            moves[old] = new
    decisions = {row["operation_id"]: row for row in request["decisions"]}
    creates = {key for key, op in operations.items() if op["kind"] == "create"}
    intake = adoption.document(get(root, request["eligibility_intake"]))
    candidates = {row["candidate_key"]: row for row in intake["candidates"]}
    require(
        len(decisions) == len(request["decisions"])
        and set(decisions) == creates == set(candidates)
        and len(candidates) == len(intake["candidates"]),
        "incomplete distinct-concept decisions/holds",
    )
    for key, decision in decisions.items():
        candidate = candidates[key]
        name = operations[key]["source_record"]
        require(
            candidate["owner_path"] == name
            and candidate["owner_sha256"] == adoption.sha(source_owners[name])
            and isinstance(candidate["known_conditions_and_holds"], list),
            "original concept holds differ",
        )
        status = decision["disposition"]
        require(status in adoption.DISPOSITIONS, "unassessed concept disposition")
        require(
            all(
                isinstance(decision[k], list)
                and all(isinstance(value, str) and value for value in decision[k])
                for k in ("identity_holds", "other_holds")
            ),
            "unassessed concept holds",
        )
        if status != "WITHHOLD_IDENTITY":
            require(decision["identity_holds"] == [], "held identity admitted")
        if status == "CREATE_DISTINCT_CONCEPT":
            group = [d for d in decisions.values() if d["concept_key"] == decision["concept_key"]]
            require(
                decision["concept_key"]
                and decision["owner_operation"] in creates
                and decision["existing_mim_id"] is None
                and any(d["operation_id"] == decision["owner_operation"] for d in group)
                and all(
                    d["disposition"] == status
                    and d["owner_operation"] == decision["owner_operation"]
                    for d in group
                ),
                "inconsistent concept owner selection",
            )
        elif status == "BIND_EXISTING_CONCEPT_ONLY":
            require(
                decision["existing_mim_id"] in existing
                and decision["concept_key"] is None
                and decision["owner_operation"] is None,
                "invalid existing concept binding",
            )
        else:
            require(
                all(
                    decision[k] is None
                    for k in ("existing_mim_id", "concept_key", "owner_operation")
                ),
                "withheld identity selected an owner",
            )
    selected = {
        d["owner_operation"]
        for d in decisions.values()
        if d["disposition"] == "CREATE_DISTINCT_CONCEPT"
    }
    for key in sorted(selected):
        name = operations[key]["source_record"]
        require(name not in records and name not in before, "new owner collides")
        records[name] = adoption.load_yaml(source_owners[name])
        require("mim_id" not in records[name], "unreviewed existing permanent ID")
    reviews = _original_adoption_reviews(
        request, manifest, context, intake, operations, source_owners, get, root, schema_root
    )
    return records, moves, context, intake, reviews


def _original_curation_reviews(
    request, manifest, source_context, before, payloads, get, root, schema_root
):
    """#1392 retain actual corrective decisions, full payloads and residual findings."""
    parser = successor._CAPTURE.script("scripts/record_review.py")
    require(
        parser.repository_identity(schema_root).lower() == adoption.REPOSITORY.lower(),
        "review Git authority is not MIM",
    )
    pins = dict(manifest["inputs"])

    class CapturedCorrectionInputs:
        def read(self, name, expected=None):
            require(
                name in pins and (expected is None or pins[name] == expected),
                "original corrective review input closure differs",
            )
            return get(root, {"path": name, "sha256": pins[name]})

        def ref(self, reference):
            adoption.keys(reference, {"path", "sha256"})
            return adoption.document(self.read(reference["path"], reference["sha256"]))

    history, seen = [], set()
    specifications = request["predecessor"]["historical_reviews"]
    require(len(specifications) >= 2, "original historical obligations omitted")
    for specification in specifications:
        original = specification["identity"]["root"]
        reference = specification["review"]
        key = (original, reference["path"])
        require(key not in seen, "duplicate original historical obligation")
        seen.add(key)
        raw = get(original, reference)
        markdown = get(
            original,
            {
                "path": str(Path(reference["path"]).with_name("review.md")),
                "sha256": specification["markdown_sha256"],
            },
        )
        report = parser.parse_review_bundle(
            reference["path"], raw, markdown, schema_root / "schema/record_review.yaml"
        )
        require(
            report["repository"] == adoption.REPOSITORY and report["completion"] == "completed",
            "original historical obligation is incomplete",
        )
        # These exact archived reports retain their original source inventories.
        # No original acquisition rerun or positive release support is asserted.
        history.append(report)
    context = {
        "capability": successor.CAPABILITY,
        "root": root,
        "identity": request["identity"],
        "predecessor": request["predecessor"],
        "complete_before_inventory": request["target_inventory"],
        "source_context": source_context,
        "historical_obligations": history,
        "operations": [operation["mim_id"] for operation in request["operations"]],
        "publication_beforeimages": {
            name: adoption.sha(before[name]) if before[name] is not None else None
            for name in successor.PUBLICATION
        },
    }
    loaded = SimpleNamespace(
        root=schema_root,
        head=request["identity"]["head"],
        request=request,
        inputs=CapturedCorrectionInputs(),
        context=context,
        payloads=payloads,
        operations={operation["mim_id"]: operation for operation in request["operations"]},
    )
    successor._admitted(loaded)
    return {
        "original_root": root,
        "context": context,
        "payloads": payloads,
        "references": [
            {
                "mim_id": operation["mim_id"],
                "primary": operation["primary"],
                "skeptic": operation["skeptic"],
            }
            for operation in request["operations"]
        ],
        "role": "original corrective decisions and holds; no current release approval",
    }


def verify_owner_steps(
    steps, read, baseline_owners, baseline_ledgers, current_owners, current_ledgers, schema_root
):
    """Reconstruct scoped owner semantics; never assert original transaction replay."""
    schema_root = Path(schema_root)
    owners, ledgers = dict(baseline_owners), dict(baseline_ledgers)
    _records(owners, ledgers)
    captured: dict[tuple[str, str, str], bytes] = {}

    def get(root, ref):
        require(
            isinstance(root, str)
            and Path(root).is_absolute()
            and ".." not in Path(root).parts
            and Path(root).as_posix() == root,
            "noncanonical original root",
        )
        adoption.keys(ref, {"path", "sha256"})
        adoption.relative(ref["path"])
        key = (root, ref["path"], ref["sha256"])
        raw = read(root, ref)
        require(
            isinstance(raw, bytes) and adoption.sha(raw) == ref["sha256"], "captured input differs"
        )
        require(key not in captured or captured[key] == raw, "captured input changed")
        captured[key] = raw
        return raw

    source_operations, retained_contexts = [], []
    step_proofs: list[dict] = []
    final_operations, predecessor_owners = [], dict(owners)
    for number, step in enumerate(steps):
        adoption.keys(step, {"kind", "root", "receipt", "manifest", "request", "afterimages"})
        kind, root = step["kind"], step["root"]
        require(kind in {"adoption", "curation"}, "unknown owner transition")
        require(kind != "adoption" or number == 0, "adoption must precede source corrections")
        receipt, manifest, request = [
            adoption.document(get(root, step[name])) for name in ("receipt", "manifest", "request")
        ]
        capability = adoption.CAPABILITY if kind == "adoption" else successor.CAPABILITY
        flag = "scientific_approval_added" if kind == "adoption" else "release_approval_added"
        require(
            receipt["schema_version"]
            == manifest["schema_version"]
            == request["schema_version"]
            == 1
            and receipt["capability"]
            == manifest["capability"]
            == request["capability"]
            == capability
            and receipt["state"] == "COMPLETE"
            and receipt["recovery_required"] is False
            and receipt[flag] is False
            and manifest[flag] is False
            and manifest["status" if kind == "adoption" else "state"] == "PREPARED_CANDIDATE_ONLY"
            and manifest["root"] == root
            and receipt["manifest"] == step["manifest"]
            and manifest["request"] == step["request"],
            "native application/manifest/request binding differs",
        )
        require(
            manifest["before_inventory"] == hashes(owners) == request["target_inventory"],
            "complete owner before-inventory differs",
        )
        before = {
            name: get(root, ref) if ref is not None else None
            for name, ref in receipt["beforeimages"].items()
        }
        require(
            {
                n: raw
                for n, raw in before.items()
                if n.startswith("data/ingredients/") and raw is not None
            }
            == owners
            and all(before.get(name) == raw for name, raw in ledgers.items()),
            "owner/ledger recovery beforeimages differ",
        )
        stage = Path(step["manifest"]["path"]).parent
        require(Path(step["manifest"]["path"]).name == "manifest.json", "invalid native stage")
        require(
            set(step["afterimages"]) == set(manifest["outputs"]), "incomplete staged output set"
        )
        outputs = {}
        for name, pin in manifest["outputs"].items():
            adoption.relative(name)
            ref = {"path": (stage / "candidate" / name).as_posix(), "sha256": pin}
            require(step["afterimages"][name] == ref, "afterimage is not the native staged output")
            outputs[name] = get(root, ref)
        require(
            receipt["expected_outputs" if kind == "adoption" else "outputs"] == manifest["outputs"],
            "completed output set differs",
        )
        for name, pin in manifest["inputs"].items():
            raw = before.get(name)
            if raw is None:
                raw = get(root, {"path": name, "sha256": pin})
            require(adoption.sha(raw) == pin, "manifest input differs")
        get(root, receipt["acceptance"])
        old_records, registry = _records(owners, ledgers)
        if kind == "adoption":
            require(
                set(before) == {*owners, *adoption.AGGREGATES, *LEDGERS}
                and manifest["head"] == request["baseline_commit"],
                "adoption baseline scope differs",
            )
            records, moves, context, intake, reviews = _adoption(
                request, manifest, owners, get, root, schema_root
            )
            # Pure deterministic plan comparison, not minting or allocation authority.
            plan = allocate_ids(registry, records, minted_on=request["timestamp"][:10])
            require(manifest["assignments"] == plan.assignments, "explicit mint assignments differ")
            for name, record in records.items():
                if "mim_id" not in record:
                    record["mim_id"] = plan.assignments[name]
                    record["legacy_identifiers"] = list(
                        dict.fromkeys(
                            [
                                *record.get("legacy_identifiers", []),
                                mim_curie_for_stem(Path(name).stem),
                                record["identifier"],
                            ]
                        )
                    )
                    record_curation_event(
                        record,
                        curator="stable_id_adoption",
                        action="ASSIGNED_MIM_ID",
                        timestamp=request["timestamp"],
                        llm_assisted=True,
                        changes=f"#1303: assigned {record['mim_id']} to the explicitly reviewed distinct concept; mapping and role holds unchanged.",
                    )
            next_ledgers = {
                LEDGERS[0]: dump_registry(plan.registry),
                LEDGERS[1]: dump_lifecycle(plan.registry),
            }
            require(
                outputs[LEDGERS[0]] == next_ledgers[LEDGERS[0]]
                and outputs[LEDGERS[0]].startswith(ledgers[LEDGERS[0]])
                and outputs[LEDGERS[1]] == next_ledgers[LEDGERS[1]] == ledgers[LEDGERS[1]],
                "registry prefix/lifecycle changed",
            )
            expected_owner_outputs = set(records)
            owner_order = list(records)
            extras: tuple[str, ...] = (*adoption.AGGREGATES, LEDGERS[1], LEDGERS[0])
            retained_contexts.append(
                {
                    "kind": kind,
                    "root": root,
                    "context": context,
                    "eligibility_intake": intake,
                    "original_native_reviews": reviews,
                    "decisions": request["decisions"],
                }
            )
        else:
            predecessor_owners = dict(owners)
            final_operations = copy.deepcopy(request["operations"])
            require(
                receipt["root"] == root and request["identity"] == manifest["identity"],
                "curation original identity differs",
            )
            require(request["identity"]["root"] == root, "curation root differs")
            require(
                receipt["predecessor"] == manifest["predecessor"] == request["predecessor"],
                "curation predecessor differs",
            )
            if step_proofs:
                prior = step_proofs[-1]
                predecessor = request["predecessor"]
                require(
                    prior["kind"] == "adoption"
                    and predecessor["kind"] == "adoption"
                    and predecessor["identity"]["root"] == prior["root"]
                    and predecessor["receipt"] == prior["receipt"]
                    and predecessor["manifest"] == prior["manifest"],
                    "curation predecessor is not the selected adoption",
                )
            source_context = adoption.document(get(root, request["source_context"]))
            if retained_contexts:
                require(
                    source_context == retained_contexts[-1]["context"],
                    "original source/hold context differs",
                )
            records, moves, selected = copy.deepcopy(old_records), {}, set()
            payloads = []
            index = build_record_index(old_records)
            require(request["operations"], "empty curation transition")
            for operation in request["operations"]:
                old, new = operation["before"]["path"], operation["after_path"]
                owner_path(new)
                require(old in owners and old not in selected, "duplicate/missing selected owner")
                require(
                    operation["before"]["sha256"] == adoption.sha(owners[old]),
                    "selected beforeimage differs",
                )
                after = adoption.load_yaml(get(root, operation["proposal"]))
                require(operation["evidence"], "curation evidence missing")
                for ref in operation["evidence"]:
                    get(root, ref)
                delta = successor._validate_change(
                    SimpleNamespace(root=schema_root, request=request),
                    operation,
                    old_records[old],
                    after,
                )
                if after["identifier"] != old_records[old]["identifier"]:
                    require(
                        all(
                            n == old
                            for n, r in old_records.items()
                            if r["identifier"] == after["identifier"]
                        ),
                        "primary identity belongs to another owner",
                    )
                    require(
                        all(n == old for n in index.aliases.get(after["identifier"], ())),
                        "identifier alias belongs to another owner",
                    )
                require(new == old or new not in records, "curation owner merge/collision")
                selected.add(old)
                del records[old]
                records[new] = after
                if old != new:
                    moves[old] = new
                payloads.append(
                    {
                        "mim_id": operation["mim_id"],
                        "before_path": old,
                        "after_path": new,
                        "before": old_records[old],
                        "after": after,
                        "delta": delta,
                        "issues": operation["issues"],
                        "evidence": operation["evidence"],
                        "inherited_holds": operation["inherited_holds"],
                        "residual_holds": operation["residual_holds"],
                        "rejected_identifiers": operation["rejected_identifiers"],
                        "rejected_labels": operation["rejected_labels"],
                        "predecessor": request["predecessor"],
                        "source_context_sha256": request["source_context"]["sha256"],
                    }
                )
                source_operations.append(copy.deepcopy(operation))
            expected_owner_outputs = {op["after_path"] for op in request["operations"]}
            owner_order = [op["after_path"] for op in request["operations"]]
            extras = (*adoption.AGGREGATES, successor.MARKER)
            next_ledgers = dict(ledgers)
            require(
                manifest["ledger_sha256"] == hashes(ledgers), "curation changed immutable ledgers"
            )
            require(
                set(before)
                == {
                    *owners,
                    *adoption.AGGREGATES,
                    *LEDGERS,
                    *successor.PUBLICATION,
                    *moves.values(),
                    successor.MARKER,
                },
                "curation beforeimage membership differs",
            )
            require(
                receipt["publication_beforeimages"]
                == manifest["publication_beforeimages"]
                == {
                    name: adoption.sha(before[name]) if before[name] is not None else None
                    for name in successor.PUBLICATION
                },
                "curation publication history differs",
            )
            require(
                adoption.document(outputs[successor.MARKER])
                == {
                    "schema_version": 1,
                    "capability": successor.CAPABILITY,
                    "root": root,
                    "request": step["request"],
                    "predecessor": request["predecessor"],
                },
                "source lineage marker differs",
            )
            retained_contexts.append(
                {
                    "kind": kind,
                    "root": root,
                    "context": source_context,
                    "operations": copy.deepcopy(request["operations"]),
                    "original_native_reviews": _original_curation_reviews(
                        request, manifest, source_context, before, payloads, get, root, schema_root
                    ),
                }
            )
        require(
            manifest["moves"] == moves and set(receipt["retired_sources"]) == set(moves),
            "declared owner moves/retirements differ",
        )
        for old, ref in receipt["retired_sources"].items():
            require(get(root, ref) == owners[old], "retired source archive differs")
        require(
            set(outputs) == expected_owner_outputs | set(extras), "unexpected maintained output"
        )
        after_owners = {name: raw for name, raw in owners.items() if name not in moves}
        after_owners.update({name: outputs[name] for name in expected_owner_outputs})
        require(
            set(after_owners) == set(records)
            and hashes(after_owners) == manifest["after_inventory"],
            "complete owner after-inventory differs",
        )
        for name, record in records.items():
            require(
                adoption.load_yaml(after_owners[name]) == record
                and not validate_ingredient(record, schema_path=schema_root / adoption.SCHEMA),
                "owner afterimage differs from native semantic reconstruction",
            )
        _records(after_owners, next_ledgers)
        _aggregate_check(outputs, records, schema_root)
        events = [
            {"kind": "write", "path": name, "sha256": adoption.sha(outputs[name])}
            for name in owner_order
            if before.get(name) != outputs[name]
        ]
        events.extend(
            {"kind": "relocate", "source": old, "destination": new} for old, new in moves.items()
        )
        events.extend(
            {"kind": "write", "path": name, "sha256": adoption.sha(outputs[name])}
            for name in extras
            if before.get(name) != outputs[name]
        )
        require(
            receipt["completed_operations"] == events, "native completed operation order differs"
        )
        owners, ledgers = after_owners, next_ledgers
        step_proofs.append(copy.deepcopy(step))
    require(
        owners == current_owners and ledgers == current_ledgers,
        "current owner/ledger endpoint differs",
    )
    _records(current_owners, current_ledgers)
    # The caller also rechecks its capsule/current inputs at the enclosing boundary.
    for (root, name, pin), raw in list(captured.items()):
        require(read(root, {"path": name, "sha256": pin}) == raw, "late captured evidence drift")
    return {
        "owners": owners,
        "ledgers": ledgers,
        "operations": final_operations,
        "predecessor_owners": predecessor_owners,
        "source_operations": source_operations,
        "retained_contexts": retained_contexts,
        "scientific_approval_added": False,
        "scope": "semantic_reconstruction_only",
    }
