"""#1247: closed private origin/operation accounting, never scientific approval.

The native owner operator is called in prepare-only mode. No receipt or owner
is written. Publication facts are checked against actual Git objects.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def closed(obj, keys, label):
    require(isinstance(obj, dict) and set(obj) == set(keys), f"{label}: unknown/missing fields")
    return obj


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def object_hash(obj):
    return digest(
        json.dumps(
            obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
        ).encode()
    )


def hash_value(value):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value), "invalid SHA256")
    return value


def text(value):
    require(isinstance(value, str) and value.strip(), "missing text")
    return value


def read_json(raw):
    def pairs(items):
        obj = {}
        for k, v in items:
            require(k not in obj, "duplicate JSON key")
            obj[k] = v
        return obj

    return json.loads(
        raw, object_pairs_hook=pairs, parse_constant=lambda _: require(False, "nonfinite JSON")
    )


class Proofs:
    def __init__(self, root, native):
        self.root = Path(root).absolute()
        self.native = native
        native.no_alias(self.root)
        require(self.root.is_dir(), "missing evidence root")
        self.files = {}
        self.start_head = native.git(self.root, "rev-parse", "HEAD").decode().strip()
        native.commit(self.start_head)

    def ref(self, ref):
        closed(ref, {"path", "sha256"}, "file reference")
        path = self.native.relative(ref["path"])
        expected = hash_value(ref["sha256"])
        captured = self.native.FrozenFile.capture(self.root / path)
        require(digest(captured.content) == expected, "file evidence hash differs")
        if path in self.files:
            require(self.files[path].content == captured.content, "input drift")
        self.files[path] = captured
        return captured.content

    def published(self, ref, head):
        closed(ref, {"path", "sha256", "published_path"}, "published reference")
        self.native.commit(head)
        rel = self.native.relative(ref["published_path"])
        raw = self.ref({k: ref[k] for k in ("path", "sha256")})
        mode = self.native.git(self.root, "ls-tree", head, "--", rel).split(b" ", 1)[0]
        require(mode in {b"100644", b"100755"}, "published proof is not a regular Git blob")
        require(
            self.native.git(self.root, "show", f"{head}:{rel}") == raw,
            "published evidence differs",
        )
        return raw

    def refs(self, values):
        require(isinstance(values, list) and bool(values), "missing exact evidence references")
        seen = set()
        for ref in values:
            raw = self.ref(ref)
            key = (ref["path"], ref["sha256"])
            require(key not in seen, "duplicate evidence reference")
            seen.add(key)
            require(bool(raw), "empty evidence file")
        return seen

    def recheck(self):
        for path, frozen in self.files.items():
            self.native.no_alias(self.root / path)
            frozen.verify()
        require(
            self.native.git(self.root, "rev-parse", "HEAD").decode().strip() == self.start_head,
            "Local HEAD changed during crosswalk verification",
        )


def _origins(rows, label):
    require(isinstance(rows, list), f"{label} must be a list")
    result = {}
    for row in rows:
        require(isinstance(row, dict), "invalid origin")
        oid = text(row.get("origin_id"))
        require(oid not in result, "duplicate origin denominator")
        result[oid] = row
    return result


def _verify_origin(row, binding, proof):
    closed(binding, {"origin_id", "proposal_ledger", "payload"}, "origin binding")
    require(binding["origin_id"] == row["origin_id"], "origin binding mismatch")
    slot = row.get("worker_slot")
    require(type(slot) is int and 1 <= slot <= 10, "invalid worker slot")
    proposal = row.get("proposal")
    require(isinstance(proposal, dict), "missing complete proposal")
    require(
        row["origin_id"] == f"w{slot:02}::{proposal.get('proposal_id')}",
        "origin identity differs",
    )
    head = row.get("published_head")
    raw = proof.published(binding["proposal_ledger"], head)
    ledger = read_json(raw)
    require(
        isinstance(ledger, dict) and isinstance(ledger.get("proposals"), list),
        "missing proposal ledger",
    )
    members = ledger["proposals"]
    ids = [p.get("proposal_id") for p in members]
    require(
        all(isinstance(p, str) and p for p in ids) and len(ids) == len(set(ids)),
        "duplicate/malformed published proposals",
    )
    matches = [p for p in members if p["proposal_id"] == proposal["proposal_id"]]
    require(matches == [proposal], "origin proposal differs from exact published object")
    require(
        hash_value(row.get("proposal_object_sha256")) == object_hash(proposal),
        "origin proposal object hash differs",
    )
    cap = closed(proposal.get("after_capture"), {"root", "path", "sha256"}, "source payload")
    require(cap["root"] == "artifact", "non-artifact source payload")
    original_path = proof.native.relative(cap["path"])
    source_hash = hash_value(cap["sha256"])
    require(hash_value(row.get("payload_sha256")) == source_hash, "origin payload hash differs")
    pubpath = binding["payload"]["published_path"]
    require(
        pubpath == original_path or pubpath.endswith("/" + original_path),
        "source payload path differs",
    )
    require(
        digest(proof.published(binding["payload"], head)) == source_hash,
        "source payload bytes differ",
    )


def _verify_native_origin(origin, row, binding, prepared):
    """#1247 join originals, not the separately reconciled final operation payload."""
    native_bindings = {b["binding_id"]: b for b in prepared.plan["bindings"]}
    for name, role, crosswalk_name in (
        ("proposal_binding", "proposal", "proposal_ledger"),
        ("payload_binding", "evidence", "payload"),
    ):
        actual = native_bindings[origin[name]]
        declared = binding[crosswalk_name]
        require(actual["role"] == role, "native original binding role differs")
        require(
            (actual["published_head"], actual["published_path"], actual["sha256"])
            == (row["published_head"], declared["published_path"], declared["sha256"]),
            "native original published binding differs",
        )
        # Native prepare already verified actual local capture bytes and Git metadata.
        # Local capture paths may differ legitimately; publication identity cannot.
        raw = prepared.inputs[actual["path"]].content
        require(digest(raw) == declared["sha256"], "native original captured bytes differ")
        if name == "proposal_binding":
            ledger = read_json(raw)
            matches = [p for p in ledger["proposals"] if p["proposal_id"] == origin["proposal_id"]]
            require(matches == [row["proposal"]], "native complete original proposal differs")
            require(
                object_hash(matches[0]) == row["proposal_object_sha256"],
                "native original proposal object hash differs",
            )
        else:
            require(
                digest(raw) == row["payload_sha256"] == row["proposal"]["after_capture"]["sha256"],
                "native original payload differs",
            )


