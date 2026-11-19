#!/usr/bin/env python3
"""Build/check the public ingredient site from a complete current source checkout."""

from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

import browser_export  # noqa: E402

from mediaingredientmech import render_ingredient_pages as render  # noqa: E402
from mediaingredientmech import records_export  # noqa: E402
from mediaingredientmech.schema_site import write_schema_site  # noqa: E402

PACKAGE_ROOT = Path(render.__file__).resolve().parent
# docs/ pages published when present; text-map-records.js serves text_map.html.
OPTIONAL_DOCS = ("404.html", "text_map.html", "text-map-records.js")


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
    for optional_doc in OPTIONAL_DOCS:
        opt_path = repo / "docs" / optional_doc
        if opt_path.exists():
            files["docs/" + optional_doc] = opt_path
    for name in DISCUSSION_FILES:
        if (repo / name).exists():
            files[name] = repo / name
    return {name: digest(path) for name, path in sorted(files.items())}


# The shared discussion browser that `just gen-discussions-data` writes from the
# records (claw's kg_microbe_discussions). Published where it is committed.
DISCUSSION_FILES = ("app/discussions/index.html", "app/discussions/data.js")
DISCUSSION_NAV = '<nav aria-label="Project navigation">'


def publish_discussions(repo: Path, stage: Path, pages: dict[str, set[str]]) -> list[str]:
    """Publish the discussion index with MIM's way back and licence added.

    The page is claw's template, regenerated verbatim by the recipe, so MIM's
    links and footer are added here, at anchors the build refuses to guess.
    `pages` maps each built record page to the discussion ids its record
    carries; an index whose ids or record links disagree with it is stale.
    """
    if not all((repo / name).exists() for name in DISCUSSION_FILES):
        return []
    data = (repo / "app/discussions/data.js").read_text(encoding="utf-8")
    found = re.search(r"window\.searchData = (\[.*?\]);\n", data, re.DOTALL)
    if not found:
        raise ValueError("app/discussions/data.js has no window.searchData list")
    listed: dict[str, set[str]] = {}
    for entry in json.loads(found.group(1)):
        target = posixpath.normpath(
            posixpath.join("app/discussions", entry["page_url"].split("#", 1)[0])
        )
        listed.setdefault(target, set()).add(entry["discussion_id"])
    if listed != {page: ids for page, ids in pages.items() if ids}:
        raise ValueError(
            "app/discussions/data.js does not match the records' discussions or pages; "
            "run `just gen-discussions-data`"
        )
    html = (repo / "app/discussions/index.html").read_text(encoding="utf-8")
    if html.count(DISCUSSION_NAV) != 1 or html.count("</body>") != 1:
        raise ValueError("app/discussions/index.html no longer has the anchors MIM extends")
    html = html.replace(
        DISCUSSION_NAV,
        DISCUSSION_NAV + '<a href="../../index.html">MediaIngredientMech</a> &middot; '
        '<a href="../../browser.html">Browse ingredients</a> &middot; ',
    ).replace(
        "</body>",
        '<footer style="max-width:1200px;margin:2rem auto;padding:1rem 1.25rem;'
        'border-top:1px solid var(--line);color:var(--muted);font-size:.85rem">'
        f"<p>{render.LICENCE_HTML}</p></footer>\n</body>",
    )
    target = stage / "app" / "discussions"
    target.mkdir(parents=True)
    (target / "index.html").write_text(html, encoding="utf-8")
    shutil.copyfile(repo / "app/discussions/data.js", target / "data.js")
    return list(DISCUSSION_FILES)


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
    for optional_doc in OPTIONAL_DOCS:
        if (repo / "docs" / optional_doc).exists():
            required_assets.add(optional_doc)
    required_assets.update(
        p.relative_to(output).as_posix() for p in (output / "schema").glob("*.html")
    )
    required_assets.add("map-record-navigation.js")
    required_assets.update(
        f"{records_export.DOWNLOADS_DIR}/{name}"
        for name in (records_export.EXPORT_NAME, records_export.MANIFEST_NAME)
    )
    if all((repo / name).exists() for name in DISCUSSION_FILES):
        required_assets.update(DISCUSSION_FILES)
    if not (output / "schema" / "index.html").exists():
        raise ValueError("Missing rendered schema reference")
    if set(receipt["assets"]) != required_assets:
        raise ValueError("Incomplete site assets")
    for name, checksum in receipt["assets"].items():
        if digest(output / name) != checksum:
            raise ValueError(f"Changed generated site asset: {name}")
    records_export.check_records_export(output, set(sources))


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
        discussions: dict[str, set[str]] = {}
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
            discussions[page] = {
                str(item.get("discussion_id", ""))
                for item in (ingredient or {}).get("discussions") or []
                if isinstance(item, dict)
            }
        render.write_index(index, successful)
        shutil.copyfile(render.TEMPLATES_DIR / "style.css", index / "style.css")
        schema_assets = write_schema_site(
            PACKAGE_ROOT / "schema" / "mediaingredientmech.yaml", stage / "schema"
        )
        # Complete records for bulk download: built here at deploy time and
        # receipted below, never committed (docs/index.html links them).
        download_assets = records_export.write_records_export(
            repo / "data" / "ingredients", files, stage
        )
        discussion_assets = publish_discussions(repo, stage, discussions)
        (stage / ".nojekyll").touch()
        optional_assets = tuple(
            name for name in OPTIONAL_DOCS if (repo / "docs" / name).exists()
        )
        asset_names = (
            "data/ingredients.json",
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
            "assets": {
                name: digest(stage / name)
                for name in (
                    *asset_names,
                    "map-record-navigation.js",
                    *schema_assets,
                    *download_assets,
                    *discussion_assets,
                )
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
