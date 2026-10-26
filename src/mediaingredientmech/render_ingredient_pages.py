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
from functools import lru_cache
from html import escape
from pathlib import Path
from urllib.parse import quote, urlencode

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.micro_source import source_term

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INGREDIENTS = REPO_ROOT / "data" / "ingredients"
DEFAULT_OUT_DIR = REPO_ROOT / "pages" / "ingredient"
DEFAULT_INDEX_DIR = REPO_ROOT / "pages"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema" / "mediaingredientmech.yaml"

GITHUB_REPO = "https://github.com/CultureBotAI/MediaIngredientMech"
SITE_ROOT = "https://culturebotai.github.io/MediaIngredientMech/"

# Worded from the repository's own LICENSE, which scopes LICENSE-DATA and
# LICENSE-CODE; every page type carries this line, the hand-written docs/
# pages included (tests/test_unified_site_features.py holds them to it).
LICENCE_HTML = Markup(
    'Project data: <a href="{repo}/blob/main/LICENSE-DATA">CC BY 4.0</a>. '
    'Code: <a href="{repo}/blob/main/LICENSE-CODE">BSD-3-Clause</a>. '
    "Third-party source material keeps its own terms "
    '(<a href="{repo}/blob/main/LICENSE">licence scope</a>).'
).format(repo=GITHUB_REPO)

# Sibling searches a record page offers, by verified route: each loads with
# HTTP 200 and restores ?q= (fleet route table, 2026-10-25). A label search is
# kept only where the sibling answers ingredient names. For 30 randomly drawn
# preferred terms, CultureMech found recipes for every term whose record
# occurs in media; PathwayMech matched 0, CMMMech 1 and NaturalProductMech 4,
# so those three searches were dropped rather than left as dead ends.
SIBLING_SEARCH = {
    "CultureMech": "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
}


_CURIE_RESOLVERS = {
    "CHEBI": "https://www.ebi.ac.uk/ols4/ontologies/chebi/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_{}",
    "FOODON": "https://www.ebi.ac.uk/ols4/ontologies/foodon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_{}",
    "ENVO": "https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_{}",
    "UBERON": "https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_{}",
    "NCIT": "https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCIT_{}",
    "MICRO": "https://www.ebi.ac.uk/ols4/ontologies/micro/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMICRO_{}",
    "cas": "https://commonchemistry.cas.org/detail?cas_rn={}",
    "mesh": "https://meshb.nlm.nih.gov/record/ui?ui={}",
    "MESH": "https://meshb.nlm.nih.gov/record/ui?ui={}",
    "BTO": "https://www.ebi.ac.uk/ols4/ontologies/bto/terms?obo_id=BTO:{}",
    "NCBITaxon": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={}",
    "MIM": None,
    "MediaIngredientMech": None,
}


def curie_to_url(curie: str | None) -> str:
    if not curie or ":" not in curie:
        return ""
    prefix, local = curie.split(":", 1)
    if prefix == "MICRO" and (term := source_term(curie)):
        return "https://www.ebi.ac.uk/ols4/ontologies/micro/classes/" + quote(
            quote(term.iri, safe=""), safe=""
        )
    template = _CURIE_RESOLVERS.get(prefix)
    if not template:
        return ""
    return template.format(quote(local, safe=""))


# A URL or DOI ends at whitespace, a tag bracket or a double quote; then
# _trim_reference() ends it at a closer it never opened, so the link text of the
# Markdown "[10.1/x](https://doi.org/10.1/x)" does not run into its target.
_REFERENCE = re.compile(
    r'https?://[^\s<>"]+|(?:doi:|DOI:)?10\.\d{4,9}/[^\s<>"]+'
    r"|(?:[A-Za-z][A-Za-z0-9_.]*):[A-Za-z0-9._-]+"
)


def reference_url(value: str) -> str:
    if value.startswith(("https://", "http://")):
        return value
    if re.fullmatch(r"CultureMech:\d{6}", value):
        return (
            "https://culturebotai.github.io/CultureMech/pages/normalized/"
            + value.split(":")[1]
            + ".html"
        )
    if value.upper().startswith("PMID:") and value[5:].isdigit():
        return "https://pubmed.ncbi.nlm.nih.gov/" + value[5:] + "/"
    doi = re.sub(r"(?i)^doi:", "", value)
    if re.match(r"^10\.\d{4,9}/", doi):
        return "https://doi.org/" + quote(doi, safe="/():;._-")
    return curie_to_url(value)


