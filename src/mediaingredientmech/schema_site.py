"""Publish a rendered schema reference, including imported enums and types."""

from html import escape
from pathlib import Path
from urllib.parse import quote

from linkml_runtime.dumpers import json_dumper  # type: ignore[import-untyped]
from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]

from mediaingredientmech.render_ingredient_pages import structured_value


def write_schema_site(schema: Path, output: Path) -> list[str]:
    view = SchemaView(str(schema))
    groups = {
        "Classes": view.all_classes(),
        "Slots": view.all_slots(),
        "Enumerations": view.all_enums(),
        "Types": view.all_types(),
    }
    output.mkdir(parents=True, exist_ok=True)

    def shell(title, content):
        return (
            '<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f"<title>{escape(title)} — MediaIngredientMech schema</title>"
            '<link rel="stylesheet" href="../records/style.css">'
            '<nav><a href="../index.html">Home</a> · <a href="index.html">Schema index</a> · '
            '<a href="https://culturebotai.github.io/mechs/">All Mech projects</a></nav>'
            f"<main><h1>{escape(title)}</h1>{content}</main>"
            '<script src="../theme-toggle.js"></script></html>'
        )

    sections = []
    for group, definitions in groups.items():
        links = []
        for name, definition in sorted(definitions.items()):
            filename = group.lower() + "-" + quote(name, safe="") + ".html"
            (output / filename).write_text(
                shell(name, str(structured_value(json_dumper.to_dict(definition))))
            )
            links.append(f'<li><a href="{escape(filename, quote=True)}">{escape(name)}</a></li>')
        sections.append(
            f'<section id="{group.lower()}"><h2>{group} ({len(definitions)})</h2><ul>{"".join(links)}</ul></section>'
        )
    (output / "index.html").write_text(
        shell(
            "Schema reference",
            '<p>Generated from the schema and its imports. <a href="../index.md">Raw Markdown index</a>.</p>'
            + "".join(sections),
        )
    )
    return sorted("schema/" + p.name for p in output.glob("*.html"))
