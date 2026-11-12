"""Apply an exact reviewed correction after adoption in a distinct real root (#1373).

The original adoption remains immutable and is verified by its own captured code.
A source correction preserves publication beforeimages and adds no release approval.
"""

from __future__ import annotations

import argparse
import builtins
import copy
import os
import time
import types
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mediaingredientmech.curate.adoption_filesystem import _new_owner, _retire
from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import (
    FrozenFile,
    check_reserved,
    finish_receipt,
    no_alias,
    publish_validated,
)
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    build_record_index,
    parse_registry,
    validate_records,
)
from mediaingredientmech.validation.write_validated import validate_ingredient

CAPABILITY = "reviewed-curation-successor-v1"
REPOSITORY = "CultureBotAI/MediaIngredientMech"
MARKER = "data/curation_successor.json"
PUBLICATION = (
    "mappings/ingredient_mappings.sssom.tsv",
    "mappings/suppressed_aliases.tsv",
    "mappings/stable_sssom_generation.json",
    "mappings/stable_sssom_publication.json",
)
LEDGERS = (str(REGISTRY_PATH), str(LIFECYCLE_PATH))
DESCRIPTION = "Exact reviewed source correction; permanent identity and residual holds retained"
# This finite v1 does not change composition, roles, identity scope or source occurrences.
EDITABLE = {
    "identifier",
    "mapping_status",
    "ontology_mapping",
    "chemical_properties",
    "kg_microbe_node_id",
    "legacy_identifiers",
    "synonyms",
    "notes",
    "curation_history",
}
_CAPTURE: Any = globals().get("_PRODUCER_CAPTURE")


def native():
    """Use captured native primitives; never use these to verify another producer."""
    return _CAPTURE.load("mediaingredientmech.curate.stable_id_adoption")


def require(value, message):
    if not value:
        raise ValueError("Curation successor: " + message)


def _ref(root, path, content=None):
    path = Path(path).absolute()
    name = path.relative_to(root).as_posix()
    native().relative(name)
    return {
        "path": name,
        "sha256": native().sha(FrozenFile.capture(path).content if content is None else content),
    }


def _path(root, value):
    path = Path(value)
    if not path.is_absolute():
        path = root / native().relative(str(path))
    require(".." not in path.parts and path.is_relative_to(root), "path escapes selected root")
    no_alias(path)
    return path


def _identity(root):
    api = native()
    top = Path(api.git(root, "rev-parse", "--show-toplevel").decode().strip())
    require(os.path.samefile(root, top), "selected root is not a Git checkout root")
    origin = api.git(root, "remote", "get-url", "origin").decode().strip()
    require(
        origin
        in {
            "https://github.com/CultureBotAI/MediaIngredientMech.git",
            "git@github.com:CultureBotAI/MediaIngredientMech.git",
        },
        "unexpected repository origin",
    )
    return {
        "root": str(root),
        "repository": REPOSITORY,
        "origin": origin,
        "head": api.git(root, "rev-parse", "HEAD").decode().strip(),
        "index_sha256": api.sha(api.git(root, "ls-files", "--stage", "-z")),
    }


def _disjoint(left, right):
    """Refuse spelling and physical ancestor aliases, including Unicode aliases."""
    no_alias(left)
    no_alias(right)
    require(not left.is_relative_to(right) and not right.is_relative_to(left), "roots overlap")
    require(
        not any(os.path.samefile(left, p) for p in (right, *right.parents))
        and not any(os.path.samefile(right, p) for p in (left, *left.parents)),
        "physical roots overlap",
    )


def _optional(root, names):
    return {
        name: FrozenFile.capture(root / name) if os.path.lexists(root / name) else None
        for name in names
    }


def _optional_hashes(files):
    return {name: native().sha(f.content) if f else None for name, f in files.items()}


def _optional_check(root, files):
    for name, frozen in files.items():
        if frozen is None:
            require(not os.path.lexists(root / name), "absent maintained input appeared: " + name)
        else:
            frozen.verify()


def _parents(root, names):
    """Retain existing ancestors even when every selected file is absent."""
    result = {}
    for name in names:
        parent = (root / name).parent
        while parent.is_relative_to(root):
            if os.path.lexists(parent):
                no_alias(parent)
                require(parent.is_dir(), "maintained ancestor is not a directory")
                result[parent] = (parent.stat().st_dev, parent.stat().st_ino)
            parent = parent.parent
    return result


def _check_parents(parents):
    for path, identity in parents.items():
        no_alias(path)
        require(
            path.is_dir() and (path.stat().st_dev, path.stat().st_ino) == identity,
            "maintained ancestor changed",
        )


