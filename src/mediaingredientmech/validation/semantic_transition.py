"""Reconstruct a native publication's semantic transition, not its transaction.

Original root/runtime identities remain provenance. This read-only consumer
reconstructs full rows, owners, negative history and exact installed products;
it does not rerun providers, leases or allocation and grants no release approval.
The original-root application verifier remains a separate required workflow gate.
"""

from __future__ import annotations

import json
import os
import types
from pathlib import Path, PurePosixPath
from types import SimpleNamespace
from typing import cast

import yaml  # type: ignore[import-untyped]

from mediaingredientmech import identity_projection as identity
from mediaingredientmech.curate import stable_sssom_publication as publication
from mediaingredientmech.curate.publication_guard import FrozenFile
from mediaingredientmech.export.reviewed_sssom import _safe_identifiers, read_sssom
from mediaingredientmech.ingredient_bundle_contract import read_json, safe_member
from mediaingredientmech.native_acquisition import Evidence as AcquisitionEvidence
from mediaingredientmech.stable_ids import LIFECYCLE_PATH, REGISTRY_PATH

CAPABILITY = "mim-semantic-transition-evidence/v1"
LEDGERS = (str(REGISTRY_PATH), str(LIFECYCLE_PATH))
POLICY = "src/mediaingredientmech/validation/semantic_transition.py"
# #1395: this capability reuses exactly the reviewed native CAS policy from
# culturebotai-claw 4287dce16ee8b5f897bf70f915bdca9aa1484bb6. This is an
# adapter authority, not a modification of any producer or vendored pin.
CAS_POLICY_SHA256 = "3a04bc0435c4f6801994901cffbde9005ca1f589723cc79b32d079fdf6f6ad33"


def require(value, message):
    if not value:
        raise ValueError("Semantic transition: " + message)


def relative(value):
    require(isinstance(value, str) and value, "relative path required")
    path = PurePosixPath(value)
    require(
        not path.is_absolute()
        and ".." not in path.parts
        and str(path) == value
        and "\\" not in value,
        "unsafe relative path",
    )
    return value


class Evidence(AcquisitionEvidence):
    """Preserve the native semantic consumer's existing acquisition API."""

    def __init__(self, inputs, packet_ref):
        super().__init__(inputs, packet_ref, read_json)


class SelectionInputs:
    """Native pure selection input interface with explicit captured pins."""

    def __init__(self, evidence, root, references):
        self.evidence, self.root, self.references = evidence, Path(root), references

    def read(self, name, expected=None):
        require(name in self.references, "uncaptured selection input: " + name)
        ref = self.references[name]
        require(expected is None or ref["sha256"] == expected, "conflicting selection pin")
        return self.evidence.read(str(self.root), ref)


def _link(evidence, root, reference):
    raw = evidence.read(root, reference)
    return raw, read_json(raw)


