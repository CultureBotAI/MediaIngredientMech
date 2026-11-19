"""Scalar lookups retain authentic captures without sharing mutable policy (#1545)."""

from __future__ import annotations

import gc
import inspect
import os
import shutil
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import get_type_hints

import pytest

from mediaingredientmech.curate import stable_publication_producer as producer
from mediaingredientmech.curate import stable_sssom_publication as public
from tests.test_stable_id_adoption import CLAW, ROOT, api, command, commit, initialize

MEMBER = "src/mediaingredientmech/curate/curation_successor.py"


class PolicyFixture:
    """Only actual captured producer code and a tiny Git tree; no native apply."""

    def __init__(self, root):
        self.root = root
        initialize(root)
        for name in public._CAPTURE.files:
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        commit(root)
        self.parent, self.publication = self.load()
        self.state = self.publication.successor_ancestry_limit.__globals__
        assert self.state is self.publication.__dict__
        assert self.state["_SUCCESSOR_ANCESTRY_POLICY"] is None

    def load(self):
        return producer.load(self.root, (self.root / producer.LOADER).read_bytes())


@pytest.fixture
def fixture(tmp_path):
    return PolicyFixture(tmp_path / "producer")


def registrations(*captures):
    prefixes = tuple(capture.prefix for capture in captures)
    return {
        name: id(module) for name, module in sys.modules.copy().items() if name.startswith(prefixes)
    }


def observe_factory(fixture, monkeypatch, after_load=None):
    original = fixture.publication.successor_native
    created = []

    def load():
        implementation = original()
        created.append(implementation)
        if after_load:
            after_load(implementation)
        return implementation

    monkeypatch.setitem(fixture.state, "successor_native", load)
    return created


def observe_verify(capture, monkeypatch, calls, name):
    original = capture.verify

    def verify():
        calls.append(name)
        return original()

    monkeypatch.setattr(capture, "verify", verify)


def test_repeated_scalar_lookup_verifies_both_original_captures(fixture, monkeypatch):
    expected = fixture.publication.successor_native().MAX_SUCCESSOR_ANCESTRY
    adoption_before = fixture.state["_ADOPTION"]
    calls = []
    observe_verify(fixture.parent, monkeypatch, calls, "parent")
    children = observe_factory(
        fixture,
        monkeypatch,
        lambda implementation: observe_verify(implementation._CAPTURE, monkeypatch, calls, "child"),
    )
    lookup = fixture.publication.successor_ancestry_limit
    value = lookup()
    policy = fixture.state["_SUCCESSOR_ANCESTRY_POLICY"]
    assert type(value) is int and value == expected
    assert policy == (value, children[0]._CAPTURE)
    known = registrations(fixture.parent, policy[1])
    for _ in range(2):
        assert lookup() == expected
        assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is policy
        assert registrations(fixture.parent, policy[1]) == known
    assert calls == ["parent", "child", "parent"] * 3
    assert len(children) == 1
    assert fixture.state["_ADOPTION"] is adoption_before


def test_public_bootstrap_calls_the_private_function_state():
    state = public.successor_ancestry_limit.__globals__
    assert state is public.successor_native.__globals__
    assert state["_CAPTURE"] is public._CAPTURE
    expected = public.successor_native().MAX_SUCCESSOR_ANCESTRY
    assert public.successor_ancestry_limit() == expected
    policy = state["_SUCCESSOR_ANCESTRY_POLICY"]
    assert state["successor_ancestry_limit"]() == expected
    assert state["_SUCCESSOR_ANCESTRY_POLICY"] is policy


def test_direct_mutation_does_not_change_scalar_or_later_factories(fixture):
    first = fixture.publication.successor_native()
    expected, original_endpoint = first.MAX_SUCCESSOR_ANCESTRY, first.Endpoint
    first.MAX_SUCCESSOR_ANCESTRY = expected + 100
    first.Endpoint = object()
    assert fixture.publication.successor_ancestry_limit() == expected
    policy = fixture.state["_SUCCESSOR_ANCESTRY_POLICY"]
    later = fixture.publication.successor_native()
    assert first is not later and first._CAPTURE is not later._CAPTURE
    assert policy[1] not in (first._CAPTURE, later._CAPTURE)
    assert later.MAX_SUCCESSOR_ANCESTRY == expected
    assert inspect.isclass(later.Endpoint) and later.Endpoint is not original_endpoint
    later._CAPTURE.verify()
    first.MAX_SUCCESSOR_ANCESTRY = expected + 200
    assert fixture.publication.successor_ancestry_limit() == expected
    assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is policy


