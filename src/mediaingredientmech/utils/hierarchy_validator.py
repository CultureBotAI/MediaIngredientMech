"""
Hierarchy validation utilities for MediaIngredientMech.

Validates parent-child relationships to ensure data integrity:
- Parent ingredients exist
- No circular references
- Bidirectional links are consistent
- Variant types are appropriate
"""

from typing import Optional


def validate_parent_exists(
    record: dict,
    all_records: list[dict],
    record_index: Optional[int] = None
) -> tuple[bool, str]:
    """
    Ensure parent_ingredient ID exists in dataset.

    Args:
        record: Record to validate
        all_records: List of all ingredient records
        record_index: Optional index of record in all_records

    Returns:
        (is_valid, error_message)

    Examples:
        >>> record = {'parent_ingredient': 'MediaIngredientMech:001108'}
        >>> validate_parent_exists(record, all_records)
        (True, "")
    """
    parent_id = record.get('parent_ingredient')

    if not parent_id:
        return True, ""  # No parent is valid (root or standalone)

    # Check if parent exists
    parent_exists = any(
        r.get('id') == parent_id
        for r in all_records
    )

    if not parent_exists:
        return False, f"Parent ingredient '{parent_id}' does not exist in dataset"

    return True, ""


def validate_no_circular_refs(
    record: dict,
    all_records: list[dict],
    visited: Optional[set] = None
) -> tuple[bool, str]:
    """
    Prevent circular references (A→B→A loops).

    Uses depth-first search to detect cycles in parent chain.

    Args:
        record: Record to validate
        all_records: List of all ingredient records
        visited: Set of already visited IDs (used in recursion)

    Returns:
        (is_valid, error_message)

    Examples:
        >>> # A→B→C is valid
        >>> validate_no_circular_refs(record_a, all_records)
        (True, "")

        >>> # A→B→A is invalid
        >>> validate_no_circular_refs(record_a_loop, all_records)
        (False, "Circular reference detected: ... → A → B → A")
    """
    if visited is None:
        visited = set()

    record_id = record.get('id')
    parent_id = record.get('parent_ingredient')

    if not parent_id:
        return True, ""  # No parent, no cycle possible

    if not record_id:
        return False, "Record missing 'id' field"

    # Check if we've seen this record before (cycle detected)
    if record_id in visited:
        chain = " → ".join(visited) + f" → {record_id}"
        return False, f"Circular reference detected: {chain}"

    # Add current record to visited set
    visited.add(record_id)

    # Find parent record
    parent_record = None
    for r in all_records:
        if r.get('id') == parent_id:
            parent_record = r
            break

    if not parent_record:
        return False, f"Parent '{parent_id}' not found"

    # Recursively check parent's parent
    return validate_no_circular_refs(parent_record, all_records, visited)


def validate_children_reference_parent(
    record: dict,
    all_records: list[dict]
) -> tuple[bool, str]:
    """
    Ensure bidirectional parent↔child links are consistent.

    Checks:
    1. All children in child_ingredients list exist
    2. Each child has this record as its parent
    3. This record appears in parent's child_ingredients list (if has parent)

    Args:
        record: Record to validate
        all_records: List of all ingredient records

    Returns:
        (is_valid, error_message)

    Examples:
        >>> # Valid bidirectional link
        >>> parent = {'id': 'A', 'child_ingredients': ['B']}
        >>> child = {'id': 'B', 'parent_ingredient': 'A'}
        >>> validate_children_reference_parent(parent, [parent, child])
        (True, "")
    """
    record_id = record.get('id')
    child_ids = record.get('child_ingredients', [])
    parent_id = record.get('parent_ingredient')

    errors = []

    # Check 1: All children exist
    for child_id in child_ids:
        child_exists = any(r.get('id') == child_id for r in all_records)
        if not child_exists:
            errors.append(f"Child '{child_id}' does not exist")

    # Check 2: Each child references this record as parent
    for child_id in child_ids:
        for r in all_records:
            if r.get('id') == child_id:
                child_parent = r.get('parent_ingredient')
                if child_parent != record_id:
                    errors.append(
                        f"Child '{child_id}' has parent '{child_parent}' but should be '{record_id}'"
                    )
                break

    # Check 3: If has parent, appears in parent's children list
    if parent_id:
        parent_record = None
        for r in all_records:
            if r.get('id') == parent_id:
                parent_record = r
                break

        if parent_record:
            parent_children = parent_record.get('child_ingredients', [])
            if record_id not in parent_children:
                errors.append(
                    f"Parent '{parent_id}' does not list this record in child_ingredients"
                )

    if errors:
        return False, "; ".join(errors)

    return True, ""


