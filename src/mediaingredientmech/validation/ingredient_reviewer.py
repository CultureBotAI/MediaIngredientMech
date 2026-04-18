"""
Ingredient reviewer for quality assurance and validation.

This module provides comprehensive validation of ontology-mapped ingredients,
checking for critical errors, warnings, and enrichment opportunities using:
- OAK (Ontology Access Kit) for term verification
- EBI OLS v4 API for chemical properties enrichment
- LinkML schema validation
- Domain-specific rules (purity, dual identifiers)
"""

import re
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import requests

from mediaingredientmech.utils.ontology_client import OntologyClient
from mediaingredientmech.validation.kg_microbe_dict import KgMicrobeDict


# Validation priority levels
PRIORITY_P1 = "P1"  # Critical errors
PRIORITY_P2 = "P2"  # High-priority warnings
PRIORITY_P3 = "P3"  # Medium-priority warnings
PRIORITY_P4 = "P4"  # Low-priority info

# Validation rules
RULE_P1_1 = "P1.1"  # Term does not exist
RULE_P1_2 = "P1.2"  # Invalid CURIE format
RULE_P1_3 = "P1.3"  # Dual identifier mismatch
RULE_P1_4 = "P1.4"  # Missing required fields

RULE_P2_1 = "P2.1"  # Label mismatch
RULE_P2_2 = "P2.2"  # Definition mismatch
RULE_P2_3 = "P2.3"  # Deprecated term
RULE_P2_4 = "P2.4"  # Purity merge violation
RULE_P2_5 = "P2.5"  # KG-Microbe dictionary disagreement

RULE_P3_1 = "P3.1"  # Missing chemical properties
RULE_P3_2 = "P3.2"  # Missing synonyms
RULE_P3_3 = "P3.3"  # Low confidence mapping
RULE_P3_4 = "P3.4"  # Ambiguous quality level

RULE_P4_1 = "P4.1"  # Additional synonyms available
RULE_P4_2 = "P4.2"  # Alternative ontology matches
RULE_P4_3 = "P4.3"  # Enrichment opportunities
RULE_P4_4 = "P4.4"  # KG-Microbe synonym enrichment candidates


@dataclass
class ValidationIssue:
    """Represents a validation issue found in an ingredient record."""

    priority: str  # P1, P2, P3, or P4
    rule_id: str  # e.g., "P1.1", "P2.3"
    category: str  # e.g., "label_mismatch", "missing_properties"
    message: str  # Human-readable description
    evidence: Dict  # Supporting data for the issue
    ingredient_id: str  # Which ingredient (preferred_term or id)


@dataclass
class CorrectionSuggestion:
    """Represents a suggested correction for a validation issue."""

    action: str  # "update_field", "enrich_properties", "add_synonym", etc.
    field_path: str  # e.g., "ontology_mapping.ontology_id"
    current_value: Any
    suggested_value: Any
    auto_correctable: bool  # Can be applied without human review
    confidence: float  # 0.0 to 1.0
    rationale: str  # Why this correction is suggested


@dataclass
class ReviewResult:
    """Result of reviewing a single ingredient."""

    status: str  # "PASS", "WARNING", or "ERROR"
    issues: List[ValidationIssue] = field(default_factory=list)
    suggestions: List[CorrectionSuggestion] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)  # timestamp, duration_ms, etc.


@dataclass
class BatchReviewResult:
    """Result of reviewing multiple ingredients."""

    summary: Dict[str, int] = field(default_factory=dict)  # P1: count, P2: count, etc.
    all_issues: List[ValidationIssue] = field(default_factory=list)
    all_suggestions: List[CorrectionSuggestion] = field(default_factory=list)
    failed: List[Dict] = field(default_factory=list)  # Ingredients that errored


