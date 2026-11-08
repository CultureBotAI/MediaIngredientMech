"""Reviewed MICRO identifiers backed by the pinned KG-Microbe ontology extract.

Some MicrO classes use legacy ``MicrO.owl/MICRO_`` IRIs. KG-Microbe assigns
them MICRO CURIEs. Keep that explicit correspondence instead of treating an
unresolvable canonical IRI as evidence that the ontology class does not exist.
Only individually reviewed entries in the manifest are accepted here.
"""

from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "ontology_sources" / "micro"


@dataclass(frozen=True)
class MicroTerm:
    """A reviewed source identifier, label, original IRI and parent references."""

    curie: str
    label: str
    iri: str
    parents: tuple[str, ...]


def load_source(directory: Path = SOURCE) -> dict[str, MicroTerm]:
    """Validate the archived evidence before admitting any source-backed term."""
    manifest = json.loads((directory / "manifest.json").read_text())
    tables = {}
    for filename in ("micro_nodes.tsv", "micro_edges.tsv", "legacy_nodes.tsv"):
        path = directory / filename
        expected = manifest["files"][filename]
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected["sha256"]:
            raise ValueError(f"MICRO source checksum mismatch: {filename}")
        with path.open(encoding="utf-8", newline="") as handle:
            tables[filename] = list(csv.DictReader(handle, delimiter="\t"))
        if len(tables[filename]) != expected["records"]:
            raise ValueError(f"MICRO source row count mismatch: {filename}")
    nodes = {row["id"]: row for row in tables["micro_nodes.tsv"]}
    legacy = {row["id"]: row for row in tables["legacy_nodes.tsv"]}
    terms = {}
    for curie, reviewed in manifest["reviewed_terms"].items():
        iri = reviewed["iri"]
        expected_iri = "http://purl.obolibrary.org/obo/MicrO.owl/" + curie.replace(":", "_")
        if iri != expected_iri:
            raise ValueError(f"MICRO source IRI mismatch: {curie}")
        legacy_id = iri.replace("http://purl.obolibrary.org/obo/", "OBO:")
        for node in (nodes.get(curie), legacy.get(legacy_id)):
            if (
                not node
                or node["name"] != reviewed["label"]
                or node.get("deprecated", "").lower() not in {"", "false", "0"}
            ):
                raise ValueError(f"MICRO source label or status mismatch: {curie}")
        parents = tuple(
            sorted(
                row["object"]
                for row in tables["micro_edges.tsv"]
                if row["subject"] == curie and row["predicate"] == "biolink:subclass_of"
            )
        )
        if not parents or list(parents) != sorted(reviewed["parents"]):
            raise ValueError(f"MICRO source parent mismatch: {curie}")
        if any(parent not in nodes for parent in parents):
            raise ValueError(f"MICRO source parent node missing: {curie}")
        terms[curie] = MicroTerm(curie, reviewed["label"], iri, parents)
    return terms


@lru_cache(maxsize=1)
def _reviewed_terms() -> dict[str, MicroTerm]:
    return load_source()


def source_term(curie: str) -> MicroTerm | None:
    """Resolve a reviewed term, without admitting other nodes in the snapshot."""
    return _reviewed_terms().get(curie)
