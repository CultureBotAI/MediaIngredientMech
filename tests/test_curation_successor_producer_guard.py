"""Recorded loader dependencies must authenticate before execution (#1420, #1373)."""

import builtins
import os
import shutil
from pathlib import Path

import pytest

from mediaingredientmech.curate import curation_successor as successor
from tests.test_curation_successor import ref
from tests.test_stable_id_adoption import ROOT, api, commit, initialize, write

LOADER = "src/mediaingredientmech/curate/curation_successor_producer.py"
HELPER = "src/mediaingredientmech/curate/adoption_producer.py"
ENTRY = "src/mediaingredientmech/curate/curation_successor.py"
SENTINEL = b"raise RuntimeError('UNAUTHENTICATED_DEPENDENCY_EXECUTED')\n"


@pytest.fixture
def producer_tree(tmp_path):
    root = tmp_path / "producer"
    initialize(root)
    pins = {}
    for name in successor._CAPTURE.files:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, path)
        pins[name] = api.sha(path.read_bytes())
    commit(root)
    return root, pins


def test_real_loader_helpers_and_dynamic_exporter_use_authenticated_buffers(
    producer_tree, monkeypatch
):
    root, pins = producer_tree
    guard = successor._ProducerBytes({root: pins})
    compiled = []
    original = guard._compile

    def observed(raw, filename, *args, **kwargs):
        assert raw is guard.files[Path(filename)].content
        compiled.append(str(Path(filename).relative_to(root)))
        return original(raw, filename, *args, **kwargs)

    monkeypatch.setattr(guard, "_compile", observed)
    capture, native = guard.load(root, LOADER)
    assert {name: api.sha(value[0]) for name, value in capture.files.items()} == pins
    capture.script("scripts/aggregate_records.py")
    capture.script("scripts/export_individual_records.py")
    assert {
        LOADER,
        HELPER,
        ENTRY,
        "src/mediaingredientmech/export/source_producer.py",
        "scripts/aggregate_records.py",
        "scripts/export_individual_records.py",
    } <= set(compiled)
    assert native.require.__globals__["builtins"] is guard.builtins
    assert native.require.__globals__["__builtins__"]["exec"] == guard.execute
    assert guard.builtins is not builtins
    assert builtins.compile is compile and builtins.exec is exec


@pytest.mark.parametrize(
    "name",
    [
        HELPER,
        ENTRY,
        "src/mediaingredientmech/export/source_producer.py",
        "scripts/export_individual_records.py",
    ],
)
def test_wrong_hash_dependency_refuses_before_top_level_sentinel(producer_tree, name):
    root, pins = producer_tree
    (root / name).write_bytes(SENTINEL)
    with pytest.raises(ValueError, match="recorded producer bytes differ"):
        successor._ProducerBytes({root: pins}).load(root, LOADER)


@pytest.mark.parametrize("alias", ["symlink", "hardlink"])
def test_same_byte_alias_refuses_before_even_a_pinned_sentinel(producer_tree, tmp_path, alias):
    root, pins = producer_tree
    helper = root / HELPER
    helper.write_bytes(SENTINEL)
    pins[HELPER] = api.sha(SENTINEL)
    other = tmp_path / "same-helper.py"
    other.write_bytes(SENTINEL)
    helper.unlink()
    if alias == "symlink":
        helper.symlink_to(other)
    else:
        os.link(other, helper)
    with pytest.raises(ValueError, match="alias"):
        successor._ProducerBytes({root: pins}).load(root, LOADER)


def test_omitted_helper_pin_cannot_execute_its_top_level_sentinel(producer_tree):
    root, pins = producer_tree
    (root / HELPER).write_bytes(SENTINEL)
    del pins[HELPER]
    with pytest.raises(ValueError, match="unrecorded producer compilation"):
        successor._ProducerBytes({root: pins}).load(root, LOADER)


def test_unchecked_late_reread_is_not_the_executable_buffer(producer_tree, monkeypatch):
    root, pins = producer_tree
    guard = successor._ProducerBytes({root: pins})
    original = Path.read_bytes

    def changed(path):
        return SENTINEL if path == root / HELPER else original(path)

    monkeypatch.setattr(Path, "read_bytes", changed)
    with pytest.raises(ValueError, match="reread differs"):
        guard.load(root, LOADER)


