"""
KG-Microbe unified entity dictionary loader.

Reads kg-microbe's published SSSOM mapping set

  kg-microbe/mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz

and reconstructs a per-entity view of it, exposing two indexes:

  by_chebi:   CHEBI:X -> {canonical_name, synonyms: set[str], formula}
  by_synonym: lower(synonym) -> set[CHEBI:X]   (1:many, intentional)

The published set is a long triple table, one row per mapping, so the
per-entity view is rebuilt by grouping on ``object_id`` -- the read pattern
kg-microbe's own ``mappings/README.md`` documents. Per row:

  object_id       the entity's primary key; only CHEBI:* is kept here
  object_label    its canonical name, repeated on every row for the entity
  object_formula  its chemical formula, likewise repeated
  subject_id      a ``kgm.name:*`` subject means the row carries a surface
                  form for the entity; any other prefix is an xref
  subject_label   that surface form
  predicate_id    skos:exactMatch on a kgm.name subject is the entity's own
                  name; skos:closeMatch is a synonym of it

Before 2026-09 this module read a wide per-entity TSV,
``mappings/unified_chemical_mappings.tsv.gz``, which kg-microbe deleted on
2026-04-30. Nothing noticed for four months, because a missing file made
``load()`` return quietly and the reviewer then disabled the checks: a clean
review looked exactly like a review that never ran (#578). Every path that
cannot produce a dictionary now says so through the module logger.

Known data-quality issues the loader defends against:
  * Symmetric-synonym pollution: short cation/anion tokens appear under
    hundreds of CHEBI IDs. The by_synonym index is kept 1:many so callers
    can filter by ambiguity count, and an entry whose synonym list is
    implausibly long is quarantined out of that index entirely.

See .claude/skills/review-ingredients/SKILL.md ("KG-Microbe Dictionary
Integration") for the P2.5 / P4.4 rules that consume this data.
"""

from __future__ import annotations

import gzip
import hashlib
import logging
import os
import re
import sqlite3
import tempfile
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import TextIO

logger = logging.getLogger(__name__)

_CURIE_RE = re.compile(r"^[A-Z][A-Za-z0-9_.]*:[A-Za-z0-9_\-]+$")

REPO_ROOT = Path(__file__).resolve().parents[3]

#: Environment variable naming the kg-microbe checkout, as the fleet spells it.
KGMICROBE_ROOT_ENV = "KGMICROBE_ROOT"

#: Where the published mapping set sits inside that checkout.
ARTIFACT_RELPATH = Path("mappings") / "kgmicrobe_unified_entity_mappings.sssom.tsv.gz"

#: Subject prefix marking a row that carries a surface form rather than an xref.
NAME_SUBJECT_PREFIX = "kgm.name:"

#: Predicate marking the entity's own name; anything else on a name row is a synonym.
CANONICAL_PREDICATE = "skos:exactMatch"

#: Predicates whose name rows assert an equivalent surface form for the entity.
#: ``skos:narrowMatch`` is deliberately absent: a narrower term's name is not a
#: synonym of the broader entity, and proposing it as one would be a mapping
#: error rather than an enrichment (#585). No such row exists in the current
#: artifact, so this is a guard against the emitter changing, not a fix.
SURFACE_FORM_PREDICATES = frozenset({"skos:exactMatch", "skos:closeMatch"})

AMBIGUITY_THRESHOLD = 5
MIN_SYNONYM_LEN = 2
# An entry with more synonyms than this is almost certainly contaminated by
# upstream symmetric-synonym propagation. Legitimate entries (enzyme
# superfamilies, etc.) cap out around 250; CHEBI:86254 observed at 50,686 in
# the 2026-04 dump.
POLLUTION_SYNONYM_THRESHOLD = 500

_REQUIRED_COLUMNS = ("subject_id", "subject_label", "predicate_id", "object_id", "object_label")

#: Overrides where the parsed index is cached. Tests point it at a tmpdir.
CACHE_DIR_ENV = "MEDIAINGREDIENTMECH_CACHE_DIR"

#: Bumping this invalidates every cache built by an older parser, which is how
#: a change to the grouping rules reaches an operator who already has one.
CACHE_SCHEMA_VERSION = 1

