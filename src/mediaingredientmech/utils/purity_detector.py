"""
Purity detection utility for MediaIngredientMech.

Detects purity concerns from existing evidence notes and record metadata
to prevent inappropriate merges between pure chemicals and impure/natural variants.

Example:
    Natural sea-salt (97-99% NaCl + trace Mg, Ca, K) should NOT merge with
    pure NaCl (>99.5% reagent grade).
"""

import re
from typing import Optional


# Keywords indicating impurity/natural variants (priority order)
PURITY_KEYWORDS = {
    # Evidence note patterns (confidence: 0.9)
    'trace_components': [
        'trace minerals',
        'trace elements',
        'trace components',
        'trace amounts',
    ],
    'impurity_explicit': [
        'impure',
        'impurity',
        'not pure',
        'lower confidence due to impurity',
    ],
    'percentage_ranges': [
        r'~?\d{2,3}-\d{2,3}%',  # e.g., "97-99%", "~95-98%"
        r'approximately \d{2,3}%',
        r'about \d{2,3}%',
    ],
    'natural_variant': [
        'natural variant',
        'as found in nature',
        'evaporated seawater',
        'mined',
    ],

    # Preferred term patterns (confidence: 0.85)
    'purity_qualifiers': [
        'natural',
        'crude',
        'technical grade',
        'commercial grade',
        'industrial grade',
    ],
    'environmental_sources': [
        'tap water',
        'seawater',
        'sea water',
        'soil extract',
        'well water',
        'spring water',
    ],

    # Synonym property patterns (confidence: 0.7)
    'undefined_component': [
        'undefined component',
        'undefined composition',
        'variable composition',
    ],
}

# Patterns that indicate a pure chemical (negates purity concerns)
PURE_INDICATORS = [
    'reagent grade',
    'analytical grade',
    'ACS grade',
    'pure',
    '>99',
    '≥99',
    'anhydrous',  # May still be purity concern if comparing with hydrate
    'distilled water',
    'deionized water',
    'ultrapure',
]


def detect_purity_concerns(record: dict) -> tuple[bool, float, str]:
    """
    Detect if record represents impure/natural variant vs pure chemical.

    Uses a multi-layer detection strategy:
    1. Evidence note keywords (highest confidence)
    2. Preferred term patterns
    3. CLOSE_MATCH + low confidence combination
    4. Synonym property extraction

    Args:
        record: IngredientRecord dict with fields:
            - preferred_term: str
            - ontology_mapping: dict with mapping_quality, evidence, confidence
            - synonyms: list of dicts with source, text, metadata
            - notes: str (optional)

    Returns:
        tuple of (has_concern, confidence, reason):
            - has_concern: True if purity concerns detected
            - confidence: 0.0-1.0 detection confidence
            - reason: Human-readable explanation of detection

    Examples:
        >>> record = {
        ...     'preferred_term': 'Natural sea-salt',
        ...     'ontology_mapping': {
        ...         'mapping_quality': 'CLOSE_MATCH',
        ...         'evidence': [{
        ...             'confidence_score': 0.75,
        ...             'notes': '97-99% NaCl + trace minerals (Mg, Ca, K)'
        ...         }]
        ...     }
        ... }
        >>> has_concern, conf, reason = detect_purity_concerns(record)
        >>> has_concern
        True
        >>> conf >= 0.85
        True
        >>> 'trace minerals' in reason
        True
    """
    # Collect all text to analyze
    preferred_term = record.get('preferred_term', '').lower()
    notes = record.get('notes', '').lower()

    # Extract ontology mapping details
    ontology_mapping = record.get('ontology_mapping', {})
    mapping_quality = ontology_mapping.get('mapping_quality', '')
    evidence_list = ontology_mapping.get('evidence', [])

    # Combine all evidence notes
    evidence_text = ' '.join(
        ev.get('notes', '') for ev in evidence_list if isinstance(ev, dict)
    ).lower()

    # Extract synonyms text and metadata
    synonyms = record.get('synonyms', [])
    synonym_parts = []
    for syn in synonyms:
        if isinstance(syn, dict):
            # The schema key is `synonym_text`; fall back to `text` only for
            # backward compatibility with older fixture-style records.
            synonym_parts.append(syn.get('synonym_text') or syn.get('text', ''))
            # Add metadata.properties if present
            metadata = syn.get('metadata', {})
            if isinstance(metadata, dict) and 'properties' in metadata:
                synonym_parts.append(metadata['properties'])
        else:
            synonym_parts.append(str(syn))
    synonym_text = ' '.join(synonym_parts).lower()

    # Combine all text for analysis
    all_text = f"{preferred_term} {notes} {evidence_text} {synonym_text}"

    # Check for pure indicators first (negates concerns)
    for pure_indicator in PURE_INDICATORS:
        if pure_indicator.lower() in all_text:
            # Exception: if also has explicit impurity markers, those take precedence
            if any(kw in all_text for kw in PURITY_KEYWORDS['impurity_explicit']):
                break  # Continue with purity detection
            return False, 0.0, "Pure chemical indicator found"

    # Detection layers (in priority order)
    reasons = []
    max_confidence = 0.0

    # Layer 1: Evidence note keywords (confidence: 0.9)
    trace_found = any(kw in evidence_text for kw in PURITY_KEYWORDS['trace_components'])
    impurity_found = any(kw in evidence_text for kw in PURITY_KEYWORDS['impurity_explicit'])

    if trace_found:
        reasons.append("trace components in evidence")
        max_confidence = max(max_confidence, 0.9)

    if impurity_found:
        reasons.append("explicit impurity noted")
        max_confidence = max(max_confidence, 0.9)

    # Check for percentage ranges in evidence
    for pattern in PURITY_KEYWORDS['percentage_ranges']:
        if re.search(pattern, evidence_text):
            reasons.append("percentage range indicates impurity")
            max_confidence = max(max_confidence, 0.9)
            break

    # Check for natural variant mentions
    if any(kw in evidence_text for kw in PURITY_KEYWORDS['natural_variant']):
        reasons.append("natural variant mentioned")
        max_confidence = max(max_confidence, 0.9)

    # Layer 2: Preferred term patterns (confidence: 0.85)
    term_has_qualifier = any(
        preferred_term.startswith(qual) or f" {qual}" in preferred_term
        for qual in PURITY_KEYWORDS['purity_qualifiers']
    )

    if term_has_qualifier:
        reasons.append("purity qualifier in term")
        max_confidence = max(max_confidence, 0.85)

    # Check for environmental sources in term
    if any(src in preferred_term for src in PURITY_KEYWORDS['environmental_sources']):
        reasons.append("environmental source")
        max_confidence = max(max_confidence, 0.85)

    # Layer 3: CLOSE_MATCH + low confidence (confidence: 0.75)
    if mapping_quality == 'CLOSE_MATCH':
        # Extract confidence score
        confidence_score = None
        for ev in evidence_list:
            if isinstance(ev, dict) and 'confidence_score' in ev:
                confidence_score = ev['confidence_score']
                break

        if confidence_score is not None and confidence_score < 0.8:
            # Only flag if there are also composition concerns in notes
            composition_keywords = ['composition', 'contains', 'includes', '%']
            if any(kw in evidence_text for kw in composition_keywords):
                reasons.append(f"CLOSE_MATCH with low confidence ({confidence_score})")
                max_confidence = max(max_confidence, 0.75)

    # Layer 4: Synonym property extraction (confidence: 0.7)
    if any(kw in synonym_text for kw in PURITY_KEYWORDS['undefined_component']):
        reasons.append("undefined component property")
        max_confidence = max(max_confidence, 0.7)

    # Return result
    if max_confidence > 0.0:
        reason_str = " + ".join(reasons)
        return True, max_confidence, reason_str
    else:
        return False, 0.0, "No purity concerns detected"


