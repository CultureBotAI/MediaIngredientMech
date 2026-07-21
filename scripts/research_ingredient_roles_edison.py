"""Edison-driven role research for one MediaIngredientMech ingredient (Step 7b lane).

Thin shim over `scripts/research_ingredient_edison.py` that pins the role
research template and the roles output subdirectory. Everything else —
CLI flags, batch mode, dry-run, capture bundle, cost tallying — is
inherited unchanged.

Usage (mirrors research_ingredient_edison.py exactly):

    just research-ingredient-roles-edison <target>
    uv run --extra dev python scripts/research_ingredient_roles_edison.py \\
        --target data/ingredients/mapped/L-cysteine.yaml [--dry-run]

Batch:

    just research-ingredient-roles-edison-batch <batch.json>
    uv run --extra dev python scripts/research_ingredient_roles_edison.py \\
        --batch reports/role_research_priority.json --limit 10

Outputs go to `research/ingredients/roles/<slug>-edison-{job}.md` (+ the
standard 6-file capture bundle). Keep them separate from identity-mapping
research (which writes to `research/ingredients/<slug>-edison-{job}.md`)
so runs never clobber each other.

The template is `templates/ingredient_role_research.md`; extending
`research_ingredient.py::template_vars()` (also in this PR) is what
supplies the five role-specific placeholders it references.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
_ROLES_TEMPLATE = REPO_ROOT / "templates" / "ingredient_role_research.md"
_ROLES_OUT_DIR = REPO_ROOT / "research" / "ingredients" / "roles"


def _inject_defaults(argv: list[str]) -> list[str]:
    """Insert `--template <roles_template>` and `--out-dir <roles_dir>` unless caller overrode."""
    args = list(argv)
    if not any(a == "--template" or a.startswith("--template=") for a in args):
        args.extend(["--template", str(_ROLES_TEMPLATE)])
    if not any(a == "--out-dir" or a.startswith("--out-dir=") for a in args):
        args.extend(["--out-dir", str(_ROLES_OUT_DIR)])
    return args


def main(argv: list[str] | None = None) -> int:
    # Import lazily so `--help` still works even if optional deps (edison-client)
    # aren't installed.
    from research_ingredient_edison import main as _upstream_main

    if argv is None:
        argv = sys.argv[1:]
    return _upstream_main(_inject_defaults(argv))


if __name__ == "__main__":
    # scripts/ is on sys.path so `import research_ingredient_edison` works when
    # this file is run directly (matches the pattern used by the tests).
    _SCRIPTS_DIR = Path(__file__).resolve().parent
    if str(_SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(_SCRIPTS_DIR))
    sys.exit(main())
