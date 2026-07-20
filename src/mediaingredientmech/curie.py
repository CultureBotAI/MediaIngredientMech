"""Canonical CURIE handling for MediaIngredientMech.

Answers three questions that external repos kept having to answer for themselves,
each of which had a wrong-but-plausible default (see issue #119):

1. **Is this CURIE syntactically valid, and is its prefix one we recognise?**
   A typo'd prefix (``CHBEI:``) must not silently pass as an unknown-but-fine
   identifier, and a foreign identifier wearing an OBO prefix (a PubChem CID as
   ``CHEBI:10716816``) must not pass as a real term.

2. **Has this MIM CURIE been renamed?** ``MIM:<name>`` is derived from the
   ingredient YAML's filename, and filenames move — 205 renames to date. A
   consumer holding an old CURIE needs it to still resolve.

3. **Which ontology term does a MIM ingredient "mean"?** 180 of 1,876 subjects
   carry more than one mapping (typically CHEBI + cas + kgmicrobe.compound), so
   this is a selection rule, not a lookup — and only ``skos:exactMatch`` rows are
   safe to treat as equivalences at all.

Nothing here does network I/O; it reads the published SSSOM and alias map.
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
CANONICAL_PREFIX = {p.casefold(): p for p in (
    "MIM", "CHEBI", "FOODON", "UBERON", "ENVO", "NCIT", "MICRO", "BTO", "GO",
    "NCBITaxon", "mesh", "cas", "kgmicrobe.compound", "kgmicrobe.ingredient",
    "mediadive.ingredient", "mediadive.medium", "mediadive.solution",
    "CultureMech", "CommunityMech", "TraitMech",
)}

# Accession ceilings. This is a WEAK heuristic and is deliberately loose: real
# CHEBI accessions reach at least 747,127 (gepotidacin), while the PubChem CIDs
# that turned up wearing a CHEBI prefix include 6-digit values (503742, 867561)
# that sit *inside* the real range. So a ceiling can only catch the egregious
# cases — it is not a substitute for checking that the id actually resolves, and
# must never be the sole reason to reject an id that an ontology can confirm.
MAX_ACCESSION = {
    "CHEBI": 1_000_000, "FOODON": 4_000_000, "UBERON": 9_000_000,
    "ENVO": 9_000_000, "NCIT": 900_000, "GO": 3_000_000,
}

# Preference when a subject carries several mappings. Ontology terms first
# (they carry semantics), then registry identifiers, then local placeholders.
PREFIX_RANK = {
    "CHEBI": 0, "FOODON": 1, "UBERON": 2, "ENVO": 3, "MICRO": 4, "BTO": 5,
    "NCIT": 6, "GO": 7, "mesh": 8, "cas": 9,
    "kgmicrobe.compound": 10, "kgmicrobe.ingredient": 11,
}

# Only these assert that subject and object denote the same thing. narrowMatch
# in particular means the MIM subject is MORE specific, so treating the object as
# an equivalent silently generalises the ingredient.
EQUIVALENT_PREDICATES = {"skos:exactMatch"}

_CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_.]*):([A-Za-z0-9_.~%\-]+)$")


def mim_curie_for_stem(stem: str) -> str:
    """`MIM:<stem>` with non-URL-safe characters ~HEX escaped.

    Must stay identical to build_mim_ingredient_sssom._mim_curie, or records on
    disk will not line up with the CURIEs the SSSOM publishes.
    """
    safe = re.sub(r"[^A-Za-z0-9_\-.]", lambda m: f"~{ord(m.group(0)):02X}", stem)
    return f"MIM:{safe}"

# MicrO mints ~1,472 of its 3,450 classes under a malformed IRI
# (…/obo/MicrO.owl/MICRO_nnnnnnn). Those CURIEs do not round-trip, and the defect
# is only visible against OLS (is_defining_ontology + IRI shape), so it cannot be
# detected offline. This is the set verified good against OLS4; anything outside
# it is refused rather than guessed at.
#
# Regenerate with: python scripts/verify_micro_ids.py
#
# KNOWN BAD, and currently present in the published SSSOM — these need
# re-grounding, see issue #119 follow-up:
#   MICRO:0002250 "V-8 juice", MICRO:0002392 "rabbit serum",
#   MICRO:0002393 "Proteose Peptone No. 2"
MICRO_VERIFIED = {
    "MICRO:0000082", "MICRO:0000094", "MICRO:0000113", "MICRO:0000114",
    "MICRO:0000175", "MICRO:0000176", "MICRO:0000178", "MICRO:0000180",
    "MICRO:0000182", "MICRO:0000183", "MICRO:0000193", "MICRO:0000253",
    "MICRO:0000307", "MICRO:0000455", "MICRO:0000457", "MICRO:0000460",
    "MICRO:0000462", "MICRO:0000522", "MICRO:0000536", "MICRO:0000541",
    "MICRO:0000568", "MICRO:0000570", "MICRO:0000594", "MICRO:0000595",
    "MICRO:0000606", "MICRO:0001229", "MICRO:0001235", "MICRO:0001238",
    "MICRO:0001349", "MICRO:0001362", "MICRO:0001363", "MICRO:0001365",
    "MICRO:0001366", "MICRO:0001574", "MICRO:0001597", "MICRO:0001647",
    "MICRO:0001668", "MICRO:0001709", "MICRO:0001773"
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

    sssom_path: Path = SSSOM
    alias_path: Path = ALIASES
    _aliases: dict[str, str] = field(default_factory=dict, repr=False)
    _mappings: dict[str, list[tuple[str, str]]] = field(default_factory=dict, repr=False)
    _subjects: set[str] = field(default_factory=set, repr=False)
    _records: set[str] = field(default_factory=set, repr=False)

    def __post_init__(self) -> None:
        # Known MIM CURIEs are the RECORDS on disk, not just the SSSOM subjects:
        # unmapped records are legitimate ingredients that carry no mapping yet,
        # so validating against the SSSOM alone would reject them.
        for sub in ("mapped", "unmapped"):
            d = REPO / "data" / "ingredients" / sub
            if d.is_dir():
                self._records |= {mim_curie_for_stem(p.stem) for p in d.glob("*.yaml")}
        if self.alias_path.exists():
            with self.alias_path.open() as f:
                self._aliases = {r["old_curie"]: r["current_curie"]
                                 for r in csv.DictReader(f, delimiter="\t")}
        if self.sssom_path.exists():
            with self.sssom_path.open() as f:
                rows = csv.DictReader((l for l in f if not l.startswith("#")),
                                      delimiter="\t")
                for r in rows:
                    s = (r.get("subject_id") or "").strip()
                    o = (r.get("object_id") or "").strip()
                    p = (r.get("predicate_id") or "").strip()
                    if s and o:
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
            return Verdict(False, problem="MALFORMED",
                           note="expected <prefix>:<local>")
        prefix, local = m.group(1), m.group(2)
        canonical = CANONICAL_PREFIX.get(prefix.casefold())
        if canonical is None:
            return Verdict(False, problem="UNKNOWN_PREFIX",
                           note=f"{prefix!r} is not a registered MIM prefix")
        out = f"{canonical}:{local}"

        ceiling = MAX_ACCESSION.get(canonical)
        if ceiling and local.isdigit() and int(local) > ceiling:
            return Verdict(False, curie=out, problem="ACCESSION_OUT_OF_RANGE",
                           note=f"{canonical} accessions do not reach {local}; "
                                "this is most likely a PubChem CID")
        if canonical == "MICRO" and out not in MICRO_VERIFIED:
            return Verdict(False, curie=out, problem="MICRO_UNVERIFIED",
                           note="MicrO has ~1,472 classes under a malformed IRI that "
                                "do not round-trip; verify is_defining_ontology=true "
                                "on OLS4 and add to MICRO_VERIFIED before use")
        note = "" if out == raw else f"prefix case normalised from {prefix!r}"
        return Verdict(True, curie=out, note=note)

    # ---- MIM identity ---------------------------------------------------

    def resolve(self, curie: str) -> Verdict:
        """Normalise, then follow any MIM rename to the CURIE in use today."""
        v = self.normalize(curie)
        if not v:
            return v
        cur = v.curie
        if not cur.startswith("MIM:"):
            return v
        hops = 0
        while cur in self._aliases and hops < 10:
            cur = self._aliases[cur]
            hops += 1
        if hops:
            return Verdict(True, curie=cur,
                           note=f"renamed from {v.curie} ({hops} hop(s)); "
                                "MIM:<name> is filename-derived and not rename-stable")
        known = self._records or self._subjects
        if known and cur not in known:
            return Verdict(False, curie=cur, problem="UNKNOWN_SUBJECT",
                           note="not a subject in the published SSSOM, and no alias "
                                "maps it to one")
        return v

    # ---- the selection rule --------------------------------------------

    def equivalent_term(self, mim_curie: str) -> Verdict:
        """The single ontology term a MIM ingredient may be cited as.

        Only ``skos:exactMatch`` rows qualify; among those the highest-ranked
        prefix wins. Returns a problem verdict — never a guess — when the subject
        has no exact match, so a caller cannot mistake a ``narrowMatch`` for an
        equivalence.
        """
        r = self.resolve(mim_curie)
        if not r:
            return r
        rows = self._mappings.get(r.curie, [])
        if not rows:
            return Verdict(False, curie=r.curie, problem="NO_MAPPING")
        exact = [(o, p) for o, p in rows if p in EQUIVALENT_PREDICATES]
        if not exact:
            preds = sorted({p for _, p in rows})
            return Verdict(False, curie=r.curie, problem="NO_EXACT_MATCH",
                           note=f"only {', '.join(preds)} available; these are not "
                                "equivalences and must not be cited as one")
        best = min(exact, key=lambda t: (PREFIX_RANK.get(t[0].split(":", 1)[0], 99),
                                         t[0]))
        others = [o for o, _ in exact if o != best[0]]
        note = f"selected by prefix rank from {len(exact)} exact matches" if others else ""
        return Verdict(True, curie=best[0], note=note)


def _cli() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Normalise / resolve MIM CURIEs.")
    ap.add_argument("curies", nargs="*", help="CURIEs to check (default: stdin)")
    ap.add_argument("--equivalent", action="store_true",
                    help="also resolve each MIM CURIE to its equivalent ontology term")
    args = ap.parse_args()

    import sys
    items = args.curies or [l.strip() for l in sys.stdin if l.strip()]
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