def _reports(evidence, root, refs, review_inputs, selection, selected_ref, required_inputs):
    """Preserve native installation decisions; they confer no release support."""
    parser = publication._CAPTURE.script("scripts/record_review.py")
    claims = {item["entry_id"]: item for item in selection["rows"] + selection["history"]}
    claims["suppressions"] = selection["suppression"]
    reports = []
    for ref in refs:
        raw = evidence.read(root, ref)
        md = str(PurePosixPath(ref["path"]).with_name("review.md"))
        require(md in review_inputs, "installation Markdown omitted")
        markdown = evidence.read(root, {"path": md, "sha256": review_inputs[md]})
        report = parser.parse_review_bundle(
            ref["path"], raw, markdown, evidence.inputs.root / "schema/record_review.yaml"
        )
        # #1391: use genuine same-repository Git objects at the consumer's
        # physical root. This verifies original revisions/blobs without
        # pretending that its filesystem path is the acquisition root.
        require(
            parser.repository_identity(evidence.inputs.root).lower()
            == "culturebotai/mediaingredientmech"
            and parser.source_provenance(evidence.inputs.root, report)["status"]
            not in {"invalid", "unverified"},
            "original installation Git provenance invalid",
        )
        require(
            report["repository"] == "CultureBotAI/MediaIngredientMech"
            and report["completion"] == "completed"
            and report["scientific_review"] is True,
            "original completed installation assessment required",
        )
        # Acquisition input inventories remain exact historical declarations.
        # Current science is supplied independently by the ordinary release pair.
        source = {item["path"]: item["sha256"] for item in report["source"]["inputs"]}
        # #1391: native _bundle separately reads report inputs; the request's
        # review_inputs need not duplicate them. Bind each actual byte instead.
        for name, pin in source.items():
            evidence.read(root, {"path": name, "sha256": pin})
            require(
                name not in review_inputs or review_inputs[name] == pin,
                "conflicting installation input pin",
            )
        require(
            all(source.get(name) == pin for name, pin in required_inputs.items()),
            "installation required input inventory differs",
        )
        targets = {
            t.get("selector"): t for t in report["targets"] if t.get("path") == selected_ref["path"]
        }
        require(set(targets) == set(claims), "installation row/history coverage incomplete")
        for key, claim in claims.items():
            target = targets[key]
            require(
                target["kind"] == "snapshot_row"
                and target.get("semantic_digest")
                == {
                    "algorithm": "sha256-canonical-json-v1",
                    "sha256": publication.native().digest(claim),
                    "description": "Complete stable publication selection",
                },
                "installation payload changed",
            )
            assessment = publication._assessment(report, target["target_id"])
            dims = {d["name"]: d["value"] for d in assessment.get("dimensions", [])}
            action = (
                "PRESERVE_SUPPRESSION_HISTORY"
                if key == "suppressions"
                else (
                    "PRESERVE_HISTORICAL_OBLIGATIONS"
                    if key.startswith("history-")
                    else claim["disposition"]
                )
            )
            require(
                dims.get("publication_action") == action
                and dims.get("publication_scope") == "canonical_installation_not_release_approval",
                "installation scope/action changed",
            )
            bases = {item["evidence_id"]: item for item in report["evidence"]}

            def captured(eid, bases=bases, source=source):
                item = bases[eid]
                return (
                    item["reference"] in source
                    and item.get("snapshot_sha256") == source[item["reference"]]
                )

            require(
                any(captured(eid) for eid in assessment["evidence_ids"]),
                "installation captured evidence omitted",
            )
            if action == "INSTALL_SUPPORTED":
                require(
                    any(
                        captured(eid)
                        and bases[eid]["kind"] in {"primary_source", "database", "authority"}
                        and bases[eid]["support"] == "supports"
                        for eid in assessment["evidence_ids"]
                    ),
                    "supported installation primary evidence omitted",
                )
        reports.append(report)
    require(
        len(reports) == 2
        and refs[0]["path"] != refs[1]["path"]
        and reports[0]["reviewer"]["identity"] != reports[1]["reviewer"]["identity"]
        and reports[1]["reviewer"].get("independence") == "independent"
        and reports[1]["reviewer"].get("independence_basis"),
        "original independent installation pair omitted",
    )


def _history(evidence, specifications):
    parser = publication._CAPTURE.script("scripts/record_review.py")
    captures = evidence.packet["history"]
    require(len(captures) == len(specifications), "historical acquisition inventory differs")
    result = []
    for number, (capture, specification) in enumerate(
        zip(captures, specifications, strict=True), 1
    ):
        require(
            set(capture) == {"binding", "source_inputs"} and capture["binding"] == specification,
            "historical binding differs",
        )
        root, ref = specification["root"], specification["review"]
        raw = evidence.read(root, ref)
        md = str(PurePosixPath(ref["path"]).with_name("review.md"))
        markdown = evidence.read(root, {"path": md, "sha256": specification["markdown_sha256"]})
        report = parser.parse_review_bundle(
            ref["path"], raw, markdown, evidence.inputs.root / "schema/record_review.yaml"
        )
        require(
            report["repository"] == "CultureBotAI/MediaIngredientMech"
            and report["completion"] == "completed",
            "historical report incomplete",
        )
        declared = {item["path"]: item["sha256"] for item in report["source"]["inputs"]}
        require(
            all(capture["source_inputs"].get(name) == pin for name, pin in declared.items()),
            "historical input declaration omitted",
        )
        require(
            capture["source_inputs"].get(ref["path"]) == ref["sha256"]
            and capture["source_inputs"].get(md) == specification["markdown_sha256"],
            "historical pair pins omitted",
        )
        result.append(
            {
                "entry_id": f"history-{number:03d}",
                "binding": specification,
                "role": "historical acquisition; not current stable-row approval",
                "original_report": report,
                "original_source_inputs": capture["source_inputs"],
            }
        )
    return result


