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
from mediaingredientmech.stable_ids import (  # noqa: E402
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    load_registry,
    resolve_id,
    resolver_url,
    validate_records,
)
from mediaingredientmech.utils.yaml_handler import load_yaml  # noqa: E402

PACKAGE_ROOT = Path(render.__file__).resolve().parent
VISUALIZATION_ASSETS = ("data/ingredient_umap.json", "data/ingredient_graph.json")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_files(repo: Path) -> list[Path]:
    return sorted(
        p
        for status in ("mapped", "unmapped")
        for p in (repo / "data" / "ingredients" / status).glob("*.yaml")
    )


def resolver_documents(repo: Path) -> dict[str, str]:
    """Render one stable route per registered ID from the current corpus.

    Source paths are looked up by immutable ID at every build. The registry's
    original label and append-only lifecycle remain visible for retired IDs.
    Existing filename routes are separately rendered without renaming them.
    """
    registry = load_registry(repo)
    records = {path.relative_to(repo).as_posix(): load_yaml(path) for path in source_files(repo)}
    validate_records(registry, records)
    by_id = {record["mim_id"]: (repo / path, record) for path, record in records.items()}
    states = registry.states
    template = render.make_env().get_template("stable_resolver.html.j2")
    documents = {}
    for entry in registry.entries:
        status, replacement = states[entry.mim_id]
        target = entry.mim_id if status == "active" else resolve_id(registry, entry.mim_id)
        source, record = by_id[target]
        page = f"ingredient/{entry.mim_id.replace(':', '_')}/index.html"
        documents[page] = template.render(
            mim_id=entry.mim_id,
            label=record["preferred_term"] if status == "active" else entry.label_at_minting,
            status=status,
            canonical_url=resolver_url(entry.mim_id),
            detail_href=f"../../records/ingredient/{render.slug_for(record, source)}.html",
            replacement=replacement,
            replacement_href=f"../{replacement.replace(':', '_')}/" if replacement else "",
            target=target,
            target_href=f"../{target.replace(':', '_')}/",
        )
    return documents


def build_inputs(repo: Path) -> dict[str, str]:
    files = {
        "builder": Path(__file__),
        "renderer": Path(render.__file__),
        "exporter": Path(browser_export.__file__),
        REGISTRY_PATH.as_posix(): repo / REGISTRY_PATH,
        LIFECYCLE_PATH.as_posix(): repo / LIFECYCLE_PATH,
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
                *VISUALIZATION_ASSETS,
            )
        }
    )
    for optional_doc in ("404.html", "text_map.html"):
        opt_path = repo / "docs" / optional_doc
        if opt_path.exists():
            files["docs/" + optional_doc] = opt_path
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
    expected_resolvers = resolver_documents(repo)
    if receipt.get("resolvers") != {
        page: hashlib.sha256(html.encode("utf-8")).hexdigest()
        for page, html in expected_resolvers.items()
    }:
        raise ValueError("Stable MIM resolver manifest is missing or stale")
    actual_resolvers = {
        path.relative_to(output).as_posix()
        for path in (output / "ingredient").rglob("*.html")
    }
    if actual_resolvers != set(expected_resolvers):
        raise ValueError("Missing or orphaned stable MIM resolver pages")
    for page, checksum in receipt["resolvers"].items():
        if digest(output / page) != checksum:
            raise ValueError(f"Changed stable MIM resolver page: {page}")
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
        ingredient = load_yaml(source)
        if row.get("record_id") != ingredient["mim_id"] or row.get("stable_url") != resolver_url(ingredient["mim_id"]):
            raise ValueError(f"Incorrect stable MIM identity: {row['source_file']}")
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
        *VISUALIZATION_ASSETS,
        "records/index.html",
        "records/style.css",
        "index.html",
        "browser.html",
        "theme-toggle.js",
    }
    for optional_doc in ("404.html", "text_map.html"):
        if (repo / "docs" / optional_doc).exists():
            required_assets.add(optional_doc)
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
    resolvers = resolver_documents(repo)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mim-site-", dir=output.parent) as temporary:
        stage = Path(temporary) / "site"
        shutil.copytree(repo / "docs", stage)
        # Never carry previously generated record pages forward into a fresh build.
        if (stage / "records").exists():
            raise ValueError("docs/records must not contain generated site output")
        if (stage / "ingredient").exists():
            raise ValueError("docs/ingredient must not contain generated stable resolver output")
        for page, html in resolvers.items():
            target = stage / page
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(html, encoding="utf-8")
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
        optional_assets = tuple(
            name for name in ("404.html", "text_map.html") if (repo / "docs" / name).exists()
        )
        asset_names = (
            "data/ingredients.json",
            *VISUALIZATION_ASSETS,
            "records/index.html",
            "records/style.css",
            "index.html",
            "browser.html",
            "theme-toggle.js",
            *optional_assets,
        )
        receipt = {
            "build_inputs": build_inputs(repo),
            "records": records,
            "resolvers": {page: digest(stage / page) for page in resolvers},
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
