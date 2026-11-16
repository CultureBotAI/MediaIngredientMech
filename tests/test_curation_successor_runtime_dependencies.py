"""Installed runtime roots require their own metadata and module provenance (#1448)."""

import base64
import csv
import hashlib
import importlib.metadata
import io
import os
import sys
import venv
from pathlib import Path

import pytest

from mediaingredientmech.curate import curation_successor as successor


def digest(raw):
    return "sha256=" + base64.urlsafe_b64encode(hashlib.sha256(raw).digest()).decode().rstrip("=")


def record(root, info, names):
    stream = io.StringIO()
    writer = csv.writer(stream, lineterminator="\n")
    for name in sorted(set(names) - {str(info / "RECORD")}):
        raw = (root / name).read_bytes()
        writer.writerow([name, digest(raw), len(raw)])
    writer.writerow([str(info / "RECORD"), "", ""])
    (root / info / "RECORD").write_text(stream.getvalue())


def copy_distribution(root, name):
    """Copy two small real distributions as fixture bytes; do not install them."""
    distribution = importlib.metadata.distribution(name)
    names = []
    for entry in distribution.files:
        if entry.is_absolute() or ".." in entry.parts or entry.suffix == ".pyc":
            continue
        source = Path(distribution.locate_file(entry))
        if not source.is_file():
            continue
        target = root / str(entry)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
        names.append(str(entry))
    info = next(Path(name).parent for name in names if name.endswith(".dist-info/METADATA"))
    record(root, info, names)
    return info, names


def synthetic_distribution(root, name, module, *, requires=(), extras=(), python=None):
    """Finite installed metadata inputs for dependency-closure decisions."""
    info = Path(name.replace("-", "_") + "-1.0.dist-info")
    metadata = f"Metadata-Version: 2.4\nName: {name}\nVersion: 1.0\n"
    if python:
        metadata += "Requires-Python: " + python + "\n"
    metadata += "".join("Provides-Extra: " + item + "\n" for item in extras)
    metadata += "".join("Requires-Dist: " + item + "\n" for item in requires)
    files = {
        str(info / "METADATA"): metadata.encode(),
        module + "/__init__.py": b"# A registered fixture module; never imported by selection.\n",
    }
    for name, raw in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    record(root, info, files)
    return info, list(files)


@pytest.fixture
def installed(tmp_path, monkeypatch):
    environment = tmp_path / "runtime"
    venv.EnvBuilder(with_pip=False, symlinks=True).create(environment)
    root = (
        environment
        / "lib"
        / f"python{sys.version_info.major}.{sys.version_info.minor}"
        / "site-packages"
    )
    distributions = {
        name: copy_distribution(root, name) for name in ("python-dotenv", "rfc3339-validator")
    }
    # The selector must reason about registered, not yet imported modules.
    # These are caller inputs; no production selection/verification is replaced.
    for name in list(sys.modules):
        if name == "dotenv" or name.startswith("dotenv.") or name == "rfc3339_validator":
            monkeypatch.delitem(sys.modules, name)
    monkeypatch.syspath_prepend(str(root))
    return root, distributions


def add_requirement(root, distribution, text):
    info, names = distribution
    metadata = root / info / "METADATA"
    raw = metadata.read_text()
    header, separator, description = raw.partition("\n\n")
    metadata.write_text(header + "\nRequires-Dist: " + text + separator + description)
    record(root, info, names)


def test_cross_record_cannot_supply_missing_seed_anchor(installed):
    """Distinguishes F001: every other origin/metadata check remains valid."""
    root, distributions = installed
    anchor = "dotenv/__init__.py"
    owner_info, owner_names = distributions["python-dotenv"]
    borrower_info, borrower_names = distributions["rfc3339-validator"]
    record(root, owner_info, [name for name in owner_names if name != anchor])
    record(root, borrower_info, [*borrower_names, anchor])
    assert (root / anchor).is_file()
    with pytest.raises(ValueError, match="own distribution"):
        successor._runtime_dependencies()
    assert "dotenv" not in sys.modules


def test_own_anchor_and_shared_consistent_record_qualify(installed):
    root, distributions = installed
    info, names = distributions["rfc3339-validator"]
    record(root, info, [*names, "dotenv/__init__.py"])
    result = successor._runtime_dependencies()
    assert result["modules"]["dotenv"] == str(root / "dotenv/__init__.py")
    assert str(root) in result["paths"]
    assert "dotenv" not in sys.modules
    assert any(name.startswith("sphinxcontrib.") for name in result["modules"])


def test_later_extra_revisits_dependency_and_false_marker_stays_unselected(installed):
    root, distributions = installed
    synthetic_distribution(
        root,
        "runtime-probe",
        "runtime_probe",
        extras=("late",),
        requires=(
            'runtime-extra-child==1.0; extra == "late"',
            'runtime-never-installed; python_version < "0"',
        ),
    )
    synthetic_distribution(root, "runtime-extra-child", "runtime_extra_child")
    # LIFO traversal sees the plain requirement first, then the extra.
    add_requirement(root, distributions["python-dotenv"], "runtime-probe[late]==1.0")
    add_requirement(root, distributions["python-dotenv"], "runtime-probe==1.0")
    result = successor._runtime_dependencies()
    assert "runtime_probe" in result["modules"]
    assert "runtime_extra_child" in result["modules"]
    assert "runtime_probe" not in sys.modules and "runtime_extra_child" not in sys.modules


