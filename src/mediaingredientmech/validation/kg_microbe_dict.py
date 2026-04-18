"""
KG-Microbe unified chemical dictionary loader.

Loads the gzipped TSV at
  kg-microbe/mappings/unified_chemical_mappings.tsv.gz
and exposes two indexes:

  by_chebi:   CHEBI:X -> {canonical_name, synonyms: set[str], formula}
  by_synonym: lower(synonym) -> set[CHEBI:X]   (1:many, intentional)

Known data-quality issues the loader defends against:
  * CSV row-merge bug: fields can contain embedded quotes; csv.DictReader
    merges subsequent rows. We parse line-by-line via split("\t") instead.
  * Field-size overflow: some synonym lists exceed the default csv field
    size limit. We raise the limit as a safeguard even though we do not
    use the csv module.
  * Symmetric-synonym pollution: short cation/anion tokens appear under
    hundreds of CHEBI IDs. The by_synonym index is kept 1:many so callers
    can filter by ambiguity count.

See .claude/skills/review-ingredients/skill.md ("KG-Microbe Dictionary
Integration") for the P2.5 / P4.4 rules that consume this data.
"""

from __future__ import annotations

import csv
import gzip
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional, Set

_CURIE_RE = re.compile(r"^[A-Z][A-Za-z0-9_.]*:[A-Za-z0-9_\-]+$")

DEFAULT_DICT_PATH = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/"
    "kg-microbe/mappings/unified_chemical_mappings.tsv.gz"
)

AMBIGUITY_THRESHOLD = 5
MIN_SYNONYM_LEN = 2
# An entry with more synonyms than this is almost certainly contaminated by
# the upstream row-merge bug. Legitimate entries (enzyme superfamilies, etc.)
# cap out around 250; CHEBI:86254 observed at 50,686 in 2026-04 dump.
POLLUTION_SYNONYM_THRESHOLD = 500

csv.field_size_limit(sys.maxsize)


@dataclass
class KgMicrobeEntry:
    chebi_id: str
    canonical_name: str
    formula: str
    synonyms: Set[str] = field(default_factory=set)


class KgMicrobeDict:
    """In-memory index over kg-microbe's unified chemical mappings TSV."""

    def __init__(self, dict_path: Optional[Path] = None):
        self.dict_path = Path(dict_path) if dict_path else DEFAULT_DICT_PATH
        self._by_chebi: Dict[str, KgMicrobeEntry] = {}
        self._by_synonym: Dict[str, Set[str]] = defaultdict(set)
        self._polluted_entries: Set[str] = set()
        self._loaded = False

    def load(self) -> None:
        """Parse the gzipped TSV and build indexes. Safe to call twice."""
        if self._loaded:
            return
        if not self.dict_path.exists():
            self._loaded = True
            return

        with gzip.open(self.dict_path, "rt", encoding="utf-8") as f:
            header_line = f.readline().rstrip("\n")
            header = header_line.split("\t")
            col = {name: i for i, name in enumerate(header)}

            # Accept either legacy "chebi_id" or current "id" as the CHEBI column
            if "chebi_id" in col:
                id_col = "chebi_id"
            elif "id" in col:
                id_col = "id"
            else:
                self._loaded = True
                return

            if "synonyms" not in col or "canonical_name" not in col:
                self._loaded = True
                return

            for raw in f:
                parts = raw.rstrip("\n").split("\t")
                if len(parts) < len(header):
                    continue

                chebi_id = parts[col[id_col]].strip()
                if not chebi_id.startswith("CHEBI:"):
                    continue

                canonical = parts[col["canonical_name"]].strip()
                formula = parts[col["formula"]].strip() if "formula" in col else ""
                syn_field = parts[col["synonyms"]]

                synonyms = {
                    s.strip()
                    for s in syn_field.split("|")
                    if s.strip()
                    and len(s.strip()) >= MIN_SYNONYM_LEN
                    and s.strip() != chebi_id
                    and not _CURIE_RE.match(s.strip())
                }

                entry = self._by_chebi.get(chebi_id)
                if entry is None:
                    entry = KgMicrobeEntry(
                        chebi_id=chebi_id,
                        canonical_name=canonical,
                        formula=formula,
                        synonyms=set(synonyms),
                    )
                    self._by_chebi[chebi_id] = entry
                else:
                    entry.synonyms.update(synonyms)
                    if not entry.canonical_name and canonical:
                        entry.canonical_name = canonical
                    if not entry.formula and formula:
                        entry.formula = formula

        # Post-process: quarantine polluted entries (row-merge-bug victims).
        # Their synonyms are clearly not real, so they must not participate
        # in the by_synonym index. Canonical name stays so the CHEBI remains
        # lookupable via get_entry() for its own ID.
        for chebi_id, entry in self._by_chebi.items():
            if len(entry.synonyms) > POLLUTION_SYNONYM_THRESHOLD:
                self._polluted_entries.add(chebi_id)
                entry.synonyms = set()

        # Build reverse index only from non-polluted entries
        for chebi_id, entry in self._by_chebi.items():
            if chebi_id in self._polluted_entries:
                # still index the canonical name (safe) but not the dumped synonyms
                if entry.canonical_name:
                    self._by_synonym[entry.canonical_name.lower()].add(chebi_id)
                continue
            lookup_terms = set(entry.synonyms)
            if entry.canonical_name:
                lookup_terms.add(entry.canonical_name)
            for term in lookup_terms:
                self._by_synonym[term.lower()].add(chebi_id)

        self._loaded = True

    def get_entry(self, chebi_id: str) -> Optional[KgMicrobeEntry]:
        self.load()
        return self._by_chebi.get(chebi_id)

    def lookup_synonym(self, surface_form: str) -> Set[str]:
        """Return the set of CHEBI IDs kg-microbe associates with this surface form."""
        self.load()
        if not surface_form:
            return set()
        return set(self._by_synonym.get(surface_form.lower(), set()))

    def is_ambiguous(self, surface_form: str) -> bool:
        """True if kg-microbe maps this surface form to too many CHEBI IDs to trust."""
        return len(self.lookup_synonym(surface_form)) > AMBIGUITY_THRESHOLD

    @property
    def loaded(self) -> bool:
        return self._loaded

    @property
    def size(self) -> int:
        self.load()
        return len(self._by_chebi)