class Predecessor:
    """Actual unchanged adoption, executed only through its pinned native loader."""

    def __init__(self, target, reference):
        api = native()
        api.keys(
            reference,
            {
                "kind",
                "identity",
                "stage",
                "manifest",
                "receipt",
                "producer",
                "publication_beforeimages",
                "publication_proof",
                "historical_reviews",
            },
        )
        require(reference["kind"] == "adoption", "exactly one adoption predecessor required")
        api.keys(reference["identity"], {"root", "repository", "origin", "head", "index_sha256"})
        self.root = api.root_path(reference["identity"]["root"], "predecessor")
        _disjoint(target, self.root)
        require(_identity(self.root) == reference["identity"], "predecessor Git identity changed")
        require(not os.path.lexists(self.root / MARKER), "branching or cyclic predecessor lineage")
        self.reference = copy.deepcopy(reference)
        self.files = api.Inputs(self.root)
        self.manifest = self.files.ref(reference["manifest"])
        self.receipt = self.files.ref(reference["receipt"])
        self.stage = _path(self.root, reference["stage"])
        require(
            reference["manifest"]["path"]
            == str((self.stage / "manifest.json").relative_to(self.root))
            and self.receipt["manifest"] == reference["manifest"],
            "predecessor stage/receipt mismatch",
        )
        require(
            self.manifest["producer"] == reference["producer"],
            "predecessor producer reference differs",
        )
        # The original loader and every executable byte must be part of the original receipt.
        name = "src/mediaingredientmech/curate/adoption_producer.py"
        raw = self.files.read(name, reference["producer"]["files"][name])
        loader = types.ModuleType("_curation_original_adoption_" + uuid.uuid4().hex)
        loader.__file__ = str(self.root / name)
        loader.__dict__["__builtins__"] = vars(builtins)
        exec(compile(raw, loader.__file__, "exec"), loader.__dict__)
        self.capture, self.api = loader.load(self.root, raw)
        require(
            {k: api.sha(v[0]) for k, v in self.capture.files.items()}
            == reference["producer"]["files"],
            "original producer closure differs",
        )
        self.verify_native()
        before = {
            name: FrozenFile.capture(self.root / api.relative(ref["path"]))
            for name, ref in self.receipt["beforeimages"].items()
        }
        self.loaded, checked, held, staged, _ = self.api._prepared(
            self.root, self.stage, before=before
        )
        require(checked == self.manifest, "predecessor manifest changed during capture")
        self.api._acceptance(self.loaded, held, self.receipt["acceptance"]["path"])
        self.held = [
            held,
            *before.values(),
            *staged.values(),
            FrozenFile.capture(self.root / self.receipt["operational_fit"]["path"]),
        ]
        self.held.extend(
            FrozenFile.capture(self.root / api.relative(ref["path"]))
            for ref in self.receipt["retired_sources"].values()
        )
        self.owners = self.api.inventory(self.root)
        self.maintained = {
            **self.owners,
            **{name: FrozenFile.capture(self.root / name) for name in (*api.AGGREGATES, *LEDGERS)},
        }
        self.publication = _optional(self.root, PUBLICATION)
        self.publication_parents = _parents(self.root, PUBLICATION)
        require(
            _optional_hashes(self.publication) == reference["publication_beforeimages"],
            "all four publication beforeimages/absences required",
        )
        self.history = []
        require(
            isinstance(reference["historical_reviews"], list)
            and len(reference["historical_reviews"]) >= 2,
            "qualified historical review obligations required",
        )
        seen = set()
        for spec in reference["historical_reviews"]:
            api.keys(spec, {"identity", "review", "markdown_sha256"})
            history_root = api.root_path(spec["identity"]["root"], "historical")
            _disjoint(target, history_root)
            _disjoint(self.root, history_root)
            require(_identity(history_root) == spec["identity"], "historical Git identity changed")
            name = spec["review"]["path"]
            require((str(history_root), name) not in seen, "duplicate historical review")
            seen.add((str(history_root), name))
            inputs = api.Inputs(history_root)
            raw = inputs.read(name, spec["review"]["sha256"])
            markdown = inputs.read(str(Path(name).with_name("review.md")), spec["markdown_sha256"])
            rr = _CAPTURE.script("scripts/record_review.py")
            report = rr.parse_review_bundle(
                name, raw, markdown, target / "schema/record_review.yaml"
            )
            require(
                report["repository"] == REPOSITORY
                and report["completion"] == "completed"
                and rr.source_provenance(history_root, report)["status"]
                not in {"invalid", "unverified"},
                "invalid original historical review",
            )
            for entry in report["source"]["inputs"]:
                inputs.read(entry["path"], entry["sha256"])
            self.history.append((spec, inputs, report))
        self.prior_publication = None
        # A native historical publication has its own authenticated beforeimages;
        # its reviews must never be reinterpreted against installed table bytes.
        if self.publication[PUBLICATION[3]]:
            proof = reference["publication_proof"]
            require(isinstance(proof, dict), "native prior-publication proof required")
            api.keys(proof, {"stage", "manifest", "receipt", "producer"})
            pub_manifest = self.files.ref(proof["manifest"])
            pub_receipt = self.files.ref(proof["receipt"])
            require(
                pub_manifest["producer"] == proof["producer"]
                and pub_receipt["manifest"] == proof["manifest"],
                "prior publication proof mismatch",
            )
            pub_stage = _path(self.root, proof["stage"])
            require(
                proof["manifest"]["path"]
                == str((pub_stage / "manifest.json").relative_to(self.root)),
                "prior publication stage mismatch",
            )
            loader_name = "src/mediaingredientmech/curate/stable_publication_producer.py"
            raw = self.files.read(loader_name, proof["producer"]["files"][loader_name])
            loader = types.ModuleType("_original_publication_" + uuid.uuid4().hex)
            loader.__file__ = str(self.root / loader_name)
            loader.__dict__["__builtins__"] = vars(builtins)
            exec(compile(raw, loader.__file__, "exec"), loader.__dict__)
            capture, pub = loader.load(self.root, raw)
            require(
                {n: api.sha(v[0]) for n, v in capture.files.items()} == proof["producer"]["files"],
                "prior publication producer differs",
            )
            require(
                pub.verify_completed(self.root, pub_stage, self.root / proof["receipt"]["path"])[
                    "status"
                ]
                == "COMPLETE_CURRENT_CANONICAL_CANDIDATE",
                "prior publication did not verify",
            )
            archives = {
                n: FrozenFile.capture(self.root / api.relative(r["path"])) if r else None
                for n, r in pub_receipt["beforeimages"].items()
            }
            publication, _, held, staged, _ = pub._prepared(
                self.root, pub_stage, before=archives, historical=True
            )
            pub._acceptance(publication, held, pub_receipt["acceptance"]["path"])
            self.held.extend([held, *staged.values(), *[f for f in archives.values() if f]])
            self.prior_publication = publication
            previous = api.document(self.publication[PUBLICATION[3]].content)
            while previous is not None:
                require(
                    previous.get("capability") == "reviewed-stable-sssom-publication-v1",
                    "unsupported prior publication provenance",
                )
                prior = previous["selection"]["context"]["historical_reviews"]
                require(
                    all(
                        any(
                            x[0]["review"] == ref["review"]
                            and x[0]["identity"]["root"] == ref["root"]
                            and x[0]["identity"]["head"] == ref["head"]
                            and x[0]["markdown_sha256"] == ref["markdown_sha256"]
                            for x in self.history
                        )
                        for ref in prior
                    ),
                    "prior historical review obligation omitted",
                )
                require(
                    all(
                        any(x[0]["review"] == ref for x in self.history)
                        for ref in previous["reviews"]
                    ),
                    "prior publication scientific pair must remain in qualified frozen history",
                )
                previous = previous["historical_publication"]
        else:
            require(reference["publication_proof"] is None, "unexpected prior publication proof")
        self.check()

    def verify_native(self):
        result = self.api.verify_completed(
            self.root, self.stage, self.root / self.reference["receipt"]["path"]
        )
        require(
            result["status"] == "COMPLETE_CURRENT_CANDIDATE",
            "strict original adoption did not verify",
        )
        return result

    def check(self):
        require(
            _identity(self.root) == self.reference["identity"], "predecessor Git context changed"
        )
        self.capture.verify()
        self.files.verify()
        self.loaded.check()
        require(
            native().hashes(self.api.inventory(self.root)) == native().hashes(self.owners),
            "predecessor owner membership changed",
        )
        for frozen in (*self.maintained.values(), *self.held):
            frozen.verify()
        _optional_check(self.root, self.publication)
        _check_parents(self.publication_parents)
        if self.prior_publication is not None:
            self.prior_publication.check()
        for spec, inputs, _ in self.history:
            require(_identity(inputs.root) == spec["identity"], "historical root changed")
            inputs.verify()

    def closure(self):
        groups = {}
        for root, files in [
            (self.root, self.files.files),
            (self.loaded.inputs.root, self.loaded.inputs.files),
            (self.loaded.legacy.root, self.loaded.legacy.files),
            (self.root, self.maintained),
            *[(i.root, i.files) for _, i, _ in self.history],
        ]:
            group = groups.setdefault(str(root), {})
            for f in files.values():
                # Original recovery files are qualified by their actual path, not relabeled current.
                key = str(f.path.relative_to(root))
                pin = native().sha(f.content)
                require(
                    key not in group or group[key] == pin, "conflicting qualified predecessor input"
                )
                group[key] = pin
        for f in self.held:
            groups.setdefault(str(self.root), {})[
                str(f.path.relative_to(self.root))
            ] = native().sha(f.content)
        for name, f in self.publication.items():
            groups.setdefault(str(self.root), {})[name] = native().sha(f.content) if f else None
        for name, frozen in self.loaded.claw.files.items():
            groups.setdefault(str(self.loaded.claw.root), {})[name] = native().sha(frozen.content)
        if self.prior_publication is not None:
            p = self.prior_publication
            for frozen in (
                *p.inputs.files.values(),
                *p.sources.values(),
                *p.history_files,
                *p.adoption_files,
            ):
                groups.setdefault("absolute_prior_publication_evidence", {})[
                    str(frozen.path)
                ] = native().sha(frozen.content)
        return groups


def _delta(before, after):
    return {
        name: {
            "before_present": name in before,
            "before": before.get(name),
            "after_present": name in after,
            "after": after.get(name),
        }
        for name in sorted(set(before) | set(after))
        if (name in before) != (name in after) or before.get(name) != after.get(name)
    }


def _validate_change(loaded, operation, before, after):
    api = native()
    require(
        before.get("mim_id") == after.get("mim_id") == operation["mim_id"],
        "permanent identity changed",
    )
    delta = _delta(before, after)
    require(
        delta and set(delta) <= EDITABLE and set(delta) != {"curation_history"},
        "unsupported or no-op source change",
    )
    require(operation["delta"] == delta, "declared complete field delta differs")
    old_history = before.get("curation_history") or []
    history = after.get("curation_history") or []
    require(
        len(history) == len(old_history) + 1 and history[:-1] == old_history,
        "curation history must preserve exact prefix",
    )
    event = history[-1]
    event_time = datetime.fromisoformat(event["timestamp"])
    require(
        event_time.utcoffset() is not None
        and event_time.utcoffset().total_seconds() == 0
        and event_time <= datetime.fromisoformat(loaded.request["timestamp"])
        and event.get("curator")
        and event.get("llm_assisted") is True
        and event.get("llm_model")
        and event.get("changes"),
        "genuine attributed curation event required",
    )
    reconstructed = {"curation_history": copy.deepcopy(old_history)}
    record_curation_event(reconstructed, **event)
    require(
        reconstructed["curation_history"] == history, "event differs from native curation helper"
    )
    require(
        event.get("previous_status") == before.get("mapping_status")
        and event.get("new_status") == after.get("mapping_status"),
        "event status transition differs",
    )
    require(
        operation["issues"]
        and all(
            isinstance(x, str)
            and x.startswith("https://github.com/CultureBotAI/MediaIngredientMech/issues/")
            for x in operation["issues"]
        ),
        "issue-bound correction required",
    )
    require(
        operation["residual_holds"] == operation["inherited_holds"],
        "hold retirement is outside successor v1",
    )
    old_aliases, new_aliases = set(before.get("legacy_identifiers", [])), set(
        after.get("legacy_identifiers", [])
    )
    rejected = operation["rejected_identifiers"]
    require(
        set(rejected) == old_aliases - new_aliases,
        "every removed resolving alias needs explicit reviewed rejection",
    )
    require(
        not (set(rejected) & ({after.get("identifier")} | new_aliases)),
        "disproved identifier remains resolving",
    )
    require(
        all(
            alias == after.get("identifier") and alias.startswith("UNMAPPED_")
            for alias in new_aliases - old_aliases
        ),
        "only the reviewed restored placeholder may be added as an alias",
    )
    require(
        all(
            alias not in api.encoded(after.get("ontology_mapping", {})).decode()
            for alias in rejected
        ),
        "rejected identifier remains in active ontology mapping",
    )
    # Raw tokens remain present; false labels are explicitly non-searchable native evidence.
    old_synonyms = before.get("synonyms", [])
    new_synonyms = after.get("synonyms", [])

    def token(item):
        return item if isinstance(item, str) else item.get("synonym_text")

    require(
        {token(x) for x in old_synonyms} <= {token(x) for x in new_synonyms},
        "raw synonym token lost",
    )
    for text in operation["rejected_labels"]:
        require(
            any(
                isinstance(x, dict)
                and token(x) == text
                and x.get("synonym_type") == "REJECTED_LABEL"
                for x in new_synonyms
            ),
            "false label must retain native REJECTED_LABEL status",
        )
    oldpath, newpath = Path(operation["before"]["path"]), Path(operation["after_path"])
    require(
        oldpath.name == newpath.name
        and newpath.parent.as_posix()
        == "data/ingredients/"
        + ("mapped" if after.get("mapping_status") == "MAPPED" else "unmapped"),
        "unsupported filename/category change",
    )
    require(
        not validate_ingredient(after, schema_path=loaded.root / api.SCHEMA),
        "invalid proposed record",
    )
    return delta


