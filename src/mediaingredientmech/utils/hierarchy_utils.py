"""
Hierarchy query utilities for MediaIngredientMech.

Provides functions to navigate and query ingredient hierarchies:
- Get all variants (parent + children)
- Navigate up/down hierarchy
- Resolve role inheritance
"""

from typing import Optional


def get_parent(ingredient_id: str, all_records: list[dict]) -> Optional[dict]:
    """
    Get parent ingredient record.

    Args:
        ingredient_id: ID of ingredient to find parent for
        all_records: List of all ingredient records

    Returns:
        Parent record or None if no parent or not found

    Examples:
        >>> parent = get_parent('MediaIngredientMech:000114', all_records)
        >>> print(parent['preferred_term'])  # "Water (base)"
    """
    # Find the record
    record = None
    for r in all_records:
        if r.get('id') == ingredient_id:
            record = r
            break

    if not record:
        return None

    parent_id = record.get('parent_ingredient')
    if not parent_id:
        return None

    # Find parent record
    for r in all_records:
        if r.get('id') == parent_id:
            return r

    return None


def get_children(ingredient_id: str, all_records: list[dict]) -> list[dict]:
    """
    Get all child ingredient records.

    Args:
        ingredient_id: ID of parent ingredient
        all_records: List of all ingredient records

    Returns:
        List of child records (empty if none)

    Examples:
        >>> children = get_children('MediaIngredientMech:001108', all_records)
        >>> print([c['preferred_term'] for c in children])
        ['Tap water', 'Demineralized water', 'Distilled water', 'Double distilled water']
    """
    # Find the record
    record = None
    for r in all_records:
        if r.get('id') == ingredient_id:
            record = r
            break

    if not record:
        return []

    child_ids = record.get('child_ingredients', [])
    if not child_ids:
        return []

    # Find child records
    children = []
    for child_id in child_ids:
        for r in all_records:
            if r.get('id') == child_id:
                children.append(r)
                break

    return children


def get_all_variants(ingredient_id: str, all_records: list[dict]) -> list[dict]:
    """
    Get all variants in the family (parent + all siblings + self).

    If record is a child, returns parent + all siblings (including self).
    If record is a parent, returns self + all children.
    If record is standalone, returns just self.

    Args:
        ingredient_id: ID of any ingredient in hierarchy
        all_records: List of all ingredient records

    Returns:
        List of all variant records in family

    Examples:
        >>> # Query from child perspective
        >>> variants = get_all_variants('MediaIngredientMech:000114', all_records)
        >>> # Returns: [Water (base), Tap water, Demineralized, Distilled, Double distilled]

        >>> # Query from parent perspective
        >>> variants = get_all_variants('MediaIngredientMech:001108', all_records)
        >>> # Returns: [Water (base), Tap water, Demineralized, Distilled, Double distilled]
    """
    # Find the record
    record = None
    for r in all_records:
        if r.get('id') == ingredient_id:
            record = r
            break

    if not record:
        return []

    variants = []

    # If this is a child, navigate to parent first
    parent_id = record.get('parent_ingredient')
    if parent_id:
        parent = get_parent(ingredient_id, all_records)
        if parent:
            # Add parent
            variants.append(parent)
            # Add all children (siblings + self)
            children = get_children(parent_id, all_records)
            variants.extend(children)
        else:
            # Parent not found, just return self
            variants.append(record)
    else:
        # This is a parent or standalone
        variants.append(record)
        # Add children if any
        children = get_children(ingredient_id, all_records)
        variants.extend(children)

    return variants


def get_siblings(ingredient_id: str, all_records: list[dict]) -> list[dict]:
    """
    Get all sibling records (other children of same parent).

    Args:
        ingredient_id: ID of ingredient
        all_records: List of all ingredient records

    Returns:
        List of sibling records (excludes self)

    Examples:
        >>> siblings = get_siblings('MediaIngredientMech:000114', all_records)
        >>> print([s['preferred_term'] for s in siblings])
        ['Tap water', 'Demineralized water', 'Double distilled water']
    """
    # Find the record
    record = None
    for r in all_records:
        if r.get('id') == ingredient_id:
            record = r
            break

    if not record:
        return []

    parent_id = record.get('parent_ingredient')
    if not parent_id:
        return []  # No parent, no siblings

    # Get all children of parent
    children = get_children(parent_id, all_records)

    # Filter out self
    siblings = [c for c in children if c.get('id') != ingredient_id]

    return siblings


def get_inherited_roles(
    ingredient_id: str,
    all_records: list[dict],
    include_own_roles: bool = True
) -> list[dict]:
    """
    Resolve role inheritance from parent.

    If role_inheritance=true, includes parent's media_roles.
    Always includes record's own roles if include_own_roles=True.

    Args:
        ingredient_id: ID of ingredient
        all_records: List of all ingredient records
        include_own_roles: If True, include record's own roles (default: True)

    Returns:
        List of role assignment dicts (may contain duplicates if overridden)

    Examples:
        >>> roles = get_inherited_roles('MediaIngredientMech:000114', all_records)
        >>> print([r['role'] for r in roles])
        ['SOLVENT']  # Inherited from Water (base)
    """
    # Find the record
    record = None
    for r in all_records:
        if r.get('id') == ingredient_id:
            record = r
            break

    if not record:
        return []

    roles = []

    # Check if should inherit
    role_inheritance = record.get('role_inheritance', False)
    parent_id = record.get('parent_ingredient')

    if role_inheritance and parent_id:
        parent = get_parent(ingredient_id, all_records)
        if parent:
            parent_roles = parent.get('media_roles', [])
            roles.extend(parent_roles)

    # Add own roles
    if include_own_roles:
        own_roles = record.get('media_roles', [])
        roles.extend(own_roles)

    return roles


