"""Reconstruct original CM preparation and reviewed intake before native proof.

Historical canonical inputs never become current owners or identity authority.
The optional capability extends the native source route; ordinary requests retain
their existing contract. #1431; Knowledge-Graph-Hub/kg-microbe#1882.
"""

from __future__ import annotations

import builtins
import hashlib
import io
import sys
import tarfile
import types
import uuid
from pathlib import Path

from mediaingredientmech.export import culturemech_replay_process as process
from mediaingredientmech.export import reviewed_sssom as external

CAPABILITY = "culturemech-intake-v3-replay-v1"
CAPSULE = "src/mediaingredientmech/export/_culturemech_capsule/v1/"
CAPSULE_MANIFEST_SHA = "39505bc1e9291f53a06c844ff7aab153c3885625d2a89290c3668486530275ac"
PREPARATION_SHA = "5ab4397f46c219e0f59f4bce14e31d30342e8486688fa91b9290d0d45e352b77"
VERIFICATION_SHA = "e9ae17fa6203c2389d181e9608240b3e38ea6d11e24350722d821408b1940254"
VERIFICATION_REVISION = "53b7237e941534ce53493fce705ef954d143f90d"
CM_VERIFIER_SHA = "6f03f52a859489682f41935296d576947fd891b8599e9f9e10f249ac03cd21e1"
RESOURCES = tuple(
    CAPSULE + name
    for name in (
        "manifest.json",
        "intake.culturemech.py.txt",
        "intake.culturemech_review.py.txt",
        "export.reviewed_sssom.py.txt",
        "curie.py.txt",
        "review_claims.py.txt",
        "sssom_metadata.py.txt",
        "synonym_policy.py.txt",
    )
)
MODULES = {
    "mediaingredientmech.intake.culturemech",
    "mediaingredientmech.export.reviewed_sssom",
    "mediaingredientmech.curie",
    "mediaingredientmech.review_claims",
    "mediaingredientmech.sssom_metadata",
    "mediaingredientmech.synonym_policy",
}


def require(condition, message):
    if not condition:
        raise ValueError("CM native replay: " + message)


def keys(value, expected):
    require(isinstance(value, dict) and set(value) == set(expected), "unexpected fields")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def relative(name):
    require(
        isinstance(name, str)
        and name
        and not Path(name).is_absolute()
        and ".." not in Path(name).parts
        and Path(name).as_posix() == name,
        "unsafe relative path",
    )
    return name


def parse(raw, name):
    return external._json_bytes(raw, name)


def capsule_sources(inputs):
    raw = inputs.read(CAPSULE + "manifest.json", CAPSULE_MANIFEST_SHA)
    manifest = parse(raw, "capsule manifest")
    require(set(manifest["modules"]) == MODULES, "historical module membership differs")
    sources = {}
    for name, entry in manifest["modules"].items():
        raw = inputs.read(CAPSULE + relative(entry["resource"]), entry["sha256"])
        require(len(raw) == entry["bytes"], "historical module size differs")
        sources[name] = (entry["original_path"], raw)
    late = manifest["later_intake"]
    later = inputs.read(CAPSULE + relative(late["resource"]), VERIFICATION_SHA)
    require(
        len(later) == late["bytes"]
        and sha(sources["mediaingredientmech.intake.culturemech"][1]) == PREPARATION_SHA,
        "unsupported historical implementation",
    )
    return sources, (late["original_path"], later)


class _Historical:
    def __init__(self, sources, directory, facade):
        self.sources = sources
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=False)
        self.facade = facade
        self.modules = {}
        self.packages = {}
        self.prefix = "_mim_cm_replay_" + uuid.uuid4().hex + "."
        self.identities = {}
        for path, raw in sources.values():
            target = self.directory / relative(path)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(raw)
            self.identities[path] = process.freeze_file(target, source=True)[0]

    def verify(self):
        actual = {
            p.relative_to(self.directory).as_posix()
            for p in self.directory.rglob("*")
            if p.is_file() or p.is_symlink()
        }
        require(actual == set(self.identities), "historical capsule membership changed")
        for frozen in self.identities.values():
            process.check_frozen(frozen, source=True)

    def imported(self, name, globals=None, locals=None, fromlist=(), level=0):
        if level == 0 and name == "subprocess":
            require(self.facade is not None, "historical subprocess has no bounded executor")
            return self.facade
        if level == 0 and (
            name == "mediaingredientmech" or name.startswith("mediaingredientmech.")
        ):
            require(bool(fromlist), "unscoped historical import")
            if name in self.sources:
                return self.load(name)
            package = self.packages.setdefault(name, types.ModuleType(self.prefix + name))
            for member in fromlist:
                child = name + "." + member
                require(child in self.sources, "uncaptured historical dependency: " + child)
                setattr(package, member, self.load(child))
            return package
        return builtins.__import__(name, globals, locals, fromlist, level)

    def load(self, name):
        self.verify()
        if name in self.modules:
            return self.modules[name]
        relative_path, raw = self.sources[name]
        path = self.directory / relative_path
        require(path.read_bytes() == raw, "historical execution materialization changed")
        module = types.ModuleType(self.prefix + name)
        module.__file__ = str(path)
        module.__package__ = name.rpartition(".")[0]
        module.__dict__["__builtins__"] = {**vars(builtins), "__import__": self.imported}
        self.modules[name] = module
        sys.modules[module.__name__] = module
        exec(compile(raw, module.__file__, "exec"), module.__dict__)
        self.verify()
        return module