class Loaded:
    """Full immutable predecessor and exact current target closure for one request."""

    def __init__(self, root, request_path, *, before=None, after_inventory=None, publication=None):
        api = native()
        self.root = api.root_path(root, "successor")
        self.inputs = api.Inputs(
            self.root,
            {
                n: f
                for n, f in (before or {}).items()
                if n.startswith("data/ingredients/") or n in (*api.AGGREGATES, *LEDGERS)
            },
        )
        self.request_path = str(_path(self.root, request_path).relative_to(self.root))
        self.request = api.document(self.inputs.read(self.request_path))
        req = self.request
        api.keys(
            req,
            {
                "schema_version",
                "capability",
                "identity",
                "predecessor",
                "timestamp",
                "curator",
                "claw_root",
                "operational_policy",
                "target_inventory",
                "target_inputs",
                "source_context",
                "operations",
                "context",
                "payloads",
                "review_inputs",
            },
        )
        require(
            req["schema_version"] == 1 and req["capability"] == CAPABILITY,
            "unsupported successor contract",
        )
        self.current_identity = _identity(self.root)
        self.identity = copy.deepcopy(req["identity"])
        api.keys(self.identity, {"root", "repository", "origin", "head", "index_sha256"})
        if before is None:
            require(self.current_identity == self.identity, "target repository/HEAD/index differs")
        else:
            require(
                all(
                    self.current_identity[k] == self.identity[k]
                    for k in ("root", "repository", "origin")
                ),
                "completed target repository/root differs",
            )
            api.git(
                self.root,
                "merge-base",
                "--is-ancestor",
                self.identity["head"],
                self.current_identity["head"],
            )
        self.head = self.identity["head"]
        self.index = api.git(self.root, "ls-files", "--stage", "-z")
        stamp = datetime.fromisoformat(req["timestamp"])
        require(
            stamp.utcoffset() is not None
            and stamp.utcoffset().total_seconds() == 0
            and req["curator"],
            "explicit UTC timestamp and curator required",
        )
        _CAPTURE.bind(self.inputs)
        self.predecessor = Predecessor(self.root, req["predecessor"])
        self.owners = {
            name: f
            for name, f in (before or api.inventory(self.root)).items()
            if f is not None and name.startswith("data/ingredients/")
        }
        require(
            api.hashes(self.owners)
            == req["target_inventory"]
            == api.hashes(self.predecessor.owners),
            "complete starting owner inventory differs",
        )
        for name, frozen in self.owners.items():
            self.inputs.read(name, api.sha(frozen.content))
        for name, expected in req["target_inputs"].items():
            self.inputs.read(name, expected)
        require(
            {*api.AGGREGATES, *LEDGERS} <= set(req["target_inputs"]),
            "complete aggregate/ledger baseline required",
        )
        for name in (*api.AGGREGATES, *LEDGERS):
            require(
                self.inputs.read(name) == self.predecessor.maintained[name].content,
                "starting aggregate/ledger differs",
            )
        # #1379: archived ledgers prove the original transition, not the current
        # endpoint. Both live ledgers must independently remain byte-identical.
        self.live_ledgers = {name: FrozenFile.capture(self.root / name) for name in LEDGERS}
        require(
            all(f.content == self.inputs.read(name) for name, f in self.live_ledgers.items()),
            "live immutable ID ledger differs",
        )
        self.publication = _optional(self.root, PUBLICATION) if publication is None else publication
        require(set(self.publication) == set(PUBLICATION), "incomplete publication beforeimage set")
        self.publication_parents = _parents(self.root, PUBLICATION)
        self.publication_transaction = publication is not None
        require(
            _optional_hashes(self.publication) == req["predecessor"]["publication_beforeimages"],
            "starting publication history differs",
        )
        self.marker = (before or {}).get(MARKER)
        require(self.marker is None, "unexpected old lineage marker")
        if after_inventory is None:
            require(not os.path.lexists(self.root / MARKER), "occupied successor marker")
        self.after_inventory = after_inventory
        self.source_context = self.inputs.ref(req["source_context"])
        require(
            self.source_context == self.predecessor.loaded.context,
            "original source/origin/hold context changed",
        )
        self.claw = api.Claw(req["claw_root"])
        self.policy = api._policy(self.inputs.ref(req["operational_policy"]))
        self.initial_dirty = set(
            api.git(self.root, "diff", "--name-only", "--no-renames", "-z", self.head)
            .decode()
            .split("\0")
        ) - {""}
        records = {name: api.load_yaml(f.content) for name, f in self.owners.items()}
        validate_records(
            parse_registry(self.inputs.read(LEDGERS[0]), self.inputs.read(LEDGERS[1])), records
        )
        self.records = copy.deepcopy(records)
        index = build_record_index(records)
        self.payloads, self.moves, self.operations = [], {}, {}
        for op in req["operations"]:
            api.keys(
                op,
                {
                    "mim_id",
                    "before",
                    "after_path",
                    "proposal",
                    "delta",
                    "issues",
                    "evidence",
                    "inherited_holds",
                    "residual_holds",
                    "rejected_identifiers",
                    "rejected_labels",
                    "primary",
                    "skeptic",
                },
            )
            require(op["mim_id"] not in self.operations, "duplicate selected owner")
            name = op["before"]["path"]
            require(
                name in self.owners
                and api.sha(self.owners[name].content) == op["before"]["sha256"],
                "selected beforeimage differs",
            )
            after = api.load_yaml(
                self.inputs.read(op["proposal"]["path"], op["proposal"]["sha256"])
            )
            require(op["evidence"], "correction evidence required")
            for ref in op["evidence"]:
                self.inputs.read(ref["path"], ref["sha256"])
            delta = _validate_change(self, op, records[name], after)
            if after.get("identifier") != records[name].get("identifier"):
                aliases = index.aliases.get(after.get("identifier"), ())
                primary_owners = [
                    n for n, r in records.items() if r.get("identifier") == after.get("identifier")
                ]
                require(
                    all(n == name for n in primary_owners),
                    "replacement primary identifier belongs to another owner",
                )
                require(
                    not aliases or all(x == name for x in aliases),
                    "replacement identifier resolves to another owner",
                )
            new = op["after_path"]
            api.relative(new)
            require(
                new == name
                or (
                    new not in self.records
                    and not os.path.lexists(self.root / new)
                    and after_inventory is None
                )
                or (after_inventory is not None and new in after_inventory),
                "new owner path occupied",
            )
            del self.records[name]
            self.records[new] = after
            if name != new:
                self.moves[name] = new
            self.operations[op["mim_id"]] = op
            self.payloads.append(
                {
                    "mim_id": op["mim_id"],
                    "before_path": name,
                    "after_path": new,
                    "before": records[name],
                    "after": after,
                    "delta": delta,
                    "issues": op["issues"],
                    "evidence": op["evidence"],
                    "inherited_holds": op["inherited_holds"],
                    "residual_holds": op["residual_holds"],
                    "rejected_identifiers": op["rejected_identifiers"],
                    "rejected_labels": op["rejected_labels"],
                    "predecessor": req["predecessor"],
                    "source_context_sha256": req["source_context"]["sha256"],
                }
            )
        require(self.operations, "empty successor scope")
        validate_records(
            parse_registry(self.inputs.read(LEDGERS[0]), self.inputs.read(LEDGERS[1])), self.records
        )
        require(
            {r["mim_id"] for r in self.records.values()} == {r["mim_id"] for r in records.values()},
            "permanent ID set changed",
        )
        self.context = {
            "capability": CAPABILITY,
            "root": str(self.root),
            "identity": self.identity,
            "predecessor": req["predecessor"],
            "complete_before_inventory": req["target_inventory"],
            "source_context": self.source_context,
            "historical_obligations": [report for _, _, report in self.predecessor.history],
            "operations": list(self.operations),
            "publication_beforeimages": _optional_hashes(self.publication),
        }
        self.check()

    def check(self, states=None, during=()):
        api = native()
        _CAPTURE.verify()
        self.claw.verify()
        self.predecessor.check()
        require(_identity(self.root) == self.current_identity, "successor Git context changed")
        for frozen in self.live_ledgers.values():
            frozen.verify()
        if not self.publication_transaction:
            _optional_check(self.root, self.publication)
        else:
            for frozen in self.publication.values():
                if frozen is not None:
                    frozen.verify()
        _check_parents(self.publication_parents)
        mutable = {*self.owners, *api.AGGREGATES, MARKER, *self.moves.values()}
        if states is None and self.after_inventory is None:
            self.inputs.verify()
            require(
                api.hashes(api.inventory(self.root)) == api.hashes(self.owners),
                "target owner inventory changed",
            )
            require(not os.path.lexists(self.root / MARKER), "successor marker appeared")
        elif states is None:
            self.inputs.verify(mutable)
            require(
                api.hashes(api.inventory(self.root)) == self.after_inventory,
                "current successor endpoint differs",
            )
        else:
            self.inputs.verify(mutable)
            for name, frozen in states.items():
                if name not in during:
                    if frozen is None:
                        require(not os.path.lexists(self.root / name), "absent output appeared")
                    else:
                        frozen.verify()
            expected = {
                name
                for name, f in states.items()
                if f is not None and name.startswith("data/ingredients/")
            }
            require(
                set(api.inventory(self.root, during=during)) - set(during)
                == expected - set(during),
                "intermediate owner membership changed",
            )
        dirty = set(
            api.git(self.root, "diff", "--name-only", "--no-renames", "-z", self.head)
            .decode()
            .split("\0")
        ) - {""}
        require(dirty <= self.initial_dirty | mutable, "unrelated tracked mutation")


