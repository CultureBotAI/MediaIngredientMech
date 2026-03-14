"""Core curation logic: mapping workflow, validation, and history tracking."""

from __future__ import annotations

import logging
import re
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

VALID_MEDIA_ROLES = {
    "CARBON_SOURCE",
    "NITROGEN_SOURCE",
    "MINERAL",
    "TRACE_ELEMENT",
    "BUFFER",
    "VITAMIN_SOURCE",
    "SALT",
    "PROTEIN_SOURCE",
    "AMINO_ACID_SOURCE",
    "SOLIDIFYING_AGENT",
    "ENERGY_SOURCE",
    "ELECTRON_ACCEPTOR",
    "ELECTRON_DONOR",
    "COFACTOR_PROVIDER",
}

VALID_CELLULAR_ROLES = {
    "PRIMARY_DEGRADER",
    "REDUCTIVE_DEGRADER",
    "OXIDATIVE_DEGRADER",
    "BIOTRANSFORMER",
    "SYNERGIST",
    "BRIDGE_ORGANISM",
    "ELECTRON_SHUTTLE",
    "DETOXIFIER",
    "COMMENSAL",
    "COMPETITOR",
}

VALID_SOLUTION_TYPES = {
    "VITAMIN_MIX",
    "TRACE_METAL_MIX",
    "AMINO_ACID_MIX",
    "BUFFER_SOLUTION",
    "CARBON_SOURCE_MIX",
    "MINERAL_STOCK",
    "COFACTOR_MIX",
    "COMPLEX_UNDEFINED",
    "OTHER",
}

VALID_CITATION_TYPES = {
    "PEER_REVIEWED_PUBLICATION",
    "PREPRINT",
    "DATABASE_ENTRY",
    "TECHNICAL_REPORT",
    "MANUAL_CURATION",
    "COMPUTATIONAL_PREDICTION",
}

