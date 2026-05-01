"""Render MIM ingredient YAMLs to per-record HTML pages.

Walks `data/ingredients/{mapped,unmapped}/*.yaml`, applies the Jinja2
template at `src/mediaingredientmech/templates/ingredient.html.j2`,
writes output to `pages/ingredient/<slug>.html`.

Idempotent: skips records whose YAML mtime is older than the existing
HTML's mtime. Pass --force to regenerate.

Phase 5 of the dismech-pattern port; see
../culturebotai-claw/docs/proposals/phase5_mkdocs_material_and_browser_parity.md
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INGREDIENTS = REPO_ROOT / "data" / "ingredients"
DEFAULT_OUT_DIR = REPO_ROOT / "pages" / "ingredient"
DEFAULT_INDEX_DIR = REPO_ROOT / "pages"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"


_CURIE_RESOLVERS = {
    "CHEBI": "https://www.ebi.ac.uk/ols4/ontologies/chebi/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_{}",
    "FOODON": "https://www.ebi.ac.uk/ols4/ontologies/foodon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_{}",
    "ENVO": "https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_{}",
    "UBERON": "https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_{}",
    "NCIT": "https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCIT_{}",
    "cas": "https://commonchemistry.cas.org/detail?cas_rn={}",
    "kgmicrobe.compound": "#",  # placeholder primary; no resolver
    "MIM": None,
    "MediaIngredientMech": None,
}


def curie_to_url(curie: str | None) -> str:
    if not curie or ":" not in curie:
        return "#"
    prefix, local = curie.split(":", 1)
    template = _CURIE_RESOLVERS.get(prefix)
    if not template:
        return "#"
    return template.format(local)


_SLUG_RE = re.compile(r"[^A-Za-z0-9._-]+")


def slug_for(ingredient: dict, source_path: Path) -> str:
    """Slug includes the parent directory (mapped / unmapped) so that
    two YAMLs with the same stem in different subdirs don't collide
    (e.g. mapped/Glucose.yaml + unmapped/Glucose.yaml both exist)."""
    parent = source_path.parent.name
    base = _SLUG_RE.sub("_", source_path.stem)
    if parent in ("mapped", "unmapped"):
        return f"{parent}/{base}"
    return base


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["curie_to_url"] = curie_to_url
    return env


def render_one(env: Environment, source_path: Path, out_dir: Path,
               force: bool = False) -> tuple[str, dict | None, str]:
    try:
        with open(source_path) as f:
            ingredient = yaml.safe_load(f) or {}
    except Exception as e:
        return f"error:{type(e).__name__}", None, ""
    if not isinstance(ingredient, dict) or not ingredient.get("identifier"):
        return "error:no-identifier", None, ""
    slug = slug_for(ingredient, source_path)
    out_path = out_dir / f"{slug}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if not force and out_path.exists():
        if out_path.stat().st_mtime >= source_path.stat().st_mtime:
            return "skipped", ingredient, slug
    template = env.get_template("ingredient.html.j2")
    # depth = number of path segments from out_dir (e.g. mapped/Glucose
    # is depth 2; bare Foo is depth 1). Used to compute relative
    # breadcrumb links.
    depth = len(slug.split("/"))
    html = template.render(
        ingredient=ingredient,
        source_path=str(source_path.relative_to(REPO_ROOT)),
        generated_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        path_up=("../" * depth),  # path back to pages/ root
    )
    out_path.write_text(html)
    return "rendered", ingredient, slug


# ---------- index ----------

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MIM — Ingredient index</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<h1>MIM — Ingredient index</h1>
<p class="muted">{count:,} ingredients, generated {generated_at}.</p>
</header>
{by_prefix}
</body>
</html>
"""


def _section(prefix: str, items: list[tuple[str, str, str]]) -> str:
    rows = "".join(
        f'<li><a href="ingredient/{slug}.html">{name}</a> '
        f'<span class="muted">— <code>{ident}</code></span></li>'
        for (ident, slug, name) in sorted(items, key=lambda x: x[2].lower())
    )
    return (f'<section><h2>{prefix} '
            f'<small class="muted">({len(items)})</small></h2>'
            f'<ul class="medium-index">{rows}</ul></section>')


def write_index(out_dir: Path, all_records: list[dict]) -> None:
    by_prefix: dict[str, list[tuple[str, str, str]]] = {}
    for r in all_records:
        ident = r["ingredient"].get("identifier") or ""
        prefix = ident.split(":", 1)[0] if ":" in ident else "(other)"
        by_prefix.setdefault(prefix, []).append(
            (ident, r["slug"], r["ingredient"].get("preferred_term") or r["slug"]))
    sections = "\n".join(
        _section(p, items) for p, items in sorted(by_prefix.items())
    )
    rows_total = sum(len(v) for v in by_prefix.values())
    html = INDEX_TEMPLATE.format(
        count=rows_total,
        generated_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        by_prefix=sections,
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ingredients-dir", type=Path, default=DEFAULT_INGREDIENTS,
                    help="root containing mapped/ and unmapped/ subdirs")
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if not args.ingredients_dir.is_dir():
        print(f"ingredients dir not found: {args.ingredients_dir}", file=sys.stderr)
        return 2
    args.out_dir.mkdir(parents=True, exist_ok=True)

    env = make_env()
    files = sorted(args.ingredients_dir.rglob("*.yaml"))
    if args.limit:
        files = files[: args.limit]
    print(f"Rendering up to {len(files)} ingredient pages → {args.out_dir}")

    rendered = skipped = errors = 0
    successful: list[dict] = []
    for path in files:
        status, ingredient, slug = render_one(
            env, path, args.out_dir, force=args.force)
        if status == "rendered":
            rendered += 1
        elif status == "skipped":
            skipped += 1
        else:
            errors += 1
            if errors <= 5:
                print(f"  {path.name}: {status}", file=sys.stderr)
        if ingredient and slug:
            successful.append({"ingredient": ingredient, "slug": slug})

    print(f"  rendered: {rendered}")
    print(f"  skipped:  {skipped}")
    print(f"  errors:   {errors}")

    print("Writing index...")
    write_index(args.index_dir, successful)
    print(f"  → {args.index_dir / 'index.html'}")

    style_src = TEMPLATES_DIR / "style.css"
    if style_src.exists():
        (args.index_dir / "style.css").write_bytes(style_src.read_bytes())

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