def get_hierarchy_path(ingredient_id: str, all_records: list[dict]) -> list[dict]:
    """
    Get path from root to this ingredient (all ancestors).

    Returns list from root → ... → parent → self.

    Args:
        ingredient_id: ID of ingredient
        all_records: List of all ingredient records

    Returns:
        List of records from root to self (includes self)

    Examples:
        >>> path = get_hierarchy_path('MediaIngredientMech:000114', all_records)
        >>> print([r['preferred_term'] for r in path])
        ['Water (base)', 'Distilled water']
    """
    # Find the record
    record = None
    for r in all_records:
        if r.get('id') == ingredient_id:
            record = r
            break

    if not record:
        return []

    path = [record]

    # Walk up the tree
    current = record
    while True:
        parent_id = current.get('parent_ingredient')
        if not parent_id:
            break

        parent = get_parent(current['id'], all_records)
        if not parent:
            break

        path.insert(0, parent)
        current = parent

    return path


def find_by_variant_type(
    variant_type: str,
    all_records: list[dict]
) -> list[dict]:
    """
    Find all ingredients with given variant_type.

    Args:
        variant_type: VariantTypeEnum value (e.g., 'PURIFIED', 'TAP')
        all_records: List of all ingredient records

    Returns:
        List of matching records

    Examples:
        >>> purified = find_by_variant_type('PURIFIED', all_records)
        >>> print([r['preferred_term'] for r in purified])
        ['Distilled water', ...]
    """
    matches = []

    for record in all_records:
        if record.get('variant_type') == variant_type:
            matches.append(record)

    return matches


def get_hierarchy_tree_string(
    ingredient_id: str,
    all_records: list[dict],
    indent: int = 0
) -> str:
    """
    Generate tree-like string representation of hierarchy.

    Args:
        ingredient_id: Root ID to start from
        all_records: List of all ingredient records
        indent: Current indentation level (for recursion)

    Returns:
        String with tree structure

    Examples:
        >>> tree = get_hierarchy_tree_string('MediaIngredientMech:001108', all_records)
        >>> print(tree)
        Water (base) [BASE_CHEMICAL]
          ├─ Tap water [TAP]
          ├─ Demineralized water [DEMINERALIZED]
          ├─ Distilled water [PURIFIED]
          └─ Double distilled water [ULTRA_PURIFIED]
    """
    # Find the record
    record = None
    for r in all_records:
        if r.get('id') == ingredient_id:
            record = r
            break

    if not record:
        return ""

    # Build current line
    prefix = "  " * indent
    variant_type = record.get('variant_type', '')
    type_str = f" [{variant_type}]" if variant_type else ""
    line = f"{prefix}{record['preferred_term']}{type_str}\n"

    # Get children
    children = get_children(ingredient_id, all_records)

    if not children:
        return line

    # Add children
    for i, child in enumerate(children):
        is_last = (i == len(children) - 1)
        child_prefix = "└─ " if is_last else "├─ "

        child_type = child.get('variant_type', '')
        child_type_str = f" [{child_type}]" if child_type else ""

        line += f"{prefix}{child_prefix}{child['preferred_term']}{child_type_str}\n"

    return line


def get_hierarchy_summary(ingredient_id: str, all_records: list[dict]) -> dict:
    """
    Get comprehensive summary of ingredient's hierarchy position.

    Args:
        ingredient_id: ID of ingredient
        all_records: List of all ingredient records

    Returns:
        Dictionary with hierarchy information

    Examples:
        >>> summary = get_hierarchy_summary('MediaIngredientMech:000114', all_records)
        >>> print(summary['role'])  # 'child'
        >>> print(summary['parent']['preferred_term'])  # 'Water (base)'
        >>> print(len(summary['siblings']))  # 3
    """
    # Find the record
    record = None
    for r in all_records:
        if r.get('id') == ingredient_id:
            record = r
            break

    if not record:
        return {}

    has_parent = bool(record.get('parent_ingredient'))
    has_children = bool(record.get('child_ingredients'))

    # Determine role in hierarchy
    if has_parent and not has_children:
        role = 'child'
    elif has_children and not has_parent:
        role = 'parent'
    elif has_children and has_parent:
        role = 'intermediate'  # Both parent and child
    else:
        role = 'standalone'

    summary = {
        'id': ingredient_id,
        'preferred_term': record.get('preferred_term'),
        'role': role,
        'variant_type': record.get('variant_type'),
        'has_parent': has_parent,
        'has_children': has_children,
        'role_inheritance': record.get('role_inheritance', False),
    }

    # Add parent info
    if has_parent:
        parent = get_parent(ingredient_id, all_records)
        if parent:
            summary['parent'] = {
                'id': parent.get('id'),
                'preferred_term': parent.get('preferred_term'),
                'variant_type': parent.get('variant_type'),
            }

    # Add children info
    if has_children:
        children = get_children(ingredient_id, all_records)
        summary['children'] = [
            {
                'id': c.get('id'),
                'preferred_term': c.get('preferred_term'),
                'variant_type': c.get('variant_type'),
            }
            for c in children
        ]
        summary['child_count'] = len(children)

    # Add siblings info
    if has_parent:
        siblings = get_siblings(ingredient_id, all_records)
        summary['siblings'] = [
            {
                'id': s.get('id'),
                'preferred_term': s.get('preferred_term'),
                'variant_type': s.get('variant_type'),
            }
            for s in siblings
        ]
        summary['sibling_count'] = len(siblings)

    # Add inherited roles
    if record.get('role_inheritance'):
        inherited_roles = get_inherited_roles(ingredient_id, all_records, include_own_roles=False)
        summary['inherited_roles'] = [r.get('role') for r in inherited_roles]

    return summary