def _cas(evidence, root, generation, manifest, before, candidate, owners, source):
    """Reconstruct every mandatory diagnostic hold from actual pinned claims."""
    reference = generation.get("cas_dispositions")
    proof = manifest.get("cas_dispositions")
    require((reference is None) == (proof is None), "CAS request/proof selection differs")
    if reference is None:
        # #1395: absence is not authority to erase an original diagnostic hold.
        # Keep exactly the native prefixed-token scope; unrelated bare numeric
        # synonyms are not silently added to this diagnostic contract.
        historical = read_sssom(Path("before"), content=before)[2]
        for row in [*historical, *candidate]:
            tokens = {
                field: "|".join(
                    token
                    for token in row.get(field, "").split("|")
                    if token.strip().casefold().startswith("cas:")
                )
                for field in ("object_id", "other", "xref")
            }
            try:
                _safe_identifiers(tokens)
            except ValueError as exc:
                raise ValueError(
                    "Semantic transition: invalid historical/current CAS requires explicit disposition proof"
                ) from exc
        return
    claw = generation["claw"]["root"]
    name = "src/kg_microbe_utils/stable_mim.py"
    absolute = str(PurePosixPath(claw) / name)
    pin = generation["claw"]["files"].get(absolute)
    require(
        pin == manifest["producer_import_snapshot"].get(absolute), "CAS producer binding differs"
    )
    raw = evidence.read(claw, {"path": name, "sha256": pin})
    require(
        pin == CAS_POLICY_SHA256 and identity.sha(raw) == CAS_POLICY_SHA256,
        "CAS producer implementation is not the reviewed adapter authority",
    )
    native = types.ModuleType("_captured_semantic_cas_contract")
    native.__file__ = absolute
    exec(compile(raw, absolute, "exec", dont_inherit=True), native.__dict__)
    request = evidence.document(root, reference)
    claims = evidence.document(root, request["claims"])
    pins = {
        **request["review_inputs"],
        request["claims"]["path"]: request["claims"]["sha256"],
        **{ref["path"]: ref["sha256"] for ref in request["reviews"]},
        **claims["evidence_inputs"],
        claims["canonical"]["path"]: claims["canonical"]["sha256"],
        **{entry["owner"]["path"]: entry["owner"]["sha256"] for entry in claims["entries"]},
    }
    if claims["source_correction"] is not None:
        pins[claims["source_correction"]["path"]] = claims["source_correction"]["sha256"]
    checked_request, checked_claims, complete = native._cas_documents(
        Path(root),
        Path(root) / reference["path"],
        evidence.read(root, reference),
        reference["sha256"],
        lambda path: evidence.read(
            root, {"path": str(path.relative_to(root)), "sha256": pins[str(path.relative_to(root))]}
        ),
    )
    require(
        checked_request == request and checked_claims == claims,
        "native CAS document contract differs",
    )
    for path, pin in complete.items():
        evidence.read(root, {"path": str(path.relative_to(root)), "sha256": pin})
    # Native document discovery is not the original scientific pair check.
    # #1395: preserve those exact decisions using explicit captured bytes and
    # the consumer's genuine Git authority. Only the physical lookup namespace
    # changes; original acquisition identities remain in the packet/proof.
    physical = evidence.inputs.root
    snapshot = {
        physical
        / str(path.relative_to(root)): evidence.read(
            root, {"path": str(path.relative_to(root)), "sha256": pin}
        )
        for path, pin in complete.items()
    }
    for policy in ("scripts/record_review.py", "schema/record_review.yaml"):
        require(
            snapshot[physical / policy] == publication._CAPTURE.files[policy][0],
            "CAS native review implementation differs: " + policy,
        )
    require(claims["head"] == generation["head"], "CAS acquisition head differs")
    reconstructed = native.cas_disposition_evidence(
        physical,
        physical / reference["path"],
        evidence.read(root, reference),
        reference["sha256"],
        snapshot,
        generation["head"],
    )
    require(
        reconstructed["path"] == str(physical / reference["path"])
        and reconstructed["relative_path"] == reference["path"]
        and proof["path"] == str(PurePosixPath(root) / reference["path"]),
        "CAS original and physical reference identities differ",
    )
    reconstructed["path"] = proof["path"]
    require(
        reconstructed
        == {k: v for k, v in proof.items() if k not in {"held_rows", "retired_entries"}},
        "CAS original native review proof differs",
    )
    require(
        proof["request"] == request
        and proof["content"] == claims
        and proof["sha256"] == reference["sha256"],
        "CAS claims/request changed",
    )
    require(
        claims["canonical"]["sha256"] == identity.sha(before)
        and claims["canonical"]["path"] == publication.CANONICAL,
        "CAS historical canonical differs",
    )
    _, _, old = read_sssom(Path("before"), content=before)
    require(
        len({entry["row_position"] for entry in claims["entries"]}) == len(claims["entries"]),
        "duplicate CAS position",
    )
    require(
        {entry["row_position"] for entry in claims["entries"]}
        == {position for position, row in enumerate(old, 1) if native._cas_invalid_tokens(row)},
        "historical invalid-CAS obligation omitted",
    )
    for entry in claims["entries"]:
        require(
            0 < entry["row_position"] <= len(old)
            and old[entry["row_position"] - 1] == entry["row"],
            "CAS historical row/position differs",
        )
        name = entry["owner"]["path"]
        require(
            name in owners and identity.sha(owners[name]) == entry["owner"]["sha256"],
            "CAS current owner differs",
        )
        native._cas_selected(
            entry, entry["row"], entry["owner"]["mim_id"], yaml.safe_load(owners[name])
        )
    # Native pure finalizer checks exhaustive invalid-token coverage, exact
    # held rows and retired non-emission. Rehashing held_rows cannot omit a hold.
    require(
        native.finalize_cas_dispositions(
            {k: v for k, v in proof.items() if k not in {"held_rows", "retired_entries"}}, candidate
        )
        == proof,
        "CAS mandatory held/retired accounting differs",
    )
    endpoint = None
    if generation.get("curation_successor") is not None:
        endpoint = SimpleNamespace(
            loaded=SimpleNamespace(
                request={"operations": source["operations"]},
                predecessor=SimpleNamespace(
                    owners={
                        name: SimpleNamespace(content=raw)
                        for name, raw in source["predecessor_owners"].items()
                    }
                ),
            )
        )
    publication._cas_source_correction(manifest, endpoint, generation.get("curation_successor"))


