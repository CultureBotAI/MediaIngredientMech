"""Core curation logic: mapping workflow, validation, and history tracking."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import yaml

from mediaingredientmech.utils.ontology_client import OntologyCandidate, OntologyClient

logger = logging.getLogger(__name__)

DEFAULT_UNMAPPED_PATH = Path("data/curated/unmapped_ingredients.yaml")

VALID_STATUSES = {
    "MAPPED",
    "UNMAPPED",
    "PENDING_REVIEW",
    "IN_PROGRESS",
    "NEEDS_EXPERT",
    "AMBIGUOUS",
    "REJECTED",
}

VALID_QUALITY = {
    "EXACT_MATCH",
    "SYNONYM_MATCH",
    "CLOSE_MATCH",
    "MANUAL_CURATION",
    "LLM_ASSISTED",
    "PROVISIONAL",
}

VALID_MATCH_LEVEL = {
    "EXACT",
    "NORMALIZED",
    "FUZZY",
    "MANUAL",
    "UNMAPPABLE",
    "UNKNOWN",
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class IngredientCurator:
    """Manages the curation workflow for ingredient records."""

    def __init__(
        self,
        data_path: Optional[Path] = None,
        curator_name: str = "anonymous",
        ontology_client: Optional[OntologyClient] = None,
    ):
        self.data_path = data_path or DEFAULT_UNMAPPED_PATH
        self.curator_name = curator_name
        self.ontology_client = ontology_client or OntologyClient()
        self._collection: dict[str, Any] = {}
        self._records: list[dict[str, Any]] = []
        self._dirty = False

    def load(self) -> list[dict[str, Any]]:
        """Load ingredient records from YAML file."""
        path = Path(self.data_path)
        if not path.exists():
            logger.warning("Data file not found: %s", path)
            self._collection = {
                "generation_date": _now_iso(),
                "total_count": 0,
                "mapped_count": 0,
                "unmapped_count": 0,
                "ingredients": [],
            }
            self._records = []
            return self._records

        with open(path) as f:
            data = yaml.safe_load(f) or {}

        self._collection = data
        self._records = data.get("ingredients", []) or []
        return self._records

    def save(self) -> None:
        """Save current state back to YAML file."""
        path = Path(self.data_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        # Update counts
        mapped = sum(1 for r in self._records if r.get("mapping_status") == "MAPPED")
        unmapped = sum(1 for r in self._records if r.get("mapping_status") == "UNMAPPED")
        self._collection["total_count"] = len(self._records)
        self._collection["mapped_count"] = mapped
        self._collection["unmapped_count"] = unmapped
        self._collection["ingredients"] = self._records

        with open(path, "w") as f:
            yaml.dump(self._collection, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        self._dirty = False
        logger.info("Saved %d records to %s", len(self._records), path)

    @property
    def records(self) -> list[dict[str, Any]]:
        return self._records

    @property
    def is_dirty(self) -> bool:
        return self._dirty

    def get_unmapped(self) -> list[dict[str, Any]]:
        """Get unmapped records sorted by occurrence count (most common first)."""
        unmapped = [r for r in self._records if r.get("mapping_status") in ("UNMAPPED", "PENDING_REVIEW")]
        unmapped.sort(
            key=lambda r: (r.get("occurrence_statistics") or {}).get("total_occurrences", 0),
            reverse=True,
        )
        return unmapped

    def search_ontologies(
        self, query: str, sources: Optional[list[str]] = None
    ) -> list[OntologyCandidate]:
        """Search ontologies for a query term."""
        return self.ontology_client.search(query, sources=sources)

    def accept_mapping(
        self,
        record: dict[str, Any],
        candidate: OntologyCandidate,
        quality: str = "MANUAL_CURATION",
        match_level: str = "MANUAL",
        llm_assisted: bool = False,
        llm_model: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> dict[str, Any]:
        """Accept an ontology mapping for a record.

        Args:
            record: The ingredient record dict to update.
            candidate: The selected OntologyCandidate.
            quality: MappingQualityEnum value.
            match_level: MatchLevelEnum value indicating how mapping was found.
            llm_assisted: Whether LLM helped with this mapping.
            llm_model: LLM model identifier if applicable.
            notes: Optional notes about the mapping.

        Returns:
            The updated record.
        """
        if quality not in VALID_QUALITY:
            raise ValueError(f"Invalid quality: {quality}. Must be one of {VALID_QUALITY}")

        if match_level not in VALID_MATCH_LEVEL:
            raise ValueError(f"Invalid match_level: {match_level}. Must be one of {VALID_MATCH_LEVEL}")

        previous_status = record.get("mapping_status", "UNMAPPED")

        # Set ontology mapping
        record["ontology_mapping"] = {
            "ontology_id": candidate.ontology_id,
            "ontology_label": candidate.label,
            "ontology_source": candidate.source,
            "mapping_quality": quality,
            "match_level": match_level,
            "evidence": [
                {
                    "evidence_type": "LLM_SUGGESTION" if llm_assisted else "CURATOR_JUDGMENT",
                    "source": self.curator_name,
                    "confidence_score": candidate.score,
                    "notes": notes,
                }
            ],
        }

        # Update identifier to ontology ID
        record["identifier"] = candidate.ontology_id
        record["mapping_status"] = "MAPPED"

        # Record curation event
        self._add_event(
            record,
            action="MAPPED",
            changes=f"Mapped to {candidate.ontology_id} ({candidate.label})",
            previous_status=previous_status,
            new_status="MAPPED",
            llm_assisted=llm_assisted,
            llm_model=llm_model,
            notes=notes,
        )

        self._dirty = True
        return record

    def change_status(
        self,
        record: dict[str, Any],
        new_status: str,
        notes: Optional[str] = None,
        llm_assisted: bool = False,
    ) -> dict[str, Any]:
        """Change the mapping status of a record.

        Args:
            record: The ingredient record to update.
            new_status: New MappingStatusEnum value.
            notes: Optional notes about the change.

        Returns:
            The updated record.
        """
        if new_status not in VALID_STATUSES:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {VALID_STATUSES}")

        previous_status = record.get("mapping_status", "UNMAPPED")
        record["mapping_status"] = new_status

        self._add_event(
            record,
            action="STATUS_CHANGED",
            changes=f"Status changed from {previous_status} to {new_status}",
            previous_status=previous_status,
            new_status=new_status,
            llm_assisted=llm_assisted,
            notes=notes,
        )

        self._dirty = True
        return record

    def add_note(self, record: dict[str, Any], note_text: str) -> dict[str, Any]:
        """Add a note/annotation to a record."""
        existing = record.get("notes", "") or ""
        if existing:
            record["notes"] = f"{existing}\n{note_text}"
        else:
            record["notes"] = note_text

        self._add_event(
            record,
            action="ANNOTATED",
            changes=f"Note added: {note_text[:100]}",
        )

        self._dirty = True
        return record

    def _add_event(
        self,
        record: dict[str, Any],
        action: str,
        changes: Optional[str] = None,
        previous_status: Optional[str] = None,
        new_status: Optional[str] = None,
        llm_assisted: bool = False,
        llm_model: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> dict[str, Any]:
        """Append a curation event to a record's history."""
        event: dict[str, Any] = {
            "timestamp": _now_iso(),
            "curator": self.curator_name,
            "action": action,
        }
        if changes:
            event["changes"] = changes
        if previous_status:
            event["previous_status"] = previous_status
        if new_status:
            event["new_status"] = new_status
        if llm_assisted:
            event["llm_assisted"] = True
            if llm_model:
                event["llm_model"] = llm_model
        if notes:
            event["notes"] = notes

        if "curation_history" not in record or record["curation_history"] is None:
            record["curation_history"] = []
        record["curation_history"].append(event)

        return event

    def get_progress_report(self) -> dict[str, Any]:
        """Generate a summary of curation progress."""
        status_counts: dict[str, int] = {}
        for r in self._records:
            status = r.get("mapping_status", "UNKNOWN")
            status_counts[status] = status_counts.get(status, 0) + 1

        total = len(self._records)
        mapped = status_counts.get("MAPPED", 0)

        return {
            "total_records": total,
            "status_breakdown": status_counts,
            "mapped_percentage": (mapped / total * 100) if total > 0 else 0.0,
            "remaining_unmapped": status_counts.get("UNMAPPED", 0),
            "needs_expert": status_counts.get("NEEDS_EXPERT", 0),
            "ambiguous": status_counts.get("AMBIGUOUS", 0),
            "pending_review": status_counts.get("PENDING_REVIEW", 0),
        }