def inspect(root, request_path):
    """Return actual complete correction payloads, never a scientific decision."""
    api = native()
    loaded = Loaded(root, request_path)
    targets = [
        {
            "target_id": p["mim_id"],
            "kind": "snapshot_row",
            "path": None,
            "selector": p["mim_id"],
            "semantic_digest": {
                "algorithm": "sha256-canonical-json-v1",
                "sha256": api.digest(p),
                "description": DESCRIPTION,
            },
        }
        for p in loaded.payloads
    ]
    loaded.check()
    return {
        "context": loaded.context,
        "payloads": loaded.payloads,
        "targets": targets,
        "scientific_approval_added": False,
    }


def _review(loaded, reference, *, scientific):
    api = native()
    api.keys(reference, {"path", "sha256", "markdown_sha256", "target_id", "assessment_id"})
    path = reference["path"]
    raw = loaded.inputs.read(path, reference["sha256"])
    md = loaded.inputs.read(str(Path(path).with_name("review.md")), reference["markdown_sha256"])
    rr = _CAPTURE.script("scripts/record_review.py")
    report = rr.parse_review_bundle(path, raw, md, loaded.root / "schema/record_review.yaml")
    require(
        rr.source_provenance(loaded.root, report)["status"] not in {"invalid", "unverified"},
        "invalid native review provenance",
    )
    require(
        report["repository"] == REPOSITORY
        and report["completion"] == "completed"
        and report["scientific_review"] is scientific
        and report["verdict"] in {"pass", "pass_with_limitations"},
        "completed applicable native review required",
    )
    source = {x["path"]: x["sha256"] for x in report["source"]["inputs"]}
    require(len(source) == len(report["source"]["inputs"]), "duplicate review source input")
    for name, expected in source.items():
        loaded.inputs.read(name, expected)
    require(
        report["source"]["state"] != "working_tree"
        or report["source"]["git_revision"] == loaded.head,
        "review working-tree HEAD differs",
    )
    tid = reference["target_id"]
    targets = [x for x in report["targets"] if x["target_id"] == tid]
    assessments = [
        x for x in report["assessments"] if x["assessment_id"] == reference["assessment_id"]
    ]
    require(
        len(targets) == len(assessments) == 1 and tid in report["scope"]["reviewed_target_ids"],
        "review target/assessment outside actual scope",
    )
    checks = [x for x in report["checks"] if x["required"] and tid in x["target_ids"]]
    require(
        checks and all(x["status"] == "passed" for x in checks),
        "required corrective check did not pass",
    )
    assessment = assessments[0]
    require(
        assessment["target_ids"] == [tid] and assessment["outcome"] == "supported",
        "explicit supported exact-target assessment required",
    )
    dimensions = {x["name"]: x["value"] for x in assessment.get("dimensions", [])}
    require(len(dimensions) == len(assessment.get("dimensions", [])), "duplicate review dimensions")
    return report, targets[0], assessment, dimensions, source


def _admitted(loaded):
    api = native()
    req = loaded.request
    require(
        loaded.inputs.ref(req["context"]) == loaded.context
        and loaded.inputs.ref(req["payloads"]) == loaded.payloads,
        "actual inspected context/payloads required",
    )
    for name, expected in req["review_inputs"].items():
        loaded.inputs.read(name, expected)
    loaded.scientists = set()
    for payload in loaded.payloads:
        op = loaded.operations[payload["mim_id"]]
        reports = []
        for role in ("primary", "skeptic"):
            ref = op[role]
            require(isinstance(ref, dict), "unassessed correction cannot prepare")
            for path, expected in (
                (ref["path"], ref["sha256"]),
                (str(Path(ref["path"]).with_name("review.md")), ref["markdown_sha256"]),
            ):
                require(
                    req["review_inputs"].get(path) == expected,
                    "native review pair missing from exact review inputs",
                )
            report, target, assessment, dimensions, source = _review(loaded, ref, scientific=True)
            required = {
                req[key]["path"]: req[key]["sha256"]
                for key in ("context", "payloads", "source_context", "operational_policy")
            }
            required.update(
                {
                    op["before"]["path"]: op["before"]["sha256"],
                    op["proposal"]["path"]: op["proposal"]["sha256"],
                    "MAPPING_SEMANTICS.md": api.sha(loaded.inputs.read("MAPPING_SEMANTICS.md")),
                }
            )
            required.update({x["path"]: x["sha256"] for x in op["evidence"]})
            require(
                all(source.get(k) == v for k, v in required.items()),
                "scientific review omits current proposal/before/context/evidence",
            )
            require(
                target.get("kind") == "snapshot_row"
                and target.get("path") == req["payloads"]["path"]
                and target.get("selector") == op["mim_id"]
                and target.get("semantic_digest")
                == {
                    "algorithm": "sha256-canonical-json-v1",
                    "sha256": api.digest(payload),
                    "description": DESCRIPTION,
                }
                and target.get("owner_paths")
                == [
                    {
                        "repository": REPOSITORY,
                        "path": req["payloads"]["path"],
                        "role": "proposed source correction",
                    }
                ],
                "scientific target differs from actual full delta",
            )
            require(
                dimensions.get("curation_action") == "apply_exact_source_delta"
                and dimensions.get("delta_sha256") == api.digest(op["delta"])
                and dimensions.get("permanent_mim_id") == op["mim_id"]
                and dimensions.get("residual_holds_json")
                == api.encoded(op["residual_holds"]).decode().strip()
                and dimensions.get("rejected_identifiers_json")
                == api.encoded(op["rejected_identifiers"]).decode().strip(),
                "explicit exact corrective scope/identity/holds required",
            )
            retained = {
                x["issue_key"]
                for x in op["residual_holds"]
                if isinstance(x, dict) and "issue_key" in x
            }
            active = [
                x
                for x in report["findings"]
                if ref["target_id"] in x["target_ids"] and x["status"] in {"open", "deferred"}
            ]
            require(
                all(x["issue_key"] in retained and x.get("disposition_reason") for x in active)
                and dimensions.get("corrective_delta_findings") == "none"
                and dimensions.get("residual_findings_json")
                == api.encoded(active).decode().strip(),
                "unresolved corrective finding; residual findings must be explicit and retained",
            )
            evidence = {x["evidence_id"]: x for x in report["evidence"]}
            require(
                any(
                    evidence[e]["kind"] in {"primary_source", "database", "authority"}
                    and evidence[e]["support"] == "supports"
                    and evidence[e]["reference"] in source
                    and evidence[e].get("snapshot_sha256") == source[evidence[e]["reference"]]
                    for e in assessment["evidence_ids"]
                ),
                "captured primary corrective evidence required",
            )
            reports.append(report)
            loaded.scientists.add(report["reviewer"]["identity"])
        require(
            op["primary"]["path"] != op["skeptic"]["path"]
            and reports[0]["reviewer"]["identity"] != reports[1]["reviewer"]["identity"]
            and reports[1]["reviewer"].get("independence") == "independent"
            and reports[1]["reviewer"].get("independence_basis"),
            "separate independent skeptical correction review required",
        )


