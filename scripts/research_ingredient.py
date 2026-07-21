"""Run deep-research-client for one MediaIngredientMech ingredient record."""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
INGREDIENTS_DIR = REPO_ROOT / "data" / "ingredients"
DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "ingredient_mapping_research.md"
DEFAULT_RESEARCH_DIR = REPO_ROOT / "research"


def load_ingredient(path: Path) -> dict[str, Any]:
    """Load one ingredient YAML file."""
    with path.open() as stream:
        doc = yaml.safe_load(stream)
    if not isinstance(doc, dict):
        raise ValueError(f"Ingredient file is not a mapping: {path}")
    return doc


def resolve_ingredient_file(
    status: str | None = None,
    slug: str | None = None,
    target: Path | None = None,
) -> Path:
    """Resolve an ingredient by status/slug or direct YAML path."""
    if target is not None:
        path = target if target.is_absolute() else REPO_ROOT / target
        if path.is_file():
            return path
        raise FileNotFoundError(f"Ingredient file not found: {path}")

    if not status or not slug:
        raise ValueError("Either --target or both --status and --slug are required")

    allowed_statuses = sorted(path.name for path in INGREDIENTS_DIR.iterdir() if path.is_dir())
    if status not in allowed_statuses:
        raise ValueError(
            f"Unknown ingredient status '{status}'. Available: {', '.join(allowed_statuses)}"
        )

    path = INGREDIENTS_DIR / status / f"{slug}.yaml"
    if path.is_file():
        return path

    raise FileNotFoundError(f"Ingredient file not found: {path}")


def infer_status_slug(path: Path) -> tuple[str, str]:
    """Infer ingredient collection status and slug from a resolved YAML path."""
    path = path.resolve()
    try:
        relative = path.relative_to(INGREDIENTS_DIR)
    except ValueError:
        return "custom", path.stem
    if len(relative.parts) >= 2:
        return relative.parts[0], path.stem
    return "custom", path.stem


def _join_values(values: list[str], fallback: str = "None recorded") -> str:
    return "; ".join(value for value in values if value) or fallback


def _scalar_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def summarize_synonyms(doc: dict[str, Any], limit: int = 20) -> str:
    synonyms = doc.get("synonyms") or []
    values: list[str] = []
    for synonym in synonyms:
        if isinstance(synonym, dict):
            text = synonym.get("synonym_text")
            synonym_type = synonym.get("synonym_type")
            source = synonym.get("source")
            pieces = [_scalar_text(text)]
            if synonym_type:
                pieces.append(f"type={synonym_type}")
            if source:
                pieces.append(f"source={source}")
            if len(pieces) > 1:
                values.append(f"{pieces[0]} ({', '.join(pieces[1:])})")
            else:
                values.append(pieces[0])
        elif synonym:
            values.append(_scalar_text(synonym))
    if len(values) > limit:
        values = values[:limit] + [f"... ({len(synonyms) - limit} more)"]
    return _join_values(values)


def summarize_mapping(doc: dict[str, Any]) -> str:
    mapping = doc.get("ontology_mapping") or {}
    if not isinstance(mapping, dict):
        return _scalar_text(mapping) or "None recorded"
    fields = ["ontology_id", "ontology_label", "ontology_source", "mapping_quality"]
    return _join_values([f"{key}={mapping[key]}" for key in fields if mapping.get(key)])


def summarize_chemical_properties(doc: dict[str, Any]) -> str:
    properties = doc.get("chemical_properties") or {}
    if not isinstance(properties, dict):
        return _scalar_text(properties) or "None recorded"
    preferred_order = [
        "molecular_formula",
        "cas_rn",
        "smiles",
        "inchi",
        "data_source",
        "retrieval_date",
    ]
    ordered_keys = preferred_order + sorted(key for key in properties if key not in preferred_order)
    return _join_values([f"{key}={properties[key]}" for key in ordered_keys if properties.get(key)])


def summarize_occurrences(doc: dict[str, Any]) -> str:
    statistics = doc.get("occurrence_statistics") or {}
    if not isinstance(statistics, dict):
        return _scalar_text(statistics) or "None recorded"
    return _join_values([f"{key}={value}" for key, value in statistics.items()])