class _HistoricalModules(dict):
    def __init__(self, original, verification):
        self.loaders = (original, verification)
        super().__init__(
            prepare=original.load("mediaingredientmech.intake.culturemech"),
            review=verification.load("mediaingredientmech.intake.culturemech"),
        )

    def verify(self):
        for loader in self.loaders:
            loader.verify()


def load_historical_modules(inputs, directory, process):
    """Use authentic preserved code with private imports and natural __file__."""
    sources, later = capsule_sources(inputs)
    original = _Historical(sources, Path(directory) / "prepare", process)
    verification = _Historical(
        {**sources, "mediaingredientmech.intake.culturemech": later},
        Path(directory) / "review",
        process,
    )
    return _HistoricalModules(original, verification)


class Selection:
    """Capture the closed accepted package's actually used historical closure."""

    def __init__(self, inputs, reference):
        keys(reference, {"path", "sha256"})
        self.inputs = inputs
        self.path = relative(reference["path"])
        self.package_root = Path(self.path).parent.as_posix()
        self.required_inputs = {}
        self.frozen_inputs = {}
        self.package = parse(self.capture(self.path, reference["sha256"]), self.path)
        keys(
            self.package,
            {
                "schema_version",
                "status",
                "consumer_commit",
                "files",
                "intake_path",
                "intake_sha256",
                "review_path",
                "reviewed_path",
                "reviewed_sha256",
                "limitations",
            },
        )
        require(
            type(self.package["schema_version"]) is int
            and self.package["schema_version"] == 1
            and self.package["status"] == "ISOLATED_REVIEWED_INTAKE_VERIFICATION_PACKAGE"
            and self.package["consumer_commit"] == VERIFICATION_REVISION,
            "unsupported accepted package",
        )
        require(isinstance(self.package["files"], dict), "invalid package inventory")
        self.consumer_files = {}
        self.member("consumer-source.tar.gz")
        self.prepared = relative(self.package["intake_path"])
        self.reviewed = relative(self.package["reviewed_path"])
        self.review_path = relative(self.package["review_path"])
        self.intake = self.json(self.prepared + "/intake.json", self.package["intake_sha256"])
        self.review = self.json(self.review_path)
        self.final = self.json(
            self.reviewed + "/reviewed-intake.json", self.package["reviewed_sha256"]
        )
        require(
            self.intake["source_contract"] == "culturemech-direct-ingredients-v3"
            and self.intake["consumer_implementation"]
            == {"sha256": PREPARATION_SHA, "bytes": 47572},
            "unsupported preparation provenance",
        )
        for prefix, manifest in ((self.prepared, self.intake), (self.reviewed, self.final)):
            require(isinstance(manifest["files"], dict), "invalid artifact membership")
            for name, pin in manifest["files"].items():
                raw = self.read(prefix + "/" + relative(name), pin["sha256"])
                require(len(raw) == pin["bytes"], "artifact size differs")
            self.inventory(
                prefix,
                set(manifest["files"])
                | {"intake.json" if prefix == self.prepared else "reviewed-intake.json"},
            )
        owners = self.intake["mim_record_inputs"]
        require(isinstance(owners, dict), "invalid historical owner inventory")
        for name, pin in owners.items():
            require(
                name.startswith("data/ingredients/") and name.endswith(".yaml"),
                "invalid historical owner path",
            )
            raw = self.read(name, pin["sha256"])
            require(len(raw) == pin["bytes"], "historical owner size differs")
        self.owner_inventory = sorted(owners)
        self.check_owners()
        canonical = self.json(
            self.intake["canonical_review_path"], self.intake["canonical_review_sha256"]
        )
        self.read(canonical["source_sssom"], canonical["source_sha256"])
        for manifest in (canonical, self.review):
            for group in ("inputs", "record_inputs"):
                for name, pin in manifest.get(group, {}).items():
                    self.read(name, pin)
        self.handoff = self.prepared + "/source"
        self.source = self.json(
            self.handoff + "/bundle/manifest.json", self.intake["source_manifest_sha256"]
        )
        self.proof_paths = {
            "source_manifest": self.handoff + "/bundle/manifest.json",
            "prepared_intake": self.prepared + "/intake.json",
            "reviewed_intake": self.reviewed + "/reviewed-intake.json",
            "binding_review": self.review_path,
        }
        capsule_sources(inputs)
        for name in RESOURCES:
            self.required_inputs[name] = inputs.hashes[name]

    def capture(self, name, expected):
        if name in self.frozen_inputs:
            raw = process.check_frozen(self.frozen_inputs[name], source=True)
        else:
            frozen, raw = process.freeze_file(self.inputs.root / name, source=True)
            self.frozen_inputs[name] = frozen
        require(self.inputs.read(name, expected) == raw, "package bytes changed during capture")
        self.required_inputs[name] = self.inputs.hashes[name]
        return raw

    def member(self, name, expected=None):
        relative(name)
        pin = self.package["files"].get(name)
        keys(pin, {"sha256", "bytes"})
        require(expected is None or pin["sha256"] == expected, "conflicting package member pin")
        full = (Path(self.package_root) / name).as_posix()
        raw = self.capture(full, pin["sha256"])
        require(
            type(pin["bytes"]) is int and len(raw) == pin["bytes"], "package member size differs"
        )
        self.required_inputs[full] = self.inputs.hashes[full]
        return raw

    def read(self, name, expected=None):
        raw = self.member("consumer/" + relative(name), expected)
        self.consumer_files[name] = raw
        return raw

    def json(self, name, expected=None):
        return parse(self.read(name, expected), name)

    def consumer_root(self):
        return self.inputs.root / self.package_root / "consumer"

    def inventory(self, prefix, expected):
        root = self.consumer_root() / prefix
        actual = {
            p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() or p.is_symlink()
        }
        require(actual == expected, "prepared/reviewed artifact membership differs")

    def check_owners(self):
        root = self.consumer_root()
        actual = sorted(
            p.relative_to(root).as_posix() for p in (root / "data/ingredients").rglob("*.yaml")
        )
        require(actual == self.owner_inventory, "historical owner membership differs")

    def recheck(self):
        self.check_owners()
        for prefix, manifest, name in (
            (self.prepared, self.intake, "intake.json"),
            (self.reviewed, self.final, "reviewed-intake.json"),
        ):
            self.inventory(prefix, set(manifest["files"]) | {name})
        self.inputs.recheck()
        for frozen in self.frozen_inputs.values():
            process.check_frozen(frozen, source=True)

    def declaration(self, path):
        full = (Path(self.package_root) / "consumer" / path).as_posix()
        return {"path": full, "sha256": self.inputs.hashes[full]}