def verify(inputs, packet_ref, history, owners, ledgers):
    """Reconstruct native semantic links; never claim portable transaction replay."""
    from mediaingredientmech.validation.semantic_owner_transition import verify_owner_steps

    evidence = Evidence(inputs, packet_ref)
    selected = evidence.packet["publication"]
    require(
        set(selected) == {"root", "receipt", "manifest", "request"}, "invalid publication selection"
    )
    root = selected["root"]
    _, receipt = _link(evidence, root, selected["receipt"])
    _, manifest = _link(evidence, root, selected["manifest"])
    _, request = _link(evidence, root, selected["request"])
    require(
        receipt["manifest"] == selected["manifest"] and manifest["request"] == selected["request"],
        "publication native reference chain differs",
    )
    require(
        receipt["capability"] == publication.CAPABILITY
        and receipt["state"] == "COMPLETE"
        and receipt["recovery_required"] is False
        and receipt["scientific_approval_added"] is False,
        "incomplete original publication evidence",
    )
    require(
        manifest["root"] == root
        and manifest["capability"] == publication.CAPABILITY
        and manifest["scientific_approval_added"] is False
        and request["capability"] == publication.CAPABILITY,
        "publication identity/scope differs",
    )
    require(
        set(receipt["beforeimages"]) == set(publication.OUTPUTS) == set(manifest["outputs"])
        and receipt["outputs"] == manifest["outputs"],
        "publication output inventory differs",
    )
    before = {
        name: None if ref is None else SimpleNamespace(content=evidence.read(root, ref))
        for name, ref in receipt["beforeimages"].items()
    }
    require(
        before[publication.CANONICAL] is not None
        and cast(SimpleNamespace, before[publication.CANONICAL]).content
        == history["proof"].after[publication.CANONICAL],
        "publication is not continuous with exact historical stable endpoint",
    )
    require(
        manifest["before"]
        == {
            name: None if value is None else identity.sha(value.content)
            for name, value in before.items()
        },
        "publication beforeimage digest differs",
    )
    baseline_owners = {
        name: raw
        for name, raw in history["proof"].after.items()
        if name.startswith("data/ingredients/")
    }
    baseline_ledgers = {name: history["proof"].after[name] for name in LEDGERS}
    source = verify_owner_steps(
        evidence.packet["sources"],
        evidence.read,
        baseline_owners,
        baseline_ledgers,
        owners,
        ledgers,
        inputs.root,
    )
    generation = evidence.document(root, request["generation"])
    require(
        generation["root"] == root
        and generation["state"] == "COMPLETE"
        and generation["returncode"] == 0,
        "original generation evidence incomplete",
    )
    diagnostic = evidence.document(root, generation["outputs"]["manifest"])
    candidate = evidence.read(root, generation["outputs"]["sssom"])
    sidecar = evidence.read(root, generation["outputs"]["suppressions"])
    _, _, candidate_rows = read_sssom(Path("candidate"), content=candidate)
    _cas(
        evidence,
        root,
        generation,
        diagnostic,
        cast(SimpleNamespace, before[publication.CANONICAL]).content,
        candidate_rows,
        owners,
        source,
    )
    records = {name: yaml.safe_load(raw) for name, raw in owners.items()}
    owner_refs = {name: SimpleNamespace(content=raw) for name, raw in owners.items()}
    require(
        manifest["owners"] == {name: identity.sha(raw) for name, raw in owners.items()},
        "publication owner inventory differs",
    )
    references = {name: {"path": name, "sha256": pin} for name, pin in manifest["inputs"].items()}
    selector_inputs = SelectionInputs(evidence, root, references)
    historical = _history(evidence, request["historical_reviews"])
    successor = None
    if "curation_successor" in generation:
        endpoint = evidence.document(root, generation["curation_successor"])
        last = evidence.packet["sources"][-1]
        source_manifest = evidence.document(last["root"], last["manifest"])
        require(
            last["kind"] == "curation"
            and endpoint["root"] == last["root"]
            and endpoint["stage"] == str(PurePosixPath(last["manifest"]["path"]).parent)
            and endpoint["manifest"] == last["manifest"]
            and endpoint["receipt"] == last["receipt"]
            and endpoint["producer"] == source_manifest["producer"],
            "source endpoint reference differs",
        )
        closure = generation["successor_input_closure"]
        require(
            closure["reference"] == endpoint
            and closure["publication_beforeimages"] == source_manifest["publication_beforeimages"]
            and source_manifest["publication_beforeimages"] == manifest["before"],
            "source publication-history closure differs",
        )
        # Preserve the original qualified acquisition closure as context. This
        # semantic consumer does not claim to rerun its original transaction.
        successor = SimpleNamespace(closure=lambda: generation["successor_input_closure"])
    loaded = SimpleNamespace(
        before=before,
        candidate=candidate,
        sidecar=sidecar,
        records=records,
        owners=owner_refs,
        manifest=diagnostic,
        generation=generation,
        request=request,
        inputs=selector_inputs,
        history=historical,
        successor=successor,
    )
    selection = evidence.document(root, request["selection"])
    unassessed = json.loads(json.dumps(selection))
    for entry in unassessed["rows"]:
        require(
            isinstance(entry.get("reason"), str) and entry["reason"].strip(),
            "missing publication rationale",
        )
        allowed = (
            {"INSTALL_SUPPORTED", "INSTALL_WITHHOLD"}
            if entry["candidate_position"]
            else {"REMOVE_WITH_HISTORY"}
        )
        require(
            entry["disposition"] in allowed
            and (
                entry.get("mandatory_disposition") is None
                or entry["disposition"] == entry["mandatory_disposition"]
            ),
            "invalid or overridden publication disposition",
        )
        entry["disposition"], entry["reason"] = None, None
    require(
        unassessed == publication._selection(loaded),
        "full native selection/position/history reconstruction differs",
    )
    required_inputs = {
        request["selection"]["path"]: request["selection"]["sha256"],
        "MAPPING_SEMANTICS.md": manifest["inputs"]["MAPPING_SEMANTICS.md"],
        **{name: identity.sha(raw) for name, raw in owners.items()},
        **{
            name: identity.sha(value.content) for name, value in before.items() if value is not None
        },
        **{name: manifest["inputs"][name] for name in (*LEDGERS, publication.CONTRACT)},
        request["generation"]["path"]: request["generation"]["sha256"],
    }
    if successor is not None:
        ref = generation["curation_successor"]
        required_inputs.update(
            {ref["path"]: ref["sha256"], **generation["successor_input_closure"]["target"]}
        )
    else:
        ref = generation["adoption"]["receipt"]
        required_inputs[ref["path"]] = ref["sha256"]
    _reports(
        evidence,
        root,
        request["reviews"],
        request["review_inputs"],
        selection,
        request["selection"],
        required_inputs,
    )
    _, fields, _ = read_sssom(Path("candidate"), content=candidate)
    rows = [
        entry["proposed_row"] for entry in selection["rows"] if entry["proposed_row"] is not None
    ]
    tsv = publication._render_candidate(candidate, fields, rows)
    suppression = publication._tsv(publication.SIDECAR_FIELDS, selection["suppression"]["proposed"])
    old_provenance = before[publication.PROVENANCE]
    provenance = {
        "schema_version": 1,
        "capability": publication.CAPABILITY,
        "scientific_approval_added": False,
        "ordinary_release_review_required": True,
        "generation": request["generation"],
        "selection": selection,
        "reviews": request["reviews"],
        "review_inputs": request["review_inputs"],
        "historical_publication": (
            None if old_provenance is None else read_json(old_provenance.content)
        ),
        "retention_policy": "Matched rows retain prior source tokens and comments; all prior rows/stamps/suppressions remain in selection history. No validation stamp is inherited.",
        "artifacts": {
            publication.CANONICAL: identity.sha(tsv),
            publication.SUPPRESSIONS: identity.sha(suppression),
        },
    }
    outputs = {
        publication.CANONICAL: tsv,
        publication.SUPPRESSIONS: suppression,
        publication.DIAGNOSTIC_MANIFEST: evidence.read(root, generation["outputs"]["manifest"]),
        publication.PROVENANCE: publication.native().encoded(provenance),
    }
    require(
        {name: identity.sha(raw) for name, raw in outputs.items()} == manifest["outputs"],
        "reconstructed publication outputs differ",
    )
    expected_events = [
        {"path": name, "sha256": identity.sha(raw)}
        for name, raw in outputs.items()
        if before[name] is None or cast(SimpleNamespace, before[name]).content != raw
    ]
    require(
        receipt["completed_operations"] == expected_events,
        "publication completed row phase accounting differs",
    )
    stage = str(PurePosixPath(selected["manifest"]["path"]).parent)
    for name, raw in outputs.items():
        require(
            evidence.read(root, {"path": stage + "/candidate/" + name, "sha256": identity.sha(raw)})
            == raw
            == inputs.read(name),
            "staged/installed canonical output differs",
        )
    # Acceptance is original transaction context, not a new approval certificate.
    evidence.read(root, receipt["acceptance"])
    inputs.recheck()
    return {
        "provenance": provenance,
        "source": source,
        "evidence": evidence,
        "scope": "semantic_reconstruction_not_transaction_reexecution",
    }