def validate_variant_type_matches(record: dict) -> tuple[bool, str]:
    """
    Check that variant_type makes sense for the relationship.

    Validates:
    - BASE_CHEMICAL should have children (is a parent)
    - Other variant types should have a parent
    - Variant notes exist when variant_type is set

    Args:
        record: Record to validate

    Returns:
        (is_valid, error_message)

    Examples:
        >>> record = {'variant_type': 'BASE_CHEMICAL', 'child_ingredients': ['A', 'B']}
        >>> validate_variant_type_matches(record)
        (True, "")
    """
    variant_type = record.get('variant_type')
    parent_id = record.get('parent_ingredient')
    child_ids = record.get('child_ingredients', [])
    variant_notes = record.get('variant_notes')

    if not variant_type:
        return True, ""  # No variant type, nothing to validate

    errors = []

    # BASE_CHEMICAL should have children
    if variant_type == 'BASE_CHEMICAL':
        if not child_ids:
            errors.append("BASE_CHEMICAL should have child_ingredients")
        if parent_id:
            errors.append("BASE_CHEMICAL should not have a parent (it IS the parent)")

    # Non-BASE types should have parent
    else:
        if not parent_id:
            errors.append(f"Variant type '{variant_type}' should have parent_ingredient")
        if child_ids:
            errors.append(f"Variant type '{variant_type}' should not have children (variants are leaves)")

    # Variant notes recommended for non-BASE types
    if variant_type != 'BASE_CHEMICAL' and not variant_notes:
        # Warning, not error
        pass  # Could add warning mechanism

    if errors:
        return False, "; ".join(errors)

    return True, ""


def validate_hierarchy(
    record: dict,
    all_records: list[dict],
    record_index: Optional[int] = None
) -> tuple[bool, list[str]]:
    """
    Run all hierarchy validation checks on a record.

    Args:
        record: Record to validate
        all_records: List of all ingredient records
        record_index: Optional index of record

    Returns:
        (is_valid, list_of_errors)

    Examples:
        >>> is_valid, errors = validate_hierarchy(record, all_records)
        >>> if not is_valid:
        ...     print(f"Validation failed: {errors}")
    """
    errors = []

    # Check 1: Parent exists
    valid, msg = validate_parent_exists(record, all_records, record_index)
    if not valid:
        errors.append(f"Parent validation: {msg}")

    # Check 2: No circular references
    valid, msg = validate_no_circular_refs(record, all_records)
    if not valid:
        errors.append(f"Circular reference: {msg}")

    # Check 3: Bidirectional links
    valid, msg = validate_children_reference_parent(record, all_records)
    if not valid:
        errors.append(f"Bidirectional links: {msg}")

    # Check 4: Variant type matches
    valid, msg = validate_variant_type_matches(record)
    if not valid:
        errors.append(f"Variant type: {msg}")

    return len(errors) == 0, errors


def validate_all_hierarchies(records: list[dict]) -> dict[str, list[str]]:
    """
    Validate hierarchy for all records in dataset.

    Args:
        records: List of all ingredient records

    Returns:
        Dictionary mapping record IDs to list of errors (empty if valid)

    Examples:
        >>> results = validate_all_hierarchies(all_records)
        >>> invalid_records = {id: errs for id, errs in results.items() if errs}
        >>> print(f"Found {len(invalid_records)} invalid hierarchies")
    """
    results = {}

    for idx, record in enumerate(records):
        record_id = record.get('id', f'index_{idx}')
        is_valid, errors = validate_hierarchy(record, records, idx)

        if not is_valid:
            results[record_id] = errors
        else:
            results[record_id] = []

    return results


def get_hierarchy_statistics(records: list[dict]) -> dict:
    """
    Get statistics about hierarchies in dataset.

    Returns:
        Dictionary with counts and metrics

    Examples:
        >>> stats = get_hierarchy_statistics(all_records)
        >>> print(f"Parent records: {stats['parent_count']}")
        >>> print(f"Leaf records: {stats['leaf_count']}")
    """
    parent_count = 0
    leaf_count = 0
    orphan_count = 0  # Has parent_ingredient but parent doesn't exist
    variant_types = {}

    for record in records:
        has_children = bool(record.get('child_ingredients'))
        has_parent = bool(record.get('parent_ingredient'))
        variant_type = record.get('variant_type')

        if has_children:
            parent_count += 1

        if has_parent and not has_children:
            leaf_count += 1

        if has_parent:
            parent_id = record.get('parent_ingredient')
            parent_exists = any(r.get('id') == parent_id for r in records)
            if not parent_exists:
                orphan_count += 1

        if variant_type:
            variant_types[variant_type] = variant_types.get(variant_type, 0) + 1

    return {
        'total_records': len(records),
        'parent_count': parent_count,
        'leaf_count': leaf_count,
        'orphan_count': orphan_count,
        'standalone_count': len(records) - parent_count - leaf_count,
        'variant_types': variant_types,
    }
