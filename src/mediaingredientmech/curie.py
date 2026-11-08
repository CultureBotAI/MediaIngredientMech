"""Canonical CURIE handling for MediaIngredientMech.

Answers three questions that external repos kept having to answer for themselves,
each of which had a wrong-but-plausible default (see issue #119):

1. **Is this CURIE syntactically valid, and is its prefix one we recognise?**
   A typo'd prefix (``CHBEI:``) must not silently pass as an unknown-but-fine
   identifier, and a foreign identifier wearing an OBO prefix (a PubChem CID as
   ``CHEBI:10716816``) must not pass as a real term.

2. **Which permanent MIM ID does this reference identify?** Numeric IDs resolve
   through the append-only registry and current corpus. Historical filename and
   placeholder aliases remain usable only when they identify one record.

3. **Which ontology term does a MIM ingredient "mean"?** 180 of 1,876 subjects
   carry more than one mapping (typically CHEBI + cas + kgmicrobe.compound), so
   this is a selection rule, not a lookup — and only ``skos:exactMatch`` rows are
   safe to treat as equivalences at all.

Nothing here does network I/O; it reads the registry, current corpus, SSSOM and
historical alias map. Shared ontology mappings do not choose between records.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SSSOM = REPO / "mappings" / "ingredient_mappings.sssom.tsv"
ALIASES = REPO / "mappings" / "mim_curie_aliases.tsv"

# Recognised prefixes and the exact case in which MIM emits them. Anything not
# listed is rejected rather than waved through, so a typo surfaces immediately.
CANONICAL_PREFIX = {
    p.casefold(): p
    for p in (
        "MIM",
        "CHEBI",
        "FOODON",
        "UBERON",
        "ENVO",
        "NCIT",
        "MICRO",
        "BTO",
        "GO",
        "NCBITaxon",
        "mesh",
        "cas",
        "kgmicrobe.compound",
        "kgmicrobe.ingredient",
        "mediadive.ingredient",
        "mediadive.medium",
        "mediadive.solution",
        "CultureMech",
        "CommunityMech",
        "TraitMech",
    )
}

# Accession ceilings. This is a WEAK heuristic and is deliberately loose: real
# CHEBI accessions reach at least 747,127 (gepotidacin), while the PubChem CIDs
# that turned up wearing a CHEBI prefix include 6-digit values (503742, 867561)
# that sit *inside* the real range. So a ceiling can only catch the egregious
# cases — it is not a substitute for checking that the id actually resolves, and
# must never be the sole reason to reject an id that an ontology can confirm.
MAX_ACCESSION = {
    "CHEBI": 1_000_000,
    "FOODON": 4_000_000,
    "UBERON": 9_000_000,
    "ENVO": 9_000_000,
    "NCIT": 900_000,
    "GO": 3_000_000,
}

# Preference when a subject carries several mappings. Ontology terms first
# (they carry semantics), then registry identifiers, then local placeholders.
PREFIX_RANK = {
    "CHEBI": 0,
    "FOODON": 1,
    "UBERON": 2,
    "ENVO": 3,
    "MICRO": 4,
    "BTO": 5,
    "NCIT": 6,
    "GO": 7,
    "mesh": 8,
    "cas": 9,
    "kgmicrobe.compound": 10,
    "kgmicrobe.ingredient": 11,
}

# Only these assert that subject and object denote the same thing. A broadMatch
# row in particular means the MIM subject is MORE specific than the object (the
# object is the broader concept, #390), so treating the object as an equivalent
# silently generalises the ingredient.
EQUIVALENT_PREDICATES = {"skos:exactMatch"}

_CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_.]*):([A-Za-z0-9_.~%\-]+)$")


def mim_curie_for_stem(stem: str) -> str:
    """`MIM:<stem>` with non-URL-safe characters ~HEX escaped.

    This is a historical alias spelling, never a new permanent record ID.
    """
    safe = re.sub(r"[^A-Za-z0-9_\-.]", lambda m: f"~{ord(m.group(0)):02X}", stem)
    return f"MIM:{safe}"


# This set contains MICRO terms verified against canonical IRIs in OLS4.
# Separately, micro_source validates reviewed KG-Microbe CURIEs against pinned
# KGX labels, parents and original legacy MicrO.owl IRIs. That source-backed
# path does not claim canonical-IRI or OLS defining-ontology verification.
#
# Regenerate with: python scripts/verify_micro_ids.py — note it only checks ids
# already present in the SSSOM, so its output is a SUBSET of this set (8 entries
# here currently have no published row). Treat a regenerator-only id as the gap,
# not a shorter list as drift.
#
# MICRO:0000543 / :0001570 / :0001572 added 2026-08-15 for `R2A agar`,
# `Defibrinated sheep blood` and `Defibrinated horse blood` (#260). Each was
# checked the way the refusal note prescribes: is_defining_ontology=true, not
# obsolete, and the canonical …/obo/MICRO_nnnnnnn IRI round-trips on OLS4. The
# control MICRO:0002115 'defibrinated blood' 404s on that IRI, so the check
# discriminates rather than passing everything.
MICRO_VERIFIED = {
    "MICRO:0000082",
    "MICRO:0000094",
    "MICRO:0000113",
    "MICRO:0000114",
    "MICRO:0000175",
    "MICRO:0000176",
    "MICRO:0000178",
    "MICRO:0000180",
    "MICRO:0000182",
    "MICRO:0000183",
    "MICRO:0000193",
    "MICRO:0000253",
    "MICRO:0000307",
    "MICRO:0000455",
    "MICRO:0000456",
    "MICRO:0000457",
    "MICRO:0000460",
    "MICRO:0000462",
    "MICRO:0000466",
    "MICRO:0000520",
    "MICRO:0000521",
    "MICRO:0000522",
    "MICRO:0000536",
    "MICRO:0000541",
    "MICRO:0000543",
    "MICRO:0000554",
    "MICRO:0000566",
    "MICRO:0000567",
    "MICRO:0000568",
    "MICRO:0000570",
    "MICRO:0000591",
    "MICRO:0000594",
    "MICRO:0000595",
    "MICRO:0000606",
    "MICRO:0000610",
    "MICRO:0000673",
    "MICRO:0001229",
    "MICRO:0001230",
    "MICRO:0001234",
    "MICRO:0001235",
    "MICRO:0001238",
    "MICRO:0001241",
    "MICRO:0001328",
    "MICRO:0001348",
    "MICRO:0001349",
    "MICRO:0001358",
    "MICRO:0001362",
    "MICRO:0001363",
    "MICRO:0001365",
    "MICRO:0001366",
    "MICRO:0001570",
    "MICRO:0001572",
    "MICRO:0001574",
    "MICRO:0001597",
    "MICRO:0001598",
    "MICRO:0001599",
    "MICRO:0001611",
    "MICRO:0001647",
    "MICRO:0001668",
    "MICRO:0001709",
    "MICRO:0001715",
    "MICRO:0001723",
    "MICRO:0001773",
}


@dataclass
class Verdict:
    """Outcome of normalising one CURIE."""

    ok: bool
    curie: str = ""
    problem: str = ""
    note: str = ""

    def __bool__(self) -> bool:
        return self.ok


@dataclass
class CurieNormalizer:
    """Validate, canonicalise and resolve MIM-facing CURIEs."""

    sssom_path: Path | None = None
    alias_path: Path | None = None
    repo_root: Path | None = None
    _aliases: dict[str, str] = field(default_factory=dict, repr=False)
    _mappings: dict[str, list[tuple[str, str]]] = field(default_factory=dict, repr=False)
    _subjects: set[str] = field(default_factory=set, repr=False)
    _records: set[str] = field(default_factory=set, repr=False)
    _alias_targets: dict[str, set[str]] = field(default_factory=dict, repr=False)
    _resolved_ids: dict[str, str] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        from mediaingredientmech.stable_ids import load_registry, resolve_id, validate_records
        from mediaingredientmech.utils.yaml_handler import load_yaml

        root = self.repo_root or REPO
        self.sssom_path = self.sssom_path or root / "mappings/ingredient_mappings.sssom.tsv"
        self.alias_path = self.alias_path or root / "mappings/mim_curie_aliases.tsv"
        self._registry = load_registry(root)
        self._resolved_ids = {
            identifier: identifier if status == "active" else resolve_id(self._registry, identifier)
            for identifier, (status, _) in self._registry.states.items()
        }
        records = {}
        for sub in ("mapped", "unmapped"):
            d = root / "data" / "ingredients" / sub
            if d.is_dir():
                for path in sorted(d.glob("*.yaml")):
                    records[path.relative_to(root).as_posix()] = load_yaml(path)
        validate_records(self._registry, records)
        for relative, record in records.items():
            mim_id = record["mim_id"]
            self._records.add(mim_id)
            for alias in [
                mim_curie_for_stem(Path(relative).stem),
                *record.get("legacy_identifiers", []),
            ]:
                self._alias_targets.setdefault(alias, set()).add(mim_id)
        if self.alias_path.exists():
            with self.alias_path.open() as f:
                for row in csv.DictReader(f, delimiter="\t"):
                    old, target = row["old_curie"], row["current_curie"]
                    if old in self._aliases and self._aliases[old] != target:
                        raise ValueError(f"Conflicting historical MIM alias: {old}")
                    self._aliases[old] = target
        if self.sssom_path.exists():
            with self.sssom_path.open() as f:
                rows = csv.DictReader(
                    (line for line in f if not line.startswith("#")), delimiter="\t"
                )
                for r in rows:
                    s = (r.get("subject_id") or "").strip()
                    o = (r.get("object_id") or "").strip()
                    p = (r.get("predicate_id") or "").strip()
                    if s and o:
                        # A lifecycle redirect locates a replacement record; it
                        # does not transfer the old record's mapping evidence.
                        resolved = self._resolve_reference(s, follow_replacements=False)
                        if not resolved:
                            continue
                        if resolved.curie.startswith("MIM:"):
                            s = resolved.curie
                        self._mappings.setdefault(s, []).append((o, p))
                        self._subjects.add(s)

    # ---- syntax / prefix ------------------------------------------------

    def normalize(self, curie: str) -> Verdict:
        """Canonicalise prefix case and reject anything unrecognised or bogus."""
        raw = (curie or "").strip()
        if not raw:
            return Verdict(False, problem="EMPTY")
        m = _CURIE_RE.match(raw)
        if not m:
            return Verdict(False, problem="MALFORMED", note="expected <prefix>:<local>")
        prefix, local = m.group(1), m.group(2)
        canonical = CANONICAL_PREFIX.get(prefix.casefold())
        if canonical is None:
            return Verdict(
                False, problem="UNKNOWN_PREFIX", note=f"{prefix!r} is not a registered MIM prefix"
            )
        out = f"{canonical}:{local}"

        ceiling = MAX_ACCESSION.get(canonical)
        if ceiling and local.isdigit() and int(local) > ceiling:
            return Verdict(
                False,
                curie=out,
                problem="ACCESSION_OUT_OF_RANGE",
                note=f"{canonical} accessions do not reach {local}; "
                "this is most likely a PubChem CID",
            )
        if canonical == "MICRO" and out not in MICRO_VERIFIED:
            # The bare-Python published-CURIE gate imports this module by path
            # for its syntax/prefix constants, without installing the package.
            from mediaingredientmech.micro_source import source_term

            if source_term(out) is None:
                return Verdict(
                    False,
                    curie=out,
                    problem="MICRO_UNVERIFIED",
                    note="MICRO term has neither canonical OLS verification nor a reviewed "
                    "entry in the pinned KG-Microbe source; verify the term and its original IRI "
                    "before use",
                )
        note = "" if out == raw else f"prefix case normalised from {prefix!r}"
        return Verdict(True, curie=out, note=note)

    # ---- MIM identity ---------------------------------------------------

    def resolve(self, curie: str) -> Verdict:
        """Resolve a stable ID or unambiguous preserved alias to a current ID."""
        return self._resolve_reference(curie, follow_replacements=True)

    def _resolve_reference(self, curie: str, *, follow_replacements: bool) -> Verdict:
        """Keep address redirects separate from current mapping ownership (#1271)."""
        v = self.normalize(curie)
        if not v:
            raw = (curie or "").strip()
            if raw not in self._alias_targets and raw not in self._aliases:
                return v
            v = Verdict(True, curie=raw)
        cur = v.curie
        if re.fullmatch(r"MIM:[0-9]{7}", cur):
            target = self._resolved_ids.get(cur)
            if target is None:
                return Verdict(
                    False, curie=cur, problem="UNKNOWN_SUBJECT", note="Unregistered stable MIM ID"
                )
            if not follow_replacements and target != cur:
                return Verdict(False, curie=cur, problem="RETIRED_SUBJECT")
            return Verdict(
                True,
                curie=target,
                note=(v.note if target == cur else f"replaced retired or merged ID {cur}"),
            )
        targets: set[str] = set()
        visited: set[str] = set()
        while True:
            if cur in visited:
                return Verdict(False, curie=cur, problem="ALIAS_CYCLE")
            visited.add(cur)
            if re.fullmatch(r"MIM:[0-9]{7}", cur):
                target = self._resolved_ids.get(cur)
                if target is None:
                    return Verdict(
                        False,
                        curie=cur,
                        problem="UNKNOWN_SUBJECT",
                        note="Unregistered stable MIM ID",
                    )
                if not follow_replacements and target != cur:
                    return Verdict(False, curie=cur, problem="RETIRED_SUBJECT")
                targets.add(target)
            targets.update(self._alias_targets.get(cur, set()))
            if cur not in self._aliases:
                break
            cur = self._aliases[cur]
        if len(targets) > 1:
            return Verdict(
                False,
                curie=v.curie,
                problem="AMBIGUOUS_ALIAS",
                note="Reference belongs to multiple MIM records",
            )
        if targets:
            target = next(iter(targets))
            return Verdict(
                True,
                curie=target,
                note=(
                    "" if target == v.curie else f"resolved legacy or retired reference {v.curie}"
                ),
            )
        if v.curie.startswith("MIM:"):
            return Verdict(
                False,
                curie=v.curie,
                problem="UNKNOWN_SUBJECT",
                note="No registered current record or preserved alias resolves this reference",
            )
        return v

    # ---- the selection rule --------------------------------------------

    def equivalent_term(self, mim_curie: str) -> Verdict:
        """The single ontology term a MIM ingredient may be cited as.

        Only ``skos:exactMatch`` rows qualify; among those the highest-ranked
        prefix wins. Returns a problem verdict — never a guess — when the subject
        has no exact match, so a caller cannot mistake a ``broadMatch`` for an
        equivalence. Lifecycle redirects provide no scientific equivalence.
        """
        r = self._resolve_reference(mim_curie, follow_replacements=False)
        if not r:
            return r
        rows = self._mappings.get(r.curie, [])
        if not rows:
            return Verdict(False, curie=r.curie, problem="NO_MAPPING")
        exact = [(o, p) for o, p in rows if p in EQUIVALENT_PREDICATES]
        if not exact:
            preds = sorted({p for _, p in rows})
            return Verdict(
                False,
                curie=r.curie,
                problem="NO_EXACT_MATCH",
                note=f"only {', '.join(preds)} available; these are not "
                "equivalences and must not be cited as one",
            )
        best = min(exact, key=lambda t: (PREFIX_RANK.get(t[0].split(":", 1)[0], 99), t[0]))
        others = [o for o, _ in exact if o != best[0]]
        note = f"selected by prefix rank from {len(exact)} exact matches" if others else ""
        return Verdict(True, curie=best[0], note=note)


def _cli() -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Normalise / resolve MIM CURIEs.")
    ap.add_argument("curies", nargs="*", help="CURIEs to check (default: stdin)")
    ap.add_argument(
        "--equivalent",
        action="store_true",
        help="also resolve each MIM CURIE to its equivalent ontology term",
    )
    args = ap.parse_args()

    import sys

    items = args.curies or [line.strip() for line in sys.stdin if line.strip()]
    n = CurieNormalizer()
    bad = 0
    for c in items:
        v = n.resolve(c)
        if v:
            line = f"OK    {c}  ->  {v.curie}"
            if args.equivalent and v.curie.startswith("MIM:"):
                e = n.equivalent_term(v.curie)
                line += f"  ==  {e.curie}" if e else f"  ==  <{e.problem}>"
                if not e:
                    bad += 1
            print(line + (f"   ({v.note})" if v.note else ""))
        else:
            bad += 1
            print(f"FAIL  {c}  [{v.problem}] {v.note}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(_cli())
