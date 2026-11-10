"""Build and exercise installed runtime resources offline (#1265, #1275).

The source copy keeps setuptools metadata and wheel output out of the checkout.
The fresh isolated interpreter cannot fall back to editable source templates.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import textwrap
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "src/mediaingredientmech"


def test_installed_wheel_renders_resolver_and_validates_frozen_snapshots(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    shutil.copytree(
        PACKAGE, source / "src/mediaingredientmech", ignore=shutil.ignore_patterns("__pycache__")
    )
    for filename in ["pyproject.toml", "README.md"]:
        shutil.copyfile(ROOT / filename, source / filename)
    # setuptools is present in the locked runtime via oaklib. Use the real
    # configured backend directly, without network/build-isolation resolution.
    environment = {key: value for key, value in os.environ.items() if key != "PYTHONPATH"}
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [
            sys.executable,
            "-I",
            "-c",
            "from setuptools.build_meta import build_wheel; build_wheel('dist')",
        ],
        cwd=source,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    wheels = list((source / "dist").glob("*.whl"))
    assert len(wheels) == 1
    installed = tmp_path / "installed"
    with zipfile.ZipFile(wheels[0]) as archive:
        names = set(archive.namelist())
        assert "mediaingredientmech/schema/pre_mint_ingredient_snapshot.yaml" not in names
        assert "mediaingredientmech/schema/pre_mint_snapshot_inventory.json" not in names
        archive.extractall(installed)
    probe = textwrap.dedent("""
        import hashlib
        import json
        from pathlib import Path
        import sys

        installed, root = map(Path, sys.argv[1:])
        sys.path.insert(0, str(installed))
        import yaml
        from mediaingredientmech import render_ingredient_pages as render
        from mediaingredientmech import stable_ids
        from mediaingredientmech.validation import historical_snapshots as snapshots
        from mediaingredientmech.validation.write_validated import validate_ingredient

        assert render.TEMPLATES_DIR == installed / "mediaingredientmech/templates"
        assert snapshots.SCHEMA_DIR == installed / "mediaingredientmech/schema/historical"
        env = render.make_env()
        for path in render.TEMPLATES_DIR.rglob("*.j2"):
            env.get_template(path.relative_to(render.TEMPLATES_DIR).as_posix())
        assert Path(stable_ids.__file__).resolve() == installed / "mediaingredientmech/stable_ids.py"
        mints = tuple(stable_ids.Mint(f"MIM:{n:07d}", f"Example {n}", "2026-11-08")
                      for n in (1, 2, 3))

        def lifecycle_context(events=()):
            registry = stable_ids.Registry(mints, events)
            resolution = stable_ids.inspect_ids(registry)["MIM:0000001"]
            by_id = {event.mim_id: event for event in registry.events}
            return dict(resolution=resolution,
                        resolution_href=f"../{resolution.at_id.replace(':', '_')}/",
                        successors=[(identifier, f"../{identifier.replace(':', '_')}/")
                                    for identifier in resolution.successors],
                        reason=by_id[resolution.at_id].reason if resolution.status != "active" else "")

        canonical = "https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_0000001"
        context = dict(mim_id="MIM:0000001", label="Example", canonical_url=canonical,
                       detail_href="../../records/mapped/Example.html", status="active")
        context.update(lifecycle_context())
        active = env.get_template("stable_resolver.html.j2").render(**context)
        assert canonical in active
        assert "url=../../records/mapped/Example.html" in active
        context.update(status="merged", replacement="MIM:0000002", target="MIM:0000002",
                       replacement_href="../MIM_0000002/", target_href="../MIM_0000002/")
        context.update(lifecycle_context((stable_ids.Lifecycle(
            "MIM:0000001", "merged", "MIM:0000002", "2026-11-08T01:00:00Z", "Merged duplicate"),)))
        terminal = env.get_template("stable_resolver.html.j2").render(**context)
        assert "MIM:0000002" in terminal and "http-equiv" not in terminal
        split_context = dict(context, status="split", replacement="MIM:0000002|MIM:0000003",
                             target=None, target_href="", replacement_href="", detail_href="")
        split_context.update(lifecycle_context((stable_ids.Lifecycle(
            "MIM:0000001", "split", "MIM:0000002|MIM:0000003", "2026-11-08T01:00:00Z",
            "Reviewed split"),)))
        split = env.get_template("stable_resolver.html.j2").render(**split_context)
        assert canonical in split and "http-equiv" not in split
        assert 'href="../MIM_0000002/"' in split and 'href="../MIM_0000003/"' in split
        assert "No single successor is selected" in split and "Reviewed split" in split
        assert "Open the current replacement record" not in split
        deprecated_context = dict(context, status="deprecated", replacement="", target=None,
                                  target_href="", replacement_href="", detail_href="")
        deprecated_context.update(lifecycle_context((stable_ids.Lifecycle(
            "MIM:0000001", "deprecated", "", "2026-11-08T01:00:00Z",
            "No justified successor"),)))
        deprecated = env.get_template("stable_resolver.html.j2").render(**deprecated_context)
        assert canonical in deprecated and "http-equiv" not in deprecated
        assert "deprecated without a justified successor" in deprecated
        assert "No justified successor" in deprecated
        assert 'href="../MIM_0000002/"' not in deprecated
        assert 'href="../MIM_0000003/"' not in deprecated
        assert "Open the current replacement record" not in deprecated
        detail = env.get_template("ingredient.html.j2").render(
            ingredient=dict(mim_id="MIM:0000001", identifier="CHEBI:1", preferred_term="Example"),
            source_path="fixture.yaml", generated_at="2026-11-08T00:00:00Z", path_up="../")
        assert canonical in detail
        assert (render.TEMPLATES_DIR / "style.css").is_file()
        inventory = json.loads((snapshots.SCHEMA_DIR / "pre_mint_snapshot_inventory.json").read_text())
        for name in inventory["files"]:
            path = root / name
            schema = snapshots.historical_schema(path, root)
            assert validate_ingredient(yaml.safe_load(path.read_text()), schema_path=schema) == []
        for name, digest in [("pre_mint_ingredient_snapshot.yaml", inventory["schema_sha256"]),
                             ("mech_shared.yaml", inventory["shared_schema_sha256"])]:
            assert hashlib.sha256((snapshots.SCHEMA_DIR / name).read_bytes()).hexdigest() == digest
        print(json.dumps({"snapshots": len(inventory["files"]), "active_and_terminal_rendered": True}))
        """)
    result = subprocess.run(
        [sys.executable, "-I", "-c", probe, str(installed), str(ROOT)],
        cwd=tmp_path,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert json.loads(result.stdout) == {"snapshots": 5, "active_and_terminal_rendered": True}