def summarize_evidence(doc: dict[str, Any], limit: int = 10) -> str:
    mapping = doc.get("ontology_mapping") or {}
    evidence = mapping.get("evidence") if isinstance(mapping, dict) else None
    if not isinstance(evidence, list):
        return "None recorded"

    values: list[str] = []
    for item in evidence:
        if isinstance(item, dict):
            bits = []
            for key in (
                "evidence_type",
                "source",
                "pmid",
                "supports",
                "notes",
                "snippet",
                "explanation",
            ):
                if item.get(key):
                    bits.append(f"{key}={item[key]}")
            values.append("; ".join(bits))
        elif item:
            values.append(_scalar_text(item))
    if len(values) > limit:
        values = values[:limit] + [f"... ({len(evidence) - limit} more)"]
    return _join_values(values)


def summarize_curation_history(doc: dict[str, Any], limit: int = 8) -> str:
    history = doc.get("curation_history") or []
    if not isinstance(history, list):
        return _scalar_text(history) or "None recorded"

    values: list[str] = []
    for event in history[-limit:]:
        if isinstance(event, dict):
            action = event.get("action", "UNKNOWN_ACTION")
            timestamp = event.get("timestamp")
            changes = event.get("changes")
            bits = [str(action)]
            if timestamp:
                bits.append(f"timestamp={timestamp}")
            if changes:
                bits.append(f"changes={changes}")
            values.append("; ".join(bits))
        elif event:
            values.append(_scalar_text(event))
    return _join_values(values)


# --- Step 7b role-facet helpers (used by templates/ingredient_role_research.md). ------

def _facet_enum_values(enum_name: str) -> list[str]:
    """Return the permissible-value token list for a facet enum in the LinkML schema.

    Uses `mediaingredientmech.curation.ingredient_curator` which already exposes
    SchemaView-derived VALID_* frozensets (added in #135). Kept as a helper so
    template rendering can compose a candidate menu Edison can pick from.
    """
    import sys
    sys.path.insert(0, str(REPO_ROOT / "src"))
    from mediaingredientmech.curation.ingredient_curator import (
        VALID_CELLULAR_METABOLIC_ROLES,
        VALID_NUTRITIONAL_ROLES,
        VALID_PHYSICOCHEMICAL_ROLES,
    )
    return sorted({
        "NutritionalRoleEnum":       VALID_NUTRITIONAL_ROLES,
        "PhysicochemicalRoleEnum":   VALID_PHYSICOCHEMICAL_ROLES,
        "CellularMetabolicRoleEnum": VALID_CELLULAR_METABOLIC_ROLES,
    }[enum_name])


def summarize_existing_role_assignments(doc: dict[str, Any]) -> str:
    """Render the three facet slots currently on the IngredientRecord for context.

    Edison sees this so it doesn't propose values that already exist AND so it
    knows which facets are the actual gaps to fill.
    """
    facets = [
        ("nutritional_roles",       "Nutritional"),
        ("physicochemical_roles",   "Physicochemical"),
        ("cellular_metabolic_roles", "Cellular-metabolic"),
    ]
    parts: list[str] = []
    for slot, label in facets:
        assignments = doc.get(slot) or []
        if not isinstance(assignments, list) or not assignments:
            parts.append(f"{label}: (none — GAP)")
            continue
        roles = []
        for a in assignments:
            if isinstance(a, dict):
                role = a.get("role", "?")
                conf = a.get("confidence")
                roles.append(f"{role}" + (f"@{conf:.2f}" if isinstance(conf, (int, float)) else ""))
            elif isinstance(a, str):
                roles.append(a)
        parts.append(f"{label}: [{', '.join(roles)}]")
    return "; ".join(parts)


def summarize_chebi_role_axioms(doc: dict[str, Any], limit: int = 15) -> str:
    """Live OAK lookup of CHEBI `has_role` axioms on the ingredient's CHEBI id.

    Returns a human-readable summary of each `has_role` target (id + label)
    so Edison can confirm or contradict what CHEBI's own hierarchy asserts.
    Falls back to "None recorded" if no CHEBI id, no OAK adapter, or no axioms.

    Slow — ~2-5s cold-start on the first call in a process. Adapter is cached
    at module level so subsequent calls are ~ms.
    """
    chebi_id = _ingredient_chebi_id(doc)
    if not chebi_id:
        return "None recorded (no CHEBI grounding)"
    adapter = _oak_chebi_adapter()
    if adapter is None:
        return "None recorded (OAK adapter unavailable)"
    try:
        triples = list(adapter.relationships(subjects=[chebi_id]))
    except Exception as exc:  # pragma: no cover — OAK failure modes are noisy.
        return f"None recorded (OAK query failed: {exc!r})"

    axioms = []
    for triple in triples:
        if not isinstance(triple, tuple) or len(triple) < 3:
            continue
        _s, pred, obj = triple[0], triple[1], triple[2]
        if pred != "RO:0000087":  # has_role
            continue
        if not isinstance(obj, str) or not obj.startswith("CHEBI:"):
            continue
        try:
            lbl = adapter.label(obj) or obj
        except Exception:
            lbl = obj
        axioms.append(f"{obj} ({lbl})")
    if not axioms:
        return "None recorded (CHEBI has no has_role axioms on this compound)"
    if len(axioms) > limit:
        axioms = axioms[:limit] + [f"... ({len(axioms) - limit} more)"]
    return "; ".join(axioms)