_CLOSERS = {")": "(", "]": "[", "}": "{"}
_OPENERS = {opener: closer for closer, opener in _CLOSERS.items()}


def _trim_reference(token: str) -> str:
    """End a token at its first unopened closer, then drop trailing punctuation and marks.

    A URL or DOI runs to the next space, so "(doi:10.1/x)" would otherwise link
    "10.1/x)" and 404 (#889), "(https://a/x)-(https://b/y)" would become one
    link, and "**10.1/x**" or "`10.1/x`" would carry emphasis or code marks into
    the target. A closer whose opener is inside the token, as in a
    Wikipedia-style "Foo_(bar)" URL, belongs to it and is kept.
    """
    opened = dict.fromkeys(_CLOSERS, 0)
    for index, char in enumerate(token):
        if char in _OPENERS:
            opened[_OPENERS[char]] += 1
        elif char in _CLOSERS:
            if not opened[char]:
                token = token[:index]
                break
            opened[char] -= 1
    return token.rstrip(".,;:!?'\"*`")


def linked_text(value: object) -> Markup:
    text = str(value)
    parts = []
    offset = position = 0
    # search() from the end of each linked token, not finditer(): a token cut
    # short leaves text where the next reference can start.
    while match := _REFERENCE.search(text, position):
        candidate = _trim_reference(match.group())
        if not candidate:
            position = match.start() + 1
            continue
        parts.append(escape(text[offset : match.start()]))
        url = reference_url(candidate)
        parts.append(
            f'<a href="{escape(url, quote=True)}" rel="noreferrer">{escape(candidate)}</a>'
            if url
            else escape(candidate)
        )
        offset = position = match.start() + len(candidate)
    parts.append(escape(text[offset:]))
    return Markup("".join(parts))


def _field_value(key: object, value: object) -> Markup:
    # A pmid slot holds a bare PubMed number, which has no reference shape for
    # linked_text to find; its key says what it is (#888).
    if str(key).lower() == "pmid":
        number = str(value).strip()
        if re.fullmatch(r"\d{1,9}", number):
            return Markup(
                '<a href="https://pubmed.ncbi.nlm.nih.gov/{0}/" rel="noreferrer">{0}</a>'
            ).format(number)
    return structured_value(value)


def structured_value(value: object) -> Markup:
    """Render curated structures without Python repr or lost evidence fields."""
    if isinstance(value, dict):
        return Markup(
            '<dl class="kv">'
            + "".join(
                "<dt>"
                + escape(str(k).replace("_", " ").capitalize())
                + "</dt><dd>"
                + str(_field_value(k, v))
                + "</dd>"
                for k, v in value.items()
                if v is not None
            )
            + "</dl>"
        )
    if isinstance(value, list):
        return Markup(
            "<ul>" + "".join("<li>" + str(structured_value(v)) + "</li>" for v in value) + "</ul>"
        )
    return linked_text(value)


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