def _outputs(loaded):
    """Derive exact finite record writes and full native-shaped aggregates."""
    api = native()
    outputs = {}
    for op in loaded.operations.values():
        outputs[op["after_path"]] = api.serialized(
            loaded.records[op["after_path"]], loaded.root / api.SCHEMA
        )
    aggregate = _CAPTURE.script("scripts/aggregate_records.py")
    for category, name in zip(("mapped", "unmapped"), api.AGGREGATES, strict=True):
        records = [
            {
                k: copy.deepcopy(v)
                for k, v in rec.items()
                if k not in aggregate.PER_RECORD_ONLY_FIELDS
            }
            for path, rec in sorted(loaded.records.items())
            if path.split("/")[2] == category
        ]
        records = aggregate._order_like(records, loaded.predecessor.root / name)
        collection = {
            "generation_date": loaded.request["timestamp"],
            "total_count": len(records),
            "mapped_count": sum(r["mapping_status"] == "MAPPED" for r in records),
            "unmapped_count": sum(r["mapping_status"] == "UNMAPPED" for r in records),
            "ingredients": records,
        }
        outputs[name] = api.serialized(collection, loaded.root / api.SCHEMA, "IngredientCollection")
    outputs[MARKER] = api.encoded(
        {
            "schema_version": 1,
            "capability": CAPABILITY,
            "root": str(loaded.root),
            "request": _ref(
                loaded.root,
                loaded.root / loaded.request_path,
                loaded.inputs.read(loaded.request_path),
            ),
            "predecessor": loaded.request["predecessor"],
        }
    )
    return outputs


def _roundtrip(loaded, staged):
    """Exercise the native exporter with a captured in-memory sink, no live writes."""
    api = native()
    exporter = _CAPTURE.script("scripts/export_individual_records.py")
    names = exporter.collect_existing_filenames(loaded.predecessor.root / "data/ingredients")
    preserved = exporter.collect_preserved_fields(loaded.predecessor.root / "data/ingredients")
    actual = {}
    for category, name in zip(("mapped", "unmapped"), api.AGGREGATES, strict=True):
        directory = loaded.root / "data/ingredients" / category

        def sink(path, record, directory=directory):
            require(path.parent == directory, "roundtrip destination escaped category")
            key = str(path.relative_to(loaded.root))
            require(key not in actual, "roundtrip owner collision")
            actual[key] = copy.deepcopy(record)

        stats = exporter.export_collection_to_individual_files(
            staged[name].path,
            directory,
            preserved=preserved,
            existing_names=names,
            record_sink=sink,
        )
        require(
            stats["total"] == len([p for p in loaded.records if p.split("/")[2] == category]),
            "native roundtrip lost category owners",
        )
    require(
        actual == loaded.records, "native exporter roundtrip changed complete records/filenames"
    )
    loaded.check()
    return {"complete_owners": len(actual), "native_exporter": True, "maintained_writes": False}


def _states(loaded):
    return {
        **loaded.owners,
        **{n: loaded.inputs.files[n] for n in (*native().AGGREGATES, *LEDGERS)},
        **loaded.publication,
        **{n: None for n in (*loaded.moves.values(), MARKER) if n not in loaded.owners},
    }


def _closure(loaded, staged):
    return {
        "qualified_predecessor": loaded.predecessor.closure(),
        "target": native().hashes(loaded.inputs.files),
        "owner_states": _optional_hashes(_states(loaded)),
        "publication_beforeimages": _optional_hashes(loaded.publication),
        "staged": {
            str(f.path.relative_to(loaded.root)): native().sha(f.content) for f in staged.values()
        },
    }


def _counts(loaded, outputs):
    states = _states(loaded)
    before_bytes = sum(len(f.content) for f in states.values() if f)
    peak_bytes = sum(
        max(len(f.content), len(outputs.get(n, f.content))) for n, f in states.items() if f
    ) + sum(len(raw) for n, raw in outputs.items() if states.get(n) is None)
    return {
        "owner_outputs": len(loaded.operations),
        "replacements": sum(states.get(n) is not None for n in outputs),
        "installations": sum(states.get(n) is None for n in outputs),
        "relocations": len(loaded.moves),
        "rechecks": 16 + 8 * len(outputs) + 6 * len(loaded.moves),
        "peak_growth_factor": max(
            1, peak_bytes / before_bytes, (len(states) + len(loaded.moves)) / len(states)
        ),
    }


def _profile(loaded, staged, context, directory):
    """Measure real complete guards and backups, keeping every qualified root."""
    api = native()
    storage = api.PreparationTree(loaded.root, directory)
    states = {n: f for n, f in _states(loaded).items() if f}
    log = directory / "fit.json"
    paths = tuple(directory / f"before-{i:05d}.bin" for i in range(len(states)))
    with reserve_receipt_outputs(log, backup_paths=paths) as handles:
        receipt, *backups = handles
        started = time.perf_counter()
        for handle, frozen in zip(backups, states.values(), strict=True):
            handle.write(frozen.content)
            handle.flush()
            os.fsync(handle.fileno())
        archived = [FrozenFile.capture(p) for p in paths]
        require(
            all(a.content == f.content for a, f in zip(archived, states.values(), strict=True)),
            "fit backup differs",
        )
        backup_seconds = time.perf_counter() - started

        def scan():
            storage.check()
            for handle, path in zip(handles, (log, *paths), strict=True):
                check_reserved(handle, path)
            for f in (*archived, *staged.values(), context):
                f.verify()
            loaded.check()

        samples = []
        stamp = datetime.now(timezone.utc).isoformat()
        for _ in range(2):
            started = time.perf_counter()
            scan()
            samples.append(time.perf_counter() - started)
        result = {
            "model": api.FIT_MODEL,
            "measured_at": stamp,
            "context": _ref(loaded.root, context.path, context.content),
            "sample_seconds": samples,
            "backup_seconds": backup_seconds,
            "measured_current_owner_count": len(loaded.owners),
            "lease_namespace": api._lease_namespace(loaded),
            "input_closure": _closure(loaded, staged),
            "maintained_writes": False,
            "lease_acquired": False,
        }
        finish_receipt(receipt, log, result, scan)
    return result, FrozenFile.capture(log)


def _manifest(loaded, outputs, validation):
    api = native()
    after = {
        n: api.sha(outputs[n]) if n in outputs else api.sha(loaded.owners[n].content)
        for n in loaded.records
    }
    return {
        "schema_version": 1,
        "capability": CAPABILITY,
        "state": "PREPARED_CANDIDATE_ONLY",
        "release_approval_added": False,
        "root": str(loaded.root),
        "identity": loaded.identity,
        "request": _ref(
            loaded.root, loaded.root / loaded.request_path, loaded.inputs.read(loaded.request_path)
        ),
        "predecessor": loaded.request["predecessor"],
        "before_inventory": api.hashes(loaded.owners),
        "after_inventory": after,
        "publication_beforeimages": _optional_hashes(loaded.publication),
        "ledger_sha256": {n: api.sha(loaded.inputs.read(n)) for n in LEDGERS},
        "moves": loaded.moves,
        "outputs": {n: api.sha(raw) for n, raw in outputs.items()},
        "inputs": api.hashes(loaded.inputs.files),
        "predecessor_closure": loaded.predecessor.closure(),
        "producer": _CAPTURE.receipt(loaded.inputs),
        "claw": loaded.claw.receipt(),
        "native_validation": validation,
    }


def prepare(root, request_path, stage):
    """Prepare exact reviewed deltas without modifying any maintained input."""
    api = native()
    started = time.perf_counter()
    loaded = Loaded(root, request_path)
    _admitted(loaded)
    # This elapsed native replay is separately counted for the required final replay.
    replay_started = time.perf_counter()
    loaded.predecessor.verify_native()
    terminal_replay = time.perf_counter() - replay_started
    outputs = _outputs(loaded)
    tree = api.PreparationTree(loaded.root, api._stage_path(loaded.root, _path(loaded.root, stage)))
    try:
        staged = {name: tree.put("candidate/" + name, raw) for name, raw in outputs.items()}
        validation = {
            "roundtrip": _roundtrip(loaded, staged),
            "native_write_dry_run": api._dry_run(loaded, outputs),
        }
        manifest = _manifest(loaded, outputs, validation)
        context = tree.put("fit-context.json", api.encoded(manifest))
        startup = time.perf_counter() - started + terminal_replay
        measurement, fit = _profile(
            loaded, staged, context, loaded.root / ".temp" / ("curation-fit-" + uuid.uuid4().hex)
        )
        counts = _counts(loaded, outputs)
        manifest["operational_budget"] = {
            "policy": loaded.request["operational_policy"],
            "policy_value": loaded.policy,
            "lease_namespace": api._lease_namespace(loaded),
            "counts": counts,
            "startup_seconds": startup,
            "terminal_predecessor_replay_seconds": terminal_replay,
            "measurement": _ref(loaded.root, fit.path, fit.content),
            "forecast_seconds": api._forecast(loaded.policy, counts, measurement, startup),
            "limitations": [
                *api.FIT_LIMITATIONS,
                "The non-scan startup term also includes a separately measured strict predecessor terminal replay; no future runtime guarantee.",
            ],
        }
        tree.put("manifest.json", api.encoded(manifest))
        tree.check()
        loaded.check()
        return manifest
    except BaseException as error:
        try:
            tree.put(
                "FAILED.json",
                api.encoded(
                    {"state": "FAILED_PREPARATION", "error": str(error), "maintained_writes": False}
                ),
            )
        except (OSError, ValueError):
            pass
        raise