def capture(root, stage, receipt_path, output):
    """Capture exact evidence only after the real original-root native verifier.

    The returned packet is not a success certificate: `verify` independently
    reconstructs its semantic links. No maintained source or publication writes.
    """
    root = Path(root).absolute()
    stage, receipt_path = Path(stage), Path(receipt_path)
    stage = stage if stage.is_absolute() else safe_member(root, stage.as_posix())
    receipt_path = (
        receipt_path if receipt_path.is_absolute() else safe_member(root, receipt_path.as_posix())
    )
    output = safe_member(root, str(output))
    require(not os.path.lexists(output), "evidence output already occupied")
    publication.verify_completed(root, stage, receipt_path)
    captured = {}
    frozen = {}

    def add(original_root, name, raw, origin):
        original_root = str(original_root)
        relative(name)
        key = (original_root, name, identity.sha(raw))
        if key not in captured:
            captured[key] = (raw, str(origin))
        return {"path": name, "sha256": key[2]}

    def read_ref(original_root, ref):
        key = (str(original_root), ref["path"], ref["sha256"])
        if key not in captured:
            path = safe_member(Path(original_root), ref["path"])
            value = FrozenFile.capture(path)
            require(
                identity.sha(value.content) == ref["sha256"],
                "original acquisition changed: " + str(path),
            )
            frozen[str(path)] = value
            add(original_root, ref["path"], value.content, path)
        return captured[key][0]

    def file_ref(original_root, path):
        path = Path(path)
        if not path.is_absolute():
            path = safe_member(Path(original_root), path.as_posix())
        value = FrozenFile.capture(path)
        frozen[str(path)] = value
        return add(original_root, str(path.relative_to(original_root)), value.content, path)

    def document(original_root, ref):
        return read_json(read_ref(original_root, ref))

    application_ref = file_ref(root, receipt_path)
    application = document(root, application_ref)
    manifest_ref = application["manifest"]
    manifest = document(root, manifest_ref)
    request_ref = manifest["request"]
    request = document(root, request_ref)
    for name, ref in application["beforeimages"].items():
        if ref is not None:
            raw = read_ref(root, ref)
            add(root, name, raw, root / ref["path"])
    for name, pin in manifest["outputs"].items():
        read_ref(root, {"path": name, "sha256": pin})
        read_ref(root, {"path": str(stage.relative_to(root)) + "/candidate/" + name, "sha256": pin})
    read_ref(root, application["acceptance"])
    read_ref(root, application["operational_fit"]["receipt"])
    generation = document(root, request["generation"])
    diagnostic = document(root, generation["outputs"]["manifest"])
    for ref in generation["outputs"].values():
        read_ref(root, ref)
    read_ref(root, generation["stdout"])
    read_ref(root, generation["stderr"])

    def source_step(kind, original_root, receipt_ref, native_manifest_ref):
        original_root = Path(original_root)
        receipt = document(original_root, receipt_ref)
        native_manifest = document(original_root, native_manifest_ref)
        req_ref = native_manifest["request"]
        req = document(original_root, req_ref)
        for name, ref in receipt["beforeimages"].items():
            if ref is not None:
                raw = read_ref(original_root, ref)
                add(original_root, name, raw, original_root / ref["path"])
        afterimages = {}
        native_stage = PurePosixPath(native_manifest_ref["path"]).parent
        for name, pin in native_manifest["outputs"].items():
            ref = {"path": str(native_stage / "candidate" / name), "sha256": pin}
            raw = read_ref(original_root, ref)
            afterimages[name] = ref
            add(original_root, name, raw, original_root / ref["path"])
        for name, pin in native_manifest["after_inventory"].items():
            if name not in afterimages:
                ref = {"path": name, "sha256": pin}
                read_ref(original_root, ref)
        for name, pin in native_manifest["inputs"].items():
            read_ref(original_root, {"path": name, "sha256": pin})
        for ref in receipt.get("retired_sources", {}).values():
            read_ref(original_root, ref)
        read_ref(original_root, receipt["acceptance"])
        if kind == "adoption":
            legacy_root = Path(req["legacy"]["root"])
            for name, pin in native_manifest["legacy_inputs"].items():
                read_ref(legacy_root, {"path": name, "sha256": pin})
        else:
            for specification in req["predecessor"]["historical_reviews"]:
                history_root = specification["identity"]["root"]
                read_ref(history_root, specification["review"])
                read_ref(
                    history_root,
                    {
                        "path": str(
                            PurePosixPath(specification["review"]["path"]).with_name("review.md")
                        ),
                        "sha256": specification["markdown_sha256"],
                    },
                )
        result = {
            "kind": kind,
            "root": str(original_root),
            "receipt": receipt_ref,
            "manifest": native_manifest_ref,
            "request": req_ref,
            "afterimages": afterimages,
        }
        return result, req

    sources: list[dict] = []
    if "curation_successor" in generation:
        endpoint = document(root, generation["curation_successor"])
        current, req = source_step(
            "curation", endpoint["root"], endpoint["receipt"], endpoint["manifest"]
        )
        predecessor = req["predecessor"]
        require(predecessor["kind"] == "adoption", "unsupported predecessor chain")
        adopted, _ = source_step(
            "adoption",
            predecessor["identity"]["root"],
            predecessor["receipt"],
            predecessor["manifest"],
        )
        sources.extend((adopted, current))
    else:
        selected = generation["adoption"]
        receipt = document(root, selected["receipt"])
        adopted, _ = source_step("adoption", root, selected["receipt"], receipt["manifest"])
        sources.append(adopted)

    # All generation source members already have explicit original root/paths.
    # Capturing them preserves CAS/retirement review inventories. They are not
    # replayed here as a substitute for current scientific release evidence.
    original_roots = [
        root,
        Path(generation["claw"]["root"]),
        Path(generation["kg_microbe"]["root"]),
    ]
    for item in diagnostic["source_inputs"]:
        if item["sha256"] is None:
            require(not os.path.lexists(item["path"]), "original explicit absence changed")
            continue
        path = Path(item["path"])
        matches = [parent for parent in original_roots if path.is_relative_to(parent)]
        require(len(matches) == 1, "ambiguous generation source root")
        original_root = matches[0]
        read_ref(
            original_root, {"path": str(path.relative_to(original_root)), "sha256": item["sha256"]}
        )
    for ref in request["reviews"]:
        read_ref(root, ref)
        md = str(PurePosixPath(ref["path"]).with_name("review.md"))
        read_ref(root, {"path": md, "sha256": request["review_inputs"][md]})
    read_ref(root, request["selection"])
    for name, pin in manifest["inputs"].items():
        # All actual publication inputs remain captured. Beforeimage aliases
        # select their original hashes, never the now-installed canonical bytes.
        read_ref(root, {"path": name, "sha256": pin})
    history = []
    for specification in request["historical_reviews"]:
        original_root = specification["root"]
        raw = read_ref(original_root, specification["review"])
        md = str(PurePosixPath(specification["review"]["path"]).with_name("review.md"))
        read_ref(original_root, {"path": md, "sha256": specification["markdown_sha256"]})
        report = yaml.safe_load(raw)
        pins = {item["path"]: item["sha256"] for item in report["source"]["inputs"]}
        pins.update(
            {
                specification["review"]["path"]: specification["review"]["sha256"],
                md: specification["markdown_sha256"],
            }
        )
        history.append({"binding": specification, "source_inputs": pins})
    for value in frozen.values():
        value.verify()
    publication.verify_completed(root, stage, receipt_path)
    for value in frozen.values():
        value.verify()
    output.mkdir()
    members = output / "members"
    members.mkdir()
    entries = []
    for number, ((original_root, name, pin), (raw, origin)) in enumerate(
        sorted(captured.items()), 1
    ):
        member = members / f"{number:06d}.bin"
        with member.open("xb") as stream:
            stream.write(raw)
        entries.append(
            {
                "root": original_root,
                "path": name,
                "sha256": pin,
                "member": str(member.relative_to(root)),
                "acquired_from": origin,
            }
        )
    packet = {
        "schema_version": 1,
        "capability": CAPABILITY,
        "scope": "semantic_reconstruction_not_transaction_reexecution",
        "files": entries,
        "publication": {
            "root": str(root),
            "receipt": application_ref,
            "manifest": manifest_ref,
            "request": request_ref,
        },
        "sources": sources,
        "history": history,
    }
    raw = publication.native().encoded(packet)
    path = output / "transition.json"
    with path.open("xb") as stream:
        stream.write(raw)
    for value in frozen.values():
        value.verify()
    return {"path": str(path.relative_to(root)), "sha256": identity.sha(raw)}