DOI_PATTERN = re.compile(r"^10\.\d{4,}/[-._;()/:A-Za-z0-9]+$")


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
        auto_enrich: bool = True,
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
            auto_enrich: Whether to automatically enrich CHEBI mappings with chemical properties.

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

        # Update ontology_id field
        record["ontology_id"] = candidate.ontology_id
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

        # Auto-enrich with chemical properties if enabled and CHEBI
        if auto_enrich and candidate.source == "CHEBI":
            self.enrich_chemical_properties(record)

        self._dirty = True
        return record

    def enrich_chemical_properties(
        self,
        record: dict[str, Any],
        client: Optional[Any] = None,
    ) -> dict[str, Any]:
        """Enrich a record with chemical properties from ChEBI/PubChem.

        Args:
            record: The ingredient record to enrich.
            client: Optional ChemicalPropertiesClient instance (created if None).

        Returns:
            The updated record (modified in place).
        """
        # Check if already enriched
        if record.get("chemical_properties"):
            logger.debug("Record already has chemical_properties, skipping enrichment")
            return record

        # Check if mapped to CHEBI
        ontology_mapping = record.get("ontology_mapping")
        if not ontology_mapping:
            logger.debug("Record has no ontology_mapping, skipping enrichment")
            return record

        ontology_source = ontology_mapping.get("ontology_source")
        if ontology_source != "CHEBI":
            logger.debug("Record is not mapped to CHEBI (%s), skipping enrichment", ontology_source)
            return record

        # Import here to avoid circular dependency
        from mediaingredientmech.utils.chemical_properties_client import (
            ChemicalPropertiesClient,
        )

        # Create client if not provided
        if client is None:
            client = ChemicalPropertiesClient(cache_enabled=True)

        # Get properties
        ontology_id = ontology_mapping.get("ontology_id")
        label = ontology_mapping.get("ontology_label", "")
        props = client.get_properties(ontology_id, label, ontology_source)

        if props:
            # Add to record
            record["chemical_properties"] = props.to_dict()

            # Log curation event
            self._add_event(
                record,
                action="ANNOTATED",
                changes=f"Added chemical properties from {props.data_source}",
                notes=f"Formula: {props.molecular_formula or 'N/A'}, SMILES: {props.smiles or 'N/A'}",
            )

            self._dirty = True
            logger.info("Enriched %s with chemical properties", ontology_id)
        else:
            logger.debug("No chemical properties found for %s", ontology_id)

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

    def add_media_role(
        self,
        record: dict[str, Any],
        role: str,
        confidence: float = 0.9,
        doi: Optional[str] = None,
        pmid: Optional[str] = None,
        reference_text: Optional[str] = None,
        reference_type: str = "MANUAL_CURATION",
        url: Optional[str] = None,
        excerpt: Optional[str] = None,
        curator_note: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> dict[str, Any]:
        """Add a media role to an ingredient with optional DOI citation.

        Args:
            record: The ingredient record dict to update.
            role: IngredientRoleEnum value (e.g., "NITROGEN_SOURCE", "BUFFER").
            confidence: Confidence score (0.0-1.0). Defaults to 0.9.
            doi: Digital Object Identifier (e.g., "10.1128/jb.00123-15").
            pmid: PubMed ID for MEDLINE citations.
            reference_text: Human-readable citation text.
            reference_type: CitationTypeEnum value. Defaults to "MANUAL_CURATION".
            url: Web URL for the reference.
            excerpt: Relevant excerpt from the source.
            curator_note: Explanation of why this supports the role.
            notes: Additional context about the role assignment.

        Returns:
            The updated record.

        Raises:
            ValueError: If role, confidence, DOI format, or reference_type is invalid.
        """
        # Validation
        if role not in VALID_MEDIA_ROLES:
            raise ValueError(f"Invalid media role: {role}. Must be one of {VALID_MEDIA_ROLES}")
        if not (0.0 <= confidence <= 1.0):
            raise ValueError(f"Confidence out of range: {confidence}. Must be between 0.0 and 1.0")
        if doi and not DOI_PATTERN.match(doi):
            raise ValueError(f"Invalid DOI format: {doi}. Must match pattern: 10.XXXX/...")
        if reference_type not in VALID_CITATION_TYPES:
            raise ValueError(
                f"Invalid reference_type: {reference_type}. Must be one of {VALID_CITATION_TYPES}"
            )

        # Create role assignment
        role_assignment: dict[str, Any] = {
            "role": role,
            "confidence": confidence,
            "evidence": [],
        }
        if notes:
            role_assignment["notes"] = notes

        # Add citation if any citation info provided
        if doi or pmid or reference_text or url:
            citation: dict[str, Any] = {"reference_type": reference_type}
            if doi:
                citation["doi"] = doi
            if pmid:
                citation["pmid"] = pmid
            if reference_text:
                citation["reference_text"] = reference_text
            elif doi:
                citation["reference_text"] = f"DOI: {doi}"
            if url:
                citation["url"] = url
            if excerpt:
                citation["excerpt"] = excerpt
            if curator_note:
                citation["curator_note"] = curator_note

            role_assignment["evidence"].append(citation)

        # Add to record
        if "media_roles" not in record or record["media_roles"] is None:
            record["media_roles"] = []
        record["media_roles"].append(role_assignment)

        # Log curation event
        changes_msg = f"Added media role: {role} (confidence: {confidence:.2f})"
        if doi:
            changes_msg += f" with DOI: {doi}"
        self._add_event(record, action="ANNOTATED", changes=changes_msg)

        self._dirty = True
        return record

    def add_cellular_role(
        self,
        record: dict[str, Any],
        role: str,
        metabolic_context: Optional[str] = None,
        confidence: float = 0.9,
        doi: Optional[str] = None,
        pmid: Optional[str] = None,
        reference_text: Optional[str] = None,
        reference_type: str = "MANUAL_CURATION",
        url: Optional[str] = None,
        excerpt: Optional[str] = None,
        curator_note: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> dict[str, Any]:
        """Add a cellular/metabolic role to an ingredient.

        Args:
            record: The ingredient record dict to update.
            role: CellularRoleEnum value (e.g., "PRIMARY_DEGRADER", "ELECTRON_DONOR").
            metabolic_context: Pathway or metabolic context (e.g., "denitrification").
            confidence: Confidence score (0.0-1.0). Defaults to 0.9.
            doi: Digital Object Identifier.
            pmid: PubMed ID.
            reference_text: Human-readable citation text.
            reference_type: CitationTypeEnum value. Defaults to "MANUAL_CURATION".
            url: Web URL for the reference.
            excerpt: Relevant excerpt from the source.
            curator_note: Explanation of why this supports the role.
            notes: Additional context about the role assignment.

        Returns:
            The updated record.

        Raises:
            ValueError: If role, confidence, DOI format, or reference_type is invalid.
        """
        # Validation
        if role not in VALID_CELLULAR_ROLES:
            raise ValueError(
                f"Invalid cellular role: {role}. Must be one of {VALID_CELLULAR_ROLES}"
            )
        if not (0.0 <= confidence <= 1.0):
            raise ValueError(f"Confidence out of range: {confidence}. Must be between 0.0 and 1.0")
        if doi and not DOI_PATTERN.match(doi):
            raise ValueError(f"Invalid DOI format: {doi}. Must match pattern: 10.XXXX/...")
        if reference_type not in VALID_CITATION_TYPES:
            raise ValueError(
                f"Invalid reference_type: {reference_type}. Must be one of {VALID_CITATION_TYPES}"
            )

        # Create role assignment
        role_assignment: dict[str, Any] = {
            "role": role,
            "confidence": confidence,
            "evidence": [],
        }
        if metabolic_context:
            role_assignment["metabolic_context"] = metabolic_context
        if notes:
            role_assignment["notes"] = notes

        # Add citation if any citation info provided
        if doi or pmid or reference_text or url:
            citation: dict[str, Any] = {"reference_type": reference_type}
            if doi:
                citation["doi"] = doi
            if pmid:
                citation["pmid"] = pmid
            if reference_text:
                citation["reference_text"] = reference_text
            elif doi:
                citation["reference_text"] = f"DOI: {doi}"
            if url:
                citation["url"] = url
            if excerpt:
                citation["excerpt"] = excerpt
            if curator_note:
                citation["curator_note"] = curator_note

            role_assignment["evidence"].append(citation)

        # Add to record
        if "cellular_roles" not in record or record["cellular_roles"] is None:
            record["cellular_roles"] = []
        record["cellular_roles"].append(role_assignment)

        # Log curation event
        changes_msg = f"Added cellular role: {role} (confidence: {confidence:.2f})"
        if metabolic_context:
            changes_msg += f" in context: {metabolic_context}"
        if doi:
            changes_msg += f" with DOI: {doi}"
        self._add_event(record, action="ANNOTATED", changes=changes_msg)

        self._dirty = True
        return record

    def set_solution_type(self, record: dict[str, Any], solution_type: str) -> dict[str, Any]:
        """Set the solution type for mixture ingredients.

        Args:
            record: The ingredient record to update.
            solution_type: SolutionTypeEnum value (e.g., "VITAMIN_MIX", "TRACE_METAL_MIX").

        Returns:
            The updated record.

        Raises:
            ValueError: If solution_type is invalid.
        """
        if solution_type not in VALID_SOLUTION_TYPES:
            raise ValueError(
                f"Invalid solution type: {solution_type}. Must be one of {VALID_SOLUTION_TYPES}"
            )

        record["solution_type"] = solution_type
        self._add_event(
            record, action="ANNOTATED", changes=f"Set solution type: {solution_type}"
        )
        self._dirty = True
        return record

    def validate_role_assignments(self, record: dict[str, Any]) -> list[str]:
        """Validate all role assignments in a record.

        Args:
            record: The ingredient record to validate.

        Returns:
            List of validation error messages (empty if valid).
        """
        errors = []

        # Validate media roles
        for i, role_assignment in enumerate(record.get("media_roles", [])):
            role = role_assignment.get("role")
            if role and role not in VALID_MEDIA_ROLES:
                errors.append(f"Invalid media role at index {i}: {role}")

            confidence = role_assignment.get("confidence")
            if confidence is not None and not (0.0 <= confidence <= 1.0):
                errors.append(f"Confidence out of range at media role {i}: {confidence}")

            # Validate DOIs in evidence
            for j, evidence in enumerate(role_assignment.get("evidence", [])):
                doi = evidence.get("doi")
                if doi and not DOI_PATTERN.match(doi):
                    errors.append(f"Invalid DOI format at media role {i}, evidence {j}: {doi}")

                ref_type = evidence.get("reference_type")
                if ref_type and ref_type not in VALID_CITATION_TYPES:
                    errors.append(
                        f"Invalid reference_type at media role {i}, evidence {j}: {ref_type}"
                    )

        # Validate cellular roles
        for i, role_assignment in enumerate(record.get("cellular_roles", [])):
            role = role_assignment.get("role")
            if role and role not in VALID_CELLULAR_ROLES:
                errors.append(f"Invalid cellular role at index {i}: {role}")

            confidence = role_assignment.get("confidence")
            if confidence is not None and not (0.0 <= confidence <= 1.0):
                errors.append(f"Confidence out of range at cellular role {i}: {confidence}")

            # Validate DOIs in evidence
            for j, evidence in enumerate(role_assignment.get("evidence", [])):
                doi = evidence.get("doi")
                if doi and not DOI_PATTERN.match(doi):
                    errors.append(f"Invalid DOI format at cellular role {i}, evidence {j}: {doi}")

                ref_type = evidence.get("reference_type")
                if ref_type and ref_type not in VALID_CITATION_TYPES:
                    errors.append(
                        f"Invalid reference_type at cellular role {i}, evidence {j}: {ref_type}"
                    )

        # Validate solution_type
        solution_type = record.get("solution_type")
        if solution_type and solution_type not in VALID_SOLUTION_TYPES:
            errors.append(f"Invalid solution type: {solution_type}")

        return errors
