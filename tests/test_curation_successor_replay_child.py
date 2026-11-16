"""The actual historical publication replay child inherits authenticated buffers."""

import os
import shutil
import subprocess

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_sssom_publication as publication
from mediaingredientmech.curate.publication_guard import FrozenFile
from tests.stable_publication_fixture import materialize_producer
from tests.test_stable_id_adoption import ROOT, api, commit, initialize

SENTINEL = b"raise RuntimeError('UNAUTHENTICATED_REPLAY_CHILD_DEPENDENCY_EXECUTED')\n"
REPLAY = "src/mediaingredientmech/curate/stable_sssom_replay.py"


@pytest.fixture
def replay_child(tmp_path):
    root = tmp_path / "publication"
    initialize(root)
    pins = {}
    for name in publication._CAPTURE.files:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, path)
        pins[name] = api.sha(path.read_bytes())
    commit(root)
    claw = tmp_path / "claw"
    materialize_producer(claw)
    sources = {path: FrozenFile.capture(path) for path in claw.rglob("*.py")}
    guard = successor._ProducerBytes(
        {
            root: pins,
            claw: {str(path.relative_to(claw)): api.sha(f.content) for path, f in sources.items()},
        },
        identities={root: successor._identity(root)},
        heads={claw: api.git(claw, "rev-parse", "HEAD").decode().strip()},
    )
    _, native = guard.load(root, "src/mediaingredientmech/curate/stable_publication_producer.py")

    def run():
        # Deliberately incomplete owner/input fixture: real captured parent and
        # child must finish authenticated imports and refuse native membership.
        # Full byte-identical native replay is covered by publication integration.
        return native._replay_generation(
            root,
            claw,
            tmp_path / "kg",
            {"outputs": {key: {"path": "unused-" + key} for key in ("sssom", "suppressions")}},
            {"canonical_label_resolution": {}, "source_revisions": {}},
            b"",
            b"",
            b"",
            {str(path): frozen for path, frozen in sources.items()},
            [],
        )

    return root, claw, guard, native, run


def test_actual_replay_child_imports_original_claw_before_native_membership_refusal(replay_child):
    _, _, _, _, run = replay_child
    with pytest.raises(ValueError, match="complete native generation input membership differs"):
        run()


@pytest.mark.parametrize("change", ["wrong-bytes", "same-bytes", "symlink", "hardlink", "parent"])
def test_actual_replay_child_refuses_launch_time_drift_before_sentinel(
    replay_child, monkeypatch, change
):
    root, claw, guard, native, run = replay_child
    dependency = claw / "scripts/kgm_unified_mappings.py"
    raw = dependency.read_bytes()
    original = getattr(guard, "_run", subprocess.run)
    children = []

    def launch(args, **kwargs):
        if args[0] != "git":
            if change == "parent":
                directory = dependency.parent
                saved = claw / "original-scripts"
                directory.rename(saved)
                directory.mkdir()
                for path in saved.iterdir():
                    path.rename(directory / path.name)
            else:
                replacement = root / "replacement.py"
                replacement.write_bytes(SENTINEL if change == "wrong-bytes" else raw)
                if change in {"symlink", "hardlink"}:
                    dependency.unlink()
                    if change == "symlink":
                        dependency.symlink_to(replacement)
                    else:
                        os.link(replacement, dependency)
                else:
                    replacement.replace(dependency)
        result = original(args, **kwargs)
        if args[0] != "git":
            children.append(result)
        return result

    if hasattr(guard, "_run"):
        monkeypatch.setattr(guard, "_run", launch)
    else:
        # Keep this an actual launch-boundary regression when only the repair
        # is reverted: the unchanged parent otherwise uses ordinary subprocess.
        monkeypatch.setattr(native._replay_generation.__globals__["subprocess"], "run", launch)
    with pytest.raises(ValueError):
        run()
    assert len(children) == 1 and children[0].returncode != 0
    assert b"Authenticated replay child:" in children[0].stderr
    assert b"UNAUTHENTICATED_REPLAY_CHILD_DEPENDENCY_EXECUTED" not in children[0].stderr


def test_replay_child_refuses_changed_top_level_before_launch(replay_child, monkeypatch):
    root, _, guard, _, run = replay_child
    (root / REPLAY).write_bytes(SENTINEL)
    launches = []
    original = guard._run

    def launch(args, **kwargs):
        if args[0] != "git":
            launches.append(args)
        return original(args, **kwargs)

    monkeypatch.setattr(guard, "_run", launch)
    with pytest.raises(ValueError, match="Captured input changed"):
        run()
    assert not launches


@pytest.mark.parametrize("drift", [False, True])
def test_actual_replay_child_skips_startup_hook_before_authentication(
    replay_child, monkeypatch, drift
):
    """A harmless known startup marker cannot precede either native or guard refusal."""
    root, claw, guard, _, run = replay_child
    marker = root / "STARTUP_EXECUTED.txt"
    (claw / "src/sitecustomize.py").write_text(
        f"from pathlib import Path\nPath({str(marker)!r}).write_text('startup executed')\n"
    )
    original = guard._run
    children = []

    def launch(args, **kwargs):
        if args[0] != "git" and drift:
            (claw / "scripts/kgm_unified_mappings.py").write_bytes(SENTINEL)
        result = original(args, **kwargs)
        if args[0] != "git":
            children.append((args, kwargs, result))
        return result

    monkeypatch.setattr(guard, "_run", launch)
    with pytest.raises(ValueError):
        run()
    assert len(children) == 1
    args, kwargs, result = children[0]
    assert not marker.exists(), "Python startup executed uncaptured customization code"
    assert args[1:5] == ["-I", "-S", "-B", "-c"]
    assert kwargs["env"]["PYTHONPATH"] == os.pathsep.join((str(claw / "src"), str(root / "src")))
    assert kwargs["env"]["MEDIAINGREDIENTMECH_ROOT"] == str(root)
    assert result.returncode != 0
    if drift:
        assert b"Authenticated replay child:" in result.stderr
        assert b"UNAUTHENTICATED_REPLAY_CHILD_DEPENDENCY_EXECUTED" not in result.stderr
    else:
        # Actual captured Claw and its installed yaml/dotenv dependencies loaded.
        # The intentionally incomplete fixture then reaches native membership.
        assert b"complete native generation input membership differs" in result.stderr