@pytest.mark.parametrize("separate_root", [False, True])
def test_publication_captures_own_independent_policy_and_lock(fixture, tmp_path, separate_root):
    if separate_root:
        other = PolicyFixture(tmp_path / "other").publication
    else:
        _, other = fixture.load()
    other_state = other.successor_ancestry_limit.__globals__
    assert other_state["_SUCCESSOR_ANCESTRY_LOCK"] is not fixture.state["_SUCCESSOR_ANCESTRY_LOCK"]
    value = fixture.publication.successor_ancestry_limit()
    assert other_state["_SUCCESSOR_ANCESTRY_POLICY"] is None
    assert other.successor_ancestry_limit() == value
    one, two = (
        fixture.state["_SUCCESSOR_ANCESTRY_POLICY"],
        other_state["_SUCCESSOR_ANCESTRY_POLICY"],
    )
    assert one is not two and one[1] is not two[1]
    if separate_root:
        (fixture.root / MEMBER).write_bytes((fixture.root / MEMBER).read_bytes() + b"\n")
        with pytest.raises(ValueError, match="executed producer/dependency changed"):
            fixture.publication.successor_ancestry_limit()
        assert other.successor_ancestry_limit() == value
        assert other_state["_SUCCESSOR_ANCESTRY_POLICY"] is two
        assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is one


def test_concurrent_first_read_publishes_one_complete_policy(fixture, monkeypatch):
    ready, release = threading.Event(), threading.Event()
    barrier = threading.Barrier(5)

    def constructed(implementation):
        ready.set()
        assert release.wait(20)

    children = observe_factory(fixture, monkeypatch, constructed)

    def lookup():
        barrier.wait(timeout=20)
        return fixture.publication.successor_ancestry_limit()

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(lookup) for _ in range(4)]
        barrier.wait(timeout=20)
        try:
            assert ready.wait(20)
            assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is None
            assert len(children) == 1
        finally:
            release.set()
        values = [future.result(timeout=30) for future in futures]
    assert len(children) == 1
    assert all(
        type(value) is int and value == children[0].MAX_SUCCESSOR_ANCESTRY for value in values
    )
    assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] == (values[0], children[0]._CAPTURE)


DRIFT_ERRORS = {
    "content": "executed producer/dependency changed",
    "replacement": "executed producer/dependency changed",
    "symlink": "symlink input",
    "hardlink": "nonregular/aliased producer",
    "git": "executing producer Git context changed",
    "runtime": "runtime dependencies changed",
}


def drift(fixture, monkeypatch, kind):
    path = fixture.root / MEMBER
    raw = path.read_bytes()
    if kind == "content":
        path.write_bytes(raw + b"\n")
    elif kind == "replacement":
        replacement = path.with_name("replacement.py")
        replacement.write_bytes(raw)
        replacement.replace(path)
    elif kind in {"symlink", "hardlink"}:
        alternate = fixture.root / "same-source.py"
        alternate.write_bytes(raw)
        path.unlink()
        if kind == "symlink":
            path.symlink_to(alternate)
        else:
            os.link(alternate, path)
    elif kind == "git":
        command(fixture.root, "commit", "--allow-empty", "-m", "Synthetic protected HEAD move")
    elif kind == "runtime":
        globals_ = fixture.parent.verify.__func__.__globals__
        actual_runtime = globals_["runtime"]

        def changed_runtime():
            return {**actual_runtime(), "python": "fixture-runtime-drift"}

        monkeypatch.setitem(globals_, "runtime", changed_runtime)
    return path, raw


@pytest.mark.parametrize("kind", list(DRIFT_ERRORS))
@pytest.mark.parametrize("initialized", [False, True])
def test_original_capture_refuses_drift_without_recapture(fixture, monkeypatch, kind, initialized):
    children = observe_factory(fixture, monkeypatch)
    lookup = fixture.publication.successor_ancestry_limit
    expected = lookup() if initialized else None
    policy = fixture.state["_SUCCESSOR_ANCESTRY_POLICY"]
    path, original = drift(fixture, monkeypatch, kind)
    for _ in range(2):
        with pytest.raises(ValueError, match=DRIFT_ERRORS[kind]):
            lookup()
        assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is policy
        assert len(children) == int(initialized)
    if kind == "content" and initialized:
        path.write_bytes(original)
        assert lookup() == expected
        assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is policy
        assert len(children) == 1


def test_factory_exception_preserves_traceback_and_does_not_retry(fixture, monkeypatch):
    error = RuntimeError("bounded fixture factory failure")
    calls = []
    known = registrations(fixture.parent)

    def failed_factory():
        calls.append("called")
        raise error

    monkeypatch.setitem(fixture.state, "successor_native", failed_factory)
    with pytest.raises(RuntimeError) as caught:
        fixture.publication.successor_ancestry_limit()
    assert caught.value is error and calls == ["called"]
    assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is None
    assert registrations(fixture.parent) == known
    frame_names = []
    trace = caught.value.__traceback__
    while trace:
        frame_names.append(trace.tb_frame.f_code.co_name)
        trace = trace.tb_next
    assert "failed_factory" in frame_names and "successor_ancestry_limit" in frame_names