#: Read in 1MB blocks: the artifact is ~13MB and hashing it is ~50ms, against
#: the ~5.4s parse the hash is there to avoid.
_HASH_BLOCK = 1 << 20


def cache_dir() -> Path:
    """
    Return the directory holding parsed dictionary indexes.

    ``MEDIAINGREDIENTMECH_CACHE_DIR`` wins, then ``XDG_CACHE_HOME``, then
    ``~/.cache``. A dot-directory under home is a tool cache, not a checkout,
    which is why the machine-path guard allows it.

    :return: The cache directory. Not created here.
    """
    override = os.environ.get(CACHE_DIR_ENV)
    if override and override.strip():
        return Path(override.strip()).expanduser()
    xdg = os.environ.get("XDG_CACHE_HOME")
    base = Path(xdg.strip()).expanduser() if xdg and xdg.strip() else Path.home() / ".cache"
    return base / "mediaingredientmech"


def kgmicrobe_root() -> Path | None:
    """
    Return the kg-microbe checkout root, or None when it cannot be located.

    ``KGMICROBE_ROOT`` wins when it is set to a non-empty value; an exported
    but empty variable is treated as unset rather than as the current
    directory, and a leading ``~`` is expanded (MediaIngredientMech#580).
    Otherwise fall back to a sibling of this checkout, which is where the
    fleet convention puts it.

    :return: The checkout root, or None when neither candidate exists.
    """
    override = os.environ.get(KGMICROBE_ROOT_ENV)
    if override and override.strip():
        return Path(override.strip()).expanduser()
    sibling = REPO_ROOT.parent / "kg-microbe"
    return sibling if sibling.is_dir() else None


def resolve_default_dict_path() -> Path | None:
    """
    Return the path to kg-microbe's published mapping set, if it can be found.

    :return: Path to the artifact, or None when the checkout cannot be located.
    """
    root = kgmicrobe_root()
    return root / ARTIFACT_RELPATH if root is not None else None


def _open_text(path: Path) -> TextIO:
    """
    Open a mapping set that may or may not be gzipped.

    :param path: File to open.
    :return: A text-mode file object.
    """
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8")
    return path.open("rt", encoding="utf-8")


@dataclass
class KgMicrobeEntry:
    chebi_id: str
    canonical_name: str
    formula: str
    synonyms: set[str] = field(default_factory=set)


