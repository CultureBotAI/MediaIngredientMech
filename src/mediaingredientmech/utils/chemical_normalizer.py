"""Chemical name normalization utilities for ontology matching.

This module provides functions to normalize chemical names by:
- Stripping hydrate notation (e.g., •7H2O, .2H2O)
- Removing catalog numbers (Fisher, Sigma, etc.)
- Fixing incomplete chemical formulas
- Expanding common abbreviations
- Generating search variants for ontology matching
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional


# Hydrate notation patterns to strip
HYDRATE_PATTERNS = [
    r'[•·.]\s*\d+\s*H2O',  # •2H2O, .7H2O, ·nH2O
    r'\s*hydrate',
    r'\s*\(hydrated\)',
    r'\s*heptahydrate',
    r'\s*dihydrate',
    r'\s*monohydrate',
    r'\s*trihydrate',
]

# Catalog/CAS patterns to strip
CATALOG_PATTERNS = [
    r'\s*\(Fisher [^)]+\)',
    r'\s*\(Sigma [^)]+\)',
    r'\s*\(CAS:\s*[^)]+\)',
    r'\s*\(MCIB [^)]+\)',
    r'\s*\([A-Z]{2,5}[- ][\w-]+\)',  # Generic catalog (XX NNNN)
]

# Common chemical formula abbreviations → full names
FORMULA_TO_NAME = {
    'NaCl': 'sodium chloride',
    'KCl': 'potassium chloride',
    'MgSO4': 'magnesium sulfate',
    'MgCl2': 'magnesium chloride',
    'CaCl2': 'calcium chloride',
    'CaSO4': 'calcium sulfate',
    'K2HPO4': 'dipotassium phosphate',
    'KH2PO4': 'monopotassium phosphate',
    'NaHCO3': 'sodium bicarbonate',
    'Na2CO3': 'sodium carbonate',
    'FeSO4': 'ferrous sulfate',
    'FeCl3': 'ferric chloride',
    'MnCl2': 'manganese chloride',
    'ZnSO4': 'zinc sulfate',
    'CuSO4': 'copper sulfate',
    'NH4Cl': 'ammonium chloride',
    'NaNO3': 'sodium nitrate',
    'KNO3': 'potassium nitrate',
    'H3BO3': 'boric acid',
}

# Common abbreviations → full terms
ABBREVIATION_EXPANSIONS = {
    'dH2O': 'distilled water',
    'H2O': 'water',
    'EDTA': 'ethylenediaminetetraacetic acid',
    'Tris': 'tris(hydroxymethyl)aminomethane',
    'MES': '2-(N-morpholino)ethanesulfonic acid',
    'HEPES': '4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid',
}

# Common incomplete formulas → corrected versions
FORMULA_CORRECTIONS = {
    'K2HPO': 'K2HPO4',
    'KH2PO': 'KH2PO4',
    'NaNO': 'NaNO3',
    'MgCO': 'MgCO3',
    'CaCO': 'CaCO3',
    'Na2SiO': 'Na2SiO3',
}


@dataclass
class NormalizationResult:
    """Result of normalizing a chemical name."""

    original: str
    normalized: str
    variants: list[str]
    applied_rules: list[str]


def strip_hydrate_notation(name: str) -> tuple[str, bool]:
    """Remove hydrate notation from chemical name.

    Examples:
        MgSO4•7H2O → MgSO4
        CaCl2.2H2O → CaCl2
        sodium chloride hydrate → sodium chloride

    Returns:
        Tuple of (cleaned_name, was_modified)
    """
    original = name
    for pattern in HYDRATE_PATTERNS:
        name = re.sub(pattern, '', name, flags=re.IGNORECASE)
    return name.strip(), name != original


def strip_catalog_info(name: str) -> tuple[str, bool]:
    """Remove catalog numbers and supplier codes.

    Examples:
        NaCl (Fisher S271-500) → NaCl
        MgSO4 (Sigma 230391) → MgSO4
        KCl (CAS: 7447-40-7) → KCl

    Returns:
        Tuple of (cleaned_name, was_modified)
    """
    original = name
    for pattern in CATALOG_PATTERNS:
        name = re.sub(pattern, '', name)
    return name.strip(), name != original


def fix_incomplete_formula(name: str) -> tuple[str, bool]:
    """Correct common incomplete chemical formulas.

    Examples:
        K2HPO → K2HPO4
        NaNO → NaNO3

    Returns:
        Tuple of (corrected_name, was_modified)
    """
    stripped = name.strip()
    for incomplete, complete in FORMULA_CORRECTIONS.items():
        if stripped == incomplete or stripped.startswith(incomplete + ' '):
            corrected = name.replace(incomplete, complete, 1)
            return corrected, True
    return name, False


def expand_abbreviation(name: str) -> Optional[str]:
    """Expand common chemical abbreviations to full names.

    Examples:
        dH2O → distilled water
        EDTA → ethylenediaminetetraacetic acid

    Returns:
        Expanded name if abbreviation recognized, else None
    """
    stripped = name.strip()
    return ABBREVIATION_EXPANSIONS.get(stripped)


def formula_to_common_name(formula: str) -> Optional[str]:
    """Convert chemical formula to common name.

    Examples:
        NaCl → sodium chloride
        MgSO4 → magnesium sulfate

    Returns:
        Common name if formula recognized, else None
    """
    stripped = formula.strip()
    return FORMULA_TO_NAME.get(stripped)


def normalize_chemical_name(name: str) -> NormalizationResult:
    """Apply all normalization rules to a chemical name.

    This is the main entry point for normalization. It applies all
    applicable rules and tracks which ones were used.

    Args:
        name: Original chemical name to normalize

    Returns:
        NormalizationResult with normalized name, variants, and applied rules
    """
    applied_rules = []
    current = name

    # Step 1: Strip catalog info
    current, modified = strip_catalog_info(current)
    if modified:
        applied_rules.append('stripped_catalog')

    # Step 2: Strip hydrate notation
    current, modified = strip_hydrate_notation(current)
    if modified:
        applied_rules.append('stripped_hydrate')

    # Step 3: Fix incomplete formulas
    current, modified = fix_incomplete_formula(current)
    if modified:
        applied_rules.append('fixed_incomplete_formula')

    normalized = current.strip()

    # Generate search variants
    variants = generate_search_variants(normalized, name)

    return NormalizationResult(
        original=name,
        normalized=normalized,
        variants=variants,
        applied_rules=applied_rules,
    )


def generate_search_variants(normalized: str, original: str) -> list[str]:
    """Generate multiple search variants for ontology matching.

    Creates various forms of the chemical name to try when searching
    ontologies, ordered from most specific to most general.

    Args:
        normalized: The normalized chemical name
        original: The original (un-normalized) name

    Returns:
        List of search variant strings (duplicates removed)
    """
    variants = []

    # Original name (in case normalization was too aggressive)
    if original.strip():
        variants.append(original.strip())

    # Normalized name (catalog/hydrate stripped)
    if normalized and normalized != original.strip():
        variants.append(normalized)

    # Try without hydrate if not already done
    no_hydrate, _ = strip_hydrate_notation(original)
    if no_hydrate and no_hydrate not in variants:
        variants.append(no_hydrate)

    # Try formula → common name expansion
    common_name = formula_to_common_name(normalized)
    if common_name:
        variants.append(common_name)

    # Try abbreviation expansion
    expanded = expand_abbreviation(normalized)
    if expanded:
        variants.append(expanded)

    # Try with incomplete formula fixed
    fixed, _ = fix_incomplete_formula(normalized)
    if fixed and fixed not in variants:
        variants.append(fixed)
        # Also try common name of fixed formula
        fixed_common = formula_to_common_name(fixed)
        if fixed_common:
            variants.append(fixed_common)

    # Remove duplicates while preserving order
    seen = set()
    unique_variants = []
    for v in variants:
        v_lower = v.lower()
        if v_lower not in seen:
            seen.add(v_lower)
            unique_variants.append(v)

    return unique_variants


def categorize_unmapped_name(name: str) -> str:
    """Categorize an unmapped ingredient name.

    Returns one of:
    - SIMPLE_CHEMICAL: Likely a simple chemical with notation issues
    - COMPLEX_MIXTURE: Vitamin solution, metal solution, media mixture
    - ENVIRONMENTAL: Soil, seawater, etc.
    - INCOMPLETE: Generic or unclear term
    - PLACEHOLDER: Reference to external source
    - UNKNOWN: Cannot categorize
    """
    name_lower = name.lower()

    # Placeholders
    if any(phrase in name_lower for phrase in [
        'full composition',
        'see source',
        'available at',
        'composition available',
    ]):
        return 'PLACEHOLDER'

    # Complex mixtures (but exclude if just a chemical with "solution" descriptor)
    complex_keywords = [
        'vitamin',
        'trace metal',
        'supplement',
        'mixture',
        'medium',
        'media',
    ]
    if any(phrase in name_lower for phrase in complex_keywords):
        return 'COMPLEX_MIXTURE'

    # Single chemical in solution form (e.g., "Thiamine HCl solution")
    # Still treat as simple chemical if just one compound
    if 'solution' in name_lower:
        # Check if it's a simple chemical solution vs complex mixture
        words = name.split()
        if len(words) <= 3:  # e.g., "CaCl2 solution"
            return 'SIMPLE_CHEMICAL'
        return 'COMPLEX_MIXTURE'

    # Environmental samples
    if any(phrase in name_lower for phrase in [
        'soil',
        'seawater',
        'sea water',
        'creek',
        'sediment',
        'greenhouse',
    ]):
        return 'ENVIRONMENTAL'

    # Incomplete/generic terms
    generic_terms = [
        'vitamin b',
        'trace element',
        'mineral',
    ]
    if any(phrase in name_lower for phrase in generic_terms) and len(name.split()) <= 2:
        return 'INCOMPLETE'

    # Natural salt is incomplete
    if 'natural' in name_lower and 'salt' in name_lower:
        return 'INCOMPLETE'

    # Check if looks like chemical formula or name with catalog/hydrate
    has_formula_pattern = bool(re.search(r'[A-Z][a-z]?\d*[A-Z]', name))  # e.g., NaCl, MgSO4
    has_simple_formula = bool(re.search(r'^[A-Z][a-z]?[A-Z0-9]+', name))  # Starts with element
    has_catalog = bool(re.search(r'\([A-Z][a-z]+ [A-Z0-9-]+\)', name))
    has_hydrate = bool(re.search(r'[•·.]\s*\d+\s*H2O', name))

    if has_formula_pattern or has_simple_formula or has_catalog or has_hydrate:
        return 'SIMPLE_CHEMICAL'

    # Check if it's in our known formulas
    stripped = name.strip()
    if stripped in FORMULA_TO_NAME or stripped in FORMULA_CORRECTIONS:
        return 'SIMPLE_CHEMICAL'

    # Check if ends with common salt forms
    if re.search(r'(chloride|sulfate|nitrate|phosphate|carbonate)$', name_lower):
        return 'SIMPLE_CHEMICAL'

    # Default
    return 'UNKNOWN'