class IngredientReviewer:
    """
    Core validation orchestrator for ingredient quality assurance.

    Integrates:
      - OAK for term existence/metadata
      - OLS for chemical properties enrichment
      - LinkML for schema validation
      - Custom rules for domain logic (purity, dual identifiers)
    """

    def __init__(
        self,
        use_local_owl: bool = False,
        owl_cache_dir: str = "ontology/cache",
        enable_llm: bool = False,
        kg_microbe_dict: Optional[KgMicrobeDict] = None,
        enable_kg_microbe_checks: bool = True,
    ):
        """
        Initialize the ingredient reviewer.

        Args:
            use_local_owl: Use cached OWL files instead of OAK remote
            owl_cache_dir: Directory containing chebi.owl, foodon.owl, etc.
            enable_llm: Enable LLM-assisted semantic comparison (P2.2)
            kg_microbe_dict: Pre-loaded kg-microbe dict for P2.5/P4.4. If None
                and enable_kg_microbe_checks is True, a KgMicrobeDict() is
                constructed lazily at first use.
            enable_kg_microbe_checks: Enable P2.5/P4.4 cross-reference against
                kg-microbe's unified chemical dictionary. Set False to skip
                (e.g., when the TSV isn't present on disk).
        """
        self.use_local_owl = use_local_owl
        self.owl_cache_dir = owl_cache_dir
        self.enable_llm = enable_llm
        self.enable_kg_microbe_checks = enable_kg_microbe_checks

        # Initialize OAK client
        self.oak_client = OntologyClient()

        # Cache for term lookups
        self._term_cache: Dict[str, Optional[Dict]] = {}

        # CURIE validation regex
        self._curie_pattern = re.compile(r"^[A-Z]+:\d+$")

        # kg-microbe dictionary (lazy-loaded on first use)
        self._kg_microbe_dict = kg_microbe_dict

    def _get_kg_microbe_dict(self) -> Optional[KgMicrobeDict]:
        """Return the kg-microbe dict, lazy-loading if needed. None if disabled."""
        if not self.enable_kg_microbe_checks:
            return None
        if self._kg_microbe_dict is None:
            self._kg_microbe_dict = KgMicrobeDict()
        self._kg_microbe_dict.load()
        if self._kg_microbe_dict.size == 0:
            # Dict file not present or empty; disable silently to avoid repeated attempts
            self.enable_kg_microbe_checks = False
            return None
        return self._kg_microbe_dict

    def review_ingredient(self, ingredient_record: Dict) -> ReviewResult:
        """
        Validate single ingredient against all rules (P1-P4).

        Args:
            ingredient_record: Dict from YAML (IngredientRecord)

        Returns:
            ReviewResult with status, issues, suggestions, and metadata

        Example:
            reviewer = IngredientReviewer()
            result = reviewer.review_ingredient(ingredient_dict)

            if result.status == "ERROR":
                print("P1 critical errors found:")
                for issue in result.issues:
                    if issue.priority == "P1":
                        print(f"  - {issue.message}")
        """
        start_time = time.time()
        issues = []
        suggestions = []

        ingredient_id = ingredient_record.get("preferred_term", "unknown")

        # Only validate mapped ingredients
        mapping_status = ingredient_record.get("mapping_status", "UNMAPPED")
        if mapping_status != "MAPPED":
            return ReviewResult(
                status="PASS",
                metadata={
                    "timestamp": datetime.now().isoformat(),
                    "duration_ms": int((time.time() - start_time) * 1000),
                    "skipped": "Not mapped",
                },
            )

        # Get ontology mapping
        ontology_mapping = ingredient_record.get("ontology_mapping", {})
        ontology_id = ontology_mapping.get("ontology_id")

        # P1 Validation - Critical Errors
        p1_issues = self._validate_p1(ingredient_record, ontology_id, ingredient_id)
        issues.extend(p1_issues)

        # If P1 errors, return early (no point checking further)
        if p1_issues:
            return ReviewResult(
                status="ERROR",
                issues=issues,
                suggestions=suggestions,
                metadata={
                    "timestamp": datetime.now().isoformat(),
                    "duration_ms": int((time.time() - start_time) * 1000),
                    "rules_checked": ["P1"],
                },
            )

        # P2 Validation - High-Priority Warnings
        p2_issues, p2_suggestions = self._validate_p2(
            ingredient_record, ontology_id, ingredient_id
        )
        issues.extend(p2_issues)
        suggestions.extend(p2_suggestions)

        # P3 Validation - Medium-Priority Warnings
        p3_issues, p3_suggestions = self._validate_p3(
            ingredient_record, ontology_id, ingredient_id
        )
        issues.extend(p3_issues)
        suggestions.extend(p3_suggestions)

        # P4 Validation - Low-Priority Info
        p4_issues, p4_suggestions = self._validate_p4(
            ingredient_record, ontology_id, ingredient_id
        )
        issues.extend(p4_issues)
        suggestions.extend(p4_suggestions)

        # Determine overall status
        if any(issue.priority == PRIORITY_P1 for issue in issues):
            status = "ERROR"
        elif any(issue.priority in [PRIORITY_P2, PRIORITY_P3] for issue in issues):
            status = "WARNING"
        else:
            status = "PASS"

        duration_ms = int((time.time() - start_time) * 1000)

        return ReviewResult(
            status=status,
            issues=issues,
            suggestions=suggestions,
            metadata={
                "timestamp": datetime.now().isoformat(),
                "duration_ms": duration_ms,
                "rules_checked": ["P1", "P2", "P3", "P4"],
            },
        )

    def batch_review(
        self,
        ingredient_records: List[Dict],
        priority_filter: Optional[List[str]] = None,
        parallel: bool = True,
        max_workers: int = 4,
    ) -> BatchReviewResult:
        """
        Validate multiple ingredients in parallel.

        Args:
            ingredient_records: List of ingredient dicts
            priority_filter: Only report these priorities (e.g., ["P1", "P2"])
            parallel: Use ThreadPoolExecutor for concurrent validation
            max_workers: Number of parallel threads

        Returns:
            BatchReviewResult with aggregated issues and suggestions

        Example:
            results = reviewer.batch_review(
                mapped_ingredients,
                priority_filter=["P1", "P2"],
                max_workers=8
            )

            print(f"P1 errors: {results.summary['P1']}")
            print(f"P2 warnings: {results.summary['P2']}")
        """
        all_issues = []
        all_suggestions = []
        failed = []

        if parallel and max_workers > 1:
            # Parallel processing
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_ingredient = {
                    executor.submit(self.review_ingredient, ing): ing
                    for ing in ingredient_records
                }

                for future in as_completed(future_to_ingredient):
                    ingredient = future_to_ingredient[future]
                    try:
                        result = future.result()
                        all_issues.extend(result.issues)
                        all_suggestions.extend(result.suggestions)
                    except Exception as e:
                        failed.append(
                            {
                                "ingredient": ingredient.get("preferred_term", "unknown"),
                                "error": str(e),
                            }
                        )
        else:
            # Sequential processing
            for ingredient in ingredient_records:
                try:
                    result = self.review_ingredient(ingredient)
                    all_issues.extend(result.issues)
                    all_suggestions.extend(result.suggestions)
                except Exception as e:
                    failed.append(
                        {
                            "ingredient": ingredient.get("preferred_term", "unknown"),
                            "error": str(e),
                        }
                    )

        # Filter by priority if specified
        if priority_filter:
            all_issues = [i for i in all_issues if i.priority in priority_filter]

        # Calculate summary statistics
        summary = {
            PRIORITY_P1: sum(1 for i in all_issues if i.priority == PRIORITY_P1),
            PRIORITY_P2: sum(1 for i in all_issues if i.priority == PRIORITY_P2),
            PRIORITY_P3: sum(1 for i in all_issues if i.priority == PRIORITY_P3),
            PRIORITY_P4: sum(1 for i in all_issues if i.priority == PRIORITY_P4),
        }

        return BatchReviewResult(
            summary=summary,
            all_issues=all_issues,
            all_suggestions=all_suggestions,
            failed=failed,
        )

    def auto_correct(
        self, ingredient_record: Dict, correction_types: Optional[List[str]] = None
    ) -> Dict:
        """
        Auto-apply safe corrections (P3/P4 only).

        Args:
            ingredient_record: Ingredient to correct
            correction_types: Which corrections to apply
              - "chemical_properties": Enrich from OLS
              - "synonyms": Add missing ontology synonyms
              - "curie_format": Normalize CURIE format
              - None: Apply all safe corrections

        Returns:
            Updated ingredient_record dict (does not save to file)

        Example:
            corrected = reviewer.auto_correct(
                ingredient,
                correction_types=["chemical_properties", "synonyms"]
            )

            # Review changes
            print(corrected.get('chemical_properties'))

            # Apply if satisfied
            curator.update_ingredient(corrected)
        """
        corrected = ingredient_record.copy()

        # Get validation result
        result = self.review_ingredient(corrected)

        # Only apply P3/P4 auto-correctable suggestions
        safe_suggestions = [
            s
            for s in result.suggestions
            if s.auto_correctable
            and any(
                issue.priority in [PRIORITY_P3, PRIORITY_P4]
                for issue in result.issues
            )
        ]

        # Filter by correction types if specified
        if correction_types:
            safe_suggestions = [
                s for s in safe_suggestions if s.action in correction_types
            ]

        # Apply suggestions
        for suggestion in safe_suggestions:
            if suggestion.action == "enrich_properties":
                ontology_id = corrected.get("ontology_mapping", {}).get("ontology_id")
                if ontology_id and ontology_id.startswith("CHEBI:"):
                    props = self.enrich_from_ols(ontology_id)
                    if props:
                        corrected["chemical_properties"] = props

            elif suggestion.action == "add_synonym":
                if "synonyms" not in corrected:
                    corrected["synonyms"] = []
                if suggestion.suggested_value not in corrected["synonyms"]:
                    corrected["synonyms"].append(
                        {
                            "text": suggestion.suggested_value,
                            "type": "ontology_derived",
                            "source": "auto_enrichment",
                        }
                    )

            elif suggestion.action == "normalize_curie":
                corrected["ontology_mapping"]["ontology_id"] = suggestion.suggested_value

        return corrected

    def enrich_from_ols(self, ontology_id: str) -> Optional[Dict]:
        """
        Fetch chemical properties from EBI OLS v4 API.

        Args:
            ontology_id: CHEBI CURIE (e.g., "CHEBI:26710")

        Returns:
            Dict with chemical_properties section containing:
              - molecular_formula
              - smiles
              - inchi
              - inchikey
              - monoisotopic_mass
              - average_mass

        Returns None if:
          - Not a CHEBI term
          - OLS API error
          - No chemical properties available

        Example:
            props = reviewer.enrich_from_ols("CHEBI:26710")
            if props:
                ingredient['chemical_properties'] = props
        """
        if not ontology_id or not ontology_id.startswith("CHEBI:"):
            return None

        chebi_id = ontology_id.replace("CHEBI:", "")
        url = f"https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_{chebi_id}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Extract properties from annotation
            annotation = data.get("annotation", {})
            properties = {}

            # Molecular formula (check both formula and generalized_empirical_formula)
            if "formula" in annotation:
                properties["molecular_formula"] = annotation["formula"][0]
            elif "generalized_empirical_formula" in annotation:
                properties["molecular_formula"] = annotation["generalized_empirical_formula"][0]

            # SMILES
            if "smiles_string" in annotation:
                properties["smiles"] = annotation["smiles_string"][0]

            # InChI
            if "inchi_string" in annotation:
                properties["inchi"] = annotation["inchi_string"][0]

            # InChIKey
            if "inchi_key_string" in annotation:
                properties["inchikey"] = annotation["inchi_key_string"][0]

            # Masses
            if "monoisotopic_mass" in annotation:
                properties["monoisotopic_mass"] = float(annotation["monoisotopic_mass"][0])

            if "mass" in annotation:
                properties["average_mass"] = float(annotation["mass"][0])

            return properties if properties else None

        except Exception:
            return None

    # P1 Validation Methods

    def _validate_p1(
        self, ingredient_record: Dict, ontology_id: Optional[str], ingredient_id: str
    ) -> List[ValidationIssue]:
        """Validate P1 critical errors."""
        issues = []

        # P1.1: Term existence
        if ontology_id:
            if not self.check_term_exists(ontology_id):
                issues.append(
                    ValidationIssue(
                        priority=PRIORITY_P1,
                        rule_id=RULE_P1_1,
                        category="term_not_found",
                        message=f"Ontology term {ontology_id} does not exist",
                        evidence={"ontology_id": ontology_id},
                        ingredient_id=ingredient_id,
                    )
                )

        # P1.2: CURIE format
        if ontology_id and not self.validate_curie(ontology_id):
            issues.append(
                ValidationIssue(
                    priority=PRIORITY_P1,
                    rule_id=RULE_P1_2,
                    category="invalid_curie",
                    message=f"Invalid CURIE format: {ontology_id}",
                    evidence={"ontology_id": ontology_id},
                    ingredient_id=ingredient_id,
                )
            )

        # P1.3: Dual identifier mismatch
        record_identifier = ingredient_record.get("identifier")
        if record_identifier and record_identifier.startswith("UNMAPPED_"):
            issues.append(
                ValidationIssue(
                    priority=PRIORITY_P1,
                    rule_id=RULE_P1_3,
                    category="dual_identifier_mismatch",
                    message=f"Mapped ingredient has UNMAPPED identifier: {record_identifier}",
                    evidence={
                        "identifier": record_identifier,
                        "ontology_id": ontology_id,
                    },
                    ingredient_id=ingredient_id,
                )
            )

        # P1.4: Missing required fields
        if not ingredient_record.get("preferred_term"):
            issues.append(
                ValidationIssue(
                    priority=PRIORITY_P1,
                    rule_id=RULE_P1_4,
                    category="missing_required_field",
                    message="Missing required field: preferred_term",
                    evidence={},
                    ingredient_id=ingredient_id,
                )
            )

        if not ontology_id:
            issues.append(
                ValidationIssue(
                    priority=PRIORITY_P1,
                    rule_id=RULE_P1_4,
                    category="missing_required_field",
                    message="Missing required field: ontology_id",
                    evidence={},
                    ingredient_id=ingredient_id,
                )
            )

        return issues

    # P2 Validation Methods

    def _validate_p2(
        self, ingredient_record: Dict, ontology_id: Optional[str], ingredient_id: str
    ) -> Tuple[List[ValidationIssue], List[CorrectionSuggestion]]:
        """Validate P2 high-priority warnings."""
        issues = []
        suggestions = []

        if not ontology_id:
            return issues, suggestions

        # Get term info from ontology
        term_info = self.get_term_info(ontology_id)
        if not term_info:
            return issues, suggestions

        # P2.1: Label mismatch
        preferred_term = ingredient_record.get("preferred_term", "")
        ontology_label = term_info.get("label", "")

        if ontology_label:
            similarity = self.compare_labels(preferred_term, ontology_label)
            if similarity < 0.8:  # Significant mismatch
                issues.append(
                    ValidationIssue(
                        priority=PRIORITY_P2,
                        rule_id=RULE_P2_1,
                        category="label_mismatch",
                        message=f"Ontology label '{ontology_label}' differs from preferred term '{preferred_term}'",
                        evidence={
                            "preferred_term": preferred_term,
                            "ontology_label": ontology_label,
                            "similarity": similarity,
                        },
                        ingredient_id=ingredient_id,
                    )
                )
                suggestions.append(
                    CorrectionSuggestion(
                        action="update_preferred_term",
                        field_path="preferred_term",
                        current_value=preferred_term,
                        suggested_value=ontology_label,
                        auto_correctable=False,  # Requires human review
                        confidence=0.9,
                        rationale="Ontology label is canonical",
                    )
                )

        # P2.3: Deprecated term
        if term_info.get("deprecated", False):
            replacement = term_info.get("replaced_by")
            issues.append(
                ValidationIssue(
                    priority=PRIORITY_P2,
                    rule_id=RULE_P2_3,
                    category="deprecated_term",
                    message=f"Term {ontology_id} is deprecated",
                    evidence={"replacement": replacement},
                    ingredient_id=ingredient_id,
                )
            )
            if replacement:
                suggestions.append(
                    CorrectionSuggestion(
                        action="remap_to_replacement",
                        field_path="ontology_mapping.ontology_id",
                        current_value=ontology_id,
                        suggested_value=replacement,
                        auto_correctable=False,
                        confidence=1.0,
                        rationale=f"Term deprecated, use {replacement}",
                    )
                )

        # P2.5: kg-microbe dictionary disagreement
        p25_issues, p25_suggestions = self._check_kg_microbe_disagreement(
            ingredient_record, ontology_id, ingredient_id
        )
        issues.extend(p25_issues)
        suggestions.extend(p25_suggestions)

        return issues, suggestions

    def _check_kg_microbe_disagreement(
        self,
        ingredient_record: Dict,
        ontology_id: str,
        ingredient_id: str,
    ) -> Tuple[List[ValidationIssue], List[CorrectionSuggestion]]:
        """P2.5: flag when kg-microbe's dict maps the same surface form elsewhere."""
        issues: List[ValidationIssue] = []
        suggestions: List[CorrectionSuggestion] = []

        if not ontology_id or not ontology_id.startswith("CHEBI:"):
            return issues, suggestions

        kg_dict = self._get_kg_microbe_dict()
        if kg_dict is None:
            return issues, suggestions

        # Collect surface forms to probe: preferred_term + explicit synonyms
        surface_forms: List[str] = []
        pt = ingredient_record.get("preferred_term", "")
        if pt:
            surface_forms.append(pt)
        for syn in ingredient_record.get("synonyms", []):
            text = syn.get("synonym_text") or syn.get("text") if isinstance(syn, dict) else syn
            if text and isinstance(text, str):
                surface_forms.append(text)

        seen_disagreements: Dict[str, str] = {}  # other_chebi -> surface_form that found it

        for form in surface_forms:
            if kg_dict.is_ambiguous(form):
                continue  # too polluted to trust (e.g., "Na+", short cations)
            kg_candidates = kg_dict.lookup_synonym(form)
            if not kg_candidates:
                continue
            for other_chebi in kg_candidates - {ontology_id}:
                if other_chebi in seen_disagreements:
                    continue
                seen_disagreements[other_chebi] = form

        if not seen_disagreements:
            return issues, suggestions

        mim_term_info = self.get_term_info(ontology_id) or {}
        mim_label = mim_term_info.get("label", "")

        for other_chebi, triggering_form in seen_disagreements.items():
            other_info = self.get_term_info(other_chebi)
            if other_info is None:
                continue  # phantom CHEBI in kg-microbe dict, skip
            other_label = other_info.get("label", "")
            issues.append(
                ValidationIssue(
                    priority=PRIORITY_P2,
                    rule_id=RULE_P2_5,
                    category="kg_microbe_disagreement",
                    message=(
                        f"kg-microbe maps '{triggering_form}' to {other_chebi} "
                        f"({other_label}), but MIM uses {ontology_id} ({mim_label})"
                    ),
                    evidence={
                        "surface_form": triggering_form,
                        "mim_chebi": ontology_id,
                        "mim_label": mim_label,
                        "kg_microbe_chebi": other_chebi,
                        "kg_microbe_label": other_label,
                    },
                    ingredient_id=ingredient_id,
                )
            )
            suggestions.append(
                CorrectionSuggestion(
                    action="investigate_kg_microbe_disagreement",
                    field_path="ontology_mapping.ontology_id",
                    current_value=ontology_id,
                    suggested_value=other_chebi,
                    auto_correctable=False,
                    confidence=0.5,
                    rationale=(
                        "kg-microbe's dict has known TSV-parse bugs; both sides "
                        "must be OAK/OLS-verified before re-mapping."
                    ),
                )
            )

        return issues, suggestions

    # P3 Validation Methods

    def _validate_p3(
        self, ingredient_record: Dict, ontology_id: Optional[str], ingredient_id: str
    ) -> Tuple[List[ValidationIssue], List[CorrectionSuggestion]]:
        """Validate P3 medium-priority warnings."""
        issues = []
        suggestions = []

        # P3.1: Missing chemical properties
        if ontology_id and ontology_id.startswith("CHEBI:"):
            chem_props = ingredient_record.get("chemical_properties", {})
            missing_props = []

            if not chem_props.get("smiles"):
                missing_props.append("smiles")
            if not chem_props.get("inchi"):
                missing_props.append("inchi")
            if not chem_props.get("molecular_formula"):
                missing_props.append("molecular_formula")

            if missing_props:
                issues.append(
                    ValidationIssue(
                        priority=PRIORITY_P3,
                        rule_id=RULE_P3_1,
                        category="missing_chemical_properties",
                        message=f"Missing chemical properties: {', '.join(missing_props)}",
                        evidence={"missing": missing_props},
                        ingredient_id=ingredient_id,
                    )
                )
                suggestions.append(
                    CorrectionSuggestion(
                        action="enrich_properties",
                        field_path="chemical_properties",
                        current_value=chem_props,
                        suggested_value="<fetch from OLS>",
                        auto_correctable=True,
                        confidence=1.0,
                        rationale="Enrich from EBI OLS API",
                    )
                )

        # P3.2: Missing synonyms
        term_info = self.get_term_info(ontology_id) if ontology_id else None
        if term_info:
            ontology_syns = set(term_info.get("synonyms", []))
            record_syns = set()
            for syn in ingredient_record.get("synonyms", []):
                if isinstance(syn, dict):
                    record_syns.add(syn.get("text", ""))
                else:
                    record_syns.add(syn)

            missing_syns = ontology_syns - record_syns
            if len(missing_syns) > 2:  # Only report if significant number missing
                issues.append(
                    ValidationIssue(
                        priority=PRIORITY_P3,
                        rule_id=RULE_P3_2,
                        category="missing_synonyms",
                        message=f"{len(missing_syns)} synonyms available in ontology",
                        evidence={"missing_count": len(missing_syns)},
                        ingredient_id=ingredient_id,
                    )
                )

        # P3.3: Low confidence mapping
        confidence = ingredient_record.get("ontology_mapping", {}).get("confidence", 1.0)
        if confidence < 0.7:
            issues.append(
                ValidationIssue(
                    priority=PRIORITY_P3,
                    rule_id=RULE_P3_3,
                    category="low_confidence",
                    message=f"Low mapping confidence: {confidence:.2f}",
                    evidence={"confidence": confidence},
                    ingredient_id=ingredient_id,
                )
            )

        return issues, suggestions

    # P4 Validation Methods

    def _validate_p4(
        self, ingredient_record: Dict, ontology_id: Optional[str], ingredient_id: str
    ) -> Tuple[List[ValidationIssue], List[CorrectionSuggestion]]:
        """Validate P4 low-priority info."""
        issues = []
        suggestions = []

        # P4.1: Additional synonyms available (informational only)
        term_info = self.get_term_info(ontology_id) if ontology_id else None
        if term_info:
            ontology_syn_count = len(term_info.get("synonyms", []))
            record_syn_count = len(ingredient_record.get("synonyms", []))

            if ontology_syn_count > record_syn_count + 5:
                issues.append(
                    ValidationIssue(
                        priority=PRIORITY_P4,
                        rule_id=RULE_P4_1,
                        category="additional_synonyms",
                        message=f"Ontology has {ontology_syn_count - record_syn_count} more synonyms",
                        evidence={
                            "ontology_count": ontology_syn_count,
                            "record_count": record_syn_count,
                        },
                        ingredient_id=ingredient_id,
                    )
                )

        # P4.4: kg-microbe synonym enrichment candidates
        p44_issues, p44_suggestions = self._check_kg_microbe_synonym_enrichment(
            ingredient_record, ontology_id, ingredient_id
        )
        issues.extend(p44_issues)
        suggestions.extend(p44_suggestions)

        return issues, suggestions

    def _check_kg_microbe_synonym_enrichment(
        self,
        ingredient_record: Dict,
        ontology_id: Optional[str],
        ingredient_id: str,
    ) -> Tuple[List[ValidationIssue], List[CorrectionSuggestion]]:
        """P4.4: propose new synonyms from kg-microbe, with per-candidate ambiguity filter."""
        issues: List[ValidationIssue] = []
        suggestions: List[CorrectionSuggestion] = []

        if not ontology_id or not ontology_id.startswith("CHEBI:"):
            return issues, suggestions

        kg_dict = self._get_kg_microbe_dict()
        if kg_dict is None:
            return issues, suggestions

        entry = kg_dict.get_entry(ontology_id)
        if entry is None or not entry.synonyms:
            return issues, suggestions

        existing = {ingredient_record.get("preferred_term", "").lower()}
        for syn in ingredient_record.get("synonyms", []):
            text = syn.get("synonym_text") or syn.get("text") if isinstance(syn, dict) else syn
            if text and isinstance(text, str):
                existing.add(text.lower())

        candidates: List[str] = []
        for syn in entry.synonyms:
            if syn.lower() in existing:
                continue
            # Ambiguity guard: skip if kg-microbe also maps this synonym elsewhere
            other_chebis = kg_dict.lookup_synonym(syn) - {ontology_id}
            if other_chebis:
                continue
            candidates.append(syn)

        if not candidates:
            return issues, suggestions

        issues.append(
            ValidationIssue(
                priority=PRIORITY_P4,
                rule_id=RULE_P4_4,
                category="kg_microbe_synonym_candidates",
                message=(
                    f"kg-microbe has {len(candidates)} synonym(s) for {ontology_id} "
                    f"not in this record"
                ),
                evidence={
                    "candidate_count": len(candidates),
                    "candidates": sorted(candidates)[:20],
                    "kg_microbe_canonical": entry.canonical_name,
                },
                ingredient_id=ingredient_id,
            )
        )
        for syn in candidates:
            suggestions.append(
                CorrectionSuggestion(
                    action="add_synonym_from_kg_microbe",
                    field_path="synonyms",
                    current_value=None,
                    suggested_value=syn,
                    auto_correctable=False,  # Human review required per P4.4 safety rule
                    confidence=0.6,
                    rationale=(
                        f"kg-microbe associates this synonym uniquely with {ontology_id}. "
                        "Human should still sanity-check before committing."
                    ),
                )
            )

        return issues, suggestions

    # Helper Methods

    def validate_curie(self, curie: str) -> bool:
        """Check if string is valid CURIE format (PREFIX:ID)."""
        return bool(self._curie_pattern.match(curie))

    def check_term_exists(self, ontology_id: str) -> bool:
        """Check if term exists in ontology via OAK."""
        term_info = self.get_term_info(ontology_id)
        return term_info is not None

    def get_term_info(self, ontology_id: str) -> Optional[Dict]:
        """
        Fetch term info from ontology via EBI OLS API.

        Returns dict with:
          - label: str
          - definition: str
          - synonyms: List[str]
          - deprecated: bool
          - replaced_by: Optional[str]

        Caches results to avoid repeated lookups.
        """
        if ontology_id in self._term_cache:
            return self._term_cache[ontology_id]

        try:
            # Extract source and ID
            if ":" not in ontology_id:
                self._term_cache[ontology_id] = None
                return None

            source, term_id = ontology_id.split(":", 1)
            source_lower = source.lower()

            # Only support CHEBI, FOODON, ENVO via OLS
            if source_lower not in ["chebi", "foodon", "envo"]:
                self._term_cache[ontology_id] = None
                return None

            # Build OLS URL
            ontology_id_encoded = ontology_id.replace(":", "_")
            url = f"https://www.ebi.ac.uk/ols4/api/ontologies/{source_lower}/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F{ontology_id_encoded}"

            response = requests.get(url, timeout=10)
            if response.status_code == 404:
                # Term doesn't exist
                self._term_cache[ontology_id] = None
                return None

            response.raise_for_status()
            data = response.json()

            # Extract term info
            term_info = {
                "label": data.get("label", ""),
                "definition": data.get("description", [""])[0] if data.get("description") else "",
                "synonyms": data.get("synonyms", []),
                "deprecated": data.get("is_obsolete", False),
                "replaced_by": None,  # Would need to parse annotation
            }

            self._term_cache[ontology_id] = term_info
            return term_info

        except requests.exceptions.RequestException:
            # Network error or term not found
            self._term_cache[ontology_id] = None
            return None
        except Exception:
            self._term_cache[ontology_id] = None
            return None

    def get_ontology_label(self, ontology_id: str) -> Optional[str]:
        """Fetch canonical label from ontology."""
        term_info = self.get_term_info(ontology_id)
        return term_info.get("label") if term_info else None

    def compare_labels(self, label1: str, label2: str) -> float:
        """
        Compare label similarity using token overlap.

        Returns: 0.0 (no match) to 1.0 (exact match)
        """
        if not label1 or not label2:
            return 0.0

        # Normalize
        l1 = label1.lower().strip()
        l2 = label2.lower().strip()

        # Exact match
        if l1 == l2:
            return 1.0

        # Token overlap
        tokens1 = set(l1.split())
        tokens2 = set(l2.split())

        if not tokens1 or not tokens2:
            return 0.0

        intersection = tokens1 & tokens2
        union = tokens1 | tokens2

        return len(intersection) / len(union)