class KgMicrobeDict:
    """In-memory per-entity index over kg-microbe's unified SSSOM mapping set."""

    def __init__(self, dict_path: Path | None = None, *, use_cache: bool = True):
        self.dict_path = Path(dict_path) if dict_path else resolve_default_dict_path()
        self.use_cache = use_cache
        self._by_chebi: dict[str, KgMicrobeEntry] = {}
        self._by_synonym: dict[str, set[str]] = defaultdict(set)
        self._polluted_entries: set[str] = set()
        self._surface_forms: dict[str, set[str]] = defaultdict(set)
        self._db: sqlite3.Connection | None = None
        self._cache_target: Path | None = None
        self._loaded = False

    def load(self) -> None:
        """
        Parse the mapping set and build the indexes. Safe to call twice.

        Every unusable outcome is logged rather than swallowed: an
        unlocatable checkout, a missing file, and a table whose columns are
        not the ones this loader groups on all leave the dictionary empty,
        and each says why (#578).

        :return: None.
        """
        if self._loaded:
            return
        self._loaded = True

        if self.dict_path is None:
            logger.warning(
                "kg-microbe dictionary unavailable: no kg-microbe checkout found. "
                "Set %s to the checkout root (expected %s inside it). "
                "P2.5/P4.4 cross-reference checks will not run.",
                KGMICROBE_ROOT_ENV,
                ARTIFACT_RELPATH,
            )
            return

        if not self.dict_path.exists():
            logger.warning(
                "kg-microbe dictionary unavailable: %s does not exist. "
                "Set %s to a checkout that publishes %s. "
                "P2.5/P4.4 cross-reference checks will not run.",
                self.dict_path,
                KGMICROBE_ROOT_ENV,
                ARTIFACT_RELPATH,
            )
            return

        if self.use_cache and self._open_cache():
            return

        try:
            with _open_text(self.dict_path) as handle:
                header = self._read_header(handle)
                if header is None:
                    return
                col = {name: i for i, name in enumerate(header)}
                missing = [name for name in _REQUIRED_COLUMNS if name not in col]
                if missing:
                    logger.warning(
                        "kg-microbe dictionary unavailable: %s is missing the column(s) %s "
                        "this loader groups on. Expected kg-microbe's unified SSSOM mapping "
                        "set. P2.5/P4.4 cross-reference checks will not run.",
                        self.dict_path,
                        ", ".join(missing),
                    )
                    return
                self._ingest_rows(handle, col)
        except (OSError, EOFError, UnicodeDecodeError) as exc:
            # A truncated or corrupt artifact must not abort a review that is
            # otherwise fine, and a half-built index must not be served as a
            # complete one (#586).
            self._by_chebi.clear()
            self._surface_forms.clear()
            logger.warning(
                "kg-microbe dictionary unavailable: %s could not be read (%s: %s). "
                "P2.5/P4.4 cross-reference checks will not run.",
                self.dict_path,
                type(exc).__name__,
                exc,
            )
            return

        self._quarantine_polluted()
        self._build_synonym_index()
        # The staging map has been folded into the entries and the reverse
        # index; holding a second copy of every surface form for the life of
        # the process is pure overhead (#589).
        self._surface_forms.clear()
        if self.use_cache:
            self._write_cache()
        logger.info(
            "kg-microbe dictionary loaded from %s: %d CHEBI entities, "
            "%d indexed surface forms, %d quarantined as polluted",
            self.dict_path,
            len(self._by_chebi),
            len(self._by_synonym),
            len(self._polluted_entries),
        )

    def _read_header(self, handle: Iterable[str]) -> list[str] | None:
        """
        Return the column names, skipping the SSSOM ``#`` metadata block.

        :param handle: Open text handle positioned at the start of the file.
        :return: Column names, or None when the file holds no header row.
        """
        for raw in handle:
            if raw.startswith("#"):
                continue
            line = raw.rstrip("\n")
            if not line.strip():
                continue
            return line.split("\t")
        logger.warning(
            "kg-microbe dictionary unavailable: %s has no header row. "
            "P2.5/P4.4 cross-reference checks will not run.",
            self.dict_path,
        )
        return None

    def _ingest_rows(self, handle: Iterable[str], col: dict[str, int]) -> None:
        """
        Group the triple rows into per-entity records.

        :param handle: Open text handle positioned just after the header.
        :param col: Column-name to index mapping.
        :return: None.
        """
        width = max(col.values()) + 1
        formula_idx = col.get("object_formula")
        for raw in handle:
            if raw.startswith("#"):
                continue
            parts = raw.rstrip("\n").split("\t")
            if len(parts) < width:
                continue

            chebi_id = parts[col["object_id"]].strip()
            if not chebi_id.startswith("CHEBI:"):
                continue

            canonical = parts[col["object_label"]].strip()
            formula = parts[formula_idx].strip() if formula_idx is not None else ""

            entry = self._by_chebi.get(chebi_id)
            if entry is None:
                entry = KgMicrobeEntry(chebi_id=chebi_id, canonical_name=canonical, formula=formula)
                self._by_chebi[chebi_id] = entry
            else:
                if not entry.canonical_name and canonical:
                    entry.canonical_name = canonical
                if not entry.formula and formula:
                    entry.formula = formula

            if not parts[col["subject_id"]].strip().startswith(NAME_SUBJECT_PREFIX):
                continue  # an xref row carries no surface form
            if parts[col["predicate_id"]].strip() not in SURFACE_FORM_PREDICATES:
                continue  # e.g. a narrowMatch name, which is not an equivalent (#585)
            surface = parts[col["subject_label"]].strip()
            if not self._is_usable_surface_form(surface, chebi_id):
                continue
            self._surface_forms[chebi_id].add(surface)

    @staticmethod
    def _is_usable_surface_form(surface: str, chebi_id: str) -> bool:
        """
        Report whether a surface form is worth indexing.

        Drops the entity's own CURIE and bare identifiers of any kind: a
        ``kgm.name`` row whose label is ``CAS:50-99-7`` is a registry code
        wearing a name's clothing, and matching MIM records against it would
        be noise.

        :param surface: The candidate surface form.
        :param chebi_id: The entity it was found under.
        :return: True when the form should be indexed.
        """
        return bool(
            surface
            and len(surface) >= MIN_SYNONYM_LEN
            and surface != chebi_id
            and not _CURIE_RE.match(surface)
        )

    def _quarantine_polluted(self) -> None:
        """
        Drop the synonym sets of entries whose size marks them as contaminated.

        The canonical name survives, so the entity stays reachable through
        :meth:`get_entry` and by its own name.

        :return: None.
        """
        for chebi_id, entry in self._by_chebi.items():
            forms = self._surface_forms.get(chebi_id, set())
            if len(forms) > POLLUTION_SYNONYM_THRESHOLD:
                self._polluted_entries.add(chebi_id)
                continue
            # The canonical name is not itself a synonym; P4.4 proposes from
            # this set and must not offer the name the entity already has.
            entry.synonyms = {f for f in forms if f.lower() != entry.canonical_name.lower()}

    def _build_synonym_index(self) -> None:
        """
        Build the reverse surface-form index, skipping quarantined entries.

        :return: None.
        """
        for chebi_id, entry in self._by_chebi.items():
            lookup_terms = set() if chebi_id in self._polluted_entries else set(entry.synonyms)
            if entry.canonical_name:
                lookup_terms.add(entry.canonical_name)
            for term in lookup_terms:
                self._by_synonym[term.lower()].add(chebi_id)

    # -- on-disk index ----------------------------------------------------
    #
    # Parsing 610,248 rows into 119,462 entities costs ~5.4s and ~350MB. A
    # batch amortises that; reviewing a single record does not, and reviewing
    # one record is what `review_ingredient.py` does (#589). The parse is a
    # pure function of the artifact's bytes, so it is done once and kept in a
    # SQLite index keyed by the artifact's content hash. Later runs answer the
    # handful of lookups a record needs straight from disk.

    def _fingerprint(self) -> str | None:
        """
        Return the artifact's content hash, or None when it cannot be read.

        Keyed on content rather than mtime so a republished-but-identical
        artifact reuses its index, and a changed one can never hit a stale
        entry.

        :return: Hex sha256, or None.
        """
        assert self.dict_path is not None
        digest = hashlib.sha256()
        try:
            with self.dict_path.open("rb") as handle:
                for block in iter(lambda: handle.read(_HASH_BLOCK), b""):
                    digest.update(block)
        except OSError as exc:
            logger.warning("could not hash %s (%s); not using a cache", self.dict_path, exc)
            return None
        return digest.hexdigest()

    def _cache_path(self) -> Path | None:
        """
        Return this artifact's index path, or None when it cannot be keyed.

        :return: Path to the SQLite index, or None.
        """
        fingerprint = self._fingerprint()
        if fingerprint is None:
            return None
        return cache_dir() / f"kgm-dict-v{CACHE_SCHEMA_VERSION}-{fingerprint[:32]}.sqlite"

    def _open_cache(self) -> bool:
        """
        Attach an existing index for this artifact, if there is a usable one.

        A cache that is missing, corrupt, or written by a different schema is
        simply not used -- the parse still works, so a bad cache must never be
        an error. A corrupt one is deleted so the next run rebuilds it rather
        than failing the same way forever.

        :return: True when queries will be served from disk.
        """
        path = self._cache_path()
        if path is None or not path.exists():
            self._cache_target = path
            return False
        try:
            db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
            count = db.execute("SELECT count(*) FROM entity").fetchone()[0]
        except (sqlite3.Error, OSError) as exc:
            logger.warning("discarding unusable dictionary cache %s (%s)", path, exc)
            path.unlink(missing_ok=True)
            self._cache_target = path
            return False
        self._db = db
        self._cache_target = path
        # Keep the quarantine set visible on this path too, so a warm instance
        # reports the same state as the one that built the index rather than
        # silently claiming nothing was quarantined.
        self._polluted_entries = {
            chebi_id for (chebi_id,) in db.execute("SELECT chebi_id FROM entity WHERE polluted = 1")
        }
        logger.info("kg-microbe dictionary served from cache %s (%d entities)", path, count)
        return True

    def _write_cache(self) -> None:
        """
        Persist the parsed view so the next run does not repeat the parse.

        Written to a temporary file and renamed, so a concurrent reader never
        sees a half-built index and two racing builders cannot corrupt one.
        Any failure is logged and ignored: a cache is an optimisation, and
        losing it must not cost a review.

        :return: None.
        """
        # Reuse the path _open_cache already derived; recomputing it would
        # re-hash the whole artifact for nothing.
        path = self._cache_target or self._cache_path()
        if path is None or not self._by_chebi:
            return
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            handle, tmp_name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
            os.close(handle)
            tmp = Path(tmp_name)
            db = sqlite3.connect(tmp)
            with db:
                # No separate reverse-index table: it would repeat every
                # surface form a third time. A lowercased column on each of the
                # two tables that already hold the strings answers the same
                # query, and `lookup_synonym` unions them. Lowercasing happens
                # in Python so it matches the in-memory path exactly -- SQLite's
                # NOCASE collation folds ASCII only, and these names are not.
                db.execute(
                    "CREATE TABLE entity (chebi_id TEXT PRIMARY KEY, canonical_name TEXT, "
                    "canonical_lower TEXT, formula TEXT, polluted INTEGER)"
                )
                db.execute("CREATE TABLE synonym (chebi_id TEXT, surface TEXT, surface_lower TEXT)")
                db.executemany(
                    "INSERT INTO entity VALUES (?, ?, ?, ?, ?)",
                    (
                        (
                            e.chebi_id,
                            e.canonical_name,
                            e.canonical_name.lower(),
                            e.formula,
                            int(e.chebi_id in self._polluted_entries),
                        )
                        for e in self._by_chebi.values()
                    ),
                )
                db.executemany(
                    "INSERT INTO synonym VALUES (?, ?, ?)",
                    (
                        (e.chebi_id, syn, syn.lower())
                        for e in self._by_chebi.values()
                        for syn in e.synonyms
                    ),
                )
                db.execute("CREATE INDEX synonym_lower ON synonym (surface_lower)")
                db.execute("CREATE INDEX synonym_chebi ON synonym (chebi_id)")
                db.execute("CREATE INDEX entity_lower ON entity (canonical_lower)")
            db.execute("VACUUM")
            db.close()
            tmp.replace(path)
            logger.info("wrote kg-microbe dictionary cache %s", path)
        except (sqlite3.Error, OSError) as exc:
            logger.warning("could not write dictionary cache (%s); continuing", exc)

    def get_entry(self, chebi_id: str) -> KgMicrobeEntry | None:
        self.load()
        if self._db is not None:
            row = self._db.execute(
                "SELECT canonical_name, formula FROM entity WHERE chebi_id = ?", (chebi_id,)
            ).fetchone()
            if row is None:
                return None
            synonyms = {
                s
                for (s,) in self._db.execute(
                    "SELECT surface FROM synonym WHERE chebi_id = ?", (chebi_id,)
                )
            }
            return KgMicrobeEntry(chebi_id, row[0], row[1], synonyms)
        return self._by_chebi.get(chebi_id)

    def lookup_synonym(self, surface_form: str) -> set[str]:
        """Return the set of CHEBI IDs kg-microbe associates with this surface form."""
        self.load()
        if not surface_form:
            return set()
        if self._db is not None:
            form = surface_form.lower()
            return {
                chebi_id
                for (chebi_id,) in self._db.execute(
                    "SELECT chebi_id FROM entity WHERE canonical_lower = ? "
                    "UNION SELECT chebi_id FROM synonym WHERE surface_lower = ?",
                    (form, form),
                )
            }
        return set(self._by_synonym.get(surface_form.lower(), set()))

    def is_ambiguous(self, surface_form: str) -> bool:
        """True if kg-microbe maps this surface form to too many CHEBI IDs to trust."""
        return len(self.lookup_synonym(surface_form)) > AMBIGUITY_THRESHOLD

    def close(self) -> None:
        """
        Release the on-disk index, if one is attached.

        A CLI exits and the handle goes with it, but a long-lived caller that
        builds many dictionaries would otherwise hold one descriptor each.

        :return: None.
        """
        if self._db is not None:
            self._db.close()
            self._db = None

    def __enter__(self) -> KgMicrobeDict:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    @property
    def loaded(self) -> bool:
        return self._loaded

    @property
    def size(self) -> int:
        self.load()
        if self._db is not None:
            return int(self._db.execute("SELECT count(*) FROM entity").fetchone()[0])
        return len(self._by_chebi)