@lru_cache(maxsize=1)
def enum_meanings() -> dict[str, dict[str, str]]:
    """The schema's own description of each mapping status and quality value.

    Record pages explain a status by quoting these rather than restating what
    a status means, so the explanation cannot drift from the definition.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(SCHEMA_PATH))
    return {
        name: {
            value: (permissible.description or "").strip()
            for value, permissible in (view.get_enum(name).permissible_values or {}).items()
        }
        for name in ("MappingStatusEnum", "MappingQualityEnum")
    }


# Quality values whose schema description asserts human review ("human-verified",
# "Manually curated by expert"). A record page never quotes those: curation
# events name processes and agents rather than people, so no record's history
# can show that a human reviewed it.
HUMAN_REVIEW_QUALITIES = frozenset({"LLM_ASSISTED", "MANUAL_CURATION"})


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["curie_to_url"] = curie_to_url
    env.globals["licence_html"] = LICENCE_HTML
    env.globals["sibling_search"] = SIBLING_SEARCH
    meanings = enum_meanings()
    env.globals["status_meanings"] = meanings["MappingStatusEnum"]
    env.globals["quality_meanings"] = {
        value: text
        for value, text in meanings["MappingQualityEnum"].items()
        if value not in HUMAN_REVIEW_QUALITIES
    }
    env.filters["linked_text"] = linked_text
    env.filters["structured"] = structured_value
    return env


def source_links(source_path: Path, slug: str) -> dict[str, str]:
    """GitHub routes for one record: its YAML, raw file, editor and a prefilled issue.

    The issue follows the fleet's template and names the record by its stable
    `MIM:` id, because identifiers are shared between records.
    """
    path = source_path.relative_to(REPO_ROOT).as_posix()
    record_id = mim_curie_for_stem(source_path.stem)
    issue = urlencode(
        {
            "title": f"Problem with {record_id}",
            "body": f"{SITE_ROOT}records/ingredient/{slug}.html",
        },
        quote_via=quote,
    )
    return {
        "source_path": path,
        "source_url": f"{GITHUB_REPO}/blob/main/{quote(path)}",
        "source_raw_url": f"{GITHUB_REPO}/raw/main/{quote(path)}",
        "source_edit_url": f"{GITHUB_REPO}/edit/main/{quote(path)}",
        "feedback_url": f"{GITHUB_REPO}/issues/new?{issue}",
    }


def render_one(
    env: Environment, source_path: Path, out_dir: Path, force: bool = False
) -> tuple[str, dict | None, str]:
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
        **source_links(source_path, slug),
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
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MIM — Ingredient index</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<nav aria-label="Site navigation"><a href="../index.html">Home</a> &middot; <a href="../browser.html">Browse ingredients</a> &middot; <a href="../text_map.html">Text Map</a> &middot; <a href="../ingredient_umap.html">KG PaCMAP</a> &middot; <a href="../ingredient_graph.html">Graph Layout</a> &middot; <a href="../app/discussions/index.html">Discussions</a> &middot; <a href="../schema/index.html">Schema</a> &middot; <a href="../index.html#downloads">Downloads</a> &middot; <a href="https://culturebotai.github.io/mechs/">All Mech projects</a></nav>
<header>
<form class="record-search" action="../browser.html" method="get" role="search">
  <label class="sr-only" for="index-search-input">Search ingredients</label>
  <input type="search" id="index-search-input" name="q" placeholder="Search ingredients, synonyms, or ontology IDs...">
  <button type="submit">Search</button>
</form>
<h1>MIM — Ingredient index</h1>
<p class="muted">{count:,} ingredients, generated {generated_at}.</p>
</header>
<main id="main-content">{by_prefix}</main>
<footer>Generated {generated_at} &middot; <a href="build.json">Build provenance (SHA-256 manifest)</a> &middot; <a href="../schema/index.html">LinkML Schema</a><br>{licence}</footer>
<script src="../theme-toggle.js"></script>
</body>
</html>
"""


def _section(prefix: str, items: list[tuple[str, str, str]]) -> str:
    rows = "".join(
        f'<li><a href="ingredient/{escape(slug, quote=True)}.html">{escape(name)}</a> '
        f'<span class="muted">— <code>{escape(ident)}</code></span></li>'
        for (ident, slug, name) in sorted(items, key=lambda x: x[2].lower())
    )
    return (
        f'<section id="prefix-{quote(prefix, safe="")}"><h2>{escape(prefix)} '
        f'<small class="muted">({len(items)})</small></h2>'
        f'<ul class="medium-index">{rows}</ul></section>'
    )


def write_index(out_dir: Path, all_records: list[dict]) -> None:
    by_prefix: dict[str, list[tuple[str, str, str]]] = {}
    for r in all_records:
        ident = r["ingredient"].get("identifier") or ""
        prefix = ident.split(":", 1)[0] if ":" in ident else "(other)"
        by_prefix.setdefault(prefix, []).append(
            (ident, r["slug"], r["ingredient"].get("preferred_term") or r["slug"])
        )
    sections = "\n".join(_section(p, items) for p, items in sorted(by_prefix.items()))
    rows_total = sum(len(v) for v in by_prefix.values())
    html = INDEX_TEMPLATE.format(
        licence=LICENCE_HTML,
        count=rows_total,
        generated_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        by_prefix='<nav aria-label="Identifier groups"><ul>'
        + "".join(
            f'<li><a href="#prefix-{quote(p, safe="")}">{escape(p)} ({len(v)})</a></li>'
            for p, v in sorted(by_prefix.items())
        )
        + "</ul></nav>"
        + sections,
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--ingredients-dir",
        type=Path,
        default=DEFAULT_INGREDIENTS,
        help="root containing mapped/ and unmapped/ subdirs",
    )
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
        status, ingredient, slug = render_one(env, path, args.out_dir, force=args.force)
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