def _materialize(directory, files):
    directory.mkdir(parents=True, exist_ok=False)
    for name, raw in files.items():
        target = directory / relative(name)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(raw)


def _producer(selection, directory):
    """Extract only authenticated regular archive members; never execute extras."""
    archive_bytes = selection.consumer_files[selection.handoff + "/producer-source.tar.gz"]
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:gz") as archive:
        seen = set()
        for member in archive.getmembers():
            name = relative(member.name)
            require(
                name not in seen and Path(name).parts[0] == "producer",
                "duplicate/unsafe archive member",
            )
            seen.add(name)
            require(member.isdir() or member.isfile(), "archive links/special members refused")
            if member.isfile():
                stream = archive.extractfile(member)
                if stream is None:
                    raise ValueError("CM native replay: archive member has no bytes")
                raw = stream.read()
                require(len(raw) == member.size, "truncated archive member")
                files[Path(name).relative_to("producer").as_posix()] = raw
    expected = {
        **selection.source["dependencies"],
        **{"data/normalized_yaml/" + name: pin for name, pin in selection.source["inputs"].items()},
    }
    fixed = {
        "scripts/ingredient_release_bundle.py",
        "scripts/ingredient_occurrences.py",
        "scripts/record_kinds.py",
        "scripts/validate_strict.py",
        "pyproject.toml",
        "uv.lock",
        "src/culturemech/data/mediaingredientmech/label_index.csv",
        "src/culturemech/data/mediaingredientmech/label_index.metadata.json",
    }
    archive_closure = {
        name
        for name in files
        if name in fixed
        or (name.startswith("src/culturemech/") and name.endswith(".py"))
        or (name.startswith("src/culturemech/schema/") and name.endswith(".yaml"))
        or (name.startswith("data/normalized_yaml/") and name.endswith(".yaml"))
    }
    require(
        archive_closure == set(expected),
        "archived source/dependency membership differs from manifest",
    )
    for name, pin in expected.items():
        selected_raw = files.get(relative(name))
        require(
            selected_raw is not None
            and {"sha256": sha(selected_raw), "bytes": len(selected_raw)} == pin,
            "archived producer dependency differs: " + name,
        )
    require(
        sha(files["scripts/ingredient_release_bundle.py"]) == CM_VERIFIER_SHA,
        "unsupported source verifier implementation",
    )
    # Do not materialize unneeded archive files or Python startup entrypoints.
    selected = {name: files[name] for name in expected}
    _materialize(directory, selected)
    return selected