_CHEBI_ID_PATHS = (
    ("identifier",),           # IngredientRecord's own identifier when it starts with CHEBI:
    ("ontology_mapping", "ontology_id"),
)


def _ingredient_chebi_id(doc: dict[str, Any]) -> str | None:
    """Extract CHEBI id from a MIM IngredientRecord."""
    for path in _CHEBI_ID_PATHS:
        cur: Any = doc
        for key in path:
            if not isinstance(cur, dict):
                cur = None
                break
            cur = cur.get(key)
        if isinstance(cur, str) and cur.startswith("CHEBI:"):
            return cur
    return None


_OAK_CACHE: dict[str, Any] = {}


def _oak_chebi_adapter():
    """Return a cached `sqlite:obo:chebi` adapter, or None if oaklib isn't available."""
    if "chebi" in _OAK_CACHE:
        return _OAK_CACHE["chebi"]
    try:
        from oaklib import get_adapter  # type: ignore
        adapter = get_adapter("sqlite:obo:chebi")
    except Exception:  # pragma: no cover — oaklib install / sqlite fetch failures
        adapter = None
    _OAK_CACHE["chebi"] = adapter
    return adapter


def template_vars(
    doc: dict[str, Any],
    ingredient_status: str,
    ingredient_slug: str,
) -> dict[str, str]:
    """Build template variables for deep-research-client.

    The five `candidate_*_roles` / `existing_role_assignments` /
    `chebi_role_axioms` entries below feed the Step 7b role-research
    template. Existing consumers of `template_vars` (identity/mapping
    research) ignore the extra keys — `_DefaultEmpty` swallows any
    placeholder the template doesn't reference.
    """
    return {
        "ingredient_label": _scalar_text(doc.get("preferred_term")) or ingredient_slug,
        "ingredient_identifier": _scalar_text(doc.get("identifier")) or "None recorded",
        "ingredient_status": ingredient_status,
        "ingredient_slug": ingredient_slug,
        "ingredient_type": _scalar_text(doc.get("ingredient_type")) or "None recorded",
        "mapping_status": _scalar_text(doc.get("mapping_status")) or "None recorded",
        "ontology_mapping": summarize_mapping(doc),
        "chemical_properties": summarize_chemical_properties(doc),
        "synonyms": summarize_synonyms(doc),
        "occurrence_summary": summarize_occurrences(doc),
        "evidence_summary": summarize_evidence(doc),
        "curation_summary": summarize_curation_history(doc),
        "notes": _scalar_text(doc.get("notes")) or "None recorded",
        # Step 7b (ingredient_role_research.md) additions:
        "candidate_nutritional_roles":       ", ".join(_facet_enum_values("NutritionalRoleEnum")),
        "candidate_physicochemical_roles":   ", ".join(_facet_enum_values("PhysicochemicalRoleEnum")),
        "candidate_cellular_metabolic_roles": ", ".join(_facet_enum_values("CellularMetabolicRoleEnum")),
        "existing_role_assignments": summarize_existing_role_assignments(doc),
        "chebi_role_axioms": summarize_chebi_role_axioms(doc),
    }


def normalize_provider(provider: str) -> str:
    """Canonical form of a ``--provider`` value.

    ``--provider`` is free-text (no argparse ``choices``), so the value reaching
    the comparisons below is whatever the caller typed. Case- and whitespace-fold
    it so ``--provider Falcon`` behaves like ``falcon``.
    """
    return (provider or "").strip().lower()