class IntSubclass(int):
    pass


@pytest.mark.parametrize("invalid", [True, IntSubclass(1)])
def test_non_builtin_integer_after_real_load_is_refused(fixture, monkeypatch, invalid):
    def corrupt(implementation):
        implementation.MAX_SUCCESSOR_ANCESTRY = invalid

    children = observe_factory(fixture, monkeypatch, corrupt)
    with pytest.raises(ValueError, match="successor ancestry policy must be an actual integer"):
        fixture.publication.successor_ancestry_limit()
    assert len(children) == 1
    assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is None


def test_real_child_from_another_root_cannot_supply_policy(fixture, tmp_path, monkeypatch):
    other = PolicyFixture(tmp_path / "other")
    child = other.publication.successor_native()
    child._CAPTURE.verify()
    monkeypatch.setitem(fixture.state, "successor_native", lambda: child)
    with pytest.raises(
        ValueError, match="successor policy capture differs from selected publication producer"
    ):
        fixture.publication.successor_ancestry_limit()
    assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is None
    assert other.state["_SUCCESSOR_ANCESTRY_POLICY"] is None


def test_inflight_replacement_refuses_both_readers_without_second_factory(fixture, monkeypatch):
    ready, release = threading.Event(), threading.Event()
    barrier = threading.Barrier(3)

    def constructed(implementation):
        ready.set()
        assert release.wait(20)

    children = observe_factory(fixture, monkeypatch, constructed)

    def lookup():
        barrier.wait(timeout=20)
        return fixture.publication.successor_ancestry_limit()

    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(lookup) for _ in range(2)]
        barrier.wait(timeout=20)
        try:
            assert ready.wait(20)
            assert len(children) == 1
            assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is None
            drift(fixture, monkeypatch, "replacement")
        finally:
            release.set()
        for future in futures:
            with pytest.raises(ValueError, match="executed producer/dependency changed"):
                future.result(timeout=30)
    assert len(children) == 1
    assert fixture.state["_SUCCESSOR_ANCESTRY_POLICY"] is None


def test_borrowed_endpoint_and_claw_lock_manager_remain_live(fixture, tmp_path):
    direct = fixture.publication.successor_native()
    endpoint = direct.Endpoint
    claw_root = tmp_path / "claw"
    initialize(claw_root)
    for name in (*api.Claw.PATHS.values(), "uv.lock", "pyproject.toml"):
        target = claw_root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(CLAW / name, target)
    commit(claw_root)
    claw = api.Claw(claw_root)
    manager_class = claw.modules["locks"].LockManager
    manager = manager_class({"locks_dir": str(tmp_path / "isolated-locks")})
    hints = get_type_hints(manager_class.__init__)
    # The real caller may keep a manager obtained from a temporary Claw wrapper.
    borrowed = (
        api.Claw(claw_root)
        .modules["locks"]
        .LockManager({"locks_dir": str(tmp_path / "borrowed-locks")})
    )
    borrowed_class = type(borrowed)
    borrowed_module = inspect.getmodule(borrowed_class)
    assert borrowed_class is not manager_class
    borrowed_hints = get_type_hints(borrowed_class.__init__)

    def check_borrowed_owner():
        # Recover its authentic import owner only for this check, not across lookups.
        imported = borrowed_module.__dict__["__builtins__"]["__import__"]
        owner = inspect.getclosurevars(imported).nonlocals["self"]
        assert owner.modules["locks"] is borrowed_module
        owner.verify()

    owners = {module.__name__: module for module in claw.modules.values()}
    owners.update({module.__name__: module for module in direct._CAPTURE.modules.values()})
    expected = direct.MAX_SUCCESSOR_ANCESTRY
    for _ in range(3):
        assert fixture.publication.successor_ancestry_limit() == expected
        gc.collect()
        assert direct.Endpoint is endpoint
        assert inspect.getmodule(endpoint) is direct
        assert inspect.getmodule(manager_class) is claw.modules["locks"]
        assert Path(inspect.getsourcefile(endpoint)).is_file()
        assert get_type_hints(manager_class.__init__) == hints
        assert manager.check_lock("synthetic-unused") is None
        assert inspect.getmodule(borrowed_class) is borrowed_module
        assert sys.modules[borrowed_class.__module__] is borrowed_module
        assert get_type_hints(borrowed_class.__init__) == borrowed_hints
        assert borrowed.check_lock("synthetic-unused") is None
        check_borrowed_owner()
        assert all(sys.modules.get(name) is module for name, module in owners.items())
        direct._CAPTURE.verify()
        claw.verify()
    assert not manager._leases
    assert not borrowed._leases