def _compare(output, expected):
    require(output.is_dir() and not output.is_symlink(), "aliased materialized root")
    members = list(output.rglob("*"))
    require(not any(p.is_symlink() for p in members), "symlink materialized member")
    actual, identities = {}, {}
    for path in members:
        if path.is_dir():
            continue
        name = path.relative_to(output).as_posix()
        frozen, raw = process.freeze_file(path, source=True)
        actual[name], identities[name] = raw, frozen
    require(
        actual == expected, "native reconstruction differs from accepted artifact bytes/membership"
    )
    return identities


def _unchanged(output, expected, identities):
    require(_compare(output, expected) == identities, "materialized member identity changed")


def replay(selection):
    """Run both real reconstructions; proof exists only after exact comparisons."""
    selection.recheck()
    inputs = selection.inputs
    base = inputs.root / ".temp/native-culturemech-replay"
    scratch = base / uuid.uuid4().hex
    package_directory = (inputs.root / selection.package_root).resolve()
    require(
        not scratch.resolve().is_relative_to(package_directory)
        and not package_directory.is_relative_to(scratch.resolve()),
        "scratch overlaps selected input package",
    )
    require(not any(p.is_symlink() for p in (base, *base.parents)), "aliased scratch root")
    base.mkdir(parents=True, exist_ok=True)
    require(not any(p.is_symlink() for p in (base, *base.parents)), "aliased scratch root")
    scratch.mkdir()
    historical = scratch / "historical"
    _materialize(historical, selection.consumer_files)
    historical_ids = _compare(historical, selection.consumer_files)
    producer = scratch / "producer"
    producer_bytes = _producer(selection, producer)
    producer_ids = _compare(producer, producer_bytes)
    bundle = historical / selection.handoff / "bundle"
    plan = process.prepare_plan(
        producer / "scripts/ingredient_release_bundle.py",
        bundle,
        selection.intake["source_manifest_sha256"],
    )
    facade = process.VerifierProcess(plan, sys.executable, producer)
    modules = load_historical_modules(inputs, scratch / "capsule", facade)
    preparation, verification = modules["prepare"], modules["review"]
    before = verification.mim_snapshot(historical)[2]
    require(
        before == selection.intake["mim_record_inputs"], "strict historical owner snapshot differs"
    )
    prepared = scratch / "prepared"
    preparation.prepare(
        historical / selection.handoff,
        selection.intake["handoff_sha256"],
        prepared,
        Path(sys.executable),
        root=historical,
        producer_root=producer,
        review=selection.intake["canonical_review_path"],
    )
    expected_prepared = {
        name[len(selection.prepared) + 1 :]: raw
        for name, raw in selection.consumer_files.items()
        if name.startswith(selection.prepared + "/")
    }
    modules.verify()
    _unchanged(historical, selection.consumer_files, historical_ids)
    _unchanged(producer, producer_bytes, producer_ids)
    prepared_ids = _compare(prepared, expected_prepared)
    require(
        verification.mim_snapshot(historical)[2] == before,
        "historical owner membership/bytes changed",
    )
    reviewed = scratch / "reviewed"
    final = verification.finalize(
        prepared,
        selection.package["intake_sha256"],
        selection.review_path,
        reviewed,
        root=historical,
    )
    expected_reviewed = {
        name[len(selection.reviewed) + 1 :]: raw
        for name, raw in selection.consumer_files.items()
        if name.startswith(selection.reviewed + "/")
    }
    reviewed_ids = _compare(reviewed, expected_reviewed)
    require(
        verification.mim_snapshot(historical)[2] == before,
        "historical owner membership/bytes changed",
    )
    modules.verify()
    _unchanged(historical, selection.consumer_files, historical_ids)
    _unchanged(producer, producer_bytes, producer_ids)
    _unchanged(prepared, expected_prepared, prepared_ids)
    _unchanged(reviewed, expected_reviewed, reviewed_ids)
    selection.recheck()
    counts = {
        "positive_inventory": selection.intake["counts"]["source_occurrences"],
        "context_only": selection.intake["counts"]["context_only_mentions"],
        "held": selection.intake["counts"]["held_source_mentions"],
        "supported_bindings": final["counts"]["SUPPORTED"],
        "withheld_bindings": final["counts"]["WITHHOLD"],
    }
    require(
        all(type(value) is int and value >= 0 for value in counts.values()), "invalid replay counts"
    )
    return {
        **{key: selection.declaration(path) for key, path in selection.proof_paths.items()},
        "counts": counts,
    }