def get_purity_details(record: dict) -> Optional[str]:
    """
    Extract detailed purity information from evidence notes.

    Useful for displaying WHY a purity concern was detected.

    Args:
        record: IngredientRecord dict

    Returns:
        Detailed purity description or None if not found

    Examples:
        >>> record = {
        ...     'ontology_mapping': {
        ...         'evidence': [{
        ...             'notes': 'Natural sea-salt = evaporated seawater, 97-99% NaCl. Contains trace minerals (Mg, Ca, K).'
        ...         }]
        ...     }
        ... }
        >>> get_purity_details(record)
        'evaporated seawater, 97-99% NaCl. Contains trace minerals (Mg, Ca, K)'
    """
    ontology_mapping = record.get('ontology_mapping', {})
    evidence_list = ontology_mapping.get('evidence', [])

    for ev in evidence_list:
        if not isinstance(ev, dict):
            continue

        notes = ev.get('notes', '')

        # Look for purity-related sentences
        purity_patterns = [
            r'(\d{2,3}[-~]?\d{0,3}%[^.]+)',  # Percentage descriptions
            r'([Cc]ontains [^.]+)',  # "Contains X, Y, Z"
            r'([Tt]race [^.]+)',  # "trace minerals..."
            r'([Nn]atural [^.]+)',  # "Natural variant..."
            r'([Uu]ndefined [^.]+)',  # "Undefined component"
        ]

        for pattern in purity_patterns:
            match = re.search(pattern, notes)
            if match:
                return match.group(1).strip()

    return None


def compare_purity_reasons(reason1: str, reason2: str) -> bool:
    """
    Check if two purity concern reasons are similar/compatible.

    Used to determine if two impure ingredients can be merged despite
    both having purity concerns.

    Args:
        reason1: Purity concern reason from first record
        reason2: Purity concern reason from second record

    Returns:
        True if reasons are similar (safe to merge), False if different

    Examples:
        >>> compare_purity_reasons(
        ...     "trace components + percentage range",
        ...     "trace components + natural variant"
        ... )
        True
        >>> compare_purity_reasons(
        ...     "trace components (Mg, Ca)",
        ...     "undefined component"
        ... )
        False
    """
    # Normalize reasons
    r1_lower = reason1.lower()
    r2_lower = reason2.lower()

    # Extract key concern types
    concern_types = {
        'trace': 'trace',
        'percentage': 'percentage',
        'natural': 'natural',
        'undefined': 'undefined',
        'environmental': 'environmental',
        'qualifier': 'purity qualifier',
    }

    r1_types = set()
    r2_types = set()

    for key, label in concern_types.items():
        if key in r1_lower or label in r1_lower:
            r1_types.add(key)
        if key in r2_lower or label in r2_lower:
            r2_types.add(key)

    # If both have overlapping concern types, they're similar
    if r1_types & r2_types:  # Set intersection
        return True

    # If one is "undefined" and other is specific, they're different
    if ('undefined' in r1_types) != ('undefined' in r2_types):
        return False

    # Otherwise, consider them different
    return False