def validate_resolution_crosswalk(
    origins,
    resolutions,
    *,
    root=None,
    origin_bindings=None,
    successor_origins=None,
    native_plan=None,
):
    """Validate actual evidence and a closed operation/retirement crosswalk.

    All supplied origins (including separately supplied published successors)
    need exactly one row. Apply rows require a real native prepare-only plan.
    Scientific applicability and author independence remain separate reviews.
    """
    initial = _origins(origins, "origins")
    extra = _origins([] if successor_origins is None else successor_origins, "successor origins")
    require(not (set(initial) & set(extra)), "duplicate origin across universes")
    universe = {**initial, **extra}
    require(bool(universe), "empty origin universe")
    require(
        root is not None and isinstance(origin_bindings, list),
        "exact evidence/native context required",
    )
    from mediaingredientmech.curate import campaign_owner_apply as native

    proof = Proofs(root, native)
    bindings = _origins(origin_bindings, "origin bindings")
    require(set(bindings) == set(universe), "origin proof universe differs")
    for oid, row in universe.items():
        _verify_origin(row, bindings[oid], proof)

    require(isinstance(resolutions, list), "resolutions must be a list")
    resolved = _origins(resolutions, "resolutions")
    require(set(resolved) == set(universe), "resolution crosswalk omits/adds origins")
    prepared = None
    native_ref = None
    if native_plan is not None:
        closed(native_plan, {"plan", "acceptance"}, "native plan proof")
        for ref in native_plan.values():
            proof.ref(ref)
        prepared = native.prepare(
            proof.root,
            proof.root / native_plan["plan"]["path"],
            proof.root / native_plan["acceptance"]["path"],
        )
        require(
            prepared.plan["baseline_commit"] == proof.start_head,
            "Native plan baseline differs from entry HEAD",
        )
        native_ref = {
            "plan_sha256": prepared.plan_ref["sha256"],
            "acceptance_sha256": prepared.acceptance_ref["sha256"],
            "before_inventory_sha256": prepared.plan["before_inventory"]["sha256"],
            "after_inventory_sha256": prepared.plan["after_inventory"]["sha256"],
            "native_input_sha256": native.hashes(prepared.inputs),
            "before_owner_sha256": native.hashes(prepared.before),
            "after_owner_sha256": prepared.after_inventory,
        }
    operations = {} if prepared is None else {e["operation_id"]: e for e in prepared.operations}
    native_origins = {}
    if prepared is not None:
        for op in prepared.operations:
            for origin in op["origins"]:
                oid = f"w{int(origin['worker_slot'].split('-')[1]):02}::{origin['proposal_id']}"
                require(
                    oid not in native_origins and oid in universe,
                    "native origin outside/duplicated in universe",
                )
                require(
                    origin["head_sha"] == universe[oid]["published_head"],
                    "native origin head differs",
                )
                require(
                    origin["case_hashes"] == universe[oid].get("case_hashes"),
                    "native source-case hashes differ",
                )
                _verify_native_origin(origin, universe[oid], bindings[oid], prepared)
                native_origins[oid] = op["operation_id"]
    seen_apply = set()
    graph = {}
    used_ops = set()
    base = {"origin_id", "status", "evidence_refs"}
    for oid, row in resolved.items():
        status = row.get("status")
        extra_keys = {
            "pending": {"missing_requirement"},
            "deferred": {"missing_requirement"},
            "retired": {"successor_origin_ids", "retirement_reason", "retirement_bridge"},
            "already_satisfied": {"satisfied_owner", "independent_review_refs"},
            "apply": {"operation_id", "payload_sha256", "independent_review_refs"},
        }
        require(status in extra_keys, "invalid resolution status")
        closed(row, base | extra_keys[status], "resolution row")
        evidence = proof.refs(row["evidence_refs"])
        if status in {"pending", "deferred"}:
            text(row["missing_requirement"])
        elif status == "already_satisfied":
            proof.native.owner_path(row["satisfied_owner"]["path"])
            proof.ref(row["satisfied_owner"])
            proof.refs(row["independent_review_refs"])
        elif status == "retired":
            targets = row["successor_origin_ids"]
            require(
                isinstance(targets, list) and len(targets) == len(set(targets)),
                "duplicate retirement successors",
            )
            require(
                all(t in universe and t != oid for t in targets),
                "unknown/self retirement successor",
            )
            reason = text(row["retirement_reason"])
            bridge = closed(
                row["retirement_bridge"], {"capture", "published_head"}, "retirement bridge"
            )
            permitted_heads = {universe[t]["published_head"] for t in targets} or {
                universe[oid]["published_head"]
            }
            require(
                bridge["published_head"] in permitted_heads,
                "retirement bridge head is not a selected successor",
            )
            statement = read_json(proof.published(bridge["capture"], bridge["published_head"]))
            expected = {
                "schema_version": 1,
                "kind": "source_origin_retirement",
                "origin_id": oid,
                "origin_proposal_sha256": universe[oid]["proposal_object_sha256"],
                "successors": {t: universe[t]["proposal_object_sha256"] for t in targets},
                "reason": reason,
            }
            require(statement == expected, "published retirement claim differs")
            require(
                (bridge["capture"]["path"], bridge["capture"]["sha256"]) in evidence,
                "retirement bridge absent from evidence",
            )
            graph[oid] = targets
        elif status == "apply":
            opid = text(row["operation_id"])
            final_hash = hash_value(row["payload_sha256"])
            reviews = proof.refs(row["independent_review_refs"])
            require(prepared is not None, "apply has no verified native plan")
            require(
                native_origins.get(oid) == opid and opid in operations,
                "origin/operation differs from native plan",
            )
            require(digest(prepared.payloads[opid]) == final_hash, "operation payload differs")
            native_bindings = {b["binding_id"]: b for b in prepared.plan["bindings"]}
            native_evidence = {
                (b["path"], b["sha256"])
                for b in native_bindings.values()
                if b["role"]
                in {
                    "evidence",
                    "reconciliation",
                    "review",
                    "proposal",
                    "decision",
                    "case_ledger",
                    "shard",
                }
            }
            accepted_reviews = {
                (native_bindings[b]["path"], native_bindings[b]["sha256"])
                for b in prepared.acceptance["review_bindings"]
            }
            require(evidence <= native_evidence, "apply evidence outside verified native bindings")
            require(
                reviews == accepted_reviews,
                "apply review differs from native accepted review bindings",
            )
            seen_apply.add(oid)
            used_ops.add(opid)
    require(seen_apply == set(native_origins), "native plan origin is not applied exactly once")
    require(used_ops == set(operations), "native operation missing from crosswalk")
    visited, active = set(), set()

    def visit(oid):
        require(oid not in active, "retirement cycle")
        if oid in visited:
            return
        active.add(oid)
        for target in graph.get(oid, []):
            visit(target)
        active.remove(oid)
        visited.add(oid)

    for oid in universe:
        visit(oid)
    proof.recheck()
    if prepared is not None:
        native._recheck(prepared)
    proof.recheck()
    return {
        "structurally_complete": True,
        "scientific_approval": False,
        "application_authorized": False,
        "origin_count": len(initial),
        "additional_successor_count": len(extra),
        "applied_origin_count": len(seen_apply),
        "native_operation_count": len(used_ops),
        "native_prepare_proof": native_ref,
        "evidence_sha256": {p: digest(f.content) for p, f in sorted(proof.files.items())},
        "local_head": proof.start_head,
    }