def _prepared(root, stage, *, before=None, publication=None):
    api = native()
    root = api.root_path(root, "successor")
    stage = _path(root, stage)
    require(not os.path.lexists(stage / "FAILED.json"), "failed stage cannot apply")
    held = FrozenFile.capture(stage / "manifest.json")
    manifest = api.document(held.content)
    require(
        manifest["schema_version"] == 1
        and manifest["capability"] == CAPABILITY
        and manifest["state"] == "PREPARED_CANDIDATE_ONLY"
        and manifest["release_approval_added"] is False,
        "invalid prepared successor",
    )
    loaded = Loaded(
        root,
        manifest["request"]["path"],
        before=before,
        after_inventory=manifest["after_inventory"] if before else None,
        publication=publication,
    )
    _admitted(loaded)
    outputs = _outputs(loaded)
    staged = {n: FrozenFile.capture(stage / "candidate" / n) for n in outputs}
    actual = set()
    for path in (stage / "candidate").rglob("*"):
        no_alias(path)
        if path.is_file():
            actual.add(str(path.relative_to(stage / "candidate")))
    require(
        actual == set(outputs) and all(staged[n].content == raw for n, raw in outputs.items()),
        "prepared output membership/content changed",
    )
    # The exporter sink is pure with respect to maintained records; actual collections are staged.
    validation = {
        "roundtrip": _roundtrip(loaded, staged),
        "native_write_dry_run": manifest["native_validation"]["native_write_dry_run"],
    }
    expected_dry = {
        "applied": False,
        "changed": [],
        "created": [],
        "unchanged": [],
        "journal": None,
    }
    for name, raw in sorted(outputs.items()):
        previous = _states(loaded).get(name)
        kind = (
            "created" if previous is None else "unchanged" if previous.content == raw else "changed"
        )
        expected_dry[kind].append(str(root / name))
    require(validation["native_write_dry_run"] == expected_dry, "native dry-run accounting differs")
    expected = _manifest(loaded, outputs, validation)
    if before is not None:
        # #1378: keep the original acquisition metadata while authenticating
        # current executable bytes/runtime and the actual descendant checkout.
        current_producer, original_producer = expected["producer"], manifest["producer"]
        require(
            set(current_producer) == set(original_producer)
            and all(
                current_producer[k] == original_producer[k]
                for k in ("schema_version", "status", "source_sha256", "files", "runtime")
            )
            and original_producer["selected_context"]["git_revision"] == loaded.identity["head"],
            "completed producer/source/runtime differs",
        )
        expected["producer"] = original_producer
    budget = manifest["operational_budget"]
    api.keys(
        budget,
        {
            "policy",
            "policy_value",
            "lease_namespace",
            "counts",
            "startup_seconds",
            "terminal_predecessor_replay_seconds",
            "measurement",
            "forecast_seconds",
            "limitations",
        },
    )
    require(
        budget["limitations"]
        == [
            *api.FIT_LIMITATIONS,
            "The non-scan startup term also includes a separately measured strict predecessor terminal replay; no future runtime guarantee.",
        ],
        "operational limitations differ",
    )
    require(
        {k: v for k, v in manifest.items() if k != "operational_budget"} == expected,
        "prepared reconstruction/provenance differs",
    )
    require(
        budget["policy"] == loaded.request["operational_policy"]
        and budget["policy_value"] == loaded.policy
        and budget["lease_namespace"] == api._lease_namespace(loaded)
        and budget["counts"] == _counts(loaded, outputs),
        "fit policy/scope/namespace changed",
    )
    measurement = api.document(
        loaded.inputs.read(budget["measurement"]["path"], budget["measurement"]["sha256"])
    )
    context = FrozenFile.capture(stage / "fit-context.json")
    # Historical Inputs are seeded with actual archives in a different insertion
    # order. Values were reconstructed above; retain the original native bytes.
    require(
        context.content
        == api.encoded({k: v for k, v in manifest.items() if k != "operational_budget"})
        and measurement["context"] == _ref(root, context.path, context.content),
        "fit context differs",
    )
    # The fit itself was created after the exact manifest input closure was frozen.
    closure = _closure(loaded, staged)
    closure["target"].pop(budget["measurement"]["path"], None)
    require(
        measurement["input_closure"] == closure
        and measurement["measured_current_owner_count"] == len(loaded.owners),
        "fit omits qualified current inputs",
    )
    api._positive(budget["terminal_predecessor_replay_seconds"], "terminal replay")
    require(
        budget["startup_seconds"] >= budget["terminal_predecessor_replay_seconds"]
        and budget["forecast_seconds"]
        == api._forecast(loaded.policy, budget["counts"], measurement, budget["startup_seconds"]),
        "fit forecast differs",
    )
    context.verify()
    loaded.check()
    held.verify()
    return loaded, manifest, held, staged, outputs


def _acceptance(loaded, held, path):
    api = native()
    name = str(_path(loaded.root, path).relative_to(loaded.root))
    value = api.document(loaded.inputs.read(name))
    api.keys(value, {"manifest_sha256", "review"})
    require(
        value["manifest_sha256"] == api.sha(held.content),
        "technical acceptance names another prepared set",
    )
    report, target, _, dimensions, source = _review(loaded, value["review"], scientific=False)
    require(
        report["reviewer"]["independence"] == "independent"
        and report["reviewer"].get("independence_basis")
        and report["reviewer"]["identity"] not in loaded.scientists,
        "independent technical prepared-set reviewer required",
    )
    relative = str(held.path.relative_to(loaded.root))
    tid = value["review"]["target_id"]
    require(
        source.get(relative) == api.sha(held.content)
        and target.get("path") == relative
        and target.get("kind") == "snapshot_row"
        and target.get("selector") == "prepared"
        and target.get("semantic_digest")
        == {
            "algorithm": "sha256",
            "sha256": api.sha(held.content),
            "description": "Exact prepared curation successor manifest bytes",
        }
        and target.get("owner_paths")
        == [{"repository": REPOSITORY, "path": relative, "role": "prepared source correction"}],
        "technical target omits exact prepared manifest",
    )
    # Technical acceptance must include the full direct scientific input union.
    for op in loaded.operations.values():
        for role in ("primary", "skeptic"):
            r, _, _, _, inputs = _review(loaded, op[role], scientific=True)
            require(
                all(source.get(n) == h for n, h in inputs.items()),
                "technical acceptance omits scientific evidence union",
            )
            require(
                source.get(op[role]["path"]) == op[role]["sha256"]
                and source.get(str(Path(op[role]["path"]).with_name("review.md")))
                == op[role]["markdown_sha256"],
                "technical acceptance omits scientific pair",
            )
    require(
        not any(
            tid in f["target_ids"] and f["status"] in {"open", "deferred"}
            for f in report["findings"]
        ),
        "unresolved prepared-set technical finding",
    )
    budget = api.document(held.content)["operational_budget"]
    require(
        dimensions.get("curation_action") == "apply_exact_prepared_set"
        and dimensions.get("operational_budget_sha256") == api.digest(budget)
        and dimensions.get("lease_seconds") == str(budget["policy_value"]["lease_seconds"])
        and dimensions.get("lease_namespace_sha256") == api.digest(budget["lease_namespace"])
        and dimensions.get("lease_scheduling") == "mediaingredientmech_and_global_conflict_reviewed"
        and dimensions.get("historical_obligations_sha256")
        == api.digest(loaded.context["historical_obligations"]),
        "technical acceptance omits exact budget/namespace/history/scheduling",
    )
    return _ref(loaded.root, loaded.root / name, loaded.inputs.read(name))


def _events(loaded, outputs):
    api = native()
    states = _states(loaded)
    events = []
    for name in [p for p in outputs if p.startswith("data/ingredients/")]:
        if states.get(name) is None or states[name].content != outputs[name]:
            events.append({"kind": "write", "path": name, "sha256": api.sha(outputs[name])})
    events.extend(
        {"kind": "relocate", "source": old, "destination": new} for old, new in loaded.moves.items()
    )
    for name in (*api.AGGREGATES, MARKER):
        if states.get(name) is None or states[name].content != outputs[name]:
            events.append({"kind": "write", "path": name, "sha256": api.sha(outputs[name])})
    return events


