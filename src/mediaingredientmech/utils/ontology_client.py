"""Client for searching ontology terms via OAK (oaklib)."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)

ONTOLOGY_SOURCES = {
    "CHEBI": "sqlite:obo:chebi",
    "FOODON": "sqlite:obo:foodon",
    "NCIT": "sqlite:obo:ncit",
    "MESH": "sqlite:obo:mesh",
    "UBERON": "sqlite:obo:uberon",
    "ENVO": "sqlite:obo:envo",
}


@dataclass
class OntologyCandidate:
    """A candidate ontology mapping returned from search."""

    ontology_id: str
    label: str
    source: str
    score: float = 0.0
    synonyms: list[str] = field(default_factory=list)
    definition: Optional[str] = None


class OntologyClient:
    """Search ontology databases for ingredient term matches."""

    def __init__(self, sources: Optional[list[str]] = None):
        self._sources = sources or ["CHEBI", "FOODON"]
        self._adapters: dict = {}

    def _get_adapter(self, source: str):
        """Lazily load an OAK adapter for the given source."""
        if source not in self._adapters:
            try:
                from oaklib import get_adapter

                resource = ONTOLOGY_SOURCES.get(source)
                if not resource:
                    logger.warning("Unknown ontology source: %s", source)
                    return None
                self._adapters[source] = get_adapter(resource)
            except Exception as e:
                logger.warning("Failed to load adapter for %s: %s", source, e)
                self._adapters[source] = None
        return self._adapters[source]

    def search(
        self,
        query: str,
        sources: Optional[list[str]] = None,
        max_results: int = 10,
    ) -> list[OntologyCandidate]:
        """Search ontologies for terms matching the query string.

        Args:
            query: The ingredient name to search for.
            sources: Ontology sources to search (defaults to instance sources).
            max_results: Maximum candidates to return per source.

        Returns:
            List of OntologyCandidate sorted by score (descending).
        """
        sources = sources or self._sources
        candidates: list[OntologyCandidate] = []

        for source in sources:
            adapter = self._get_adapter(source)
            if adapter is None:
                continue
            try:
                results = list(adapter.basic_search(query))
                for curie in results[:max_results]:
                    label = adapter.label(curie) or ""
                    # Compute a simple score based on label similarity
                    score = _similarity_score(query, label)
                    syns = []
                    try:
                        syns = [s for s in (adapter.entity_aliases(curie) or []) if s != label]
                    except Exception:
                        pass
                    defn = None
                    try:
                        defn = adapter.definition(curie)
                    except Exception:
                        pass
                    candidates.append(
                        OntologyCandidate(
                            ontology_id=curie,
                            label=label,
                            source=source,
                            score=score,
                            synonyms=syns,
                            definition=defn,
                        )
                    )
            except Exception as e:
                logger.warning("Search failed for source %s: %s", source, e)

        candidates.sort(key=lambda c: c.score, reverse=True)
        return candidates


def _similarity_score(query: str, label: str) -> float:
    """Simple normalized similarity between query and label."""
    q = query.lower().strip()
    l = label.lower().strip()
    if not q or not l:
        return 0.0
    if q == l:
        return 1.0
    if q in l or l in q:
        return 0.8
    # Token overlap
    q_tokens = set(q.split())
    l_tokens = set(l.split())
    if not q_tokens or not l_tokens:
        return 0.0
    overlap = len(q_tokens & l_tokens)
    return overlap / max(len(q_tokens), len(l_tokens))