@pytest.mark.parametrize("failure", ["version", "python"])
def test_incompatible_declared_dependency_refuses(installed, failure):
    root, distributions = installed
    synthetic_distribution(
        root, "runtime-probe", "runtime_probe", python=">=99" if failure == "python" else None
    )
    add_requirement(
        root,
        distributions["python-dotenv"],
        "runtime-probe>=2" if failure == "version" else "runtime-probe",
    )
    with pytest.raises(ValueError, match="metadata/version differs|excludes the selected Python"):
        successor._runtime_dependencies()
    assert "runtime_probe" not in sys.modules


@pytest.mark.parametrize("failure", ["missing-record", "metadata", "anchor", "editable"])
def test_installed_metadata_and_origin_refusals(installed, failure):
    root, distributions = installed
    info, names = distributions["python-dotenv"]
    if failure == "missing-record":
        (root / info / "RECORD").unlink()
    elif failure == "metadata":
        with (root / info / "METADATA").open("a") as stream:
            stream.write("\nChanged metadata\n")
    elif failure == "anchor":
        (root / "dotenv/__init__.py").write_text("raise AssertionError('UNEXECUTED_ANCHOR')\n")
    else:
        (root / info / "direct_url.json").write_text('{"dir_info":{"editable":true}}\n')
    with pytest.raises(ValueError, match="no RECORD|METADATA differs|origin differs|editable"):
        successor._runtime_dependencies()
    assert "dotenv" not in sys.modules


def test_arbitrary_project_path_is_not_forwarded(tmp_path, monkeypatch):
    project = tmp_path / "arbitrary-project"
    project.mkdir()
    monkeypatch.syspath_prepend(str(project))
    monkeypatch.setenv("PYTHONPATH", str(project))
    assert str(project) not in successor._runtime_dependencies()["paths"]


@pytest.mark.parametrize("kind", ["project", "loaded"])
def test_shadowed_anchor_refuses_before_import(installed, tmp_path, monkeypatch, kind):
    root, _ = installed
    shadow = tmp_path / "shadow"
    shadow.mkdir()
    (shadow / "dotenv.py").write_text("raise AssertionError('UNEXECUTED_SHADOW')\n")
    if kind == "project":
        monkeypatch.syspath_prepend(str(shadow))
    else:
        import types

        module = types.ModuleType("dotenv")
        module.__file__ = str(shadow / "dotenv.py")
        monkeypatch.setitem(sys.modules, "dotenv", module)
    with pytest.raises(ValueError, match="shadowed|loaded dependency"):
        successor._runtime_dependencies()


@pytest.mark.parametrize("selected", ["METADATA", "RECORD", "anchor", "root"])
def test_runtime_snapshot_refuses_same_byte_replacement(installed, selected):
    root, distributions = installed
    snapshot = successor._runtime_dependencies()
    info, _ = distributions["python-dotenv"]
    if selected == "root":
        saved = root.with_name("original-site-packages")
        root.rename(saved)
        root.mkdir()
        for path in saved.iterdir():
            path.rename(root / path.name)
    else:
        path = root / ("dotenv/__init__.py" if selected == "anchor" else str(info / selected))
        replacement = root.parent / "same-bytes"
        replacement.write_bytes(path.read_bytes())
        replacement.replace(path)
    with pytest.raises(ValueError, match="runtime.*changed|parent changed|file changed"):
        successor._runtime_check(snapshot)


def test_runtime_package_manager_hardlink_remains_allowed(installed):
    root, _ = installed
    path = root / "dotenv/__init__.py"
    os.link(path, root.parent / "package-cache-link")
    result = successor._runtime_dependencies()
    assert result["modules"]["dotenv"] == str(path)


def test_selected_dependency_refuses_wrong_base_environment(installed):
    root, _ = installed
    config = root.parents[2] / "pyvenv.cfg"
    lines = config.read_text().splitlines()
    assert sum(line.startswith("home =") for line in lines) == 1
    config.write_text(
        "\n".join(
            (
                "home = " + str(root.parents[2] / "unselected-interpreter")
                if line.startswith("home =")
                else line
            )
            for line in lines
        )
        + "\n"
    )
    with pytest.raises(ValueError, match="not an environment of the selected interpreter"):
        successor._runtime_dependencies()
    assert "dotenv" not in sys.modules


def test_requirement_parser_project_shadow_refuses_before_first_import(tmp_path, monkeypatch):
    shadow = tmp_path / "parser-shadow"
    package = shadow / "packaging"
    package.mkdir(parents=True)
    marker = tmp_path / "PARSER_SHADOW_EXECUTED"
    (package / "__init__.py").write_text(
        f"from pathlib import Path\nPath({str(marker)!r}).write_text('unexpected parser import')\n"
    )
    # Model the selector's first import; no finder, metadata reader or guard is
    # replaced. The real package metadata remains in its installed library.
    for name in list(sys.modules):
        if name == "packaging" or name.startswith("packaging."):
            monkeypatch.delitem(sys.modules, name)
    monkeypatch.syspath_prepend(str(shadow))
    with pytest.raises(ValueError, match="requirement parser is shadowed"):
        successor._runtime_dependencies()
    assert "packaging" not in sys.modules
    assert not marker.exists()
