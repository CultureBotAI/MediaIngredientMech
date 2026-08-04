#!/usr/bin/env python3
"""Flag agent-instruction files that name recipes or paths which no longer exist.

Skills, commands and `/goal` prompts are executable in practice: an agent reads
them and does what they say. When they drift they do not fail loudly like code —
they quietly send the next agent down a path that no longer exists, or worse, one
that is actively wrong. `.claude/commands/ground-or-propose-ingredient.md` kept
recommending `just export-individual` / `just aggregate-collections` "to keep
per-record files and collections in sync" long after that pairing was identified
as the mechanism which silently reverted 55 curation events (#148); it had to be
corrected twice, both times because a human happened to notice (#167, #179).

This is the mechanical version of noticing. It reports two kinds of drift:

* `just <recipe>` naming a recipe the justfile does not define;
* a repo-relative path (`scripts/x.py`, `data/y.yaml`, …) that does not exist.

Deliberately narrow, because a false positive in a docs check is how the check
gets ignored:

* only references inside a code span or fenced block count — prose like "just the
  collection" is not a recipe reference;
* a path must contain a `/`, so a bare "mapped_ingredients.yaml" in prose is not
  treated as a path claim;
* paths resolve against the repo root AND the containing file's directory, since
  skills reference their own `reference/*.md` relatively.

Legitimate references that this cannot verify — a sibling repo's recipe, a file
the reader is told to create, a deliberate mention of something removed — are
declared in `conf/instruction_refs.yaml` with a reason, or suppressed inline with
`<!-- refcheck: ignore -->` on the same line.

Exit codes: 0 = clean (or severity=warn), 1 = findings with severity=error,
2 = configuration/usage error.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = REPO_ROOT / "conf" / "instruction_refs.yaml"

INLINE_SUPPRESS = "<!-- refcheck: ignore -->"

CODE_SPAN = re.compile(r"`([^`\n]+)`")
JUST_CALL = re.compile(r"^just\s+([a-z0-9][a-z0-9-]*)")
# A path claim needs a directory separator and a known extension: this is a
# reference to a file in the repo, not an ordinary filename mentioned in prose.
PATH_CLAIM = re.compile(
    r"^([A-Za-z0-9_.][A-Za-z0-9_./-]*/[A-Za-z0-9_./-]+\.(?:py|ya?ml|tsv|json|sh|md|j2))$"
)


@dataclass(frozen=True)
class Finding:
    kind: str  # "recipe" | "path"
    path: str  # file containing the stale reference
    line: int
    ref: str

    def __str__(self) -> str:
        what = f"just {self.ref}" if self.kind == "recipe" else self.ref
        return f"{self.path}:{self.line}  {what}"


def known_recipes(root: Path) -> set[str]:
    """Recipe names the justfile defines, via `just --list`."""
    proc = subprocess.run(
        ["just", "--list"], cwd=root, capture_output=True, text=True, check=False
    )
    if proc.returncode != 0:
        raise SystemExit(
            f"`just --list` failed (exit {proc.returncode}); cannot verify recipe "
            f"references.\n{proc.stderr.strip()}"
        )
    found = set()
    for line in proc.stdout.splitlines():
        match = re.match(r"\s{4}([a-z0-9][a-z0-9-]*)", line)
        if match:
            found.add(match.group(1))
    return found


def _references(text: str):
    """Yield (line_no, code_span) for every code span and fenced-block line."""
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if INLINE_SUPPRESS in line:
            continue
        if in_fence:
            yield line_no, line.strip()
        else:
            for match in CODE_SPAN.finditer(line):
                yield line_no, match.group(1).strip()


def scan_file(path: Path, root: Path, recipes: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    rel = path.relative_to(root).as_posix()
    for line_no, span in _references(path.read_text(encoding="utf-8")):
        recipe = JUST_CALL.match(span)
        if recipe and recipe.group(1) not in recipes:
            findings.append(Finding("recipe", rel, line_no, recipe.group(1)))
        claim = PATH_CLAIM.match(span)
        if claim:
            target = claim.group(1)
            # Repo-relative, or relative to the file itself (skills reference
            # their own reference/*.md that way).
            if not (root / target).exists() and not (path.parent / target).exists():
                findings.append(Finding("path", rel, line_no, target))
    return findings


def load_config(config_path: Path) -> dict:
    if not config_path.is_file():
        raise SystemExit(f"Config not found: {config_path}")
    cfg = yaml.safe_load(config_path.read_text()) or {}
    for key in ("targets", "severity"):
        if key not in cfg:
            raise SystemExit(f"Config {config_path} is missing required key: {key}")
    return cfg


def collect_targets(root: Path, globs: list[str]) -> list[Path]:
    seen: dict[Path, None] = {}
    for pattern in globs:
        for path in sorted(root.glob(pattern)):
            if path.is_file():
                seen.setdefault(path, None)
    return list(seen)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument(
        "--severity",
        choices=("warn", "error"),
        default=None,
        help="Override the config's severity. `error` exits 1 on any finding.",
    )
    args = parser.parse_args(argv)

    cfg = load_config(args.config)
    severity = args.severity or cfg["severity"]
    ignored_recipes = {
        entry["name"] for entry in (cfg.get("ignore_recipes") or []) if "name" in entry
    }
    ignored_paths = {
        entry["path"] for entry in (cfg.get("ignore_paths") or []) if "path" in entry
    }

    recipes = known_recipes(REPO_ROOT)
    targets = collect_targets(REPO_ROOT, cfg["targets"])
    if not targets:
        raise SystemExit(f"No instruction files matched: {cfg['targets']}")

    findings: list[Finding] = []
    for path in targets:
        for finding in scan_file(path, REPO_ROOT, recipes):
            if finding.kind == "recipe" and finding.ref in ignored_recipes:
                continue
            if finding.kind == "path" and finding.ref in ignored_paths:
                continue
            findings.append(finding)

    print(f"Scanned {len(targets)} agent-instruction file(s) against {len(recipes)} recipes.")
    if not findings:
        print("OK: every referenced recipe and path exists.")
        return 0

    stale_recipes = [f for f in findings if f.kind == "recipe"]
    stale_paths = [f for f in findings if f.kind == "path"]
    if stale_recipes:
        print(f"\nRecipes that no longer exist ({len(stale_recipes)}):")
        for finding in stale_recipes:
            print(f"  {finding}")
    if stale_paths:
        print(f"\nPaths that no longer exist ({len(stale_paths)}):")
        for finding in stale_paths:
            print(f"  {finding}")

    print(
        "\nEach of these tells the next agent to run or read something that is not "
        "there.\nFix the reference, or — if it is a sibling repo's recipe, a file the "
        "reader creates,\nor a deliberate mention of something removed — declare it in "
        f"{args.config.relative_to(REPO_ROOT)} with a reason,\nor add "
        f"`{INLINE_SUPPRESS}` to the line."
    )

    if severity == "error":
        return 1
    print("\n(severity=warn: reporting only, not failing the build)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