def provider_args(provider: str) -> list[str]:
    """Mirror deep-research-client provider flags used by sibling Mech repos."""
    if normalize_provider(provider) == "cborg":
        return ["--use-cborg"]
    return ["--provider", provider]


def research_env(provider: str) -> dict[str, str]:
    """Build the subprocess environment, honouring the deprecated FutureHouse alias.

    ``--provider falcon`` IS the Edison provider. "Falcon"/"FutureHouse" is the
    former brand: ``deep_research_client/client.py`` registers it as
    ``# Edison provider (formerly Falcon/FutureHouse)`` and resolves its
    credential as ``os.getenv("EDISON_API_KEY") or os.getenv("FUTUREHOUSE_API_KEY")``,
    then hands it to ``EdisonClient``. One Edison credential covers both names,
    and ``FUTUREHOUSE_API_KEY`` is a deprecated alias for that same key — the
    client emits a DeprecationWarning when it falls back to it.

    So there is no cross-vendor credential question here, and nothing to
    withhold: passing ``EDISON_API_KEY`` to ``--provider falcon`` sends an Edison
    key to Edison. The only thing worth doing is honouring the deprecated alias
    when the canonical variable is unset, for client versions that don't.
    """
    env = os.environ.copy()
    if (
        normalize_provider(provider) == "falcon"
        and not env.get("EDISON_API_KEY")
        and env.get("FUTUREHOUSE_API_KEY")
    ):
        env["EDISON_API_KEY"] = env["FUTUREHOUSE_API_KEY"]
    return env


def build_command(
    provider: str,
    template: Path,
    output_file: Path,
    citations_file: Path,
    variables: dict[str, str],
    passthrough_args: list[str] | None = None,
    client_command: str = "deep-research-client",
) -> list[str]:
    """Build a deep-research-client command."""
    command = [
        client_command,
        "research",
        "--template",
        str(template),
    ]
    for key in sorted(variables):
        command.extend(["--var", f"{key}={variables[key]}"])
    command.extend(provider_args(provider))
    command.extend(["--output", str(output_file), "--separate-citations", str(citations_file)])
    command.extend(passthrough_args or [])
    return command


def build_provider_command(
    provider: str | None = None,
    client_command: str = "deep-research-client",
) -> list[str]:
    """Build a deep-research-client provider availability command."""
    command = [client_command, "providers"]
    if provider:
        command.extend(["--provider", provider])
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", default="falcon", help="deep-research-client provider")
    parser.add_argument(
        "--provider-status",
        metavar="PROVIDER",
        help="Check availability for one deep-research-client provider",
    )
    parser.add_argument(
        "--list-providers",
        action="store_true",
        help="List deep-research-client providers",
    )
    parser.add_argument("--status", help="Ingredient status directory, such as mapped or unmapped")
    parser.add_argument("--slug", help="Ingredient YAML stem under data/ingredients/<status>")
    parser.add_argument("--target", type=Path, help="Direct path to an ingredient YAML file")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH_DIR)
    parser.add_argument("--client-command", default="deep-research-client")
    parser.add_argument("--dry-run", action="store_true", help="Print command without running it")
    parser.add_argument(
        "passthrough",
        nargs=argparse.REMAINDER,
        help="Additional deep-research-client args",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.provider_status:
        command = build_provider_command(args.provider_status, args.client_command)
        subprocess.run(command, check=True, env=research_env(args.provider_status))
        return 0
    if args.list_providers:
        command = build_provider_command(client_command=args.client_command)
        subprocess.run(command, check=True, env=research_env(args.provider))
        return 0

    target = resolve_ingredient_file(args.status, args.slug, args.target)
    ingredient_status, ingredient_slug = infer_status_slug(target)
    doc = load_ingredient(target)
    variables = template_vars(doc, ingredient_status, ingredient_slug)

    output_dir = args.research_dir / "ingredients" / ingredient_status
    output_file = output_dir / f"{ingredient_slug}-deep-research-{args.provider}.md"
    citations_file = output_dir / f"{ingredient_slug}-deep-research-{args.provider}.citations.md"
    command = build_command(
        provider=args.provider,
        template=args.template,
        output_file=output_file,
        citations_file=citations_file,
        variables=variables,
        passthrough_args=args.passthrough,
        client_command=args.client_command,
    )

    print(f"Researching: {variables['ingredient_label']} ({args.provider}) -> {output_file}")
    if args.dry_run:
        print(shlex.join(command))
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(command, check=True, env=research_env(args.provider))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