def apply(root, stage, acceptance_path, receipt_dir, *, enabled=False):
    """Apply only the exact paired-reviewed delta under the unchanged native lease."""
    api = native()
    started = time.perf_counter()
    root = api.root_path(root, "successor")
    receipt_dir = _path(root, receipt_dir)
    # No implicit partial resume or caller-selected retry into an occupied receipt.
    require(not os.path.lexists(receipt_dir), "application receipt directory already exists")
    loaded, manifest, held, staged, outputs = _prepared(root, stage)
    acceptance = _acceptance(loaded, held, acceptance_path)
    budget = manifest["operational_budget"]
    measurement = api.document(
        loaded.inputs.read(budget["measurement"]["path"], budget["measurement"]["sha256"])
    )
    api._fit_age(loaded.policy, measurement)
    if not enabled:
        result = api._dry_run(loaded, outputs)
        loaded.check()
        return {
            "applied": False,
            "approval": "NONE",
            "native_write_dry_run": result,
            "manifest": _ref(root, held.path, held.content),
            "acceptance": acceptance,
        }
    # Include a measured strict predecessor replay in the non-scan term for its
    # mandatory terminal invocation. No assumption about a cheap cached proof.
    replay = time.perf_counter()
    loaded.predecessor.verify_native()
    replay = time.perf_counter() - replay
    startup = max(budget["startup_seconds"], time.perf_counter() - started + replay)
    measurement, fit = _profile(
        loaded, staged, held, root / ".temp" / ("curation-fit-" + uuid.uuid4().hex)
    )
    forecast = api._forecast(loaded.policy, budget["counts"], measurement, startup)
    api._fit_age(loaded.policy, measurement)
    require(api._lease_namespace(loaded) == budget["lease_namespace"], "accepted namespace changed")
    locks = loaded.claw.modules["locks"].LockManager()
    lease_started = time.monotonic()
    with locks.lock(
        "mediaingredientmech",
        "reviewed exact source curation successor",
        timeout=loaded.policy["lease_seconds"],
    ):
        with locks._leases_guard:
            token = locks._leases.get("mediaingredientmech")
        lease = locks.check_lock("mediaingredientmech")
        require(
            token and lease and lease.get("lease_token") == token,
            "native acquired lease ownership lost",
        )
        expires = lease["expires_at"]
        deadline = datetime.fromisoformat(expires)
        require(
            deadline.utcoffset() is not None and locks._utc_now() < deadline,
            "native lease already expired",
        )
        loaded.check()
        api._dry_run(loaded, outputs)
        storage = api.PreparationTree(root, api._stage_path(root, receipt_dir))
        states = _states(loaded)
        backups = {
            name: receipt_dir / f"before-{i:05d}.bin"
            for i, (name, f) in enumerate(states.items())
            if f
        }
        for i, _ in enumerate(loaded.moves):
            storage.ensure(receipt_dir / f"relocation-{i:05d}")
        log = receipt_dir / "application.json"
        result = {
            "schema_version": 1,
            "capability": CAPABILITY,
            "state": "PREPARED",
            "release_approval_added": False,
            "root": str(root),
            "manifest": _ref(root, held.path, held.content),
            "predecessor": loaded.request["predecessor"],
            "acceptance": acceptance,
            "beforeimages": {
                name: _ref(root, backups[name], f.content) if f else None
                for name, f in states.items()
            },
            "publication_beforeimages": manifest["publication_beforeimages"],
            "outputs": manifest["outputs"],
            "completed_operations": [],
            "retired_sources": {},
            "recovery_required": False,
            "operational_fit": {
                "receipt": _ref(root, fit.path, fit.content),
                "startup_seconds": startup,
                "terminal_predecessor_replay_seconds": replay,
                "forecast_seconds": forecast,
                "budget_sha256": api.digest(budget),
            },
        }
        archives = []
        with reserve_receipt_outputs(log, backup_paths=tuple(backups.values())) as handles:
            receipt, *backup_handles = handles

            def lease_current():
                with locks._leases_guard:
                    require(
                        locks._leases.get("mediaingredientmech") == token,
                        "native lease ownership lost",
                    )
                current = locks.check_lock("mediaingredientmech")
                require(
                    current
                    and current.get("lease_token") == token
                    and current.get("expires_at") == expires
                    and locks._utc_now() < deadline
                    and time.monotonic() - lease_started < loaded.policy["lease_seconds"]
                    and api._lease_namespace(loaded) == budget["lease_namespace"],
                    "native lease expired/lost or namespace changed",
                )

            def recheck(during=()):
                lease_current()
                storage.check()
                for handle, path in zip(handles, (log, *backups.values()), strict=True):
                    check_reserved(handle, path)
                for frozen in (*archives, *staged.values(), held, fit):
                    frozen.verify()
                loaded.check(states, during)
                lease_current()

            def progress():
                check_reserved(receipt, log)
                receipt.seek(0)
                receipt.truncate()
                receipt.write(api.encoded(result).decode())
                receipt.flush()
                os.fsync(receipt.fileno())
                check_reserved(receipt, log)

            try:
                for name, handle in zip(backups, backup_handles, strict=True):
                    handle.write(states[name].content)
                    handle.flush()
                    os.fsync(handle.fileno())
                archives.extend(FrozenFile.capture(path) for path in backups.values())
                recheck()
                progress()
                result["state"] = "APPLYING"
                for name in [
                    *[n for n in outputs if n.startswith("data/ingredients/")],
                    "__RELOCATIONS__",
                    *api.AGGREGATES,
                    MARKER,
                ]:
                    recheck()
                    if name == "__RELOCATIONS__":
                        for i, (old, new) in enumerate(loaded.moves.items()):
                            retired = _retire(
                                states[old], receipt_dir / f"relocation-{i:05d}", recheck
                            )
                            states[old] = None
                            archives.append(retired)
                            result["retired_sources"][old] = _ref(
                                root, retired.path, retired.content
                            )
                            result["completed_operations"].append(
                                {"kind": "relocate", "source": old, "destination": new}
                            )
                            recheck()
                            progress()
                        continue
                    raw = outputs[name]
                    if states.get(name) is not None and states[name].content == raw:
                        continue

                    def boundary(name=name):
                        recheck((name,))

                    if states.get(name) is None:
                        installed = _new_owner(root, name, raw, boundary)
                    else:

                        def render(path, raw=raw):
                            path.write_bytes(raw)

                        installed = publish_validated(states[name], render, boundary)
                    require(installed.content == raw, "installed output differs")
                    states[name] = installed
                    result["completed_operations"].append(
                        {"kind": "write", "path": name, "sha256": api.sha(raw)}
                    )
                    recheck()
                    progress()
                require(
                    api.hashes(api.inventory(root)) == manifest["after_inventory"]
                    and result["completed_operations"] == _events(loaded, outputs),
                    "completed owner scope/operation log differs",
                )
                validate_records(
                    parse_registry(loaded.inputs.read(LEDGERS[0]), loaded.inputs.read(LEDGERS[1])),
                    {n: api.load_yaml(f.content) for n, f in api.inventory(root).items()},
                )
                # This original native invocation is never redirected to our successor.
                loaded.predecessor.verify_native()
                recheck()
                result["state"] = "COMPLETE"
                receipt.seek(0)
                receipt.truncate()
                finish_receipt(receipt, log, result, recheck)
                return result
            except BaseException as error:
                result.update(
                    state="FAILED", recovery_required=True, error=f"{type(error).__name__}: {error}"
                )
                result["observed_outputs"] = {}
                for name in set(outputs) | set(loaded.moves):
                    try:
                        result["observed_outputs"][name] = _ref(root, root / name)
                    except (ValueError, OSError) as observed:
                        result["observed_outputs"][name] = {"error": str(observed)}
                try:
                    progress()
                except (ValueError, OSError):
                    pass
                raise


def _completed(root, stage, receipt_path, *, publication=None):
    """Reconstruct the native source transition; no receipt-shaped object is enough."""
    api = native()
    root = api.root_path(root, "successor")
    stage = _path(root, stage)
    receipt_file = FrozenFile.capture(_path(root, receipt_path))
    receipt = api.document(receipt_file.content)
    require(
        receipt["schema_version"] == 1
        and receipt["capability"] == CAPABILITY
        and receipt["state"] == "COMPLETE"
        and receipt["recovery_required"] is False
        and receipt["release_approval_added"] is False
        and receipt["root"] == str(root),
        "completed source correction required",
    )
    manifest_file = FrozenFile.capture(stage / "manifest.json")
    manifest = api.document(manifest_file.content)
    require(
        receipt["manifest"] == _ref(root, manifest_file.path, manifest_file.content),
        "completion belongs to another stage",
    )
    before = {}
    for name, ref in receipt["beforeimages"].items():
        api.relative(name)
        if ref is not None:
            before[name] = FrozenFile.capture(_path(root, ref["path"]))
            require(api.sha(before[name].content) == ref["sha256"], "recovery beforeimage differs")
    loaded, expected, held, staged, outputs = _prepared(
        root, stage, before=before, publication=publication
    )
    require(
        expected == manifest and held.content == manifest_file.content,
        "manifest changed during replay",
    )
    require(
        set(receipt["beforeimages"]) == set(_states(loaded))
        and _optional_hashes(_states(loaded))
        == {n: ref["sha256"] if ref else None for n, ref in receipt["beforeimages"].items()},
        "beforeimage membership/content differs",
    )
    require(
        receipt["predecessor"] == loaded.request["predecessor"]
        and receipt["publication_beforeimages"] == manifest["publication_beforeimages"]
        and receipt["outputs"] == manifest["outputs"]
        and receipt["completed_operations"] == _events(loaded, outputs),
        "completion accounting differs",
    )
    require(
        _acceptance(loaded, held, receipt["acceptance"]["path"]) == receipt["acceptance"],
        "technical acceptance changed",
    )
    fit = receipt["operational_fit"]
    fit_file = FrozenFile.capture(_path(root, fit["receipt"]["path"]))
    require(api.sha(fit_file.content) == fit["receipt"]["sha256"], "application fit changed")
    measurement = api.document(fit_file.content)
    budget = manifest["operational_budget"]
    closure = _closure(loaded, staged)
    require(
        measurement["input_closure"] == closure
        and measurement["context"] == _ref(root, held.path, held.content)
        and measurement["lease_namespace"] == budget["lease_namespace"]
        and fit["budget_sha256"] == api.digest(budget)
        and fit["forecast_seconds"]
        == api._forecast(loaded.policy, budget["counts"], measurement, fit["startup_seconds"]),
        "completed operational fit differs",
    )
    require(set(receipt["retired_sources"]) == set(loaded.moves), "retirement membership differs")
    for old, ref in receipt["retired_sources"].items():
        archived = FrozenFile.capture(_path(root, ref["path"]))
        loaded.inputs.files[str(archived.path.relative_to(root))] = archived
        require(
            not os.path.lexists(root / old)
            and api.sha(archived.content) == ref["sha256"] == manifest["before_inventory"][old],
            "retired source changed/reappeared",
        )
    current = {name: FrozenFile.capture(root / name) for name in outputs}
    require(
        all(current[name].content == raw for name, raw in outputs.items()),
        "current source output differs",
    )
    loaded.predecessor.verify_native()
    loaded.check()
    for f in (*before.values(), *staged.values(), *current.values(), held, fit_file, receipt_file):
        f.verify()
    return (
        loaded,
        manifest,
        [*before.values(), *staged.values(), *current.values(), held, fit_file, receipt_file],
    )


