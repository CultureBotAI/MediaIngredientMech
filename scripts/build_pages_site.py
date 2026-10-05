#!/usr/bin/env python3
"""Build/check the public ingredient site from a complete current source checkout."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

import browser_export  # noqa: E402

from mediaingredientmech import render_ingredient_pages as render  # noqa: E402
from mediaingredientmech.schema_site import write_schema_site  # noqa: E402

PACKAGE_ROOT = Path(render.__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_files(repo: Path) -> list[Path]:
    return sorted(
        p
        for status in ("mapped", "unmapped")
        for p in (repo / "data" / "ingredients" / status).glob("*.yaml")
    )


def build_inputs(repo: Path) -> dict[str, str]:
    files = {
        "builder": Path(__file__),
        "renderer": Path(render.__file__),
        "exporter": Path(browser_export.__file__),
    }
    files.update(
        {
            "template/" + p.relative_to(render.TEMPLATES_DIR).as_posix(): p
            for p in render.TEMPLATES_DIR.rglob("*")
            if p.is_file()
        }
    )
    # Local renderer/exporter dependencies affect scientific labels and URLs too.
    # Exclude interpreter caches, which are unrelated to the generated content.
    files.update(
        {
            "package/" + p.relative_to(PACKAGE_ROOT).as_posix(): p
            for p in PACKAGE_ROOT.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
        }
    )
    files.update(
        {
            "docs/" + name: repo / "docs" / name
            for name in (
                "index.html",
                "browser.html",
                "theme-toggle.js",
                "map-record-navigation.js",
                "ingredient_umap.html",
                "ingredient_graph.html",
            )
        }
    )
    return {name: digest(path) for name, path in sorted(files.items())}


def check_site(repo: Path, output: Path) -> None:
    """Refuse missing pages, stale sources/templates, and incomplete catalog links."""
    ingredient_root = repo / "data" / "ingredients"
    sources = {p.relative_to(ingredient_root).as_posix(): p for p in source_files(repo)}
    if not sources:
        raise ValueError("No ingredient sources found")
    receipt = json.loads((output / "records" / "build.json").read_text())
    if receipt["build_inputs"] != build_inputs(repo):
        raise ValueError("Site templates or build inputs are stale")
    catalog = json.loads((output / "data" / "ingredients.json").read_text())
    catalog_rows = catalog["ingredients"]
    if len(catalog_rows) != len(sources) or {r["source_file"] for r in catalog_rows} != set(
        sources
    ):
        raise ValueError("Catalog does not cover every ingredient source exactly once")
    records = receipt["records"]
    if set(records) != set(sources):
        raise ValueError("Record manifest does not cover every ingredient source")
    expected_pages = set()
    for row in catalog_rows:
        source = sources[row["source_file"]]
        expected = f"records/ingredient/{render.slug_for({}, source)}.html"
        if row.get("detail_page") != expected or expected in expected_pages:
            raise ValueError(f"Non-unique or incorrect detail URL: {row['source_file']}")
        expected_pages.add(expected)
        record = records[row["source_file"]]
        if record != {
            "source_sha256": digest(source),
            "page": expected,
            "page_sha256": digest(output / expected),
        }:
            raise ValueError(f"Missing or stale ingredient page: {row['source_file']}")
    actual_pages = {
        p.relative_to(output).as_posix()
        for p in (output / "records" / "ingredient").rglob("*.html")
    }
    if actual_pages != expected_pages:
        raise ValueError("Missing or orphaned ingredient pages")
    required_assets = {
        "data/ingredients.json",
        "records/index.html",
        "records/style.css",
        "index.html",
        "browser.html",
        "theme-toggle.js",
    }
    required_assets.update(
        p.relative_to(output).as_posix() for p in (output / "schema").glob("*.html")
    )
    required_assets.add("map-record-navigation.js")
    if not (output / "schema" / "index.html").exists():
        raise ValueError("Missing rendered schema reference")
    if set(receipt["assets"]) != required_assets:
        raise ValueError("Incomplete site assets")
    for name, checksum in receipt["assets"].items():
        if digest(output / name) != checksum:
            raise ValueError(f"Changed generated site asset: {name}")


def build_site(repo: Path, output: Path) -> int:
    """Stage, render all records, validate, then promote a new output directory."""
    if output.exists():
        raise ValueError(f"Output already exists: {output}; choose a fresh build directory")
    files = source_files(repo)
    if not files:
        raise ValueError("No ingredient sources found")
    urls = [render.slug_for({}, p) for p in files]
    if len(set(urls)) != len(urls):
        raise ValueError("Ingredient source names collide after slug normalization")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mim-site-", dir=output.parent) as temporary:
        stage = Path(temporary) / "site"
        shutil.copytree(repo / "docs", stage)
        # Never carry previously generated record pages forward into a fresh build.
        if (stage / "records").exists():
            raise ValueError("docs/records must not contain generated site output")
        browser_export.export_ingredients_to_json(
            repo / "data" / "ingredients", stage / "data" / "ingredients.json"
        )
        env = render.make_env()
        index = stage / "records"
        records = {}
        successful = []
        for source in files:
            status, ingredient, slug = render.render_one(
                env, source, index / "ingredient", force=True
            )
            if status != "rendered":
                raise ValueError(f"Cannot render {source.name}: {status}")
            page = f"records/ingredient/{slug}.html"
            key = source.relative_to(repo / "data" / "ingredients").as_posix()
            records[key] = {
                "source_sha256": digest(source),
                "page": page,
                "page_sha256": digest(stage / page),
            }
            successful.append({"ingredient": ingredient, "slug": slug})
        render.write_index(index, successful)
        shutil.copyfile(render.TEMPLATES_DIR / "style.css", index / "style.css")
        schema_assets = write_schema_site(
            PACKAGE_ROOT / "schema" / "mediaingredientmech.yaml", stage / "schema"
        )
        (stage / ".nojekyll").touch()
        asset_names = (
            "data/ingredients.json",
            "records/index.html",
            "records/style.css",
            "index.html",
            "browser.html",
            "theme-toggle.js",
        )
        receipt = {
            "build_inputs": build_inputs(repo),
            "records": records,
            "assets": {
                name: digest(stage / name)
                for name in (*asset_names, "map-record-navigation.js", *schema_assets)
            },
        }
        (index / "build.json").write_text(json.dumps(receipt, indent=2) + "\n")
        check_site(repo, stage)
        stage.rename(output)
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "site")
    parser.add_argument("--check", type=Path, help="check an existing built artifact")
    args = parser.parse_args()
    try:
        if args.check:
            check_site(ROOT, args.check.resolve())
            print("Ingredient site is complete and current")
        else:
            count = build_site(ROOT, args.output.resolve())
            print(f"Built and verified {count} public ingredient pages")
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f"Site build failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