@pytest.mark.parametrize("replacement", ["wrong-bytes", "same-bytes"])
def test_late_helper_replacement_after_loader_exec_refuses_before_dependency(
    producer_tree, monkeypatch, replacement
):
    root, pins = producer_tree
    guard = successor._ProducerBytes({root: pins})
    original = guard._exec
    helper = root / HELPER
    raw = helper.read_bytes()
    changed = []

    def after_loader(code, namespace, locals=None, **kwargs):
        result = original(code, namespace, locals, **kwargs)
        if code.co_filename == str(root / LOADER):
            temporary = root / "replacement.py"
            temporary.write_bytes(SENTINEL if replacement == "wrong-bytes" else raw)
            temporary.replace(helper)
            changed.append(helper)
        return result

    monkeypatch.setattr(guard, "_exec", after_loader)
    with pytest.raises(ValueError, match="identity changed|Captured input changed"):
        guard.load(root, LOADER)
    assert changed == [helper]


def test_initial_parent_identity_remains_bound_with_unchanged_leaf_inodes(producer_tree):
    root, pins = producer_tree
    guard = successor._ProducerBytes({root: pins})
    parent = (root / HELPER).parent
    identity = (root / HELPER).stat().st_ino
    saved = root / "original-parent"
    parent.rename(saved)
    parent.mkdir()
    for path in saved.iterdir():
        path.rename(parent / path.name)
    assert (root / HELPER).stat().st_ino == identity
    with pytest.raises(ValueError, match="parent changed"):
        guard.load(root, LOADER)


def test_code_compiled_outside_authenticated_boundary_cannot_execute(producer_tree):
    root, pins = producer_tree
    guard = successor._ProducerBytes({root: pins})
    code = compile(SENTINEL, str(root / HELPER), "exec")
    with pytest.raises(ValueError, match="not compiled from authenticated buffers"):
        guard.execute(code, {})


@pytest.mark.parametrize("kind", ["adoption", "successor"])
@pytest.mark.parametrize("timing", ["before-capture", "after-capture"])
def test_predecessor_entrypoint_authenticates_before_bootstrap_sentinel(
    producer_tree, tmp_path, monkeypatch, kind, timing
):
    """Incomplete proof-shaped inputs get no chance to execute unpinned code.

    These are structural bootstrap counterexamples, not native completion claims.
    The test fails with the actual sentinel when the production guard call is
    removed while leaving the guard class itself in place.
    """
    root, pins = producer_tree
    target = tmp_path / "target"
    target.mkdir()
    claw = tmp_path / "claw"
    initialize(claw)
    (claw / "dummy.py").write_bytes(b"# Never executed by this refusal test.\n")
    claw_head = commit(claw)
    claw_spec = {
        "root": str(claw),
        "head": claw_head,
        "files": {"dummy.py": api.sha((claw / "dummy.py").read_bytes())},
    }

    def structural_reference(selected, predecessor=None):
        request = {"predecessor": predecessor}
        write(selected / "request.json", request)
        manifest = {
            "request": ref(selected, selected / "request.json"),
            "producer": {"files": pins},
            "claw": claw_spec,
        }
        receipt = {}
        if predecessor is not None:
            manifest["predecessor"] = receipt["predecessor"] = predecessor
            write(
                selected / successor.MARKER,
                {
                    "root": str(selected),
                    "request": manifest["request"],
                    "predecessor": predecessor,
                },
            )
            manifest["outputs"] = {
                successor.MARKER: api.sha((selected / successor.MARKER).read_bytes())
            }
        write(selected / "stage/manifest.json", manifest)
        receipt["manifest"] = ref(selected, selected / "stage/manifest.json")
        write(selected / "receipt.json", receipt)
        return {
            "kind": "successor" if predecessor is not None else "adoption",
            "identity": successor._identity(selected),
            "stage": "stage",
            "manifest": receipt["manifest"],
            "receipt": ref(selected, selected / "receipt.json"),
            "producer": manifest["producer"],
            "publication_beforeimages": dict.fromkeys(successor.PUBLICATION),
            "publication_proof": None,
            "historical_reviews": [],
        }

    predecessor = None
    if kind == "successor":
        adoption = tmp_path / "adoption"
        shutil.copytree(root, adoption)
        predecessor = structural_reference(adoption)
    reference = structural_reference(root, predecessor)
    corrupted = (
        HELPER if kind == "successor" else "src/mediaingredientmech/export/source_producer.py"
    )
    if timing == "before-capture":
        (root / corrupted).write_bytes(SENTINEL)
    else:
        namespace = successor.Predecessor.__init__.__globals__
        original = namespace["_producer_bytes"]

        def replace_after_authentication(references):
            guard = original(references)
            (root / corrupted).write_bytes(SENTINEL)
            return guard

        monkeypatch.setitem(namespace, "_producer_bytes", replace_after_authentication)
    with pytest.raises(ValueError, match="recorded producer bytes differ|Captured input changed"):
        successor.Predecessor(target, reference)