def verify_completed(root, stage, receipt_path):
    """Verify the current exact source endpoint, including unchanged mapping history."""
    loaded, manifest, held = _completed(root, stage, receipt_path)
    loaded.check()
    for frozen in held:
        frozen.verify()
    return {
        "status": "COMPLETE_CURRENT_SOURCE_SUCCESSOR",
        "release_approval_added": False,
        "manifest_sha256": native().digest(manifest),
        "root": str(loaded.root),
        "predecessor": loaded.request["predecessor"],
        "original_identity": loaded.identity,
        "current_identity": loaded.current_identity,
    }


class Endpoint:
    """Captured, reconstructed source transition selected by an explicit reference.

    Publication may take ownership of the four mapping paths only inside its
    native transaction. A historical use additionally binds that transaction's
    actual receipt; the enclosing native verifier must authenticate its complete
    reconstruction before returning any success. No public verifier accepts raw
    archived maps as authority.
    """

    def __init__(self, root, reference, *, publication=None, publication_receipt=None):
        api = native()
        self.root = api.root_path(root, "source successor endpoint")
        api.keys(
            reference,
            {"schema_version", "capability", "root", "stage", "manifest", "receipt", "producer"},
        )
        require(
            reference["schema_version"] == 1
            and reference["capability"] == CAPABILITY
            and reference["root"] == str(self.root),
            "invalid/foreign successor endpoint",
        )
        self.reference = copy.deepcopy(reference)
        self.stage = _path(self.root, reference["stage"])
        self.manifest_file = FrozenFile.capture(_path(self.root, reference["manifest"]["path"]))
        self.receipt_file = FrozenFile.capture(_path(self.root, reference["receipt"]["path"]))
        require(
            _ref(self.root, self.manifest_file.path, self.manifest_file.content)
            == reference["manifest"]
            and self.manifest_file.path == self.stage / "manifest.json"
            and _ref(self.root, self.receipt_file.path, self.receipt_file.content)
            == reference["receipt"],
            "successor endpoint reference differs",
        )
        self.manifest = api.document(self.manifest_file.content)
        require(
            self.manifest["producer"] == reference["producer"],
            "successor endpoint producer differs",
        )
        self.publication_receipt = publication_receipt
        if publication_receipt is not None:
            require(publication is not None, "publication archival context omitted")
            previous = api.document(publication_receipt.content)
            require(
                previous["capability"] == "reviewed-stable-sssom-publication-v1"
                and previous["state"] == "COMPLETE"
                and previous["recovery_required"] is False
                and previous["scientific_approval_added"] is False,
                "not a completed native publication",
            )
            require(
                set(previous["beforeimages"]) == set(PUBLICATION)
                and set(publication) == set(PUBLICATION),
                "incomplete native publication archives",
            )
            for name, archived in publication.items():
                ref = previous["beforeimages"][name]
                require(
                    (ref is None and archived is None)
                    or (
                        ref is not None
                        and archived is not None
                        and _ref(self.root, archived.path, archived.content) == ref
                    ),
                    "publication archive differs from native receipt",
                )
            pub_manifest = FrozenFile.capture(_path(self.root, previous["manifest"]["path"]))
            require(
                _ref(self.root, pub_manifest.path, pub_manifest.content) == previous["manifest"],
                "publication manifest receipt differs",
            )
            spec = api.document(pub_manifest.content)
            request = FrozenFile.capture(_path(self.root, spec["request"]["path"]))
            require(
                _ref(self.root, request.path, request.content) == spec["request"],
                "publication request differs",
            )
            generation_ref = api.document(request.content)["generation"]
            generated = FrozenFile.capture(_path(self.root, generation_ref["path"]))
            require(
                _ref(self.root, generated.path, generated.content) == generation_ref,
                "publication generation differs",
            )
            selected = api.document(generated.content)
            endpoint_ref = selected.get("curation_successor")
            require(
                endpoint_ref is not None and selected["adoption"] is None,
                "publication is not the selected successor route",
            )
            endpoint = FrozenFile.capture(_path(self.root, endpoint_ref["path"]))
            require(
                _ref(self.root, endpoint.path, endpoint.content) == endpoint_ref
                and api.document(endpoint.content) == reference,
                "publication names another source endpoint",
            )
            self.publication_files = [
                pub_manifest,
                request,
                generated,
                endpoint,
                publication_receipt,
            ]
        else:
            require(
                publication is None, "naked publication beforeimages cannot authorize an endpoint"
            )
            self.publication_files = []
        self.loaded, actual, self.held = _completed(
            self.root, self.stage, self.receipt_file.path, publication=publication
        )
        require(actual == self.manifest, "successor endpoint manifest changed")
        self.check()

    def publication_guard(self):
        """Transfer only mapping-path checks to the enclosing native transaction."""
        self.check()
        if self.publication_receipt is None:
            receipt = native().document(self.receipt_file.content)
            archives = {}
            for name in PUBLICATION:
                ref = receipt["beforeimages"][name]
                frozen = FrozenFile.capture(_path(self.root, ref["path"])) if ref else None
                require(
                    (frozen is None and self.manifest["publication_beforeimages"][name] is None)
                    or (
                        frozen is not None
                        and native().sha(frozen.content)
                        == ref["sha256"]
                        == self.manifest["publication_beforeimages"][name]
                    ),
                    "source mapping archive differs",
                )
                archives[name] = frozen
            self.loaded.publication = archives
        self.loaded.publication_transaction = True

    def check(self):
        self.loaded.check()
        for frozen in (*self.held, self.manifest_file, self.receipt_file, *self.publication_files):
            frozen.verify()

    def verify_native(self):
        require(
            self.publication_receipt is None and not self.loaded.publication_transaction,
            "terminal publication verification belongs to the native publication verifier",
        )
        result = verify_completed(self.root, self.stage, self.receipt_file.path)
        self.check()
        return result

    def local_inputs(self):
        files = [
            *self.loaded.inputs.files.values(),
            *self.loaded.live_ledgers.values(),
            *self.held,
            self.manifest_file,
            self.receipt_file,
        ]
        return {
            str(f.path.relative_to(self.root)): native().sha(f.content)
            for f in files
            if f.path.is_relative_to(self.root)
        }

    def closure(self):
        return {
            "reference": self.reference,
            "target": self.local_inputs(),
            "predecessor": self.loaded.predecessor.closure(),
            "publication_beforeimages": self.manifest["publication_beforeimages"],
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["inspect", "prepare", "apply", "verify"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    for name in ("request", "stage", "acceptance", "receipt"):
        parser.add_argument("--" + name, type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.operation == "inspect":
        result = inspect(args.root, args.request)
    elif args.operation == "prepare":
        result = prepare(args.root, args.request, args.stage)
    elif args.operation == "apply":
        result = apply(args.root, args.stage, args.acceptance, args.receipt, enabled=args.apply)
    else:
        result = verify_completed(args.root, args.stage, args.receipt)
    print(native().encoded(result).decode())


if _CAPTURE is None:
    _root = Path(__file__).absolute().parents[3]
    _loader_path = _root / "src/mediaingredientmech/curate/curation_successor_producer.py"
    _raw = _loader_path.read_bytes()
    _loader = types.ModuleType("_curation_successor_loader")
    _loader.__file__ = str(_loader_path)
    exec(compile(_raw, str(_loader_path), "exec"), _loader.__dict__)
    _capture, _implementation = _loader.load(_root, _raw)
    for _name, _value in vars(_implementation).items():
        if not _name.startswith("__"):
            globals()[_name] = _value

if __name__ == "__main__":
    main()
